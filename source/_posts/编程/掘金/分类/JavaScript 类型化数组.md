
---
title: 'JavaScript 类型化数组'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bded323a9b348a3bcdbe959069483f0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 18 May 2021 03:24:49 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bded323a9b348a3bcdbe959069483f0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://blog.bitsrc.io/javascript-typed-arrays-ccfa5ae8838d" target="_blank" rel="nofollow noopener noreferrer">JavaScript Typed Arrays</a></li>
<li>原文作者：<a href="https://medium.com/@mahdhirezvi" target="_blank" rel="nofollow noopener noreferrer">Mahdhi Rezvi</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/javascript-typed-arrays.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/PassionPenguin" target="_blank" rel="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：<a href="https://github.com/KimYangOfCat" target="_blank" rel="nofollow noopener noreferrer">KimYang</a>、<a href="https://github.com/Kimhooo" target="_blank" rel="nofollow noopener noreferrer">Kimhooo</a></li>
</ul>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bded323a9b348a3bcdbe959069483f0~tplv-k3u1fbpfcp-watermark.image" alt="图源 Pierre Bamin，出自 Unsplash" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 JavaScript 这门语言中，我们所有人都必须对数组足够熟悉，知晓数组本质上是动态的，并且可以容纳任何 JavaScript 对象。不过，如果你曾经使用过类似于 C 语言这样的其他语言，你应该知道其数组本质上不是动态的。而且你只能在该数组中存储特定的数据类型，毕竟从性能角度来看，这可以确保数组效率更高。但数组的动态化与存储信息类型的多样化其实并没有使 JavaScript 数组效率低下。在 JavaScript 引擎优化的帮助下，JavaScript 中数组的执行速度其实非常快。</p>
<p>随着 Web 应用程序功能越来越强大，我们开始需要让 Web 应用程序处理和操纵原始二进制数据。JavaScript 数组无法处理这些原始二进制数据，也因此我们引入了 JavaScript 的类型化数组。</p>
<h2 data-id="heading-0">类型化数组</h2>
<p>类型化数组是与数组非常相似的对象，但是它提供了一种将原始二进制数据写入内存缓冲区的机制。所有主要浏览器均很好地支持此功能，并且 ES6 已将其集成到 JavaScript 核心框架中，也可以访问诸如 <code>map()</code>、<code>filter()</code> 等 Array 方法。我强烈建议你浏览本文结尾处提到的资源，以更深入了解类型化数组。</p>
<h3 data-id="heading-1">组成</h3>
<p>类型化数组由两个主要部分组成，<code>Buffer</code> 和 <code>View</code>。</p>
<h4 data-id="heading-2">缓冲区</h4>
<p><code>Buffer</code> 是 <code>ArrayBuffer</code> 类型的对象，表示一个数据块。此原始二进制数据块无法被单独访问或修改。你可能好奇，无法访问或修改的数据对象的能有什么用途。实际上视图是缓冲区的读写接口。</p>
<h4 data-id="heading-3">视图</h4>
<p><code>View</code> 是一个对象，允许你访问和修改存储在 <code>ArrayBuffer</code> 中的原始二进制内容。一般来说有两种视图。</p>
<h4 data-id="heading-4"><code>TypedArray</code> 对象的实例</h4>
<p>这些类型的对象与普通数组非常相似，但是仅存储单一类型的数值数据。诸如 <code>Int8</code>、<code>Uint8</code>、<code>Int16</code>、<code>Float32</code> 就是类型化数组的数据类型。类型中的数字表示为数据类型分配的位数。例如，<code>Int8</code> 表示 8 位的整数。</p>
<blockquote>
<p>你可以阅读 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Typed_arrays#%E7%B1%BB%E5%9E%8B%E6%95%B0%E7%BB%84%E8%A7%86%E5%9B%BE" target="_blank" rel="nofollow noopener noreferrer">参考文档</a> 来详细了解类型化数组的数据类型。</p>
</blockquote>
<h4 data-id="heading-5"><code>DataView</code> 对象的实例</h4>
<p><code>DataView</code> 是一个低级接口，提供了一个 <code>getter</code> / <code>setter</code> API 来读取和写入任意数据到缓冲区。这很大程度上方便了我们的开发，尤其是需要在单个类型化数组中处理多种数据类型时。</p>
<p>使用 <code>DataView</code> 的另一个好处是，它可以让你控制数据的字节序 —— 类型化数组使用平台的字节序。当然如果你的程序运行在本地，这将不是问题，因为你的设备将使用与输入数组相同的字节序。在大多数情况下，你的类型化数组将为低端字节序，因为英特尔采取的是小端字节序。由于英特尔在计算机处理器中非常普遍，因此大多数时候不会出现问题。但是，如果将小端字节序编码的数据传输到使用大端字节序编码的设备，则会导致读取时候的错误，最终可能导致数据的丢失。由于 <code>DataView</code> 使你可以控制字节序的方向，因此你可以在必要时使用它。</p>
<h2 data-id="heading-6">是什么使它们与普通数组不同</h2>
<p>如前所述，普通的 JavaScript 数组已通过 JavaScript 引擎进行了优化，你没必要为了提升性能而使用类型化数组，因为这不会给你带来太多升级。但是有些特性使类型化数组不同于普通数组，这才可能是你选择它们的原因。</p>
<ul>
<li>让你能够处理原始二进制数据</li>
<li>由于它们处理的数据类型是有限的，因此与普通数组相比，你的引擎更易优化类型化数组，因为普通数组的优化其实是一个非常复杂的过程。</li>
<li>不能保证普通数组永远都能得到优化，因为你的引擎可能因各种原因决定不进行优化。</li>
</ul>
<h2 data-id="heading-7">在 Web 开发中的用途</h2>
<h3 data-id="heading-8">XMLHttpRequest API</h3>
<p>你可以根据你的响应类型以 <code>ArrayBuffer</code> 形式接收数据响应。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
xhr.open(<span class="hljs-string">'GET'</span>, exampleUrl);
xhr.responseType = <span class="hljs-string">'arraybuffer'</span>;

xhr.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> arrayBuffer = xhr.response;
    <span class="hljs-comment">// 处理数据</span>
&#125;;

xhr.send();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">Fetch API</h3>
<p>类似于 XMLHttpRequest API，Fetch API 还允许你在 <code>ArrayBuffer</code> 中接收响应。你只需在 fetch API 响应中使用 <code>arrayBuffer()</code> 方法，你就能够收到一个使用 <code>ArrayBuffer</code> 解析的 <code>Promise</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">fetch(url)
.then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> response.arrayBuffer())
.then(<span class="hljs-function"><span class="hljs-params">arrayBuffer</span> =></span> &#123;
   <span class="hljs-comment">// 处理数据</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">HTML Canvas</h3>
<p>HTML5 Canvas 元素使你可以渲染动态的 2D 形状和位图图像。该元素仅充当图形的容器，而图形则是在 JavaScript 的帮助下绘制。</p>
<p>canvas 的 2D Context 使你可以将位图数据作为 <code>Uint8ClampedArray</code> 的实例进行检索。让我们看一下 Axel 博士提供的示例代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'my_canvas'</span>);
<span class="hljs-keyword">const</span> context = canvas.getContext(<span class="hljs-string">'2d'</span>);
<span class="hljs-keyword">const</span> imageData = context.getImageData(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, canvas.width, canvas.height);
<span class="hljs-keyword">const</span> uint8ClampedArray = imageData.data;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">WebGL</h3>
<p>WebGL 允许你渲染高性能的交互式 3D 和 2D 图形。它在很大程度上依赖于类型化数组，因为它会处理原始像素数据以在画布上输出必要的图形。</p>
<p>你可以在 <a href="https://blog.bitsrc.io/understanding-webgl-51ab81ccb48c" target="_blank" rel="nofollow noopener noreferrer">这篇文章</a> 中阅读有关 WebGL 基础的更多信息。</p>
<h3 data-id="heading-12">Web Socket</h3>
<p>Web Socket 允许你以 Blob 或数组缓冲区的形式发送和接收原始二进制数据。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> socket = <span class="hljs-keyword">new</span> WebSocket(<span class="hljs-string">"ws://localhost:8080"</span>);
socket.binaryType = <span class="hljs-string">"arraybuffer"</span>;

<span class="hljs-comment">// 监听 message</span>
socket.addEventListener(<span class="hljs-string">"message"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
    <span class="hljs-keyword">const</span> view = <span class="hljs-keyword">new</span> <span class="hljs-built_in">DataView</span>(event.data);
    <span class="hljs-comment">// 处理接收数据</span>
&#125;);

<span class="hljs-comment">// 发送二进制数据</span>
socket.addEventListener(<span class="hljs-string">'open'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
    <span class="hljs-keyword">const</span> typedArray = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint16Array</span>(<span class="hljs-number">7</span>);
    socket.send(typedArray.buffer);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尽管初学者可能不需要详细了解类型化数组，但是当你进入中高级 JavaScript 开发的时候，它们是必不可少的。这主要是因为你可能要开发需要使用类型化数组的更复杂的应用程序。</p>
<p>要深入了解类型化数组，请浏览下面附带的资源链接。</p>
<p>感谢你的阅读，祝你编程愉快！！</p>
<h2 data-id="heading-13">资源</h2>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Typed_arrays" target="_blank" rel="nofollow noopener noreferrer">JavaScript 类型化数组 - MDN 文档</a></li>
<li><a href="https://exploringjs.com/es6/ch_typed-arrays.html" target="_blank" rel="nofollow noopener noreferrer">Exploring JS by Dr. Axel</a></li>
</ul>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            