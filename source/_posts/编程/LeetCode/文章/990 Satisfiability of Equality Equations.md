
---
title: '990. Satisfiability of Equality Equations'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Documents/990/990_example.drawio.svg'
author: LeetCode
comments: false
date: Mon, 08 Aug 2022 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Documents/990/990_example.drawio.svg'
---

<div>   
<p>You are given an array of strings <code>equations</code> that represent relationships between variables where each string <code>equations[i]</code> is of length <code>4</code> and takes one of two different forms: <code>"x<sub>i</sub>==y<sub>i</sub>"</code> or <code>"x<sub>i</sub>!=y<sub>i</sub>"</code>.Here, <code>x<sub>i</sub></code> and <code>y<sub>i</sub></code> are lowercase letters (not necessarily different) that represent one-letter variable names.</p>

<p>Return <code>true</code><em> if it is possible to assign integers to variable names so as to satisfy all the given equations, or </em><code>false</code><em> otherwise</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> equations = ["a==b","b!=a"]
<strong>Output:</strong> false
<strong>Explanation:</strong> If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> equations = ["b==a","a==b"]
<strong>Output:</strong> true
<strong>Explanation:</strong> We could assign a = 1 and b = 1 to satisfy both equations.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= equations.length <= 500</code></li>
<li><code>equations[i].length == 4</code></li>
<li><code>equations[i][0]</code> is a lowercase letter.</li>
<li><code>equations[i][1]</code> is either <code>'='</code> or <code>'!'</code>.</li>
<li><code>equations[i][2]</code> is <code>'='</code>.</li>
<li><code>equations[i][3]</code> is a lowercase letter.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>Recall the problem description and the property of relationship <code>==</code>:</p>
<ul>
<li><strong>reflective</strong>: <code>a==a</code> must hold for all variable <code>a</code>.</li>
<li><strong>symmetric</strong>: if <code>a==b</code> holds, then we have <code>b==a</code>.</li>
<li><strong>transtive</strong>: if <code>a==b</code> and <code>b==c</code>, then we have <code>a==c</code>.</li>
</ul>
<p>Therefore, if we can build an undirected graph based on the <code>==</code> relationship among all variables by adding an edge between <code>a</code> and <code>b</code> if we have <code>a==b</code> in <code>equations</code>, then all variables, which are represented as vertices in the graph, that can reach from each other must have a relationship of <code>==</code>. In other words, all variables in a common <strong>connected components</strong> must share the same value. </p>
<p>For example, assume that we have the following equations:</p>
<pre><code>a==b
c==a
c==d
e==f
</code></pre>
<p>A graph can be built as below:</p>
<p><img src="https://leetcode.com/articles/Documents/990/990_example.drawio.svg" alt="Every <code>==</code> plays a role of an edge in the graph, the variables that in the same connected components (in the same color) are equal to each other" referrerpolicy="no-referrer"></p>
<p>Now, it is clear that the key challenge to solving this problem is how to figure out all connected components exactly in the graph above. Once it finishes, we can easily enumerate all equations in the form of <code>x!=y</code> to check if there is any contradiction showing that <code>x</code> and <code>y</code> are indeed in the same connected components in that graph. If no such contradiction, all the given equations can be satisfied; otherwise, no possible values can be assigned to them. </p>
<p>In this solution, we provide the following two approaches to achieve the goal of obtaining all connected components correctly: the first approach is to perform a depth-first search and color all visited variables in each round of traversal starting from a given variable; the second approach is to maintain a union-find data structure to manage all known connected components so far.</p>
<h4 id="approach1depthfirstsearchdfs">Approach 1: Depth-first Search (DFS)</h4>
<p><strong>Intuition</strong></p>
<p>Recall how we build a graph based on <code>==</code> relationship between variables.After obtaining the graph in an adjacency list form, we can do one pass of <strong>depth-first search</strong> (see <a href="https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/">this explore card</a>) from any vertice, and all visited vertices are in the same connected component with the starting vertice. Thus, they are marked with the same color, and we can check if two vertices are in the same connected component by querying their colors.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Build an undirected graph based on <code>==</code> relationship as what we discussed in Overview.</li>
<li>Initialize all variables as uncolored.</li>
<li>When there is still any uncolored variable in the graph, pick any of them to denote as <code>node</code> and choose a unique color <code>c</code>. </li>
<li>Do a depth-first search starting from <code>node</code>, color all traversed variables during this pass with c. Repeat step 3 until there is no uncolored variables.</li>
<li>Enumerate all statements of the form <code>x!=y</code>, check if any <code>x</code> and <code>y</code> in a statement are in the same color. If so, we say they can't be equal. It is impossible to satisfy the equations, then return false.</li>
<li>Otherwise, all <code>x</code>s and <code>y</code>s are in different colors, our coloring demonstrates a way to satisfy the equations, and thus the result is true.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/W7rehqgn/shared" frameborder="0" width="100%" height="500" name="W7rehqgn"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity:  $$O(\max(N,|\Sigma|))$$ where $$N$$ is the length of <code>equations</code> and $$\Sigma$$ is the alphabet set of variables and $$|\Sigma|$$ refers to its size. Since $$\Sigma$$ is limited to the space of only 26 lowercase letters in this problem, we regard $$|\Sigma|$$ as 26 and the final time complexity as $$O(N)$$.</p></li>
<li><p>Space Complexity:  $$O(\max(N,|\Sigma|))$$, though the variables are restricted to $$\Sigma$$, we may still include the duplicated vertices when building the adjacency list <code>graph</code>. As we discussed before, $$|\Sigma|$$ is fixed and small, so the time complexity is also $$O(N)$$.  However, we can reduce it to $$O(|\Sigma|)$$ (i.e., $$O(1)$$) if we apply a hash set instead of a list as <code>graph[i]</code> to guarantee all vertices in <code>graph[i]</code> are unique.</p></li>
</ul>
<p><br>
<br></p>
<hr>
<h4 id="approach2unionfind">Approach 2: Union-find</h4>
<p><strong>Intuition</strong></p>
<p>Union-find, or disjoint-set (see <a href="https://leetcode.com/explore/learn/card/graph/618/disjoint-set/">this explore card</a>), is also a popular approach to maintain the connected relationship in a graph we build as what we discuss in Overview. We can build this data structure during the enumeration of all <code>==</code> equations. Instead of searching after building the entire graph like approach 1, we handle the each <code>==</code> relationship on the fly, which provides a smaller constant in the time complexity, especially when we compress paths and merge those components in an optimal way. Similar to approach 1, after obtaining the union-find data structure that contains the information of all connected components, we check if any contradiction occurs and get the final result.</p>
<p><strong>Algorithm</strong></p>
<p>Similar to Approach 1, starting with a union-find data structure that sets all roots of the variables to themselves, we first pick all equations in the form of <code>x==y</code> and perform the union operation between variable <code>x</code> and <code>y</code>, which actually merge the connected components which <code>x</code> and <code>y</code> belong to respectively. Instead of searching after building the entire graph, we handle the each <code>==</code> relationship on the fly, which provides a smaller constant in the time complexity especially when we compress paths and merge those components in an optimal way.</p>
<ol>
<li>Initialize a union-find data structure that sets all roots of the variables to themselves. All variables are isolated now.</li>
<li>Similar to approach 1, enumerate all equations in the form of <code>x==y</code> and perform the <em>union</em> operation between variable <code>x</code> and <code>y</code>,  which actually <strong>merges</strong> the connected components that <code>x</code> and <code>y</code> belong to respectively.</li>
<li>Enumerate all equations in the form of <code>x!=y</code> by <em>find</em> query to see if <code>x</code> and <code>y</code> are in the same connected component. If they are, we return <code>false</code> immediately. If all those equations can pass, we return <code>true</code>.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/3BVfLyFV/shared" frameborder="0" width="100%" height="500" name="3BVfLyFV"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(N\log |\Sigma|)$$, the time complexity of performing $$m$$-length sequence of <code>find</code> or <code>union</code> operations on $$n$$ vertices with path compression is $$O(m\log n)$$. However, for this problem, $$|\Sigma|$$ is only 26, as we discussed before. Thus, the overall time complexity is just $$O(N\log 26) = O(N)$$ as we invoke <code>find</code> or <code>union</code> methods to upper $$O(N)$$ times.</p></li>
<li><p>Space complexity: $$O(|\Sigma|)$$, only a <code>root</code> array of alphabet size is introduced as extra space here. Similar, it is actually $$O(1)$$ because $$|\Sigma|=26$$.</p></li>
</ul>  
</div>
            