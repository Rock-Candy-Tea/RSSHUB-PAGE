
---
title: 'Electron IPC 渲染线程和主线程通讯'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7d938d4a93340d5a305d927fec0111c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 01:10:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7d938d4a93340d5a305d927fec0111c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第2天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7d938d4a93340d5a305d927fec0111c~tplv-k3u1fbpfcp-zoom-1.image" alt="electron" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有了 Electron ，我们就可以轻松地写桌面应用了，然后可以运行在不同操作系统，这是因为其原理基于浏览器内核实现应用。今天就来看一看在 Electron 中主线程是如何和渲染线程进行通讯的。那么需要先了解一下什么是<strong>主线程</strong>，什么又是<strong>渲染线程</strong>。</p>
<p>Electron 中，从 package.json 的 main 载入的 js 就是<strong>主进程</strong>，由主进程加载出来的页面就是<strong>渲染进程</strong>。主进程负责管理 Web 页面以及页面相应的渲染进程，包括原生的组件操作。而在 Electron 里的每个页面都有自己的进程，叫作渲染进程，主要负责 Web 的渲染。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Demo "</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"main.js"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">" Electron "</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"start"</span>: <span class="hljs-string">"electron ."</span>
  &#125;,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"electron"</span>: <span class="hljs-string">"^5.0.3"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建项目时候，在 package.json 中 main 属性指定文件就是 Electron 的主线程文件。Electron 会先运行此文件来启动我们应用。</p>
<pre><code class="copyable">function createWindow() &#123;
    mainWindow = new BrowserWindow(&#123;
        width: 800,
        height: 600,
        webPreferences: &#123;
            devTools:true,
            nodeIntegration:true
        &#125;
    &#125;)
    mainWindow.loadFile('index.html')
    mainWindow.webContents.openDevTools()
    mainWindow.on('closed', function () &#123;
        mainWindow = null
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以创建一个浏览器窗口，浏览器会加载项目下<code>index.html</code>文件。</p>
<pre><code class="copyable">  <script src="./index.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 index.html 文件中引用的 index.js 是运行在渲染线程中。所以在 index.js 中 console 我们可以浏览器调试工具可以看到。而在 main.js 中的 console 是可以在后端看到输出。</p>
<h4 data-id="heading-0">index.js（渲染进程）</h4>
<pre><code class="copyable">const &#123;ipcRenderer&#125; = require('electron');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入 ipc 依赖，使用 ipcRender 的 send 方法消息给 main.js(主线程）这个是异步的，我么可以在<code>async-reply</code>通道监听到返回事件，从而获取到事件对象来获取返回值。</p>
<pre><code class="copyable">ipcRenderer.send('async-msg','ping');
ipcRenderer.on('async-reply',(event,arg) => &#123;
    console.log(arg);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">main.js (主线程）</h4>
<pre><code class="copyable">const &#123;
    app,
    BrowserWindow,
    ipcMain,
    shell
&#125; = require('electron');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入 ipcMain 线程，然后在 <code>async-msg</code>通道监听到从 index.js 发送过来请求，然后这里通过使用 nodejs 的 fs 模块提供方法来读取目录下文件，然后返回给渲染线程。这样就完成一来一回通讯</p>
<pre><code class="copyable">
ipcMain.on('async-msg',(event,arg)=>&#123;
    console.log(arg)

    fs.readdir('/Users/jangwoo/Desktop/Zi/sf-test',(err,filenames)=>&#123;
        if(err)&#123;
            event.reply('async-reply',err);
            return;
        &#125;
        filenames.forEach((filename)=>&#123;
            event.reply('async-reply',filename);
        &#125;)
    &#125;)
    
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            