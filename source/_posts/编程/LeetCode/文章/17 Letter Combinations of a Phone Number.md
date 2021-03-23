
---
title: '17. Letter Combinations of a Phone Number'
categories: 
    - 编程
    - LeetCode
    - 文章

author: LeetCode
comments: false
date: Wed, 10 Mar 2021 00:00:00 GMT
thumbnail: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png'
---

<div>   
<p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent. Return the answer in <strong>any order</strong>.</p>

<p>A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png" style="width: 200px; height: 162px;" referrerpolicy="no-referrer"></p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> digits = "23"
<strong>Output:</strong> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> digits = ""
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> digits = "2"
<strong>Output:</strong> ["a","b","c"]
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>0 <= digits.length <= 4</code></li>
<li><code>digits[i]</code> is a digit in the range <code>['2', '9']</code>.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>One of the first things you should always do is look at the constraints. Quite often, you can figure out what sort of approach needs to be taken simply from looking at the input size. In an interview, asking your interviewer about the constraints will also show your attention to detail - on top of giving you information.</p>
<p>In this particular problem, the length of the input is <strong>extremely</strong> small, <code>0 <= digits.length <= 4</code>. With such small input sizes, we can safely assume that a brute force solution in which we generate all combinations of letters will be accepted.</p>
<p>Whenever you have a problem where you need to generate all combinations/permutations of some group of letters/numbers, the first thought you should have is backtracking. If you're new to backtracking, check out our <a href="https://leetcode.com/explore/featured/card/recursion-ii/472/backtracking/">backtracking explore card</a>. Backtracking algorithms can often keep the <em>space complexity</em> linear with the input size. </p>
<p><br></p>
<hr>
<h4 id="approach1backtracking">Approach 1: Backtracking</h4>
<p><strong>Intuition</strong></p>
<p>There aren't any smart tricks needed for this problem - the hard part is just figuring out how to correctly generate all possible combinations, and to do this using a standard backtracking algorithm template. Let's break down the problem, by starting with an input that is only 1-digit long, for example <code>digits = "2"</code>. This example is trivial - just generate all letters that correspond with <code>digit = "2"</code>, which would be <code>["a", "b", "c"]</code>.</p>
<p>What if instead we had a 2-digit long input, <code>digits = "23"</code>? Imagine taking each letter of <code>digit = "2"</code> as a <em>starting point</em>. That is, <strong>lock the first letter in</strong>, and solve all the possible combinations that <strong>start with that letter</strong>. If our first letter will always be <code>"a"</code>, then the problem is trivial again - it's the 1-digit case, and all we have to do is generate all the letters corresponding with <code>digit = "3"</code>, and add that to <code>"a"</code>, to get <code>["ad", "ae","af"]</code>. This was easy because we ignored the first letter, and said it will always be <code>"a"</code>. But we know how to generate all the first letters too - it's the 1-digit case which we already solved to be <code>["a", "b", "c"]</code>.</p>
<p>As you can see, solving the 1-digit case is trivial, and solving the 2-digit case is just solving the 1-digit case twice. The same reasoning can be extended to <code>n</code> digits. For the 3-digit case, solve the 2-digit case to generate all combinations of the first 2 letters, and then solve the 1-digit case for the final digit. Now that we know how to solve the 3-digit case, to solve the 4-digit case, solve the 3-digit case for all combinations of the first 3 letters, and then solve the 1-digit case for the final digit. We could extend this to infinity, but, don't worry, for this problem we're finished after 4. </p>
<p>!?!../Documents/17<em>Letter</em>Combinations_Phone.json:960,540!?!</p>
<p><strong>Algorithm</strong></p>
<p>As mentioned previously, we need to <strong>lock-in</strong> letters when we generate new letters. The easiest way to save state like this is to use recursion. Our algorithm will be as follows:</p>
<ol>
<li><p>If the input is empty, return an empty array.</p></li>
<li><p>Initialize a data structure (e.g. a hash map) that maps digits to their letters, for example, mapping "6" to "m", "n", and "o".</p></li>
<li><p>Use a backtracking function to generate all possible combinations.</p>
<ul>
<li>The function should take 2 primary inputs: the current combination of letters we have, <code>path</code>, and the <code>index</code> we are currently checking.</li>
<li>As a base case, if our current combination of letters is the same length as the input <code>digits</code>, that means we have a complete combination. Therefore, add it to our answer, and backtrack.</li>
<li>Otherwise, get all the letters that correspond with the current digit we are looking at, <code>digits[index]</code>.</li>
<li>Loop through these letters. For each letter, add the letter to our current <code>path</code>, and call <code>backtrack</code> again, but move on to the next digit by incrementing <code>index</code> by 1.</li>
<li>Make sure to remove the letter from <code>path</code> once finished with it.</li></ul></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/a4vWh4VR/shared" frameborder="0" width="100%" height="500" name="a4vWh4VR"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(4^N \cdot N)$$, where $$N$$ is the length of <code>digits</code>. Note that $$4$$ in this expression is referring to the maximum <em>value</em> length in the <em>hash map</em>, and <strong><em>not</em></strong> to the length of the <em>input</em>.</p>
<p>The worst-case is where the input consists of only 7s and 9s. In that case, we have to explore 4 additional paths for every extra digit. Then, for each combination, it costs up to $$N$$ to build the combination. This problem can be generalized to a scenario where numbers correspond with up to $$M$$ digits, in which case the time complexity would be $$O(M^N \cdot N)$$. For the problem constraints, we're given, $$M = 4$$, because of digits 7 and 9 having 4 letters each.</p></li>
<li><p>Space complexity: $$O(N)$$, where $$N$$ is the length of <code>digits</code>.</p>
<p>Not counting space used for the output, the extra space we use relative to input size is the space occupied by the recursion call stack. It will only go as deep as the number of digits in the input since whenever we reach that depth, we backtrack.</p>
<p>As the hash map does not grow as the inputs grows, it occupies $$O(1)$$ space. </p></li>
</ul>
<p><br></p>
<hr>  
</div>
            