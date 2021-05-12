
---
title: '49. Group Anagrams'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/49_groupanagrams1.png'
author: LeetCode
comments: false
date: Tue, 11 May 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/49_groupanagrams1.png'
---

<div>   
<p>Given an array of strings <code>strs</code>, group <strong>the anagrams</strong> together. You can return the answer in <strong>any order</strong>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= strs.length <= 10<sup>4</sup></code></li>
<li><code>0 <= strs[i].length <= 100</code></li>
<li><code>strs[i]</code> consists of lower-case English letters.</li>
</ul><p>[TOC]</p>
<h2 id="videosolution">Video Solution</h2>
<hr>
<div class="video-preview"></div>
<div> 
 </div>
<h2 id="solutionarticle">Solution Article</h2>
<hr>
<h4 id="approach1categorizebysortedstring">Approach 1: Categorize by Sorted String</h4>
<p><strong>Intuition</strong></p>
<p>Two strings are anagrams if and only if their sorted strings are equal.</p>
<p><strong>Algorithm</strong></p>
<p>Maintain a map <code>ans : &#123;String -> List&#125;</code> where each key $$\text&#123;K&#125;$$ is a sorted string, and each value is the list of strings from the initial input that when sorted, are equal to $$\text&#123;K&#125;$$.</p>
<p>In Java, we will store the key as a string, eg. <code>code</code>.  In Python, we will store the key as a hashable tuple, eg. <code>('c', 'o', 'd', 'e')</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/49_groupanagrams1.png" alt="Anagrams" referrerpolicy="no-referrer"></p>
<iframe src="https://leetcode.com/playground/NGc8spVj/shared" frameborder="0" width="100%" height="293" name="NGc8spVj"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity:  $$O(NK \log K)$$, where $$N$$ is the length of <code>strs</code>, and $$K$$ is the maximum length of a string in <code>strs</code>.  The outer loop has complexity $$O(N)$$ as we iterate through each string.  Then, we sort each string in $$O(K \log K)$$ time.</p></li>
<li><p>Space Complexity: $$O(NK)$$, the total information content stored in <code>ans</code>.
<br></p></li>
</ul>
<h2 id="br"><br></h2>
<h4 id="approach2categorizebycount">Approach 2: Categorize by Count</h4>
<p><strong>Intuition</strong></p>
<p>Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.</p>
<p><strong>Algorithm</strong></p>
<p>We can transform each string $$\text&#123;s&#125;$$ into a character count, $$\text&#123;count&#125;$$, consisting of 26 non-negative integers representing the number of $$\text&#123;a&#125;$$'s, $$\text&#123;b&#125;$$'s, $$\text&#123;c&#125;$$'s, etc.  We use these counts as the basis for our hash map.</p>
<p>In Java, the hashable representation of our count will be a string delimited with '<strong>#</strong>' characters.  For example, <code>abbccc</code> will be <code>#1#2#3#0#0#0...#0</code> where there are 26 entries total.  In python, the representation will be a tuple of the counts.  For example, <code>abbccc</code> will be <code>(1, 2, 3, 0, 0, ..., 0)</code>, where again there are 26 entries total.</p>
<p><img src="https://leetcode.com/articles/Figures/49_groupanagrams2.png" alt="Anagrams" referrerpolicy="no-referrer"></p>
<iframe src="https://leetcode.com/playground/o64x8Vq4/shared" frameborder="0" width="100%" height="412" name="o64x8Vq4"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity:  $$O(NK)$$, where $$N$$ is the length of <code>strs</code>, and $$K$$ is the maximum length of a string in <code>strs</code>.  Counting each string is linear in the size of the string, and we count every string.</p></li>
<li><p>Space Complexity: $$O(NK)$$, the total information content stored in <code>ans</code>.</p></li>
</ul>  
</div>
            