
---
title: 'CSS回顾总结（一）——CSS简介，语法规范，选择器，三元素'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a330226266f64e3284b1c64091213587~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 00:33:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a330226266f64e3284b1c64091213587~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>目录</strong></p>
<p> </p>
<p><a href="https://juejin.cn/post/6943136009928310815#%E4%BB%80%E4%B9%88%E6%98%AF%20CSS%3F">什么是 CSS?</a></p>
<p><a href="https://juejin.cn/post/6943136009928310815#%E8%AF%AD%E8%A8%80%E7%89%B9%E7%82%B9">语言特点</a></p>
<p><a href="https://juejin.cn/post/6943136009928310815#CSS%E7%9A%84%E4%BD%BF%E7%94%A8">CSS的使用</a></p>
<p><a href="https://juejin.cn/post/6943136009928310815#CSS%E7%9A%84%E8%AF%AD%E6%B3%95%E8%A7%84%E8%8C%83">CSS的语法规范</a></p>
<p><a href="https://juejin.cn/post/6943136009928310815#CSS%E7%9A%84%E6%B3%A8%E9%87%8A">CSS的注释</a></p>
<p><a href="https://juejin.cn/post/6943136009928310815#CSS%E5%B8%B8%E7%94%A8%E7%9A%84%E9%80%89%E6%8B%A9%E5%99%A8">CSS常用的选择器</a></p>
<p><a href="https://juejin.cn/post/6943136009928310815#id%20%E5%92%8C%20class%20%E9%80%89%E6%8B%A9%E5%99%A8">id 和 class 选择器</a></p>
<p><a href="https://juejin.cn/post/6943136009928310815#CSS%EF%BC%9A%E5%9D%97%E5%85%83%E7%B4%A0%E5%92%8C%E5%86%85%E8%81%94%E5%85%83%E7%B4%A0%EF%BC%8C%E8%A1%8C%E5%86%85%E5%9D%97%E5%85%83%E7%B4%A0">CSS：块元素和内联元素，行内块元素</a></p>
<hr>
<p>CSS是我很久之前学的了，最近有些忘记了，所以拿出来写一些博客做整理了。</p>
<h2 data-id="heading-0">什么是 CSS?</h2>
<ul>
<li>CSS 指层叠样式表 (<strong>C</strong>ascading <strong>S</strong>tyle <strong>S</strong>heets)</li>
<li>样式定义<strong>如何显示</strong> HTML 元素</li>
<li>样式通常存储在<strong>样式表</strong>中</li>
<li>把样式添加到 HTML 4.0 中，是为了<strong>解决内容与表现分离的问题</strong></li>
<li><strong>外部样式表</strong>可以极大提高工作效率</li>
<li>外部样式表通常存储在 <strong>CSS 文件</strong>中</li>
<li>多个样式定义可<strong>层叠</strong>为一个</li>
</ul>
<p>层叠样式表(英文全称:Cascading Style Sheets)是一种用来表现<a href="https://baike.so.com/doc/5869876-6082735.html" target="_blank" rel="nofollow noopener noreferrer">HTML</a>(标准通用标记语言的一个应用)或XML(标准通用标记语言的一个子集)等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。</p>
<p>CSS 能够对网页中元素位置的排版进行像素级精确控制，支持几乎所有的字体字号样式，拥有对网页对象和模型样式编辑的能力。</p>
<h2 data-id="heading-1"><strong>语言特点</strong></h2>
<p>CSS为HTML标记语言提供了一种样式描述，定义了其中元素的显示方式。CSS在Web设计领域是一个突破。利用它可以实现修改一个小的样式更新与之相关的所有页面元素。</p>
<p>总体来说，CSS具有以下特点:</p>
<p><strong>丰富的样式定义</strong></p>
<p>CSS提供了丰富的文档样式外观，以及设置文本和背景属性的能力;允许为任何元素创建边框，以及元素边框与其他元素间的距离，以及元素边框与元素内容间的距离;允许随意改变文本的大小写方式、修饰方式以及其他页面效果。</p>
<p><strong>易于使用和修改</strong></p>
<p>CSS可以将样式定义在HTML元素的style属性中，也可以将其定义在HTML文档的header部分，也可以将样式声明在一个专门的CSS文件中，以供HTML页面引用。总之，CSS样式表可以将所有的样式声明统一存放，进行统一管理。</p>
<p>另外，可以将相同样式的元素进行归类，使用同一个样式进行定义，也可以将某个样式应用到所有同名的HTML标签中，也可以将一个CSS样式指定到某个页面元素中。如果要修改样式，我们只需要在样式列表中找到相应的样式声明进行修改。</p>
<p><strong>多页面应用</strong></p>
<p>CSS样式表可以单独存放在一个CSS文件中，这样我们就可以在多个页面中使用同一个CSS样式表。CSS样式表理论上不属于任何页面文件，在任何页面文件中都可以将其引用。这样就可以实现多个页面风格的统一。</p>
<p><strong>层叠</strong></p>
<p>简单的说，层叠就是对一个元素多次设置同一个样式，这将使用最后一次设置的属性值。例如对一个站点中的多个页面使用了同一套CSS样式表，而某些页面中的某些元素想使用其他样式，就可以针对这些样式单独定义一个样式表应用到页面中。这些后来定义的样式将对前面的样式设置进行重写，在浏览器中看到的将是最后面设置的样式效果。</p>
<p><strong>页面压缩</strong></p>
<p>在使用HTML定义页面效果的网站中，往往需要大量或重复的表格和font元素形成各种规格的文字样式，这样做的后果就是会产生大量的HTML标签，从而使页面文件的大小增加。而将样式的声明单独放到CSS样式表中，可以大大的减小页面的体积，这样在加载页面时使用的时间也会大大的减少。另外，CSS样式表的复用更大程序的缩减了页面的体积，减少下载的时间。</p>
<p> </p>
<h2 data-id="heading-2">CSS的使用</h2>
<ul>
<li>方法1</li>
</ul>
<p>描述：可以将CSS编写到head中的style标签里（内部样式表）<br>
将样式表编写在style标签中，然后通过CSS选择器选择指定元素，可以为这些元素同时设置样式<br>
将样式表编写在style标签中，也可以使表现和结构进一步分离，推荐的使用方式</p>
<p>例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">title</span>></span>CSS<span class="hljs-tag"></<span class="hljs-name">title</span>></span> 
<span class="hljs-comment"><!--p&#123;&#125;中的属性设置会对所以p标签起作用--></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-selector-tag">p</span>&#123;
<span class="hljs-attribute">color</span>: blue;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>   
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>谁知盘中餐，粒粒皆辛苦<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>待到花开九月八，我花开尽百花杀<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a330226266f64e3284b1c64091213587~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<ul>
<li>方法2</li>
</ul>
<p>描述：可以将CSS样式编写到元素的style标签属性当中<br>
style后面可以写多个属性<br>
将样式直接写入style属性中，这样的样式为内联样式<br>
内联样式只对当前元素中的内容起作用,内联样式不方便重复使用<br>
内联样式属于结构和表现耦合，不方便后期的维护，不推荐使用 <br>
例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: red; font-size: 30px;"</span>></span>窗前明月光，疑是地上霜<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e474b0ff09c477288688757c364840b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>方法3</li>
</ul>
<p>描述：还可以将样式表编写到外部的CSS文件中，然后通过link标签来将外部CSS文件引用到当前页面中<br>
这样外部CSS文件将会被应用到当前文件中<br>
link中rel="stylesheet" type="text/css"固定写上去<br>
<br>
将CSS样式统一写到外部的样式表当中，完全使结构和表现分离，可以使样式表在不同的页面中使用<br>
最大限度的使样式进行复用，将样式统一写在样式表中，然后通过link进行引用，可以利用浏览器缓存<br>
加快用户访问速度，提升了用户体验，所以在开发中，最推荐使用的方式就是外部CSS文件</p>
<p>HTML代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>CSS<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"style.css"</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>谁知盘中餐，粒粒皆辛苦<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>待到花开九月八，我花开尽百花杀<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS代码：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*将p标签内容变蓝*/</span>
<span class="hljs-selector-tag">p</span>&#123;
<span class="hljs-attribute">color</span>: blue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f257543f1f834199a37ed8022c70cafd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h2 data-id="heading-3">CSS的语法规范</h2>
<p>在CSS的style中不能再使用html的标签语句了</p>
<p>CSS的注释，作用和html的类似，必须编写在style标签中，或者CSS文件中<br>
选择器     声明块</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8597aa8431a44631a99575d148bae1ec~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>选择器：通过选择器可以选中页面中指定的元素，并且将声明块应用到选择器对应的元素上。选择器通常是您需要改变样式的 HTML 元素。</p>
<p>声明块：</p>
<ul>
<li>声明块紧跟在选择器的后面，使用&#123;&#125;包含。声明块中实际上就是一组组名值对结构color名，red值                                      </li>
<li>这一组组的名值对，称为声明 ，每条声明由一个属性和一个值组成。                                                             </li>
<li>在一个声明块中，可以写多个声明，多个声明之间用；隔开。声明的样式名和样式值之间使用：连接</li>
</ul>
<h3 data-id="heading-4">CSS的注释</h3>
<p>注释是用来解释你的代码，并且可以随意编辑它，浏览器会忽略它。CSS注释以 "/*" 开始, 以 "*/" 结束</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8bd04d7acbd4f429cfa0d4d08d6cc29~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h2 data-id="heading-5">CSS常用的选择器</h2>
<h3 data-id="heading-6"><strong>id 和 class 选择器</strong></h3>
<p>如果你要在HTML元素中设置CSS样式，你需要在元素中设置"id" 和 "class"选择器。</p>
<p><strong>id 选择器</strong></p>
<p><strong>作用：通过元素的id属性值选中唯一的一个元素<br>
语法：#id属性值&#123;&#125;</strong></p>
<p>id 选择器可以为标有特定 id 的 HTML 元素指定特定的样式。</p>
<p>HTML元素以id属性来设置id选择器,CSS 中 id 选择器以 "#" 来定义。</p>
<p><strong>class 选择器</strong></p>
<p><strong>作用：通过元素的class属性值选中一组元素<br>
语法：.class属性值&#123;&#125;</strong></p>
<p>class 选择器用于描述一组元素的样式，class 选择器有别于id选择器，class可以在多个元素中使用。</p>
<p>class 选择器在HTML中以class属性表示, 在 CSS 中，类选择器以一个点"."号显示</p>
<p> </p>
<p><strong>选择器分组（并集选择器）：通过选择器分组，可以选择多个选择器对应的内容<br>
语法：选择器1，选择器2，选择器3</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#no1</span>,<span class="hljs-selector-class">.b</span>,<span class="hljs-selector-class">.k</span>&#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>通配选择器：可以选择页面中所有的元素 <br>
语法：*&#123;&#125;</strong></p>
<pre><code class="hljs language-css copyable" lang="css">*&#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复合选择器（交集选择器）：可以选择同时满足多个选择器的元素<br>
语法：选择器1选择器2选择器3</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#no1</span><span class="hljs-selector-class">.b</span><span class="hljs-selector-class">.k</span>&#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以为元素设置class属性，class属性和id属性相似，但class属性可以重复<br>
拥有相同class属性的元素，可以说是一组元素<br>
可以为一个元素同时设置多个class属性，class之间使用空格隔开</p>
<p><strong>具体示例：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">title</span>></span>常用的选择器<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-comment">/*
 * 为页面中的所以p元素设置字体为红色
 * 元素选择器：
 * 作用：通过元素选择器可以选择页面中的所有指定元素
 * 语法：标签名&#123;&#125;
 */</span>
<span class="hljs-selector-tag">p</span>&#123;
<span class="hljs-attribute">color</span>: blue;
&#125;

<span class="hljs-comment">/**
 * id选择器：
 * 作用：通过元素的id属性值选中唯一的一个元素
 * 语法：#id属性值&#123;&#125;
 */</span>
<span class="hljs-selector-id">#no1</span>&#123;
<span class="hljs-attribute">background-color</span>: red;
&#125;

<span class="hljs-comment">/*
 * 类选择器：
 * 作用：通过元素的class属性值选中一组元素
 * 语法：.class属性值&#123;&#125;
 */</span>
<span class="hljs-selector-class">.k</span>&#123;
<span class="hljs-attribute">color</span>: gold;
&#125;
<span class="hljs-selector-class">.b</span>&#123;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;

<span class="hljs-comment">/*
 * 选择器分组（并集选择器）：通过选择器分组，可以选择多个选择器对应的内容
 * 语法：选择器1，选择器2，选择器3
 */</span>
<span class="hljs-selector-id">#no1</span>,<span class="hljs-selector-class">.b</span>,<span class="hljs-selector-class">.k</span>&#123;

&#125;

<span class="hljs-comment">/*
 * 通配选择器：可以选择页面中所有的元素 
 *语法：*&#123;&#125;
 */</span>
*&#123;

&#125;

<span class="hljs-comment">/*
 * 复合选择器（交集选择器）：可以选择同时满足多个选择器的元素
 * 语法：选择器1选择器2选择器3
 */</span>
<span class="hljs-selector-id">#no1</span><span class="hljs-selector-class">.b</span><span class="hljs-selector-class">.k</span>&#123;

&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>日出东方，唯我不败<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"no1"</span>></span>锄禾日当午，汗滴禾下土<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"no2"</span>></span>锄禾日当午，汗滴禾下土<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>锄禾日当午，汗滴禾下土<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"k b"</span>></span>锄禾日当午，汗滴禾下土<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"k"</span>></span>锄禾日当午，汗滴禾下土<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"k"</span>></span>锄禾日当午，汗滴禾下土<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>锄禾日当午，汗滴禾下土<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c93dda1d49b54b85838e5dcc359e209e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h2 data-id="heading-7">CSS：块元素和内联元素，<strong>行内块元素</strong></h2>
<p><strong>描述：块元素和内联元素</strong><br>
<br>
div元素就是一个块元素，所谓的块元素就是一个独占一行的元素,无论它的内容有多少<br>
div、p、ul、li、h1~h6、dl、dt、dd元素都是块元素<br>
div这个标签没有任何语义，就是一个纯粹的块元素，且不会为它里面的元素设置任何默认样式<br>
div元素主要就是来对页面进行布局的<br>
<br>
span是一个内联元素，或者说行内元素。<br>
所谓的行内元素，指的是只占自身大小的元素，比如有多少字占多少格<br>
常见的内联元素：a,img,iframe，em，b，strong<br>
span也没有任何语义，专门用来选中文字，然后为文字设置样式</p>
<p><strong>解决内联元素间隙的方法</strong></p>
<p>1、去掉内联元素之间的换行<br>
2、将内联元素的父级设置font-size为0，内联元素自身再设置font-size<br>
<br>
块元素主要用来做页面布局，内联元素主要用来为文本设置样式<br>
一般情况下只使用块元素去包含内联元素，而不使用内联元素包含块元素<br>
a元素可以包含任意元素，除了它本身<br>
p元素中不可包含其他的块元素</p>
<p><strong>内联块元素</strong></p>
<p>内联块元素，也叫行内块元素，是新增的元素类型，现有元素没有归于此类别的，img和input元素的行为类似这种元素，但是也归类于内联元素，我们可以用display属性将块元素或者内联元素转化成这种元素。它们在布局中表现的行为：</p>
<ul>
<li>支持全部样式</li>
<li>如果没有设置宽高，宽高由内容决定</li>
<li>盒子并在一行</li>
<li>代码换行，盒子会产生间距</li>
<li>子元素是内联块元素，父元素可以用text-align属性设置子元素水平对齐方式。</li>
</ul>
<p><strong>例子：</strong></p>
<pre><code class="hljs language-python copyable" lang="python"><head>
<meta charset=<span class="hljs-string">"utf-8"</span>>
<title>块和内联</title>
</head>
<body>
<div style=<span class="hljs-string">"color: purple;"</span>>北冥有鱼，其名为鲲</div>
<div style=<span class="hljs-string">"background-color: deeppink;"</span>>鲲之大，其不知几千里也</div>
<hr />
<span >待到秋来九月八</span>
<span>我花开尽百花杀</span>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5567489ff43f4ec3a100c2f7b51fe107~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><br>
</p>
<p> </p>
<p><strong>一起学习，一起进步 -.- ，如有错误，可以发评论</strong> </p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            