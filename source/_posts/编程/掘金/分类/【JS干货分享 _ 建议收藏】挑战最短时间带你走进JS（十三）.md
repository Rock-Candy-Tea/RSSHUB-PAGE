
---
title: '【JS干货分享 _ 建议收藏】挑战最短时间带你走进JS（十三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/217ad076ab47412a88b9ebfc69fc53b4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 18:38:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/217ad076ab47412a88b9ebfc69fc53b4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 28 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p><strong>感激相遇 你好 我是阿ken</strong></p>
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
<h1 data-id="heading-2"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3_获取元素</h1>
<p>在开发中，想要操作页面上的某个部分 ( 如控制一个 div 元素的显示或隐藏、修改 div 元素的内容等 )，需要先获取到该部分对应的元素，再对其进行操作。</p>
<p>下面我们将分别介绍<strong>获取元素的几种常见方式</strong>。</p>
<h2 data-id="heading-3"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.1_根据 id 获取元素</h2>
<p><strong>getElementById() 方法是由 document 对象提供的用于查找元素的方法。该方法返回的是拥有指定 id 的元素，如果没有找到指定 id 的元素则返回 null ，如果存在多个指定 id 的元素则返回 undefined 。需要注意的是，JavaScript 中严格区分大小写，所以在书写时一定要遵守书写规范，否则程序会报错。</strong></p>
<p>案例：演示 document.getElementById(‘id’) 方法的使用，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span>你好<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> Obox = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'box'</span>);
<span class="hljs-built_in">console</span>.log (Obox);<span class="hljs-comment">// 结果为: <div id="box">你好</div></span>
<span class="hljs-built_in">console</span>.log (<span class="hljs-keyword">typeof</span> Obox);<span class="hljs-comment">// 结果为: object</span>
<span class="hljs-built_in">console</span>.dir (Obox);<span class="hljs-comment">// 结果为: div#box</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/217ad076ab47412a88b9ebfc69fc53b4~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码中，在第2行定义了一个< div>标签，由于文档是从上往下加载的，所以第 3 ~ 8 行的 < script> 标签和 JavaScript 代码要写在第 2 行代码的下面，这样才可以正确获取到 div 元素。第 4 行代码用于获取 HTML 中 id 为 box 的元素，并赋值给变量 Obox 。需要注意的是，id 值不能像 CSS 那样加 “ # ”，如 getElementByld ( “#box” ) 是错误的。第7行的 console.dir() 方法用来在控制台中查看对象的属性和方法。</p>
<h2 data-id="heading-4"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.2_根据标签获取元素</h2>
<p><strong>根据标题名获取元素有两种方式，分别是通过 document 对象获取元素和通过 element 对象获取元素。</strong></p>
<p>代码如下所示，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">document</span>.getElementByTagName (<span class="hljs-string">'标签名'</span>);
element.getElementsByTagName (<span class="hljs-string">'标签名'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>上述代码中的 element 是元素对象的统称。通过元素对象可以查找该元素的子元素或后代元素，实现局部查找元素的效果，而 document 对象是从整个文档中查找元素。</strong></p>
<p><strong>由于相同标签名的元素可能有多个，上述方法返回的不是单个元素对象，而是一个集合。这个集合是一个类数组对象，或称为伪数组，它可以像数组一样用索引来访问元素， 但不能使用 push() 等方法。使用 Array.isArray() 也可以证明它不是一个数组。</strong></p>
<p>案例：演示，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>苹果<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>香蕉<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>西瓜<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>樱桃<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

<span class="hljs-tag"><<span class="hljs-name">ol</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"ol"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>绿色<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>蓝色<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>白色<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>红色<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ol</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> lis = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'li'</span>);
<span class="hljs-comment">// 结果为: HTMLCollection(8) [li, li, li, li, li, li, li, li]</span>
<span class="hljs-built_in">console</span>.log(lis);  

<span class="hljs-comment">// 查看集合中的索引为 0 的元素，结果为: <li>苹果</li></span>
<span class="hljs-built_in">console</span>.log(lis[<span class="hljs-number">0</span>]);

<span class="hljs-comment">//遍历集合中的所有元素</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < lis.length; i++) &#123;
<span class="hljs-built_in">console</span>.log(lis[i]);
&#125;

<span class="hljs-comment">//通过元素对象获取元素</span>
<span class="hljs-keyword">var</span> ol = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'ol'</span>);
<span class="hljs-comment">// 结果为: HTMLCollection(4) [li, li, li, li]</span>
<span class="hljs-built_in">console</span>.log (ol.getElementsByTagName(<span class="hljs-string">'li'</span>));

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://img-blog.csdnimg.cn/20201215182505576.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码中，<br>
定义了一个 < ul> 无序列表，<br>
定义了一个 id 为 ol 的 < ol> 有序列表。<br>
演示了 document.getElementsByTagName() 的用法，其中返回的是所有 < li> 标签元素对象的集合。</p>
<p>需要注意的是，即使页面中只有一个 li 元素，返回结果仍然是一个集合，如果页面中没有该元素，那么将会返回一个空的集合。</p>
<p>通过代码的输出结果可以看出，lis 是一个包含 8 个 li 元索的集合对象，这个对象的构造函数是 HTMLCollection 。<br>
返回集合中的第 1 个 li 元素。<br>
采用遍历的方式依次打印了集合里面的元素对象。<br>
演示了 element.getElementsByName() 的用法，这里的 element 必须是单个对象，不能是一个集合，所以需要用 document.getElementsById() 获取元素，再调用方法。<br>
使用 getElementsByTagName() 去获取 ol 中的所有 li 元素。</p>
<ul>
<li>注意：<br>
_<br>
getElementsByTagName() 方法获取到的集合是动态集合， 也就是说， 当页面增加了标签，这个集合中也会自动增加元素。</li>
</ul>
<h2 data-id="heading-5"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.3_根据 name 获取元素</h2>
<p><strong>通过 name 属性来获取元素应使用 document.getElementsByName() 方法，一般用于获取表单元素。</strong></p>
<p><strong>name 属性的值不要求必须是唯一的， 多个元素也可以有同样的名字，如表单中的单选框和复选框。</strong></p>
<p>案例：演示复选框，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>请选择你最喜欢的水果(多选)<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">label</span>></span><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"fruit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"苹果"</span>></span>苹果<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">label</span>></span><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"fruit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"香蕉"</span>></span>香蕉<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">label</span>></span><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"fruit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"西瓜"</span>></span>西瓜<span class="hljs-tag"></<span class="hljs-name">label</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> fruits = <span class="hljs-built_in">document</span>.getElementsByName(<span class="hljs-string">'fruit'</span>);
fruits[<span class="hljs-number">0</span>].checked = <span class="hljs-literal">true</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a91d268fb28e4cadb376a719cc75264d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上述代码中，getElementsByName() 方法返回的是一个对象集合， 使用索引获取元素。fruit [0].checked 为 true，表示将 fruits 中的第1个元素的 checked 属性值设置为 true ，表示将这一项勾选。</p>
<h2 data-id="heading-6"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.4_HTML5 新增的获取方式</h2>
<blockquote>
<p>HTML5 中为 document 对象新增了 getElementsByClassName()、 querySelector() 和 querySelectorAIl() 方法，在使用时需要考虑到浏览器的兼容性问题。</p>
</blockquote>
<h3 data-id="heading-7"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>1. 根据类名获取 document.ElementsByClassName()</h3>
<p><strong>document.ElementsByClassName() 方法，用于通过类名来获得某些元素集合。</strong></p>
<p>下面通过案例代码进行演示，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>



<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"one"</span>></span>英语<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"two"</span>></span>数学<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"one"</span>></span>语文<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"two"</span>></span>物理<span class="hljs-tag"></<span class="hljs-name">span</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">var</span> Ospan1 = <span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">'one'</span>);
<span class="hljs-keyword">var</span> Ospan2 = <span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">'two'</span>);
Ospan1[<span class="hljs-number">0</span>].style.fontWeight = <span class="hljs-string">'bold'</span>;
Ospan2[<span class="hljs-number">1</span>].style.background = <span class="hljs-string">'red'</span>;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aa92f73780a4c2d8d5ec8408590b647~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码中，分别使用 getElementsByClassName() 方法获取类名为 one 和 two 的集合，并分别存储在 Ospan1 和 Ospan2 中。使用下标的形式，查找并设置 Ospan1 数组中下标为 0 所对应的第 1 个元素的 fontWeight 属性为 bold，Ospan2 数组中下标为 1 所对应的第 2 个元素的 backgound 属性为 red 。</p>
<h3 data-id="heading-8"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>2. querySelector() 和querySelectorAIl()</h3>
<p><strong>querySelector() 方法用于返回指定选择器的第一个元素对象。querySelectorAll() 方法用于返回指定选择器的所有元素对象集合。</strong></p>
<p>案例：演示，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>盒子1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>盒子2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nav"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>产品<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">var</span> firstBox = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.box'</span>);
<span class="hljs-built_in">console</span>.log(firstBox); <span class="hljs-comment">// 获取class为box的第1个div</span>

<span class="hljs-keyword">var</span> nav = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#nav'</span>);
<span class="hljs-built_in">console</span>.log(nav); <span class="hljs-comment">// 获取id为nav的第1个div</span>

<span class="hljs-keyword">var</span> li = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'li'</span>);
<span class="hljs-built_in">console</span>.log(li); <span class="hljs-comment">// 获取匹配到的第1个li</span>

<span class="hljs-keyword">var</span> allBox = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'.box'</span>);
<span class="hljs-built_in">console</span>.log(allBox); <span class="hljs-comment">// 获取class为box的所有div</span>

<span class="hljs-keyword">var</span> lis = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'li'</span>);
<span class="hljs-built_in">console</span>.log(lis); <span class="hljs-comment">// 获取匹配到的所有li</span>

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eab6151f45d64657bda2afb08c111c16~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上述代码可以看出，在利用 querySelector() 和 querySelectorAlI() 方法获取操作的元素时，直接书写标签名或 CSS 选择器名称即可。 根据类名获取元素时在类名前面加上 “.”，根据 id 获取元素时在 id 前面加上 “#” 。</p>
<h2 data-id="heading-9"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.5_document 对象的属性</h2>
<p><strong>document 对象提供了一些属性， 可用于获取文档中的元素</strong>，例如，获取所有表单标签、图片标签等。</p>
<p><strong>document 对象的属性：</strong></p>





























<table><thead><tr><th>属性</th><th>说明</th></tr></thead><tbody><tr><td>document.body</td><td>返回文档的body元素</td></tr><tr><td>document.title</td><td>返回文档的title元素</td></tr><tr><td>document.documentElement</td><td>返回文档的html元素</td></tr><tr><td>document.forms</td><td>返回对文档中所有Form对象的引用</td></tr><tr><td>document.images</td><td>返回对文档中所有Image对象的引用</td></tr></tbody></table>
<p><strong>document 对象中的 body 属性用于返回 body 元素，而 documentElement 属性用于返回 HTML 文档的根节点 html 元素。</strong></p>
<p>案例：演示 获取 body 元素和 html 元素，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">var</span> bodyEle = <span class="hljs-built_in">document</span>.body;
<span class="hljs-built_in">console</span>.dir(bodyEle);

<span class="hljs-keyword">var</span> htmlEle = <span class="hljs-built_in">document</span>.documentElement;
<span class="hljs-built_in">console</span>.log(htmlEle);

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://img-blog.csdnimg.cn/20201215192251505.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码中，第 3、4 行代码通过 document.body 的方式获取 body 元素，并通过 console.dir() 的方式在控制台打印出结果。第 5、6 行代码通过 document.documentElement 的方式获取 html 元素，并输出结果。</p>
<p><strong>今日入门学习暂时告一段落<br>
Peace</strong></p>
<h1 data-id="heading-10"><strong>🌊🌈往期回顾：</strong></h1>
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
<a href="https://juejin.cn/post/7000555502988394533" target="_blank" title="https://juejin.cn/post/7000555502988394533"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（十一）</strong></a><br>
<a href="https://juejin.cn/post/7000892038417743885" target="_blank" title="https://juejin.cn/post/7000892038417743885"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（十二）</strong></a></p>
<h1 data-id="heading-11"><strong>🌊🌈关于后记：</strong></h1>
<p><strong>感谢阅读，希望能对你有所帮助 博文若有瑕疵请在评论区留言或在主页个人介绍中添加联系方式私聊我 感谢每一位小伙伴不吝赐教</strong></p>
<p>原创不易，<strong>「点赞」+「关注」</strong> 谢谢支持❤</p></div>  
</div>
            