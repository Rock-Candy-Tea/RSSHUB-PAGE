
---
title: 'HTML中的JavaScript'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2132'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 06:03:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=2132'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">目录</h3>
<ul>
<li>使用<code><script></code>元素</li>
<li>行内脚本与外部脚本的比较</li>
<li>文档模式对JavaScript有什么影响</li>
<li>确保JavaScript不可用时的用户体验</li>
</ul>
<h2 data-id="heading-1">使用<code><scrip></code>元素</h2>
<p><code><sript></code>元素有以下8个属性：</p>
<ul>
<li>async：可选。表示应该立即开始下载脚本，但不能阻止其他页面动作，比如下载资源或等待其他脚本加载。只对外部脚本文件有效。</li>
<li>charset：可选。使用src属性指定的代码字符集。这个属性很少使用，因为大多数浏览器不在乎它的值。</li>
<li>crossorigin</li>
<li>defer：可选。表示脚本可以延迟到文档完全被解析和显示之后再执行。只对外部脚本文件有效。在IE7及更早的版本中，对行内脚本也可以指定这个属性。</li>
<li>integrity</li>
<li>language：废弃。</li>
<li>src：可选。表示包含要执行的代码的外部文件。</li>
<li>type：可选。代替language，表示代码块中脚本语言的内容类型。按照惯例，这个值始终都是"text/javascript。</li>
</ul>
<p>两种使用方式：<br></p>
<ol>
<li>直接把代码放在<code><script></code>元素中，在<code><script></code>元素中的代码被计算完成之前，页面的其余内容不会被加载，也不会被显示。注意代码中不能出现字符串<code></script></code>，需要转义字符“\”。</li>
<li>要包含外部文件中的JavaScript，就必须使用src属性。这个属性的值是一个URL，指向包含JavaScript代码的文件，也可以是外部域，但要确保该域是可信来源。与解释行内JavaScript一样，在解释外部JavaScript文件时，页面也会阻塞。拓展名.js不是必须的，这为其它语言转译为JS提供了可能性。</li>
</ol>
<p>不管包含的是什么代码，浏览器都会按照<code><script></code>在页面中出现的顺序依次解释它们，前提是它们没有使用defer和async属性。</p>
<h3 data-id="heading-2">2.1.1 标签位置</h3>
<p>过去，所有<code><script></code>元素都被放在页面的<code><head></code>标签内，这会导致页面渲染的明显延迟，现代Web应用程序通常将所有JavaScript引用放在<code><body></code>元素中的页面内容后面，页面加载更快。</p>
<h3 data-id="heading-3">2.1.2 推迟执行脚本</h3>
<p>HTML 4.01为<code><script></code>元素定义了一个叫defer的属性，相当于告诉浏览器立即下载，但延迟执行。在HTML5中defer只对外部脚本文件有效。</p>
<h3 data-id="heading-4">2.1.3 异步执行脚本</h3>
<p>从改变脚本处理方式上看，async属性与defer类似。当然，它们两者也都只适用于外部脚本，都会告诉浏览器立即开始下载。不过，与defer不同的是，标记为async的脚本并不保证能按照它们出现的次序执行。</p>
<h3 data-id="heading-5">2.1.4 动态加载脚本</h3>
<p>通过向DOM中动态添加script元素同样可以加载指定的脚本。</p>
<pre><code class="copyable">let script = document createElement('script');
script.src = 'gibberish.js';
script.async = false;
document.head.appendChild(script);

//要想让预加载器知道这些动态请求文件的存在，可以在文档头部显式声明它们
<link ref="preload" hrefe="gibberish.js">
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.1.5 XHTML中的变化</h3>
<p>可扩展超文本标记语言（XHTML, Extensible HyperText MarkupLanguage）是将HTML作为XML的应用重新包装的结果，已退出历史舞台。</p>
<h2 data-id="heading-7">2.2 行内代码与外部文件</h2>
<p>虽然可以直接在HTML文件中嵌入JavaScript代码，但通常认为最佳实践是尽可能将JavaScript代码放在外部文件中，理由如下：</p>
<ul>
<li>可维护性：分散的JS代码会导致维护困难，用一个目录保存所有JS文件更容易维护。</li>
<li>缓存：浏览器会根据特定的设置缓存所有外部链接的JavaScript文件，这意味着如果两个页面都用到同一个文件，则该文件只需下载一次。这最终意味着页面加载更快。</li>
<li>适应未来：把JS放入外部文件中就不必考虑如XHTML的注释黑科技。</li>
</ul>
<h2 data-id="heading-8">2.3 文档模式</h2>
<p>最初的文档模式有两种：混杂模式（quirks mode）和标准模式（standardsmode）。随着浏览器的普遍实现，又出现了第三种文档模式：准标准模式（almost standardsmode）。这种模式下的浏览器支持很多标准的特性，但是没有标准规定得那么严格。主要区别在于如何对待图片元素周围的空白。<br>
准标准模式与标准模式非常接近，很少需要区分。人们在说到“标准模式”时，可能指其中任何一个。</p>
<h2 data-id="heading-9">2.4 <code><noscript></code>元素</h2>
<p>该元素被用于给不支持JavaScript的浏览器提供替代内容。在浏览器不支持脚本或浏览器对脚本的支持被关闭的情况下才会显示<code><noscript></code>元素内的内容。</p>
<h2 data-id="heading-10">2.5 小结</h2>
<p>JavaScript是通过<code><script></code>元素插入到HTML页面中的。这个元素可用于把JavaScript代码嵌入到HTML页面中，跟其他标记混合在一起，也可用于引入保存在外部文件中的JavaScript。本章的重点可以总结如下。</p>
<ul>
<li>要包含外部JavaScript文件，必须将src属性设置为要包含文件的URL。文件可以跟网页在同一台服务器上，也可以位于完全不同的域。</li>
<li>所有<code><script></code>元素会依照它们在网页中出现的次序被解释。在不使用defer和async属性的情况下，包含在<code><script></code>元素中的代码必须严格按次序解释。</li>
<li>对不推迟执行的脚本，浏览器必须解释完位于元素放到页面末尾，介于主内容之后及<code></body></code>标签之前。</li>
<li>可以使用defer属性把脚本推迟到文档渲染完毕后再执行。推迟的脚本原则上按照它们被列出的次序执行。</li>
<li>可以使用async属性表示脚本不需要等待其他脚本，同时也不阻塞文档渲染，即异步加载。异步脚本不能保证按照它们在页面中出现的次序执行。</li>
<li>通过使用<code><noscript></code>元素，可以指定在浏览器不支持脚本时显示的内容。如果浏览器支持并启用脚本，则<code><noscript></code>元素中的任何内容都不会被渲染。</li>
</ul></div>  
</div>
            