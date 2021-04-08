
---
title: '使用hooks写React组件注意的5个地方'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0581b0673f134417a585d94782cfdf36~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 23:33:42 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0581b0673f134417a585d94782cfdf36~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="搜狗截图20210405114309.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0581b0673f134417a585d94782cfdf36~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
Hook是React16.8开始新增的特性。虽然React官方文档已经作出了针对React hooks的相关概念的讲解，但是光看官方文档是很难将hooks使用好的，在编写hooks的过程中很容易跳进陷阱和错误。本文总结了5个不好的地方。</p>
<h2 data-id="heading-0">01.不需要render的场景下使用<code>useState</code></h2>
<p>在函数组件中我们可以使用<code>useState</code>来管理状态，这使得对状态的管理变得很简单，但是也容易被滥用，我们通过下面的代码样例看下容易忽略的地方。</p>
<p><strong>不推荐×</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ClickButton</span>(<span class="hljs-params">props</span>)</span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = setState(<span class="hljs-number">0</span>)
  <span class="hljs-keyword">const</span> onClickCount = <span class="hljs-function">() =></span> &#123;
    setCount(<span class="hljs-function">(<span class="hljs-params">c</span>) =></span> c + <span class="hljs-number">1</span>)
  &#125;
  <span class="hljs-keyword">const</span> onClickRequest = <span class="hljs-function">() =></span> &#123;
    apiCall(count)
  &#125;
  
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onClickCount&#125;</span>></span>Click<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onClickRequest&#125;</span>></span>Submit<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题所在：仔细看上面的代码，乍一看其实也没什么问题，点击按钮更新 <code>count</code>。但是问题也就出在这里，我们的 <code>return</code> 部分并没有用到 count 状态，而每次 <code>setCount</code> 都会使组件重新渲染一次，而这个渲染并不是我们需要的，多出来的渲染会使得页面的性能变差，因此我们可以改造一下代码，如下代码：</p>
<p><strong>推荐√</strong><br>
如果我们只是单纯的想要一个能在组件声明周期内保存的变量，但是变量的更新不需要组件的重新渲染，我们可以使用<code> useRef</code> 钩子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ClickButton</span>(<span class="hljs-params">props</span>)</span>&#123;
  <span class="hljs-keyword">const</span> count = useRef(<span class="hljs-number">0</span>)
  <span class="hljs-keyword">const</span> onClickCount = <span class="hljs-function">() =></span> &#123;
    count.current++
  &#125;
  <span class="hljs-keyword">const</span> onClickRequest = <span class="hljs-function">() =></span> &#123;
    apiCall(count.current)
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onClickCount&#125;</span>></span>Click<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onClickRequest&#125;</span>></span>Submit<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">02.使用了<code>router.push</code>而非<code>link</code></h2>
<p>在React SPA应用中，我们用<code>react-router</code>来处理路由的跳转，我们很经常在组件中写了一个按钮，通过点击按钮的事件来处理路由的跳转，如下代码：</p>
<p><strong>不推荐×</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ClickButton</span>(<span class="hljs-params">props</span>)</span>&#123;
  <span class="hljs-keyword">const</span> history = useHistory()
  <span class="hljs-keyword">const</span> onClickGo = <span class="hljs-function">() =></span> &#123;
    history.push(<span class="hljs-string">'/where-page'</span>)
  &#125;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onClickGo&#125;</span>></span>Go to where<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题所在：尽管上述代码可以正常工作，但是却不符合Accessibility（易访问性设计）的要求，此类按钮并不会被屏幕阅读器当作一个可以跳转的链接。因此我们可以改造一下代码，如下代码：</p>
<p>推荐√</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ClickButton</span>(<span class="hljs-params">props</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/next-page"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>Go to where<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">Link</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">03.通过<code>useEffect</code>来处理actions</h2>
<p>有时候，我们只想在 React 更新 DOM 之后运行一些额外的代码。比如发送网络请求，手动变更 DOM，记录日志。</p>
<p><strong>不推荐×</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">DataList</span>(<span class="hljs-params">&#123; onSuccess &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [loading, setLoading] = useState(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">const</span> [error, setError] = useState(<span class="hljs-literal">null</span>);
  <span class="hljs-keyword">const</span> [data, setData] = useState(<span class="hljs-literal">null</span>);

  <span class="hljs-keyword">const</span> fetchData = <span class="hljs-function">() =></span> &#123;
    setLoading(<span class="hljs-literal">true</span>);
    callApi()
      .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> setData(res))
      .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> setError(err))
      .finally(<span class="hljs-function">() =></span> setLoading(<span class="hljs-literal">false</span>));
  &#125;;

  useEffect(<span class="hljs-function">() =></span> &#123;
    fetchData();
  &#125;, []);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (!loading && !error && data) &#123;
      onSuccess();
    &#125;
  &#125;, [loading, error, data, onSuccess]);

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Data: &#123;data&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题所在：上面的代码使用了两个<code>useEffect</code> ，第一个用来请求异步数据，第二个用来调用回调函数。在第一个异步请求数据成功，才会触发第二个 <code>useEffect</code> 的执行，但是，我们并不能完全保证，第二个 <code>useEffect </code>的依赖项完全受控于第一个 <code>useEffect</code> 的成功请求数据。因此我们可以改造一下代码，如下代码：</p>
<p><strong>推荐√</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">DataList</span>(<span class="hljs-params">&#123; onSuccess &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [loading, setLoading] = useState(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">const</span> [error, setError] = useState(<span class="hljs-literal">null</span>);
  <span class="hljs-keyword">const</span> [data, setData] = useState(<span class="hljs-literal">null</span>);

  <span class="hljs-keyword">const</span> fetchData = <span class="hljs-function">() =></span> &#123;
    setLoading(<span class="hljs-literal">true</span>);
    callApi()
      .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        setData(res)
        onSuccess()
       &#125;)
      .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> setError(err))
      .finally(<span class="hljs-function">() =></span> setLoading(<span class="hljs-literal">false</span>));
  &#125;;

  useEffect(<span class="hljs-function">() =></span> &#123;
    fetchData();
  &#125;, []);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Data: &#123;data&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">04.单一职责组件</h2>
<p>什么时候该把一个组件分成几个更小的组件？如何构建组件树？在使用基于组件的框架时，所有这些问题每天都会出现。然而，设计组件时的一个常见错误是将两个用例组合成一个组件。</p>
<p><strong>不推荐×</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Header</span>(<span class="hljs-params">&#123; menuItems &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">header</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">HeaderInner</span> <span class="hljs-attr">menuItems</span>=<span class="hljs-string">&#123;menuItems&#125;</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">header</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HeaderInner</span>(<span class="hljs-params">&#123; menuItems &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> isMobile() ? <span class="xml"><span class="hljs-tag"><<span class="hljs-name">BurgerButton</span> <span class="hljs-attr">menuItems</span>=<span class="hljs-string">&#123;menuItems&#125;</span> /></span></span> : <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Tabs</span> <span class="hljs-attr">tabData</span>=<span class="hljs-string">&#123;menuItems&#125;</span> /></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题所在：上面的代码通过这种方法，组件<code>HeaderInner</code>试图同时成为两个不同的东西，一次做不止一件事情并不是很理想。此外，它还使得在其他地方测试或重用组件变得更加困难。因此我们可以改造一下代码，如下代码：</p>
<p><strong>推荐√</strong></p>
<p>将条件提升一级，可以更容易地看到组件的用途，并且它们只有一个职责，即<code><Tabs/></code>或<code><BurgerButton/></code>，而不是试图同时成为两个不同的东西。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Header</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">header</span>></span>
      &#123;isMobile() ? <span class="hljs-tag"><<span class="hljs-name">BurgerButton</span> <span class="hljs-attr">menuItems</span>=<span class="hljs-string">&#123;menuItems&#125;</span> /></span> : <span class="hljs-tag"><<span class="hljs-name">Tabs</span> <span class="hljs-attr">tabData</span>=<span class="hljs-string">&#123;menuItems&#125;</span> /></span>&#125;
    <span class="hljs-tag"></<span class="hljs-name">header</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">05.单一职责useEffects</h2>
<p>通过对比<code>componentWillReceiveProps</code>或<code>componentDidUpdate</code>方法，才认识到<code>userEffect</code>的美丽。但是没有妥当使用useEffect也是容易出问题的。</p>
<p><strong>不推荐×</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Example</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> location = useLocation();
  <span class="hljs-keyword">const</span> fetchData = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">/*  Calling the api */</span>
  &#125;;

  <span class="hljs-keyword">const</span> updateBreadcrumbs = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">/* Updating the breadcrumbs*/</span>
  &#125;;

  useEffect(<span class="hljs-function">() =></span> &#123;
    fetchData();
    updateBreadcrumbs();
  &#125;, [location.pathname]);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">BreadCrumbs</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题所在：上面的<code>useEffect</code>同时触发了两个副作用，但是并不都是我们需要的副作用，因此我们可以改造一下代码，如下代码：</p>
<p><strong>推荐√</strong><br>
将两个副作用从一个useEffect中分离出来。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Example</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> location = useLocation();

  <span class="hljs-keyword">const</span> fetchData = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">/*  Calling the api */</span>
  &#125;;

  <span class="hljs-keyword">const</span> updateBreadcrumbs = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">/* Updating the breadcrumbs*/</span>
  &#125;;

  useEffect(<span class="hljs-function">() =></span> &#123;
    fetchData();
    updateBreadcrumbs();
  &#125;, [location.pathname]);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">BreadCrumbs</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://www.lorenzweiss.de/common_mistakes_react_hooks/" target="_blank" rel="nofollow noopener noreferrer">参考：Five common mistakes writing react components (with hooks) in 2020</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            