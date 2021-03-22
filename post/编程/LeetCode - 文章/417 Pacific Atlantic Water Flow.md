
---
title: 417. Pacific Atlantic Water Flow
categories: 
    - 编程
    - LeetCode - 文章
author: LeetCode - 文章
comments: false
date: Mon, 01 Mar 2021 00:00:00 GMT
thumbnail: ''
---

<div>   
<p>Given an <code>m x n</code> matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.</p>

<p>Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.</p>

<p>Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.</p>

<p><b>Note:</b></p>

<ol>
<li>The order of returned grid coordinates does not matter.</li>
<li>Both <i>m</i> and <i>n</i> are less than 150.</li>
</ol>

<p> </p>

<p><b>Example:</b></p>

<pre>Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
</pre>

<p> </p><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>Matrices such as this one are a type of <strong>graph</strong> representation. Standard graph traversal algorithms such as BFS and DFS can be used to solve this problem. If you aren't familiar with these algorithms, check out the <a href="https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/">Explore Card on BFS</a>.</p>
<p>The naive approach would be to check every cell - that is, iterate through every cell, and at each one, start a traversal that follows the problem's conditions. That is, find every cell that manages to reach both oceans.</p>
<p>This approach, however, is extremely slow, as it repeats a ton of computation. Instead of looking for every path from cell to ocean, let's start at the oceans and try to work our way to the cells. This will be much faster because when we start a traversal at a cell, whatever result we end up with can be applied to only that cell. However, when we start from the ocean and work backwards, we already know that every cell we visit must be connected to the ocean.</p>
<p><br></p>
<hr>
<h4 id="approach1breadthfirstsearchbfs">Approach 1: Breadth First Search (BFS)</h4>
<p><strong>Intuition</strong></p>
<p>If we start traversing from the ocean and flip the condition (check for higher height instead of lower height), then we know that every cell we visit during the traversal can flow into that ocean. Let's start a BFS traversal from every cell that is immediately beside the Pacific ocean, and figure out what cells can flow into the Pacific. Then, let's do the exact same thing with the Atlantic ocean. At the end, the cells that end up connected to both oceans will be our answer.</p>
<p>!?!../Documents/417<em>Pacific</em>Atlantic.json:960,540!?!</p>
<p><br></p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>If the input is empty, immediately return an empty array.</p></li>
<li><p>Initialize variables that we will use to solve the problem:</p>
<ul>
<li>Number of rows and columns in our matrix;</li>
<li>2 queues, one for the Atlantic Ocean and one for the Pacific Ocean that will be used for BFS;</li>
<li>2 data structures, again one for each ocean, that we'll use to keep track of cells we already visited, to avoid infinite loops;</li>
<li>A small array <code>[(0, 1), (1, 0), (-1, 0), (0, -1)]</code> that will help with BFS.</li></ul></li>
<li><p>Figure out all the cells that are adjacent to each ocean, and fill the respective data structures with them.</p></li>
<li><p>Perform BFS from each ocean. The data structure used to keep track of cells already visited has a double purpose - it also
contains every cell that can flow into that ocean.</p></li>
<li><p>Find the intersection, that is all cells that can flow into both oceans.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<p>Putting it all together for the final solution:</p>
<iframe src="https://leetcode.com/playground/bfE7YkW4/shared" frameborder="0" width="100%" height="500" name="bfE7YkW4"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(M \cdot N)$$, where $$M$$ is the number of rows and $$N$$ is the number of columns.</p>
<p>In the worst case, such as a matrix where every value is equal, we would visit every cell twice. This is because we perform 2 traversals, and during each traversal, we visit each cell exactly once. There are $$M \cdot N$$ cells total, which gives us a time complexity of $$O(2 \cdot M \cdot N) = O(M \cdot N)$$.</p></li>
<li><p>Space complexity: $$O(M \cdot N)$$, where $$M$$ is the number of rows and $$N$$ is the number of columns.</p>
<p>The extra space we use comes from our queues, and the data structure we use to keep track of what cells have been visited. Similar to the time complexity, for a given ocean, the amount of space we will use scales linearly with the number of cells. For example, in the Java implementation, to keep track of what cells have been visited, we simply used 2 matrices that have the same dimensions as the input matrix.</p>
<p>The same logic follows for the queues - we can't have more cells in the queue than there are cells in the matrix!</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2depthfirstsearchdfs">Approach 2: Depth First Search (DFS)</h4>
<p>Intuitively, BFS makes more sense for this problem since water flows in the same manner. However, we can also use DFS, and it doesn't really make much of a difference. So, if you prefer DFS, then that's perfectly fine for this problem. Additionally, it's possible that your interviewer will ask you to implement the problem recursively instead of iteratively. Recursion must be DFS, not BFS.</p>
<p><strong>Algorithm</strong></p>
<p>DFS is very similar to BFS. Instead of using a queue and working iteratively, we'll use recursion. Our <code>dfs</code> method will be called for every reachable cell. Note: we could also work iteratively with DFS, in which case we would simply use a stack instead of a queue like in the Approach 1 code, with mostly everything else being identical to the BFS approach.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/VioDJwZV/shared" frameborder="0" width="100%" height="500" name="VioDJwZV"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(M \cdot N)$$, where $$M$$ is the number of rows and $$N$$ is the number of columns.</p>
<p>Similar to approach 1. The <code>dfs</code> function runs exactly once for each cell accessible from an ocean.</p></li>
<li><p>Space complexity: $$O(M \cdot N)$$, where $$M$$ is the number of rows and $$N$$ is the number of columns.</p>
<p>Similar to approach 1. Space that was used by our queues is now occupied by <code>dfs</code> calls on the recursion stack.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            