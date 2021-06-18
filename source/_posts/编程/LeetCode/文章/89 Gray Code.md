
---
title: '89. Gray Code'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/89/89_Gray_Code_Table.png'
author: LeetCode
comments: false
date: Sat, 05 Jun 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/89/89_Gray_Code_Table.png'
---

<div>   
<p>An <strong>n-bit gray code sequence</strong> is a sequence of <code>2<sup>n</sup></code> integers where:</p>

<ul>
<li>Every integer is in the <strong>inclusive</strong> range <code>[0, 2<sup>n</sup> - 1]</code>,</li>
<li>The first integer is <code>0</code>,</li>
<li>An integer appears <strong>no more than once</strong> in the sequence,</li>
<li>The binary representation of every pair of <strong>adjacent</strong> integers differs by <strong>exactly one bit</strong>, and</li>
<li>The binary representation of the <strong>first</strong> and <strong>last</strong> integers differs by <strong>exactly one bit</strong>.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>any valid <strong>n-bit gray code sequence</strong></em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> [0,1,3,2]
<strong>Explanation:</strong>
The binary representation of [0,1,3,2] is [00,01,11,10].
- 0<u>0</u> and 0<u>1</u> differ by one bit
- <u>0</u>1 and <u>1</u>1 differ by one bit
- 1<u>1</u> and 1<u>0</u> differ by one bit
- <u>1</u>0 and <u>0</u>0 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- <u>0</u>0 and <u>1</u>0 differ by one bit
- 1<u>0</u> and 1<u>1</u> differ by one bit
- <u>1</u>1 and <u>0</u>1 differ by one bit
- 0<u>1</u> and 0<u>0</u> differ by one bit
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> [0,1]
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= n <= 16</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>According to <a href="https://en.wikipedia.org/wiki/Gray_code">Wikipedia</a> the reflected binary code (RBC) or Gray code, named after Frank Gray, is an ordering of the binary numeral system such that two successive values differ by only one bit (binary digit).</p>
<p>The Gray code sequence for <code>n = 3</code> bit numbers is: <code>[000, 001, 011, 010, 110, 111, 101, 100]</code>. The difference in decimal, binary, Gray code sequence can be better understood using this table:</p>
<p><img src="https://leetcode.com/articles/Figures/89/89_Gray_Code_Table.png" alt="fig" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1. The decimal, binary, Gray code, Gray decimal sequence generated for n = 3 bits</em>
&#123;:align="center"&#125;</p>
<p>Next, if you observe the Gray code sequence, you'll find some patterns. For example the $$0^&#123;th&#125;$$ bit (from the right) at every consecutive gray decimal number has the following pattern: <code>0 1 1 0</code> (these are the last bits of each number in the Gray Decimal column). Similarly, the $$1^&#123;st&#125;$$ bit at every consecutive Gray Decimal number has the following pattern: <code>0 0 1 1 1 1 0 0</code>. If you partition these sequences at their center, you get two sequences that are mirror images of each other. Next, consider the first $$2 ^ 1 = 2$$ numbers, then the first $$2 ^ 2 = 4$$ numbers and so on in the above table. For the first $$2 ^ n$$ numbers, a similar mirror image pattern is visible upon partitioning the sequence into two halves. The first <code>n - 1</code> bits (from the right) are mirror images in the two partitions. The most significant bit (MSB) is set to <code>0</code> in the numbers of the first half and <code>1</code> in the second half. Now that we have observed these patterns, lets look at the implementation (five different approaches).</p>
<p>Note that we need to return the numbers in the resulting sequence in decimal form i.e, the answer for <code>n = 3</code> will be <code>[0,1,3,2,6,7,5,4]</code> (not <code>[000, 001, 011, 010, 110, 111, 101, 100]</code>). Also for a particular <code>n</code> there can be more than one valid sequence. For example for <code>n = 2</code> both of the following sequences are valid : <code>[00, 01, 11, 10]</code> and <code>[00, 10, 11, 01]</code>. Also, the Gray code sequence of <code>n</code> bits will be of length $$2 ^ n$$ and it consists of unique numbers ranging from $$0$$ to $$2 ^ n - 1$$.</p>
<p><br></p>
<hr>
<h4 id="approach1backtracking">Approach 1: Backtracking</h4>
<p><strong>Intuition</strong></p>
<p>If you're not familiar with backtracking, check out our <a href="https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/">Explore Card</a>.</p>
<p>In the Gray code sequence, the adjacent numbers in the sequence should differ by only one bit (binary digit). Also, we know that the Gray code sequence always starts with $$0$$. As a brute force solution, we can start a Depth First Search from the number $$0$$. For a given number, we will try all possibilities i.e, we continue with all possible numbers which satisfy two conditions: </p>
<ol>
<li>They are not a part of the current sequence.</li>
<li>Their binary representation differs from the current number by exactly one bit.</li>
</ol>
<p>We will stop our search when no number satisfies the above conditions or when the length of the sequence reaches $$2 ^ n$$ where <code>n</code> is the total number of bits in the code (<code>n</code> bits will produce $$2 ^ n$$ length sequence). </p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize a <code>result</code> list to store the solution sequence. Add <code>0</code> to the list before calling the helper method as all gray code sequences start with <code>0</code>.</p></li>
<li><p>Initialize a set <code>visited</code>. This keeps track of the numbers present in the current sequence to prevent repetition.</p></li>
<li><p>Start with the number <code>0</code>.</p></li>
<li><p>In the <code>grayCodeHelper()</code> function, use a <code>for</code> loop to find each possible number (<code>next</code>) that can be generated by changing one bit of the last number in the <code>result</code> list (<code>current</code>). We do so by toggling the $$i^&#123;th&#125;$$ bit at each iteration. Since the maximum possible number of bits present in any number of the sequence is <code>n</code>, we need to toggle <code>n</code> bits. </p></li>
<li><p>If <code>next</code> is not present in the set of used numbers (<code>isPresent</code>) add it to the <code>result</code> list and the <code>isPresent</code> set. </p></li>
<li><p>Continue the search with <code>next</code>. </p>
<ul>
<li><p>If <code>grayCodeHelper(next)</code> returns true, it means we have found a valid sequence. So no further search is required (<strong>early stop</strong>). This early termination improves the runtime.</p></li>
<li><p>If no valid sequence is found with <code>next</code>, we remove it from the <code>result</code> list and the <code>isPresent</code> set and continue our search.</p></li></ul></li>
<li><p>Upon reaching the base condition, when the length of the current sequence is $$2 ^ n$$, return <code>true</code>.</p></li>
<li><p>Exiting the <code>for</code> loop implies no valid Gray code sequence was found with <code>current</code> as the last number. So return <code>false</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/G5eSbwso/shared" frameborder="0" width="100%" height="500" name="G5eSbwso"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here $$n$$ is the total number of bits in the Gray code.</p>
<ul>
<li><p>Time complexity: $$O(n* 2 ^ n)$$</p>
<p>For $$n$$ bits $$2 ^ n$$ numbers are possible. The maximum depth of the recursive function stack is $$2 ^ n$$ (The recursion stops when the size of <code>result</code> list is $$2 ^ n$$). </p>
<p>In our backtracking algorithm, at every function call we iterate over a loop of length $$n$$ and try to find out all possible successors of the last added number in the present sequence. We continue our search with the first value that succeeds (not present in the <code>isPresent</code> set). Since we are using <code>HashSet</code> and <code>unordered_set</code> which have an amortized runtime of $$O(1)$$ in all operations, use of sets doesn't increase the time complexity.</p>
<p>Another key observation is that in this particular problem the program never backtracks and always finds a path forward. We can check this by executing the solution after removing the following lines from our code:</p>
<pre><code>            isPresent.erase(next);
            result.pop_back();
</code></pre>
<p>This means that greedily changing the right-most bit that does not result in a number already in <code>result</code>, will always lead to the solution. However, we would not know that beforehand while we are coming up with the solution, so we have to assume that backtracking may be needed should something not work out. So in theory the runtime is $$O(2^n)!$$ but in practice, it comes out to $$O(n * 2 ^ n)$$.</p></li>
<li><p>Space complexity: $$O(2 ^ n)$$</p>
<p>We use a set <code>isPresent</code> which will contain at most $$2 ^ n$$ numbers. The space occupied by the output <code>result</code> is not considered in the space complexity analysis.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2recursion">Approach 2: Recursion</h4>
<p><strong>Intuition</strong></p>
<p>If you're not familiar with recursion, check out our <a href="https://leetcode.com/explore/learn/card/recursion-i/">Explore Card</a>.</p>
<p>Consider the sequence generated for <code>n = 0 to 3</code>.</p>
<p>For <code>n = 0</code> the Gray code sequence is <code>[0]</code>.</p>
<p>For <code>n = 1</code> the Gray code sequence is <code>[0, 1]</code>.</p>
<p>Similarly, we had <code>[0, 1]</code> from <code>n = 1</code> and for <code>n = 2</code> the Gray code sequence is <code>[00, 01, 11, 10]</code>.</p>
<p>By observing the sequences generated with n = 0, 1, 2…. we will find a pattern. We can obtain the Gray code sequence for <code>n</code> from the Gray code sequence for <code>n - 1</code>.</p>
<p>For example the Gray code sequence for <code>n = 3</code> is <code>[000, 001, 011, 010, 110, 111, 101, 100]</code> (<code>G(3)</code>). This sequence can be obtained from the sequence <code>[00, 01, 11, 10]</code>(say <code>G(2)</code>) for <code>n = 2</code> as follows :</p>
<ol>
<li><p>Add <code>0</code> to the $$(n - 1)^&#123;th&#125;$$ position (0 based indexed, the $$2^&#123;nd&#125;$$ bit from the right) to the entire sequence of <code>G(2)</code>. 
<code>[00, 01, 11, 10]</code> -> <code>[000, 001, 011, 010]</code> (<code>G(3a)</code>).</p></li>
<li><p>Reverse <code>G(2)</code> sequence and add <code>1</code> (<code>1 << n - 1</code>) to the $$(n - 1)^&#123;th&#125;$$ position (the $$2^&#123;nd&#125;$$ bit from the right)
<code>[00, 01, 11, 10]</code> -> <code>[10, 11, 01, 00]</code> -> <code>[110, 111 101, 100]</code> (<code>G(3b)</code>).</p></li>
<li><p>Concatenate <code>G(3a)</code> and <code>G(3b)</code> to get the Gray code sequence for <code>n = 3</code> (<code>G(3)</code>) : <code>[000, 001, 011, 010, 110, 111, 101, 100]</code></p></li>
</ol>
<p>This can be better understood with the following animation.</p>
<p>!?!../Documents/89<em>Gray</em>Code.json:960,540!?!</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize a list <code>result</code> which will return the Gray code sequence for the value of <code>n</code>.</p></li>
<li><p>Use a recursive helper function <code>grayCodeHelper</code> and pass the <code>result</code> list as a reference.</p></li>
<li><p>At base condition (<code>n = 0</code>) add the number <code>0</code> to <code>result</code> and return. This is because the Gray code sequence starts with <code>0</code>.</p></li>
<li><p>As demonstrated in the intuition section, we can derive the sequence for <code>n</code> from the sequence for <code>n - 1</code>. So make a recursive call to <code>grayCodeHelper</code> function with <code>n - 1</code>.</p></li>
<li><p>Set the bit at $$(n - 1)^&#123;th&#125;$$ position and assign it to a variable <code>mask</code>. <code>mask</code> is used to set the $$(n - 1)^&#123;th&#125;$$ bit from the least significant bit (LSB) of all the numbers present in the current list <code>result</code>.</p></li>
<li><p>Iterate backward over the <code>result</code> list. </p></li>
<li><p>Set the $$(n - 1)^&#123;th&#125;$$ bit of the $$i^&#123;th&#125;$$ number and add the new number formed to the <code>result</code> list. Thus, the size of the <code>result</code> list will double.</p></li>
<li><p>The <code>result</code> list contains a valid Gray code sequence for the current given number of bits. Return the <code>result</code> list.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/gByZPTWr/shared" frameborder="0" width="100%" height="497" name="gByZPTWr"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here $$n$$ is the total number of bits in the code.</p>
<ul>
<li><p>Time complexity: $$O(2 ^ n)$$</p>
<p>The maximum depth of the recursive function stack is $$n$$. At every function call we iterate over the list <code>result</code> and at each iteration we add a new number to the sequence. At $$n = 0$$ the size of the list is $$1$$. At $$n = 1$$ we iterate over the list $$[0]$$ of size $$2 ^ 0 = 1$$. Next, at $$n = 2$$ we iterate over the list $$[0, 1]$$ of size $$2 ^ 1 = 2$$. Likewise, at $$n = 3$$ we iterate over the list $$[0, 1, 3, 2]$$ of size $$2 ^ 2 = 4$$. This ends at $$n$$ where we iterate over a list of size $$2 ^ &#123;n - 1&#125;$$.</p>
<p>The mathematical expression for the above analysis reflects a geometric progression as follows $$1 + 2 + 4 + 8 + ……2 ^&#123;n - 1&#125;$$. Thus the time complexity will be $$O(2 ^ n)$$.</p></li>
<li><p>Space complexity: $$O(n)$$</p>
<p>We start from $$n$$ and continue our recursive function call until our base condition $$n = 0$$ is reached. Thus, the depth of the function call stack will be $$O(n)$$.</p>
<p>All $$2 ^ n$$ numbers are added to the same list. At every function call, we iterate over the list, and at each iteration, we add a new number to the sequence. Thus, the size of the list <code>result</code> at the end of a function call is twice its size at the previous function call.</p>
<p>The space occupied by the output <code>result</code> is not considered in the space complexity analysis.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3iteration">Approach 3: Iteration</h4>
<p><strong>Intuition</strong></p>
<p>The concept used in Approach 2 can be applied iteratively. The iterative method of generating <code>G(n)</code> from <code>G(n - 1)</code> involves using two for loops instead of making recursive calls to find <code>G(n - 1)</code>.</p>
<p>Recall that <code>G(n)</code> is the Gray code sequence consisting of numbers between $$0$$ to $$2 ^&#123;n - 1&#125;$$. We iteratively find <code>G(n - 1)</code> first. Then we add the prefix $$0$$ to each digit of <code>G(n - 1)</code>. Next, we reverse <code>G(n - 1)</code> and add the prefix $$1$$ to each digit of the reversed <code>G(n - 1)</code> sequence. Finally, combining the above two sequences gives us <code>G(n)</code>.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize an empty list <code>result</code> and add $$0$$ to it.</p></li>
<li><p>Since the Gray code sequence for $$i$$ bits (<code>G(i)</code>) can be constructed from the Gray code sequence for $$i - 1$$ bits (<code>G(i - 1)</code>), we run a for loop from $$\text&#123;i&#125; \hspace&#123;3pt&#125; = 1 \hspace&#123;3pt&#125; \text&#123;to&#125; \hspace&#123;3pt&#125; n$$ to find Gray code sequences with increasing bits.</p>
<ul>
<li><p>At each iteration, we set the bit at $$(i - 1)^&#123;th&#125;$$ position and assign it to a variable <code>mask</code>. <code>mask</code> is used to set the $$(i - 1)^&#123;th&#125;$$ bit from the LSB of all the numbers present in the current sequence <code>result</code> (<code>G(i - 1)</code>).</p></li>
<li><p>Iterate backward over the current sequence <code>result</code>. Add prefix $$1$$ (<code>mask</code>) to each number present in <code>result</code>.</p></li></ul></li>
<li><p>Return <code>result</code> which represents the Gray code sequence with <code>n</code> total bits. </p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/MTVp6R3C/shared" frameborder="0" width="100%" height="327" name="MTVp6R3C"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here $$n$$ is the total number of bits in the Gray code.</p>
<ul>
<li><p>Time complexity: $$O(2 ^ n)$$</p>
<p>One insight regarding the time complexity is that in the iterative algorithm, we are building the list in a deterministic and non-redundant way. This means that there is no backtracking, each iteration will produce a series of valid elements in the final sequence.
Since the total number of elements in the final sequence is $$2 ^ n$$, it will take a total of $$2 ^ n$$ steps to produce the sequence.</p>
<p>Here the outer loop runs from $$i = 1 \hspace&#123;3pt&#125; \text&#123;to&#125; \hspace&#123;3pt&#125; n$$. At $$i^&#123;th&#125;$$ step the length of the <code>result</code> list is $$2 ^ &#123;i - 1&#125;$$. So the number of iterations at $$n = 1$$ is $$1$$, at $$n = 2$$ is $$2$$, $$n = 3$$ is $$4$$ and so on. Similar to Approach 2 the mathematical expression for the above analysis reflects a geometric progression as follows $$1 + 2 + 4 + 8 + … + 2 ^&#123;n - 1&#125;$$. </p>
<p>Thus the time complexity will be $$O(2 ^ n)$$.</p></li>
<li><p>Space complexity: $$O(1)$$</p>
<p>The space occupied by the output <code>result</code> is not considered in the space complexity analysis. So overall no extra space is required in this approach.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach4recursion2">Approach 4: Recursion 2</h4>
<p><strong>Intuition</strong></p>
<p>This is an alternate recursion-based solution. We use a global variable <code>nextNum</code> which we update during specific recursive calls (every terminating condition) to obtain the Gray code sequence. We initialize <code>nextNum</code> as 0. Assuming we start with <code>n</code>, we call the function recursively with <code>n - 1</code> until <code>n = 0</code> (i.e. the $$0^&#123;th&#125;$$ bit). At <code>n = 0</code>, we add the value of <code>nextNum</code> to <code>result</code>. We then flip the bit at the $n - 1^&#123;th&#125;$ position from the right and again call the function until we reach the base condition (<code>n = 0</code>). Thus, the numbers get added to <code>result</code> only at the base condition. To think of this intuitively in a top-down manner, if n is the MSB, then we want n to be 0 first and then 1. First, we set it to 0, then make recursive calls so smaller bits (n - 1 through 0) get resolved, then set this MSB to 1, and repeat the process so lower bits get re-set to their correct values.</p>
<p>The recursion tree depicts a complete binary tree. For <code>n</code> bits, the height of the tree will be <code>n + 1</code> and the total number of nodes in it will be $$2^&#123;n + 1&#125; - 1$$. Each node represents one function call. There will be $$2^&#123;n&#125;$$ leaf nodes and at these leaf nodes, the actual values of the gray code sequence will be added to the <code>result</code>. Traversing the leaf nodes from left to right will give us the Gray code sequence for <code>n</code> bits.</p>
<p>This can be better understood with the below diagram. The black arrow indicates the value of <code>nextNum</code> while making forward recursive calls and the red arrow indicates the value of <code>nextNum</code> while returning to each internal node.</p>
<p><img src="https://leetcode.com/articles/Figures/89/89_Gray_Code_Tree.png" alt="fig" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 2. The recursion tree for n = 3 bits</em>
&#123;:align="center"&#125;</p>
<p>The figure shows the program flow for <code>n = 3</code> bits. Roughly, the steps followed here are as follows:</p>
<ul>
<li>Start with <code>n = 3</code>, <code>nextNum</code> = <code>000</code><ul>
<li>Solve for <code>n = 2</code><ul>
<li>Solve for <code>n = 1</code><ul>
<li>Solve for <code>n = 0</code>. Add <code>000</code> (<code>0</code>).</li></ul></li>
<li>Flip 0th bit. <code>nextNum</code> = <code>001</code>.</li>
<li>Solve again for <code>n = 1</code><ul>
<li>Solve for <code>n = 0</code>. Add <code>001</code> (<code>1</code>).</li></ul></li></ul></li>
<li>Flip 1st bit. <code>nextNum</code> = <code>011</code></li>
<li>Solve again for <code>n = 2</code> <ul>
<li>Solve for <code>n = 1</code><ul>
<li>Solve for <code>n = 0</code>. Add <code>011</code> (<code>3</code>).</li></ul></li>
<li>Flip 0th bit. <code>nextNum</code> = <code>010</code>.</li>
<li>Solve again for <code>n = 1</code><ul>
<li>Solve for <code>n = 0</code>. Add <code>010</code> (<code>2</code>).</li></ul></li></ul></li>
<li>Flip 2nd bit. <code>nextNum</code> = <code>110</code>.</li>
<li>Solve again for <code>n = 3</code></li></ul></li>
</ul>
<p>(Repeat the above steps for <code>n = 3</code>, exactly once more with nextNum set to <code>110</code>. Note that this time, it will go in the reverse order since we're starting with <code>10</code> as opposed to <code>00</code> for the last 2 digits)</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Take a global variable <code>nextNum</code> and initialize it to <code>0</code>.</p></li>
<li><p>Recursively call the <code>grayCodeHelper</code> function till the base condition (<code>n = 0</code>) is reached.</p></li>
<li><p>On reaching the base condition add the current value of <code>nextNum</code> to the <code>result</code>.</p></li>
<li><p>Inside the <code>grayCodeHelper</code> function for <code>n</code>, flip the $$(n - 1)^&#123;th&#125;$$ bit of nextNum. Go to step 2 and continue.</p></li>
<li><p>Return the <code>result</code> from the <code>grayCode</code> function.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/ErZ9cmVG/shared" frameborder="0" width="100%" height="463" name="ErZ9cmVG"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here $$n$$ is the total number of bits in the code.</p>
<ul>
<li><p>Time complexity: $$O(2 ^ n)$$</p>
<p>The above diagram illustrates the recursion tree. If we consider each node as a block of statements executed at each recursive function call, the total time complexity will be in terms of the number of nodes present. For $$n$$ bits the total number of nodes (internal + leaf) is $$2 ^ &#123;n + 1&#125; - 1$$. So the overall time complexity is $$O(2 ^ &#123;n + 1&#125; - 1)$$ = $$O(2 ^ n)$$.</p></li>
<li><p>Space complexity: $$O(n)$$</p>
<p>From the diagram, we can conclude that the maximum depth of the function call stack will be $$n + 1$$. So the space complexity will be $$O(n)$$. The space occupied by the <code>result</code> is not considered in the space complexity analysis.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach5iterationwithasingleloop">Approach 5: Iteration with a single loop</h4>
<p><strong>Intuition</strong></p>
<p>This solution is inspired by a <a href="https://leetcode.com/problems/gray-code/discuss/29881/An-accepted-three-line-solution-in-JAVA">post</a> written by a fellow LeetCode user and <a href="https://en.wikipedia.org/wiki/Gray_code#Converting_to_and_from_Gray_code">Wikipedia</a>. Unlike the previous iterative approach, this approach uses a single loop to calculate all the Gray code sequence numbers.</p>
<p>This solution would be very challenging to come up with during an interview without prior knowledge.  We have included it here for completeness because it is optimal in terms of the overall complexity.</p>
<p>For some problems, by comparing the input values to the expected output values, we can identify a pattern or a relationship between the two that allows us to calculate the output values in a more efficient way.  In this case, we first need to solve the problem using one of the previously discussed, more intuitive, approaches to get the expected Gray code value at each index.  Afterwhich, we can search for a pattern that relates each index to the Gray code value at that index.</p>
<p>Take a minute to look at the table provided in the overview of this article. Can you spot the relationship between index, <code>i</code>, and the Gray code value, <code>G(i)</code>? This approach is outside the expectations of a normal interview because the pattern is very difficult to identify. Let's see what happens if we take the XOR of <code>i</code> and <code>G(i)</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/89/89_Gray_Code_Table2.png" alt="fig" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 3. Table illustrating the XOR of <code>i</code> and <code>G(i)</code></em>
&#123;:align="center"&#125;</p>
<p>Notice that $$i \oplus G(i)$$ always equals $$i / 2$$, where $$\oplus$$ signifies XOR and $$i / 2$$ uses floor division.</p>
<p>Rearranging the equation, we can say that  $$G(i) = i \oplus (i / 2)$$ or equivalently $$G(i) = i \oplus (i >> 1)$$.
If this pattern is always true, then we can calculate the Gray code value for each index in constant time.</p>
<p>How do we know if this pattern will always be true? At first glance, this formula might not seem very convincing. Thus we will test its validity before proceeding to the implementation.</p>
<p>To validate this formula we need to prove two things:</p>
<ol>
<li><p><code>G(i)</code> and <code>G(i + 1)</code> differ by exactly one digit.</p>
<blockquote>
  <p>$$
   \begin&#123;align&#125;
  G(i) \oplus G(i + 1) &= (i \oplus (i >> 1)) \oplus ((i + 1) \oplus ((i + 1) >> 1))\
  &= i \oplus (i >> 1) \oplus (i + 1) \oplus ((i + 1) >> 1) \hspace&#123;3pt&#125; \text&#123;XOR&#125; \hspace&#123;3pt&#125; \text&#123;is&#125; \hspace&#123;3pt&#125; \text&#123;commutative&#125;\
  &= (i \oplus (i + 1)) \oplus ((i \oplus (i + 1)) >> 1) \
  &= X \oplus Y (say) \
  \end&#123;align&#125;\
  \text&#123;where&#125; \hspace&#123;3pt&#125; X = (i \oplus (i + 1)) \hspace&#123;3pt&#125; \text&#123;and&#125; \hspace&#123;3pt&#125; Y = ((i \oplus (i + 1)) >> 1)</p>
</blockquote></li>
</ol>
<p>$$ </p>
<pre><code>Adding 1 to any number is equivalent to toggling every bit from the rightmost zero bit to the end. Let's use $$87 + 1 = 88$$ as an example: $$1010111 + 0000001 = 1011000$$. Notice that the $$0^&#123;th&#125;$$ through $$3^&#123;rd&#125;$$ bits are flipped while all the other bits remain the same. 
Thus in general if $$i = ...#01...1 , i + 1$$ will be $$...#10...0$$. Here $$#$$ represents the first bit to the left of the rightmost zero bit and `...` represents any sequence of binary digits. As we can observe the length of the tailing $$1$$ bits of $$i$$ will be the same as the length of the tailing $$0$$ bits of $$i + 1$$. The bits from the beginning upto # will remain the same in both $$i$$ and $$i + 1$$ and the bits after # will be opposite in $$i$$ and $$i + 1$$. Thus we can show that xor product of $$i$$ and $$i + 1$$ will be of the form $$0000000111111$$ (sequence of zeros followed by a sequence of ones):

>$$ 
</code></pre>
<p>\begin&#123;align&#125;</p>
<p>X = i \oplus (i + 1) &= 0000000111111\
Y = ((i \oplus (i + 1)) >> 1) &= 0000000011111 \</p>
<pre><code>    X \oplus Y  &= 0000000100000\\
</code></pre>
<p>\end&#123;align&#125;
$$</p>
<p>From the above observation we can say that $$G(i) \oplus G(i + 1) = X \oplus Y$$ differs in only one bit.</p>
<ol start="2">
<li><p>No number is repeated in the sequence i.e, <code>G(i)</code> is bijective, <code>G(i) = G(j)</code> if and only if <code>i = j</code>.</p>
<blockquote>
  <p>$$
  \begin&#123;align&#125;</p>
</blockquote></li>
</ol>
<p>\text&#123;Let&#125; \hspace&#123;3pt&#125;G(i) = i \oplus (i >> 1) \hspace&#123;3pt&#125; \text&#123;and&#125; \hspace&#123;3pt&#125; G(j) = j \oplus (j >> 1) \
\end&#123;align&#125;\
 \text&#123;If&#125; \hspace&#123;3pt&#125; G(i) = G(j) \hspace&#123;3pt&#125; \text&#123;then&#125;\
$$
$$
\begin&#123;align&#125;
&=>G(i) \oplus G(j) &= 0 \
                    &= (i \oplus (i >> 1)) \oplus (j \oplus (j >> 1)) &= 0 \
                    &= (i \oplus j) \oplus ((i \oplus j) >> 1) &= 0\
\end&#123;align&#125;\ 
\text&#123;Let&#125; \hspace&#123;3pt&#125; X = i \oplus j = b^&#123;n - 1&#125; b^&#123;n - 2&#125; … b ^&#123;0&#125;</p>
<p>$$
$$\text&#123;(binary &#125;\hspace&#123;3pt&#125;\text&#123;representation&#125; \hspace&#123;3pt&#125;\text&#123;of&#125; \hspace&#123;3pt&#125;\text&#123;the&#125; \hspace&#123;3pt&#125;\text&#123;XOR&#125; \hspace&#123;3pt&#125;\text&#123;product)&#125; \hspace&#123;3pt&#125;\
X >> 1 = 0 b^&#123;n - 1&#125; b^&#123;n - 2&#125; … b ^&#123;1&#125;\
     \text&#123;If&#125; \hspace&#123;3pt&#125; X \oplus (X >> 1) = 0 \
    => (b^&#123;n - 1&#125; b^&#123;n - 2&#125; … b ^&#123;0&#125;) \oplus (0 b^&#123;n - 1&#125; b^&#123;n - 2&#125; … b ^&#123;1&#125;) = 0\
\text&#123;On&#125; \hspace&#123;3pt&#125;\text&#123;doing&#125; \hspace&#123;3pt&#125;\text&#123;bitwise&#125; \hspace&#123;3pt&#125;\text&#123;comparison&#125; ,\</p>
<pre><code>b^&#123;n - 1&#125; \oplus 0 = 0 => b^&#123;n - 1&#125; = 0\\
b^&#123;n - 2&#125; \oplus b^&#123;n - 2&#125; = 0 => b^&#123;n - 2&#125; = 0\\
b^&#123;n - 3&#125; \oplus b^&#123;n - 4&#125; = 0 => b^&#123;n - 3&#125; = 0\\
.\\
</code></pre>
<p>.\
    . \
    b ^&#123;0&#125; \oplus b^&#123;1&#125; = 0 => b^&#123;0&#125; = 0\
   \text&#123;Thus&#125; \hspace&#123;3pt&#125;  X = i \oplus j = b^&#123;n - 1&#125; b^&#123;n - 2&#125; … b ^&#123;0&#125;  = 0   \
    \text&#123;We&#125; \hspace&#123;3pt&#125; \text&#123;can&#125; \hspace&#123;3pt&#125; \text&#123;conclude&#125; \hspace&#123;3pt&#125; \text&#123;that&#125; \hspace&#123;3pt&#125; i \oplus j = 0 => i = j\
$$</p>
<p>Thus the sequence generated by $$G(i)$$ consists of unique numbers.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize <code>sequenceLength</code> variable to $$2^n$$. <code>sequenceLength</code> denotes the total number of elements present in the Gray code sequence.</p></li>
<li><p>Run a for loop for $$i = 0 \hspace&#123;3pt&#125; \text&#123;to&#125; \hspace&#123;3pt&#125; 2^n$$.</p>
<ul>
<li><p>At each iteration calculate the next number to be added in the sequence using the formula $$G(i) = i \oplus (i >> 1)$$ and assign it to <code>num</code>.</p></li>
<li><p>Add <code>num</code> to the <code>result</code>.</p></li></ul></li>
<li><p>Return <code>result</code> list.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/HeYuaQac/shared" frameborder="0" width="100%" height="276" name="HeYuaQac"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here $$n$$ is the total number of bits in the Gray code.</p>
<ul>
<li><p>Time complexity: $$O(2 ^ n)$$</p>
<p>We use a single for loop to add all the $$2^n$$ numbers of the Gray code sequence to the <code>result</code>. Thus the time complexity will be $$O(2 ^ n)$$.</p></li>
<li><p>Space complexity: $$O(1)$$</p>
<p>The space occupied by the output <code>result</code> is not considered in the space complexity analysis. So overall no extra space is used in this approach.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            