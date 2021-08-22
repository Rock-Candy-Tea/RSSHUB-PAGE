
---
title: 'leetcode刷题-贪心'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1161'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 06:32:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=1161'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">leetcode刷题-贪心</h1>
<p>保证每次操作都是局部最优的，并且最后得到的结果是全局最优的</p>
<h2 data-id="heading-1">1. <a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fassign-cookies%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/assign-cookies/" ref="nofollow noopener noreferrer">分发饼干</a></h2>
<h3 data-id="heading-2">题目</h3>
<p>假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。</p>
<p>对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。</p>
<h3 data-id="heading-3">思路</h3>
<p>典型的贪心算法</p>
<p>证明：假设在某次选择中，贪心策略选择给当前满足度最小的孩子分配第M个饼干，第M个饼干为可以满足该孩子的最小饼干； 假设存在一种最优策略，给该孩子分配第N个饼干，并且M<N,可以发现，经过这一轮的分配，<strong>贪心策略分配后剩下的饼干一定有一个比最优策略来得大</strong>。因此，在后续的分配中，贪心策略一定能够满足更多的孩子，也就是说贪心策略也就是最优策略。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> findContentChildren = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">g, s</span>) </span>&#123;
  g.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b);
  s.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b);

  <span class="hljs-keyword">let</span> gi = <span class="hljs-number">0</span>, si = <span class="hljs-number">0</span>;
  
  <span class="hljs-keyword">while</span>(gi < g.length && si < s.length) &#123;
    <span class="hljs-keyword">if</span> (g[gi] <= s[si]) &#123;
      gi++;
    &#125;
    si++;
  &#125;

  <span class="hljs-keyword">return</span> gi;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">2. <a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fnon-overlapping-intervals%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/non-overlapping-intervals/" ref="nofollow noopener noreferrer">无重叠区间</a></h2>
<h3 data-id="heading-5">题目</h3>
<p>给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。</p>
<p>注意:</p>
<p>可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。</p>
<h3 data-id="heading-6">思路</h3>
<ul>
<li>先计算最多能组成的不重叠的区间个数，然后用区间总个数减去不重叠的区间的个数</li>
<li>如何计算出最多的不重叠区间的个数？ 贪心：每次选择结尾最小的区间，因为选择的区间结尾越小，留给后面的区间的空间越大，后面能够选择的区间个数也越大</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> eraseOverlapIntervals = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">intervals</span>) </span>&#123;
  intervals.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a[<span class="hljs-number">1</span>] - b[<span class="hljs-number">1</span>]);
  <span class="hljs-keyword">let</span> count = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">let</span> end = intervals[<span class="hljs-number">0</span>][<span class="hljs-number">1</span>];

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < intervals.length; i++) &#123;
    <span class="hljs-keyword">const</span> item = intervals[i];
    <span class="hljs-keyword">if</span> (item[<span class="hljs-number">0</span>] < end) &#123;
      <span class="hljs-keyword">continue</span>;
    &#125;
    count++;
    end = item[<span class="hljs-number">1</span>];
  &#125;

  <span class="hljs-keyword">return</span> intervals.length - count;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3. <a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fminimum-number-of-arrows-to-burst-balloons%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/" ref="nofollow noopener noreferrer">用最少数量的箭引爆气球</a></h2>
<h3 data-id="heading-8">题目</h3>
<p>在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。</p>
<p>一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。</p>
<p>给你一个数组 points ，其中 points [i] = [xstart,xend] ，返回引爆所有气球所必须射出的最小弓箭数。</p>
<h3 data-id="heading-9">思路</h3>
<p>第二题的变种</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> findMinArrowShots = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">points</span>) </span>&#123;
  points.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a[<span class="hljs-number">1</span>] - b[<span class="hljs-number">1</span>]);

  <span class="hljs-keyword">let</span> count = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">let</span> minEnd = points[<span class="hljs-number">0</span>][<span class="hljs-number">1</span>];

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < points.length; i++) &#123;
    <span class="hljs-keyword">const</span> item = points[i];

    <span class="hljs-keyword">if</span> (item[<span class="hljs-number">0</span>] <= minEnd) &#123;
      <span class="hljs-keyword">continue</span>;
    &#125;

    count++;
    minEnd = item[<span class="hljs-number">1</span>];
  &#125;

  <span class="hljs-keyword">return</span> count;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">4. <a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fqueue-reconstruction-by-height%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/queue-reconstruction-by-height/" ref="nofollow noopener noreferrer">根据身高重建队列</a></h2>
<h3 data-id="heading-11">题目</h3>
<p>假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。</p>
<p>请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。</p>
<h3 data-id="heading-12">思路</h3>
<p>身高降序，K值升序，然后按排好序的顺序插入队列的第K个位置中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> reconstructQueue = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">people</span>) </span>&#123;
  people.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a[<span class="hljs-number">0</span>] === b[<span class="hljs-number">0</span>] ? a[<span class="hljs-number">1</span>] - b[<span class="hljs-number">1</span>] : b[<span class="hljs-number">0</span>] - a[<span class="hljs-number">0</span>])
  <span class="hljs-keyword">const</span> resArr = [];

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < people.length; i++) &#123;
    <span class="hljs-keyword">const</span> item = people[i];
    resArr.splice(item[<span class="hljs-number">1</span>], <span class="hljs-number">0</span>, item);
  &#125;

  <span class="hljs-keyword">return</span> resArr;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">5. <a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fpartition-labels%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/partition-labels/" ref="nofollow noopener noreferrer">划分字母区间</a></h2>
<h3 data-id="heading-14">题目</h3>
<p>字符串 <code>S</code> 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> partitionLabels = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">s</span>) </span>&#123;
  <span class="hljs-keyword">const</span> letterArr = initArr(s);
  letterArr.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a[<span class="hljs-number">0</span>] - b[<span class="hljs-number">0</span>]);
  <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < letterArr.length; i++) &#123;
    <span class="hljs-keyword">if</span> (letterArr[i][<span class="hljs-number">0</span>] !== -<span class="hljs-number">1</span>) &#123;
      index = i;
      <span class="hljs-keyword">break</span>;
    &#125;
  &#125;

  <span class="hljs-keyword">let</span> begin = letterArr[index][<span class="hljs-number">0</span>];
  <span class="hljs-keyword">let</span> end = letterArr[index][<span class="hljs-number">1</span>];
  <span class="hljs-keyword">const</span> res = [];

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = index + <span class="hljs-number">1</span>; i < letterArr.length; i++) &#123;
    <span class="hljs-keyword">const</span> item = letterArr[i];
    <span class="hljs-keyword">if</span> (item[<span class="hljs-number">0</span>] < end) &#123;
      end = <span class="hljs-built_in">Math</span>.max(end, item[<span class="hljs-number">1</span>]);
    &#125; <span class="hljs-keyword">else</span> &#123;
      res.push(end - begin + <span class="hljs-number">1</span>);
      begin = item[<span class="hljs-number">0</span>];
      end = item[<span class="hljs-number">1</span>];
    &#125;
  &#125;

  res.push(end - begin + <span class="hljs-number">1</span>);

  <span class="hljs-keyword">return</span> res;
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initArr</span>(<span class="hljs-params">s</span>) </span>&#123;
  <span class="hljs-keyword">const</span> letterArr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">26</span>);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">26</span>; i++) &#123;
    letterArr[i] = [-<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>];
  &#125;
  <span class="hljs-keyword">const</span> lettera = <span class="hljs-string">'a'</span>.charCodeAt();
  <span class="hljs-keyword">const</span> sArr = s.split(<span class="hljs-string">''</span>);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < s.length; i++) &#123;
    <span class="hljs-keyword">const</span> code = sArr[i].charCodeAt() - lettera;
    <span class="hljs-keyword">if</span> (letterArr[code][<span class="hljs-number">0</span>] === -<span class="hljs-number">1</span>) &#123;
      letterArr[code][<span class="hljs-number">0</span>] = i;
    &#125;
    letterArr[code][<span class="hljs-number">1</span>] = i;
  &#125;

  <span class="hljs-keyword">return</span> letterArr;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">6、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fcan-place-flowers%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/can-place-flowers/" ref="nofollow noopener noreferrer">种花问题</a></h2>
<h3 data-id="heading-16">题目</h3>
<p>假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。</p>
<p>给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> canPlaceFlowers = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">flowerbed, n</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (n === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>; 

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len = flowerbed.length; i < len; i++) &#123;
    <span class="hljs-keyword">if</span> (flowerbed[i] === <span class="hljs-number">1</span>) &#123; <span class="hljs-comment">// 等于1的时候，直接跳2格</span>
      i += <span class="hljs-number">1</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 等于0且能够种花</span>
      <span class="hljs-keyword">if</span> ((i + <span class="hljs-number">1</span> === len) || (i + <span class="hljs-number">1</span> < len && flowerbed[i + <span class="hljs-number">1</span>] === <span class="hljs-number">0</span>)) &#123;
        n--;
        <span class="hljs-keyword">if</span> (n === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        i += <span class="hljs-number">1</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 等于0的时候但是不能种花，直接跳2个格</span>
        i += <span class="hljs-number">2</span>;
      &#125;
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> n === <span class="hljs-number">0</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">7、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fis-subsequence%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/is-subsequence/" ref="nofollow noopener noreferrer">判断子序列</a></h2>
<p>给定字符串 s 和 t ，判断 s 是否为 t 的子序列。</p>
<p>字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> isSubsequence = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s, t</span>) </span>&#123;
  <span class="hljs-keyword">const</span> m = s.length, n = t.length;
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, j = <span class="hljs-number">0</span>;

  <span class="hljs-keyword">while</span>(i < m && j < n) &#123;
    <span class="hljs-keyword">if</span> (s[i] === t[j]) &#123;
      i++;
    &#125;
    j++;
  &#125;

  <span class="hljs-keyword">return</span> i === m;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">8、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fnon-decreasing-array%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/non-decreasing-array/" ref="nofollow noopener noreferrer">非递减数列</a>（重要）</h2>
<p>给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。</p>
<p>我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> checkPossibility = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
  <span class="hljs-keyword">const</span> n = nums.length;
  <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n; i++) &#123;
    <span class="hljs-keyword">const</span> x = nums[i], y = nums[i + <span class="hljs-number">1</span>];
    <span class="hljs-keyword">if</span> (x > y) &#123;
      count++;
      <span class="hljs-keyword">if</span> (count > <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
      <span class="hljs-keyword">if</span> (i > <span class="hljs-number">0</span> && y < nums[i - <span class="hljs-number">1</span>]) &#123;
        nums[i + <span class="hljs-number">1</span>] = x;
      &#125;
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">9、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fbest-time-to-buy-and-sell-stock-ii%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/" ref="nofollow noopener noreferrer">买卖股票的最佳时机 II</a></h2>
<p>给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。</p>
<p>设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> maxProfit = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">prices</span>) </span>&#123;
  <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < prices.length; i++) &#123;
    <span class="hljs-keyword">if</span> (i + <span class="hljs-number">1</span> && prices[i + <span class="hljs-number">1</span>] > prices[i]) &#123;
      sum += (prices[i + <span class="hljs-number">1</span>] - prices[i]);
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> sum;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">10、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fmaximum-subarray%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/maximum-subarray/" ref="nofollow noopener noreferrer">最大子序和</a></h2>
<p>给定一个整数数组 <code>nums</code> ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。</p>
<h3 data-id="heading-21">思路</h3>
<p>动态规划：<code>f(i)</code>表示以i元素为结尾的连续子数组的最大和</p>
<pre><code class="hljs language-js copyable" lang="js">f(i) = <span class="hljs-built_in">Math</span>.max(f(i-<span class="hljs-number">1</span>) + x, x);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> maxSubArray = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
  <span class="hljs-keyword">let</span> res = nums[<span class="hljs-number">0</span>];
  <span class="hljs-keyword">let</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>();
  arr[<span class="hljs-number">0</span>] = nums[<span class="hljs-number">0</span>];

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < nums.length; i++) &#123;
    arr[i] = <span class="hljs-built_in">Math</span>.max(arr[i - <span class="hljs-number">1</span>] + nums[i], nums[i]);
    res = <span class="hljs-built_in">Math</span>.max(res, arr[i]);
  &#125;

  <span class="hljs-keyword">return</span> res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">11、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fbest-time-to-buy-and-sell-stock%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/" ref="nofollow noopener noreferrer">买卖股票的最佳时机</a></h2>
<p>给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。</p>
<p>你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。</p>
<p>返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> maxProfit = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">prices</span>) </span>&#123;
  <span class="hljs-keyword">let</span> res = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">let</span> minArr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(prices.length).fill(<span class="hljs-number">10001</span>);
  minArr[<span class="hljs-number">0</span>] = prices[<span class="hljs-number">0</span>];

  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < prices.length; i++) &#123;
    minArr[i] = <span class="hljs-built_in">Math</span>.min(minArr[i - <span class="hljs-number">1</span>], prices[i]);
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < prices.length; i++) &#123;
    res = <span class="hljs-built_in">Math</span>.max(prices[i] - minArr[i], res);
  &#125;

  <span class="hljs-keyword">return</span> res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            