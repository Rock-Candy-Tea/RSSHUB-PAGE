
---
title: '十大经典排序算法（JavaScript版）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff191f3083104b6da00a56fa32a55709~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 01:45:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff191f3083104b6da00a56fa32a55709~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>本文整理了常用的十大经典排序算法，如果对答案有不一样见解的同学欢迎评论区补充讨论，当然有问题，也欢迎在评论区指出。</p>
<p>该篇文章基本引用于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fw3cnote%2Ften-sorting-algorithm.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/w3cnote/ten-sorting-algorithm.html" ref="nofollow noopener noreferrer">菜鸟教程</a>，笔者只是做了一个简化版，以作记录</p>
<h2 data-id="heading-1">1.1 冒泡排序</h2>
<h3 data-id="heading-2">1. 算法步骤</h3>
<ol>
<li>
<p>比较相邻的元素。如果第一个比第二个大，就交换他们两个。</p>
</li>
<li>
<p>对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。</p>
</li>
</ol>
<h3 data-id="heading-3">2. 动图演示</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff191f3083104b6da00a56fa32a55709~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">3. JavaScript 代码实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bubbleSort</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">const</span> len = arr.length;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<len-<span class="hljs-number">1</span>;i++)&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j=<span class="hljs-number">0</span>;j<len-i;j++)&#123;
            <span class="hljs-keyword">if</span>(arr[j-<span class="hljs-number">1</span>]>arr[j])&#123;<span class="hljs-comment">// 相邻元素两两对比</span>
                [arr[j-<span class="hljs-number">1</span>],arr[j]] = [arr[j],arr[j-<span class="hljs-number">1</span>]];<span class="hljs-comment">// 元素交换</span>
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;
<span class="hljs-built_in">console</span>.log(bubbleSort([<span class="hljs-number">4</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">41</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">1.2 选择排序</h2>
<h3 data-id="heading-6">1. 算法步骤</h3>
<ol>
<li>
<p>首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。</p>
</li>
<li>
<p>再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。</p>
</li>
</ol>
<h3 data-id="heading-7">2. 动图演示</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd8dab5d43964849a455b151508a346e~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">3. JavaScript 代码实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">selectionSort</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">const</span> len = arr.length;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<len;i++)&#123;
        <span class="hljs-keyword">let</span> minIndex = i;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j=i+<span class="hljs-number">1</span>;j<len;j++)&#123;
            <span class="hljs-keyword">if</span>(arr[minIndex]>arr[j])&#123;<span class="hljs-comment">// 寻找最小的数</span>
                minIndex = j;<span class="hljs-comment">// 将最小数的索引保存</span>
            &#125;
        &#125;
        [arr[i],arr[minIndex]] = [arr[minIndex],arr[i]];<span class="hljs-comment">//每轮只用交换一次</span>
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;
<span class="hljs-built_in">console</span>.log(selectionSort([<span class="hljs-number">23</span>,<span class="hljs-number">4</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">4</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">1.3 插入排序</h2>
<h3 data-id="heading-10">1. 算法步骤</h3>
<ol>
<li>
<p>将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。</p>
</li>
<li>
<p>从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）</p>
</li>
</ol>
<h3 data-id="heading-11">2. 动图演示</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11b719edfcd24e0796df9bd5f3aadba1~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">3. JavaScript代码实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">insertionSort</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">const</span> len = arr.length;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">1</span>;i<len;i++)&#123;
        <span class="hljs-keyword">let</span> index = i;
        <span class="hljs-keyword">const</span> current = arr[i];
        <span class="hljs-keyword">while</span> (current<arr[index-<span class="hljs-number">1</span>]&&index>=<span class="hljs-number">0</span>)&#123;
            arr[index]=arr[index-<span class="hljs-number">1</span>];
            index--;
        &#125;
        arr[index]=current;
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="hljs-built_in">console</span>.log(insertionSort([<span class="hljs-number">23</span>,<span class="hljs-number">4</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">4</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">1.4 希尔排序</h2>
<h3 data-id="heading-14">1. 算法步骤</h3>
<ol>
<li>
<p>选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；</p>
</li>
<li>
<p>按增量序列个数 k，对序列进行 k 趟排序；</p>
</li>
<li>
<p>每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。</p>
</li>
</ol>
<h3 data-id="heading-15">2. JavaScript</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shellSort</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">var</span> len = arr.length,
        temp,
        gap = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">while</span>(gap < len/<span class="hljs-number">3</span>) &#123;          <span class="hljs-comment">//动态定义间隔序列</span>
        gap =gap*<span class="hljs-number">3</span>+<span class="hljs-number">1</span>;
    &#125;
    <span class="hljs-keyword">for</span> (gap; gap > <span class="hljs-number">0</span>; gap = <span class="hljs-built_in">Math</span>.floor(gap/<span class="hljs-number">3</span>)) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = gap; i < len; i++) &#123;
            temp = arr[i];
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = i-gap; j >= <span class="hljs-number">0</span> && arr[j] > temp; j-=gap) &#123;
                arr[j+gap] = arr[j];
            &#125;
            arr[j+gap] = temp;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">1.5 归并排序</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeSort</span>(<span class="hljs-params">arr</span>) </span>&#123;  <span class="hljs-comment">// 采用自上而下的递归方法</span>
    <span class="hljs-keyword">const</span> len = arr.length;
    <span class="hljs-keyword">if</span>(len<<span class="hljs-number">2</span>) <span class="hljs-keyword">return</span> arr;
    <span class="hljs-keyword">const</span> mid = <span class="hljs-built_in">Math</span>.floor(len/<span class="hljs-number">2</span>);
    <span class="hljs-keyword">const</span> leftArr = arr.slice(<span class="hljs-number">0</span>,mid);
    <span class="hljs-keyword">const</span> rightArr = arr.slice(mid);
    <span class="hljs-keyword">return</span> merge(mergeSort(leftArr),mergeSort(rightArr));
&#125;
​
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">merge</span>(<span class="hljs-params">left, right</span>) </span>&#123;
    <span class="hljs-keyword">const</span> res = [];
    <span class="hljs-keyword">while</span> (left.length&&right.length)&#123;
        <span class="hljs-keyword">if</span>(left[<span class="hljs-number">0</span>]<right[<span class="hljs-number">0</span>])&#123;
            res.push(left.shift());
        &#125;<span class="hljs-keyword">else</span>&#123;
            res.push(right.shift());
        &#125;
    &#125;
    <span class="hljs-keyword">while</span> (left.length)&#123;
        res.push(left.shift());
    &#125;
    <span class="hljs-keyword">while</span> (right.length)&#123;
        res.push(right.shift());
    &#125;
    <span class="hljs-keyword">return</span> res;
&#125;
<span class="hljs-built_in">console</span>.log(mergeSort([<span class="hljs-number">23</span>,<span class="hljs-number">4</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">4</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">1.6 快速排序</h2>
<h3 data-id="heading-18">1. 算法步骤</h3>
<ol>
<li>从数列中挑出一个元素，称为 "基准"（pivot）;</li>
<li>重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；</li>
<li>递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；</li>
</ol>
<h3 data-id="heading-19">2. 动图演示</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b824a100a00644018660cb1cb02836fe~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-20">3. JavaScript</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">quickSort</span>(<span class="hljs-params">arr, left, right</span>) </span>&#123;
    <span class="hljs-keyword">const</span> len = arr.length;
    left = <span class="hljs-keyword">typeof</span> left != <span class="hljs-string">'number'</span> ? <span class="hljs-number">0</span> : left;
    right = <span class="hljs-keyword">typeof</span> right != <span class="hljs-string">'number'</span> ? len - <span class="hljs-number">1</span> : right;
    <span class="hljs-keyword">if</span>(left<right)&#123;
        <span class="hljs-keyword">const</span> partitionIndex = partition(arr,left,right);
        quickSort(arr,left,partitionIndex-<span class="hljs-number">1</span>);
        quickSort(arr,partitionIndex+<span class="hljs-number">1</span>,right);
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;
​
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">partition</span>(<span class="hljs-params">arr, left ,right</span>) </span>&#123;     <span class="hljs-comment">// 分区操作</span>
    <span class="hljs-keyword">const</span> pivot = left;
    <span class="hljs-keyword">let</span> index = left+<span class="hljs-number">1</span>;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=index;i<=right;i++)&#123;
        <span class="hljs-keyword">if</span>(arr[pivot]>arr[i])&#123;
            [arr[index],arr[i]]=[arr[i],arr[index]];
            index++;
        &#125;
    &#125;
    [arr[pivot],arr[index-<span class="hljs-number">1</span>]] = [arr[index-<span class="hljs-number">1</span>],arr[pivot]];
    <span class="hljs-keyword">return</span> index-<span class="hljs-number">1</span>
&#125;
<span class="hljs-built_in">console</span>.log(quickSort([<span class="hljs-number">23</span>,<span class="hljs-number">4</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">4</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">1.7 堆排序</h2>
<h3 data-id="heading-22">1. 算法步骤</h3>
<ol>
<li>创建一个堆 H[0……n-1]；</li>
<li>把堆首（最大值）和堆尾互换；</li>
<li>把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；</li>
<li>重复步骤 2，直到堆的尺寸为 1。</li>
</ol>
<h3 data-id="heading-23">2. 动图演示</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa8c0a859f584db896f3b6c181dd3c7b~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-24">3. JavaScript</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> len;    <span class="hljs-comment">// 因为声明的多个函数都需要数据长度，所以把len设置成为全局变量</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildMaxHeap</span>(<span class="hljs-params">arr</span>) </span>&#123;   <span class="hljs-comment">// 建立大顶堆</span>
    len = arr.length;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-built_in">Math</span>.floor(len/<span class="hljs-number">2</span>); i >= <span class="hljs-number">0</span>; i--) &#123;
        heapify(arr, i);
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">heapify</span>(<span class="hljs-params">arr, i</span>) </span>&#123;     <span class="hljs-comment">// 堆调整</span>
    <span class="hljs-keyword">var</span> left = <span class="hljs-number">2</span> * i + <span class="hljs-number">1</span>,
        right = <span class="hljs-number">2</span> * i + <span class="hljs-number">2</span>,
        largest = i;
    <span class="hljs-keyword">if</span> (left < len && arr[left] > arr[largest]) &#123;
        largest = left;
    &#125;
    <span class="hljs-keyword">if</span> (right < len && arr[right] > arr[largest]) &#123;
        largest = right;
    &#125;
    <span class="hljs-keyword">if</span> (largest != i) &#123;
        swap(arr, i, largest);
        heapify(arr, largest);
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">swap</span>(<span class="hljs-params">arr, i, j</span>) </span>&#123;
    <span class="hljs-keyword">var</span> temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">heapSort</span>(<span class="hljs-params">arr</span>) </span>&#123;
    buildMaxHeap(arr);
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = arr.length-<span class="hljs-number">1</span>; i > <span class="hljs-number">0</span>; i--) &#123;
        swap(arr, <span class="hljs-number">0</span>, i);
        len--;
        heapify(arr, <span class="hljs-number">0</span>);
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">1.8 计数排序</h2>
<h3 data-id="heading-26">1. 算法步骤</h3>
<ol>
<li>找出待排序的数组中最大和最小的元素 (0)</li>
<li>统计数组中每个值为i的元素出现的次数，存入数组C的第i项</li>
<li>对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）</li>
<li>反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1</li>
</ol>
<h3 data-id="heading-27">2. 动图演示</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/473235604fa2404bbf93bcaec8db6712~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-28">3. JavaScript</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">countingSort</span>(<span class="hljs-params">arr, maxValue</span>) </span>&#123;
    <span class="hljs-keyword">const</span> res = [];
    <span class="hljs-keyword">const</span> container = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(maxValue+<span class="hljs-number">1</span>).fill(<span class="hljs-number">0</span>);
    <span class="hljs-comment">//将所有数据存放在容器里</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<arr.length;i++)&#123;
        container[arr[i]]++;
    &#125;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j=<span class="hljs-number">0</span>;j<=maxValue;j++)&#123;
        <span class="hljs-keyword">while</span> (container[j]><span class="hljs-number">0</span>)&#123;
            res.push(j);
            container[j]--;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> res;
&#125;
<span class="hljs-built_in">console</span>.log(countingSort([<span class="hljs-number">23</span>,<span class="hljs-number">4</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">4</span>],<span class="hljs-number">23</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">1.9 桶排序</h2>
<h3 data-id="heading-30">1. 示意图</h3>
<p>元素分布在桶中：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5eff2bc5664498f8f128fb66a30143a~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后，元素在每个桶中排序：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78c103d96c8e4243bdca27efb5b893c3~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-31">2. 算法步骤</h3>
<ol>
<li>找到数组中的最大值、最小值</li>
<li>设置桶的数量，然后由最大值、最小值和桶的数量，计算出每个桶装的数的大小范围</li>
<li>遍历数组，将数据分别放入每个桶中</li>
<li>对每个桶进行排序</li>
</ol>
<h2 data-id="heading-32">1.10 基数排序</h2>
<p>原理是将整数按位数切割成不同的数字，然后按每个位数分别比较</p>
<p>这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异：</p>
<ul>
<li>基数排序：根据键值的每位数字来分配桶；</li>
<li>计数排序：每个桶只存储单一键值；</li>
<li>桶排序：每个桶存储一定范围的数值；</li>
</ul>
<h3 data-id="heading-33">2. 基数排序动图演示</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bec3beea0924acd884195919da2ae20~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-34">总结</h1>
<p>觉得写得好的，对你有帮助的，可以分享给身边人，<strong>知识越分享越多，千万不要吝啬呀</strong></p>
<p>后续继续分享我的经验总结，请关注我，我们一起学前端</p></div>  
</div>
            