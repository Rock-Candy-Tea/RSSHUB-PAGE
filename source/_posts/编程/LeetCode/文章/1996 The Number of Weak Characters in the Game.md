
---
title: '1996. The Number of Weak Characters in the Game'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=5272'
author: LeetCode
comments: false
date: Wed, 13 Jul 2022 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5272'
---

<div>   
<p>You are playing a game that contains multiple characters, and each of the characters has <strong>two</strong> main properties: <strong>attack</strong> and <strong>defense</strong>. You are given a 2D integer array <code>properties</code> where <code>properties[i] = [attack<sub>i</sub>, defense<sub>i</sub>]</code> represents the properties of the <code>i<sup>th</sup></code> character in the game.</p>

<p>A character is said to be <strong>weak</strong> if any other character has <strong>both</strong> attack and defense levels <strong>strictly greater</strong> than this character's attack and defense levels. More formally, a character <code>i</code> is said to be <strong>weak</strong> if there exists another character <code>j</code> where <code>attack<sub>j</sub> > attack<sub>i</sub></code> and <code>defense<sub>j</sub> > defense<sub>i</sub></code>.</p>

<p>Return <em>the number of <strong>weak</strong> characters</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> properties = [[5,5],[6,3],[3,6]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> No character has strictly greater attack and defense than the other.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> properties = [[2,2],[3,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The first character is weak because the second character has a strictly greater attack and defense.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> properties = [[1,5],[10,4],[4,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The third character is weak because the second character has a strictly greater attack and defense.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>2 <= properties.length <= 10<sup>5</sup></code></li>
<li><code>properties[i].length == 2</code></li>
<li><code>1 <= attack<sub>i</sub>, defense<sub>i</sub> <= 10<sup>5</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">## Solution</h2>
<h4 id="overview">Overview</h4>
<p>We have a list of $$N$$ pairs denoting <code>(attack, defense)</code> of the $$N$$ characters. A character is weak if there exists any other character with the attack and defense value strictly more than it. We need to calculate the number of weak characters.</p>
<p>The brute force approach would be to check for every character if it's weak or not and, to check this we can iterate over every other character and see if there is any pair with both values (attack and defense) greater than it. This approach, however, is not efficient as we would be iterating over all the $$N$$ pairs for every character, and hence the time complexity would be $$O(N^2)$$. We will discuss two possible efficient approaches below.
<br></p>
<hr>
<h4 id="approach1sorting">Approach 1: Sorting</h4>
<p><strong>Intuition</strong></p>
<p>Consider a simpler problem, where we only have one parameter say the attack value. In this case, all the characters except the one with the highest attack value will be weak. Hence, the number of weak characters will be the total characters minus the count of characters with the highest attack value. An alternative approach will be: we could sort the array in ascending order and then we can iterate over the array from the right end keeping the maximum attack value we have achieved so far. If this value is more than the current value then the character is weak.</p>
<p>We need to do something similar here, the only difference is we have two parameters. Let's sort these pairs in ascending order of their first value (<code>attack</code>). This way we will only need to take care of the second value (<code>defense</code>) because the character at a smaller index will not be stronger (i.e., will have a weaker attack value) than the character at a greater index.</p>
<p>Now once we have the array sorted in ascending order of their attack value, we can iterate over the pairs from right to left keeping the maximum defense value achieved so far. If this maximum defense value is more than the defense value at the current index then it's a weak character.</p>
<p>The above-mentioned theory has a catch. Consider the list of pairs <code>[(1, 2), (3, 4), (3, 6), (3, 7)]</code>, the pairs are sorted in ascending order of their attack value and in ascending order of defense value in case of a tie in the attack values. When we iterate from the right end the maximum defense value will be equal to <code>7</code> when we reach the pair <code>(3, 6)</code>, and we will consider this pair to be weak. Although, it's not as the attack value is equal and not strictly greater. The point to note here is, that we need to ignore the defense value of the pairs with the same attack value.</p>
<p>We can achieve it by sorting the pairs by ascending order of their attack value and then in descending order of their defense value in case of a tie. This way, the above list would be <code>[(1, 2), (3, 7), (3, 6), (3, 4)]</code> and hence when we iterate over it from the right end, the maximum defense value will be equal to <code>4</code> when we reach the pair <code>(3, 6)</code>. We can take another example <code>[(1, 1), (2, 1), (2, 2), (1, 2)]</code>, after sorting the pairs in ascending order of attack and in ascending order of defense in case of a tie will be  <code>[(1, 1), (1, 2), (2, 1), (2, 2)]</code>, now when we will iterate it from right to left the maximum defense value will be <code>2</code> when we reach the pair <code>(2, 1)</code>, this will lead us to conclude that the pair <code>(2, 1)</code> is weak but it's not. On the other hand, sorting the pairs with the same attack value will produce <code>[(1, 2), (1, 1), (2, 2), (2, 1)]</code> and hence we will not face the previously mentioned issue here.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Sort the list of pairs <code>properties</code> in ascending order of their attack and then in descending order of the defense value. We can achieve it using the custom comparator.</p></li>
<li><p>Initialize the maximum defense value achieved <code>maxDefense</code> to <code>0</code>.</p></li>
<li><p>Iterate over the pairs from right to left and for each pair:</p>
<p>a. If the <code>maxDefense</code> is greater than the defense value of the current character, increment the value <code>weakCharacters</code>.</p>
<p>b. Update the value of <code>maxDefense</code> if it's smaller than the current defense value.</p></li>
<li><p>Return <code>weakCharacters</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/6tCZg6oU/shared" frameborder="0" width="100%" height="429" name="6tCZg6oU"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here, $$N$$ is the number of pairs in the given list <code>properties</code>.</p>
<ul>
<li><p>Time complexity: $$O(N \log N)$$</p>
<p>Sorting a list of $$N$$ elements takes $$O(N \log N)$$ time. The iteration over the sorted list to count the weak character takes $$O(N)$$ time. Hence the time complexity equals $$O(N \log N)$$.</p></li>
<li><p>Space complexity: $$O(\log N)$$</p>
<p>We only need two variables <code>maxDefense</code> and <code>weakCharacters</code> to solve the problem. Some space will be used for sorting the list. The space complexity of the sorting algorithm depends on the implementation of each programming language. For instance, in Java, the <code>Arrays.sort()</code> for primitives is implemented as a variant of the quicksort algorithm whose space complexity is $$O(\log N)$$. In C++ <code>std::sort()</code> function provided by STL is a hybrid of Quick Sort, Heap Sort, and Insertion Sort and has a worst-case space complexity of $$O(\log N)$$. Thus, the use of the inbuilt sort() function might add up to $$O(\log N)$$ to space complexity.
<br></p></li>
</ul>
<hr>
<h4 id="approach2greedy">Approach 2: Greedy</h4>
<p><strong>Intuition</strong></p>
<p>In the previous approach, we sorted the pairs by their attack value first, this helped us to ignore the attack value and decide the type of character based on the defense value. We know that the character will be weak only if there is any character with both attack and defense values greater than it. For a pair <code>(a, b)</code> we can say it to be weak if the maximum defense value among all the pairs with <code>attack-value > a</code> is greater than <code>b</code>. So we will keep the maximum defense value among all the pairs with an attack value greater than <code>x</code>, for every value of <code>x</code>. Then the pair <code>(a, b)</code> will be weak if the maximum defense value stored for value <code>a + 1</code> is greater than <code>b</code>.</p>
<p>To find the maximum defense value as mentioned above. We first find the maximum defense value for the particular value of the attack, to find this we can iterate over the properties from left to right and for each attack value in the pairs, we find the maximum defense value and store it in the <code>maxDefense</code>. Then we can iterate over all the possible values of attack and keep the maximum defense value achieved so far in the array, iterating over the attack values from highest to lowest.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Iterate over <code>properties</code>, and store the maximum defense value for attack values in the array <code>maxDefense</code>.</li>
<li>Iterate over all the possible values of attack from the maximum possible attack value (<code>100000</code>) to <code>0</code>. Keep the maximum value seen so far, <code>maxDefense[i]</code> will represent the maximum value in the suffix <code>[i, maxAttack]</code>.</li>
<li>Iterate over the <code>properties</code> for every pair <code>(attack, defense)</code>, increment the counter <code>weakCharacters</code> if the value at <code>maxDefense[attack + 1]</code> is greater than <code>defense</code>.</li>
<li>Return <code>weakCharacters</code>.</li>
</ol>
<p>The following slideshow demonstrates the algorithm:</p>
<p>!?!../Documents/1996<em>The</em>Number<em>of</em>Weak<em>Characters</em>in<em>the</em>Game.json:960,720!?! <br></p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/4qxxZZz9/shared" frameborder="0" width="100%" height="500" name="4qxxZZz9"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here, $$N$$ is the number of pairs in the given list <code>properties</code>, and $$K$$ is the maximum attack value possible.</p>
<ul>
<li><p>Time complexity: $$O(N + K)$$</p>
<p>The iteration over the pairs to find the maximum defense value for a particular attack value takes $$O(N)$$ time. The iteration over the possible value of the attack property takes $$O(K)$$ time. The iteration over the properties to count the weak characters takes $$O(N)$$ time. Therefore, the total time complexity equals to $$O(N + K)$$.</p></li>
<li><p>Space complexity: $$O(K)$$</p>
<p>The array <code>maxDefense</code> will be of size $$K$$ to store the defense value corresponding to all the attack values.
<br></p></li>
</ul>
<hr>  
</div>
            