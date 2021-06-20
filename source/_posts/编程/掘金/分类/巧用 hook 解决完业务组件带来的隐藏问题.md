
---
title: '巧用 hook 解决完业务组件带来的隐藏问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://github.com/AngelPP52/blog/raw/main/ES/%E5%85%88%E9%80%89%E4%B8%AD%E5%90%8E%E5%9B%9E%E8%BD%A6.gif'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 19:27:45 GMT
thumbnail: 'https://github.com/AngelPP52/blog/raw/main/ES/%E5%85%88%E9%80%89%E4%B8%AD%E5%90%8E%E5%9B%9E%E8%BD%A6.gif'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>模糊搜索组件（后面称 <code>ES</code> 组件）是整个团队一个十分常用的业务组件。几乎每一个列表页，都离不开搜索功能。然而，就算我们已经对这个业务组件做了尽可能完善的封装，却还是在组件繁多的回调以及复杂的业务要求中重复踩了很多的坑。</p>
<p>而这一次后，我再也不想听到 QA 因为 <code>ES</code> 搜索出现了前端的问题而找到我。</p>
<blockquote>
<p>本次分享所需的代码，可配合文章一起服用：<a href="https://git.garena.com/shopee/bg-logistics/wms-lite/wms-lite-fe/-/tree/master/src/hooks" target="_blank" rel="nofollow noopener noreferrer">git.garena.com/shopee/bg-l…</a></p>
</blockquote>
<p>那么，在开始正文之前，需要大家对我们以前的回调代码有一个初步的认识。注意请不要看完所有代码，有个整体的了解即可。</p>
<blockquote>
<p><code>EsSearch</code> 组件。</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// ES搜索1</span>
<span style=&#123;&#123; <span class="hljs-attr">marginRight</span>: <span class="hljs-number">8</span> &#125;&#125;>&#123;translate(<span class="hljs-string">'filtersku.product'</span>)&#125;</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">EsSearch</span>
  <span class="hljs-attr">url</span>=<span class="hljs-string">&#123;</span>`/<span class="hljs-attr">api</span>/<span class="hljs-attr">es</span>/<span class="hljs-attr">autocomplete</span>/<span class="hljs-attr">product_name</span>?<span class="hljs-attr">include_delete</span>=<span class="hljs-string">$&#123;includeDelete&#125;</span>`&#125;
  <span class="hljs-attr">esDocName</span>=<span class="hljs-string">"product_name"</span>
  <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(value:</span> <span class="hljs-attr">any</span>) =></span> &#123;
    setSearchModel(&#123;
      ...searchModel,
      product_name: value,
      search_type: value ? 1 : undefined
    &#125;);
  &#125;&#125;
  onSelect=&#123;(value: any) => &#123;
    const newPager = &#123; pageno: 1 &#125;;
    const newSearchType = value ? 0 : lastSearchTypeSku;
    const newSearchModel = &#123;
      product_name: value,
      search_type: newSearchType
    &#125;;
    lastSearchTypeProduct = newSearchType;
    beforeLoadList(newPager, newSearchModel);
  &#125;&#125;
  onPressEnter=&#123;(value: any) => &#123;
    const pressLastSelected = searchModel.product_name === value && !searchModel.search_type;
    if (pressLastSelected) return;
    const newPager = &#123; pageno: 1 &#125;;
    const newSearchType = value ? 1 : lastSearchTypeSku;
    const newSearchModel = &#123;
      product_name: value,
      search_type: newSearchType
    &#125;;
    lastSearchTypeProduct = newSearchType;
    beforeLoadList(newPager, newSearchModel);
  &#125;&#125;
  /></span>

<span class="hljs-comment">// ES搜索2</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">marginRight:</span> <span class="hljs-attr">8</span> &#125;&#125;></span>&#123;translate('filtersku.variation')&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">EsSearch</span>
  <span class="hljs-attr">url</span>=<span class="hljs-string">&#123;</span>`/<span class="hljs-attr">api</span>/<span class="hljs-attr">es</span>/<span class="hljs-attr">autocomplete</span>/<span class="hljs-attr">sku_name</span>?<span class="hljs-attr">include_delete</span>=<span class="hljs-string">$&#123;includeDelete&#125;</span>`&#125;
  <span class="hljs-attr">esDocName</span>=<span class="hljs-string">"sku_name"</span>
  <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(value:</span> <span class="hljs-attr">any</span>) =></span> &#123;
    setSearchModel(&#123;
      ...searchModel,
      sku_name: value,
      search_type: value ? 1 : undefined
    &#125;);
  &#125;&#125;
  onSelect=&#123;(value: any) => &#123;
    const newPager = &#123; pageno: 1 &#125;;
    const newSearchType = value ? 0 : lastSearchTypeProduct;
    const newSearchModel = &#123;
      sku_name: value,
      search_type: newSearchType
    &#125;;
    lastSearchTypeSku = newSearchType;
    beforeLoadList(newPager, newSearchModel);
  &#125;&#125;
  onPressEnter=&#123;(value: any) => &#123;
    const pressLastSelected = searchModel.sku_name === value && !searchModel.search_type;
    if (pressLastSelected) return;
    const newPager = &#123; pageno: 1 &#125;;
    const newSearchType = value ? 1 : lastSearchTypeProduct;
    const newSearchModel = &#123;
      sku_name: value,
      search_type: newSearchType
    &#125;;
    lastSearchTypeSku = newSearchType;
    beforeLoadList(newPager, newSearchModel);
  &#125;&#125;
  /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，只是为了实现页面上的两个 ES 功能，就要写到 100 行代码，这种代码如果嵌套在业务逻辑里面，有时会很让人摸不着头脑。</p>
<p>除此之外，细心的同学已经发现，虽然是两个 ES 功能，但是其 <code>onChange</code>、<code>onSelect</code>、<code>onPressEnter</code> 回调函数里面的处理逻辑却惊人地相似，而且惊人地难阅读。</p>
<blockquote>
<p><code>SelectInput</code> 组件，一个可以配置支持 ES 搜索、或精确搜索的组件。</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><SelectInput
  customQuery=&#123;customQuery&#125;
  onSelect=&#123;<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> newPager = &#123; ...pager, <span class="hljs-attr">current</span>: <span class="hljs-number">1</span> &#125;;
    <span class="hljs-keyword">const</span> newSearchModel = &#123;
      ...searchModel,
      <span class="hljs-attr">platform_product_name</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">physical_product_name</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">physical_sku_id_barcode</span>: <span class="hljs-literal">null</span>,
    &#125;;
    setPager(newPager);
    setSearchModel(newSearchModel);
    getSalesOrderList(newPager, filterModel, sorterModel, newSearchModel);
  &#125;&#125;
  onEsSearchSelect=&#123;<span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-keyword">const</span> newPager = &#123; ...pager, <span class="hljs-attr">current</span>: <span class="hljs-number">1</span> &#125;;
    <span class="hljs-keyword">const</span> newSearchModel = &#123;
      ...searchModel,
      <span class="hljs-attr">platform_product_name</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">physical_product_name</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">physical_sku_id_barcode</span>: <span class="hljs-literal">null</span>,
      ...value,
      <span class="hljs-attr">search_type</span>: <span class="hljs-number">0</span>
    &#125;;
    setPager(newPager);
    setSearchModel(newSearchModel);
    getSalesOrderList(newPager, filterModel, sorterModel, newSearchModel);
  &#125;&#125;
  onPressEnter=&#123;<span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-keyword">const</span> newPager = &#123; ...pager, <span class="hljs-attr">current</span>: <span class="hljs-number">1</span> &#125;;
    <span class="hljs-keyword">const</span> newSearchModel = &#123;
      ...searchModel,
      <span class="hljs-attr">platform_product_name</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">physical_product_name</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">physical_sku_id_barcode</span>: <span class="hljs-literal">null</span>,
      ...value,
      <span class="hljs-attr">search_type</span>: <span class="hljs-number">1</span>
    &#125;;
    setPager(newPager);
    setSearchModel(newSearchModel);
    getSalesOrderList(newPager, filterModel, sorterModel, newSearchModel);
  &#125;&#125;
  onChange=&#123;<span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.keys(value).includes(<span class="hljs-string">'physical_sku_id_barcode'</span>)) &#123;
      <span class="hljs-keyword">const</span> newPager = &#123; ...pager, <span class="hljs-attr">current</span>: <span class="hljs-number">1</span> &#125;;
      <span class="hljs-keyword">const</span> newSearchModel = &#123;
        ...searchModel,
        <span class="hljs-attr">platform_product_name</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">physical_product_name</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">physical_sku_id_barcode</span>: <span class="hljs-literal">null</span>,
        ...value
      &#125;;
      setPager(newPager);
      setSearchModel(newSearchModel);
      delayedFetch(newPager, filterModel, sorterModel, newSearchModel, activeKey);
    &#125;
  &#125;&#125;
  />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简直可怕！这一段代码足足 100 余行，正常的 <code>VS Code</code> 编辑器中一个屏幕最多只能看 50 行左右，这意味着，你想一眼看清楚这里的计算逻辑，根本不可能。为了读懂这里面的逻辑，必须重复上下滚动，我想大部分开发者到此都已经望而却步。</p>
<p>如果没有人跟你解释 <code>onSelect</code>、<code>onEsSearchSelect</code>、<code>onPressEnter</code>、<code>onChange</code> 分别什么含义，以及回调具体的生命周期，我想你更加是没有阅读下去的勇气了。</p>
<p>更何况让你每次写类似的功能，而这些隐藏逻辑都永远不会在你的 <code>checklist</code> 里，出现 bug 了就只能哭爹喊娘骂产品 [doge]。</p>
<p>当然，以上两个案例只是一个小小的缩影，可以知道的是，通过检索 A 项目的代码后发现，<code>EsSearch</code> 组件的使用次数已达到 25 次（20 个文件），<code>SelectInput</code> 组件的使用次数已达到 15 次（13 个文件）。</p>
<p>而且，只要出现一个问题是与业务不对齐，就有可能修改 40 处，阅读至少 (25 * 50 + 15 * 100) 行的代码，在 33 个文件之间反复横跳。试问谁想做这样的优化需求呢？</p>
<p>“这下是不是已经有需求被迫 delay 的好借口 [doge]”。</p>
<h2 data-id="heading-1">正文</h2>
<p>当然，上面一句只是玩笑话，发现了问题，我们就需要寻求解决问题之道。</p>
<p>我想没有人喜欢在反反复复的修改中消耗时间，就像一个“美丽”的 <code>PRD</code> 一样能让人拥有一天“美丽”的“好”心情。</p>
<p>经过仔细统计，以及与业务和其他前端开发进行了对齐之后，我总结了以下目前几个需要统一解决的问题：</p>
<ol>
<li>统一的防抖策略。</li>
<li>一种异常发起请求的场景：先选中再回车。</li>
<li>一个向下兼容的处理：SelectInput 组件的一个不友好用法。</li>
<li>输入就触发，实现系统交互操作的统一。</li>
<li>空字符串、空白字符串的特殊处理。</li>
<li>兼容多个 ES 组件存在的场景（以及 <code>EsSearch</code>、<code>SelectInput</code> 混用场景）。</li>
<li>彻底地与业务逻辑解藕。</li>
<li>对4、5个回调彻底说拜拜，极大降低 ES 组件的使用成本；独立的 <code>hooks</code> 使 ES查询逻辑具备了可维护性，而且极大提高了拓展性。</li>
</ol>
<blockquote>
<p>在开始一一阐述以上问题前，我想先让大家感受一下 2.0 重构后的 <code>demo</code> 代码：</p>
<p><em>注释：1.0 重构的代码是写了一个 <code>reducer</code> 去处理复杂的回调，但未实现与业务代码解藕以及使用自定义 <code>hook</code></em></p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"> <span class="hljs-comment">// 由 hook 内部完成计算，并且更新到 esState 中 </span>
<span class="hljs-keyword">const</span> [esState, esProps] = useEsSearchOnChange(selectOptions); <span class="hljs-comment">// selectOptions 为使用 SelectInput 组件应有的配置</span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">SelectInput</span>
  <span class="hljs-attr">selectOptions</span>=<span class="hljs-string">&#123;selectOptions&#125;</span>
  &#123;<span class="hljs-attr">...esProps</span>&#125;
  <span class="hljs-attr">selectProps</span>=<span class="hljs-string">&#123;&#123;</span>
    <span class="hljs-attr">defaultValue:</span> '<span class="hljs-attr">product_name</span>',
      <span class="hljs-attr">style:</span> &#123; <span class="hljs-attr">width:</span> <span class="hljs-attr">160</span> &#125;,
        <span class="hljs-attr">dropdownMatchSelectWidth:</span> <span class="hljs-attr">336</span>
  &#125;&#125;
  /></span></span>
...
 <ProTable 
   searchModel=&#123;esState&#125; <span class="hljs-comment">// 结合Protable，自动完成请求</span>
   ...
   />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有没有瞬间感觉幸福指数飙升？</p>
<p>再也不需要管理复杂的回调生命周期，再也不需要在每个业务需求中做额外的 <code>checklist</code>，再也不用为了阅读一段 100 行的代码而耗费了大量时间。。。</p>
<h3 data-id="heading-2">整体思路</h3>
<p>问题已经整理完毕，重构后前端使用 ES 组件感受完毕。接下来我先介绍一下重构的整体思路。</p>
<p>利用 <code>React.useReducer</code> 可以使用一个 <code>reducer</code> 函数作为 state 的特性，在函数内部对 ES 组件那几个复杂的回调函数进行整合处理。而外界（指使用方）只需要关心 <code>useReducer</code> 返回的状态即可。如上述 <code>demo</code> 代码的 <code>esState</code>。</p>
<p>我们使用 <code>useReducer</code> 返回的 <code>dispatch</code>，给外界（指使用方：ES 组件）提供一个更新 <code>state</code> 的方法对象，如上述 <code>demo</code> 代码的 <code>esProps</code>：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx">&#123;
      <span class="hljs-attr">onChange</span>: <span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span>
        debounceDispatch(&#123; <span class="hljs-attr">payload</span>: value, <span class="hljs-attr">type</span>: <span class="hljs-string">'onChange'</span>, isEsSearch &#125;),
      <span class="hljs-attr">onPressEnter</span>: <span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span>
        debounceDispatch(&#123; <span class="hljs-attr">payload</span>: value, <span class="hljs-attr">type</span>: <span class="hljs-string">'onPressEnter'</span>, isEsSearch &#125;),
      <span class="hljs-attr">onEsSearchSelect</span>: <span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span>
        debounceDispatch(&#123; <span class="hljs-attr">payload</span>: value, <span class="hljs-attr">type</span>: <span class="hljs-string">'onEsSearchSelect'</span>, isEsSearch &#125;),
      <span class="hljs-attr">onSelect</span>: <span class="hljs-function">(<span class="hljs-params">key: <span class="hljs-built_in">any</span></span>) =></span>
        debounceDispatch(&#123; <span class="hljs-attr">payload</span>: key, <span class="hljs-attr">type</span>: <span class="hljs-string">'onSelect'</span>, isEsSearch &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 ES 组件的行为导致某个回调被触发时，会根据回调的类型 <code>type</code> 走到对应的计算逻辑，如 <code>onPressEnter</code> 回调对应  <code>onPressEnter</code> 类型。</p>
<p>接下来，我们要关注的点就是如何写这个 <code>reducer</code>。</p>
<h3 data-id="heading-3">统一的防抖策略</h3>
<p>基于 <code>lodash/debounce</code>，我们团队已经封装过一个 <code>useDebounce</code> 的 <code>hook</code>。传入 <strong>需要防抖的回调</strong>、<strong>防抖时效</strong>、<strong>防抖函数配置</strong>、<strong>需要关注的依赖</strong>，即会返回一个支持防抖的函数。</p>
<p>关于这个 hook 使用后感，我们组内的小伙伴有总结过一篇文章，有兴趣可以学习一下：<a href="https://confluence.shopee.io/pages/viewpage.action?pageId=532416632" target="_blank" rel="nofollow noopener noreferrer">confluence.shopee.io/pages/viewp…</a></p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> &#123; DependencyList, useEffect, useRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> debounce <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash/debounce'</span>;
<span class="hljs-keyword">import</span> &#123; DebounceSettings &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash'</span>;

<span class="hljs-keyword">const</span> useDebounce = <span class="hljs-function">(<span class="hljs-params">
  initialFn: <span class="hljs-built_in">any</span>,
  delay = <span class="hljs-number">200</span>,
  options: DebounceSettings = &#123; leading: <span class="hljs-literal">true</span> &#125;,
  deps: DependencyList = [delay, initialFn]
</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> fnRef = useRef(debounce(initialFn, delay, options));
  useEffect(<span class="hljs-function">() =></span> &#123;
    fnRef.current = debounce(initialFn, delay, options);
    <span class="hljs-keyword">return</span> fnRef.current.cancel;
  &#125;, deps); <span class="hljs-comment">// eslint-disable-line react-hooks/exhaustive-deps</span>
  <span class="hljs-keyword">return</span> fnRef.current;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> useDebounce;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>useEsSearchOnChange</code> 中使用 <code>useDebounce</code> :</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> [state, dispatch] = useReducer(reducer, &#123;&#125;);
  <span class="hljs-keyword">const</span> debounceDispatch = useDebounce(
    dispatch, <span class="hljs-comment">// 对 dispatch 进行防抖，实际上外界调用的是 debounceDispatch</span>
    <span class="hljs-number">300</span>,
    &#123; <span class="hljs-attr">trailing</span>: <span class="hljs-literal">true</span> &#125;,
    []
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">一种异常场景</h3>
<p>异常场景的回顾：</p>
<p><img src="https://github.com/AngelPP52/blog/raw/main/ES/%E5%85%88%E9%80%89%E4%B8%AD%E5%90%8E%E5%9B%9E%E8%BD%A6.gif" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体的操作为：先选中 <code>ES</code> 结果中的一个，然后直接回车，可以看到列表被刷新了。</p>
<p>异常的地方就在于，本来选中的时候应该是<code>精确搜索</code>，但是如果用户无意中点击了回车，将触发了页面上的两件事：</p>
<ol>
<li>ES 组件选择器展开；</li>
<li>发起一个<code>模糊搜索</code>。</li>
</ol>
<p>这导致了，用户想要<code>精确搜索</code>，却看到了<code>模糊搜索</code>的结果。</p>
<p>问题的根因就是，<code>ES</code> 业务组件内部对回车事件无法确定是想要模糊搜索还是想要展开选择器，<code>enter</code> 事件的职责从根本上是不确切的，所以要通过改 ES 业务组件来达到效果是不太科学的。</p>
<p>最后，为了不让用户对这里的功能存疑，我们的解决方案是：</p>
<p>如果上次用户未修改选中的结果，那么就认为用户还是希望看到精确搜索的结果。</p>
<p>对应的处理逻辑：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state: <span class="hljs-built_in">any</span>, action: ActionType</span>) =></span> &#123;
  ...
  <span class="hljs-comment">// 先精确搜索再模糊搜索：先选中再回车。不发起请求。</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">type</span> === <span class="hljs-string">'onPressEnter'</span>) &#123;
    <span class="hljs-keyword">const</span> pressLastSelected =
      !state.search_type && state[key] && state[key] === value;
    <span class="hljs-keyword">if</span> (pressLastSelected) <span class="hljs-keyword">return</span> state;
  &#125;
  ...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">一个向下兼容的处理</h3>
<p>由于 <code>SelectInput</code> 组件的作者在封装时，对 <code>EsSearch</code> 组件的 <code>onSelect</code> 回调手动触发了外层的 <code>onChange</code> 导致的一个问题：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> handleValueChange = <span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span> &#123;
  ...
  onChange(&#123; <span class="hljs-comment">// 这个触发没有意义的，却给用户带来了很多麻烦</span>
    [selectedOption.value]: value,
  &#125;);
&#125;;
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">EsSearch</span>
 <span class="hljs-attr">...</span>
  <span class="hljs-attr">onSelect</span>=<span class="hljs-string">&#123;(value:</span> <span class="hljs-attr">string</span>) =></span> &#123;
    ...
    handleValueChange(value);
    ...
  &#125;&#125;
  ...
  /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了不导致网页出现 <code>Bug</code>，每个用户都要在 <code>SelectInput</code> 组件中加这样的一段代码，以修复 <code>onChange</code> 回调带来的隐患：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><SelectInput
  ...
  onChange=&#123;<span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-comment">// 这段代码给业务代码增加了不必要的阅读困难</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.keys(value).includes(<span class="hljs-string">'physical_sku_id_barcode'</span>)) &#123;
      ...
    &#125;
  &#125;&#125;
  ..
  />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基本没人能猜测到：这个判断是为了在 <code>onChange</code> 中只允许非 ES 的搜索而禁止 ES 的搜索。</p>
<p>所以，为了避免业务逻辑中额外的阅读成本，我在 <code>useEsSearchOnChange</code> 中做了这样的处理，解决这个向下兼容的问题：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state: <span class="hljs-built_in">any</span>, action: ActionType</span>) =></span> &#123;
  ...
  <span class="hljs-comment">// type:esSearch onChange事件不处理，不发起请求。</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> payload === <span class="hljs-string">'object'</span> && <span class="hljs-keyword">type</span> === <span class="hljs-string">'onChange'</span>) &#123;
    <span class="hljs-keyword">if</span> (isEsSearch(key)) <span class="hljs-keyword">return</span> state;
  &#125;
  ...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">输入即请求</h3>
<p>这是以前规范的交互示例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4257f95bb290424bbd07fd6927b14b24~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是现在规范的交互示例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7839fed819e046499d4484d1d7d861b7~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>区别在于，用户停止输入后，是否发起一个请求（这是一个精确搜索的请求）。</p>
<p>通过阅读 <code>SelectInput</code>的代码发现，对 <code>EsSearch</code> 组件的 <code>onChange</code> 回调处理有提供一个 <code>onEsSearchChange</code> 的回调，使用 <code>SelectInput</code> 的用户可以监听此回调来实现输入即请求的功能。</p>
<p>既然是一次性解决 <code>ES</code> 组件带来的隐患，自然少不了为 <code>useEsSearchOnChange</code> 补上一段逻辑，以支持【输入即请求】：</p>
<pre><code class="hljs language-TSX copyable" lang="TSX"><span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state: <span class="hljs-built_in">any</span>, action: ActionType</span>) =></span> &#123;
  ...
  <span class="hljs-comment">// 每次触发 dispatch 都清空。</span>
  <span class="hljs-keyword">const</span> newState = &#123;&#125;;
  <span class="hljs-keyword">switch</span> (<span class="hljs-keyword">type</span>) &#123;
    ...
    <span class="hljs-keyword">case</span> <span class="hljs-string">'onEsSearchChange'</span>: <span class="hljs-comment">// 输入就触发请求</span>
      <span class="hljs-built_in">Object</span>.assign(
        newState,
        payload,
        value && isEsSearch(key) ? &#123; <span class="hljs-attr">search_type</span>: <span class="hljs-number">1</span> &#125; : &#123;&#125;
      );
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'onSelect'</span>:
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">default</span>:
  &#125;
  <span class="hljs-keyword">return</span> newState;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>reducer</code> 返回了一个新的对象，所以 <code>esState</code> 会被更新为新的状态，从而触发 <code>ProTable</code> 自动请求的逻辑，最终达到目的。</p>
<h3 data-id="heading-7">特殊字符的特殊处理</h3>
<p>从后台的接口规范中得知，如果参数为空或空白字符，会被认为是一段无意义的传参。</p>
<p>实际上 <code>axios</code> 已经帮我们做了类似的事情，如我们传参 <code>&#123;a: null&#125;</code> 或者 <code>&#123;a: undefined&#125;</code>，参数 <code>a</code> 则不会被传到后台。</p>
<p>这里处理比较简单，没有什么技术含量，请直接看代码：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state: <span class="hljs-built_in">any</span>, action: ActionType</span>) =></span> &#123;
  ...
  <span class="hljs-comment">// 空、空白的字符不带到请求参数。</span>
  <span class="hljs-keyword">if</span> (!value || !value.trim()) &#123;
    <span class="hljs-keyword">return</span> &#123;&#125;;
  &#125;
  ...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">兼容多个 ES 组件</h3>
<p>多个ES组件存在几种组合：</p>
<ol>
<li><code>EsSearch + EsSearch</code></li>
<li><code>SelectInput + SelectInput</code></li>
<li><code>EsSearch + SelectInput</code></li>
</ol>
<p>为何需要做这样的兼容工作？还是从实际场景去看，注意观察右侧打印：</p>
<p><img src="https://github.com/AngelPP52/blog/raw/main/ES/%E5%85%BC%E5%AE%B9%E5%A4%9A%E4%B8%AAES%E7%BB%84%E4%BB%B6.gif" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>仔细的同学已经发现，<code>ES</code> 组件 1 与 ES 组件 2 同时参与查询的时候是没有问题的，使用模糊搜索或者精确搜索都以最后一次操作为准。</p>
<p>但是，在两个组件同时有值的同时，去清空其中一个组件的值，可以发现，一定发起了精确搜索。这是因为清空动作对应的回调是：<code>onEsSearchSelect</code>，可以从 <code>onEsSearchChange</code> 看到这个回调类型表示是精确搜索。</p>
<p>不得不说，<code>ES</code> 组件是非常复杂的，一部分是因为业务场景比较多，另一部分也表现在组件本身提供了很多职责不够清晰的回调。</p>
<p>再与业务方对齐，得到的结果是：</p>
<p>一定发起精确搜索的逻辑是不符合用户习惯的，应该改成，记忆用户对每个 ES 组件的操作，并且能够在清空其中一个时，能恢复另外一个组件最后一次操作的结果。</p>
<p>翻译过来的意思就是：如果组件 1 最后一次是精确搜索，组件 2 最后一次是模糊搜索，清空组件 1 的内容，这个时候应该以组件 2 的最后一次操作为准，发起一个模糊搜索而不是精确搜索。</p>
<p>可以解决的一种方案：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 在调用方合并 esState</span>
<span class="hljs-keyword">const</span> [esState1, esProps1] = useEsSearchOnChange(selectOptions1);
<span class="hljs-keyword">const</span> [esState2, esProps2] = useEsSearchOnChange(selectOptions2);
<span class="hljs-comment">// 合并的 esState</span>
<span class="hljs-keyword">const</span> [totalEsState, setTotalEsState] = React.useState(&#123;...esState1, ...esState2&#125;)

React.useEffect(<span class="hljs-function">() =></span> &#123;
  setTotalEsState(&#123;...esState1, ...esState2&#125;);
&#125;, [esState1, esState2])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的优点是，search_type 是属于不同的 esState 的，符合记忆的功能，合并对象以后会采用有值的一方，符合满足用户习惯的功能。缺点是合并逻辑要耦合在业务代码中。</p>
<h3 data-id="heading-9">与业务逻辑解藕</h3>
<p>自定义的 <code>hook</code>，可以很好地将非业务关心和稳定性高的逻辑封装起来，实现与业务逻辑的解藕，让业务代码专心负责页面核心的逻辑。</p>
<p>这也是为什么我从版本 <code>1.0</code> 重构到 <code>2.0</code> 的目的，在 <code>1.0</code> 里，复杂的 <code>reducer</code> 代码仍然内嵌在业务代码里，而每个相关的组件使用的 <code>reducer</code> 却十分相似。使得业务代码不得不臃肿起来，这是不能被接收的事情。</p>
<h3 data-id="heading-10">告别复杂的回调函数</h3>
<p>可以看一下 <code>useEsSearchOnChange</code> 的返回：</p>
<ol>
<li><code>esState</code> 是结合 ES 组件的数据计算后的结果；</li>
<li>&#123;<code>onChange</code>, <code>onPressEnter</code>, <code>onEsSearchSelect</code>, <code>onSelect</code>&#125; 是传给 ES 组件的属性。</li>
</ol>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> useEsSearchOnChange = <span class="hljs-function">(<span class="hljs-params">selectOptions: <span class="hljs-built_in">any</span>[]</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> isEsSearch = <span class="hljs-function">(<span class="hljs-params">key: <span class="hljs-built_in">any</span></span>) =></span>
    selectOptions.some(
      <span class="hljs-function">(<span class="hljs-params">opt: <span class="hljs-built_in">any</span></span>) =></span> opt.type === <span class="hljs-string">'esSearch'</span> && opt.value === key
    );
  <span class="hljs-keyword">const</span> [state, dispatch] = useReducer(reducer, &#123;&#125;);
  <span class="hljs-keyword">const</span> debounceDispatch = useDebounce(
    dispatch,
    <span class="hljs-number">300</span>,
    &#123; <span class="hljs-attr">trailing</span>: <span class="hljs-literal">true</span> &#125;,
    []
  );
  <span class="hljs-comment">// 1.es state</span>
  <span class="hljs-comment">// 2.es props</span>
  <span class="hljs-keyword">return</span> [
    state,
    &#123;
      <span class="hljs-attr">onChange</span>: <span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span>
        debounceDispatch(&#123; <span class="hljs-attr">payload</span>: value, <span class="hljs-attr">type</span>: <span class="hljs-string">'onChange'</span>, isEsSearch &#125;),
      <span class="hljs-attr">onPressEnter</span>: <span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span>
        debounceDispatch(&#123; <span class="hljs-attr">payload</span>: value, <span class="hljs-attr">type</span>: <span class="hljs-string">'onPressEnter'</span>, isEsSearch &#125;),
      <span class="hljs-attr">onEsSearchSelect</span>: <span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) =></span>
        debounceDispatch(&#123; <span class="hljs-attr">payload</span>: value, <span class="hljs-attr">type</span>: <span class="hljs-string">'onEsSearchSelect'</span>, isEsSearch &#125;),
      <span class="hljs-attr">onSelect</span>: <span class="hljs-function">(<span class="hljs-params">key: <span class="hljs-built_in">any</span></span>) =></span>
        debounceDispatch(&#123; <span class="hljs-attr">payload</span>: key, <span class="hljs-attr">type</span>: <span class="hljs-string">'onSelect'</span>, isEsSearch &#125;)
    &#125;,
  ];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自定义 <code>hook：useEsSearchOnChange</code> 把复杂的回调函数的处理统一交给了 <code>reducer</code> 来做。大大解放了使用者做需求所需的时间。</p>
<h2 data-id="heading-11">其他解决方案</h2>
<p>解决 <code>ES</code> 组件带来的问题以上并不是唯一解，这只是一种解决问题的思维。例如，为了让代码更加健壮，模块解藕是很好的方式；为了组件更加好用，二次封装是很好的方式；巧用 <code>hook</code> 让组件更易于维护，等等。</p>
<p>组件的迭代过程必然是不断出现问题和解决问题的过程，开发者在封装阶段一般很难做好覆盖，首先时间上也不允许，其次组件质量大多因人而异。所以针对封装公共组件，最好的方法就是“找到变化，封装变化”。</p>
<p>我还想到的其他解决方案：</p>
<ol>
<li>
<p>你也可以通过二次封装，把 <code>ES</code> 组件与 <code>Table</code> 组件组合到 <code>ProTable</code> 组件中，由 <code>ProTable</code> 组件内部去完成恶心的回调函数。</p>
</li>
<li>
<p>对 <code>ES</code> 组件再封装一层，在这一层中完成恶心的回调函数。</p>
</li>
<li>
<p>重构原有 <code>ES</code> 组件的回调，让回调函数更加直观明了且更好用。</p>
</li>
</ol>
<p>等等...</p>
<h2 data-id="heading-12">最后</h2>
<p>以上就是本次的所有分享，希望您看到这里能有所收获。</p>
<p>才疏学浅，如有讲述不清之处，还请指正，共同进步。</p>
<h2 data-id="heading-13">参考资料</h2>
<ul>
<li>洞察设计模式的底层逻辑 - <a href="https://mp.weixin.qq.com/s/qRjn_4xZdmuUPQFoWMBQ4Q" target="_blank" rel="nofollow noopener noreferrer">mp.weixin.qq.com/s/qRjn_4xZd…</a></li>
<li><a href="https://zh-hans.reactjs.org/docs/hooks-reference.html#usereducer" target="_blank" rel="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/hooks-…</a></li>
</ul></div>  
</div>
            