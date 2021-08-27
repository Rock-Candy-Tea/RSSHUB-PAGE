
---
title: '【建议收藏_熬夜爆肝】万字文带你了解DOM，文末有彩蛋嗷!!!!✨✨✨'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/217ad076ab47412a88b9ebfc69fc53b4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 15:56:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/217ad076ab47412a88b9ebfc69fc53b4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 27 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
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
<blockquote>
<p>JavaScript DOM上</p>
</blockquote>
<h1 data-id="heading-2"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.1_Web API简介</h1>
<p>Web API 是浏览器提供的一套操作浏览器功能和页面元素的接口。</p>
<p>例如，在前面的学习中，经常使用的 console.log() 就是一个接口。 这里的 console 对象表示浏览器的控制台，调用它的 log() 方法就可以在控制台中输出调试信息。</p>
<h2 data-id="heading-3"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.1.1_初识Web API</h2>
<p><strong>JavaScript 语言由3部分组成，分别是 ECMAScript ( JavaScript 语法 )、BOM( 页面文档对象模型 ) 和 DOM ( 浏览器对象模型 )</strong> ，其中 ECMAScript 是 JavaScript 语言的核心，它的内容包括前面学习的 JavaScript 基本语法、 数组、函数和对象等，即 JavaScript 基础。而 <strong>Web API 包括 BOM 和 DOM 两部分</strong>。</p>
<p>在学习 JavaScript 时，基础阶段学习的是 ECMAScript 的基础语法，是为学习 Web API 部分做前期的铺垫；学习 Web API 阶段是 JavaScript 的实战应用。在这一阶段将会大量使用 JavaScript 基础语法来实现网页的交互效果。</p>
<h2 data-id="heading-4"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.1.2_Web API 与 API 的关系</h2>
<h3 data-id="heading-5"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>1. API</h3>
<p>_<br>
<strong>应用程序编程接口 ( Application Prgramming Interface，API）是一些预先定义的函数，这些函数是由某个软件开放给开发人员使用的，帮助开发者实现某种功能。开发人员无须访问源码、无须理解其内部工作机制细节，只需知道如何使用即可</strong>。<br>
_<br>
例如，开发一个美颜相机的手机应用。该应用需要调起手机上的摄像头来拍摄画面，如果没有 API ，则开发这个应用将无从下手。因此，手机的操作系统为了使其他应用具有访同手机摄像头的能力，就开放了一套 API ，然后由手机应用的开发工具将 API 转换成一个可以被直接调用的函数。直接调用函数就能完成调用摄像头，获取摄像头拍摄的画面等功能。开发人员的主要工作是查阅 API 文档，了解 API 如何使用。</p>
<h3 data-id="heading-6"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>2. Web API</h3>
<p>_<br>
<strong>Web API是主要针对浏览器的 API ，在 JavaScript 语言中被封装成了对象，通过调用对象的属性和方法就可以使用 Web API</strong>。在前面的学习中，经常使用 console.log() 在控制台中输出调试信息，这里的 console 对象就是一个 Web API 。</p>
<p>案例：使用 document.title 属性获取或设置页面的标题、使用 document.write 方法写人页面内容，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">document</span>.title = <span class="hljs-string">'设置新标题'</span>;<span class="hljs-comment">// 设置页面标题</span>
<span class="hljs-built_in">console</span>.log (<span class="hljs-built_in">document</span>.title);<span class="hljs-comment">// 获取页面标题</span>
<span class="hljs-built_in">document</span>.write (<span class="hljs-string">'<h1>网页内容</h1>'</span>);<span class="hljs-comment">// 将字符串写入页面</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.2_DOM 简介</h1>
<h2 data-id="heading-8"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.2.1_什么是 DOM</h2>
<p><strong>文档对象模型 ( Document Object Model, DOM )，是 W3C 组织推荐的处理可扩展标记语言 ( HTML或者XML ) 的标准编程接口。</strong></p>
<p>W3C 定义了一系列的 DOM 接口，利用 DOM 可完成对 HTML 文档内所有元素的获取、访问、标签属性和样式的设置等操作。在实际开发中，诸如改变盒子的大小、标签栏的切换、购物车功能等带有交互效果的页面，都离不开 DOM。</p>
<h2 data-id="heading-9"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.2.2_DOM 树</h2>
<p><strong>DOM 中将 HTML 文档视为树结构，所以被称之为文档树模型，把文档映射成树形结构，通过节点对象对其处理，处理的结果可以加人到当前的页面。</strong></p>
<p>树</p>
<p>上图展示了 DOM 树中各节点之间的关系后，接下来我们针对 DOM 中的专有名词进行解释，具体如下：</p>
<ul>
<li><strong>文档 ( document ): 一个页面就是一个文档 。</strong></li>
<li><strong>元素 ( element ): 页面中的所有标签都是元素。</strong></li>
<li><strong>节点 ( node ): 网页中的所有内容，在文档树中都是节点 ( 如元素节点、属性节点、文本节点、注释节点等 )。DOM 会把所有的节点都看作是对象，这些对象拥有自己的属性和方法。</strong></li>
</ul>
<h1 data-id="heading-10"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3_获取元素</h1>
<p>在开发中，想要操作页面上的某个部分 ( 如控制一个 div 元素的显示或隐藏、修改 div 元素的内容等 )，需要先获取到该部分对应的元素，再对其进行操作。</p>
<p>下面我们将分别介绍<strong>获取元素的几种常见方式</strong>。</p>
<h2 data-id="heading-11"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.1_根据 id 获取元素</h2>
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
<h2 data-id="heading-12"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.2_根据标签获取元素</h2>
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
<h2 data-id="heading-13"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.3_根据 name 获取元素</h2>
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
<h2 data-id="heading-14"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.4_HTML5 新增的获取方式</h2>
<blockquote>
<p>HTML5 中为 document 对象新增了 getElementsByClassName()、 querySelector() 和 querySelectorAIl() 方法，在使用时需要考虑到浏览器的兼容性问题。</p>
</blockquote>
<h3 data-id="heading-15"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>1. 根据类名获取 document.ElementsByClassName()</h3>
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
<h3 data-id="heading-16"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>2. querySelector() 和querySelectorAIl()</h3>
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
<h2 data-id="heading-17"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.5_document 对象的属性</h2>
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
<h1 data-id="heading-18"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.4_事件基础</h1>
<p><strong>在获取到元素后，如果需要为元素添加交互行为，这就需要用到事件来实现。</strong></p>
<p>例如，当鼠标指针经过导航栏中的某一项时，自动展开二级菜单，或者在阅读文章时，选中文本后自动弹出分享、复制等选项。</p>
<h2 data-id="heading-19"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.4.1_事件概述</h2>
<p><strong>在开发中，JavaScript 帮助开发者创建带有交互效果的页面，是依靠事件来实观的</strong>。</p>
<p><strong>事件是指可以被 JavaScript 侦测到的行为，是一种 " 触发-响应 " 的机制。</strong></p>
<p>这些行为指的就是页面的加载、鼠标单击页面、鼠标指针滑过某个区域等具体的动作，它对实现网页的交互效果起着重要的作用。</p>
<h2 data-id="heading-20"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.4.2_事件三要素</h2>
<p>在学习事件时，我们需要对一些非常基本又相当重要的概念有一定的了解。 <strong>事件由事件源、事件类型和事件处理程序这 3 部分组成</strong>，又称为事件三要素，具体解释如下。</p>
<p><strong>(1) 事件源: 触发事件的元素。</strong></p>
<p><strong>(2) 事件类型: 如 click 单击事件。</strong></p>
<p><strong>(3) 事件处理程序: 事件触发后要执行的代码 ( 函数形式 )，也称事件处理函数。</strong></p>
<p>以上三要素可以简单理解为 " 谁触发了事件 " " 触发了什么事件 " " 触发事件以后要做什么 " 。</p>
<p>在开发中，为了让元素在触发事件时执行特定的代码，需要为元素注册事件，绑定事件处理函数。具体步骤是，首先获取元素，其次注册事件，最后编写事件处理代码。</p>
<p>案例：演示事件的使用 —— 为按钮绑定单击事件，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span>></span>单击<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

    <span class="hljs-comment">// 第1步:获取事件源</span>
<span class="hljs-keyword">var</span> btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>);
 
<span class="hljs-comment">// 第2步:注册事件btn.onclick</span>
btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-comment">// 第3步:添加事件处理程序(采取函数赋值形式)</span>
alert(<span class="hljs-string">'弹出'</span>);
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cdb2405b1bb46fb88fc5f04894a6eb3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c24cd36a8774f0096c284c0858875ae~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码中，定义了一个 id 为 btn 的 < button>标签。<br>
通过 getElementById() 的方式获取事件源 btn 。<br>
给事件源 btn 注册事件，语法为 " btn.on 事件类型 "，事件类型 click 表示单击事件，这步操作实际上是为 btn 的 onclick 属性赋值一个函数，这个函数就是事件中处理程序。</p>
<p>通过浏览器打开上述案例代码，使用鼠标单击页面中的按钮，就会弹出个警告框， 说明页面中的按钮已经绑定了单击事件。在事件处理函数中，我们可以编写其他想要在事件触发时执行的代码。另外，事件类型除了 click，还有很多其他的类型，具体会在后面的章节进行详细讲解。</p>
<h1 data-id="heading-21"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.5_操作元素</h1>
<p><strong>在 Javascript 中，DOM 操作可以改变网页内容、结构和样式。</strong></p>
<p>接下来我们将会讲解如何利用 DOM 操作元素的对象属性，改变元素的内容、属性和样式。</p>
<h2 data-id="heading-22"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.5.1_操作元素内容</h2>
<p><strong>操作元素内容的常用属性：</strong></p>





















<table><thead><tr><th>属性</th><th>说明</th></tr></thead><tbody><tr><td>element.innerHTML</td><td>设置或返回元素开始和结束标签之间的 HTML，包括 HTML 标签，同时保留空格和换行</td></tr><tr><td>element.innerText</td><td>设置或返回元素的文本内容，在返回的时候会去除 HTML 标签和多余的空格、换行，在设置的时候会进行特殊字符转义</td></tr><tr><td>element.textContent</td><td>设置或者返回指定节点的文本内容，同时保留空格和换行</td></tr></tbody></table>
<p>上述表中的属性在使用时有一定的区别，innerHTML 在使用时会保持编写的格式以及标签样式；而 innerTest 则是去掉所有格式以及标签的纯文本内容；textContent 属性在去掉标签后会保留文本格式。</p>
<p>案例：分别利用 innerHTML、innerText、textContent 属性在控制台输出一段 HTML 文本，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span>

The first parapraph...
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>
The second Paragraph...
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>third<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.5.2_操作元素属性</h2>
<p><strong>在 DOM 中，HTML 属性操作是指使用 JavaScript 来操作一个元素的 HTML 属性。一个元素包含很多的属性，例如，对于一个 img 图片元素来说，我们可以操作它的 src、title 属性等；或者对于 input 元素来说，我们可以操作它的 disabled 、 checked 、 selected 属性等。</strong></p>
<p>案例：如何操作常用元素属性及表单元素属性。</p>
<h3 data-id="heading-24"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>1. img 元素的属性操作</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"flower"</span>></span>鲜花<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"grass"</span>></span>四叶草<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"四叶草"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-comment">// 1.获取元素</span>
<span class="hljs-keyword">var</span> flower = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'flower'</span>);
<span class="hljs-keyword">var</span> grass = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'grass'</span>);
<span class="hljs-keyword">var</span> img = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'img'</span>);

<span class="hljs-comment">// 2.注册事件处理程序</span>
flower.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
img.src = <span class="hljs-string">'#'</span>;
img.title = <span class="hljs-string">'鲜花'</span>;
&#125;

grass.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
img.src = <span class="hljs-string">'#'</span>;
img.title = <span class="hljs-string">'四叶草'</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，通过 querySelector() 方法获取元素。<br>
为 flower 和 grass 事件源添加 onclick 事件。在处理程序中，通过 " 元素对象.属性名 " 来获取属性的值，通 " 元素对象.属性名 = 值 " 的方式设置图片的 src 和 title 属性。</p>
<h3 data-id="heading-25"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>2. 表单 input 元素的属性操作</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"输入内容"</span> /></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-comment">// 1.获取元素</span>
<span class="hljs-keyword">var</span> btn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'button'</span>);
<span class="hljs-keyword">var</span> input = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'input'</span>);

<span class="hljs-comment">// 2.注册事件处理程序</span>
btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
input.value = <span class="hljs-string">'被点击了!'</span>; <span class="hljs-comment">// 通过value来修改表单里面的值</span>
<span class="hljs-built_in">this</span>.disabled = <span class="hljs-literal">true</span>; <span class="hljs-comment">// this指向的是时间函数的调用者btn</span>
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90ee6835f8974d3290b49c2e58f32ade~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
点击一下 " 按钮 "：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcf18925874e4da3b8d64c6351f382a1~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码中，通过querySelector() 方法获取元素。<br>
为 btn 添加 onclick 事件。在处理程序中，通过 " 元素对象.属性名 = 值 " 的方式设置 input 文本框的 disabled 和 value 属性。最后结果为，当单击按钮后，input 的文本内容变为 ” 被点击了! " 。</p>
<h2 data-id="heading-26"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.5.3_[案例]显示隐藏密码明文</h2>
<ol>
<li>案例分析</li>
</ol>
<p>在登录页面，为了优化用户体验，方便用户进行密码输人，在设计密码框时，可添加一个“眼睛”图片，充当按钮功能，单击可以切换按钮的状态，控制密码的显示和隐藏。实现步骤如下。</p>
<p>(1)准备一个父盒子div。</p>
<p>(2)在父盒子中放人两个子元素，一个input元素和一个img元素。</p>
<p>(3)单击眼睛图片切换input的type值(ext和pasword )。</p>
<p>隐藏密码的效果如图6-8所示。</p>
<p>显示密码的效果如图6 -9所示。</p>
<p>1234567</p>
<p>图6-8隐藏密码</p>
<p>图6-9显示密码</p>
<p>我就是天花板 2020/10/18 14:11:34</p>
<p>2代码实现结构，完成页面布局，示侧代码如下号HTIL</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">dJabolsreminagea/clooe .png<span class="hljs-string">" altonn id-"</span>eyo<span class="hljs-string">">e/label>

cnputtye-pasverd"</span> name-<span class="hljs-string">""</span> id-<span class="hljs-string">"ped"</span>>

cscript

<span class="hljs-number">11</span> <span class="hljs-number">1.</span>我取元素

war eye”<span class="hljs-built_in">document</span> .getElementById(<span class="hljs-string">'eye'</span>);

↓

<span class="hljs-keyword">var</span> pid - <span class="hljs-built_in">document</span>. getElementById(<span class="hljs-string">'pwd'</span>);

<span class="hljs-number">12</span>

<span class="hljs-number">11</span> <span class="hljs-number">2.</span>注册事件处理程序

<span class="hljs-number">13</span>

<span class="hljs-keyword">var</span> flag = <span class="hljs-number">0</span>;

eye.cnclick”<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) (<span class="hljs-params">

<span class="hljs-number">15</span>

<span class="hljs-number">11</span>每次单击，修改flag的值

<span class="hljs-keyword">if</span> (fag <span class="hljs-number">0</span>) (

pid.type = <span class="hljs-string">'text'</span>;

<span class="hljs-number">1</span>

eye.sre”<span class="hljs-string">' images/open.png'</span>;

<span class="hljs-number">19</span>

flag <span class="hljs-number">.1</span>;

<span class="hljs-number">20</span>

) <span class="hljs-keyword">else</span> <span class="hljs-number">1</span>

<span class="hljs-number">21</span>

pd.type = <span class="hljs-string">'password'</span>;

<span class="hljs-number">22</span>

eye.src . <span class="hljs-string">'images/close.png'</span>;

flag = <span class="hljs-number">0</span>;

<span class="hljs-number">2</span>

<span class="hljs-number">25</span>

<span class="hljs-number">26</span> </acript>

<span class="hljs-number">27</span> </body>
</span></span><span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，第10、11 行代码获取了按钮元素和文本框元素。第13行代码声明了一个全局变量fag,来记录lype的状态。第14行代码给eye按钮元素添加了onelick 单击事件。第16~ 24行代码使用if判断语句，根据flag的值来改变type和sre的值，当密码隐藏时，单击“眼睛”图片，密码显示;当密码显示时，单击“眼睛”图片，密码隐藏。</p>
<h2 data-id="heading-27"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.5.4_操作元素样式</h2>
<p>操作元素样式有两种方式，一种是操作 style 属性，另一种是操作 className 属性。下面我们分别进行讲解。</p>
<h3 data-id="heading-28"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>1. 操作style属性</h3>
<p><strong>除了前面讲解的元素内容和属性外，对于元素对象的样式，可以直接通过 " 元素对象style. 样式属性名 " 的方式操作。样式属性名对应 CSS 样式名，但需要去掉 CSS 样式名里的半字线 " - " ，并将半字线后面的英文的首字母大写</strong>。<br>
例如，设置字体大小的样式名 font-size，对应的样式属性名为 fontSize。</p>
<p><strong>常用 style 属性中 CSS 样式名称：</strong></p>

























































<table><thead><tr><th>名称</th><th>说明</th></tr></thead><tbody><tr><td>background</td><td>设置或返同元素的背景属性</td></tr><tr><td>backgroundColor</td><td>设置或返回元素的背景色</td></tr><tr><td>display</td><td>设置或返同元素的显示类型</td></tr><tr><td>fontSize</td><td>设置或返回元素的字体大小</td></tr><tr><td>height</td><td>设置或返回元素的高度</td></tr><tr><td>left</td><td>设置或返回定位元素的左部位置</td></tr><tr><td>listStyleType</td><td>设置或返回列表项标记的类型</td></tr><tr><td>overflow</td><td>设置或返回如何处理呈现在元素框外面的内容</td></tr><tr><td>textAlign</td><td>设置或返回文本的水平对齐方式.</td></tr><tr><td>textDecoration</td><td>设置或返回文本的修饰</td></tr><tr><td>textIndent</td><td>设置成返回文本第一行的缩进</td></tr><tr><td>transform</td><td>向元素应用2D或3D转换</td></tr></tbody></table>
<p>案例：如何对元素的样式进行添加，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">var</span> ele = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box'</span>);
ele.style.width = <span class="hljs-string">'100px'</span>;
ele.style.height = <span class="hljs-string">'100px'</span>;
ele.style.transform = <span class="hljs-string">'rotate(7deg)'</span>;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述第 4 ~ 6 行代码用于为获取的 ele 元素对象添加样式，其效果相当于在 CSS 中添加以下样式。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#box</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">7deg</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>2. 操作 className 属性</h3>
<p>在开发中，如果样式修改较多，可以采取操作类名的方式更改元素样式，语法为 " 元素对象.className " 访问 className 属性的值表示获取元素的类名，为 className 属性赋值表示更改元素类名。如果元素有多个类名，在 className 中以空格分隔。</p>
<p>案例：如何使用 className 更改元素的样式。</p>
<p>(1) 编写 html 结构代码，具体示例如下。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-tag">div</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">background-color</span>: pink;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"first"</span>></span>文本<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://img-blog.csdnimg.cn/20201215210154810.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码中，第 9 行代码给 div 元素添加 first 类，并在 style 中设置了 first 的样式。</p>
<p>(2) 单击 div 元素更改元素的样式，示例代码如下。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> test = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'div'</span>);
test.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">this</span>.className = <span class="hljs-string">'change'</span>;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，第 2 行代码获取 div 元素存储在 test 对象中。第 3 ~ 5 行代码为 text 对象添加 onclick 单击事件，第 4 行执行事件处理程序使用 thisclassName 给 test 对象设置 change 类名，其中 this 指的是 test 对象。</p>
<p>(3) 在 style 中添加 change 类，样式代码如下。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.change</span> &#123;
<span class="hljs-attribute">background-color</span>: purple;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">25px</span>;
<span class="hljs-attribute">margin-top</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://img-blog.csdnimg.cn/20201215210411563.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>(4) 单击 div 盒子，浏览器预览效果如下图所示。</p>
<p>执行上述代码之后，会直接把原先的类名 first 修改为 change ，如果想要保留原先的类名，可以采取多类名选择器的方式，修收第 (2) 步的第 4 行代码，示例代码如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.className = <span class="hljs-string">'first change'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改之后，在控制台可查看到 div 元素的类已经修改成了 < div class = " first change "> 文本< /div>，保留了之前的类名。</p>
<h2 data-id="heading-30"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.5.5_[案例]显示隐藏文本框内容</h2>
<ol>
<li>案例分析</li>
</ol>
<p>本案例需要为一个文本框添加提示文本。当单击文本框时，里面的默认提示文字会隐藏，鼠标指针离开文本框，里面的文字会显示出来。</p>
<p>具体实现步骤如下：</p>
<p>(1) 为元素绑定获取文本框焦点事件 onfocus 和失去焦点事件 onblur。</p>
<p>(2) 如果获取焦点时，需要判断表单里面的内容是否为默认文字；如果是默认文字，就清空表单内容。</p>
<p>(3) 如果失去焦点，需要判断表单内容是否为空；如果为空，则表单里边的内容改为默认文字。</p>
<ol start="2">
<li>代码实现</li>
</ol>
<p>编写 HTML 结构，完成页面布局，示例代码如下。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"手机"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color:999"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，第 2 行代码给 input 文本框设置了 value 值，默认内容为 " 手机 " ，字体颜色为 " #999 " 。</p>
<p>编写实现获取焦点时效果的 JavaScript 代码，示例代码如下。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">var</span> text = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'input'</span>); <span class="hljs-comment">// 获取元素</span>
text.onfocus = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;  <span class="hljs-comment">// 注册获得焦点事件onfocus</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.value === <span class="hljs-string">'手机'</span>) &#123;
<span class="hljs-built_in">this</span>.value = <span class="hljs-string">' '</span>;
<span class="hljs-built_in">this</span>.style.color  = <span class="hljs-string">'#333'</span>;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，第 2 行代码获取 input 元素并存储在 text 对象中。第 3 ~ 8 行代码给 text 元素注册 onfocus 获得焦点事件。其中，第 4 ~ 7 行使用 if 判断语句，如果文本框的值为默认的手机，则清空表单内容，否则改变文本框里面的文字颜色。</p>
<p>接下来我们继续编写实现失去焦点时效果的JavaScript代码，示例代码如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">text.onblur = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 注册失去焦点事件onblur</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.value === <span class="hljs-string">''</span>) &#123;
<span class="hljs-built_in">this</span>.value = <span class="hljs-string">'手机'</span>;
&#125;
<span class="hljs-comment">// 失去焦点需要把文本框里面的文字颜色变浅色</span>
<span class="hljs-built_in">this</span>.style.color = <span class="hljs-string">'#999'</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码用来给 text 元素注册 onblur 失去焦点事件。其中，第 2 ~ 4 行代码使用 if 语句判断如果文本框的值为空，则表单里边的内容改为默认文字 " 手机 " 。然后用第 6 行代码改变文本框里面的文字颜色。</p>
<p><strong>今日入门学习暂时告一段落<br>
Peace</strong></p>
<h1 data-id="heading-31"><strong>🌊🌈往期回顾：</strong></h1>
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
<a href="https://juejin.cn/post/7000175914680057870" title="https://juejin.cn/post/7000175914680057870" target="_blank"><strong>【JS干货分享 | 建议收藏】挑战最短时间带你走进JS（十）</strong></a></p>
<h1 data-id="heading-32"><strong>🌊🌈关于后记：</strong></h1>
<p><strong>感谢阅读，希望能对你有所帮助 博文若有瑕疵请在评论区留言或在主页个人介绍中添加联系方式私聊我 感谢每一位小伙伴不吝赐教</strong></p>
<p>原创不易，<strong>「点赞」+「关注」</strong> 谢谢支持❤</p>
<h1 data-id="heading-33"><strong>🌊🌈关于彩蛋</strong></h1>
<p>入驻掘金也有一月有余，为回馈大佬们这段时间的支持，特地创建一个大佬技术交流群，评论区放二维码哦~</p></div>  
</div>
            