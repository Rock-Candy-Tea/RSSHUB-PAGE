
---
title: '前端笔记-CSS清除浏览器默认样式｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://img-blog.csdnimg.cn/2020030609553897.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 18:26:41 GMT
thumbnail: 'https://img-blog.csdnimg.cn/2020030609553897.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://img-blog.csdnimg.cn/2020030609553897.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图我们可以看出虽然我对div和p没设置任何外边距内边距，但是他们之间还是会出现间隔。这是因为浏览器给他们设置了默认的边距。设置了默认值不要紧，但是不同浏览器会设定不同的默认值，这种默认样式在开发中会造成影响，因此我们要将其去除，使页面中的样式在所有浏览器中显示效果都相同。<strong>本文给出三种对策。</strong></p>
<h4 data-id="heading-0">可以下载我提供的文件，引入即刻生效。我在文章末尾给出了源码，也可以直接复制使用。</h4>
<p> </p>
<h1 data-id="heading-1">*通配选择器简单处理</h1>
<p>对于简单页面，使用就可以去除了，但是这种在复杂页面中是远远不够的，因此需要方法二。</p>
<pre><code class="hljs language-css copyable" lang="css">
*&#123;

       <span class="hljs-attribute">margin</span>:<span class="hljs-number">0px</span>;

       <span class="hljs-attribute">padding</span>: <span class="hljs-number">0px</span>;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h1 data-id="heading-2">CSS reset</h1>
<p>html中有那么多的标签，如果我们每次去除样式都需要去挨个消除是很麻烦的，当然这是一个普遍需求，因此已经有前人为我们做好这项工作了，我们只需要在做的时候把文件直接引入就好了。</p>
<p><strong>方法二是将所有样式都去除，但是你还要每个都重新设置，那为什么不直接找一个全部都已经设置好的呢？</strong> 这就可以用到方法三了。</p>
<p> </p>
<p>官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmeyerweb.com%2Feric%2Ftools%2Fcss%2Freset%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://meyerweb.com/eric/tools/css/reset/" ref="nofollow noopener noreferrer">meyerweb.com/eric/tools/…</a></p>
<p>引入reset之后问题就解决了。</p>
<p><img src="https://img-blog.csdnimg.cn/20200306100714301.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">/* http://meyerweb.com/eric/tools/css/reset/

   v2.0 | 20110126

   License: none (public domain)

*/</span>

html, body, div, span, applet, object, iframe,

h1, h2, h3, h4, h5, h6, p, blockquote, pre,

a, abbr, acronym, address, big, cite, code,

del, dfn, em, img, ins, kbd, q, s, samp,

small, strike, strong, sub, sup, tt, <span class="hljs-keyword">var</span>,

b, u, i, center,

dl, dt, dd, ol, ul, li,

fieldset, form, label, legend,

table, caption, tbody, tfoot, thead, tr, th, td,

article, aside, canvas, details, embed,

figure, figcaption, footer, header, hgroup,

menu, nav, output, ruby, section, summary,

time, mark, audio, video &#123;

       <span class="hljs-attr">margin</span>: <span class="hljs-number">0</span>;

       padding: <span class="hljs-number">0</span>;

       border: <span class="hljs-number">0</span>;

       font-size: <span class="hljs-number">100</span>%;

       font: inherit;

       vertical-align: baseline;

&#125;

<span class="hljs-comment">/* HTML5 display-role reset for older browsers */</span>

article, aside, details, figcaption, figure,

footer, header, hgroup, menu, nav, section &#123;

       <span class="hljs-attr">display</span>: block;

&#125;

body &#123;

       line-height: <span class="hljs-number">1</span>;

&#125;

ol, ul &#123;

       list-style: none;

&#125;

blockquote, q &#123;

       <span class="hljs-attr">quotes</span>: none;

&#125;

<span class="hljs-attr">blockquote</span>:before, <span class="hljs-attr">blockquote</span>:after,

<span class="hljs-attr">q</span>:before, <span class="hljs-attr">q</span>:after &#123;

       <span class="hljs-attr">content</span>: <span class="hljs-string">''</span>;

       content: none;

&#125;

table &#123;

       border-collapse: collapse;

       border-spacing: <span class="hljs-number">0</span>;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">CSS Normalize</h1>
<p>是一个可以定制的CSS文件，它让不同的浏览器在渲染网页元素的时候形式更统一。</p>
<p>Normalize.css 能干什么：</p>
<p>-    保留有用的默认值，不同于许多 CSS 的重置</p>
<p>-    标准化的样式，适用范围广的元素。</p>
<p>-    纠正错误和常见的浏览器的不一致性。</p>
<p>-    一些细微的改进，提高了易用性。</p>
<p> </p>
<p><img src="https://img-blog.csdnimg.cn/20200306102451772.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">使用normalize之后样式中已经设置好了各个标签的值，在所有浏览器中显示的样式都是一致的，如果要求不高的话，则可以直接使用这个。</p>
<p> </p>
<p>项目地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnecolas%2Fnormalize.css%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/necolas/normalize.css/" ref="nofollow noopener noreferrer">github.com/necolas/nor…</a></p>
<pre><code class="hljs language-css copyable" lang="css">
<span class="hljs-comment">/*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */</span>

 

<span class="hljs-comment">/* Document

   ========================================================================== */</span>

 

<span class="hljs-comment">/**

 * 1. Correct the line height in all browsers.

 * 2. Prevent adjustments of font size after orientation changes in iOS.

 */</span>

 

<span class="hljs-selector-tag">html</span> &#123;

  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">1.15</span>; <span class="hljs-comment">/* 1 */</span>

  -webkit-text-size-adjust: <span class="hljs-number">100%</span>; <span class="hljs-comment">/* 2 */</span>

&#125;

 

<span class="hljs-comment">/* Sections

   ========================================================================== */</span>

 

<span class="hljs-comment">/**

 * Remove the margin in all browsers.

 */</span>

 

<span class="hljs-selector-tag">body</span> &#123;

  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;

&#125;

 

<span class="hljs-comment">/**

 * Render the `main` element consistently in IE.

 */</span>

 

<span class="hljs-selector-tag">main</span> &#123;

  <span class="hljs-attribute">display</span>: block;

&#125;

 

<span class="hljs-comment">/**

 * Correct the font size and margin on `h1` elements within `section` and

 * `article` contexts in Chrome, Firefox, and Safari.

 */</span>

 

<span class="hljs-selector-tag">h1</span> &#123;

  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">2em</span>;

  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0.67em</span> <span class="hljs-number">0</span>;

&#125;

 

<span class="hljs-comment">/* Grouping content

   ========================================================================== */</span>

 

<span class="hljs-comment">/**

 * 1. Add the correct box sizing in Firefox.

 * 2. Show the overflow in Edge and IE.

 */</span>

 

hr &#123;

  <span class="hljs-attribute">box-sizing</span>: content-box; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">height</span>: <span class="hljs-number">0</span>; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">overflow</span>: visible; <span class="hljs-comment">/* 2 */</span>

&#125;

 

<span class="hljs-comment">/**

 * 1. Correct the inheritance and scaling of font size in all browsers.

 * 2. Correct the odd `em` font sizing in all browsers.

 */</span>

 

pre &#123;

  <span class="hljs-attribute">font-family</span>: monospace, monospace; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1em</span>; <span class="hljs-comment">/* 2 */</span>

&#125;

 

<span class="hljs-comment">/* Text-level semantics

   ========================================================================== */</span>

 

<span class="hljs-comment">/**

 * Remove the gray background on active links in IE 10.

 */</span>

 

<span class="hljs-selector-tag">a</span> &#123;

  <span class="hljs-attribute">background-color</span>: transparent;

&#125;

 

<span class="hljs-comment">/**

 * 1. Remove the bottom border in Chrome 57-

 * 2. Add the correct text decoration in Chrome, Edge, IE, Opera, and Safari.

 */</span>

 

<span class="hljs-selector-tag">abbr</span><span class="hljs-selector-attr">[title]</span> &#123;

  <span class="hljs-attribute">border-bottom</span>: none; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">text-decoration</span>: underline; <span class="hljs-comment">/* 2 */</span>

  <span class="hljs-attribute">text-decoration</span>: underline dotted; <span class="hljs-comment">/* 2 */</span>

&#125;

 

<span class="hljs-comment">/**

 * Add the correct font weight in Chrome, Edge, and Safari.

 */</span>

 

<span class="hljs-selector-tag">b</span>,

<span class="hljs-selector-tag">strong</span> &#123;

  <span class="hljs-attribute">font-weight</span>: bolder;

&#125;

 

<span class="hljs-comment">/**

 * 1. Correct the inheritance and scaling of font size in all browsers.

 * 2. Correct the odd `em` font sizing in all browsers.

 */</span>

 

<span class="hljs-selector-tag">code</span>,

<span class="hljs-selector-tag">kbd</span>,

<span class="hljs-selector-tag">samp</span> &#123;

  <span class="hljs-attribute">font-family</span>: monospace, monospace; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1em</span>; <span class="hljs-comment">/* 2 */</span>

&#125;

 

<span class="hljs-comment">/**

 * Add the correct font size in all browsers.

 */</span>

 

small &#123;

  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">80%</span>;

&#125;

 

<span class="hljs-comment">/**

 * Prevent `sub` and `sup` elements from affecting the line height in

 * all browsers.

 */</span>

 

sub,

<span class="hljs-selector-tag">sup</span> &#123;

  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">75%</span>;

  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">0</span>;

  <span class="hljs-attribute">position</span>: relative;

  <span class="hljs-attribute">vertical-align</span>: baseline;

&#125;

 

sub &#123;

  <span class="hljs-attribute">bottom</span>: -<span class="hljs-number">0.25em</span>;

&#125;

 

<span class="hljs-selector-tag">sup</span> &#123;

  <span class="hljs-attribute">top</span>: -<span class="hljs-number">0.5em</span>;

&#125;

 

<span class="hljs-comment">/* Embedded content

   ========================================================================== */</span>

 

<span class="hljs-comment">/**

 * Remove the border on images inside links in IE 10.

 */</span>

 

<span class="hljs-selector-tag">img</span> &#123;

  <span class="hljs-attribute">border-style</span>: none;

&#125;

 

<span class="hljs-comment">/* Forms

   ========================================================================== */</span>

 

<span class="hljs-comment">/**

 * 1. Change the font styles in all browsers.

 * 2. Remove the margin in Firefox and Safari.

 */</span>

 

<span class="hljs-selector-tag">button</span>,

<span class="hljs-selector-tag">input</span>,

optgroup,

select,

<span class="hljs-selector-tag">textarea</span> &#123;

  <span class="hljs-attribute">font-family</span>: inherit; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">100%</span>; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">1.15</span>; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>; <span class="hljs-comment">/* 2 */</span>

&#125;

 

<span class="hljs-comment">/**

 * Show the overflow in IE.

 * 1. Show the overflow in Edge.

 */</span>

 

<span class="hljs-selector-tag">button</span>,

<span class="hljs-selector-tag">input</span> &#123; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">overflow</span>: visible;

&#125;

 

<span class="hljs-comment">/**

 * Remove the inheritance of text transform in Edge, Firefox, and IE.

 * 1. Remove the inheritance of text transform in Firefox.

 */</span>

 

<span class="hljs-selector-tag">button</span>,

select &#123; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">text-transform</span>: none;

&#125;

 

<span class="hljs-comment">/**

 * Correct the inability to style clickable types in iOS and Safari.

 */</span>

 

<span class="hljs-selector-tag">button</span>,

<span class="hljs-selector-attr">[type=<span class="hljs-string">"button"</span>]</span>,

<span class="hljs-selector-attr">[type=<span class="hljs-string">"reset"</span>]</span>,

<span class="hljs-selector-attr">[type=<span class="hljs-string">"submit"</span>]</span> &#123;

  -webkit-appearance: button;

&#125;

 

<span class="hljs-comment">/**

 * Remove the inner border and padding in Firefox.

 */</span>

 

<span class="hljs-selector-tag">button</span>::-moz-focus-inner,

[type=<span class="hljs-string">"button"</span>]::-moz-focus-inner,

[type=<span class="hljs-string">"reset"</span>]::-moz-focus-inner,

[type=<span class="hljs-string">"submit"</span>]::-moz-focus-inner &#123;

  border-style: none;

  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;

&#125;

 

<span class="hljs-comment">/**

 * Restore the focus styles unset by the previous rule.

 */</span>

 

<span class="hljs-selector-tag">button</span>:-moz-focusring,

[type=<span class="hljs-string">"button"</span>]:-moz-focusring,

[type=<span class="hljs-string">"reset"</span>]:-moz-focusring,

[type=<span class="hljs-string">"submit"</span>]:-moz-focusring &#123;

  outline: <span class="hljs-number">1px</span> dotted ButtonText;

&#125;

 

<span class="hljs-comment">/**

 * Correct the padding in Firefox.

 */</span>

 

<span class="hljs-selector-tag">fieldset</span> &#123;

  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0.35em</span> <span class="hljs-number">0.75em</span> <span class="hljs-number">0.625em</span>;

&#125;

 

<span class="hljs-comment">/**

 * 1. Correct the text wrapping in Edge and IE.

 * 2. Correct the color inheritance from `fieldset` elements in IE.

 * 3. Remove the padding so developers are not caught out when they zero out

 *    `fieldset` elements in all browsers.

 */</span>

 

<span class="hljs-selector-tag">legend</span> &#123;

  <span class="hljs-attribute">box-sizing</span>: border-box; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">color</span>: inherit; <span class="hljs-comment">/* 2 */</span>

  <span class="hljs-attribute">display</span>: table; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">max-width</span>: <span class="hljs-number">100%</span>; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>; <span class="hljs-comment">/* 3 */</span>

  <span class="hljs-attribute">white-space</span>: normal; <span class="hljs-comment">/* 1 */</span>

&#125;

 

<span class="hljs-comment">/**

 * Add the correct vertical alignment in Chrome, Firefox, and Opera.

 */</span>

 

progress &#123;

  <span class="hljs-attribute">vertical-align</span>: baseline;

&#125;

 

<span class="hljs-comment">/**

 * Remove the default vertical scrollbar in IE 10+.

 */</span>

 

<span class="hljs-selector-tag">textarea</span> &#123;

  <span class="hljs-attribute">overflow</span>: auto;

&#125;

 

<span class="hljs-comment">/**

 * 1. Add the correct box sizing in IE 10.

 * 2. Remove the padding in IE 10.

 */</span>

 

<span class="hljs-selector-attr">[type=<span class="hljs-string">"checkbox"</span>]</span>,

<span class="hljs-selector-attr">[type=<span class="hljs-string">"radio"</span>]</span> &#123;

  <span class="hljs-attribute">box-sizing</span>: border-box; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>; <span class="hljs-comment">/* 2 */</span>

&#125;

 

<span class="hljs-comment">/**

 * Correct the cursor style of increment and decrement buttons in Chrome.

 */</span>

 

<span class="hljs-selector-attr">[type=<span class="hljs-string">"number"</span>]</span>::-webkit-inner-spin-button,

[type=<span class="hljs-string">"number"</span>]::-webkit-outer-spin-button &#123;

  height: auto;

&#125;

 

<span class="hljs-comment">/**

 * 1. Correct the odd appearance in Chrome and Safari.

 * 2. Correct the outline style in Safari.

 */</span>

 

<span class="hljs-selector-attr">[type=<span class="hljs-string">"search"</span>]</span> &#123;

  -webkit-appearance: textfield; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">outline-offset</span>: -<span class="hljs-number">2px</span>; <span class="hljs-comment">/* 2 */</span>

&#125;

 

<span class="hljs-comment">/**

 * Remove the inner padding in Chrome and Safari on macOS.

 */</span>

 

<span class="hljs-selector-attr">[type=<span class="hljs-string">"search"</span>]</span>::-webkit-search-decoration &#123;

  -webkit-appearance: none;

&#125;

 

<span class="hljs-comment">/**

 * 1. Correct the inability to style clickable types in iOS and Safari.

 * 2. Change font properties to `inherit` in Safari.

 */</span>

 

::-webkit-file-upload-button &#123;

  -webkit-appearance: button; <span class="hljs-comment">/* 1 */</span>

  <span class="hljs-attribute">font</span>: inherit; <span class="hljs-comment">/* 2 */</span>

&#125;

 

<span class="hljs-comment">/* Interactive

   ========================================================================== */</span>

 

<span class="hljs-comment">/*

 * Add the correct display in Edge, IE 10+, and Firefox.

 */</span>

 

<span class="hljs-selector-tag">details</span> &#123;

  <span class="hljs-attribute">display</span>: block;

&#125;

 

<span class="hljs-comment">/*

 * Add the correct display in all browsers.

 */</span>

 

<span class="hljs-selector-tag">summary</span> &#123;

  <span class="hljs-attribute">display</span>: list-item;

&#125;

 

<span class="hljs-comment">/* Misc

   ========================================================================== */</span>

 

<span class="hljs-comment">/**

 * Add the correct display in IE 10+.

 */</span>

 

template &#123;

  <span class="hljs-attribute">display</span>: none;

&#125;

 

<span class="hljs-comment">/**

 * Add the correct display in IE 10.

 */</span>

 

<span class="hljs-selector-attr">[hidden]</span> &#123;

  <span class="hljs-attribute">display</span>: none;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            