
---
title: 'css之flex'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/799cecff861b43a289b65221d02707c8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 04:43:18 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/799cecff861b43a289b65221d02707c8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>之前写过一篇介绍grid的文章，也懒了好久，今天来聊一聊flex吧。</p>
<h2 data-id="heading-0">display:flex</h2>
<p>使用flex首先要将容器的<code>display</code>属性设置为<code>flex</code>或<code>inline-flex</code>。使其转换为flex容器。</p>
<ul>
<li>flex：块状felx</li>
<li>inline-flex：内联flex</li>
</ul>
<p>首先我们先准备一套容器备用：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item i1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item i2"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item i3"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item i4"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item i5"</span>></span>5<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item i6"</span>></span>6<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item i7"</span>></span>7<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item i8"</span>></span>8<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item i9"</span>></span>9<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.flex</span> <span class="hljs-selector-class">.item</span>&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid blue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，页面的样子是：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/799cecff861b43a289b65221d02707c8~tplv-k3u1fbpfcp-watermark.image" alt="初始容器.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后，我们将.flex的display设置为flex，</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.flex</span>&#123;
    <span class="hljs-attribute">display</span>: flex;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面变为</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60ccb7e486c149fbbcf4f2c42ca7c7e2~tplv-k3u1fbpfcp-watermark.image" alt="flex容器.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为什么会这样呢？其实是当元素被设置为flex容器时，会有一些默认的属性和值生效。其中导致子<code>div</code>——<code>.item</code>,也可称他们为flex元素，变成横向排列的的属性时<code>flex-direction</code>。他的默认值是<code>row</code>，即横向排列。既然说到这里了，那么接下来就介绍他吧。</p>
<p>在这之前呢，先来了解两个概念：轴和起止线</p>
<h2 data-id="heading-1">轴和起止线</h2>
<p>flex容器有两根轴，主轴和交叉轴。其中主轴由<code>flex-direction</code>的值决定。默认值<code>row</code>表示主轴是从左到右。起止线分别位于左右两边，左起右止（本文只讨论ltr的情况，rtl与之左右相反，右起左止）。交叉轴方向为从上到下，起止线为上起下止。了解这个以后我们就可以继续了。</p>
<h2 data-id="heading-2">flex-direction</h2>
<p>flex-direction有四个值，分别是：</p>
<ul>
<li>row               主轴从左到右，交叉轴从上到下</li>
<li>row-reverse       主轴从右到左，交叉轴从上到下</li>
<li>column            主轴从上到下，交叉轴从左到右</li>
<li>column-reverse    主轴从下到上，交叉轴从左到右</li>
</ul>
<p>下面是四种值的对应表现：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/068ee34f283b48ab817d2855e7a7ddad~tplv-k3u1fbpfcp-watermark.image" alt="direction.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>flex容器的默认值除了<code>flex-direction:row</code>之外，还有：</p>
<ul>
<li>元素从主轴起始线开始。</li>
<li>元素在主轴方向不会被拉伸——元素属性<code>flex-grow:0</code>，但可以缩小——元素属性<code>flex-shrink:1</code>。</li>
<li>元素在交叉轴上会被拉伸——容器属性<code>align-items: stretch</code>;</li>
<li>元素不会换行——容器属性<code>flex-wrap:nowrap</code></li>
<li><code>flex-basis:auto</code></li>
</ul>
<p>接下来我们就来一一认识他们吧。</p>
<h2 data-id="heading-3">flex-shrink</h2>
<p>flex-shrink可以定义元素的缩小规则，值为非负整数，默认值为1。为了看到效果，我们先把容器的宽度设置为小于总元素的值</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.flex</span>&#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">600px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b00681b594d4ac0a4ea432a8e5f7dec~tplv-k3u1fbpfcp-watermark.image" alt="shrink1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，所有元素立马缩小了，宽度依然保持相等。因为所有元素的<code>flex-shrink</code>的值都是默认值1，所以他们缩小的比例也是相同的。如果更改其中某个元素的值呢？</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.i1</span>&#123;
    <span class="hljs-attribute">flex-shrink</span>: <span class="hljs-number">2</span>;
&#125;
<span class="hljs-selector-class">.i2</span>&#123;
    <span class="hljs-attribute">flex-shrink</span>: <span class="hljs-number">3</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了方便计算，我们先去除<code>border</code>，来看一下吧：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e27facf0051644bda5da0e51fd23f5b2~tplv-k3u1fbpfcp-watermark.image" alt="shrink2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到<code>i1</code>的宽度为50，<code>i2</code>为25，其他均为75，这是怎么算出来的呢。原始元素总长度为<code>100*9=900</code>，现在容器长度为600。相差300。缩小的范围就在相差的300px之中，具体计算规则为：300除以总shrink的和值。上面为<code>2+3+1*7</code>，其他7个为默认值1。300除以12等于25。再用元素的初始宽度减去（shrink的值乘以25），所以<code>i1</code>的宽度为 <code>100-25*2=50</code>,同理<code>i2</code>为<code>100-25*3=25</code>。总结后为：</p>
<p><code>元素初始宽度-（原始所有元素宽度-现在所有元素宽度）/所有元素总shrink和值*元素shrink值</code></p>
<p>但是当这个值非常小的时候，元素会保留它的最小宽度（示例中文字宽度）。</p>
<p>如果<code>flex-shirink</code>值为0，则不会缩小。</p>
<p>如果加上<code>border</code>要怎么计算呢？首先我们要用差值加上<code>border</code>的总和值——其实是<code>原始所有元素宽度-（现在所有元素宽度-border总和）</code>算出content的宽，最后在算出的值加上自己的<code>border</code>就行。如上例子就是：<code>300+18=318</code>，<code>318/12=26.5</code>，i1：<code>100-26.5*2+1+1=49</code>，i2：<code>100-26.5*3+1+1=22.5</code>。</p>
<h2 data-id="heading-4">flex-grow</h2>
<p>用于设置元素的放大规则，将多余空间按照<code>flex-grow</code>的总和值平分后加到原有元素上。上面说过<code>flex-grow</code>的默认值为0，不会放大。那么来更改几个元素看看吧：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.flex</span>&#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">1200px</span>;
&#125;
<span class="hljs-selector-class">.i1</span>&#123;
    <span class="hljs-attribute">flex-grow</span>: <span class="hljs-number">2</span>;
&#125;
<span class="hljs-selector-class">.i2</span>&#123;
    <span class="hljs-attribute">flex-grow</span>: <span class="hljs-number">3</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总宽度1200，原始宽度900，多出300，分成<code>2+3=5</code>份，每份60px，所以<code>i1</code>的最终宽度为<code>100+60*2=220</code>，<code>i2</code>为<code>100+60*3=280</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/963e7afa6a374a68b800009cc78c9452~tplv-k3u1fbpfcp-watermark.image" alt="grow.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">flex-basis</h2>
<p><code>flex-basis</code>可以设置元素在主轴方向上的大小。如<code>flex-direction</code>值为<code>row[-reverse]</code>，相当于<code>width</code>。<code>column[-reverse]</code>相当于<code>height</code>。当<code>flex-basis</code>（非<code>auto</code>）和<code>width</code>、<code>height</code>同时存在时，<code>flex-basis</code>的优先级更高。值为<code>auto</code>时则会使用<code>width</code>、<code>height</code>。上面例子都是默认值<code>auto</code>，这里就不赘述了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbc1a3f669744f4191a50538643b62bc~tplv-k3u1fbpfcp-watermark.image" alt="basis.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当<code>flex-basis</code>值为0时，元素会保留其能显示最小宽度，其余空间均为剩余空间，可用于<code>flex-grow</code>或<code>flex-shrink</code>计算。</p>
<blockquote>
<p>据说某些浏览器0会出现问题，可尝试使用0%替换。</p>
</blockquote>
<h2 data-id="heading-6">flex-wrap</h2>
<p>用于控制当元素超出时是否换行。</p>
<ul>
<li>nowrap 不换行，默认值</li>
<li>wrap 多行</li>
<li>warp-reverse 多行，但交换交叉轴的起止点</li>
</ul>
<p>我们改变flex容器的<code>flex-wrap</code>值来看下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.flex</span>&#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">600px</span>;
    <span class="hljs-attribute">flex-wrap</span>: wrap;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c7cb05091b845398000c09c4524c191~tplv-k3u1fbpfcp-watermark.image" alt="wrap.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">flex-flow</h2>
<p>此为<code>flex-direction</code>和<code>flex-wrap</code>的缩写，如:<code>flex-flow:row wrap;</code></p>
<h2 data-id="heading-8">flex</h2>
<p>为flex-grow/flex-shrink/flex-basis的缩写形式。如：<code>flex:1 1 0</code>，此属性有四种预定义属性：</p>
<ul>
<li>initial 相当于 0 1 auto</li>
<li>auto  相当于 1 1 auto</li>
<li>none  相当于 0 0 auto</li>
<li>数值 相当于 数值 1 0% 如：<code>flex:1</code> 为 1 1 0%</li>
</ul>
<h2 data-id="heading-9">order</h2>
<p>值为整数，可以用来改变元素的顺序，默认值为0。小的值排在大的值前面。设置如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.i1</span>&#123;
    <span class="hljs-attribute">order</span>:<span class="hljs-number">2</span>
&#125;
<span class="hljs-selector-class">.i3</span>&#123;
    <span class="hljs-attribute">order</span>:-<span class="hljs-number">2</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/607b52fade7f4336b0ea1bc959f6916a~tplv-k3u1fbpfcp-watermark.image" alt="order.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">gap</h2>
<p>同<code>grid</code>的<code>gap</code>，用于设置两个元素之间的间距：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.flex</span>&#123;
    gap:<span class="hljs-number">30px</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc3b0b55035b441da57dc26c0f9f73fb~tplv-k3u1fbpfcp-watermark.image" alt="gap.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">justify-content</h2>
<p>用于设置元素在主轴上的对齐方式。(口是元素，—是空白)</p>
<ul>
<li>flex-start 主轴起始线对齐                         |口口口——————|</li>
<li>flex-end 主轴终止线对齐                           |——————口口口|</li>
<li>center 居中                                      |———口口口———|</li>
<li>space-between 元素之间间距相同，左右元素挨着两边    |口———口———口|</li>
<li>space-around 元素左右两侧有相同的间距              |—口——口——口—|</li>
<li>space-evenly 元素之间、元素与边之间间距相同         |—口—口—口—|</li>
</ul>
<h2 data-id="heading-12">align-items</h2>
<p>用于设置元素在交叉轴上的对齐方式。</p>
<ul>
<li>flex-start 交叉轴起始线对齐</li>
<li>flex-end 交叉轴终止线对齐</li>
<li>center 居中</li>
<li>stretch 拉伸补充，默认值。</li>
</ul>
<p><code>stretch</code>的效果可以将flex容器的高度设置为<code>100px</code>，此时可以看到元素的高度填满整个高度。但是元素如果设置有自己的大小限制的话，则不会拉伸。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3efe02490ccf4f96abfec969a456925d~tplv-k3u1fbpfcp-watermark.image" alt="stretch.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">align-content</h2>
<p>当有多行时，用于设置多行相对于容器的对齐方式，其值包含了上述<code>justify-content</code>和<code>align-items</code>的所有值。效果也是一样的，来浏览一下吧</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0533449625414961ab0b1d416d1fd3f0~tplv-k3u1fbpfcp-watermark.image" alt="alignContent.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">align-self</h2>
<p>用于控制单个元素的对齐方式。可覆盖<code>align-items</code>的值。</p>
<p>将容器<code>align-items</code>设置为<code>center</code>，<code>i1</code>的<code>align-self</code>设置为<code>flex-start</code>。效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45598f5b0cd942518a68f84483de92b7~tplv-k3u1fbpfcp-watermark.image" alt="self.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>经测，当多行时，<code>align-content</code>拥有高优先级，<code>align-self</code>不能覆盖其值。</p>
</blockquote>
<p>呼~，可以愉快的去玩耍了。溜了溜了</p></div>  
</div>
            