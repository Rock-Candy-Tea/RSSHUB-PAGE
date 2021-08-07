
---
title: 'React 最佳实践：集成第三方库（D3.js）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e8522d0a0cf483a8c79af982d5c620a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 08:26:24 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e8522d0a0cf483a8c79af982d5c620a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>React 提供了声明式方式，让我们可以更方便清晰的描述 UI ，但是，<strong>对于需要依赖真实 DOM 节点的第三方 js 库，例如 D3.js，我们又该怎么在 React 组件中使用呢</strong>？我们至少要思考以下三点：</p>
<ul>
<li>
<p>Q：如何获取原生 DOM 节点？</p>
<p>A：使用 <strong><code>ref</code></strong> 获取原生 DOM 节点引用。</p>
</li>
<li>
<p>Q：如何更新原生 DOM 节点上的组件状态？</p>
<p>A：手动更新，React 只会维护虚拟 DOM 节点上的组件状态。</p>
</li>
<li>
<p>需要注意，在组件销毁时移除原生节点上的 DOM 事件。</p>
</li>
</ul>
<p>我们以 <code>D3.js</code> 作为例子，具体聊聊～</p>
<h2 data-id="heading-0">D3.js 是什么？</h2>
<p><code>D3</code>（<code>Data-Driven Documents</code> 或 <code>D3.js</code>）是一个非常著名的画图的 <code>JavaScript</code> 库，用于使用 <code>Web</code> 标准将数据可视化。它是必须要对底层的 <code>DOM</code> 节点进行操作的，这也是选择 <code>D3.js</code> 的其中原因；其次，它数据驱动的属性和 React 也十分类似。</p>
<p>目前也有基于 <code>D3.js</code> 封装的 React 库，一般来说功能会收到限制，肯定不如直接使用 <code>D3.js</code> 得到的功能更完备。掌握 <code>D3.js</code> 在 React 中的使用，对于开发可视化会有很大的帮助。</p>
<h2 data-id="heading-1">创建一个仿真力模型</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e8522d0a0cf483a8c79af982d5c620a~tplv-k3u1fbpfcp-watermark.image" alt="d3-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每个节点（Node）都是可以拖动的，并且有一个力反馈的效果。用户可以为中间的圈手动添加新的节点（Node）。</p>
<h3 data-id="heading-2">安装</h3>
<ul>
<li>yarn</li>
</ul>
<pre><code class="copyable">yarn add d3
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>npm</li>
</ul>
<pre><code class="copyable">npm install d3
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">类组件实现</h3>
<h4 data-id="heading-4">创建（componentDidMount）</h4>
<p>首页，我们定义了一组初始数据，包括节点（nodes）和节点之间的关系（links）：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"nodes"</span>: [
    &#123;
      <span class="hljs-attr">"id"</span>: <span class="hljs-string">"id1"</span>,
      <span class="hljs-attr">"group"</span>: <span class="hljs-number">1</span>
    &#125;,
    &#123;
      <span class="hljs-attr">"id"</span>: <span class="hljs-string">"id2"</span>,
      <span class="hljs-attr">"group"</span>: <span class="hljs-number">2</span>
    &#125;,
    &#123;
      <span class="hljs-attr">"id"</span>: <span class="hljs-string">"id3"</span>,
      <span class="hljs-attr">"group"</span>: <span class="hljs-number">3</span>
    &#125;,
    &#123;
      <span class="hljs-attr">"id"</span>: <span class="hljs-string">"id4"</span>,
      <span class="hljs-attr">"group"</span>: <span class="hljs-number">4</span>
    &#125;
  ],
  <span class="hljs-attr">"links"</span>: [
    &#123;
      <span class="hljs-attr">"source"</span>: <span class="hljs-string">"id1"</span>,
      <span class="hljs-attr">"target"</span>: <span class="hljs-string">"id2"</span>,
      <span class="hljs-attr">"value"</span>: <span class="hljs-number">1</span>
    &#125;,
    &#123;
      <span class="hljs-attr">"source"</span>: <span class="hljs-string">"id1"</span>,
      <span class="hljs-attr">"target"</span>: <span class="hljs-string">"id3"</span>,
      <span class="hljs-attr">"value"</span>: <span class="hljs-number">1</span>
    &#125;,
    &#123;
      <span class="hljs-attr">"source"</span>: <span class="hljs-string">"id1"</span>,
      <span class="hljs-attr">"target"</span>: <span class="hljs-string">"id4"</span>,
      <span class="hljs-attr">"value"</span>: <span class="hljs-number">1</span>
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 d3 而言，它需要一个 DOM Node 作为画图区域。 在 React 中，可以通过 <code>ref</code> 得到对组件真正实例的引用，ref 属性可以设置为一个回调函数，这也是官方强烈推荐的用法：</p>
<ul>
<li>
<p>组件被挂载后，回调函数被立即执行，回调函数的参数为该组件的具体实例。</p>
</li>
<li>
<p>组件被卸载或者原有的 ref 属性本身发生变化时，回调也会被立即执行，此时回调函数参数为 null，以确保内存泄露。</p>
</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// d3Node 作为我们的画图区域</span>
<div className=<span class="hljs-string">"d3-node"</span> ref=&#123;<span class="hljs-function">(<span class="hljs-params">node</span>) =></span> (<span class="hljs-built_in">this</span>.d3Node = node)&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件挂载完成后，也就是 componentDidMount，d3Node 会初始化一个 svg（包括长宽背景色等样式和一个力学仿真空间）。<code>linksGroup</code> 是线条的存放容器，<code>nodesGroup</code> 是节点的存放容器。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.svg = d3
  .select(<span class="hljs-built_in">this</span>.d3Node)
  .append(<span class="hljs-string">'svg'</span>)
  .attr(<span class="hljs-string">'width'</span>, width)
  .attr(<span class="hljs-string">'height'</span>, height);
<span class="hljs-built_in">this</span>.color = d3.scaleOrdinal(d3.schemeCategory10);
<span class="hljs-built_in">this</span>.simulation = d3
  .forceSimulation()
  .force(
    <span class="hljs-string">'link'</span>,
    d3.forceLink().id(<span class="hljs-function">(<span class="hljs-params">d</span>) =></span> d.id),
  )
  .force(<span class="hljs-string">'charge'</span>, d3.forceManyBody())
  .force(<span class="hljs-string">'center'</span>, d3.forceCenter(width / <span class="hljs-number">2</span>, height / <span class="hljs-number">2</span>));

<span class="hljs-built_in">this</span>.linksGroup = <span class="hljs-built_in">this</span>.svg.append(<span class="hljs-string">'g'</span>);
<span class="hljs-built_in">this</span>.nodesGroup = <span class="hljs-built_in">this</span>.svg.append(<span class="hljs-string">'g'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于数据渲染的逻辑，在首次绘制和后续更新中是一样的，所以我们可以共用这部分的代码，画图的主要逻辑就是 <strong>有多少个 node 就画多少个圈，他们之间的关系有 line 连接</strong>，关于 node 的位置由 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxswei%2Fd3-force%2Fblob%2Fmaster%2FREADME.md%23_force" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xswei/d3-force/blob/master/README.md#_force" ref="nofollow noopener noreferrer">d3.force API</a> 自动生成：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">updateDiagrarm</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; data &#125; = <span class="hljs-built_in">this</span>.state;
    <span class="hljs-keyword">let</span> link = <span class="hljs-built_in">this</span>.linksGroup
      .attr(<span class="hljs-string">'class'</span>, <span class="hljs-string">'links'</span>)
      .selectAll(<span class="hljs-string">'line'</span>)
      .data(data.links);
    link.exit().remove();
    link = link
      .enter()
      .append(<span class="hljs-string">'line'</span>)
      .attr(<span class="hljs-string">'stroke-width'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">d</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.sqrt(d.value);
      &#125;)
      .merge(link);

    <span class="hljs-keyword">let</span> node = <span class="hljs-built_in">this</span>.nodesGroup
      .attr(<span class="hljs-string">'class'</span>, <span class="hljs-string">'nodes'</span>)
      .selectAll(<span class="hljs-string">'circle'</span>)
      .data(data.nodes);
    node.exit().remove();
    node = node
      .enter()
      .append(<span class="hljs-string">'circle'</span>)
      .attr(<span class="hljs-string">'r'</span>, <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> (d.id === <span class="hljs-string">'id1'</span> ? <span class="hljs-number">24</span> : <span class="hljs-number">16</span>))
      .attr(<span class="hljs-string">'fill'</span>, <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.color(d.group);
      &#125;)
      .call(
        d3
          .drag()
          .on(<span class="hljs-string">'start'</span>, <span class="hljs-built_in">this</span>.dragstarted)
          .on(<span class="hljs-string">'drag'</span>, <span class="hljs-built_in">this</span>.dragged)
          .on(<span class="hljs-string">'end'</span>, <span class="hljs-built_in">this</span>.dragended),
      )
      .merge(node);

    <span class="hljs-built_in">this</span>.simulation.nodes(data.nodes).on(<span class="hljs-string">'tick'</span>, ticked);

    <span class="hljs-built_in">this</span>.simulation.force(<span class="hljs-string">'link'</span>).links(data.links).distance(<span class="hljs-number">100</span>);

    <span class="hljs-built_in">this</span>.simulation.alpha(<span class="hljs-number">1</span>).restart();

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ticked</span>(<span class="hljs-params"></span>) </span>&#123;
      link
        .attr(<span class="hljs-string">'stroke'</span>, <span class="hljs-string">'#c7c7c7'</span>)
        .attr(<span class="hljs-string">'x1'</span>, <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> d.source.x)
        .attr(<span class="hljs-string">'y1'</span>, <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> d.source.y)
        .attr(<span class="hljs-string">'x2'</span>, <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> d.target.x)
        .attr(<span class="hljs-string">'y2'</span>, <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> d.target.y);

      node.attr(<span class="hljs-string">'cx'</span>, <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> d.x).attr(<span class="hljs-string">'cy'</span>, <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> d.y);
    &#125;
  &#125;

  dragstarted = <span class="hljs-function">(<span class="hljs-params">event, d</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!event.active) <span class="hljs-built_in">this</span>.simulation.alphaTarget(<span class="hljs-number">0.3</span>).restart();
    d.fx = d.x;
    d.fy = d.y;
  &#125;;
  dragged = <span class="hljs-function">(<span class="hljs-params">event, d</span>) =></span> &#123;
    d.fx = event.x;
    d.fy = event.y;
  &#125;;
  dragended = <span class="hljs-function">(<span class="hljs-params">event, d</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!event.active) <span class="hljs-built_in">this</span>.simulation.alphaTarget(<span class="hljs-number">0</span>);
    d.fx = <span class="hljs-literal">null</span>;
    d.fy = <span class="hljs-literal">null</span>;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">更新（componentDidUpdate）</h4>
<p>基于 D3 数据驱动这个性质，新增 Node 的行为就是为 data 新增 node 和新 node 的对应关系：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">handleAddNode = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> id = <span class="hljs-string">`id<span class="hljs-subst">$&#123;<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()&#125;</span>`</span>;
  <span class="hljs-keyword">const</span> node = &#123; id, <span class="hljs-attr">group</span>: _.random(<span class="hljs-number">1</span>, <span class="hljs-number">9</span>) &#125;;
  <span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">nodes</span>: [...this.state.data.nodes, node],
      <span class="hljs-attr">links</span>: [
        ...this.state.data.links,
        &#123; <span class="hljs-attr">source</span>: <span class="hljs-string">'id1'</span>, <span class="hljs-attr">target</span>: id, <span class="hljs-attr">value</span>: <span class="hljs-number">1</span> &#125;,
      ],
    &#125;,
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，<code>React</code> 只会管理到 <code>d3Node</code> 层，<code>d3Node</code> 以下的内容都是我们手动管理的，所以在 <code>componentDidUpdate</code> 中，我们添加更新逻辑：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params">prevProps, prevState</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state.data !== prevState.data) <span class="hljs-built_in">this</span>.updateDiagrarm();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">销毁</h4>
<p>在这个例子中，因为没有为真实 Dom 绑定额外的事件，在组件销毁之后，React 会移除 d3Node 这个节点的同时，也会移除 d3Node 下的所有内容。</p>
<h3 data-id="heading-7">函数组件实现</h3>
<p>React Hooks 中的画图逻辑和类组件中是一样的。</p>
<ul>
<li>
<p>初始化 Svg</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// initSvg</span>
&#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在 data 变化时，更新视图</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// updateDiagrarm</span>
&#125;, [data]);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>在实践的时候，发现有两个坑需要防一下：</p>
<ul>
<li>
<p>避免重复绘图，为 <code>useEffect</code> 添加第二个参数 <code>[]</code>，并不能完全避免这个问题，我们可以再加一层判断：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> checkElementExist = <span class="hljs-function">(<span class="hljs-params">element</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (element) &#123;
    element.remove();
  &#125;
&#125;;
checkElementExist(getSvg().selectAll(<span class="hljs-string">'svg'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>useState</code> 必须要执行完 <code>react</code> 整个生命周期才会获取最新值，这就导致在生命周期结束前无法操作新建的 Dom 节点。其实我们也不需要通过 useState 来自动更新视图，这里可以用 useRef 代替。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> color = useRef(<span class="hljs-literal">null</span>);
<span class="hljs-keyword">const</span> simulation = useRef(<span class="hljs-literal">null</span>);
<span class="hljs-keyword">const</span> linksGroup = useRef(<span class="hljs-literal">null</span>);
<span class="hljs-keyword">const</span> nodesGroup = useRef(<span class="hljs-literal">null</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-8">完整代码</h2>
<p>想自己上手跑一跑的朋友，可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpinkqq%2Freact-antd%2Ftree%2Fmain%2Fsrc%2Fpages%2Fd3" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pinkqq/react-antd/tree/main/src/pages/d3" ref="nofollow noopener noreferrer">戳这里</a></p>
<h2 data-id="heading-9">React 最佳实践</h2>
<ul>
<li><a href="https://juejin.cn/post/6993154734580301832" target="_blank" title="https://juejin.cn/post/6993154734580301832">React 最佳实践：如何实现原生对话框（Portals）</a></li>
<li><a href="https://juejin.cn/post/6992833914104463367" target="_blank" title="https://juejin.cn/post/6992833914104463367">React 最佳实践：可拖拽侧边栏</a></li>
<li><a href="https://juejin.cn/post/6992408029308289054/" target="_blank" title="https://juejin.cn/post/6992408029308289054/">React 最佳实践：基于路由实现分步操作</a></li>
<li><a href="https://juejin.cn/post/6992030786358607879" target="_blank" title="https://juejin.cn/post/6992030786358607879">React 最佳实践：处理多个数据源</a></li>
<li><a href="https://juejin.cn/post/6991665381790203912" target="_blank" title="https://juejin.cn/post/6991665381790203912">React 最佳实践：完成一个列表需求叭</a></li>
<li><a href="https://juejin.cn/post/6991306379956846606" target="_blank" title="https://juejin.cn/post/6991306379956846606">React 最佳实践：动态表单</a></li>
</ul></div>  
</div>
            