
---
title: '你必须学会的flex布局'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c8514dd80304723a08357fc48124925~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Apr 2021 00:35:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c8514dd80304723a08357fc48124925~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">CSS3中的Flex布局</h1>
<p>flex布局是2009年W3C提出的一种新的布局方案，可以非常简洁方便的完成网页布局，与平常的浮动，定位相比，flex布局显得更灵活更好上手和理解</p>
<h3 data-id="heading-1">什么是flex布局？</h3>
<p>flex意思是弹性布局 用来给盒模型提供最大的灵活性 任何一个容器都可以指定成flex布局，而且flex布局可以实现响应式布局（一套布局能够适配不同设备，能响应屏幕大小的布局）当然前提是哪些地方能给宽高哪些地方要用flex-grow放大。要想使用父盒的属性必须保证父盒是flex盒子也就是说必须要将该盒子display设成flex，子元素要想使用子盒属性必须保证自己的父盒的display是flex</p>
<pre><code class="copyable">.box&#123;
    display : flex
&#125;   //给一个容器的display设置成flex 这个容器就成为了flex的盒子

.box-one&#123;
    display : inline-flex
&#125;   //行内元素也可以设置flex
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先要理解flex布局的一个概念，当一个容器的display被设置成了flex，那么这个容器就编程了一个flex的盒子
里面所有的子元素的float、clear和vertical-align属性将失效，并且自己的子元素会默认在一行一顺排列</p>
<pre><code class="copyable">CSS
 .box&#123;
    display: flex;
    height: 500px;
    width: 500px;
    background-color: pink;
&#125;
.item&#123;
    height: 50px;
    width: 50px;
    border-radius: 50%;
    background-color: #000;
&#125;
HTML
<div class="box">
    <div class="item"></div>
    <div class="item"></div>
    <div class="item"></div>
    <div class="item"></div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c8514dd80304723a08357fc48124925~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里可以看到给box设置了display:flex后 item全部都排列在了一行</p>
<h2 data-id="heading-2">flex布局里面的基线</h2>
<p>采用 Flex 布局的元素，称为 Flex 容器（flex container），简称"容器"。它的所有子元素自动成为容器成员，称为 Flex 项目（flex item），简称"项目"。</p>
<p><img alt="企业微信截图_16186269031980.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3761b9ec703c4d1788453159f2c8e018~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>容器默认存在两根轴：水平的主轴（main axis）和垂直的交叉轴（cross axis）。主轴的开始位置（与边框的交叉点）叫做main start，结束位置叫做main end；交叉轴的开始位置叫做cross start，结束位置叫做cross end。
项目默认沿主轴排列。单个项目占据的主轴空间叫做main size，占据的交叉轴空间叫做cross size。</p>
<p>可能你觉得这个基线图很难看明白很难看懂，不过后面的例子应该可以让你很清晰的看懂到底什么是flex布局</p>
<h2 data-id="heading-3">容器的属性</h2>
<p>首先在容器上面有6个属性   容器就是上面例子中的box元素 也可以说是父盒子 这6个属性是设置在父盒子上的属性 可以理解成要设置在有display : flex 属性的容器上</p>
<h4 data-id="heading-4">flex-direction</h4>
<pre><code class="copyable">//flex-direction  决定主轴的方向
有四个值
row（默认值）：主轴为水平方向，起点在左端。 |你的item（子盒子）从左往右排序
row-reverse：主轴为水平方向，起点在右端。 |你的item从右往左排序
column：主轴为垂直方向，起点在上沿。 |你的item从上往下排序
column-reverse：主轴为垂直方向，起点在下沿。 |你的item从下往上排序
.box &#123;
  flex-direction: row | row-reverse | column | column-reverse;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还是以上面的代码为例子</p>
<pre><code class="copyable"><div class="box">
        <div class="item one">1号</div>
        <div class="item two">2号</div>
        <div class="item three">3号</div>
        <div class="item four">4号</div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当box的flex-direction设成row</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bac594c7aa24d25943af9239a90aada~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>row-reverse</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9e5c19c294b4fec8c77b76466c5607e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>column</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7740225e3418495f850ccd1517ab092b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>column-reverse</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8635672e22f343a3a70afb2b7f6ec8b2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">flex-wrap</h4>
<p>定义子盒子换行的情况</p>
<pre><code class="copyable">一共有3个属性
flex-wrap: nowrap | wrap | wrap-reverse;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>nowrap 不换行   子元素会被挤小</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06239fd08a1b48f3916440af2710b8dd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>wrap  换行  第二行开始从左往右</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c73760acdda141188657909d8dfd167a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>wrap-reverse 换行 第一行在下方</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36f9ed63d42e492a90f0464ef19ca08c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">flex-flow</h4>
<p>是flex-direction和flex-wrap的简写</p>
<pre><code class="copyable">用法
.box &#123;
  flex-flow: <flex-direction> || <flex-wrap>;  <>表示填写flex-direction和flex-wrap的属性
  例如 flex-flow:row , nowrap
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">justify-content</h4>
<p>justify-content属性定义了项目在主轴上的对齐方式</p>
<pre><code class="copyable">.box &#123;
  justify-content: flex-start | flex-end | center | space-between | space-around;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里以父盒的flex-direction为row为例 不同的direction效果也会不同 如果不懂可以自己去敲一下 试一下你就知道direction和justify-content联动起来可以做出什么效果了</p>
<p>flex-start   左对齐</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4695a2683694d7994a19669fbc3dc4c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>flex-end 右对齐</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21aae366bf9842a68c1bce0dedf126d7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>center 居中</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91aa19c5a5e948ac968e034d3a39dcf0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>space-betweet 两端对齐，项目之间的间隔都相等</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9ab04a4f51a4bf0a1f2a0cd870d32fe~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>space-around 每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d57c2bf9b93c4a61a0337773e2c62f20~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">align-items</h4>
<p>align-items属性定义项目在交叉轴上如何对齐</p>
<pre><code class="copyable">.box &#123;
  align-items: flex-start | flex-end | center | baseline | stretch;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里以box的direction为row、 justify-content为space-between为例</p>
<p>flex-start 交叉轴的起点对齐</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b9ff6b287354f5382a7386dbed3824d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>flex-end 交叉轴的终点对齐</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f474592466ac4d589544d762a18463b1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>center 交叉轴的中点对齐</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4f3831c12614a37a36e79940b3b51ec~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>baseline 项目的第一行文字的基线对齐</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cd5b2b019a84c9c929bed5589ab4da0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里我给三个子盒子设置了不同的高度不同的行高 当align-item设置了baseline可以看出项目对齐方式变成了第一行文字的基线 就是以文字的基线来对齐的</p>
<p>stretch（默认值） 如果项目未设置高度或设为auto，将占满整个容器的高度</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40664d7c70f5483f9005049c9fe9efd6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里把子盒子的高度取消了 所以子盒子的高度占满了容器</p>
<h4 data-id="heading-9">align-content</h4>
<p>align-content属性定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用。也就是说如果子元素只有一行那么这个属性不会起作用，必须要两行及以上的元素设置这个属性才有效，下面的例子会以box的flex-wrap为wrap（换行）来执行</p>
<pre><code class="copyable">.box &#123;
  align-content: flex-start | flex-end | center | space-between | space-around | stretch;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>flex-start 与交叉轴的起点对齐</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a55a25a171d247dd93d8d7f5d085014d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>flex-end 与交叉轴的终点对齐</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3a8ad44cf9d4b898caeba6063df1eea~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>center 与交叉轴的中点对齐</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c24055b99774b959b7d32f57dabe097~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>space-between 与交叉轴两端对齐，轴线之间的间隔平均分布</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82c2f70ad4454025ac328576a25625e3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>space-around 每根轴线两侧的间隔都相等。所以，轴线之间的间隔比轴线与边框的间隔大一倍。</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/523c4c1a90f8497896f6ae61d1db1507~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>stretch（默认值）如果子元素没设置高度 轴线占满整个交叉轴 此处把子元素的高度取消了所以占满了整个交叉轴</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bd5533a2c33414f826eba2ef3eaa808~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">项目上的属性</h2>
<p>以下6个属性设置在项目上。（设置在子元素上的属性--item）</p>
<pre><code class="copyable">order
flex-grow
flex-shrink
flex-basis
flex
align-self
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">order</h4>
<p>order属性定义项目的排列顺序。数值越小，排列越靠前，默认为0。</p>
<pre><code class="copyable">.item-one&#123;
    order: 4;
    background-color: powderblue;
&#125;
.item-two&#123;
    order: 3;
    background-color:turquoise;
&#125;
.item-three&#123;
    order: 2;
    background-color: salmon;
&#125;
.item-four&#123;
    order: 1;
    background-color: springgreen;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我把1-4号子元素设置了order属性 并且1-4号的order是从大到小 所以结果是这样的 ：4号排在了最前面</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20de1522560e4ea283f18b73559defc0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">flex-grow属性</h4>
<p>flex-grow属性定义项目的放大比例，默认为0，即如果存在剩余空间，也不放大。
这个属性是一个比较重要的属性，可以这样来理解这个属性 一旦一个子元素设置了这个属性且值不为0，那么这个子元素就会放大，如果<strong>其他</strong>子元素没有设置这个属性，那么设置了这个属性的元素会分掉所有剩余空间，如果所有子元素都设置了这个属性且值相等，那么剩余的空间会被所有子元素等分，如果其中有一个子元素设置的是2其余子元素设置的是1那么设置2的子元素分掉剩余空间会比设置1的元素多一倍</p>
<p><strong>flex-grow为0的时候</strong></p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95d57df635d94a46bdcfc9067343ddb7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>例子1 <strong>所有子元素flex-grow设成1</strong></strong></p>
<pre><code class="copyable">.one&#123;
    flex-grow: 1;
    background-color: powderblue;
&#125;
.two&#123;
    flex-grow: 1;
    background-color:turquoise;
&#125;
.three&#123;
    flex-grow: 1;
    background-color: salmon;
&#125;
.four&#123;
    flex-grow: 1;
    background-color: springgreen;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果   所有子元素平分了剩余空间</strong></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6cc4f14950b4edf9704feaf41f9b483~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>例子2 把2号设置成1  其余不设置  2号独自分掉了剩余空间</strong></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c23b3bd50e8e4626a25f3db159129096~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>例子3 把2号设置成2，3号设置成1 其余设置成0  2号分掉的剩余空间是3号的一倍</strong></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c986671ebb1347889be7ca8288dcffc5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">flex-shrink属性</h4>
<p>flex-shrink属性定义了项目的缩小比例，默认为1，即如果空间不足，该项目将缩小，这个属性一般用到的地方是当一个父盒子横向或者纵向空间不足时用到，假设你的父盒有3个子元素，你想让第二个子元素占满剩余空间，于是你设置了第二个子元素的flex-grow为1其余子元素不设置，然后第二个子元素占满了所有空间但是由于第二个子元素空间太大，第一个和第三个子元素默认被缩小了比例，这个时候可以设置flex-shrink的值为0来恢复第一、三个子元素的大小，如果不理解可以看后面的例子</p>
<pre><code class="copyable">.item &#123;
  flex-shrink: <number>; /* default 1 */输入数字类型 默认值是1
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子   这里给第三个子元素设置了flex-shrink为0 所以当空间不足时第三个子元素没有变小</p>
<pre><code class="copyable">.one&#123;
    background-color: powderblue;
&#125;
.two&#123;
    background-color:turquoise;
&#125;
.three&#123;
    flex-shrink: 0;
    background-color: salmon;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f53a124d07304d408ee9024de3c0d00c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">flex-basis属性</h4>
<p>flex-basis属性定义了在分配多余空间之前，项目占据的主轴空间（main size）。浏览器根据这个属性，计算主轴是否有多余空间。它的默认值为auto，即项目的本来大小。</p>
<pre><code class="copyable">.one&#123;
    background-color: powderblue;
    flex: 1;
&#125;
.two&#123;
    background-color:turquoise;
    flex: 1;
&#125;
.three&#123;
    flex: 1;
    flex-basis: 100px;
    background-color: salmon;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里给第三个子元素设置了flex-basis值是100px 然后三个子元素flex：1（flex-grow, flex-shrink 和 flex-basis的简写，三个元素将平分剩余空间），我们可以看到前面两个子元素是133.33px而第三个子元素是233.33px
多分掉了100px</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0eac24e2484145f29c06be5acfc470f2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">flex属性</h4>
<p>flex属性是flex-grow, flex-shrink 和 flex-basis的简写，默认值为0 1 auto。后两个属性可选。这个属性会用到很多 因为是简写 一般想让一个子元素占满剩余空间的时候都会写flex：1，想让子元素平分剩余空间就在所有子元素上都写一个flex：1</p>
<pre><code class="copyable">.item &#123;
  flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]
&#125;
该属性有两个快捷值：auto (1 1 auto) 和 none (0 0 auto)。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">align-self属性</h4>
<p>align-self属性允许单个项目有与其他项目不一样的对齐方式，可覆盖align-items属性。默认值为auto，表示继承父元素的align-items属性，如果没有父元素，则等同于stretch。意思就是假如你有一个子元素和其他子元素的对齐方式不同，那么你可以在这个子元素上设置align-slef属性 值是你想要的对齐属性</p>
<pre><code class="copyable">.item &#123;
  align-self: auto | flex-start | flex-end | center | baseline | stretch;
&#125;
该属性可能取6个值，除了auto，其他都与align-items属性完全一致。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">flex布局的属性就只有这么多，看懂属性很重要，自己动手练习也很重要，这里说一下经常用到的属性有哪些</h3>
<pre><code class="copyable">display：flex  //将盒子设置成flex容器
flex-direction //设置父盒从哪开始排列
下面两个属性可以理解一个是横向对齐方式一个是纵向对齐方式
justify-content //子元素在父盒主轴的对齐方式
align-item // 子元素在交叉轴的对齐方式

常用的子元素属性
flex-shrink //子元素被挤压是否缩小
flex  //grow shrink basis三个属性的简写 经常flex：1来让子元素吸收多少剩余空间 而不用flex-grow
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">flex布局的优点就是在于任何容器都可使用flex布局，它可以让你不用在布局的时候计算高度，并且非常的灵活通用，在布局前先想清楚思路，你拿到的需求应该怎么用flex布局来写，其实很简单，就是一层一层的来写，先从最外层下手，把最外层元素设置成flex然后看里面一层是什么结构应该怎么对齐，然后再把里面一层设置成flex再看里面的结构应该怎么对齐......</h4>
<h3 data-id="heading-19">最后用flex布局展示一下常见的布局 container(容器) main（主要区域） header（页面头部） footer（页面尾部） aside（侧边栏）</h3>
<p><strong>例1</strong></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/522ff7e88c8540589917318f9622321c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">HTML//

<div class="container">
    <div class="header">我是header</div>
    <div class="main">我是main</div>
</div>

CSS//

 .container&#123;
    display: flex;
    height: 500px;
    width: 500px;
    background-color: pink;
    flex-direction: column;
&#125;
.header&#123;
    height: 100px;
    width: 100%;
    background-color: wheat;
    text-align: center;
&#125;
.main&#123;
    width: 100%;
    flex: 1;
    text-align: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>例2</strong></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0f574d4b63b45dcb40676e1b364c923~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">HTML//
 <div class="container">
    <div class="header">我是页头</div>
    <div class="right">
        <div class="aside">我是侧边栏</div>
        <div class="main">我是main</div>
    </div>
</div>

CSS//

 .container&#123;
    display: flex;
    height: 500px;
    width: 500px;
    background-color: pink;
    flex-direction: column;
&#125;
.right&#123;
    display: flex;
    flex-direction: row;  
    flex: 1;  
&#125;
.header&#123;
    height: 80px;
    width: 100%;
    line-height: 80px;
    background-color: wheat;
    text-align: center;
&#125;
.main&#123;
    width: 100%;
    flex: 1; 
    text-align: center;
    line-height: 300px;
&#125;
.aside&#123;
    width: 80px;
    line-height: 400px;
    background-color: violet;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>例3</strong></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2293e3a7efa4122b172928dc3e6302e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">HTML//

<div class="container">
    <div class="aside">我是侧边栏</div>
    <div class="right">
        <div class="header">我是页头</div>
        <div class="main">我是main</div>
        <div class="footer">我是页尾</div>
    </div>
</div>

CSS//

 .container&#123;
    display: flex;
    height: 500px;
    width: 500px;
    background-color: pink;
    flex-direction: row;
&#125;
.right&#123;
    display: flex;
    flex-direction: column;   //让header、main、footer纵向排列
    flex: 1;   //占满container剩余宽度
&#125;
.header&#123;
    height: 100px;   //固定高度
    width: 100%; 
    line-height: 100px;
    background-color: wheat;
    text-align: center;
&#125;
.footer&#123;
    height: 100px;   //固定高度
    background-color: yellow;
    text-align: center;
    line-height: 100px;
&#125;
.main&#123;
    width: 100%;
    flex: 1;     //占满剩余高度
    line-height: 300px;
    text-align: center;
&#125;
.aside&#123;
    width: 50px;   //固定宽度
    height: 100%;
    background-color: violet;
    line-height: 500px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结尾：还有更多的例子可以参考阮一峰老师的flex教程 本篇教程是根据阮一峰老师的flex布局教程语法篇来做出的教程 还有一篇flex布局实例篇大家可以去参考一下里面有很详细很透彻的flex布局实例解析以及代码</p>
<p>教程篇：<a href="http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html" target="_blank" rel="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2015/0…</a></p>
<p>实例篇：<a href="http://www.ruanyifeng.com/blog/2015/07/flex-examples.html" target="_blank" rel="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2015/0…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            