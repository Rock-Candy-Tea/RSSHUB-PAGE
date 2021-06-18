
---
title: '205. Isomorphic strings'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/205/img1.png'
author: LeetCode
comments: false
date: Wed, 09 Jun 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/205/img1.png'
---

<div>   
<p>Given two strings <code>s</code> and <code>t</code>, <em>determine if they are isomorphic</em>.</p>

<p>Two strings <code>s</code> and <code>t</code> are isomorphic if the characters in <code>s</code> can be replaced to get <code>t</code>.</p>

<p>All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "egg", t = "add"
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "foo", t = "bar"
<strong>Output:</strong> false
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "paper", t = "title"
<strong>Output:</strong> true
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= s.length <= 5 * 10<sup>4</sup></code></li>
<li><code>t.length == s.length</code></li>
<li><code>s</code> and <code>t</code> consist of any valid ascii character.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>This is one of those problems where we can come up with a whole suite of different solutions, with similar time and space complexities. The discussion section is filled with various tricks to solve this problem, however, we will stick to a couple of approaches that have the optimal time and space complexity and are reasonably easy to come up with during an interview. Regardless of which approach we use, three conditions must be met for the two strings to be isomorphic:</p>
<ol>
<li>We can map a character only to itself or to one other character.</li>
<li>No two character should map to same character.</li>
<li>Replacing each character in string <code>s</code> with the character it is mapped to results in string <code>t</code>.</li>
</ol>
<p>Matching the order will be easy.  Since we will iterate over the two strings and do some sort of comparison from left to right, the task of ensuring that the character order is the same in both strings will take care of itself. Next, we need to somehow maintain a mapping of characters (hint: dictionary) or come up with a way to "convert" both of the strings to a common format (think integer assignment to characters) and then check if the converted strings are the same.</p>
<p>These are the two solutions that we will explore. Again, many other tricks can be used to solve this problem, and thus there are a variety of different solutions.  A compilation of other solutions can be found <a href="https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-(dictionary-etc)">here</a>, however, some of these solutions would be difficult to come up with during an interview.  So, in this article, we will focus on solutions that are both intuitive and have optimal complexity.</p>
<p><br></p>
<hr>
<h4 id="approach1charactermappingwithdictionary">Approach 1: Character Mapping with Dictionary</h4>
<p><strong>Intuition</strong></p>
<p>The first solution is based on the approach indicated in the problem statement itself. We will process both of the strings from left to right. At each step, we take one character at a time from the two strings and compare them. There are three cases we need to handle here:</p>
<ol>
<li><p>If the characters don't have a mapping, we add one in the dictionary and move on.</p>
<p><img src="https://leetcode.com/articles/Figures/205/img1.png" alt="Example for when we don't have a mapping" referrerpolicy="no-referrer"></p>
<p><em>Figure 1. The first encounter for a new character in both strings which are not yet mapped.</em></p></li>
<li><p>The characters already have a mapping in the dictionary. If that is the case, then we're good to go.</p>
<p><img src="https://leetcode.com/articles/Figures/205/img2.png" alt="Example for when we have a mapping" referrerpolicy="no-referrer"></p>
<p><em>Figure 2. Example for when we already had a mapping between the corresponding characters.</em></p></li>
<li><p>The final case is when a mapping already exists for one of the characters but it <em>doesn't map to the other character at hand</em>. In this case, we can safely conclude that the given strings are not isomorphic and we can return.</p></li>
</ol>
<p>If at this point you're ready to move on to the algorithm, take a step back and think about the correctness of this solution. The above three cases only care about <strong>one-way-mapping</strong> i.e. mapping characters from the first string to the second one only. Don't we need the mapping from the other side as well? </p>
<p><img src="https://leetcode.com/articles/Figures/205/img3.png" alt="Breaking example using our existing 3 cases" referrerpolicy="no-referrer"></p>
<p><em>Figure 3. Example for when a single dictionary implementation breaks.</em></p>
<p>We will need two dictionaries instead of one since we need <code>one-to-one</code> mapping from the string <code>s</code> to string <code>t</code> and vice versa. Let's look at the algorithm to see the modified cases.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>We define a dictionary <code>mapping_s_t</code> which will be used to map characters in string <code>s</code> to characters in string <code>t</code> and another dictionary <code>mapping_t_s</code> which will be used to map characters in string <code>t</code> to characters in string <code>s</code>. </li>
<li>Next, we iterate over the two strings one character at a time.</li>
<li>Let's assume the character in the first string is <code>c1</code> and the corresponding character in the second string is <code>c2</code>. </li>
<li>If <code>c1</code> does not have a mapping in <code>mapping_s_t</code> and <code>c2</code> does not have a mapping in <code>mapping_t_s</code>, we add the corresponding mappings in both the dictionaries and move on to the next character.</li>
<li>At this point, we expect both the character mappings to exist in the dictionaries and their values should be <code>mapping_s_t[c1] = c2</code> and <code>mapping_t_s[c2] = c1</code>. If either of these conditions fails (<code>c1</code> is not in the dictionary, <code>c2</code> is not in the dictionary, unexpected mapping), we return <code>false</code>.</li>
<li>Return <code>true</code> once both the strings have been exhausted.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/76kYqrsf/shared" frameborder="0" width="100%" height="500" name="76kYqrsf"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here $$N$$ is the length of each string (if the strings are not the same length, then they cannot be isomorphic).</p>
<ul>
<li>Time Complexity: $$O(N)$$. We process each character in both the strings exactly once to determine if the strings are isomorphic.</li>
<li>Space Complexity: $$O(1)$$ since the size of the ASCII character set is fixed and the keys in our dictionary are all valid ASCII characters according to the problem statement.</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2firstoccurencetransformation">Approach 2: First occurence transformation</h4>
<p><strong>Intuition</strong></p>
<p>This approach is based on the idea that the two given strings, if isomorphic, will in some way be exactly the same. If we have two isomorphic strings, we can replace the characters in the first string with the corresponding mapped characters to get the second string. The idea we explore here is the following:</p>
<blockquote>
  <p>Is there any string transformation we can apply to both the strings such that to check for isomorphism, we simply check if their modified versions are <strong><em>exactly</em></strong> the same?</p>
</blockquote>
<p>One can come up with various such transformations giving us different variations of this solution. We will stick with one such transformations for the official solution. </p>
<blockquote>
  <p>For each character in the given string, we replace it with the index of that character's first occurence in the string. </p>
</blockquote>
<p>For a string like <code>paper</code>, the transformed string will be <code>01034</code>. The character <code>p</code> occurs first at the index <code>0</code>; so we replace future occurrences of <code>p</code> with the index <code>0</code>. Similar modifications are made for the other characters. Now let's look at <code>title</code>. The transformed string would be <code>01034</code> which is the same as that for <code>paper</code>. This confirms the isomorphic nature of both the strings.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Define a function called <code>transform</code> that takes a string as an input and returns a new string with modifications as explained in the intuition section.</li>
<li>We maintain a dictionary to store the character to index mapping for the given string.</li>
<li>For each character, we look up the mapping in the dictionary. If there is a mapping, that means this character already has its first occurrence recorded and we simply use the first occurrence's index in the new string. Otherwise, we use the current index for the first occurrence.</li>
<li>We find the transformed strings for both of our input strings. Let's say the transformed strings are <code>s1</code> and <code>s2</code> respectively.</li>
<li>If <code>s1 == s2</code>, that implies the two input strings are isomorphic. Otherwise, they're not.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/XzcHrqPz/shared" frameborder="0" width="100%" height="412" name="XzcHrqPz"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here $$N$$ is the length of each string (if the strings are not the same length, they cannot be isomorphic).</p>
<ul>
<li>Time Complexity: $$O(N)$$. We process each character in both the strings exactly once to determine if they are isomorphic.</li>
<li>Space Complexity: $$O(N)$$. We form two new strings returned by our transformation function. The size of ASCII character set is fixed and the keys in our dictionary are valid ASCII characters only. So the size of the map in the transform function doesn't contribute to the space complexity.</li>
</ul>  
</div>
            