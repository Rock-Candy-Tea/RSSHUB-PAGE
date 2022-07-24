
---
title: '2034. Stock Price Fluctuation'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=1137'
author: LeetCode
comments: false
date: Thu, 23 Jun 2022 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1137'
---

<div>   
<p>You are given a stream of <strong>records</strong> about a particular stock. Each record contains a <strong>timestamp</strong> and the corresponding <strong>price</strong> of the stock at that timestamp.</p>

<p>Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream <strong>correcting</strong> the price of the previous wrong record.</p>

<p>Design an algorithm that:</p>

<ul>
<li><strong>Updates</strong> the price of the stock at a particular timestamp, <strong>correcting</strong> the price from any previous records at the timestamp.</li>
<li>Finds the <strong>latest price</strong> of the stock based on the current records. The <strong>latest price</strong> is the price at the latest timestamp recorded.</li>
<li>Finds the <strong>maximum price</strong> the stock has been based on the current records.</li>
<li>Finds the <strong>minimum price</strong> the stock has been based on the current records.</li>
</ul>

<p>Implement the <code>StockPrice</code> class:</p>

<ul>
<li><code>StockPrice()</code> Initializes the object with no price records.</li>
<li><code>void update(int timestamp, int price)</code> Updates the <code>price</code> of the stock at the given <code>timestamp</code>.</li>
<li><code>int current()</code> Returns the <strong>latest price</strong> of the stock.</li>
<li><code>int maximum()</code> Returns the <strong>maximum price</strong> of the stock.</li>
<li><code>int minimum()</code> Returns the <strong>minimum price</strong> of the stock.</li>
</ul>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
<strong>Output</strong>
[null, null, null, 5, 10, null, 5, null, 2]

<strong>Explanation</strong>
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= timestamp, price <= 10<sup>9</sup></code></li>
<li>At most <code>10<sup>5</sup></code> calls will be made <strong>in total</strong> to <code>update</code>, <code>current</code>, <code>maximum</code>, and <code>minimum</code>.</li>
<li><code>current</code>, <code>maximum</code>, and <code>minimum</code> will be called <strong>only after</strong> <code>update</code> has been called <strong>at least once</strong>.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>We are given a stream of <strong>records</strong> of the <strong>price</strong> of stock at different <strong>timestamps</strong>. We need to implement some functions to get the lowest, highest, and latest price of the stock based on the records provided.     </p>
<p>The records do not come in chronological order. Another record with the same timestamp may appear later in the stream, correcting the price of the previous wrong record; this correction can affect the lowest, highest, and latest price of the stock.</p>
<p>Let's walk through an example to make sure we clearly understand what this problem is asking. Suppose the stock prices in increasing order of timestamp are, $$ [2, 10, 3, 3, 5, 9] $$.<br>
Here, the lowest price of the stock is $$ 2 $$, the highest price is $$ 10 $$, and the latest price is $$ 9 $$.       </p>
<ul>
<li>If the $$ 1^&#123;st&#125; $$ record is corrected from $$ 2 $$ to $$ 4 $$, then the lowest price changes from $$ 2 $$ to $$ 3 $$. </li>
<li>If the last record is corrected from $$ 9 $$ to $$ 6 $$, then the latest price changes to $$ 6 $$.      </li>
<li>If $$ 2^&#123;nd&#125; $$ record is corrected from $$ 10 $$ to $$ 20 $$, then the highest price changes to $$ 20 $$. </li>
</ul>
<p>Thus, we need to store all the records of the stock price and make corrections when necessary.<br>
We can use a hashmap to store timestamp as key and price as value, where the correction of records will only take constant time.</p>
<p>Now we need to get the highest and lowest price of the stock. We could think of sorting the stock prices but when an update or an insertion of a new price is made we would need to sort the prices again.</p>
<p>Thus, we will prefer using a data structure that allows us to track the current minimum and maximum values efficiently. We can use a sorted set, sorted map, or min and max-heaps; the intuition will remain the same only the implementation will differ. 
All these data structures keep the elements sorted, and the insertion and removal of elements take only logarithmic time.</p>
<hr>
<h4 id="approach1hashedandsortedmap">Approach 1: Hashed and Sorted Map</h4>
<p><strong>Intuition</strong></p>
<p>We will use a hashmap (<code>timestampPriceMap</code>) to store the price of the stocks. A hashmap stores the elements as key-value pairs. Here, our key is the timestamp and the value is the price of the stock at the respective timestamp, i.e. the hashmap maps <code>timestamp</code> to <code>price</code>.    </p>
<p>Now, we will use a sorted map (<code>priceFrequency</code>) to store the stock prices in increasing order.<br>
A sorted map also stores the elements as key-value pairs and keeps elements sorted on the basis of the key. Thus, we will store the price of the stocks as the key and its occurrence (count) in our records stream as the value, i.e. the sorted map maps the <code>price</code> to the <code>frequency</code>. It denotes how many times a price is present in our records stream.</p>
<p><strong>Insertion of Record:</strong>     </p>
<ul>
<li>Insert the stock price at the current timestamp in <code>timestampPriceMap</code>.</li>
<li>Increase the stock price's count in <code>priceFrequency</code>. Initially, it is assumed the count is 0 when the price is not present in the map.   </li>
</ul>
<p><strong>Updation of Record:</strong>     </p>
<ul>
<li>Update the stock price of the current timestamp in <code>timestampPriceMap</code>.       </li>
<li>Decrease the count of the old price from <code>priceFrequency</code> and if the count reaches $$ 0 $$ then remove it and increase the correct stock price's count.</li>
</ul>
<p><strong>Get the Latest Price:</strong></p>
<ul>
<li>Use one variable to keep track of the latest time and get the stock's price at the latest time from <code>timestampPriceMap</code>.</li>
</ul>
<p><strong>Get Minimum and Maximum Stock Price:</strong> </p>
<ul>
<li>The first element's key of <code>priceFrequency</code> is the lowest price of the stock.</li>
<li>The last element's key of <code>priceFrequency</code> is the highest price of the stock.</li>
</ul>
<p>!?!../Documents/2034/slideshow1.json:960,540!?!</p>
<p><br></p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize variables:<ul>
<li><code>latestTime</code>, variable to store the latest timestamp according to the records.</li>
<li><code>timestampPriceMap</code>, a hashmap to store timestamp and prices of the stock.</li>
<li><code>priceFrequency</code>, a sorted map to store all prices in increasing order.</li></ul></li>
<li>In the <code>update</code> function, the current record can be a new record or a correction to an old record:<ul>
<li>Try to update <code>latestTime</code>, to the current timestamp.</li>
<li>If the current timestamp is already present in <code>timestampPriceMap</code> it means this record is a correction then we reduce the count of the old price from <code>priceFrequency</code>.</li>
<li>Add/update the current timestamp's price in <code>timestampPriceMap</code>.</li>
<li>Increment the count of the current timestamp's price in <code>priceFrequency</code>.</li></ul></li>
<li>In the <code>current</code> function, we need to return the latest price of the stock, i.e. price of the stock at <code>latestTime</code> in <code>timestampPriceMap</code>.</li>
<li>In the <code>maximum</code> function, we need to return the maximum stock price, i.e. the key of the last element in <code>priceFrequency's</code>.</li>
<li>In the <code>minimum</code> function, we need to return the minimum stock price, i.e. the key of the first element in <code>priceFrequency's</code>.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/4jGoRcuN/shared" frameborder="0" width="100%" height="500" name="4jGoRcuN"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>If $$ N $$ is the number of records in the input stream.</p>
<ul>
<li><p>Time complexity: $$ O(N \log N) $$</p></li>
<li><p>In the <code>update</code> function, we add and remove a record in both hashmap and sorted map. In hashmap, both operations take constant time, but in the sorted map they take $$ O(\log N) $$ time.</p></li>
<li><p>Each call to the <code>maximum</code>, <code>minimum</code>, or <code>current</code> function will take only constant time to return the result.</p>
<blockquote>
  <p>But in Java, getting first or last element of tree map takes <code>log(N)</code> time. Thus, here <code>maximum</code>, <code>minimum</code> functions will take <code>O(log(N))</code> time for each function call.</p>
</blockquote></li>
<li><p>In the worst-case scenario, all $$ N $$ calls will be to the <code>update</code> function, which will require a total of $$ O(N \log N) $$ time. </p></li>
<li><p>Space complexity: $$ O(N) $$</p></li>
<li><p>In the <code>update</code> function, we add and remove a record in both the hashmap and sorted map. Thus each function call takes $$ O(1) $$ space. So for $$ N $$ update calls, it will take $$ O(N) $$ space.</p></li>
<li><p>The <code>maximum</code>, <code>minimum</code>, and <code>current</code> functions do not use any additional space.</p></li>
<li><p>Thus, in the worst-case, we will add all $$ N $$ records in both the hashmap and sorted map, which takes $$ O(N) $$ space.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2hashmapandheaps">Approach 2: Hashmap and Heaps</h4>
<p><strong>Intuition</strong></p>
<p>In this approach, again, we will use a hashmap (<code>timestampPriceMap</code>) to record the stock's price at each <code>timestamp</code>. </p>
<p>However, it is not necessary for us to maintain a sorted map as we did in the previous approach. Any time we need to efficiently keep track of the lowest or highest value, we should consider using a heap data structure. Here, we will store each record in 2 different heaps, a min-heap to efficiently track the lowest stock price and a max-heap to efficiently track the highest stock price.</p>
<p>Now the real challenge will be, how to update stock prices?<br>
We can directly change the stock price in the hashmap, but in the heaps, we would have to pop all stock prices until the old price comes on top and then push the new price and all other popped prices back. This would make the update operation very costly.</p>
<p>One way to resolve this issue is every time we get a new price, we push it into each heap, and only while getting the top element we need to verify if the price is correct or outdated.   </p>
<p>But how do we know which prices are outdated?<br>
For this, we can use our hashmap (<code>timestampPriceMap</code>). Every time we receive a <code>(price, timestamp)</code> pair, we will set the value for the key (<code>timestamp</code>) to the given <code>price</code>. If the <code>timestamp</code> already exists in the hashmap, we overwrite the old price. 
So, when finding the maximum or minimum price, we will check to see if the <code>(price, timestamp)</code> pair on the top of the heap agrees with the <code>price</code> listed for the <code>timestamp</code> in the hashmap. If it does not, then the price is outdated, and we discard this pair and get the next top element and again check with the hashmap.           </p>
<p><strong>Insertion/Updation of Record:</strong>     </p>
<ul>
<li>Insert/Update the stock price at the current timestamp in <code>timestampPriceMap</code>.</li>
<li>Push the <code>(price, timestamp)</code> pair into the <code>minHeap</code> and <code>maxHeap</code>.  </li>
</ul>
<p><strong>Get the Latest Price:</strong></p>
<ul>
<li>Use one variable to keep track of the latest time and get the stock's price at the latest time from <code>timestampPriceMap</code>.</li>
</ul>
<p><strong>Get Minimum and Maximum Stock Price:</strong> </p>
<ul>
<li>Get the <code>(price, timestamp)</code> pair from the top of <code>minHeap</code>/<code>maxHeap</code>.</li>
<li>If <code>timestampPriceMap[timestamp] != price</code>, it means the price for the current <code>timestamp</code> was updated and that this <code>price</code> is outdated. So we discard this pair and repeat the above step. Otherwise, return the current <code>price</code>.</li>
</ul>
<p>!?!../Documents/2034/slideshow2.json:960,540!?!</p>
<p><br></p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize variables:<ul>
<li><code>latestTime</code>, variable to store the latest timestamp according to the records.</li>
<li><code>timestampPriceMap</code>, a hashmap to store timestamp and prices of the stock.</li>
<li><code>minHeap, maxHeap</code>, heaps to store <code>(price, timestamp)</code> pairs and sort elements based on <code>price</code>.</li></ul></li>
<li>In the <code>update</code> function, the current record can be a new record or a correction to an old record:<ul>
<li>Try to update <code>latestTime</code>, to the current timestamp.</li>
<li>Add/update the current timestamp's price in <code>timestampPriceMap</code>.</li>
<li>Push <code>(price, timestamp)</code> pair in the heaps.</li></ul></li>
<li>In the <code>current</code> function, we need to return the latest price of the stock, i.e. price of the stock at <code>latestTime</code> in <code>timestampPriceMap</code>.</li>
<li>In the <code>maximum</code> / <code>minimum</code> function, we get the <code>(price, timestamp)</code> pair from the top of <code>maxHeap</code> / <code>minHeap</code>. If <code>timestampPriceMap[timestamp]</code> is not same as <code>price</code>, we discard this pair and repeat the same step again. Otherwise, return the current <code>price</code>.</li>
</ol>
<p><strong>Implementation</strong></p>
<blockquote>
  <p><strong>Note:</strong> In python, in min-heap we push stock prices after multiplying with <code>-1</code> so that the min-heap behaves as a max-heap. This helps in keeping the implementation simpler.    </p>
</blockquote>
<iframe src="https://leetcode.com/playground/KsYu7HKG/shared" frameborder="0" width="100%" height="500" name="KsYu7HKG"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$ N $$ be the number of records in the input stream.</p>
<ul>
<li><p>Time complexity: $$ O(N \log N) $$</p></li>
<li><p>In the <code>update</code> function, we add one record to the hashmap and to each heap. Adding the record to the hashmap takes constant time. However, for a heap, each push operation takes $$ O(\log N) $$ time. So for $$ N $$ update calls, it will take $$ O(N\log N) $$ worst-case time.</p></li>
<li><p>Each <code>current</code> function call takes only constant time to return the result. </p></li>
<li><p>In the <code>maximum</code> and <code>minimum</code> functions, we pop any outdated records that are at the top of the heap. In the worst-case scenario, we might pop $$ (N - 1) $$ elements and each pop takes $$ O(\log N) $$ time, so it might seem for one function call the time complexity is $$N \log N$$, so for $$ N $$ functions calls it could be $$ N^&#123;2&#125; \log N $$. 
However, when we pop a record from the heap, it's gone and won't be popped again. So overall, if we push $$N$$ elements into a heap, we cannot pop more than $$N$$ elements, taking into account all function calls. Thus, calls to <code>maximum</code> and <code>minimum</code> will at most require $$ O(N \log N) $$ time.</p></li>

<li><p>Space complexity: $$ O(N) $$</p></li>
<li><p>In the <code>update</code> function, we add a record to the hashmap and each heap. Since each stock price takes $$ O(1) $$ space, for $$ N $$ update calls, it will take $$ O(N) $$ space.</p></li>
<li><p>The <code>current</code> function does not use any additional space.</p></li>
<li><p>In the <code>maximum</code> and <code>minimum</code> functions, we only remove elements from the heap thus these functions also do not use any additional space.</p></li>
<li><p>Thus, in the worst-case, we will add all $$ N $$ records to the hashmap and to both heaps, which takes $$ O(N) $$ space.</p></li>
</ul>  
</div>
            