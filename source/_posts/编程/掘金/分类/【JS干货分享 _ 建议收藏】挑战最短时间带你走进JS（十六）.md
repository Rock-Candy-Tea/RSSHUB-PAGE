
---
title: '【JS干货分享 _ 建议收藏】挑战最短时间带你走进JS（十六）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd5ba08d3e57408cabf60f371333f369~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 16:11:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd5ba08d3e57408cabf60f371333f369~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 31 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p><strong>不知不觉也来掘金快两个月了，为了感谢掘金读者这段时间的支持，在主页放上了私人微信，有需要技术交流等可直接加阿ken微信与我交流哦</strong><br>
<br>
<strong>感激相遇 你好 我是阿ken</strong></p>
<blockquote>
<p>作者：请叫我阿ken<br>
链接：<a href="https://juejin.cn/user/1091187754155048/posts" title="https://juejin.cn/user/1091187754155048/posts" target="_blank">juejin.cn/user/109118…</a><br>
来源：掘金<br>
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。</p>
</blockquote>
<h1 data-id="heading-0"><strong>🌊🌈关于前言：</strong></h1>
<p><strong>文章部分内容及图片出自网络，如有问题请与我本人联系(主页介绍中有公众号)</strong></p>
<p><strong>本博客暂适用于刚刚接触<code>JS</code>以及好久不看想要复习的小伙伴。</strong></p>
<h1 data-id="heading-1"><strong>🌊🌈关于内容：</strong></h1>
<blockquote>
<p>DOM下</p>
</blockquote>
<h1 data-id="heading-2"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>7.2_属性操作</h1>
<p>在 HTML 中，元素有一些自带的属性，如 div 元素的属性有 id、class、title、style 。<strong>开发者也可以为元素添加自定义属性</strong>。在实际开发中，自定义属性有很广泛的应用，例如：保存一些需要在 JavaScript 中用到的数据。</p>
<h2 data-id="heading-3"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>7.2.1_获取属性值 element.属性</h2>
<p><strong>在 DOM 对象中可以使用 " element.属性 " 的方式来来获取内置的属性值，但是 DOM 对象并不能直接使用点语法获取到自定义属性的值</strong>，那么如何获取收自定义属性值呢?在 DOM 中，<strong>可以使用 getAttribute(‘属性’)方法来返回指定元素的属性值。</strong></p>
<p>案例：演示如何获取属性值，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span> <span class="hljs-attr">index</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"nav"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'div'</span>);
<span class="hljs-built_in">console</span>.log(div.id); <span class="hljs-comment">// 结果为:demo</span>
<span class="hljs-built_in">console</span>.log(div.getAttribute(<span class="hljs-string">'id'</span>)); <span class="hljs-comment">// 结果为:demo</span>
<span class="hljs-built_in">console</span>.log(div.getAttribute(<span class="hljs-string">'index'</span>)); <span class="hljs-comment">// 结果为:1</span>

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd5ba08d3e57408cabf60f371333f369~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码中，分别使用 element.属性 和 element.getAttribute 两种方式获取 div 元素的内置属性 id ,输出结果为 demo 。虽然以上两种方式都可以获取内置属性值，但是在实际运用中推荐使用 ” element. 属性 “ 这种较为简洁的方式。<br>
使用 getAttribute(‘index’) 方式来获取开发者自定义的 index 属性，输出结果为 1 。</p>
<h2 data-id="heading-4"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>7.2.2_设置属性值 element.setAttribute(‘属性’,’ 值’)</h2>
<p><strong>在 DOM 对象中可以使用 " element.属性 = ‘值’ " 的方式设置内置的属性值，并且针对于自定义属性，提供了 " element.setAttribute(‘属性’,’ 值’) " 的方式进行设置。</strong><br>
值得一提的是，设置了自定义属性的标签，在浏览器中的 HTML 结构中可以看到该属性。</p>
<p>案例：演示如何设置属性值，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'div'</span>);
div.id = <span class="hljs-string">'test'</span>;
div.className = <span class="hljs-string">'navs'</span>;
div.setAttribute(<span class="hljs-string">'index'</span>, <span class="hljs-number">2</span>);

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，使用 " element.属性 = ‘值’ " 的方式设置 div 元素内置属性，设置 id 值为 test , class 类名为 navs 。<br>
使用 setAttribute() 方法，设置属性名为 index ，值为2。</p>
<p>另外，如果想要使用 setAttribute() 方式设置元素的类名，则可以添加以下代码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">div.setAttribute (<span class="hljs-string">'class'</span>, <span class="hljs-string">'footer'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 class 比较特殊，在这里使用的属性值为 class , 值为 footer。</p>
<h2 data-id="heading-5"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>7.2.3_移除属性 element.removeAttribute( 属性)</h2>
<p>掌握了元素属性的获取和设置之后，还有一个要学习的操作，就是元素属性的移除。<br>
<strong>在DOM中使用 " element.removeAttribute( 属性) " 的方式来移除元素属性。</strong></p>
<p>案例：演示如何移除属性值，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"test"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer"</span> <span class="hljs-attr">index</span>=<span class="hljs-string">"2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'div'</span>);
div.removeAttribute(<span class="hljs-string">'id'</span>);
div.removeAttribute(<span class="hljs-string">'class'</span>);
div.removeAttribute(<span class="hljs-string">'index'</span>);

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，使用 removeAttribute() 方法移除 div 元素的id、class、index 属性。</p>
<h2 data-id="heading-6"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>7.2.4_[ 案例 ] Tab栏切换</h2>
<p>标签栏在网站中的使用非常普遍，它的优势在于可以在有限的空间内展示多块的内容，用户可以通过标签在多个内容块之间进行切换。</p>
<p>接下来我们使用自定义属性相关知识实现 Tab 栏切换效果。</p>
<p>(1) 编写 HTML 页面，示例代码如下，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"tab"</span>>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tab_list"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"current"</span>></span>商品介绍<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>规格与包装<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>售后保障<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>商品评价(50000)<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>手机社区<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">u1</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tab_con"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">" display: block; "</span>></span>商品介绍模块内容<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>规格与包装模块内容<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>售后保障模块内容<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>商品评价(50000)模块内容<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>手机社区模块内容<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，class 为 tab 的元素用于实现标签栏的外边框。第 2 ~ 10 行和第 11 ~ 17 行代码分别实现标签栏的标签部分和内容部分。其中，标签部分第 1 个 li 添加了 current 样式，用于实现当前标签的选中效果。同样的，将该标签下对应的内容块 div 也添加了 display: block 样式，用于显示当前标签下的内容，隐藏其他标签下的内容。</p>
<p>(2) 实现标签栏切换，具体代码如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
<span class="hljs-comment">// 获取标签部分的所有元素对象</span>
<span class="hljs-keyword">var</span> tab_list = <span class="hljs-built_in">document</span>.querySelector (<span class="hljs-string">' .tab_llst '</span>);
<span class="hljs-keyword">var</span> lis = tab_list.guerySelectorAll(<span class="hljs-string">'li'</span>);
<span class="hljs-comment">// 获取内容部分的所有内容对象</span>
<span class="hljs-keyword">var</span> items = <span class="hljs-built_in">document</span>.querySelectorAll (<span class="hljs-string">'.item'</span>);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;i < lis.length; i++) &#123;  <span class="hljs-comment">// for循环绑定点击事件</span>
lis[i].setAttribute (<span class="hljs-string">'index'</span>,i);
lis[i].className = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < lis.length; i++) &#123;
lis[i].className = <span class="hljs-string">''</span>;
&#125;
<span class="hljs-built_in">this</span>.className = <span class="hljs-string">'current'</span>;
<span class="hljs-comment">// 下面的显示内容模块</span>
<span class="hljs-keyword">var</span> index = <span class="hljs-built_in">this</span>.getAttribute(<span class="hljs-string">'index'</span>);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++) &#123;
items[i].style.display = <span class="hljs-string">'none'</span>;
&#125;
items[index].style.display = <span class="hljs-string">'block'</span>;
&#125;;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，第 3、4 行通过 querySeletorAIl() 方法获取元素。第 7 ~ 21 行代码用于遍历标签部分的每个元素对象 lis[i] ，并绑定单击事件。在事件处理函数中， 第 10 ~ 12 行代码利用排他思想实现单击当前项，清除所有 li 的 class 类，并且在第 13 行给自己设置 current 类。同时当事件发生时执行第 15 ~ 19 行代码，显示当前鼠标单击的标签及其对应的内容，隐藏其他标签的显示。</p>
<p><strong>今日入门学习暂时告一段落<br>
Peace</strong></p>
<h1 data-id="heading-7"><strong>🌊🌈往期回顾：</strong></h1>
<p><a href="https://juejin.cn/post/6987731486707286030" title="https://juejin.cn/post/6987731486707286030" target="_blank"><strong>阿ken的HTML、CSS的入门指南(一)_HTML基础</strong></a><br>
<a href="https://juejin.cn/post/6988080294242811918/" title="https://juejin.cn/post/6988080294242811918/" target="_blank"><strong>阿ken的HTML、CSS的入门指南(二)_HTML页面元素和属性</strong></a><br>
<a href="https://juejin.cn/post/6988714719125176351" title="https://juejin.cn/post/6988714719125176351" target="_blank"><strong>阿ken的HTML、CSS的入门指南(三)_文本样式属性</strong></a><br>
<a href="https://juejin.cn/post/6991276111527149605" title="https://juejin.cn/post/6991276111527149605" target="_blank"><strong>阿ken的HTML、CSS的入门指南(四)_CSS3选择器</strong></a><br>
<a href="https://juejin.cn/post/6991769219910074399" title="https://juejin.cn/post/6991769219910074399" target="_blank"><strong>阿ken的HTML、CSS的入门指南(五)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6992015827692159007" title="https://juejin.cn/post/6992015827692159007" target="_blank"><strong>阿ken的HTML、CSS的入门指南(六)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6992383017834512421" title="https://juejin.cn/post/6992383017834512421" target="_blank"><strong>阿ken的HTML、CSS的入门指南(七)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6992747291685699614" title="https://juejin.cn/post/6992747291685699614" target="_blank"><strong>阿ken的HTML、CSS的入门指南(八)_CSS盒子模型</strong></a><br>
<a href="https://juejin.cn/post/6993130330479656968#heading-6" title="https://juejin.cn/post/6993130330479656968#heading-6" target="_blank"><strong>阿ken的HTML、CSS的入门指南(九)_浮动与定位</strong></a><br>
<a href="https://juejin.cn/post/6993487356665790495" title="https://juejin.cn/post/6993487356665790495" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十)_浮动与定位</strong></a><br>
<a href="https://juejin.cn/post/6993855890856083487" title="https://juejin.cn/post/6993855890856083487" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十一)_浮动与定位</strong></a><br>
<a href="https://juejin.cn/post/6994207456041631780" title="https://juejin.cn/post/6994207456041631780" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十二)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6994610939089649678" title="https://juejin.cn/post/6994610939089649678" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十三)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6994995902825906207" title="https://juejin.cn/post/6994995902825906207" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十四)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6995318091039113253" title="https://juejin.cn/post/6995318091039113253" target="_blank"><strong>阿ken的HTML、CSS的入门指南(十五)_表单的应用</strong></a><br>
<a href="https://juejin.cn/post/6995721790550966302" title="https://juejin.cn/post/6995721790550966302" target="_blank"><strong>阿ken的HTML、CSS的入门指南（十六）_多媒体技术</strong></a><br>
<a href="https://juejin.cn/post/6996068586783506463" title="https://juejin.cn/post/6996068586783506463" target="_blank"><strong>阿ken的HTML、CSS的入门指南（十七）_多媒体技术</strong></a></p>
<p><a href="https://juejin.cn/post/6997535282757287950" title="https://juejin.cn/post/6997535282757287950" target="_blank"><strong>【HTML干货分享 | 建议收藏】挑战最短时间带你走进HTML（十八）</strong></a><br>
<a href="https://juejin.cn/post/6997953156730585119" title="https://juejin.cn/post/6997953156730585119" target="_blank"><strong>【HTML干货分享 | 建议收藏】挑战最短时间带你走进HTML（十九）</strong></a><br>
<a href="https://juejin.cn/post/6998293783968219149" title="https://juejin.cn/post/6998293783968219149" target="_blank"><strong>【HTML干货分享 | 建议收藏】挑战最短时间带你走进HTML（二十）</strong></a></p>
<p><a href="https://juejin.cn/post/6985072343257677855" title="https://juejin.cn/post/6985072343257677855" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（一）</strong></a><br>
<a href="https://juejin.cn/post/6987241984154927134" title="https://juejin.cn/post/6987241984154927134" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（二）</strong></a><br>
<a href="https://juejin.cn/post/6985456953661063204" title="https://juejin.cn/post/6985456953661063204" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（三）</strong></a><br>
<a href="https://juejin.cn/post/6996434668908183566" title="https://juejin.cn/post/6996434668908183566" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（四）</strong></a><br>
<a href="https://juejin.cn/post/6996819069504585736" title="https://juejin.cn/post/6996819069504585736" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（五）</strong></a><br>
<a href="https://juejin.cn/post/6997220640759496734" title="https://juejin.cn/post/6997220640759496734" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（六）</strong></a><br>
<a href="https://juejin.cn/post/6999229094839713822" title="https://juejin.cn/post/6999229094839713822" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（七）</strong></a><br>
<a href="https://juejin.cn/post/6999431171121610788" title="https://juejin.cn/post/6999431171121610788" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（八）</strong></a><br>
<a href="https://juejin.cn/post/6999797569056423967" title="https://juejin.cn/post/6999797569056423967" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（九）</strong></a><br>
<a href="https://juejin.cn/post/7000175914680057870" title="https://juejin.cn/post/7000175914680057870" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（十）</strong></a><br>
<a href="https://juejin.cn/post/7000555502988394533" title="https://juejin.cn/post/7000555502988394533" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（十一）</strong></a><br>
<a href="https://juejin.cn/post/7000892038417743885" title="https://juejin.cn/post/7000892038417743885" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（十二）</strong></a><br>
<a href="https://juejin.cn/post/7001303652673519624" title="https://juejin.cn/post/7001303652673519624" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（十三）</strong></a><br>
<a href="https://juejin.cn/post/7001658214127239205" target="_blank" title="https://juejin.cn/post/7001658214127239205"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（十四）</strong></a><br>
<a href="https://juejin.cn/post/7002053263902277668" target="_blank" title="https://juejin.cn/post/7002053263902277668"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（十五）</strong></a></p>
<h1 data-id="heading-8"><strong>🌊🌈关于后记：</strong></h1>
<p><strong>感谢阅读，希望能对你有所帮助 博文若有瑕疵请在评论区留言或在主页个人介绍中添加联系方式私聊我 感谢每一位小伙伴不吝赐教</strong></p>
<p>原创不易，<strong>「点赞」+「关注」</strong> 谢谢支持❤</p></div>  
</div>
            