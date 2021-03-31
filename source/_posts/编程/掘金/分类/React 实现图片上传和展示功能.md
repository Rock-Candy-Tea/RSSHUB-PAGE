
---
title: 'React 实现图片上传和展示功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc74599c1f904c119a915ece59349e6c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 30 Mar 2021 23:26:32 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc74599c1f904c119a915ece59349e6c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">基本介绍 📝</h2>
<ul>
<li>最近完成了产品提出的一个类似微信发图文朋友圈的需求（以下实现均基于 React + mobx 项目）：
<ul>
<li>1⃣️ 通过➕号按钮选择系统图片，最多可选择9张图，选择的图片以九宫格形式展示</li>
<li>2⃣️ 选择图片后开始上传，图片大小限制为 20 MB，超过限制不上传且不展示</li>
<li>3⃣️ 展示图片上传过程中的 loading 状态</li>
<li>4⃣️ 图片上传失败可点重试按钮重新上传</li>
<li>5⃣️ 可以删除选中的图片（若上传中删除前还需中断 xhr 请求）</li>
<li>6⃣️ 发布后的图片内容按照一定规则展示（单图片、四宫格和九宫格）</li>
</ul>
</li>
<li>历尽千辛万苦终于实现了以上的功能，具体效果如下：
<ul>
<li>上传图片页面：</li>
</ul>
<img alt="show.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc74599c1f904c119a915ece59349e6c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<ul>
<li>展示页面（单图，按照单图规则展示）：</li>
</ul>
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06df0732677f47b19a33d64143af31ab~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<ul>
<li>展示页面（四图，四宫格）：</li>
</ul>
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9b0d26c206243b3aa18313cbf8be50d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<ul>
<li>展示页面（多图，九宫格）：</li>
</ul>
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acae73f650eb4b6490cf27bd9915b6b3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
<li>该需求涉及到许多零散的知识点，遂以此文做总结记录，下面将介绍思路和具体的实现代码。</li>
</ul>
<h2 data-id="heading-1">思路分析 🤔</h2>
<h3 data-id="heading-2">选择图片</h3>
<ul>
<li>选择图片可以用设置 <code>type</code> 属性为 <code>file</code> 值的 <code>input</code> 标签：</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span> <span class="hljs-attr">accept</span>=<span class="hljs-string">"image/gif,image/jpeg,image/jpg,image/png"</span> <span class="hljs-attr">multiple</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过设置其 <code>multiple</code> 属性和 <code>accept</code> 属性可以使得 <code>input</code> 标签支持多选和仅支持选择 <code>gif</code>、<code>jpg/jpeg</code> 和 <code>png</code> 类型的文件。</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56a6173b972a4eba9c31af2042af67c4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>当点击标签时，则可以从文件系统中选择照片。我们的需求是提供一个➕号按钮作为选择图片的入口，这里可以使用 <code>ref</code> 获取该 <code>input</code> 元素，当点击➕号按钮时触发 <code>input</code> 的点击事件，即可以调用系统的相册进行图片选取。</li>
</ul>
<h3 data-id="heading-3">限制图片大小和数量、预览本地图片</h3>
<ul>
<li>当 <code>input</code> 元素的 <code>change</code> 事件被触发时，可以通过 <code>input.files</code> 获取到当前选中文件的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/FileList" target="_blank" rel="nofollow noopener noreferrer">FileList</a> 类数组对象，当选择两张图片后，打印 <code>FileList</code> 对象：
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08b5692fa797458a80b3ffb2691e39f9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
<li>可以看到每个 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/File" target="_blank" rel="nofollow noopener noreferrer">File</a> 对象都有 size 字段，可以用来判断图片大小（字节）是否超过限制（<code>20MB</code> 是<code>20 * 1024 * 1024</code>）。</li>
<li>区别于原生 APP，web 网页无法阻止用户选择超过 9 张图片，只能在代码中做限制，当总选择的图片超过 9 张则做超出数量提示和截断处理（取前 9 张图）。</li>
<li>由于可以获取到每张图片的 <code>File</code> 对象，则可以使用 <code>URL.createObjectURL()</code> 创建一个对象 URL，可以作为 <code>img</code> 标签的 <code>src</code> 值进行传入，则能实现本地图片的预览功能。</li>
<li>需要注意的是，当不再需要这些使用 <code>URL.createObjectURL()</code> 创建的 URL 对象时，每个对象必须通过调用 <code>URL.revokeObjectURL()</code> 方法来释放，让浏览器知道不用在内存中继续保留对这个文件的引用了（可设置图片的load事件处理器来释放对象URL，当图片加载完成之后对象URL就不再需要了）。
<pre><code class="hljs language-bash copyable" lang="bash">const localUrl = URL.createObjectURL(flieList[0])
// localUrl 可作为图片的源
<img src=&#123;localUrl&#125; alt=<span class="hljs-string">''</span> />

// 无需使用时释放内存
window.URL.revokeObjectURL(localUrl);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-4">上传图片和失败重试</h3>
<ul>
<li>通过前面的分析，我们可以获取到每张图片的 <code>File</code> 对象，我们就可以通过新建一个 <code>FromData</code> 对象，并将 <code>File</code> 对象添加到 <code>FromData</code> 对象中，使用 <code>XMLHttpRequest</code> 来处理无刷新上传图片。
<pre><code class="hljs language-bash copyable" lang="bash">const xhr = new XMLHttpRequest();
const formData = new FormData();
formData.append(<span class="hljs-string">'file'</span>, fileData);
xhr.open(<span class="hljs-string">'POST'</span>, UPLOAD_IMAGE_URL); // 需要后端提供上传 URL
xhr.send(formData);
xhr.onreadystatechange = () => &#123;
  <span class="hljs-keyword">if</span> (xhr.readyState === 4) &#123;
    <span class="hljs-keyword">if</span> (xhr.status === 200) &#123;
      // handle response
    
    &#125; <span class="hljs-keyword">else</span> &#123;
      // handle error
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>上传失败时则重新执行以上上传逻辑。</li>
</ul>
<h3 data-id="heading-5">图片展示</h3>
<ul>
<li>发布后的图片需要按照一定的规则展示：
<ul>
<li>单张图使用<a target="_blank" href="https://zhuanlan.zhihu.com/p/24805757" rel="nofollow noopener noreferrer">微信朋友圈图片的显示规则</a>，需要获取图片原本的宽高，因此需要后端在上传图片完成后返回图片的原始宽高。</li>
<li>四张图时使用四宫格</li>
<li>其他数量的图片以九宫格形式展示</li>
</ul>
</li>
<li>为了使得图片在保持其宽高比的同时填充 <code>img</code> 元素的整个内容框，我们通过可以设置 <code>img</code> 元素的 <a target="_blank" href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/object-fit" rel="nofollow noopener noreferrer">object-fit</a> CSS 属性值为 <code>cover</code> 来实现。</li>
<li>下面将介绍整个图片上传和展示功能的具体实现代码。</li>
</ul>
<h2 data-id="heading-6">具体实现 🧐</h2>
<h3 data-id="heading-7">上传图片页面相关组件</h3>
<ul>
<li>
<p>这部分将实现创建页的上传图片组件，当添加图片张数少于9张时展示➕号按钮，图片添加后开始上传图片，图片上传过程中展示 loading 状态，添加的图片可以被删除，即效果如下：
<img alt="show.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc74599c1f904c119a915ece59349e6c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>首先是 <code>UploadImage</code> 组件，代码如下：
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b575ba6ea4f4321ac077495a283c817~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc6cabe6b9ad4e069e182fad14a762eb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p><code>UploadImage</code> 组件中使用了 <code>ImageItem</code> 子组件，封装了上传、删除、重试逻辑，相关代码如下：
<img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc11f8557bfe4a86ad6846b7bd691119~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>样式文件代码如下：
<img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14fe641d9f294fcfb83d3ea4fe757158~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>可以看到，在使用 <code>UploadImage</code> 组件时需要传入 <code>imageList</code> 和及其更新方法 <code>updateImageList</code>。接下来我们看使用 <code>updateImageList</code> 组件的最外层组件 <code>PostEditorView</code> 的相关代码：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c65e86c9a3dd44a8b0aeb175dc2f163b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>上面的代码可以看到，可以写一些自定义 <code>hooks</code> 来减小 <code>PostEditorView</code> 组件的大小：</p>
<ul>
<li><code>useConfirmModal</code> 封装提交内容时的弹框逻辑</li>
<li><code>useAlertModal</code> 封装图片上传失败时的弹框逻辑</li>
<li><code>useUploadInput</code> 封装选择图片相关逻辑</li>
</ul>
</li>
<li>
<p>至此，上传图片页面相关组件的代码均已展示完成，建议结合思路阅读相关代码，仅提供思路，部分无关代码已删除。</p>
</li>
</ul>
<h3 data-id="heading-8">展示图片页面组件</h3>
<ul>
<li>
<p>这部分将实现内容页的展示图片组件。<code>BlogImageList</code> 组件相关代码如下：
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae152cf9b9834193b00ba1c8a6c577a8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>样式文件代码如下：
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abc81b48f1b047dfba89a9cd6fc7ba6e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>在展示页面，只需要将带图片id、原始宽高的图片列表传给组件即可。</p>
</li>
<li>
<p>PS：单张图使用<a target="_blank" href="https://zhuanlan.zhihu.com/p/24805757" rel="nofollow noopener noreferrer">微信朋友圈图片的显示规则</a>，如下图所示，假设图片宽高比 X，当图片 1:1 时显示的尺寸为 Y * Y（在项目中 Y = 180，L = 4）：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/111951d452ab42399118e68e5cd5884a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h2 data-id="heading-9">总结 👀</h2>
<ul>
<li>本文主要整理了在 React 项目实现图片上传和展示功能的相关思路和代码，涉及到使用 <code>input[type=file]</code> 标签来唤起系统选择图片功能，使用 <code>URL.createObjectURL()</code> 对 File 对象进行处理实现本地图片预览，以及使用 <code>xhr</code> 实现无刷新图片上传等知识点。</li>
</ul>
<blockquote>
<p>以上内容如有遗漏错误，欢迎留言 ✍️指出，一起进步💪💪💪</p>
</blockquote>
<blockquote>
<p>如果觉得本文对你有帮助，🏀🏀留下你宝贵的 👍</p>
</blockquote>
<h2 data-id="heading-10">参考资料</h2>
<ol>
<li><a target="_blank" href="https://www.cnblogs.com/yugege/p/11756915.html" rel="nofollow noopener noreferrer">前端图片上传那些事儿</a></li>
<li><a target="_blank" href="https://developer.mozilla.org/zh-CN/docs/Web/API/File/Using_files_from_web_applications#example.3a_using_object_urls_to_display_images" rel="nofollow noopener noreferrer">在web应用程序中使用文件</a></li>
<li><a target="_blank" href="https://developer.mozilla.org/zh-CN/docs/Web/API/URL/createObjectURL" rel="nofollow noopener noreferrer">MDN - URL.createObjectURL()</a></li>
<li><a target="_blank" href="https://zhuanlan.zhihu.com/p/24805757" rel="nofollow noopener noreferrer">微信朋友圈图片的显示规则</a></li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            