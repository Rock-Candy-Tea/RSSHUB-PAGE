
---
title: '你知道 React setState 的原理吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f46d801ac6d04509a3fad8c59d1058f7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 01:41:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f46d801ac6d04509a3fad8c59d1058f7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家都知道，在 React 中是通过 setState 来更新类组件的状态的，但是你真的了解其运行机制吗？</p>
<h2 data-id="heading-0">现象描述</h2>
<p>下面是一个最基础的类组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SetStateDemo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props)
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">number</span>: <span class="hljs-number">0</span> &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;this.state.number&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleClick&#125;</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;

  handleClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-built_in">this</span>.state.number + <span class="hljs-number">1</span> &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当点击按钮的时候，会把内部状态 number 的值在原有基础上递增 1，这个并没有什么异议，但是当我们在 handleClick 函数中添加两行 setState 的时候，有意思的问题就来了：</p>
<pre><code class="hljs language-js copyable" lang="js">  handleClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-built_in">this</span>.state.number + <span class="hljs-number">1</span> &#125;)
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-built_in">this</span>.state.number + <span class="hljs-number">1</span> &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当每次点击之后，程序并没有将 number 的值递增 2，而是仍然递增 1，这是为什么呢？这里先不忙解释具体原因，而是再把另外一个场景也放在这里对比一下，即添加定时器包裹之后：</p>
<pre><code class="hljs language-js copyable" lang="js">  handleClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-built_in">this</span>.state.number + <span class="hljs-number">1</span> &#125;)
      <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-built_in">this</span>.state.number + <span class="hljs-number">1</span> &#125;)
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候会发现 number 的值每次会按 2 递增！如果这个现象也使你感到迷惑的话，可以继续看下去：</p>
<h2 data-id="heading-1">原理分析</h2>
<p>在 React 中，状态的更新默认情况下是异步的、批量的，并非同步更新，也就是说当开发者调用 setState 的时候，并没有立即执行，而是先缓存起来，等到事件函数处理完成之后，再批量更新，只更新和渲染一次。</p>
<p>为什么要这么做？试想下面的一个场景：</p>
<pre><code class="hljs language-js copyable" lang="js">  handleClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-number">1</span> &#125;)
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-number">2</span> &#125;)
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-number">3</span> &#125;)
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-number">4</span> &#125;)
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-number">5</span> &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开发者在事件处理函数中频繁调用 setState，如果每次都是立即更新和渲染，就会导致页面频繁刷新，对性能造成影响。在上面的例子中，最终的状态就是 number 等于 5，中间的状态完全不必要保留。</p>
<p>在 React 中，事件处理函数被 React 接管，只要是在 React 的控制范围内，都会进行合并和批量更新，而 setTimeout 等异步操作脱离了 React 主线程的控制，则不会合并和批量更新。先看下面这张图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f46d801ac6d04509a3fad8c59d1058f7~tplv-k3u1fbpfcp-zoom-1.image" alt="setState" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个地方是 React 的一个重点和难点，一定要搞懂其实现原理哦，接下来上代码！</p>
<h3 data-id="heading-2">非批量更新</h3>
<p>我们知道类组件总是继承自 React.Component，下面就是该 Component 的实现逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createDOM &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./react-dom'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-keyword">static</span> isReactComponent = <span class="hljs-literal">true</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.props = props
    <span class="hljs-built_in">this</span>.state = &#123;&#125;
  &#125;
  <span class="hljs-comment">// 非批量更新的 setState 实现</span>
  <span class="hljs-function"><span class="hljs-title">setState</span>(<span class="hljs-params">nextState, callback</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> nextState === <span class="hljs-string">'function'</span>) nextState = nextState(<span class="hljs-built_in">this</span>.state)
    <span class="hljs-built_in">this</span>.state = &#123; ...this.state, ...nextState &#125;
    <span class="hljs-built_in">this</span>.forceUpdate()
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback === <span class="hljs-string">'function'</span>) callback()
  &#125;
​
  <span class="hljs-comment">// 强制刷新</span>
  <span class="hljs-function"><span class="hljs-title">forceUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.componentWillUpdate?.() <span class="hljs-comment">// 调用 componentWillUpdate 钩子</span>
    <span class="hljs-keyword">const</span> oldDOM = <span class="hljs-built_in">this</span>.dom <span class="hljs-comment">// 类组件当前对应的真实DOM</span>
    <span class="hljs-keyword">const</span> newDOM = createDOM(<span class="hljs-built_in">this</span>.render()) <span class="hljs-comment">// 新的DOM</span>
    oldDOM.parentNode.replaceChild(newDOM, oldDOM) <span class="hljs-comment">// 替换</span>
    <span class="hljs-built_in">this</span>.dom = newDOM
    <span class="hljs-built_in">this</span>.componentDidUpdate?.() <span class="hljs-comment">// 调用 componentDidUpdate 钩子</span>
  &#125;
​
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'此方法为抽象方法，需要子类实现'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，代码很简单，就是内部使用 this.state 保存状态，用 setState 函数更新 this.state 的值，然后用 react-dom 库中的 createDOM 方法把 render 函数中返回的虚拟 DOM 生成真实 DOM 并替换旧的。</p>
<h3 data-id="heading-3">批量更新</h3>
<p>这样的话，每次开发者调用 setState 都会重新渲染和替换。为了优化这个过程，可以引入了 updateQueue 全局对象和 Updater 类专门用于批量更新：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> updateQueue = &#123;
  <span class="hljs-attr">isBatchingUpdate</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 是否处于批量更新模式</span>
  <span class="hljs-attr">updaters</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(),
  <span class="hljs-function"><span class="hljs-title">batchUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> updater <span class="hljs-keyword">of</span> updateQueue.updaters) &#123;
      updater.updateClassComponent()
    &#125;
    updateQueue.isBatchingUpdate = <span class="hljs-literal">false</span>
  &#125;,
&#125;

<span class="hljs-comment">// 专门负责更新的类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Updater</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">it</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.classInstance = it <span class="hljs-comment">// 类组件的实例</span>
    <span class="hljs-built_in">this</span>.pendingStates = [] <span class="hljs-comment">// 等待生效的状态，可能是一个对象，也可能是一个函数</span>
    <span class="hljs-built_in">this</span>.callbacks = [] <span class="hljs-comment">// 回调数组</span>
  &#125;

  <span class="hljs-function"><span class="hljs-title">addState</span>(<span class="hljs-params">partialState, callback</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.pendingStates.push(partialState) <span class="hljs-comment">// 缓存用户设置的新状态（可能是函数或对象）</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback === <span class="hljs-string">'function'</span>) <span class="hljs-built_in">this</span>.callbacks.push(callback)
    <span class="hljs-built_in">this</span>.emitUpdate() <span class="hljs-comment">// 通知更新</span>
  &#125;

  <span class="hljs-comment">// 无论属性变了还是状态变了，都会更新</span>
  <span class="hljs-function"><span class="hljs-title">emitUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (updateQueue.isBatchingUpdate) &#123;
      updateQueue.updaters.add(<span class="hljs-built_in">this</span>) <span class="hljs-comment">// 如果处于批量更新模式，则不立即更新类组件，setState处理完毕</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.updateClassComponent() <span class="hljs-comment">// 更新函数组件</span>
    &#125;
  &#125;

  <span class="hljs-comment">// 立即更新函数组件</span>
  <span class="hljs-function"><span class="hljs-title">updateClassComponent</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; classInstance, pendingStates, callbacks &#125; = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">if</span> (pendingStates.length > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">const</span> nextState = <span class="hljs-built_in">this</span>.getState() <span class="hljs-comment">// 计算新状态</span>
      classInstance.state = nextState

      <span class="hljs-comment">/* 生命周期钩子拒绝更新的场景 */</span>
      <span class="hljs-keyword">const</span> flag = classInstance.shouldComponentUpdate?.(classInstance.props, nextState)
      <span class="hljs-keyword">if</span> (flag === <span class="hljs-literal">false</span>) <span class="hljs-keyword">return</span>

      classInstance.forceUpdate() <span class="hljs-comment">// 强制更新</span>
      callbacks.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb())
      callbacks.length = <span class="hljs-number">0</span>
    &#125;
  &#125;

  <span class="hljs-comment">// 获取批量更新最后的状态</span>
  <span class="hljs-function"><span class="hljs-title">getState</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> &#123; state &#125; = <span class="hljs-built_in">this</span>.classInstance
    <span class="hljs-built_in">this</span>.pendingStates.forEach(<span class="hljs-function"><span class="hljs-params">nextState</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> nextState === <span class="hljs-string">'function'</span>) nextState = nextState(state)
      state = &#123; ...state, ...nextState &#125;
    &#125;)
    <span class="hljs-built_in">this</span>.pendingStates.length = <span class="hljs-number">0</span>
    <span class="hljs-keyword">return</span> state
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码量并不多，其实就是做了一件事：提供一个接口，允许将开发者每次 setState 的状态给缓存起来，最后一次性批量更新。</p>
<h3 data-id="heading-4">合成事件</h3>
<p>同步代码的使用效果为每次值递增 1：</p>
<pre><code class="hljs language-js copyable" lang="js">handleClick = <span class="hljs-function">() =></span> &#123;
  updateQueue.isBatchingUpdate = <span class="hljs-literal">true</span>
  <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-built_in">this</span>.state.number + <span class="hljs-number">1</span> &#125;)
  <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-built_in">this</span>.state.number + <span class="hljs-number">1</span> &#125;)
  updateQueue.batchUpdate()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>异步代码的使用效果为每次值递增 2：</p>
<pre><code class="hljs language-js copyable" lang="js">handleClick = <span class="hljs-function">() =></span> &#123;
  updateQueue.isBatchingUpdate = <span class="hljs-literal">true</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-built_in">this</span>.state.number + <span class="hljs-number">1</span> &#125;)
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-built_in">this</span>.state.number + <span class="hljs-number">1</span> &#125;)
  &#125;)
  updateQueue.batchUpdate()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这其实就是 setState 的原理，React 认为这种批量更新的行为应该是内置的，所以对每个事件监听函数进行了一层封装，即以 on 开头的 DOM 事件例如 onClick 等不再是原生的 DOM 事件，而是被 React 封装过一层的事件了，这样做的好处有：</p>
<ul>
<li>可以对所有事件处理函数内置批量更新逻辑</li>
<li>可以屏蔽不同浏览器对 DOM 事件实现的差异</li>
</ul></div>  
</div>
            