
---
title: '【第一批吃螃蟹】试用 React 18 ！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d96a57a7220c4faa875fa07071214c3e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 02:26:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d96a57a7220c4faa875fa07071214c3e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>React 团队最近发布了 React 18 的 alpha 版本。这个版本主要是增强 React 应用程序的 <code>并发渲染</code> 能力，你可以在 React 18 中尝试体验以下几个新特性：</p>
<ul>
<li>新的 <code>ReactDOM.createRoot()</code> API（替换 <code>ReactDOM.render()</code>）</li>
<li>新的 <code>startTransition</code> API（用于非紧急状态更新）</li>
<li>渲染的自动批处理优化（主要解决异步回调中无法批处理的问题）</li>
<li>支持 <code>React.lazy</code> 的 全新 SSR 架构（支持 <code><Suspense></code> 组件）</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d96a57a7220c4faa875fa07071214c3e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这不，这个版本才刚刚发布社区里已经有很多小伙伴已经跃跃欲试了，我也迫不及待跟着社区的大佬们一起尝试了一下。感兴趣的小伙伴们可以一起跟着我的记录来试一下：</p>
<h2 data-id="heading-0">安装 React 18 Alpha</h2>
<p>想要在你的项目里试用 React 18 Alpha，可以尝试执行下面的命令：</p>
<pre><code class="copyable">npm install react@alpha react-dom@alpha
# or
yarn add react@alpha react-dom@alpha
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你是使用 <code>Create React App</code> 初始化的项目，你可能会遇到一个由于 <code>react-scripts</code> 引起的 <code>could not resolve dependency</code> 错误：</p>
<pre><code class="copyable">Could not resolve dependency:
peer react@">= 16" from react-scripts@4.0.3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以在安装的时候尝试加上 <code>--force</code> 来解决这个问题：</p>
<pre><code class="hljs language-npm copyable" lang="npm">npm install react@alpha react-dom@alpha --force
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">ReactDOM.createRoot()</h2>
<p>在 React 18 版本中，<code>ReactDOM.createRoot()</code> 替代了通常作为程序入口的  <code>ReactDOM.render()</code> 方法。</p>
<p>这个方法主要是防止  React 18 的不兼容更新导致你的应用程序崩溃。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>;
<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>);
<span class="hljs-comment">// Create a root.</span>
<span class="hljs-keyword">const</span> root = ReactDOM.createRoot(container);
<span class="hljs-comment">// Render the top component to the root.</span>
root.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>当你更新到 React 18 时，如果你还使用 redner 函数作为程序入口，控制台会打印一个错误日志来提醒你使用 createRoot() ，只有使用了这个方法后才能使用 React 18 新功能。</p>
</blockquote>
<h2 data-id="heading-2">渲染的自动批处理</h2>
<p>React 有一道经典面试题，<code>setState</code> 到底是同步的还是异步的，我面试的时候也会经常问，具体的我在两年前的一篇文章中有介绍过：</p>
<p><a href="https://mp.weixin.qq.com/s/vDJ_Txm4wi-cMVlX5xypLg" target="_blank" rel="nofollow noopener noreferrer">由实际问题探究setState的执行机制</a></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Example</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">val</span>: <span class="hljs-number">0</span>
    &#125;;
  &#125;
  
  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">val</span>: <span class="hljs-built_in">this</span>.state.val + <span class="hljs-number">1</span>&#125;);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.val);   
    <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">val</span>: <span class="hljs-built_in">this</span>.state.val + <span class="hljs-number">1</span>&#125;);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.val);   

    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">val</span>: <span class="hljs-built_in">this</span>.state.val + <span class="hljs-number">1</span>&#125;);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.val); 
      <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">val</span>: <span class="hljs-built_in">this</span>.state.val + <span class="hljs-number">1</span>&#125;;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.val);  
    &#125;, <span class="hljs-number">0</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如上面的代码，我们来考虑一下两种情况：</p>
<ul>
<li>假设 React 完全没有批处理机制，那么执行一个 setState 就会立即触发一次页面渲染，打印顺序应该是 1、2、3、4</li>
<li>假设 React 有一个完美的批处理机制，那么应该等整个函数执行完了之后再统一处理所有渲染，打印顺序应该是 0、0、0、0</li>
</ul>
<p>实际上，在 React 18 版本之前，上面代码的打印顺序是 0、0、2、3</p>
<p>出现这个问题的主要原因就是在 <code>React</code> 的事件函数和异步回调中的状态批处理机制不一样。在异步回调外面，能够将所有渲染合并成一次，异步回调里面，则不会合并，会渲染多次。</p>
<p>实际上，在大部分的场景下，我们都需要在调用一个接口或者做了一些其他事情之后，再去回调函数里更新状态，上面的批处理机制就会显得非常鸡肋。</p>
<p>现在，React 18 版本解决了这个问题，无论你是在 Promise、setTimeout、或者其他异步回调中更新状态，都会触发批处理，上面的代码真的就会一直打印 <code>0、0、0、0</code> 了！</p>
<blockquote>
<p>是不是很棒！React 帮我们消灭的一道面试题 😎。</p>
</blockquote>
<p>通常情况下，批处理是没什么问题的，但是有可能在某些特殊的需求（比如某个状态更改后要立刻从 DOM 中获取一些内容）下不太合适，我们可以使用 <code>ReactDOM.flushSync()</code> 退出批处理：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> &#123; flushSync &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>; <span class="hljs-comment">// Note: react-dom, not react</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
  flushSync(<span class="hljs-function">() =></span> &#123;
    setCounter(<span class="hljs-function"><span class="hljs-params">c</span> =></span> c + <span class="hljs-number">1</span>);
  &#125;);
  <span class="hljs-comment">// React has updated the DOM by now</span>
  flushSync(<span class="hljs-function">() =></span> &#123;
    setFlag(<span class="hljs-function"><span class="hljs-params">f</span> =></span> !f);
  &#125;);
  <span class="hljs-comment">// React has updated the DOM by now</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Ricky</code> 在这篇文章（<code>https://github.com/reactwg/react-18/discussions/21</code>） 详细介绍了 <code>Automatic batching</code> ，感兴趣可以一起到评论区讨论。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d74e97df01c4b6fbd5df14b111c5e2f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">SSR 下的懒加载支持</h2>
<p><code>React.lazy</code> 函数能让你像渲染常规组件一样处理动态引入组件。<code>React.lazy</code> 接受一个函数，这个函数需要动态调用 <code>import()</code>。它必须返回一个 <code>Promise</code>，该 <code>Promise</code> 需要 <code>resolve</code> 一个 <code>default export</code> 的 React 组件。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> MonacoEditor = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'react-monaco-editor'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>React.lazy</code> 必须要配合 <code><Suspense></code> 才能更好的使用，在 <code>Suspense</code> 组件中渲染 <code>lazy</code> 组件，可以使用在等待加载 <code>lazy</code> 组件时做优雅降级（比如渲染一些 <code>loading</code> 效果 ）。<code>fallback</code> 属性接受任何在组件加载过程中你想展示的 <code>React</code> 元素。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> OtherComponent = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./OtherComponent'</span>));

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyComponent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="hljs-comment">// Displays <Spinner> until OtherComponent loads</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">Spinner</span> /></span>&#125;>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">OtherComponent</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">React.Suspense</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>React 18</code> 以前， SSR 模式下是不支持使用 <code>Suspense</code> 组件的，而在 React 18 中服务端渲染的组件也支持使用 <code><Suspense></code> 了：如果你把组件包裹在了 <code><Suspense></code>
中，服务端首先会把 <code>fallback</code> 中的组件作为 HTML 流式传输，一旦主组件加载完成，React 会发送新的 <code>HTML</code> 来替换该组件。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Layout> 
  < Article /> 
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">Spinner</span> /></span>&#125;>
     <span class="hljs-tag"><<span class="hljs-name">Comments</span> /></span> 
  <span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span></span>
 </Layout>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如上面的代码，<code><Article></code> 组件首先会被渲染，<code><Comments></code> 组件将被 <code>fallback</code> 替换为 <code><Spinner></code> 。一旦 <code><Comments></code> 组件加载完成后，React 会才将其发送到浏览器，替换 <code><Spinner></code> 组件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0e346ee419a426fbc13c7d6e3ae10c8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>Dan Abramov</code> 在这篇文章（<code>https://github.com/reactwg/react-18/discussions/37</code>） 中详细介绍了这个机制，感兴趣可以到评论区一起讨论。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b3ddc4e234a48149e42c522e751e25c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">startTransition API</h2>
<p><code>startTransition</code> 是 React 18 新增加的一个 API，它可以让你区分 <code>非紧急</code> 的状态更新。</p>
<p>比如现在有这样一个场景：我们要去 <code>Input</code> 框输入一个值，然后下面需要同时给出通过我们输入后的值过滤出来的一些数据。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9620c879fc3f44caa976676360a4724d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为你每次需要动态渲染出过滤后的值，所以你可能会将输入的值存储在一个 <code>state</code> 中，你的代码可能是下面这样的：</p>
<pre><code class="hljs language-js copyable" lang="js">setInputValue (input) ; 
setSearchQuery (input) ;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先用户输入上去的值肯定是需要立刻渲染出来的，但是过滤出来的联想数据可能不需要那么快的渲染，如果我们不做任何额外的处理，在 React 18 之前，所有更新都会立刻被渲染，如果你的原始数据非常多，那么每次输入新的值后你需要进行的计算量（根据输入的值过滤出符合条件的数据）就非常大，所以每次用户输入后可能会有卡顿现象。</p>
<p>所以，在以前我们可能会自己去加一些防抖这样的操作去人为的延迟过滤数据的计算和渲染。</p>
<p>新的 startTransition API 可以让我们把数据标记成 <code>transitions</code> 状态。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; startTransition &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;


<span class="hljs-comment">// Urgent: Show what was typed</span>
setInputValue(input);

<span class="hljs-comment">// Mark any state updates inside as transitions</span>
startTransition(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// Transition: Show the results</span>
  setSearchQuery(input);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有在 <code>startTransition</code> 回调中的更新都会被认为是 <code>非紧急处理</code>，如果出现更紧急的更新（比如用户又输入了新的值），则上面的更新都会被中断，直到没有其他紧急操作之后才会去继续执行更新。</p>
<blockquote>
<p>怎么样，是不是比我们人工实现一个防抖更优雅 😇</p>
</blockquote>
<p>同时，React 还给我们提供了一个带有 <code>isPending</code> 过渡标志的 <code>Hook</code>：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span>  &#123;  useTransition  &#125;  <span class="hljs-keyword">from</span>  <span class="hljs-string">'react'</span> ; 

<span class="hljs-keyword">const</span>  [ isPending ,  startTransition ]  =  useTransition ( ) ;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以使用它和一些 <code>loading</code> 动画结合使用：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">&#123; isPending  &&  < Spinner  / > &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Ricky</code> 在这篇文章（<code>https://github.com/reactwg/react-18/discussions/41</code>） 详细介绍了 <code>startTransition</code> ，感兴趣可以一起到评论区讨论。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51f69b52bfc046688075561e31a55ec4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">React 18 发布计划</h2>
<p>React 18 官方介绍（<code>https://github.com/reactwg/react-18/discussions/4</code>）中提到的其他两个 API <code>useDeferredValue</code>、<code><SuspenseList></code> 还没 <code>released</code> ，我们下次再用，下面是 React 18 的发布时间表：</p>
<ul>
<li><code>React 18 Alpha</code> 版本：现在就能用</li>
<li>公开的 Beta 版：至少在 Alpha 版本后的几个月</li>
<li>RC 版本：至少在 Beta 版发布后的几周</li>
<li>正式版：至少在 RC 版本发布之后的几周</li>
</ul>
<h2 data-id="heading-6">参考</h2>
<ul>
<li><a href="https://github.com/reactwg/react-18/discussions/4" target="_blank" rel="nofollow noopener noreferrer">github.com/reactwg/rea…</a></li>
<li><a href="https://github.com/reactwg/react-18/discussions/41" target="_blank" rel="nofollow noopener noreferrer">github.com/reactwg/rea…</a></li>
<li><a href="https://github.com/reactwg/react-18/discussions/37" target="_blank" rel="nofollow noopener noreferrer">github.com/reactwg/rea…</a></li>
<li><a href="https://blog.bitsrc.io/trying-out-react-18-alpha-release-bad9aed12bee" target="_blank" rel="nofollow noopener noreferrer">blog.bitsrc.io/trying-out-…</a></li>
</ul>
<h2 data-id="heading-7">最后</h2>
<p>文中如有错误，欢迎在评论区指正，如果这篇文章帮助到了你，欢迎点赞和关注。</p>
<p>本文首发在我的个人公众号：【code秘密花园】：<a href="https://mp.weixin.qq.com/s/y8xcMa8ocvPooHVLTa_UAQ" target="_blank" rel="nofollow noopener noreferrer">试用 React 18 ！</a> ，欢迎关注。</p>
<p>抖音前端正急缺人才，如果你想加入我们，欢迎加我微信和我联系。另外如果你想加入前端、面试、理财等交流群，或者你有任何其他事情也可以添加我的个人微信 <code>ConardLi</code> 一起交流。</p></div>  
</div>
            