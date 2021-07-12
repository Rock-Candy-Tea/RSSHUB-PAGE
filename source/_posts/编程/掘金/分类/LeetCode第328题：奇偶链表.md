
---
title: 'LeetCode第328题：奇偶链表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5802'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 22:53:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=5802'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">题干</h2>
<p>给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。</p>
<p>请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。</p>
<p><strong>示例 1:</strong></p>
<pre><code class="copyable">输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2:</strong></p>
<pre><code class="copyable">输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来源：力扣（LeetCode）
链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fodd-even-linked-list" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/odd-even-linked-list" ref="nofollow noopener noreferrer">leetcode-cn.com/problems/od…</a>
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。</p>
<h2 data-id="heading-1">解法:合成链表</h2>
<p>这道题的解法和86题分隔链表时非常像的，我们依然使用两个左右链表进行筛选再进行连接就可以高效的完成这道题目。</p>
<p>代码实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Definition for singly-linked list.
 * function ListNode(val, next) &#123;
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;ListNode&#125;</span> <span class="hljs-variable">head</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;ListNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> oddEvenList = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">head</span>) </span>&#123;
    <span class="hljs-keyword">let</span> left = <span class="hljs-keyword">new</span> ListNode(-<span class="hljs-number">1</span>);
    <span class="hljs-keyword">let</span> Right = <span class="hljs-keyword">new</span> ListNode(-<span class="hljs-number">1</span>);
    <span class="hljs-keyword">let</span> leftCurrent = left;
    <span class="hljs-keyword">let</span> rightCurrent = Right;
    <span class="hljs-keyword">let</span> currentIndex = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">while</span> (head != <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">if</span> (currentIndex % <span class="hljs-number">2</span> != <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">let</span> node1 = <span class="hljs-keyword">new</span> ListNode(head.val);
            leftCurrent.next = node1;
            leftCurrent = leftCurrent.next;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">let</span> node2 = <span class="hljs-keyword">new</span> ListNode(head.val);
            rightCurrent.next = node2;
            rightCurrent = rightCurrent.next;
        &#125;
        head=head.next;
        currentIndex++;
    &#125;
    <span class="hljs-comment">// 拼接两奇偶链表</span>
    leftCurrent.next=Right.next;
    <span class="hljs-keyword">return</span> left.next
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            