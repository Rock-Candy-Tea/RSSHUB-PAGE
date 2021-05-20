
---
title: '【夯实基础--CSS】=＞ 盒子模型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/025b110674894034bfa3efe1d267d556~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 18 May 2021 21:40:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/025b110674894034bfa3efe1d267d556~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>其实，CSS就三个大模块：  <code>盒子模型 、 浮动 、 定位</code>，其余的都是细节。这三部分，<code>无论如何也要学的非常精通。</code></p>
<p>所谓盒子模型就是把HTML页面中的元素看作是一个矩形的盒子，也就是一个盛装内容的容器。</p>
<p>每个矩形都由元素的<code>内容(content)、内边距（padding）、边框（border）和外边距（margin）</code>组成。</p>
<h2 data-id="heading-1">盒子模型</h2>
<p><strong>网页布局的本质</strong></p>
<ul>
<li>首先利用CSS设置好盒子的大小，然后摆放盒子的位置。</li>
<li>最后把网页元素比如文字图片等等，放入盒子里面。</li>
</ul>
<h3 data-id="heading-2">1. 盒子模型(Box Model)</h3>
<ul>
<li>盒子模型就是把HTML页面中的布局元素看作是一个矩形的盒子，也就是一个盛装内容的容器。</li>
<li>盒子模型由<code>元素的内容、边框（border）、内边距（padding）、和外边距（margin）</code>组成。</li>
<li>盒子里面的文字和图片等元素是 内容区域</li>
<li>盒子的<code>厚度</code> 我们称为为盒子的<code>边框</code></li>
<li>盒子内容与边框的距离是内边距</li>
<li>盒子与盒子之间的距离是外边距</li>
</ul>
<p>所有的文档元素（标签）都会生成一个矩形框，我们成为元素框（element box），它描述了一个文档元素再网页布局汇总所占的位置大小。因此，<code>每个盒子除了有自己大小和位置外，还影响着其他盒子的大小和位置</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/025b110674894034bfa3efe1d267d556~tplv-k3u1fbpfcp-zoom-1.image" alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-h4RRj33t-1620959107048)(盒子模型.assets/image-20210514102348298.png)]" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>W3c标准盒子模型</strong></p>
<p>标准 w3c 盒子模型的范围包括<code> margin、border、padding、content</code></p>
<p>当设置为box-sizing: content-box;时，将采用标准模式解析计算，也是默认模式；</p>
<pre><code class="copyable">内盒尺寸计算(元素实际大小)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>宽度：Element Height = content height + padding + border （Height为内容高度）</code></li>
<li><code>高度：Element  Width = content width + padding + border （Width为内容宽度）</code></li>
<li>盒子的实际大小：<strong>内容的宽度和高度 +  内边距  +  边框</strong></li>
</ul>
<p>注意：</p>
<p>1、宽度属性width和高度属性height仅适用于块级元素，对行内元素无效（ img 标签和 input除外）。</p>
<p>2、计算盒子模型的总高度时，还应考虑上下两个盒子垂直外边距合并的情况。</p>
<p>3、<strong>如果一个盒子没有给定宽度/高度或者继承父亲的宽度/高度，则padding 不会影响本盒子大小</strong>。</p>
<p>IE 盒子模型的 content 部分包含了 border 和 pading</p>
<p>当设置为box-sizing: border-box时，将采用怪异模式解析计算；</p>
<h3 data-id="heading-3">2. 盒子边框(border)</h3>





















<table><thead><tr><th align="left">属性</th><th align="center">作用</th></tr></thead><tbody><tr><td align="left">border-width</td><td align="center">定义边框粗细，单位是px</td></tr><tr><td align="left">border-style</td><td align="center">边框的样式</td></tr><tr><td align="left">border-color</td><td align="center">边框颜色</td></tr></tbody></table>
<p><strong>边框的样式：</strong></p>
<ul>
<li>none：没有边框即忽略所有边框的宽度（默认值）</li>
<li>solid：边框为单实线(最为常用的)</li>
<li>dashed：边框为虚线</li>
<li>dotted：边框为点线</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css">边框综合设置
<span class="hljs-attribute">border</span> : border-width || border-style || border-color 

border: <span class="hljs-number">1px</span> solid red;  没有顺序要求  
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>盒子边框写法总结表：</strong></p>
<p>很多情况下，我们不需要指定4个边框，我们是可以单独给4个边框分别指定的。</p>



































<table><thead><tr><th align="left">上边框</th><th align="left">下边框</th><th align="left">左边框</th><th align="left">右边框</th></tr></thead><tbody><tr><td align="left">border-top-style:样式;</td><td align="left">border-bottom-style:样式;</td><td align="left">border-left-style:样式;</td><td align="left">border-right-style:样式;</td></tr><tr><td align="left">border-top-width:宽度;</td><td align="left">border- bottom-width:宽度;</td><td align="left">border-left-width:宽度;</td><td align="left">border-right-width:宽度;</td></tr><tr><td align="left">border-top-color:颜色;</td><td align="left">border- bottom-color:颜色;</td><td align="left">border-left-color:颜色;</td><td align="left">border-right-color:颜色;</td></tr><tr><td align="left">border-top:宽度 样式 颜色;</td><td align="left">border-bottom:宽度 样式 颜色;</td><td align="left">border-left:宽度 样式 颜色;</td><td align="left">border-right:宽度 样式 颜色;</td></tr></tbody></table>
<p><strong>表格的细线边框：</strong></p>
<ul>
<li>
<p>通过表格的<code>cellspacing="0"</code>,将单元格与单元格之间的距离设置为0，</p>
</li>
<li>
<p>但是两个单元格之间的边框会<code>出现重叠，从而使边框变粗</code></p>
</li>
<li>
<p>通过css属性：table&#123; border-collapse:collapse; &#125;</p>
<ul>
<li><code>collapse</code> 单词是合并的意思,<code>border-collapse: collapse;</code>表示相邻边框合并在一起。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><style>
 <span class="hljs-selector-tag">table</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid red;
 &#125;
 <span class="hljs-selector-tag">td</span> &#123;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid red;
  <span class="hljs-attribute">text-align</span>: center;
 &#125;
 <span class="hljs-selector-tag">table</span>, <span class="hljs-selector-tag">td</span> &#123;
  <span class="hljs-attribute">border-collapse</span>: collapse;  <span class="hljs-comment">/*合并相邻边框*/</span>
 &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2. 内边距(padding)</h3>
<p>padding属性用于设置内边距。是指<code>边框与内容之间的距离。</code></p>
<p><strong>设置</strong></p>

























<table><thead><tr><th align="left">属性</th><th align="left">作用</th></tr></thead><tbody><tr><td align="left">padding-left</td><td align="left">左内边距</td></tr><tr><td align="left">padding-right</td><td align="left">右内边距</td></tr><tr><td align="left">padding-top</td><td align="left">上内边距</td></tr><tr><td align="left">padding-bottom</td><td align="left">下内边距</td></tr></tbody></table>
<p><strong>padding简写</strong></p>

























<table><thead><tr><th align="left">值的个数</th><th align="left">表达意思</th></tr></thead><tbody><tr><td align="left">1个值</td><td align="left">padding：上下左右内边距;</td></tr><tr><td align="left">2个值</td><td align="left">padding: 上下内边距   左右内边距 ；</td></tr><tr><td align="left">3个值</td><td align="left">padding：上内边距  左右内边距  下内边距；</td></tr><tr><td align="left">4个值</td><td align="left">padding: 上内边距 右内边距 下内边距 左内边距 ；</td></tr></tbody></table>
<p>当我们给盒子指定padding值之后， 发生了2件事情：</p>
<ol>
<li>内容和边框 有了距离，添加了内边距。</li>
<li><code>盒子会变大</code></li>
</ol>
<p><strong>解决措施：</strong> 通过给设置了宽高的盒子，减去相应的内边距的值，维持盒子原有的大小。</p>
<p><strong>padding不影响盒子大小情况：👉</strong>如果没有给一个盒子指定宽度， 此时，如果给这个盒子指定padding， 则不会撑开盒子。</p>
<h3 data-id="heading-5">3. 外边距（margin）</h3>
<p>margin属性用于设置外边距。margin就是控制<code>盒子和盒子之间的距离</code></p>
<p><strong>设置</strong></p>

























<table><thead><tr><th align="left">属性</th><th align="left">作用</th></tr></thead><tbody><tr><td align="left">margin-left</td><td align="left">左外边距</td></tr><tr><td align="left">margin-right</td><td align="left">右外边距</td></tr><tr><td align="left">margin-top</td><td align="left">上外边距</td></tr><tr><td align="left">margin-bottom</td><td align="left">下外边距</td></tr></tbody></table>
<p>margin值的简写 （复合写法）代表意思  跟 padding 完全相同。</p>
<p><strong>块级盒子水平居中</strong></p>
<ul>
<li>盒子必须指定宽度（width）</li>
<li>然后就给左右的外边距都设置为auto</li>
</ul>
<p>实际工作中常用这种方式进行网页布局，示例代码如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.header</span>  &#123; <span class="hljs-attribute">width</span>: <span class="hljs-number">960px</span>; <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常见的写法，以下三种都可以👇👇。</p>
<ul>
<li>margin-left: auto;  margin-right: auto;</li>
<li>margin: auto;</li>
<li>margin: 0 auto;</li>
</ul>
<p><strong>文字居中和盒子居中区别👇👇</strong></p>
<ol>
<li>盒子内的文字水平居中是 text-align: center; 而且还可以让 行内元素和行内块居中对齐</li>
<li>块级盒子水平居中  左右margin 改为 auto</li>
</ol>
<p><strong>插入图片和背景图片区别👇👇</strong></p>
<ol>
<li><code>插入图片</code>我们用的最多 比如产品展示类  移动位置只能靠盒模型 padding margin</li>
<li><code>背景图片</code>我们一般用于小图标背景或者超大背景图片、背景图片，移动位置只能通过  background-position</li>
</ol>
<p><strong>清除元素的默认内外边距👇👇</strong></p>
<ul>
<li><code>行内元素为了照顾兼容性,尽量只设置左右内外边距，不要设置上下内外边距。</code></li>
</ul>
<pre><code class="hljs language-css copyable" lang="css">* &#123;
   <span class="hljs-attribute">padding</span>:<span class="hljs-number">0</span>;         <span class="hljs-comment">/* 清除内边距 */</span>
   <span class="hljs-attribute">margin</span>:<span class="hljs-number">0</span>;          <span class="hljs-comment">/* 清除外边距 */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">4.外边距合并</h3>
<p>使用margin定义块元素的 <strong>「垂直外边距」</strong> 时，可能会出现外边距的合并。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5e56d50016444f89e8400be392d7469~tplv-k3u1fbpfcp-zoom-1.image" alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-eyv45WV0-1620959107054)(盒子模型.assets/image-20210514101435125.png)]" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">(1). 相邻块元素垂直外边距的合并</h4>
<ul>
<li>当上下相邻的两个块元素相遇时，如果上面的元素有下外边距margin-bottom</li>
<li>下面的元素有上外边距margin-top，则他们之间的垂直间距不是margin-bottom与margin-top之和</li>
<li><strong>「取两个值中的较大者」</strong> 这种现象被称为相邻块元素垂直外边距的合并（也称外边距塌陷）。</li>
</ul>
<p><strong>「解决方案：尽量给只给一个盒子添加margin值」</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cc0a41610f34d50b689f96d79bd71b2~tplv-k3u1fbpfcp-zoom-1.image" alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-Z3nstoQO-1620959107070)(盒子模型.assets/image-20210514101458497.png)]" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">(2). 嵌套块元素垂直外边距的合并（塌陷）</h4>
<ul>
<li>对于两个嵌套关系的块元素，如果父元素没有上内边距及边框</li>
<li>父元素的上外边距会与子元素的上外边距发生合并</li>
<li>合并后的外边距为两者中的较大者</li>
</ul>
<p><strong>「解决方案：」</strong></p>
<ol>
<li>可以为父元素定义上边框或者上内边距</li>
<li>可以为<code>父元素添加overflow: hidden。</code></li>
</ol>
<p>还有其他方法，比如浮动、固定、绝对定位的盒子不会有问题，后面咱们再总结。。。</p>
<h4 data-id="heading-9">盒子模型布局稳定性</h4>
<p>优先使用  宽度 （width）  其次 使用内边距（padding）   再次  外边距（margin）</p>
<pre><code class="copyable">width >  padding  >   margin   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>原因：</strong></p>
<ul>
<li>margin 会有外边距合并 还有 ie6下面margin 加倍的bug（讨厌）所以最后使用。</li>
<li>padding  会影响盒子大小， 需要进行加减计算（麻烦） 其次使用。</li>
<li>width  没有问题（嗨皮）我们经常使用宽度剩余法 高度剩余法来做。</li>
</ul>
<hr>
<h2 data-id="heading-10">CSS3 新增</h2>
<h3 data-id="heading-11">圆角边框</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">border-radius</span>:length;
<span class="hljs-attribute">border-top-left-radius</span>   定义了左上角的弧度
<span class="hljs-attribute">border-top-right-radius</span>   定义了右上角的弧度
<span class="hljs-attribute">border-bottom-right-radius</span>   定义了右下角的弧度
<span class="hljs-attribute">border-bottom-left-radius</span>   定义了左下角的弧度
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>其中每一个值可以为 数值或百分比的形式。</li>
<li>技巧：让一个正方形 变成圆圈</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要在四个角上一一指定，可以使用以下规则👇👇：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">border-radius</span>: 左上角 右上角  右下角  左下角;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>四个值: 第一个值为左上角，第二个值为右上角，第三个值为右下角，第四个值为左下角。</li>
<li>三个值: 第一个值为左上角, 第二个值为右上角和左下角，第三个值为右下角</li>
<li>两个值: 第一个值为左上角与右下角，第二个值为右上角与左下角</li>
<li>一个值：四个圆角值相同</li>
</ol>
<h3 data-id="heading-12">盒子阴影</h3>
<pre><code class="hljs language-css copyable" lang="css">盒子阴影(<span class="hljs-attribute">box-shadow</span>)：
<span class="hljs-attribute">box-shadow</span>: offset-x offset-y [blur [spread]] [color] [inset]
box-shadow:水平阴影 垂直阴影 模糊距离 阴影尺寸（影子大小） 阴影颜色  内/外阴影；
<span class="copy-code-btn">复制代码</span></code></pre>

































<table><thead><tr><th align="left">值</th><th align="left">描述</th></tr></thead><tbody><tr><td align="left">offset-x</td><td align="left">阴影的水平偏移量。正数向右偏移，负数向左偏移。</td></tr><tr><td align="left">offset-y</td><td align="left">阴影的垂直偏移量。正数向下偏移，负数向上偏移。</td></tr><tr><td align="left">blur</td><td align="left">可选。阴影模糊距离，不能取负数。</td></tr><tr><td align="left">spread</td><td align="left">可选。阴影大小</td></tr><tr><td align="left">color</td><td align="left">可选。阴影的颜色</td></tr><tr><td align="left">inset</td><td align="left">可选。表示添加内阴影，默认为外阴影</td></tr></tbody></table>
<ol>
<li>前两个属性是必须写的。其余的可以省略。</li>
<li><code>外阴影 (outset) 不能写出来，是默认的</code>，写出来之后会报错。想要内阴影就写inset</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
   <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
   <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
   <span class="hljs-attribute">border</span>: <span class="hljs-number">10px</span> solid red;
   <span class="hljs-comment">/* box-shadow: 5px 5px 3px 4px rgba(0, 0, 0, .4);  */</span>
   <span class="hljs-comment">/* box-shadow:水平位置 垂直位置 模糊距离 阴影尺寸（影子大小） 阴影颜色  内/外阴影； */</span>
   <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">15px</span> <span class="hljs-number">30px</span>  <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">4</span>);   
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            