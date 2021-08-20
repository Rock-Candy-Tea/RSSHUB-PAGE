
---
title: '纯CSS绘制弯曲曲线图形'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f92fcae5d804bbb9cc3ed6ac934276e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 03:12:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f92fcae5d804bbb9cc3ed6ac934276e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h2 data-id="heading-0">问题起源</h2>
<p>就在昨天，我们通过文章<a href="https://juejin.cn/post/6997722260815478814" target="_blank" title="https://juejin.cn/post/6997722260815478814">纯CSS绘制五角星</a>简单介绍了CSS中的一个截取属性值：<code>clip-path</code>可以按照指定的方式截取指定形状的图形，并且介绍了<code>clip-path</code>的两种取值：</p>
<ol>
<li>
<p>按照盒模型取值：<code>margin-box</code>，<code>border-box</code>等</p>
</li>
<li>
<p>取函数，如<code>polygon</code>多边形函数，我们了解到可以通过如下方式绘制，或者说截取一个多边形：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">clip-path</span>: <span class="hljs-built_in">polygon</span>(x1 y1, x2 y2, x3 y3, ....)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>那么，<code>clip-path</code>还有哪些精妙的取值来绘制图形呢？</p>
<p>今天我们来认识一下其他函数。</p>
<h2 data-id="heading-1">inset</h2>
<p>改函数定义为截取一个矩形，4个参数分别表示距离外层盒模型的上、右、下、左边界的偏移量。类似<code>margin</code>、<code>padding</code>，也可以通过1,2,4个值来设定4个偏移量。（刚知道这种简略写法被称为：边际速记语法）。</p>
<p>如下所示，第二行类似<code>border-radius</code>，设置截图图形的4角的弧度。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">clip-path</span>: <span class="hljs-built_in">inset</span>(<span class="hljs-number">22%</span> <span class="hljs-number">12%</span> <span class="hljs-number">15px</span> <span class="hljs-number">30px</span>);
<span class="hljs-attribute">clip-path</span>: <span class="hljs-built_in">inset</span>(<span class="hljs-number">22%</span> <span class="hljs-number">12%</span> <span class="hljs-number">15px</span> <span class="hljs-number">30px</span> round <span class="hljs-number">6px</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如图所示：</p>
<p>完整图形：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f92fcae5d804bbb9cc3ed6ac934276e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>截图代码：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">clip-path</span>: <span class="hljs-built_in">inset</span>(<span class="hljs-number">10%</span> <span class="hljs-number">20%</span> <span class="hljs-number">20%</span> <span class="hljs-number">20%</span> round <span class="hljs-number">280px</span> <span class="hljs-number">10px</span> <span class="hljs-number">10px</span> <span class="hljs-number">280px</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>截图效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ada73a0ce8a42bc9b826c5450949b4e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">circle</h2>
<p>见字知意，截取一个圆形图案，函数参数解释如下所示：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">clip-path</span>: <span class="hljs-built_in">circle</span>(<span class="hljs-number">6rem</span> at <span class="hljs-number">0rem</span> <span class="hljs-number">0rem</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码表示在盒模型中，以坐标<code>(0rem, 0rem)</code>的位置为圆心，已<code>6rem</code>长度为半径R，截图圆形图案。当然，这个位置截图的效果会是一个扇形。</p>
<p>仍然采用上图为原图，以下代码的截图效果：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">clip-path</span>: <span class="hljs-built_in">circle</span>(<span class="hljs-number">200px</span> at <span class="hljs-number">40%</span> <span class="hljs-number">40%</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a54a4133a5f4843a84b86366d57f5e3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">ellipse</h2>
<p>同样见字知意，绘制椭圆，其含义为：</p>
<pre><code class="hljs language-css copyable" lang="css">ellipse(x半径 y半径 as x y)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>x, y表示圆心位置。对比<code>circle</code>并不难理解。</p>
<p>代码：<code>clip-path: ellipse(200px 100px at 40% 40%);</code></p>
<p>截图效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/080701473a574cf0ace3f2b6af042160~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">遗留了一个未解决的问题</h2>
<p>一个图形能否使用两个<code>clip-path</code>截图函数呢？</p>
<p>比如我对完整图形先使用<code>circle</code>截图，如何再对截图后的图案再次进行截图，CSS允许这样做吗？</p></div>  
</div>
            