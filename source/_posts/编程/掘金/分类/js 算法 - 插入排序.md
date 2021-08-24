
---
title: 'js 算法 - 插入排序'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc78a970377f449f9b32fc8877b87de3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 19:28:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc78a970377f449f9b32fc8877b87de3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h1 data-id="heading-0">插入排序</h1>
<p>插入排序是一种简单的排序算法，插入排序将一组数据分为有序区间和无序区间，每次从无序区间找到合适的一个数据插入到有序区间的合适位置，当无序区间没数据，即只剩下有序区间时，这组数据就变为完全有序。</p>
<h2 data-id="heading-1">算法描述</h2>
<p>假设是从小到大排序</p>
<ol>
<li>将一组数据的首个数据组成有序区间，其他数据组成无序区间</li>
<li>在无序区间抽出首个数据 A</li>
<li>A 依次与有序区间的各个数据进行对比。若遇到数据比 A 大的，则将 A 插入到该数据的前面一个位置，若 A 比有序区间的任何数据都要大，则插入到有序区间末尾。总之，保证插入后的有序区间依然有序。</li>
<li>重复 2 和 3 操作，直到无序区间没有数据</li>
</ol>
<h2 data-id="heading-2">算法图解</h2>
<p>假设一组数据里有：3、5、4、1、2。</p>
<p>“第一次插入”步骤，3 作为一个有序区间，5、4、1、2 作为无序区间。标记无序区间的首个数据 5，与有序区间的数据 3 作对比，5 比 3 大，由于有序区间后面没有数据了，所以 5 插入到有序区间的 3 后面。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc78a970377f449f9b32fc8877b87de3~tplv-k3u1fbpfcp-watermark.image" alt="1629774503(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>“第二次插入”步骤，3、5 作为有序区间，4、1、2 作为无序区间。标记无序区间的首个数据 4，与有序区间的 3 作对比，4 比 3 大，因此需要继续与后面一个数据对比。4 与有序区间的 5 作对比，比 5 小，因此 4 插入到有序区间的 5 的前面。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/672768bcd1c54768bc25967ecaefae97~tplv-k3u1fbpfcp-watermark.image" alt="1629774541(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>“第三次插入”步骤，同样地，标记无序区间的首个数据 1，1 与有序区间的 3 对比，1 比 3 小，插入到 3 的前面。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ed82da4b8ef4f4cb42206c4f4193580~tplv-k3u1fbpfcp-watermark.image" alt="1629774573(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>“第四次插入”步骤，无序区间唯一的数据 2，比有序区间的 1 大，比有序区间的 3 小，因此插入 3 的前面。到了这里，整组数据就已经达到了完全有序。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0efa001305144c690de77348c71863e~tplv-k3u1fbpfcp-watermark.image" alt="1629774600(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有没有发现，插入排序特别像抽扑克牌？</p>
<p>手上的牌是有序区间，放在桌子上的牌堆是无序区间，每次抽牌时，都要依次与手上的每张牌进行对比，并将该牌插入到相应的位置，保证手上的牌有序。当牌堆抽完了，手上的整副扑克牌就是有序了。</p>
<h1 data-id="heading-3">代码实现</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 插入排序</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">insertionSort</span>(<span class="hljs-params">arr</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (arr.length <= <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> arr
  &#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i=<span class="hljs-number">1</span>; i<arr.length; i++) &#123;
    <span class="hljs-keyword">var</span> j = i - <span class="hljs-number">1</span> <span class="hljs-comment">// j 是有序区间的最大下标</span>
    <span class="hljs-keyword">var</span> val = arr[i] <span class="hljs-comment">// val 是无序区间的首个数据，用来与有序区间的各个数做对比</span>
    <span class="hljs-keyword">for</span> (; j>=<span class="hljs-number">0</span>; j--) &#123;
      <span class="hljs-keyword">if</span> (arr[j] > val) &#123; <span class="hljs-comment">// 由于要求排序从小到大，也就是说 val 比 arr[j] 小的时候，val 需要排在 arr[j] 前面，arr[j] 需要移位</span>
        arr[j+<span class="hljs-number">1</span>] = arr[j]
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">break</span> <span class="hljs-comment">// 当不需要移位时，由于有序区间是有序的，直接跳出循环即可</span>
      &#125;
    &#125;
    arr[j+<span class="hljs-number">1</span>] = val
  &#125;
  <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>





















<table><thead><tr><th></th><th>原地排序</th><th>稳定性</th><th>最好时间复杂度</th><th>最坏时间复杂度</th><th>平均时间复杂度</th></tr></thead><tbody><tr><td>插入排序</td><td>是</td><td>稳定</td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td></tr></tbody></table>
<p>插入排序其实是可以改进优化的，优化版的插入排序叫希尔排序，后面再做介绍。</p>
<h1 data-id="heading-4">js 算法系列文章推荐</h1>
<ul>
<li><a href="https://juejin.cn/post/6998423128753831950" target="_blank" title="https://juejin.cn/post/6998423128753831950">js 算法 - 冒泡排序 (juejin.cn)</a></li>
</ul></div>  
</div>
            