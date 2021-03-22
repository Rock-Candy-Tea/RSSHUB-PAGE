
---
title: '322. Coin Change'
categories: 
    - 编程
    - LeetCode - 文章
author: LeetCode - 文章
comments: false
date: Wed, 10 Mar 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/media/original_images/322_coin_change_tree.png'
---

<div>   
<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>

<p>Return <em>the fewest number of coins that you need to make up that amount</em>. If that amount of money cannot be made up by any combination of the coins, return <code>-1</code>.</p>

<p>You may assume that you have an infinite number of each kind of coin.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> coins = [1,2,5], amount = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> 11 = 5 + 5 + 1
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> coins = [2], amount = 3
<strong>Output:</strong> -1
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> coins = [1], amount = 0
<strong>Output:</strong> 0
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> coins = [1], amount = 1
<strong>Output:</strong> 1
</pre>

<p><strong>Example 5:</strong></p>

<pre><strong>Input:</strong> coins = [1], amount = 2
<strong>Output:</strong> 2
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= coins.length <= 12</code></li>
<li><code>1 <= coins[i] <= 2<sup>31</sup> - 1</code></li>
<li><code>0 <= amount <= 10<sup>4</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="videosolution">Video Solution</h2>
<hr>
<div class="video-preview"></div>
<div> 
</div>
<h2 id="solutionarticle">Solution Article</h2>
<hr>
<h4 id="approach1bruteforcetimelimitexceeded">Approach #1 (Brute force) [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>The problem could be modeled as the following optimization problem :
$$
\min<em>&#123;x&#125; \sum</em>&#123;i=0&#125;^&#123;n - 1&#125; x<em>i \
\text&#123;subject to&#125; \sum</em>&#123;i=0&#125;^&#123;n - 1&#125; x<em>i*c</em>i = S
$$</p>
<p>, where $$S$$ is the amount,    $$c<em>i$$ is the coin denominations, $$x</em>i$$  is the number of coins with denominations $$c<em>i$$ used in change of amount $$S$$. We could easily see that $$x</em>i = [&#123;0, \frac&#123;S&#125;&#123;c_i&#125;&#125;]$$.</p>
<p>A trivial solution is to enumerate all subsets of coin frequencies $$[x<em>0\dots\ x</em>&#123;n - 1&#125;]$$  that satisfy the constraints above, compute their sums and return the minimum among them.</p>
<p><strong>Algorithm</strong></p>
<p>To apply this idea, the algorithm uses backtracking technique 
to generate all combinations of coin frequencies $$[x<em>0\dots\ x</em>&#123;n-1&#125;]$$ 
in the range $$([&#123;0, \frac&#123;S&#125;&#123;c_i&#125;&#125;])$$ which satisfy the constraints above. It makes a sum of the combinations and returns their minimum or $$-1$$ in case there is no acceptable combination.</p>
<iframe src="https://leetcode.com/playground/bLMVsjQ9/shared" frameborder="0" width="100%" height="497" name="bLMVsjQ9"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : $$O(S^n)$$. In the worst case, complexity is exponential in the number of the coins $$n$$. The reason is that every coin denomination $$c<em>i$$ could have at most $$\frac&#123;S&#125;&#123;c</em>i&#125;$$ values. Therefore the number of possible combinations is :</li>
</ul>
<p>$$
\frac&#123;S&#125;&#123;c<em>1&#125;<em>\frac&#123;S&#125;&#123;c</em>2&#125;</em>\frac&#123;S&#125;&#123;c<em>3&#125;\ldots\frac&#123;S&#125;&#123;c</em>n&#125; = \frac&#123;S^&#123;n&#125;&#125;&#123;&#123;c<em>1&#125;<em>&#123;c</em>2&#125;</em>&#123;c<em>3&#125;\ldots&#123;c</em>n&#125;&#125;
$$</p>
<ul>
<li>Space complexity : $$O(n)$$.
In the worst case the maximum depth of recursion is $$n$$. Therefore we need $$O( n)$$ space used by the system recursive stack.</li>
</ul>
<hr>
<h4 id="approach2dynamicprogrammingtopdownaccepted">Approach #2 (Dynamic programming - Top down) [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Could we improve the exponential solution above? Definitely! The problem could be solved with polynomial time using Dynamic programming technique. First, let's define:</p>
<blockquote>
  <p>$$F(S)$$ - minimum number of coins needed to make change for amount $$S$$ using coin denominations $$[&#123;c<em>0\ldots c</em>&#123;n-1&#125;&#125;]$$</p>
</blockquote>
<p>We note that this problem has an optimal substructure property, which is the key piece in solving any Dynamic Programming problems. In other words, the optimal solution can be constructed from optimal solutions of its subproblems.
How to split the problem into subproblems? Let's assume that we know $$F(S)$$ where some change $$val<em>1, val</em>2, \ldots$$ for $$S$$ which is optimal and the last coin's denomination is $$C$$.
Then the following equation should be true because of optimal substructure of the problem:</p>
<p>$$
F(S) = F(S - C) + 1
$$</p>
<p>But we don't know which is the denomination of the last coin $$C$$. We compute  $$F(S - c<em>i)$$ for each possible denomination $$c</em>0, c<em>1, c</em>2 \ldots c_&#123;n -1&#125;$$ and choose the minimum among them. The following recurrence relation holds:</p>
<p>$$
F(S) = \min<em>&#123;i=0 … n-1&#125; &#123; F(S - c</em>i) &#125; + 1 \
\text&#123;subject to&#125; \ \  S-c_i \geq 0 \
$$</p>
<p>$$
F(S) = 0 \ , \text&#123;when&#125; \ S = 0 \
F(S) = -1 \ , \text&#123;when&#125; \ n = 0
$$</p>
<p><img src="https://leetcode.com/media/original_images/322_coin_change_tree.png" alt="Recursion tree for finding coin change of amount 6 with coin denominations &#123;1,2,3&#125;." referrerpolicy="no-referrer">&#123;:width="100%"&#125;
&#123;:align="center"&#125;</p>
<p>In the recursion tree above, we could see that a lot of subproblems were calculated multiple times.  For example the problem $$F(1)$$ was calculated $$13$$ times. Therefore we should cache the solutions to the subproblems in a table and access them in constant time when necessary</p>
<p><strong>Algorithm</strong></p>
<p>The idea of the algorithm is to build the solution of the problem from top to bottom. It applies the idea described above. It use backtracking and cut the partial solutions in the recursive tree, which doesn't lead to a viable solution. Тhis happens when we try to make a change of a coin with a value greater than the amount <em>$$S$$</em>. To improve  time complexity we should store the solutions of the already calculated subproblems in a table.</p>
<iframe src="https://leetcode.com/playground/Nv8g2Moo/shared" frameborder="0" width="100%" height="412" name="Nv8g2Moo"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity : $$O(S<em>n)$$. where S is the amount, n is denomination count.
In the worst case the recursive tree of the algorithm has height of $$S$$ and the algorithm  solves only $$S$$ subproblems because it caches precalculated solutions in a table. Each subproblem is computed with  $$n$$ iterations, one by coin denomination. Therefore there is $$O(S</em>n)$$ time complexity.</p></li>
<li><p>Space complexity : $$O(S)$$, where $$S$$ is the amount to change
We use extra space for the memoization table.</p></li>
</ul>
<hr>
<h4 id="approach3dynamicprogrammingbottomupaccepted">Approach #3 (Dynamic programming - Bottom up) [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>For the iterative solution, we think in bottom-up manner. Before calculating <em>$$F(i)$$</em>, we have to compute all minimum counts for amounts up to $$i$$. On each iteration $$i$$ of the algorithm <em>$$F(i)$$</em> is computed as $$\min<em>&#123;j=0 \ldots n-1&#125;&#123;F(i -c</em>j)&#125; + 1$$</p>
<p><img src="https://leetcode.com/media/original_images/322_coin_change_table.png" alt="Bottom-up approach using a table to build up the solution to F6." referrerpolicy="no-referrer">&#123;:width="539px"&#125;
&#123;:align="center"&#125;</p>
<p>In the example above you can see that:</p>
<p>$$
\begin&#123;align&#125;
F(3) &= \min&#123;&#123;F(3- c<em>1), F(3-c</em>2), F(3-c_3)&#125;&#125; + 1 \
&= \min&#123;&#123;F(3- 1), F(3-2), F(3-3)&#125;&#125; + 1 \
&= \min&#123;&#123;F(2), F(1), F(0)&#125;&#125; + 1 \
&= \min&#123;&#123;1, 1, 0&#125;&#125; + 1 \
&= 1
\end&#123;align&#125;
$$</p>
<iframe src="https://leetcode.com/playground/gAL5xEtG/shared" frameborder="0" width="100%" height="327" name="gAL5xEtG"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : $$O(S*n)$$.
On each step the algorithm finds the next *$$F(i)$$* in $$n$$ iterations, where $$1\leq i \leq S$$. Therefore in total the iterations are $$S*n$$.</li>
<li>Space complexity : $$O(S)$$.
We use extra space for the memoization table.</li>
</ul>  
</div>
            