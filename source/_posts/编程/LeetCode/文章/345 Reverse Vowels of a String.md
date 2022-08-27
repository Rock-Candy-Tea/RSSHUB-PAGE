
---
title: '345. Reverse Vowels of a String'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/345/345A.png'
author: LeetCode
comments: false
date: Fri, 26 Aug 2022 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/345/345A.png'
---

<div>   
<p>Given a string <code>s</code>, reverse only all the vowels in the string and return it.</p>

<p>The vowels are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>, and they can appear in both cases.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "hello"
<strong>Output:</strong> "holle"
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> "leotcede"
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= s.length <= 3 * 10<sup>5</sup></code></li>
<li><code>s</code> consist of <strong>printable ASCII</strong> characters.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h3 id="overview">Overview</h3>
<p>This problem is an extension to the problem <a href="https://leetcode.com/problems/reverse-string/">344 Reverse String</a>. In this problem, we have to reverse only the vowels instead of every character as in the original problem.
<br></p>
<hr>
<h3 id="approach1twopointers">Approach 1: Two Pointers</h3>
<h4 id="intuition">Intuition</h4>
<p>we will initialize two pointers, one pointer (referred as <code>left</code>) pointing to the left end of the input string and the other pointer (named as <code>right</code>) pointing to the right end of the string.</p>
<p>The only difference compared to the problem <a href="https://leetcode.com/problems/reverse-string/">344 Reverse String</a> is that we don't want to swap all characters instead we want to swap just the vowels. So the <code>left</code> and <code>right</code> pointers as we discussed should be pointing to the vowels only.</p>
<p>To achieve this, we would initialize a <code>left</code> pointer to <code>0</code> and keep incrementing it until we get a vowel. Similarly, we initialize the <code>right</code> pointer to the last index and keep decrementing it until it points to a vowel. At each such iteration where both the pointers are pointing to the vowel, we would swap the characters at these pointers.</p>
<p><img src="https://leetcode.com/articles/Figures/345/345A.png" alt="fig" referrerpolicy="no-referrer"></p>
<h4 id="algorithm">Algorithm</h4>
<ol>
<li>Initialize the left pointer <code>start</code> to <code>0</code>, and the right pointer <code>end</code> to <code>s.size() - 1</code>.</li>
<li>Keep iterating until the left pointer catches up with the right pointer:</li>
<li>Keep incrementing the left pointer <code>start</code> until it's pointing to a non-vowel character.</li>
<li>Keep decrementing the right pointer <code>end</code> until it's pointing to a non-vowel character.</li>
<li>Swap the characters at the <code>start</code> and <code>end</code>.</li>
<li>Increment the <code>start</code> pointer and decrement the <code>end</code> pointer.</li>
<li>Return the string <code>s</code>.</li>
</ol>
<h4 id="implementation">Implementation</h4>
<iframe src="https://leetcode.com/playground/ZMivGaEy/shared" frameborder="0" width="100%" height="500" name="ZMivGaEy"></iframe>
<h4 id="complexityanalysis">Complexity Analysis</h4>
<p>Here, $$N$$ is the length of the string <code>s</code>.</p>
<ul>
<li><p>Time complexity: $$O(N)$$</p>
<p>It might be tempting to say that there are two nested loops and hence the complexity would be $$O(N^2)$$. However, if we observe closely the pointers <code>start</code> and <code>end</code> will only traverse the index once. Each element of the string <code>s</code> will be iterated only once either by the left or right pointer and not both. We swap characters when both pointers point to vowels which are $$O(1)$$ operation. Hence the total time complexity will be $$O(N)$$. </p>
<p>Note that in Java we need to convert the string to a char array as strings are immutable and hence it would take $$O(N)$$ time.</p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>In C++ we only need an extra temporary variable to perform the swap and hence the space complexity is $$O(1)$$. However, in Java, we need to convert the string to a char array that would take $$O(N)$$ space, and therefore the space complexity for Java would be $$O(N)$$.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            