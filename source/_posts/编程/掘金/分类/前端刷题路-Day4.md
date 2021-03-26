
---
title: '前端刷题路-Day4'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6704'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 16:26:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=6704'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">两两交换链表中的节点（题号24）</h3>
<h4 data-id="heading-1">题目</h4>
<p>给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。</p>
<p>你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。</p>
<p>示例 1：</p>
<pre><code class="copyable">输入：head = [1,2,3,4]
输出：[2,1,4,3]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<pre><code class="copyable">输入：head = []
输出：[]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 3：</p>
<pre><code class="copyable">输入：head = [1]
输出：[1]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<ul>
<li>链表中节点的数目在范围 [0, 100] 内</li>
<li>0 <= Node.val <= 100</li>
</ul>
<h4 data-id="heading-2">链接</h4>
<p><a href="https://leetcode-cn.com/problems/swap-nodes-in-pairs/" target="_blank" rel="nofollow noopener noreferrer">leetcode-cn.com/problems/sw…</a></p>
<h4 data-id="heading-3">解释</h4>
<p>这一题还好，根据昨天写的反转链表，使用了递归的方法来进行操作，没啥可说的，主要是更好的答案，这里采用的是迭代，反正我是没太看懂，以后有时间可以看看</p>
<h4 data-id="heading-4">自己的解法</h4>
<pre><code class="copyable">var swapPairs = function(head) &#123;
  if (!head || !head.next) return head
  var dummy = head.next
  if (dummy.next) dummy.next = swapPairs(dummy.next)
  head.next = dummy.next
  dummy.next = head
  head = dummy
  return head
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">更好的答案</h4>
<pre><code class="copyable">var swapPairs = function(head) &#123;
  // 1. 确认 head 大于等于两个，否则返回;
  if (!head || !head.next) return head;
  // 2. 新建链表哨兵头并创建指针curr；
  let res = new ListNode(null);
  res.next = head;
  let prev = res;
  console.log(prev)
  // 3. 循环开始
  //    3.1 走两步，存为fst, snd;
  //    3.2 哨兵->snd, fst->snd.next, snd->fst;
  //    3.3 推进 curr = curr.next.next;
  while (prev.next && prev.next.next) &#123;
    let [fst, snd] = [prev.next, prev.next.next];
    [prev.next, fst.next, snd.next] = [snd, snd.next, fst];
    prev = prev.next.next;
  &#125;
  // 4. 返回res.next;
  return res.next;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">环形链表（题号141）</h3>
<h4 data-id="heading-7">题目</h4>
<p>给定一个链表，判断链表中是否有环。</p>
<p>如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。   为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。<br>
如果 pos 是 -1，则在该链表中没有环。<br>
注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。<br>
如果链表中存在环，则返回 true 。 否则，返回 false 。</p>
<p>进阶：</p>
<ul>
<li>你能用 O(1)（即，常量）内存解决此问题吗？</li>
</ul>
<p>示例 1：</p>
<pre><code class="copyable">输入：head = [3,2,0,-4], pos = 1  
输出：true  
解释：链表中有一个环，其尾部连接到第二个节点。 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例2：</p>
<pre><code class="copyable">输入：head = [1,2], pos = 0  
输出：true  
解释：链表中有一个环，其尾部连接到第一个节点。  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 3：</p>
<pre><code class="copyable">输入：head = [1], pos = -1  
输出：false  
解释：链表中没有环。  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<ul>
<li>链表中节点的数目范围是 [0, 104]</li>
<li>-105 <= Node.val <= 105</li>
<li>pos 为 -1 或者链表中的一个 有效索引 。</li>
</ul>
<h4 data-id="heading-8">链接</h4>
<p><a href="https://leetcode-cn.com/problems/linked-list-cycle/solution/jsshi-xian-si-chong-fang-fa-by-careteenl/" target="_blank" rel="nofollow noopener noreferrer">leetcode-cn.com/problems/li…</a></p>
<h4 data-id="heading-9">解释</h4>
<p>这题首先是想到了一种诡异无比的写法，直接使用<code>JSON.stringify(head)</code>来判断，如果是循环，会报错，然后捕获错误就好，非常简单方便，就是性能堪忧，只能超过5%的人。</p>
<p>第二种解法就比较正常了，使用了迭代的方法，把每个结点的<code>next</code>都存在<code>Map</code>中，之后开始循环，如果<code>Map</code>中已经存在该节点，那就证明已经循环了，直接返回<code>true</code>，碰到<code>null</code>就返回<code>false</code>。</p>
<p>更好的解法其实是双指针迭代，第一种是其实更多的是类似单指针的操作，简单来说就是两个人跑步，一个人先出发，另一个人后触发，如果是一个圈，那么先出发的人必然会遇到后出发的人，也就是它超过第一个人一圈的时候。</p>
<p>第二种更好的解法就是双指针，两个人同时出发，一个人跑的快，一个人跑得慢，是上一种方法的小优化吧，看上去更简洁，运行起来也快一丢丢。</p>
<h4 data-id="heading-10">自己的解法1</h4>
<pre><code class="copyable">var hasCycleSpecial = function(head) &#123;
  try &#123;
    JSON.stringify(head)
    return false
  &#125; catch(err) &#123;
    return !!err
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">自己的解法2</h4>
<pre><code class="copyable">var hasCycle = function(head) &#123;
  if (!head || !head.next) return false
  var res = head;
  var obj = new Map
  var ans = false
  while (res) &#123;
    if (obj.has(res)) &#123;
      ans = true
      res = null
    &#125; else &#123;
      obj.set(res, 1)
      res = res.next  
    &#125;
  &#125;
  return ans
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">更好的答案1</h4>
<pre><code class="copyable">var hasCycle = function(head) &#123;
  if (!head || !head.next) return false
  var fast = head.next
  var slow = head
  while (fast !== slow) &#123;
    if (!fast || !fast.next) &#123;
      return false
    &#125;
    fast = fast.next.next
    slow = slow.next
  &#125;
  return true
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">更好的答案2</h4>
<pre><code class="copyable">var hasCycle4 = function (head) &#123;
  var slow = head,
    fast = head
  while (fast && fast.next) &#123;
    slow = slow.next
    fast = fast.next.next
    if (slow == fast) return true
  &#125;
  return false
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            