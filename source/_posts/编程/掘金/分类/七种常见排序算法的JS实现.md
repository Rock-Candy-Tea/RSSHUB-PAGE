
---
title: '七种常见排序算法的JS实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2797'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 18:51:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=2797'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>1.冒泡排序</p>
<pre><code class="copyable">// 交换函数
function swap(arr, i, j) &#123;
    var temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr
&#125;

// 1.冒泡排序
function bubbleSort(nums) &#123;
    let len = nums.length
    if (len == 0 || len == 1) return nums
    // 从 len-1 遍历到 1 的位置
    for (let i = len - 1; i > 0; i--) &#123;
        // j从 0 遍历到 i-1 的位置
        for (let j = 0; j < i; j++) &#123;
            // 和 j+1 的元素进行比较
            if (nums[j] > nums[j + 1]) &#123;
                swap(nums, j, j + 1)
            &#125;
        &#125;
    &#125;
    return nums
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.选择排序</p>
<pre><code class="copyable">// 2.选择排序：选择未排序元素中的最小值和当前位（从左往右遍历）元素进行交换
function selectSort(nums) &#123;
    var len = nums.length
    if (len == 0 || len == 1) return nums
    // 从左到右遍历每一个位置（最后一个不用）
    var curPosition = 0
    for (let i = 0; i < len - 1; i++) &#123;
        // 选出从当前位置到最后一个元素中最小的元素并记录其索引index
        var min = nums[i]
        var index = i
        for (let j = i + 1; j < len; j++) &#123;
            if (nums[j] < min) &#123;
                min = nums[j]
                index = j
            &#125;
        &#125;
        // 交换当前位置元素和最小值所在的位置
        swap(nums, i, index)
    &#125;
    return nums
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.插入排序</p>
<pre><code class="copyable">// 3.插入排序：从左到右遍历每个位置，将当前位置元素插入到前面已排序数组的合适位置
function insertSort(nums) &#123;
    let len = nums.length
    if (len == 0 || len == 1) return nums
    // 从左到右遍历每一个位置（第一个可以除外）
    for (let i = 1; i < len; i++) &#123;
        // 和前面已经排好序的元素比较
        let j = i - 1
        while (j >= 0) &#123;
            if (nums[j + 1] < nums[j]) &#123;
                swap(nums, j, j + 1)
                j--
            &#125; else break // 否则就退出循环
        &#125;
    &#125;
    return nums
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.希尔排序</p>
<pre><code class="copyable">// 4.希尔排序：根据增量进行分组插入排序（多个增量需互质，且最后一个为1）
function shellSort(nums) &#123;
    var len = nums.length
    if (len == 0 || len == 1) return nums
    var gap = parseInt(len / 2) // 设置增量（步长）的初始值
    while (gap) &#123; // nlogn 次
        // 循环 步长 次
        for (let n = 0; n < gap; n++) &#123;
            var num = Math.ceil(len / gap) // 定义组数
            // 对间隔步长的元素进行插入排序
            // 从左到右遍历每一个位置（第一个可以除外）
            for (let i = gap; i < num + gap; i++) &#123;
                if (i < len) &#123; // 最后一组可能不是gap个
                    // 和前面已经排好序的元素比较
                    var j = i - gap
                    while (j >= n) &#123;
                        if (nums[j + gap] < nums[j]) &#123;
                            swap(nums, j, j + gap)
                            j -= gap
                        &#125; else break
                    &#125;
                &#125;
            &#125;
        &#125;
        gap = parseInt(gap / 2)
    &#125;
    return nums
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.归并排序</p>
<pre><code class="copyable">// 5.归并排序：分治
function mergeSort(nums) &#123;
    var len = nums.length
    if (len < 2) return nums
    var mid = Math.floor(len / 2)
    var left = nums.slice(0, mid) // 包括 begin，不包括end
    var right = nums.slice(mid) // 如果 end 被省略，则 slice 会一直提取到原数组末尾
    return merge(mergeSort(left), mergeSort(right))
&#125;
// 归并两个有序数组
function merge(left, right) &#123;
    var newArr = []
    while (left.length && right.length) &#123;
        if (left[0] <= right[0]) &#123;
            newArr.push(left.shift())
        &#125; else newArr.push(right.shift())
    &#125;
    return newArr.concat(left).concat(right)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6.快速排序</p>
<pre><code class="copyable">// 6.快速排序：分治、双指针；设置最左元素为基准点，右指针先动 // 内存不足
function quickSort(nums) &#123;
    var len = nums.length
    if (len == 0 || len == 1) return nums
    var piovt = nums[0] // 设置基准点的值为nums[0]
    var left = 0 // 设置左指针
    var right = len - 1 // 设置右指针
    while (left < right) &#123;
        // 右指针先动，找到比基准点小的元素
        if (nums[right] < piovt) &#123;
            // 再动左指针，找到比基准点大的元素
            if (nums[left] > piovt) &#123;
                // 进行交换
                swap(nums, left, right)
            &#125; else left++
        &#125; else right--
    &#125;
    if (left == right) &#123;
        swap(nums, 0, left)
    &#125;
    // 拼接字符串：对当前基准点元素的左边排序 + 基准点元素 + 对当前基准点元素的右边排序
    return quickSort(nums.slice(0, left)).concat(nums[left]).concat(quickSort(nums.slice(left + 1)))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7.堆排序</p>
<pre><code class="copyable">// 7.堆排序：
function heapSort(nums) &#123;
    var len = nums.length
    if (len < 2) return nums
    for (let i = len - 1; i >= 0; i--) &#123;
        // 1.将未排序部分的nums[0-i]调整为最大堆
        nums = adjustMaxHeap(nums, 0, i)
        // 2.交换堆顶和数组最后一个元素
        nums = swap(nums, 0, i)
    &#125;
    return nums
&#125;
// 构建最大堆
function adjustMaxHeap(nums, start, end) &#123; // 为了不浪费新的内存空间，新增end参数，保证后面已经排好的元素可以保留
    var left = 2 * start + 1 // 左节点
    var right = 2 * start + 2 // 右节点
    // 如果当前节点是不是根节点
    if (left > end) return nums
    // 如果当前节点是根节点，调整他的左右子节点为最大堆
    adjustMaxHeap(nums, left, end)
    right <= end && adjustMaxHeap(nums, right, end)

    // 先和左节点比较
    if (nums[start] < nums[left]) &#123;
        swap(nums, start, left)
    &#125;
    // 如果有右节点还需要和右节点进行比较
    if (right <= end && nums[start] < nums[right]) &#123;
        swap(nums, start, right)
    &#125;
    return nums
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            