
---
title: '1048. Longest String Chain'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/1048/1048_Overview_Diagram.png'
author: LeetCode
comments: false
date: Sat, 01 May 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/1048/1048_Overview_Diagram.png'
---

<div>   
<p>Given a list of words, each word consists of English lowercase letters.</p>

<p>Let's say <code>word1</code> is a predecessor of <code>word2</code> if and only if we can add exactly one letter anywhere in <code>word1</code> to make it equal to <code>word2</code>. For example, <code>"abc"</code> is a predecessor of <code>"abac"</code>.</p>

<p>A <em>word chain </em>is a sequence of words <code>[word_1, word_2, ..., word_k]</code> with <code>k >= 1</code>, where <code>word_1</code> is a predecessor of <code>word_2</code>, <code>word_2</code> is a predecessor of <code>word_3</code>, and so on.</p>

<p>Return the longest possible length of a word chain with words chosen from the given list of <code>words</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["a","b","ba","bca","bda","bdca"]
<strong>Output:</strong> 4
<strong>Explanation</strong>: One of the longest word chain is "a","ba","bda","bdca".
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
<strong>Output:</strong> 5
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= words.length <= 1000</code></li>
<li><code>1 <= words[i].length <= 16</code></li>
<li><code>words[i]</code> only consists of English lowercase letters.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>A word chain is a sequence of words (word1 -> word2 -> word3 -> word4 -> word5……) such that word1 is a predecessor of word2 and so on. A key point in the problem statement is that word1 can be a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. In other words, word2 should have one letter more than word1 and the position of this new letter can be anywhere. Note that <em>the order of the words in the list does not need to be maintained while creating the word sequence</em>.</p>
<p>Suppose that word1 is <code>ab</code> then word2 can be <code>ab*</code>, <code>a*b</code>, <code>*ab</code> where * is any lowercase English letter.   </p>
<p>Therefore, it is possible for a particular word to have more than one predecessor in the given list, and thus belong to more than one word sequence. Our objective is to determine the length of the longest possible word sequence.</p>
<p>Let us consider the following example : <code>['abcd','abc','bcd','abd','ab','ad','b']</code>
In this list, the immediate predecessors of <code>abcd</code> are <code>['abc','bcd','abd']</code> as all these words are missing exactly one letter from the word <code>abcd</code>.
Similarly, the immediate predecessors of <code>abd</code> are <code>['ab','ad']</code> and the predecessor of <code>ab</code> is <code>['b']</code>.</p>
<p><br></p>
<hr>
<h4 id="approach1topdowndynamicprogrammingrecursionmemoization">Approach 1: Top-Down Dynamic Programming (Recursion + Memoization)</h4>
<p><strong>Intuition</strong></p>
<p>If you're not familiar with DFS (Depth First Search), check out our <a href="https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/">Explore Card</a>.</p>
<p>Here we work backwards to find the longest chain, this means that we will start from a word and delete one character at a time. We continue this chain until we come across a word that is not present in the list or is one letter long. </p>
<p>In the above example some of the possible word sequences are: <code>abcd -> abd -> ab -> b</code> , <code>abcd -> abc -> ab -> b</code> , <code>abcd -> bcd</code> and so on.
The possible word sequences are illustrated in Figure 1.</p>
<p><img src="https://leetcode.com/articles/Figures/1048/1048_Overview_Diagram.png" alt="fig" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1. Figure demonstrating DFS to find the longest word sequence.</em>
&#123;:align="center"&#125;</p>
<p>In this graph, we can observe that the length of the longest possible word sequence is <code>4</code>. There are two word sequences that have the longest length : <code>abcd -> abd -> ab -> b</code>  and <code>abcd -> abc -> ab -> b</code>. (The longest path is shown in the diagram with red arrows).</p>
<p>Notice that a particular sequence can be a part of more than one word sequence. For example the sequence <code>ab -> b</code> is  part of both the following sequences : <code>abcd -> abd -> ab -> b</code> and <code>abcd -> abc -> ab -> b</code>. This leads to repeated calculations because every time we encounter <code>ab</code> we need to explore the subpath <code>ab -> a</code>. For a small list, this is not a problem but as the size of the list increases, the size of the graph grows exponentially.</p>
<p>What we can do is whenever we encounter a new word, we will find all possible sequences with this word as the last word in the sequence. Then, we will store the length of the longest possible sequence that ends with this word. </p>
<p>We will use a map for this where each <code>key</code> will be an ending word and the <code>value</code> will be the length of the longest possible word sequence ending with this word. In the above example when we first encounter the word <code>ab</code> we will store the value 2 (word sequence <code>ab -> b</code>) for <code>key</code> <code>ab</code>. The next time we encounter <code>ab</code>, we will simply return the value stored against it in the map instead of going through the entire subtree again. This process is known as <em>memoization</em> and it prevents recalculation. For every word present in the list, we only need to determine the length of the longest path that ends with this word once.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize a <code>set</code> (<code>wordsPresent</code>) and add all the words in the list to the set. This set will be used to check if a word is present in the list.</p></li>
<li><p>Initialize a map (<code>memo</code>) having <code>key</code> type as <code>String</code> and <code>value</code> type as <code>Integer</code>. This map will store the length of the longest possible word sequence where the <code>key</code> is the last word in the sequence.</p></li>
<li><p>Iterate over the list. For each word in the list perform a depth-first search.</p></li>
<li><p>In the DFS, consider the current word (<code>currentWord</code>) as the last word in the word sequence.</p></li>
<li><p>If <code>currentWord</code> was encountered previously we just return its corresponding value in the map <code>memo</code>.</p></li>
<li><p>Initialize <code>maxLength</code> to 1.</p></li>
<li><p>Iterate over the entire length of the <code>currentWord</code>. </p>
<ul>
<li>Create all possible words (<code>newWord</code>) by taking out one character at a time.</li>
<li>If <code>newWord</code> is present in the <code>set</code> perform a DFS with this word and store the intermediate result in a variable <code>currentLength</code>.</li>
<li>Update the <code>maxLength</code> so that it contains the length of the longest sequence possible where the <code>currentWord</code> is the end word.</li></ul></li>
<li><p>Set the <code>maxLength</code> as the <code>value</code> for <code>currentWord</code> (<code>key</code>) in the map.</p></li>
<li><p>Return <code>maxLength</code>.        </p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/nvupxDfa/shared" frameborder="0" width="100%" height="500" name="nvupxDfa"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the number of words in the list and $$L$$ be the maximum possible length of a word.</p>
<ul>
<li><p>Time complexity: $$O(L ^ 2 \cdot N)$$.</p>
<p>Initially, we iterate over the list to store all the given words in a <code>set</code> (adds $$N$$ to the complexity).</p>
<p>Next, we perform a DFS for each word ($$O(N)$$). For each word, we iterate over its length($$O(L)$$). At each index (<code>i</code>) we create a new word by deleting the character at position <code>i</code> from the original word ($$O(L)$$). Therefore, the overall time complexity is $$O(N + (L ^ 2 \cdot N))$$ = $$O(L ^ 2 \cdot N))$$, because the $$N$$ term is insignificant relative to the $$L ^ 2 \cdot N$$ term. Note that because of memoization we can be sure that each word in the list is traversed only once.</p></li>
<li><p>Space complexity: $$O(N)$$. </p>
<p>The extra space is used by the recursion call stack. In worst case all the words are a part of the longest word sequence which requires a recursion stack size of $$N$$.</p>
<p>Also, we use a <code>set</code> to store all distinct words (size $$N$$) and a <code>map</code> to store intermediate results (size $$N$$). Since the maximum number of distinct words will be $$N$$ (when there is no repetition) the overall space complexity is $$O(2 \cdot N)$$ which in Big O notation equals $$O(N)$$.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2bottomupdynamicprogramming">Approach 2: Bottom-Up Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>In this solution, we will create the word sequence by adding one letter at a time to the last word in the sequence. Thus the resulting word sequence will be a series of words where each word has one more letter than its predecessor. </p>
<p>If we know the length (<code>previousLength</code>) of the longest word sequence that ends with a word we can use this value to find the length of the longest word sequence for its successor(<code>newLength = previousLength + 1</code>).</p>
<p>Let us again consider the above example <code>['abcd','abc','bcd','abd','ab','ad','b']</code>. 
The longest word sequence with the word <code>b</code> is 1. Thus the length of the longest word sequence with the word <code>ab</code> will be <code>1 + 1 = 2</code> (<code>ab -> b</code>). This result can in turn be used to find the length of the longest word sequence for the word <code>abc</code> (<code>2 + 1 = 3</code> for sequence <code>abc -> ab -> b</code>). </p>
<p>The length of the words in a sequence increases as we move from left to right.  Also, we know that the order of the words in the list doesn't matter. So we can sort the words in ascending order based on their length. Next, we can iterate over the sorted list and calculate the length of the longest sequence possible where the word at index $$i$$ is the end word. We store this result in a map where <code>key</code> is the word and <code>value</code> is the sequence length. By doing this we ensure that, for each word that we encounter, we already know the result of all of its possible predecessors. This process is demonstrated in the following animation.</p>
<p>!?!../Documents/1048<em>Longest</em>String_Chain.json:960,540!?!</p>
<p><br></p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize a map where <code>key</code> is the word and <code>value</code> is the length of the longest word sequence possible with the <code>key</code> as the end word.</p></li>
<li><p>Sort the word list in increasing order of the word length.</p></li>
<li><p>Initialize <code>longestWordSequenceLength</code> to 1. This variable holds the length of the longest word sequence possible.</p></li>
<li><p>Iterate over the sorted list.</p></li>
<li><p>For each word initialize <code>presentLength</code> to 1.</p></li>
<li><p>Iterate over the entire length of each word.</p>
<ul>
<li>Delete the character at $$i^&#123;th&#125;$$ position from the current word and assign the new word to the variable <code>predecessor</code>.</li>
<li>Check if <code>predecessor</code> is present in the list or not.</li>
<li>If the <code>predecessor</code> is present, then assign its mapped value to <code>previousLength</code>. Update the <code>presentLength</code> if <code>previousLength + 1</code> is greater than the <code>presentLength</code>. </li></ul></li>
<li><p>After terminating the inner <code>for</code> loop, assign <code>presentLength</code> to the current word in the map <code>dp</code>.</p></li>
<li><p>Update the <code>longestWordSequenceLength</code> if the longest word sequence formed with the current word as the end word is longer than the previously considered word sequence.</p></li>
<li><p>After terminating the outer <code>for</code> loop, return <code>longestWordSequenceLength</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/HfbnNnwQ/shared" frameborder="0" width="100%" height="500" name="HfbnNnwQ"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the number of words in the list and $$L$$ be the maximum possible length of a word.</p>
<ul>
<li><p>Time complexity: $$O(N \cdot (\log N + L ^ 2))$$.</p>
<p>Sorting a list of size $$N$$ takes $$O(N \log N)$$ time. Next, we use two for loops in which the outer loop runs for $$O(N)$$ iterations and the inner loop runs for $$O(L ^ 2)$$ iterations in the worst case scenario.  The first $$L$$ is for the inner loop and the second $$L$$ is for creating each <code>predecessor</code>. Thus the overall time complexity is $$O(N \log N + (N \cdot L ^ 2))$$ which equals $$O(N \cdot (\log N + L ^ 2))$$.</p></li>
<li><p>Space complexity: $$O(N)$$. </p>
<p>We use a map to store the length of the longest sequence formed with each of the $$N$$ words as the end word.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            