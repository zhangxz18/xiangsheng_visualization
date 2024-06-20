import express from 'express';
import cors from 'cors';
import bodyParser from 'body-parser';
import { spawn } from 'child_process';
import { promises as fs } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
const app = express();
const port = 3001;
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
app.use(cors());
app.use(bodyParser.json());


const directoryPath = path.join(__dirname, '../xiangsheng');
app.get('/api/files', async (req, res) => {
  //const directoryPath = 'D:/xiangsheng/'; // 修改为你的文件路径，
  try {
    console.log(`Reading directory: ${directoryPath}`);
    const files = await fs.readdir(directoryPath);
    
    const txtFiles = files.filter(file => path.extname(file).toLowerCase() === '.txt');
    
    res.json(txtFiles);
  } catch (err) {
    
    res.status(500).json({ error: 'Unable to scan directory' });
  }
});



app.post('/api/process-files', async (req, res) => {
  const { files } = req.body;
  //const directoryPath = 'D:/xiangsheng'; // 修改为你的文件路径
    
  const filepath = files.map(file => ({ path: path.join(directoryPath, file) }));

// 打印 fileContents 数组以便调试
  console.log("File contents:", filepath);

  const a=JSON.stringify(filepath);
  // 调用 Python 脚本并传递文件内容
  //const pythonProcess = spawn('python', ['src/python-scripts/yuntu.py']);
  const pythonScriptPath = path.join(__dirname,'python-scripts', 'yuntu.py');
  const pythonProcess = spawn('python', [pythonScriptPath]);

  pythonProcess.stdin.write(a);
  pythonProcess.stdin.end();

  let dataBuffer = '';
  let responseSent = false;

  pythonProcess.stdout.on('data', (data) => {
    dataBuffer += data.toString();
  });
  // function convertToPublicPath(filePath) {
  //   const fileName = filePath.split('\\').pop(); // 获取文件名部分
  //   return `public/${fileName}`;
  // }
  function convertToPublicPath(filePath) {
    const relativePath = path.relative(path.join(__dirname, '../public'), filePath);
    return `public/${relativePath.replace(/\\/g, '/')}`;
  }


  pythonProcess.stdout.on('end', () => {
    if (!responseSent) {
      try {
        const result = JSON.parse(dataBuffer);
        console.log(result);
        const wordcloudImage = convertToPublicPath(result.wordcloud_image);
        const wordbarPath = convertToPublicPath(result.wordbar_image_path);
        const wordFreqPath = convertToPublicPath(result.word_freq_path);
        res.json({
          uuid: result.uuid,
          wordcloud_image: wordcloudImage,
          wordbar_image_path:wordbarPath,
          word_freq_path: wordFreqPath
        });
        responseSent = true; // 已经发送响应
      } catch (error) {
        console.error('Error parsing JSON:', error);
        if (!responseSent) {
          res.status(500).json({ error: 'Error parsing JSON from Python script' });
          responseSent = true; // 已经发送响应
        }
      }
    }
  });
  pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    if (!responseSent) {
      if (code !== 0) {
        console.error(`Python process exited with code ${code}`);
        res.status(500).json({ error: 'Python script error' });
        responseSent = true; // 已经发送响应
      }
    }
  });
});
app.use('/public', express.static(path.join(__dirname, '../public')));


app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});