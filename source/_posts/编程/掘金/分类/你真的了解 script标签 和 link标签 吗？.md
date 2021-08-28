
---
title: '你真的了解 script标签 和 link标签 吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1246'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 06:48:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=1246'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><script>标签</h2>
<blockquote>
<p><code>script</code>元素最简单用法就是通过直接在页面嵌入 JS 代码或者通过加载外部脚本文件。而且大家都知道浏览器解析文档时遇到<code>script</code>会依次等代码下载、执行完以后才会继续解析，因此现在Web应用程序一般都会把引用的JS代码放在<code><body></code>元素的后面。</p>
</blockquote>
<p>所以在<code>HTML规范</code>中为了解决这个引入顺序问题，在<code>script</code>标签上提供了<code>async</code>和<code>defer</code>这两个属性，使得文档解析到<code>script</code>时不会发生阻塞。</p>
<h3 data-id="heading-1">defer 延迟脚本</h3>
<p>加入defer属性后，即使把<code><script></code>标签放入<code><head></code>也不会阻塞后面DOM的解析，而且脚本会延迟到整个DOM解析完后在去执行。也就是<code><script></code>标签加入defer属性会告诉<code>浏览器立即下载脚本，但是延迟执行脚本</code>。</p>
<p>先看测试用例：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f8d007f37b84c0da18cd2f604741bd7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Chrome加载面板分析：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d3d6770ee347b2b2f62976817b9aa6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1、可以看到主进程的<code>Parse HTML</code>并不会受<code><script></code>标签影响，网络进程还是会立即去加载脚本资源。<br>
2、多个设置了<code>defer属性 的 script</code>标签，会按照顺序执行这些<code><script></code>的内容。<br>
3、会在HTML解析完毕后，<code>DOMContentLoaded</code>事件调用前执行。</strong></p>
<p>最终打印测试验证：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e276edc07a044608da722e9d26c0824~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">async 异步脚本</h3>
<p><code><script></code>标签加入async属性会告诉<code>浏览器立即下载脚本，哪个脚本先加载完就先执行，而且是加载完就立马执行</code>。如果有DOM正在解析，会阻塞解析。</p>
<p>测试用例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6638241275594745809ab4e2b8ee0579~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Chrome加载面板分析：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/188c9b81c9bd4f2ba05d8761419a4477~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1、DOMContentLoaded<code>事件的触发并不受</code>async<code>脚本加载的影响，</code>async<code>脚本会在</code>load`事件调用前执行。</strong></p>
<p><strong>2、这里文档解析太快没体现出来，其实<code>DOMContentLoaded</code>事件调用跟<code>async</code>脚本执行顺序是不定的。</strong></p>
<p>打印测试验证：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89b7a3064315433e8e7d8b9a196ea560~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3"><link>标签</h2>
<h3 data-id="heading-4">prefetch</h3>
<p>prefetch是一种浏览器机制，利用浏览器空闲时间来下载后续可能需要使用的资源。<code>在浏览器完成当前页面的加载后开始静默地拉取指定的文档并将其存储在缓存中。</code></p>
<p>使用方式：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"prefetch"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"xxx"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试用例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67aed123739348e8b89f7280305aa3d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Chrome Network面板分析：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73b07ee0d57a4d4e9b3268d01fdc25b3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>可以看到<code>link prefetch</code>出现了coffee.jpg的加载请求。后续通过<code>img src</code>再次请求coffee.jpg时，直接就通过<code>prefetch cache</code>获取了</strong>。所以验证了浏览器在空闲时间预先加载资源，真正使用时直接从浏览器缓存中快速获取。</p>
<h3 data-id="heading-5">preload</h3>
<p>顾名思义，preload就是希望浏览器尽早的请求资源，且不阻塞正常的onload。</p>
<p>使用方式：</p>
<pre><code class="copyable"><link rel="preload" href="xxx" as="xxx"/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试用例：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03c62177ff59429685f62d696e6123c6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Chrome Network面板分析：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9e7dd7b75474fd09526af1487ba5671~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>可以发现脚本的加载时机提前了，在浏览器开始解析html后很快就进行了加载。</strong></p>
<blockquote>
<p>注意：preload link必须设置as属性来声明资源的类型（font/image/style/script等)，否则浏览器可能无法正确加载资源。<code>对于字体文件或者可以加载的跨域资源需要加上crossorigin属性。</code></p>
</blockquote></div>  
</div>
            