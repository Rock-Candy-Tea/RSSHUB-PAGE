
---
title: 'html5响应式table表格布局'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/204b4b236ffb4c2480c3b2bf20fd857b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 19:58:41 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/204b4b236ffb4c2480c3b2bf20fd857b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、无边框</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/204b4b236ffb4c2480c3b2bf20fd857b~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">html代码</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
 
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"Content-Type"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"text/html; charset=UTF-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width,initial-scale=1.0,user-scalable=no"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>html5无边框响应式table表格布局<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">h5table.css.css</span>"/></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"H5Table"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">thead</span>></span>
<span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">th</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>地区<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
<span class="hljs-tag"><<span class="hljs-name">th</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>确诊<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
<span class="hljs-tag"><<span class="hljs-name">th</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>治愈<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
<span class="hljs-tag"><<span class="hljs-name">th</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>死亡<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
<span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"></<span class="hljs-name">thead</span>></span>
<span class="hljs-tag"><<span class="hljs-name">tbody</span>></span>
<span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>湖北<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>13522<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>396<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>414<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>广西<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>189<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>10<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>0<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>广东<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>762<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>25<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>2<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>湖南<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>230<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>16<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span>></span>1<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"></<span class="hljs-name">tbody</span>></span>
<span class="hljs-tag"></<span class="hljs-name">table</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
 
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">css代码</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.H5Table</span> &#123;
<span class="hljs-attribute">table-layout</span>: fixed;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
<span class="hljs-attribute">margin-top</span>: .<span class="hljs-number">5rem</span>;
<span class="hljs-attribute">padding-bottom</span>: .<span class="hljs-number">5rem</span>;
<span class="hljs-attribute">text-align</span>: center;
<span class="hljs-attribute">border-spacing</span>: <span class="hljs-number">2px</span> <span class="hljs-number">6px</span>;
<span class="hljs-attribute">font-size</span>: .<span class="hljs-number">938rem</span>;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#4d5054</span>;
<span class="hljs-attribute">border-collapse</span>: collapse;
&#125;
<span class="hljs-selector-class">.H5Table</span> <span class="hljs-selector-tag">tr</span> &#123;
<span class="hljs-attribute">height</span>: <span class="hljs-number">1.875rem</span>;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">1.875rem</span>;
&#125;
<span class="hljs-selector-class">.H5Table</span> <span class="hljs-selector-tag">td</span>,
<span class="hljs-selector-class">.H5Table</span> <span class="hljs-selector-tag">th</span> &#123;
<span class="hljs-attribute">text-align</span>: center;
<span class="hljs-attribute">width</span>: <span class="hljs-number">30%</span>;
&#125;
<span class="hljs-selector-class">.H5Table</span> <span class="hljs-selector-tag">thead</span> &#123;
<span class="hljs-attribute">font-size</span>: .<span class="hljs-number">938rem</span>
&#125;
<span class="hljs-selector-class">.H5Table</span> <span class="hljs-selector-tag">thead</span> <span class="hljs-selector-tag">tr</span> &#123;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#555</span>;
<span class="hljs-attribute">text-align</span>: center;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">1</span>
font-weight: <span class="hljs-number">700</span>;
&#125;
 
<span class="hljs-selector-class">.H5Table</span> <span class="hljs-selector-tag">tbody</span> <span class="hljs-selector-tag">tr</span> &#123;
<span class="hljs-attribute">height</span>: <span class="hljs-number">2rem</span>;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">2rem</span>;
<span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#f5f5f5</span>;
&#125;
<span class="hljs-selector-class">.H5Table</span> <span class="hljs-selector-tag">tbody</span> <span class="hljs-selector-tag">tr</span><span class="hljs-selector-pseudo">:last-child</span> &#123;
<span class="hljs-attribute">border-bottom</span>: none;
&#125;
<span class="hljs-selector-class">.H5Table</span> <span class="hljs-selector-tag">tbody</span>  <span class="hljs-selector-tag">tr</span> <span class="hljs-selector-tag">td</span> &#123;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#4d5054</span>;
&#125;
<span class="hljs-selector-class">.H5Table</span> <span class="hljs-selector-tag">tbody</span>  <span class="hljs-selector-tag">tr</span> <span class="hljs-selector-tag">td</span><span class="hljs-selector-pseudo">:first</span>-child&#123;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#00BEC7</span>;
<span class="hljs-attribute">font-weight</span>: <span class="hljs-number">700</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">有边框</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/762e560315cf445892b1cebfb3471345~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">html+css代码</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
 
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>html5响应式table表格布局<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-selector-tag">body</span> &#123;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
<span class="hljs-attribute">font-weight</span>: normal;
&#125;

<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">98%</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
<span class="hljs-attribute">border-collapse</span>: collapse;
<span class="hljs-comment">/*border-collapse:collapse合并内外边距(去除表格单元格默认的2个像素内外边距*/</span>
&#125;
<span class="hljs-comment">/* 设置表格单元格边框 */</span>

<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> <span class="hljs-selector-tag">th</span>,
<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> <span class="hljs-selector-tag">td</span> &#123;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#666</span>;
<span class="hljs-attribute">padding</span>: .<span class="hljs-number">5em</span> <span class="hljs-number">1em</span>;
&#125;
<span class="hljs-comment">/* 设置表头颜色 */</span>

<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> <span class="hljs-selector-tag">th</span> &#123;
<span class="hljs-attribute">font-weight</span>: normal;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#F2F2F2</span>;
&#125;
<span class="hljs-comment">/* 设置超链接格式 */</span>

<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> <span class="hljs-selector-class">.actions</span> <span class="hljs-selector-tag">a</span> &#123;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#ff5c00</span>;
<span class="hljs-comment">/* 设置超链接字体没有下划线 */</span>
<span class="hljs-attribute">text-decoration</span>: none;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">4px</span>;
&#125;

<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> <span class="hljs-selector-class">.number</span>,
<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> <span class="hljs-selector-class">.actions</span> &#123;
<span class="hljs-attribute">text-align</span>: center;
&#125;
<span class="hljs-comment">/* 捕捉浏览器宽度最大为480px时触发以下css样式 */</span>

<span class="hljs-keyword">@media</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">480px</span>) &#123;
<span class="hljs-comment">/* 清除其它宽度下所设置的表格样式 */</span>
<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> &#123;
-webkit-<span class="hljs-attribute">box-shadow</span>: none;
-moz-<span class="hljs-attribute">box-shadow</span>: none;
<span class="hljs-attribute">box-shadow</span>: none;
<span class="hljs-attribute">border</span>: none;
&#125;
<span class="hljs-comment">/* 隐藏表头（这里的隐藏与visiblity隐藏不同，这里的隐藏将不会为隐藏部分留下空白位置，而visiblity会为隐藏部分留下空白位置） */</span>
<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> <span class="hljs-selector-tag">thead</span> &#123;
<span class="hljs-attribute">display</span>: none;
&#125;
<span class="hljs-comment">/* 将所有表格变成块级元素，以使表格独行显示 */</span>
<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> <span class="hljs-selector-tag">td</span> &#123;
<span class="hljs-attribute">display</span>: block;
<span class="hljs-attribute">border</span>: none;
&#125;
<span class="hljs-comment">/* 设置第一例左对齐并添加颜色 */</span>
<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> <span class="hljs-selector-class">.number</span> &#123;
<span class="hljs-attribute">text-align</span>: left;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#35B558</span>;
&#125;
<span class="hljs-comment">/* 设置相对路径，以便子元素使用绝对路径 */</span>
<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> <span class="hljs-selector-tag">tr</span> &#123;
<span class="hljs-attribute">position</span>: relative;
&#125;
<span class="hljs-comment">/* 通过绝对路径设置修改删除在第一行：
　　　　　　因number的position值为static，所以number会在tr容器的第一行，
　　　　　　这里修改删除通过绝对路径，设置距tr容器上面0px，则修改删除也会出现在tr容器第一行，这里一定要设置tr位置为相对路径 */</span>
<span class="hljs-selector-tag">table</span><span class="hljs-selector-class">.responsive</span> <span class="hljs-selector-class">.actions</span> &#123;
<span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
<span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
&#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
 
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"responsive"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">thead</span>></span>
<span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">th</span>></span>程序序号<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
<span class="hljs-tag"><<span class="hljs-name">th</span>></span>课程名称<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
<span class="hljs-tag"><<span class="hljs-name">th</span>></span>课程操作<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
<span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"></<span class="hljs-name">thead</span>></span>
<span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"number"</span>></span>150406<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>移动应用开发<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"actions"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>修改<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"del"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"number"</span>></span>150407<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>HTML前段开发<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"><<span class="hljs-name">td</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"actions"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>修改<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"del"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
<span class="hljs-tag"></<span class="hljs-name">table</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
 
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            