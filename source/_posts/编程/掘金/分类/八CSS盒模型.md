
---
title: '八.CSS盒模型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfde9526403c4bd5a5e32d039c1a99ff~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 12 May 2021 03:24:03 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfde9526403c4bd5a5e32d039c1a99ff~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>CSS盒模型本质上是一个盒子，封装周围的HTML元素，它包括：边距，边框，填充，和实际内容。盒模型允许我们在其它元素和周围元素边框之间的空间放置元素。</p>
<p>下面的图片说明了盒子模型(Box Model)：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfde9526403c4bd5a5e32d039c1a99ff~tplv-k3u1fbpfcp-watermark.image" alt="box-sizing.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">1.外边距margin</h3>
<ul>
<li>常规流动模式下，元素之间有<code>间隔</code>的原因就是因为元素有外边距;</li>
<li>外边距的作用是在元素之间添加格外的空白，在这个空白的区域，其他元素不能共存，但是可见父元素的背景；</li>
<li>用margin属性设置外边距;属性值可以是长度单位，也可以是百分比，若果是百分比需要注意的是，百分数外边距值是相对父元素的内容区宽度计算的，上下左右相对宽度计算；</li>
<li>相邻元素外边距会发生<code>折叠现象</code>，即谁的外边距大就以谁为准；</li>
</ul>
<h4 data-id="heading-1">奇怪的现象-嵌套元素设margin</h4>
<pre><code class="hljs language-css copyable" lang="css">若果只给子元素设置<span class="hljs-attribute">margin</span>，父元素会随子元素一起往下移动，
应用：子元素在父元素内居中
    <span class="hljs-number">1</span>.子元素设置左右<span class="hljs-attribute">margin</span>：<span class="hljs-attribute">auto</span>;(为父元素的<span class="hljs-attribute">width</span>-子元素的<span class="hljs-attribute">width</span>)/<span class="hljs-number">2</span>
    <span class="hljs-number">2</span>.子元素设置上下<span class="hljs-attribute">margin</span>：;(为父元素的高度-子元素的<span class="hljs-attribute">width</span>)/<span class="hljs-number">2</span>
    <span class="hljs-number">3</span>.子元素设置上下<span class="hljs-attribute">margin</span>父元素会塌陷，给他一个BFC属性，<span class="hljs-attribute">overflow</span>:hidden;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">margin负值</h4>
<pre><code class="hljs language-css copyable" lang="css">对于<span class="hljs-attribute">margin-right</span>,<span class="hljs-attribute">margin-left</span>：
若果元素本身没有宽度，<span class="hljs-attribute">margin</span>负值会会增加元素宽度；
如果元素自身有宽度，会产生位移；（这个很有用）

<span class="hljs-attribute">margin-top</span>为负值，不管是否设置高度，都不会增加高度，而是会产生向上的位移；

<span class="hljs-attribute">margin-bottom</span>为负值的时候不会位移,而是会减少自身供css读取的高度.

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">行内元素外边距</h4>
<pre><code class="hljs language-css copyable" lang="css">行内元素一般有默认的外边距，我们并不想要这样，可以给他的父元素设置<span class="hljs-attribute">font-size</span>:<span class="hljs-number">0</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.边框线border</h3>
<pre><code class="hljs language-css copyable" lang="css">元素的内边距之外就是边框;

边框三要素：
宽度：默认<span class="hljs-number">2px</span>；
     <span class="hljs-attribute">border-width</span>:<span class="hljs-number">10px</span>;

样式：默认为<span class="hljs-attribute">none</span>；所以你看不到
即：如果缺少<span class="hljs-attribute">border-style</span>声明，就不会有边框；
    <span class="hljs-attribute">border-style</span>:solid ;
        solid:实线
        dotted：点虚线
        dashed：长虚线
        double：双线
     可以设置多个样式：
     border-style:solid dotted dashed double ;
     
     
颜色：默认为前景色，也就是<span class="hljs-attribute">color</span>；

简写边框：
连写(同时设置四条边的边框)
<span class="hljs-attribute">border</span>: 边框的宽度 边框的样式 边框的颜色;

连写(分别设置四条边的边框)
<span class="hljs-attribute">border-top</span>: 边框的宽度 边框的样式 边框的颜色;
<span class="hljs-attribute">border-right</span>: 边框的宽度 边框的样式 边框的颜色;
<span class="hljs-attribute">border-bottom</span>: 边框的宽度 边框的样式 边框的颜色;
<span class="hljs-attribute">border-left</span>: 边框的宽度 边框的样式 边框的颜色;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">边框圆角</h4>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">border-radius</span>: <span class="hljs-number">100px</span> <span class="hljs-number">100px</span> <span class="hljs-number">100px</span> <span class="hljs-number">100px</span>;
边框圆角的格式
<span class="hljs-attribute">border-radius</span>: 左上 右上 右下 左下;

<span class="hljs-number">1</span>.画⚪
对一个正方形设置；
<span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;

<span class="hljs-number">2</span>.当边框圆角的值 > 边框宽度的时候, 外边框和内边框都会变成圆角；

<span class="hljs-number">3</span>.当边框圆角的值 <= 边框宽度的时候, 外边框是圆角, 内边框是直角；

<span class="hljs-number">4</span>.设置椭圆
对一个长方形设置：<span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">图像边框</h4>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-attribute">border-image-source</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">"images/border.jpg"</span>);
 <span class="hljs-comment">/*
 告诉浏览器让哪一张图片成为边框
   注意点:
   如果只通过source指定了哪一张图片作为边框的图片, 默认情况下会将图片放到边框的四个顶点;
   如果设置了边框图片, 那么就不会显示边框颜色, 边框图片的优先级高于边框颜色
 */</span>


 <span class="hljs-attribute">border-image-slice</span>: <span class="hljs-number">70</span> <span class="hljs-number">70</span> <span class="hljs-number">70</span> <span class="hljs-number">70</span>;
 <span class="hljs-comment">/*
 告诉浏览器如何对指定的边框图片进行切割，距离顶部，右边，底部，左边70的位置各切一张，注意点: 不带单位 
 */</span>
 
 <span class="hljs-attribute">border-image-slice</span>: <span class="hljs-number">70</span> <span class="hljs-number">70</span> <span class="hljs-number">70</span> <span class="hljs-number">70</span> fill;
<span class="hljs-comment">/*中间的切割部分也用上了，按下列方式进行放置*/</span>

  <span class="hljs-attribute">border-image-width</span>: <span class="hljs-number">10px</span>;  
  <span class="hljs-comment">/*
  告诉浏览器边框图片显示的宽度, 并不是指定边框的宽度
  注意点: 
  如果通过border-image-width指定了边框图片的宽度, 那么默认的边框宽度就会失效
  */</span>


  <span class="hljs-attribute">border-image-repeat</span>: stretch; 默认
  <span class="hljs-comment">/*
  告诉浏览器除了边框图片四个角以外的图片如何填充, 默认是拉伸
     repeat;中间部分按切割好的平铺，显示不完就显示不完
     round;先平铺不够就拉伸
 */</span>
 
  <span class="hljs-attribute">border-image-outset</span>: <span class="hljs-number">10px</span> <span class="hljs-number">30px</span> <span class="hljs-number">50px</span> <span class="hljs-number">70px</span>;   
  <span class="hljs-comment">/*告诉浏览器边框图片需要向外移动多少  上   右   下   左*/</span>


  连写方式：
  <span class="hljs-attribute">border-image</span>: 资源地址 切割方式 填充模式;
  <span class="hljs-attribute">border-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">"images/border.jpg"</span>) <span class="hljs-number">70</span> fill repeat;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">3.内填充padding</h3>
<ul>
<li>内填充(内边距)是位于内容和边框之间的距离，用padding设置；它适用于所有元素，且取值只能为正；</li>
<li>background默认会延伸到内边距区域；</li>
<li>内边距的作用是使内容与边框隔开一点，所以如果加了边框，通常最好加一些内边距；</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">padding</span>：<span class="hljs-number">20px</span>；
<span class="hljs-comment">/* 上右下左都为20px */</span>

<span class="hljs-attribute">padding</span>:<span class="hljs-number">20px</span> <span class="hljs-number">10px</span>;
<span class="hljs-comment">/* 上下为20px，左右为10px*/</span>

<span class="hljs-attribute">padding</span>:<span class="hljs-number">10</span>,<span class="hljs-number">20</span>,<span class="hljs-number">30</span>;
<span class="hljs-comment">/* 第四个值是左边，没写复用第二个值*/</span>

<span class="hljs-attribute">padding</span>:<span class="hljs-number">10px</span> <span class="hljs-number">20px</span> <span class="hljs-number">30px</span> <span class="hljs-number">40px</span>;
<span class="hljs-comment">/* 顺序是上 右 下 左 */</span>

也可以按照方位单个写:
padding-top: ;
<span class="hljs-attribute">padding-right</span>: ;
<span class="hljs-attribute">padding-bottom</span>: ;
<span class="hljs-attribute">padding-left</span>: ;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">行内非置换元素的内边距</h5>
<ul>
<li>在行内元素设置padding值左右有效，上下无效（没有视觉效果）；但是要小心，如果如果行内元素有背景色和内填充，背景会向上下延伸；</li>
</ul>
<h5 data-id="heading-9">置换元素的内边距</h5>
<p>对于置换元素的内边距，会出现在内容四周，而且背景会填充到内边距区域
置换元素有</p>
<pre><code class="hljs language-css copyable" lang="css"><<span class="hljs-selector-tag">img</span>>、<<span class="hljs-selector-tag">input</span>>、<<span class="hljs-selector-tag">textarea</span>>、<select>、<<span class="hljs-selector-tag">object</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">4.内容content</h3>
<h3 data-id="heading-11">盒子的 box-sizing 属性</h3>
<p>CSS3 中新增了一个 box-sizing 属性, 这个属性的某个值可以保证我们给盒子新增 padding 和 border 之后, 盒子元素的宽度和高度不变。
有两种模式：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">box-sizing</span>: content-box;<span class="hljs-comment">/*默认情况*/</span>
        宽度 = <span class="hljs-attribute">width</span> + <span class="hljs-attribute">padding</span> + <span class="hljs-attribute">border</span>;
        高度 = <span class="hljs-attribute">height</span> + <span class="hljs-attribute">padding</span> + <span class="hljs-attribute">border</span>;
       ！！！！！！ 上边框线是一个复合属性，只写<span class="hljs-number">50px</span>是无效的，会让上边框线不存在

<span class="hljs-attribute">box-sizing</span>: border-box;
        宽度=<span class="hljs-attribute">width</span>;(<span class="hljs-attribute">padding</span>和<span class="hljs-attribute">border</span>已经算进去了)
        高度=<span class="hljs-attribute">height</span>;
<span class="hljs-attribute">border</span>-box告诉浏览器：你想要设置的边框和内边距的值是包含在<span class="hljs-attribute">width</span>内的;

注意点: 
<span class="hljs-number">1</span>.如果两个盒子是嵌套关系, 那么设置了里面一个盒子顶部的外边距, 外面一个盒子也会被顶下来 
<span class="hljs-number">2</span>.如果外面的盒子不想被一起定下来,那么可以给外面的盒子添加一个边框属性 
<span class="hljs-number">3</span>.在企业开发中, 一般情况下如果需要控制嵌套关系盒子之间的距离, 应该首先考虑 padding, 其次再考虑 margin,margin 本质上是用于控制兄弟关系之间的间隙的

注意点:
<span class="hljs-number">1</span>.在嵌套关系的盒子中, 我们可以利用 margin: <span class="hljs-number">0</span> auto;的方式来让里面的盒子在外面的盒子中水平居中
<span class="hljs-number">2</span><span class="hljs-selector-class">.margin</span>: <span class="hljs-number">0</span> auto; 只对水平方向有效, 对垂直方向无效
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            