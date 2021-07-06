
---
title: 'react项目改造为electron+react项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1210'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 22:33:53 GMT
thumbnail: 'https://picsum.photos/400/300?random=1210'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. 安装electron依赖</h1>
<p><code>npm install electron --save-dev</code></p>
<p><strong>electron</strong> 一定要安装在 <strong>devDependencies</strong> 开发环境依赖里面，不然之后打包会有报错。（见坑）</p>
<h1 data-id="heading-1">2. 根目录新建 main.js</h1>
<pre><code class="copyable">const &#123; app, BrowserWindow ,ipc&#125; = require("electron");
const path = require("path");
let mainWindow = null;
//判断命令行脚本的第二参数
const mode = process.argv[2];

// 限制只启动一个
function makeSingleInstance() &#123;
  if (process.mas) return;
  app.requestSingleInstanceLock();
  app.on("second-instance", () => &#123;
    if (mainWindow) &#123;
      if (mainWindow.isMinimized()) mainWindow.restore();
      mainWindow.focus();
    &#125;
  &#125;);
&#125;

// 用于添加Chromium插件
function createDevTools() &#123;
  const &#123;
    default: installExtension,
    REACT_DEVELOPER_TOOLS,
    REDUX_DEVTOOLS,
  &#125; = require('electron-devtools-installer');
  // 安装devtron
  const devtronExtension = require('devtron');
  devtronExtension.install();
  // 安装React开发者工具
  installExtension(REACT_DEVELOPER_TOOLS);
  installExtension(REDUX_DEVTOOLS);
&#125;

// createWindow()方法来将index.html加载进一个新的BrowserWindow实例。
function createWindow() &#123;
  const windowOptions = &#123;
    width: 1000,
    height: 700,
    webPreferences: &#123;
      preload: path.join(__dirname, "preload.js"),
    &#125;,
    // frame:false, // 有没有边框
  &#125;;
  mainWindow = new BrowserWindow(windowOptions);
  //判断是否是开发模式
  if (mode === "dev") &#123;
    mainWindow.loadURL("http://localhost:8002/"); // http://localhost:8002/ 前端开发环境地址
    mainWindow.webContents.openDevTools(); // 自动打开控制台
    createDevTools();
  &#125; else &#123; 
    mainWindow.loadURL(path.join("file://", __dirname, "/build/index.html"));
  &#125;
  //接收渲染进程的信息
  ipc.on("min", function () &#123;
    mainWindow.minimize();
  &#125;);
  ipc.on("max", function () &#123;
    mainWindow.maximize();
  &#125;);
  ipc.on("login", function () &#123;
    mainWindow.maximize();
  &#125;);

  mainWindow.on("closed", () => &#123;
    mainWindow = null;
  &#125;);
&#125;

// 限制器
makeSingleInstance();

// app主进程的事件和方法
// 只有在ready事件被激发后才能创建浏览器窗口
app.whenReady().then(() => &#123;
  createWindow();
  // 针对macos系统，在没有浏览器窗口打开的情况下调用你仅存的 createWindow() 方法
  app.on("activate", function () &#123;
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  &#125;);
&#125;);
// 关闭所有窗口通常会完全退出一个应用程序
app.on("window-all-closed", () => &#123;
  if (process.platform !== "darwin") &#123;
    app.quit();
  &#125;
&#125;);
app.on("activate", () => &#123;
  if (mainWindow === null) &#123;
    createWindow();
  &#125;
&#125;);
module.exports = mainWindow;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">3. 根目录新建 preload.js</h1>
<pre><code class="copyable">// 预加载脚本
// 预加载脚本在渲染器进程加载之前加载，并有权访问两个 渲染器全局 (例如 window 和 document) 和 Node.js 环境
window.addEventListener("DOMContentLoaded", () => &#123;
    const replaceText = (selector, text) => &#123;
      const element = document.getElementById(selector);
      if (element) element.innerText = text;
    &#125;;
    for (const dependency of ["chrome", "node", "electron"]) &#123;
      replaceText(`$&#123;dependency&#125;-version`, process.versions[dependency]);
    &#125;
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">4. 配置package.json</h1>
<h2 data-id="heading-4">(1)更改main属性</h2>
<pre><code class="copyable">&#123;
     "main": "main.js", // 有的改一下，没有的加一下
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">(2)配置electron启动命令</h2>
<pre><code class="copyable">&#123;
    "scripts": &#123;
        "dev": "cross-env NODE_ENV=development webpack-dev-server --config webpack.config.js --progress --hot",
        "webpack": "webpack --progress",
        "electron:dev": "electron . dev", // 开发环境下使用
        "electron": "electron ."
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">5. 启动electron</h1>
<p><code>npm run electron</code></p>
<p>如果成功了，恭喜你，可以继续下一步了。</p>
<h1 data-id="heading-7">6. 打包</h1>
<h2 data-id="heading-8">(1)引入electron-builder打包工具</h2>
<p><code> npm install electron-builder --save-dev</code></p>
<p><strong>electron-builder</strong> 跟 <strong>electron</strong> 一样，一定要安装在 <strong>devDependencies</strong> 开发环境依赖里面，不然之后打包会有报错。（见坑）</p>
<h2 data-id="heading-9">(2)package.json配置打包属性和命令</h2>
<pre><code class="copyable">&#123;
    "build": &#123;
        "productName":"zwtzzwwtt", //项目名 这也是生成的exe文件的前缀名
        "appId": "1997", // 包名 
        "directories": &#123;
          "output": "builder" // 输出文件夹
        &#125;,
        "win": &#123;
          "target": [
            "nsis", // 目标封装类型，默认使用niss，win平台一般也是用这个，可写可不写
            "zip"
          ]
        &#125;,
        // niss一般用来配置安装和卸载程序的
        "nsis": &#123;
          "shortcutName": "makalo-cnblog-tool",  // 用于所有快捷方式的名称。默认为应用程序名称
          "oneClick": false,  // 是创建一键安装程序还是辅助安装程序
          "perMachine": true,  // 是否开启安装时权限限制（此电脑或当前用户）true 表示此电脑，false代表当前用户
          "allowElevation": true,  // 仅辅助安装程序有效。允许请求提升。如果为false，则用户将不得不以提升的权限重新启动安装程序
          "allowToChangeInstallationDirectory": true,  // 仅辅助安装程序有效。是否允许用户更改安装目录
          "createDesktopShortcut": true, // 创建桌面图标
          "createStartMenuShortcut": true, // 创建开始菜单图标
        &#125;
        "files": [
          "build/**/*", // 需要打包的前端已打包好的文件
          "main.js" // 主文件main.js
        ]
    &#125;,
    "scripts": &#123;
        "dev": "cross-env NODE_ENV=development webpack-dev-server --config webpack.config.js --progress --hot",
        "webpack": "webpack --progress", // 打包前端页面
        "electron": "electron .",
        "dist": "electron-builder" // 打包electron
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">(3)打包前端代码</h2>
<p><code>npm run webpack</code></p>
<h2 data-id="heading-11">(4)打包electron</h2>
<p><code>npm run dist</code></p>
<h2 data-id="heading-12">(5)安装exe文件</h2>
<h1 data-id="heading-13">7. 坑</h1>
<h2 data-id="heading-14">(1)执行electron-builder命令时，会报错误导致打包中断</h2>
<p><code>Package "electron-builder" is only allowed in "devDependencies". Please remove it from the "dependencies" section in your package.json</code></p>
<p><code>Package "electron" is only allowed in "devDependencies". Please remove it from the "dependencies" section in your package.json.</code></p>
<p>提示 <strong>electron</strong> 和 <strong>electron-builder</strong> 应该放在 <strong>devDependencies</strong> 下面</p>
<p>这也是上面在安装 <strong>electron</strong> 和 <strong>electron-builder</strong> 依赖的时候，提醒的说一定要把这两个安装在开发环境下</p>
<p>解决办法：<code>npm install electron electron-builder --save-dev</code></p>
<h2 data-id="heading-15">(2)打包过程中会出现某些zip文件下载失败的报错</h2>
<p>例如：<code>https://github.com/electron/electron/releases/download/v13.1.6/electron-v13.1.6-win32-x64.zip （这些资源国外的，下载特别慢）</code></p>
<p>解决办法：可以通过更改 <strong>npm</strong> 的 <strong>config</strong> 来加快下载速度（最后的 / 别漏了）</p>
<p><code>npm config set ELECTRON_MIRROR " https://npm.taobao.org/mirrors/electron/ "</code></p></div>  
</div>
            