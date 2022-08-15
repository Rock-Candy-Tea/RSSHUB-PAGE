
---
title: '557. Reverse Words In A String III'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/557/second_observation.png'
author: LeetCode
comments: false
date: Tue, 26 Jul 2022 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/557/second_observation.png'
---

<div>   
<p>Given a string <code>s</code>, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "Let's take LeetCode contest"
<strong>Output:</strong> "s'teL ekat edoCteeL tsetnoc"
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "God Ding"
<strong>Output:</strong> "doG gniD"
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= s.length <= 5 * 10<sup>4</sup></code></li>
<li><code>s</code> contains printable <strong>ASCII</strong> characters.</li>
<li><code>s</code> does not contain any leading or trailing spaces.</li>
<li>There is <strong>at least one</strong> word in <code>s</code>.</li>
<li>All the words in <code>s</code> are separated by a single space.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>The problem is a variation of similar reverse string problems, <a href="https://leetcode.com/problems/reverse-words-in-a-string/">Reverse Words In a String</a> and <a href="https://leetcode.com/problems/reverse-words-in-a-string-ii/">Reverse Words In String II</a>.</p>
<p>In the first one, we had to reverse all characters, and in the second variation, we had to reverse the order of words. In this problem, we have to reverse the characters of each word in the sentences.</p>
<hr>
<h4 id="approach1traverseandreverseeachcharacteronebyone">Approach 1: Traverse and Reverse each character one by one</h4>
<p><strong>Intuition</strong></p>
<p>To solve the problem let's look at the example carefully,</p>
<pre><code>Input: "Let's take LeetCode contest"`

Output: "s'teL ekat edoCteeL tsetnoc"
</code></pre>
<p>There are a few observations here,</p>
<ul>
<li><p>The characters of each word in the string are reversed, but the order of words remains the same.</p>
<p>For example, in the input, the word <code>Let's</code> is the first word in the string. In the output, the characters in the word <code>Let's</code> are reversed to <code>s'teL</code>. But it is still at the first position in the string.
Similarly the second word <code>take</code> is reversed as <code>ekat</code> and placed at the same second position in the output string.</p></li>
<li><p>The words in the string are separated by a space character. So we can say that to build the output string, we must extract and reverse the substring between 2 consecutive space characters.</p>
<p><img src="https://leetcode.com/articles/Figures/557/second_observation.png" alt="Second Observation Illustration" referrerpolicy="no-referrer"></p></li>
</ul>
<p>Using this intuition, let's understand how to implement this problem.</p>
<p><strong>Algorithm</strong></p>
<p>By analyzing the above two key observations, we can derive the following algorithm,</p>
<ul>
<li><p>Find the starting and ending position of each word in the string.</p>
<p>As a space character is a separator for each word, we are finding the substrings having a space character before its first character and after its last character.</p></li>
</ul>
<blockquote>
  <p>Note: Take care of 2 edge cases here, the first word does not have a space before its first character. Similarly, the last word does not have a space after its last character.</p>
</blockquote>
<ul>
<li>For each identified word, reverse the characters of the word one by one.</li>
</ul>
<p><em>Steps</em></p>
<p>Traverse the string from left to right, starting from $$0^&#123;th&#125;$$ to $$n^&#123;th&#125;$$ index. As we traverse, the pointer <code>strIndex</code> tracks each character.
The implementation can be divided into 2 steps,</p>
<ol>
<li><p>Find the start and end index of every word</p>
<ul>
<li><p>Traverse over the string until the current pointer <code>strIndex</code> points to a space character.</p></li>
<li><p>As <code>strIndex</code> points to the space character, the index <code>strIndex - 1</code> points to the last character of the current word.</p>
<p><img src="https://leetcode.com/articles/Figures/557/current_pointer_traversal.png" alt="Current Pointer Traversal" referrerpolicy="no-referrer"></p></li></ul></li>
</ol>
<ul>
<li><p>Let's understand how to find the first character of the word,</p>
<ul>
<li><p>For the first word, its first character is always the first character of the string.</p></li>
<li><p>For the remaining words, the first character would be the character after the last space character.</p>
<p>Thus, to mark the start of the current character, we must keep track of the last found space character. Let's use a variable <code>lastSpaceIndex</code>. The variable will be initialized to <code>-1</code>  and updated every time we find the next space character.</p>
<p><img src="https://leetcode.com/articles/Figures/557/start_and_end_index.png" alt="Mark Start And End Index" referrerpolicy="no-referrer"></p>
<p>The first character of the current word is thus <code>lastSpaceIndex + 1</code>.</p></li></ul></li>
</ul>
<ol>
<li>Reverse the characters within the word</li>
</ol>
<ul>
<li><p>Now that we have the first and last index of the current word, we have to reverse the current word and append it to the result string.</p></li>
<li><p>To reverse the current word, we can traverse it in reverse order i.e start from the end index <code>strIndex - 1</code> to the first index i.e <code>lastSpaceIndex + 1</code>, appending each character one by one to the result string.</p></li>
<li><p>To separate the current word from the next, append a space character (" ") at the end after the reverse operation. However, for the last word, this step is skipped.</p></li>
</ul>
<p>Repeat 1 and 2 for all the words in the string.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/hRe8qeLh/shared" frameborder="0" width="100%" height="412" name="hRe8qeLh"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of input string <code>s</code>.</p>
<p>Time Complexity: $$\mathcal&#123;O&#125;(N)$$ Every character in the string is traversed twice. First, to find the end of the current word, and second to reverse the word and append it to the result. Thus the time complexity is, $$\mathcal&#123;O&#125;(N + N) = \mathcal&#123;O&#125;(N)$$.</p>
<p>Space Complexity: $$\mathcal&#123;O&#125;(1)$$ We use constant extra space to track the last space index.</p>
<hr>
<h4 id="approach2usingtwopointers">Approach 2: Using Two Pointers</h4>
<p><strong>Intuition</strong></p>
<p>In the previous approach, the words were reversed by copying every character into another string one by one in reverse order. This operation takes $$\mathcal&#123;O&#125;(N)$$ time, where <code>N</code> is the length of the word.</p>
<p>However, there is another optimal approach to reverse the string in $$\mathcal&#123;O&#125;(N/2)$$ time in place using two pointer approach.  </p>
<p>In this solution, we will traverse the string and find every word's start and end index. Then, we will reverse each word using the two-pointer approach.</p>
<p><em>Approach to reverse a string using a two-pointer approach</em></p>
<ol>
<li><p>Find the start and end index of every word given by <code>startIndex</code> and <code>endIndex</code>.</p></li>
<li><p>Swap the characters in the word pointed by <code>startIndex</code> and <code>endIndex</code>.</p></li>
<li><p>Increment <code>startIndex</code> by 1 and decrement <code>endIndex</code> by 1.</p></li>
<li><p>Repeat steps 2 and 3 until <code>startIndex < endIndex</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/557/2_pointer_approach.png" alt="Two Pointer Approach To Reverse String" referrerpolicy="no-referrer"></p></li>
</ol>
<p>Here's the code snippet for reversing the string stored in character array <code>chArray</code> using two pointer approach.</p>
<pre><code class="java language-java">while (startIndex < endIndex) &#123;
        char temp = chArray[startIndex];
        chArray[startIndex] = chArray[endIndex];
        chArray[endIndex] = temp;
        startIndex++;
        endIndex--;
&#125;
</code></pre>
<p><strong>Algorithm</strong></p>
<ul>
<li><p>The variable <code>lastSpaceIndex</code> stores the index of space character last found. Initialize its value to <code>-1</code>.</p></li>
<li><p>Traverse over each character of the string from $$0^&#123;th&#125;$$ index to $$n^&#123;th&#125;$$ index using pointer <code>strIndex</code>.</p></li>
<li><p>As <code>strIndex</code> points to a space character, mark the start and end index of the current word in the variables <code>startIndex</code> and <code>endIndex</code> as,</p></li>
<li><p>The <code>startIndex</code> of the current word is the value of <code>lastSpaceIndex + 1</code>.</p></li>
<li><p>The <code>endIndex</code> of the current word is the value of <code>strIndex - 1</code>.</p></li>
<li><p>Reverse the characters in the current word using two pointer approach.</p></li>
<li><p>Update the <code>lastSpaceIndex</code> to the value of <code>strIndex</code> i.e the index of current space character. The next iteration will refer to this variable to identify the start position of the next word.</p></li>
<li><p>Repeat the process for all the words in the string.</p></li>
</ul>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/b5GQpzDy/shared" frameborder="0" width="100%" height="463" name="b5GQpzDy"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of string <code>s</code>.</p>
<ul>
<li><p>Time Complexity: $$\mathcal&#123;O&#125;(N)$$ The outer loop iterates over $$\text&#123;N&#125;$$ characters to find the <code>start</code> and <code>end</code> index of every word. The algorithm to reverse the word also iterates $$\text&#123;N&#125;$$ times to perform $$\text&#123;N/2&#125;$$ swaps. Thus, the time complexity is $$\mathcal&#123;O&#125;(N + N) = &#123;O&#125;(N)$$.</p></li>
<li><p>Space Complexity: $$\mathcal&#123;O&#125;(1)$$ We use constant extra space to track the last space index.</p></li>
</ul>  
</div>
            