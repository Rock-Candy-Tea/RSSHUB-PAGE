
---
title: '更强大的文件接口，File System Access API｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b96b0289958a45eeb816b6e7f3fc8dd0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 18:06:21 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b96b0289958a45eeb816b6e7f3fc8dd0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><blockquote>
<p>8月更文挑战第一篇，冲冲冲</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>在 <code>HTML5 </code>标准的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FFile" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/File" ref="nofollow noopener noreferrer"><code>File API</code></a>出现之前，前端对于文件的操作是非常有局限性的，大多需要配合后端实现。出于安全角度考虑，从本地上传文件时，代码不可能获取文件在用户本地的地址，所以纯前端不可能完成一些类似图片预览的功能。但是 <code>File API</code> 的出现，让这一切变成了可能。</p>
<p>然而出于安全性考虑，<code>File API</code>存在很多局限性，例如不能直接读取本地文件，创建文件需要通过下载的方式，以及读取文件后不能即时保存修改等等。</p>
<p>本文要介绍的是由 [<code>WICG(Web Incubator Community Group)</code> ](<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.io/" ref="nofollow noopener noreferrer">Web Incubator Community Group (WICG)</a>) 制定的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.github.io%2Ffile-system-access%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.github.io/file-system-access/" ref="nofollow noopener noreferrer"><code>File System Access API</code></a>，其基于现有<code>FIle </code>接口提供了更强大的方法来处理本地文件。</p>
<p>来自官方文档的描述：</p>
<blockquote>
<p>This document defines a web platform API that enables developers to build powerful web apps that interact with files on the user’s local device. It builds on <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.github.io%2Ffile-system-access%2F%23biblio-file-api" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.github.io/file-system-access/#biblio-file-api" ref="nofollow noopener noreferrer">File API</a> for file reading capabilities, and adds new API surface to enable modifying files, as well as working with directories.</p>
<p>本文档定义了一个web平台API，使开发者能够构建强大的web应用程序，与用户本地设备上的文件进行交互。它以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.github.io%2Ffile-system-access%2F%23biblio-file-api" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.github.io/file-system-access/#biblio-file-api" ref="nofollow noopener noreferrer">File API</a>为基础，提供文件读取功能，并添加了新的接口，以支持修改文件以及使用目录。</p>
</blockquote>
<p>这个接口所提供的一系列方法能够让网页直接读取文件并保存修改到本地，以及访问目录。相比于<code>HTML5 </code>所提供的<code>File</code>、<code>FileReader </code>确实是提供了更强大的能力。不过目前该接口只在<code>Chrome</code>及<code>chromium</code>系的<code>Edge</code>浏览器上使用。</p>
<p>这里介绍下<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.io/" ref="nofollow noopener noreferrer"><code>Web Incubator Community Group (WICG)</code></a>，中文全称翻译叫<strong>web平台孵化器社区小组</strong>，是<code>w3c</code>组织的一个分支，负责设计下一代的web标准，因此它们会时不时发布一些接口提案，有兴趣的可以看下这篇介绍 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2Fblog%2F2015%2F07%2Fwicg%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/blog/2015/07/wicg/" ref="nofollow noopener noreferrer"><code>WICG: Evolving the Web from the ground up | W3C Blog</code></a>。</p>
<p>在<code>WICG</code>官网，有许多正在孵化的<code>API</code>实现，这里我们主要关注<code>File System Access</code>，这个接口经历了初始草案，迭代并发布，下面就让我们来使用它。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b96b0289958a45eeb816b6e7f3fc8dd0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">开始</h2>
<p>我们可以新建一个页面文件或者直接在控制台来使用<code>File System Access</code>的相关方法。</p>
<h3 data-id="heading-2">打开文件</h3>
<p>打开文件我们需要调用一个全局方法<code>showOpenFilePicker()</code>，该方法是异步的，调用后会弹出一个文件选择对话框，选择文件后会返回一个存有文件句柄的数组，之所以是数组，因为它允许我们选择多个文件,只需在调用时传入相应的参数即可，包括默认打开的文件目录、文件类型、文件数量等等。</p>
<p>给打开文件按钮绑定一个事件，点击后调用<code>showOpenFilePicker</code>函数，并将文件句柄保存起来。</p>
<p>文件句柄通常是一个系统标识符，可以用来描述窗体、文件等，在<code>C++</code>中，文件句柄就是指向各类对象的指针。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> BtnOpenFile = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn-choose-file'</span>)
<span class="hljs-keyword">const</span> editor = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'editor'</span>)
<span class="hljs-keyword">let</span> fileHandle;
BtnOpenFile.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-keyword">async</span> () => &#123;
  [fileHandle] = <span class="hljs-keyword">await</span> <span class="hljs-built_in">window</span>.showOpenFilePicker()
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从<code>fileHandle</code>对象上，我们能获得文件的内容，属性等信息，</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb31e9cc43fc45029e0afd584ad935b7~tplv-k3u1fbpfcp-watermark.image" alt="image-20210727204843887.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>调用它的<code>getFile</code>方法，得到一个[<code>Blob</code>](<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FBlob%2FBlob" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Blob/Blob" ref="nofollow noopener noreferrer">Blob() - Web API 接口参考 | MDN (mozilla.org)</a>)对象，再调用<code>text()</code>获得文件的内容，对于<code>Blob</code>的其他方法如<code>slice</code>，常用的就是用来作文件切片，这里就不多加介绍。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> BtnOpenFile = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn-choose-file'</span>)
<span class="hljs-keyword">const</span> editor = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'editor'</span>)
<span class="hljs-keyword">const</span> fileHandle;
BtnOpenFile.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-keyword">async</span> () => &#123;
  [fileHandle] = <span class="hljs-keyword">await</span> <span class="hljs-built_in">window</span>.showOpenFilePicker()
<span class="hljs-keyword">const</span> fileBlob = <span class="hljs-keyword">await</span> fileHandle.getFile()
editor.value = <span class="hljs-keyword">await</span> fileBlob.text()
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开文件并获取内容<code>input</code>标签也能实现。</p>
<p><code>getFile()</code>获取的文件句柄可能会失效。当获取了句柄后，删除或移动源文件会造成文件句柄对象失效，这时只能重新调用<code>getFile()</code>获得新的句柄。</p>
<h3 data-id="heading-3">新建文件并保存</h3>
<p>要新建文件，我们调用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.github.io%2Ffile-system-access%2F%23api-showsavefilepicker" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.github.io/file-system-access/#api-showsavefilepicker" ref="nofollow noopener noreferrer"><code>showSaveFilePicker()</code></a>方法，它会打开一个保存文件对话框，同时我们还能传入参数来设置文件的名称、类型等，调用后返回新创建文件的句柄。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> BtnSaveAs = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn-save-as'</span>)

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fileSaveAs</span>(<span class="hljs-params">description</span>) </span>&#123;
  <span class="hljs-keyword">const</span> options = &#123;
    <span class="hljs-attr">types</span>: [
      &#123;
        description,
        <span class="hljs-attr">accept</span>: &#123;
          <span class="hljs-string">'text/plain'</span>: [<span class="hljs-string">'.txt'</span>],
        &#125;,
      &#125;,
    ],
  &#125;;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> <span class="hljs-built_in">window</span>.showSaveFilePicker(options);
&#125;

BtnSaveAs.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-keyword">async</span> ()=>&#123;
  <span class="hljs-keyword">const</span> handle = <span class="hljs-keyword">await</span> fileSaveAs(<span class="hljs-string">"Hello File Access Api"</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击按钮并选择保存位置后，新的文件便被创建和保存，但此时文件是空的，下面我们就往文件内写入数据。</p>
<p>以前要保存文件我们通常生成标签<code><a download="file_name"></code>，然后模拟点击把文件下载下来，如果它是基于现有文件修改的，并不会覆盖原文件。</p>
<h3 data-id="heading-4">写入数据</h3>
<p>要往文件里写入内容，需要调用文件句柄对象上的<code>createWritable()</code>来创建流，它是一个<code>FileSystemWritableFileStream</code>对象。由于从<code>web</code>写入文件到系统是一种不安全的行为，所以浏览器会询问我们是否授权。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">writeFile</span>(<span class="hljs-params">fileHandle, contents</span>) </span>&#123;
   <span class="hljs-comment">// createWritable()创建一个可写流对象WritableStream</span>
   <span class="hljs-keyword">const</span> writable = <span class="hljs-keyword">await</span> fileHandle.createWritable();
   <span class="hljs-comment">// 通过管道将数据传输到文件</span>
   <span class="hljs-keyword">await</span> writable.write(contents);
   <span class="hljs-comment">// 管道使用完毕后需要关闭</span>
   <span class="hljs-keyword">await</span> writable.close();
 &#125;

BtnSaveAs.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-keyword">async</span> ()=>&#123;
  <span class="hljs-keyword">const</span> handle = <span class="hljs-keyword">await</span> fileSaveAs(<span class="hljs-string">"Hello File Access Api"</span>)
  <span class="hljs-keyword">await</span> writeFile(handle,editor.value)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写入文件的过程是流操作，使用了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FStreams_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Streams_API" ref="nofollow noopener noreferrer"><code>Stream</code></a>相关的<code>API</code>，这里使用的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.github.io%2Ffile-system-access%2F%23api-filesystemwritablefilestream" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.github.io/file-system-access/#api-filesystemwritablefilestream" ref="nofollow noopener noreferrer"><code>FileSystemWritableFileStream</code></a>实际上是一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWritableStream" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/WritableStream" ref="nofollow noopener noreferrer"><code>WritableStream</code></a>实例。</p>
<p><code>write()</code>方法负责写入数据，可以是字符串，<code>Blob</code>对象，也可以是流。</p>
<p>举个栗子，<code>fetch</code>请求响应的<code>response.body</code>就是一个<code>readableStream</code>实例，因此可以直接通过<code>write()</code>写入文件中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">writeURLToFile</span>(<span class="hljs-params">fileHandle, url</span>) </span>&#123;
  <span class="hljs-comment">// 创建要写入的FileSystemWritableFileStream实例</span>
  <span class="hljs-keyword">const</span> writable = <span class="hljs-keyword">await</span> fileHandle.createWritable();
  <span class="hljs-comment">// 请求资源</span>
  <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> fetch(url);
  <span class="hljs-comment">// response.body是一个readableStream实例，使用pipeTo建立管道进行数据传输</span>
  <span class="hljs-keyword">await</span> response.body.pipeTo(writable);
  <span class="hljs-comment">// pipeTo()创建的管道会自动关闭</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而就像在<code>node</code>中使用管道一样，数据传输完成后，如果管道不会自动关闭，那么一定要手动关闭。</p>
<h3 data-id="heading-5">使用默认文件名和默认目录</h3>
<p>有时我们希望保存文件时有一个默认文件名，就像<code>Typora</code>的默认文件名是<code>Untitled</code>那样，又或者我们希望能设置打开文件时所处的默认目录，这些都能通过<code>suggestedName</code>、<code>startIn</code>这两个属性来实现，只需掉调用类似<code>showXxxPicker</code>方法时传入即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fileHandle = <span class="hljs-keyword">await</span> self.showSaveFilePicker(&#123;
  <span class="hljs-comment">// 默认文件名</span>
  <span class="hljs-attr">suggestedName</span>: <span class="hljs-string">'Untitled'</span>,
  <span class="hljs-comment">// 默认打开桌面目录</span>
  <span class="hljs-attr">startIn</span>: <span class="hljs-string">'desktop'</span>
  <span class="hljs-attr">types</span>: [&#123;
    <span class="hljs-attr">description</span>: <span class="hljs-string">'Text documents'</span>,
    <span class="hljs-attr">accept</span>: &#123;
      <span class="hljs-string">'text/plain'</span>: [<span class="hljs-string">'.txt'</span>],
    &#125;,
  &#125;],
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是常用的系统目录列表：</p>
<ul>
<li><code>desktop</code>: 桌面</li>
<li><code>documents</code>: 文档</li>
<li><code>downloads</code>: 下载</li>
<li><code>music</code>: 音乐</li>
<li><code>pictures</code>: 图像</li>
<li><code>videos</code>: 视频</li>
</ul>
<p>除了常用的系统目录，我们也能传入自定义目录的句柄，自定义目录需要我们调用<code>showDirectoryPicker()</code>获得。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 选择文件要保存的目录</span>
<span class="hljs-keyword">const</span> directoryHandle = <span class="hljs-keyword">await</span> showDirectoryPicker()
<span class="hljs-keyword">const</span> fileHandle = <span class="hljs-keyword">await</span> showOpenFilePicker(&#123;
  <span class="hljs-comment">// 作为文件保存的起始目录</span>
  <span class="hljs-attr">startIn</span>: directoryHandle
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">打开目录并获取其内容</h3>
<p>调用<code>showDirectoryPicker()</code>，我们可以选择要查看的目录，然后返回对应的目录句柄，它是一个<code>FileSystemDirectoryHandle</code>对象实例，使用它的<code>values()</code>方法我们就能查看目录中有哪些文件了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> btnOpenDirectory = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn-open-dir'</span>);
btnOpenDirectory.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> dirHandle = <span class="hljs-keyword">await</span> <span class="hljs-built_in">window</span>.showDirectoryPicker();
  <span class="hljs-keyword">for</span> <span class="hljs-keyword">await</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> dirHandle.values()) &#123;
    <span class="hljs-built_in">console</span>.log(item)
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在打开之前，浏览器会询问我们是否允许，允许后会在地址栏内出现一个目录标志。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0e1fe1c5b6746a7b615c3e70c404bda~tplv-k3u1fbpfcp-watermark.image" alt="image-20210727220600828.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37e44310ae974b0ca910ae3737e04d3e~tplv-k3u1fbpfcp-watermark.image" alt="image-20210727220638745.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>控制台输出了目录中有哪些文件。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4836cfce15144a94bbbf5ee821b8ea51~tplv-k3u1fbpfcp-watermark.image" alt="image-20210727220714123.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是处于安全着想，浏览器不允许我们访问一些敏感目录，例如包含系统文件的目录或者组策略不允许访问的目录。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5628fac834c464b9f8fb5764d6627e9~tplv-k3u1fbpfcp-watermark.image" alt="image-20210727220934861.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">创建或访问目录中的文件与文件夹</h3>
<p>在目录中，可以调用目录句柄的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.github.io%2Ffile-system-access%2F%23dom-filesystemdirectoryhandle-getfilehandle" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.github.io/file-system-access/#dom-filesystemdirectoryhandle-getfilehandle" ref="nofollow noopener noreferrer"><code>getFileHandle()</code></a>和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.github.io%2Ffile-system-access%2F%23dom-filesystemdirectoryhandle-getdirectoryhandle" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.github.io/file-system-access/#dom-filesystemdirectoryhandle-getdirectoryhandle" ref="nofollow noopener noreferrer"><code>getDirectoryHandle()</code></a>方法来访问文件和子目录，同时可以传入一个<code>&#123;create&#125;</code>对象参数，表示在当文件或目录不存在时创建它。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 当MyDocuments不存在时将会创建它</span>
<span class="hljs-keyword">const</span> newDirectoryHandle = <span class="hljs-keyword">await</span> existingDirectoryHandle.getDirectoryHandle(<span class="hljs-string">'MyDocuments'</span>, &#123;
  <span class="hljs-attr">create</span>: <span class="hljs-literal">true</span>,
&#125;);
<span class="hljs-comment">// 当text.txt在当前目录不存在则新建</span>
<span class="hljs-keyword">const</span> newFileHandle = <span class="hljs-keyword">await</span> newDirectoryHandle.getFileHandle(<span class="hljs-string">'text.txt'</span>, &#123; <span class="hljs-attr">create</span>: <span class="hljs-literal">true</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">删除文件或目录</h3>
<p>当已经获得了一个目录的句柄时，要想删除该目录或目录下的某个文件，可以调用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.github.io%2Ffile-system-access%2F%23dom-filesystemdirectoryhandle-removeentry" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.github.io/file-system-access/#dom-filesystemdirectoryhandle-removeentry" ref="nofollow noopener noreferrer"><code>removeEntry()</code></a>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 删除文件</span>
<span class="hljs-keyword">await</span> directoryHandle.removeEntry(<span class="hljs-string">'text.txt'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认条件下，只能删除空目录，否则会报错，但是可以传入一个对象表示要递归删除目录下的所有子目录和文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 递归删除目录下的所有文件和子目录</span>
<span class="hljs-keyword">await</span> directoryHandle.removeEntry(<span class="hljs-string">'oldDir'</span>, &#123; <span class="hljs-attr">recursive</span>: <span class="hljs-literal">true</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还要注意的是，如果删除不存的目录或文件，返回的操作结果也是成功的。</p>
<h3 data-id="heading-9">解析目录下文件的路径</h3>
<p>通过目录句柄的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.github.io%2Ffile-system-access%2F%23api-filesystemdirectoryhandle-resolve" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.github.io/file-system-access/#api-filesystemdirectoryhandle-resolve" ref="nofollow noopener noreferrer"><code>resolve()</code></a>方法，我们能获得一个表示文件所处路径的数组，文件必须位于目录内，可以是目录的子目录。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-keyword">await</span> directoryHandle.resolve(fileHandle);
<span class="hljs-comment">// `path` is now ["desktop", "text.txt"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">浏览器支持</h2>
<p>通过[Can I use](<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F%3Fsearch%3DFile" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/?search=File" ref="nofollow noopener noreferrer">caniuse.com/?search=Fil…</a> Access)网站看，除了谷歌、<code>Edge</code>、<code>Opera</code>外，其他浏览器一律不支持。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d69ca01f4bb4019b4644033dba813ff~tplv-k3u1fbpfcp-watermark.image" alt="8-1-4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">总结</h2>
<p>对比现有的<code>File API</code>，<code>File System Access API</code>确实更加强大，但由于没有成为标准，甚至未来某一天被废弃或者更改，因此用于生产环境前需要谨慎考虑，但对于个人开发者来说，我们可以利用它实现一个网页端的文本编辑器，比如说基于<code>PWN</code>的低配版<code>Typora</code>，或者将它作为<code>web</code>应用安装到桌面。<code>Typora</code>基于<code>Electron</code> 和 <code>node</code>拥有操控系统文件的能力，现有的<code>File API</code> 不能打开一个目录，虽然<code><input type="file" webkitdirectory></code>可以实现，但它不是标准，<code>File System Access API</code>能帮我们实现这个功能。综上，使用<code>File System Access</code>做一个小项目也是个不错的主意。</p>
<p>推荐一个库<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FGoogleChromeLabs%2Fbrowser-fs-access" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/GoogleChromeLabs/browser-fs-access" ref="nofollow noopener noreferrer">browser-fs-access</a>，它提供了对<code>File Access System API</code>的封装，当浏览器支持时会优先使用，当浏览器不支持会进行降级使用<code>File API</code>.</p>
<p>相关<code>Demo</code>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbrowser-fs-access.glitch.me%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://browser-fs-access.glitch.me/" ref="nofollow noopener noreferrer">Browser-FS-Access.js Demo</a></p>
<h2 data-id="heading-12">参考</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwicg.github.io%2Ffile-system-access%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://wicg.github.io/file-system-access/" ref="nofollow noopener noreferrer">File System Access (wicg.github.io)</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FStreams_API%2FConcepts" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Streams_API/Concepts" ref="nofollow noopener noreferrer">Streams API 概念 - Web API 接口参考 | MDN (mozilla.org)</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FFile" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/File" ref="nofollow noopener noreferrer">File - Web API 接口参考 | MDN (mozilla.org)</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FWICG%2Ffile-system-access" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/WICG/file-system-access" ref="nofollow noopener noreferrer">WICG/file-system-access: Expose the file system on the user’s device, so Web apps can interoperate with the user’s native applications. (github.com)</a></li>
</ul></div>  
</div>
            