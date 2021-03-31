
---
title: '970. Powerful Integers'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=3133'
author: LeetCode
comments: false
date: Mon, 22 Mar 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3133'
---

<div>   
<p>Given three integers <code>x</code>, <code>y</code>, and <code>bound</code>, return <em>a list of all the <strong>powerful integers</strong> that have a value less than or equal to</em> <code>bound</code>.</p>

<p>An integer is <strong>powerful</strong> if it can be represented as <code>x<sup>i</sup> + y<sup>j</sup></code> for some integers <code>i >= 0</code> and <code>j >= 0</code>.</p>

<p>You may return the answer in <strong>any order</strong>. In your answer, each value should occur <strong>at most once</strong>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> x = 2, y = 3, bound = 10
<strong>Output:</strong> [2,3,4,5,7,9,10]
<strong>Explanation:</strong>
2 = 2<sup>0</sup> + 3<sup>0</sup>
3 = 2<sup>1</sup> + 3<sup>0</sup>
4 = 2<sup>0</sup> + 3<sup>1</sup>
5 = 2<sup>1</sup> + 3<sup>1</sup>
7 = 2<sup>2</sup> + 3<sup>1</sup>
9 = 2<sup>3</sup> + 3<sup>0</sup>
10 = 2<sup>0</sup> + 3<sup>2</sup>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> x = 3, y = 5, bound = 15
<strong>Output:</strong> [2,4,6,8,10,14]
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= x, y <= 100</code></li>
<li><code>0 <= bound <= 10<sup>6</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>We rarely come across problems where the simplest solution, a brute-force solution, is the optimal one. Luckily for us, this is one of those problems! As we can see from the description given for the first example, both the numbers have powers that range from <code>0</code> to a certain higher value. E.g. in the case where <code>x = 2</code>, <code>y = 3</code>, and <code>bound = 10</code>, the power of <code>x</code> ranges from <code>0..3</code> and the power of <code>y</code> ranges from <code>0..2</code>. More specifically we have</p>
<p>$$
x^a + y^b <= bound
$$</p>
<p>If we know the bounds for <code>a</code> and <code>b</code>, then we can simply use a nested loop to find all possible powerful integers. It all boils down to determining these bounds. <strong>Note</strong> that the problem statement asks us to find <em>all</em> powerful integers. Had the problem statement been to find <em>how many</em> powerful integers there are, we might have been able to use some mathematical formula to find the exact count. However, because the problem asks us to list all the values, we have to use a nested-loop-based brute-force solution to find and list all such values.</p>
<p><br></p>
<hr>
<h4 id="approachlogartihmicbounds">Approach: Logartihmic Bounds</h4>
<p><strong>Intuition</strong></p>
<p>Our approach here will only focus on finding the bounds for numbers <code>x</code> and <code>y</code>. One way to get the bounds on the powers is to have nested loops that iterate from $$[0 \cdots \text&#123;bound&#125;]$$. However, this is very inefficient because the <code>bound</code> can be an extremely large value and a nested-loop over this <code>bound</code> will take forever to finish. Also, we don't need to iterate over all of the values and combinations.  There is a way to find a much smaller bound for the powers. </p>
<p>$$
m^n <= \text&#123;bound&#125;
$$</p>
<p>This formula implies that</p>
<p>$$
n <= \log_m \text&#123;bound&#125;
$$</p>
<blockquote>
  <p>We can use the log function to determine the bounds for the powers of "x" and "y".</p>
</blockquote>
<p><strong>Algorithm</strong></p>
<ol>
<li>Let's define <code>a</code> as the power bound for the number <code>x</code>. Thus $$\text&#123;a&#125; = \log_x \text&#123;bound&#125;$$.</li>
<li>Similarly, let's define <code>b</code> as the power bound for the number <code>y</code>. Thus $$\text&#123;b&#125; = \log_y \text&#123;bound&#125;$$.</li>
<li>Now we will have our nested for-loop structure where the outer loop will iterate from $$[0 \cdots a]$$ and the inner loop will iterate from $$[0 \cdots b]$$.</li>
<li>We will use a set to store our results. This is because we might generate the same value multiple times. E.g. <code>2^1 + 3^2 = 11</code> and <code>2^3 + 3^1 = 11</code>. We only need to include the value <code>11</code> once and hence, we will use a set called <code>powerfulIntegers</code> to store our answers.</li>
<li>At each step, we calculate <code>x^a + y^b</code> and check if this value is less than or equal to <code>bound</code>. If it is, then this is a powerful integer and we add it to our set of answers.</li>
<li>We need special break conditions to handle the scenario when <code>x</code> or <code>y</code> is <code>1</code>. This is because if the number <code>x</code> or <code>y</code> is <code>1</code>, then their power-bound will be equal to <code>bound</code> itself. Also, it doesn't matter what their power-bound is because $$1^N$$ is always $$1$$. Thus, when the number is <code>1</code>, we don't need to loop from $$[0 \cdots N]$$ and we can break early.</li>
<li>Finally, convert the set to a list and return.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/eFNDhPqT/shared" frameborder="0" width="100%" height="500" name="eFNDhPqT"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity: Let $$N$$ be $$\text&#123;log&#125;<em>x \text&#123;bound&#125;$$ and $$M$$ be $$\text&#123;log&#125;</em>y \text&#123;bound&#125;$$. Then the overall time complexity is $$O(N \times M)$$ because we used a nested loop structure to calculate all of the powerful integers.</p></li>
<li><p>Space Complexity: $$O(N \times M)$$ because we use a set to omit duplicates. We could just use our result list to check membership before adding values. However, that would be costly in terms of time complexity because it would require a full scan of the result list to see if the value already exists.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            