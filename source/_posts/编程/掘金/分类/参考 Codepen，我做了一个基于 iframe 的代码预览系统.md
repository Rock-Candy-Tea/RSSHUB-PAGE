
---
title: '参考 Codepen，我做了一个基于 iframe 的代码预览系统'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61ff634d90f24ba3b42e554faee61eb2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 20:38:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61ff634d90f24ba3b42e554faee61eb2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>一直觉得 Codepen 的在线代码预览系统很神奇，能够所见即所得地实时展示代码的运行效果，无论是代码演示，还是测试功能，都是非常方便快捷的存在。刚好最近手头有业务需要用到类似 Codepen 的能力，经过一番调研之后开发了一个具有基本的在线运行代码能力的 demo 出来。</p>
<blockquote>
<p>在线体验地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjrainlau.github.io%2Fonline-code-runner%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jrainlau.github.io/online-code-runner/" ref="nofollow noopener noreferrer">jrainlau.github.io/online-code…</a></p>
<p>由于业务只需要执行 JS 代码，因此 demo 也只具备 JS 代码的运行能力。</p>
</blockquote>
<h1 data-id="heading-0">一、原理</h1>
<p>我们知道，浏览器是通过自带的引擎来处理 html，css 和 js 资源的，处理过程在页面载入的时候就已经开始。如果我们想要动态地运行这些资源，对于 html 和 css 我们可以用 DOM 操作的方式，对于 js 我们可以用 <code>eval</code> 或者 <code>new Function()</code>。但是这些操作都偏复杂且不安全（<code>eval</code> 和 <code>new Function()</code>很容易出事），那么有没有什么办法可以既优雅方便，又能安全地动态运行呢？我们看看大名鼎鼎的 Codepen 是怎么做的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61ff634d90f24ba3b42e554faee61eb2~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我在 Codepen 里面简单地写了一个按钮，绑定了样式和点击事件，可以看到白色区域已经展示出我们想要的结果。打开控制台自吸观察后可以发现，整个白色区域是一个 <code>iframe</code>，当中的 html 内容就是我们刚刚所编辑的代码。</p>
<p>不难想象，它的运行原理有点类似于 <code>document.write</code>，把内容直接写入到某一个 html 文件中，然后把它以 iframe 的方式内嵌到其他网页当中，实现代码预览的逻辑。那么使用 iframe 有什么好处呢？iframe 可以独立成为一个和宿主隔离的沙箱环境，在当中运行的代码在大部分情况下不会影响宿主，能有效地保证安全。配合 HTML5 新增的 <code>sandbox</code> 属性，可以给 iframe 定义更为精细的权限，比如是否允许它运行脚本，是否允许它弹窗等等。</p>
<h1 data-id="heading-1">二、实现方式</h1>
<p>要实现类似 Codepen 的效果，最重要的一步就是如何把代码注入到 iframe 当中。由于我们需要使用到操控 iframe 的相关 API，浏览器出于安全的考虑，我们只能使用<strong>同域的 iframe 链接</strong>，否则将会报跨域的错误。</p>
<p>首先准备好一个 <code>index.html</code> 和 <code>iframe.html</code>，使用一个静态资源服务器把它们跑起来，假设均跑在 <code>localhost:8080</code>。然后我们在 <code>index.html</code> 里面插入一个 iframe，其链接就是 <code>localhost:8080/iframe.html</code>，代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">iframe</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"localhost:8080/iframe.html"</span>></span><span class="hljs-tag"></<span class="hljs-name">iframe</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们可以使用 <code>iframe.contentDocument</code> 来获取 iframe 的内容，然后操作它：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="handlebars"><span class="xml">
  const ifrme = document.querySelector('iframe');
  const iframeDoc = iframe.contentDocument;
  iframeDoc.open(); // 需要先调用 `open()`，打开“写”的开关

  iframeDoc.write(`
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css"><span class="hljs-selector-tag">button</span> &#123; <span class="hljs-attribute">color</span>: red &#125;</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span>></span>Click<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'button'</span>).addEventListener(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'on-click!'</span>)
      &#125;)
    <\/script>
  </body>
  <span class="hljs-string">`);

  iframeDoc.close(); // 最后调用 `</span>close()<span class="hljs-string">`，关闭“写”的开关
</span></span></span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行完毕后，我们可以在 <code>localhost:8080/index.html</code> 里面看到和前文 Codepen 所展示的一样的效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d10b2a83db484ad29a7cb83af6e3ec2b~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4554ff7c81f44bd90f082249c28e405~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>后续我们只需要找个输入框，把所写的代码保存成变量，然后调用 <code>iframeDoc.write()</code> 就可以动态地把代码写入到 iframe 并实时运行了。</p>
<h1 data-id="heading-2">三、控制台输出及安全</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1360c9a19ed4552b25468c321a28c3d~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>观察 Codepen 的页面，可以看到有一个 Console 的面板，它可以把 iframe 当中的 <code>console</code> 信息直接输出。这是怎么实现的呢？答案很简单，我们可以在 iframe 页面中劫持 <code>console</code> 等 API，在保留原有的控制台输出的功能的前提下，把相关的信息通过 <code>postMessage</code> 的方式把它们输出给父页面，父页面监听到 message 以后把信息整理后输出到页面上，实现 Console 面板。</p>
<p>在 <code>iframe.html</code> 中，我们在<code><body></body></code> 以外写入一段 js 代码（因为父页面调用 <code>iframeDoc.write()</code> 会覆盖 <code><body></body></code> 内的全部内容）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">rewriteConsole</span>(<span class="hljs-params">type</span>) </span>&#123;
  <span class="hljs-keyword">const</span> origin = <span class="hljs-built_in">console</span>[type];
  <span class="hljs-built_in">console</span>[type] = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;
    <span class="hljs-built_in">window</span>.parent.postMessage(&#123; <span class="hljs-attr">from</span>: <span class="hljs-string">'codeRunner'</span>, type, <span class="hljs-attr">data</span>: args &#125;, <span class="hljs-string">'*'</span>);
    origin.apply(<span class="hljs-built_in">console</span>, args);
  &#125;;
&#125;

rewriteConsole(<span class="hljs-string">'log'</span>);
rewriteConsole(<span class="hljs-string">'info'</span>);
rewriteConsole(<span class="hljs-string">'debug'</span>);
rewriteConsole(<span class="hljs-string">'warn'</span>);
rewriteConsole(<span class="hljs-string">'error'</span>);
rewriteConsole(<span class="hljs-string">'table'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外我们会给 iframe 设置 <code>sandbox</code> 属性来限制其部分权限，但是这里有一个套娃的隐患，就是如果在 iframe 里面执行 <code>window.parent.document</code> 相关 API 的话，可以让 iframe 去改写父页面的内容，甚至改写 <code>sandbox</code> 属性，这肯定是不安全的，因此我们需要在 iframe 中把这相关 API 给屏蔽掉：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">window</span>, <span class="hljs-string">'disableParent'</span>, &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'无法调用 window.parent 属性！'</span>);
  &#125;,
  <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在调用父页面的 <code>iframeDoc.write(code)</code> 之前，我们需要先把用户输入的自定义代码 <code>code</code> 进行一次 <code>replace</code>，把当中的所有 <code>parent.document</code> 改成 <code>window.disableParent</code>。当用户调用 <code>parent.document</code> 相关 API 时，实际在 iframe 运行的是 <code>window.disableParent</code>，届时将会直接报错<code>无法调用 window.parent 属性！</code>，有效避免了套娃的安全隐患。</p>
<h1 data-id="heading-3">四、使用 monaco-editor 实现编辑模块和 Console 面板模块</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44a9a6c67ade4a8497655a351816116e~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我所搭建的这个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fjrainlau.github.io%2Fonline-code-runner%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jrainlau.github.io/online-code-runner/" ref="nofollow noopener noreferrer">online-code-runner</a> 是基于 monaco-editor 来实现编辑模块和 Console 面板模块的，接下来会简单讲述它们分别都是怎么实现的。</p>
<hr>
<p>对于编辑模块来说，就是一个简单的 monaco-editor，只需要简单地设置它的样式就可以了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">monaco.editor.create(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#editor'</span>), &#123;
  &#123;
    <span class="hljs-attr">language</span>: <span class="hljs-string">'javascript'</span>,
    <span class="hljs-attr">tabSize</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">autoIndent</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">theme</span>: <span class="hljs-string">'github'</span>,
    <span class="hljs-attr">automaticLayout</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">wordWrap</span>: <span class="hljs-string">'wordWrapColumn'</span>,
    <span class="hljs-attr">wordWrapColumn</span>: <span class="hljs-number">120</span>,
    <span class="hljs-attr">lineHeight</span>: <span class="hljs-number">28</span>,
    <span class="hljs-attr">fontSize</span>: <span class="hljs-number">16</span>,
    <span class="hljs-attr">minimap</span>: &#123;
      <span class="hljs-attr">size</span>: <span class="hljs-string">'fill'</span>,
    &#125;,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击”执行代码“的按钮后，可以通过 <code>editor.getValue()</code> 把编辑模块中的内容读取出来，然后交给 iframe 去运行。</p>
<hr>
<p>对于 Console 面板来说，它是另一个<strong>只读</strong>的 monaco-editor，主要有2个问题会有一点点费劲。其一是如何让新添加的内容挨个插入进去；其二是如何根据不同的 <code>console</code> 类型产生不用的背景色。</p>
<p>问题一的解法很简单，只需要定义一个<strong>字符串类型</strong>变量 <code>infos</code>，每当监听到来自 iframe 的 <code>postMessage()</code> 时，就往 <code>infos</code> 添加当中的信息，最后调用 <code>editor.setValue()</code> 即可。</p>
<p>问题二的解法，我们已经在 iframe 中劫持 <code>console</code> 的逻辑，在 <code>postMessage</code> 的时候同时告诉父页面 <code>consle[type]</code> 到底是 <code>log</code> 还是 <code>warn</code> 还是其他，因此父页面可以根据这里的 <code>console[type]</code> 来知道具体的类型。</p>
<p>接下来我们可以调用 <code>editor.deltaDecorations</code> 方法来设置某行某列的背景色：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> deltaDecorations = []

<span class="hljs-comment">// 每当有新的 consle 消息推送过来时，都往 deltaDecorations 里插入一条信息，后面会用到</span>
<span class="hljs-comment">// 这里的 startLine 和 endLine 代表着这条新的消息的起始行号和结束行号，需要自行记录</span>
<span class="hljs-comment">// `$&#123;info.type&#125;Decoration` 为不同 `console[type]` 的背景色对应的 className，对应着具体的 CSS</span>
deltaDecorations.push(&#123;
  <span class="hljs-attr">range</span>: <span class="hljs-keyword">new</span> monaco.Range(startLine, <span class="hljs-number">1</span>, endLine, <span class="hljs-number">1</span>),
  <span class="hljs-attr">options</span>: &#123; <span class="hljs-attr">isWholeLine</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">className</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;info.type&#125;</span>Decoration`</span> &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们可以定义不同 <code>consle[type]</code> 对应的背景色 CSS：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.warnDecoration</span> &#123;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#ffd900</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span> <span class="hljs-meta">!important</span>;
&#125;
<span class="hljs-selector-class">.errorDecoration</span> &#123;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#ff3300</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span> <span class="hljs-meta">!important</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体代码可以看这里：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjrainlau%2Fonline-code-runner%2Fblob%2Fmain%2Fsrc%2Fcomponents%2FConsole.vue%23L62-L71" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jrainlau/online-code-runner/blob/main/src/components/Console.vue#L62-L71" ref="nofollow noopener noreferrer">github.com/jrainlau/on…</a></p>
<h1 data-id="heading-4">五、小结</h1>
<p>本文通过分析 Codepen 的实现方式，使用 iframe 的方式配合 monaco-editor 自行开发了一套专用于执行 JavaScript 代码的在线代码预览系统。除了可以作为代码预览、展示的作用外，对于一些管理系统而言，往往需要人为编写一些后置脚本来处理系统中的数据，正好可以利用本文的方式去搭建一套代码预览系统，实时又安全地预览后置脚本，用处非常大。</p></div>  
</div>
            