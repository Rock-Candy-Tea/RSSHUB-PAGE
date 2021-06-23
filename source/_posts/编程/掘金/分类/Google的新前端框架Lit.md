
---
title: 'Google的新前端框架Lit'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0dc1fe8b4bd44518dedb91321005a86~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 22 Jun 2021 02:07:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0dc1fe8b4bd44518dedb91321005a86~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0dc1fe8b4bd44518dedb91321005a86~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Google的新框架 <code>Lit</code> ，有 Google 加持的框架引起了我的兴趣，就去简单的了解了一下，简单的给大家分享一下学习成果。由于<code>Lit</code>框架还在快递迭代中，文中讲到的一些代码实现很可能已经重构，感兴趣的同学，可以去翻一下<code>Lit</code>源码。</p>
<h2 data-id="heading-0">什么是 Lit</h2>
<p><code>Lit</code> 是一个基于 <code>Web-Component</code> 构建的前端框架，前身基本可以理解为即 <code>Polymer</code> ， <code>Lit</code> 提供了如下具有竞争力的特性</p>
<ul>
<li>
<p>基于 <code>Web-Component</code> 的更高层封装，提供了现代前端开发习惯的响应式数据，声明式的模版，减少了web component的一部分样板代码.</p>
</li>
<li>
<p>小。运行时仅有5K</p>
</li>
<li>
<p>性能强悍。规避了 <code>VDOM</code> 的一些弊端，更新时仅处理 UI 中的异步部分（可以理解成仅处理响应式的部分）</p>
</li>
<li>
<p>兼容性较好。因为 <code>web-component</code> 是 HTML 的原生能力，也就代表着 <code>web-component</code> 可以在任何使用 HTML 的地方使用，框架无关。</p>
</li>
</ul>
<p>小和框架无关是促使我关注这个框架的一个重点（svelte也是，有时间再说，学不动了），因为对于一些通用业务代码来说， <strong>运行时尽可能的小</strong> 和 <strong>框架无关</strong> 是最核心的两个技术选型指标。</p>
<h2 data-id="heading-1"></h2>
<h2 data-id="heading-2">什么是 Web-Component</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f4ee8b491d34226a9831087d14fbe84~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Web Components is a suite of different technologies allowing you to create reusable custom elements — with their functionality encapsulated away from the rest of your code — and utilize them in your web apps.</p>
</blockquote>
<p>我个人认为，组件化是现在前端快速发展和规模壮大的一个比较重要的原因，想想写 JQ 的年代，HTML 代码基本都长这个样子</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"button1"</span> ></span>按钮<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"button2 active"</span> ></span>按钮<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"button3"</span> ></span>按钮<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>哪怕后面出现了模版语法，状况也没有变得更好（与服务端协作共用模版 -> JSP or 要在JS中封装方法，通过模版语法注入 -> handlebars），单纯的loop循环渲染可能能方便的解决DOM复用的问题，但是跨层级的组件复用仍然是一个问题。</p>
<p>因此任何一个想要进一步发展的前端框架技术，组件化是必不可少的一步。 <code>Web-Component</code> 就是这样一个浏览器原生支持的创建可重用元素（自定义组件）的能力，而 <code>Lit</code> 则是基于 <code>Web-Component</code> 构建的。</p>
<p>那我们需要先了解下 Web-Component</p>
<h2 data-id="heading-3">Web-Component 的简单开发流</h2>
<blockquote>
<p>Create a class in which you specify your web component functionality, using the ECMAScript 2015 class syntax <br>
Register your new custom element using the <a href="https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry/define" target="_blank" rel="nofollow noopener noreferrer">CustomElementRegistry.define()</a> method, passing it the element name to be defined, the class or function in which its functionality is specified, and optionally, what element it inherits from.<br>
If required, attach a shadow DOM to the custom element using <a href="https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow" target="_blank" rel="nofollow noopener noreferrer">Element.attachShadow()</a> method. Add child elements, event listeners, etc., to the shadow DOM using regular DOM methods.<br>
If required, define an HTML template using <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template" target="_blank" rel="nofollow noopener noreferrer"><code><template></code></a> and <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot" target="_blank" rel="nofollow noopener noreferrer"><code><slot></code></a> . Again use regular DOM methods to clone the template and attach it to your shadow DOM.<br>
Use your custom element wherever you like on your page, just like you would any regular HTML element.</p>
</blockquote>
<p>我们先了解 Web-Component 的两个核心点，了解了这两个属性就可以构建你自己的组件了</p>
<h3 data-id="heading-4">Custom Element 自定义元素</h3>
<p>首先，我们需要通过浏览器提供的 <code>**CustomElementRegistry**</code> ****接口实例注册自定义元素，实例被挂载在 <code>window.customElements</code> 上</p>
<p>CustomElementRegistry的 <code>define</code> 方法可以用来注册一个自定义的元素，有两种类型可选</p>
<ul>
<li>
<p><strong>自定义元素</strong> ：独立元素，行为完全由开发者定义。</p>
</li>
<li>
<p><strong>自定义内置元素</strong> ：这些元素继承并扩展内置HTML元素</p>
</li>
</ul>
<p>API如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">customElements.define(name, <span class="hljs-title">constructor</span>, <span class="hljs-title">options</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b20b419f22c14060aab9513ced1bd587~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>name</strong> 就是你自定义的元素名称（符合 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/DOMString" target="_blank" rel="nofollow noopener noreferrer">DOMString</a> 标准，必须带短横线），以上述为例，可以通过 <code><my-component></my-component></code> 的形式使用
<strong>constructor</strong> 就是我们定义的组件
<strong>options</strong> 声明了我们定义的是哪种类型的自定义元素，目前只有一个extends可用，指定继承于什么元素。
当定义了继承什么元素之后，使用方式就与自定义元素不太一致了，需要用到 <strong>is</strong> 属性假设你定义了一个名为my-paragraph的继承自p标签的自定义内置元素，那么使用时，需要 <code><p is="my-paragraph"></p></code> 这样写</p>
<p>这么看来， <code>Web-Component</code> 的逻辑核心就在constructor上了，我们如何定义一个自己的 component 呢？
不同于 React 和 Vue，可以在 render 方法中书写 JSX 或者模版语法来创建一颗 VDOM 树来定义组件结构。 <code>Web-Component</code> 并没有提供可以用来书写模版的方式（但这也代表着他可以使用任何模版语法）。通常是使用常规的 DOM 操作来在 constructor 中创建你的组件结构。举个栗子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HTMLElement</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">super</span>()

      <span class="hljs-keyword">const</span> wrapper = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'span'</span>);
      wrapper.setAttribute(<span class="hljs-string">'class'</span>,<span class="hljs-string">'wrapper'</span>);
      <span class="hljs-keyword">const</span> info = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'span'</span>);
      info.setAttribute(<span class="hljs-string">'class'</span>,<span class="hljs-string">'info'</span>);
      info.textContent = <span class="hljs-built_in">this</span>.getAttribute(<span class="hljs-string">'text'</span>) || <span class="hljs-string">'default'</span>;

      <span class="hljs-built_in">this</span>.appendChild(wrapper);
      wrapper.appendChild(info);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这段代码创建了一个根据双层span嵌套的文本节点</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">my-component</span>></span><span class="hljs-tag"></<span class="hljs-name">my-component</span>></span>
<span class="hljs-comment"><!-- 等价于 --></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"info"</span>></span>default<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>

<span class="hljs-tag"><<span class="hljs-name">my-component</span> <span class="hljs-attr">text</span>=<span class="hljs-string">"test"</span>></span><span class="hljs-tag"></<span class="hljs-name">my-component</span>></span>
<span class="hljs-comment"><!-- 等价于 --></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"info"</span>></span>test<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，单纯的创建UI没有什么意思，我们来思考下，现代框架还提供了什么能力？</p>
<p>响应式！事件绑定！lifecycle！</p>
<p>OK，安排。</p>
<p>先说比较简单的事件绑定，既然 DOM 都是内部创建的，那么绑定事件也是轻而易举（注意this指向）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HTMLElement</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">super</span>()
      <span class="hljs-built_in">this</span>.handleClick = <span class="hljs-built_in">this</span>.handleClick.bind(<span class="hljs-built_in">this</span>)

      <span class="hljs-keyword">const</span> wrapper = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'span'</span>);
      wrapper.setAttribute(<span class="hljs-string">'class'</span>,<span class="hljs-string">'wrapper'</span>);
      <span class="hljs-keyword">const</span> info = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'span'</span>);
      info.setAttribute(<span class="hljs-string">'class'</span>,<span class="hljs-string">'info'</span>);
      info.textContent = <span class="hljs-built_in">this</span>.getAttribute(<span class="hljs-string">'text'</span>) || <span class="hljs-string">'default'</span>;

      <span class="hljs-built_in">this</span>.appendChild(wrapper);
      wrapper.appendChild(info);

      <span class="hljs-keyword">const</span> button = <span class="hljs-built_in">this</span>.querySelector(<span class="hljs-string">'#button'</span>);
      button.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-built_in">this</span>.handleClick)
    &#125;

    handleClick () &#123;
      <span class="hljs-built_in">this</span>.parentNode.removeChild(<span class="hljs-built_in">this</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">my-life-cycle-component</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'button'</span>></span>Remove this<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">my-life-cycle-component</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码创建在之前的文本基础上，多了一个按钮，点一下这个按钮就会把整个 custom element 移除掉（当然，这个按钮也可以由组件自己创建）</p>
<p>然后我们再来说 <strong>lifecycle</strong> ，customeElemnts.define接受的构造函数中，允许开发者定义如下几个生命周期，会在相关的时机被调用</p>
<ul>
<li>
<p><code>connectedCallback</code> ：当 custom element 首次被插入文档DOM时，被调用。</p>
</li>
<li>
<p><code>disconnectedCallback</code> ：当 custom element 从文档DOM中删除时，被调用。</p>
</li>
<li>
<p><code>adoptedCallback</code> ：当 custom element 被移动到新的文档时，被调用。</p>
</li>
<li>
<p><code>attributeChangedCallback</code> ：当 custom element 增加、删除、修改自身属性时，被调用</p>
</li>
</ul>
<p>简单来说，就是</p>
<ul>
<li>
<p>componentDidMount</p>
</li>
<li>
<p>componentWillUnmount</p>
</li>
<li>
<p>Not exist（这个我还没测试出什么场景会用出现）</p>
</li>
<li>
<p>componentDidUpdate</p>
</li>
</ul>
<p>因为没有 state 这个概念，所有的组件内部属性的变化监听都需要我们手动处理，心智负担可能会略重一些。
<del>当然也可以把他们作为自定义元素的属性，通过</del> <code>~~attributeChangedCallback~~</code> <del>处理</del></p>
<p>顺路，有了属性变化的回调响应式也就出来了（当然，只是响应式的基础，属性变化并不会直接作用到内部渲染逻辑上，心智负担 <strong>+1</strong> ）
如果需要在元素属性变化后，触发回调函数，必须通过定义 <code>observedAttributes()</code> get函数来监听这个属性</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b5a8ff0e66941b0949a2fab4f555b5e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">my-life-cycle-component</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'button1'</span>></span>Remove this<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'button2'</span>></span>Toggle this<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">my-life-cycle-component</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看下代码，这里定义了一个带输入框的组件，输入框输入后，会重新渲染 componnet 内部的文本。同时监听 style 属性，变化后打印出来（无意义的demo +1）</p>
<h3 data-id="heading-5">Shadow DOM 影子DOM</h3>
<p><code>Shadow DOM</code> 的好处有很多。
<code>Shadow DOM</code> 主要的作用在于，“他可以将独立的一个DOM（style标签也属于）附加到元素上（这个DOM是隐藏的），且不会影响外层的样式，这给web component带来了十分强大的封装能力，能够完全的将组件的结构，样式和行为动作对外隐藏起来，对外隔离”]</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17d444eef72343c8beb6fd39feded2a0~tplv-k3u1fbpfcp-watermark.image" alt="image-6-1624330780387.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有一个需要关注的概念 - <code>Shadow boundary</code>
<code>Shadow boundary</code> 指的是 <code>Shadow DOM</code> 结束的地方，也是常规 DOM 开始的地方。整个 <code>shadow dom</code> 内的样式、元素都不会对外影响超过 <code>shadow boundary</code> 的范围。</p>
<blockquote>
<p>Shadow DOM 不是一个新事物——在过去的很长一段时间里，浏览器用它来封装一些元素的内部结构。以一个有着默认播放控制按钮的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/video" target="_blank" rel="nofollow noopener noreferrer"><code><video></code></a> 元素为例。你所能看到的只是一个 <code><video></code> 标签，实际上，在它的 Shadow DOM 中，包含来一系列的按钮和其他控制器。Shadow DOM 标准允许你为你自己的元素（custom element）维护一组 Shadow DOM。
<em>引用自MDN</em></p>
</blockquote>
<p>那么，如何使用呢？
有一个核心API， <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Element/attachShadow" target="_blank" rel="nofollow noopener noreferrer">Element.attachShadow(&#123;mode: &#125;)</a> ，可以将一个 shadow root 附加到任何一个元素上，mode 的取值有 open 或者 closed。区别在于能否从外部获取到 shadowDOM 的结构。想要更深入的了解 open 和 close 的区别可以参考 <a href="https://blog.revillweb.com/open-vs-closed-shadow-dom-9f3d7427d1af" target="_blank" rel="nofollow noopener noreferrer">blog.revillweb.com/open-vs-clo…</a> 这篇文章，这里就不展开描述了。</p>
<p>那么，拿上边最简单的那个例子做一下改造</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">customElements.define(<span class="hljs-string">'my-component'</span>, <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HTMLElement</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">super</span>()

      <span class="hljs-keyword">const</span> shadow = <span class="hljs-built_in">this</span>.attachShadow(&#123;<span class="hljs-attr">mode</span>: <span class="hljs-string">'open'</span>&#125;);
      <span class="hljs-keyword">const</span> info = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'span'</span>);

      info.setAttribute(<span class="hljs-string">'class'</span>,<span class="hljs-string">'info'</span>);
      info.textContent = <span class="hljs-built_in">this</span>.getAttribute(<span class="hljs-string">'text'</span>) || <span class="hljs-string">'default'</span>;

      <span class="hljs-comment">// this.appendChild(info)</span>
      shadow.appendChild(info);
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就创建了一个基于 shadowDOM 的自定义元素了，看起来没什么差别，我们再添加一些自定义的样式试试</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">customElements.define(<span class="hljs-string">'my-component'</span>, <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HTMLElement</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">super</span>()

      <span class="hljs-keyword">const</span> shadow = <span class="hljs-built_in">this</span>.attachShadow(&#123;<span class="hljs-attr">mode</span>: <span class="hljs-string">'open'</span>&#125;);
      <span class="hljs-keyword">const</span> info = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'span'</span>);

      info.setAttribute(<span class="hljs-string">'class'</span>,<span class="hljs-string">'info'</span>);
      info.textContent = <span class="hljs-built_in">this</span>.getAttribute(<span class="hljs-string">'text'</span>) || <span class="hljs-string">'default'</span>;

      <span class="hljs-keyword">const</span> style = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'style'</span>)
      style.textContent = <span class="hljs-string">`
        span &#123;
          color: red;
        &#125;
      `</span>
      <span class="hljs-comment">// this.appendChild(info)</span>
      shadow.appendChild(style);
      shadow.appendChild(info);

    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以尝试在页面的其他地方也添加一些span标签，但是你会发现，只有  下面的 span 标签生效了红色的样式。</p>
<p>上述两个属性可以创建一个不受外部影响，且拥有内部JS运行逻辑、拥有独立CSS的自定义元素（也就是Web Component）
我觉得大家已经开始在吐槽，这种类JQ的写法简直是异类，DOM复杂起来之后就很难整了。那么如何组装更复杂的dom，难道无解了么？不，那么这里需要提到另外一个属性</p>
<h3 data-id="heading-6">Template & Slot</h3>
<p>template 元素是浏览器一直以来都支持的一个特性，template 中的内容在渲染 HTML 到屏幕上的时候不会显示出来，需要通过 Javascript 获取到模版后才能实例化，并渲染到页面上。
那么，我们可以把 template 作为一个可以储存在文档中的内容片段，然后在组件渲染的时候把 template 填充到 <code>Web-Component</code> 的 <code>shadow dom</code> 里面。还是拿上边的那个例子做修改</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"my-component"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">span</span> &#123;
          <span class="hljs-attribute">color</span>: red;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"info"</span>></span>
        12312312
    <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">customElements.define(<span class="hljs-string">'my-component'</span>, <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HTMLElement</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">super</span>()

      <span class="hljs-keyword">const</span> template = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'my-paragraph'</span>);
      <span class="hljs-keyword">const</span> templateContent = template.content.cloneNode(<span class="hljs-literal">true</span>);
      <span class="hljs-keyword">const</span> shadow = <span class="hljs-built_in">this</span>
          .attachShadow(&#123;<span class="hljs-attr">mode</span>: <span class="hljs-string">'open'</span>&#125;)
          .appendChild(templateContent);      
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样以来，是不是有点 Vue 那个意思了，但是还缺点什么，my-component 上之前可以读取 text 属性填充到 <a href="http://span.info/" target="_blank" rel="nofollow noopener noreferrer">span.info</a> 里面，现在好像没有这个能力了。</p>
<p>这个时候需要请出我们的 slot 槽来做这件事</p>
<blockquote>
<p><strong>HTML<code><slot></code>元素 ，</strong> 作为 <a href="https://developer.mozilla.org/en-US/docs/Web/Web_Components" target="_blank" rel="nofollow noopener noreferrer">Web Components</a> 技术套件的一部分，是Web组件内的一个占位符。该占位符可以在后期使用自己的标记语言填充，这样您就可以创建单独的DOM树，并将它与其它的组件组合在一起。</p>
</blockquote>
<p>Slot 通过 name 属性标示，放置的位置表示他在模版中的位置，当有另外一个元素定义了同名的 slot 属性，那么这个元素就会被替换到模版中。我们修改下上边的那个例子</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 使用 --></span>
<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"my-component"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">span</span> &#123;
          <span class="hljs-attribute">color</span>: red;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"my-slot"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'info'</span> ></span>default<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-comment"><!-- 使用 --></span>
<span class="hljs-tag"><<span class="hljs-name">my-component</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"my-slot"</span>></span>
        12312312
    <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">my-component</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">customElements.define(<span class="hljs-string">'my-component'</span>, <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HTMLElement</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">super</span>()

      <span class="hljs-keyword">const</span> template = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'my-paragraph'</span>);
      <span class="hljs-keyword">const</span> templateContent = template.content.cloneNode(<span class="hljs-literal">true</span>);
      <span class="hljs-keyword">const</span> shadow = <span class="hljs-built_in">this</span>
          .attachShadow(&#123;<span class="hljs-attr">mode</span>: <span class="hljs-string">'open'</span>&#125;)
          .appendChild(templateContent);      
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然这里只是最为简单的用法，但至此，基本上 <code>Web-Component</code> 你就算入门了。整体写起来难度也不算太高，但还是有不少值得吐槽的地方 <a href="https://www.webcomponents.org/introduction" target="_blank" rel="nofollow noopener noreferrer">（更多关于Web Component）</a> 。那么我们来看看 <code>Lit</code> 做了啥，能不能让 <code>Web-Component</code> 变得更好用些</p>
<h2 data-id="heading-7">Lit做了啥</h2>
<p>看下我们刚才说到的 <code>Web-Component</code> 里面的几个槽点</p>
<ol>
<li>
<p>响应式仅有回调，无法自动映射到UI上</p>
</li>
<li>
<p>没有 state 内部状态，自己维护的状态无法直接监听变化</p>
</li>
<li>
<p>没有模版语法（可以用 slot 和 template）</p>
</li>
</ol>
<p>明确一点，在学习 <code>Lit</code> 的过程中，可以认为没有 state 这个概念（实际上有，理解为私有的 reactive properties），只有名为 <code>reactive properties</code> 的成员属性。可以简单的理解成又是 state，又是 props。</p>
<p>那么现在问题转变成了</p>
<ol>
<li>
<p>如何响应reactive properties的变化，并应用到UI上</p>
</li>
<li>
<p>如何解决模版语法</p>
</li>
</ol>
<p>Lit 用了两个个核心库来解决这个问题，分别是 <code>lit-element</code> 和 <code>lit-html</code></p>
<h3 data-id="heading-8">Lit-html</h3>
<p><code>lit-html</code> 是 <code>Lit</code> 的核心逻辑，可以理解为 <code>Literal Html</code> ，他异于JSX创造了另外一种高性能的字符流HTML模版引擎。
Lit选择了直接继承Polymer的LitHTML项目，并将整体框架重命名为 Lit
我们知道 <code>jsx</code> 是需要编译的它的底层最终还是 <code>createElement</code> ....。而 <code>lit-html</code> 就不一样了，它是基于 <code>tagged template</code> 的，使得它不用编译就可以在浏览器上运行，并且和 <code>HTML Template</code> 结合想怎么玩怎么玩，扩展能力更强。下面我们展开来看。</p>
<p><code>lit-html</code> 提供了两个核心方法 <code>render</code> 和 <code>html</code></p>
<h4 data-id="heading-9">lit-html.html</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">html`<span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span></span><span class="hljs-subst">$&#123;content&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">p</span>></span>`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个是es6的原生语法 - <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Template_literals#%E5%B8%A6%E6%A0%87%E7%AD%BE%E7%9A%84%E6%A8%A1%E6%9D%BF%E5%AD%97%E7%AC%A6%E4%B8%B2" target="_blank" rel="nofollow noopener noreferrer">带标签的模板字符串</a> （tagged template），并不是什么magic，html 这个函数会接受到如下的参数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">type taggedFunc = <span class="hljs-function">(<span class="hljs-params">strings: string[], ...values: any[]</span>) =></span> any;
<span class="hljs-comment">// 上边的那个段代码接收到的参数就是</span>
<span class="hljs-comment">// ['<p>', '</p'>], content</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过 <code>lit-html</code> 的修饰上面这段代码最终会构造一个 <code>Template Result</code> 对象，形如</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">declare</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TemplateResult</span> </span>&#123;
    <span class="hljs-keyword">readonly</span> strings: TemplateStringsArray;
    <span class="hljs-keyword">readonly</span> values: <span class="hljs-keyword">readonly</span> unknown[];
    <span class="hljs-keyword">readonly</span> <span class="hljs-keyword">type</span>: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// html or svg</span>
    <span class="hljs-keyword">readonly</span> processor: TemplateProcessor;
    <span class="hljs-title">constructor</span>(<span class="hljs-params">strings: TemplateStringsArray, values: <span class="hljs-keyword">readonly</span> unknown[], <span class="hljs-keyword">type</span>: <span class="hljs-built_in">string</span>, processor: TemplateProcessor</span>);
    
    getHTML(): <span class="hljs-built_in">string</span>;
    getTemplateElement(): HTMLTemplateElement;
&#125;

<span class="hljs-keyword">const</span> templateResult = &#123;
    <span class="hljs-attr">strings</span>: [<span class="hljs-string">'<p>'</span>, <span class="hljs-string">'</p>'</span>],
    <span class="hljs-attr">value</span>: [content]
    <span class="hljs-attr">type</span>: <span class="hljs-string">'html'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意一下 <code>getHTML</code> 和 <code>getTemplateElement</code> 方法，这两个方法可以将strings转化成为一个 <code><template></code> 标记，也就是上面提到的 template</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> template = <span class="hljs-function">(<span class="hljs-params">title, content, className</span>) =></span> html`<span class="xml">
  <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"</span></span></span><span class="hljs-subst">$&#123;className&#125;</span><span class="xml"><span class="hljs-tag"><span class="hljs-string">"</span>></span></span><span class="hljs-subst">$&#123;title&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span></span><span class="hljs-subst">$&#123;content&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
`</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-htmlbars copyable" lang="htmlbars"><span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>$<span class="hljs-attr">lit</span>$=<span class="hljs-string">\</span>"</span></span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">lit-7227407027270176</span>&#125;&#125;</span><span class="xml"><span class="hljs-tag">\"></span><span class="hljs-comment"><!--</span></span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">lit-7227407027270176</span>&#125;&#125;</span><span class="xml"><span class="hljs-comment">--></span><span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-comment"><!--</span></span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">lit-7227407027270176</span>&#125;&#125;</span><span class="xml"><span class="hljs-comment">--></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>简单的解释一下，这个过程就是逐个处理strings中的数据，根据不同的情况</p>
<ul>
<li>
<p>Attribute</p>
</li>
<li>
<p>Node</p>
</li>
<li>
<p>Comment</p>
</li>
</ul>
<p>拼接成一个完整的字符串，然后innerHTML插入到创建好的template标记中。
Q：如何区分代码中真正的comment？</p>
<h4 data-id="heading-10">lit-html.render</h4>
<p>现在我们有了通过标签模版得到的 <code>TemplateResult</code> （一个纯值对象），接下来需要调用 <code>render</code> 方法去渲染模版到页面上，先看API
<code>render(templateResult, container, options?)</code>
<code>render</code> 接收一个 <code>templateResult实例</code> 和 container 渲染容器来完成一次渲染，这里分为首次渲染和更新渲染。</p>
<h5 data-id="heading-11">首次渲染</h5>
<p>先创建一个 <code>NodePart</code> 对象（继承自Part，可以理解为节点的构造器controller，这个是核心实现，暂时不展开，后面来看），然后调用 <code>NodePart</code> 实例的 <code>appendInto</code> 方法，在渲染容器中加入两个 <code>comment</code> ，同时记录了两个 <code>comment</code> 的引用。后续 <code>NodePart</code> 会把 <code>DOM</code> 渲染到这两个 <code>comment</code> 中间</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"container"</span>></span><span class="hljs-comment"><!---><!---></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-comment"><!-- 他是使用comment作为占位符的。 --></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后会调用 <code>part.commit</code> 方法，将内容渲染到容器中
commit分为了几种情况</p>
<ul>
<li>
<p>directive</p>
</li>
<li>
<p>primitive（原始类型）</p>
</li>
<li>
<p>templateResult</p>
</li>
<li>
<p>node</p>
</li>
<li>
<p>Iterable</p>
</li>
<li>
<p>清空</p>
</li>
</ul>
<p>根据前面的逻辑，第一次一定会直接走进 <code>templateResult</code> 的分支，这里的逻辑可以简单这么描述，
通过 <code>Factory</code> ，使用 <code>TemplateResult</code> 中的模版部分 strings 创建一个 <code>Template</code> 对象（中间产物）， <code>Factory</code> 这里做了一层缓存，如果使用 <code>TemplateResult</code> 的模版（strings）有现成的模版的话，直接使用现成的模版，如果没有，则重新创建。
在后续调用 render方法时，相同的模版（strings 值与第一次调用时是完全一致）是重用第一次的Template的，可以理解为编译时期就确定的一个常量值，而变化的只有 value 数组</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">declare</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Template</span> </span>&#123;
    <span class="hljs-keyword">readonly</span> parts: TemplatePart[];
    <span class="hljs-keyword">readonly</span> element: HTMLTemplateElement;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TemplatePart = &#123;
  <span class="hljs-keyword">readonly</span> <span class="hljs-keyword">type</span>: <span class="hljs-string">'node'</span>; index: <span class="hljs-built_in">number</span>;
&#125; | &#123;
  <span class="hljs-keyword">readonly</span> <span class="hljs-keyword">type</span>: <span class="hljs-string">'attribute'</span>;
  index: <span class="hljs-built_in">number</span>;
  <span class="hljs-keyword">readonly</span> name: <span class="hljs-built_in">string</span>;
  <span class="hljs-keyword">readonly</span> strings: ReadonlyArray<<span class="hljs-built_in">string</span>>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<p>先用TemplateResult的模版（string）找有没有现成的模版，如果有，直接复用</p>
</li>
<li>
<p>如果没有，则检查keyString的模版中有没有 模版.join markerKey的引用（markKey means lit-7227407027270176）</p>
</li>
<li>
<p>如果还是没有，则创建一个Template实例，并且将Template 使用模版 和 keyString缓存起来</p>
</li>
</ol>
<p>缓存流程不展开讲解，如果有兴趣自己看一下</p>
<p><code>Template</code> 对象中分为 parts 和 element，element就是TemplateResult转化出来的 <code><template></code> ，parts部分，是在遍历<code><template></code>（dom walker）的时候生成的。处理流程简化理解</p>
<ul>
<li>
<p>如果是Node节点</p>
<ul>
<li>判断是否有attribute，且属性名有特殊标记，有的话，移除template上的属性，并往part push一个 <code>&#123;type: 'attribute', index, name, strings: statics&#125;</code> 的结构，index是当前的walker下标，name是属性名，strings是这个属性的插值前后字符</li>
</ul>
</li>
<li>
<p>如果是Comment节点</p>
<ul>
<li>
<p>如果comment的内容等同于marker -（这里可以和真正的comment区分开），然后往part中推入一个node节点 <code>&#123;type: 'node', index&#125;</code></p>
<ul>
<li>如果是第一个节点或者前面一个节点已经是一个part的标记了，会先在当前节点前添加一个空的comment节点，</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-htmlbars copyable" lang="htmlbars"><span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>$<span class="hljs-attr">lit</span>$=<span class="hljs-string">\</span>"</span></span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">lit-7227407027270176</span>&#125;&#125;</span><span class="xml"><span class="hljs-tag">\"></span><span class="hljs-comment"><!--</span></span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">lit-7227407027270176</span>&#125;&#125;</span><span class="xml"><span class="hljs-comment">--></span><span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-comment"><!--</span></span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">lit-7227407027270176</span>&#125;&#125;</span><span class="xml"><span class="hljs-comment">--></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>处理完成后</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">element</span>: template
    <span class="hljs-attr">parts</span>: [
        &#123;<span class="hljs-attr">type</span>: <span class="hljs-string">"attribute"</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"class"</span>, <span class="hljs-attr">strings</span>: [<span class="hljs-string">""</span>, <span class="hljs-string">""</span>]&#125;,
        &#123;<span class="hljs-attr">type</span>: <span class="hljs-string">"node"</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">3</span>&#125;,
        &#123;<span class="hljs-attr">type</span>: <span class="hljs-string">"node"</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">7</span>&#125;,
    ]
&#125;
<span class="hljs-comment">// templatee也会会简化成如下结构</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span><span class="hljs-comment"><!----></span><span class="hljs-comment"><!----></span><span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-comment"><!----></span><span class="hljs-comment"><!----></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以理解 <code>Template</code> 是一个已经成型的 <code>DOM</code> 模版，他拥有完整的 <code>DOM</code> 和需要插值的位置定位，但他还没渲染到 <code>DOM</code> 上</p>
<p>接下来检查当前的 <code>Template</code> 是否已经创建了 <code>TemplateInstance</code> 实例，如果没有，实例化一个 <code>TemplateInstance</code></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TemplateInstance</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">readonly</span> __parts;
    <span class="hljs-keyword">readonly</span> processor: TemplateProcessor;
    <span class="hljs-keyword">readonly</span> options: RenderOptions;
    <span class="hljs-keyword">readonly</span> template: Template;
    <span class="hljs-title">constructor</span>(<span class="hljs-params">template: Template, processor: TemplateProcessor, options: RenderOptions</span>);
    update(values: <span class="hljs-keyword">readonly</span> unknown[]): <span class="hljs-built_in">void</span>;
    _clone(): DocumentFragment;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>TemplateInstance 会通过<code><template></code>创建 <code>fragment</code> ; 然后遍历 <code>parts</code> ，根据 <code>TemplatePart</code> 字面量的类型，分别创建 NodePart 和 AttributePart 实例。</p>
<p>最终调用 <code>TemplateInstance</code> 实例的 <code>update</code> 方法，这个方法会逐个调用 <code>Part</code> 实例的 <code>setValue</code> （真实的值）和 <code>commit</code> （渲染方法）方法，至此，循环回了render的最开始的方法调用，剩下的就是递归调用，直到找到原始的值类型的那一层，渲染到Fragment上。</p>
<ul>
<li>
<p><code>__commitText</code> ：直接修改文本节点的文本</p>
</li>
<li>
<p><code>__commitNode</code> ：清空父亲节点中的startNode到endNode（最开始提到的那两个comment占位），然后把node添加进去。</p>
</li>
</ul>
<p>当递归回到最顶层后， <code>commitNode</code> 拿到的就是完整的 <code>fragment</code> ，塞到容器中就可以了。</p>
<h6 data-id="heading-12">核心流程</h6>
<p>至此，第一次的渲染完成，大致流程如下</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b6574d17e714607bf9bfea7ea6e4f35~tplv-k3u1fbpfcp-watermark.image" alt="image-7-1624330788460.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可能听起来有些绕，我们可以暂时忽略 <code>Template</code> ，它是一个中间状态</p>
<p><code>TemplateResult</code> 是类似 <code>JSX</code> 的一种更轻量的对于模版的字面量描述，是一个模型
<code>TemplateInstance</code> 可以理解成一个小的 <code>MVC</code> 框架的嵌套</p>
<ul>
<li>
<p>DOM（fragment） 是应用的外层框架，是不变的 View 部分</p>
</li>
<li>
<p><code>TemplateResult</code> 中的成员 <code>value</code> 是 Model</p>
</li>
<li>
<p>Controller（Part）中连接了 View 和 Model。提供了更新数据的方法（setValue）和渲染到视图的方法（Commit）</p>
</li>
</ul>
<h5 data-id="heading-13">更新渲染</h5>
<p>可以类比SQL执行过程中的库缓存，如果SQL结构一致就复用已有的模型
逐层比较检查所有的缓存是否命中（对比类型 和 模版 - strings结构）</p>
<ol>
<li>
<p>如果命中的话就使用已有模版，找到 <code>TemplateInstance</code> 的 <code>Part</code> ，把 <code>templateResult</code> 的 <code>value</code> 更新给 <code>Part</code></p>
</li>
<li>
<p>如果没有命中的话，就走第一次渲染的流程</p>
</li>
</ol>
<h4 data-id="heading-14">效率</h4>
<ul>
<li>
<p><code>带标签的模版字符串</code> 执行相比 <code>JSX</code> 会更加高效。 <code>JSX</code> 的每次 render 都需要完整的构造一个虚拟DOM，而 <code>lit-html</code> ，则只是重新构建一个十分轻量的 TemplateResult 对象，变化的只有 value 集合。</p>
</li>
<li>
<p>从 TemplateResult 到 < template> 的过程，是直接从 TemplateResult 构造 html ，然后使用 template.innerHTML 完成解析的。这个过程完全使用浏览器自己的语法解析器来完成的。由于使用了 template 技术，这个DOM是一个Fragement，并不是真实DOM的一部分，内存占用小</p>
</li>
<li>
<p>实际渲染的DOM生成，是从 template.importNode 来完成DOM的复制。而不是像React一样逐个Dom节点的创建。对于较大的DOM，效率十分可观</p>
</li>
<li>
<p>在增量更新的过程中，Lit 和 React 相类似，都是按照相同层次的节点重用的方式，React通过 <code>diff(VDOM, DOM)</code> 来实现增量更新，而LitHtml并没有使用diff算法，而是基于相同模板的渲染，只需要对动态部分进行更新即可。没有diff算法会更加的轻</p>
</li>
</ul>
<blockquote>
<p>有关注过尤大状态的同学应该在Vue 3 发布的时候，可能会看到过一个东西横空出世，vue-lit，vue-lit就是基于lit-html模版引擎和@vue/reactivity的数据绑定做的一款面向未来的玩具。
Lit 自身也提供了一个数据绑定，数据响应式的包来支撑整个框架</p>
</blockquote>
<h3 data-id="heading-15">Lit-element</h3>
<p>OK，模版语法有了，剩下的就是如何把状态变化响应式的应用到模版里了。</p>
<h4 data-id="heading-16">如何使用</h4>
<p>这部分实际上不复杂，有过Vue开发经历的同学一定都清楚Vue是如何将数据和视图绑定起来。 <code>Lit-element</code> 也是如此
在Lit中，你需要这样声明一个组件</p>
<pre><code class="hljs language-scala copyable" lang="scala"><span class="hljs-meta">@customElement</span>(<span class="hljs-symbol">'simple</span>-greeting')
export <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SimpleGreeting</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">LitElement</span> </span>&#123; <span class="hljs-comment">/* ..*/</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>customElement 实际上是 customElement.defined 的语法糖，而 <code>LitElement</code> 是 <code>Lit</code> 提供的一个基类，其中就处理了数据的响应式处理（实际上 <code>LitElement</code> 还继承了 <code>UpdateElement</code> ，由 <code>UpdateElement</code> 做响应式的处理）。</p>
<h4 data-id="heading-17">Reactivity Property</h4>
<p>我们先看看，Lit的文档中要求怎么定义 <code>reactivity property</code></p>
<pre><code class="hljs language-scala copyable" lang="scala"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyElement</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">LitElement</span> </span>&#123;
  <span class="hljs-meta">@property</span>()
  name: string;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们会会发现，如果需要响应式属性的话，需要使用 property 这个装饰器来装饰属性，property 这个装饰器的逻辑为，调用所在类的静态方法 <code>createProperty</code> 往类的静态成员 <code>_classProperties</code> 中注册这个属性，同时，给这个属性添加 getter 和 setter，到这里，类准备工作就做好了。</p>
<ul>
<li>
<p>getter：直接取</p>
</li>
<li>
<p>setter：更新后触发更新</p>
</li>
</ul>
<p>每次在组件内部修改 <code>reactive property</code> 的时候，属性更新完成后会重新调用 <code>lit-html</code> 的 render 方法渲染到UI上。</p>
<p>这个和 state 的概念十分的相似，那么 <code>lit-element</code> 又是如何处理外部传输属性（props）的变化呢？
这里我们需要应用到前面提到的 <code>Web-Component</code> 的生命周期<code>get observedAttributes</code> 和 <code>attributeChangedCallback</code> 。每次当传递给 component 的属性发生变化的时候，这两个周期就会触发，只需要查询是否在 <code>_classProperties</code> 中，并主动更新 <code>reactive property</code> 即可。
除此之外，property 装饰器还可以接受一个 options 配置一些属性来进行适配</p>
<ol>
<li>
<p>attribute - 定义这个成员变量是否和元素属性绑定</p>
</li>
<li>
<p>converter - 定义转化逻辑，从元素属性（都是string）到真实属性</p>
</li>
<li>
<p>hasChanged - 判断属性是否发生变化</p>
</li>
<li>
<p>type - 在没有定义converter时使用，转化元素类型</p>
</li>
<li>
<p>state - 如果定义了state的话，象征这个成员变量是一个内部状态，是私有的，新版的 <code>Lit</code> 提供了一个单独的装饰器@state 来替代这个属性</p>
</li>
</ol>
<p><code>Lit</code> 剩下的诸如装饰器，事件绑定之类的就不再展开细说了，有兴趣的同学可以去阅读下源码，整体上比 React 易读性高的多（Doge）。至此，一个完整的可用的面向未来的前端框架就完成了。</p>
<h2 data-id="heading-18">小结</h2>
<p><code>Lit</code> 因为兼容性问题现在还不能应用到实际的业务场景中，但是确实是一个值得关注和学习的框架。其中的一些设计思想和理念，跳出了 React 限制的框架，给出了前端框架的另一种可能的解决方案。在框架领域上一家独大不是什么好事，有更多的奇思妙想和拥抱未来才能让前端的发展更加广阔。</p>
<p>还有个不能实际场景应用的问题，Lit 还在快速的迭代中，每次都是很大的 Breaking changes。比如刚才提到的UpdateElement又被拆成单独的包了。。。。</p></div>  
</div>
            