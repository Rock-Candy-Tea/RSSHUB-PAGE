
---
title: '680. Valid Palindrome II'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=4089'
author: LeetCode
comments: false
date: Fri, 18 Mar 2022 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4089'
---

<div>   
<p>Given a string <code>s</code>, return <code>true</code> <em>if the </em><code>s</code><em> can be palindrome after deleting <strong>at most one</strong> character from it</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "aba"
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "abca"
<strong>Output:</strong> true
<strong>Explanation:</strong> You could delete the character 'c'.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "abc"
<strong>Output:</strong> false
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= s.length <= 10<sup>5</sup></code></li>
<li><code>s</code> consists of lowercase English letters.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approachtwopointers">Approach: Two Pointers</h4>
<p><strong>Intuition</strong></p>
<p>Let's start by thinking about how we can solve this problem without the optional deletion included. How can we check if a given string <code>s</code> is a palindrome?</p>
<blockquote>
  <p>A string is a palindrome if it reads the same forward as backwards.</p>
</blockquote>
<p>For a string to be a palindrome, the first and last character must be the same, the second and the second last character must be the same, and so on. An efficient way to check if a string is a palindrome is to use two pointers.</p>
<ul>
<li>Initialize one pointer at the start of the string and one at the end. </li>
<li>Compare the characters at these pointers - if they're different, the string can't be a palindrome. If they're the same, then move the pointers towards each other. </li>
<li>Continue until there is a mismatch (signifying the string is not a palindrome) or until the pointers meet each other (which would mean the string is a palindrome).</li>
</ul>
<p>!?!../Documents/680<em>Valid</em>Palindrome_II.json:960,540!?!</p>
<p>We can write a handy helper function <code>checkPalindrome(s, i, j)</code> that implements this logic, where <code>s</code> is the string we are checking, and <code>i</code> and <code>j</code> are the left and right bounds we want to consider. For example, to check if the entire string <code>s</code> is a palindrome, <code>i</code> will start at <code>0</code> and <code>j</code> will start at <code>s.length() - 1</code>.</p>
<iframe src="https://leetcode.com/playground/AW5pmPGR/shared" frameborder="0" width="100%" height="242" name="AW5pmPGR"></iframe>
<p>An important thing to notice is that once we verify two characters match at positions <code>i</code> and <code>j</code>, we only care about the indices <strong>between</strong> <code>i</code> and <code>j</code>. For example, with <code>s = 'racecar'</code>, after verifying that <code>s[0]</code> and <code>s[6]</code> are the same character, we only care about indices <code>1</code> through <code>5</code>, which represent the substring <code>'aceca'</code>. If <code>'aceca'</code> is a palindrome, then <code>'racecar'</code> is a palindrome as well. </p>
<blockquote>
  <p>For our purposes, we can basically pretend that matched characters no longer exist. For example, after verifying that the first and last characters of 'racecar' match, we can reframe the problem as checking if 'aceca' can be a palindrome with at most one deletion.</p>
</blockquote>
<p>Let's assume we have some string <code>s = 'abbxa'</code>. On its own, <code>s</code> is not a palindrome. However, if we delete the <code>'x'</code>, then <code>s</code> becomes <code>'abba'</code>, which is a palindrome. If we use the same algorithm in <code>checkPalindrome</code>, we will see that the first and last characters match as <code>'a'</code>. The pointers move inwards, and the "new" string we're focused on is <code>'bbx'</code>.</p>
<p>The next check will be a mismatch - <code>'b' != 'x'</code>. This means that our original string is not a palindrome. However, we can delete one character. If <code>s</code> can be a palindrome after one deletion, the deletion <strong>must</strong> be of one of these mismatched characters. Deleting the character <code>'b'</code> gives us <code>'bx'</code>, and deleting the character <code>'x'</code> gives us <code>'bb'</code>. Because <code>'bb'</code> is a palindrome (which we can verify using <code>checkPalindrome</code>), the original string <code>'abbxa'</code> can become a palindrome with at most one character deletion.</p>
<p>Here's an animation that demonstrates the process using a slightly longer example:</p>
<p>!?!../Documents/680<em>Valid</em>Palindrome<em>II</em>2.json:960,540!?!</p>
<p>This leaves us two scenarios:</p>
<ol>
<li><p><code>s</code> is a palindrome - great, we can just return <code>true</code>.</p></li>
<li><p>Somewhere in <code>s</code>, there will be a pair of mismatched characters. We <strong>must</strong> use our allowed deletion on one of these characters. Try both options - if neither results in a palindrome, then return <code>false</code>. Otherwise, return <code>true</code>. We can "delete" the character at <code>j</code> by moving our bounds to <code>(i, j - 1)</code>. Likewise, we can "delete" the character at <code>i</code> by moving our bounds to <code>(i + 1, j)</code>. </p></li>
</ol>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Create a helper function <code>checkPalindrome</code> that takes a string <code>s</code>, and two pointers <code>i</code> and <code>j</code>. This function returns a boolean indicating if <code>s.substring(i, j)</code> is a palindrome. Implementation details for this function can be found in the first section of this article.</p></li>
<li><p>Initialize two pointers, <code>i = 0</code> and <code>j = s.length() - 1</code>.</p></li>
<li><p>While <code>i < j</code>, check if the characters at indices <code>i</code> and <code>j</code> match. If they don't, that means we must spend our deletion on one of these characters. Try both options using <code>checkPalindrome</code>. In other words, return true if either <code>checkPalindrome(s, i, j -1)</code> or <code>checkPalindrome(s, i + 1, j)</code> is true.</p></li>
<li><p>If we exit the while loop, that means the original string is a palindrome. Since we didn't <strong>need</strong> to use the deletion, we should return <code>true</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/nNKcQPLg/shared" frameborder="0" width="100%" height="500" name="nNKcQPLg"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the length of <code>s</code>,</p>
<ul>
<li><p>Time complexity: $$O(N)$$.</p>
<p>The main while loop we use can iterate up to <code>N / 2</code> times, since each iteration represents a pair of characters. On any given iteration, we may find a mismatch and call <code>checkPalindrome</code> twice. <code>checkPalindrome</code> can also iterate up to <code>N / 2</code> times, in the worst case where the first and last character of <code>s</code> do not match.</p>
<p>Because we are only allowed up to one deletion, the algorithm only considers one mismatch. This means that <code>checkPalindrome</code> will never be called more than twice.</p>
<p>As such, we have a time complexity of $$O(N)$$.</p></li>
<li><p>Space complexity: $$O(1)$$.</p>
<p>The only extra space used is by the two pointers <code>i</code> and <code>j</code>, which can be considered constant relative to the input size.</p></li>
</ul>
<p><br></p>  
</div>
            