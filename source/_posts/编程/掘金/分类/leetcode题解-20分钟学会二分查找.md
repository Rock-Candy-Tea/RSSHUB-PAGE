
---
title: 'leetcode题解-20分钟学会二分查找'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e395791401b24ca68d55ba51238f36ca~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 18:02:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e395791401b24ca68d55ba51238f36ca~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e395791401b24ca68d55ba51238f36ca~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>今天介绍下二分查找这个算法套路，学会此招，你的内力会精进三分，与路边程序员能立马拉开差距！</p>
<h4 data-id="heading-0">题目描述</h4>
<p>整数数组 nums 按升序排列，数组中的值 互不相同 。</p>
<p>在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。</p>
<p>给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。</p>
<p><strong>示例 1：</strong></p>
<pre><code class="copyable">输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<pre><code class="copyable">输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 3：</strong></p>
<pre><code class="copyable">输入：nums = [1], target = 0
输出：-1
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示：</strong></p>
<ul>
<li>1 <= nums.length <= 5000</li>
<li>-10^4 <= nums[i] <= 10^4</li>
<li>nums 中的每个值都 独一无二</li>
<li>题目数据保证 nums 在预先未知的某个下标上进行了旋转</li>
<li>-10^4 <= target <= 10^4</li>
</ul>
<p>**进阶：**你可以设计一个时间复杂度为 O(log n) 的解决方案吗？</p>
<h4 data-id="heading-1">题解</h4>
<p>这题看着简单，因为常规解法很容易想到，直接暴力遍历就可以了。看代码：</p>
<pre><code class="copyable">/**
 * @param &#123;number[]&#125; nums
 * @param &#123;number&#125; target
 * @return &#123;number&#125;
 */
var search = function(nums, target) &#123;
    var res = -1
    for(var i = 0; i <nums.length; i++) &#123;
        if(nums[i] === target) &#123;
            res = i
            return res;
        &#125;
    &#125;
    return res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种解法的时间复杂度是O(n);</p>
<p>此题还有更好的解法：二分查找！它的时间复杂度是O(logn)，题目中也提到了这个，向我们发起了挑战！来看如何接招吧！</p>
<p>先介绍下二分查找这个算法，非常适合这种题目。这是有一定套路的解法，主要就是约定几个索引位，从数组两头向中间进行夹逼推进，最终找到目标值。而在每次推进过程中都会舍弃掉当前资源中的一半，这样算下去，最终的时间复杂度就是O(logn)。它的套路解法还有一个代码模板，适合初学的人理解记忆：</p>
<pre><code class="copyable">left,right = 0,len(array) -1
while left<= right;
 mid = (left + right)/2
 if array[mid] == target;
  #find the target!!
        break or return result
 elif array[mid]< target:
     left = mid + 1
 else:
     right = mid - 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单解释就是，初始变量设置数组的一头一尾的索引位置，然后取其中间位置，这个中间位置就可以将数组分为两段，接着去判断目标值所在的大概位置，同时调整查找范围，这样不断的排除查找，最终锁定目标值。</p>
<p>落到此题目中来，原本的一个顺序数组在某个位置旋转了，这样一来，取了中间值之后，左侧部分可能是有序的，也可能是包含旋转点即无序的。如果左侧有序，就判断目标值是否在左侧范围，不在就把左索引移至mid + 1；如果左侧无序，就判断目标值是否在左侧范围，不在就把左索引移至 mid + 1;其他情况（即目标值在左侧范围）就移动右索引至mid；这样不断夹逼，头尾两个索引位会不断逼近目标值，直到他们相遇，此时目标值也好判断了。js要考虑特殊情况，因为最后推到只有两个元素时，算出来的mid是0；这时直接判断两个元素是否匹配就可以了，不纠结！</p>
<pre><code class="copyable">/**
 * @param &#123;number[]&#125; nums
 * @param &#123;number&#125; target
 * @return &#123;number&#125;
 */
var search = function(nums, target) &#123;
    var lo = 0,hi = nums.length -1;
    while(lo < hi)&#123;
        var mid = parseInt((lo + hi)/2);
        if(nums[mid] === target) return mid;
        if(nums[mid + 1] === target) return mid+1;
        if(nums[0] < nums[mid] && (target > nums[mid] || target < nums[0]))&#123;
            lo = mid + 1;
        &#125; else if (target > nums[mid]&&target < nums[0])&#123;
            lo = mid + 1;
        &#125; else &#123;
            hi = mid;
        &#125;
    &#125;
    return nums[lo] == target ? lo : -1;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">复杂度分析</h4>
<p><strong>时间复杂度：</strong> 由于每次都会砍掉当前元素的一半，最终逼近目标值，这个复杂度就是O(logn)</p>
<p><strong>空间复杂度：</strong> 由于mid每次遍历都会变，所以这个只能每次都存下来，这个复杂度也是O(logn)</p>
<p>题目来源：力扣（LeetCode）
链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fsearch-in-rotated-sorted-array" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/search-in-rotated-sorted-array" ref="nofollow noopener noreferrer">leetcode-cn.com/problems/se…</a></p></div>  
</div>
            