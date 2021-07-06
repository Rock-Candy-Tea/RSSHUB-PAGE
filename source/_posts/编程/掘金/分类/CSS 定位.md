
---
title: 'CSS 定位'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/446b3a26e9ee4c8b88e5c4a1c1a01fdc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 03:43:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/446b3a26e9ee4c8b88e5c4a1c1a01fdc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">定位：</h2>
<p>·</p>
<table><thead><tr><th>position 属性</th><th>说明</th></tr></thead><tbody><tr><td>static</td><td>默认值，没有定位</td></tr><tr><td>relative</td><td>相对定位</td></tr><tr><td>absolute</td><td>绝对定位</td></tr><tr><td>fixed</td><td>固定定位</td></tr></tbody></table>、
<p>·</p>
<h2 data-id="heading-1">标准文档流</h2>
<blockquote>
<p><strong>标准文档流是指页面上从上到下, 从左到右, 网页元素一个挨一个的简单的正常的布局方式。</strong></p>
</blockquote>
<p><strong>一般在 HTML 元素分为两种：块级元素和行内元素。</strong><br>
<strong>块级元素：</strong></p>
<blockquote>
<p>块级元素是从上到下一行一行的排列，默认一个块级元素会占用一行，而跟在后面的元素会另起一行排列。<br>
像 div,p 这些的元素属于块级元素。</p>
</blockquote>
<p><strong>行内元素：</strong></p>
<blockquote>
<p>行内元素是在一行中水平布置，从左到右的排列 。span,strong 等属于行内元素</p>
</blockquote>
<h2 data-id="heading-2">static 定位</h2>
<pre><code class="copyable">position:static

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>元素没有定位，以标准流方式显示</strong><br>
<strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>position属性</title>
<style>
div &#123;
    width: 300px;
    margin:10px;
    padding:5px;
    font-size:12px;
    line-height:25px;
&#125;
#father &#123;
    width: 500px;
    margin: 50px auto;
    border:1px #666 solid;
    padding:10px;
&#125;
#first &#123;
    background-color:#FC9;
    border:1px #B55A00 dashed;
&#125;
#second &#123;
    background-color:#CCF;
    border:1px #0000A8 dashed;
&#125;
#third &#123;
    background-color:#C5DECC;
    border:1px #395E4F dashed;
&#125;
</style>
</head>
<body>
<div>
  <div>第一个盒子</div>
  <div>第二个盒子</div>
  <div>第三个盒子</div>
</div>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/446b3a26e9ee4c8b88e5c4a1c1a01fdc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">相对定位</h2>
<p><strong>relative 属性值</strong></p>
<blockquote>
<p>相对定位就是相对自身原来位置进行偏移</p>
</blockquote>
<p>偏移设置：top、left、right、bottom。</p>
<p>可以用 <strong>left</strong> 来描述盒子<strong>向右</strong>移动<br>
可以用 <strong>right</strong> 来描述盒子<strong>向左</strong>的移动<br>
可以用 <strong>top</strong> 来描述盒子<strong>向下</strong>的移动<br>
可以用 <strong>bottom</strong> 来描述 盒子的<strong>向上</strong>的移动<br>
如果是<strong>负数</strong>就是<strong>相反</strong>的方向</p>
<blockquote>
<p><strong>例如：left:10px 就是距离左边 10px（也就是往右移动 10px）</strong></p>
</blockquote>
<blockquote>
<p>相对定位的盒子，不脱离标准流，老家保留位置，其后的元素不能占用其原有位置。<br>
相对定位的主要用途是作为其内部元素绝对定位时的参照标准，相对于 “我” 而言。</p>
</blockquote>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>relative属性</title>
<style>
div &#123;
    width: 300px;
    margin:10px;
    padding:5px;
    font-size:12px;
    line-height:25px;
&#125;
#father &#123;
    width: 500px;
    margin: 50px auto;
    border:1px #666 solid;
    padding:10px;
&#125;
#first &#123;
    background-color:#FC9;
    border:1px #B55A00 dashed;
    position:relative;
    top:10px;
    left:150px;
&#125;
#second &#123;
    background-color:#CCF;
    border:1px #0000A8 dashed;
&#125;
#third &#123;
    background-color:#C5DECC;
    border:1px #395E4F dashed;
&#125;
</style>
</head>
<body>
<div>
  <div>第一个盒子</div>
  <div>第二个盒子</div>
  <div>第三个盒子</div>
</div>
</body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d46e014bb7064129a4f82c7b5a3b213b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">绝对定位</h2>
<p><strong>absolute 属性值</strong><br>
偏移设置： left、right、top、bottom。</p>
<blockquote>
<p><strong>使用了绝对定位的元素以它最近的一个 “已经定位” 的“== 祖先元素” 为基准进行偏移。如果没有已经定位的祖先元素，那么会以浏览器窗口为基准进行定位。绝对定位的元素从标准文档流中脱离，其后的元素会占据其原有的位置。</strong></p>
</blockquote>
<p><strong>样例代码 1：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>absolute属性</title>
<style>
div &#123;
    width: 300px;
    margin:10px;
    padding:5px;
    font-size:12px;
    line-height:25px;
&#125;
#father &#123;
    width: 500px;
    margin: 50px auto;
    border:1px #666 solid;
    padding:10px;
&#125;
#first &#123;
    background-color:#FC9;
    border:1px #B55A00 dashed;
    position: absolute;
    top:10px;
    right: 10px;
&#125;
#second &#123;
    background-color:#CCF;
    border:1px #0000A8 dashed;
&#125;
#third &#123;
    background-color:#C5DECC;
    border:1px #395E4F dashed;
&#125;
</style>
</head>
<body>
<div>
  <div>第一个盒子</div>
  <div>第二个盒子</div>
  <div>第三个盒子</div>
</div>
</body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图 1：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96f23707e3b148e297c0bbb65dab536c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
<strong>样例代码 2：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>absolute属性</title>
<style>
div &#123;
    width: 300px;
    margin:10px;
    padding:5px;
    font-size:12px;
    line-height:25px;
&#125;
#father &#123;
    width: 500px;
    margin: 50px auto;
    border:1px #666 solid;
    padding:10px;
    position: relative;
&#125;
#first &#123;
    background-color:#FC9;
    border:1px #B55A00 dashed;
    position: absolute;
    top:10px;
    right: 10px;
&#125;
#second &#123;
    background-color:#CCF;
    border:1px #0000A8 dashed;
&#125;
#third &#123;
    background-color:#C5DECC;
    border:1px #395E4F dashed;
&#125;

</style>
</head>
<body>
<div>
  <div>第一个盒子</div>
  <div>第二个盒子</div>
  <div>第三个盒子</div>
</div>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图 2：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e83021bbc5d245ba8960cca845bf7060~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">固定定位</h2>
<blockquote>
<p><strong>固定定位，就是始终让一个元素固定在一个位置，不管怎么滚动页面，那个固定的元素也不会改变位置。</strong></p>
</blockquote>
<pre><code class="copyable">position: fixed;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>fixed 属性值</strong><br>
偏移设置： left、right、top、bottom。</p>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
.d1 &#123;
position: fixed;
width: 100px;
height: 100px;
left: 50%;
background-color: #666666;
&#125;
</style>
<title></title>
</head>
<body>
<div>这是个固定在中间位置的div块</div>
<p>Keafmd</p>
<p>这是一句话1</p>
<p>这是一句话2</p>
<p>这是一句话3</p>
<p>这是一句话4</p>
<p>这是一句话5</p>
<p>这是一句话6</p>
<p>这是一句话7</p>
<p>这是一句话8</p>
<p>这是一句话9</p>
<p>这是一句话10</p>
<p>这是一句话11</p>
<p>这是一句话12</p>
<p>这是一句话13</p>
<p>这是一句话14</p>
<p>这是一句话15</p>
<p>这是一句话16</p>
<p>这是一句话17</p>
<p>这是一句话18</p>
<p>这是一句话19</p>
<p>这是一句话20</p>

</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图（动图）：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3491cbde46e24b82aff1e735d1fb1b13~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">z-index 属性</h2>
<p><strong>调整元素定位时重叠层的上下位置</strong></p>
<blockquote>
<p>z-index 属性值：整数，默认值为 0 设置了 positon 属性时，z-index 属性可以设置各元素之间的重叠高低关系。<br>
z-index 值大的层位于其值小的层上方。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7028d202400542c89b2a81699949a8de~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">网页元素透明度</h2>
<p><strong>CSS 设置元素透明度 opacity:x<br>
x 值为 0~1，值越小越透明</strong></p>
<blockquote>
<p>例：opacity:0.4;</p>
</blockquote>
<p><strong>filter:alpha(opacity=x)<br>
x 值为 0~100，值越小越透明</strong></p>
<blockquote>
<p>例：filter:alpha(opacity=40);</p>
</blockquote>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    .container&#123;
        position: relative;
    &#125;
    .container div&#123;
        position: absolute;
    &#125;
</style>
<title></title>
</head>
<body>
<div>
    <div>牛哄哄的柯南</div>
    <div>Keafmd</div>
    <div>一起加油</div>
</div>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48f7875577804c38a2f82fd45c38844b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">圆角边框</h2>
<p><strong>通过设置 border-radius 属性（边框圆半径）</strong><br>
<strong>↓这样设置就可以让正方形的 div 框成为圆。</strong></p>
<blockquote>
<p><strong>border-radius:50% ;</strong></p>
</blockquote>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
.d1&#123;
height: 100px; 
width: 100px;
background-color: #6495ED;
line-height:100px ;
text-align: center;
border-radius:50% ;
&#125;
</style>
<title></title>
</head>
<body>
  <div>Keafmd</div>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e39a69ce4de349329a7692bf428e57da~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
<strong>写作不易，读完如果对你有帮助，感谢点赞支持！<br>
如果你是电脑端，看见右下角的 “一键三连” 了吗，没错点它 [哈哈]</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dd011297921466d9c921b3fcb86fa09~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>加油！</strong></p>
<p><strong>共同努力！</strong></p>
<p><strong>Keafmd</strong></p></div>  
</div>
            