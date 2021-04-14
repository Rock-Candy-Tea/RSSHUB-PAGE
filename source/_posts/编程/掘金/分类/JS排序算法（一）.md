
---
title: 'JS排序算法（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4847'
author: 掘金
comments: false
date: Wed, 14 Apr 2021 03:38:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=4847'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.冒泡排序</h2>
<h4 data-id="heading-1">简介</h4>
<p>冒泡排序（Bubble Sort）是最易懂的排序算法，但是效率较低，生产环境中很少使用。</p>
<p>它的基本思想是：</p>
<ol>
<li>
<p>依次比较相邻的两个数，如果不符合排序规则，则调换两个数的位置。这样一遍比较下来，能够保证最大（或最小）的数排在最后一位。</p>
</li>
<li>
<p>再对最后一位以外的数组，重复前面的过程，直至全部排序完成。</p>
</li>
</ol>
<p>由于每进行一次这个过程，在该次比较的最后一个位置上，正确的数会自己冒出来，就好像“冒泡”一样，这种算法因此得名。</p>
<h4 data-id="heading-2">算法实现</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype.bubbleSort = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>; i++) &#123;
    <span class="hljs-comment">//循环第一次之后数组最后一位就是最大的，下一次循环到最后一位的前i位就行，所有-i,这样每次冒泡排序的区间都会把已排序好的区间减掉</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < <span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span> - i; j++) &#123;
      <span class="hljs-comment">//第一位和第二位比较，如果第一位比第二位大，则交换位置</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>[j] > <span class="hljs-built_in">this</span>[j + <span class="hljs-number">1</span>]) &#123;
        <span class="hljs-keyword">const</span> temp = <span class="hljs-built_in">this</span>[j];
        <span class="hljs-built_in">this</span>[j] = <span class="hljs-built_in">this</span>[j + <span class="hljs-number">1</span>];
        <span class="hljs-built_in">this</span>[j + <span class="hljs-number">1</span>] = temp;
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
&#125;;
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">5</span>, <span class="hljs-number">4</span>, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>];
<span class="hljs-built_in">console</span>.log(arr.bubbleSort());


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bubbleSort</span>(<span class="hljs-params">arr</span>) </span>&#123;
  <span class="hljs-keyword">let</span> length = arr.length;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length - <span class="hljs-number">1</span>; i++) &#123;
    <span class="hljs-comment">//循环第一次之后数组最后一位就是最大的，下一次循环到最后一位的前i位就行，所有-i,这样每次冒泡排序的区间都会把已排序好的区间减掉</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < length - <span class="hljs-number">1</span> - i; j++) &#123;
      <span class="hljs-comment">//第一位和第二位比较，如果第一位比第二位大，则交换位置</span>
      <span class="hljs-keyword">if</span> (arr[j] > arr[j + <span class="hljs-number">1</span>]) &#123;
        <span class="hljs-keyword">const</span> temp = arr[j];
        arr[j] = arr[j + <span class="hljs-number">1</span>];
        arr[j + <span class="hljs-number">1</span>] = temp;
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> arr;
&#125;
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">5</span>, <span class="hljs-number">5</span>, <span class="hljs-number">7</span>, <span class="hljs-number">2</span>, <span class="hljs-number">8</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">1</span>];
<span class="hljs-built_in">console</span>.log(bubbleSort(arr));

<span class="copy-code-btn">复制代码</span></code></pre>
<p>时间复杂度：O(n^2) 空间复杂度：O(1) 稳定性：冒泡排序是稳定的排序算法，因为可以实现值相等的元素的相对位置不变</p>
<h2 data-id="heading-3">2.选择排序</h2>
<h4 data-id="heading-4">简介</h4>
<p>选择排序（Selection Sort）与冒泡排序类似，也是依次对相邻的数进行两两比较。不同之处在于，它不是每比较一次就调换位置，而是一轮比较完毕，找到最大值（或最小值）之后，将其放在正确的位置，其他数的位置不变。</p>
<h4 data-id="heading-5">算法实现</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> sort = <span class="hljs-function">(<span class="hljs-params">numbers</span>) =></span> &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < numbers.length - <span class="hljs-number">1</span>; i++) &#123;
                <span class="hljs-keyword">let</span> index = minIndex(numbers.slice(i)) + i
                <span class="hljs-keyword">if</span> (index !== i) &#123;
                    swap(numbers, index, i)
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> numbers
        &#125;

        <span class="hljs-keyword">let</span> swap = <span class="hljs-function">(<span class="hljs-params">array, i, j</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> temp = array[i]
            array[i] = array[j]
            array[j] = temp
        &#125;
        <span class="hljs-keyword">let</span> minIndex = <span class="hljs-function">(<span class="hljs-params">numbers</span>) =></span> &#123;
                <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < numbers.length; i++) &#123;
                    <span class="hljs-keyword">if</span> (numbers[i] < numbers[index]) &#123;
                        index = i
                    &#125;
                &#125;
                <span class="hljs-keyword">return</span> index
            &#125;
            <span class="hljs-comment">//调用</span>
        sort([<span class="hljs-number">12</span>, <span class="hljs-number">5</span>, <span class="hljs-number">8</span>, <span class="hljs-number">7</span>, <span class="hljs-number">9</span>, <span class="hljs-number">77</span>, <span class="hljs-number">6</span>, <span class="hljs-number">33</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>时间复杂度：O(n^2) 空间复杂度：O(1) 稳定性：选择排序是不稳定的排序算法，因为无法保证值相等的元素的相对位置不变.</p>
<h2 data-id="heading-6">3.快速排序</h2>
<h4 data-id="heading-7">简介</h4>
<p>快速排序（quick sort）是公认最快的排序算法之一，有着广泛的应用。</p>
<p>它的基本思想很简单：先确定一个“支点”（pivot），将所有小于“支点”的值都放在该点的左侧，大于“支点”的值都放在该点的右侧，然后对左右两侧不断重复这个过程，直到所有排序完成。</p>
<h4 data-id="heading-8">算法实现</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> quickSort = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (arr.length <= <span class="hljs-number">1</span>) &#123;
                <span class="hljs-keyword">return</span> arr
            &#125;
            <span class="hljs-keyword">let</span> pivotIndex = <span class="hljs-built_in">Math</span>.floor(arr.length / <span class="hljs-number">2</span>) <span class="hljs-comment">//pivotIndex基准</span>
            <span class="hljs-keyword">let</span> pivot = arr.splice(pivotIndex, <span class="hljs-number">1</span>)[<span class="hljs-number">0</span>]
            <span class="hljs-keyword">let</span> left = []
            <span class="hljs-keyword">let</span> right = []
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
                <span class="hljs-keyword">if</span> (arr[i] < pivot) &#123;
                    left.push(arr[i])
                &#125; <span class="hljs-keyword">else</span> &#123;
                    right.push(arr[i])
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> quickSort(left).concat(
                [pivot], quickSort(right))
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>时间复杂度：平均O(nlogn)，最坏O(n2)，实际上大多数情况下小于O(nlogn) 空间复杂度:O(logn)（递归调用消耗） 稳定性：不稳定，无法保证相等的元素的相对位置不变</p>
<h2 data-id="heading-9">4.归并排序</h2>
<h4 data-id="heading-10">简介</h4>
<p>它的基本思想是，将两个已经排序的数组合并，要比从头开始排序所有元素来得快。因此，可以将数组拆开，分成n个只有一个元素的数组，然后不断地两两合并，直到全部排序完成。</p>
<h4 data-id="heading-11">算法实现</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> mergeSort = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> &#123;
            <span class="hljs-keyword">let</span> k = arr.length
            <span class="hljs-keyword">if</span> (k === <span class="hljs-number">1</span>) &#123;
                <span class="hljs-keyword">return</span> arr
            &#125;
            <span class="hljs-keyword">let</span> left = arr.slice(<span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.floor(k / <span class="hljs-number">2</span>))
            <span class="hljs-keyword">let</span> right = arr.slice(<span class="hljs-built_in">Math</span>.floor(k / <span class="hljs-number">2</span>))
            <span class="hljs-keyword">return</span> merge(mergrSort(left), mergeSort(right))
        &#125;
        <span class="hljs-keyword">let</span> merge = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (a.length === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> b
            <span class="hljs-keyword">if</span> (b.length === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> a
            <span class="hljs-keyword">return</span> a[<span class="hljs-number">0</span>] > b[<span class="hljs-number">0</span>] ? [b[<span class="hljs-number">0</span>]].concat(merge(a, b.slice(<span class="hljs-number">1</span>))) : [a[<span class="hljs-number">0</span>]].concat(merge(a.slice(<span class="hljs-number">1</span>), b))
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>时间复杂度：O(nlogn)，递归劈成两半logn,循环n次，所以nlogn 空间复杂度:O(n) 稳定性：归并排序是稳定的排序算法</p>
<h2 data-id="heading-12">5.计数排序</h2>
<h4 data-id="heading-13">简介</h4>
<p>计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。</p>
<h4 data-id="heading-14">算法实现</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> countSort = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> &#123;
                <span class="hljs-keyword">let</span> hashTable = &#123;&#125;,
                    max = <span class="hljs-number">0</span>,
                    result = []
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
                    <span class="hljs-keyword">if</span> (!(arr[i] <span class="hljs-keyword">in</span> hashTable)) &#123;
                        hashTable[arr[i]] = <span class="hljs-number">1</span>
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        hashTable[arr[i]] += <span class="hljs-number">1</span>
                    &#125;
                    <span class="hljs-keyword">if</span> (arr[i] > max) &#123;
                        max = arr[i]
                    &#125;
                &#125; <span class="hljs-comment">//遍历数组，找出最大值</span>

                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j <= max; j++) &#123;
                    <span class="hljs-keyword">if</span> (j <span class="hljs-keyword">in</span> hashTable) &#123;
                        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < hashTable[j]; i++) &#123;
                            result.push(j)
                        &#125;
                    &#125;
                &#125;
                <span class="hljs-keyword">return</span> result
            &#125; <span class="hljs-comment">//遍历哈希表，如果在就打出来</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>时间复杂度：n+max</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            