
---
title: 'JavaScript 如何在线解压 ZIP 文件？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9261b3c0780d49d3b6935995e631fc0d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 15:26:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9261b3c0780d49d3b6935995e631fc0d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>相信大家对 ZIP 文件都不会陌生，当你要打开本地的 ZIP 文件时，你就需要先安装支持解压 ZIP 文件的解压软件。但如果预解压的 ZIP 文件在服务器上，我们应该如何处理呢？最简单的一种方案就是把文件下载到本地，然后使用支持 ZIP 格式的解压软件进行解压。那么能不能在线解压 ZIP 文件呢？答案是可以的，接下来阿宝哥将介绍浏览器解压和服务器解压两种在线解压 ZIP 文件的方案。</p>
<p>在介绍在线解压 ZIP 文件的两种方案前，我们先来简单了解一下 ZIP 文件格式。</p>
<h3 data-id="heading-0">一、ZIP 格式简介</h3>
<p>ZIP 文件格式是一种数据压缩和文档储存的文件格式，原名 Deflate，发明者为菲尔·卡茨（Phil Katz），他于 1989 年 1 月公布了该格式的资料。ZIP 通常使用后缀名 “.zip”，它的 MIME 格式为 “application/zip”。目前，ZIP 格式属于几种主流的压缩格式之一，其竞争者包括RAR 格式以及开放源码的 7z 格式。</p>
<p>ZIP 是一种相当简单的分别压缩每个文件的存档格式，分别压缩文件允许不必读取另外的数据而检索独立的文件。理论上，这种格式允许对不同的文件使用不同的算法。然而，在实际上，ZIP 大多数都是在使用卡茨（Katz）的 DEFLATE 算法。</p>
<p>简单介绍完 ZIP 格式，接下来阿宝哥先来介绍基于 <code>JSZip</code> 这个库的浏览器解压方案。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 11 篇 Vue 3 进阶系列教程。</p>
</blockquote>
<h3 data-id="heading-1">二、浏览器解压方案</h3>
<p><a href="https://stuk.github.io/jszip/" target="_blank" rel="nofollow noopener noreferrer">JSZip</a> 是一个用于创建、读取和编辑 <code>.zip</code> 文件的 JavaScript 库，该库支持大多数浏览器，具体的兼容性如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9261b3c0780d49d3b6935995e631fc0d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实有了 <a href="https://stuk.github.io/jszip/" target="_blank" rel="nofollow noopener noreferrer">JSZip</a> 这个库的帮助，要实现浏览器端在线解压 ZIP 文件的功能并不难。因为官方已经为我们提供了 <strong>解压本地文件、解压远程文件和生成 ZIP 文件</strong> 的完整示例。好的，废话不多说，下面我们来一步步实现在线解压 ZIP 文件的功能。</p>
<h4 data-id="heading-2">2.1 定义工具类</h4>
<p>浏览器端在线解压 ZIP 文件的功能，可以拆分为 <strong>下载 ZIP 文件、解析 ZIP 文件和展示 ZIP 文件</strong> 3 个小功能。考虑到功能复用性，阿宝哥把下载 ZIP 文件和解析 ZIP 文件的逻辑封装在 <code>ExeJSZip</code> 类中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ExeJSZip</span> </span>&#123;
  <span class="hljs-comment">// 用于获取url地址对应的文件内容</span>
  <span class="hljs-function"><span class="hljs-title">getBinaryContent</span>(<span class="hljs-params">url, progressFn = () => &#123;&#125;</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> url !== <span class="hljs-string">"string"</span> || !<span class="hljs-regexp">/https?:/</span>.test(url))
        reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"url 参数不合法"</span>));
      JSZipUtils.getBinaryContent(url, &#123; <span class="hljs-comment">// JSZipUtils来自于jszip-utils这个库</span>
        <span class="hljs-attr">progress</span>: progressFn,
        <span class="hljs-attr">callback</span>: <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (err) &#123;
            reject(err);
          &#125; <span class="hljs-keyword">else</span> &#123;
            resolve(data);
          &#125;
        &#125;,
      &#125;);
    &#125;);
  &#125;
  
  <span class="hljs-comment">// 遍历Zip文件</span>
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">iterateZipFile</span>(<span class="hljs-params">data, iterationFn</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> iterationFn !== <span class="hljs-string">"function"</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"iterationFn 不是函数类型"</span>);
    &#125;
    <span class="hljs-keyword">let</span> zip;
    <span class="hljs-keyword">try</span> &#123;
      zip = <span class="hljs-keyword">await</span> JSZip.loadAsync(data); <span class="hljs-comment">// JSZip来自于jszip这个库</span>
      zip.forEach(iterationFn);
      <span class="hljs-keyword">return</span> zip;
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> error();
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2.2 在线解压 ZIP 文件</h4>
<p>利用 <code>ExeJSZip</code> 类的实例，我们就可以很容易实现在线解压 ZIP 文件的功能：</p>
<h5 data-id="heading-4">html 代码</h5>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">label</span>></span>请输入ZIP文件的线上地址：<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"zipUrl"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"unzipBtn"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"unzipOnline()"</span>></span>在线解压<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"status"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"fileList"</span>></span><span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">JS 代码</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> zipUrlEle = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#zipUrl"</span>);
<span class="hljs-keyword">const</span> statusEle = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#status"</span>);
<span class="hljs-keyword">const</span> fileList = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#fileList"</span>);
<span class="hljs-keyword">const</span> exeJSZip = <span class="hljs-keyword">new</span> ExeJSZip();

<span class="hljs-comment">// 执行在线解压操作</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unzipOnline</span>(<span class="hljs-params"></span>) </span>&#123;
  fileList.innerHTML = <span class="hljs-string">""</span>;
  statusEle.innerText = <span class="hljs-string">"开始下载文件..."</span>;
  <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> exeJSZip.getBinaryContent(
    zipUrlEle.value,
    handleProgress
  );
  <span class="hljs-keyword">let</span> items = <span class="hljs-string">""</span>;
  <span class="hljs-keyword">await</span> exeJSZip.iterateZipFile(data, <span class="hljs-function">(<span class="hljs-params">relativePath, zipEntry</span>) =></span> &#123;
    items += <span class="hljs-string">`<li class=<span class="hljs-subst">$&#123;zipEntry.dir ? <span class="hljs-string">"caret"</span> : <span class="hljs-string">"indent"</span>&#125;</span>>
      <span class="hljs-subst">$&#123;zipEntry.name&#125;</span></li>`</span>;
  &#125;);
  statusEle.innerText = <span class="hljs-string">"ZIP文件解压成功"</span>;
  fileList.innerHTML = items;
&#125;

<span class="hljs-comment">// 处理下载进度</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleProgress</span>(<span class="hljs-params">progressData</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; percent, loaded, total &#125; = progressData;
  <span class="hljs-keyword">if</span> (loaded === total) &#123;
    statusEle.innerText = <span class="hljs-string">"文件已下载，努力解压中"</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，在浏览器端如何通过 <a href="https://stuk.github.io/jszip/" target="_blank" rel="nofollow noopener noreferrer">JSZip</a> 这个库来实现在线解压 ZIP 文件的功能已经介绍完了，我们来看一下以上示例的运行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20eaaf0cb7994463825d9c4301f448a3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我们已经可以在线解压 ZIP 文件了，这时有的小伙伴可能会问，能否预览解压后的文件呢？答案是可以的，因为 JSZip 这个库为我们提供了 <code>file</code> API，通过这个 API 我们就可以读取指定文件中的内容。比如这样使用 <code>zip.file("amount.txt").async("arraybuffer")</code> ，之后我们就可以执行对应的操作来实现文件预览的功能。</p>
<p>需要注意的是，基于 JSZip 的方案并不是完美的，它存在一些限制。比如它不支持解压加密的 ZIP 文件，当解压较大的文件时，在 IE 10 以下的浏览器可能会出现闪退问题。此外，它还有一些其它的限制，这里阿宝哥就不详细说明了。感兴趣的小伙伴，可以阅读 <a href="https://stuk.github.io/jszip/documentation/limitations.html" target="_blank" rel="nofollow noopener noreferrer">Limitations of JSZip</a> 文章中的相关内容。</p>
<p>既然浏览器解压方案存在一些弊端，特别是在线解压大文件的情形，要解决该问题，我们可以考虑使用服务器解压方案。</p>
<h3 data-id="heading-6">三、服务器解压方案</h3>
<p>服务器解压方案就是允许用户通过文件 ID 或文件名进行在线解压，接下来阿宝哥将基于 <a href="https://koajs.com/" target="_blank" rel="nofollow noopener noreferrer">koa</a> 和 <a href="https://github.com/antelle/node-stream-zip" target="_blank" rel="nofollow noopener noreferrer">node-stream-zip</a> 这两个库来介绍如何实现服务器在线解压 ZIP 文件的功能。如果你对 <a href="https://koajs.com/" target="_blank" rel="nofollow noopener noreferrer">koa</a> 还不了解的话，建议你先大致阅读一下 koa 的官方文档。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa"</span>);
<span class="hljs-keyword">const</span> cors = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@koa/cors"</span>);
<span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@koa/router"</span>);
<span class="hljs-keyword">const</span> StreamZip = <span class="hljs-built_in">require</span>(<span class="hljs-string">"node-stream-zip"</span>);

<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> Router();
<span class="hljs-keyword">const</span> ZIP_HOME = path.join(__dirname, <span class="hljs-string">"zip"</span>); <span class="hljs-comment">// ZIP文件的根目录</span>
<span class="hljs-keyword">const</span> UnzipCaches = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(); <span class="hljs-comment">// 保存已解压的文件信息</span>

router.get(<span class="hljs-string">"/"</span>, <span class="hljs-keyword">async</span> (ctx) => &#123;
  ctx.body = <span class="hljs-string">"服务端在线解压ZIP文件示例（阿宝哥）"</span>;
&#125;);

<span class="hljs-comment">// 注册中间件</span>
app.use(cors());
app.use(router.routes()).use(router.allowedMethods());

app.listen(<span class="hljs-number">3000</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"app starting at port 3000"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上代码中，我们使用了 <code>@koa/cors</code> 和 <code>@koa/router</code> 两个中间件并创建了一个简单的 Koa 应用程序。基于上述的代码，我们来注册一个用于处理在线解压指定文件名的路由。</p>
<h4 data-id="heading-7">3.1 根据文件名解压指定 ZIP 文件</h4>
<h5 data-id="heading-8">app.js</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript">router.get(<span class="hljs-string">"/unzip/:name"</span>, <span class="hljs-keyword">async</span> (ctx) => &#123;
  <span class="hljs-keyword">const</span> fileName = ctx.params.name;
  <span class="hljs-keyword">let</span> filteredEntries;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">if</span> (UnzipCaches.has(fileName)) &#123; <span class="hljs-comment">// 优先从缓存中获取</span>
      filteredEntries = UnzipCaches.get(fileName);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">const</span> zip = <span class="hljs-keyword">new</span> StreamZip.async(&#123; <span class="hljs-attr">file</span>: path.join(ZIP_HOME, fileName) &#125;);
      <span class="hljs-keyword">const</span> entries = <span class="hljs-keyword">await</span> zip.entries();
      filteredEntries = <span class="hljs-built_in">Object</span>.values(entries).map(<span class="hljs-function">(<span class="hljs-params">entry</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">name</span>: entry.name,
          <span class="hljs-attr">size</span>: entry.size,
          <span class="hljs-attr">dir</span>: entry.isDirectory,
        &#125;;
      &#125;);
      <span class="hljs-keyword">await</span> zip.close();
      UnzipCaches.set(fileName, filteredEntries);
    &#125;
    ctx.body = &#123;
      <span class="hljs-attr">status</span>: <span class="hljs-string">"success"</span>,
      <span class="hljs-attr">entries</span>: filteredEntries,
    &#125;;
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    ctx.body = &#123;
      <span class="hljs-attr">status</span>: <span class="hljs-string">"error"</span>,
      <span class="hljs-attr">msg</span>: <span class="hljs-string">`在线解压<span class="hljs-subst">$&#123;fileName&#125;</span>文件失败`</span>,
    &#125;;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上代码中，我们通过 <code>ZIP_HOME</code> 和 <code>fileName</code> 获得文件的最终路径，然后使用 <code>StreamZip</code> 对象来执行解压操作。为了避免重复执行解压操作，阿宝哥定义了一个 <code>UnzipCaches</code> 缓存对象，用来保存已解压的文件信息。定义好上述路由，下面我们来验证一下对应的功能。</p>
<h4 data-id="heading-9">3.2 在线解压 ZIP 文件</h4>
<h5 data-id="heading-10">html 代码</h5>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">label</span>></span>请输入ZIP文件名：<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"fileName"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"kl_161828427993677"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"unzipBtn"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"unzipOnline()"</span>></span>在线解压<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"status"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"fileList"</span>></span><span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">JS 代码</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fileList = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#fileList"</span>);
<span class="hljs-keyword">const</span> fileNameEle = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#fileName"</span>);

<span class="hljs-keyword">const</span> request = axios.create(&#123;
  <span class="hljs-attr">baseURL</span>: <span class="hljs-string">"http://localhost:3000/"</span>,
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">10000</span>,
&#125;);

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unzipOnline</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> fileName = fileNameEle.value;
  <span class="hljs-keyword">if</span>(!fileName) <span class="hljs-keyword">return</span>;
  <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> request.get(<span class="hljs-string">`unzip/<span class="hljs-subst">$&#123;fileName&#125;</span>`</span>);
  <span class="hljs-keyword">if</span> (response.data && response.data.status === <span class="hljs-string">"success"</span>) &#123;
    <span class="hljs-keyword">const</span> entries = response.data.entries;
    <span class="hljs-keyword">let</span> items = <span class="hljs-string">""</span>;
    entries.forEach(<span class="hljs-function">(<span class="hljs-params">zipEntry</span>) =></span> &#123;
      items += <span class="hljs-string">`<li class=<span class="hljs-subst">$&#123;zipEntry.dir ? <span class="hljs-string">"caret"</span> : <span class="hljs-string">"indent"</span>&#125;</span>><span class="hljs-subst">$&#123;
        zipEntry.name
      &#125;</span></li>`</span>;
    &#125;);
    fileList.innerHTML = items;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上示例成功运行后的结果如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a653a1432b7543d3b7ffccdf688131fa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我们已经实现根据文件名解压指定 ZIP 文件，那么我们可以预览压缩文件中指定路径的文件么？答案也是可以的，利用 <code>zip</code> 对象提供的 <code>entryData(entry: string | ZipEntry): Promise<Buffer></code> 方法就可以读取指定路径下文件的内容。</p>
<h4 data-id="heading-12">3.3 预览 ZIP 文件中指定路径的文件</h4>
<h5 data-id="heading-13">app.js</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript">router.get(<span class="hljs-string">"/unzip/:name/entry"</span>, <span class="hljs-keyword">async</span> (ctx) => &#123;
  <span class="hljs-keyword">const</span> fileName = ctx.params.name; <span class="hljs-comment">// ZIP压缩文件名</span>
  <span class="hljs-keyword">const</span> entryPath = ctx.query.path; <span class="hljs-comment">// 文件的路径</span>
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> zip = <span class="hljs-keyword">new</span> StreamZip.async(&#123; <span class="hljs-attr">file</span>: path.join(ZIP_HOME, fileName) &#125;);
    <span class="hljs-keyword">const</span> entryData = <span class="hljs-keyword">await</span> zip.entryData(entryPath);
    <span class="hljs-keyword">await</span> zip.close();
    ctx.body = &#123;
      <span class="hljs-attr">status</span>: <span class="hljs-string">"success"</span>,
      <span class="hljs-attr">entryData</span>: entryData,
    &#125;;
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    ctx.body = &#123;
      <span class="hljs-attr">status</span>: <span class="hljs-string">"error"</span>,
      <span class="hljs-attr">msg</span>: <span class="hljs-string">`读取<span class="hljs-subst">$&#123;fileName&#125;</span>中<span class="hljs-subst">$&#123;entryPath&#125;</span>文件失败`</span>,
    &#125;;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上代码中，我们通过 <code>zip.entryData</code> 方法来读取指定路径的文件内容，它返回的是一个 <code>Buffer</code> 对象。当前端接收到该数据时，还需要把接收到的 <code>Buffer</code> 对象转换为 <code>ArrayBuffer</code> 对象，对应的处理方式如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toArrayBuffer</span>(<span class="hljs-params">buf</span>) </span>&#123;
  <span class="hljs-keyword">let</span> ab = <span class="hljs-keyword">new</span> <span class="hljs-built_in">ArrayBuffer</span>(buf.length);
  <span class="hljs-keyword">let</span> view = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(ab);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < buf.length; ++i) &#123;
    view[i] = buf[i];
  &#125;
  <span class="hljs-keyword">return</span> ab;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义完 <code>toArrayBuffer</code> 函数之后，我们就可以通过调用 <code>app.js</code> 定义的 API 来实现预览功能，具体的代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">previewZipFile</span>(<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">const</span> fileName = fileNameEle.value; <span class="hljs-comment">// 获取文件名</span>
  <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> request.get(
    <span class="hljs-string">`unzip/<span class="hljs-subst">$&#123;fileName&#125;</span>/entry?path=<span class="hljs-subst">$&#123;path&#125;</span>`</span>
  );
  <span class="hljs-keyword">if</span> (response.data && response.data.status === <span class="hljs-string">"success"</span>) &#123;
    <span class="hljs-keyword">const</span> &#123; entryData &#125; = response.data;
    <span class="hljs-keyword">const</span> entryBuffer = toArrayBuffer(entryData.data);
    <span class="hljs-keyword">const</span> blob = <span class="hljs-keyword">new</span> Blob([entryBuffer]);
    <span class="hljs-comment">// 使用URL.createObjectURL或blob.text()读取文件信息</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于完整的示例代码内容比较多，阿宝哥就不放具体的代码了。感兴趣的小伙伴，可以访问以下地址浏览示例代码。</p>
<blockquote>
<p><a href="https://gist.github.com/semlinker/3bb9634f4e4ec7b6ab4008a688583115" target="_blank" rel="nofollow noopener noreferrer">gist.github.com/semlinker/3…</a></p>
<p>注意：以上代码仅供参考，请根据实际业务进行调整。</p>
</blockquote>
<h3 data-id="heading-14">四、总结</h3>
<p>本文阿宝哥介绍了在线解压 ZIP 文件的两种方案，在实际项目中，建议使用服务器解压的方案。这样不仅可以解决浏览器的兼容性问题，而且也可以解决大文件在线解压的问题，同时也方便后期扩展支持其它的压缩格式。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 11 篇 Vue 3 进阶系列教程。<strong>想一起学习 TS/Vue 3.0 的小伙伴可以添加阿宝哥微信 —— semlinker</strong>。</p>
</blockquote>
<h3 data-id="heading-15">五、参考资源</h3>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/ZIP%E6%A0%BC%E5%BC%8F" target="_blank" rel="nofollow noopener noreferrer">维基百科 ZIP 格式</a></li>
<li><a href="https://stuk.github.io/jszip/documentation/limitations.html" target="_blank" rel="nofollow noopener noreferrer">Limitations of JSZip</a></li>
</ul></div>  
</div>
            