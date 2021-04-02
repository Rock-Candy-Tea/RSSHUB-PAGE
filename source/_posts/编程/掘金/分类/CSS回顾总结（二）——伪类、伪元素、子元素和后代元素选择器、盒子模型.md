
---
title: 'CSS回顾总结（二）——伪类、伪元素、子元素和后代元素选择器、盒子模型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb8504fab2804f9cb391e677a00dfc63~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 00:33:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb8504fab2804f9cb391e677a00dfc63~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>目录</strong></p>
<p><a href="https://juejin.cn/post/6943135997483810823#%E4%BC%AA%E7%B1%BB">伪类</a></p>
<p><a href="https://juejin.cn/post/6943135997483810823#%E4%BC%AA%E5%85%83%E7%B4%A0">伪元素</a></p>
<p><a href="https://juejin.cn/post/6943135997483810823#%E5%AD%90%E5%85%83%E7%B4%A0%E5%92%8C%E5%90%8E%E4%BB%A3%E5%85%83%E7%B4%A0%E9%80%89%E6%8B%A9%E5%99%A8">子元素和后代元素选择器</a></p>
<p><a href="https://juejin.cn/post/6943135997483810823#%E7%9B%92%E5%AD%90%E6%A8%A1%E5%9E%8B">盒子模型</a></p>
<p><a href="https://juejin.cn/post/6943135997483810823#%E8%BE%B9%E8%B7%9D">边距</a></p>
<p><a href="https://juejin.cn/post/6943135997483810823#%E8%BE%B9%E6%A1%86">边框</a></p>
<p><a href="https://juejin.cn/post/6943135997483810823#%E8%BE%B9%E6%A1%86%E6%A0%B7%E5%BC%8F">边框样式</a></p>
<p><a href="https://juejin.cn/post/6943135997483810823#%E5%86%85%E8%81%94%E5%85%83%E7%B4%A0%E7%9B%92%E5%AD%90%E6%A8%A1%E5%9E%8B">内联元素盒子模型</a></p>
<hr>
<h2 data-id="heading-0">伪类</h2>
<p>伪类：专门用来表示元素的一种特殊状态<br>
*         比如：访问过的超链接，普通的超链接。获取焦点的文本框<br>
*         当我们需要为这些需要处在这些特殊状态的元素设置样式时，就可以使用伪类<br>
*         给链接设置：<br>
*             正常链接：a:link<br>
*             访问过的链接：a:visited（只能定义字体颜色）<br>
*             鼠标滑过的链接：a:hover<br>
*             正在点击的链接：a:active<br>
*             浏览器通过浏览记录判断链接是否访问过，由于涉及到用户隐私，所以visited只能定义颜色<br>
*             hover和active也可以为其他元素设置</p>
<p><strong>例子：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
 <span class="hljs-comment">/*
  * 为没访问过的链接设置一个颜色
  */</span>
 <span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:link</span>&#123;
 <span class="hljs-attribute">color</span>: purple;
 &#125; 
 <span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:hover</span>&#123;
 <span class="hljs-attribute">color</span>: gold;
 &#125; 
 <span class="hljs-comment">/*
  * :foucs:获取焦点:before:获取焦点前
  * :after:获取焦点后::selection:选中的元素
  * 文本框获取焦点以后，修改背景颜色
  */</span>
 <span class="hljs-selector-tag">input</span><span class="hljs-selector-pseudo">:focus</span>&#123;
 <span class="hljs-attribute">background-color</span>: yellowgreen;
 &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"块和内联.html"</span>></span>访问块和内联的链接<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>鼠标未移动到链接上 </p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb8504fab2804f9cb391e677a00dfc63~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>鼠标移动到超链接上</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ffa5d3d903c4410a48cb225cc83291d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>鼠标点击输入框之后</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecac1eff4f2742d2923784bcdb1e0629~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h2 data-id="heading-1">伪元素</h2>
<p><strong>CSS 伪元素用于向某些选择器设置特殊效果。</strong></p>
<p><strong>伪元素选择器：使用伪元素来表示元素中的一些特殊位置<br>
比如：首字母：:first-letter<br>
首行：:first-line<br>
:brfore ：表示元素最前面的部分，一般before都需要和content一起使用<br>
:after  ：表示元素最后面的部分，一般after都需要和content一起使用<br>
通过content可以向before和after添加一些内容，不能被选中</strong></p>
<p>伪元素的语法：</p>
<p>selector:pseudo-element &#123;property:value;&#125;</p>
<p>CSS类也可以使用伪元素：</p>
<p>selector.class:pseudo-element &#123;property:value;&#125;</p>
<p><strong>伪元素基本应用例子：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-comment">/*
 * 为p中的第一个字符来设置一个特殊的样式
 */</span>
<span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">:first</span>-letter&#123;
<span class="hljs-attribute">color</span>: blue;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>伪元素选择器<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0dfefbc3a55f49afb565f33f5395adee~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h2 data-id="heading-2">子元素和后代元素选择器</h2>
<p><strong>子元素选择器；选中指定父元素的指定子元素<br>
*         语法：父元素>子元素&#123;&#125;</strong></p>
<p><strong>例子：</strong></p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>子元素和后代元素选择器<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-comment">/*
 * 子元素选择器；选中指定父元素的指定子元素
 * 语法：父元素>子元素
 */</span>
<span class="hljs-selector-tag">div</span>><span class="hljs-selector-tag">p</span>><span class="hljs-selector-tag">span</span>&#123;
<span class="hljs-attribute">color</span>: red;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> ></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是一个div元素中的p元素<span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">span</span>></span>这是一个div元素中的p元素中的span元素<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3af81a81eb024cd59c4ed3f7e95c0f2b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>后代元素选择器：选中指定元素的指定后代元素<br>
*         语法：祖先元素 后代元素&#123;&#125;</strong></p>
<p><strong>例子：</strong></p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>子元素和后代元素选择器<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-comment">/**
 * 为div元素中的span元素设置一个颜色为红色
 * 后代元素选择器：选中指定元素的指定后代元素
 * 语法：祖先元素 后代元素&#123;&#125;
 * 
 */</span>
<span class="hljs-selector-tag">div</span> <span class="hljs-selector-class">.o</span> <span class="hljs-selector-tag">span</span>&#123;
<span class="hljs-attribute">color</span>: blue;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> ></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"o"</span>></span>这是一个div元素中的p元素<span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">span</span>></span>这是一个div元素中的p元素中的span元素<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc93618c0aee43d99b05bfcc4086540a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h2 data-id="heading-3">盒子模型</h2>
<p><strong><a href="https://www.runoob.com/css/css-boxmodel.html" target="_blank" rel="nofollow noopener noreferrer">CSS 盒子模型(Box Model)</a></strong></p>
<p>所有HTML元素可以看作盒子，在CSS中，"box model"这一术语是用来设计和布局时使用。</p>
<p>CSS盒模型本质上是一个盒子，封装周围的HTML元素，它包括：边距，边框，填充，和实际内容。</p>
<p>盒模型允许我们在其它元素和周围元素边框之间的空间放置元素。</p>
<p>一个盒子会分成几个部分：<br>
1.内容区    2.内边距    3.边框    4.外边距</p>
<p>下面的图片说明了盒子模型(Box Model)：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35cb32d88f974b19b2aab6642f89d6c8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>Margin(外边距)</strong> - 清除边框外的区域，外边距是透明的。</li>
<li><strong>Border(边框)</strong> - 围绕在内边距和内容外的边框。</li>
<li><strong>Padding(内边距)</strong> - 清除内容周围的区域，内边距是透明的。</li>
<li><strong>Content(内容)</strong> - 盒子的内容，显示文本和图像。</li>
</ul>
<h3 data-id="heading-4">边距</h3>
<p><strong>盒子可见框的宽度=border-left-width + padding-left + width +padding-right + border-right-width</strong></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc9d7ae0b9a64a9f8b1970d9ad5c7fee~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>**内边距（padding）：    盒子里内容区与边框之间的距离<br>
一共有四个方向的内边距，可以通过四个属性设置<br>
内边距会影响盒子的可见框大小，元素的背景会延伸到内边距<br>
**</p>
<p><strong>padding属性定义及使用说明</strong></p>
<p>padding 简写属性在一个声明中设置所有填充属性。该属性可以有1到4个值。</p>
<p>实例:</p>
<ul>
<li>
<p><strong>padding:10px 5px 15px 20px;</strong></p>
<ul>
<li>上填充是 10px</li>
<li>右填充是 5px</li>
<li>下填充是 15px</li>
<li>左填充是 20px</li>
</ul>
</li>
<li>
<p><strong>padding:10px 5px 15px;</strong></p>
<ul>
<li>上填充是 10px</li>
<li>右填充和左填充是 5px</li>
<li>下填充是 15px</li>
</ul>
</li>
<li>
<p><strong>padding:10px 5px;</strong></p>
<ul>
<li>上填充和下填充是 10px</li>
<li>右填充和左填充是 5px</li>
</ul>
</li>
<li>
<p><strong>padding:10px;</strong></p>
<ul>
<li>所有四个填充都是 10px</li>
</ul>
</li>
</ul>
<p>例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>边距<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-selector-class">.box1</span>&#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
<span class="hljs-attribute">background-color</span>: greenyellow;
<span class="hljs-attribute">border</span>: double;

<span class="hljs-attribute">padding-left</span>:<span class="hljs-number">100px</span> ;
<span class="hljs-attribute">padding-right</span>:<span class="hljs-number">100px</span> ;
<span class="hljs-attribute">padding-top</span>:<span class="hljs-number">100px</span> ;
<span class="hljs-attribute">padding-bottom</span>:<span class="hljs-number">100px</span> ;
&#125;
<span class="hljs-selector-id">#box2</span>&#123;
<span class="hljs-comment">/*创建一个子元素box2来覆盖父元素*/</span>
<span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
<span class="hljs-attribute">background-color</span>: royalblue;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box1"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box2"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20cd396856b8481bbb276454de69cafa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<p><strong>外边距：</strong></p>
<p><strong>可能的值</strong></p>





















<table><thead><tr><th>值</th><th>说明</th></tr></thead><tbody><tr><td>auto</td><td>设置浏览器边距。 这样做的结果会依赖于浏览器</td></tr><tr><td><em>length</em></td><td>定义一个固定的margin（使用像素，pt，em等）</td></tr><tr><td><em>%</em></td><td>定义一个使用百分比的边距</td></tr></tbody></table>
<p>margin 清除周围的（外边框）元素区域。margin 没有背景颜色，是完全透明的。</p>
<p>margin 可以单独改变元素的上，下，左，右边距，也可以一次改变所有的属性。</p>
<p><strong>外边距指的是盒子与其他盒子之间的距离，不会影响盒子可见框的大小<br>
有四个方向的外边距:</strong></p>
<ol>
<li><strong>margin-top</strong></li>
<li><strong>margin-left</strong></li>
<li><strong>margin-right</strong></li>
<li><strong>margin-bottom</strong></li>
</ol>
<p><strong>例子：</strong></p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>边距<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
 <span class="hljs-selector-class">.box3</span>&#123;
 <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
 <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
 <span class="hljs-attribute">background-color</span>: red;
 <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">50px</span>;
 <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">100px</span>;
 &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box3"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/014d3fcf1d7749cdbf4c078a951f880d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h3 data-id="heading-5">边框</h3>
<p>CSS边框属性允许你指定一个元素边框的样式和颜色。</p>
<p>为元素设置一个边框必须指定三个样式：</p>
<ol>
<li>border-width边框宽度</li>
<li>border-color边框颜色</li>
<li>border-style边框样式:solid实线，dashed虚线，dotted点状边框,double双线</li>
</ol>
<p>边框宽度可以不一致border-width:10px 20px 30px 40px;</p>
<p> </p>
<h2 data-id="heading-6">边框样式</h2>
<p>边框样式属性指定要显示什么样的边界。</p>
<p><strong>border-style</strong>属性用来定义边框的样式</p>
<p><strong>border-style 值:</strong></p>









































<table><thead><tr><th><strong>none</strong></th><th><strong>默认无边框</strong></th></tr></thead><tbody><tr><td><strong>dotted</strong></td><td><strong>定义一个点线边框</strong></td></tr><tr><td><strong>dashed</strong></td><td><strong>定义一个虚线边框</strong></td></tr><tr><td><strong>solid</strong></td><td><strong>定义实线边框</strong></td></tr><tr><td><strong>double</strong></td><td><strong>定义两个边框。 两个边框的宽度和 border-width 的值相同</strong></td></tr><tr><td><strong>groove</strong></td><td><strong>定义3D沟槽边框。效果取决于边框的颜色值</strong></td></tr><tr><td><strong>ridge</strong></td><td><strong>定义3D脊边框。效果取决于边框的颜色值</strong></td></tr><tr><td><strong>inset</strong></td><td><strong>定义一个3D的嵌入边框。效果取决于边框的颜色值</strong></td></tr><tr><td><strong>outset</strong></td><td><strong>定义一个3D突出边框。 效果取决于边框的颜色值</strong></td></tr></tbody></table>
<p><strong>例子：</strong></p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>盒子模型(框模型)<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-selector-class">.box1</span>&#123;
<span class="hljs-comment">/*
 *使用width，height来显示内容区的宽度和高度
 * */</span>
<span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">background-color</span>:yellow ;

<span class="hljs-attribute">border-width</span>:<span class="hljs-number">5px</span> ;
<span class="hljs-attribute">border-color</span>: green orange blueviolet red; 
<span class="hljs-attribute">border-style</span>:dotted ;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box1"</span>></span>

<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33499491e99b4e688083e5d23474abf7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h3 data-id="heading-7">内联元素盒子模型</h3>
<p>内联元素不能设置width和height<br>
内联元素可以设置水平方向内边距和垂直方向内边距padding-left\right\top\bottom</p>
<p>将一个内联元素变成块元素，通过display样式可以修改元素的类型</p>
<ul>
<li>inline：将一个元素变成内联元素显示</li>
<li>block：将一个元素变成块元素显示</li>
<li>inline-block:将一个元素设置为行内块元素，既可以设置宽高，又不独占一行</li>
</ul>
<p><strong>例子：</strong></p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>内联元素的盒子模型<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-selector-id">#a</span>&#123;
<span class="hljs-attribute">background-color</span>: cornflowerblue;
<span class="hljs-attribute">padding-left</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">padding-right</span>: <span class="hljs-number">50px</span>;
<span class="hljs-comment">/**内联元素支持边框，可以设置边框**/</span>
<span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> red solid;
<span class="hljs-comment">/**内联元素可以设置外边距,水平方向外边距不会重叠*/</span>
<span class="hljs-attribute">margin-right</span>: <span class="hljs-number">30px</span>;
&#125;
<span class="hljs-selector-tag">a</span>&#123;
<span class="hljs-attribute">background-color</span>: chartreuse;

<span class="hljs-attribute">display</span>: block;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
<span class="hljs-comment">/**visibility可以用来设置元素的隐藏和显示状态
 * visible:默认值，元素显示
 * hidden:元素隐藏*/</span>
<span class="hljs-attribute">visibility</span>: visible;
&#125;
<span class="hljs-selector-id">#box1</span>&#123;
<span class="hljs-attribute">background-color</span>: greenyellow;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"a"</span>></span>
这是一个span元素，有多大占多大
<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"b"</span>></span>
这是一个span元素，有多大占多大
<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box1"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>这是一个超链接<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71ad8fc5920747d1b947b11e2031ab30~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<p><strong>一起学习，一起进步 -.- ，如有错误，可以发评论</strong> </p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            