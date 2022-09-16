
---
title: '听说你至今不晓得缓存淘汰算法？实现LRU、LFU和FIFO？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ec9ac0d6f5a486e834ee5326e981774~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
author: 掘金
comments: false
date: Wed, 14 Sep 2022 17:01:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ec9ac0d6f5a486e834ee5326e981774~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>。<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fslbyml.github.io%2Falgorithm%2Fcache.html" target="_blank" rel="nofollow noopener noreferrer" title="https://slbyml.github.io/algorithm/cache.html" ref="nofollow noopener noreferrer">首发个人博客地址</a></p>
<h2 data-id="heading-0">前言</h2>
<p>我们有一个自制的浏览器程序，现在需要对所有浏览过的页面数据进行缓存，如果页面已经被存储过则直接将数据拿出来进行页面的数据填充来提升访问性能，但是我们的程序是不可能为这部分缓存提供无限大的内存空间，而是要分配一个固定的最大空间来专门做这部分事情。因为这个空间大小的限制，若新访问的页面数据需要存入内存时发现内存空间已经满了，此时我们希望能够删除一些历史缓存数据，从而使新的访问数据可以被存储，此时删除什么样子的缓存数据就成了我们首先需要考虑问题。</p>
<p>一般我们认为，在当前自身业务场景下，淘汰算法中，缓存波动最小，命中率最高，运行性能最好的实现方式就是我们需要的的最优解，所以没有最优，只有最合适！</p>
<h2 data-id="heading-1">最优算法：OPT</h2>
<p>由Belady在1966年提出的理念：优先淘汰以后不会被访问或者最迟才需要被访问的页面，它能保证我们的未来的命中率最高。但现实是很残酷的，这个方法需要我们去预测未来的操作，大部分情况下，未来是无规律可循，是无法预知的，因此也是无法被实现的。但它依然有被存在的意义：那就是为实现算法对性能进行衡量比较。</p>
<h2 data-id="heading-2">先进先出：FIFO</h2>
<p><code>FIFO</code>是所有算法中最容易理解也是最好实现的一种，它的本质就是<code>清除最先进入内存的数据</code>：因为最先进入内存的数据，其不再被使用的可能性比刚进入内存的数据可能性大，也因为这个特性，其在大多数的应用场景下效率不高，命中率比较低，因此使用频率非常低</p>
<p>实现原理：我们通过队列的方式来存储数据，新数据先检测队列内是否有对应的存储，如果有则不做处理，否则插入到队列的末尾，如果在插入时发现队列已经满了，则先删除队列头的数据，在将新数据插入到队列尾
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ec9ac0d6f5a486e834ee5326e981774~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="fifo" loading="lazy" referrerpolicy="no-referrer"><br>
Array：<code>[1,2,3,4,2,5,1,2,4,3]</code>；size：<code>3</code></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">class</span> <span class="hljs-title class_">FIFOCaches</span> &#123;
  <span class="hljs-keyword">private</span> <span class="hljs-attr">caches</span>:<span class="hljs-built_in">number</span>[] = []
  <span class="hljs-keyword">private</span> <span class="hljs-attr">limit</span>:<span class="hljs-built_in">number</span> = <span class="hljs-number">3</span>
  <span class="hljs-title function_">has</span>(<span class="hljs-attr">cache</span>:<span class="hljs-built_in">number</span>):<span class="hljs-built_in">boolean</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">indexOf</span>(cache) >= <span class="hljs-number">0</span>
  &#125;
  <span class="hljs-title function_">getCaches</span>():<span class="hljs-built_in">number</span>[] &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>
  &#125;
  <span class="hljs-title function_">set</span>(<span class="hljs-attr">cache</span>:<span class="hljs-built_in">number</span>):<span class="hljs-built_in">void</span> &#123;
    <span class="hljs-keyword">const</span> isCache = <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">has</span>(cache)
    <span class="hljs-keyword">if</span> (isCache) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-property">length</span> >= <span class="hljs-variable language_">this</span>.<span class="hljs-property">limit</span>) <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">shift</span>();
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">push</span>(cache)
  &#125;
&#125;
<span class="hljs-comment">// test</span>
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>]
<span class="hljs-keyword">const</span> fifo = <span class="hljs-keyword">new</span> <span class="hljs-title class_">FIFOCaches</span>()
arr.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">item</span> =></span> fifo.<span class="hljs-title function_">set</span>(item))
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(fifo.<span class="hljs-title function_">getCaches</span>()) <span class="hljs-comment">// [ 2, 4, 3 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码输出如下：</p>






































































<table><thead><tr><th>访问</th><th>in：1</th><th>in：2</th><th>in：3</th><th>in：4</th><th>in：2</th><th>in：5</th><th>in：1</th><th>in：2</th><th>in：4</th><th>in：3</th></tr></thead><tbody><tr><td>存储</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>3</td><td>4</td><td>5</td><td>1</td><td>2</td></tr><tr><td>存储</td><td></td><td>2</td><td>2</td><td>3</td><td>3</td><td>4</td><td>5</td><td>1</td><td>2</td><td>4</td></tr><tr><td>存储</td><td></td><td></td><td>3</td><td>4</td><td>4</td><td>5</td><td>1</td><td>2</td><td>4</td><td>3</td></tr><tr><td>命中</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td><td>✓</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td></tr></tbody></table>
<h2 data-id="heading-3">最少使用：LFU</h2>
<p>LFU 是 Least Frequently Used 的缩写，也就是<code>优先删除使用频率最低的数据</code>，因为一般我们认为在当前阶段访问次数最少的数据，在未来也是一样的。因此它和数据被访问的次数是息息相关的。</p>
<blockquote>
<p>存在的问题：存在<code>缓存末端抖动</code>；旧的热点数据因为其基数比较高，所以不容被清除。而新的热点数据存储因为其频次基数还比较低，所以总是容易被淘汰。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c6879f0582043df9fbde3945705978c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="lfu" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Array：<code>[1,2,3,4,2,5,1,2,4,3]</code>；size：<code>3</code></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> <span class="hljs-title class_">Icache</span> &#123;
  <span class="hljs-attr">value</span>: <span class="hljs-built_in">number</span>,
  <span class="hljs-attr">freq</span>: <span class="hljs-built_in">number</span>
&#125;
<span class="hljs-keyword">class</span> <span class="hljs-title class_">LFUCache</span> &#123;
  <span class="hljs-keyword">private</span> <span class="hljs-attr">caches</span>:<span class="hljs-title class_">Map</span><<span class="hljs-built_in">number</span>, <span class="hljs-title class_">Icache</span>>=<span class="hljs-keyword">new</span> <span class="hljs-title class_">Map</span>()
  <span class="hljs-keyword">private</span> <span class="hljs-attr">limit</span>:<span class="hljs-built_in">number</span> = <span class="hljs-number">3</span>
   <span class="hljs-title function_">getCaches</span>():<span class="hljs-title class_">Map</span><<span class="hljs-built_in">number</span>, <span class="hljs-title class_">Icache</span>> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>
  &#125;
   <span class="hljs-title function_">set</span>(<span class="hljs-attr">cache</span>:<span class="hljs-built_in">number</span>):<span class="hljs-built_in">void</span> &#123;
    <span class="hljs-keyword">const</span> _cache = <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">get</span>(cache)
    <span class="hljs-keyword">if</span> (_cache) &#123; <span class="hljs-comment">// 有则更新命中次数</span>
      _cache.<span class="hljs-property">freq</span>++
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">set</span>(cache, _cache)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">if</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-property">size</span> >= <span class="hljs-variable language_">this</span>.<span class="hljs-property">limit</span>)&#123; <span class="hljs-comment">// 存储超长则删除使用次数最少的cache</span>
        <span class="hljs-keyword">let</span> minFreqKey = <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">keys</span>().<span class="hljs-title function_">next</span>().<span class="hljs-property">value</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">forEach</span>(<span class="hljs-function">(<span class="hljs-params">item, key</span>) =></span> &#123;
          minFreqKey = (<span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">get</span>(minFreqKey) <span class="hljs-keyword">as</span> <span class="hljs-title class_">Icache</span>).<span class="hljs-property">freq</span> > item.<span class="hljs-property">freq</span> ? key : minFreqKey
        &#125;)
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">delete</span>(minFreqKey)
      &#125;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">set</span>(cache, &#123;<span class="hljs-attr">value</span>: cache, <span class="hljs-attr">freq</span>: <span class="hljs-number">1</span>&#125;)
    &#125;
  &#125;
&#125;
<span class="hljs-comment">// test</span>
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>]
<span class="hljs-keyword">const</span> fifo = <span class="hljs-keyword">new</span> <span class="hljs-title class_">LFUCache</span>()
arr.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">item</span> =></span> fifo.<span class="hljs-title function_">set</span>(item))
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(fifo.<span class="hljs-title function_">getCaches</span>()); <span class="hljs-comment">// 2,4,3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码输出如下：</p>






































































<table><thead><tr><th>访问</th><th>in：1</th><th>in：2</th><th>in：3</th><th>in：4</th><th>in：2</th><th>in：5</th><th>in：1</th><th>in：2</th><th>in：4</th><th>in：3</th></tr></thead><tbody><tr><td>存储</td><td>1(1)</td><td>1(1)</td><td>1(1)</td><td>2(1)</td><td>2(2)</td><td>2(2)</td><td>2(2)</td><td>2(3)</td><td>2(3)</td><td>2(3)</td></tr><tr><td>存储</td><td></td><td>2(1)</td><td>2(1)</td><td>3(1)</td><td>3(1)</td><td>4(1)</td><td>5(1)</td><td>5(1)</td><td>1(1)</td><td>4(1)</td></tr><tr><td>存储</td><td></td><td></td><td>3(1)</td><td>4(1)</td><td>4(1)</td><td>5(1)</td><td>1(1)</td><td>1(1)</td><td>4(1)</td><td>3(1)</td></tr><tr><td>命中</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td><td>✓</td><td>✗</td><td>✗</td><td>✓</td><td>✗</td><td>✗</td></tr></tbody></table>
<h2 data-id="heading-4">最久未使用：LRU</h2>
<p>LRU 是 Least Recently Used 的缩写，<code>LRU算法</code>和<code>OPT算法</code>的理念有些类似，只不过一个分析的是现在，一个分析的是未来。<code>LRU算法清除的是内存中最久没有被访问到的数据</code>。它和数据被创建和最后访问更新的时间息息相关，这种算法算是命中率和使用频率非常高的一种。在vue的<code>keey-alive</code>组件中用的就是这种算法:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fcore%2Fblob%2F0841b9b5243acdaf191099b25e9a145b30189dea%2Fpackages%2Fruntime-core%2Fsrc%2Fcomponents%2FKeepAlive.ts%23L306" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/core/blob/0841b9b5243acdaf191099b25e9a145b30189dea/packages/runtime-core/src/components/KeepAlive.ts#L306" ref="nofollow noopener noreferrer">keeyAlive</a></p>
<blockquote>
<p>存在的问题：缓存污染，当存在偶发性、周期性的批量操作时，访问历史会被大量更新，造成后面的常规数据命中率急剧下降</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7d6fb1f6dc5461789810c79494e5fe8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="lru" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> <span class="hljs-title class_">Icache</span> &#123;
  <span class="hljs-attr">value</span>: <span class="hljs-built_in">number</span>
&#125;
<span class="hljs-keyword">class</span> <span class="hljs-title class_">LRUCache</span> &#123;
  <span class="hljs-keyword">private</span> <span class="hljs-attr">caches</span>:<span class="hljs-title class_">Map</span><<span class="hljs-built_in">number</span>,<span class="hljs-title class_">Icache</span> >=<span class="hljs-keyword">new</span> <span class="hljs-title class_">Map</span>()
  <span class="hljs-keyword">private</span> <span class="hljs-attr">limit</span>:<span class="hljs-built_in">number</span> = <span class="hljs-number">3</span>
   <span class="hljs-title function_">getCaches</span>():<span class="hljs-title class_">Map</span><<span class="hljs-built_in">number</span>,<span class="hljs-title class_">Icache</span> > &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>
  &#125;
  <span class="hljs-title function_">get</span>(<span class="hljs-params">cache:<span class="hljs-built_in">number</span></span>)&#123; <span class="hljs-comment">//数据被访问，就更新缓存</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">has</span>(cache)) &#123; <span class="hljs-comment">// 存在即更新</span>
      <span class="hljs-keyword">let</span> temp = <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">get</span>(cache);
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">delete</span>(cache);
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">set</span>(cache, &#123;<span class="hljs-attr">value</span>:cache&#125;);
      <span class="hljs-keyword">return</span> temp;
    &#125;
    <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
  &#125;
   <span class="hljs-title function_">set</span>(<span class="hljs-attr">cache</span>:<span class="hljs-built_in">number</span>):<span class="hljs-built_in">void</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">has</span>(cache)) &#123;<span class="hljs-comment">// 存在即更新（删除后加入）</span>
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">delete</span>(cache);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-property">size</span> >= <span class="hljs-variable language_">this</span>.<span class="hljs-property">limit</span>) &#123; <span class="hljs-comment">// 缓存超过最大值，则移除最近没有使用的</span>
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">delete</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">keys</span>().<span class="hljs-title function_">next</span>().<span class="hljs-property">value</span>);
    &#125;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">caches</span>.<span class="hljs-title function_">set</span>(cache,&#123;<span class="hljs-attr">value</span>:cache&#125;);
  &#125;
&#125;
<span class="hljs-comment">// test</span>
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>]
<span class="hljs-keyword">const</span> fifo = <span class="hljs-keyword">new</span> <span class="hljs-title class_">LRUCache</span>()
arr.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">item</span> =></span> fifo.<span class="hljs-title function_">set</span>(item))
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(fifo.<span class="hljs-title function_">getCaches</span>()); <span class="hljs-comment">//2、4、3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fslbyml.github.io%2Falgorithm%2Fmedium.html%23lru%25E7%25AE%2597%25E6%25B3%2595leetcode146" target="_blank" rel="nofollow noopener noreferrer" title="https://slbyml.github.io/algorithm/medium.html#lru%E7%AE%97%E6%B3%95leetcode146" ref="nofollow noopener noreferrer">leetcode146</a>;代码输出如下：</p>






































































<table><thead><tr><th>访问</th><th>in：1</th><th>in：2</th><th>in：3</th><th>in：4</th><th>in：2</th><th>in：5</th><th>in：1</th><th>in：2</th><th>in：4</th><th>in：3</th></tr></thead><tbody><tr><td>存储</td><td>1</td><td>1</td><td>1</td><td>2</td><td>3</td><td>4</td><td>2</td><td>5</td><td>1</td><td>2</td></tr><tr><td>存储</td><td></td><td>2</td><td>2</td><td>3</td><td>4</td><td>2</td><td>5</td><td>1</td><td>2</td><td>4</td></tr><tr><td>存储</td><td></td><td></td><td>3</td><td>4</td><td>2</td><td>5</td><td>1</td><td>2</td><td>4</td><td>3</td></tr><tr><td>命中</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td><td>✓</td><td>✗</td><td>✗</td><td>✓</td><td>✗</td><td>✗</td></tr></tbody></table>
<h2 data-id="heading-5">优化LRU：LRU-K&Two queues(2Q)&MQ</h2>
<p>很多业务中的最优算法都不是独立存在的，而是结合多种算法，继承他们的优点进行使用，LRU-K就是这样；其中K代表最近使用次数，我们可以认为上面的算法为<code>LRU-1</code>。此算法就是为了解决上面提到的“缓存污染”的问题，它的核心思想就是增加一个缓冲区：最近使用小于K次时进入缓冲队列，大于K次则进入LRUcache内。</p>
<p><code>2Q算法</code>是<code>LRU-2</code>的一种具体实现，它的缓冲区规定使用<code>FIFO</code>来实现</p>
<ul>
<li>优先从LRUcache中查找数据，如果命中则将数据取出来重新加入到LRUcache缓存末尾</li>
<li>当缓存穿透则在缓冲队列内查看是否命中</li>
<li>当缓冲队列内命中，则将该数据在队列内索引+1，否则将数据加入缓冲队列</li>
<li>当缓冲队列的索引达到了K，则将其从队列内删除并加入到LRUcache内</li>
<li>如果在插入时LRUcache已满，则按照LRU逻辑将最久未使用的数据置换掉，然后在插入到LRUcache末尾</li>
</ul>
<p>具体代码实现可以结合上面算法来实现：FIFO(作为缓冲历史队列)+LRU(作为LRUcache)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bff1aa9db0741de94db9daa06037b6c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="lru-k" loading="lazy" referrerpolicy="no-referrer"><br>
在实际环境中，K越大，命中率就越高，但却需要更多的访问才能将缓存记录替换掉，因此适用性可能并没有那么大，而<code>LUR-2</code>可能是综合各种因素后最优的选择，</p>
<p>当然还有更加进阶的<code>LRU-Multi queues(MQ)算法</code>，在LRU基础上增加了多个缓冲队列，是<code>2Q</code>的扩展，每个队列对应不同的优先级，根据淘汰算法进行相应的升级和降级处理，此算法复杂度相对较高、成本比较大</p>
<h2 data-id="heading-6">参考：</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fslbyml.github.io%2Falgorithm%2Fcache.html" target="_blank" rel="nofollow noopener noreferrer" title="https://slbyml.github.io/algorithm/cache.html" ref="nofollow noopener noreferrer">博主本人博客</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fu010223431%2Farticle%2Fdetails%2F105498387" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/u010223431/article/details/105498387" ref="nofollow noopener noreferrer">LRU算法及其变种算法原理分析</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FsuperSmart_Dong%2Farticle%2Fdetails%2F116276642" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/superSmart_Dong/article/details/116276642" ref="nofollow noopener noreferrer">操作系统原理：页置换算法</a></p></div>  
</div>
            