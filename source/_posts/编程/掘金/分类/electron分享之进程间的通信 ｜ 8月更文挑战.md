
---
title: 'electron分享之进程间的通信 ｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3619'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 07:42:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=3619'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>1、主进程与渲染进程间通过IPC进行通信，例如：<br></p>
</blockquote>
<p>①<code>主进程</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; ipcMain &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'electron'</span>) 
<span class="hljs-comment">// 监听渲染进程信息</span>
ipcMain.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">event, arg</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ping'</span>)
  event.sender.send(<span class="hljs-string">'message-reply'</span>, <span class="hljs-string">'pong'</span>) <span class="hljs-comment">// 回复子程序</span>
&#125;)
<span class="hljs-comment">// 主进程单独往渲染进程发信息</span>
win.webContents.send(<span class="hljs-string">'message-reply'</span>, <span class="hljs-string">'pong'</span>)

ipcMain.handle(<span class="hljs-string">'perform-action'</span>, <span class="hljs-function">(<span class="hljs-params">event, ...args</span>) =></span> &#123;
  <span class="hljs-comment">// ... 代表渲染器操作</span>
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>②<code>渲染进程</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; ipcRenderer &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'electron'</span>)
ipcRenderer.send(<span class="hljs-string">'message'</span>, <span class="hljs-string">'ping'</span>) <span class="hljs-comment">// 发送给主进程</span>
ipcRenderer.on(<span class="hljs-string">'message-reply'</span>, <span class="hljs-function">(<span class="hljs-params">event, arg</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(arg) <span class="hljs-comment">// pong</span>
&#125;

<span class="hljs-comment">//渲染进程中调用主进程方法</span>
ipcRenderer.invoke(<span class="hljs-string">'perform-action'</span>, ...args)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>2、使用remote模块 -->只能在渲染进程中去调用主进程的模块<br></p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimweb.io%2Ftopic%2F5b3b72ab4d378e703a4f4435" target="_blank" rel="nofollow noopener noreferrer" title="https://imweb.io/topic/5b3b72ab4d378e703a4f4435" ref="nofollow noopener noreferrer">实现原理</a>：类似于 Java 中的 RMI，底层基于IPC</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; BrowserWindow ...(主进程的API模块) &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'electron'</span>).remote
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注：因为electron基于node开发的，node的模块化是commonjs(require)规范,与esm（import - es6）有所不同 <br></p>
</blockquote>
<p>解决方法：使用webpack打包</p>
<blockquote>
<p>electron快捷键开发</p>
</blockquote>
<p>这里使用的是electron的原生方法。当然也可以使用第三方JS库，如mousetrap等。</p>
<ol>
<li>主进程中监听键盘事件</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-comment">//1、本地快捷键 -->利用menu模块的accelerator属性 必须当应用获取焦点时才能被触发</span>
  <span class="hljs-keyword">const</span> &#123; Menu, MenuItem &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'electron'</span>)  --commnJS规范

  <span class="hljs-keyword">const</span> menu = <span class="hljs-keyword">new</span> Menu()
  menu.append(<span class="hljs-keyword">new</span> MenuItem(&#123;
    <span class="hljs-attr">label</span>: <span class="hljs-string">'Electron'</span>,
    <span class="hljs-attr">submenu</span>: [&#123;
      <span class="hljs-attr">role</span>: <span class="hljs-string">'help'</span>,
      <span class="hljs-attr">accelerator</span>: process.platform === <span class="hljs-string">'darwin'</span> ? <span class="hljs-string">'Alt+Cmd+I'</span> : <span class="hljs-string">'Alt+Shift+I'</span>,
      <span class="hljs-attr">click</span>: <span class="hljs-function">() =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Electron rocks!'</span>) &#125;
    &#125;]
  &#125;))

  Menu.setApplicationMenu(menu)

  <span class="hljs-comment">//2、全局快捷键  监听键盘事件，无论应用是否获取焦点，都会被触发</span>
  app.on(<span class="hljs-string">'ready'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">//注册</span>
    globalShortcut.register(<span class="hljs-string">'CommandOrControl+Alt+K'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      dialog.showMessageBox(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'info'</span>,
        <span class="hljs-attr">message</span>: <span class="hljs-string">'成功!'</span>,
        <span class="hljs-attr">detail</span>: <span class="hljs-string">'你按下了一个全局注册的快捷键绑定.'</span>,
        <span class="hljs-attr">buttons</span>: [<span class="hljs-string">'好的'</span>]
      &#125;)
    &#125;)
  &#125;)
  
  app.on(<span class="hljs-string">'will-quit'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">//注销所有快捷键</span>
    globalShortcut.unregisterAll()
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>渲染进程中监听键盘事件</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//1、使用浏览窗口监听键盘事件 需要自行判断什么键按下</span>
e.g.
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'keyup'</span>, doSomething, <span class="hljs-literal">true</span>)
<span class="hljs-literal">true</span>，这意味着当前监听器总是在其他监听器之前接收按键，以避免其它监听器调用 stopPropagation()。

<span class="hljs-comment">//2、使用第三方库 mousetrap(推荐)</span>





<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            