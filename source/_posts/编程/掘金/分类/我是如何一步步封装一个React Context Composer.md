
---
title: '我是如何一步步封装一个React Context Composer'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5174'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 06:41:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=5174'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">动机</h2>
<p>React的状态管理方案有很多，比如<code>Redux</code>、<code>Mobx</code>、<code>Recoil</code>等，目前我只体验过<code>Redux</code>，觉得还是比较笨重一点。因为平时写Hooks比较多，所以我比较倾向于使用<code>Context Provider</code>配合<code>useContext</code>这个hook来做，这样也易于状态的拆分与组合。这里，我们不讨论各家状态管理方案的优劣，将目光聚焦于在使用<code>Context</code>时遇到的一个<strong>多层嵌套</strong>的问题。</p>
<p>下图，是我最近在写的一个<code>taro + react hooks + ts</code>项目抽离出来的一些代码。我对一些全局状态进行了拆分（拆分的目的是为了减少不必要的重新渲染），然后再把它们嵌套起来。这种写法让我回想起了曾经被回调地狱支配的感觉，很难受。因此，我想到了自己去封一个<strong>高阶组件</strong>，从写法上把结构“扁平化”。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><LoadingContext.Provider value=&#123;&#123; loading, setLoading &#125;&#125;>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">UserDataContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">name:</span> "<span class="hljs-attr">ascodelife</span>", <span class="hljs-attr">age:</span> <span class="hljs-attr">25</span> &#125;&#125;></span>
    <span class="hljs-tag"><<span class="hljs-name">ThemeContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;</span>"<span class="hljs-attr">light</span>"&#125;></span>
    &#123;/* ....more Providers as long as you want */&#125;
    <span class="hljs-tag"></<span class="hljs-name">ThemeContext.Provider</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">UserDataContext.Provider</span>></span></span>
</LoadingContext.Provider>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">最易得的方案</h2>
<p>这里，我很快的就写出了第一种方案，借助<code>reduce</code>去完成<code>Provider</code>的嵌套。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// ContextComposer.tsx</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">type</span> IContextComposerProps = &#123;
  <span class="hljs-attr">contexts</span>: &#123; <span class="hljs-attr">context</span>: React.Context<<span class="hljs-built_in">any</span>>; value: <span class="hljs-built_in">any</span> &#125;[];
&#125;;

<span class="hljs-keyword">const</span> ContextComposer: React.FC<IContextComposerProps> = <span class="hljs-function">(<span class="hljs-params">&#123; contexts, children &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      &#123;contexts.reduce((child, parent) => &#123;
        const &#123; context, value &#125; = parent;
        return <span class="hljs-tag"><<span class="hljs-name">context.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;value&#125;</span>></span>&#123;child&#125;<span class="hljs-tag"></<span class="hljs-name">context.Provider</span>></span>;
      &#125;, children)&#125;
    <span class="hljs-tag"></></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> ContextComposer;


<span class="hljs-comment">// App.tsx</span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ContextComposer</span>
  <span class="hljs-attr">contexts</span>=<span class="hljs-string">&#123;[</span>
    &#123; <span class="hljs-attr">context:</span> <span class="hljs-attr">ThemeContext</span>, <span class="hljs-attr">value:</span> "<span class="hljs-attr">light</span>" &#125;,
    &#123; <span class="hljs-attr">context:</span> <span class="hljs-attr">UserDataContext</span>, <span class="hljs-attr">value:</span> &#123; <span class="hljs-attr">name:</span> "<span class="hljs-attr">ascodelife</span>", <span class="hljs-attr">age:</span> <span class="hljs-attr">25</span> &#125; &#125;,
    &#123; <span class="hljs-attr">context:</span> <span class="hljs-attr">LoadingContext</span>, <span class="hljs-attr">value:</span> &#123; <span class="hljs-attr">loading</span>, <span class="hljs-attr">setLoading</span> &#125; &#125;,
  ]&#125;></span>
    &#123; children &#125;
<span class="hljs-tag"></<span class="hljs-name">ContextComposer</span>></span></span>


<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际体验后发现，虽然说能用是能用，但是开发体验差那么一点。它的问题在于，组件入参时传的<code>value</code>是<code>any</code>类型，这就意味着放弃了ts的静态类型检查。在传参时，由于不会对<code>value</code>做静态类型检查，敲起代码来不仅不会有任何代码提示，也有可能造成一些比较低级的运行时错误。差评！🤢</p>
<h2 data-id="heading-2">基于React.cloneElement()的改造方案</h2>
<p>为了改造上面的这种方案，我翻到了一个比较冷门但好用的函数—— <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh-hans.reactjs.org%2Fdocs%2Freact-api.html%23cloneelement" target="_blank" rel="nofollow noopener noreferrer" title="https://zh-hans.reactjs.org/docs/react-api.html#cloneelement" ref="nofollow noopener noreferrer">React.cloneElement()</a>。这个函数没有很多需要值得注意的点，主要看一眼它的三个入参，第一个是<code>parent element</code>，第二个是<code>parent props</code>，第三个是剩余参数<code>...children</code>，除第一个参数外，其他都是可选值。</p>
<p>举个例子🌰：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 调用函数 --></span>
React.cloneElement(<span class="hljs-tag"><<span class="hljs-name">div</span>/></span>,&#123;&#125;,<span class="hljs-tag"><<span class="hljs-name">span</span>/></span>);

<span class="hljs-comment"><!-- 相当于创建了这样一个结构 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么下面开始改造，<code>reduce</code>的架子不动，改一下入参的类型和<code>reduce</code>的回调。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// ContextComposer.tsx</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">type</span> IContextComposerProps = &#123;
  <span class="hljs-attr">contexts</span>: React.ReactElement[];
&#125;;

<span class="hljs-keyword">const</span> ContextComposer: React.FC<IContextComposerProps> = <span class="hljs-function">(<span class="hljs-params">&#123; contexts, children &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      &#123;contexts.reduce((child, parent) => &#123;
        return React.cloneElement(parent,&#123;&#125;,child);
      &#125;, children)&#125;
    <span class="hljs-tag"></></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> ContextComposer;



<span class="hljs-comment">// App.tsx</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ContextComposer</span>
  <span class="hljs-attr">contexts</span>=<span class="hljs-string">&#123;[</span>
      <<span class="hljs-attr">ThemeContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;</span>"<span class="hljs-attr">light</span>"&#125; /></span>,
      <span class="hljs-tag"><<span class="hljs-name">UserDataContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">name:</span> "<span class="hljs-attr">ascodelife</span>", <span class="hljs-attr">age:</span> <span class="hljs-attr">25</span> &#125;&#125; /></span>,
      <span class="hljs-tag"><<span class="hljs-name">LoadingContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">loading</span>, <span class="hljs-attr">setLoading</span> &#125;&#125; /></span>,
  ]&#125;>
    &#123; children &#125;
<span class="hljs-tag"></<span class="hljs-name">ContextComposer</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过改造后，我们在传参时就好像是真的在创建一个组件（当然实际上也创建了组件，只是这个组件本身没有被渲染到虚拟Dom上，实际渲染上去的是被克隆后的副本）。同时，我们刚才关注的<code>value</code>的静态类型检查问题也得到了解决。<br>
<strong>📣tips</strong>: <code>React.cloneElement(parent,&#123;&#125;,child)</code>等价于<code>React.cloneElement(parent,&#123;children:child&#125;)</code>，你知道为什么吗？</p>
<h2 data-id="heading-3">相关资源</h2>
<p>源码已经同步到了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fascodelife%2Freact-context-provider-composer" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ascodelife/react-context-provider-composer" ref="nofollow noopener noreferrer">github</a>。</p>
<p>同时也打包到了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40ascodelife%2Freact-context-provider-composer" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/@ascodelife/react-context-provider-composer" ref="nofollow noopener noreferrer">npm仓库</a>中，欢迎体验。🤞</p></div>  
</div>
            