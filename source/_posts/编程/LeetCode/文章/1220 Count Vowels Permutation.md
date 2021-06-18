
---
title: '1220. Count Vowels Permutation'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/1220/1220-Page-1.png'
author: LeetCode
comments: false
date: Tue, 01 Jun 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/1220/1220-Page-1.png'
---

<div>   
<p>Given an integer <code>n</code>, your task is to count how many strings of length <code>n</code> can be formed under the following rules:</p>

<ul>
<li>Each character is a lower case vowel (<code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, <code>'u'</code>)</li>
<li>Each vowel <code>'a'</code> may only be followed by an <code>'e'</code>.</li>
<li>Each vowel <code>'e'</code> may only be followed by an <code>'a'</code> or an <code>'i'</code>.</li>
<li>Each vowel <code>'i'</code> <strong>may not</strong> be followed by another <code>'i'</code>.</li>
<li>Each vowel <code>'o'</code> may only be followed by an <code>'i'</code> or a <code>'u'</code>.</li>
<li>Each vowel <code>'u'</code> may only be followed by an <code>'a'.</code></li>
</ul>

<p>Since the answer may be too large, return it modulo <code>10^9 + 7.</code></p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> All possible strings are: "a", "e", "i" , "o" and "u".
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 10
<strong>Explanation:</strong> All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
</pre>

<p><strong>Example 3: </strong></p>

<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> 68</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= n <= 2 * 10^4</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>Don't be scared by the <em>complex</em> rules! To solve this problem, we just need to tweak the rules a little bit.</p>
<p>There are five rules in the description (excluding the first bullet point) and each rule says <strong>given a vowel, what vowels can be appended to it</strong>. If we treat each vowel as a node, we can visualize the rules as shown in Figure 1. As you can see, Figure 1 illustrates all of the given rules.</p>
<p><img src="https://leetcode.com/articles/Figures/1220/1220-Page-1.png" alt="Visualize the rules." referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1. Visualization of the rules.</em>
&#123;:align="center"&#125;</p>
<p>We must follow all of the rules while looking for permutations, so let's put all of the rules together. As shown in Figure 2, there are two ways to visualize the rules: (a) demonstrates the relationship between each pair of letters - the current letter and the following letter while (b) presents the rules as a directed cycle.</p>
<p><img src="https://leetcode.com/articles/Figures/1220/1220-Page-2.png" alt="Putting the rules together." referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 2. Putting the rules together.</em>
&#123;:align="center"&#125;</p>
<blockquote>
  <p>We can also model this problem using the <a href="https://en.wikipedia.org/wiki/Finite-state_machine">state machine</a>. State machines are a mathematical model of computation and they have powerful applications in advanced dynamic programming problems such as the <em>Best Time to Buy and Sell Stock</em> problems. As shown in (b), if we picture strings that end with different vowels as different states, what we have acquired is actually a map of all possible state transitions.</p>
</blockquote>
<p>That said, if we are given the number of strings of length <code>i</code> that end in each vowel, like <code>aCount</code>, <code>eCount</code>, <code>iCount</code>, <code>oCount</code>, and <code>uCount</code>, we can compute the number of strings of length <code>i + 1</code> that end in each vowel by simple addition:</p>
<pre><code>aCountNew = eCount + iCount + uCount
eCountNew = aCount + iCount
iCountNew = eCount + oCount
oCountNew = iCount
uCountNew = iCount + oCount
</code></pre>
<p>Starting from here, we have two approaches:</p>
<ul>
<li>Bottom-up: We will initialize the number of strings of size <code>1</code> to be <code>1</code> for each vowel. As the size grows from <code>1</code> to <code>n</code>, we will iteratively increase the count of strings that end in each vowel according to the rules above.</li>
<li>Top-down: We can also perform the above idea recursively.</li>
</ul>
<blockquote>
  <p>In fact, we have more than two options.  There exist solutions that take $$O(logN)$$ time, however, they are more advanced and likely fall outside the scope of what you will be expected to know in an interview.  As such, they will not be discussed in this article.  All the same, we encourage you to learn about them in the <a href="https://leetcode.com/problems/count-vowels-permutation/discuss/?currentPage=1&orderBy=most_votes&query=log">discussion section</a>.
  <br></p>
</blockquote>
<hr>
<h4 id="approach1dynamicprogrammingbottomup">Approach 1: Dynamic Programming (Bottom-up)</h4>
<p><strong>Algorithm</strong></p>
<ul>
<li><p>Initialize five 1D arrays of size <code>n</code>, where <code>aVowelPermutationCount[i]</code>, <code>eVowelPermutationCount[i]</code>, <code>iVowelPermutationCount[i]</code>, <code>oVowelPermutationCount[i]</code>, and <code>uVowelPermutationCount[i]</code> will store the number of strings of length <code>i</code> that end in each vowel accordingly.</p></li>
<li><p>Initialize the first element in each of the five arrays to <code>1</code>. This is because for each starting vowel there is only one permutation when the length of the string is <code>1</code>.</p></li>
<li><p>Iterate the string length, <code>i</code>, from <code>1</code> to <code>n</code>:</p></li>
<li><p>Follow the rules to count the number of strings that end in each vowel. Take the sum of the last element from each of the five arrays and that will be the answer.</p></li>
</ul>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/ZTztc5Tf/shared" frameborder="0" width="100%" height="500" name="ZTztc5Tf"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(N)$$ ($$N$$ equals the input length <code>n</code>). This is because iterating from <code>1</code> to <code>n</code> will take $$O(N)$$ time. The initializations take constant time. Putting them together gives us $$O(N)$$ time.</p></li>
<li><p>Space complexity: $$O(N)$$. This is because we initialized and used five 1D arrays to store the intermediate results.</p></li>
</ul>
<h4 id="approach2dynamicprogrammingbottomupwithoptimizedspace">Approach 2: Dynamic Programming (Bottom-up) with Optimized Space</h4>
<p>It is worth noting that, in Approach 1, the <code>i</code>th element in each array only depends on the <code>i - 1</code>th element in some of the arrays. Therefore, the space complexity can be optimized by using five long variables (instead of 5 arrays of length <code>n</code>) to store the counts.</p>
<iframe src="https://leetcode.com/playground/FNwZjGW4/shared" frameborder="0" width="100%" height="412" name="FNwZjGW4"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(N)$$ ($$N$$ equals the input length <code>n</code>). This is because iterating from <code>1</code> to <code>n</code> will take $$O(N)$$ time. The initializations take constant time. Putting them together gives us $$O(N)$$ time.</p></li>
<li><p>Space complexity: $$O(1)$$. This is because we don't use any additional data structures to store data.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3dynamicprogrammingtopdownrecursion">Approach 3: Dynamic Programming (Top-down, Recursion)</h4>
<h4 id="overview-1">Overview</h4>
<p>In <strong>approach 1</strong>, we filled the table <code>vowelPermutationCount</code> for each length and each vowel, by iterating length, <code>i</code>, from <code>1</code> to <code>n</code>.  However, in this approach, we will fill it from <code>n</code> to <code>1</code> using recursive calls.</p>
<p>Let's create a function <code>vowelPermutationCount(i, vowel)</code> that returns the number of strings of length <code>i</code> that end with <code>vowel</code>.  When <code>i</code> is <code>0</code>, the string is already of length <code>n</code>, so we return <code>1</code> signifying that <code>1</code> string has been formed.  Otherwise, in accordance with the given rules, the recursive solution will work as follows:</p>
<pre><code>vowelPermutationCount(i, 'a') = vowelPermutationCount(i - 1, 'e') + vowelPermutationCount(i - 1, 'i') + vowelPermutationCount(i - 1, 'u')
vowelPermutationCount(i, 'e') = vowelPermutationCount(i - 1, 'a') + vowelPermutationCount(i - 1, 'i')
vowelPermutationCount(i, 'i') = vowelPermutationCount(i - 1, 'e') + vowelPermutationCount(i - 1, 'o')
vowelPermutationCount(i, 'o') = vowelPermutationCount(i - 1, 'i')
vowelPermutationCount(i, 'u') = vowelPermutationCount(i - 1, 'i') + vowelPermutationCount(i - 1, 'o')
</code></pre>
<p>We will also add memoization to the solution by using a 2D array <code>memo</code> of size <code>n x 5</code>, so that <code>memo[i][j]</code> stores <code>vowelPermutationCount[i][j]</code> to avoid repeated computations.</p>
<blockquote>
  <p>If you are not familiar with memoization, it is an optimization technique that we use to reduce the time complexity of solutions by avoiding repeated computations. Feel free to check out our <a href="https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/">Explore Card</a>!</p>
</blockquote>
<h4 id="algorithm">Algorithm</h4>
<p>We use the indices from <code>0</code> to <code>4</code> (inclusive) to represent the five vowels <code>a</code>, <code>e</code>, <code>i</code>, <code>o</code>, and <code>u</code>.</p>
<ul>
<li>Initialize a 2D array <code>memo</code> of size <code>n x 5</code> for memoization.
Return the sum of <code>vowelPermutationCount(n - 1, vowel)</code> for each vowel as the answer.</li>
<li>Function <code>vowelPermutationCount(i, vowel)</code>:</li>
<li>It returns a number of strings of length <code>i</code> that ends with <code>vowel</code>.</li>
<li>If this has been computed and saved to <code>memo</code>, return it directly.</li>
<li>According to each vowel, apply the appropriate rule, as stated above, to count.</li>
<li>Store the value in <code>memo</code> and return it.</li>
</ul>
<p>Note that in Python, we use a hashmap for memoization, therefore we are able to use characters (<code>a</code>, <code>e</code>, <code>i</code>, <code>o</code>, and <code>u</code>) as the second parameter for the function <code>vowelPermutationCount</code>. The benefit of doing so is to enhance readability.</p>
<iframe src="https://leetcode.com/playground/o9SgnpKx/shared" frameborder="0" width="100%" height="500" name="o9SgnpKx"></iframe>
<ul>
<li>Time complexity: $$O(N)$$. This is because there are $$N$$ recursive calls to each vowel. Therefore, the total number of function calls to <code>vowelPermutationCount</code> is $$5 \cdot N$$, which leads to time complexity of $$O(N)$$. Initializations will take $$O(1)$$ time. Putting them together, this solution takes $$O(N)$$ time.</li>
</ul>
<h2 id="spacecomplexityddonddthisisbecauseddo5cdotnddspaceisrequiredformemoizationfurthermorethesizeofthesystemstackusedbyrecursioncallswillbeddonddputtingthemtogetherthissolutionusesddonddspace">* Space complexity: $$O(N)$$. This is because $$O(5 \cdot N)$$ space is required for memoization.  Furthermore, the size of the system stack used by recursion calls will be $$O(N)$$. Putting them together, this solution uses $$O(N)$$ space.</h2>
<p><br></p>  
</div>
            