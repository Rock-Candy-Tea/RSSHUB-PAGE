
---
title: '38. Count and Say'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg'
author: LeetCode
comments: false
date: Tue, 30 Aug 2022 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg'
---

<div>   
<p>The <strong>count-and-say</strong> sequence is a sequence of digit strings defined by the recursive formula:</p>

<ul>
<li><code>countAndSay(1) = "1"</code></li>
<li><code>countAndSay(n)</code> is the way you would "say" the digit string from <code>countAndSay(n-1)</code>, which is then converted into a different digit string.</li>
</ul>

<p>To determine how you "say" a digit string, split it into the <strong>minimal</strong> number of substrings such that each substring contains exactly <strong>one</strong> unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.</p>

<p>For example, the saying and conversion for digit string <code>"3322251"</code>:</p>
<img alt src="https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg" style="width: 581px; height: 172px;" referrerpolicy="no-referrer">
<p>Given a positive integer <code>n</code>, return <em>the </em><code>n<sup>th</sup></code><em> term of the <strong>count-and-say</strong> sequence</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> "1"
<strong>Explanation:</strong> This is the base case.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 4
<strong>Output:</strong> "1211"
<strong>Explanation:</strong>
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= n <= 30</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h3 id="overview">Overview</h3>
<p>The main task in this problem is to find the result of "saying" a
digit string.</p>
<hr>
<h3 id="approach1straightforward">Approach 1: Straightforward</h3>
<h4 id="intuition">Intuition</h4>
<p>Start with the initial string $s="1"$. $n-1$ times do $s=f(s)$, where
$f(s)$ denotes the result of saying a digit string $s$. After this
process, $s$ will be the answer to the problem.</p>
<p>To find $f(s)$, one needs to split $s$ into substrings of
equal digits.</p>
<h4 id="algorithm">Algorithm</h4>
<p>The algorithm of "saying" $s$ is the following.</p>
<ol>
<li>Start at position $j=0$ (all indices are 0-based).</li>
<li>Let $k$ be the leftmost position to the right of $j$ that
$s<em>k \ne s</em>j$ if it exists, and $|s|$ otherwise ($|s|$ denotes the length of $s$).</li>
<li>All digits of $s$ between $j$ inclusively and $k$ exclusively are
equal. The number of these digits is $k-j$. Add to the result the
string representation of $k-j$ and the element $s_j$.</li>
<li>Assign $j \leftarrow k$.</li>
<li>If $j < |s|$ go to 2.</li>
<li>Stop.</li>
</ol>
<h4 id="implementation">Implementation</h4>
<iframe src="https://leetcode.com/playground/3iwyo72w/shared" frameborder="0" width="100%" height="310" name="3iwyo72w"></iframe>
<h4 id="complexityanalysis">Complexity Analysis</h4>
<ul>
<li><p>Time Complexity: $O(4^&#123;n/3&#125;)$.</p>
<p>One can notice that the inequality
$|f(s+t)| \le |f(s)+f(t)|$ holds for all strings $s$, $t$.</p>
<p>If the last digit of $s$ differs from the first digit of $t$, then
$f(s+t)=f(s)+f(t)$.
Otherwise, let denote $s=s^&#123;pref&#125;+s^&#123;suf&#125;$, $t=t^&#123;pref&#125;+t^&#123;suf&#125;$,
where $s^&#123;suf&#125;$ is the maximal substring of equal digits at the end of $s$,
$t^&#123;pref&#125;$ is the maximal substring of equal digits at the beginning of $t$.
Then $f(s+t)=f(s^&#123;pref&#125;)+f(s^&#123;suf&#125;+t^&#123;pref&#125;)+f(t^&#123;suf&#125;)$.
Let $s^&#123;suf&#125;$ consist of $x$ digits $d$ and $t^&#123;pref&#125;$ of $y$ digits $d$.
$f(s^&#123;suf&#125;)=str(x)+d$, $f(t^&#123;pref&#125;)=str(y)+d$,
$f(s^&#123;suf&#125;+t^&#123;pref&#125;)=str(x+y)+d$, where $str(x)$ denotes the decimal
representation of an integer $x$. Since $|str(x+y)| \le |str(x)|+|str(y)|$, we have
$|f(s^&#123;suf&#125;+t^&#123;pref&#125;)|=|str(x+y)|+1 \le (|str(x)|+1)+(|str(y)|+1)=|f(s^&#123;suf&#125;)|+|f(t^&#123;pref&#125;)|$.
Finally, $|f(s+t)| \le |f(s^&#123;pref&#125;)|+|f(s^&#123;suf&#125;)|+|f(t^&#123;pref&#125;)|+|f(t^&#123;suf&#125;)|=|f(s)|+|f(t)|$.</p>
<p>Let us see, what happens to a string of one digit after 3 iterations of "saying".
$1 \to 11 \to 21 \to 1211$, $d \to 1d \to 111d \to 311d$, where $d$ is a digit other than $1$.
We see that the length became equal to 4.
Considering the above inequality we obtain that after 3 iterations the length of
an arbitrary string cannot increase more than fourfold.
This leads us to the following bound: $|countAndSay(i)|=O(4^&#123;i/3&#125;)$.</p>
<p>However, this estimate is not tight.
The length of $countAndSay(30)$ is just $4462$ which
is far from $4^&#123;10&#125;$.</p>
<p>The total time complexity is the sum of the lengths of the strings which
is $\sum_&#123;i=1&#125;^n O(4^&#123;i/3&#125;) = O(4^&#123;n/3&#125;)$.</p></li>
<li><p>Space Complexity: $O(4^&#123;n/3&#125;)$.</p>
<p>The sum of the lengths of $countAndSay(i)$ for all $1 \le i \le n$
is $O(4^&#123;n/3&#125;)$. So this is the space complexity.</p></li>
</ul>
<hr>
<h3 id="approach2regularexpression">Approach 2: Regular Expression</h3>
<p>Note. This approach is for those familiar with <a href="https://en.wikipedia.org/wiki/Regular_expression">regular expressions</a>.
If you are not, it might be hard to understand.</p>
<h4 id="intuition-1">Intuition</h4>
<p>This problem could be a good exercise to apply pattern matching,
where we need to find the substrings of equal digits.</p>
<h4 id="algorithm-1">Algorithm</h4>
<p>We want to use a pattern that matches the strings of equal characters
such as <code>"4"</code>, <code>"7777"</code>, <code>"2222222"</code>.</p>
<p>If you have an experience with regular
expressions, you may find that the pattern <code>(.)\\1*</code> works.
We could break down this regex into three parts:</p>
<ul>
<li><p><code>(.)</code>: it defines a group containing a single character that could be of anything.</p></li>
<li><p><code>\\1</code>: it is a backreference to whatever matches in group 1 (the pattern matched in the parenthesis). Group 1 is the only group <code>(.)</code>.</p></li>
<li><p><code>*</code>:  this qualifier, followed by the group reference <code>\\1</code>, indicates that we would like to see the group repeats itself zero or more times.</p></li>
</ul>
<p>So the pattern matches strings which consist of some character
and then zero or more repetitions of this character after its first occurrence. It is what we need.</p>
<p>We find all the matches to the regex and then concatenate the results.</p>
<h4 id="implementation-1">Implementation</h4>
<iframe src="https://leetcode.com/playground/kaoKyjko/shared" frameborder="0" width="100%" height="412" name="kaoKyjko"></iframe>
<h4 id="complexityanalysis-1">Complexity Analysis</h4>
<ul>
<li><p>Time Complexity: $O(4^&#123;n/3&#125;)$.</p>
<p>As we already showed in Approach 1, the total length of the strings is $O(4^&#123;n/3&#125;)$.
The time complexity of regex matching is linear in the input string length.
The total time complexity is $O(4^&#123;n/3&#125;)$.</p></li>
<li><p>Space Complexity: $O(4^&#123;n/3&#125;)$.</p>
<p>The space complexity is the same as in the previous approach.</p></li>
</ul>  
</div>
            