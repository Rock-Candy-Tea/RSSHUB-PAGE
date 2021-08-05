
---
title: '1629. Slowest Key'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/1629/Approach1_durationCalculation.png'
author: LeetCode
comments: false
date: Mon, 26 Jul 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/1629/Approach1_durationCalculation.png'
---

<div>   
<p>A newly designed keypad was tested, where a tester pressed a sequence of <code>n</code> keys, one at a time.</p>

<p>You are given a string <code>keysPressed</code> of length <code>n</code>, where <code>keysPressed[i]</code> was the <code>i<sup>th</sup></code> key pressed in the testing sequence, and a sorted list <code>releaseTimes</code>, where <code>releaseTimes[i]</code> was the time the <code>i<sup>th</sup></code> key was released. Both arrays are <strong>0-indexed</strong>. The <code>0<sup>th</sup></code> key was pressed at the time <code>0</code>, and every subsequent key was pressed at the <strong>exact</strong> time the previous key was released.</p>

<p>The tester wants to know the key of the keypress that had the <strong>longest duration</strong>. The <code>i<sup>th</sup></code><sup> </sup>keypress had a <strong>duration</strong> of <code>releaseTimes[i] - releaseTimes[i - 1]</code>, and the <code>0<sup>th</sup></code> keypress had a duration of <code>releaseTimes[0]</code>.</p>

<p>Note that the same key could have been pressed multiple times during the test, and these multiple presses of the same key <strong>may not</strong> have had the same <strong>duration</strong>.</p>

<p><em>Return the key of the keypress that had the <strong>longest duration</strong>. If there are multiple such keypresses, return the lexicographically largest key of the keypresses.</em></p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> releaseTimes = [9,29,49,50], keysPressed = "cbcd"
<strong>Output:</strong> "c"
<strong>Explanation:</strong> The keypresses were as follows:
Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9).
Keypress for 'b' had a duration of 29 - 9 = 20 (pressed at time 9 right after the release of the previous character and released at time 29).
Keypress for 'c' had a duration of 49 - 29 = 20 (pressed at time 29 right after the release of the previous character and released at time 49).
Keypress for 'd' had a duration of 50 - 49 = 1 (pressed at time 49 right after the release of the previous character and released at time 50).
The longest of these was the keypress for 'b' and the second keypress for 'c', both with duration 20.
'c' is lexicographically larger than 'b', so the answer is 'c'.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
<strong>Output:</strong> "a"
<strong>Explanation:</strong> The keypresses were as follows:
Keypress for 's' had a duration of 12.
Keypress for 'p' had a duration of 23 - 12 = 11.
Keypress for 'u' had a duration of 36 - 23 = 13.
Keypress for 'd' had a duration of 46 - 36 = 10.
Keypress for 'a' had a duration of 62 - 46 = 16.
The longest of these was the keypress for 'a' with duration 16.</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>releaseTimes.length == n</code></li>
<li><code>keysPressed.length == n</code></li>
<li><code>2 <= n <= 1000</code></li>
<li><code>1 <= releaseTimes[i] <= 10<sup>9</sup></code></li>
<li><code>releaseTimes[i] < releaseTimes[i+1]</code></li>
<li><code>keysPressed</code> contains only lowercase English letters.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>The problem is to find the slowest key, i.e. the key which was pressed for the longest duration.</p>
<p>This can be solved using simple array traversal. Given the <code>keysPressed</code> and their respective <code>releaseTimes</code>, we can find the duration for each keypress. Once we know this, we can find the longest duration among all key presses and return the slowest key.</p>
<p>Let's look at different approaches to solve the problem.</p>
<hr>
<h4 id="approach1usingmap">Approach 1: Using Map</h4>
<p><strong>Intuition</strong></p>
<p>Let's split the problem into 2 parts:</p>
<ol>
<li><p><em>Find the duration of all keypresses</em></p>
<p>We will traverse the array <code>releaseTimes</code> and find the keypress duration for each corresponding key in <code>keysPressed</code>. For each key at $$i^&#123;th&#125;$$ position in string <code>keysPressed</code>, the keypress duration can be calculated as</p>
<p>Duration for $$i^&#123;th&#125;$$ key = releaseTimes[i] - releaseTimes[i - 1]  //if i > 0
   Duration for $$0^&#123;th&#125;$$ key = releaseTimes[0]                                       </p>
<p>The following figure illustrates the calculation of press duration for <code>keysPressed = cbcd</code> and <code>releaseTimes = [9, 29, 49, 50]</code></p>
<p><img src="https://leetcode.com/articles/Figures/1629/Approach1_durationCalculation.png" alt="Calculation of release times for each keypress duration" referrerpolicy="no-referrer"></p></li>
<li><p><em>Find the key with longest press duration</em></p>
<p>For this, we must first store the press duration that we calculated for each key in the first part. Once we retrieve and store all the durations, the longest press duration can be calculated as:</p>
<p>Longest keypress duration = maximum(longest keypress duration found so far, current keypress duration)</p>
<p>However, the important question is "<em>What is the best way to store the duration of each keypress</em>?"
 Let's evaluate different data structures for this.</p>
<ul>
<li><p>We can store the durations for each keypress in a <em>List</em>.  Each element in the list will store the key and its press duration.   <code>(key, duration)</code>.</p>
<p>The following figure illustrates the list structure for <code>keysPressed = cbcd</code> and <code>releaseTimes = [9, 29, 49, 50]</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/1629/Approach1_listStorage.png" alt="Store the keypress durations in List Data Structure" referrerpolicy="no-referrer"></p></li></ul>
<blockquote>
  <p>Do you notice any problems in this implementation?</p>
</blockquote>
<p>We know that a key can be pressed multiple times. In the above example, the key <code>c</code> is pressed twice. Using lists, we are storing all the press durations of a key. But we are only concerned about the longest keypress duration of each unique key.</p>
<p>In the above example, we can replace the first entry for <code>key = c</code> and <code>duration = 9</code> from the list when we encounter <code>key = c</code> and <code>duration = 20</code>, as we found a new keypress duration for key <code>c</code> that is greater than <code>9</code>.
 However, checking the list to see if <code>c</code> has been pressed before requires linear time, because a list is a <em>Linear</em> data structure.</p>
<blockquote>
  <p>Linear Data Structures store elements in <em>Sequential</em> order. When the data structure is not sorted, locating a specific element may require iterating over every element in the data structure.</p>
</blockquote>
<ul>
<li><p>We can use a <em>map</em> having key-value pair. For each key, the value will be the press duration. Using the map, we can find if the current key has already been encountered in constant time. We can choose to store only the value with the longest keypress duration seen so far for the key.</p>
<p>The following figure illustrates the idea for <code>key = c</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/1629/Approach1_mapStorage.png" alt="Store the keypress durations in Map Data Structure" referrerpolicy="no-referrer"></p></li></ul></li>
</ol>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Iterate over the array <code>releaseTimes</code> to find the press duration <code>currentDuration</code> for each key <code>currentKey</code>.</p></li>
<li><p>Build a map <code>durationMap</code> to store the keypress duration of each key in the form of key-value pair, <code>currentKey -> currentDuration</code>.  If the key is already present in the map, store the duration with the maximum value.</p></li>
<li><p>Iterate over each element in <code>durationMap</code>. Track the maximum duration in the variable <code>longestPressDuration</code> and the corresponding key in the variable  <code>slowestKey</code>. For each entry of the map, get the <code>duration</code> and <code>key</code> and check for the following conditions:</p></li>
</ol>
<ul>
<li><p>If the value of <code>duration</code> is greater than the <code>longestPressDuration</code> found so far, then update the <code>longestPressDuration</code> with the value of <code>duration</code>. Also, the <code>slowestKey</code> will be updated with the corresponding <code>key</code> value.</p></li>
<li><p>If the value of <code>duration</code> is equal to the <code>longestPressDuration</code>, check if the <code>key</code> is lexicographically larger than the <code>slowestKey</code>. If so, update the <code>slowestKey</code> with the <code>key</code> value.</p>
<blockquote>
  <p>Lexicographically larger key denotes the key that is larger than the other key in alphabetical order. For example, <code>b</code> is lexicographically larger than <code>a</code>, <code>c</code> is larger than <code>b</code>, and so on.</p>
</blockquote></li>
</ul>
<ol>
<li>At the end, return the <code>slowestKey</code> found after iterating over all the elements in the map.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/Eck3Ftep/shared" frameborder="0" width="100%" height="500" name="Eck3Ftep"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the size of array <code>releaseTimes</code> and $$K$$ be the number of distinct characters in <code>keysPressed</code>.</p>
<ul>
<li><p>Time Complexity: $$O(N)$$. Let's find the time complexity of each step.</p>
<p>We iterate over the array <code>releaseTimes</code> of size $$N$$ to find the duration of each key. The time complexity of each iteration is constant, so the overall time complexity of iterating over the array is $$O(N)$$.</p>
<p>Next, we iterate over all elements of <code>durationMap</code>. In the worst case, if all the keys are unique, the size of <code>durationMap</code> would be equal to $$K$$. Thus, the time complexity is $$O(K)$$.</p>
<p>This gives us total time complexity is $$O(N) + O(K)$$.  Since, in this problem, $$K$$ is at most 26 and must be less than or equal to $$N$$ the time complexity simplifies to $$O(N)$$.</p></li>
<li><p>Space Complexity: $$O(K)$$, as we are using additional space for <code>durationMap</code> which can have maximum $$K$$ elements.</p></li>
</ul>
<hr>
<h4 id="approach2fixedsizearray">Approach 2: Fixed Size Array</h4>
<p><strong>Intuition</strong></p>
<p>In the previous approach, we were able to efficiently store only the longest keypress duration for each key by using a <code>map</code>.</p>
<p>However, we know that the <code>keysPressed</code> contains only the lowercase English letters. We can simplify our solution even further by using a fixed-size array, where each element in the array represents each key. As there are <code>26</code> lowercase letters in the English alphabet, we will use an array of size <code>26</code>.</p>
<blockquote>
  <p>The advantage of using an array is that it takes slightly less time to access elements in an array compared to a hashmap.  Also, when the array is dense (all elements are sequential and the first element starts at index 0 as shown below) it uses slightly less space than a hashmap.</p>
</blockquote>
<p>The following figure illustrates how the press duration would be stored for each key.</p>
<p><img src="https://leetcode.com/articles/Figures/1629/Approach2_arrayStorage.png" alt="Store the keypress durations in Fixed Size Array" referrerpolicy="no-referrer"></p>
<p>This implementation has one additional benefit. When two keys have been pressed for the same duration, we will consider the lexicographically largest key. Unlike in the unordered map, where we can't access the keys in sorted order, in the list we can traverse values in descending order. Therefore, we no longer need to check for cases when the current keypress duration is equal to the longest keypress duration found so far.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Build an array <code>durationArray</code> of size <code>26</code> to store the keypress duration of each key and initialize all the values in the array to <code>0</code>.</p></li>
<li><p>Iterate over the array <code>releaseTime</code> to calculate the longest press duration <code>currentDuration</code> for each key <code>currentKey</code>.</p>
<p>Each iteration, find the index for <code>currentKey</code> in <code>durationArray</code> and store its press duration at that location.</p>
<p>For example, if <code>currentKey</code> is <code>d</code>, it is at $$4^&#123;th&#125;$$ position in alphabetical order (<code>a</code>, <code>b</code>, <code>c</code>,<code>d</code>, …, <code>z</code>). Hence, store the press duration <code>currentDuration</code> for <code>d</code> at position <code>durationArray[3]</code>(since array is 0-indexed).</p></li>
</ol>
<blockquote>
  <p>The easiest way to find the position for any key <code>currentKey</code> in its alphabetical order is by subtracting the ASCII value of <code>a</code> from the <code>currentKey</code>. This will give us the distance of the <code>currentKey</code> from <code>a</code> in alphabetical order.
       We will always store the maximum press duration seen so far for each key as we did in <em>Approach 1</em>.</p>
</blockquote>
<ol start="3">
<li><p>Next, iterate over <code>durationArray</code> and find the key with the longest press duration. As discussed above, we will start from the lexicographically largest key. Hence, we will iterate over <code>durationArray</code> in reverse order.</p>
<p>Initially, assume the slowest key is <code>z</code> at position <code>durationArray[25]</code>. We will only keep track of the index of the slowest key found so far in the <code>slowestKeyIndex</code> variable. Iterate from <code>y</code> to <code>a</code> and update the <code>slowestKeyIndex</code> when <code>currentDuration</code> is greater than the keypress duration of the slowest key found so far.</p></li>
<li><p>At the end, return the slowest key.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/ATxvmWV2/shared" frameborder="0" width="100%" height="463" name="ATxvmWV2"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the size of array <code>releaseTimes</code> and $$M$$ be the maximum possible number of distinct characters.  The value of $$M$$ is fixed as 26 for this problem because <code>keysPressed</code> contains only lowercase English letters.</p>
<ul>
<li><p>Time Complexity: $$O(N + M)$$. Let's find the time complexity of each step.</p>
<p>We iterate over the array <code>releaseTimes</code> of size $$N$$ to find the duration of each key. The time complexity of each iteration is constant, so the overall time complexity of iterating over the array is $$O(N)$$.</p>
<p>Next, we iterate over all elements of <code>durationArray</code> of size $$M$$ which takes $$O(M)$$ time.</p>
<p>This gives us total time complexity is $$O(N) + O(M)$$.  Since, in this problem, the value of $$M$$ is fixed at 26, $$O(M)$$ may be considered as constant and the total time complexity would simplify to $$O(N)$$.</p></li>
<li><p>Space Complexity: $$O(M)$$, as we are using $$O(M)$$ extra space for <code>durationArray</code>.  However, since the value of $$M$$ is fixed at 26, the space complexity may be considered as $$O(1)$$.</p></li>
</ul>
<hr>
<h4 id="approach3constantextraspace">Approach 3: Constant Extra Space</h4>
<p><strong>Intuition</strong></p>
<p>In the above approaches, we implemented the problem in 2 steps. First, we calculated the press duration for each key and stored the results. Then we iterated over the stored results to find the slowest key.</p>
<p>We can combine this into a single step. As we are iterating over the <code>releaseTimes</code> to calculate the duration for each key, we can also keep track of the <code>slowestKey</code> found so far. In this way, the solution can be implemented in a single iteration without the need for an additional data structure.
Let's look at the algorithm in detail.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initially, assume the slowest key is the first key in the string <code>keysPressed</code>. The press duration for this slowest key is initialized to <code>releaseTimes[0]</code>. Let's use the variables <code>slowestKey</code> and <code>longestPress</code> to track the slowest key and its corresponding press duration.</p></li>
<li><p>As we iterate over the <code>releaseTimes</code>, calculate the press duration <code>currentDuration</code> for each key. The new slowest key is found if either of the following 2 conditions is satisfied:</p></li>
<li><p>The value of <code>currentDuration</code> is larger than <code>longestPress</code>.</p></li>
<li><p>The value of <code>currentDuration</code> is equal to <code>longestPress</code> and the current key is lexicographically larger than the slowest key found so far.</p>
<p>Update the <code>longestPress</code> and <code>slowestKey</code> if either of the above conditions is satisfied.</p></li>
<li><p>At the end, return the <code>slowestKey</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/A8KsAySu/shared" frameborder="0" width="100%" height="395" name="A8KsAySu"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the size of array <code>releaseTimes</code>.</p>
<ul>
<li><p>Time Complexity: $$O(N)$$. We iterate over the array <code>releaseTimes</code> of size $$N$$ once to find the slowest key and each iteration requires only constant time.</p></li>
<li><p>Space Complexity: $$O(1)$$, as we are using only constant extra space.</p></li>
</ul>
<hr>  
</div>
            