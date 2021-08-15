
---
title: 'Web Compoent 系列(2)—自己动手实现一个 Web Component'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8521'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 04:44:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=8521'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h3 data-id="heading-0">web component</h3>
<p>聊一聊什么是 web component 以及 web component 有什么优势，以及如何整合现有 web 技术来实现一个 web component</p>
<h4 data-id="heading-1">什么是 web component</h4>
<p>所谓组件(component)是和平台无关的，也就是组件不受平台所限制。
组件设计初衷是将组件的代码封装成一个漂亮的、可重复使用的包，来实现足够的可用操作性。
也就是我们设计组件最大可能满足不同 team 对组件需求，为不同 team 提供一个同一标准组件供调用</p>
<h4 data-id="heading-2">为什么是 web component</h4>
<p>为什么是 web component ,也就什么是 web component 的优点。</p>
<ul>
<li><strong>最大化互用性(interoperability)</strong>， 通过 web component 可以对组件进行封装，提供组件行为，对于一个拥有多个产品公司，通过 web component 让用户体验在不同产品上保持一致性，例如登录流程，这样不但节省了团队开发成本，从用户方面来看，因为一些流程或者操作一致性，也节省了用户学习不同产品的成本，从而提供良好的用户体验。</li>
<li><strong>更好的性能(better performance)</strong>: 这一点有更容易理解，web component 因为是原生浏览器支持，用 js 直接编写，也就是大力鼓励，浏览器全力支持的技术，相对于框架如 vue、react 和 angular 中的 component 自然有自己的在性能上的优势。因为框架中 component 依赖框架，所以 bundle 文件时需要引入对 component 支持文件所以 bundle 后 js 体积要远远大于原生 js 支持 web component 的体积。</li>
<li>封装性(encapsulation): 有关封装这一天在之前 shadow DOM 已经谈了很多这里不想多谈</li>
<li><strong>样式化(styling)</strong>: 在今天丰富多彩世界里少不了个性突出的应用， web 应用也和好 app 也好大家，大家都在最求用户体验，当然 app 也要自己风格，自己不同于其他 app 的自己特点，这些不同当然也体现在样式上、风格上，鲜明的主题良好设计势必给用户一个深刻印象。所以今天风格也变得非常重要，</li>
</ul>
<h3 data-id="heading-3">基于以下技术得以实现 web component</h3>
<h4 data-id="heading-4">html 模板(HTML Template)</h4>
<p>HTML template(模板)就是可以声明式去定义一个段标签，浏览器可以将其解析为 HTML
<code><template><template></code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"card-tmpl"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
            <span class="hljs-selector-id">#card</span>&#123;
                <span class="hljs-attribute">flex-direction</span>: row;
                <span class="hljs-attribute">background-color</span>: lightblue;
            &#125;
            <span class="hljs-selector-id">#title</span>&#123;
                <span class="hljs-attribute">align-items</span>: center;
                justify-self: center;
                <span class="hljs-attribute">color</span>: darkslateblue;
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"card"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"title"</span>></span>machine learning<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"content"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 template 标签内容不会在浏览器加载页面时被渲染出来，不过可以通过<code>var template = document.getElementById('card-tmpl')</code>获取 template 标签，在 template DOM 元素有一个属性 <code>content</code>,通过该属性可以获取到<code>template</code> 标签内的内容，然后可以将这个 DOM 元素 <code>const shadowRoot = this.attachShadow(&#123;mode: 'open'&#125;).appendChild(template.cloneNode(true));</code> 添加到 shadowRoot 下作为作为 shadow DOM 结点。</p>
<h4 data-id="heading-5">custom element</h4>
<p>我们自己定义一个 html 标签，如何创建一个自定义元素，首先创建一个 class 需要让该类继承 <code>HTMLElement</code> 然后就可以获取到一下 DOM 生命周期回调函数，在自定义元素添加到 DOM 或者从 DOM 移除时进行一个相应的处理工作。</p>
<ul>
<li>connectedCallback：当 custom element首次被插入文档DOM时的回调函数。</li>
<li>disconnectedCallback：当 custom element从文档DOM中删除时的回调函数</li>
<li>adoptedCallback：当 custom element被移动到新的文档时的回调函数</li>
<li>attributeChangedCallback: 当 custom element增加、删除、修改自身属性时的回调被调用</li>
</ul>
<p>而且需要自定义元素的构造函数调用一下其父类构造方法<code>super()</code>, 有时候我们需要在元素监听一下元素上某一个自定义属性，</p>
<pre><code class="copyable"><my-counter style="--background-bg-color: lightblue; --btn-width:600px;" id="counter" count="10"></my-counter>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要监听 <code>count</code> 属性的变化，我们就需要在自定义元素中定义以下静态方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">static</span> <span class="hljs-keyword">get</span> <span class="hljs-title">observedAttributes</span>()&#123;
        <span class="hljs-keyword">return</span> [<span class="hljs-string">"count"</span>]; <span class="hljs-comment">// 返回</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，如果需要在元素属性变化后，触发 attributeChangedCallback()回调函数，必须监听这个属性。这可以通过定义observedAttributes() get函数来实现，observedAttributes()函数体内包含一个 return语句，返回一个数组，包含了需要监听的属性名称。还需要实现一下有关 count 这个属性 set 和 get 方法。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">get</span> <span class="hljs-title">count</span>()&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getAttribute(<span class="hljs-string">"count"</span>);
    &#125;

    <span class="hljs-keyword">set</span> <span class="hljs-title">count</span>(<span class="hljs-params">val</span>)&#123;
        <span class="hljs-built_in">this</span>.setAttribute(<span class="hljs-string">'count'</span>,val)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">shadow DOM</h4>
<p><a href="https://juejin.cn/post/6993238862805860366" target="_blank" title="https://juejin.cn/post/6993238862805860366">Web Compoent 系列—shadow DOM(1)</a></p>
<h4 data-id="heading-7">ES6 module</h4>
<p>有关模块化，在 ES6 上也十分简单</p>
<pre><code class="hljs language-js copyable" lang="js"><script type=<span class="hljs-string">"module"</span> src=<span class="hljs-string">"counter.js"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果几年前你和人提起 web component，大家对这个技术可能还会抱有怀疑态度，因为大多数浏览器版本对这个新兴 API 支持还不算好
为此需要做大量额外工作以让你定义 web component every where，不过我们再看今天，几乎所有的浏览器都提供对 web component 良好的支持。</p>
<h3 data-id="heading-8">样式化(Styling)</h3>
<h4 data-id="heading-9">通过 CSS 中 var 将样式定义交个使用者</h4>
<p>我们希望将一些样式的修改权交个使用该组件的用户，这个可以通过<code>var</code>来实现，然后在自定标签的<code>style</code>属性来对这些变量进行赋值从而控制。</p>
<pre><code class="hljs language-html copyable" lang="html">#btn&#123;
  outline:None;
  color:white;
  max-width:var(--btn-width,200px);
  background-color:var(--background-bg-color,green);
  border: 0px;
  padding:20px;
  font-size:1.2em;
  border-radius:10px;
text-align: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">my-counter</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"--background-bg-color: lightblue; --btn-width:600px;"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"counter"</span> <span class="hljs-attr">count</span>=<span class="hljs-string">"10"</span>></span><span class="hljs-tag"></<span class="hljs-name">my-counter</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">通过 CSS 中 part 将 shadow DOM 样式暴露给外部</h4>
<p>引入 shadow DOM 就是为了让我们组件内部 html 和 CSS 有自己独立空间，外面的定义样式不会影响到自定义元素内部，这里</p>
<pre><code class="hljs language-html copyable" lang="html">h1&#123;
color: dodgerblue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不会影响到 shadow DOM 下面 h1 元素的样式 <code><h1>计数器</h1></code> 如果想要在外面影响 shadow DOM 元素样式可以通过 CSS part 方式来解决问题，也就是<code><h1 part="title">计数器</h1></code> 给 shadow DOM 中 h1 标签添加<code>part="title"</code> 然后就可以外部样式表通过<code>my-counter::part(title)</code></p>
<pre><code class="hljs language-js copyable" lang="js">my-counter::<span class="hljs-function"><span class="hljs-title">part</span>(<span class="hljs-params">title</span>)</span>&#123;
<span class="hljs-attr">color</span>: dodgerblue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        
        <span class="hljs-built_in">this</span>.shadowRoot.innerHTML = <span class="hljs-string">`
        <style>
        *&#123;
            box-sizing: border-box;
            margin:0;
            padding:0;
            box-sizing: border-box;
        &#125;
        .container&#123;
            display:flex;
            flex-direction:column;
            align-items: center;
            justify-content: center;
        &#125;
        
        #btn&#123;
            outline:None;
            color:white;
            max-width:var(--btn-width,200px);
            background-color:var(--background-bg-color,green);
            border: 0px;
            padding:20px;
            font-size:1.2em;
            border-radius:10px;
            text-align: center;
        &#125;
        span&#123;
            font-size:2.75em;
            font-weight:bold;
        &#125;
        </style>
        <div class="container">
        <h1 part="title">计数器</h1>
        <span><span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.count&#125;</span></span>
        <button id="btn">Increment</button> 
        </div>
        `</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">完整代码</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>web component<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        *&#123;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
        &#125;
        <span class="hljs-comment">/* my-counter&#123;
            width: 100vw;
        &#125; */</span>
        my-counter<span class="hljs-selector-pseudo">::part</span>(title)&#123;
            <span class="hljs-attribute">color</span>: dodgerblue;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>template<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">my-counter</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"--background-bg-color: lightblue; --btn-width:600px;"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"counter"</span> <span class="hljs-attr">count</span>=<span class="hljs-string">"10"</span>></span><span class="hljs-tag"></<span class="hljs-name">my-counter</span>></span>
    <span class="hljs-comment"><!-- <button onclick="update"></button> --></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"counter.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span>&#123;

            <span class="hljs-keyword">let</span> counter = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#counter"</span>)
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// custom element</span>
<span class="hljs-comment">// 定义一个 class 并且这个类继承 HTMLElment</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyCounterElement</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HTMLElement</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 调用父类构造方法</span>
        <span class="hljs-built_in">super</span>();
        <span class="hljs-comment">//添加 shadow DOM， element.add shadow dom shadowRoot</span>
        <span class="hljs-comment">//形成一个作用域，样式和事件误会影响作用域以外，从而形成封闭</span>
        <span class="hljs-built_in">this</span>.attachShadow(&#123;<span class="hljs-attr">mode</span>:<span class="hljs-string">'open'</span>&#125;)
        <span class="hljs-comment">// this.shadowRoot</span>
        <span class="hljs-comment">// this.template = document.querySelector("#counter");</span>
        <span class="hljs-comment">// this.template.content;</span>
        <span class="hljs-comment">// slot </span>

    &#125;
    <span class="hljs-keyword">get</span> <span class="hljs-title">count</span>()&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getAttribute(<span class="hljs-string">"count"</span>);
    &#125;

    <span class="hljs-keyword">set</span> <span class="hljs-title">count</span>(<span class="hljs-params">val</span>)&#123;
        <span class="hljs-built_in">this</span>.setAttribute(<span class="hljs-string">'count'</span>,val)
    &#125;

    <span class="hljs-comment">// 静态方法，watch count</span>
    <span class="hljs-comment">/**
     * 需要注意的是，如果需要在元素属性变化后，触发 attributeChangedCallback()回调函数，
     * 你必须监听这个属性。这可以通过定义observedAttributes() get函数来实现，
     * observedAttributes()函数体内包含一个 return语句，
     * 返回一个数组，包含了需要监听的属性名称
     */</span>
    <span class="hljs-keyword">static</span> <span class="hljs-keyword">get</span> <span class="hljs-title">observedAttributes</span>()&#123;
        <span class="hljs-keyword">return</span> [<span class="hljs-string">"count"</span>]; <span class="hljs-comment">// 返回</span>
    &#125;

    <span class="hljs-function"><span class="hljs-title">bindBtn</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> btn = <span class="hljs-built_in">this</span>.shadowRoot.querySelector(<span class="hljs-string">"#btn"</span>);
        btn.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-built_in">this</span>.increment.bind(<span class="hljs-built_in">this</span>));
    &#125;

    <span class="hljs-function"><span class="hljs-title">attributeChangedCallback</span>(<span class="hljs-params">prop, oldVal, newOld</span>)</span>&#123;
        <span class="hljs-keyword">if</span> (prop === <span class="hljs-string">"count"</span>)&#123;
            <span class="hljs-built_in">this</span>.render();
            <span class="hljs-built_in">this</span>.bindBtn();
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.count++;
    &#125;
    <span class="hljs-comment">//当 custom element首次被插入文档DOM时，被调用。</span>
    <span class="hljs-function"><span class="hljs-title">connectedCallback</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 渲染</span>
        <span class="hljs-built_in">this</span>.render();
        <span class="hljs-comment">//绑定事件</span>
        <span class="hljs-built_in">this</span>.bindBtn();
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        
        <span class="hljs-built_in">this</span>.shadowRoot.innerHTML = <span class="hljs-string">`
        <style>
        *&#123;
            box-sizing: border-box;
            margin:0;
            padding:0;
            box-sizing: border-box;
        &#125;
        .container&#123;
            display:flex;
            flex-direction:column;
            align-items: center;
            justify-content: center;
        &#125;
        
        #btn&#123;
            outline:None;
            color:white;
            max-width:var(--btn-width,200px);
            background-color:var(--background-bg-color,green);
            border: 0px;
            padding:20px;
            font-size:1.2em;
            border-radius:10px;
            text-align: center;
        &#125;
        span&#123;
            font-size:2.75em;
            font-weight:bold;
        &#125;
        </style>
        <div class="container">
        <h1 part="title">计数器</h1>
        <span><span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.count&#125;</span></span>
        <button id="btn">Increment</button> 
        </div>
        `</span>
    &#125;
    
&#125;

customElements.define(<span class="hljs-string">'my-counter'</span>,MyCounterElement);

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            