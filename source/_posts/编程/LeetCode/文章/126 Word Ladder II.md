
---
title: '126. Word Ladder II'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/126/126A.png'
author: LeetCode
comments: false
date: Tue, 15 Jun 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/126/126A.png'
---

<div>   
<p>A <strong>transformation sequence</strong> from word <code>beginWord</code> to word <code>endWord</code> using a dictionary <code>wordList</code> is a sequence of words <code>beginWord -> s<sub>1</sub> -> s<sub>2</sub> -> ... -> s<sub>k</sub></code> such that:</p>

<ul>
<li>Every adjacent pair of words differs by a single letter.</li>
<li>Every <code>s<sub>i</sub></code> for <code>1 <= i <= k</code> is in <code>wordList</code>. Note that <code>beginWord</code> does not need to be in <code>wordList</code>.</li>
<li><code>s<sub>k</sub> == endWord</code></li>
</ul>

<p>Given two words, <code>beginWord</code> and <code>endWord</code>, and a dictionary <code>wordList</code>, return <em>all the <strong>shortest transformation sequences</strong> from</em> <code>beginWord</code> <em>to</em> <code>endWord</code><em>, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words </em><code>[beginWord, s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub>]</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
<strong>Output:</strong> [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
<strong>Explanation:</strong> There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
<strong>Output:</strong> []
<strong>Explanation:</strong> The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= beginWord.length <= 5</code></li>
<li><code>endWord.length == beginWord.length</code></li>
<li><code>1 <= wordList.length <= 1000</code></li>
<li><code>wordList[i].length == beginWord.length</code></li>
<li><code>beginWord</code>, <code>endWord</code>, and <code>wordList[i]</code> consist of lowercase English letters.</li>
<li><code>beginWord != endWord</code></li>
<li>All the words in <code>wordList</code> are <strong>unique</strong>.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>This problem is an extension of the problem <a href="https://leetcode.com/problems/word-ladder/">Word Ladder</a>, where we only need to find the minimum number of words in the transformation from <code>beginWord</code> to <code>endWord</code>. Here, we need to find all the transformations that exist between <code>beginWord</code> and <code>endWord</code> that are the minimum length. We can use BFS to find the minimum number of words in the transformation, however, finding all such transformations is tricky because the number of transformations may be enormous.
<br></p>
<hr>
<h4 id="approach1breadthfirstsearchbfsbacktracking">Approach 1: Breadth-First Search (BFS) + Backtracking</h4>
<p><strong>Intuition</strong></p>
<p>The problem can be correlated with the graph data structure. We can represent the words as the vertices and an edge can be used to connect two words which differ by a single letter.</p>
<p>Before diving further let's see how we can find all the direct connections of a particular word. To find the adjacent words for a particular word, one approach is to traverse all of the other words and add an edge for those that differ by a single letter. This approach requires $$O(N\cdot K)$$ time where $N$ is the number of words given and $K$ is the maximum length of a word. The observation behind the optimal approach is that the words only consist of lowercase English letters. Hence we can change each character of the word to all other English lowercase characters and check whether or not that word exists in the <code>wordList</code>(this particular check operation takes $$O(1)$$ in C++ while in Java it will take $$O(K)$$ due to the immutable nature of Strings).This way the number of operations will be $$(25\cdot K*K + 1)$$, hence the time complexity will be $$O(K^2)$$.</p>
<p>Thus we can find all the words that are directly connected.  Now, the task is to find all of the shortest paths from <code>beginWord</code> to <code>endWord</code>. </p>
<p>The naive way to do this is to use backtracking. We will start from <code>beginWord</code>, then traverse all the adjacent words until we reach the <code>endWord</code>. When we reach the <code>endWord</code>, we can compare the path length and find all the paths that have the minimum path length. This method however is extremely inefficient because the number of paths between two vertices can be enormous.</p>
<p>Let's try to optimize our approach. Somehow, we need to reduce the number of traversed paths. Let's say the number of shortest paths that exist between <code>beginWord</code> and <code>endWord</code> is <code>x</code> and the number of paths that we must traverse to find these shortest paths is <code>y</code>. The closer the value <code>y</code> gets to the value <code>x</code>,  the more efficient our approach will be.</p>
<p>The diagram below shows the graph that represents the connectivity among words. As shown in the diagram we want to go from <code>red</code> to <code>tax</code>.  While backtracking on this graph, we will also cover the edges upwards that is from the <code>tad</code> to <code>ted</code> similarly from <code>tex</code> we will traverse to <code>ted</code> as well as <code>rex</code>. The key observation here is that going back in the upward direction will never lead us to the shortest path. We should always traverse the edges in the direction of <code>beginWord</code> to <code>endWord</code>. 
<img src="https://leetcode.com/articles/Figures/126/126A.png" alt="fig" referrerpolicy="no-referrer">
To ensure that we never traverse up the ladder, let's use directed edges to connect the words. The edges in the graph below are all directed towards <code>endWord</code>. Also, notice that graphs produced by BFS do not contain cycles.  Thus, the graph will be a Directed Acyclic Graph (DAG).
<img src="https://leetcode.com/articles/Figures/126/126B.png" alt="fig" referrerpolicy="no-referrer">
Now for the easy part, think of the previous graph as a bunch of layers and observe that once we reach a particular layer we don't want the future words to have the connection back to this layer. We will build our DAG using BFS.  We will then add all the directed edges from the words present in the current layer and once all words in this layer have been traversed, we will remove them from the <code>wordList</code>. This way we will avoid adding any edges that point towards <code>beginWord</code>.</p>
<p>After constructing the graph, we can use our same backtracking approach to find the shortest paths between <code>beginWord</code> and <code>endWord</code>. Also, note that in the graph all paths between <code>beginWord</code> and <code>endWord</code>, obtained through BFS, will be the shortest possible. This is because all the edges in the graph will be directed in the direction of <code>beginWord</code> to <code>endWord</code>.  Furthermore, there will not be any edge between the words that are on the same level.  Therefore, iterating over any edge will bring us one step closer to the <code>endWord</code>, thus there is no need to compare the length of the path each time we reach the <code>endWord</code>.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Store the words present in <code>wordList</code> in an unordered set so that the words can be efficiently removed during the breadth-first search.</p></li>
<li><p>Perform the BFS, and add the edges to the adjacency list <code>adjList</code>. Also once a level is finished remove the <code>visited</code> words from the <code>wordList</code>.</p></li>
<li><p>Start from <code>beginWord</code> and while keep tracking of the current path as <code>currPath</code> traverse all the possible paths, whenever the path leads to the <code>endWord</code> store the path in <code>shortestPaths</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/SedpZWux/shared" frameborder="0" width="100%" height="500" name="SedpZWux"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(NK^2 + α)$$.</p>
<p>Here $$N$$ is the number of words in <code>wordList</code>, $$K$$ is the maximum length of a word, $$α$$ is the number of possible paths from <code>beginWord</code> to <code>endWord</code> in the directed graph we have.</p>
<p>Copying the <code>wordList</code> into the set will take $$&#123;O&#125;(N)$$.</p>
<p>In BFS, every word will be traversed and for each word, we will find the neighbors using the function <code>findNeighbors</code> which has a time complexity of $O(K^2)$. Therefore the total complexity for all the <code>N</code> words will be $O(NK^2)$. Also, each word will be enqueued and will be removed from the set hence it will take $$&#123;O&#125;(N)$$. The total time complexity of BFS will therefore be equal to $O(NK^2 )$.</p>
<p>While backtracking, we will essentially be finding all the paths from <code>beginWord</code> to 
<code>endWord</code>. Thus the time complexity will be equal to $O(α)$.</p>
<p>We can estimate the upper bound for $$α$$ by assuming that every layer except the first and the last layer in the DAG has $$x$$ number of words and is fully connected to the next layer. Let $$h$$ represent the height of the DAG, so the total number of paths will be $$x^h$$ (because we can choose any one word out of $$x$$ words in each layer and each choice will be part of a valid shortest path that leads to the <code>endWord</code>). Here, $$h$$ equals $$(N-2)/x$$. This would result in $$x^&#123;(N-2)/x&#125;$$ total paths, which is maximized when $$x = 2.718$$, which we will round to $$3$$ because $$x$$ must be an integer. Thus the upper bound for $$α$$ is $$3^&#123;(N/3)&#125;$$, however, this is a very loose bound because the nature of this problem precludes the possibility of a DAG where every layer is fully connected to the next layer.</p>
<p>The total time complexity is therefore equal to $$O(NK^2 + α)$$.</p></li>
<li><p>Space complexity: $$&#123;O&#125;(NK)$$.</p>
<p>Here $$N$$ is the Number of words in <code>wordList</code>, $$K$$ is the Maximum length of a word.</p>
<p>Storing the words in a set will take $$&#123;O&#125;(NK)$$ space.</p>
<p>To build the adjacency list $$&#123;O&#125;(N)$$ space is required as the BFS will produce a directed 
graph and hence there will be at max $$(N - 1)$$ edges.</p>
<p>In backtracking, stack space will be consumed which will be equal to the maximum number of active functions in the stack which is equal to the $N$ as the path can have all the words in the <code>wordList</code>. Hence space required is $$&#123;O&#125;(N)$$.</p>
<p>The total space complexity is therefore equal to $$&#123;O&#125;(NK)$$.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2bidirectionalbreadthfirstsearchbfsbacktracking">Approach 2: Bidirectional Breadth-First Search (BFS) + Backtracking</h4>
<p><strong>Intuition</strong></p>
<p>This approach is very similar to the previous one in that both approaches will use the same Directed Acyclic Graph (DAG). The difference lies in the way that the graph is produced, which is better optimized in this case.</p>
<p>In the previous solution, we performed BFS starting from <code>beginWord</code> and explored down the ladder until we reached <code>endWord</code>.  However, now we will start from <code>beginWord</code> stored in <code>forwardQueue</code> and from <code>endWord</code> stored in <code>backwardQueue</code> and explore towards the middle of the ladder. At each iteration, we will connect the words to their neighbors, which we will find using <code>findNeighbors</code>. At each iteration, we will have two options, either to connect edges using the<code>forwardQueue</code> or by using the <code>backwardQueue</code>. The optimal choice is to use the queue that contains fewer words. In this solution, for simplicity, we will swap <code>forwardQueue</code> and <code>backwardQueue</code> whenever <code>forwardQueue</code> is larger.  In doing so, we will always choose the <code>forwardQueue</code>.</p>
<p>We will traverse the <code>forwardQueue</code> find the neighbors of each of the words present using <code>findNeighbors</code> and add the edge to the <code>adjList</code>.  We will also store the next layer words in the <code>visited</code> list. Once a level is finished we can assign the <code>forwardQueue</code> to <code>visited</code>.  We will repeat this process until either the size of <code>forwardQueue</code> becomes zero, signifying that there is no valid sequence from <code>beginWord</code> to <code>endWord</code>, or until the contents of <code>forwardQueue</code> and <code>backwardQueue</code> overlap.  The reason for stopping when <code>forwardQueue</code> and <code>backwardQueue</code> overlap is because after completing this level, it is guaranteed that <code>beginWord</code> and <code>endWord</code> will be connected by at least one sequence that that passes through the words that exist in both queues.  Thus, the DAG will be completed.</p>
<p>The remaining process is the same as Approach 1, once the queue has been traversed, at each iteration, we will remove those words from the <code>wordList</code> to avoid including any edges to previous layers. Once the graph is complete, we will use backtracking to find all of the paths between <code>beginWord</code>and <code>endWord</code>.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Store the words present in <code>wordList</code> in an unordered set so that the words can be efficiently removed during the breadth-first search.</p></li>
<li><p>Perform a bidirectional BFS.  Initialize two queues, <code>forwardQueue</code> with <code>beginWord</code> and <code>backwardQueue</code> with <code>endWord</code>. At each iteration add the edges to the adjacency list <code>adjList</code> by extending the shorter queue. The parameter <code>direction</code> is used to decide in which direction the edges should be connected, where <code>1</code> indicates towards <code>endWord</code> (down the ladder) and vice versa. Also once a level is finished, remove the <code>forwardQueue</code> words from the <code>wordList</code>.</p></li>
<li><p>If a sequence connecting <code>beginWord</code> to <code>endWord</code> does not exist, return an empty list. Otherwise, start from <code>beginWord</code> and while keeping track of the current path as <code>currPath</code> traverse all the possible paths, whenever the path leads to the <code>endWord</code> store the path in <code>shortestPaths</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/9qoB7yfc/shared" frameborder="0" width="100%" height="500" name="9qoB7yfc"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(NK^2 + α)$$.</p>
<p>Here $$N$$ is the Number of words in <code>wordList</code>, $$K$$ is the maximum length of a word, $$α$$ is the Number of possible paths from <code>beginWord</code> to <code>endWord</code> in the directed graph we have.</p>
<p>Copying the <code>wordList</code> into the set will take $$&#123;O&#125;(N)$$.</p>
<p>In the worst-case scenario, the number of operations in the bidirectional BFS will be equal to the BFS approach discussed before. However, in some cases, this approach will perform better because the search space is reduced by selecting the shorter queue at each iteration.   In bidirectional BFS, at most, every word will be traversed once, and for each word, we will find the neighbors using the function <code>findNeighbors</code> which has a time complexity of $O(K^2)$. Therefore the total complexity for all the <code>N</code> words will be $O(NK^2)$. Also, each word will be enqueued and will be removed from the set which will take $$&#123;O&#125;(N)$$. Thus, the total time complexity of bidirectional BFS will be $O(NK^2)$.</p>
<p>In the backtracking process, we will essentially find all of the paths from <code>beginWord</code> to <code>endWord</code>. Thus, the time complexity is equal to $O(α)$.</p>
<p>We can estimate the upper bound for $$α$$ by assuming that every layer except the first and the last layer in the DAG has $$x$$ number of words and is fully connected to the next layer. Let $$h$$ represent the height of the DAG, so the total number of paths will be $$x^h$$ (because we can choose any one word out of $$x$$ words in each layer and each choice will be part of a valid shortest path that leads to the <code>endWord</code>). Here, $$h$$ equals $$(N-2)/x$$. This would result in $$x^&#123;(N-2)/x&#125;$$ total paths, which is maximized when $$x = 2.718$$, which we will round to $$3$$ because $$x$$ must be an integer. Thus the upper bound for $$α$$ is $$3^&#123;(N/3)&#125;$$, however, this is a very loose bound because the nature of this problem precludes the possibility of a DAG where every layer is fully connected to the next layer.</p>
<p>The total time complexity is therefore equal to $$O(NK^2 + α)$$.</p></li>
<li><p>Space complexity: $$&#123;O&#125;(NK)$$.</p>
<p>Here $$N$$ is the Number of words in <code>wordList</code>, $$K$$ is the Maximum length of a word.</p>
<p>Storing the words in a set will take $$&#123;O&#125;(NK)$$ space.</p>
<p>To build the adjacency list $$&#123;O&#125;(N)$$ space is required as the BFS will produce a directed graph and hence there will be at most $$(N - 1)$$ edges. Also, in the worst-case scenario, the combined size of both queues will be equal to $$N$$.</p>
<p>In backtracking, stack space will be consumed which will be equal to the maximum number of active functions in the stack, which is equal to the $N$ as the path can have all the words in the <code>wordList</code>. Hence the space required is $$&#123;O&#125;(N)$$.</p>
<p>The total space complexity is therefore equal to $$&#123;O&#125;(NK)$$.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            