
---
title: 'React实践指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1638'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 17:56:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=1638'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>每天都在写业务代码中度过，但是呢，经常在写业务代码的时候，会感觉自己写的某些代码有点别扭，但是又不知道是哪里别扭，今天这篇文章我整理了一些在项目中使用的一些小的技巧点。</p>
</blockquote>
<h3 data-id="heading-0">状态逻辑复用</h3>
<p>在使用<code>React Hooks</code>之前，我们一般复用的都是组件，对组件内部的状态是没办法复用的，而<code>React Hooks</code>的推出很好的解决了状态逻辑的复用，而在我们日常开发中能做到哪些状态逻辑的复用呢？下面我罗列了几个当前我在项目中用到的通用状态复用。</p>
<h4 data-id="heading-1"><code>useRequest</code></h4>
<p>为什么要封装这个<code>hook</code>呢？在数据加载的时候，有这么几点是可以提取成共用逻辑的</p>
<ol>
<li><code>loading</code>状态复用</li>
<li>异常统一处理</li>
</ol>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> useRequest = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [loading, setLoading] = useState(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">const</span> [error, setError] = useState();

  <span class="hljs-keyword">const</span> run = useCallback(<span class="hljs-keyword">async</span> (...fns) => &#123;
    setLoading(<span class="hljs-literal">true</span>);
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all(
        fns.map(<span class="hljs-function">(<span class="hljs-params">fn</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> fn === <span class="hljs-string">'function'</span>) &#123;
            <span class="hljs-keyword">return</span> fn();
          &#125;
          <span class="hljs-keyword">return</span> fn;
        &#125;)
      );
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      setError(error);
    &#125; <span class="hljs-keyword">finally</span> &#123;
      setLoading(<span class="hljs-literal">false</span>);
    &#125;
  &#125;, []);

  <span class="hljs-keyword">return</span> &#123; loading, error, run &#125;;
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; loading, error, run &#125; = useRequest();
  useEffect(<span class="hljs-function">() =></span> &#123;
    run(
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          resolve();
        &#125;, <span class="hljs-number">2000</span>);
      &#125;)
    );
  &#125;, []);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Spin</span> <span class="hljs-attr">spinning</span>=<span class="hljs-string">&#123;loading&#125;</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Table</span> <span class="hljs-attr">columns</span>=<span class="hljs-string">&#123;columns&#125;</span> <span class="hljs-attr">dataSource</span>=<span class="hljs-string">&#123;data&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Table</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Spin</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">usePagination</h4>
<p>我们用表格的时候，一般都会用到分页，通过将分页封装成<code>hook</code>，一是可以介绍前端代码量，二是统一了前后端分页的参数，也是对后端接口的一个约束。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> usePagination = <span class="hljs-function">(<span class="hljs-params">
  initPage = &#123;
    total: <span class="hljs-number">0</span>,
    current: <span class="hljs-number">1</span>,
    pageSize: <span class="hljs-number">10</span>,
  &#125;
</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> [pagination, setPagination] = useState(initPage);

  <span class="hljs-comment">// 用于接口查询数据时的请求参数</span>
  <span class="hljs-keyword">const</span> queryPagination = useMemo(
    <span class="hljs-function">() =></span> (&#123; <span class="hljs-attr">limit</span>: pagination.pageSize, <span class="hljs-attr">offset</span>: pagination.current - <span class="hljs-number">1</span> &#125;),
    [pagination.current, pagination.pageSize]
  );

  <span class="hljs-keyword">const</span> tablePagination = useMemo(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      ...pagination,
      <span class="hljs-attr">onChange</span>: <span class="hljs-function">(<span class="hljs-params">page, pageSize</span>) =></span> &#123;
        setPagination(&#123;
          ...pagination,
          <span class="hljs-attr">current</span>: page,
          pageSize,
        &#125;);
      &#125;,
    &#125;;
  &#125;, [pagination]);

  <span class="hljs-keyword">const</span> setTotal = useCallback(<span class="hljs-function">(<span class="hljs-params">total</span>) =></span> &#123;
    setPagination(<span class="hljs-function">(<span class="hljs-params">prev</span>) =></span> (&#123;
      ...prev,
      total,
    &#125;));
  &#125;, []);
  <span class="hljs-keyword">const</span> setCurrent = useCallback(<span class="hljs-function">(<span class="hljs-params">current</span>) =></span> &#123;
    setPagination(<span class="hljs-function">(<span class="hljs-params">prev</span>) =></span> (&#123;
      ...prev,
      current,
    &#125;));
  &#125;, []);

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-comment">// 用于antd 表格使用</span>
    <span class="hljs-attr">pagination</span>: tablePagination,
    <span class="hljs-comment">// 用于接口查询数据使用</span>
    queryPagination,
    setTotal,
    setCurrent,
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了上面示例的两个<code>hook</code>，其实自定义<code>hook</code>可以无处不在，只要有公共的逻辑可以被复用，都可以被定义为独立的<code>hook</code>，然后在多个页面或组件中使用，我们在使用<code>redux</code>,<code>react-router</code>的时候，也会用到它们提供的<code>hook</code>。</p>
<h3 data-id="heading-3">在合适场景给<code>useState</code>传入函数</h3>
<p>我们在使用<code>useState</code>的<code>setState</code>的时候，大部分时候都会给<code>setState</code>传入一个值，但实际上<code>setState</code>不但可以传入普通的数据，而且还可以传入一个函数。下面极端代码分别描述了几个传入函数的例子。</p>
<h4 data-id="heading-4">下面的代码3秒后输出什么？</h4>
<p>如下代码所示，也有有两个按钮，一个按钮会在点击后延迟三秒然后给<code>count + 1</code>, 第二个按钮会在点击的时候，直接给<code>count + 1</code>,那么假如我先点击延迟的按钮，然后多次点击不延迟的按钮，三秒钟之后，<code>count</code>的值是多少？</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> &#123; useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      setCount(count + <span class="hljs-number">1</span>);
    &#125;, <span class="hljs-number">3000</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClickSync</span>(<span class="hljs-params"></span>) </span>&#123;
    setCount(count + <span class="hljs-number">1</span>);
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>count:&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>延迟加一<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClickSync&#125;</span>></span>加一<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们知道，<code>React</code>的函数式组件会在自己内部的状态或外部传入的<code>props</code>发生变化时，做重新渲染的动作。实际上这个重新渲染也就是重新执行这个函数式组件。</p>
<p>当我们点击延迟按钮的时候，因为<code>count</code>的值需要三秒后才会改变，这时候并不会重新渲染。然后再点击直接加一按钮，<code>count</code>值由<code>1</code>变成了<code>2</code>,  需要重新渲染。这里需要注意的是，虽然组件重新渲染了，但是<code>setTimeout</code>是在上一次渲染中被调用的，这也意味着<code>setTimeout</code>里面的<code>count</code>值是组件第一次渲染的值。</p>
<p>所以即使第二个按钮加一多次，三秒之后，<code>setTimeout</code>回调执行的时候因为引用的<code>count</code>的值还是初始化的<code>0</code>, 所以三秒后<code>count + 1</code>的值就是<code>1</code></p>
<h4 data-id="heading-5">如何让上面的代码延迟三秒后输出正确的值？</h4>
<p>这时候就需要使用到<code>setState</code>传入函数的方式了，如下代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> &#123; useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      setCount(<span class="hljs-function">(<span class="hljs-params">prevCount</span>) =></span> prevCount + <span class="hljs-number">1</span>);
    &#125;, <span class="hljs-number">3000</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClickSync</span>(<span class="hljs-params"></span>) </span>&#123;
    setCount(count + <span class="hljs-number">1</span>);
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>count:&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>延迟加一<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClickSync&#125;</span>></span>加一<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面代码可以看到，<code>setCount(count + 1)</code>被改为了<code> setCount((prevCount) => prevCount + 1)</code>。我们给<code>setCount</code>传入一个函数，<code>setCount</code>会调用这个函数，并且将前一个状态值作为参数传入到函数中，这时候我们就可以在<code>setTimeout</code>里面拿到正确的值了。</p>
<h4 data-id="heading-6">还可以在<code>useState</code>初始化的时候传入函数</h4>
<p>看下面这个例子，我们有一个<code>getColumns</code>函数，会返回一个表格的所以列,同时有一个<code>count</code>状态，每一秒加一一次。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> columns = getColumns();
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
      setCount(<span class="hljs-function">(<span class="hljs-params">prevCount</span>) =></span> prevCount + <span class="hljs-number">1</span>);
    &#125;, <span class="hljs-number">1000</span>);
  &#125;, []);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'columns发生了变化'</span>);
  &#125;, [columns]);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>count: &#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Table</span> <span class="hljs-attr">columns</span>=<span class="hljs-string">&#123;columns&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Table</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码执行之后，会发现每次<code>count</code>发生变化的时候，都会打印出<code>columns发生了变化</code>,而<code>columns</code>发生变化便意味着表格的属性发生变化，表格会重新渲染，这时候如果表格数据量不大，没有复杂处理逻辑还好，但如果表格有性能问题，就会导致整个页面的体验变得很差？其实这时候解决方案有很多，我们看一下如何用<code>useState</code>来解决呢？</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 将columns改为如下代码</span>
<span class="hljs-keyword">const</span> [columns] = useState(<span class="hljs-function">() =></span> getColumns());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候<code>columns</code>的值在初始化之后就不会再发生变化了。有人提出我也可以这样写 <code>useState(getColumns())</code>, 实际这样写虽然也可以，但是假如<code>getColumns</code>函数自身存在复杂的计算，那么实际上虽然<code>useState</code>自身只会初始化一次，但是<code>getColumn</code>还是会在每次组件重新渲染的时候被执行。</p>
<p>上面的代码也可以简化为</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> [columns] = useState(getColumns);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">了解<code>hook</code>比较算法的原理</h3>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> useColumns = <span class="hljs-function">(<span class="hljs-params">options</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; isEdit, isDelete &#125; = options;
  <span class="hljs-keyword">return</span> useMemo(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> [
      &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">'标题'</span>,
        <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'title'</span>,
        <span class="hljs-attr">key</span>: <span class="hljs-string">'title'</span>,
      &#125;,
      &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">'操作'</span>,
        <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'action'</span>,
        <span class="hljs-attr">key</span>: <span class="hljs-string">'action'</span>,
        <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><></span>
              &#123;isEdit && <span class="hljs-tag"><<span class="hljs-name">Button</span>></span>编辑<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>&#125;
              &#123;isDelete && <span class="hljs-tag"><<span class="hljs-name">Button</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>&#125;
            <span class="hljs-tag"></></span></span>
          );
        &#125;,
      &#125;,
    ];
  &#125;, [options]);
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> columns = useColumns(&#123; <span class="hljs-attr">isEdit</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">isDelete</span>: <span class="hljs-literal">false</span> &#125;);
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">1</span>);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'columns变了'</span>);
  &#125;, [columns]);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(count + 1)&#125;>修改count:&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Table</span> <span class="hljs-attr">columns</span>=<span class="hljs-string">&#123;columns&#125;</span> <span class="hljs-attr">dataSource</span>=<span class="hljs-string">&#123;[]&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Table</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上面的代码，当我们点击按钮修改<code>count</code>的时候，我们期待只有<code>count</code>的值会发生变化，但是实际上<code>columns</code>的值也发生了变化。想了解为什么<code>columns</code>会发生变化，我们先了解一下<code>react</code>比较算法的原理。</p>
<p><code>react</code>比较算法底层是使用的<code>Object.is</code>来比较传入的<code>state</code>的.</p>
<blockquote>
<p>语法： Object.is(value1, value2);</p>
</blockquote>
<p>如下代码是<code>Object.is</code>比较不同数据类型的数据时的返回值:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.is(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'foo'</span>);     <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.is(<span class="hljs-built_in">window</span>, <span class="hljs-built_in">window</span>);   <span class="hljs-comment">// true</span>

<span class="hljs-built_in">Object</span>.is(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'bar'</span>);     <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Object</span>.is([], []);           <span class="hljs-comment">// false</span>

<span class="hljs-keyword">var</span> foo = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;;
<span class="hljs-keyword">var</span> bar = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;;
<span class="hljs-built_in">Object</span>.is(foo, foo);         <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.is(foo, bar);         <span class="hljs-comment">// false</span>

<span class="hljs-built_in">Object</span>.is(<span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>);       <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 特例</span>
<span class="hljs-built_in">Object</span>.is(<span class="hljs-number">0</span>, -<span class="hljs-number">0</span>);            <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Object</span>.is(<span class="hljs-number">0</span>, +<span class="hljs-number">0</span>);            <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.is(-<span class="hljs-number">0</span>, -<span class="hljs-number">0</span>);           <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.is(<span class="hljs-literal">NaN</span>, <span class="hljs-number">0</span>/<span class="hljs-number">0</span>);         <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的代码可以看到，<code>Object.is</code>对于对象的比较是比较引用地址的，而不是比较值的，所以<code>Object.is([], []), Object.is(&#123;&#125;,&#123;&#125;)</code>的结果都是<code>false</code>。而对于基础类型来说，大家需要注意的是最末尾的四个特列，这是与<code>===</code>所不同的。</p>
<p>再回到上面代码的例子中，<code>useColumns</code>将传入的<code>options</code>作为<code>useMemo</code>的第二个参数，而<code>options</code>是一个对象。当组件的<code>count</code>状态发生变化的时候，会重新执行整个函数组件，这时候<code>useColumns</code>会被调用然后传入<code>&#123; isEdit: true, isDelete: false &#125;</code>,这是一个新创建的对象，与上一次渲染所创建的<code>options</code>的内容虽然一致，但是<code>Object.is</code>比较结果依然是<code>false</code>，所以<code>columns</code>的结果会被重新创建返回。</p>
<h3 data-id="heading-8">通过二次封装标准化组件</h3>
<p>我们在项目中使用<code>antd</code>作为组件库，虽然<code>antd</code>可以满足大部分的开发需要，但是有些地方通过对<code>antd</code>进行二次封装，不仅可以减少开发代码量，而且对于页面的交互起到了标准化作用。</p>
<p>看一下下面这个场景， 在我们开发一个数据表格的时候，一般会用到哪些功能呢？</p>
<ol>
<li>表格可以分页</li>
<li>表格最后一列会有操作按钮</li>
<li>表格顶部会有搜索区域</li>
<li>表格顶部可能会有操作按钮</li>
</ol>
<p>还有其他等等一系列的功能，这些功能在系统中会大量使用，而且其实现方式基本是一致的，这时候如果能把这些功能集成到一起封装成一个标准的组件，那么既能减少代码量，而且也会让页面展现上更加统一。</p>
<p>以封装表格操作列为例，一般用操作列我们会像下面这样封装</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> columns = [&#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">'操作'</span>,
        <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'action'</span>,
        <span class="hljs-attr">key</span>: <span class="hljs-string">'action'</span>,
        <span class="hljs-attr">width</span>: <span class="hljs-string">'10%'</span>,
        <span class="hljs-attr">align</span>: <span class="hljs-string">'center'</span>,
        <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">_, row</span>) =></span> &#123;
          <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><></span>
              <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"link"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> handleEdit(row)&#125;>
                编辑
              <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">Popconfirm</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"确认要删除?"</span> <span class="hljs-attr">onConfirm</span>=<span class="hljs-string">&#123;()</span> =></span> handleDelete(row)&#125;>
                <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"link"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">Popconfirm</span>></span>
            <span class="hljs-tag"></></span></span>
          );
        &#125;
      &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们期望的是操作列也可以像表格的<code>columns</code>一样通过配置来生成，而不是写<code>jsx</code>。看一下如何封装呢？</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 定义操作按钮</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> IAction <span class="hljs-keyword">extends</span> Omit<ButtonProps, 'onClick'> &#123;
  <span class="hljs-comment">// 自定义按钮渲染</span>
  render?: <span class="hljs-function">(<span class="hljs-params">row: <span class="hljs-built_in">any</span>, index: <span class="hljs-built_in">number</span></span>) =></span> React.ReactNode;
  onClick?: <span class="hljs-function">(<span class="hljs-params">row: <span class="hljs-built_in">any</span>, index: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>;
  <span class="hljs-comment">// 是否有确认提示</span>
  confirm?: <span class="hljs-built_in">boolean</span>;
  <span class="hljs-comment">// 提示文字</span>
  confirmText?: <span class="hljs-built_in">boolean</span>;
  <span class="hljs-comment">// 按钮显示文字</span>
  text: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-comment">// 定义表格列</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> IColumn<T = any> <span class="hljs-keyword">extends</span> ColumnType<T> &#123;
  actions?: IAction[];
&#125;

<span class="hljs-comment">// 然后我们可以定义一个hooks,专门用来修改表格的columns,添加操作列</span>
<span class="hljs-keyword">const</span> useActionButtons = (
  columns: IColumn[],
  <span class="hljs-attr">actions</span>: IAction[] | <span class="hljs-literal">undefined</span>
): IColumn[] => &#123;
  <span class="hljs-keyword">return</span> useMemo(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (!actions || actions.length === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">return</span> columns;
    &#125;
    <span class="hljs-keyword">return</span> [
      ...columns,
      &#123;
        <span class="hljs-attr">align</span>: <span class="hljs-string">'center'</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'操作'</span>,
        <span class="hljs-attr">key</span>: <span class="hljs-string">'__action'</span>,
        <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'__action'</span>,
        <span class="hljs-attr">width</span>: <span class="hljs-built_in">Math</span>.max(<span class="hljs-number">120</span>, actions.length * <span class="hljs-number">85</span>),
        <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">value: <span class="hljs-built_in">any</span>, row: <span class="hljs-built_in">any</span>, index: <span class="hljs-built_in">number</span></span>)</span> &#123;
          <span class="hljs-keyword">return</span> actions.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (item.render) &#123;
              <span class="hljs-keyword">return</span> item.render(row, index);
            &#125;
            <span class="hljs-keyword">if</span>(item.confirm) &#123;
              <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Popconfirm</span> <span class="hljs-attr">title</span>=<span class="hljs-string">&#123;item.confirmText</span>  || '确认要删除?'&#125;
                       <span class="hljs-attr">onConfirm</span>=<span class="hljs-string">&#123;()</span> =></span> item.onClick?.(row, index)&#125;>
                <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"link"</span>></span>&#123;item.text&#125;<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">Popconfirm</span>></span></span>
            &#125;
            <span class="hljs-keyword">return</span> (
              <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span>
                &#123;<span class="hljs-attr">...item</span>&#125;
                <span class="hljs-attr">type</span>=<span class="hljs-string">"link"</span>
                <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.text&#125;</span>
                <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> item.onClick?.(row, index)&#125;
              >
                &#123;item.text&#125;
              <span class="hljs-tag"></<span class="hljs-name">Button</span>></span></span>
            );
          &#125;);
        &#125;
      &#125;
    ];
  &#125;, [columns, actions, actionFixed]);
&#125;;

<span class="hljs-comment">// 最后我们对表格再做一个封装</span>
<span class="hljs-keyword">const</span> CustomTable: React.FC<ITableProps> = <span class="hljs-function">(<span class="hljs-params">&#123;
  actions,
  columns,
  ...props
&#125;</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> actionColumns = useActionColumns(columns,actions)
  <span class="hljs-comment">// 渲染表格</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的封装，我们再使用表格的时候，就可以这样去写</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">  <span class="hljs-keyword">const</span> actions: IAction[] = [
    &#123;
      <span class="hljs-attr">text</span>: <span class="hljs-string">'编辑'</span>,
      <span class="hljs-attr">onClick</span>: handleModifyRecord,
    &#125;,
  ];

<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">CustomTable</span> <span class="hljs-attr">actions</span>=<span class="hljs-string">&#123;actions&#125;</span> <span class="hljs-attr">columns</span>=<span class="hljs-string">&#123;columns&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">CustomTable</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">避免重复渲染</h3>
<p>重复渲染，包含重复计算，重复发请求等等，这个在开发中很容易遇到。比如某一个页面代码的时候，某个接口被调用了两次，对于这种情况，我们还是需要去尽量避免的。</p>
<p>先看一下下面几个示例代码</p>
<h5 data-id="heading-10">示例一</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  useEffect(<span class="hljs-function">() =></span> &#123;
    setCount(<span class="hljs-number">1</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      setCount(<span class="hljs-number">0</span>);
    &#125;, <span class="hljs-number">1000</span>);
  &#125;, [count]);

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">示例二</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">//组件</span>
<span class="hljs-keyword">import</span> React, &#123; useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">const</span> Test = <span class="hljs-function">() =></span> &#123;
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'此处发送请求'</span>);
  &#125;, []);

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Test;

<span class="hljs-comment">// 页面</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
   <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
   useEffect(<span class="hljs-function">() =></span> &#123;
     <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
       setCount(<span class="hljs-number">1</span>)
     &#125;,<span class="hljs-number">0</span>)
   &#125;,[])
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><></span>
    <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"test"</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;()</span> =></span> <span class="hljs-tag"><<span class="hljs-name">Test</span>></span><span class="hljs-tag"></<span class="hljs-name">Test</span>></span>&#125; />
    <span class="hljs-tag"></></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">示例三</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [pageSize, setPageSize] = useState(<span class="hljs-number">10</span>);
  <span class="hljs-keyword">const</span> [currentPage, setCurrentPage] = useState(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">const</span> [update, setUpdate] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [appCode, setAppCode] = useState(<span class="hljs-string">''</span>);
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'发送请求'</span>);
  &#125;, [pageSize, currentPage, update]);

  <span class="hljs-comment">// 当 appCode 值发生变化时，修改 update 从而重新请求数据</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    setUpdate(update + <span class="hljs-number">1</span>);
  &#125;, [appCode]);

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请问，上面三个示例存在什么问题呢？</p>
<p>第一个：会导致死循环</p>
<p>第二个：进入页面会发送两次请求</p>
<p>第三个：进入页面会发送两次请求</p>
<p>接下来我们来逐一分析原因</p>
<h5 data-id="heading-13">分析示例一</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx">useEffect(<span class="hljs-function">() =></span> &#123;
    setCount(<span class="hljs-number">1</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      setCount(<span class="hljs-number">0</span>);
    &#125;, <span class="hljs-number">1000</span>);
  &#125;, [count]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码为示例一中的<code>useEffect</code>,可以看到<code>useEffect</code>监听的是<code>count</code>的变化，而且里面有一个<code>setTimeout</code>会每一秒钟修改一次<code>count</code>的值，而<code>count</code>的变化又会导致<code>useEffect</code>重新被执行，然后就进入了死循环。那么应该如何解决呢？方法就是<code>useEffect</code>不要去监听<code>count</code>的变化。即改为</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">useEffect(<span class="hljs-function">() =></span> &#123;
    setCount(<span class="hljs-number">1</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      setCount(<span class="hljs-number">0</span>);
    &#125;, <span class="hljs-number">1000</span>);
  &#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">分析示例二</h5>
<p>示例二关键问题在于下面这段代码</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Route exact key=<span class="hljs-string">"test"</span> path=<span class="hljs-string">"/"</span> component=&#123;<span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Test</span>></span><span class="hljs-tag"></<span class="hljs-name">Test</span>></span></span>&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在代码中，<code>count</code>的值初始化为<code>1</code>,然后一秒钟后被修改为<code>0</code>, 这会导致<code>App</code>组件产生两次渲染，注意上面的代码<code>component</code>传入的参数是一个箭头函数，而两次渲染会导致初始化两个箭头函数，这就导致两次给<code>Route</code>传入的<code>component</code>是不一样的，从而产生两次渲染，<code>Test</code>组件也就被渲染了两次，从而内部 的请求发送了两次。如何去修改呢？</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Route exact key=<span class="hljs-string">"test"</span> path=<span class="hljs-string">"/"</span> component=&#123;Test&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">分析示例三</h5>
<p>示例三中为了在<code>appCode</code>发生变化时重新请求数据，然后加了一个<code>update</code>属性，通过调整这个属性来触发<code>useEffect</code>执行，但是问题就在于下面这段代码</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">  <span class="hljs-comment">// 当 appCode 值发生变化时，修改 update 从而重新请求数据</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    setUpdate(update + <span class="hljs-number">1</span>);
  &#125;, [appCode]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化页面的时候，<code>useEffect</code>会被默认执行一遍，所以初始化的时候会发送一个请求，同时上面的<code>useEffect</code>也会被执行，这时候<code>update</code>发生变化了，所以又会导致请求再发送一次，如何调整呢？</p>
<p>其实完全不需要<code>update</code>,直接在下面代码监听<code>appCode</code>就好了</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'发送请求'</span>);
  &#125;, [pageSize, currentPage, appCode]);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            