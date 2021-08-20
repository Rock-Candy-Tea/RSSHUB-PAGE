
---
title: 'Flex布局—语法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8e5e48117574500918809982a77a24b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 23:42:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8e5e48117574500918809982a77a24b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2015%2F07%2Fflex-grammar.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2015/07/flex-grammar.html" ref="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2015/0…</a></p>
</blockquote>
<h2 data-id="heading-0">布局方式</h2>
<p>布局一直是css的重点知识 flex布局更是近几年流行的布局方式</p>
<h3 data-id="heading-1">1.传统布局方式</h3>
<hr>
<p>传统盒模型 基本用display + position + float 就可以解决 但是针对一些自适应的宽度/设置垂直居中的特殊布局非常不方便</p>
<h3 data-id="heading-2">2.Flex布局方式</h3>
<h4 data-id="heading-3">1.什么是Flex布局</h4>
<hr>
<p>Flex 是 Flexible Box 的缩写，意为"弹性布局"，用来为盒状模型提供最大的灵活性。</p>
<p>任何容器都可以指定为Flex布局</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">display</span>: flex
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>行内元素也可以使用Flex布局</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">display</span>: inline-flex
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：设为flex布局后 子元素的float、clear和vertical-align属性都将失效</p>
<p>注释：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Ffloat" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/float" ref="nofollow noopener noreferrer">float</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Fclear" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/clear" ref="nofollow noopener noreferrer">clear</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Fvertical-align" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/vertical-align" ref="nofollow noopener noreferrer">vertical-align</a></p>
<h4 data-id="heading-4">2.基本概念</h4>
<hr>
<p>采用 Flex 布局的元素，称为 Flex 容器（flex container），简称"容器"。它的所有子元素自动成为容器成员，称为 Flex 项目（flex item），简称"项目"。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8e5e48117574500918809982a77a24b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>容器默认存在两根轴：水平的主轴（main axis）和垂直的交叉轴（cross axis）主轴的开始位置叫做main start 主轴的结束为止 main end （默认左边开始位置是main start 右边结束位置 main end）交叉轴开始位置叫做cross start 交叉轴结束位置叫做 cross end （默认上边是开始位置cross start 下边是结束位置cross end）</p>
<p>注意：项目默认是沿主轴排列的 单个项目占据的主轴空间为main size 交叉轴占据的空间叫 cross size</p>
<p>重点：搞清主轴和交叉轴的定义和默认方向</p>
<h4 data-id="heading-5">3.容器的属性（重点）</h4>
<hr>
<p>以下6个属性设置在容器上（<code>display:flex</code>所在的元素）</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex-direction</span>
<span class="hljs-attribute">flex-wrap</span>
<span class="hljs-attribute">flex-flow</span>
<span class="hljs-attribute">justify-content</span>
<span class="hljs-attribute">align-items</span>
<span class="hljs-attribute">align-content</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">3.1 flex-direction属性</h4>
<hr>
<p><code>flex-direction</code>属性 决定主轴的方向（项目的排列方向）</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">flex-direction</span>: row | row-reverse | column | column-reverse
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/987742d291704409929231090bb1c85e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图分别代表：column-reverse  column  row   row-reverse</p>
<p>值有4个分别是</p>
<ul>
<li>row（默认值）：主轴为水平方向 起点在左侧</li>
<li>row-reverse ：主轴为水平方向 起点在右侧</li>
<li>column：主轴为垂直方向 起点在上沿</li>
<li>column-reverse：主轴为垂直方向 起点在下沿</li>
</ul>
<h4 data-id="heading-7">3.2 flex-wrap属性</h4>
<hr>
<p>默认情况下，项目都排在一条线（又称"轴线"）上。<code>flex-wrap</code>属性定义，如果一条轴线排不下，如何换行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b262045ef5445b8a54a9cf2eb569be9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">.box &#123;
flex-wrap: nowrap | wrap | wrap-reverse
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值有三个分别是</p>
<p>1.<code>nowrap</code>（默认）：不换行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b93d44043d4427890780bef1c640c9c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2.<code>wrap</code>：换行 第一行在上方</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02bbe747a53a44cb93ceb49f37368188~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>3.<code>nowrap</code>换行 第一行在下方</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b42afb9688224e099a135adf0faedf1c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">3.3 flex-flow属性</h4>
<hr>
<p><code>flex-flow</code>属性是<code>flex-direction</code>属性和<code>flex-wrap</code>属性的简写形式，默认值为<code>row nowrap</code></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">flex-flow</span>: <flex-direction> || <flex-wrap>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>样式结果比较多 可以自己尝试组合一下</p>
<h4 data-id="heading-9">3.4 justify-content属性</h4>
<hr>
<p><code>justify-content</code>属性定义了项目在主轴上的对齐方式</p>
<pre><code class="copyable">.box &#123;
justify-content: flex-start | flex-end | center | space-between | space-around
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5d4e66fc2d24170a0e41137c19afb1e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>值有5个，具体对齐方式跟主轴方向有关 下面假设主轴方向是从左到右</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex</span>-start:(默认值) 左对齐
flex-end: 右对齐
center: 居中
space-between: 两端对齐 项目之间的间隔都相等
space-around: 每个项目两侧的间隔相等 所以 项目之间的间隔比项目和边框的间隔大一倍
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：space-between和space-around的区别</p>
<p>space-between：两侧项目与边框无间隔 剩余项目间隔相等</p>
<p>space-around：两侧项目与边框有间隔 剩余项目间隔相等</p>
<h4 data-id="heading-10">3.5 align-items属性</h4>
<hr>
<p><code>aligin-items</code>属性定义项目在交叉轴上如何对齐</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">align-items</span>: flex-start | flex-end | center | baseliine | stretch
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a9cfa6a930c4a6eb5d22699d2796dda~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>值有5个 具体对齐的方式和交叉轴的方向有关 下面假设交叉轴从上到下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex</span>-start: 交叉轴的起点对齐
flex-end: 交叉轴的终点对齐
center: 交叉轴的中点对齐
baseline: 项目的第一行文字的基线对齐。
stretch: （默认值）如果项目未设置高度或设为auto，将占满整个容器的高度。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">3.6 align-content属性</h4>
<hr>
<p><code>align-content</code>属性定义了多根轴线的对齐方式 如果项目只有一根轴线 该属性不起作用</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">align-content</span>: flex-start | flex-end | center | space-between | space-around
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81b26233d02a4692bb0a8de97c9d1899~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">值有6个分别是</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex</span>-start:与交叉轴的起点对齐
flex-end:与交叉轴的终点对齐
center: 与交叉轴的中点对齐
space-between: 与交叉轴两端对齐 轴线之间的间隔平均分配
space-around: 每根轴线两侧的间隔都相等 所以 轴线之间的间隔比轴线边框的间隔大一倍
stretch: (默认值) 轴线占满整个交叉轴
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4.项目的属性</h3>
<hr>
<p>以下6个属性设置在项目上</p>
<pre><code class="copyable">order
flex-grow
flex-shrink
flex-basis
flex
align-self
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">4.1 order属性</h4>
<hr>
<p><code>order</code>属性定义项目的排列顺序 数值越小 排列越靠前 默认值为0</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.item</span> &#123;
<span class="hljs-attribute">order</span>: <integer>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d4743ab38b4441a88c042b4c2fccca0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">4.2 flex-grow属性</h4>
<hr>
<p><code>flex-grow</code>属性定义项目的放大比例 默认为0 即如果存在剩余空间 也不放大</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.item</span> &#123;
<span class="hljs-attribute">flex-grow</span>: <number>  /* defalut <span class="hljs-number">0</span> */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/097d912c40c141dd98c447673f5e186f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意：</p>
<p>如果所有项目的<code>flex-grow</code>属性都为1，则它们将等分剩余空间（如果有的话）。</p>
<p>如果一个项目的<code>flex-grow</code>属性为2，其他项目都为1，则前者占据的剩余空间将比其他项多一倍。</p>
<h4 data-id="heading-15">4.3 flex-shrink属性</h4>
<p>flex-shrink属性定义了项目的缩小比例 默认为1 即如果空间不足 该项目将缩小</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.item</span> &#123;
<span class="hljs-attribute">flex-shrink</span>: <number> /* defalut <span class="hljs-number">1</span> */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41a76eea9299433386c3517d90e9db18~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意：</p>
<p>如果所有项目的<code>flex-shrink</code>属性都为1，当空间不足时，都将等比例缩小。</p>
<p>如果一个项目的<code>flex-shrink</code>属性为0，其他项目都为1，则空间不足时，前者不缩小。</p>
<h4 data-id="heading-16">4.4 flex-basis属性</h4>
<hr>
<p><code>flex-basis</code>属性定义了在分配多余空间之前，项目占据的主轴空间（main size）。浏览器根据这个属性，计算主轴是否有多余空间。它的默认值为<code>auto</code>，即项目的本来大小。</p>
<pre><code class="hljs language- css copyable" lang=" css">.item &#123;
flex-basis: <length> | auto /* defalut auto */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它可以设为跟width或height属性一样的值（比如350px）则项目将占据固定空间</p>
<h4 data-id="heading-17">4.5 flex属性</h4>
<hr>
<p><code>flex</code>属性是<code>flex-grow</code>, <code>flex-shrink</code> 和 <code>flex-basis</code>的简写，默认值为<code>0 1 auto</code>。后两个属性可选。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.item</span> &#123;
<span class="hljs-attribute">flex</span>: none | <<span class="hljs-string">'flex-grow'</span>><<span class="hljs-string">'flex-shrink'</span>>? || <<span class="hljs-string">'flex-basis'</span>>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该属性有两个快捷值：<code>auto</code> (<code>1 1 auto</code>) 和 none (<code>0 0 auto</code>)。</p>
<p>建议优先使用这个属性，而不是单独写三个分离的属性，因为浏览器会推算相关值。</p>
<h4 data-id="heading-18">4.6 align-self属性</h4>
<hr>
<p><code>align-self</code>属性允许单个项目有与其他项目不一样的对齐方式，可覆盖<code>align-items</code>属性。默认值为<code>auto</code>，表示继承父元素的<code>align-items</code>属性，如果没有父元素，则等同于<code>stretch</code>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.item</span> &#123;
<span class="hljs-attribute">align-self</span>: auto | flex-start | flex-end | center | baseline | stretch
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a57d9a73ca45420b9489a383af87d8be~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>该属性可能取6个值，除了auto，其他都与align-items属性完全一致。</p></div>  
</div>
            