
---
title: '【CSS基础】背景图片定位'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b9052f319674e27874f927a41142b29~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 18:02:23 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b9052f319674e27874f927a41142b29~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第31天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>作者：<a href="https://juejin.cn/user/3677241439685368" target="_blank" title="https://juejin.cn/user/3677241439685368">battleKing</a><br>
仓库：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdreamgo88" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dreamgo88" ref="nofollow noopener noreferrer">Github</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2FCyber970801" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/Cyber970801" ref="nofollow noopener noreferrer">CodePen</a><br>
博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_44361450%3Fspm%3D1000.2115.3001.5343" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_44361450?spm=1000.2115.3001.5343" ref="nofollow noopener noreferrer">CSDN</a>、<a href="https://juejin.cn/user/3677241439685368" target="_blank" title="https://juejin.cn/user/3677241439685368">掘金</a><br>
反馈邮箱：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmail.qq.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://mail.qq.com/" ref="nofollow noopener noreferrer">myh19970701@foxmail.com</a><br>
特别声明：原创不易，未经授权不得转载或抄袭，如需转载可联系笔者授权</p>
</blockquote>
<h2 data-id="heading-0">背景</h2>
<p>在学习 <code>CSS</code> 的过程中，大家肯定会遇到一个背景图片不知道 <code>如何快速定位</code> 的问题，但是大部分基础的 CSS 教程并没有提及如何解决这个问题，所以今天我们就通过这一篇文章快速解决这一问题。</p>
<h2 data-id="heading-1">相关知识</h2>
<p>首先我们先来介绍一下 <code>哪些 CSS 属性</code> 与 <code>背景图片</code> 密切相关。</p>
<h3 data-id="heading-2">1. background-image 属性</h3>
<p><code>background-image</code> 属性是用来引入背景图片的。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'https://lf3-cdn-tos.bytescm.com/obj/static/xitu_juejin_web/6bdafd801c878b10edb5fed5d00969e9.svg'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2. background-repeat 属性</h3>
<p><code>background-repeat</code> 属性是规定如何重复背景图像，一般设置为 <code>no-repeat</code> 。</p>
<ul>
<li>可选值</li>
</ul>

























<table><thead><tr><th>值</th><th>描述</th></tr></thead><tbody><tr><td><code>repeat</code></td><td>默认。背景图像将在垂直方向和水平方向重复。</td></tr><tr><td><code>repeat-x</code></td><td>背景图像将在水平方向重复。</td></tr><tr><td><code>repeat-y</code></td><td>背景图像将在垂直方向重复。</td></tr><tr><td><code>no-repeat</code></td><td>背景图像将仅显示一次。</td></tr></tbody></table>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">background-repeat</span>: no-repeat;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3. background-size 属性</h3>
<p><code>background-size</code> 属性规定背景图片的尺寸</p>
<ul>
<li>可选值</li>
</ul>

























<table><thead><tr><th>值</th><th>描述</th></tr></thead><tbody><tr><td><em>length</em></td><td>设置背景图像的高度和宽度。第一个值设置宽度，第二个值设置高度。如果只设置一个值，则第二个值会被设置为 "auto"。</td></tr><tr><td><em>percentage</em></td><td>以父元素的百分比来设置背景图像的宽度和高度。第一个值设置宽度，第二个值设置高度。如果只设置一个值，则第二个值会被设置为 "auto"。</td></tr><tr><td>cover</td><td>把背景图像扩展至足够大，以使背景图像完全覆盖背景区域。背景图像的某些部分也许无法显示在背景定位区域中。</td></tr><tr><td>contain</td><td>把图像图像扩展至最大尺寸，以使其宽度和高度完全适应内容区域。</td></tr></tbody></table>
<h3 data-id="heading-5">3. background-position 属性</h3>
<p><code>background-position</code> 属性规定背景图像的位置</p>
<p><code>background-position</code> 属性的三个属性值对应的就是背景图片定位的三种方法</p>
<ol>
<li>
<p>关键字：<code>background-position: top right bottom left;</code></p>
</li>
<li>
<p>像素：<code>background-position: 0px 0px;</code></p>
</li>
<li>
<p>百分比：<code>background-position: 0% 0%;</code></p>
</li>
</ol>
<h2 data-id="heading-6">关键字</h2>
<p><code>background-position</code> 后面的 top、right、bottom、left 表示的都是背景图片紧贴容器某条边。</p>
<blockquote>
<p>最常见的是<code>background-position: top left;</code> 表示背景图片定位在容器的左上角</p>
</blockquote>
<h2 data-id="heading-7">像素</h2>
<p><code>background-position</code> 后面的第一个 px 表示背景图片相对于容器左上角的水平方向偏移量，第二个 px 表示背景图片相对于容器左上角的竖直方向偏移量。</p>
<blockquote>
<p>最常见的就是 <code>background-position: 0px 0px;</code> 表示背景图片定位在容器的左上角</p>
</blockquote>
<h2 data-id="heading-8">百分比</h2>
<p><code>background-position</code> 后面两个 <code>x%，y%</code> 表示背景图片本身相对于左上角水平方向偏移 <code>x%</code>，垂直方向偏移 <code>y%</code> 的点与背景图片的容器相对于左上角水平方向偏移 <code>x%</code>，垂直方向偏移 <code>y%</code> 的点重合对齐</p>
<blockquote>
<p>假设 <code>background-position: 20% 20%;</code></p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b9052f319674e27874f927a41142b29~tplv-k3u1fbpfcp-watermark.image" alt="图片定位.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">总结</h2>
<ol>
<li><code>background-position: 0px 0px;</code> 并不能根据窗口大小自适应。</li>
<li><code>background-position: top left</code> 和 <code>background-position: x% y%</code> 的优势是背景图片可以根据窗口的大小，自动适应。</li>
<li>所以我们应该 <code>根据具体情况来选择哪一种方式</code> 来定位图片。</li>
</ol>
<h2 data-id="heading-10">❤️ 感谢大家</h2>
<p><strong>如果本文对你有帮助，就点个赞支持下吧，你的「赞」是我创作的动力。</strong></p>
<blockquote>
<p>如果你喜欢这篇文章的话，可以「点赞」 + 「收藏」 + 「转发」 给更多朋友。</p>
</blockquote></div>  
</div>
            