
---
title: 'CSS 浮动'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf60f4cff872442197d304edb05275d4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 03:44:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf60f4cff872442197d304edb05275d4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">浮动的特性</h1>
<blockquote>
<p><strong>1. 浮动主要用于使得 div 脱离标准文档流，生成多列布局<br>
2. 浮动就是让元素可以向左或向右移动，直到它的外边距碰到其父级的内边距或者是上一个元素的外边距 (这里指的上一个元素不管它有没有设置浮动，都会紧挨着上一个元素）<br>
3. 浮动元素支持所有的 css 样式 、内容撑开宽高 、多个元素设置浮动，宽度足够的话，会排在一行 、脱离文档流 、提升层级半级（也就是说：一个元素设置了浮动属性后，下一个元素就会无视这个元素的存在，但是下一个元素中的文本内容依然会为这个元素让出位置使自身的文本内容环绕在设置浮动元素的周围）。</strong></p>
</blockquote>
<blockquote>
<p><strong>注意：不管是行级还是块级元素，如果设置了浮动属性，该元素就变成了具有 inline-block 属性的元素。</strong></p>
</blockquote>
<h1 data-id="heading-1">float 属性</h1>
<table><thead><tr><th>属性</th><th>说明</th></tr></thead><tbody><tr><td>left</td><td>元素向左浮动</td></tr><tr><td>right</td><td>元素向右浮动</td></tr><tr><td>none</td><td>默认值，元素不浮动</td></tr></tbody></table>
<p><strong>下面我们用三个 div 来设置不同情况的 div 浮动来通过例子来理解 float 以及 overflow。</strong></p>
<h2 data-id="heading-2">三个 div 都不浮动</h2>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title></title>
<style>
.class1 &#123;
width: 200px;
height: 100px;
background: palegreen;
&#125;


.class2 &#123;
width: 250px;
height: 130px;
background: gold;
&#125;


.class3 &#123;
width: 300px;
height: 180px;
background: red;
&#125;
</style>
</head>
<body>



<div>我是块级元素1，没有设置浮动</div>

<div>我是块级元素2，没有设置浮动</div>

<div>我是块级元素3，没有设置浮动</div>



</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf60f4cff872442197d304edb05275d4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>在不设置浮动的情况下，三个 div 块会竖着在一列显示</p>
</blockquote>
<h2 data-id="heading-3">第一个 div 浮动</h2>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title></title>
<style>
.class1 &#123;
width: 200px;
height: 100px;
background: palegreen;
float: left
&#125;


.class2 &#123;
width: 250px;
height: 130px;
background: gold;

&#125;


.class3 &#123;
width: 300px;
height: 180px;
background: red;

&#125;
</style>
</head>
<body>



<div>块级元素1，设置浮动</div>

<div>块级元素2，没有设置浮动，块级元素2，没有设置浮动，块级元素2，没有设置浮动，块级元素2，没有设置浮动</div>

<div>块级元素3，没有设置浮动</div>



</body>
</html>



<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a30e26bd72f4a05b75db5c53c051644~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>故意将第二个 div 块中的内容写得多点，我们可以得出下面的结论：<br>
<strong>1. 没有设置浮动的元素会填充浮动元素留下来的空间<br>
2. 浮动元素会和非浮动元素发生重叠，浮动元素会在图层的最上面<br>
3. 使用浮动时，该元素会脱离文档流，后面的元素会无视这个元素，但文本依然会为这个浮动元素让出位置，并且元素中的文字内容会环绕在其周围。</strong></p>
</blockquote>
<h2 data-id="heading-4">第二个 div 浮动</h2>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title></title>
<style>
.class1 &#123;
width: 200px;
height: 100px;
background: palegreen;

&#125;


.class2 &#123;
width: 250px;
height: 130px;
background: gold;
float: left
&#125;


.class3 &#123;
width: 300px;
height: 180px;
background: red;

&#125;
</style>
</head>
<body>



<div>块级元素1，没有设置浮动</div>

<div>块级元素2，设置浮动</div>

<div>块级元素3，没有设置浮动</div>



</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7b68a2c9d0f4662991cdea05cdac5a6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>由此我们可以很明显的看出：<br>
<strong>浮动元素不会超越其前面的元素</strong></p>
</blockquote>
<h2 data-id="heading-5">三个 div 都浮动</h2>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title></title>
<style>
.class1 &#123;
width: 200px;
height: 100px;
background: palegreen;
float: left
&#125;


.class2 &#123;
width: 250px;
height: 130px;
background: gold;
float: left
&#125;


.class3 &#123;
width: 300px;
height: 180px;
background: red;
float: left
&#125;
</style>
</head>
<body>



<div>块级元素1，设置浮动</div>

<div>块级元素2，设置浮动</div>

<div>块级元素3，设置浮动</div>



</body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<strong>浏览器宽度足够时，三个 div 会并排排列 。</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bac985da4e474e6e8d9377020c0254c5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
<strong>当我们发大页面时，浏览器宽度不足以容纳最后一个 div 时，最后一个 div 掉下来，并且顶部不会超过倒数第二个 div 的底部。</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36cadc4b4ac245c08dc9e5e8d3ab4784~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">浮动的父子关系</h1>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
#wrap2 &#123;
width: 55px;
height: 90px;
border: 3px solid red;
&#125;


.class1 &#123;
width: 20px;
height: 40px;
background: blue;
float: left;
&#125;


.class2 &#123;
width: 20px;
height: 30px;
background: yellow;
float: left;
&#125;


.class3 &#123;
width: 20px;
height: 30px;
background: fuchsia;
float: left;
&#125;


.class4 &#123;
width: 20px;
height: 20px;
background: chartreuse;
float: left;
&#125;
</style>
<title></title>
</head>
<body>
<div>
<div></div>

<div></div>

<div></div>

<div></div>

</div>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68cdeb11b6474d1e8a9925c0deefa905~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>由此我们可以得到下面的结论：<br>
<strong>1. 浮动元素不会在其浮动方向上溢出父级的包含块 也就是说元素左浮动，其左外边距不会超过父级的左内边距，元素右浮动，其右外边距不会超过父级的右内边距 。<br>
2. 浮动元素的位置受到同级同向浮动元素的影响 也就是说同一父级中有多个浮动元素，后一个元素的位置会受到前一个浮动元素位置的影响，他们不会相互遮挡，后一个浮动元素会紧挨着前一个浮动元素的左外边距进行定位，如果当前空间不足，则会换行，否则会放置在前一个浮动元素的下面。</strong></p>
</blockquote>
<h2 data-id="heading-7">浮动影响父层盒子高度</h2>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
#wrap2 &#123;
width: 55px;
border: 3px solid red;
&#125;


.class1 &#123;
width: 20px;
height: 40px;
background: blue;
float: left;
&#125;


.class2 &#123;
width: 20px;
height: 30px;
background: yellow;
float: left;
&#125;


.class3 &#123;
width: 20px;
height: 30px;
background: fuchsia;
float: left;
&#125;


.class4 &#123;
width: 20px;
height: 20px;
background: chartreuse;
float: left;
&#125;
</style>
<title></title>
</head>
<body>
<div>
<div></div>

<div></div>

<div></div>

<div></div>

</div>
</body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48d256aa9aa4418bafd2600e3a9faed9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>由此我们可以得到下面的结论：<br>
<strong>父元素的高度靠子元素撑开，子元素全部浮动后，均脱离文档流，父元素高度塌陷。</strong></p>
</blockquote>
<h1 data-id="heading-8">overflow 属性</h1>
<table><thead><tr><th>overflow 属性</th><th>说明</th></tr></thead><tbody><tr><td>visible</td><td>默认值。内容不会被修剪，会呈现在盒子之外</td></tr><tr><td>hidden</td><td>内容会被修剪，并且其余内容是不可见的</td></tr><tr><td>scroll</td><td>内容会被修剪，但是浏览器会显示滚动条以便查看其余内容</td></tr><tr><td>auto</td><td>如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容</td></tr></tbody></table>
<blockquote>
<p><strong>overflow 属性的妙用：<br>
配合着浮动父容器，解决父容器高度他塌陷的问题。<br>
使用 overflow 扩展盒子高度，overflow 属性会触发浏览器重新计算父元素盒子高度。</strong></p>
</blockquote>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
#wrap2 &#123;
width: 55px;
border: 3px solid red;
overflow: hidden;
&#125;


.class1 &#123;
width: 20px;
height: 40px;
background: blue;
float: left;
&#125;


.class2 &#123;
width: 20px;
height: 30px;
background: yellow;
float: left;
&#125;


.class3 &#123;
width: 20px;
height: 30px;
background: fuchsia;
float: left;
&#125;


.class4 &#123;
width: 20px;
height: 20px;
background: chartreuse;
float: left;
&#125;
</style>
<title></title>
</head>
<body>
<div>
<div></div>

<div></div>

<div></div>

<div></div>

</div>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3888654bbcd4136a8223b9acc0ad448~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">溢出处理</h2>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <style>
            #d1&#123;
                /* 容器 */
                border: solid 1px red;
                height: 200px;
                width: 150px;
                /* overflow: visible; */
                /* overflow: hidden; */
                /* overflow : scroll; */
                /* overflow: auto; */
                overflow-x: scroll;
            &#125;

            #d2&#123;
                /* 出现移除的内容*/ 
                width: 180px;
                border: solid 2px green;
            &#125;

        </style>
    </head>
    <body>

        <div>
            <div>222222</div>

        </div>
    </body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65d0cca6c4e249f3859ae1e530b7d7b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>当 d2 的宽度超过了父级 d1 的宽度时，我们可以通过设置不同的 overflow 属性值来实现不同的解决办法，我所演示的是浏览器会显示滚动条以便查看其余内容。</strong></p>
</blockquote>
<h1 data-id="heading-10">清除浮动</h1>
<table><thead><tr><th>clear 属性</th><th>说明</th></tr></thead><tbody><tr><td>left</td><td>在左侧不允许浮动元素</td></tr><tr><td>right</td><td>在右侧不允许浮动元素</td></tr><tr><td>both</td><td>在左、右两侧不允许浮动元素</td></tr><tr><td>none</td><td>默认值，允许浮动元素出现在两侧</td></tr></tbody></table>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <style>
            .container&#123;
                border: solid 1px blue;
                
            &#125;
            .class1 &#123;
                width: 200px;
                height: 100px;
                background: palegreen;
                float: left;
            &#125;    

            .class2 &#123;
                width: 250px;
                height: 130px;
                background: gold;

                float: left;
            &#125;

            .class3 &#123;
                width: 300px;
                height: 180px;
                background: red;
                float: left;

            &#125;
            /* .clear&#123;
                clear: both;
            &#125; */
        </style>
    </head>
    <body>
        <div>
            <div>我是块级元素1</div>
            <div>我是块级元素2</div>
            <div>我是块级元素3</div>
            <div>牛哄哄的柯南牛哄哄的柯南牛哄哄的柯南牛哄哄的柯南牛哄哄的柯南</div>
        </div>

    </body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>没有清除两侧浮动效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8aaa2a99d0e467493fd08a290064ee9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
<strong>把代码中的这段代码的注释去掉，来清除两侧浮动</strong></p>
<pre><code class="copyable">/* .clear&#123;
    clear: both;
&#125; */

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>清除两侧浮动效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c16600d4cec4271b42fc49b506d96bd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>可以很明显的看出：<br>
清除两侧浮动后，有扩展父级盒子高度的作用</strong></p>
</blockquote>
<p><strong>写作不易，读完如果对你有帮助，感谢点赞支持！<br>
如果你是电脑端，看见右下角的 “一键三连” 了吗，没错点它 [哈哈]</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1c17fd001e64fb48233694fc7ac6e74~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>加油！</strong></p>
<p><strong>共同努力！</strong></p>
<p><strong>Keafmd</strong></p></div>  
</div>
            