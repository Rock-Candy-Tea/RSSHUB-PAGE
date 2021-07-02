
---
title: '为了提高开发效率，我实现了 uTools 的超级面板'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b3d6ea7a25b4b908acc471471628979~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 02:29:59 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b3d6ea7a25b4b908acc471471628979~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>为了进一步提高开发工作效率，最近我们基于 <code>electron</code> 开发了一款媲美 <code>uTools</code> 的开源工具箱 <a href="https://github.com/clouDr-f2e/rubick" target="_blank" rel="nofollow noopener noreferrer">rubick</a>。该工具箱不仅仅开源，最重要的是可以使用 <code>uTools</code> 生态内所有开源插件！这将是巨大的能力，意味着 <code>uTools</code> 生态内所有插件可以无差异化使用到  <a href="https://github.com/clouDr-f2e/rubick" target="_blank" rel="nofollow noopener noreferrer">rubick</a> 中。为了更满足 <code>uTools</code> 生态使用者的习惯，提高工作开发效率，我们又实现了 <code>uTools</code> 的超级面板能力：</p>
<h3 data-id="heading-1">代码仓库</h3>
<p><a href="https://github.com/clouDr-f2e/rubick" target="_blank" rel="nofollow noopener noreferrer">Rubick github</a></p>
<h3 data-id="heading-2">功能截图：</h3>
<h4 data-id="heading-3">文件夹下长按右建</h4>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b3d6ea7a25b4b908acc471471628979~tplv-k3u1fbpfcp-watermark.image" width="300" loading="lazy" referrerpolicy="no-referrer">
<h4 data-id="heading-4">选择文件后长按右键</h4>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e220166cb464328b432f42d14ba9ab2~tplv-k3u1fbpfcp-watermark.image" width="300" loading="lazy" referrerpolicy="no-referrer">
<h4 data-id="heading-5">选择文字后长按右键</h4>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9f909d08a8441e8a506831796908ef9~tplv-k3u1fbpfcp-watermark.image" width="300" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-6">实现原理</h2>
<h3 data-id="heading-7">获取选中文案</h3>
<p>要实现改功能核心是要读取当前用户选中的文案或者文件，根据当前选择内容进行不同功能展示。但是核心有一个问题是如何来实现获取当前选中的内容。这个问题思考了很久很久，要想获取选中的文案，感觉唯一的办法是使用 <code>ctrl + c</code> 或者 <code>command + c</code> 来先复制到剪切板，再通过 <code>electron clipboard</code> 来获取当前剪切板内容。但是 <code>utools</code> 可不是通过先复制再长按这样的操作来实现的，而是直接选中文本或者文件长按后呼起超级面板。<strong>所以一定要在右击长按前获取到当前选中的内容。</strong></p>
<p>如果要这么干，可能真的无解了，之前就因为这么想，才被无解了。正确的思路应该是先长按再获取选中的内容。别看只是掉了个个，但实现确实天壤之别：</p>
<ol>
<li>先获取选中内容：这就要求我们必须监听原生系统选中事件，但是 <code>electron</code> 并没有提供能力，我们也无法监听系统选择事件。</li>
<li>先右击，后获取内容，这样的好处在于先右击可以通过监听鼠标右击事件，相比选择事件更加容易。</li>
</ol>
<p>所以思路就有了，先监听长按右击事件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// macos</span>
<span class="hljs-keyword">const</span> mouseEvents = <span class="hljs-built_in">require</span>(<span class="hljs-string">"osx-mouse"</span>);

<span class="hljs-keyword">const</span> mouseTrack = mouseEvents();
<span class="hljs-comment">// 按下去的 time</span>
<span class="hljs-keyword">let</span> down_time = <span class="hljs-number">0</span>;

<span class="hljs-comment">// 是否弹起</span>
<span class="hljs-keyword">let</span> isPress = <span class="hljs-literal">false</span>;

<span class="hljs-comment">// 监听右击</span>
mouseTrack.on(<span class="hljs-string">'right-down'</span>, <span class="hljs-function">() =></span> &#123;
    isPress = <span class="hljs-literal">true</span>;
    down_time = <span class="hljs-built_in">Date</span>.now();
    <span class="hljs-comment">// 长按 500ms 后触发</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">if</span> (isPress) &#123;
        <span class="hljs-comment">// 获取选中内容</span>
        <span class="hljs-keyword">const</span> copyResult = <span class="hljs-keyword">await</span> getSelectedText();
    &#125;, <span class="hljs-number">500</span>);
&#125;)
mouseTrack.on(<span class="hljs-string">'right-up'</span>, <span class="hljs-function">() =></span> &#123;
    isPress = <span class="hljs-literal">false</span>;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来一步就是要去实现获取选中内容，要获取选中内容有个比较骚的操作，就是：</p>
<ol>
<li>通过 <code>clipboard</code> 先获取当前剪切板内容，并存下 A</li>
<li>通过 <code>robot.js</code> 来调用系统 <code>command + c</code> 或者 <code>ctrl + c</code></li>
<li>再通过 <code>clipboard</code> 先获取当前剪切板内容，并存下 B</li>
<li>再将 A 写到剪切板中，返回 B</li>
</ol>
<p>先存剪切板内容的目的在于我们是偷偷帮用户执行了复制动作，当读取完用户选择内容后，需要回复用户之前的剪切板内容。接下来看一下简单的实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> getSelected = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-comment">// 缓存之前的文案</span>
    <span class="hljs-keyword">const</span> lastText = clipboard.readText(<span class="hljs-string">'clipboard'</span>);

    <span class="hljs-keyword">const</span> platform = process.platform;
    
    <span class="hljs-comment">// 执行复制动作</span>
    <span class="hljs-keyword">if</span> (platform === <span class="hljs-string">'darwin'</span>) &#123;
      robot.keyTap(<span class="hljs-string">'c'</span>, <span class="hljs-string">'command'</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
      robot.keyTap(<span class="hljs-string">'c'</span>, <span class="hljs-string">'control'</span>);
    &#125;

    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 读取剪切板内容</span>
      <span class="hljs-keyword">const</span> text = clipboard.readText(<span class="hljs-string">'clipboard'</span>) || <span class="hljs-string">''</span>
      <span class="hljs-keyword">const</span> fileUrl = clipboard.read(<span class="hljs-string">'public.file-url'</span>);
      
      <span class="hljs-comment">// 恢复剪切板内容</span>
      clipboard.writeText(lastText);

      resolve(&#123;
        text,
        fileUrl
      &#125;)
    &#125;, <span class="hljs-number">300</span>);
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">通知超级面板窗口当前选中内容</h3>
<p>当获取到了选中内容后，接下来就是需要创建超级面板的 <code>BrowserWindow</code>:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; BrowserWindow, ipcMain, app &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"electron"</span>);

<span class="hljs-built_in">module</span>.exports = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">let</span> win;

  <span class="hljs-keyword">let</span> init = <span class="hljs-function">(<span class="hljs-params">mainWindow</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (win === <span class="hljs-literal">null</span> || win === <span class="hljs-literal">undefined</span>) &#123;
      createWindow();
    &#125;
  &#125;;

  <span class="hljs-keyword">let</span> createWindow = <span class="hljs-function">() =></span> &#123;
    win = <span class="hljs-keyword">new</span> BrowserWindow(&#123;
      <span class="hljs-attr">frame</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">autoHideMenuBar</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">width</span>: <span class="hljs-number">250</span>,
      <span class="hljs-attr">height</span>: <span class="hljs-number">50</span>,
      <span class="hljs-attr">show</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">alwaysOnTop</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">webPreferences</span>: &#123;
        <span class="hljs-attr">webSecurity</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">enableRemoteModule</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">backgroundThrottling</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">nodeIntegration</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">devTools</span>: <span class="hljs-literal">false</span>,
      &#125;,
    &#125;);
    win.loadURL(<span class="hljs-string">`file://<span class="hljs-subst">$&#123;__static&#125;</span>/plugins/superPanel/index.html`</span>);
    win.once(<span class="hljs-string">'ready-to-show'</span>, <span class="hljs-function">() =></span> win.show());
    win.on(<span class="hljs-string">"closed"</span>, <span class="hljs-function">() =></span> &#123;
      win = <span class="hljs-literal">undefined</span>;
    &#125;);
  &#125;;

  <span class="hljs-keyword">let</span> getWindow = <span class="hljs-function">() =></span> win;

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">init</span>: init,
    <span class="hljs-attr">getWindow</span>: getWindow,
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再通知 <code>superPanel</code> 进行内容展示：</p>
<pre><code class="hljs language-js copyable" lang="js"> win.webContents.send(<span class="hljs-string">'trigger-super-panel'</span>, &#123;
  ...copyResult,
  <span class="hljs-attr">optionPlugin</span>: optionPlugin.plugins,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">超级面板点击操作</h3>
<p>接下来要实现超级面板点击操作，这块也是比较简单的了，直接上代码好了：</p>
<h4 data-id="heading-10">1. 打开 Terminal</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; spawn &#125; = <span class="hljs-built_in">require</span> (<span class="hljs-string">'child_process'</span>);

spawn(<span class="hljs-string">'open'</span>, [ <span class="hljs-string">'-a'</span>, <span class="hljs-string">'Terminal'</span>, fileUrl ]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">2. 新建文件</h4>
<pre><code class="hljs language-js copyable" lang="js">remote.dialog.showSaveDialog(&#123;
  <span class="hljs-attr">title</span>: <span class="hljs-string">"请选择要保存的文件名"</span>,
  <span class="hljs-attr">buttonLabel</span>: <span class="hljs-string">"保存"</span>,
  <span class="hljs-attr">defaultPath</span>: fileUrl.replace(<span class="hljs-string">'file://'</span>, <span class="hljs-string">''</span>),
  <span class="hljs-attr">showsTagField</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">nameFieldLabel</span>: <span class="hljs-string">''</span>,
&#125;).then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
  fs.writeFileSync(result.filePath, <span class="hljs-string">''</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">3. 复制路径</h4>
<pre><code class="hljs language-js copyable" lang="js">clipboard.writeText(fileUrl.replace(<span class="hljs-string">'file://'</span>, <span class="hljs-string">''</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">最后</h2>
<p>本篇主要介绍如何实现一个类似于 utools 的超级面板功能，当然这远远不是 utools 的全部，下期我们再继续介绍如何实现 utools 其他能力。欢迎大家前往体验 <a href="https://github.com/clouDr-f2e/rubick" target="_blank" rel="nofollow noopener noreferrer">Rubick</a> 有问题可以随时提 issue 我们会及时反馈。</p>
<p>另外，如果觉得设计实现思路对你有用，也欢迎给个 Star：<a href="https://github.com/clouDr-f2e/rubick" target="_blank" rel="nofollow noopener noreferrer">github.com/clouDr-f2e/…</a></p></div>  
</div>
            