
---
title: '1770. Maximum Score from Performing Multiplication Operations'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Documents/1770/1770_Recursion_Tree.svg'
author: LeetCode
comments: false
date: Fri, 12 Aug 2022 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Documents/1770/1770_Recursion_Tree.svg'
---

<div>   
<p>You are given two integer arrays <code>nums</code> and <code>multipliers</code><strong> </strong>of size <code>n</code> and <code>m</code> respectively, where <code>n >= m</code>. The arrays are <strong>1-indexed</strong>.</p>

<p>You begin with a score of <code>0</code>. You want to perform <strong>exactly</strong> <code>m</code> operations. On the <code>i<sup>th</sup></code> operation <strong>(1-indexed)</strong>, you will:</p>

<ul>
<li>Choose one integer <code>x</code> from <strong>either the start or the end </strong>of the array <code>nums</code>.</li>
<li>Add <code>multipliers[i] * x</code> to your score.</li>
<li>Remove <code>x</code> from the array <code>nums</code>.</li>
</ul>

<p>Return <em>the <strong>maximum</strong> score after performing </em><code>m</code> <em>operations.</em></p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3], multipliers = [3,2,1]
<strong>Output:</strong> 14
<strong>Explanation:</strong> An optimal solution is as follows:
- Choose from the end, [1,2,<strong><u>3</u></strong>], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,<strong><u>2</u></strong>], adding 2 * 2 = 4 to the score.
- Choose from the end, [<strong><u>1</u></strong>], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
<strong>Output:</strong> 102
<strong>Explanation: </strong>An optimal solution is as follows:
- Choose from the start, [<u><strong>-5</strong></u>,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [<strong><u>-3</u></strong>,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [<strong><u>-3</u></strong>,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,<strong><u>1</u></strong>], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,<strong><u>7</u></strong>], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>n == nums.length</code></li>
<li><code>m == multipliers.length</code></li>
<li><code>1 <= m <= 10<sup>3</sup></code></li>
<li><code>m <= n <= 10<sup>5</sup></code><code> </code></li>
<li><code>-1000 <= nums[i], multipliers[i] <= 1000</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h3 id="overview">Overview</h3>
<p>As per the problem description, we have to do <code>m</code> operations and find the maximum score. At every operation, we have to select $i^&#123;th&#125;$ integer from <code>multipliers</code> and multiply it with an integer <code>x</code> from <code>nums</code>. The integer <code>x</code> can be chosen from either the start or the end of the <code>nums</code>. And then we have to remove that integer from <code>nums</code>.</p>
<p>At first glance, a greedy approach looks promising. In step <code>i</code>, out of <code>nums[start]</code> and <code>nums[end]</code>, we can pick the integer <code>x</code> that maximizes <code>x * multipliers[i]</code>.</p>
<p>This greedy approach works well for one of the given examples.</p>
<pre><b>nums = [1,2,3], multipliers = [3,2,1]</b>

<b>Taking Decision</b>
‣ From multipliers, we have <b>3</b>, nums is [1, 2, 3], from <b>3</b> * 1 and <b>3</b> * 3, pick 3, add 3 * 3 = <u>9</u>.
‣ From multipliers, we have <b>2</b>, nums is [1, 2], from <b>2</b> * 1 and <b>2</b> * 2, pick 2, add 2 * 2 = <u>4</u>.
‣ From multipliers, we have <b>1</b>, nums is [1], add 1 * 1 = <u>1</u>.

Total Score is <u>9+4+1</u>=<b>14</b>, which is correct
</pre>
<p>However, it fails for the second example.</p>
<pre><b>nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]</b>

<b>Taking Decision</b>
‣ From multipliers, we have <b>10</b>, nums is [-5,-3,-3,-2,7,1], from <b>(-10)</b> * (-5) and <b>(-10)</b> * 1, pick -5, add (-10) * (-5) = <u>50</u>.   
‣ From multipliers, we have <b>-5</b>, nums is [-3,-3,-2,7,1], from <b>(-5)</b> * (-3) and <b>(-5)</b> * 1, pick -3, add (-5) * (-3) = <u>15</u>.   
‣ From multipliers, we have <b>3</b>, nums is [-3,-2,7,1], from <b>3</b> * (-3) and <b>3</b> * 1, pick 1, add 3 * 1 = <u>3</u>.   
‣ From multipliers, we have <b>4</b>, nums is [-3,-2,7], from <b>4</b> * (-3) and <b>4</b> * 7, pick 7, add 4 * 7 = <u>28</u>.   
‣ From multipliers, we have <b>6</b>, nums is [-3,-2], from <b>6</b> * (-3) and <b>6</b> * (-2), pick -2, add 6 * (-2) = <u>-12</u>.   

Total Score is <u>50+15+3+28+(-12)</u>=<b>84</b> which isn't optimal.   
102 is <u>Optimal Solution</u> as given in Problem Example.
</pre>
<p>The logical intuition of <strong>why it is not optimal</strong> can be deduced from the following two cases:</p>
<ol>
<li><p>Greedy is short-sighted. For global optimum, we pick local optimum. But picking this Local Optimum <em>may</em>  restrict greater positive product afterward.      </p>
<pre><code>nums = [-10,1,1000,1,1,100], multipliers = [1,1,1]
</code></pre>
<pre><code>     
</code></pre>
<p>If we pick 100 over -10, we would never ever be able to collect 1000. There are only three elements in <code>multipliers</code>, and we can collect 1000 by taking the left integers only. But selecting 100 at the first point restricts it.</p></li>
<li><p>Moreover, what if both ends of <code>nums</code> are identical? We don't know which one to favor. One may yield another score, another may yield a very different score.     </p>
<pre><code>nums = [2, 1000, -1, 2], multipliers = [1, 1]
</code></pre>
<p><br>
<strong>a.</strong> if we select Left 2 first, then at the next step, there would be a contest between Left 1000 and Right 2. As per approach we now would select left 1000, obtaining <u>1002</u> as the answer.</p>
<p><strong>b.</strong> if we select Right 2 first, then at the next step, there would be a contest between Left 2 and Right -1. As per approach we now would select left 2, obtaining <u>4</u> as the answer.</p></li>
</ol>
<p>Thus, these examples suggest that we have to <strong>look for all two possible combinations</strong> at each step:    </p>
<ol>
<li><p>Select <code>nums[start]</code>, now problem reduces to another subproblem with <code>nums</code> being <code>nums[start+1]</code> to <code>nums[end]</code> and <code>multipliers</code> being <code>multipliers[i+1]</code> to <code>multipliers[m-1]</code>. Moreover, the number of operations is lessened by one.    </p></li>
<li><p>Select <code>nums[end]</code>, now problem reduces to another subproblem with <code>nums</code> being <code>nums[start]</code> to <code>nums[end-1]</code> and <code>multipliers</code> being <code>multipliers[i+1]</code> to <code>multipliers[m-1]</code>. Moreover, the number of operations is lessened by one.</p></li>
</ol>
<p>We then have to solve these subproblems successively and at each step return the maximum of two possible answers. When all operations are done, we can return 0.</p>
<hr>
<h3 id="approach1bruteforce">Approach 1: Brute Force</h3>
<h4 id="intuition">Intuition</h4>
<p>As explained above, at each step we have to reduce the problem to two subproblems, with one less operation. And then we have to repeatedly solve these subproblems. This hints at recursion. Now, for solving each subproblem, we essentially need three things</p>
<ul>
<li><p><code>nums</code>: the remaining integers to be considered</p></li>
<li><p><code>multipliers</code>: the remaining multipliers to be considered</p></li>
<li><p><code>op</code>: number of operations done.</p></li>
</ul>
<p><strong>Minute Improvement:</strong> We need not pass <code>multipliers</code>. We are only interested in its <code>i</code>$^&#123;th&#125;$ element. And this <code>i</code> is closely related to <code>op</code>. If we have done <code>0</code> operations, this implies we have to do the next operation from <code>multipliers[0]</code>. If we have done <code>1</code> operation, this implies we have to do the next operation from <code>multipliers[1]</code>. And so on. </p>
<blockquote>
  <p><strong>Note:</strong> There are two possible definitions of <code>op</code>. However, logically they are equivalent.</p>
  <ul>
  <li><p>One is to define <code>op</code> as the number of operations done. If we have done <code>0</code> operation, this implies we have to do the next operation from <code>multipliers[0]</code>. If we have done <code>1</code> operation, this implies we have to do the next operation from <code>multipliers[1]</code>. And so on. In this case, the terminating condition is <code>op == m</code>, when all operations are done.  </p></li>
  <li><p>Another is to define <code>op</code> as the number of operations remaining, then the indexing of <code>multipliers</code> and base condition will change. If we have <code>m-0</code> operations remaining, this implies we have to do next operation from <code>multipliers[0]</code>. If we have <code>m-1</code> operation remaining, this implies we have to do next operation from <code>multipliers[1]</code>. And so on. In this case, terminating condition is <code>op == 0</code>, when no operation is remaining.      </p></li>
  </ul>
  <p>We have defined <code>op</code> as the number of operations done. </p>
</blockquote>
<h4 id="algorithm">Algorithm</h4>
<ol>
<li><p>Define a <code>helper</code> function that takes two arguments <code>nums</code>, and <code>op</code>.</p></li>
<li><p>If we are done with all operations, <code>op</code>, return 0.</p></li>
<li><p>Otherwise,   </p>
<p>3.1  One time multiply <code>multipliers[op]</code> with <code>nums[0]</code>. Now, solve the subproblem with <code>nums[1:]</code> and <code>op+1</code>. Add the result of the subproblem to the product.  </p>
<p>3.2 Another time multiply <code>multipliers[op]</code> with <code>nums[-1]</code>. Now, solve the subproblem with <code>nums[:-1]</code> and <code>op+1</code>. Add the result of the subproblem to the product.</p></li>
<li><p>Return the maximum of two results.</p></li>
<li><p>Call the <code>helper</code> function with <code>nums</code> and <code>op=0</code> as parameters indicating we have done zero operations so far!</p></li>
</ol>
<h4 id="implementation">Implementation</h4>
<iframe src="https://leetcode.com/playground/HBkrGsTc/shared" frameborder="0" width="100%" height="344" name="HBkrGsTc"></iframe>
<p><strong>Note:</strong> It is likely to give TLE since the time complexity is too high.</p>
<p>Note that in <code>python</code> string slicing creates another copy. This consumes a lot of memory. We can reduce it too likewise we removed the passing of the <code>multipliers</code> array.    </p>
<blockquote>
  <p>In the<code>multipliers</code> array, we were interested in the left pointer, we obtained it very easily with the <code>op</code> parameter.</p>
  <p>In the <code>nums</code> array, we were interested in both <code>left</code> and  <code>right</code> pointers. Thus, instead of passing the entire <code>nums</code>, we can pass these pointers.</p>
</blockquote>
<iframe src="https://leetcode.com/playground/HL7v45vS/shared" frameborder="0" width="100%" height="378" name="HL7v45vS"></iframe>
<p><strong>Note :</strong> It is likely to give TLE because the algorithm is not efficient.</p>
<h4 id="complexityanalysis">Complexity Analysis</h4>
<p>Let $M$ be the size of <code>multipliers</code>, the same as the number of operations.  </p>
<ul>
<li><p>Time complexity: $O(2^M)$.</p>
<p>This can be calculated using the fact that at every step we are reducing the problem of size $M$ to two subproblems of size $M-1$, for doing so we are doing constant time operations (increasing/decreasing <code>left</code>, <code>right</code> and <code>op</code>, and multiplying with <code>y</code> are constant time operations). Thus, the recurrence relation is $T(M)=2T(M-1)+O(1)$, which can be solved using Master Theorem and the result is $O(2^M)$.</p>
<p>Another way of analyzing is that at each step, we branch two sub-tree. The height of the recursion tree will be $M$. Thus, there will be $2^M$ nodes in the recursion tree. </p></li>
<li><p>Space complexity: $O(M)$, the recursion stack will take $O(M)$ space. </p></li>
</ul>
<hr>
<h3 id="approach2recursivedynamicprogramming">Approach 2: Recursive Dynamic Programming</h3>
<h4 id="intuition-1">Intuition</h4>
<p>We can notice that we may need to solve for a particular (<code>left</code>, <code>right</code>, <code>op</code>) state multiple times.<br>
<strong>Example:</strong> <code>nums = [a, b, c, d, e]</code> and <code>multipliers = [u, v, w, x, y]</code></p>
<p><img src="https://leetcode.com/articles/Documents/1770/1770_Recursion_Tree.svg" alt="Overlapping" referrerpolicy="no-referrer"></p>
<p>The tree indicates that from two different paths, we have reached a common state/sub-problem <code>x</code> with <code>c vs d</code>. Thus, we have repeated states. Hence, we can solve this once, and can use its result.</p>
<p>Thus, <strong>Dynamic Programming</strong>. Select best from all possible states and instead of computing again and again, save what you have already computed. Memoizing the pre-visited states while trying all the possible scenarios will reduce the complexity.</p>
<p>To determine a <strong>state</strong>, we essentially need 3 things</p>
<ul>
<li><p><code>left</code>: specify we have used <code>left</code> integers from the left side of <code>nums</code> so far. Next, we may use <code>nums[left]</code></p></li>
<li><p><code>right</code>: specify we have used <code>right</code> integers from the right side of <code>nums</code> so far. Next, we may use <code>nums[right]</code></p></li>
<li><p><code>op</code>: number of operations done.</p></li>
</ul>
<p>Hence, there are 3 state variables, <code>left</code>, <code>right</code>, and <code>op</code>.  Thus, it's a 3D Dynamic Programming problem. And to memoize it, we may need a 3D array.</p>
<blockquote>
  <p>If there are <code>n</code> state variables, then we need an array of <u>at most</u> <code>n</code> dimensions.</p>
</blockquote>
<p>However, with mathematics, we can reduce these 3 state variables to 2. Can you think of how to do that? Try this multiple choice question!<br>
<em>(Note that <code>len(nums)</code> will be constant in this approach, since we are not modifying <code>nums</code> and passing indices instead)</em></p>
<p>!mcq!
&#123;
  "description": " The <code>right</code> is related to <code>op</code>, <code>left</code> and <code>len(nums)</code> as",
  "answer": 1,
  "choices": [
    &#123; "description": "len(nums)-1-left" &#125;,
    &#123; "description": "len(nums)-1-(op-left)" &#125;,
    &#123; "description": "len(nums)-1-op" &#125;,
    &#123; "description": "op-(left-len(nums))" &#125;
  ],
  "explanation": "Now, there are <code>len(nums)</code> elements in <code>nums</code>. If we have accomplished <code>op</code> operations, and the left-pointer is <em>ahead</em> by <code>left</code>, means there are <code>op - left</code> operations from the right side. Thus, <code>right</code> should be <em>behind</em> <code>n-1</code> by <code>op-left</code>. Thus, this formula."
&#125;
!mcq!      </p>
<!---Have used <br> in next line for a reason. After MCQ Explanation there should be one line gap. This gap was not rendered using ENTER. Thus, <br>-->
<p><br>Therefore, we can define a state with only two state variables <code>op</code> and <code>left</code>. We will use <code>dp</code> to denote the state in the following.</p>
<blockquote>
  <p><code>dp[op][left]</code> stores the <strong>maximum possible score</strong> after we have done <code>op</code> total operations and used <code>left</code> numbers from the left/start side.</p>
</blockquote>
<p>From this state, we have two options</p>
<ul>
<li><p><strong>Select Left:</strong> Number of operations will advance by one. And, so does the left pointer. Thus, we will multiply <code>mulitpliers[op]</code> and <code>nums[left]</code> (since we have selected from left), and add this product to (optimal) result of state <code>dp[op+1][left+1]</code>.</p></li>
<li><p><strong>Select Right:</strong> Then also the number of operations will advance by one. Then, we will multiply <code>mulitpliers[op]</code> with <code>nums[n-1-(op-left)]</code> (since we have selected from right), and add this product to (optimal) result of state <code>dp[op+1][left]</code> (Now, <code>left</code> will not increment since number has not been chosen from left).</p></li>
</ul>
<p>Select <strong>maximum</strong> of results obtained by selecting from Left, and Right.<br>
If <code>op == m</code>, means we have performed <code>m</code> operations, add 0. The base Condition of Recursion.</p>
<p>Let $\text&#123;mul&#125;$ represent <code>multipliers</code>, and $\text&#123;nums&#125;$ represent <code>nums</code>. Then we can have the following equation!</p>
<p>$$
dp[op][left] =
\begin&#123;cases&#125;
\text&#123;max&#125;\bigg((\text&#123;mul&#125;[op]\cdot \text&#123;nums&#125;[left]) + dp[op+1][left+1],\\quad\quad\quad(\text&#123;mul&#125;[op]\cdot \text&#123;nums&#125;[n-1-(op-left)]) + dp[op+1][left]\bigg),  & \text&#123;if $op \neq m$ &#125; \[2ex]
0, & \text&#123;if $op=m$&#125;
\end&#123;cases&#125;
$$</p>
<h4 id="algorithm-1">Algorithm</h4>
<ol>
<li><p>Initialize variable <code>m</code> as the size of <code>multipliers</code> and <code>n</code> as the size of <code>nums</code>. Now, <code>m</code> will help us in determining the number of operations, and with help of <code>n</code>, we can calculate the <code>right</code> pointer.</p></li>
<li><p>Create a dictionary <code>memo</code> to memoize states.</p></li>
<li><p>Define a <code>dp</code> function that takes two arguments <code>op</code>, and <code>left</code>.</p></li>
<li><p>If we are done with all operations,  i.e. <code>op == m</code>, return 0.</p></li>
<li><p>If we have already computed and memoized the state, return the value from the dictionary.</p></li>
<li><p>Otherwise,  </p>
<p>6.1.  One time multiply <code>multipliers[op]</code> with <code>nums[left]</code>. Now, solve the subproblem with <code>left+1</code> and <code>op+1</code> as parameters. Add the result of the subproblem to the product. </p>
<p>6.2.  Another time multiply <code>multipliers[op]</code> with <code>nums[(n-1)-(op-left)]</code>. The index points to the right pointer. Now, solve the subproblem with <code>left</code> and <code>op+1</code> as parameters. Add the result of the subproblem to the product.</p></li>
<li><p>Memoize the maximum of 6.1 and 6.2 as the result of state <code>(op, left)</code>.</p></li>
<li><p>Return the memoized result of state <code>op, left</code>.</p></li>
<li><p>Call the <code>dp</code> function with <code>op = 0</code> and <code>left = 0</code>.</p></li>
</ol>
<h4 id="implementation-1">Implementation</h4>
<iframe src="https://leetcode.com/playground/8RNJu5DB/shared" frameborder="0" width="100%" height="500" name="8RNJu5DB"></iframe>
<p><strong>Note:</strong> The <code>python</code> code of top-down DP may give Time Limit Exceeded/Memory Limit Exceeded since it has a larger constant factor.</p>
<h4 id="complexityanalysis-1">Complexity Analysis</h4>
<p>Let $M$ be the size of <code>multipliers</code>, the same as the number of operations.  </p>
<ul>
<li><p>Time complexity: $O(M^2)$.</p>
<p><code>op</code> can vary from <code>0</code> to <code>M-1</code>. Now, in two recursive calls that we are making, one time we are incrementing <code>left</code>, alongwith <code>op</code>. Other time, we are not incrementing <code>left</code>, but incrementing <code>op</code>. So, <code>left</code> is atmost <code>op</code>. Thus, <code>left</code> also varies from <code>0</code> to <code>M-1</code>. So, there are $O(M^2)$ such pairs for computing.</p></li>
<li><p>Space complexity: $O(M^2)$, the <code>memo</code> will store atmost $M^2$ such pairs!</p></li>
</ul>
<hr>
<h3 id="approach3iterativedynamicprogramming">Approach 3: Iterative Dynamic Programming</h3>
<h4 id="intuition-2">Intuition</h4>
<p>Using the same equation, we can solve this problem using iterative dynamic programming. We will start from the base condition, and then we will compute the optimal result for each state.</p>
<p>We need to convert function <code>dp(operation, left)</code> to <code>dp[op][left]</code>. Hence, we need to use a 2D array. But, we only need those cells where <code>op >= left</code>. Hence, we only need the bottom-right triangle, where <code>left</code> will always be less than or equal to <code>op</code>. As you can see in the diagram, red cells are invalid.</p>
<p><img src="https://leetcode.com/articles/Documents/1770/1770_Lower_Half_Triangle.svg" alt="HalfTriangle" referrerpolicy="no-referrer"></p>
<p>Since we know the base condition, we can start from <code>op = m</code> and fill it up. Moreover, since the number of operations at any stage is greater than or equal to the integer chosen from left (<code>op >= left</code>), the <code>left</code> will drop from <code>op</code> to <code>0</code>. </p>
<h4 id="algorithm-2">Algorithm</h4>
<ol>
<li><p>Create a 2D array <code>dp</code> of size <code>m+1</code> by <code>m+1</code>. Reason being <code>op</code> can vary from <code>0</code> to <code>m</code>, and so does <code>left</code>. </p></li>
<li><p>Initialized all elements to <code>0</code>. By this initialization, we have filled the base condition, that when we have done <code>m</code> operations, and this operation will add nothing to the result.</p></li>
<li><p>Iterate over <code>op</code> from <code>m-1</code> to <code>0</code>.</p></li>
<li><p>For each <code>op</code>, iterate over <code>left</code> from <code>op</code> to <code>0</code>.</p></li>
<li><p>Using the equation, compute the optimal result for state <code>dp[op][left]</code>.</p></li>
<li><p>We have formulated the problem in such a way that <code>dp[0][0]</code> will force us to do <code>m</code> operations in a row. In other words, <code>dp[0][0]</code> stores the optimal answer. Hence, we can return <code>dp[0][0]</code> at the end.</p></li>
</ol>
<h4 id="implementation-2">Implementation</h4>
<iframe src="https://leetcode.com/playground/d3HGz2PK/shared" frameborder="0" width="100%" height="412" name="d3HGz2PK"></iframe>
<h4 id="complexityanalysis-2">Complexity Analysis</h4>
<p>Let $M$ be the size of <code>multipliers</code>, the same as the number of operations.  </p>
<ul>
<li><p>Time complexity: $O(M^2)$  </p>
<p><code>op</code> varies from <code>M-1</code> to <code>0</code>, and <code>left</code> varies from  to <code>op</code> to <code>0</code>. This is equivalent to iterating half matrix of order $M\times M$. So, we are computing $O(\frac&#123;M^2&#125;&#123;2&#125;)$ states.</p></li>
<li><p>Space complexity: $O(M^2)$, as evident from <code>dp</code> array.</p></li>
</ul>
<hr>
<h3 id="approach4spaceoptimizeddynamicprogramming">Approach 4: Space Optimized Dynamic Programming</h3>
<h4 id="intuition-3">Intuition</h4>
<p>On carefully eyeing mathematical formula and iterative code, we can say that for computing present row $dp[op]$, we need next row $dp[op+1]$ ONLY. Therefore, we can have 1D Array only. We will fill the <code>dp</code> array from bottom to top, saving the next row in a temporary array, and then computing the present row using the saved temporary array. </p>
<blockquote>
  <p><strong>Interview Tip:</strong> Always spend time on <strong>forming</strong> and <strong>analyzing</strong> Dynamic Programming Equation. For Dynamic Programming, forming an equation requires time. Writing code isn't tough in most cases. Moreover, by analyzing the equation, quite a few times, we can solve the problem using less space.</p>
</blockquote>
<h4 id="algorithm-3">Algorithm</h4>
<ol>
<li><p>Create a 1D array <code>dp</code> of size <code>m+1</code>. Initialize all elements to <code>0</code>.</p></li>
<li><p>Iterate over <code>op</code> from <code>m-1</code> to <code>0</code>.</p></li>
<li><p>Since <code>dp</code> array will be modified using next row, and this next row result is saved in <code>dp</code> only, we need to use a temporary array to store the next row. Thus, save all current entries of <code>dp</code> in <code>next_row</code>.</p></li>
<li><p>For each <code>op</code>, iterate over <code>left</code> from <code>op</code> to <code>0</code>.</p></li>
<li><p>Using the equation, compute the optimal result for state <code>dp[left]</code>.</p></li>
<li><p>Return <code>dp[0]</code> at the end.</p></li>
</ol>
<h4 id="implementation-3">Implementation</h4>
<iframe src="https://leetcode.com/playground/X3vzCtYe/shared" frameborder="0" width="100%" height="395" name="X3vzCtYe"></iframe>
<h4 id="complexityanalysis-3">Complexity Analysis</h4>
<p>Let $M$ be the size of <code>multipliers</code>, the same as the number of operations.  </p>
<ul>
<li><p>Time complexity: $O(M^2)$  </p>
<p><code>op</code> varies from <code>M-1</code> to <code>0</code>, and <code>left</code> varies from  to <code>op</code> to <code>0</code>. This is equivalent to iterating half matrix of order $M\times M$. So, we are computing $O(\frac&#123;M^2&#125;&#123;2&#125;)$ states.</p></li>
<li><p>Space complexity: $O(M)$, since we have used <code>dp</code> array of size <code>M</code>.</p></li>
</ul>
<hr>  
</div>
            