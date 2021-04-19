
---
title: '前端刷题路-Day21｜刷题打卡'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5123'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 16:30:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=5123'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>掘金团队号上线，助你 Offer 临门！ 点击 <a href="https://juejin.cn/offer" target="_blank">查看详情</a></p>
<h3 data-id="heading-0">爬楼梯（题号70）</h3>
<h4 data-id="heading-1">题目</h4>
<p>假设你正在爬楼梯。需要 <code>n</code> 阶你才能到达楼顶。</p>
<p>每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>
<p>注意：给定 <code>n</code> 是一个正整数。</p>
<p>示例 1：</p>
<pre><code class="copyable">输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。

1.  1 阶 + 1 阶
2.  2 阶
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<pre><code class="copyable">输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。

1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">链接</h4>
<p><a href="https://leetcode-cn.com/problems/climbing-stairs/" target="_blank" rel="nofollow noopener noreferrer">leetcode-cn.com/problems/cl…</a></p>
<h4 data-id="heading-3">解释</h4>
<p>乍一看一脸懵逼，仔细一看就是斐波那契数列，问题迎刃而解。</p>
<h4 data-id="heading-4">自己的答案（简单递归）</h4>
<pre><code class="copyable">var climbStairs = function(n) &#123;
  if (n <= 2) return n
  return climbStairs(n - 2) + climbStairs(n - 1)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>确实很简单，但递归次数太多，会直接超时，无法采用</p>
<h4 data-id="heading-5">自己的答案（递归+记忆化）</h4>
<pre><code class="copyable">var climbStairs = function(n) &#123;
  var res = [0,  1, 2]
  function findNum(n) &#123;
    if (!res[n]) &#123;
      res[n] = (res[n - 1] || findNum(n - 1)) + (res[n - 2] || findNum(n - 2))
      return res[n]
    &#125;
    return res[n]
  &#125;
  return findNum(n)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用<code>res</code>存储已经算过的值，如果有直接取，如果没有则开始i计算。</p>
<p>其实这种方法的性能已经不错了，跑了几次，最高能到90%以上，也不知道为啥，但仍然有更优解。</p>
<h4 data-id="heading-6">自己的答案（动态规划）</h4>
<pre><code class="copyable">var climbStairs = function(n) &#123;
  var res = [0, 1, 2]
  for (let i = 3; i < n + 1; i++) &#123;
    res[i] = res[i - 1] + res[i - 2]
  &#125;
  return res[n]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先给<code>res</code>赋值，为了解决<code>n</code>是1或者2的情况。</p>
<p>之后从3开始循环，直到<code>i</code>等于<code>n</code>，每次新的<code>i</code>值等于前两位的和。</p>
<p>最后取<code>res</code>的最后一位即可。</p>
<p>倒序思想，从小到大递增，简单易懂。</p>
<h4 data-id="heading-7">自己的答案（动态规划升级）</h4>
<p>从👆的答案可以看出来，其实每次<code>n</code>只要取<code>n-1</code>和<code>n-2</code>的值即可，那么数组里是不是只要留两个值就行了？答案是可以的：</p>
<pre><code class="copyable">var climbStairs = function(n) &#123;
  if (n <= 2) return n
  var res = [1, 2]
  for (let i = 3; i < n + 1; i++) &#123;
    res = [res[1], res[0] + res[1]]
  &#125;
  return res[1]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然了，其实用两个变量来代替<code>res[0]</code>和<code>res[1]</code>也可以，性能上的细微差别。</p>
<h4 data-id="heading-8">更好的方法</h4>
<p>更好的方法当然是有的，但笔者这辈子是不可能想出来的，有两种：</p>
<ol>
<li>
<h4 data-id="heading-9">矩阵快速幂</h4>
</li>
<li>
<h4 data-id="heading-10">通项公式</h4>
</li>
</ol>
<p>有兴趣的同学可以看看LeetCode的官方题解，说的比较详细：<a href="https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/" target="_blank" rel="nofollow noopener noreferrer">leetcode-cn.com/problems/cl…</a></p>
<br>
<br>
<p>PS：想查看往期文章和题目可以点击下面的链接：</p>
<p>这里是按照日期分类的👇</p>
<p><a href="https://juejin.cn/post/6943975117349191711" target="_blank">前端刷题路-目录（日期分类）</a></p>
<p>经过有些朋友的提醒，感觉也应该按照题型分类<br>
这里是按照题型分类的👇</p>
<p><a href="https://juejin.cn/post/6943978947528884260/" target="_blank">前端刷题路-目录（题型分类）</a></p>
<p>有兴趣的也可以看看我的个人主页👇</p>
<p><a href="https://rexkentzheng.github.io/rexkentzheng/" target="_blank" rel="nofollow noopener noreferrer">Here is RZ</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            