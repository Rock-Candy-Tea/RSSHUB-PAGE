
---
title: '百万PV商城实践系列 - 前端长列表渲染优化实战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d072876ea5494132927c0539b29b42fc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 16:29:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d072876ea5494132927c0539b29b42fc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>⚠️ 本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<h2 data-id="heading-0">简介</h2>
<p>本篇文章是<code>商城实践系列</code>的第二篇文章，主要内容是对商城项目中一些<code>长列表渲染</code>进行优化，提高渲染的效率、优化显示速度。</p>
<p>我们在使用电商平台的过程中，打开首页时，我们一直向下滑动就会有源源不断的推荐内容向我们展示。随着浏览页面操作越来越多，数据也越来越庞大，这类场景我们都可以统一称为长列表渲染。</p>
<p>在商城项目当中，长列表渲染出现的页面都与用户密切相关，如<code>订单列表</code>、<code>优惠券列表</code>、<code>购物车</code>等都是我们日常生活中经常浏览的一些页面，因此长列表渲染的<code>性能效率</code>与<code>用户体验</code>两者是成<code>正比</code>的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d072876ea5494132927c0539b29b42fc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而在长列表页面做性能优化和开发设计的时候，我们大多数会碰到以下两个问题：</p>
<ul>
<li><code>数据过多</code>，首次展示内容时间过长，接口返回数据过多，页面数据不好处理。</li>
<li><code>DOM元素过多</code>，页面渲染卡顿、操作不流畅，浏览器性能压力重。</li>
</ul>
<p>这些问题该怎么解决呢？我建议使用分页加载+虚拟列表的方案。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6772d315449f4f96b19a48cc85d280bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">为什么使用分页+虚拟列表的方案？</h2>
<p>为了方便大家查阅，我把<code>详细的场景</code>、<code>问题和可用的解决方案</code>整理在了思维导图中。其中，可用的解决方案包括<code>分页加载</code>、<code>切片加载</code>、<code>虚拟列表</code>，以及<code>分页+虚拟列表</code>。那么，我为什么选择<code>分页+虚拟列表</code>这个方案呢？</p>
<p>首先，我们将每个方案可以<code>解决的问题</code>和<code>不能解决的问题</code>做一个梳理，具体的优缺点如下：</p>
<ul>
<li>
<p><strong>分页加载</strong>：解决了数据过多问题，通过数据分页的方式减少了<code>首次页面加载的数据和DOM数量</code>。是现今绝大部分的应用都会采用的实施手段。随着页面<code>浏览的页面数据增多</code>，DOM数量也越来越多，还是会存在部分问题。</p>
</li>
<li>
<p><strong>分片加载</strong>：与分页加载相同，只是将用户触底行为获取最新数据的时间节点在一开始进行了切片加载，优先显示页面数据在加载其他数据。<code>会出现页面阻塞和性能问题</code>。</p>
</li>
<li>
<p><strong>虚拟列表</strong>：将驱动交给数据，通过区间来直接<code>渲染区间内容中的数据DOM</code>，解决了页面列表内元素过多操作卡顿的问题, 与数据加载无挂钩。</p>
</li>
</ul>
<p>当列举了<code>三种常见</code>的方式后，我们发现<code>单一的方案</code>很难满足我们的诉求。因此，我选择使用<code>分页的方式</code>处理数据加载，同时将渲染页面的事情交给<code>虚拟列表</code>进行渲染。通过结合两种不同侧重点的方案，来满足我们初步的诉求。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/feb2e430439d46a0b10a7cf3d85eaa3b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">实现虚拟列表</h2>
<p>既然敲定了解决方案，我们就先来看看虚拟列表是什么东西吧🥳。</p>
<p>通过下面的示意图，我们将整体列表划分为<code>滚动窗口</code>和<code>可视窗口</code>。左边是真实的列表，所有的列表项都是真实的DOM元素，而虚拟列表从图中可以看到，只有出现在可视窗口内的列表项才是真实的DOM元素，而未出现在可视窗口中的元素则只是虚拟数据，并未加载到页面上。</p>
<blockquote>
<p>与真实列表不同的是，虚拟列表的滚动都是通过transform或者是marginTop做的偏移量，本身列表中只显示视窗区的DOM元素。</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a3363e976bb4e4cabf99d0414077809~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面，我们就来从0到1实现一个基本的虚拟列表吧。</p>
<h3 data-id="heading-3">基本布局</h3>
<p>如下结构图，我们先分析下基本页面构成：</p>
<ul>
<li>第一层为<code>容器层</code>，选定一个固定高度，也就是我们说的可视化窗口</li>
<li>第二层为<code>内容层</code>，一般在这里撑开高度，使容器形成<code>scroll</code>。</li>
<li>第三层为<code>子内容层</code>，居于内容层内部，也就是列表中的列表项。</li>
<li><code>......</code></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d484e0dd47754b2ba8ea70c42c3df4bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>分析后，我将结构图中代码使用<code>JSX</code>实现后，就是下面这个简单的结构：</p>
<p><code>页面布局代码</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    ... List Item Element
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>;

.App &#123;
    font-family: sans-serif;
    text-align: center;
&#125;

.showElement &#123;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid #000;
    margin-bottom: 8px;
    border-radius: 4px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先搭建一个简单的页面，然后通过<code>currentViewList</code>渲染出对应的列表项内容。</p>
<h3 data-id="heading-4">初始化页面</h3>
<p>当我们确定了页面的基本结构后，我们再来完善一些布局与配置，实现一个真实渲染上千条数据的列表。</p>
<p>我先定义了一些配置，包含容器高度、列表项高度、预加载偏移数量等需要用到的固定内容。</p>
<ul>
<li><strong>容器高度</strong>：当前虚拟列表的高度</li>
<li><strong>列表项高度</strong>： 列表项的高度</li>
<li><strong>预加载偏移</strong>：可视窗上下做预加载时需要额外展示几个预备内容</li>
</ul>
<p><code>页面属性</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/** <span class="hljs-doctag">@name </span>页面容器高度 */</span>

<span class="hljs-keyword">const</span> SCROLL_VIEW_HEIGHT: <span class="hljs-built_in">number</span> = <span class="hljs-number">500</span>;

<span class="hljs-comment">/** <span class="hljs-doctag">@name </span>列表项高度 */</span>

<span class="hljs-keyword">const</span> ITEM_HEIGHT: <span class="hljs-built_in">number</span> = <span class="hljs-number">50</span>;

<span class="hljs-comment">/** <span class="hljs-doctag">@name </span>预加载数量 */</span>

<span class="hljs-keyword">const</span> PRE_LOAD_COUNT: <span class="hljs-built_in">number</span> = SCROLL_VIEW_HEIGHT / ITEM_HEIGHT;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，创建一个<code>useRef</code>用来存储元素，然后获取视窗高度和偏移属性。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/** 容器Ref */</span>

<span class="hljs-keyword">const</span> containerRef = useRef<HTMLDivElement | <span class="hljs-literal">null</span>>(<span class="hljs-literal">null</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，创建数据源，并且生成<code>3000</code>条随机数据做显示处理。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> [sourceData, setSourceData] = useState<<span class="hljs-built_in">number</span>[]>([]);

<span class="hljs-comment">/**
 * 创建列表显示数据
 */</span>
<span class="hljs-keyword">const</span> createListData = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> initnalList: <span class="hljs-built_in">number</span>[] = <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">Array</span>(<span class="hljs-number">4000</span>).keys());
  setSourceData(initnalList);
&#125;;

useEffect(<span class="hljs-function">() =></span> &#123;
  createListData();
&#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，为相对应的容器绑定高度。在最外层div标签设置高度为<code>SCROLL_VIEW_HEIGHT</code>，对列表div的高度则设置为<code>sourceData.length * ITEM_HEIGHT</code>。</p>
<p><code>获取列表整体高度</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * scrollView整体高度
 */</span>
 <span class="hljs-keyword">const</span> scrollViewHeight = useMemo(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> sourceData.length * ITEM_HEIGHT;
&#125;, [sourceData]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>绑定页面视图</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>
  <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;containerRef&#125;</span>
  <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
    <span class="hljs-attr">height:</span> <span class="hljs-attr">SCROLL_VIEW_HEIGHT</span>,
    <span class="hljs-attr">overflow:</span> "<span class="hljs-attr">auto</span>",
  &#125;&#125;
  <span class="hljs-attr">onScroll</span>=<span class="hljs-string">&#123;onContainerScroll&#125;</span>
></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>
    <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
      <span class="hljs-attr">width:</span> "<span class="hljs-attr">100</span>%",
      <span class="hljs-attr">height:</span> <span class="hljs-attr">scrollViewHeight</span> <span class="hljs-attr">-</span> <span class="hljs-attr">scrollViewOffset</span>,
      <span class="hljs-attr">marginTop:</span> <span class="hljs-attr">scrollViewOffset</span>,
    &#125;&#125;
  ></span>
    &#123;sourceData.map((e) => (
      <span class="hljs-tag"><<span class="hljs-name">div</span>
        <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
          <span class="hljs-attr">height:</span> <span class="hljs-attr">ITEM_HEIGHT</span>,
        &#125;&#125;
        <span class="hljs-attr">className</span>=<span class="hljs-string">"showElement"</span>
        <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;e&#125;</span>
      ></span>
        Current Position: &#123;e&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    ))&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当数据初始化后，我们的列表页面就初步完成了，来看下效果吧。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d76f0c0670543aa904a53c74d5411f5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">内容截取</h3>
<p>对于虚拟列表来说，并不需要全量将数据渲染在页面上。那么，在这里我们就要开始做数据截取的工作了。</p>
<p>首先，如下图，我们通过<code>showRange</code>来控制页面显示元素的数量。通过<code>Array.slice</code>的函数方法对<code>sourceData</code>进行数据截取, 返回值就是我们在页面上去显示的列表数据了。我将上面代码中直接遍历<code>souceData</code>换成我们的新数据列表。如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts">&#123;currentViewList.map(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>
    <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
      <span class="hljs-attr">height:</span> <span class="hljs-attr">ITEM_HEIGHT</span>
    &#125;&#125;
    <span class="hljs-attr">className</span>=<span class="hljs-string">"showElement"</span>
    <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;e.data&#125;</span>
  ></span>
    Current Position: &#123;e.data&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
))&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面使用到的<code>currentViewList</code>是一个<code>useMemo</code>的返回值，它会随着<code>showRange</code>和<code>sourceData</code>的更新发生变化。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 当前scrollView展示列表
 */</span>
 <span class="hljs-keyword">const</span> currentViewList = useMemo(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> sourceData.slice(showRange.start, showRange.end).map(<span class="hljs-function">(<span class="hljs-params">el, index</span>) =></span> (&#123;
    <span class="hljs-attr">data</span>: el,
    index,
  &#125;));
&#125;, [showRange, sourceData]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08ebcff5d55a46cc9ab00cb1ced956df~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">滚动计算</h3>
<p>至此，已经完成了一个基本的虚拟列表雏形，下一步我们就需要监听视窗滚动事件来计算<code>showRange</code>中的<code>start</code>和<code>end</code>的偏移量，同时调整对应的滚动条进度来实现一个真正的列表效果。</p>
<p>首先，我先为滚动视窗(scrollContainer)绑定onScroll事件，也就是下面的<code>onContainerScroll</code>函数方法。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * onScroll事件回调
 * <span class="hljs-doctag">@param </span>event &#123; UIEvent<HTMLDivElement> &#125; scrollview滚动参数
 */</span>
 <span class="hljs-keyword">const</span> onContainerScroll = <span class="hljs-function">(<span class="hljs-params">event: UIEvent<HTMLDivElement></span>) =></span> &#123;
  event.preventDefault();
  calculateRange();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在事件主要做的事情就计算当前<code>showRange</code>中的<code>start</code>和<code>end</code>所处位置，同时更新页面视图数据。下面，我们来看看它是怎么处理的吧！</p>
<p>首先，通过<code>containerRef.current.scrollTop</code>可以知道元素滚动条内的顶部隐藏列表的高度，然后使用<code>Math.floor</code>方法向下取整后，来获取当前偏移的元素数量，在减去一开始的上下文预加载数量<code>PRE_LOAD_COUNT</code>，就可以得出截取内容开始的位置。</p>
<p>其次，通过<code>containerRef.current.clientHeight</code>可以获取滚动视窗的高度，那么通过<code>containerRef.current.clientHeight / ITEM_HEIGHT</code>这个公式就可以得出当前容器窗口可以容纳几个列表项。</p>
<p>当我通过当前滚动条位置下之前滚动的元素个数且已经计算出截取窗口的起始位置后，就可以通过<code>启动位置 + 容器显示个数 + 预加载个数</code>这个公式计算出了当前截取窗口的结束位置。使用<code>setShowPageRange</code>方法更新新的位置下标后，当我上下滑动窗口，显示的数据会根据<code>showRange</code>切割成为不同的数据渲染在页面上。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 计算元素范围
 */</span>
 <span class="hljs-keyword">const</span> calculateRange = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> element = containerRef.current;
  <span class="hljs-keyword">if</span> (element) &#123;
    <span class="hljs-keyword">const</span> offset: <span class="hljs-built_in">number</span> = <span class="hljs-built_in">Math</span>.floor(element.scrollTop / ITEM_HEIGHT) + <span class="hljs-number">1</span>;
    <span class="hljs-built_in">console</span>.log(offset, <span class="hljs-string">"offset"</span>);
    <span class="hljs-keyword">const</span> viewItemSize: <span class="hljs-built_in">number</span> = <span class="hljs-built_in">Math</span>.ceil(element.clientHeight / ITEM_HEIGHT);
    <span class="hljs-keyword">const</span> startSize: <span class="hljs-built_in">number</span> = offset - PRE_LOAD_COUNT;
    <span class="hljs-keyword">const</span> endSize: <span class="hljs-built_in">number</span> = viewItemSize + offset + PRE_LOAD_COUNT;
    setShowPageRange(&#123;
      <span class="hljs-attr">start</span>: startSize < <span class="hljs-number">0</span> ? <span class="hljs-number">0</span> : startSize,
      <span class="hljs-attr">end</span>: endSize > sourceData.length ? sourceData.length : endSize,
    &#125;);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc0a4cd3562d43379357b98a0b758484~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">滚动条偏移</h3>
<p>上面，我们提到会根据<code>containerRef.current.scrollTop</code>计算当前滚动过的高度。那么问题来了，页面上其实并没有真实的元素，又该如何去撑开这个高度呢？</p>
<p>目前而言，比较流行的解决方案分为<code>MarinTop</code>和<code>TranForm</code>做距离顶部的偏移来实现高度的撑开。</p>
<ul>
<li>margin是属于布局属性，该属性的变化会导致页面的重排</li>
<li>transform是合成属性，浏览器会为元素创建一个独立的复合层，当元素内容没有发生变化，该层不会被重绘，通过重新复合来创建动画帧。</li>
</ul>
<p>两种方案并没有太大的区别，都可以用来实现距离顶部位置的偏移，达到撑开列表实际高度的作用。</p>
<p>下面，我就以<code>MarinTop</code>的方法来处理这个问题，来完善当前的虚拟列表。</p>
<p>首先，我们需要计算出列表页面距离顶部的<code>MarginTop</code>的距离，通过公式：<code>当前虚拟列表的起始位置 * 列表项高度</code>，我们可以计算出当前的<code>scrollTop</code>距离。</p>
<p>通过<code>useMemo</code>将逻辑做一个缓存处理，依赖项为<code>showRange.start</code>, 当<code>showRange.start</code>发生变化时会更新<code>marginTop</code>的高度计算。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * scrollView 偏移量
 */</span>
 <span class="hljs-keyword">const</span> scrollViewOffset = useMemo(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(showRange.start, <span class="hljs-string">"showRange.start"</span>);
  <span class="hljs-keyword">return</span> showRange.start * ITEM_HEIGHT;
&#125;, [showRange.start]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在页面上为列表窗口绑定<code>marginTop: scrollViewOffset</code>属性，并且在总高度中减去<code>scrollViewOffset</code>来维持平衡，防止多出距离的白底。</p>
<p><code>如下代码</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>
    <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
        <span class="hljs-attr">width:</span> "<span class="hljs-attr">100</span>%",
        <span class="hljs-attr">height:</span> <span class="hljs-attr">scrollViewHeight</span> <span class="hljs-attr">-</span> <span class="hljs-attr">scrollViewOffset</span>,
        <span class="hljs-attr">marginTop:</span> <span class="hljs-attr">scrollViewOffset</span>
    &#125;&#125;
></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，我们已经完成了一个基本的虚拟列表，下面我们来一起看看实际的效果吧。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d3cf7f0245e4e49a86b92688b3fb33b~tplv-k3u1fbpfcp-watermark.image" alt="Kapture 2021-08-08 at 17.51.29.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">结合分页加载</h2>
<p>当我们有了一个虚拟列表后，就可以尝试结合分页加载来实现一个懒加载的长虚拟列表了。</p>
<p>如果做过分页滚动加载的小伙伴可能立马就想到实现思路了，不了解的同学也不要着急，下面我就带大家一起来实现一个带分页加载的虚拟列表，相信你看完之后会对这类问题有一个更加深入的理解。</p>
<h3 data-id="heading-9">判断是否到底部</h3>
<p>想要实现列表的分页加载，我们需要绑定<code>onScroll</code>事件来判断当前滚动视窗是否滚动到了底部，当滚动到底部后需要为<code>sourceData</code>进行数据的添加。同时将挪动指针，将数据指向下一个起始点。</p>
<p>具体实现代码如下，<code>reachScrollBottom</code>函数的返回值是当前滚动窗口是否已经到达了底部。因此，我们通过函数的返回值进行条件判断。到达底部后，我们模拟一批数据后通过<code>setSourceData</code>设置源数据。结束之后在执行<code>calculateRange</code>重新设置内容截取的区间。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * onScroll事件回调
 * <span class="hljs-doctag">@param </span>event &#123; UIEvent<HTMLDivElement> &#125; scrollview滚动参数
 */</span>
 <span class="hljs-keyword">const</span> onContainerScroll = <span class="hljs-function">(<span class="hljs-params">event: UIEvent<HTMLDivElement></span>) =></span> &#123;
  event.preventDefault();
  <span class="hljs-keyword">if</span> (reachScrollBottom()) &#123;
    <span class="hljs-comment">// 模拟数据添加，实际上是 await 异步请求做为数据的添加</span>
    <span class="hljs-keyword">let</span> endIndex = showRange.end;
    <span class="hljs-keyword">let</span> pushData: <span class="hljs-built_in">number</span>[] = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; index < <span class="hljs-number">20</span>; index++) &#123;
      pushData.push(endIndex++);
    &#125;
    setSourceData(<span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> [...arr, ...pushData];
    &#125;);
  &#125;
  calculateRange();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么，<code>calculatScrollTop</code>是如何判断当前是否已经触底呢？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47ba10f8c1c84943877caccdbd5c9b33~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>分析上图，我通过<code>containerRef</code>可以拿到滚动窗口的高度<code>scrollHeight</code>或者直接使用<code>soureData.length * ITEM_HEIGHT</code>充当滚动窗口的高度两者作用是一样的。</p>
<p>同时，我也可以拿到<code>scrollTop</code>滚动位置距离顶部的高度和<code>clientHeight</code>当前视窗高度。通过三者的关系，可以得出条件公式：<code>scrollTop + clientHeight >= scrollHeight</code>，满足这个条件就说明当前窗口已经到达底部。我们将其写成<code>reachScrollBottom</code>方法，如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 计算当前是否已经到底底部
 * <span class="hljs-doctag">@returns </span>是否到达底部
 */</span>
 <span class="hljs-keyword">const</span> reachScrollBottom = (): <span class="hljs-function"><span class="hljs-params">boolean</span> =></span> &#123;
  <span class="hljs-comment">//滚动条距离顶部</span>
  <span class="hljs-keyword">const</span> contentScrollTop = containerRef.current?.scrollTop || <span class="hljs-number">0</span>; 
  <span class="hljs-comment">//可视区域</span>
  <span class="hljs-keyword">const</span> clientHeight = containerRef.current?.clientHeight || <span class="hljs-number">0</span>; 
  <span class="hljs-comment">//滚动条内容的总高度</span>
  <span class="hljs-keyword">const</span> scrollHeight = containerRef.current?.scrollHeight || <span class="hljs-number">0</span>;
  <span class="hljs-keyword">if</span> (contentScrollTop + clientHeight >= scrollHeight) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">无限列表演示</h3>
<p>至此，我们的虚拟列表实现已经基本完成了，下面我们一起来看看效果吧，这里先简单的模拟一个商品列表来作为演示页面，效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ab17038bd5e4718990bf2387bce4d85~tplv-k3u1fbpfcp-watermark.image" alt="Kapture 2021-08-08 at 22.51.01.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">资源推荐</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fxuniliebiaodaimashili-moi5f%3Ffile%3D%2Fsrc%2FApp.tsx%3A3138-3148" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/xuniliebiaodaimashili-moi5f?file=/src/App.tsx:3138-3148" ref="nofollow noopener noreferrer"># 文章源码地址</a></li>
<li><a href="https://juejin.cn/post/6844903982742110216" target="_blank" title="https://juejin.cn/post/6844903982742110216"># 「前端进阶」高性能渲染十万条数据(虚拟列表)</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F366416646" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/366416646" ref="nofollow noopener noreferrer"># 如何实现一个高度自适应的虚拟列表</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fahooks.js.org%2Fhooks%2Fui%2Fuse-virtual-list" target="_blank" rel="nofollow noopener noreferrer" title="https://ahooks.js.org/hooks/ui/use-virtual-list" ref="nofollow noopener noreferrer"># ahooks虚拟列表</a></li>
</ul>
<h2 data-id="heading-12">总结</h2>
<p>本篇文章中，我讲了针对商城项目中出现长列表的部分场景，同时针对这些场景列举了不同的解决方案及其优缺点。在选择<code>分页 + 虚拟列表</code>的组合方式来解决问题的过程中，我一步一步带大家实现了一个简单的分页虚拟列表，帮助大家了解其内部的原理。</p>
<p>当然，这个方案还有很多需要完善的地方，我也在这里说说它需要优化的地方。</p>
<ul>
<li>滚动事件可以添加节流事件避免造成性能浪费。</li>
<li>列表项高度不固定需要给定一个默认高度后设置新的高度在重新刷新容易截取的开始和结束位置。</li>
<li>滑动过快出现白屏问题可以尝试动态加载loading显示过渡，优化一些细节体验。</li>
<li>列表项中存在阴影元素需要考虑缓存处理，不然滚动时必然会引起重新加载。</li>
</ul>
<p>市面上已经有很多<code>开源库</code>可以解决这些问题，如react中<code>ahooks</code>就有相对完善的虚拟列表实践，本文的代码相对而言也是对其的源码分析。</p>
<p>总的来说，我们在真实开发中并不需要从零开始造一个完善的轮子，直接使用成熟的方案，搭配好的产品设计可以很好地解决大部分的问题。</p>
<blockquote>
<p>对于一个商城项目来说，它的挑战性不是在于功能的实现逻辑上，而在于部分视觉感受与体验的优化上。如果觉得文章对你有帮助，可以点个👍，给我加个油。如果对前端电商项目想了解更多的Yoyo们可以关注本专栏。</p>
</blockquote>
<h2 data-id="heading-13">近期好文</h2>
<ul>
<li><a href="https://juejin.cn/post/6989751020255445005" target="_blank" title="https://juejin.cn/post/6989751020255445005"># 百万PV商城实践系列 - 前端图片资源优化实战</a></li>
<li><a href="https://juejin.cn/post/6984908770149138446" target="_blank" title="https://juejin.cn/post/6984908770149138446"># 【收藏就会】浏览器WebStorage缓存使用指南</a></li>
<li><a href="https://juejin.cn/post/6976782987480432670" target="_blank" title="https://juejin.cn/post/6976782987480432670"># 我 & 掘金，毕业一年后，我被掘金签约了｜2021 年中总结</a></li>
<li><a href="https://juejin.cn/post/6970841540776329224" target="_blank" title="https://juejin.cn/post/6970841540776329224"># 总结TypeScript在项目开发中的应用实践体会</a></li>
</ul>
<h2 data-id="heading-14">尾注</h2>
<blockquote>
<p>本文首发于：<a href="https://juejin.cn/" target="_blank" title="https://juejin.cn">掘金技术社区</a><br>
类型：签约文章<br>
作者：<a href="https://juejin.cn/user/4248168660735310/posts" target="_blank" title="https://juejin.cn/user/4248168660735310/posts">wangly19</a><br>
收藏于专栏：<a href="https://juejin.cn/column/6984070080191528997" target="_blank" title="https://juejin.cn/column/6984070080191528997"># 百万PV商城实践系列</a><br>
公众号: ItCodes 程序人生</p>
</blockquote></div>  
</div>
            