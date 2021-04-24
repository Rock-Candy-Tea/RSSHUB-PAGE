
---
title: 'WebGL 中的图片解码优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e91f1af71d24257bcc9c8eead8a1faf~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 06:25:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e91f1af71d24257bcc9c8eead8a1faf~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者 - <a href="https://github.com/gz65555" target="_blank" rel="nofollow noopener noreferrer">Oasis 团队-月木</a></p>
<p>虽然 WebGL 支持 <a href="https://zh.wikipedia.org/wiki/%E7%BA%B9%E7%90%86%E5%8E%8B%E7%BC%A9" target="_blank" rel="nofollow noopener noreferrer">压缩纹理</a>，上传 GPU 不存在解码耗时的问题，但日常应用中还是会用到 png/jpg/webp 等压缩过的图片格式。这些格式在 WebGL 中渲染需要转换成位图，即每个像素使用 RGB 或 RGBA 表示。这个过程称为<strong>图片解码</strong>。图片解码在渲染中是非常重要的一环，若直接使用 Image 对象上传(<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/WebGLRenderingContext/texImage2D" target="_blank" rel="nofollow noopener noreferrer">texImage2D</a>)至 GPU，往往耗时较长，阻塞主线程，比如说会导致动画播放卡顿，影响用户体验。所以，在这里我们对浏览器中的一些 WebGL 中图片解码的方案做了一些研究和测试。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e91f1af71d24257bcc9c8eead8a1faf~tplv-k3u1fbpfcp-zoom-1.image" alt="左.gif" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c0673756894493b2d852f047061749~tplv-k3u1fbpfcp-zoom-1.image" alt="右.gif" loading="lazy" referrerpolicy="no-referrer">
第一幅图是同步解码，第二幅图是异步解码，可以看到明显缓解动画的卡顿</p>
<p>本文重点测试的是 <a href="https://developer.mozilla.org/zh-cn/docs/Web/API/HTMLImageElement/decode" target="_blank" rel="nofollow noopener noreferrer">Image.decode</a> 方法和 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/WindowOrWorkerGlobalScope/createImageBitmap" target="_blank" rel="nofollow noopener noreferrer">createImageBitmap</a> 方法。</p>
<h2 data-id="heading-0">Image.decode</h2>
<p><code>Image.decode</code> 可以异步对 <code>Image</code> 进行解码，异步的解码不会阻塞主线程动画和交互。使用方法如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> img = <span class="hljs-keyword">new</span> Image();
img.src = <span class="hljs-string">'...'</span>;
img.decode().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">document</span>.body.appendChild(img);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">createImageBitmap</h2>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/ImageBitmap" target="_blank" rel="nofollow noopener noreferrer">ImageBitmap</a> 是专门为 Canvas 和 WebGL 渲染使用的一种数据格式。<code>createImageBitmap</code> 会异步返回一个含 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/ImageBitmap" target="_blank" rel="nofollow noopener noreferrer">ImageBitmap</a> 对象的 Promise。<code>createImageBitmap</code> 可以在 worker 中使用，ImageBitmap 也可以在 worker 之间传输。createImageBitmap 接受多种数据源，本文重点测试 Blob 和 HTMLImageElement，这两种对象在渲染引擎中最常使用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用 image 作为源</span>
createImageBitmap(image).then(<span class="hljs-function">(<span class="hljs-params">imageBitmap</span>)=></span>&#123;
  gl.texImage2D(gl.TEXTURE_2D, <span class="hljs-number">0</span>, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, imageBitmap);
&#125;)

<span class="hljs-comment">// 使用 blob 作为源</span>
createImageBitmap(blob).then(<span class="hljs-function">(<span class="hljs-params">imageBitmap</span>)=></span>&#123;
  gl.texImage2D(gl.TEXTURE_2D, <span class="hljs-number">0</span>, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, imageBitmap);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-2">性能测试</h2>
<p>上面介绍完了两个异步解码 API 的基本使用，接下去我用 5 种方式对 100 张<strong>不同</strong>的 1024 * 1024 图（图片由<a href="https://github.com/gz65555/image-decode-test/blob/main/process.js" target="_blank" rel="nofollow noopener noreferrer">脚本</a>随机生成）进行解码测试，对比图片的解码时间和纹理上传时间。五种方式如下：</p>
<ol>
<li>使用 Image 作为源用 createImageBitmap 方法。（<a href="https://github.com/gz65555/image-decode-test/blob/main/image-bitmap-upload.html" target="_blank" rel="nofollow noopener noreferrer">示例</a>）</li>
<li>使用 Blob 作为源使用 createImageBitmap 。（<a href="https://github.com/gz65555/image-decode-test/blob/main/bitmap-blob.html" target="_blank" rel="nofollow noopener noreferrer">示例</a>）</li>
<li>开启 5 个 worker 使用 createImageBitmap 方法。（<a href="https://github.com/gz65555/image-decode-test/blob/main/bitmap-decode-worker.html" target="_blank" rel="nofollow noopener noreferrer">示例</a>）</li>
<li>使用 image.decode 进行解码。（<a href="https://github.com/gz65555/image-decode-test/blob/main/image-upload-decode.html" target="_blank" rel="nofollow noopener noreferrer">示例</a>）</li>
<li>使用 image 直接上传纹理。（<a href="https://github.com/gz65555/image-decode-test/blob/main/image-upload.html" target="_blank" rel="nofollow noopener noreferrer">示例</a>）</li>
</ol>
<p>进过上面几项测试得出结果（上下浮动 100ms 左右）：</p>
<h4 data-id="heading-3">1. MacOS（2.6 GHz i7 chrome 87 降低 6 倍性能)</h4>















































<table><thead><tr><th>使用方法</th><th>解码时间(毫秒)</th><th>纹理上传时间(毫秒)</th><th>总时间</th><th>备注</th></tr></thead><tbody><tr><td>createImageBitmap(Image)</td><td>2625</td><td>2967</td><td>5592</td><td>异步解码</td></tr><tr><td>createImageBitmap(Blob)</td><td>559</td><td>2180</td><td>2739</td><td>异步解码</td></tr><tr><td>createImageBitmap(Blob) + worker</td><td>210</td><td>2000</td><td>2210</td><td>异步 + 多线程解码</td></tr><tr><td>image 直接上传</td><td></td><td>3020</td><td>3020</td><td>同步解码</td></tr><tr><td>image.decode 后上传</td><td>210</td><td>4978</td><td>5188</td><td>异步解码</td></tr></tbody></table>
<h4 data-id="heading-4">2. Android U4（Mi 10 Pro U4 3.21.0.172）</h4>















































<table><thead><tr><th>使用方法</th><th>解码时间(毫秒)</th><th>纹理上传时间(毫秒)</th><th>总时间</th><th>备注</th></tr></thead><tbody><tr><td>createImageBitmap(Image)</td><td>1540</td><td>878</td><td>2418</td><td>异步解码</td></tr><tr><td>createImageBitmap(Blob)</td><td>1096</td><td>129</td><td>1225</td><td>异步解码</td></tr><tr><td>createImageBitmap(Blob) + worker</td><td>715</td><td>142</td><td>857</td><td>异步 + 多线程解码</td></tr><tr><td>image 直接上传</td><td></td><td>905</td><td>905</td><td>同步解码</td></tr><tr><td><del>image.decode 后上传</del></td><td></td><td></td><td>decode 报错，The source image cannot be decoded.</td><td>异步解码</td></tr></tbody></table>
<h4 data-id="heading-5">3. Android Chrome（Mi 10 Pro Android Chrome 87）</h4>















































<table><thead><tr><th>使用方法</th><th>解码时间(毫秒)</th><th>纹理上传时间(毫秒)</th><th>总时间</th><th>备注</th></tr></thead><tbody><tr><td>createImageBitmap(Image)</td><td>522</td><td>504</td><td>1026</td><td>异步解码</td></tr><tr><td>createImageBitmap(Blob)</td><td>310</td><td>135</td><td>445</td><td>异步解码</td></tr><tr><td>createImageBitmap(Blob) + worker</td><td>249</td><td>145</td><td>394</td><td>异步 + 多线程解码</td></tr><tr><td>image 直接上传</td><td></td><td>510</td><td>510</td><td>同步解码</td></tr><tr><td><del>image.decode 后上传</del></td><td></td><td></td><td>decode 报错，The source image cannot be decoded.</td><td>异步解码</td></tr></tbody></table>
<h4 data-id="heading-6">4. iOS safari（iPhone7 iOS 14.2）</h4>















































<table><thead><tr><th>使用方法</th><th>解码时间(毫秒)</th><th>纹理上传时间(毫秒)</th><th>总时间</th><th>备注</th></tr></thead><tbody><tr><td><del>createImageBitmap(Image)</del></td><td></td><td></td><td>不支持</td><td></td></tr><tr><td><del>createImageBitmap(Blob)</del></td><td></td><td></td><td>不支持</td><td></td></tr><tr><td><del>createImageBitmap(Blob) + worker</del></td><td></td><td></td><td>不支持</td><td></td></tr><tr><td>image 直接上传</td><td></td><td>1076</td><td>1076</td><td>同步解码</td></tr><tr><td>image.decode 后上传</td><td>2076</td><td>300</td><td>2376</td><td>异步解码</td></tr></tbody></table>
<h2 data-id="heading-7">结论</h2>
<p>通过以上测试，可以得出以下结论：</p>
<ol>
<li>Android 和 Mac Chrome 推荐用 <code>createImageBitmap</code>，数据源务必使用 <code>Blob</code>，解码可以提升 10% 左右的性能：
<ol>
<li>若数据源使用 <code>Blob</code>，无解码时间；若数据源使用 <code>Image</code>，有两次时间消耗，首先创建 bitmap 耗时很长，其次在 performance 里查看仍有解码时间（预期不该有解码时间，这是 Chrome 的 Bug，已经给 chromium 提了一个 <a href="https://bugs.chromium.org/p/chromium/issues/detail?id=1164969" target="_blank" rel="nofollow noopener noreferrer">issue</a>，chrome 官方已经确认问题存在）。</li>
<li>在 worker 中调用 <code>createImageBitmap</code> 可以利用多线程能力，能进一步提升 15% 左右的性能。因为 worker 线程还不算特别稳定，是否开启 worker 解码交由用户配置决定，用户根据当前 cpu 负载及所需解码数量和业务场景去决定是否使用 worker 解码。</li>
</ol>
</li>
<li>iOS  不要用任何异步解码方案：
<ol>
<li>不支持 <code>createImageBitmap</code>；</li>
<li>使用 <code>Image.decode</code> 的总时间是同步解码的两倍；</li>
</ol>
</li>
</ol>
<p>根据上面测试的结果以及推导的结论，在 WebGL 中采取的图片请求最佳解码方案是：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ace798caf924944beaef85f1670bf39~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上方案即将应用到 oasis-engine 中，欢迎大家在 <a href="https://github.com/oasis-engine/engine/pull/249" target="_blank" rel="nofollow noopener noreferrer">PR</a> 中讨论。</p></div>  
</div>
            