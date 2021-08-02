
---
title: '36. Valid Sudoku'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png'
author: LeetCode
comments: false
date: Mon, 26 Jul 2021 00:00:00 GMT
thumbnail: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png'
---

<div>   
<p>Determine if a <code>9 x 9</code> Sudoku board is valid. Only the filled cells need to be validated <strong>according to the following rules</strong>:</p>

<ol>
<li>Each row must contain the digits <code>1-9</code> without repetition.</li>
<li>Each column must contain the digits <code>1-9</code> without repetition.</li>
<li>Each of the nine <code>3 x 3</code> sub-boxes of the grid must contain the digits <code>1-9</code> without repetition.</li>
</ol>

<p><strong>Note:</strong></p>

<ul>
<li>A Sudoku board (partially filled) could be valid but is not necessarily solvable.</li>
<li>Only the filled cells need to be validated according to the mentioned rules.</li>
</ul>

<p> </p>
<p><strong>Example 1:</strong></p>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height:250px; width:250px" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
<strong>Output:</strong> false
<strong>Explanation:</strong> Same as Example 1, except with the <strong>5</strong> in the top left corner being modified to <strong>8</strong>. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>board.length == 9</code></li>
<li><code>board[i].length == 9</code></li>
<li><code>board[i][j]</code> is a digit or <code>'.'</code>.</li>
</ul><p>[TOC]</p>
<h2 id="overview">Overview</h2>
<p>A valid sudoku board should satisfy three conditions: (1) each row, (2) each column, and (3) each box has no duplicate numbers.</p>
<p>For instance, in example 1 from the problem description, for <code>board[2][1] = 9</code>, we need to check the following conditions.</p>
<p><img src="https://leetcode.com/articles/Figures/36/Example_1.jpg" alt="example_1" referrerpolicy="no-referrer"></p>
<ol>
<li><p>Does number 9 appear more than once in the third row?</p></li>
<li><p>Does number 9 appear more than once in the second column?</p></li>
<li><p>Does number 9 appear more than once in the first box?</p></li>
</ol>
<p>In order to check 9 rows, 9 columns, and 9 boxes, we need to distinguish each of these entities.
It is comparatively intuitive to check for duplicates in each row and column, given the row index <code>r</code> and column index <code>c</code>.</p>
<p>We can create a hash set for each row. For <code>board[r][c]</code>, we check if the number already exists in the hash set corresponding to $$r^&#123;th&#125;$$ row. If yes, this row contains a duplicate value, therefore the sudoku is not valid. Otherwise, we will proceed to check the next position until we finish scanning the whole sudoku board. The same logic can be applied to each column.</p>
<p>The tricky part is when we check the validity of each box. The question is, given row index <code>r</code> and column index <code>c</code>, how to assign the position to one of the 9 boxes correctly?
The first observation is that, in each column, rows 0, 1, and 2 belong to the same box, as do rows 3, 4, and 5, and rows 6, 7, and 8.</p>
<p>What do they have in common? Every group of three belonging to the same box has the same outcome when we perform integer division by three. Therefore, we can use <code>r/3</code> (<code>/</code> signifies floor division) to ensure that the rows are grouped as expected and use <code>c/3</code> to ensure that the columns are grouped correctly. Then, <code>(r/3, c/3)</code> can uniquely mark each box, and we can directly use the tuple as the hash key if we want to create a hash set for each box.</p>
<p>Alternatively, we can use the numbers  0 through 8 to represent these boxes, where <code>(r/3) * 3 + (c/3)</code> is used calculate a number in the range from 0 to 8. I.e. the square located at <code>(r, c)</code> belongs to the box <code>(r/3) * 3 + (c/3)</code>.</p>
<p>!?!../Documents/36/36<em>subsqare</em>definitions.json:960,680!?!</p>
<p>Notice that reading from left to right, the box indices are continuous from 0 to 8, and will increase by column first.</p>
<p>For each row, column, and box, there are several ways to store which numbers have already appeared so far. Here are three that we will use in this article:</p>
<ol>
<li>Create a hash set for each row, column, and box (see Approach 1 for illustration).</li>
<li>Create an array of length 9 with values 0 and 1 representing "not seen" and "previously seen" states, respectively (see Approach 2 for illustration).</li>
<li>Use a binary number with a value 0 or 1 at each position representing the previous occurrence of each number (see Approach 3 for illustration).</li>
</ol>
<p>Many problems can be solved using hash sets, arrays, or binary numbers to record previously seen numbers, and below, we will show how each of these methods can be used to help check the validity of a sudoku board.</p>
<blockquote>
  <p>After solving this problem, you can practice the above techniques on a similar problem (<a href="https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/">Find Winner on a Tic Tac Toe Game</a>) or try a more advanced follow-up problem (<a href="https://leetcode.com/problems/sudoku-solver/">Sudoku Solver</a>).</p>
</blockquote>
<p><br></p>
<hr>
<h4 id="approach1hashset">Approach 1: Hash Set</h4>
<p><strong>Intuition</strong></p>
<p>In a valid sudoku puzzle, each row, column, and box contains digits in the range from 1 through 9 without repetition. To check if the sudoku is valid, for each number, we must check if that number is repeated anywhere in the same row, column, or box. However, it would be very inefficient to read the entire row, column, and box every time we check if a number is a duplicate. Instead, as we are iterating over the numbers in the sudoku, we can use hash sets to store the previously seen numbers in each row, column, and box. Via hash sets, we can determine if the current number already exists in the corresponding row, column, or box in constant time. An example of this process is shown below.</p>
<p>!?!../Documents/36/36<em>method1</em>hashset.json:960,680!?!</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize a list containing 9 hash sets, where the hash set at index <code>r</code> will be used to store previously seen numbers in row <code>r</code> of the sudoku. Likewise, initialize lists of 9 hash sets to track the columns and boxes too.</p></li>
<li><p>Iterate over each position <code>(r, c)</code> in the sudoku. At each iteration, if there is a number at the current position:</p>
<ul>
<li><p>Check if the number exists in the hash set for the current row, column, or box. If it does, return <code>false</code>, because this is the second occurrence of the number in the current row, column, or box.</p></li>
<li><p>Otherwise, update the set responsible for tracking previously seen numbers in the current row, column, and box. The index of the current box is <code>(r / 3) * 3 + (c / 3)</code> where <code>/</code> represents floor division.</p></li></ul></li>
<li><p>If no duplicates were found after every position on the sudoku board has been visited, then the sudoku is valid, so return <code>true</code>.</p></li>
</ol>
<iframe src="https://leetcode.com/playground/ak2r6EHE/shared" frameborder="0" width="100%" height="500" name="ak2r6EHE"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the board length, which is 9 in this question. Note that since the value of $$N$$ is fixed, the time and space complexity of this algorithm can be interpreted as $$O(1)$$.  However, to better compare each of the presented approaches, we will treat $$N$$ as an arbitrary value in the complexity analysis below.</p>
<ul>
<li><p>Time complexity: $$O(N^2)$$ because we need to traverse every position in the board, and each of the four check steps is an $$O(1)$$ operation.</p></li>
<li><p>Space complexity: $$O(N^2)$$ because in the worst-case scenario, if the board is full, we need a hash set each with size <code>N</code> to store all seen numbers for each of the <code>N</code> rows, <code>N</code> columns, and <code>N</code> boxes, respectively.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2arrayoffixedlength">Approach 2: Array of Fixed Length</h4>
<p><strong>Intuition</strong></p>
<p>Apart from using a hash set, we can also use an array of fixed length to check for duplicates. Each position (<code>pos</code>) in the array represents the status of the number <code>pos + 1</code>. Therefore, we can determine if we have already seen some number in constant time. We need an array for each row, column, and box. This approach is a mental stepping stone for Approach 3 where bitmasking is used.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize an array of size <code>N</code> filled with zeros for each row, column, and box, where <code>N</code> is the sudoku board length, which is 9 in this case.</p></li>
<li><p>Iterate over each position <code>(r, c)</code> in the sudoku. At each iteration, if there is a number at the current position:</p>
<ul>
<li><p>Check if the number <code>n</code> has been previously seen by checking the $$n-1^&#123;th&#125;$$ index in the array. If the value at this index equals to 1, it means that we have already seen this number, so the sudoku is not valid. We return <code>false</code> in this case.</p></li>
<li><p>Otherwise, if the value at this position equals 0, then it is the first time encountering this number, so we update the value at this position to 1 to mark that we have seen this number.</p></li></ul></li>
<li><p>Once every position on the sudoku board is checked, with no duplicates found, we will return <code>true</code>.</p></li>
</ol>
<p>Let's take the leftmost column in the sudoku shown below as an example.</p>
<p>!?!../Documents/36/36<em>method2</em>array.json:960,680!?!</p>
<iframe src="https://leetcode.com/playground/DMaDigHW/shared" frameborder="0" width="100%" height="500" name="DMaDigHW"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the board length, which is 9 in this question. Note that since the value of $$N$$ is fixed, the time and space complexity of this algorithm can be interpreted as $$O(1)$$.  However, to better compare each of the presented approaches, we will treat $$N$$ as an arbitrary value in the complexity analysis below.</p>
<ul>
<li><p>Time complexity: $$O(N^2)$$ because we need to traverse every position in the board, and each of the four check steps is an $$O(1)$$ operation.</p></li>
<li><p>Space complexity: $$O(N^2)$$ because we need to create <code>3N</code> arrays each with size <code>N</code> to store all previously seen numbers for all rows, columns, and boxes.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3bitmasking">Approach 3: Bitmasking</h4>
<p><strong>Intuition</strong></p>
<p>In Approach 2 we showed how we can use values at different positions of an array to mark whether the number corresponding to each position has been seen or not. Each position in the array can take a value of 0 or 1, which can be represented by a single bit. Therefore, we can improve on the space complexity by using bitmasking.</p>
<p>To recap, for a binary number, each bit can take a value of 0 or 1. We can use a binary number with 9 digits to represent whether numbers 1 through 9 have been visited or not. Now the question is, "how do we set a bit to 1 when a number is seen and how do we check if a bit is already set to 1?"
Let's first review the two most commonly used operations for <code>get</code> and <code>set</code> in bitmasking. Such operations on bits are commonly referred to as bitwise operations.</p>
<ol>
<li>Check if the $$i^&#123;th&#125;$$ bit of a binary number is set to 1: <code>x & (1 << i)</code>. If this expression evaluates to <code>0</code>, the bit is not set.  Let's elaborate on how this works:</li>
</ol>
<ul>
<li><p><code>1 << i</code> means the number 1 is bit shifted to the left <code>i</code> times.  For example, <code>1 << 2</code> changes the number 1 (<code>'0001'</code>) to the number 4 (<code>'0100'</code>).  Notice that in the binary representation, the 1 is shifted two places to the left.</p></li>
<li><p>Bitwise AND (<code>&</code>) returns only the bits that are set in both the left <strong>and</strong> right operand.  For example, <code>5 & 4 = '0101' & '0100' = '0100' = 4</code>.  Notice that in the binary representation, the only remaining set bit is the bit that was set in both numbers.  One more example for clarity, <code>10 & 4 = '1010' & '0100' = '0000' = 0</code>. When two numbers do not share any set bits, bitwise AND returns 0, otherwise, it will return a nonzero value.  This is why we can use bitwise AND to check if the $$i^&#123;th&#125;$$ bit from the right has been set.  </p></li>
</ul>
<ol>
<li>Set the $$i^&#123;th&#125;$$ bit of a binary number <code>x</code> to 1: <code>x = x | (1 << i)</code></li>
</ol>
<ul>
<li>Bitwise OR (<code>|</code>) returns the bits that are set in the left <strong>or</strong> right operand. For example, <code>10 | 4 = '1010' | '0100' = '1110' = 14</code>.  Notice that the third bit from the right has been set (changed from 0 to 1).  This is why we can use <code>x = x | (1 << i)</code> to set the $$i^&#123;th&#125;$$ bit from the right in the integer <code>x</code>.</li>
</ul>
<blockquote>
  <p>Here we use 9 bits to represent numbers 1 to 9. You might wonder, if these numbers are not continuous, can we still use bitmasking to represent the presence or absence of each number? The answer is yes. For instance, if we know upfront that the possible discrete values are <code>[1, 9, 10, 100]</code> (any small set of possible values), we can use a hashmap <code>&#123;1:0, 9:1, 10:2, 100:3&#125;</code> to track the correspondence between possible values and positions in the binary number. So, we can use a 4-digit binary number to represent the status of each number in <code>[1, 9, 10, 100]</code>, even though these numbers are not continuous.</p>
  <p>To better understand bit manipulation, you may check out this post (<a href="https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently">A summary: how to use bit manipulation to solve problems easily and efficiently</a>) by @LHearen.</p>
</blockquote>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Use an integer for each row, column, and box to track which numbers have been previously seen. The $$i^&#123;th&#125;$$ bit from the right marks the previous occurrence of the number <code>i</code>. For example, <code>'000001010'</code> signifies the numbers 2 and 4 have been previously seen.</p></li>
<li><p>Iterate over each position <code>(r, c)</code> in the sudoku board. At each iteration, if there is a number at the current position:</p>
<ul>
<li><p>Use <code>x & (1 << i)</code> to check if we have seen the number <code>i + 1</code> previously. If <code>x & (1 << i)</code> is nonzero, then the number <code>i + 1</code> is a duplicate and the sudoku is not valid.</p></li>
<li><p>Otherwise, we haven't seen this number before, and we will use <code>x | (1 << i)</code> to set the $$i^&#123;th&#125;$$ bit from the right to signify the number <code>i + 1</code> has been seen.</p></li></ul></li>
<li><p>Once every position on the sudoku board has been checked, if no duplicates were found, we return <code>true</code>.</p></li>
</ol>
<p>Let's take the upper-left box as an example.</p>
<p>!?!../Documents/36/36<em>method3</em>binary.json:960,680!?!</p>
<iframe src="https://leetcode.com/playground/JfaaNSLw/shared" frameborder="0" width="100%" height="500" name="JfaaNSLw"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the board length, which is 9 in this question. Note that since the value of $$N$$ is fixed, the time and space complexity of this algorithm can be interpreted as $$O(1)$$.  However, to better compare each of the presented approaches, we will treat $$N$$ as an arbitrary value in the complexity analysis below.</p>
<ul>
<li><p>Time complexity: $$O(N^2)$$ because we need to traverse every position in the board, and each of the four check steps is an $$O(1)$$ operation.</p></li>
<li><p>Space complexity: $$O(N)$$ because in the worst-case scenario, if the board is full, we need <code>3N</code> binary numbers to store all seen numbers in all rows, columns, and boxes. Using a binary number to record the occurrence of numbers is probably the most space-efficient method.</p></li>
</ul>  
</div>
            