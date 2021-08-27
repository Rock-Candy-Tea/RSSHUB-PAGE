
---
title: '不懂动态规划？21道 LeetCode题目带你学会动态规划！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c34801b433744a348e6f18bc13e915a0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 17:05:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c34801b433744a348e6f18bc13e915a0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>“这是我参与8月更文挑战的第17天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>”</p>
<hr>
<p>这篇文章大概是四五月份开始写的，后来忙于毕业就一直忘了写🤣。这几天刚好有时间把这篇文章收收尾，如果觉得有用就点个赞吧！</p>
<p><strong>注：</strong> 本文21道动态规划相关的LeetCode题目节选自CodeTop中考察频率较高的动态规划题目，文章较长，全文约15000字，可以收藏一波嗷~~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c34801b433744a348e6f18bc13e915a0~tplv-k3u1fbpfcp-watermark.image" alt="动态规划.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">1. 动态规划概述</h3>
<h4 data-id="heading-1">（1）基本概念</h4>
<p>动态规划算法通常用于<strong>求解具有某种最优性质的问题</strong>。在这类问题中，可能会有许多可行解。每一个解都对应于一个值，而我们希望找到具有最优值的解。动态规划算法与分治法类似，<strong>基本思想也是将待求解问题分解成若干个子问题，先求解子问题，然后从这些子问题的解得到原问题的解</strong>。</p>
<p>动态规划问题经分解得到的子问题往往不是互相独立的。需要保存已解决的子问题的答案，而在需要时再找出已保存的答案，这样就可以避免大量的重复计算。可以用一个表来记录所有已解的子问题的答案。不管该子问题以后是否被用到，只要它被计算过，就将其结果填入表中。这就是动态规划法的基本思路。</p>
<p>动态规划有两个重要的概念：</p>
<ul>
<li><strong>状态</strong>：解决某一问题的中间结果，它是子问题的一个抽象定义。</li>
<li><strong>状态转移方程</strong>：状态与状态之间的递推关系。</li>
</ul>
<p>动态规划解题步骤：</p>
<ol>
<li>状态定义：找出子问题抽象定义。</li>
<li>确定状态转移方程：找出状态与状态之间的递推关系。</li>
<li>初始状态和边界情况：最简单的子问题的结果，也是程序的出口条件 。</li>
<li>返回值：对于简单问题，返回值可能就是最终状态；对于复杂问题可能还需对最终状态做一些额外处理。</li>
</ol>
<p>下面就通过<strong>爬楼梯问题</strong>来看看动态规划的具体应用。</p>
<p><strong>题目描述</strong>：假设正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？其中 n 是一个正整数。</p>
<p><strong>示例 1</strong>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入： <span class="hljs-number">2</span>
输出： <span class="hljs-number">2</span>
解释： 有两种方法可以爬到楼顶。
<span class="hljs-number">1.</span> <span class="hljs-number">1</span> 阶 + <span class="hljs-number">1</span> 阶
<span class="hljs-number">2.</span> <span class="hljs-number">2</span> 阶
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2</strong>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入： <span class="hljs-number">3</span>
输出： <span class="hljs-number">3</span>
解释： 有三种方法可以爬到楼顶。
<span class="hljs-number">1.</span> <span class="hljs-number">1</span> 阶 + <span class="hljs-number">1</span> 阶 + <span class="hljs-number">1</span> 阶
<span class="hljs-number">2.</span> <span class="hljs-number">1</span> 阶 + <span class="hljs-number">2</span> 阶
<span class="hljs-number">3.</span> <span class="hljs-number">2</span> 阶 + <span class="hljs-number">1</span> 阶
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这道题有两个关键特征：</p>
<ul>
<li>要求给出达成某个目的的<strong>解法个数；</strong></li>
<li>不要求给出每一种解法对应的具体路径。</li>
</ul>
<p>这样的问题往往可以用动态规划进行求解。对于这个问题，每次爬楼梯只有两种情况：</p>
<ul>
<li>最后一步爬 1 级台阶，前面有 n - 1 级台阶，这种情况下共有f(n - 1)种方法；</li>
<li>最后一步爬 2 级台阶，前面有 n - 2 级台阶，这种情况下共有f(n - 2)种方法；</li>
</ul>
<p>f(n) 为以上两种情况之和，即 f(n)=f(n-1)+f(n-2)，这就是本题用到的递推关系。下面就根据动态规划的四个步骤来看那一下：</p>
<ol>
<li><strong>状态定义</strong>：初始化一个f数组，f[i]表示爬到i级台阶的方法数量；</li>
<li><strong>状态转移方程</strong>：f(n)=f(n-1)+f(n-2)；</li>
<li><strong>初始状态</strong>：一级台阶时，共1种爬法；两级台阶时，可以一级一级爬，也可以一次爬两级，共有2种爬法。即f[1] = 1，f[2] = 2；</li>
<li><strong>返回值</strong>：f[n] ，即 n 级台阶共有多少种爬法。</li>
</ol>
<p>动态规划实现代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">n</span></span>
* <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
*/</span>
<span class="hljs-keyword">const</span> climbStairs = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-comment">// 初始化状态数组</span>
    <span class="hljs-keyword">const</span> f = [];
    <span class="hljs-comment">// 初始化已知值</span>
    f[<span class="hljs-number">1</span>] = <span class="hljs-number">1</span>;
    f[<span class="hljs-number">2</span>] = <span class="hljs-number">2</span>;
    <span class="hljs-comment">// 动态更新每一层楼梯对应的结果</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">3</span>;i <= n;i++)&#123;
        f[i] = f[i-<span class="hljs-number">2</span>] + f[i-<span class="hljs-number">1</span>];
    &#125;
    <span class="hljs-comment">// 返回目标值</span>
    <span class="hljs-keyword">return</span> f[n];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">（2）使用场景</h4>
<p>上面用动态规划的思想解决了<strong>爬楼梯</strong>的问题，当然我们的目的并不是为了解决这个问题，而是通过这个问题来看动态规划，下面就来重新认识一下动态规划。</p>
<p>上面说过了分支问题，它的核心思想是：<strong>把一个问题分解为相互独立的子问题，逐个解决子问题后，再组合子问题的答案，就得到了问题的最终解。</strong></p>
<p>动态规划的思想和“分治”有点相似。不同之处在于，“分治”思想中，各个子问题之间是独立的：比如说归并排序中，子数组之间的排序并不互相影响。而动态规划划分出的子问题，往往是相互依赖、相互影响的。</p>
<p>那什么样的题应该用动态规划来做？要抓以下关键特征：</p>
<ul>
<li><strong>最优子结构</strong>，它指的是问题的最优解包含着子问题的最优解——不管前面的决策如何，此后的状态必须是基于当前状态（由上次决策产生）的最优决策。就这道题来说，<code>f(n)</code>和<code>f(n-1)</code>、<code>f(n-2)</code>之间的关系（状态转移方程）印证了这一点。</li>
<li><strong>重叠子问题</strong>，在递归的过程中，出现了反复计算的情况。</li>
<li><strong>无后效性</strong>，无后效性有两层含义，第一层含义是，在推导后面阶段的状态的时候，只关心前面阶段的状态值，不关心这个状态是怎么一步一步推导出来的。第二层含义是，某阶段状态一旦确定，就不受之后阶段的决策影响。无后效性是一个非常“宽松”的要求。只要满足前面提到的动态规划问题模型，其实基本上都会满足无后效性。</li>
</ul>
<p>所以，只要需要解决的问题符合这三个关键特征，就可以使用动态规划来求解。</p>
<h3 data-id="heading-3">2. LeetCode 路径问题</h3>
<h4 data-id="heading-4">（1）不同路径</h4>
<p>一个机器人位于一个 <code>m x n</code>网格的左上角 （起始点在下图中标记为 “Start” ）。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。</p>
<p>问总共有多少条不同的路径？
<strong>示例 1：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5aadeee2c54b4182a41e68e657796e63~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：m = <span class="hljs-number">3</span>, n = <span class="hljs-number">7</span>
输出：<span class="hljs-number">28</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：m = <span class="hljs-number">3</span>, n = <span class="hljs-number">2</span>
输出：<span class="hljs-number">3</span>
解释：
从左上角开始，总共有 <span class="hljs-number">3</span> 条路径可以到达右下角。
<span class="hljs-number">1.</span> 向右 -> 向下 -> 向下
<span class="hljs-number">2.</span> 向下 -> 向下 -> 向右
<span class="hljs-number">3.</span> 向下 -> 向右 -> 向下
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 3：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：m = <span class="hljs-number">7</span>, n = <span class="hljs-number">3</span>
输出：<span class="hljs-number">28</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 4：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：m = <span class="hljs-number">3</span>, n = <span class="hljs-number">3</span>
输出：<span class="hljs-number">6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>1 <= m, n <= 100</code></li>
<li>题目数据保证答案小于等于 <code>2 * 10</code></li>
</ul>
<p>这个题目和爬楼梯问题其实是一样的思路，只不过爬楼梯问题算是一维的问题，而这个问题是一个二维的问题。看到这个问题，我们自然而然的就能想到<strong>动态规划</strong>。</p>
<p>每一个网格的路径数都和其上侧和左侧的路径数相关，可以得出递推方程：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">a[i][j] = a[i - <span class="hljs-number">1</span>][j] + a[i][j - <span class="hljs-number">1</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先初始化一个m * n 的二维数组，数组的所有节点值都先初始为0，由于最上边一行和最左边一列都是边界，只能有一种走法，所以初始为1。然后根据递推方程求解即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">m</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">n</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> uniquePaths = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">m, n</span>) </span>&#123;
    <span class="hljs-keyword">const</span> dp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(m).fill(<span class="hljs-number">0</span>).map(<span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(n).fill(<span class="hljs-number">0</span>))

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < m; i++)&#123;
        dp[i][<span class="hljs-number">0</span>] = <span class="hljs-number">1</span>
    &#125;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < n; j++)&#123;
        dp[<span class="hljs-number">0</span>][j] = <span class="hljs-number">1</span>
    &#125;

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < m; i++)&#123; 
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">1</span>; j < n; j++)&#123;
            dp[i][j] = dp[i - <span class="hljs-number">1</span>][j] + dp[i][j - <span class="hljs-number">1</span>]
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> dp[m - <span class="hljs-number">1</span>][n - <span class="hljs-number">1</span>]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(mn)，其中m和n分别是网格的长宽，我们需要两层遍历，所以空间复杂度为O(mn)。</li>
<li>空间复杂度：O(mn)，其中m和n分别是网格的长宽，我们需要一个m * n 的二维数组来存储所有状态，所以所需空间复杂度为O(mn)。</li>
</ul>
<h4 data-id="heading-5">（2）不同路径 II</h4>
<p>一个机器人位于一个 <code>m x n</code> 网格的左上角 （起始点在下图中标记为“Start” ）。</p>
<p>机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。</p>
<p>现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/339748118e1144d7a44ac04f6ea0ccd8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>网格中的障碍物和空位置分别用 <code>1</code> 和 <code>0</code> 来表示。</p>
<p><strong>示例 1：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20a06f628502477684caf766d7bd7b87~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：obstacleGrid = [[<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>],[<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">0</span>],[<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>]]
输出：<span class="hljs-number">2</span>
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 <span class="hljs-number">2</span> 条不同的路径：
<span class="hljs-number">1.</span> 向右 -> 向右 -> 向下 -> 向下
<span class="hljs-number">2.</span> 向下 -> 向下 -> 向右 -> 向右
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba34b65988ff4c7bb21f5bddbda74cf3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：obstacleGrid = [[<span class="hljs-number">0</span>,<span class="hljs-number">1</span>],[<span class="hljs-number">0</span>,<span class="hljs-number">0</span>]]
输出：<span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>m == obstacleGrid.length</code></li>
<li><code>n == obstacleGrid[i].length</code></li>
<li><code>1 <= m, n <= 100</code></li>
<li><code>obstacleGrid[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>
<p>这道题目和62题不同路径 是一样的思路：<strong>动态规划。</strong></p>
<p>不同的是，这个题目中出现了障碍物，所以在遍历的时候需要注意以下两点：</p>
<ul>
<li>在给第一行和第一列元素设置初始值时，如果遇到网格的值是1，也就是有障碍物的情况，就直接停下来，不需要往前继续遍历了，因为前面就不可能在经过了；</li>
<li>在计算每个网格的路径数时，如果该方格元素是就直接跳过，不需要计算。</li>
</ul>
<p>以上两点就是本题和62题的不同之处，根据这个思路实现即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[][]&#125;</span> <span class="hljs-variable">obstacleGrid</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> uniquePathsWithObstacles = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">obstacleGrid</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!obstacleGrid.length || obstacleGrid[<span class="hljs-number">0</span>][<span class="hljs-number">0</span>] === <span class="hljs-number">1</span>)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
    &#125;

    <span class="hljs-keyword">const</span> m = obstacleGrid.length, n = obstacleGrid[<span class="hljs-number">0</span>].length
    <span class="hljs-keyword">const</span> dp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(m).fill(<span class="hljs-number">0</span>).map(<span class="hljs-function">() =></span>  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(n).fill(<span class="hljs-number">0</span>))

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < m && obstacleGrid[i][<span class="hljs-number">0</span>] == <span class="hljs-number">0</span>; i++) &#123;
        dp[i][<span class="hljs-number">0</span>] = <span class="hljs-number">1</span>;
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < n && obstacleGrid[<span class="hljs-number">0</span>][j] == <span class="hljs-number">0</span>; j++) &#123;
        dp[<span class="hljs-number">0</span>][j] = <span class="hljs-number">1</span>;
    &#125;
    
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < m; i++)&#123; 
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">1</span>; j < n; j++)&#123;
            <span class="hljs-keyword">if</span>(obstacleGrid[i][j] === <span class="hljs-number">0</span>)&#123;
                dp[i][j] = dp[i - <span class="hljs-number">1</span>][j] + dp[i][j - <span class="hljs-number">1</span>]
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> dp[m - <span class="hljs-number">1</span>][n - <span class="hljs-number">1</span>]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(mn)，其中m和n分别是网格的长宽，我们需要两层遍历，所以空间复杂度为O(mn)。</li>
<li>空间复杂度：O(mn)，其中m和n分别是网格的长宽，我们需要一个m * n 的二维数组来存储所有状态，所以所需空间复杂度为O(mn)。</li>
</ul>
<h4 data-id="heading-6">（3）最小路径和</h4>
<p>给定一个包含非负整数的 <code>m x n</code> 网格 <code>grid</code> ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。</p>
<p><strong>说明：</strong> 每次只能向下或者向右移动一步。
 </p>
<p><strong>示例 1：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdf92aafd1034e0ab7bd8f8f3a875434~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：grid = [[<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">1</span>],[<span class="hljs-number">1</span>,<span class="hljs-number">5</span>,<span class="hljs-number">1</span>],[<span class="hljs-number">4</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>]]
输出：<span class="hljs-number">7</span>
解释：因为路径 <span class="hljs-number">1</span>→<span class="hljs-number">3</span>→<span class="hljs-number">1</span>→<span class="hljs-number">1</span>→<span class="hljs-number">1</span> 的总和最小。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：grid = [[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>],[<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]]
输出：<span class="hljs-number">12</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>m == grid.length</code></li>
<li><code>n == grid[i].length</code></li>
<li><code>1 <= m, n <= 200</code></li>
<li><code>0 <= grid[i][j] <= 100</code></li>
</ul>
<p>对于这道题目，路径的方向只能是从上到下，从左向右。我们可以知道，当前点的路径和都和上一个点的路径和相关，所以这里我们可以使用动态规划来解答。</p>
<p>对于第一行的元素，它只能是左边的元素移动过来的，当前的元素的路径总和关系如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">grid[i][<span class="hljs-number">0</span>] += grid[i - <span class="hljs-number">1</span>][<span class="hljs-number">0</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于第一列的元素，它只能是上边的元素移动过来的，当前的元素的路径总和关系如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">grid[<span class="hljs-number">0</span>][j] += grid[<span class="hljs-number">0</span>][j - <span class="hljs-number">1</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于其他位置的元素，他可以是上边移动过来的，也可以是左边移动过来的，因为要求的是最小路径和，所以我们只需要选取左边和上面的路径和最小值，当前的元素的路径总和关系如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">grid[i][j] = <span class="hljs-built_in">Math</span>.min(grid[i - <span class="hljs-number">1</span>][j], grid[i][j - <span class="hljs-number">1</span>]) + grid[i][j];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，经过遍历之后，每个节点的值就是当前的最小路径和。最后只需要返回右下角元素的值即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[][]&#125;</span> <span class="hljs-variable">grid</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> minPathSum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">grid</span>) </span>&#123;
    <span class="hljs-keyword">let</span> m = grid.length, n = grid[<span class="hljs-number">0</span>].length

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < m; i++)&#123;
        grid[i][<span class="hljs-number">0</span>] += grid[i - <span class="hljs-number">1</span>][<span class="hljs-number">0</span>]
    &#125;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">1</span>; j < n; j++)&#123;
        grid[<span class="hljs-number">0</span>][j] += grid[<span class="hljs-number">0</span>][j - <span class="hljs-number">1</span>]
    &#125;

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < m; i++)&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">1</span>; j < n; j++)&#123;
            grid[i][j] = <span class="hljs-built_in">Math</span>.min(grid[i - <span class="hljs-number">1</span>][j], grid[i][j - <span class="hljs-number">1</span>]) + grid[i][j];
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> grid[m - <span class="hljs-number">1</span>][n - <span class="hljs-number">1</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(mn)，其中 m 和 n 分别是网格的行数和列数。需要对整个网格遍历一次，计算 grid 的每个元素的值。</li>
<li>空间复杂度：O(1)，这里我们是在原数组的基础上进行的操作，所需的额外的空间为常数。</li>
</ul>
<h4 data-id="heading-7">（4）三角形最小路径和</h4>
<p>给定一个三角形 <code>triangle</code> ，找出自顶向下的最小路径和。</p>
<p>每一步只能移动到下一行中相邻的结点上。</p>
<p><strong>相邻的结点</strong>在这里指的是<strong>下标</strong>与<strong>上一层结点下标</strong>相同或者等于 <strong>上一层结点下标 + 1</strong> 的两个结点。也就是说，如果正位于当前行的下标 <code>i</code> ，那么下一步可以移动到下一行的下标 <code>i</code> 或 <code>i + 1</code> 。
 </p>
<p><strong>示例 1：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：triangle = [[<span class="hljs-number">2</span>],[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>],[<span class="hljs-number">6</span>,<span class="hljs-number">5</span>,<span class="hljs-number">7</span>],[<span class="hljs-number">4</span>,<span class="hljs-number">1</span>,<span class="hljs-number">8</span>,<span class="hljs-number">3</span>]]
输出：<span class="hljs-number">11</span>
解释：如下面简图所示：
   <span class="hljs-number">2</span>
  <span class="hljs-number">3</span> <span class="hljs-number">4</span>
 <span class="hljs-number">6</span> <span class="hljs-number">5</span> <span class="hljs-number">7</span>
<span class="hljs-number">4</span> <span class="hljs-number">1</span> <span class="hljs-number">8</span> <span class="hljs-number">3</span>
自顶向下的最小路径和为 <span class="hljs-number">11</span>（即，<span class="hljs-number">2</span> + <span class="hljs-number">3</span> + <span class="hljs-number">5</span> + <span class="hljs-number">1</span> = <span class="hljs-number">11</span>）。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：triangle = [[-<span class="hljs-number">10</span>]]
输出：-<span class="hljs-number">10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>1 <= triangle.length <= 200</code></li>
<li><code>triangle[0].length == 1</code></li>
<li><code>triangle[i].length == triangle[i - 1].length + 1</code></li>
<li><code>-104 <= triangle[i][j] <= 104</code></li>
</ul>
<p> 
<strong>进阶：</strong></p>
<ul>
<li>你可以只使用 <code>O(n)</code> 的额外空间（<code>n</code> 为三角形的总行数）来解决这个问题吗？</li>
</ul>
<p>这道题目和最小路径和那道题的阶梯思路类似，都是使用<strong>动态规划</strong>来解决。</p>
<p>这里，其实我们并不需要初始化一个数组来保存每一步的状态（每个节点的最小路径值），可以在原数组上进行操作，因为每个节点都只遍历一次，在遍历完之后，我们只需要将当前节点的状态赋值给当前节点即可。</p>
<p>这里同样需要处理两个边界的问题，对于第一列元素，他只能是上面的元素下来的，所以他的状态转移方程是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">triangle[i][j] += triangle[i - <span class="hljs-number">1</span>][j]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于每一行的最后一位，它只能是上一行的最后一位下来的，所以他的状态转移方程是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">triangle[i][j] += triangle[i - <span class="hljs-number">1</span>][j - <span class="hljs-number">1</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于其他的元素，可以是其对应序号以及对应序号减一的元素移动下来的，所以他的状态转移方程是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">triangle[i][j] += <span class="hljs-built_in">Math</span>.min(triangle[i - <span class="hljs-number">1</span>][j], triangle[i - <span class="hljs-number">1</span>][j - <span class="hljs-number">1</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们只需要返回最后一行元素的最小值即可，这里我们用...扩展运算符配合Math的min方法求得最后一行的最小值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[][]&#125;</span> <span class="hljs-variable">triangle</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> minimumTotal = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">triangle</span>) </span>&#123;
    <span class="hljs-keyword">const</span> n = triangle.length

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < n; i++)&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j <= i; j++)&#123;
            <span class="hljs-keyword">if</span>(j === <span class="hljs-number">0</span>)&#123;
                triangle[i][j] += triangle[i - <span class="hljs-number">1</span>][j]
            &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(j === i)&#123;
                triangle[i][j] += triangle[i - <span class="hljs-number">1</span>][j - <span class="hljs-number">1</span>]
            &#125;<span class="hljs-keyword">else</span>&#123;
                triangle[i][j] += <span class="hljs-built_in">Math</span>.min(triangle[i - <span class="hljs-number">1</span>][j], triangle[i - <span class="hljs-number">1</span>][j - <span class="hljs-number">1</span>])
            &#125;
        &#125;
    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.min(...triangle[n - <span class="hljs-number">1</span>])
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n2)，其中 n 是三角形的行数。</li>
<li>空间复杂度：O(1)。这里我们在原数组的基础上进行的操作，所以所需要的额外的空间为常数。</li>
</ul>
<h3 data-id="heading-8">3. LeetCode 买卖股票问题</h3>
<h4 data-id="heading-9">（1）买卖股票的最佳时机</h4>
<p>给定一个数组，它的第 <em>i</em> 个元素是一支给定股票第 <em>i</em> 天的价格。如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。注意：你不能在买入股票前卖出股票。</p>
<p><strong>示例 1:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: [<span class="hljs-number">7</span>,<span class="hljs-number">1</span>,<span class="hljs-number">5</span>,<span class="hljs-number">3</span>,<span class="hljs-number">6</span>,<span class="hljs-number">4</span>]
输出: <span class="hljs-number">5</span>
解释: 在第 <span class="hljs-number">2</span> 天（股票价格 = <span class="hljs-number">1</span>）的时候买入，在第 <span class="hljs-number">5</span> 天（股票价格 = <span class="hljs-number">6</span>）的时候卖出，最大利润 = <span class="hljs-number">6</span>-<span class="hljs-number">1</span> = <span class="hljs-number">5</span> 。
     注意利润不能是 <span class="hljs-number">7</span>-<span class="hljs-number">1</span> = <span class="hljs-number">6</span>, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: [<span class="hljs-number">7</span>,<span class="hljs-number">6</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">1</span>]
输出: <span class="hljs-number">0</span>
解释: 在这种情况下, 没有交易完成, 所以最大利润为 <span class="hljs-number">0</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（1）直接遍历</strong></p>
<p>我们需要对股票进行一次买入、一次卖出，卖出在买入之后，并且要计算最大的利润。</p>
<p>这里初始化一个最小值min，和一个最大的结果值max。遍历数组，如果当前数组元素小于最小值民，就更新最小值，始终让其保持最小。如果当前值减去最小值大于最大值，就更新最大值。直到遍历完数组所有的元素，返回最后的结果。</p>
<p><strong>（2）动态规划</strong></p>
<p>对于这道题，我们可以使用<strong>动态规划</strong>来解决。这里我们只需要进行一次买入卖出。那到最后交易时，可能会有三种状态：</p>
<ul>
<li><code>dp[0]</code>：一直没有买</li>
<li><code>dp[1]</code>：：到最后只买了一笔，未卖出</li>
<li><code>dp[2]</code>：：到最后只卖了一笔，并卖出</li>
</ul>
<p>由于第一种状态未进行任何操作，所以可以不用记录。然后我们对后两种状态进行转移：</p>
<ul>
<li><code>dp[1] = Math.max(dp[1], -prices[i])</code>：前一天也是b1状态或者是没有任何操作，今天买入一笔变成b1状态；</li>
<li><code>dp[2] = Math.max(dp[2], dp[1] + prices[i])</code>：前一天也是s1状态或者是b1状态，今天卖出一笔变成s1状态；</li>
</ul>
<p><strong>（1）直接遍历</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">prices</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> maxProfit = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">prices</span>) </span>&#123;
    <span class="hljs-keyword">let</span> max = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> min = prices[<span class="hljs-number">0</span>]

    prices.forEach( <span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
        <span class="hljs-keyword">if</span>(item < min) min = item
        <span class="hljs-keyword">if</span>(item - min > max) max = item - min
    &#125;)
    <span class="hljs-keyword">return</span> max
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li><strong>时间复杂度：</strong> O(n)，其中n是数组的长度，我们需要将数组遍历一遍</li>
<li><strong>空间复杂度：</strong> O(1)，这里只需要常数空间来储存最小值min和最大结果值max</li>
</ul>
<p><strong>（2）动态规划</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">prices</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> maxProfit = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">prices</span>) </span>&#123;
    <span class="hljs-keyword">let</span> len = prices.length;
    <span class="hljs-keyword">const</span> dp = [<span class="hljs-number">0</span>, -prices[<span class="hljs-number">0</span>], <span class="hljs-number">0</span>]
    
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < len; i++) &#123;
        dp[<span class="hljs-number">1</span>] = <span class="hljs-built_in">Math</span>.max(dp[<span class="hljs-number">1</span>], -prices[i])
        dp[<span class="hljs-number">2</span>] = <span class="hljs-built_in">Math</span>.max(dp[<span class="hljs-number">2</span>], dp[<span class="hljs-number">1</span>] + prices[i])
    &#125;
    <span class="hljs-keyword">return</span> dp[<span class="hljs-number">2</span>];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li><strong>时间复杂度</strong>：O(n)，其中 n 是数组 prices 的长度。</li>
<li><strong>空间复杂度</strong>：O(1)。</li>
</ul>
<h4 data-id="heading-10">（2）买卖股票的最佳时机 II</h4>
<p>给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</p>
<p>示例 1:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: [<span class="hljs-number">7</span>,<span class="hljs-number">1</span>,<span class="hljs-number">5</span>,<span class="hljs-number">3</span>,<span class="hljs-number">6</span>,<span class="hljs-number">4</span>]
输出: <span class="hljs-number">7</span>
解释: 在第 <span class="hljs-number">2</span> 天（股票价格 = <span class="hljs-number">1</span>）的时候买入，在第 <span class="hljs-number">3</span> 天（股票价格 = <span class="hljs-number">5</span>）的时候卖出, 这笔交易所能获得利润 = <span class="hljs-number">5</span>-<span class="hljs-number">1</span> = <span class="hljs-number">4</span> 。
     随后，在第 <span class="hljs-number">4</span> 天（股票价格 = <span class="hljs-number">3</span>）的时候买入，在第 <span class="hljs-number">5</span> 天（股票价格 = <span class="hljs-number">6</span>）的时候卖出, 这笔交易所能获得利润 = <span class="hljs-number">6</span>-<span class="hljs-number">3</span> = <span class="hljs-number">3</span> 。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]
输出: <span class="hljs-number">4</span>
解释: 在第 <span class="hljs-number">1</span> 天（股票价格 = <span class="hljs-number">1</span>）的时候买入，在第 <span class="hljs-number">5</span> 天 （股票价格 = <span class="hljs-number">5</span>）的时候卖出, 这笔交易所能获得利润 = <span class="hljs-number">5</span>-<span class="hljs-number">1</span> = <span class="hljs-number">4</span> 。
     注意你不能在第 <span class="hljs-number">1</span> 天和第 <span class="hljs-number">2</span> 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 3:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: [<span class="hljs-number">7</span>,<span class="hljs-number">6</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">1</span>]
输出: <span class="hljs-number">0</span>
解释: 在这种情况下, 没有交易完成, 所以最大利润为 <span class="hljs-number">0</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<ul>
<li>1 <= prices.length <= 3 * 10</li>
<li>0 <= prices[i] <= 10</li>
</ul>
<p>对于这道题目，我们可以使用<strong>动态规划</strong>来解答。每个点的状态描述：手里有股票或者没股票。</p>
<p>1）dp[i][0]表示：第 i 天手里没股票，至今（第 i 天）的最大收益。第 i 天手里没股票，有两种可能：</p>
<ul>
<li>昨天也没持有股票：dp[i-1][0]</li>
<li>昨天买了股票，今天卖了: dp[i-1][1] + prices[i]</li>
<li>dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])</li>
</ul>
<p>2）dp[i][1]表示：第 i 天手里有股票，至今（第 i 天）的最大收益。第 i 天手里有股票，有两种可能：</p>
<ul>
<li>昨天也有股票：dp[i-1][1]</li>
<li>昨天卖了，今天买了: dp[i-1][0] - prices[i]</li>
<li>dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])</li>
</ul>
<p>最终目标是求出：<code>dp[prices.length-1][0]</code>和<code>dp[prices.length-1][1]</code>的较大者，前者肯定>=后者，求<code>dp[prices.length-1][0]</code>即可。</p>
<p><strong>对于开始：</strong></p>
<ul>
<li>day 0 没买:dp[0][0] = 0</li>
<li>day 0 买了:dp[0][1] = -prices[0]</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">prices</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">maxProfit</span>(<span class="hljs-params">prices</span>) </span>&#123;
  <span class="hljs-keyword">const</span> len = prices.length;
  <span class="hljs-keyword">if</span> (len < <span class="hljs-number">2</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
  &#125;;
  <span class="hljs-keyword">const</span> dp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(len);
  dp[<span class="hljs-number">0</span>] = [<span class="hljs-number">0</span>, -prices[<span class="hljs-number">0</span>]];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < len; i++) &#123;
    dp[i] = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">2</span>);
    dp[i][<span class="hljs-number">0</span>] = <span class="hljs-built_in">Math</span>.max(dp[i - <span class="hljs-number">1</span>][<span class="hljs-number">0</span>], dp[i - <span class="hljs-number">1</span>][<span class="hljs-number">1</span>] + prices[i]); <span class="hljs-comment">// 没有股票</span>
    dp[i][<span class="hljs-number">1</span>] = <span class="hljs-built_in">Math</span>.max(dp[i - <span class="hljs-number">1</span>][<span class="hljs-number">1</span>], dp[i - <span class="hljs-number">1</span>][<span class="hljs-number">0</span>] - prices[i]); <span class="hljs-comment">// 有股票</span>
  &#125;
  <span class="hljs-keyword">return</span> dp[len - <span class="hljs-number">1</span>][<span class="hljs-number">0</span>];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li><strong>时间复杂度：</strong> O(n)，其中 n 为数组的长度。一共有 2n 个状态，每次状态转移的时间复杂度为 O(1)，因此时间复杂度为 O(2n)=O(n)。</li>
<li><strong>空间复杂度</strong>：O(n)，我们需要开辟O(n) 空间存储动态规划中的所有状态。</li>
</ul>
<h4 data-id="heading-11">（3）买卖股票的最佳时机 III</h4>
<p>给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你最多可以完成 <strong>两笔</strong> 交易。注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</p>
<p>示例 1:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：prices = [<span class="hljs-number">3</span>,<span class="hljs-number">3</span>,<span class="hljs-number">5</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">3</span>,<span class="hljs-number">1</span>,<span class="hljs-number">4</span>]
输出：<span class="hljs-number">6</span>
解释：在第 <span class="hljs-number">4</span> 天（股票价格 = <span class="hljs-number">0</span>）的时候买入，在第 <span class="hljs-number">6</span> 天（股票价格 = <span class="hljs-number">3</span>）的时候卖出，这笔交易所能获得利润 = <span class="hljs-number">3</span>-<span class="hljs-number">0</span> = <span class="hljs-number">3</span> 。
     随后，在第 <span class="hljs-number">7</span> 天（股票价格 = <span class="hljs-number">1</span>）的时候买入，在第 <span class="hljs-number">8</span> 天 （股票价格 = <span class="hljs-number">4</span>）的时候卖出，这笔交易所能获得利润 = <span class="hljs-number">4</span>-<span class="hljs-number">1</span> = <span class="hljs-number">3</span> 。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：prices = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]
输出：<span class="hljs-number">4</span>
解释：在第 <span class="hljs-number">1</span> 天（股票价格 = <span class="hljs-number">1</span>）的时候买入，在第 <span class="hljs-number">5</span> 天 （股票价格 = <span class="hljs-number">5</span>）的时候卖出, 这笔交易所能获得利润 = <span class="hljs-number">5</span>-<span class="hljs-number">1</span> = <span class="hljs-number">4</span> 。   
     注意你不能在第 <span class="hljs-number">1</span> 天和第 <span class="hljs-number">2</span> 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 3：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：prices = [<span class="hljs-number">7</span>,<span class="hljs-number">6</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">1</span>] 
输出：<span class="hljs-number">0</span> 
解释：在这个情况下, 没有交易完成, 所以最大利润为 <span class="hljs-number">0</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 4：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：prices = [<span class="hljs-number">1</span>]
输出：<span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<ul>
<li>1 <= prices.length <= 105</li>
<li>0 <= prices[i] <= 105</li>
</ul>
<p>对于这道题，我们可以使用<strong>动态规划</strong>来解决。在《买卖股票的最佳时机》中，我们只能进行一次买入卖出。而这道题，我们可以进行至多两次的买入卖出，那到最后交易时，可能会有五种状态：</p>
<ul>
<li><code>dp[0]</code>：一直没有买</li>
<li><code>dp[1]</code>：到最后只买了一笔，未卖出</li>
<li><code>dp[2]</code>：到最后只卖了一笔，并卖出</li>
<li><code>dp[3]</code>：到最后买了两笔，只卖出一笔</li>
<li><code>dp[4]</code>：到最后买了两笔，两笔都卖出</li>
</ul>
<p>由于第一种状态未进行任何操作，所以可以不用记录。然后我们对后四种状态进行转移：</p>
<ul>
<li><code>dp[1] = Math.max(dp[1], -prices[i])</code>：前一天也是b1状态或者是没有任何操作，今天买入一笔变成b1状态；</li>
<li><code>dp[2] = Math.max(dp[2], dp[1] + prices[i])</code>：前一天也是s1状态或者是b1状态，今天卖出一笔变成s1状态；</li>
<li><code>dp[3] = Math.max(dp[3], dp[2] - prices[i])</code>：前一天也是b2状态或者是s1状态，今天买入一笔变成b2状态；</li>
<li><code>dp[4] = Math.max(dp[4], dp[3] + prices[i])</code>：前一天也是s2状态或者是b2状态，今天冒出一笔变成s2状态。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">prices</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">maxProfit</span>(<span class="hljs-params">prices</span>) </span>&#123;
    <span class="hljs-keyword">let</span> len = prices.length;
    <span class="hljs-keyword">const</span> dp = [<span class="hljs-number">0</span>, -prices[<span class="hljs-number">0</span>], -prices[<span class="hljs-number">0</span>], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>]
    
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < len; i++) &#123;
        dp[<span class="hljs-number">1</span>] = <span class="hljs-built_in">Math</span>.max(dp[<span class="hljs-number">1</span>], -prices[i])
        dp[<span class="hljs-number">2</span>] = <span class="hljs-built_in">Math</span>.max(dp[<span class="hljs-number">2</span>], dp[<span class="hljs-number">1</span>] + prices[i])
        dp[<span class="hljs-number">3</span>] = <span class="hljs-built_in">Math</span>.max(dp[<span class="hljs-number">3</span>], dp[<span class="hljs-number">2</span>] - prices[i])
        dp[<span class="hljs-number">4</span>] = <span class="hljs-built_in">Math</span>.max(dp[<span class="hljs-number">4</span>], dp[<span class="hljs-number">3</span>] + prices[i])
    &#125;
    <span class="hljs-keyword">return</span> dp[<span class="hljs-number">4</span>];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li><strong>时间复杂度</strong>：O(n)，其中 n 是数组 prices 的长度。</li>
<li><strong>空间复杂度</strong>：O(1)。</li>
</ul>
<h4 data-id="heading-12">（4）买卖股票的最佳时机 IV</h4>
<p>给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</p>
<p>示例 1：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：k = <span class="hljs-number">2</span>, prices = [<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">1</span>]
输出：<span class="hljs-number">2</span>
解释：在第 <span class="hljs-number">1</span> 天 (股票价格 = <span class="hljs-number">2</span>) 的时候买入，在第 <span class="hljs-number">2</span> 天 (股票价格 = <span class="hljs-number">4</span>) 的时候卖出，这笔交易所能获得利润 = <span class="hljs-number">4</span>-<span class="hljs-number">2</span> = <span class="hljs-number">2</span> 。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：k = <span class="hljs-number">2</span>, prices = [<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">6</span>,<span class="hljs-number">5</span>,<span class="hljs-number">0</span>,<span class="hljs-number">3</span>]
输出：<span class="hljs-number">7</span>
解释：在第 <span class="hljs-number">2</span> 天 (股票价格 = <span class="hljs-number">2</span>) 的时候买入，在第 <span class="hljs-number">3</span> 天 (股票价格 = <span class="hljs-number">6</span>) 的时候卖出, 这笔交易所能获得利润 = <span class="hljs-number">6</span>-<span class="hljs-number">2</span> = <span class="hljs-number">4</span> 。
     随后，在第 <span class="hljs-number">5</span> 天 (股票价格 = <span class="hljs-number">0</span>) 的时候买入，在第 <span class="hljs-number">6</span> 天 (股票价格 = <span class="hljs-number">3</span>) 的时候卖出, 这笔交易所能获得利润 = <span class="hljs-number">3</span>-<span class="hljs-number">0</span> = <span class="hljs-number">3</span> 。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<ul>
<li>0 <= k <= 100</li>
<li>0 <= prices.length <= 1000</li>
<li>0 <= prices[i] <= 1000</li>
</ul>
<p>在题目《买卖股票的最佳时机》中，我们只能进行一次买入卖出，在题目123《买卖股票的最佳时机 III》中，我们可以进行两次买入卖出操作。而在这道题目中，我们可以进行k次买入卖出操作。这里我们也可以使用<strong>动态规划</strong>来解答。</p>
<p>每次我们只能进行<code>[1, k]</code>次中的某次交易或不交易，所以可能有2k+1中状态：</p>
<ul>
<li>无操作，一直没有买</li>
<li>dp[0]：到最后只买了一笔，未卖出</li>
<li>dp[1]：到最后只卖了一笔，并卖出</li>
<li>dp[2]：到最后买了两笔，只卖出一笔</li>
<li>dp[3]：到最后买了两笔，两笔都卖出</li>
<li>dp[4]：到最后买了三笔，只卖出两笔</li>
<li>······</li>
</ul>
<p>可以枚举一天的所有可能，取现金最大值：</p>
<ul>
<li>不交易，现金 不变</li>
<li>进行<code>[1, k]</code>的某次交易
<ul>
<li>买入，现金 -= 当天股票价格</li>
<li>卖出，现金 += 当天股票价格</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">k</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">prices</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> maxProfit = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">k, prices</span>) </span>&#123;
    <span class="hljs-keyword">const</span> dp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int16Array</span>(k * <span class="hljs-number">2</span>).fill(-prices[<span class="hljs-number">0</span>])
    
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < prices.length; i++) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < dp.length; j++) 
            &#123;
                dp[j] = <span class="hljs-built_in">Math</span>.max(dp[j], (dp[j - <span class="hljs-number">1</span>] || <span class="hljs-number">0</span>) + (j & <span class="hljs-number">1</span> ? prices[i] : -prices[i]))
            &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.max(<span class="hljs-number">0</span>, ...dp) 
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li><strong>时间复杂度</strong>：O(n * min(n, k))，其中 n 是数组 prices 的长度，即使用双重循环进行动态规划需要的时间。</li>
<li><strong>空间复杂度</strong>：O(min(n,k))。</li>
</ul>
<h3 data-id="heading-13">4. LeetCode 打家劫舍问题</h3>
<h4 data-id="heading-14">（1）打家劫舍</h4>
<p>你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，<strong>如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警</strong>。</p>
<p>给定一个代表每个房屋存放金额的非负整数数组，计算你<strong>不触动警报装置的情况下</strong>，一夜之内能够偷窃到的最高金额。</p>
<p><strong>示例 1：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">1</span>]
输出：<span class="hljs-number">4</span>
解释：偷窃 <span class="hljs-number">1</span> 号房屋 (金额 = <span class="hljs-number">1</span>) ，然后偷窃 <span class="hljs-number">3</span> 号房屋 (金额 = <span class="hljs-number">3</span>)。
     偷窃到的最高金额 = <span class="hljs-number">1</span> + <span class="hljs-number">3</span> = <span class="hljs-number">4</span> 。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：[<span class="hljs-number">2</span>,<span class="hljs-number">7</span>,<span class="hljs-number">9</span>,<span class="hljs-number">3</span>,<span class="hljs-number">1</span>]
输出：<span class="hljs-number">12</span>
解释：偷窃 <span class="hljs-number">1</span> 号房屋 (金额 = <span class="hljs-number">2</span>), 偷窃 <span class="hljs-number">3</span> 号房屋 (金额 = <span class="hljs-number">9</span>)，接着偷窃 <span class="hljs-number">5</span> 号房屋 (金额 = <span class="hljs-number">1</span>)。
     偷窃到的最高金额 = <span class="hljs-number">2</span> + <span class="hljs-number">9</span> + <span class="hljs-number">1</span> = <span class="hljs-number">12</span> 。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>0 <= nums.length <= 100</code></li>
<li><code>0 <= nums[i] <= 400</code></li>
</ul>
<p>对于这道题目，我们可以使用<strong>动态规划</strong>来实现。首先来看最简单的两种情况，如果只有一间房屋，那这个屋子就是最高的金额，如果有两间房屋，那不能同时偷，只能偷其中其中金额高的那间，如果大于两间屋子，就要进行讨论了。</p>
<ul>
<li>如果偷第n个房间，那么就不能偷第n - 1个房间，那么总金额就是前n - 2间屋子能偷到的最高的金额之和；</li>
<li>如果不偷第k间屋，那么能偷到的总金额就是前k - 1个房间的最高总金额。</li>
</ul>
<p>这两者，我们只要取总金额的较大值即可。</p>
<p>我们可以用 dp[i] 表示前 i 间房屋能偷窃到的最高总金额，那么就有如下的状态转移方程：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">dp[i]=max(dp[i−<span class="hljs-number">2</span>]+nums[i],dp[i−<span class="hljs-number">1</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>边界条件为：</p>
<ul>
<li>dp[0] = nums[0] ：只有一间房屋，则偷窃该房屋</li>
<li>dp[1] = max(nums[0], nums[1])：只有两间房屋，选择其中金额较高的房屋进行偷窃</li>
</ul>
<p>最终的答案即为 dp[n−1]，其中 n 是数组的长度。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> rob = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
    <span class="hljs-keyword">const</span> len = nums.length
    <span class="hljs-keyword">if</span>(!len)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
    &#125;

    <span class="hljs-keyword">const</span> dp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(len + <span class="hljs-number">1</span>)
    dp[<span class="hljs-number">0</span>] = <span class="hljs-number">0</span>
    dp[<span class="hljs-number">1</span>] = nums[<span class="hljs-number">0</span>]

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>; i <= len; i++)&#123;
        dp[i] = <span class="hljs-built_in">Math</span>.max(dp[i-<span class="hljs-number">1</span>], dp[i-<span class="hljs-number">2</span>] + nums[i-<span class="hljs-number">1</span>]);
    &#125;
    <span class="hljs-keyword">return</span> dp[len];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中 n 是数组长度。只需要对数组遍历一次。</li>
<li>空间复杂度：O(1)。使用数组只存储前两间房屋的最高总金额，而不需要存储整个数组的结果，因此空间复杂度是 O(1)</li>
</ul>
<h4 data-id="heading-15">（2）打家劫舍 II</h4>
<p>你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 <strong>围成一圈</strong> ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，<strong>如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警</strong> 。
​</p>
<p>给定一个代表每个房屋存放金额的非负整数数组，计算你 <strong>在不触动警报装置的情况下</strong> ，能够偷窃到的最高金额。
 
<strong>示例 1：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：nums = [<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>]
输出：<span class="hljs-number">3</span>
解释：你不能先偷窃 <span class="hljs-number">1</span> 号房屋（金额 = <span class="hljs-number">2</span>），然后偷窃 <span class="hljs-number">3</span> 号房屋（金额 = <span class="hljs-number">2</span>）, 因为他们是相邻的。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：nums = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">1</span>]
输出：<span class="hljs-number">4</span>
解释：你可以先偷窃 <span class="hljs-number">1</span> 号房屋（金额 = <span class="hljs-number">1</span>），然后偷窃 <span class="hljs-number">3</span> 号房屋（金额 = <span class="hljs-number">3</span>）。
     偷窃到的最高金额 = <span class="hljs-number">1</span> + <span class="hljs-number">3</span> = <span class="hljs-number">4</span> 。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 3：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：nums = [<span class="hljs-number">0</span>]
输出：<span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>1 <= nums.length <= 100</code></li>
<li><code>0 <= nums[i] <= 1000</code></li>
</ul>
<p>打家劫舍这类问题其实都可以使用动态规划来解答，这个题目和打家劫舍类似，不过就是多了两种情况：</p>
<ul>
<li>不偷第一家</li>
<li>不偷最后一家</li>
</ul>
<p>这样就可以分类讨论，当不偷第一家时，就排除到第一家，对其他家进行计算，当不偷最后一家时，就排除掉最后一家，对其他家进行计算。</p>
<p>当前节点的最大值就是当前节点和之前的第二个节点的和与上个节点的值的最大值，这样说可能比较绕，状态转移方程代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">dp[i] = <span class="hljs-built_in">Math</span>.max(dp[i - <span class="hljs-number">1</span>], dp[i - <span class="hljs-number">2</span>] + nums[i])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码实现：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> rob = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
    <span class="hljs-keyword">const</span> len = nums.length
    <span class="hljs-keyword">let</span> res1 = <span class="hljs-number">0</span>, res2 = <span class="hljs-number">0</span>
    <span class="hljs-keyword">if</span>(len === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
    <span class="hljs-keyword">if</span>(len === <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> nums[<span class="hljs-number">0</span>]

    <span class="hljs-keyword">const</span> dp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(len)
    
    <span class="hljs-comment">// 不偷第一家</span>
    dp[<span class="hljs-number">0</span>] = <span class="hljs-number">0</span>
    dp[<span class="hljs-number">1</span>] = nums[<span class="hljs-number">1</span>]
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>; i <= len - <span class="hljs-number">1</span>; i++)&#123;
        dp[i] = <span class="hljs-built_in">Math</span>.max(dp[i - <span class="hljs-number">1</span>], dp[i - <span class="hljs-number">2</span>] + nums[i]);
    &#125;
    res1 = dp[len - <span class="hljs-number">1</span>]

    <span class="hljs-comment">// 不偷最后一家</span>
    dp[<span class="hljs-number">0</span>] = nums[<span class="hljs-number">0</span>]
    dp[<span class="hljs-number">1</span>] = <span class="hljs-built_in">Math</span>.max(nums[<span class="hljs-number">0</span>], nums[<span class="hljs-number">1</span>])
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>; i <= len - <span class="hljs-number">2</span>; i++)&#123;
        dp[i] = <span class="hljs-built_in">Math</span>.max(dp[i - <span class="hljs-number">1</span>], dp[i - <span class="hljs-number">2</span>] + nums[i]);
    &#125;
    res2 = dp[len - <span class="hljs-number">2</span>]
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.max(res1, res2)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中n是数组的长度，我们需要遍历两次数组；</li>
<li>空间复杂度：O(n)，其中n是数组的长度，我们需要初始化一个长度为n的数组来保存当前节点的状态。</li>
</ul>
<h4 data-id="heading-16">（3）打家劫舍 III</h4>
<p>在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。</p>
<p>计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。</p>
<p><strong>示例 1:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: [<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">3</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">1</span>]
     <span class="hljs-number">3</span>
    / \
   <span class="hljs-number">2</span>   <span class="hljs-number">3</span>
    \   \ 
     <span class="hljs-number">3</span>   <span class="hljs-number">1</span>
输出: <span class="hljs-number">7</span> 
解释: 小偷一晚能够盗取的最高金额 = <span class="hljs-number">3</span> + <span class="hljs-number">3</span> + <span class="hljs-number">1</span> = <span class="hljs-number">7.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: [<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">1</span>]
     <span class="hljs-number">3</span>
    / \
   <span class="hljs-number">4</span>   <span class="hljs-number">5</span>
  / \   \ 
 <span class="hljs-number">1</span>   <span class="hljs-number">3</span>   <span class="hljs-number">1</span>
输出: <span class="hljs-number">9</span>
解释: 小偷一晚能够盗取的最高金额 = <span class="hljs-number">4</span> + <span class="hljs-number">5</span> = <span class="hljs-number">9.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于这道题目，可以使用动态规划来解答。</p>
<p>对于二叉树，每个节点都有两种状态，选中或者不选中，我们可以使用深度优先遍历来遍历这棵二叉树：</p>
<ul>
<li>当节点被选中时，它的左右孩子都不能被选中，所以最大值就是：node.val + left[1] + right[1]；</li>
<li>当节点不被选中时，它的左右子孩子可以选中也可以不选中，所以最大值就是：Math.max(left[0], left[1]) + Math.max(right[0], right[1]);</li>
</ul>
<p>最后返回左右子树中最大值即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) &#123;
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> rob = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-keyword">const</span> dfs = <span class="hljs-function">(<span class="hljs-params">node</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (node === <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-keyword">return</span> [<span class="hljs-number">0</span>, <span class="hljs-number">0</span>];
        &#125;
        <span class="hljs-keyword">const</span> left = dfs(node.left);
        <span class="hljs-keyword">const</span> right = dfs(node.right);
      
        <span class="hljs-keyword">const</span> select = node.val + left[<span class="hljs-number">1</span>] + right[<span class="hljs-number">1</span>];
        <span class="hljs-keyword">const</span> notSelect = <span class="hljs-built_in">Math</span>.max(left[<span class="hljs-number">0</span>], left[<span class="hljs-number">1</span>]) + <span class="hljs-built_in">Math</span>.max(right[<span class="hljs-number">0</span>], right[<span class="hljs-number">1</span>]);
        <span class="hljs-keyword">return</span> [select, notSelect];
    &#125;
    <span class="hljs-keyword">const</span> res = dfs(root)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.max(res[<span class="hljs-number">0</span>], res[<span class="hljs-number">1</span>])
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，对二叉树进行了一次后序遍历，所以时间复杂度是 O(n)；</li>
<li>空间复杂度：O(n)，递归栈空间的使用代价是 O(n)。</li>
</ul>
<h3 data-id="heading-17">5. LeetCode 回文串问题</h3>
<h4 data-id="heading-18">（1）回文子串</h4>
<p>给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。</p>
<p>示例 1：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：<span class="hljs-string">"abc"</span>
输出：<span class="hljs-number">3</span>
解释：三个回文子串: <span class="hljs-string">"a"</span>, <span class="hljs-string">"b"</span>, <span class="hljs-string">"c"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：<span class="hljs-string">"aaa"</span>
输出：<span class="hljs-number">6</span>
解释：<span class="hljs-number">6</span>个回文子串: <span class="hljs-string">"a"</span>, <span class="hljs-string">"a"</span>, <span class="hljs-string">"a"</span>, <span class="hljs-string">"aa"</span>, <span class="hljs-string">"aa"</span>, <span class="hljs-string">"aaa"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：输入的字符串长度不会超过 1000 。</p>
<p>这个题目最直接的方法就是使用暴力循环来解决，遍历每一种可能，具体思路如下：</p>
<ul>
<li>首先，根据题目，我们可以看出，每个元素自身也算是一个回文子串，所以要将字符串的长度加进去</li>
<li>定义一个函数用来检测字符串是否是回文串</li>
<li>两层遍历字符串，截取字符串的所有的子串，并判断其是否是回文串</li>
</ul>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度为O(n2)，需要两层遍历。</li>
<li>空间复杂度为O(1)</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">s</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> countSubstrings = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
    <span class="hljs-keyword">let</span> count = s.length
    <span class="hljs-keyword">let</span> len = s.length
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++)&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = i + <span class="hljs-number">1</span>; j < len; j++)&#123;
            <span class="hljs-keyword">let</span> temp = s.substr(i, j-i+<span class="hljs-number">1</span>)
            <span class="hljs-keyword">if</span>(isSub(temp))&#123;
                count++
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> count
&#125;;
<span class="hljs-keyword">const</span> isSub = <span class="hljs-function"><span class="hljs-params">str</span> =></span> &#123;
        <span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>
        <span class="hljs-keyword">let</span> b = str.length - <span class="hljs-number">1</span>
        <span class="hljs-keyword">while</span>(a <= b)&#123;
            <span class="hljs-keyword">if</span>(str[a] !== str[b])&#123;
                <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
            &#125;
            a++
            b--
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">（2）最长回文子串</h4>
<p>给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。</p>
<p><strong>示例 1：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: <span class="hljs-string">"babad"</span>
输出: <span class="hljs-string">"bab"</span>
注意: <span class="hljs-string">"aba"</span> 也是一个有效答案。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: <span class="hljs-string">"cbbd"</span>
输出: <span class="hljs-string">"bb"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里使用两种方法来解答这个问题：</p>
<p><strong>（1）方法一：中心扩展法</strong></p>
<p>中心扩展法的思想就是枚举出可能出现的回文串的中心，从这个中心位置尽可能的向两边扩散出去，得到一个回文串，具体实现步骤如下：</p>
<ul>
<li>选取对称中心（奇数长度的字符串为中心两个字符的中间，偶数长度的字符串中心为中间的字符）</li>
<li>通过对比扩展之后得出的两种组合较大的回文子串长度</li>
<li>对比之前的长度，判断是否更新起始的位置</li>
<li>遍历完之后，根据起始位置，截取最长回文子串</li>
</ul>
<p><strong>代码实现：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">s</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;string&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> longestPalindrome = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(s == <span class="hljs-literal">null</span> || s.length <<span class="hljs-number">1</span>)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
    &#125;
    <span class="hljs-keyword">let</span> start = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> end = <span class="hljs-number">0</span>
    <span class="hljs-comment">// 定义中心扩展的方法</span>
    <span class="hljs-keyword">const</span> fn = <span class="hljs-function">(<span class="hljs-params">s,left,right</span>) =></span> &#123;
        <span class="hljs-keyword">while</span>(left >=<span class="hljs-number">0</span> && right< s.length && s[left] === s[right])&#123;
            left--
            right++
        &#125;
        <span class="hljs-keyword">return</span> right - left -<span class="hljs-number">1</span>
    &#125;
    <span class="hljs-comment">// 遍历字符串</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i<s.length; i++)&#123;
        <span class="hljs-keyword">const</span> len1 = fn(s, i, i)
        <span class="hljs-keyword">const</span> len2 = fn(s, i, i+<span class="hljs-number">1</span>)
        <span class="hljs-keyword">const</span> len = <span class="hljs-built_in">Math</span>.max(len1, len2)
        <span class="hljs-comment">// 判断起始位置是否更新</span>
        <span class="hljs-keyword">if</span>(len > end - start)&#123;
            start = i- <span class="hljs-built_in">Math</span>.floor((len-<span class="hljs-number">1</span>)/<span class="hljs-number">2</span>)
            end = i+ <span class="hljs-built_in">Math</span>.floor(len/<span class="hljs-number">2</span>)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> s.substring(start, end+<span class="hljs-number">1</span>)
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li><strong>时间复杂度</strong>：O(n2)，枚举“中心位置”时间复杂度为 O(n)，从“中心位置”扩散得到“回文子串”的时间复杂度为 O(n)，因此时间复杂度是 O(n2)。</li>
<li><strong>空间复杂度</strong>：O(1)，这里只用到了两个常数临时变量start、end，因此空间复杂度为O(1)。</li>
</ul>
<p><strong>（2）方法二：动态规划</strong></p>
<p>解决这类问题的核心思想就是两个字<strong>延伸</strong>，具体来说</p>
<ul>
<li>如果一个字符串是回文串，那么在它左右分别加上一个相同的字符，那么它一定还是一个回文串</li>
<li>如果在一个不是回文字符串的字符串两端添加任何字符，或者在回文串左右分别加不同的字符，得到的一定不是回文串</li>
</ul>
<p>事实上，上面的分析已经建立了<strong>大问题</strong>和<strong>小问题</strong>之间的关联，因为我们可以建立动态规划模型。可以用 dp[i][j] 表示 s 中从 i 到 j（包括 i 和 j）是否可以形成回文，状态转移方程只是将上面的描述转化为代码即可：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (s[i] === s[j] && dp[i + <span class="hljs-number">1</span>][j - <span class="hljs-number">1</span>]) &#123;
  dp[i][j] = <span class="hljs-literal">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中：</p>
<ul>
<li>s[i] === s[j]：说明当前中心可以继续扩张，进而有可能扩大回文串的长度</li>
<li>dp[i+1][j-1]：true，说明s[i,j]的子串s[i+1][j-1]也是回文串，其中，i是从最大值开始遍历的，j是从最小值开始遍历的</li>
</ul>
<p>总结一下，使用动态规划的具体实现步骤如下：</p>
<ul>
<li>确定dp[i][j]是否是回文数，只需要dp[i+1][j-1]是回文数并且s[i] === s[j]即可。</li>
<li>长度为0或1的回文传需要特殊处理，即j-i < 2;</li>
<li>因为知道dp[i]需要先知道dp[i+1]，所以i需要从大到小开始遍历</li>
<li>因为知道dp[j]需要先知道dp[j-1]，所以j需要从小到大开始遍历</li>
</ul>
<p><strong>代码实现：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">s</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;string&#125;</span></span>
 */</span>
<span class="hljs-comment">// 扩展中心</span>
<span class="hljs-keyword">var</span> longestPalindrome = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
   <span class="hljs-keyword">let</span> res = <span class="hljs-string">''</span>;
    <span class="hljs-keyword">let</span> n = s.length;
    <span class="hljs-keyword">let</span> dp = <span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(n), <span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>().fill(<span class="hljs-number">0</span>));
    
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = n-<span class="hljs-number">1</span>; i >=<span class="hljs-number">0</span>; i--) &#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = i; j < n; j++) &#123;
            dp[i][j] = s[i] === s[j] && ( j - i < <span class="hljs-number">2</span> || dp[i+<span class="hljs-number">1</span>][j-<span class="hljs-number">1</span>])
            <span class="hljs-keyword">if</span>(dp[i][j] && j - i + <span class="hljs-number">1</span> > res.length) &#123;
                res = s.substr(i,j - i + <span class="hljs-number">1</span>);
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li><strong>时间复杂度</strong>：O(n2)，其中 n是字符串的长度。动态规划的状态总数为 O(n2)，对于每个状态，需要转移的时间为 O(1)。</li>
<li><strong>空间复杂度</strong>：O(n2)，即存储动态规划状态需要的空间。</li>
</ul>
<h4 data-id="heading-20">（3）最长回文子序列</h4>
<p>给定一个字符串 <code>s</code> ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 <code>s</code> 的最大长度为 <code>1000</code> 。
 </p>
<p><strong>示例 1:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: <span class="hljs-string">"bbbab"</span>
输出: <span class="hljs-number">4</span>
一个可能的最长回文子序列为 <span class="hljs-string">"bbbb"</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: <span class="hljs-string">"cbbd"</span>
输出: <span class="hljs-number">2</span>
一个可能的最长回文子序列为 <span class="hljs-string">"bb"</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>1 <= s.length <= 1000</code></li>
<li><code>s</code> 只包含小写英文字母</li>
</ul>
<p>对于这种回文子串的问题，我们可以考虑能否使用<strong>动态规划</strong>来求解。</p>
<p>这里我们尝试使用动态规划来解答，初始化一个dp二维数组来保存子串的长度，dp[i][j]表示s中的第i个字符到第j个字符组成的子串中，最长的回文序列的长度。</p>
<p>下面最重要的就是找出状态转移方程：</p>
<ul>
<li>如果字符串s的第i个和第j个字符相同：<code>f[i][j] = f[i + 1][j - 1] + 2</code></li>
<li>如果字符串s的第i个和第j个字符不相同：<code>f[i][j] = max(f[i + 1][j], f[i][j - 1])</code></li>
</ul>
<p>这里需要注意遍历时的顺序，i是从最后一个字符开始遍历的，j是从i+1开始向后遍历，这样就能保证每个子问题都计算好了。最后只要返回<code>dp[0][len-1]</code>即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">s</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> longestPalindromeSubseq = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
    <span class="hljs-keyword">let</span> len = s.length;
    
    <span class="hljs-keyword">let</span> dp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(len)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
        dp[i] = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(len).fill(<span class="hljs-number">0</span>);
    &#125;
    
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = len - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--) &#123;
        dp[i][i] = <span class="hljs-number">1</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = i+<span class="hljs-number">1</span>; j < len; j++) &#123;
            <span class="hljs-keyword">if</span> (s[i] === s[j]) &#123;
                dp[i][j] = dp[i+<span class="hljs-number">1</span>][j-<span class="hljs-number">1</span>] + <span class="hljs-number">2</span>;
            &#125; <span class="hljs-keyword">else</span> &#123;
                dp[i][j] = <span class="hljs-built_in">Math</span>.max(dp[i+<span class="hljs-number">1</span>][j], dp[i][j-<span class="hljs-number">1</span>])
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> dp[<span class="hljs-number">0</span>][len-<span class="hljs-number">1</span>];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n2)，其中n是字符串的长度，我们需要一个双层的遍历；</li>
<li>空间复杂度：O(n2)，其中n是字符串的长度，我们需要初始化一个二维数组。</li>
</ul>
<h3 data-id="heading-21">6. LeetCode 子序列问题</h3>
<h4 data-id="heading-22">（1）最大子序和</h4>
<p>给定一个整数数组 <code>nums</code> ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。</p>
<p><strong>示例:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: [-<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,-<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,-<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,-<span class="hljs-number">5</span>,<span class="hljs-number">4</span>]
输出: <span class="hljs-number">6</span>
解释: 连续子数组 [<span class="hljs-number">4</span>,-<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>] 的和最大，为 <span class="hljs-number">6</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>进阶:</strong>
如果你已经实现复杂度为 O(<em>n</em>) 的解法，尝试使用更为精妙的分治法求解。</p>
<p><strong>动态规划求解：</strong>
通常我们遍历子串或者子序列有三种遍历方式</p>
<ul>
<li>以某个节点为开头的所有子序列: 如 [a]，[a, b]，[ a, b, c] ... 再从以 b 为开头的子序列开始遍历 [b] [b, c]。</li>
<li>根据子序列的长度为标杆，如先遍历出子序列长度为 1 的子序列，在遍历出长度为 2 的 等等。</li>
<li>以子序列的结束节点为基准，先遍历出以某个节点为结束的所有子序列，因为每个节点都可能会是子序列的结束节点，因此要遍历下整个序列，如: 以 b 为结束点的所有子序列: [a , b] [b] ，以 c 为结束点的所有子序列: [a, b, c] [b, c] [ c ]。</li>
</ul>
<p>其中，第一种方式通常会使用暴力方法的求解，第二种方式在上面第五题已将用到过了，重点是第三种方式：<strong>因为可以产生递推关系, 采用动态规划时, 经常通过此种遍历方式, 如背包问题、最大公共子串 , 这里的动态规划解法也是以先遍历出以某个节点为结束节点的所有子序列的思路。</strong></p>
<p><strong>代码实现：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> maxSubArray = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
    <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>, res = nums[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> num <span class="hljs-keyword">of</span> nums)&#123;
        sum > <span class="hljs-number">0</span> ? sum += num : sum = num
        res = <span class="hljs-built_in">Math</span>.max(sum, res)
    &#125;
    <span class="hljs-keyword">return</span> res
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中 n 为 nums 数组的长度，只需要遍历一遍数组即可求得答案。</li>
<li>空间复杂度：O(1)，只需要常数空间存放若干变量。</li>
</ul>
<h4 data-id="heading-23">（2）最长递增子序列</h4>
<p>给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。</p>
<p>子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。</p>
<p>示例 1：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：nums = [<span class="hljs-number">10</span>,<span class="hljs-number">9</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">3</span>,<span class="hljs-number">7</span>,<span class="hljs-number">101</span>,<span class="hljs-number">18</span>]
输出：<span class="hljs-number">4</span>
解释：最长递增子序列是 [<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">7</span>,<span class="hljs-number">101</span>]，因此长度为 <span class="hljs-number">4</span> 。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：nums = [<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">0</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]
输出：<span class="hljs-number">4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 3：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：nums = [<span class="hljs-number">7</span>,<span class="hljs-number">7</span>,<span class="hljs-number">7</span>,<span class="hljs-number">7</span>,<span class="hljs-number">7</span>,<span class="hljs-number">7</span>,<span class="hljs-number">7</span>]
输出：<span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<ul>
<li>1 <= nums.length <= 2500</li>
<li>-104 <= nums[i] <= 104</li>
</ul>
<p>进阶：</p>
<ul>
<li>你可以设计时间复杂度为 O(n2) 的解决方案吗？</li>
<li>你能将算法的时间复杂度降低到 O(n log(n)) 吗?</li>
</ul>
<p>碰到子序列的问题，我们最容易想到的就是动态规划。首先初始化一个数组dp来保存每个子问题的最优解，dp[i]表示数组前n的元素的最长连续子序列，最后返回所有子序列中最长的序列就可以了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> lengthOfLIS = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
    <span class="hljs-keyword">const</span> n = nums.length
    <span class="hljs-keyword">if</span>(!n)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
    &#125;

    <span class="hljs-keyword">let</span> dp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(n).fill(<span class="hljs-number">1</span>)
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < n; i++)&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < i; j++)&#123;
            <span class="hljs-keyword">if</span>(nums[i] > nums[j])&#123;
                dp[i] = <span class="hljs-built_in">Math</span>.max(dp[i], dp[j] + <span class="hljs-number">1</span>)
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.max(...dp)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li><strong>时间复杂度</strong>：O(n)，其中 n 为数组 nums 的长度。动态规划的状态数为 n，计算状态 dp[i] 时，需要 O(n) 的时间遍历dp[0…i−1] 的所有状态，所以总时间复杂度为 O(n)。</li>
<li><strong>空间复杂度</strong>：O(n)，需要额外使用长度为 n 的 dp 数组。</li>
</ul>
<h4 data-id="heading-24">（3）乘积最大的子数组</h4>
<p>给你一个整数数组 <code>nums</code> ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
 </p>
<p><strong>示例 1:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: [<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,-<span class="hljs-number">2</span>,<span class="hljs-number">4</span>]
输出: <span class="hljs-number">6</span>
解释: 子数组 [<span class="hljs-number">2</span>,<span class="hljs-number">3</span>] 有最大乘积 <span class="hljs-number">6</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: [-<span class="hljs-number">2</span>,<span class="hljs-number">0</span>,-<span class="hljs-number">1</span>]
输出: <span class="hljs-number">0</span>
解释: 结果不能为 <span class="hljs-number">2</span>, 因为 [-<span class="hljs-number">2</span>,-<span class="hljs-number">1</span>] 不是子数组。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于这道题目，我们可以使用动态规划来解答。</p>
<p>我们只需要在遍历数组时，不断更新最大值即可，这个过程中，我们需要维护两个值：</p>
<ul>
<li>max，当前的最大值，将当前的值与当前的值和之前的最大值的乘积进行对比，保存最大值</li>
<li>min，当前的最小值，将当前的值与当前的值和之前的最小值的乘积进行对比，保存最小值</li>
</ul>
<p>我们这里求的是最大值，那为啥还要保存最小值呢？这是因为数组中可能会有负数，当当前的值是负数时，与之前的值相乘就会导致最大值和最小值交换，所以我们需要维护一个最大值和一个最小值。然后不断使用当前的最大值保存为结果，最后返回结果即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> maxProduct = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
    <span class="hljs-keyword">let</span> res = -<span class="hljs-literal">Infinity</span>, max = <span class="hljs-number">1</span>, min = <span class="hljs-number">1</span>;

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < nums.length; i++)&#123;
        <span class="hljs-keyword">if</span>(nums[i] < <span class="hljs-number">0</span>)&#123;
            <span class="hljs-keyword">let</span> temp = max
            max = min
            min = temp
        &#125;
        max = <span class="hljs-built_in">Math</span>.max(nums[i], nums[i] * max)
        min = <span class="hljs-built_in">Math</span>.min(nums[i], nums[i] * min)

        res = <span class="hljs-built_in">Math</span>.max(res, max)
    &#125;
    <span class="hljs-keyword">return</span> res
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，我们需要遍历一遍数组，所以时间复杂度为O(n)；</li>
<li>空间复杂度：O(1)，这里我们需要的额外空间为常数级，所以空间复杂度为O(1)。</li>
</ul>
<h4 data-id="heading-25">（4）最长重复子数组</h4>
<p>给两个整数数组 <code>A</code> 和 <code>B</code> ，返回两个数组中公共的、长度最长的子数组的长度。
 </p>
<p><strong>示例：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：
<span class="hljs-attr">A</span>: [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>]
<span class="hljs-attr">B</span>: [<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">4</span>,<span class="hljs-number">7</span>]
输出：<span class="hljs-number">3</span>
解释：
长度最长的公共子数组是 [<span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>] 。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>1 <= len(A), len(B) <= 1000</code></li>
<li><code>0 <= A[i], B[i] < 100</code></li>
</ul>
<p>对于这道题目，我们可以使用动态规划来解决。动态规划就是要保持上一个状态和下一个状态有关系，并且是连续的。这里的子数组就相当于子串，是连续的。</p>
<p>这里我们初始化一个dp数组保存当前的最大连续值，dp[i][j]表示数组A的前i个元素和数组B的前j个元素组成的最长公共子数组的长度。</p>
<p>在遍历数组时：</p>
<ul>
<li>如果当前的两个元素的值相等，也就是A[i] === B[j]，则说明当前的元素可以构成公共子数组，所以让前一个元素的最长公共子数组的长度加一，此时的状态转移方程是：dp[i][j] = dp[i - 1][j - 1] + 1；</li>
<li>如果当前的两个元素的值不相等，所以此时的dp值保存为0（初始化为0）。</li>
</ul>
<p>在遍历的过程中，不断更新最长公共子序列最大值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">A</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">B</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> findLength = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">A, B</span>) </span>&#123;
    <span class="hljs-keyword">const</span> m = A.length, n = B.length;

    <span class="hljs-keyword">let</span> dp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(m + <span class="hljs-number">1</span>)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <= m; i++) &#123; 
        dp[i] = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(n + <span class="hljs-number">1</span>).fill(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-keyword">let</span> res = <span class="hljs-number">0</span>

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i <= m; i++)&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">1</span>; j <= n; j++)&#123;
            <span class="hljs-keyword">if</span>(A[i - <span class="hljs-number">1</span>] === B[j - <span class="hljs-number">1</span>])&#123;
                dp[i][j] = dp[i - <span class="hljs-number">1</span>][j - <span class="hljs-number">1</span>] + <span class="hljs-number">1</span>
            &#125;
            res = <span class="hljs-built_in">Math</span>.max(dp[i][j], res)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> res
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(mn)，其中m和n分别是A和B两个数组的长度，这里我们需要两层遍历两个数组。</li>
<li>空间复杂度：O(mn)，其中m和n分别是A和B两个数组的长度，我们需要初始化一个dp二维数组来保存当前的最长公共子数组的长度。</li>
</ul>
<h3 data-id="heading-26">7. LeetCode 其他问题</h3>
<h4 data-id="heading-27">（1）接雨水</h4>
<p>给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。</p>
<p>示例 1：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b3753ef12c64e13b3931317d354f7c6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：height = [<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">0</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>]
输出：<span class="hljs-number">6</span>
解释：上面是由数组 [<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">0</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>] 表示的高度图，在这种情况下，可以接 <span class="hljs-number">6</span> 个单位的雨水（蓝色部分表示雨水）。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：height = [<span class="hljs-number">4</span>,<span class="hljs-number">2</span>,<span class="hljs-number">0</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>]
输出：<span class="hljs-number">9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<ul>
<li>n == height.length</li>
<li>0 <= n <= 3 * 104</li>
<li>0 <= height[i] <= 105</li>
</ul>
<p>看到这道题，我们自然而然的可以想到<strong>木桶效应</strong>，每根柱子上的雨水的深度取决于它两侧最高的柱子中较短的那根柱子的长度。</p>
<ul>
<li>如果这个较短的柱子的长度大于当前柱子，那么雨水的深度就是较短的柱子减去当前柱子的长度；</li>
<li>如果这个较短的柱子的长度小于等于当前柱子，那么雨水的深度就是0。</li>
</ul>
<p>对于下标 i，下雨后水能到达的最大高度等于下标 i 两边的最大高度的最小值，下标 i 处能接的雨水量等于下标 i 处的水能到达的最大高度减去 height[i]。</p>
<p>最直接的做法是对于数组 height 中的每个元素，分别向左和向右扫描并记录左边和右边的最大高度，然后计算每个下标位置能接的雨水量。使用动态规划的方法，可以在 O(n)的时间内预处理得到每个位置两边的最大高度。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">height</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> trap = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">height</span>) </span>&#123;
    <span class="hljs-keyword">let</span> len = height.length, sum = <span class="hljs-number">0</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len - <span class="hljs-number">1</span>; i++)&#123;
        <span class="hljs-comment">// 计算当前柱子左侧的最大值</span>
        <span class="hljs-keyword">let</span> left = <span class="hljs-number">0</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = i - <span class="hljs-number">1</span>; j >= <span class="hljs-number">0</span>; j--)&#123;
            left = <span class="hljs-built_in">Math</span>.max(height[j], left)
        &#125;
        <span class="hljs-comment">// 计算当前柱子右侧的最大值</span>
        <span class="hljs-keyword">let</span> right = <span class="hljs-number">0</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = i + <span class="hljs-number">1</span>; j < len; j++)&#123;
            right = <span class="hljs-built_in">Math</span>.max(height[j],right)
        &#125;
        <span class="hljs-comment">// 计算当前柱子能接的雨水量</span>
        <span class="hljs-keyword">if</span>(min > height[i])&#123;
            sum += <span class="hljs-built_in">Math</span>.min(left, right) - height[i]
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> sum
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中 n 是数组 height 的长度。需要遍历两次height数组；</li>
<li>空间复杂度：O(1)。</li>
</ul>
<h4 data-id="heading-28">（2）爬楼梯</h4>
<p>假设你正在爬楼梯。需要 <em>n</em> 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>
<p><strong>注意：</strong> 给定 <em>n</em> 是一个正整数。</p>
<p><strong>示例 1：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入： <span class="hljs-number">2</span>
输出： <span class="hljs-number">2</span>
解释： 有两种方法可以爬到楼顶。
<span class="hljs-number">1.</span>  <span class="hljs-number">1</span> 阶 + <span class="hljs-number">1</span> 阶
<span class="hljs-number">2.</span>  <span class="hljs-number">2</span> 阶
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入： <span class="hljs-number">3</span>
输出： <span class="hljs-number">3</span>
解释： 有三种方法可以爬到楼顶。
<span class="hljs-number">1.</span>  <span class="hljs-number">1</span> 阶 + <span class="hljs-number">1</span> 阶 + <span class="hljs-number">1</span> 阶
<span class="hljs-number">2.</span>  <span class="hljs-number">1</span> 阶 + <span class="hljs-number">2</span> 阶
<span class="hljs-number">3.</span>  <span class="hljs-number">2</span> 阶 + <span class="hljs-number">1</span> 阶
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到这个题目，我们应该想到的就是<strong>动态规划</strong>，<strong>将一个大问题分解成多个子问题</strong>。首先来看：</p>
<ul>
<li>第一级台阶：1种方法</li>
<li>第二级台阶：2种方法</li>
<li>第n级台阶：从第n-1级台阶爬一级，或从第n-2级台阶爬2级</li>
</ul>
<p>所以可以得出递推公式：f(n) = f(n−1) + f(n−2)
这样，我们就可以通过递归完成计算。</p>
<p>上面这种普通递归很显然，有很多的重复计算，所以，我们可以将每次计算的结果进行保存，以便下次计算时直接使用。</p>
<p><strong>普通递归：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">n</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> climbStairs = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-keyword">const</span> dp = []
    dp[<span class="hljs-number">0</span>] = <span class="hljs-number">1</span>
    dp[<span class="hljs-number">1</span>] = <span class="hljs-number">1</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>; i <= n; i ++)&#123;
        dp[i] = dp[i - <span class="hljs-number">1</span>] + dp[i - <span class="hljs-number">2</span>]
    &#125;
    <span class="hljs-keyword">return</span> dp[n]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>记忆递归：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">n</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> climbStairs = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>, b = <span class="hljs-number">1</span>, res = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < n; i++) &#123;
        a = b
        b = res
        res = a + b
    &#125;
    <span class="hljs-keyword">return</span> res
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>普通递归复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n2)，递归树的深度为n，所以时间复杂度为O(n2)；</li>
<li>空间复杂度：O(n)，这里需要初始化一个数组用来保存每一层台阶的方法数，有n个数，所以空间复杂度为O(n)；</li>
</ul>
<p><strong>记忆递归复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，需要循环执行n次，所以时间复杂度为O(n)；</li>
<li>空间复杂度：O(1)，这里只用了常数个变量作为辅助空间，所以空间复杂度为 O(1)；</li>
</ul>
<h4 data-id="heading-29">（3）最大正方形</h4>
<p>在一个由 <code>'0'</code> 和 <code>'1'</code> 组成的二维矩阵内，找到只包含 <code>'1'</code> 的最大正方形，并返回其面积。
 </p>
<p><strong>示例 1：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78ab564e2fa44b1991b6de0d4b23531b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：matrix = [[<span class="hljs-string">"1"</span>,<span class="hljs-string">"0"</span>,<span class="hljs-string">"1"</span>,<span class="hljs-string">"0"</span>,<span class="hljs-string">"0"</span>],[<span class="hljs-string">"1"</span>,<span class="hljs-string">"0"</span>,<span class="hljs-string">"1"</span>,<span class="hljs-string">"1"</span>,<span class="hljs-string">"1"</span>],[<span class="hljs-string">"1"</span>,<span class="hljs-string">"1"</span>,<span class="hljs-string">"1"</span>,<span class="hljs-string">"1"</span>,<span class="hljs-string">"1"</span>],[<span class="hljs-string">"1"</span>,<span class="hljs-string">"0"</span>,<span class="hljs-string">"0"</span>,<span class="hljs-string">"1"</span>,<span class="hljs-string">"0"</span>]]
输出：<span class="hljs-number">4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38632ae769cd47f08aad2d60b65a6dd5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：matrix = [[<span class="hljs-string">"0"</span>,<span class="hljs-string">"1"</span>],[<span class="hljs-string">"1"</span>,<span class="hljs-string">"0"</span>]]
输出：<span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 3：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：matrix = [[<span class="hljs-string">"0"</span>]]
输出：<span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>m == matrix.length</code></li>
<li><code>n == matrix[i].length</code></li>
<li><code>1 <= m, n <= 300</code></li>
<li><code>matrix[i][j]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>
<p>对于这道题目，可以使用动态规划来解决，这里我们需要初始化与一个dp数组，dp[i][i]表示以 (i, j)为右下角，且只包含 1 的正方形的边长最大值。我们只需要遍历这个二维矩阵，计算机每个dp的值，选出最大值，即正方形的最大边长，最后返回这个正方形的面积即可。</p>
<p>计算dp的每个值有以下规则：</p>
<ul>
<li>如果当前的值为0，此时该点不存在于正方形中，直接给dp[i][j]赋值为0；</li>
<li>如果当前的值为1，dp[i][j]的值由其上、左、左上的三个值的最小值决定，所以其状态转移方程是：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">dp[i][j] = <span class="hljs-built_in">Math</span>.min(dp[i - <span class="hljs-number">1</span>][j], dp[i][j - <span class="hljs-number">1</span>], dp[i - <span class="hljs-number">1</span>][j - <span class="hljs-number">1</span>]) + <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除此之外，我们还需要考虑二维矩阵的最左边一列和最上面一行，如果值是1，就直接将dp[i][j]赋值为1。</p>
<p>代码实现：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;character[][]&#125;</span> <span class="hljs-variable">matrix</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> maximalSquare = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">matrix</span>) </span>&#123;
    <span class="hljs-keyword">const</span> m = matrix.length, n = matrix[<span class="hljs-number">0</span>].length
    <span class="hljs-keyword">let</span> res = <span class="hljs-number">0</span>
    <span class="hljs-keyword">if</span>(!matrix || m === <span class="hljs-number">0</span> || n === <span class="hljs-number">0</span>)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
    &#125;

    <span class="hljs-keyword">let</span> dp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(m)
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < m; i++)&#123;
        dp[i] = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(n).fill(<span class="hljs-number">0</span>)
    &#125;

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < m; i++)&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < n; j++)&#123;
            <span class="hljs-keyword">if</span>(matrix[i][j] === <span class="hljs-string">'1'</span>)&#123;
                <span class="hljs-keyword">if</span>(i === <span class="hljs-number">0</span> || j === <span class="hljs-number">0</span>)&#123;
                    dp[i][j] = <span class="hljs-number">1</span>
                &#125;<span class="hljs-keyword">else</span>&#123;
                    dp[i][j] = <span class="hljs-built_in">Math</span>.min(dp[i - <span class="hljs-number">1</span>][j], dp[i][j - <span class="hljs-number">1</span>], dp[i - <span class="hljs-number">1</span>][j - <span class="hljs-number">1</span>]) + <span class="hljs-number">1</span>
                &#125;
                res = <span class="hljs-built_in">Math</span>.max(dp[i][j], res)
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> res * res
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(mn)，其中 m 和 n 是二维矩阵的行数和列数。我们需要遍历二维矩阵中的每个元素来计算 dp 的值。</li>
<li>空间复杂度：O(mn)，其中 m 和 n 是二维矩阵的行数和列数。我们创建了一个和原始矩阵大小相同的数组 dp 来保存当前正方形的最大边长。</li>
</ul>
<p><strong>相关文章推荐：</strong></p>
<ul>
<li>
<p><a href="https://juejin.cn/post/6943091553250312229" title="https://juejin.cn/post/6943091553250312229" target="_blank">3.5w字 | 47道 LeetCode 题目带你看看二叉树的那些套路（上）</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6943092291561062436" title="https://juejin.cn/post/6943092291561062436" target="_blank">3.5w字 | 47道 LeetCode 题目带你看看二叉树的那些套路（下）</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6943787446505046046" target="_blank" title="https://juejin.cn/post/6943787446505046046">2w字 | 28道 LeetCode 题目带你看看链表的那些套路</a></p>
</li>
</ul></div>  
</div>
            