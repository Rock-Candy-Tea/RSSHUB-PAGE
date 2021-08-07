
---
title: '1189. Maximum Number of Balloons'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG'
author: LeetCode
comments: false
date: Sat, 07 Aug 2021 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG'
---

<div>   
<p>Given a string <code>text</code>, you want to use the characters of <code>text</code> to form as many instances of the word <strong>"balloon"</strong> as possible.</p>

<p>You can use each character in <code>text</code> <strong>at most once</strong>. Return the maximum number of instances that can be formed.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<p><strong><img alt src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG" style="width: 132px; height: 35px;" referrerpolicy="no-referrer"></strong></p>

<pre><strong>Input:</strong> text = "nlaebolko"
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>

<p><strong><img alt src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG" style="width: 267px; height: 35px;" referrerpolicy="no-referrer"></strong></p>

<pre><strong>Input:</strong> text = "loonbalxballpoon"
<strong>Output:</strong> 2
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> text = "leetcode"
<strong>Output:</strong> 0
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= text.length <= 10<sup>4</sup></code></li>
<li><code>text</code> consists of lower case English letters only.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>This problem can be interestingly related to production management. Assume there is an industry that produces a product <code>X</code>. The product <code>X</code> can be produced by assembling one instance of each of five different parts. We have some fixed quantity of each of these parts, then the maximum number of product <code>X</code> that can be produced will be equal to the quantity of that part which is available in the least quantity. This least available part is known as the bottleneck resource.</p>
<p>In this problem, the product <code>X</code> is the string $balloon$ and the five parts are the characters $b$, $a$, $l$, $o$, and $n$.
<br></p>
<hr>
<h4 id="approach1countingcharacters">Approach 1: Counting Characters</h4>
<p><strong>Intuition</strong></p>
<p>The word $balloon$ consists of five different characters with counts of <code>&#123;'b':1, 'a':1, 'l':2, 'o':2, 'n':1&#125;</code>. The first thing to note is that in order to find the number of instances of $balloon$ that can be produced by any given string <code>text</code> we only need to count the above five characters and the remaining twenty-one lowercase English letters can be ignored.</p>
<p>Now we will observe each of these five characters in isolation. We define the <code>potential</code> of a character as the number of times that $balloon$ can be produced, assuming there is an infinite supply of other characters. </p>
<p>For instance, to find the <code>potential</code> of character $b$, which has a limited quantity equal to $x$, then the answer is $x$. We cannot form more than $x$ instances as we need one $b$ to produce each instance of $balloon$. Similarly, for character $l$, with a limited quantity of $x$ the <code>potential</code> will be $x/2$ as we need two instances of $l$ to produce each instance of $balloon$.</p>
<p>After we find the <code>potential</code> of all five characters, we can make use of each character's <code>potential</code> to find the maximum number of $balloon$ strings that we can produce. The point to note here is that the production of the word $balloon$ depends on the bottleneck character. As in the above case, despite having an infinite capacity of other characters, we can only form $x$ instances of $balloon$ because character $b$ is the bottleneck.</p>
<p><strong>Algorithm</strong></p>
<p>Per the discussion above, the algorithm is: Find the <code>potential</code> of each of the five characters in isolation and then find the bottleneck character among them. The table below shows the <code>potential</code> for each character given $x$ instances of the character and an infinite supply of other characters.</p>
<p><img src="https://leetcode.com/articles/Figures/1189/1189A.png" alt="fig" referrerpolicy="no-referrer"></p>
<p>Now that we have the <code>potential</code> of each character, we can find the bottleneck character (the one with the lowest <code>potential</code>).</p>
<p><strong>Implementation</strong></p>
<ol>
<li>Store the frequency of all the five characters in the given string <code>text</code>.</li>
<li>Find the <code>potential</code> of each of the five characters.</li>
<li>Return the minimum <code>potential</code> of the five characters.</li>
</ol>
<p>The code below prioritizes readability; it could be written more succinctly by using an array (which is discussed in the next approach).</p>
<iframe src="https://leetcode.com/playground/7qLjng53/shared" frameborder="0" width="100%" height="500" name="7qLjng53"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here $$N$$ is equal to the length of <code>text</code>.</p>
<ul>
<li><p>Time complexity: $$O(N)$$</p>
<p>We iterate over all the characters of string <code>text</code> which requires $$N$$ operations.</p></li>
<li><p>Space complexity: $$O(1)$$</p>
<p>All we need is the $$5$$ variables to store the frequency of characters. Hence the space complexity is constant.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2generalizedsolutionusinganarray">Approach 2: Generalized Solution using an Array</h4>
<p><strong>Intuition</strong></p>
<p>As a follow-up exercise, let's consider how we can approach this problem if the word is not guaranteed to be $$balloon$$. Suppose we are given an arbitrary string <code>pattern</code> instead of $balloon$ then we can use the same counting characters approach, except we must do so in a more generalized way. Close observation of the previous approach reveals that the <code>potential</code> of each character is equal to the number of instances in <code>text</code> divided by the number of instances in <code>pattern</code> ($balloon$ in the previous approach). So we just need to find the frequency of all the letters in the strings <code>text</code> and <code>pattern</code>. Then the minimum <code>potential</code> of a character will be the answer.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Store the frequency of all the characters in <code>text</code> in <code>freqInText</code> and the frequency of all the characters in <code>pattern</code> in <code>freqInPattern</code>.</li>
<li>Find the potential of all the lowercase English letters. The potential will be equal to its frequency in <code>text</code> divided by its frequency in <code>pattern</code>.</li>
<li>Return the minimum potential of a character.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/HxXvvMMc/shared" frameborder="0" width="100%" height="500" name="HxXvvMMc"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here $$N$$ equals the length of <code>text</code>, $$M$$ equals the length of <code>pattern</code>, and $$K$$ equals the maximum possible number of distinct letters in <code>pattern</code>.</p>
<ul>
<li><p>Time complexity: $$O(N + M)$$</p>
<p>We traverse over <code>text</code> having length $$N$$ and over the string <code>pattern</code> of length $$M$$ to find the frequency of each character in each string.  Lastly, we traverse over the frequency arrays of length $$K$$ to find the bottleneck character.  Since this problem only uses lowercase English letters, $$K$$ is fixed at $$26$$. Hence, we can consider the space complexity to be $$O(N + M)$$.</p></li>
<li><p>Space complexity: $$O(1)$$</p>
<p>The integer arrays used to store the frequency of characters in <code>text</code> and <code>pattern</code> each require $$O(K)$$ space.  Since this problem only uses lowercase English letters, $$K$$ is fixed at $$26$$. Hence, we can consider the space complexity to be constant.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            