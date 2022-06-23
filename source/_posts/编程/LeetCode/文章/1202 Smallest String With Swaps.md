
---
title: '1202. Smallest String With Swaps'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/1202/Slide1.png'
author: LeetCode
comments: false
date: Sat, 19 Mar 2022 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/1202/Slide1.png'
---

<div>   
<p>You are given a string <code>s</code>, and an array of pairs of indices in the string <code>pairs</code> where <code>pairs[i] = [a, b]</code> indicates 2 indices(0-indexed) of the string.</p>

<p>You can swap the characters at any pair of indices in the given <code>pairs</code> <strong>any number of times</strong>.</p>

<p>Return the lexicographically smallest string that <code>s</code> can be changed to after using the swaps.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "dcab", pairs = [[0,3],[1,2]]
<strong>Output:</strong> "bacd"
<strong>Explaination:</strong> 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "dcab", pairs = [[0,3],[1,2],[0,2]]
<strong>Output:</strong> "abcd"
<strong>Explaination: </strong>
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "cba", pairs = [[0,1],[1,2]]
<strong>Output:</strong> "abc"
<strong>Explaination: </strong>
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= s.length <= 10^5</code></li>
<li><code>0 <= pairs.length <= 10^5</code></li>
<li><code>0 <= pairs[i][0], pairs[i][1] < s.length</code></li>
<li><code>s</code> only contains lower case English letters.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>We have a string of lowercase English letters and some pairs of the form <code>(a, b)</code> where <code>a</code> and <code>b</code>  are indices in the string. Our goal is to find the lexicographically smallest string by swapping the characters at indices <code>a</code> and <code>b</code>. There is no restriction on the maximum number of swaps.</p>
<blockquote>
  <p>Note: The important point to note here is that if we have pairs like <code>(a, b)</code> and <code>(b, c)</code>, then we can swap characters at indices <code>a</code> and <code>c</code>. Although we don't have the pair <code>(a, c)</code>, we can still swap them by first swapping them with the character at index <code>b</code>. Thus, because we can swap the characters at these indices any number of times, we can rearrange the characters <code>a</code>, <code>b</code>, and <code>c</code> into any order.</p>
</blockquote>
<p>This can be depicted as a graph problem. Each index is a vertex and each given pair is an edge between the vertices. An edge implies that we can travel from one vertex to another, or in other words, we can swap them. As shown in the figure below, we have some pairs, and we draw an edge between the two vertices for each pair. If a pair of vertices exists on the same path, then they can be swapped by repeatedly swapping with other vertices in the path between them.</p>
<p><img src="https://leetcode.com/articles/Figures/1202/Slide1.png" alt="fig" referrerpolicy="no-referrer"></p>
<p>This demonstrates how we can swap any pair of vertices present in the same connected component. Thus, we can rearrange the characters such that any character is at any index within the connected component. To find the lexicographically smallest string, we need to sort the characters that correspond to these indices in ascending order and then place the $$i<em>&#123;th&#125;$$ character at the $$i</em>&#123;th&#125;$$ index.</p>
<p>Therefore, we can break the solution down into four steps: build a graph using the given pairs, find the connected components in the graph, sort the characters in each connected component in ascending order, and build the smallest string.</p>
<p>The biggest challenge in solving this problem was figuring out that, with infinite swaps, we can arrange all characters that belong to the same connected component in sorted order. With that hurdle behind us, our next challenge is, how do we find out which indices belong to the same connected component?</p>
<p>DFS, BFS, and Union-Find are each commonly used to find connected components. Since the DFS and BFS solutions are quite similar in implementation, we will only cover DFS and Union-Find in this article. If you would like to learn more about DFS, BFS, or Union-Find, we encourage you to check out the <a href="https://leetcode.com/explore/featured/card/graph/">Graph Explore Card</a>.
<br></p>
<hr>
<h4 id="approach1depthfirstsearchdfs">Approach 1: Depth-First Search (DFS)</h4>
<p><strong>Intuition</strong></p>
<blockquote>
  <p>If you're not familiar with DFS, check out our <a href="https://leetcode.com/explore/featured/card/graph/619/depth-first-search-in-graph/3882/">Explore Card</a>.</p>
</blockquote>
<p>We will build the adjacency list using the pairs given i.e., for each pair <code>(x, y)</code> we will add an edge from <code>x</code> to <code>y</code> and from <code>y</code> to <code>x</code>. Then we will iterate over the indices from <code>0</code> to <code>n-1</code> where <code>n</code> is the length of the given string <code>s</code>. For each index, if it has not been visited yet, we will perform a DFS and store the vertices (index) and the characters at these indices in a list. Each list will represent a different component in the graph. Then we will sort each list of indices and each list of characters and place the $$i<em>&#123;th&#125;$$ character at the $$i</em>&#123;th&#125;$$ index in the string <code>smallestString</code>.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Iterate over the <code>pairs</code> and create an adjacency list such that <code>adj[source]</code> contains all the adjacent vertices of vertex <code>source</code>.</li>
<li>Iterate over the indices from <code>0</code> to <code>s.size() - 1</code>. For each index <code>vertex</code> we will:<ul>
<li>Perform DFS if <code>vertex</code> is not visited yet (<code>visited[vertex]</code> is <code>false</code>)<ul>
<li>While performing DFS, store <code>vertex</code> in the list <code>indices</code> and the character <code>s[vertex]</code> in the list <code>characters</code>.</li></ul></li>
<li>Sort the lists <code>indices</code> and <code>characters</code>.</li>
<li>Iterate over <code>indices</code> and <code>characters</code>, and place the $$i<em>&#123;th&#125;$$ character at the $$i</em>&#123;th&#125;$$ index in the string <code>smallestString</code>.</li></ul></li>
<li>Return <code>smallestString</code>.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/Uy7oGJjK/shared" frameborder="0" width="100%" height="500" name="Uy7oGJjK"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here, $$V$$ represents the number of vertices (the length of the given string) and $$E$$ represents the number of edges (the number of pairs).</p>
<ul>
<li><p>Time complexity: $$O(E + V \log V)$$</p>
<p>Building the adjacency list will take $$O(E)$$ operations, as we iterate over the list of pairs once, and inserting an element into the adjacency list takes $$O(1)$$ time.</p>
<p>During the DFS traversal, each vertex will only be visited once. This is because we mark each vertex as visited as soon as we see it, and then we only visit vertices that are not marked as visited. When we iterate over the edge list of each vertex, we look at each edge once. This has a total cost of $$O(V + E)$$.</p>
<p>Additionally, we also sort the list <code>indices</code> and <code>characters</code> for each component. In the worst case, all of the vertices in the graph belong to the same component. In that case, sorting two lists of $$V$$ elements will take $$O(V \log V)$$ time. Hence the total time complexity is equal to $$O(E + V \log V)$$.</p></li>
<li><p>Space complexity: $$O(E + V)$$</p>
<p>Building the adjacency list will take $$O(E)$$ space. To track the visited vertices, an array <code>visited</code> of size $$O(V)$$ is required. In the worst case, <code>indices</code> and <code>characters</code> can take $$O(V)$$ space. Also, the run-time stack for DFS will use $$O(V)$$ space i.e., one active function call for each vertex.</p>
<p>Additional space is used for sorting the lists  <code>indices</code>  and <code>characters</code>. The space complexity of the sorting algorithm is language-specific. For instance, in Java, the Arrays.sort() for primitives is implemented as a variant of quicksort algorithm whose space complexity is $$O(\log V)$$. In C++ sort() function provided by STL is a hybrid of Quick Sort, Heap Sort, and Insertion Sort and has a worst-case space complexity of $$O(\log V)$$. Thus, using the inbuilt sort() function might add up to $$O(\log V)$$ to space complexity.</p>
<p>The total space required is $$(E + V + \log V)$$ and hence, the space complexity is equal to $$O(E + V)$$.
<br></p></li>
</ul>
<hr>
<h4 id="approach2disjointsetuniondsu">Approach 2: Disjoint Set Union (DSU)</h4>
<p><strong>Intuition</strong></p>
<p>Remember, our first task is to determine which indices belong to the same connected component. In this approach, we will use the Union-Find data structure to accomplish this.</p>
<blockquote>
  <p>If you're not familiar with DSU, check out our <a href="https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3881/">Explore Card</a>.</p>
</blockquote>
<p>First, we will union all vertices that share an edge (vertices <code>a</code> and <code>b</code> share an edge if <code>(a, b)</code> or <code>(b, a)</code> exists in <code>pairs</code>). After which, all vertices with the same root will belong to the same component. This way, by looking at the root node for each vertex, we can put the vertices and the characters at these vertices (indices) in separate lists corresponding to the component they belong to. Then, similar to the previous approach, we will sort the list of characters that belong to the same component and place the $$i<em>&#123;th&#125;$$ character at the $$i</em>&#123;th&#125;$$ index in a string <code>smallestString</code>.</p>
<p>Note that we don't need to sort the list of indices in this approach because, as we iterate over vertices in ascending order, we will store the vertices that belong to the same component in ascending order.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Iterate over the <code>pairs</code>, for each pair <code>(a, b)</code> perform the union operation for vertices <code>a</code> and <code>b</code>.</li>
<li>Iterate over the indices from <code>0</code> to <code>s.size() - 1</code>. For each index (<code>vertex</code>) we will:</li>
</ol>
<ul>
<li>Perform the find operation on <code>vertex</code> to find the <code>root</code>.</li>
<li>Store the <code>vertex</code> in the list corresponding to <code>root</code> in the HashMap <code>rootToComponent</code>.</li>
</ul>
<ol>
<li>Iterate over each list in the HashMap <code>rootToComponent</code>:<ul>
<li>For each list <code>indices</code>, iterate over the list and for each element store the corresponding character in <code>s</code> in the list of characters (<code>characters</code>). Here, each element in <code>indices</code> represents an index in <code>s</code> and each character in <code>characters</code> represents the characters at this index in <code>s</code>.</li></ul></li>
</ol>
<ul>
<li>Sort the list and <code>characters</code>.</li>
<li>Iterate over the lists <code>indices</code> and <code>characters</code>, place the $$i<em>&#123;th&#125;$$ character at the $$i</em>&#123;th&#125;$$ index in the string <code>smallestString</code>.</li>
</ul>
<ol>
<li>Return <code>smallestString</code>.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/fWBm2Q24/shared" frameborder="0" width="100%" height="500" name="fWBm2Q24"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here, $$V$$ represents the number of vertices (the length of the given string) and $$E$$ represents the number of edges (the number of pairs).</p>
<ul>
<li><p>Time complexity: $$O((E + V) \cdot \alpha(V) + V \log V)$$</p>
<p>The amortized time complexity for each union-find operation is $$O(\alpha(V))$$, where $$\alpha$$ is <a href="https://en.wikipedia.org/wiki/Ackermann_function#Inverse">The Inverse Ackermann Function</a>, this is because we have used union by rank as well as path compression in the DSU implementation.</p>
<p>We iterate over each pair and perform the union, which takes $$O(E \cdot \alpha(V))$$ time. Then iterating over each vertex and performing the find operation will take $$O(V \cdot \alpha(V))$$ time.</p>
<p>Additionally, we are sorting the list <code>indices</code> and <code>characters</code> for each component. In the worst case, we can have a connected graph with a single component, and sorting two lists of size $$V$$ will take $$O(V \log V)$$ time.</p>
<p>Hence, the total time complexity is $$O((E + V) \cdot \alpha(V) + V \log V)$$.</p></li>
<li><p>Space complexity: $$O(V)$$</p>
<p>The size of lists <code>root</code>, <code>rank</code> in DSU is $$V$$. The HashMap <code>rootToComponent</code> will contain all the vertices and hence will take $$O(V)$$ space. In the worst case, the lists <code>indices</code> and <code>characters</code> can take $$O(V)$$ space.</p>
<p>Some space will be used for sorting the list <code>indices</code> and string <code>characters</code>. The space complexity of the sorting algorithm depends on the implementation of each programming language. For instance, in Java, the Arrays.sort() for primitives is implemented as a variant of quicksort algorithm whose space complexity is $$O(\log V)$$. In C++ sort() function provided by STL is a hybrid of Quick Sort, Heap Sort, and Insertion Sort and has a worst-case space complexity of $$O(\log V)$$. Thus, the use of the inbuilt sort() function might add up to $$O(\log V)$$ to space complexity.</p>
<p>The total space required is $$(V + \log V)$$ and hence, the space complexity is $$O(V)$$.
<br></p></li>
</ul>
<hr>  
</div>
            