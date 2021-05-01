
---
title: 'Vue进行Electron开发近期增补记录'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64978e1532b34b419e11d04ddbe420ca~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Apr 2021 23:13:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64978e1532b34b419e11d04ddbe420ca~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>继上一篇文章: <a href="https://www.jianshu.com/p/9d5e9bc001f5" target="_blank" rel="nofollow noopener noreferrer">如何用Vue开发Electron桌面程序? 这篇就够了! - 简书 (jianshu.com)</a></p>
</blockquote>
<p>这篇文章主要介绍</p>
<ul>
<li><code>asar</code>包的简单保护</li>
<li>支持快捷键的使用</li>
<li>菜单的动态修改</li>
<li>日志功能</li>
</ul>
<h3 data-id="heading-0">1. <code>asar</code>的包的使用</h3>
<p>从上篇我们知道, <code>asar</code>包可以用7z的插件或者直接使用asar命令解压, 但是有时候我们不像让人解压直接看到我们的代码逻辑, 可以使用一个库来修改, 即<a href="https://github.com/sleeyax/asarmor" target="_blank" rel="nofollow noopener noreferrer">asarmo</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64978e1532b34b419e11d04ddbe420ca~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我也有幸贡献了代码, 将它的<code>write</code>方法修改成返回Promise对象, 方便进行同步操作, 比如打增量包
<a href="https://github.com/sleeyax/asarmor/pull/10" target="_blank" rel="nofollow noopener noreferrer">feat: make asarmor.write() return the Promise by klren0312 · Pull Request #10 · sleeyax/asarmor (github.com)</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; Asarmor, Trashify, FileCrash &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'asarmor'</span>)
<span class="hljs-keyword">const</span> &#123; join &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> AdmZip = <span class="hljs-built_in">require</span>(<span class="hljs-string">'adm-zip'</span>)
<span class="hljs-keyword">const</span> pkg = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./package.json'</span>)
<span class="hljs-built_in">exports</span>.default = <span class="hljs-keyword">async</span> (&#123; appOutDir, packager, outDir &#125;) => &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> asarPath = join(packager.getResourcesDir(appOutDir), <span class="hljs-string">'app.asar'</span>)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`applying asarmor protections to <span class="hljs-subst">$&#123;asarPath&#125;</span>`</span>)
    <span class="hljs-keyword">const</span> asarmor = <span class="hljs-keyword">new</span> Asarmor(asarPath)
    asarmor.applyProtection(<span class="hljs-keyword">new</span> FileCrash(<span class="hljs-string">'background.js.LICENSE.txt'</span>))
    asarmor.applyProtection(<span class="hljs-keyword">new</span> Trashify([<span class="hljs-string">'.git'</span>, <span class="hljs-string">'.env'</span>]))
    <span class="hljs-keyword">await</span> asarmor.write(asarPath)

    <span class="hljs-keyword">const</span> targetPath = join(appOutDir, <span class="hljs-string">'./resources'</span>)
    <span class="hljs-keyword">const</span> zip = <span class="hljs-keyword">new</span> AdmZip()
    zip.addLocalFolder(targetPath)
    <span class="hljs-keyword">const</span> partUpdateFile = <span class="hljs-string">`update-win-<span class="hljs-subst">$&#123;pkg.version&#125;</span>.zip`</span>
    zip.writeZip(join(outDir, partUpdateFile))
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.error(err)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://github.com/sleeyax/asarmor" target="_blank" rel="nofollow noopener noreferrer">asarmo</a>库有以下几个功能(使用7z插件进行解压, 虽然都会报错, 但是只有第一种时无法将文件解压出来, 其他其实都已经解压出来了)</p>
<ol>
<li>对压缩包中的指定文件进行损坏(一定是不会被调用的文件, 不然会使<code>electron</code>也无法访问, 导致无法运行)</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74798700932940c28ab39eaa9106d5e9~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe6f3f0a241341fabd04799b2ca1b707~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>生成大量随机文件填充压缩包, 解压的时候阻塞解压(可以指定文件的体积, 例如10G, 则解压时会进行10G文件解压), 但是这样似乎不会导致文件无法解压, 取消解压后, 其实文件已经解压出来了</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7bbc4e92ae04ec3828f4347d8991e11~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d766abb54f3d4aa0bf89832bdbc9fff7~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf92cf875088408386a8ba0a6f8eee5d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>往压缩包里添加不存在文件</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed5b78bf2ec64188b902ef2ea1d89c71~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48e36b74031c48238da2909dd8779676~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd6d0a89bfbe4958b756c72b842cdc1c~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://github.com/sleeyax/asarmor" target="_blank" rel="nofollow noopener noreferrer">asarmo</a>实现这些的主要原理就是通过<a href="https://github.com/electron-archive/node-chromium-pickle" target="_blank" rel="nofollow noopener noreferrer">chromium-pickle</a>来对<code>asar</code>打包和解包的工具, 对包的header信息进行修改, 从而使解压出现错误</p>
<ol>
<li>上面的第一种方法, 我们可以看到, 我们指定的文件size修改成了负值</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/563a7fe99f4e40029d1ac65b47744581~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>第二种方法, 我们可以看到, header信息里被添加了很多随机文件</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/005b61893e594c9e9a5cc1d049d4d6d1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>第三种方法, 我们可以看到, 添加了我们指定的不存在的文件</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30ecbc5680e6403c82346a409f90138b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">2. 支持快捷键的使用</h3>
<p><code>electron</code>官方已经支持了快捷键的使用, 可以访问<a href="https://www.electronjs.org/docs/api/global-shortcut" target="_blank" rel="nofollow noopener noreferrer">globalShortcut</a>
了解
我们可以在窗口<code>focus</code>的时候注册快捷键, 然后在<code>blur</code>的时候注销快捷键</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 窗口聚焦</span>
win.on(<span class="hljs-string">'focus'</span>, <span class="hljs-function">() =></span> &#123;
    globalShortcut.register(<span class="hljs-string">'Alt+A'</span>, <span class="hljs-function">() =></span> &#123;
       <span class="hljs-comment">// 相关逻辑</span>
    &#125;)
&#125;)
<span class="hljs-comment">// 窗口失焦</span>
win.on(<span class="hljs-string">'blur'</span>, <span class="hljs-function">() =></span> &#123;
  globalShortcut.unregister(<span class="hljs-string">'Alt+A'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. 菜单的动态修改</h3>
<p>获取<code>const menuInstance = Menu.buildFromTemplate(this.template)</code>创建的菜单实例
通过<code>menuInstance.items</code>获取菜单数组, 来修改相关菜单</p>
<h3 data-id="heading-3">4. 日志功能</h3>
<p>使用<a href="https://github.com/winstonjs/winston" target="_blank" rel="nofollow noopener noreferrer">winston</a>来实现日志功能,
通过<a href="https://github.com/winstonjs/winston-daily-rotate-file" target="_blank" rel="nofollow noopener noreferrer">winston-daily-rotate-file: A transport for winston which logs to a rotating file each day. (github.com)</a>对日志进行限制, 定期清除</p>
<p>封装日志组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; transports, createLogger, format &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'winston'</span>)
<span class="hljs-keyword">const</span> &#123; combine, timestamp, printf &#125; = format
<span class="hljs-built_in">require</span>(<span class="hljs-string">'winston-daily-rotate-file'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-keyword">const</span> dateFormat = <span class="hljs-function"><span class="hljs-params">date</span> =></span> &#123;
  <span class="hljs-keyword">const</span> addZero = <span class="hljs-function"><span class="hljs-params">num</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (num < <span class="hljs-number">10</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'0'</span> + num
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> num
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> year = date.getFullYear()
  <span class="hljs-keyword">const</span> month = addZero(date.getMonth() + <span class="hljs-number">1</span>)
  <span class="hljs-keyword">const</span> day = addZero(date.getDate())
  <span class="hljs-keyword">const</span> hour = addZero(date.getHours())
  <span class="hljs-keyword">const</span> minute = addZero(date.getMinutes())
  <span class="hljs-keyword">const</span> second = addZero(date.getSeconds())
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;year&#125;</span>-<span class="hljs-subst">$&#123;month&#125;</span>-<span class="hljs-subst">$&#123;day&#125;</span> <span class="hljs-subst">$&#123;hour&#125;</span>:<span class="hljs-subst">$&#123;minute&#125;</span>:<span class="hljs-subst">$&#123;second&#125;</span>`</span>
&#125;

<span class="hljs-keyword">const</span> myFormat = printf(<span class="hljs-function">(<span class="hljs-params">&#123; level, message, timestamp &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;dateFormat(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(timestamp))&#125;</span> - <span class="hljs-subst">$&#123;level&#125;</span>: <span class="hljs-subst">$&#123;message&#125;</span>`</span>
&#125;)

<span class="hljs-keyword">const</span> app =
  process.type === <span class="hljs-string">'browser'</span>
    ? <span class="hljs-built_in">require</span>(<span class="hljs-string">'electron'</span>).app
    : <span class="hljs-built_in">require</span>(<span class="hljs-string">'electron'</span>).remote.app

<span class="hljs-keyword">const</span> logDir = path.resolve(app.getPath(<span class="hljs-string">'userData'</span>), <span class="hljs-string">'logs'</span>)

<span class="hljs-comment">// const logLevel = process.env.NODE_ENV === 'production' ? 'info' : 'debug';</span>
<span class="hljs-keyword">const</span> logLevel = <span class="hljs-string">'debug'</span>

<span class="hljs-keyword">const</span> levels = &#123;
  <span class="hljs-attr">debug</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">info</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">warn</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">error</span>: <span class="hljs-number">3</span>
&#125;

<span class="hljs-keyword">const</span> d = <span class="hljs-function">(<span class="hljs-params">level, message</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (levels[level] >= levels[logLevel]) &#123;
    <span class="hljs-keyword">const</span> consoleLevel = level === <span class="hljs-string">'debug'</span> ? <span class="hljs-string">'log'</span> : level
    <span class="hljs-built_in">console</span>[consoleLevel](message)
  &#125;
&#125;

<span class="hljs-comment">// App进程</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">AppLogger</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> appLogFileName = path.resolve(logDir, <span class="hljs-string">'appLogs%DATE%.log'</span>)
  <span class="hljs-keyword">const</span> transport = <span class="hljs-keyword">new</span> transports.DailyRotateFile(&#123;
    <span class="hljs-attr">level</span>: logLevel,
    <span class="hljs-attr">filename</span>: appLogFileName,
    <span class="hljs-attr">maxSize</span>: <span class="hljs-string">'5m'</span>,
    <span class="hljs-attr">maxFiles</span>: <span class="hljs-string">'15d,100m'</span> <span class="hljs-comment">// 15天以前的自动删除，文件大小超过100m时将旧文件删</span>
  &#125;)

  <span class="hljs-built_in">this</span>.logger = createLogger(&#123;
    <span class="hljs-attr">format</span>: combine(timestamp(), myFormat),
    <span class="hljs-attr">transports</span>: [transport]
  &#125;)
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
&#125;

AppLogger.prototype.debug = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debug</span>(<span class="hljs-params">message</span>) </span>&#123;
  d(<span class="hljs-string">'debug'</span>, message)
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.logger.debug(message)
&#125;

AppLogger.prototype.info = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">info</span>(<span class="hljs-params">message</span>) </span>&#123;
  d(<span class="hljs-string">'info'</span>, message)
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.logger.info(message)
&#125;

AppLogger.prototype.warn = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">warn</span>(<span class="hljs-params">message</span>) </span>&#123;
  d(<span class="hljs-string">'warn'</span>, message)
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.logger.warn(message)
&#125;

AppLogger.prototype.error = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">error</span>(<span class="hljs-params">message</span>) </span>&#123;
  d(<span class="hljs-string">'error'</span>, message)
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.logger.error(message)
&#125;

<span class="hljs-keyword">const</span> appLogger = <span class="hljs-keyword">new</span> AppLogger()

<span class="hljs-built_in">module</span>.exports = &#123;
  appLogger
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用日志组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; appLogger &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./Logger'</span>
appLogger.info(<span class="hljs-string">`------ 日志 ------`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52e185fb167e43b6a8be5c7a4cf4f708~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            