
---
title: '1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_2.png'
author: LeetCode
comments: false
date: Thu, 13 May 2021 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_2.png'
---

<div>   
<p>Given a rectangular cake with height <code>h</code> and width <code>w</code>, and two arrays of integers <code>horizontalCuts</code> and <code>verticalCuts</code> where <code>horizontalCuts[i]</code> is the distance from the top of the rectangular cake to the <code>ith</code> horizontal cut and similarly, <code>verticalCuts[j]</code> is the distance from the left of the rectangular cake to the <code>jth</code> vertical cut.</p>

<p><em>Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays <code>horizontalCuts</code> and <code>verticalCuts</code>. </em>Since the answer can be a huge number, return this modulo 10^9 + 7.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<p><img alt src="https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_2.png" style="width: 300px; height: 320px;" referrerpolicy="no-referrer"></p>

<pre><strong>Input:</strong> h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
<strong>Output:</strong> 4 
<strong>Explanation:</strong> The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
</pre>

<p><strong>Example 2:</strong></p>

<p><strong><img alt src="https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_3.png" style="width: 300px; height: 320px;" referrerpolicy="no-referrer"></strong></p>

<pre><strong>Input:</strong> h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
<strong>Output:</strong> 9
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>2 <= h, w <= 10^9</code></li>
<li><code>1 <= horizontalCuts.length < min(h, 10^5)</code></li>
<li><code>1 <= verticalCuts.length < min(w, 10^5)</code></li>
<li><code>1 <= horizontalCuts[i] < h</code></li>
<li><code>1 <= verticalCuts[i] < w</code></li>
<li>It is guaranteed that all elements in <code>horizontalCuts</code> are distinct.</li>
<li>It is guaranteed that all elements in <code>verticalCuts</code> are distinct.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>Calculating the area of every possible piece of cake can get out of hand very quickly. In the first example alone, there are already 12 pieces of cake, and our input can have up to 100,000 vertical and horizontal cuts. We need a smarter way to find the area of the largest piece of cake.</p>
<p>The key insight to solve this problem is that not all of the pairs of horizontal and vertical cuts matter. Let's take a step back - the area of a cake piece is defined by <code>width * height</code>. If we were to consider <strong>only</strong> the horizontal cuts, then we would end up with many pieces of cake with <code>width = w</code> and varying heights. For each new piece, making a vertical cut will change the width, but not the height.</p>
<p>Let's use the first test case in the problem description as an example. If we were to only apply the horizontal cuts <code>[1, 2, 4]</code>, we will end up with 4 pieces of cake, all with <code>width = 4</code>. Take the piece of cake with <code>height = 2</code> between the cuts at <code>2</code> and <code>4</code>, and make any vertical cut you want - notice that the height will always be <code>2</code>. The same logic can be applied when considering the vertical cuts first - we will have many pieces of cake with <code>height = h</code> and varying widths.</p>
<p>Therefore, we know the largest piece of cake must have a height equal to the tallest height after applying only the horizontal cuts, and it will have a width equal to the widest width after applying only the vertical cuts.</p>
<p>!?!../Documents/1465<em>Max</em>Area_Cake.json:960,540!?!</p>
<p><br></p>
<hr>
<h4 id="approachsort">Approach: Sort</h4>
<p><strong>Intuition</strong></p>
<p>As mentioned above, we can find the max height and the max width separately. Our final answer will be <code>maxHeight * maxWidth</code>. Each height and width is defined by the distance between 2 cuts. In the first example, the max height of <code>2</code> is defined by the distance between cuts <code>2</code> and <code>4</code> (4 - 2 = 2). To find all heights and widths, we must first sort our inputs <code>horizontalCuts</code> and <code>verticalCuts</code>. This will ensure that all of the cuts that are beside each other on the cake are also beside each other in the array. Then, we can iterate through the sorted inputs one at a time and find each height or width by simply taking the difference between two adjacent cuts.</p>
<p>One thing to be careful about is the edges. For cuts in the middle, the distance is defined by the difference between two cuts. However, for the edges, they are defined by the cake's dimensions. </p>
<ul>
<li>The top-most cut's height will be equal to <code>horizontalCuts[0]</code>, while the bottom-most cut's height will be equal to <code>h - horizontalCuts[horizontalCuts.length - 1]</code>.</li>
<li>The left-most cut's width will be equal to <code>verticalCuts[0]</code>, while the right-most cut's width will be equal to <code>w - verticalCuts[verticalCuts.length - 1]</code>.</li>
</ul>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Sort both <code>horizontalCuts</code> and <code>verticalCuts</code> in ascending order.</p></li>
<li><p>Initialize a variable <code>maxHeight</code> as the larger of the top and bottom edge: <code>maxHeight = max(horizontalCuts[0], h - horizontalCuts[horizontalCuts.length - 1])</code>.</p></li>
<li><p>Iterate through <code>horizontalCuts</code> starting from index 1 (skip the 0th index since it represents the edge cut, which we accounted for in the previous step). At each iteration, find the height defined by the $$i^&#123;th&#125;$$ cut and the nearest cut above, <code>horizontalCuts[i] - horizontalCuts[i - 1]</code>. Update <code>maxHeight</code> if necessary.</p></li>
<li><p>Initialize a variable <code>maxWidth</code> as the larger of the left and right edge: <code>maxWidth = max(verticalCuts[0], w - verticalCuts[verticalCuts.length - 1])</code>.</p></li>
<li><p>Iterate through <code>verticalCuts</code> starting from index 1. At each iteration, find the width defined by the $$i^&#123;th&#125;$$ cut and the nearest cut to the left, <code>verticalCuts[i] - verticalCuts[i - 1]</code>. Update <code>maxWidth</code> if necessary.</p></li>
<li><p>Our maximum area is <code>maxHeight * maxWidth</code>. Don't forget the modulo $$10^&#123;9&#125; + 7$$, and depending on what language you're using, be careful of overflow. Return the maximum area.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/QtvEkVav/shared" frameborder="0" width="100%" height="500" name="QtvEkVav"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the length of <code>horizontalCuts</code> and $$M$$ as the length of <code>verticalCuts</code>,</p>
<ul>
<li><p>Time complexity: $$O(N \cdot \log(N) + M \cdot \log(M))$$</p>
<p>Sorting an array of length $$n$$ costs $$n \cdot logn$$ time. We need to sort both <code>horizontalCuts</code> and <code>verticalCuts</code>, which is why both are present in the time complexity. Although we also iterate through both arrays, which costs $$O(N)$$ and $$O(M)$$ time, these iterations are not as expensive as the sorting, and by the rules of Big O, do not get included in the final time complexity.</p></li>
<li><p>Space complexity: $$O(1)$$</p>
<p>Regardless of the input size, we only ever need to use 2 variables: <code>maxHeight</code> and <code>maxWidth</code>.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            