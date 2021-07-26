
---
title: '什么是归并排序 mergeSort'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e1a010153724938884a159e52e76ce8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 00:19:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e1a010153724938884a159e52e76ce8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. 什么是归并排序？</h3>
<p>归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。</p>
<p>作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：</p>
<ul>
<li>自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；</li>
<li>自下而上的迭代；</li>
</ul>
<p>在《数据结构与算法 JavaScript 描述》中，作者给出了自下而上的迭代方法。但是对于递归法，作者却认为：</p>
<blockquote>
<p>However, it is not possible to do so in JavaScript, as the recursion goes too deep for the language to handle.</p>
<p>然而，在 JavaScript 中这种方式不太可行，因为这个算法的递归深度对它来讲太深了。</p>
</blockquote>
<p>和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是 O(nlogn) 的时间复杂度。代价是需要额外的内存空间。</p>
<h3 data-id="heading-1">2. 算法步骤</h3>
<p>归并排序使用<strong>分而治之</strong>的概念对给定的元素列表进行排序。它将问题分解为较小的子问题，直到它们变得足够简单以至可以直接解决为止。</p>
<p>以下是归并排序的步骤：</p>
<ol>
<li>将给定的列表分为两半（如果列表中的元素数为奇数，则使其大致相等）。</li>
<li>以相同的方式继续划分子数组，直到只剩下单个元素数组。</li>
<li>从单个元素数组开始，<strong>合并</strong>子数组，以便对每个合并的子数组进行排序。</li>
<li>重复第 3 步单元，直到最后得到一个排好序的数组。</li>
</ol>
<h3 data-id="heading-2">3. 动图演示</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e1a010153724938884a159e52e76ce8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-3">代码实现</h2>
<p>将两个已排序子数组合并为一个已排序数组的函数 <code>merge()</code></p>
<pre><code class="copyable">function merge(left, right) &#123;
    let arr = []
    // 如果任何一个数组为空，就退出循环
    while (left.length && right.length) &#123;
        // 从左右子数组的最小元素中选择较小的元素
        if (left[0] < right[0]) &#123;
            arr.push(left.shift())  
        &#125; else &#123;
            arr.push(right.shift()) 
        &#125;
    &#125;
    
    // 连接剩余的元素，防止没有把两个数组遍历完整
    return [ ...arr, ...left, ...right ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更完整的实现</p>
<pre><code class="copyable">function mergeSort(array) &#123;
  const half = array.length / 2
  
  if(array.length < 2)&#123;
    return array 
  &#125;
  
  const left = array.splice(0, half)
  return merge(mergeSort(left),mergeSort(array))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            