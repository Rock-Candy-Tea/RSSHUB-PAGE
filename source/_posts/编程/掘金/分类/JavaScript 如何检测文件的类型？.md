
---
title: 'JavaScript 如何检测文件的类型？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba59f570a184413c952c69db1a63f5ca~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 15:12:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba59f570a184413c952c69db1a63f5ca~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在日常工作中，文件上传是一个很常见的功能。在某些情况下，我们希望能限制文件上传的类型，比如限制只能上传 PNG 格式的图片。针对这个问题，我们会想到通过 <code>input</code> 元素的 <code>accept</code> 属性来限制上传的文件类型：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"inputFile"</span> <span class="hljs-attr">accept</span>=<span class="hljs-string">"image/png"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方案虽然可以满足大多数场景，但如果用户把 JPEG 格式的图片后缀名更改为 <code>.png</code> 的话，就可以成功突破这个限制。那么应该如何解决这个问题呢？其实我们可以通过读取文件的二进制数据来识别正确的文件类型。在介绍具体的实现方案前，阿宝哥先以图片类型的文件为例，来介绍一下相关的知识。</p>
<h3 data-id="heading-0">一、如何查看图片的二进制数据</h3>
<p>要查看图片对应的二进制数据，我们可以借助一些现成的编辑器，比如 Windows 平台下的 <strong>WinHex</strong> 或 macOS 平台下的 <strong>Synalyze It! Pro</strong> 十六进制编辑器。这里我们使用 <strong>Synalyze It! Pro</strong> 这个编辑器，以十六进制的形式来查看阿宝哥头像对应的二进制数据。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba59f570a184413c952c69db1a63f5ca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 50 几篇 TS 系列教程。</p>
</blockquote>
<h3 data-id="heading-1">二、如何区分图片的类型</h3>
<p><strong>计算机并不是通过图片的后缀名来区分不同的图片类型，而是通过 “魔数”（Magic Number）来区分。</strong> 对于某一些类型的文件，起始的几个字节内容都是固定的，根据这几个字节的内容就可以判断文件的类型。</p>
<p>常见图片类型对应的魔数如下表所示：</p>






























<table><thead><tr><th>文件类型</th><th>文件后缀</th><th>魔数</th></tr></thead><tbody><tr><td>JPEG</td><td>jpg/jpeg</td><td>0xFF D8 FF</td></tr><tr><td>PNG</td><td>png</td><td>0x89 50 4E 47 0D 0A 1A 0A</td></tr><tr><td>GIF</td><td>gif</td><td>0x47 49 46 38（GIF8）</td></tr><tr><td>BMP</td><td>bmp</td><td>0x42 4D</td></tr></tbody></table>
<p>同样使用 <strong>Synalyze It! Pro</strong> 这个编辑器，来验证一下阿宝哥的头像（abao.png）的类型是否正确：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d00b4bc360a64bc39853631ad614c200~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由上图可知，PNG 类型的图片前 8 个字节是 <strong>0x89 50 4E 47 0D 0A 1A 0A</strong>。当你把 <code>abao.png</code> 文件修改为 <code>abao.jpeg</code> 后，再用编辑器打开查看图片的二进制内容，你会发现文件的前 8 个字节还是保持不变。但如果使用 <code>input[type="file"]</code> 输入框的方式来读取文件信息的话，将会输出以下结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8dfd93c6de354e53b0a796a34d7f4432~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>很明显通过 <strong>文件后缀名或文件的 MIME 类型</strong> 并不能识别出正确的文件类型。接下来，阿宝哥将介绍在上传图片时，如何通过读取图片的二进制信息来确保正确的图片类型。</p>
<h3 data-id="heading-2">三、如何检测图片的类型</h3>
<h4 data-id="heading-3">3.1 定义 readBuffer 函数</h4>
<p>在获取文件对象后，我们可以通过 FileReader API 来读取文件的内容。因为我们并不需要读取文件的完整信息，所以阿宝哥封装了一个 <code>readBuffer</code> 函数，用于读取文件中指定范围的二进制数据。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readBuffer</span>(<span class="hljs-params">file, start = <span class="hljs-number">0</span>, end = <span class="hljs-number">2</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> reader = <span class="hljs-keyword">new</span> FileReader();
    reader.onload = <span class="hljs-function">() =></span> &#123;
      resolve(reader.result);
    &#125;;
    reader.onerror = reject;
    reader.readAsArrayBuffer(file.slice(start, end));
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 PNG 类型的图片来说，该文件的前 8 个字节是 <strong>0x89 50 4E 47 0D 0A 1A 0A</strong>。因此，我们在检测已选择的文件是否为 PNG 类型的图片时，只需要读取前 8 个字节的数据，并逐一判断每个字节的内容是否一致。</p>
<h4 data-id="heading-4">3.2 定义 check 函数</h4>
<p>为了实现逐字节比对并能够更好地实现复用，阿宝哥定义了一个 <code>check</code> 函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">check</span>(<span class="hljs-params">headers</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">buffers, options = &#123; offset: <span class="hljs-number">0</span> &#125;</span>) =></span>
    headers.every(
      <span class="hljs-function">(<span class="hljs-params">header, index</span>) =></span> header === buffers[options.offset + index]
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">3.3 检测 PNG 图片类型</h4>
<p>基于前面定义的 <code>readBuffer</code> 和 <code>check</code> 函数，我们就可以实现检测 PNG 图片的功能：</p>
<h5 data-id="heading-6">3.3.1 html 代码</h5>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
   选择文件：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"inputFile"</span> <span class="hljs-attr">accept</span>=<span class="hljs-string">"image/*"</span>
              <span class="hljs-attr">onchange</span>=<span class="hljs-string">"handleChange(event)"</span> /></span>
   <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"realFileType"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">3.3.2 JS 代码</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> isPNG = check([<span class="hljs-number">0x89</span>, <span class="hljs-number">0x50</span>, <span class="hljs-number">0x4e</span>, <span class="hljs-number">0x47</span>, <span class="hljs-number">0x0d</span>, <span class="hljs-number">0x0a</span>, <span class="hljs-number">0x1a</span>, <span class="hljs-number">0x0a</span>]); <span class="hljs-comment">// PNG图片对应的魔数</span>
<span class="hljs-keyword">const</span> realFileElement = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#realFileType"</span>);

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleChange</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-keyword">const</span> file = event.target.files[<span class="hljs-number">0</span>];
  <span class="hljs-keyword">const</span> buffers = <span class="hljs-keyword">await</span> readBuffer(file, <span class="hljs-number">0</span>, <span class="hljs-number">8</span>);
  <span class="hljs-keyword">const</span> uint8Array = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(buffers);
  realFileElement.innerText = <span class="hljs-string">`<span class="hljs-subst">$&#123;file.name&#125;</span>文件的类型是：<span class="hljs-subst">$&#123;
    isPNG(uint8Array) ? <span class="hljs-string">"image/png"</span> : file.type
  &#125;</span>`</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上示例成功运行后，对应的检测结果如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebc0f907780145f1838cb25eef8979db~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由上图可知，我们已经可以成功地检测出正确的图片格式。如果你要检测 JPEG 文件格式的话，你只需要定义一个 <code>isJPEG</code> 函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> isJPEG = check([<span class="hljs-number">0xff</span>, <span class="hljs-number">0xd8</span>, <span class="hljs-number">0xff</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而，如果你要检测其他类型的文件，比如 PDF 文件的话，应该如何处理呢？这里我们先使用 <strong>Synalyze It! Pro</strong> 编辑器来浏览一下 PDF 文件的二进制内容：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06ba46908a3f4298909ff5e814e4e4e4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>观察上图可知，PDF 文件的头 4 个字节的是 <strong>0x25 50 44 46</strong>，对应的字符串是 <strong>%PDF</strong>。为了让用户能更直观地辨别出检测的类型，阿宝哥定义了一个 <code>stringToBytes</code> 函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">stringToBytes</span>(<span class="hljs-params">string</span>) </span>&#123;
  <span class="hljs-keyword">return</span> [...string].map(<span class="hljs-function">(<span class="hljs-params">character</span>) =></span> character.charCodeAt(<span class="hljs-number">0</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于 <code>stringToBytes</code> 函数，我们就可以很容易的定义一个 <code>isPDF</code> 函数，具体如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> isPDF = check(stringToBytes(<span class="hljs-string">"%PDF"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了 <code>isPDF</code> 函数，你就实现 PDF 文件检测的功能了。但在实际工作中，遇到的文件类型是多种多样的，针对这种情形，你可以使用现成的第三库来实现文件检测的功能，比如 <a href="https://github.com/sindresorhus/file-type#readme" target="_blank" rel="nofollow noopener noreferrer">file-type</a> 这个库。</p>
<p>其实基于文件的二进制数据，除了可以检测文件的类型之外，我们还可以读取文件相关的元信息，比如图片的尺寸、位深度、色彩类型和压缩算法等，我们继续以阿宝哥的头像（abao.png）为例，来看一下实际的情况：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d584b3c2dd64361b7e7d8c5ae7ec9f4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好的，在前端如何检测文件类型就介绍到这里。在实际项目中，对于文件上传的场景，出于安全考虑，建议小伙伴们在开发过程中，都限制一下文件上传的类型。对于更严格的场景来说，就可以考虑使用阿宝哥介绍的方法来做文件类型的校验。此外，如果你对前端如何处理二进制数据感兴趣可以阅读 <a href="https://mp.weixin.qq.com/s/QHi6BVM5Jt8XwZ_FKcRYsg" target="_blank" rel="nofollow noopener noreferrer">玩转前端二进制</a>。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 11 篇 Vue 3 进阶系列教程。<strong>想一起学习 TS/Vue 3.0 的小伙伴可以添加阿宝哥微信 —— semlinker</strong>。</p>
</blockquote>
<h3 data-id="heading-8">四、参考资源</h3>
<ul>
<li><a href="https://mp.weixin.qq.com/s/QHi6BVM5Jt8XwZ_FKcRYsg" target="_blank" rel="nofollow noopener noreferrer">玩转前端二进制</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/FileReader" target="_blank" rel="nofollow noopener noreferrer">MDN - FileReader</a></li>
</ul></div>  
</div>
            