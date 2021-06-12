
---
title: 'Electron重学—基础知识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8148'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 00:18:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=8148'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第12天，活动详情查看: <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h4 data-id="heading-0">1, Electron是什么</h4>
<p>（1）Electron是有github开发的开源框架</p>
<p>（2）它允许开发者使用web技术构建跨平台桌面应用</p>
<p>Electron + Chromium + Node.js + Native API</p>
<pre><code class="hljs language-js copyable" lang="js">Electron谁在使用：
Atom, VSCode, Whatsapp, WordPress, slack, 大象
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(3) 原理</p>
<pre><code class="copyable">Electron是基于Chromium架构设计的，
Chrominum是Chrome的开源版本，有自己的窗口，Tab页面，标签等等，而处理这些事项的进程我们称为：主进程，
Browser,对应每个页面渲染的进程，我们称为：渲染进程，Render. 两个进程之间是需要通信的，也就是跨进程通
信，我们称为：IPC，

Node.js和Chromium的整合：
nodejs事件循环给予libuv, chromium基于message-pump
chromium集成到nodejs，用libuv实现message pump
<span class="copy-code-btn">复制代码</span></code></pre>






















































<table><thead><tr><th></th><th>Eelctron</th><th>Native</th><th>QT</th><th>NW</th></tr></thead><tbody><tr><td>性能</td><td>1</td><td>3</td><td>2</td><td>1</td></tr><tr><td>安装包大小</td><td>1</td><td>3</td><td>1</td><td>1</td></tr><tr><td>原生体验</td><td>1</td><td>3</td><td>2</td><td>1</td></tr><tr><td>跨平台</td><td>3</td><td>1</td><td>3</td><td>3</td></tr><tr><td>开发效率</td><td>3</td><td>2</td><td>2</td><td>2</td></tr><tr><td>社区，人才储备</td><td>3</td><td>2</td><td>1</td><td>2</td></tr></tbody></table>
<p>如果你想要做一个跨平台应用：如果想追求速度，提升开发效率，Electron是最好的选择，如果你想追求原生体验效果，Native是最好的选择</p>
<pre><code class="copyable">node -v
v14.16.1
npm -v
6.14.12
<span class="copy-code-btn">复制代码</span></code></pre>
<p>快速安装方法：</p>
<pre><code class="hljs language-js copyable" lang="js">ELECTRON_MIRROR=https:<span class="hljs-comment">//cdn.npm.taobao.org/dist/electron/  npm install electron --save-dev</span>

安装完之后验证：
npx electron -v
v13<span class="hljs-number">.1</span><span class="hljs-number">.2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2, Electron模块</h4>
<p>引入模块，各进程之间在Electron模块引入即可</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 引入主线程app, BrowserWindow模块</span>
<span class="hljs-keyword">const</span> &#123;app, BrowserWindow &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'electron'</span>) 
<span class="hljs-comment">// 引入渲染进程ipcRenderer模块</span>
<span class="hljs-keyword">const</span> &#123; ipcRenderer &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'electron'</span>)

<span class="hljs-comment">// 渲染进程跟主进程发送请求</span>
ipcRenderer.invoke().then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
    handleResult()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>App 模块用于控制应用生命周期，</p>
</li>
<li>
<p>BrowserWindow 用于创建和控制窗口</p>
<p>let win=new BrowserWindow(&#123;width, height&#125;). // 创建窗口，并设置宽高</p>
<p>​      win.loadURL(url) // 加载远程URL页面</p>
<p>​      win.loadFile(path)  // 加载本地页面</p>
</li>
<li>
<p>Notification</p>
<p>let notification = new Notification(&#123;title, body, actions:[&#123;text,type&#125;]&#125;)</p>
</li>
</ul>
<p>​              Notification.show()</p>
<ul>
<li>ipcMain.handle(channel, handler)  // 处理渲染进程的channer请求，在handler中返回结果</li>
</ul>
<h4 data-id="heading-2">3, Electron进程</h4>
<p>(1),  <strong>主进程</strong></p>
<ul>
<li>
<p>Electron 运行package.json的main脚本的进程被称为主进程</p>
</li>
<li>
<p>每一个应用只有一个主进程</p>
</li>
<li>
<p>管理原生GUI， 典型的窗口</p>
</li>
<li>
<p>创建渲染进程</p>
</li>
<li>
<p>控制应用生命周期</p>
<p>(1),  <strong>渲染进程</strong></p>
</li>
<li>
<p>展示web页面的进程称为渲染进程</p>
</li>
<li>
<p>通过node's，electron提供的API可以跟系统底层打交道</p>
</li>
<li>
<p>一个electron应用可以有多个渲染进程</p>
</li>
</ul>
<p>各个进程中有很多模块</p>
<p>主进程模块：</p>
<pre><code class="copyable">app  : 管理应用APP的生命周期，
BrowserWindow : 管理我们的窗口
ipcMain : 它是跟ipcRenderer进行IPC通信的
Menu:   原生的GUI
Tray： 原生的GUI
MenuItem：原生的GUI
dialog： 原生的GUI
Notification： 运行我们可以做一个可交互的通知
webContents： 用来加载我们具体的页面
autoUpdater:  用来更新模块
globalShortcut： 用来设置全局的一个快捷键
systemPreferences
TouchBar
netLog
powerMonitor
inAppPurchase
net
powerSaveBlocker
contentTracing
BrowserView
session
protocol
Screen
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染进程：</p>
<pre><code class="copyable">ipcRenderer
remote： 可以调用我们主进程的模块
desktopCapture： 捕获我们的桌面流，桌面截图
webFrame
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两个进程都有的模块：</p>
<pre><code class="copyable">clipboard： 用来访问和读写我们的剪切板
crashReporter： 用来监视我们的主进程和渲染进程是否崩溃
shell
nativeImage
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">3, 进程通信</h4>
<p>（1）<strong>进程间通信的目的</strong></p>
<ul>
<li>通知事件</li>
<li>数据传输</li>
<li>共享数据</li>
</ul>
<p>ipcMain, ipcRenderer都是EventEmitter对象，Electron提供了IPC通信模块，主进程的ipcMain和渲染进程的ipcRenderer</p>
<p>（2）<strong>从渲染进程到主进程</strong></p>
<pre><code class="copyable">ipcRenderer.invoke(channel, ...args)

ipcMain.handle(channel, handler)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（3）<strong>从主进程到渲染进程</strong></p>
<pre><code class="copyable">ipcRenderer.on(channel, handler)
webContents.send(channel)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（4）<strong>页面间（渲染进程与渲染进程间）通信</strong></p>
<p>通知事件：</p>
<pre><code class="copyable">ipcRenderer.sendTo()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数据共享：</p>
<pre><code class="copyable">web技术（localStorage, sessionStorage, indexedDB）
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">4, 踩坑</h4>
<ul>
<li>少用remote模块</li>
<li>不要呀sync模式</li>
<li>在请求+响应的通信模块下，需要自定义超时限制</li>
</ul>
<h4 data-id="heading-5">5, Electron原生能力</h4>
<p><strong>GUI</strong></p>
<ul>
<li>
<p>BrowserWindow 应用窗口</p>
</li>
<li>
<p>Tray 托盘</p>
</li>
<li>
<p>app 设置 dock.badge</p>
</li>
<li>
<p>Menu菜单</p>
</li>
<li>
<p>dialog原生弹框</p>
</li>
<li>
<p>TouchBar 苹果触控</p>
<p><strong>API</strong></p>
</li>
<li>
<p>clipboard 剪切板</p>
</li>
<li>
<p>globalShortcut 全局快捷键</p>
</li>
<li>
<p>desktopCapture 捕获桌面</p>
</li>
<li>
<p>Shell    打开文件，URL</p>
</li>
</ul>
<pre><code class="copyable">LazyLoad(https://mathiasbynens.be/demo/img-loading-lazy)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">6, 与web相比</h4>
<ul>
<li>无浏览器兼容问题</li>
<li>最新浏览器Feature</li>
<li>ES 高级语法</li>
<li>无跨域问题</li>
<li>Powered by Node.js</li>
</ul>
<h4 data-id="heading-7">7, 实战</h4>
<p>1, 安装</p>
<pre><code class="copyable">ELECTRON_MIRROR=https://cdn.npm.taobao.org/dist/electron/  npm install electron --save-dev

安装完之后验证：
npx electron -v
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Main.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 引入主线程app, BrowserWindow, ipcRenderer模块</span>
<span class="hljs-keyword">const</span> &#123;app, BrowserWindow, Notification, ipcMain &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'electron'</span>) 

<span class="hljs-keyword">let</span> mainWindow;
app.on(<span class="hljs-string">'ready'</span>, <span class="hljs-function">() =></span> &#123;
    mainWindow = <span class="hljs-keyword">new</span> BrowserWindow(&#123;
        <span class="hljs-attr">width</span>: <span class="hljs-number">300</span>,
        <span class="hljs-attr">height</span>: <span class="hljs-number">300</span>,
        <span class="hljs-attr">webPreferences</span>: &#123;
            <span class="hljs-attr">nodeIntegration</span>: <span class="hljs-literal">true</span>
        &#125;
    &#125;)
    mainWindow.loadFile(<span class="hljs-string">'./index.html'</span>)
    mainWindow.on(<span class="hljs-string">'closed'</span>, <span class="hljs-function">() =></span> &#123;
        mainWindow = <span class="hljs-literal">null</span>
    &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            