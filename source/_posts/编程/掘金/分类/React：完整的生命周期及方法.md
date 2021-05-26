
---
title: 'React：完整的生命周期及方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8e9a51a2a1d452fb519ef47aef42447~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 03:01:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8e9a51a2a1d452fb519ef47aef42447~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是生命周期</h2>
<p>在具有许多组件的应用程序中，当组件被销毁时释放所占用的资源是非常重要的。</p>
<p>组件从 <strong>被创建</strong> 到 <strong>被销毁</strong> 的过程称为组件的生命周期。</p>
<p>组件的生命周期可分成三个状态：</p>
<ul>
<li><strong>Mounting（挂载时）</strong></li>
<li><strong>Updating（更新时）</strong></li>
<li><strong>Unmounting（卸载时）</strong></li>
</ul>
<p>组件的生命周期可分为三个阶段：</p>
<ul>
<li><strong>Render：</strong> 用于计算当前的状态/更新信息，会根据产生的任务的优先级，安排任务的调度（schedule）</li>
<li><strong>Pre-commit：</strong> commit 之前，可以获取当前 DOM 的快照（snap）</li>
<li><strong>Commit：</strong> 把所有更新都 commit 到 DOM 树上</li>
</ul>
<h2 data-id="heading-1">生命周期方法</h2>
<h3 data-id="heading-2">图解</h3>
<h4 data-id="heading-3">常见方法版</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8e9a51a2a1d452fb519ef47aef42447~tplv-k3u1fbpfcp-watermark.image" alt="react-lifecycle-1.png" loading="lazy" referrerpolicy="no-referrer">
（ 图片来源：<a href="https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/" target="_blank" rel="nofollow noopener noreferrer">projects.wojtekmaj.pl/react-lifec…</a> ）</p>
<h4 data-id="heading-4">完整方法版</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8ee6dc5af7b48b697aa2ecd3dcffdd4~tplv-k3u1fbpfcp-watermark.image" alt="react-lifecycle.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（ 图片来源：<a href="https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/" target="_blank" rel="nofollow noopener noreferrer">projects.wojtekmaj.pl/react-lifec…</a> ）</p>
<h3 data-id="heading-5">方法</h3>
<h4 data-id="heading-6">- contructor</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常，在 <code>React</code> 中，构造函数仅用于以下两种情况：</p>
<ul>
<li>通过给 <code>this.state</code> 赋值对象来初始化内部 <code>state</code>。( 唯一可以直接修改 <code>state</code> 的地方)</li>
<li>为事件处理函数绑定实例</li>
</ul>
<p>在 <code>constructor()</code> 函数中<strong>不要调用 <code>setState()</code> 方法。</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
  <span class="hljs-built_in">super</span>(props);
  <span class="hljs-comment">// 不要在这里调用 this.setState()</span>
  <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span> &#125;;
  <span class="hljs-built_in">this</span>.handleClick = <span class="hljs-built_in">this</span>.handleClick.bind(<span class="hljs-built_in">this</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">- getDerivedStateFromProps</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">static</span> getDerivedStateFromProps(props, state)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法是 “如何用 <code>props</code> 初始化 <code>state</code> ” 的最佳实践。</p>
<p><strong>注意，该方法在每次 render 前都会被调用。</strong></p>
<p>此方法适用于罕见的用例（表单控件获取默认值）。当 <code>state</code> 是从 <code>props</code> 获取时，就必须要维护两者的一致性，这将会增加复杂度和 <code>bug</code>。</p>
<h4 data-id="heading-8">- shouldComponentUpate</h4>
<pre><code class="hljs language-js copyable" lang="js">shouldComponentUpdate(nextProps, nextState);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 <code>props</code> 或 <code>state</code> 发生变化时，<code>shouldComponentUpdate()</code> 会在渲染执行之前被调用。返回值默认为 <code>true</code>。首次渲染或使用 <code>forceUpdate()</code> 时不会调用该方法。</p>
<p>此方法 <strong>仅作为性能优化</strong> 的方式而存在。它的工作一般可以由 <a href="https://zh-hans.reactjs.org/docs/react-api.html#reactpurecomponent" target="_blank" rel="nofollow noopener noreferrer">PrueComponent</a> 自动实现。</p>
<blockquote>
<p>后续版本，<code>React</code> 可能会将 <code>shouldComponentUpdate</code> 仅视为提示，并且，当返回 <code>false</code> 时，仍可能导致组件重新渲染。</p>
</blockquote>
<h4 data-id="heading-9">- render</h4>
<pre><code class="hljs language-js copyable" lang="js">render();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用于描述 <code>DOM</code> 结构，组件中唯一必须实现的方法。</p>
<h4 data-id="heading-10">- getSnapshotBeforeUpdate</h4>
<pre><code class="hljs language-js copyable" lang="js">getSnapshotBeforeUpdate(prevProps, prevState);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>能在组件发生更改之前从 <code>DOM</code> 中捕获一些信息（例如，滚动位置）。此生命周期方法的任何返回值将作为参数传递给 <code>componentDidUpdate()</code>。</p>
<h4 data-id="heading-11">- componentDidMount</h4>
<pre><code class="hljs language-js copyable" lang="js">componentDidMount();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件挂载后（插入 <code>DOM</code> 树中）立即调用。在这里可以安全操作 <code>DOM</code> 节点、发送<code>ajax</code> 请求（<code>DOM</code> 节点的初始化）或一些副作用的事情（订阅）</p>
<p>如果你在这里调用了 <code>setState</code>，它将触发额外渲染，虽然此渲染会发生在浏览器更新屏幕之前，但会导致性能问题。</p>
<h4 data-id="heading-12">- componentDidUpdate</h4>
<pre><code class="hljs language-js copyable" lang="js">componentDidUpdate(prevProps, prevState, snapshot);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在更新后会被立即调用。首次渲染不会执行此方法。</p>
<p><strong>⚠️ 注意，</strong> 如果直接调用 <code>setState()</code>，它必须被包裹在一个条件语句里，否则会导致死循环。</p>
<h4 data-id="heading-13">- componentWillUnmount</h4>
<pre><code class="hljs language-js copyable" lang="js">componentWillUnmount();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件卸载及销毁之前直接调用，做一些资源释放操作，例如，清除 <code>timer</code>，取消网络请求或清除在 <code>componentDidMount()</code> 中创建的订阅等。</p>
<p><strong>⚠️ 注意：不应调用 <code>setState()</code></strong>，因为该组件将永远不会重新渲染。</p>
<h2 data-id="heading-14">演示</h2>
<h3 data-id="heading-15">Clock</h3>
<p>用官方的经典 <code>Clock</code> 组件，可以清楚的展示出常见生命周期方法的应用：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">date</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.timerID = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.tick(), <span class="hljs-number">1000</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.timerID);
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"component did update!"</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">tick</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">date</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
    &#125;);
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, world!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>It is &#123;this.state.date.toLocaleTimeString()&#125;.<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Clock</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件第一次挂载时，设置一个定时器；同时，在组件卸载时，清除定时器。</p>
<p><code>state.date</code> 发生改变时，会引发组件的重新渲染。</p>
<h3 data-id="heading-16">getSnapshotBeforeUpdate 实践</h3>
<p>以特殊方式处理滚动位置的聊天线程：因为每一条新消息的置顶设定，无法让页面固定在某处，所以在每次更新前都需要计算调整滚动条的位置。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ScrollList</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PureComponent</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">messages</span>: [],
  &#125;;
  <span class="hljs-function"><span class="hljs-title">getSnapshotBeforeUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.rootNode.scrollHeight;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params">prevProps, prevState, prevScrollHeight</span>)</span> &#123;
    <span class="hljs-keyword">const</span> scrollTop = <span class="hljs-built_in">this</span>.rootNode.scrollTop;
    <span class="hljs-keyword">if</span> (scrollTop < <span class="hljs-number">5</span>) <span class="hljs-keyword">return</span>;
    <span class="hljs-built_in">this</span>.rootNode.scrollTop =
      scrollTop + (<span class="hljs-built_in">this</span>.rootNode.scrollHeight - prevScrollHeight);
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"scroll-list"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;(n)</span> =></span> (this.rootNode = n)&#125;>
        &#123;this.state.messages.map((msg) => (
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;msg&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        ))&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>DOM</code> 更新前，通过 <code>getSnapshotBeforeUpdate</code> 获取原来的元素内容高度（ <code>scrollHeight</code> ），并作为第三个参数传给 <code>componentDidUpdate</code> ；</p>
<p>在 <code>componentDidUpdate</code> 中，通过添加元素内容高度差值（ <code>this.rootNode.scrollHeight - prevScrollHeight</code> ），调整滚动条位置（ <code>scrollTop</code> ）。</p>
<h2 data-id="heading-17">参考资料</h2>
<ul>
<li>State & 生命周期：<a href="https://zh-hans.reactjs.org/docs/state-and-lifecycle.html" target="_blank" rel="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/state-…</a></li>
<li>React.Component：<a href="https://zh-hans.reactjs.org/docs/react-component.html#constructor" target="_blank" rel="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/react-…</a></li>
</ul></div>  
</div>
            