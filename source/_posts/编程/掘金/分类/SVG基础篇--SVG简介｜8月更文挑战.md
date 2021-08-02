
---
title: 'SVG基础篇--SVG简介｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/377dbfd72c044ef88e8f586b57cc512d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 03:29:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/377dbfd72c044ef88e8f586b57cc512d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>"不畏惧，不将就，未来的日子好好努力"——大家好！我是小芝麻😄</p>
</blockquote>
<p>攒了多年的草稿箱，本打算完善之后一篇发布，但为了参加活动，也只能一点一点发布了，没办法才疏学浅，新创作肯定是来不及了，为了赶上进度，只能出此下策了😂</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/377dbfd72c044ef88e8f586b57cc512d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、SVG简介</h2>
<h3 data-id="heading-1">1、什么是SVG</h3>
<blockquote>
<p><code>SVG</code> 全称 <code>Scalable Vector Graphics</code> (可缩放矢量图形)。它是一种用来描述二维矢量图形的 <code>XML</code> 标记语言。</p>
</blockquote>
<ul>
<li>SVG 指可伸缩矢量图形 (Scalable Vector Graphics)</li>
<li>SVG 用来定义用于网络的基于矢量的图形</li>
<li>SVG 使用 XML 格式定义图形</li>
<li>SVG 图像在放大或改变尺寸的情况下其图形质量不会有所损失</li>
<li>SVG 是万维网联盟的标准</li>
<li>SVG 与诸如 DOM 和 XSL 之类的 W3C 标准是一个整体</li>
</ul>
<h3 data-id="heading-2">2、特点及优势</h3>
<p>与其他图像格式相比，使用 SVG 的优势在于：</p>
<ul>
<li>SVG 可被非常多的工具读取和修改（比如记事本）</li>
<li>SVG 与 JPEG 和 GIF 图像比起来，尺寸更小，且可压缩性更强。</li>
<li>SVG 图像可在任何的分辨率下被高质量地打印</li>
<li>SVG 可在图像质量不下降的情况下被放大</li>
<li>SVG 图像中的文本是可选的，同时也是可搜索的（很适合制作地图）</li>
<li>SVG 是开放的标准</li>
<li>SVG 文件是纯粹的 XML</li>
</ul>
<h3 data-id="heading-3">3、浏览器兼容</h3>
<p>支持 chrome、Safari、foxfire1.5、Opera9、ie9 及以上浏览器，但是SVG SMIL动画 IE浏览器(包括IE11)整体不支持（对于移动端来说，基本支持）</p>
<h2 data-id="heading-4">二、SVG的使用方式</h2>
<p>对于直接支持SVG的浏览器，SVG主要采用两面两种呈现的方式。</p>
<h3 data-id="heading-5">1、内联到HTML</h3>
<p>SVG是标准的HTML元素，直接写到HTML中就可以了，像下面这样：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span> <span class="hljs-attr">version</span>=<span class="hljs-string">"1.1"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100%"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100%"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"red"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"black"</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"50%"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"50%"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"yellow"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">'dominant-baseline:middle;text-anchor:middle;font-size:36px'</span>></span>Hello world<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77c2f37110254e58ae1969cec9dcce07~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">2、独立SVG文件</h3>
<blockquote>
<p>独立SVG指的是通过使用svg文件扩展名来提供向量图形文件格式。如下格式：</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfa3f07368ea4dcfb96dc70f559d3aed~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>1、在浏览器直接打开</li>
<li>2、在HTML中使用 <img> 标签引入</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./1.svg"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3、作为 CSS 背景使用</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'./1.svg'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>4、使用 <embed> <object> <iframe>  引入</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">embed</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"1.svg"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"image/svg+xml"</span>
    <span class="hljs-attr">pluginspage</span>=<span class="hljs-string">"http://www.adobe.com/svg/viewer/install/"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>embed 优势：所有主要浏览器都支持，并允许使用脚本</li>
<li>embed 缺点：不推荐在HTML4和XHTML中使用（但在HTML5允许）</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-tag"><<span class="hljs-name">object</span> <span class="hljs-attr">data</span>=<span class="hljs-string">"1.svg"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"image/svg+xml"</span>
  <span class="hljs-attr">codebase</span>=<span class="hljs-string">"http://www.adobe.com/svg/viewer/install/"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>object 优势：所有主要浏览器都支持，并支持HTML4，XHTML和HTML5标准</li>
<li>object 缺点：不允许使用脚本。</li>
</ul>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">iframe</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"1.svg"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span><span class="hljs-tag"></<span class="hljs-name">iframe</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>iframe 优势：所有主要浏览器都支持，并允许使用脚本</li>
<li>iframe 缺点：不推荐在HTML4和XHTML中使用（但在HTML5允许）</li>
</ul>
<h2 data-id="heading-7">三、SVG的渲染</h2>
<h3 data-id="heading-8">1、渲染顺序</h3>
<p>SVG是严格按照定义元素的顺序来渲染的，这个与HTML靠z-index值来控制分层不一样。</p>
<p>在SVG中，写在前面的元素先被渲染，写在后面的元素后被渲染。后续元素被绘制在先前绘制的元素之上。=> “后来居上”</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"outline: 2px solid red;"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"150"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"150"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"yellow"</span>/></span>
  <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"red"</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67fe64258b584839aaf2225cd43e0c8c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">2、渲染步骤</h3>
<p>渲染单个图形元素时: (组的渲染同理)</p>
<ul>
<li>1、创建一个透明黑色的临时画布</li>
<li>2、将元素绘制到该临时画布上</li>
<li>3、应用相应的滤镜效果</li>
<li>4、设置相应的剪裁、遮罩、不透明度效果</li>
<li>5、将修改后的临时画布组合到背景中</li>
</ul>
<h3 data-id="heading-10">3、支持渲染的三种图像类型</h3>
<p>SVG 支持三种基本的图像元素：矢量图形、文字、点阵图像。</p>
<ul>
<li>矢量图形：指直线曲线色块的组合；</li>
<li>文字：指文本方式的字符</li>
<li>点阵图像：指一个矩形区域像素点颜色值的描述块，表现为一个二维数组。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7564d45c945a42a8abd606872425cf0d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下一篇《SVG坐标系简介》我们再见</p>
<h2 data-id="heading-11">参考文献</h2>
<ul>
<li>[1] <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fpingfan1990%2Fp%2F4757934.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/pingfan1990/p/4757934.html" ref="nofollow noopener noreferrer">SVG学习笔录（一）</a></li>
<li>[2] <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3school.com.cn%2Fsvg%2Fsvg_inhtml.asp" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3school.com.cn/svg/svg_inhtml.asp" ref="nofollow noopener noreferrer">w3school</a></li>
</ul></div>  
</div>
            