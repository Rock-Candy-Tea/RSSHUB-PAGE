
---
title: '953. Verifying an Alien Dictionary'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/953/953.png'
author: LeetCode
comments: false
date: Sat, 27 Mar 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/953/953.png'
---

<div>   
<p>In an alien language, surprisingly they also use english lowercase letters, but possibly in a different <code>order</code>. The <code>order</code> of the alphabet is some permutation of lowercase letters.</p>

<p>Given a sequence of <code>words</code> written in the alien language, and the <code>order</code> of the alphabet, return <code>true</code> if and only if the given <code>words</code> are sorted lexicographicaly in this alien language.</p>
<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
<strong>Output:</strong> true
<strong>Explanation: </strong>As 'h' comes before 'l' in this language, then the sequence is sorted.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
<strong>Output:</strong> false
<strong>Explanation: </strong>As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
<strong>Output:</strong> false
<strong>Explanation: </strong>The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (<a href="https://en.wikipedia.org/wiki/Lexicographical_order" target="_blank">More info</a>).
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= words.length <= 100</code></li>
<li><code>1 <= words[i].length <= 20</code></li>
<li><code>order.length == 26</code></li>
<li>All characters in <code>words[i]</code> and <code>order</code> are English lowercase letters.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>To check if the given <code>words</code> are sorted, for each word we need to check if every word on its right is lexicographically larger.  Likewise, for each word we could check if every word on its left is lexicographically smaller. That said, we don't need to compare every word to all of the words to its right. Instead, we can just compare each pair of adjacent words. If all pairs of adjacent words are sorted, then we can safely conclude that <code>words</code> is sorted.  Furthermore, if any pair of adjacent words is not sorted, then we know that <code>words</code> is not sorted.</p>
<p><img src="https://leetcode.com/articles/Figures/953/953.png" alt="Compare adjacent words." referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1. Compare adjacent words.</em>
&#123;:align="center"&#125;</p>
<p><br></p>
<hr>
<h4 id="approach1compareadjacentwords">Approach 1: Compare adjacent words</h4>
<p><strong>Intuition</strong></p>
<p>Following the above overview, we want to compare each pair of adjacent words to see if they are sorted lexicographically. This can be achieved by a naive for-loop iterating over the input array. We can store the <code>letter-order</code> relation of each letter with its ranking in <code>order</code>, so that we can easily access the order of letters when we compare them.</p>
<p>The remaining piece of the puzzle is how to compare two words lexicographically. This is not difficult, but there are a few edge cases that we must consider. To compare two adjacent words <code>words[i]</code> and <code>words[i+1]</code>, we want to find the first letter that is different: if <code>words[i]</code> has the lexicographically smaller letter, then we can exit from the iteration because we know <code>words[i]</code> and <code>words[i+1]</code> are in the right order; however, if <code>words[i]</code> has the lexicographically larger letter, then we immediately return <code>false</code>, because we found one pair of words that are in the wrong order.</p>
<p>We also need to consider the boundaries. While we loop from the beginning to the end of one word, we need to check if the other word has ended. Take the words <code>apple</code> and <code>app</code> as an example, we cannot iterate over all of the letters in <code>apple</code> because the word <code>app</code> is shorter. In this case, we reach the end of one word before finding the first different letter.  When this happens, we must examine the length of each word: if the words are the same length or the former word is shorter, then <code>words</code> is sorted.  However, if the latter word is shorter, then <code>words</code> is not sorted.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Initialize a hashmap/array to record the relations between each letter and its ranking in <code>order</code>.</li>
<li>Iterate over <code>words</code> and compare each pair of adjacent words.</li>
<li>Iterate over each letter to find the first different letter between <code>words[i]</code> and <code>words[i + 1]</code>.<ul>
<li>If <code>words[i + 1]</code> ends before <code>words[i]</code> and no different letters are found, then we need to return false because <code>words[i + 1]</code> should come before <code>words[i]</code> (for example, <code>apple</code> and <code>app</code>).</li>
<li>If we find the first different letter and the two words are in the correct order, then we can exit from the current iteration and proceed to the next pair of words.</li>
<li>If we find the first different letter and the two words are in the wrong order, then we can safely return false.</li></ul></li>
<li>If we reach this point, it means that we have examined all pairs of adjacent words and that they are all sorted. Therefore we can return true.</li>
</ul>
<iframe src="https://leetcode.com/playground/JxNcaknG/shared" frameborder="0" width="100%" height="500" name="JxNcaknG"></iframe>
<p><strong>Complexity analysis</strong></p>
<p>Let $$N$$ be the length of <code>order</code>, and $$M$$ be the total number of characters in <code>words</code>.</p>
<ul>
<li><p>Time complexity : $$O(M)$$.</p>
<p>Storing the <code>letter-order</code> relation of each letter takes $$O(N)$$ time. For the nested for-loops, we examine each pair of words in the outer-loop and for the inner loop, we check each letter in the current word. Therefore, we will iterate over all of letters in <code>words</code>.</p>
<p>Taking both into consideration, the time complexity is $$O(M + N)$$. However, we know that $$N$$ is fixed as $$26$$. Therefore, the time complexity is $$O(M)$$.</p></li>
<li><p>Space complexity : $$O(1)$$.
The only extra data structure we use is the hashmap/array that serves to store the <code>letter-order</code> relations for each word in <code>order</code>. Because the length of <code>order</code> is fixed as $$26$$, this approach achieves constant space complexity.</p></li>
</ul>
<hr>  
</div>
            