
---
title: '1531. String Compression II'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/1531/1531_1.png'
author: LeetCode
comments: false
date: Wed, 10 Aug 2022 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/1531/1531_1.png'
---

<div>   
<p><a href="http://en.wikipedia.org/wiki/Run-length_encoding">Run-length encoding</a> is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string <code>"aabccc"</code> we replace <font face="monospace"><code>"aa"</code></font> by <font face="monospace"><code>"a2"</code></font> and replace <font face="monospace"><code>"ccc"</code></font> by <font face="monospace"><code>"c3"</code></font>. Thus the compressed string becomes <font face="monospace"><code>"a2bc3"</code>.</font></p>

<p>Notice that in this problem, we are not adding <code>'1'</code> after single characters.</p>

<p>Given a string <code>s</code> and an integer <code>k</code>. You need to delete <strong>at most</strong> <code>k</code> characters from <code>s</code> such that the run-length encoded version of <code>s</code> has minimum length.</p>

<p>Find the <em>minimum length of the run-length encoded version of </em><code>s</code><em> after deleting at most </em><code>k</code><em> characters</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "aaabcccd", k = 2
<strong>Output:</strong> 4
<b>Explanation: </b>Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "aabbaa", k = 2
<strong>Output:</strong> 2
<b>Explanation: </b>If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "aaaaaaaaaaa", k = 0
<strong>Output:</strong> 3
<strong>Explanation: </strong>Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= s.length <= 100</code></li>
<li><code>0 <= k <= s.length</code></li>
<li><code>s</code> contains only lowercase English letters.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>There are a few more characteristics of this problem that hint to us that DP is a viable first approach. If we consider building the string one character at a time, for each character we will have a choice, we can either keep it or delete it, and we need to choose the optimal action. Each of these choices will lead us to another subproblem. Furthermore, whether we are allowed to delete a character depends on if we have already deleted k characters, so our current options are affected by our past decisions. These are both characteristics of problems that can be solved using dynamic programming.</p>
<p>The final clue given to us is that the problem is asking us to "find the minimum length of the run-length encoded version of s after deleting at most k characters," which means that this is an optimization problem. Whenever a problem asks us to minimize or maximize a result based on a given set of rules, we should always include dynamic programming in our list of approaches to consider. Here, we will demonstrate how to solve this problem using dynamic programming.</p>
<p><br></p>
<hr>
<h4 id="approach1dynamicprogramming">Approach 1: dynamic programming</h4>
<p><strong>Intuition</strong></p>
<p>Let us traverse symbols from left to right, adding symbol by symbol. Then we require the following pieces of information to fully describe the current state.</p>
<ul>
<li><code>idx</code>: Index of the current symbol</li>
<li><code>lastChar</code>: The last symbol we have in our compression</li>
<li><code>lastCharCount</code>: The number of <code>lastChar</code> we have considered</li>
<li><code>k</code>: The number of symbols we are still allowed to delete</li>
</ul>
<p>We will discuss about these states in detail later.</p>
<p><strong>Algorithm</strong></p>
<p>Let us consider the example <code>abbbcc</code> and take <code>k = 3</code>. We traverse over the symbols from left to right and for each symbol, we decide whether to take it or not. This leaves us with the state: <code>(string, left to take)</code>. We can represent our possible states as binary trees, where for the left children are where we take symbols and for the right, we do not take them. Notice that we can not have a negative value of <code>k</code>. Also if we look at all levels of this tree, there will be just too many options to deal with: $$2^n$$ (where $$n$$ is the length of the given string). Notice however that there will be a lot of repeating subproblems, which is a good indicator of dynamic programming. For example, <code>(ab, 2)</code> and <code>(b, 1)</code> are both repeated in the image below. If we go even deeper in the tree, we will have even more repetitions.</p>
<p><img src="https://leetcode.com/articles/Figures/1531/1531_1.png" referrerpolicy="no-referrer"></p>
<p>Now we need to understand what parameters to use to define each DP state. We need several of them:</p>
<ol>
<li>First is the number of symbols we have already traversed. We need it to know the next symbol to be processed.</li>
<li>The last letter that was added to the compressed string that we are building. This is so that we can decide how the compression will change if a new symbol is added.</li>
<li>The count of the last letter. Imagine that we have compression <code>a3b5</code>. If we add one more <code>b</code>, our compression will become <code>a3b6</code>. We need to be careful with several cases. When we have, say, <code>a3</code> compression, and we add a <code>b</code>, then we will now have <code>a3b</code>. Also if we have <code>a3b9</code> and we add one more <code>b</code>, then we will have <code>a3b10</code>. Similarly, <code>a3b99</code> will change to <code>a3b100</code> after addition of a <code>b</code>. Notice that when the count of the last letter is 0, 1, 9, or 99, <strong>the length of the compression will change</strong>. However, when the count of the last letter is anything else, <strong>the length of the compression will not change</strong>. </li>
<li>Finally, we need to keep track of how many symbols we are still allowed to delete.</li>
</ol>
<p>The result that we will return for each state will be the minimum length of the compressed string: which is exactly what we were asked to find.</p>
<p>Now, let us discuss how our states will be connected with each other. Let us say that we have already compressed the string <code>abbcaaa</code> so far. The following image discusses the options that we have for the next character.</p>
<p><img src="https://leetcode.com/articles/Figures/1531/1531_2.png" referrerpolicy="no-referrer"></p>
<ol>
<li>We can delete a new symbol, then we increase <code>i</code> by one and decrease <code>k</code> by one.</li>
<li>We decide to take a new symbol, then there are two possibilities:</li>
<li>This symbol is equal to the last symbol in compression, then the total length of compression will not change, except when the frequency of the last symbol is <code>1</code>, <code>9</code> or <code>99</code>.</li>
<li>This symbol is not equal to the last symbol in compression, then the total length will increase by one.</li>
</ol>
<p><strong>Implementation</strong></p>
<ol>
<li><strong>Python implementation details</strong>. In python, we can use the functionality of <code>@cache</code>, which will do all the job of memoization for us.</li>
<li><strong>Java implementation details</strong>. There is no such alternative in Java. So, we can build a DP table, but it will lead to bad complexity and a possibility of TLE. If we use a table with size $n \times n \times k \times 26$, then the time and space complexities will be $O(26n^2k)$, which is worse than the allowed complexity (see complexity analysis for more details). So one of the alternative ways to avoid this is to use a <code>HashMap</code>, where we compress our tuples of <code>4</code> elements to one.</li>
</ol>
<iframe src="https://leetcode.com/playground/BbC9RgCx/shared" frameborder="0" width="100%" height="500" name="BbC9RgCx"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity: $$O(nk^2)$$.</li>
</ul>
<p>Each recursive call will require only constant time, so we can calculate our time complexity as <code>O(1)</code> times the number of recursive calls made. Since we are using memoization, the number of recursive calls will be proportional to the number of DP states.</p>
<p>Each DP state is defined as <code>(idx, last, cnt, k)</code>, so we can calculate the number of DP states as the product of the number of possible values for each parameter. There will be $$n$$ possible values for idx, $$A$$ possible values for last, where $$A = 26$$ is the size of the alphabet, $$n$$ possible values for cnt, and $$k$$ possible values for k. Thus, there are $$O(An^2k)$$ possible DP states. </p>
<p>However we can tighten our upper bound and get rid of $A$ in our complexity. Let us look at pairs <code>(last, cnt)</code> and check how many of them we have. Consider the case <code>aaababbbcc</code>. Then for letter <code>a</code> we can have states <code>(a, 1), (a, 2), (a, 3)</code> and <code>(a, 4)</code>, because we have only <code>4</code> letters <code>a</code> in our string and after deletions we can not have more. We have states <code>(b, 1), (b, 2), (b, 3), (b, 4), (c, 1), (c, 2)</code>. Notice that some of these states can not be reached, because we do not have enough deletions. But what we know for sure is that the total number of pairs <code>(last, cnt)</code> is not more than $$n$$. Now we can adjust our analysis and we have:</p>
<ol>
<li>When we consider our states, we have $n$ options to choose index</li>
<li>We have $n$ options in total to choose a pair <code>(l, lc)</code>, because for each letter the maximum length is the frequency of this letter.</li>
<li>We have $k + 1$ options to choose how many elements we need to delete: it can be <code>(0, ..., k)</code>.</li>
</ol>
<p>Also we have at most <code>2</code> transitions from one state to another and it makes total time complexity $$O(nk^2)$$.</p>
<ul>
<li>Space complexity: $$O(nk^2)$$.
We already found the number of states when we calculated time complexity, here is the same reasoning.</li>
</ul>
<p><br></p>
<hr>  
</div>
            