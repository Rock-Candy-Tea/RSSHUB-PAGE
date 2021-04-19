
---
title: '65. Valid Number'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/65/dfa.png'
author: LeetCode
comments: false
date: Sun, 18 Apr 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/65/dfa.png'
---

<div>   
<p>A <strong>valid number</strong> can be split up into these components (in order):</p>

<ol>
<li>A <strong>decimal number</strong> or an <strong>integer</strong>.</li>
<li>(Optional) An <code>'e'</code> or <code>'E'</code>, followed by an <strong>integer</strong>.</li>
</ol>

<p>A <strong>decimal number</strong> can be split up into these components (in order):</p>

<ol>
<li>(Optional) A sign character (either <code>'+'</code> or <code>'-'</code>).</li>
<li>One of the following formats:
<ol>
<li>At least one digit, followed by a dot <code>'.'</code>.</li>
<li>At least one digit, followed by a dot <code>'.'</code>, followed by at least one digit.</li>
<li>A dot <code>'.'</code>, followed by at least one digit.</li>
</ol>
</li>
</ol>

<p>An <strong>integer</strong> can be split up into these components (in order):</p>

<ol>
<li>(Optional) A sign character (either <code>'+'</code> or <code>'-'</code>).</li>
<li>At least one digit.</li>
</ol>

<p>For example, all the following are valid numbers: <code>["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]</code>, while the following are not valid numbers: <code>["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]</code>.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if </em><code>s</code><em> is a <strong>valid number</strong></em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "0"
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "e"
<strong>Output:</strong> false
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "."
<strong>Output:</strong> false
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> s = ".1"
<strong>Output:</strong> true
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= s.length <= 20</code></li>
<li><code>s</code> consists of only English letters (both uppercase and lowercase), digits (<code>0-9</code>), plus <code>'+'</code>, minus <code>'-'</code>, or dot <code>'.'</code>.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>You're browsing through LeetCode's problems and notice a problem marked as hard with a 16% acceptance rate, the lowest you've ever seen. What could it be? 4D Dynamic Programming + binary search? An esoteric graph algorithm with a name you can't pronounce?</p>
<p>Actually, it's "determine if a string is a number". What gives? In my opinion, the reason this problem is so "difficult" isn't necessarily because it is <strong>super</strong> hard. I think it's just really hard to approach the problem in a way that covers <em>all</em> possible edge cases - something this problem definitely does not lack. Additionally, this is not your typical LeetCode problem, but a problem that is highly representative of a "real world" problem - a seemingly simple task that is frustratingly full of edge cases.</p>
<p>Don't feel discouraged if you're struggling with this problem. When we solve a lot of problems, we discover common patterns, algorithms, and neat tricks that stick with us. We can then apply this knowledge to solve similar problems in the future. The issue with this problem is that there isn't really any other problem on LeetCode that prepares you for it. The key to solving this problem is to carefully read the problem statement, think about edge cases, and keep your code <strong><em>simple</em></strong>.  </p>
<blockquote>
  <p><strong>Interview Tip:</strong> Asked a question like this in an interview? Be sure to communicate thoroughly with your interviewer to make sure you're covering all cases.</p>
</blockquote>
<p><br></p>
<hr>
<h4 id="approach1followtherules">Approach 1: Follow The Rules!</h4>
<p><strong>Intuition</strong></p>
<p>The problem statement outlines a very specific set of rules. Let's put all possible characters into groups, and then create a set of rules for each group. Then, we can iterate through the input and evaluate if the characters are following the rules or not.</p>
<p>What are all of the possible character groups, and what can we say about them? Reading through the problem statement <strong>very carefully</strong>, we can ascertain:</p>
<ol>
<li><p>Digits (one of <code>["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]</code>)</p>
<ul>
<li>Both <strong>decimal numbers</strong> and <strong>integers</strong> must contain at least one digit.</li></ul></li>
<li><p>A sign (<code>"+"</code> or <code>"-"</code>)</p>
<ul>
<li>Sign characters are optional for both <strong>decimal numbers</strong> and <strong>integers</strong>, but if one is present, it will always be the first character. Note, this means that a sign character can also appear immediately after an exponent.</li></ul></li>
<li><p>An exponent (<code>"e"</code> or <code>"E"</code>)</p>
<ul>
<li>Exponents are also optional, but if the string contains one then it must be after a <strong>decimal number</strong> or an <strong>integer</strong>.</li>
<li>An <strong>integer</strong> must follow the exponent.</li></ul></li>
<li><p>A dot (<code>"."</code>)</p>
<ul>
<li>A <strong>decimal number</strong> should only contain one dot. <strong>Integers</strong> cannot contain dots.</li></ul></li>
<li><p>Anything else</p>
<ul>
<li>There will never be anything else in a <em>valid number</em>.</li></ul></li>
</ol>
<p>From these facts, we can logically determine a set of rules to follow in our algorithm.</p>
<p><strong>Rules</strong></p>
<ol>
<li><p>Digits</p>
<ul>
<li>First of all, there must always be at least one digit in the input for it to form a valid number. Let's use a variable <code>seenDigit</code> to indicate whether we have seen a digit yet.</li></ul></li>
<li><p>Signs</p>
<ul>
<li>If a sign is present, it must be the first character in a <strong>decimal number</strong> or <strong>integer</strong>. In a valid number, there are two possible locations for these signs - at the front of the number, or right after an exponent (<code>"e"</code> or <code>"E"</code>) e.g., <code>-63e+7</code>. Therefore, if we see a sign, and it is not the first character of the input, and does not come immediately after an exponent (<code>"e"</code> or <code>"E"</code>), then we know the number is not valid.</li></ul></li>
<li><p>Exponents (<code>"e"</code> or <code>"E"</code>)</p>
<ul>
<li>There cannot be more than one exponent in a <em>valid number</em>, so we will use a variable <code>seenExponent</code> to indicate whether we have already seen an exponent.</li>
<li>An exponent must appear after a <strong>decimal number</strong> or an <strong>integer</strong>. This means if we see an exponent, we must have already seen a digit.</li></ul></li>
<li><p>Dots</p>
<ul>
<li>There cannot be more than one dot in a <em>valid number</em>, since only <strong>integers</strong> are allowed after an exponent, so there cannot be more than one <strong>decimal number</strong>. We will use a variable <code>seenDot</code> to indicate whether we have seen a dot.</li>
<li>If we see a dot appear after an exponent, the number is not valid, because <strong>integers</strong> cannot have dots.</li></ul></li>
<li><p>Anything else</p>
<ul>
<li>Seeing anything else instantly invalidates the input.</li></ul></li>
</ol>
<p><strong>Algorithm</strong></p>
<p>Now that we have laid out the rules, let's iterate over the input. For each character, determine what group it belongs to, and verify that it follows the rules.</p>
<ol>
<li><p>Declare 3 variables <code>seenDigit</code>, <code>seenExponent</code>, and <code>seenDot</code>. Set all of them to <code>false</code>.</p></li>
<li><p>Iterate over the input.</p></li>
<li><p>If the character is a digit, set <code>seenDigit = true</code>.</p></li>
<li><p>If the character is a sign, check if it is either the first character of the input, or if the character before it is an exponent. If not, <code>return false</code>.</p></li>
<li><p>If the character is an exponent, first check if we have already seen an exponent <strong>or</strong> if we have not yet seen a digit. If either is true, then <code>return false</code>. Otherwise, set <code>seenExponent = true</code>, and <code>seenDigit = false</code>. We need to reset <code>seenDigit</code> because after an exponent, we must construct a new <strong>integer</strong>.</p></li>
<li><p>If the character is a dot, first check if we have already seen either a dot or an exponent. If so, <code>return false</code>. Otherwise, set <code>seenDot = true</code>.</p></li>
<li><p>If the character is anything else, <code>return false</code>.</p></li>
<li><p>At the end, return <code>seenDigit</code>. This is one reason why we have to reset <code>seenDigit</code> after seeing an exponent - otherwise an input like <code>"21e"</code> would be incorrectly judged as valid.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/KGRm5qDH/shared" frameborder="0" width="100%" height="500" name="KGRm5qDH"></iframe>
<p><em>"One day I will find the right words, and they will be simple."</em> - Jack Kerouac</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(N)$$, where $$N$$ is the length of <code>s</code>.</p>
<p>We simply iterate over the input once. The number of operations we perform for each character in the input is <em>independent</em> of the length of the string, and therefore only requires constant time. This results in $$N \cdot O(1) = O(N)$$.</p></li>
<li><p>Space complexity: $$O(1)$$.</p>
<p>Regardless of the input size, we only store 3 variables, <code>seenDigit</code>, <code>seenExponent</code>, and <code>seenDot</code>.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2deterministicfiniteautomatondfa">Approach 2: Deterministic Finite Automaton (DFA)</h4>
<p><strong>Intuition</strong></p>
<p>Let's now view Approach 1 from a different angle. There were $$2^3 = 8$$ <strong>states</strong> that the 3 boolean variables could be in. Each time we read a character in the string, we either stayed in the current state (boolean variables stayed the same) or we <strong>transitioned</strong> into a new state (boolean variables changed).
What we've described above is a lot like a  <a href="https://en.wikipedia.org/wiki/Deterministic_finite_automaton">deterministic finite automaton</a>. A DFA is a finite number of states, with transition rules to move between them. </p>
<blockquote>
  <p><strong>Never heard of a DFA before?</strong> </p>
  <p>DFA's are useful for solving many problems, including advanced dynamic programming problems such as <a href="https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/">1411. Number of Ways to Paint N X 3 Grid</a>. So if you're not yet familiar with them, we recommend that you read up on them. It will be worth it!</p>
  <p>DFAs share a lot of similarities with the trie data structure. Recall that a <a href="https://leetcode.com/explore/learn/card/trie/">trie</a> is used to represent a dictionary of words, in a space-efficient manner.  To check whether or not a word is in the dictionary, we would simultaneously traverse through the word and the trie. If we end at a node that is marked as a valid end-point, then we would return true. Otherwise, if we get "stuck", or end at a node that is not an end-point, we would return false. It's the same for a DFA: we start at a "root" node, and then check each character one by one, checking whether or not there is a valid transition we can make. </p>
  <p>There are a few key differences between DFA's and tries, so keep these in mind while reading through the remainder of this section. </p>
  <ol>
  <li>While a trie can only represent a <em>finite</em> number of strings (the given dictionary), a DFA can represent an <em>infinite</em> number of different strings. </li>
  <li>While a trie can only move down the implicit tree, a DFA can essentially "loopback" to a higher level, or stay on the same level, or even the same node.</li>
  <li>A trie is a type of tree, and a DFA is a type of directed graph.</li>
  </ol>
  <p>Other than that, you can lean on your existing knowledge of tries to wrap your head around this new data structure.</p>
</blockquote>
<p><strong>Algorithm</strong></p>
<p>The first step is to design our DFA. Picture the DFA as a directed graph, where each node is a state, and each edge is a transition labeled with a character group (digit, exponent, sign, or dot). There are two key steps to designing it.</p>
<ol>
<li>Identify all valid combinations that the aforementioned boolean variables can be in. Each combination is a <strong>state</strong>. Draw a circle for each state, and label what it means.</li>
<li>For each <strong>state</strong>, consider what a character from each group would mean in the context of that state. Each group will either cause a <strong>transition</strong> into another state, or it will signify that the string is invalid. For each valid transition, draw a directed arrow between the two states and write the group next to the arrow.</li>
</ol>
<blockquote>
  <p><strong>Try this on your own before reading any further!</strong> Take a few minutes and try to design the DFA. Keep in mind that a state can point to itself. For example, with the input <code>"12345"</code>, if we were to use the first approach, after the first character, none of the boolean variables change, so the state should not change. Therefore, the node should have an edge that points to itself, labeled by "digit". Another hint: the start node should have 3 outgoing edges labeled "digit", "sign", and "dot".</p>
</blockquote>
<p><br></p>
<p><img src="https://leetcode.com/articles/Figures/65/dfa.png" width="960" referrerpolicy="no-referrer"></p>
<p><br><br></p>
<p>With our constructed DFA, our algorithm will be:</p>
<ol>
<li><p>Initialize the DFA as an array of hash tables. Each hash table's keys will be a character group, and the values will be the state it should transition to. We can use the indexes of the array to handle state transitions. Set the <code>currentState = 0</code>.</p></li>
<li><p>Iterate through the input. For each character, first determine what group it belongs to. Then, check if that group exists in the current state's hash table. If it does, transition to the next state. Otherwise, return <code>false</code>.</p></li>
<li><p>At the end, check if we are currently in a valid end state: 1, 4, or 7.</p></li>
</ol>
<p>If you're having trouble with your implementation, try to go through your DFA with a complicated case such as <code>-123.456E+789</code>. Follow along with your designed DFA, and if there is a bug, check which edge case went wrong and adjust the graph accordingly. Once your DFA is correctly designed, the coding part will be less challenging.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/V8PqNnMB/shared" frameborder="0" width="100%" height="500" name="V8PqNnMB"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(N)$$, where $$N$$ is the length of <code>s</code>.</p>
<p>We simply iterate through the input once. The number of operations we perform for each character in the input is <em>independent</em> of the length of the string, and therefore each operation requires constant time. So we get $$N \cdot O(1) = O(N)$$.</p></li>
<li><p>Space complexity: $$O(1)$$.</p>
<p>We will construct the same DFA regardless of the input size.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            