
---
title: 'LeetCode算法学习之--数组--三数之和'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f09042ed0d5400a8c63189e9611fe7f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 01:34:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f09042ed0d5400a8c63189e9611fe7f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好今天给大家分享下一道 LeetCode  中等难度 的题目 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2F3sum%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/3sum/" ref="nofollow noopener noreferrer">三数之和</a></p>
<blockquote>
<p>这里主要是分享思路和注释，供大家更好的理解题目解法，代码部分是参考LeetCode 转写成javascript 代码，</p>
</blockquote>
<h4 data-id="heading-0">题目</h4>
<blockquote>
<p>给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。</p>
<p>注意：答案中不可以包含重复的三元组。</p>
<pre><code class="hljs language-markdown copyable" lang="markdown">示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]


<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h4 data-id="heading-1">分析</h4>
<blockquote>
<p><em>1.为了去重需要排序+使用Set</em></p>
<p><em>2.因为暴力法是3层迭代，时间复杂度是O（n^3）,所以想办法找到k同时减低复杂度是关键</em></p>
<p><em>一种有三种解法</em></p>
<p><em>1.暴力法 O(n^3)</em></p>
<p><em>2.Set值的方式减少时间复杂度,因为set查询为O(1)</em></p>
<p><em>3.双指针内夹 O(n^2)</em></p>
</blockquote>
<h4 data-id="heading-2">解法一：<em>暴力法</em>（通过不了，只提供思路）</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">思路
<span class="hljs-number">1.</span>三层遍历数组 判断每一种可能性
<span class="hljs-number">2.</span>添加set 来防止重复
<span class="hljs-number">3.</span>一定要排序，不然会统计到重复的数据
*/
<span class="hljs-keyword">var</span> threeSum = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">nums</span>) </span>&#123;
  <span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
  <span class="hljs-keyword">const</span> res = [];
  <span class="hljs-comment">//  一定要排序 不然组合不好统计 例如 [[-1,0,1],[-1,2,-1],[0,1,-1]]</span>
  nums.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b);
  <span class="hljs-comment">// 第一层可以是 nums.length - 2, 因为给 j 和k 留2个位置，同理如下</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < nums.length - <span class="hljs-number">2</span>; i++) &#123;
    <span class="hljs-comment">// 第二层的起点是 j=i+1,因为是题目不能同一个位置上的同一个元素不能选择2次，同理如下</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = i + <span class="hljs-number">1</span>; j < nums.length - <span class="hljs-number">1</span>; j++) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k = j + <span class="hljs-number">1</span>; k < nums.length; k++) &#123;
        <span class="hljs-keyword">const</span> key = nums[i] + <span class="hljs-string">"_"</span> + nums[j] + <span class="hljs-string">"_"</span> + nums[k];
        <span class="hljs-keyword">if</span> (nums[i] + nums[k] + nums[j] === <span class="hljs-number">0</span> && !set.has(key)) &#123;
          res.push([nums[i], nums[k], nums[j]]);
          set.add(key);
        &#125;
      &#125;
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> res;
&#125;;

<span class="hljs-comment">/* 复杂度
时间 O(n^3)
空间 O(1)
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">解法二：<em><strong>Set 法</strong></em></h4>
<p>代码借鉴 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2F3sum%2Fsolution%2Fsan-shu-zhi-he-javajian-ji-ti-jie-by-wang-zi-hao-z%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-javajian-ji-ti-jie-by-wang-zi-hao-z/" ref="nofollow noopener noreferrer">leetcode-cn.com/problems/3s…</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-number">1.</span>排序 避免重复，
<span class="hljs-number">2.</span>因为不能有重复的三元组，所以利用<span class="hljs-built_in">Set</span> 来去重
<span class="hljs-number">3.</span>采用遍历的方式， 看下是否能获取 三个元素相加为<span class="hljs-number">0</span> 的情况
<span class="hljs-number">4.</span>暴力法不同的地方在于， 不再采用第三层遍历，而是使用<span class="hljs-built_in">Set</span>的方法来判断是否存在 v= -nums[i] - nums[j],
因为set的查询时间复杂度为O(<span class="hljs-number">1</span>) 所以总的复杂度为O(n^<span class="hljs-number">2</span>)
*/

<span class="hljs-keyword">var</span> threeSum = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">nums</span>) </span>&#123;
  <span class="hljs-keyword">const</span> res = [];
  <span class="hljs-comment">// 去重使用</span>
  <span class="hljs-keyword">const</span> uniqueSet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
  nums.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b);

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < nums.length - <span class="hljs-number">1</span>; i++) &#123;
    <span class="hljs-comment">// 存放 nums[j]的值</span>
    <span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = i + <span class="hljs-number">1</span>; j < nums.length; j++) &#123;
      <span class="hljs-comment">// 需要求得的值</span>
      <span class="hljs-keyword">const</span> v = -nums[i] - nums[j];
      <span class="hljs-comment">// 三元数组的唯一标识，放入set中防止重复取值</span>
      <span class="hljs-keyword">const</span> str = nums[i] + <span class="hljs-string">"_"</span> + v + <span class="hljs-string">"_"</span> + nums[j];
      <span class="hljs-keyword">if</span> (set.has(v) && !uniqueSet.has(str)) &#123;
        res.push([nums[i], v, nums[j]]);
        uniqueSet.add(str);
      &#125; <span class="hljs-keyword">else</span> &#123;
        set.add(nums[j]);
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> res;
&#125;;

<span class="hljs-comment">/* 复杂都
时间 O(n^2)
空间 O(n)
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f09042ed0d5400a8c63189e9611fe7f~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">解法二：<strong><strong>双指针</strong></strong></h4>
<p>代码借鉴 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2F3sum%2Fsolution%2Fhua-jie-suan-fa-15-san-shu-zhi-he-by-guanpengchn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/3sum/solution/hua-jie-suan-fa-15-san-shu-zhi-he-by-guanpengchn/" ref="nofollow noopener noreferrer">leetcode-cn.com/problems/3s…</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">思路
<span class="hljs-number">1.</span>排序防止重复
<span class="hljs-number">2.</span>遍历一次元素，获取一个三个元素中的一个，nums[i],
<span class="hljs-number">3.</span>再次遍历一次数组，利用双指针 左边放置一个指针j 右边放置一个指针k，往中间内夹
令 sum = nums[i]+nums[j]+nums[k]，因为数组有序
如果sum><span class="hljs-number">0</span> 则左边k对应的值大了 所以应该
*/

<span class="hljs-keyword">var</span> threeSum = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">nums</span>) </span>&#123;
  <span class="hljs-keyword">const</span> res = [];
  <span class="hljs-comment">// 老规矩 排序防止重复的情况发生</span>
  nums.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b);
  <span class="hljs-comment">// 遍历</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < nums.length; i++) &#123;
    <span class="hljs-comment">// 如果nums[i]都已经大于0了， 那么其他元素相加不可能再等于零 所以直接break</span>
    <span class="hljs-keyword">if</span> (nums[i] > <span class="hljs-number">0</span>) <span class="hljs-keyword">break</span>;
    <span class="hljs-comment">// 说明有重复， 但是不能判断 nums[i]===nums[i+1]的时候就continue 因为会错过元素例如（-1,-1，2） 这种情况就会被错过</span>
    <span class="hljs-keyword">if</span> (i > <span class="hljs-number">0</span> && nums[i - <span class="hljs-number">1</span>] === nums[i]) <span class="hljs-keyword">continue</span>;

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = i + <span class="hljs-number">1</span>, k = nums.length - <span class="hljs-number">1</span>; j < k; ) &#123;
      <span class="hljs-keyword">const</span> sum = nums[i] + nums[j] + nums[k];
      <span class="hljs-comment">// 说明nums[k]大了， 所以需要k--</span>
      <span class="hljs-keyword">if</span> (sum > <span class="hljs-number">0</span>) &#123;
        k--;
        <span class="hljs-comment">// 说明nums[j]小了， 所以需要j++</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sum < <span class="hljs-number">0</span>) &#123;
        j++;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 说明找到了答案了</span>
        res.push([nums[i], nums[j], nums[k]]);
        <span class="hljs-keyword">while</span> (j < k && nums[j] === nums[j + <span class="hljs-number">1</span>]) j++;
        <span class="hljs-keyword">while</span> (j < k && nums[k] === nums[k - <span class="hljs-number">1</span>]) k--;
        j++;
        k--;
      &#125;
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> res;
&#125;;
<span class="hljs-comment">/* 复杂度
时间 O(n^2)
空间 O(1)
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79f35241c15e43a6882fd5d1123d4910~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">总结</h4>
<p>这道题 ，考察大家对双指针 和 Set的理解，因为他们可以很好的降低时间复杂度</p>
<p>大家可以看看我分享的一个专栏（<a href="https://juejin.cn/column/6984791578099335204" target="_blank" title="https://juejin.cn/column/6984791578099335204">前端搞算法</a>）里面有更多关于算法的题目的分享，希望能够帮到大家，我会尽量保持每天晚上更新，如果喜欢的麻烦帮我点个赞，十分感谢</p>
<p><em>文章内容目的在于学习讨论与分享学习算法过程中的心得体会，文中部分素材来源网络，如有侵权，请联系删除，邮箱 <a href="https://link.juejin.cn/?target=mailto%3A182450609%40qq.com" target="_blank" title="mailto:182450609@qq.com" ref="nofollow noopener noreferrer">182450609@qq.com</a></em></p>
<p><strong>今天很有幸的去支持了下鸿星尔克和蜜雪冰城，不得不说为中国的良心企业点赞，为我的祖国感到骄傲，郑州加油！河南加油！中国加油！</strong></p></div>  
</div>
            