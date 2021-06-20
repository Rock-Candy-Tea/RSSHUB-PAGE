
---
title: 'JavaScript window 对象详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7419'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 19:16:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=7419'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 14 天，活动详情查看: <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h4 data-id="heading-0">1. 概述</h4>
<p>window对象 指当前的浏览器窗口，它也是当前页面的顶层对象，即最高一层的对象，所有其他对象都是它的下属。
一个变量如果未声明，那么默认就是顶层对象的属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// a是一个没有声明就直接赋值的变量，它自动成为顶层对象的属性。</span>
a = <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.a) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>window 有自己的实体含义，其实不适合当作最高一层的顶层对象，这是一个语言的设计失误。
最早，设计这门语言的时候，原始设想是语言内置的对象越少越好，这样可以提高浏览器的性能。因此，语言设计者 Brendan Eich 就把 window 对象当作顶层对象，所有未声明就赋值的变量都自动变成 window 对象的属性。这种设计使得编译阶段无法检测出未声明变量，但到了今天已经没有办法纠正了。</p>
<h4 data-id="heading-1">2. window 对象的属性</h4>
<p><strong>2.1 window.name</strong>
window.name属性是一个字符串，表示当前浏览器窗口的名字。
窗口不一定需要名字，这个属性主要配合超链接和表单的target属性使用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.name = <span class="hljs-string">'Hello World!'</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.name) <span class="hljs-comment">// "Hello World!"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该属性只能保存字符串，如果写入的值不是字符串，会自动转成字符串。
只要浏览器窗口不关闭，这个属性是不会消失的。
举例来说，访问a.com时，该页面的脚本设置了window.name，接下来在同一个窗口里面载入了b.com，新页面的脚本可以读到上一个网页设置的 window.name。页面刷新也是这种情况。一旦浏览器窗口关闭后，该属性保存的值就会消失，因为这时窗口已经不存在了。</p>
<p><strong>2.2  window.closed，window.opener</strong></p>
<p><strong>2.2.1 window.closed 属性返回一个布尔值，表示窗口是否关闭；</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.closed <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码检查当前窗口是否关闭。这种检查意义不大，因为只要能运行代码，当前窗口肯定没有关闭。
这个属性一般用来检查，使用脚本打开的新窗口是否关闭。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> popup = <span class="hljs-built_in">window</span>.open();
<span class="hljs-keyword">if</span> ((popup !== <span class="hljs-literal">null</span>) && !popup.closed) &#123;
<span class="hljs-comment">// 窗口仍然打开着</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.2.2  window.opener 属性表示打开当前窗口的父窗口；</strong>
如果当前窗口没有父窗口（即直接在地址栏输入打开），则返回null。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 表达式会打开一个新窗口，然后返回 true</span>
<span class="hljs-built_in">window</span>.open().opener === <span class="hljs-built_in">window</span> <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果两个窗口之间不需要通信，建议将子窗口的 opener 属性显式设为 null，这样可以减少一些安全隐患。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 子窗口的 opener 属性设为 null，两个窗口之间就没办法再联系了</span>
<span class="hljs-keyword">var</span> newWin = <span class="hljs-built_in">window</span>.open(<span class="hljs-string">'example.html'</span>, <span class="hljs-string">'newWindow'</span>, <span class="hljs-string">'height=400,width=400'</span>);
newWin.opener = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 opener 属性，可以获得父窗口的全局属性和方法，但只限于两个窗口同源的情况，且其中一个窗口由另一个打开。
< a > 元素添加 rel="noopener" 属性，可以防止新打开的窗口获取父窗口，减轻被恶意网站修改父窗口 URL 的风险。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><a href=<span class="hljs-string">"https://an.evil.site"</span> target=<span class="hljs-string">"_blank"</span> rel=<span class="hljs-string">"noopener"</span>> 恶意网站 </a>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.3 window.self，window.window</strong>
window.self和window.window属性都指向窗口本身,这两个属性只读</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.self === <span class="hljs-built_in">window</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.window === <span class="hljs-built_in">window</span>) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.4 window.frames，window.length</strong>
window.frames 属性返回一个类似数组的对象，成员为页面内所有框架窗口，包括 frame 元素和 iframe 元素。
window.frames[0]表示页面中第一个框架窗口。</p>
<p>如果 iframe 元素设置了 id 或 name 属性，那么就可以用属性值，引用这个 iframe 窗口。
< iframe name="myIFrame"> 可以用 frames['myIFrame'] 或者 frames.myIFrame 来引用。</p>
<p>frames属性实际上是window对象的别名。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">frames === <span class="hljs-built_in">window</span> <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，frames[0] 也可以用 window[0] 表示。
从语义上看 frames 更清晰，而且考虑到 window 还是全局对象，因此推荐表示多窗口时，总是使用 frames[0] 的写法。
window.length属性返回当前网页包含的框架总数。如果当前网页不包含 frame 和 iframe 元素，那么 window.length 就返回 0。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// window.frames.length 与 window.length 应该是相等的</span>
<span class="hljs-built_in">window</span>.frames.length === <span class="hljs-built_in">window</span>.length <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.5 window.frameElement</strong>
window.frameElement 属性主要用于当前窗口嵌在另一个网页的情况（嵌入< object >、< iframe >或< embed >元素），返回当前窗口所在的那个元素节点。如果当前窗口是顶层窗口，或者所嵌入的那个网页不是同源的，该属性返回null。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// HTML 代码如下</span>
<span class="hljs-comment">// <iframe src="about.html"></iframe></span>

<span class="hljs-comment">// 下面的脚本在 about.html 里面</span>
<span class="hljs-keyword">var</span> frameEl = <span class="hljs-built_in">window</span>.frameElement;
<span class="hljs-keyword">if</span> (frameEl) &#123;
  frameEl.src = <span class="hljs-string">'other.html'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，frameEl变量就是 < iframe > 元素。</p>
<p><strong>2.6 window.top，window.parent</strong>
window.top 属性指向最顶层窗口，主要用于在框架窗口（frame）里面获取顶层窗口;
window.parent 属性指向父窗口。如果当前窗口没有父窗口，window.parent指向自身;
对于不包含框架的网页，这两个属性等同于window对象</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.parent !== <span class="hljs-built_in">window</span>.top) &#123;
  <span class="hljs-comment">// 表明当前窗口嵌入不止一层</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.7 window.status</strong>
window.status属性用于读写浏览器状态栏的文本。
<strong>注意：</strong> 现在很多浏览器都不允许改写状态栏文本，所以使用这个方法不一定有效。</p>
<p><strong>2.8 window.devicePixelRatio</strong>
window.devicePixelRatio属性返回一个数值，表示一个 CSS 像素的大小与一个物理像素的大小之间的比率。
它表示一个 CSS 像素由多少个物理像素组成。它可以用于判断用户的显示环境，如果这个比率较大，就表示用户正在使用高清屏幕，因此可以显示较大像素的图片。</p>
<h4 data-id="heading-2">3. 位置大小属性</h4>
<p><strong>3.1 window.screenX，window.screenY（只读）</strong>
window.screenX和window.screenY属性，返回浏览器窗口左上角相对于当前屏幕左上角的水平距离和垂直距离（单位像素）。</p>
<p><strong>3.2 window.innerHeight，window.innerWidth（只读）</strong>
window.innerHeight和window.innerWidth属性，返回网页在当前窗口中可见部分的高度和宽度，即“视口”（viewport）的大小（单位像素）。</p>
<p>用户放大网页的时候（比如将网页从100%的大小放大为200%），这两个属性会变小。因为这时网页的像素大小不变（比如宽度还是960像素），只是每个像素占据的屏幕空间变大了，因为可见部分（视口）就变小了。</p>
<p>注意，这两个属性值包括滚动条的高度和宽度。</p>
<p><strong>3.3 window.outerHeight，window.outerWidth（只读）</strong>
window.outerHeight 和 window.outerWidth 属性返回浏览器窗口的高度和宽度，包括浏览器菜单和边框（单位像素）。</p>
<p><strong>3.4 window.scrollX，window.scrollY（只读）</strong>
window.scrollX属性返回页面的水平滚动距离，window.scrollY属性返回页面的垂直滚动距离，单位都为像素。</p>
<p><strong>注意：</strong> 这两个属性的返回值不是整数，而是双精度浮点数。如果页面没有滚动，它们的值就是0。
举例来说，如果用户向下拉动了垂直滚动条75像素，那么window.scrollY就是75左右。用户水平向右拉动水平滚动条200像素，window.scrollX就是200左右。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 如果页面向下滚动的距离小于75像素，那么页面向下滚动75像素</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.scrollY < <span class="hljs-number">75</span>) &#123;
  <span class="hljs-built_in">window</span>.scroll(<span class="hljs-number">0</span>, <span class="hljs-number">75</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.5 window.pageXOffset，window.pageYOffset</strong>
window.pageXOffset属性和window.pageYOffset属性，是window.scrollX和window.scrollY别名。</p>
<h4 data-id="heading-3">4. 组件属性</h4>
<p>组件属性返回浏览器的组件对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.locationbar <span class="hljs-comment">// 地址栏对象</span>
<span class="hljs-built_in">window</span>.menubar  <span class="hljs-comment">// 菜单栏对象</span>
<span class="hljs-built_in">window</span>.scrollbars <span class="hljs-comment">// 窗口的滚动条对象</span>
<span class="hljs-built_in">window</span>.toolbar <span class="hljs-comment">// 工具栏对象</span>
<span class="hljs-built_in">window</span>.statusbar <span class="hljs-comment">// 状态栏对象</span>
<span class="hljs-built_in">window</span>.personalbar <span class="hljs-comment">// 用户安装的个人工具栏对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些对象的 visible 属性是一个布尔值，表示这些组件是否可见。这些属性只读。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.locationbar.visible
<span class="hljs-built_in">window</span>.menubar.visible
<span class="hljs-built_in">window</span>.scrollbars.visible
<span class="hljs-built_in">window</span>.toolbar.visible
<span class="hljs-built_in">window</span>.statusbar.visible
<span class="hljs-built_in">window</span>.personalbar.visible
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">5. 全局对象属性</h4>
<p>全局对象属性指向一些浏览器原生的全局对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.document  <span class="hljs-comment">// 指向document对象。注意，这个属性有同源限制。只有来自同源的脚本才能读取这个属性。</span>
<span class="hljs-built_in">window</span>.location  <span class="hljs-comment">// 指向Location对象，用于获取当前窗口的 URL 信息。它等同于document.location属性。</span>
<span class="hljs-built_in">window</span>.navigator  <span class="hljs-comment">// 指向Navigator对象，用于获取环境信息。</span>
<span class="hljs-built_in">window</span>.history  <span class="hljs-comment">// 指向History对象，表示浏览器的浏览历史。</span>
<span class="hljs-built_in">window</span>.localStorage  <span class="hljs-comment">// 指向本地储存的localStorage数据。</span>
<span class="hljs-built_in">window</span>.sessionStorage  <span class="hljs-comment">// 指向本地储存的sessionStorage数据。</span>
<span class="hljs-built_in">window</span>.console  <span class="hljs-comment">// 指向console对象，用于操作控制台。</span>
<span class="hljs-built_in">window</span>.screen  <span class="hljs-comment">// 指向Screen对象，表示屏幕信息。</span>
<span class="hljs-built_in">window</span>.isSecureContext  <span class="hljs-comment">// 属性返回一个布尔值，表示当前窗口是否处在加密环境。如果是 HTTPS 协议，就是true，否则就是false。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">6. window 对象的方法</h4>
<p><strong>6.1 window.alert() ,  window.prompt() , window.confirm()</strong>
这三个方法都具有堵塞效应，一旦弹出对话框，整个页面就是暂停执行，等待用户做出反应。</p>
<p><strong>window.alert() 方法弹出的对话框，只有一个“确定”按钮，往往用来通知用户某些信息。</strong>
用户只有点击“确定”按钮，对话框才会消失。对话框弹出期间，浏览器窗口处于冻结状态，如果不点“确定”按钮，用户什么也干不了。
window.alert()方法的参数只能是字符串，没法使用 CSS 样式，但是可以用\n指定换行。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.alert(<span class="hljs-string">'Hello World'</span>);
alert(<span class="hljs-string">'本条提示\n分成两行'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>window.prompt() 方法弹出的对话框，提示文字的下方，还有一个输入框，要求用户输入信息，并有“确定”和“取消”两个按钮。</strong>
window.prompt()方法的第二个参数是可选的，但是最好总是提供第二个参数，作为输入框的默认值。
它往往用来获取用户输入的数据。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 代码会跳出一个对话框，文字提示为“您的年龄？”，要求用户在对话框中输入自己的年龄（默认显示25）。用户填入的值，会作为返回值存入变量result。</span>
<span class="hljs-keyword">var</span> result = prompt(<span class="hljs-string">'您的年龄？'</span>, <span class="hljs-number">25</span>)
<span class="hljs-built_in">console</span>.log(result)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>window.prompt()的返回值有两种情况，可能是字符串（有可能是空字符串），也有可能是null。
具体分成三种情况:</p>
<ol>
<li>用户输入信息，并点击“确定”，则用户输入的信息就是返回值。</li>
<li>用户没有输入信息，直接点击“确定”，则输入框的默认值就是返回值。</li>
<li>用户点击了“取消”（或者按了 ESC 按钮），则返回值是null。</li>
</ol>
<p><strong>window.confirm() 方法弹出的对话框，除了提示信息之外，只有“确定”和“取消”两个按钮，往往用来征询用户是否同意。</strong>
confirm方法返回一个布尔值，如果用户点击“确定”，返回true；如果用户点击“取消”，则返回false。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> okay = confirm(<span class="hljs-string">'Please confirm this message.'</span>);
<span class="hljs-keyword">if</span> (okay) &#123;
  <span class="hljs-comment">// 用户按下“确定”</span>
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 用户按下“取消”</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>confirm的一个用途是，用户离开当前页面时，弹出一个对话框，问用户是否真的要离开。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.onunload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">window</span>.confirm(<span class="hljs-string">'你确定要离开当面页面吗？'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.2 window.open(),  window.close(),  window.stop()</strong></p>
<p><strong>window.open() 方法用于新建另一个浏览器窗口，类似于浏览器菜单的新建窗口选项。它会返回新窗口的引用，如果无法新建窗口，则返回null。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 浏览器弹出一个新建窗口，网址是当前域名下的somefile.html</span>
<span class="hljs-keyword">var</span> popup = <span class="hljs-built_in">window</span>.open(<span class="hljs-string">'somefile.html'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>open方法一共可以接受三个参数:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.open(url, windowName, [windowFeatures])

url：字符串，表示新窗口的网址。如果省略，默认网址就是about:blank。
windowName：字符串，表示新窗口的名字。
如果该名字的窗口已经存在，则占用该窗口，不再新建窗口。
如果省略，就默认使用_blank，表示新建一个没有名字的窗口。
另外还有几个预设值，_self表示当前窗口，_top表示顶层窗口，_parent表示上一层窗口。
windowFeatures：字符串，内容为逗号分隔的键值对（如下所列），表示新窗口的参数，比如有没有提示栏、工具条等等。
如果省略，则默认打开一个完整的新窗口。
如果新建的是一个已经存在的窗口，则该参数不起作用，浏览器沿用以前窗口的参数。

第三个参数可以设定如下属性:
left：新窗口距离屏幕最左边的距离（单位像素）。注意，新窗口必须是可见的，不能设置在屏幕以外的位置。
top：新窗口距离屏幕最顶部的距离（单位像素）。
height：新窗口内容区域的高度（单位像素），不得小于<span class="hljs-number">100</span>。
width：新窗口内容区域的宽度（单位像素），不得小于<span class="hljs-number">100</span>。
outerHeight：整个浏览器窗口的高度（单位像素），不得小于<span class="hljs-number">100</span>。
outerWidth：整个浏览器窗口的宽度（单位像素），不得小于<span class="hljs-number">100</span>。
menubar：是否显示菜单栏。
toolbar：是否显示工具栏。
location：是否显示地址栏。
personalbar：是否显示用户自己安装的工具栏。
status：是否显示状态栏。
dependent：是否依赖父窗口。如果依赖，那么父窗口最小化，该窗口也最小化；父窗口关闭，该窗口也关闭。
minimizable：是否有最小化按钮，前提是dialog=yes。
noopener：新窗口将与父窗口切断联系，即新窗口的<span class="hljs-built_in">window</span>.opener属性返回<span class="hljs-literal">null</span>，
  父窗口的<span class="hljs-built_in">window</span>.open()方法也返回<span class="hljs-literal">null</span>。
resizable：新窗口是否可以调节大小。
scrollbars：是否允许新窗口出现滚动条。
dialog：新窗口标题栏是否出现最大化、最小化、恢复原始大小的控件。
titlebar：新窗口是否显示标题栏。
alwaysRaised：是否显示在所有窗口的顶部。
alwaysLowered：是否显示在父窗口的底下。
close：新窗口是否显示关闭按钮。

对于那些可以打开和关闭的属性，设为yes或<span class="hljs-number">1</span>或不设任何值就表示打开;
比如status=yes、status=<span class="hljs-number">1</span>、status都会得到同样的结果。
如果想设为关闭，不用写no，而是直接省略这个属性即可。
如果在第三个参数中设置了一部分属性，其他没有被设置的yes/no属性都会被设成no;
只有titlebar和关闭按钮除外（它们的值默认为yes）。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 打开的新窗口高度和宽度都为200像素，没有地址栏，但有状态栏和滚动条，允许用户调整大小。</span>
<span class="hljs-keyword">var</span> popup = <span class="hljs-built_in">window</span>.open(
  <span class="hljs-string">'somepage.html'</span>,
  <span class="hljs-string">'DefinitionsWindows'</span>,
  <span class="hljs-string">'height=200,width=200,location=no,status=yes,resizable=yes,scrollbars=yes'</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>open() 方法的第二个参数虽然可以指定已经存在的窗口，但是不等于可以任意控制其他窗口。为了防止被不相干的窗口控制，浏览器只有在两个窗口同源，或者目标窗口被当前网页打开的情况下，才允许open方法指向该窗口。</p>
<p>window.open方法返回新窗口的引用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> windowB = <span class="hljs-built_in">window</span>.open(<span class="hljs-string">'windowB.html'</span>, <span class="hljs-string">'WindowB'</span>);
windowB.window.name <span class="hljs-comment">// "WindowB"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意:</strong> 如果新窗口和父窗口不是同源的（即不在同一个域），它们彼此不能获取对方窗口对象的内部属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 打开一个新窗口，然后在该窗口弹出一个对话框，再将网址导向example.com</span>
<span class="hljs-keyword">var</span> w = <span class="hljs-built_in">window</span>.open();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'已经打开新窗口'</span>);
w.location = <span class="hljs-string">'http://example.com'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于open这个方法很容易被滥用，许多浏览器默认都不允许脚本自动新建窗口。
只允许在用户点击链接或按钮时，脚本做出反应，弹出新窗口。因此，有必要检查一下打开新窗口是否成功。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> popup = <span class="hljs-built_in">window</span>.open();
<span class="hljs-keyword">if</span> (popup === <span class="hljs-literal">null</span>) &#123;
  <span class="hljs-comment">// 新建窗口失败</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>window.close() 方法用于关闭当前窗口，一般只用来关闭window.open方法新建的窗口。</strong>
该方法只对顶层窗口有效，iframe框架之中的窗口使用该方法无效。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.close()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>window.stop() 方法完全等同于单击浏览器的停止按钮，会停止加载图像、视频等正在或等待加载的对象。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.stop()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.3 window.moveTo(), window.resizeBy()</strong>
<strong>注意：</strong> 为了防止有人滥用这两个方法，随意移动用户的窗口，目前只有一种情况，浏览器允许用脚本移动窗口：该窗口是用window.open方法新建的，并且它所在的 Tab 页是当前窗口里面唯一的。除此以外的情况，使用上面两个方法都是无效的。</p>
<p><strong>window.moveTo() 方法用于移动浏览器窗口到指定位置。</strong>
它接受两个参数，分别是窗口左上角距离屏幕左上角的水平距离和垂直距离，单位为像素。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 将窗口移动到屏幕(100, 200)的位置</span>
<span class="hljs-built_in">window</span>.moveTo(<span class="hljs-number">100</span>, <span class="hljs-number">200</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>window.moveBy() 方法将窗口移动到一个相对位置。</strong>
它接受两个参数，分布是窗口左上角向右移动的水平距离和向下移动的垂直距离，单位为像素。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 将窗口向右移动25像素、向下移动50像素</span>
<span class="hljs-built_in">window</span>.moveBy(<span class="hljs-number">25</span>, <span class="hljs-number">50</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.4 window.scrollTo()，window.scroll()，window.scrollBy()</strong></p>
<p><strong>window.scrollTo() 方法用于将文档滚动到指定位置。</strong>
接受两个参数，表示滚动后位于窗口左上角的页面坐标。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.scrollTo(x-coord, y-coord)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以接受一个配置对象作为参数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.scrollTo(options)
配置对象options有三个属性：
  top：滚动后页面左上角的垂直坐标，即y坐标。
  left：滚动后页面左上角的水平坐标，即x坐标。
  behavior：字符串，表示滚动的方式，有三个可能值（smooth、instant、auto），默认值为auto。

<span class="hljs-built_in">window</span>.scrollTo(&#123;
  <span class="hljs-attr">top</span>: <span class="hljs-number">1000</span>,
  <span class="hljs-attr">behavior</span>: <span class="hljs-string">'smooth'</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>window.scroll() 方法是 window.scrollTo() 方法的别名。</strong></p>
<p><strong>window.scrollBy() 方法用于将网页滚动指定距离（单位像素）。</strong>
它接受两个参数：水平向右滚动的像素，垂直向下滚动的像素。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 用于将网页向下滚动一屏</span>
<span class="hljs-built_in">window</span>.scrollBy(<span class="hljs-number">0</span>, <span class="hljs-built_in">window</span>.innerHeight)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">如果不是要滚动整个文档，而是要滚动某个元素，可以使用下面三个属性和方法:
Element.scrollTop
Element.scrollLeft
Element.scrollIntoView()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.5 window.print()</strong>
window.print() 方法会跳出打印对话框，与用户点击菜单里面的“打印”命令效果相同。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 常见的打印按钮代码如下</span>
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'printLink'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">window</span>.print();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 非桌面设备（比如手机）可能没有打印功能，这时可以这样判断</span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span>.print === <span class="hljs-string">'function'</span>) &#123;
  <span class="hljs-comment">// 支持打印功能</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.6 window.focus()，window.blur()</strong>
<strong>window.focus() 方法会激活窗口，使其获得焦点，出现在其他窗口的前面。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 先检查popup窗口是否依然存在，确认后激活该窗口</span>
<span class="hljs-keyword">var</span> popup = <span class="hljs-built_in">window</span>.open(<span class="hljs-string">'popup.html'</span>, <span class="hljs-string">'Popup Window'</span>);

<span class="hljs-keyword">if</span> ((popup !== <span class="hljs-literal">null</span>) && !popup.closed) &#123;
  popup.focus();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>window.blur() 方法将焦点从窗口移除。</strong></p>
<p>当前窗口获得焦点时，会触发focus事件；当前窗口失去焦点时，会触发blur事件。</p>
<p><strong>6.7 window.getSelection()</strong>
window.getSelection方法返回一个Selection对象，表示用户现在选中的文本。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> selObj = <span class="hljs-built_in">window</span>.getSelection();
<span class="hljs-comment">// 使用Selection对象的toString方法可以得到选中的文本</span>
<span class="hljs-keyword">var</span> selectedText = selObj.toString();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.8 window.getComputedStyle()，window.matchMedia()</strong></p>
<p>window.getComputedStyle() 方法接受一个元素节点作为参数，返回一个包含该元素的最终样式信息的对象。
window.matchMedia() 方法用来检查 CSS 的mediaQuery语句。</p>
<p><strong>6.9 window.requestAnimationFrame()</strong></p>
<p>window.requestAnimationFrame() 方法跟 setTimeout 类似，都是推迟某个函数的执行。
不同之处在于: setTimeout 必须指定推迟的时间，window.requestAnimationFrame() 则是推迟到浏览器下一次重流时执行，执行完才会进行下一次重绘。重绘通常是 16ms 执行一次，不过浏览器会自动调节这个速率，比如网页切换到后台 Tab 页时，requestAnimationFrame()会暂停执行。</p>
<p>如果某个函数会改变网页的布局，一般就放在window.requestAnimationFrame()里面执行，这样可以节省系统资源，使得网页效果更加平滑。因为慢速设备会用较慢的速率重流和重绘，而速度更快的设备会有更快的速率。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.requestAnimationFrame(callback)

callback是一个回调函数。
callback执行时，它的参数就是系统传入的一个高精度时间戳（performance.now()的返回值），单位是毫秒，表示距离网页加载的时间。

<span class="hljs-built_in">window</span>.requestAnimationFrame()的返回值是一个整数，这个整数可以传入<span class="hljs-built_in">window</span>.cancelAnimationFrame()，用来取消回调函数的执行。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 下面是一个window.requestAnimationFrame()执行网页动画的例子,持续时间是2秒，会让元素向右移动。</span>
<span class="hljs-keyword">var</span> element = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'animate'</span>);
element.style.position = <span class="hljs-string">'absolute'</span>;

<span class="hljs-keyword">var</span> start = <span class="hljs-literal">null</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">step</span>(<span class="hljs-params">timestamp</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!start) start = timestamp;
  <span class="hljs-keyword">var</span> progress = timestamp - start;
  <span class="hljs-comment">// 元素不断向左移，最大不超过200像素</span>
  element.style.left = <span class="hljs-built_in">Math</span>.min(progress / <span class="hljs-number">10</span>, <span class="hljs-number">200</span>) + <span class="hljs-string">'px'</span>;
  <span class="hljs-comment">// 如果距离第一次执行不超过 2000 毫秒，</span>
  <span class="hljs-comment">// 就继续执行动画</span>
  <span class="hljs-keyword">if</span> (progress < <span class="hljs-number">2000</span>) &#123;
    <span class="hljs-built_in">window</span>.requestAnimationFrame(step);
  &#125;
&#125;

<span class="hljs-built_in">window</span>.requestAnimationFrame(step);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.10 window.requestIdleCallback()</strong>
window.requestIdleCallback()跟setTimeout类似，也是将某个函数推迟执行，但是它保证将回调函数推迟到系统资源空闲时执行。也就是说，如果某个任务不是很关键，就可以使用window.requestIdleCallback()将其推迟执行，以保证网页性能。</p>
<p><strong>它跟window.requestAnimationFrame() 的区别：</strong> 后者指定回调函数在下一次浏览器重排时执行，问题在于下一次重排时，系统资源未必空闲，不一定能保证在16毫秒之内完成；window.requestIdleCallback()可以保证回调函数在系统资源空闲时执行。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.requestIdleCallback(callback[, options])

callback参数是一个回调函数。
该回调函数执行时，系统会传入一个IdleDeadline对象作为参数。
IdleDeadline对象有一个didTimeout属性（布尔值，表示是否为超时调用）和一个timeRemaining()方法（返回该空闲时段剩余的毫秒数）。
options参数是一个配置对象，目前只有timeout一个属性，用来指定回调函数推迟执行的最大毫秒数，该参数可选。

<span class="hljs-built_in">window</span>.requestIdleCallback()方法返回一个整数，该整数可以传入<span class="hljs-built_in">window</span>.cancelIdleCallback()取消回调函数。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// requestIdleCallback()用来执行非关键任务myNonEssentialWork。该任务先确认本次空闲时段有剩余时间，然后才真正开始执行任务</span>
requestIdleCallback(myNonEssentialWork);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myNonEssentialWork</span>(<span class="hljs-params">deadline</span>) </span>&#123;
  <span class="hljs-keyword">while</span> (deadline.timeRemaining() > <span class="hljs-number">0</span>) &#123;
    doWorkIfNeeded();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// processPendingAnalyticsEvents必须在未来2秒之内执行</span>
requestIdleCallback(processPendingAnalyticsEvents, &#123; <span class="hljs-attr">timeout</span>: <span class="hljs-number">2000</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果由于超时导致回调函数执行，则 deadline.timeRemaining() 返回 0，deadline.didTimeout 返回true。</p>
<p>如果多次执行 window.requestIdleCallback()，指定多个回调函数，那么这些回调函数将排成一个队列，按照先进先出的顺序执行。</p>
<h4 data-id="heading-6">7. 事件</h4>
<p>window对象可以接收以下事件</p>
<p><strong>7.1 load 事件和 onload 属性</strong>
load事件发生在文档在浏览器窗口加载完毕时,window.onload属性可以指定这个事件的回调函数;</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在网页加载完毕后，获取指定元素并进行处理</span>
<span class="hljs-built_in">window</span>.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> elements = <span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">'example'</span>);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < elements.length; i++) &#123;
    <span class="hljs-keyword">var</span> elt = elements[i];
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.2 error 事件和 onerror 属性</strong>
浏览器脚本发生错误时，会触发 window 对象的 error 事件,可以通过 window.onerror 属性对该事件指定回调函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">message, filename, lineno, colno, error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"出错了！--> %s"</span>, error.stack);
&#125;;

<span class="hljs-built_in">window</span>的error事件的回调函数不接受错误对象作为参数，而是一共可以接受五个参数，它们的含义依次如下:
出错信息, 出错脚本的网址, 行号, 列号, 错误对象

老式浏览器只支持前三个参数。

不是所有的错误，都会触发 JavaScript 的error事件（即让 JavaScript 报错）。
一般来说，只有 JavaScript 脚本的错误，才会触发这个事件，而像资源文件不存在之类的错误，都不会触发。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 如果整个页面未捕获错误超过3个，就显示警告</span>
<span class="hljs-built_in">window</span>.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">msg, url, line</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (onerror.num++ > onerror.max) &#123;
    alert(<span class="hljs-string">'ERROR: '</span> + msg + <span class="hljs-string">'\n'</span> + url + <span class="hljs-string">':'</span> + line);
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;
&#125;
onerror.max = <span class="hljs-number">3</span>;
onerror.num = <span class="hljs-number">0</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意:</strong> 如果脚本网址与网页网址不在同一个域（比如使用了 CDN），浏览器根本不会提供详细的出错信息，只会提示出错，错误类型是“Script error.”，行号为0，其他信息都没有。这是浏览器防止向外部脚本泄漏信息。
一个解决方法是在脚本所在的服务器，设置Access-Control-Allow-Origin的 HTTP 头信息:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Access-Control-Allow-Origin: *
<span class="hljs-comment">// 在网页的<script>标签中设置crossorigin属性</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">crossorigin</span>=<span class="hljs-string">"anonymous"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"//example.com/file.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

上面代码的 crossorigin=<span class="hljs-string">"anonymous"</span> 表示，读取文件不需要身份信息，即不需要 cookie 和 HTTP 认证信息。
如果设为crossorigin=<span class="hljs-string">"use-credentials"</span>，就表示浏览器会上传 cookie 和 HTTP 认证信息，
同时还需要服务器端打开 HTTP 头信息Access-Control-Allow-Credentials。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.3 window 对象的事件监听属性</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.onafterprint  <span class="hljs-comment">// afterprint事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onbeforeprint  <span class="hljs-comment">// beforeprint事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onbeforeunload  <span class="hljs-comment">// beforeunload事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onhashchange  <span class="hljs-comment">// hashchange事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onlanguagechange  <span class="hljs-comment">// languagechange的监听函数。</span>
<span class="hljs-built_in">window</span>.onmessage  <span class="hljs-comment">// message事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onmessageerror <span class="hljs-comment">// MessageError事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onoffline  <span class="hljs-comment">// offline事件的监听函数。</span>
<span class="hljs-built_in">window</span>.ononline  <span class="hljs-comment">// online事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onpagehide  <span class="hljs-comment">// pagehide事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onpageshow  <span class="hljs-comment">// pageshow事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onpopstate  <span class="hljs-comment">// popstate事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onstorage  <span class="hljs-comment">// storage事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onunhandledrejection  <span class="hljs-comment">// 未处理的Promise对象的reject事件的监听函数。</span>
<span class="hljs-built_in">window</span>.onunload  <span class="hljs-comment">// unload事件的监听函数。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">8. 多窗口操作</h4>
<p>由于网页可以使用 iframe 元素，嵌入其他网页，因此一个网页之中会形成多个窗口。如果子窗口之中又嵌入别的网页，就会形成多级窗口。
<strong>8.1 窗口的引用</strong>
各个窗口之中的脚本，可以引用其他窗口,浏览器提供了一些特殊变量，用来返回其他窗口。</p>
<ol>
<li>top：顶层窗口，即最上层的那个窗口；</li>
<li>parent：父窗口；</li>
<li>self：当前窗口，即自身；</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 判断当前窗口是否为顶层窗口</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.top === <span class="hljs-built_in">window</span>.self) &#123;
  <span class="hljs-comment">// 当前窗口是顶层窗口</span>
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 当前窗口是子窗口</span>
&#125;

<span class="hljs-comment">// 判断，当前窗口是否为顶层窗口</span>
<span class="hljs-built_in">window</span>.parent.history.back();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与这些变量对应，浏览器还提供一些特殊的窗口名，供window.open()方法、< a > 标签、< form > 标签等引用。</p>
<ol>
<li>_top：顶层窗口;</li>
<li>_parent：父窗口;</li>
<li>_blank：新窗口;</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在顶层窗口打开链接</span>
<a href=<span class="hljs-string">"somepage.html"</span> target=<span class="hljs-string">"_top"</span>>Link</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>8.2  iframe 元素</strong>
对于 iframe 嵌入的窗口，document.getElementById 方法可以拿到该窗口的 DOM 节点，然后使用 contentWindow 属性获得iframe 节点包含的 window 对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> frame = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'theFrame'</span>);
<span class="hljs-keyword">var</span> frameWindow = frame.contentWindow;

<span class="hljs-comment">// 上面代码中，frame.contentWindow 可以拿到子窗口的 window 对象。</span>
<span class="hljs-comment">// 然后，在满足同源限制的情况下，可以读取子窗口内部的属性。</span>
<span class="hljs-comment">// 获取子窗口的标题</span>
frameWindow.title
<span class="copy-code-btn">复制代码</span></code></pre>
<p>< iframe > 元素的 contentDocument 属性，可以拿到子窗口的 document 对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> frame = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'theFrame'</span>);
<span class="hljs-keyword">var</span> frameDoc = frame.contentDocument;

<span class="hljs-comment">// 等同于</span>
<span class="hljs-keyword">var</span> frameDoc = frame.contentWindow.document;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>< iframe >元素遵守同源政策，只有当父窗口与子窗口在同一个域时，两者之间才可以用脚本通信，否则只有使用window.postMessage 方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><iframe> 窗口内部，使用 <span class="hljs-built_in">window</span>.parent 引用父窗口。如果当前页面没有父窗口，则 <span class="hljs-built_in">window</span>.parent 属性返回自身。
因此，可以通过 <span class="hljs-built_in">window</span>.parent 是否等于 <span class="hljs-built_in">window</span>.self，判断当前窗口是否为 iframe 窗口。
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.parent !== <span class="hljs-built_in">window</span>.self) &#123;
  <span class="hljs-comment">// 当前窗口是子窗口</span>
&#125;


<iframe>窗口的<span class="hljs-built_in">window</span>对象，有一个frameElement属性，返回<iframe>在父窗口中的 DOM 节点。
对于非嵌入的窗口，该属性等于<span class="hljs-literal">null</span>。
<span class="hljs-keyword">var</span> f1Element = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'f1'</span>);
<span class="hljs-keyword">var</span> f1Window = f1Element.contentWindow;
f1Window.frameElement === f1Element <span class="hljs-comment">// true</span>
<span class="hljs-built_in">window</span>.frameElement === <span class="hljs-literal">null</span> <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>8.3 window.frames 属性</strong>
window.frames 属性返回一个类似数组的对象，成员是所有子窗口的 window 对象。可以使用这个属性，实现窗口之间的互相引用。
如：frames[0]返回第一个子窗口，frames[1].frames[2]返回第二个子窗口内部的第三个子窗口，parent.frames[1]返回父窗口的第二个子窗口。</p>
<p><strong>注意：</strong> window.frames 每个成员的值，是框架内的窗口（即框架的window对象），而不是iframe标签在父窗口的 DOM 节点。如果要获取每个框架内部的 DOM 树，需要使用 window.frames[0].document 的写法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">如果 <iframe> 元素设置了name或id属性，那么属性值会自动成为全局变量，可通过 <span class="hljs-built_in">window</span>.frames 属性引用，返回子窗口的 <span class="hljs-built_in">window</span> 对象。

<span class="hljs-comment">// HTML 代码为 <iframe id="myFrame"></span>
<span class="hljs-built_in">window</span>.myFrame <span class="hljs-comment">// [HTMLIFrameElement]</span>
frames.myframe === myFrame <span class="hljs-comment">// true</span>

name属性的值会自动成为子窗口的名称，可以用在<span class="hljs-built_in">window</span>.open方法的第二个参数，或者<a>和<frame>标签的target属性
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            