
---
title: 'react库的那些重要的Change'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1461'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 01:06:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=1461'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0"><a href="mailto:React@15.x">React@15.x</a></h3>
<h4 data-id="heading-1">1. React的生命周期</h4>
<p>Mounting:</p>
<ul>
<li><code>constructor</code></li>
<li><code>componentWillMount</code></li>
<li><code>componentDidMount</code></li>
<li><code>render</code></li>
</ul>
<p>Updating</p>
<ul>
<li><code>componentWillReceivedProps</code></li>
<li><code>SCU</code>
<ul>
<li>shadow state and props comparision</li>
</ul>
</li>
<li><code>componentWillUpdate</code></li>
<li><code>render</code></li>
<li><code>componentDidUpdate</code></li>
</ul>
<p>Unmounting</p>
<ul>
<li><code>componnentWillUnmount</code></li>
</ul>
<h4 data-id="heading-2">2. Error handling</h4>
<p><code>js</code>内部的error会导致程序崩溃，会在页面上渲染出晦涩的错误提示，<code>React</code>没有提供方式可以恢复现场。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// react@15.6.2</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">componentWillMount</span>(<span class="hljs-params"></span>)</span> &#123;
     <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'something Wrong'</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      App render
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  &#125;
&#125;
ReactDom.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#root'</span>)) <span class="hljs-comment">// 直接白屏</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3"><a href="mailto:React@16.0">React@16.0</a></h3>
<ul>
<li>Components can now return arrays and strings from <code>render</code></li>
<li><code>ErrorBoundary</code>
<ul>
<li>componengDidCatch</li>
<li>getDerivedStateFromError</li>
</ul>
</li>
<li><code>ReactDOM.createPortal()</code></li>
</ul>
<p><code>ErrorBoundary</code></p>
<ul>
<li>
<p>能捕获</p>
<ul>
<li><code>constructor</code>内的错误</li>
<li>生命周期内的错误</li>
<li><code>render</code>过程的错误</li>
</ul>
</li>
<li>
<p>不能捕获</p>
<ul>
<li>event handler，可以在代码里用<code>try&#123;&#125;catch(e)&#123;&#125;</code></li>
<li>异步代码</li>
<li>服务端渲染</li>
<li><code>ErrorBoudary</code>内部的代码</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 添加 ErrorBoundary 组件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ErrorBoundary</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">hasError</span>: <span class="hljs-literal">false</span> &#125;;
  &#125;
  <span class="hljs-function"><span class="hljs-title">componentDidCatch</span>(<span class="hljs-params">error, info</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">hasError</span>: <span class="hljs-literal">true</span> &#125;);
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state.hasError) &#123;      
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Something went wrong.<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>; <span class="hljs-comment">// falllback ui</span>
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.props.children;
  &#125;
&#125;
<span class="hljs-keyword">const</span> el = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ErrorBoundary</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">ErrorBoundary</span>></span></span>
<span class="hljs-comment">// 页面会显示Something went wrong.的文本内容</span>
ReactDom.render(el, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#root'</span>)) 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4"><a href="mailto:React@16.3">React@16.3</a></h3>
<h4 data-id="heading-5">1. 生命周期</h4>
<ul>
<li>Mounting
<ul>
<li>在<code>componentWillMount</code>之前增加 <code>static getDerivedStateFromProps</code></li>
<li><code>componentWillMount/UNSAFE_ComponentWillMount</code></li>
</ul>
</li>
<li>Updating
<ul>
<li>在<code>SCU</code>的之前增加<code>static getDerivedStateFromProps</code></li>
<li><code>componentWillReceiveProps/UNSAFE_componentWillReceiveProps</code></li>
<li><code>componentWillUpdate/UNSAFE_componentWillUpdate</code></li>
<li><code>render</code>之后<code>ComponentDidUpdate</code>之前，增加了<code>getSnapshotBeforeUpdate</code>钩子</li>
</ul>
</li>
</ul>
<h4 data-id="heading-6">2. <code><React.StrictMode></code></h4>
<p>这个高阶组件是用来检测一些老的api或者不安全的生命周期的使用，会给出相应的警告。<a href="https://reactjs.org/docs/strict-mode.html" target="_blank" rel="nofollow noopener noreferrer">文档portal</a></p>
<h4 data-id="heading-7">3.<code>ref</code></h4>
<ul>
<li>createRef</li>
<li>forwardRef</li>
</ul>
<h3 data-id="heading-8"><a href="mailto:React@16.6">React@16.6</a></h3>
<ul>
<li><code>React.memo</code></li>
<li><code>React.lazy</code></li>
<li><code>Suspense</code> （配合<code>react.lazy可以实现code-spliting</code>）</li>
</ul>
<h3 data-id="heading-9"><a href="mailto:React@16.8">React@16.8</a></h3>
<ul>
<li>hooks</li>
</ul>
<h3 data-id="heading-10"><a href="mailto:React@17.0">React@17.0</a></h3>
<ul>
<li>Concurrent Mode</li>
</ul>
<hr>
<h4 data-id="heading-11">小抄：</h4>
<p>Data change without mutation</p>
<ul>
<li>Easier Undo/Redo and Time Travel。保存引用就可以了。</li>
<li>tracking change...如果是基于之前的对象做改变，对比就可能需要遍历所有属性；但是如果传入新的对象，只需要比对引用就可以了</li>
<li>PureComponent时，更容易比对之后得出何时渲染。shouldComponentUpdate。</li>
</ul></div>  
</div>
            