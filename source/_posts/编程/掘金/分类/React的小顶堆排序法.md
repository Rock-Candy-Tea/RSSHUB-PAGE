
---
title: 'React的小顶堆排序法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31f539422a8b4424b3cf11bc194a99b4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 04:37:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31f539422a8b4424b3cf11bc194a99b4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>想要了解react源码，还是得要了解一丢丢的算法，周末学习一个堆排序里面的小顶堆。</p>
<p>为什么要了解堆排序，因为react17源码里任务优先级调度，采用的就是小顶堆。</p>
<h2 data-id="heading-1">基础知识</h2>
<p>假如一个数组[1,2,3,4,5,6,7],生成二叉树的结构是什么样，就是下面的样子,<strong>小括号里面</strong>是对应<strong>数组的索引</strong></p>
<p>一个父节点有两个子节点，左边叫左子节点，右边叫右子节点</p>
<p>其中数字1相当于2，3的父节点，2相当于4，5的父节点，3相当于6，7的父节点</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31f539422a8b4424b3cf11bc194a99b4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">代码安排</h2>
<p>假如一个随机的数组arr1 = [3,6,4,9,2,1,7]，里面是数代表着，不同的任务，对应的数字越小，代表优先级最高</p>
<h3 data-id="heading-3">数组排列成小顶堆</h3>
<p>小顶堆：每一个父节点都比它的两个子节点小，第一个父节点是最小的</p>
<ul>
<li>每次push进去一个元素，和这个元素的索引</li>
<li>找出这个子元素的父元素，然后比较大小，递归执行该方法，直到找到最上层第一个元素</li>
</ul>
<p><strong>排列之后：</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dde1331d2124d42898137a6fb7a5331~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">排序</h3>
<p>排序的过程实际上也是react事件的调度的过程</p>
<p>取出最顶端元素（优先级最高的任务去执行）；最后一位元素，移动到第一位；再重新排序</p>
<p>1.根据父节点的索引0，找出它的两个子节点</p>
<p>2.父节点和左子节点比较</p>
<ul>
<li>左子节点小于父节点，再比较左子节点与右子节点
<ul>
<li>右子节点小于左子节点，将右子节点与父节点互换，右子节点作为父节点，继续循环比较</li>
<li>右子节点大于左子节点，将左子节点与父节点互换，左子节点作为父节点，继续循环比较</li>
</ul>
</li>
<li>左子节点大于父节点，比较右子节点与父节点
<ul>
<li>右子节点小于父节点，将右子节点与父节点互换，右子节点作为父节点，继续循环比较</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr1 = [<span class="hljs-number">3</span>,<span class="hljs-number">6</span>,<span class="hljs-number">4</span>,<span class="hljs-number">9</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">7</span>];
<span class="hljs-keyword">var</span> heap = []  <span class="hljs-comment">// 存排列好的小顶堆</span>
<span class="hljs-keyword">var</span> stack = [] <span class="hljs-comment">// 排序好的数组</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>,len = arr1.length;i<len;i++) &#123;
    <span class="hljs-keyword">const</span> index = heap.length;
    <span class="hljs-keyword">const</span> node =  arr1[i] 
    heap.push(node);
    siftUp(heap, node, index);
&#125;

<span class="hljs-keyword">while</span>(heap.length) &#123;
    <span class="hljs-keyword">const</span> first = heap[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">const</span> last = heap.pop()
    stack.push(first)
    <span class="hljs-keyword">if</span>(first !=last) &#123;
        heap[<span class="hljs-number">0</span>] = last;
        siftDown(heap, last, <span class="hljs-number">0</span>)
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">break</span>;
    &#125;
&#125;
    
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">siftDown</span>(<span class="hljs-params">heap, node, i</span>) </span>&#123;
    <span class="hljs-keyword">let</span> index = i;
    <span class="hljs-keyword">const</span> length = heap.length
    <span class="hljs-keyword">const</span> halfLength = length >>> <span class="hljs-number">1</span>
    <span class="hljs-keyword">while</span>(index < halfLength) &#123;
       <span class="hljs-comment">// 根据顶层父节点索引，找出它的左右子节点</span>
       <span class="hljs-keyword">const</span> leftIndex = (index + <span class="hljs-number">1</span>) * <span class="hljs-number">2</span> - <span class="hljs-number">1</span>
       <span class="hljs-keyword">const</span> left = heap[leftIndex]
       <span class="hljs-keyword">const</span> rightIndex = leftIndex + <span class="hljs-number">1</span>
       <span class="hljs-keyword">const</span> right = heap[rightIndex]
       <span class="hljs-comment">// 左子节点小于父节点</span>
       <span class="hljs-keyword">if</span> (left < node) &#123;
           <span class="hljs-comment">// 右子节点小于左子节点,两个交换，右子节点作为父节点，继续循环</span>
           <span class="hljs-keyword">if</span>(rightIndex < length && right < left) &#123;
               heap[index] = right
               heap[rightIndex] = node
               index = rightIndex
           &#125; <span class="hljs-keyword">else</span> &#123;
               <span class="hljs-comment">// 右子节点大于左子节点,两个交换，左子节点作为父节点，继续循环</span>
               heap[index] = left
               heap[leftIndex] = node
               index = leftIndex
           &#125;
       &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (rightIndex < length && right < node) &#123;
           <span class="hljs-comment">// 右子节点小于父节点，两个交换，右子节点作为父节点，继续循环</span>
           heap[index] = right
           heap[rightIndex] = node
           index = rightIndex
       &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-keyword">return</span> 
       &#125;
    &#125;
&#125;
    
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">siftUp</span>(<span class="hljs-params">heap, node, i</span>) </span>&#123;
    <span class="hljs-keyword">let</span> index = i
    <span class="hljs-comment">// 找到第一个元素，不再比较</span>
    <span class="hljs-keyword">while</span>(index > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-comment">// 根据子节点索引，找到父节点</span>
        <span class="hljs-keyword">const</span> parentIndex = (index - <span class="hljs-number">1</span>) >>> <span class="hljs-number">1</span>
        <span class="hljs-keyword">const</span> parent = heap[parentIndex]
        <span class="hljs-comment">// 父节点大于子节点，父子节点交换位置</span>
        <span class="hljs-keyword">if</span> (parent > node) &#123;
            heap[parentIndex] = node
            heap[index]= parent
            <span class="hljs-comment">// 指针移动到父节点位置，作为子节点，找它的父节点</span>
            index = parentIndex
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span>
        &#125;
    &#125;
&#125;
    
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">总结</h2>
<p>堆也是一种数据类型，React的事件调度采用最小堆，非常经典的算法运用。空闲时间还是需要加强算法。</p>
<p>感兴趣的小伙伴可以看看源码react/packages/scheduler/src/SchedulerMinHeap.js</p>
<p>最后祝大家周末愉快，求点赞~</p></div>  
</div>
            