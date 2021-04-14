
---
title: '204. Count Primes'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/204/img1.png'
author: LeetCode
comments: false
date: Tue, 13 Apr 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/204/img1.png'
---

<div>   
<p>Count the number of prime numbers less than a non-negative number, <code>n</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>0 <= n <= 5 * 10<sup>6</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>The basic brute-force solution for this problem is to iterate from <code>0</code> to <code>n</code> and for each number, we do a prime-check. To check if a number is prime or not, we simply check if its divisors include anything other than <code>1</code> and the number itself. If so, then it is not a prime number. This method will not scale for the given limits on <code>n</code>. The iteration itself has $$O(n)$$ time complexity and for each iteration, we have the prime check which takes $$O(\sqrt&#123;n&#125;)$$. This will exceed the problem's time limit.  Therefore, we need a more efficient solution.</p>
<blockquote>
  <p>Instead of checking if each number is prime or not, what if we mark the multiples of a prime number as non-prime?</p>
</blockquote>
<p><br></p>
<hr>
<h4 id="approachsieveoferatosthenes">Approach: Sieve of Eratosthenes</h4>
<p><strong>Intuition</strong></p>
<p>Suppose we are required to count the number of primes that are less than <code>21</code>. Start by creating an array that contains 21 integers (each index represents an integer).</p>
<p><img src="https://leetcode.com/articles/Figures/204/img1.png" alt="Array of 21 integers" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1. An array of 21 integers which we'll use to mark primes and non-primes.</em>
&#123;:align="center"&#125;</p>
<p>Now, let's start with the smallest prime number we know, which is <code>2</code>. We mark the multiples of this number as non-primes in the array. To mark a number as non-prime, we set a sentinel value of <code>-1</code> in the array at the index corresponding to that number. E.g. the number <code>4</code> is not a prime number, so we mark <code>primes[4] = -1</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/204/img2.png" alt="Multiples of "2" marked as composites" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 2. Multiples of 2 marked as composites in the array.</em>
&#123;:align="center"&#125;</p>
<blockquote>
  <p>Now let's move on to the next available element in the array that has not yet been marked as a composite number. That number is 3, which is also a prime. Now, we repeat the same process with 3 i.e. we mark all the multiples (some will be repeats like 6) as composites.</p>
</blockquote>
<p><img src="https://leetcode.com/articles/Figures/204/img3.png" alt="Multiples of "3" marked as composites" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 3. Multiples of 3 are marked as composites in the array.</em>
&#123;:align="center"&#125;</p>
<p>At this point, you may notice that all of the numbers remaining in the array (that are not marked as composites) are primes.</p>
<p><img src="https://leetcode.com/articles/Figures/204/img4.png" alt="Remaining numbers as primes" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 4. Highlighting the remaining numbers as primes.</em>
&#123;:align="center"&#125;</p>
<blockquote>
  <p>We can start with the smallest prime number, 2, and mark all of its multiples up to "n" as non-primes.  Then we repeat the same process for the next available number in the array that is not marked as composite and so on.  </p>
</blockquote>
<p>We have a nested-loop structure. Now the question is: <em>What are the bounds on these two loops?</em> The outer loop will start at <code>2</code> and go up to $$\sqrt&#123;n&#125;$$. This is because by that point we will have considered all of the possible multiples of all the prime numbers below <code>n</code>. Let's look at the example where <code>n</code> is <code>30</code>. Now the square-root of <code>n</code> is greater than <code>5</code>.  </p>
<pre>It is not necessary to consider any number greater than the square root of n. 

6 * 1 = 6 = 1 * 6
6 * 2 = 12 = 2 * 6
6 * 3 = 18 = 3 * 6
6 * 4 = 24 = 2 * 12
6 * 5 = 30 = 5 * 6
6 * 6 = 36 > 30

Notice that every multiple of 6 was already addressed by some multiple of a prime number less than 6.
</pre>
<p>Now that the outer loop's boundaries are defined, let's define the boundaries of the inner loop. We will invariantly pick the next available prime number (a number/index not yet marked in the array as a composite) before entering the inner loop. Say the index we picked from the outer loop is <code>i</code>, then the inner loop will start at <code>i*i</code> and increase by increments of <code>i</code> until it surpasses <code>n</code>. In short, we iterate over every multiple of <code>i</code> between <code>i</code> and <code>n</code>.  </p>
<p>The question now is why should we start at <code>i*i</code>. Why not start at <code>2*i</code> to keep things simple? The reason is that all of the previous multiples would already have been covered by previous primes. In number theory, <a href="https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic">the fundamental theorem of arithmetic</a>, also called the unique factorization theorem or the unique prime factorization theorem, states that every integer greater than 1 either is a prime number itself or can be represented as the product of prime numbers. So the prime numbers smaller than <code>i</code> would have already covered the multiples smaller than <code>i*i</code>. Let's look at the prime number <code>7</code> to see how all the multiples up to <code>7*7</code> are already covered by primes smaller than '7'.</p>
<pre>
Let's assume that n is 50 (a value greater than 7*7) to demonstrate this claim. 

7 * 2 = 14 = 2 * 7
7 * 3 = 21 = 3 * 7
7 * 4 = 28 = 2 * 2 * 7 = 2 * 14
7 * 5 = 35 = 5 * 7
7 * 6 = 42 = 2 * 3 * 7 = 2 * 21
</pre>
<p><strong>Algorithm</strong></p>
<p><a href="https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes">Wikipedia</a> provides a great approach for this algorithm. So we will follow their method step by step to find all the prime numbers less than or equal to a given integer <code>n</code> by Eratosthenes' method:</p>
<ol>
<li>Create a list of consecutive integers from <code>2</code> through <code>n</code>: <code>(2, 3, 4, ..., n)</code>.</li>
<li>Let <code>p</code> be the variable we use in the outer loop that iterates from <code>2</code> to $$\sqrt&#123;n&#125;$$. Initially, let <code>p</code> equal <code>2</code>, the smallest prime number.</li>
<li>Enumerate the multiples of <code>p</code> by counting in increments of <code>p</code> from <code>p*p</code> to <code>n</code>, and mark them in the list (these will be <code>p*p</code>, <code>p*p + p</code>, <code>p*p + 2*p</code>, …; <code>p</code> itself should be prime).</li>
<li>Find the smallest number in the list greater than <code>p</code> that is not marked. If there was no such number, stop. Otherwise, let <code>p</code> now equal this new number (which is the next prime), and repeat from step 3. </li>
<li>When the algorithm terminates, all of the remaining numbers that are not marked are prime.</li>
</ol>
<p>A key observation is that p will always be prime because every composite value less than p*p has already been marked as a multiple of some smaller prime. Note that some of the numbers may be marked more than once (e.g., <code>15</code> will be marked by both <code>3</code> and <code>5</code>).</p>
<p><strong>Implementation Improvement (Theoretical)</strong></p>
<p>The original algorithm advocates using an array to keep track of primes. However, if we do that, we will spend $$O(n)$$ space just to initialize the array and $$O(n)$$ time iterating over the array to count the primes. To avoid this, we will use a dictionary. There are two advantages to this:</p>
<ol>
<li>We don't need to iterate from <code>0..n</code> to initialize the dictionary. If a number is not a part of the dictionary, it is prime by definition.</li>
<li>In the end, we can simply subtract the length of the dictionary (number of non-primes) from <code>n</code> to find the number of primes.</li>
</ol>
<p>For <code>n = 10</code>, the dictionary would contain <code>4, 6, 8, 9</code>. Excluding <code>1</code> and <code>10</code>, we have <code>10 - 2 - 4 = 4 primes</code>.</p>
<p>This dictionary-based approach unfortunately does not execute within the time limit. Even though on paper it looks like it's worth saving the extra $$O(n)$$ space, in practice, the time required to evaluate and maintain the dictionary makes this approach impractical. So we will stick with the traditional array-based approach. This will add an additional $$O(n)$$ to the time complexity.</p>
<p>Why does this happen you might ask? Well, it's probably because of the localization property of an array. An array is stored as a consecutive chunk of memory. The compiler can cache most of the array's elements in the RAM and other internal caches for super-fast access since these elements are right next to each other in memory. This is why it takes much less time to access elements in an array than to access elements in a dictionary.  Furthermore, this is what offsets the savings we see on paper regarding the overall complexity for the dictionary-based approach.</p>
<iframe src="https://leetcode.com/playground/P2Sa6NCX/shared" frameborder="0" width="100%" height="480" name="P2Sa6NCX"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity: The overall time complexity is $$O(\sqrt&#123;n&#125; \log \log n))$$. The $$\sqrt&#123;n&#125;$$ comes from the outer loop. Each time we hit a prime, we "cross out" the multiples of that prime because we know they aren't prime. But how many iterations do we perform for each prime number? That depends on how many multiples of that number are lower than $$n$$. Let's look at a rough estimate of these values for all the primes.</p>
<pre>For 2, we have to cross out n/2 numbers.
For 3, we have to cross out n/3 numbers.
For 5, we have to cross out n/5 numbers.
...etc for each prime less than n.
</pre>
<p>This means that the time complexity of "crossing out" is $$O(\frac&#123;n&#125;&#123;2&#125; + \frac&#123;n&#125;&#123;3&#125; + \frac&#123;n&#125;&#123;5&#125; + … + \frac&#123;n&#125;&#123;\text&#123;last prime < n&#125;&#125;)$$. This is bounded by $$O(\log \log n)$$ and the proof is available <a href="http://www.cs.umd.edu/~gasarch/BLOGPAPERS/sump.pdf">here</a>. Cheers to this <a href="https://bit.ly/3fgqsE0">discussion</a> post for explaining the complexity analysis in a detailed manner!</p></li>
<li><p>Space Complexity: $$O(n)$$ because we use an array of length $$n + 1$$ to track primes and their multiples. If you use a dictionary instead of an array, you will still end up marking at least $$\frac&#123;n&#125;&#123;2&#125;$$ elements as composites of the number <code>2</code>. Thus, the overall complexity when using a dictionary is also $$O(n)$$.</p></li>
</ul>  
</div>
            