
---
title: '【task0001】HTML, CSS基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ac7497992df4f25891daf02d65ba749~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 00:53:55 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ac7497992df4f25891daf02d65ba749~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>任务目的：掌握<code>HTML</code>、<code>CSS</code>基础知识、能够较为熟练地使用<code>HTML</code>、<code>CSS</code>编写页面</p>
<p>任务前说明：本任务<strong>1-6</strong>小节的内容是面向零基础的同学，如果您已经有一定的基础，可以 跳过前面你觉得确认已经掌握的内容。
对于零基础的同学，1-5小节建议用一天时间，第6小节建议用两到三天时间。</p>
<h2 data-id="heading-0">1.建立你的第一个网页</h2>
<p>这个页面中，需要有以下内容：</p>
<ul>
<li>一个一级标题，内容是你的Github账号</li>
<li>一个无序列表，包括2个项目，里面每一个项目是一个链接，分别链接到<code>task0001.html</code>以及你的微博（或其他什么网站）</li>
<li>一个二级标题，内容随意（不能违法、反动、色情等）</li>
<li>一个段落，内容随意（不能违法、反动、色情等）</li>
<li>一个图片（不能违法、反动、色情等）。</li>
</ul>
<p>预期效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ac7497992df4f25891daf02d65ba749~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>任务解析：</p>
<ol>
<li>在h1标签中插入自己的Github账号。</li>
<li>注意段落前圆点，说明是无序排列，应用ul, li标签。插入链接因用a标签。</li>
<li>二级标题标签为h2。</li>
<li>段落标签为p。</li>
<li>图片标签为img，并在标签内的src中插入图片链接。</li>
</ol>
<p>最终代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><h1>Uris863</h1>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"task0001.html"</span>></span>HomePage<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://juejin.cn/user/369882145764535"</span>></span>Blog<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>这是一个二级标题<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是我的第一个html页面，这里有一个文字段落<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./img/1.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>最终效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e2e516a602846b0ba3d076ce371e51a~tplv-k3u1fbpfcp-watermark.image" alt="2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2.给你的网页加点样式</h2>
<p>学习以下<code>CSS</code>是怎么运作的，然后创建一个<code>task0001.css</code>的文件，并在<code>task0001.html</code>中引入它，然后我们对<code>task0001.html</code>做一些让他变得花哨一点的事情：</p>
<ul>
<li>让一级标题的文字颜色变成蓝色</li>
<li>二级标题的文字大小变成<code>14px</code></li>
<li>段落的文字大小变成<code>12px</code>，文字颜色是黄色，带一个黑色的背景色</li>
<li>图片有一个红色的，<code>2px</code>粗的边框</li>
</ul>
<p>预期效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/187747f28ea242739fb65908cda81c30~tplv-k3u1fbpfcp-watermark.image" alt="3.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>任务解析：</p>
<ol>
<li>创建一个task001.css文件，用link标签在html文件的head区域引入。</li>
<li>在css文件中在h1标签内添加 color并赋值。</li>
<li>在h2标签内添加 font-size并赋值</li>
<li>在p标签内添加 font-size, color 与 background-color并赋值。</li>
<li>在img标签内添加 border并赋值。</li>
</ol>
<p>最终代码：</p>
<pre><code class="hljs language-js copyable" lang="js">h1 &#123;
    <span class="hljs-attr">color</span>: blue;
&#125;

h2 &#123;
    font-size: 14px;
&#125;

p &#123;
   font-size: 12px;
   color: yellow;
   background-color: black;
&#125;

img &#123;
    <span class="hljs-attr">border</span>: 2px solid red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65ced00e6b8c4e97882a7ea743d596df~tplv-k3u1fbpfcp-watermark.image" alt="4.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">3. 稍微放松一下</h2>
<p>了解一下HTML及CSS的发展史，了解一下HTML4到5究竟变化了什么</p>
<p>就其核心而言， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FGlossary%2FHTML" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Glossary/HTML" ref="nofollow noopener noreferrer">HTML</a> 是一种相当简单的、由不同<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FGlossary%2F%25E5%2585%2583%25E7%25B4%25A0" title="https://developer.mozilla.org/zh-CN/docs/Glossary/%E5%85%83%E7%B4%A0" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">元素</a>组成的标记语言，它可以应用于文本片段，使文本在文档中具有不同的含义（它是一个段落吗？它是一个项目列表吗？它是一个表格吗？），将文档结构化为逻辑块（文档是否有头部？有三列内容？有一个导航菜单？），并且可以将图片，影像等内容嵌入到页面中。</p>
<p>层叠样式表（<strong>C</strong>ascading <strong>S</strong>tyle <strong>S</strong>heet，简称：CSS）是为网页添加样式的代码。和 HTML 类似，CSS 也不是真正的编程语言，甚至不是标记语言。它是一门样式表语言，这也就是说人们可以用它来选择性地为 HTML 元素添加样式。</p>
<p>了解HTML4到HTML5的变化请点击<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2Fhtml5-diff%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/html5-diff/" ref="nofollow noopener noreferrer">此处</a>。</p>
<h2 data-id="heading-3">4. CSS基础</h2>
<p>请点击<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/CSS" ref="nofollow noopener noreferrer">此处</a>。</p>
<h2 data-id="heading-4">5. 让页面丰富起来</h2>
<p>text-indent: 设置段前距，可用0，30%，-3em;<br>
text-transform: 设置首字母大写，全文大写小写等，可用capitalize, uppercase, lowercase等；<br>
text-decoration: 设置有无下划线以及下划线样式等，可用underline, dotted, red；<br>
text-align: 定义行内内容的对齐，可用left, right, center, justify等；<br>
word-spacing: 字间距设置；<br>
white-space； 设置处理元素中的空白，可用normal, no-wrap等；<br>
color: 字体颜色；<br>
line-height: 行高；<br>
font: 字体；<br>
font-family: 允许您通过给定一个有先后顺序的，由字体名或者字体族名组成的列表来为选定的元素设置字体。<br>
font-size: 字体大小。<br>
font-weight: 字体粗细。<br>
font-face: 定义了一个字体的外部属性。</p>
<h2 data-id="heading-5">6.盒模型及定位</h2>
<ul>
<li>用两种方法来实现一个背景色为<code>红色</code>、宽度为<code>960px</code>的<code><DIV></code>在浏览器中居中</li>
<li>有的圆角矩形是复杂图案，无法直接用border-radius，请在不使用border-radius的情况下实现一个可复用的高度和宽度都自适应的圆角矩形</li>
<li>用两种不同的方式来实现一个三列布局，其中左侧和右侧的部分宽度固定，中间部分宽度随浏览器宽度的变化而自适应变化</li>
<li>实现一个浮动布局，红色容器中每一行的蓝色容器数量随着浏览器宽度的变化而变化</li>
</ul>
<p>任务解析：</p>
<ol>
<li>实现div元素浏览器居中的方式:</li>
</ol>
<p>利用绝对定位，设置四个方向的值都为0，并将margin设置为auto，由于宽高固定，因此对应方向实现平分，可以实现水平和垂直方向上的居中。<br>
利用绝对定位，先将元素的左上角通过top:50%和left:50%定位到页面的中心，然后再通过margin负值来调整元素的中心点到页面的中心。<br>
使用flex布局，通过align-items:center和justify-cotent:center设置容器的垂直和水平方向上为居中对齐，然后它的子元素也可以实现垂直和水平的居中。<br>
2. 不适用border-radius的圆角矩形：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.cxyzjd.com%2Farticle%2Flllittlemud%2F104812491" target="_blank" rel="nofollow noopener noreferrer" title="http://www.cxyzjd.com/article/lllittlemud/104812491" ref="nofollow noopener noreferrer">链接</a>。<br>
3. 三列布局：</p>
<pre><code class="copyable"> .container&#123;
        display: flex;
        height: 300px;
    &#125;
    .left&#123;
        width: 100px;
        background-color: red;
    &#125;
    .middle&#123;
        flex: 1;
        background-color: green;
    &#125;
    .right&#123;
       width: 100px;
        background-color: blue;
    &#125;
   <div class="container">
    <div class="left">qqq</div>
    <div class="middle">qqq</div>
    <div class="right">wwww</div>
</div>

或者

.container&#123;
display: flex;
height: 300px;
&#125;
.left &#123;
width: 100px;
flex: 0 0 100px
&#125;
.middle &#123;
flex: 1 1 auto;
&#125;
.right &#123;
width: 100px;
flex: 0 0 100px
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>容器数量随着浏览器宽度变化而变化：</li>
</ol>
<pre><code class="copyable"><div id="float-container">
         <div class="float-element"></div>
         <div class="float-element"></div>
         <div class="float-element"></div>
         <div class="float-element"></div>
         <div class="float-element"></div>
         <div class="float-element"></div>
         <div class="float-element"></div>
         <div class="float-element"></div>
         <div class="float-element"></div>
</div>

#float-container &#123;
    background-color: red;
    height: 100%;
    width: 100%;
    overflow: hidden;
&#125;
.float-element &#123;
    float: left;
    width: 50px;
    height: 30px;
    background-color: blue;
    margin: 10px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            