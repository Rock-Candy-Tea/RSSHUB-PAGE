
---
title: '218. The Skyline Problem'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2020/12/01/merged.jpg'
author: LeetCode
comments: false
date: Wed, 03 Aug 2022 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2020/12/01/merged.jpg'
---

<div>   
<p>A city's <strong>skyline</strong> is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return <em>the <strong>skyline</strong> formed by these buildings collectively</em>.</p>

<p>The geometric information of each building is given in the array <code>buildings</code> where <code>buildings[i] = [left<sub>i</sub>, right<sub>i</sub>, height<sub>i</sub>]</code>:</p>

<ul>
<li><code>left<sub>i</sub></code> is the x coordinate of the left edge of the <code>i<sup>th</sup></code> building.</li>
<li><code>right<sub>i</sub></code> is the x coordinate of the right edge of the <code>i<sup>th</sup></code> building.</li>
<li><code>height<sub>i</sub></code> is the height of the <code>i<sup>th</sup></code> building.</li>
</ul>

<p>You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height <code>0</code>.</p>

<p>The <strong>skyline</strong> should be represented as a list of "key points" <strong>sorted by their x-coordinate</strong> in the form <code>[[x<sub>1</sub>,y<sub>1</sub>],[x<sub>2</sub>,y<sub>2</sub>],...]</code>. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate <code>0</code> and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.</p>

<p><b>Note:</b> There must be no consecutive horizontal lines of equal height in the output skyline. For instance, <code>[...,[2 3],[4 5],[7 5],[11 5],[12 7],...]</code> is not acceptable; the three lines of height 5 should be merged into one in the final output as such: <code>[...,[2 3],[4 5],[12 7],...]</code></p>

<p> </p>
<p><strong>Example 1:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2020/12/01/merged.jpg" style="width: 800px; height: 331px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
<strong>Output:</strong> [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
<strong>Explanation:</strong>
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> buildings = [[0,2,3],[2,5,3]]
<strong>Output:</strong> [[0,3],[5,0]]
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= buildings.length <= 10<sup>4</sup></code></li>
<li><code>0 <= left<sub>i</sub> < right<sub>i</sub> <= 2<sup>31</sup> - 1</code></li>
<li><code>1 <= height<sub>i</sub> <= 2<sup>31</sup> - 1</code></li>
<li><code>buildings</code> is sorted by <code>left<sub>i</sub></code> in non-decreasing order.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>In this problem, we are given a list of buildings and would like to construct the <strong>skyline</strong>, a set of key points that describes the contour of the buildings, as shown in the picture below.</p>
<p><img src="https://leetcode.com/articles/Figures/218_re/218_description.png" alt="img" referrerpolicy="no-referrer"></p>
<p>This problem is very interesting and challenging with some tricky corner cases. Here we introduce several approaches starting with two brute-force algorithms that might not pass under the limited time but can pave the way for more efficient approaches.</p>
<p><br></p>
<hr>
<h4 id="approach1bruteforcei">Approach 1: Brute Force I</h4>
<p>Collect all the positions of the left and right edges from <code>buildings</code>, that's all the possible <code>x</code> where skyline key points are generated. For convenience, let's number these unique positions sequentially, representing these positions by indexes according to their location on the x-axis.</p>
<p><img src="https://leetcode.com/articles/Figures/218_re/218_bf1_more.png" alt="img" referrerpolicy="no-referrer"></p>
<p>If a building with height <code>h</code> covers the indexes from <code>x_i</code> to <code>x_j</code>, then all the indexes from <code>x_i</code> to <code>x_j</code> (exclusive) have the height of <code>h</code> at least. Notice that the right edge of a building doesn't count!</p>
<p>Therefore, we can iterate over all the buildings, and for each building we find the positions of its left edge and right edge and their corresponding indexes <code>left_index</code> and <code>right_index</code>. Then we update the maximum height for all the indexes within the range <code>[left_index, right_index)</code>. Finally, traverse the updated <code>heights</code> and output all the positions where height changes as skyline key points!</p>
<p>!?!../Documents/218<em>re/bf</em>1.json:601,301!?!</p>
<p><strong>Algorithm</strong></p>
<p>1) Collect all unique positions for the left and right edges of the buildings in <code>buildings</code> and save them in list <code>edgeSet</code>.
2) Initalize:
    - an empty list <code>heights</code> of the same length as <code>edgeSet</code>.
    - hashtable <code>edge_index_map</code> stores corresponding index and value of elements from <code>heights</code>.
    - empty list <code>answer</code> for skyline key points.
3) Iterate over <code>buildings</code>, for each building <code>buildings[i]</code>:
    - Get the index of its left edge and right edge <code>left_index</code>, <code>right_index</code>, and its height <code>height</code>.
    - For index in <code>[left_index, right_index)</code>, update <code>heights[index]</code> if necessary.
4) Traverse the updated <code>heights</code> and add all the positions where the height changes to <code>answer</code> as skyline key points.
5) Return <code>answer</code> as the skyline.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/o3jQQPuz/shared" frameborder="0" width="100%" height="500" name="o3jQQPuz"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the length of the input array <code>buildings</code>.</p>
<ul>
<li><p>Time complexity: $$O(n^2)$$</p>
<ul>
<li>Obtaining our sorted list of positions will require an average of $$O(n \log n)$$ time.</li>
<li>Then for each of the $$n$$ buildings, we need to update the maximum heights at all the indexes covered by its left edge and right edge. In the worst-case scenario, we have to update $$n$$ values in each iteration step, so this process will take $$O(n^2)$$ time.</li></ul></li>
<li><p>Space complexity: $$O(n)$$</p>
<ul>
<li>The number of left and right edges is $$2n$$, thus we need a set and an array of size $$O(n)$$.</li>
<li>Then we need a hash table of indexes and an array of heights, both of size $$O(n)$$.</li>
<li>We also use an answer array to store all the skyline points, of which there are at most $$n$$.</li></ul></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2bruteforceiisweepline">Approach 2: Brute Force II, Sweep Line</h4>
<p>Another instinctive idea is to use a vertical line of infinite length to sweep over the ground from the left to right. The line stops by every edge and we shall record the maximum height among all the buildings that intersect with the line. As shown in the picture below, the right edge of a building doesn't count!</p>
<p><img src="https://leetcode.com/articles/Figures/218_re/218_sw_exp.png" alt="img" referrerpolicy="no-referrer"></p>
<p>Let's refer to the slides below for an explanation:</p>
<p>!?!../Documents/218<em>re/bf</em>2.json:601,301!?!</p>
<p>For more information about Sweep Line Algorithm, please refer to <a href="https://en.wikipedia.org/wiki/Sweep_line_algorithm">wikipedia</a>.</p>
<p><strong>Algorithm</strong>
1) Initialize an empty list <code>answer</code> for skyline key points.
2) Use a set (<code>edgeSet</code>) to store all distinct edges in <code>buildings</code>.
3) Iterate over the sorted <code>positions</code>, and for each position:
    - Check for buildings that intersect with the imaginary vertical line at <code>position</code>. (A building is considered to be intersecting with the line if <code>position</code> is within the range <code>[left, right)</code>.)
4) The <code>max_height</code> is the maximum height of the intersecting buildings at <code>position</code>, or <code>0</code> if no building intersects with the line.
5) If <code>max_height</code> differs from that of the previous skyline point, add a new skyline point to <code>answer</code>.
6) Return <code>answer</code> as the skyline.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/oP9nWx7a/shared" frameborder="0" width="100%" height="500" name="oP9nWx7a"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the length of the input array <code>buildings</code>.</p>
<ul>
<li><p>Time complexity: $$O(n^2)$$</p>
<ul>
<li>Obtaining our sorted list of positions will require an average of $$O(n \log n)$$ time.</li>
<li>Then for each of the $$2 n$$ positions we need to check if any of the $$n$$ buildings intersect with the line at that position. This process will take $$O(n^2)$$ time.</li></ul></li>
<li><p>Space complexity: $$O(n)$$</p>
<ul>
<li>The number of left and right edges is $$2 n$$, thus we need a set and an array of size $$O(n)$$.</li>
<li>We also use an answer array to store all the skyline points, of which there are at most $$n$$.</li></ul></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3sweeplinepriorityqueue">Approach 3: Sweep Line + Priority Queue</h4>
<p><strong>Intuition</strong>   </p>
<p>In the previous sweep line approach, we had to iterate through all the buildings at each position and ended up with $$O(n^2)$$ time complexity. We are looking for a more efficient way of determining such intersecting buildings. (For convenience, let's call them "live" buildings from now on.)</p>
<p>Notice that the current height is only decided by the tallest "live" building, hence we no longer need to traverse over all the buildings if we can get the tallest "live" building directly! This can be implemented by using a <strong>priority queue</strong>. Similar to the previous approach, we can use a vertical line to sweep along the <code>x</code> axis. In this approach, however, we add each intersecting building to the priority queue <code>live</code>. Therefore, whenever we need to get the height of the tallest "live" building, we can just check the top result from <code>live</code> (or 0 if <code>live</code> is empty), rather than iterating over all the buildings! </p>
<p><strong>What if we run into the right edge of a building?</strong></p>
<p>Theoretically, we should remove the building from <code>live</code> once we run into its right edge (recall the right-edge-doesn't-count conclusion), meaning we have passed this building so it won't contribute to the skyline height anymore. As long as the tallest building is surely live, it's okay if some lower buildings that have been passed are still in <code>live</code>. We only need to make sure we remove a "past" building once it becomes the tallest one in <code>live</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/218_re/218_sl_exp2.png" alt="img" referrerpolicy="no-referrer"></p>
<p>First, we need to sort all the edges in non-decreasing order for the sweep line algorithm. In order to track which building a certain edge belongs to, we should also mark each edge with the index of the building in <code>buildings</code>. </p>
<p>Since there might be multiple edges at the same position on the x-axis, we should finish handling all edges at the same position before moving on to the next position.</p>
<p>Take the slide below as an example!</p>
<p>!?!../Documents/218_re/sl.json:601,301!?!</p>
<p><strong>Algorithm</strong></p>
<p>2) Iterate over <code>buildings</code> and store each building's edges separately with the building's index as a reference in <code>edges</code>. 
3) Sort the entries in <code>edges</code> by their first element.
4) Iterate over the sorted <code>edges</code> and for each edge/index:
    - If <code>buildings[b][0] == curr_x</code>, meaning its a left edge and the <code>building[b]</code> is live, we add <code>(height, right)</code> to <code>live</code>.<br>
    - While the tallest live building has been passed, remove it from <code>live</code>.
5) Once we finish handling all the edges at the <code>curr_x</code>, we shall move on to the next position.
6) After the iteration, return <code>answer</code> as the skyline.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/CCgCGTcp/shared" frameborder="0" width="100%" height="500" name="CCgCGTcp"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the length of the input array <code>buildings</code>.</p>
<ul>
<li><p>Time complexity: $$O(n\log n)$$</p>
<ul>
<li>There are $$2 n$$ edges so we have at most $$O(n)$$ unique positions during the iteration.</li>
<li>At each step, we need to pop out the passed buildings from priority queue <code>live</code> and put in the newly added building (if exist). In worse-case scenario, we have $$O(n)$$ live buildings in <code>live</code>, both the <code>pop</code> and <code>push</code> operations take $$O(\log n)$$ time.</li>
<li>To sum up, the overall time complexity is $$O(n \log n)$$.</li></ul></li>
<li><p>Space complexity: $$O(n)$$</p>
<ul>
<li>We initalize <code>edges</code> of size $$O(2n)$$ to store all the edges and its indexes, empty list <code>answer</code> to store all the skyline key points. </li>
<li>We maintain a priority queue <code>live</code> which has at most $$O(n)$$ elements.</li>
<li>There can be at most $$O(n)$$ skyline key points, thus <code>answer</code> takes at most $$O(n)$$ space.</li>
<li>Therefore, the overall space complexity is $$O(n)$$. </li></ul></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach4sweeplinetwopriorityqueue">Approach 4: Sweep Line + Two Priority Queue</h4>
<p>We still use a priority queue <code>live</code> to keep all the buildings we picked up. Recall that in the previous approaches, we have to assign an auxiliary mark (the mark could either be the position of its right edge, or its original index in <code>buildings</code>) to each building, thus we can get the position of its right edge, so as to judge if the top building from <code>live</code> should be dropped. Here, we can make this step more intuitive, by discarding this unique index and only storing the heights of buildings: Whenever we meet the left edge of a building, we just add its height to <code>live</code>. </p>
<p>But how do we know if some buildings apart from the top buildings should be removed? Since we are not expected to remove an intermediate element from a regular priority queue.</p>
<blockquote>
  <p>We use another priority queue (let's call it <code>past</code>) to keep all the buildings that <strong>should be</strong> removed from <code>live</code> but <strong>haven't been</strong> yet.</p>
</blockquote>
<p>We can see that <code>live</code> works as a debt card: it can temporarily record our "debt". Once we are able to pay the "debt", that is. when the top building in <code>live</code> equals the top building in <code>past</code>, we will remove it from <code>past</code>. Since the "debt" has been cleared, we will remove the top building from <code>past</code> as well.</p>
<p>We repeatedly remove top building from both <code>live</code> and <code>past</code>, until:</p>
<ul>
<li><code>past</code> is empty, meaning every building in <code>live</code> is literally "live".</li>
<li>The top building in <code>live</code> is taller than the top building in <code>past</code>, in this case, we may still have some buildings to remove, but their height is too small to affect the height of the top building.</li>
</ul>
<p>Take the following slides as an example:</p>
<p>!?!../Documents/218_re/2pq.json:601,301!?!</p>
<p><strong>Algorithm</strong>
1) Initalize: 
    - an empty list <code>edges</code> for storing all the x-values of the left and right edges.
    - an empty list <code>answer</code> for storing all the skyline key points.
    - an empty priority queue <code>live</code> for storing the live buildings.
    - an empty priority queue <code>past</code> for storing the buildings that should be removed already.
2) Iterate over <code>buildings</code>, for <code>building[i] = [left, right, height]</code>, add <code>[left, height]</code>, <code>[right, -height]</code> to <code>edges</code>, thus we can easily distinguish if an edge is a left edge (<code>height > 0</code>) or a right edge (<code>height < 0</code>).
3) Sort <code>edges</code> by the first elements of its elements. 
4) Iterate over <code>edges</code>, for every <code>edges[idx]</code> let <code>curr_x = edge[idx][0]</code>, while <code>curr_x = edge[idx][0]</code>:
    - If <code>height > 0</code>, add <code>height</code> to <code>live</code>.<br>
    - Otherwise, add <code>height</code> to <code>past</code>.
    - increment <code>idx</code> by 1.
6) While <code>past</code> is not empty and top buildings from <code>live</code> and <code>past</code> have the same height, remove top building from both <code>live</code> and <code>past</code>. 
7) Get <code>max_height</code> from <code>live</code> (<code>max_height = 0</code> if <code>live</code> is empty).
8) If <code>answer</code> is empty or <code>max_height</code> changes, add <code>[curr_x, max_height]</code> to <code>answer</code> as a new skyline key point.
9) After the iteration, return <code>answer</code> as the skyline.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/VUM6UxtA/shared" frameborder="0" width="100%" height="500" name="VUM6UxtA"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the length of the input array <code>buildings</code>.</p>
<ul>
<li><p>Time complexity: $$O(n\cdot\log n)$$</p>
<ul>
<li>We sort a list with length of $$2\cdot n$$, which takes $$O(n)$$ time.</li>
<li>Then we iterate over all the sorted edges, during the iteration, we have to manipulate on two priority queues, the amortized cost of this operation is $$O(\log n)$$.</li>
<li>To sum up, the overall time complexity is $$O(n\cdot\log n)$$</li></ul></li>
<li><p>Space complexity: $$O(n)$$</p>
<ul>
<li>We used an empty array <code>edges</code> to store the information of all the left and right edges. There are $$2\cdot n$$ edges and will cost $$O(n)$$ space.</li>
<li>Besides, we need to maintain two priority queues, in the worst-case scenario, each of them takes $$O(n)$$ space. </li>
<li>To sum up, the overall space complexity is $$O(n)$$.</li></ul></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach5unionfind">Approach 5: Union Find</h4>
<p><strong>Algorithm</strong></p>
<p>Recall the first brute-force solution with $$O(n^2)$$ time complexity; whenever we added a new building, we had to traverse over all the indexes covered by the building and update the appropriate values in <code>heights</code>. Now suppose that a building has a very small height, and many of its <code>heights</code> values have previously been updated by some taller buildings, thus won't update this time. </p>
<p><img src="https://leetcode.com/articles/Figures/218_re/218_uf_brute.png" alt="img" referrerpolicy="no-referrer"></p>
<p>Can we find a method to avoid such "unnecessary" non-updates? The answer is: "Yes!"</p>
<p>Imagine if we give some indexes a billboard saying:</p>
<blockquote>
  <p><strong>All the heights starting from me and ending by XXX (an index on its right) have already been updated! These heights are larger than yours, thus you don't need to bother attempting to update these heights; just jump directly to XXX and move on!</strong></p>
</blockquote>
<p>It seems feasible! Let's give it a shot by assigning a value to each edge, which equals the rightmost edge of the consecutive range having a height no less than the current edge.</p>
<p><strong>What is the use of such value?</strong></p>
<blockquote>
  <p>It will help identify the range of edges that we can just skip past.</p>
</blockquote>
<p><img src="https://leetcode.com/articles/Figures/218_re/218_uf_mark.png" alt="img" referrerpolicy="no-referrer"></p>
<p>As shown in the picture below, unlike iterating over every index and updating nothing, we will first look up the current index in <code>root</code> to see if we can skip past any intermediate indexes that have already been updated by some taller buildings. This is the core difference between this approach and the brute-force one!</p>
<p><img src="https://leetcode.com/articles/Figures/218_re/218_uf_skip.png" alt="img" referrerpolicy="no-referrer"></p>
<p><strong>How can we maximize skips by assuring that the updates are made by taller buildings first?</strong></p>
<blockquote>
  <p>We can iterate over the buildings by descending height. Therefore, for each building, all the previous updates in <code>heights</code> are made by buildings of larger or equal height! We can safely skip those indexes that have been updated already.</p>
</blockquote>
<p><strong>Which data structure should we use?</strong></p>
<blockquote>
  <p>We can use a disjoint-set data structure to store this relation between indexes. The <code>root</code> of an index <code>x_i</code> can be regarded as the rightmost index <code>x_j</code> where all indexes in the range <code>[x_i, x_j)</code> have larger or equal heights as that of <code>x_i</code>.</p>
</blockquote>
<p>Let's refer to the slides below as an example:</p>
<p>!?!../Documents/218_re/uf.json:601,301!?!</p>
<p><strong>Implementation</strong></p>
<p>1) Use a set to collect all the unique positions of left and right edges of the buildings in <code>buildings</code> and make sure they're in sorted order.
3) Iterate over all the buildings by descending height, and for each building:
    - Use the hash table to convert the left and right edges into <code>leftIndex</code> and <code>rightIndex</code>.
    - While <code>leftIndex < rightIndex</code>:
        - Use the <code>UnionFind.Find()</code> to advance <code>leftIndex</code> to <code>Find(leftIndex)</code>, skipping past unnecessary indexes.
        - Update <code>heights</code> with the current <code>height</code> at the new <code>leftIndex</code>.
        - Use the <code>UnionFind.Union()</code> to set the root of <code>leftIndex</code> to the root of <code>rightIndex</code> and increment <code>leftIndex</code> by 1.
5) Iterate over the updated <code>heights</code> and add every position where the height changes to <code>answer</code> as the skyline key points.</p>
<iframe src="https://leetcode.com/playground/ZWK2SePL/shared" frameborder="0" width="100%" height="500" name="ZWK2SePL"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the length of the input array <code>buildings</code>.</p>
<ul>
<li><p>Time complexity: $$O(n\log n)$$</p>
<ul>
<li>Sorting the $$n$$ buildings has an average time complexity of $$O(n \log n)$$, though sorting algorithms vary by language.</li>
<li>There are at most $$2 n$$ unique positions for $$2n$$ edges, and sorting them similarly has an average time complexity of $$O(n \log n)$$.</li>
<li>The <code>UnionFind.union()</code> function has a time complexity of $$O(1)$$ and will run at most $$2n$$ times for an overall time complexity of $$O(n)$$.</li>
<li>The <code>UnionFind.find()</code> function has a time complexity of $$O(n)$$ for the worst-case scenario, but using a collapsing find technique brings this down to $$O(1)$$ with repeated use. This amortizes to an overall time complexity of $$O(n)$$, as each successful <code>find()</code> will update a value in <code>root</code>, and there are up to $$2n$$ elements in <code>root</code>. As shown in the picture below.</li></ul>
<p><img src="https://leetcode.com/articles/Figures/218_re/218_uf_time.png" alt="img" referrerpolicy="no-referrer"></p></li>
<li><p>Space complexity: $$O(n)$$</p>
<ul>
<li>There are at most $$2n$$ edges, thus the set <code>edgeSet</code>, the lists <code>edges</code>, <code>heights</code>, and <code>answers</code>, the union-find's <code>root</code> list, and the recursion stack for the union-find's <code>find()</code> are each limited to $$O(n)$$ space.</li></ul></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach6divideandconquer">Approach 6: Divide-and-Conquer</h4>
<p><strong>Intuition</strong>   </p>
<p>The divide-and-conqueror algorithm is a common algorithmic paradigm based on recursion with three core parts:</p>
<ul>
<li>Divide: Divide the original problem into a number of smaller sub-problems.</li>
<li>Conquer: Solve the sub-problems recursively.</li>
<li>Combine: Merge these sub-problem solutions into a solution for the original problem.</li>
</ul>
<p>For more information on divide-and-conqueror, please refer to the <a href="https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/">LeetCode explore card</a>.</p>
<p>Recall how we sort a list of numbers using merge-sort (divide-and-conqueror):</p>
<ul>
<li>Divide the unsorted list into two roughly even sublists.</li>
<li>Sort each of the sublists recursively.</li>
<li>Merge the sorted sublists back together.</li>
</ul>
<p>Similarly, we can solve this problem using the divide-and-conquer algorithm. </p>
<ul>
<li>Divide the list of buildings into two roughly even sublists.</li>
<li>Get the skyline from each of the sublists recursively.</li>
<li>Merge the two skylines together.</li>
</ul>
<p><img src="https://leetcode.com/articles/Figures/218_re/218_dc_main.png" alt="img" referrerpolicy="no-referrer"></p>
<p>The first step is straightforward as we can simply split the list of buildings into two halves. For the base case in the second step, we can get the skyline from a single building directly. In the third part, two skylines should be merged into one skyline, we would use a much simplier version of sweep line algorithm.</p>
<p>Let's take the following slides as an example.</p>
<p>!?!../Documents/218_re/dc.json:601,401!?!</p>
<blockquote>
  <p>We always compare the heights from both skylines, even if <code>R</code> comes before <code>L</code>, we should also consider the height of <code>L</code> as well. </p>
</blockquote>
<p>Take the picture below as an example: </p>
<p><img src="https://leetcode.com/articles/Figures/218_re/218_dc_background.png" alt="img" referrerpolicy="no-referrer"></p>
<p>In the graphic's first case, <code>R</code> has many skyline points, yet we don't add any of them to our answer, That's because they're "hidden" behind the taller building in <code>L</code>. Hence the merged skyline's height doesn't change unless the current point's height is taller than the current height of the opposite side. In the graphic's second case, for example, we can add a skyline point where the height of <code>R</code> exceeds <code>L</code>.</p>
<p><strong>Algorithm</strong>
1) Recursively divide the current array <code>buildings</code> into two halves.
2) When the recursion reaches the base case of a single building, return the simple skyline.
3) Merge the resulting skylines using a line sweep algorithm moving from left to right.
4) Return the fully merged skyline.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/HoGuzS66/shared" frameborder="0" width="100%" height="500" name="HoGuzS66"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the length of the input array <code>buildings</code>.</p>
<ul>
<li><p>Time complexity: $$O(n\log n)$$</p>
<ul>
<li>During the divide-and-conquer process, we recursively cut the array into two halves, thus $$\log n$$ steps are needed to split the original input array into single buildings and then merge them back together. In other words, the recursion stack has a depth of $$\log n$$ levels.</li>
<li>In each level of the recursion, it takes a total of $$O(n)$$ time to merge all the sub-skylines into larger skylines.</li></ul></li>
<li><p>Space complexity: $$O(n)$$</p>
<ul>
<li>We need $$O(n)$$ space to create the answer array to record the merged skylines as there are at most $$2n$$ skyline key points.</li>
<li>The recursion stack also requires an additional $$O(\log n)$$ space.</li></ul></li>
</ul>
<p><br></p>  
</div>
            