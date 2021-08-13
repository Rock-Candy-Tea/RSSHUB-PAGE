
---
title: '日常优化，React 避免不必要的重复渲染'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d70297eaf0a242f0869c84b81d0ce963~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 17:08:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d70297eaf0a242f0869c84b81d0ce963~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>大家在用 React 开发时，有没有遇到过这样的问题“<strong>我们有时候只想更新单个组件，却触发了大量无关组件的渲染</strong>”，正常情况，我们只想重新渲染有数据变化的组件，而不涉及其他无关组件。所以我们需要避免无效的重复渲染，毕竟 React 的协调成本很昂贵。</p>
<p>在 React 中性能问题有两类，长列表和重复渲染。长列表指的是你的页面渲染了很长的列表，通常有上百、上千甚至几千行数据。长列表本身不是 React 框架特有的问题，无论是什么技术栈，都可能遇到。它的通用解决方案是采用虚拟滚动，业界做得比较好的解决方案有 react-virtualized 和 react-window，已经非常成熟了。</p>
<p>那对于重复渲染有没有好的解决方案了，今天我们就一起来看看吧。</p>
<h2 data-id="heading-1">1. 定位小工具</h2>
<p>为大家介绍一个 React 中常用的小工具 React Developer Tools。通过 React Developer Tools 中的 Profiler 分析组件渲染次数、开始时间及耗时。React Profiler 的详细使用方式建议阅读官方文档：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh-hans.reactjs.org%2Fblog%2F2018%2F09%2F10%2Fintroducing-the-react-profiler.html" target="_blank" rel="nofollow noopener noreferrer" title="https://zh-hans.reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html" ref="nofollow noopener noreferrer">zh-hans.reactjs.org/blog/2018/0…</a></p>
<p>如果你已经知道这个小工具 <strong>React Developer Tools</strong> 的使用，请跳过这一小节。</p>
<p>在工具的设置中，开启【<strong>Highlight updates when components render.</strong>】，当我们组建渲染了，会在页面中高亮显示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d70297eaf0a242f0869c84b81d0ce963~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23bd8c2af7144a47ab5487bd2664a696~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>或者你可以开发录制功能，在页面操作完之后，会看到相应的渲染情况，不渲染的内容，会直接标记为 <strong>Did not render</strong>。重复渲染的内容可直接查看渲染耗时等消息。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/185546c921c6446681a57ea0839e4e83~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>react-dom 16.5+ 在 DEV 模式下支持性能分析。在生产环境也可以使用 react-dom/profiling 代码包进行性能分析， 查阅 fb.me/react-profiling 了解更多如何使用这个代码包。</p>
</blockquote>
<h2 data-id="heading-2">2. 一个测试例子</h2>
<p>下面的代码是一个简单的示例代码（示例代码来源于网络代码），功能很简单表格的上移下移，</p>
<ul>
<li>List，组件用于展示列表，执行上下移动的逻辑；</li>
<li>ListItem，也就是列表中展示的行，渲染每行的内容。</li>
</ul>
<p>列子测试代码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Ftest-reset-pddm7%3Ffile%3D%2Fsrc%2FApp.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/test-reset-pddm7?file=/src/App.js" ref="nofollow noopener noreferrer">codesandbox.io/s/test-rese…</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">const</span> initListData = [];

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
  initListData.push(&#123; <span class="hljs-attr">text</span>: i, <span class="hljs-attr">id</span>: i &#125;);
&#125;

<span class="hljs-keyword">const</span> ListItem = <span class="hljs-function">(<span class="hljs-params">&#123; text, onMoveUp, onMoveDown, index &#125;</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;text&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> onMoveUp(index)&#125;>上移<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> onMoveDown(index)&#125;>下移<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">List</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">listData</span>: initListData
  &#125;;

  handleMoveUp = <span class="hljs-function">(<span class="hljs-params">index</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> _listData = [...this.state.listData];
    <span class="hljs-comment">// 部分实现</span>
    <span class="hljs-keyword">if</span> (index === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">const</span> data = _listData.shift();
      _listData.push(data);
      <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">listData</span>: _listData
      &#125;);
    &#125;
  &#125;;

  handleMoveDown = <span class="hljs-function">(<span class="hljs-params">index</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> _listData = [...this.state.listData];
    <span class="hljs-comment">// 部分实现</span>
    <span class="hljs-keyword">if</span> (index === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">const</span> data = _listData.pop();
      _listData.unshift(data);
      <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">listData</span>: _listData
      &#125;);
    &#125;
  &#125;;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; listData &#125; = <span class="hljs-built_in">this</span>.state;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        &#123;listData.map((&#123; text, id &#125;, index) => (
          <span class="hljs-tag"><<span class="hljs-name">ListItem</span>
            <span class="hljs-attr">text</span>=<span class="hljs-string">&#123;text&#125;</span>
            <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;index&#125;</span>
            <span class="hljs-attr">onMoveUp</span>=<span class="hljs-string">&#123;this.handleMoveUp&#125;</span>
            <span class="hljs-attr">onMoveDown</span>=<span class="hljs-string">&#123;this.handleMoveDown&#125;</span>
          /></span>
        ))&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">List</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们执行列表行的上下移动时，发现当操作一行，整个 ListItem 的<strong>其他行也会被重新渲染</strong>。如文章开始说道，我们只想重新渲染有数据变化的组件，而不涉及其他无关组件，毕竟 React 的协调成本很昂贵。 那如何避免不必要的重复渲染了，接着往下看。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3baf55bdbea46e09e63fe4af1cb9cf6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">3. React.memo</h2>
<p>在 React16.6 加入的一个专门用来优化 函数组件 (Functional Component)性能的方法: <strong>React.memo</strong>。React.memo() 是一个高阶函数，它与 React.PureComponent 类似，但是一个函数组件而非一个类。</p>
<p>为 ListItem 添加 React.memo 就可以阻止每行内容重新渲染。如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ListItem =  React.memo(<span class="hljs-function">(<span class="hljs-params">&#123; text, onMoveUp, onMoveDown, index &#125;</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;text&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> onMoveUp(index)&#125;>上移<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> onMoveDown(index)&#125;>下移<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
));
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c1bf3a734f240a68ffcfaecc417293e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>发现加上 React.memo 之后，并不是每一行都会渲染。但是 React.memo 是通过<strong>浅比较</strong>的方式对比变化前后的 props 与 state，但是这种方式很容易失效，那就是使用<strong>箭头函</strong>数。箭头函数在每次调用 render 时都会动态生成一个新的函数，函数的引用变化了，这时即便使用 React.memo 也是无效的，所以大家在使用的时候要注意。作者也会经常的使用箭头函数来写，但是这其实是一种不好的习惯，比较好的书写方式是将整个函数提取为一个类属性的函数。</p>
<p>当然如果你使用的 React Hooks，你可以使用 useMemo，useMemo 被称为更加精细的 memo。React.memo 是对组件级别的重新渲染进行管控。React.useMemo 是对组件的某个或者几个部分的重渲染进行管控。React.memo 控制是否需要重渲染一个组件，而 useMemo 控制的则是是否需要重复执行某一段逻辑。</p>
<h2 data-id="heading-4">4. PureComponent</h2>
<p>PureComponent 它内置了对 shouldComponentUpdate 的实现：PureComponent 将会在 shouldComponentUpdate 中对组件更新前后的 props 和 state 进行浅比较，并根据浅比较的结果，决定是否需要继续更新流程。还有 PureComponent 有和 React.memo 一样的尿性很容易失效，那就是使用箭头函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ListItem</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">PureComponent</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; text, onChange, index &#125; = <span class="hljs-built_in">this</span>.props;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;text&#125;</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;text&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> onChange(index)&#125;>修改 text <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5287b58fbc0480683509a3b55d50b7e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">5. ImmutableJS-不可变数据</h2>
<p><strong>React.memo</strong>、<strong>PureComponent</strong>、<strong>PureRenderMixin</strong>都是用过浅比较的方式来对比变化前后的 props 与 state。它们只能针对值类型数据对比其值是否相等，而针对数组、对象等引用类型的数据对比时只会对比它的引用。这样的话比较的时候就不会太准确。</p>
<ul>
<li>如果数据内容没有变，但是数据的引用改变了，浅比较仍然会认为“数据发生了变化”，进而触发一次不必要的更新，导致过度渲染；</li>
<li>如果深层嵌套，数据内容改变，引用没变，浅比较则会认为“数据没有发生变化”，进而阻断一次更新，导致不渲染。
而 ImmutableJS 可以保证修改操作返回一个新引用，并且只修改需要修改的节点。Immutable 的结构不可变性&&结构共享性，能够快速进行数据的比较:</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCompare</span>(<span class="hljs-params">instance, nextProps, nextState</span>) </span>&#123;
  <span class="hljs-keyword">return</span> !Immutable.is(instance.props, nextProps) ||
    !Immutable.is(instance.state, nextState);
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ListItem</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">shouldComponentUpdate</span>(<span class="hljs-params">nextProps, nextState</span>)</span> &#123;
    <span class="hljs-keyword">return</span> deepCompare(<span class="hljs-built_in">this</span>, nextProps, nextState);
  &#125;;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; text, onChange, index &#125; = <span class="hljs-built_in">this</span>.props;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;text&#125;</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;text&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> onChange(index)&#125;>修改 text <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然 ImmutableJS 可以在某些情况解决重复渲染，但是如果需要频繁地与服务器交互，那么 Immutable 对象就需要不断地与原生 js 进行转换，操作起来显得很繁琐，并且这种方案某种层面上来说有一定心智成本。所以如今 immerjs 更为流行。</p>
<h2 data-id="heading-6">6. reselect-缓存</h2>
<p>reselect 会将输入与输出建立映射，缓存函数产出结果。只要输入一致，那么会直接吐出对应的输出结果，从而保证计算结果不变，以此来保证不会被破防。这种方式是通过缓存，使用 reselect 缓存函数执行结果，来避免产生新的对象。小编本人多这种方案了解不深，也没有使用过，但是如果你有兴趣可以自己去尝试一下。</p>
<p>github: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fgarylesueur%2Freselect" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/garylesueur/reselect" ref="nofollow noopener noreferrer">github.com/garylesueur…</a></p>
<h2 data-id="heading-7">7. 手动控制</h2>
<p>自己手动控制，通过使用 shouldComponentUpdate API 来处理，但是 shouldComponentUpdate 可能会带来意想不到的 Bug，所以这个方案应该放到最后考虑。而且这种方法仅限于类组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ListItem</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">shouldComponentUpdate</span>(<span class="hljs-params">nextProps, nextState</span>)</span> &#123;
    <span class="hljs-keyword">if</span>(nextProps.text === <span class="hljs-built_in">this</span>.props.text) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; text, onChange, index &#125; = <span class="hljs-built_in">this</span>.props;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;text&#125;</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;text&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> onChange(index)&#125;>修改 text <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">使用前</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb28ece692d948e98cd08b2d9a900de6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">使用后</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acae00109592458f9a38af37f0f2d866~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">总结</h2>
<p>避免重复渲染常用的解决方案是使用 PureComponent 或者使用 React.memo（useMemo） 等组件缓存 API，减少重新渲染。但错误的使用方式会使其完全无效，比如使用箭头函数或者每次都生成新的对象，那基本就是做了无用功。针对这些问题，使用 ImmutableJS、immerjs 转换数据结构或者 reselect 缓存函数执行结果 都可以解决。亦或者自己手动控制，自己实现 shouldComponentUpdate 函数，但这类方案一般不推荐，因为容易带来意想不到的 Bug，可以作为保底手段使用。</p>
<p>码字不易，如果对你有帮助，帮忙点个赞吧。</p>
<h2 data-id="heading-11">参考</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FSunday97%2Farticle%2Fdetails%2F116117308" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/Sunday97/article/details/116117308" ref="nofollow noopener noreferrer">blog.csdn.net/Sunday97/ar…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fgarylesueur%2Freselect" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/garylesueur/reselect" ref="nofollow noopener noreferrer">github.com/garylesueur…</a></li>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fzhenhua-lee.github.io%2Freact%2FImmutable.html" target="_blank" rel="nofollow noopener noreferrer" title="http://zhenhua-lee.github.io/react/Immutable.html" ref="nofollow noopener noreferrer">zhenhua-lee.github.io/react/Immut…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fkaiwu.lagou.com%2Fcourse%2FcourseInfo.htm%3FcourseId%3D566%23%2Fdetail%2Fpc%3Fid%3D5804" target="_blank" rel="nofollow noopener noreferrer" title="https://kaiwu.lagou.com/course/courseInfo.htm?courseId=566#/detail/pc?id=5804" ref="nofollow noopener noreferrer">kaiwu.lagou.com/course/cour…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Freselect" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/reselect" ref="nofollow noopener noreferrer">www.npmjs.com/package/res…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fgarylesueur%2Freselect" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/garylesueur/reselect" ref="nofollow noopener noreferrer">github.com/garylesueur…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh-hans.reactjs.org%2Fblog%2F2018%2F09%2F10%2Fintroducing-the-react-profiler.html" target="_blank" rel="nofollow noopener noreferrer" title="https://zh-hans.reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html" ref="nofollow noopener noreferrer">zh-hans.reactjs.org/blog/2018/0…</a></li>
</ul></div>  
</div>
            