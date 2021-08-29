
---
title: 'React如何捕捉错误'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b04f8b3be4054ee189105297ab3da139~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 17:31:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b04f8b3be4054ee189105297ab3da139~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第29天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">背景</h2>
<p>错误在我们日常编写代码是非常常见的</p>
<p>举个例子，在<code>react</code>项目中去编写组件内<code>JavaScript</code>代码错误会导致 <code>React</code> 的内部状态被破坏，导致整个应用崩溃，这是不应该出现的现象</p>
<p>作为一个框架，<code>react</code>也有自身对于错误的处理的解决方案</p>
<h2 data-id="heading-1">如何捕捉错误</h2>
<p>为了解决出现的错误导致整个应用崩溃的问题，<code>react16</code>引用了<strong>错误边界</strong>新的概念</p>
<p>错误边界是一种 <code>React</code> 组件，这种组件可以捕获发生在其子组件树任何位置的 <code>JavaScript</code> 错误，并打印这些错误，同时展示降级 <code>UI</code>，而并不会渲染那些发生崩溃的子组件树</p>
<p>错误边界在渲染期间、生命周期方法和整个组件树的构造函数中捕获错误</p>
<p>形成错误边界组件的两个条件：</p>
<ul>
<li>使用了 static getDerivedStateFromError()</li>
<li>使用了 componentDidCatch()</li>
</ul>
<p>抛出错误后，请使用 <code>static getDerivedStateFromError()</code> 渲染备用 UI ，使用 <code>componentDidCatch()</code> 打印错误信息，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ErrorBoundary</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">hasError</span>: <span class="hljs-literal">false</span> &#125;;
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getDerivedStateFromError</span>(<span class="hljs-params">error</span>)</span> &#123;
    <span class="hljs-comment">// 更新 state 使下一次渲染能够显示降级后的 UI</span>
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">hasError</span>: <span class="hljs-literal">true</span> &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidCatch</span>(<span class="hljs-params">error, errorInfo</span>)</span> &#123;
    <span class="hljs-comment">// 你同样可以将错误日志上报给服务器</span>
    logErrorToMyService(error, errorInfo);
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state.hasError) &#123;
      <span class="hljs-comment">// 你可以自定义降级后的 UI 并渲染</span>
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Something went wrong.<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.props.children; 
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就可以把自身组件的作为错误边界的子组件，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><ErrorBoundary>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyWidget</span> /></span></span>
</ErrorBoundary>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面这些情况无法捕获到异常：</p>
<ul>
<li>事件处理</li>
<li>异步代码</li>
<li>服务端渲染</li>
<li>自身抛出来的错误</li>
</ul>
<p>在<code>react 16</code>版本之后，会把渲染期间发生的所有错误打印到控制台</p>
<p>除了错误信息和 JavaScript 栈外，React 16 还提供了组件栈追踪。现在你可以准确地查看发生在组件树内的错误信息：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcamo.githubusercontent.com%2F2dd02d7fda586ba9c0f2b3c1b758dc8d3aab80eba58c2a9d103ec0a4fc4bf269%2F68747470733a2f2f7374617469632e7675652d6a732e636f6d2f37623262353164302d663238392d313165622d616239302d6439616538313462323430642e706e67" target="_blank" rel="nofollow noopener noreferrer" title="https://camo.githubusercontent.com/2dd02d7fda586ba9c0f2b3c1b758dc8d3aab80eba58c2a9d103ec0a4fc4bf269/68747470733a2f2f7374617469632e7675652d6a732e636f6d2f37623262353164302d663238392d313165622d616239302d6439616538313462323430642e706e67" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b04f8b3be4054ee189105297ab3da139~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>可以看到在错误信息下方文字中存在一个组件栈，便于我们追踪错误</p>
<p>对于错误边界无法捕获的异常，如事件处理过程中发生问题并不会捕获到，是因为其不会在渲染期间触发，并不会导致渲染时候问题</p>
<p>这种情况可以使用<code>js</code>的<code>try...catch...</code>语法，如下：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">error</span>: <span class="hljs-literal">null</span> &#125;;
    <span class="hljs-built_in">this</span>.handleClick = <span class="hljs-built_in">this</span>.handleClick.bind(<span class="hljs-built_in">this</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// 执行操作，如有错误则会抛出</span>
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-built_in">this</span>.setState(&#123; error &#125;);
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state.error) &#123;
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Caught an error.<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    &#125;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleClick&#125;</span>></span>Click Me<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除此之外还可以通过监听<code>onerror</code>事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'error'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123; ... &#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            