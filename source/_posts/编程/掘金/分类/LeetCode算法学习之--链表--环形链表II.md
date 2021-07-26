
---
title: 'LeetCode算法学习之--链表--环形链表II'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/314c48b3959e43888b53d2d4cf2ed6a1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 02:26:31 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/314c48b3959e43888b53d2d4cf2ed6a1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好今天给大家分享下一道 LeetCode  中间难度 的题目<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Flinked-list-cycle-ii%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/linked-list-cycle-ii/" ref="nofollow noopener noreferrer">环形链表 II</a></p>
<blockquote>
<p>这里主要是分享思路和注释，供大家更好的理解题目解法，代码部分是参考LeetCode 转写成javascript 代码，</p>
</blockquote>
<h4 data-id="heading-0">题目</h4>
<blockquote>
<p>给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。</p>
<p>为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。</p>
<p>说明：不允许修改给定的链表。</p>
<p>进阶：</p>
<p>你是否可以使用 O(1) 空间解决此题？</p>
</blockquote>
<blockquote>
<pre><code class="hljs language-markdown copyable" lang="markdown">示例1
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

示例2
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h4 data-id="heading-1">分析</h4>
<blockquote>
<p><em>本体是延续 环形链表的进阶题，关键点就是如何判断入环的第一个点</em></p>
<p><em>解法有2中</em></p>
<p><em>1.Map法</em></p>
<p><em>2.指针法</em></p>
</blockquote>
<h4 data-id="heading-2">解法一：<strong>Map 法</strong></h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">思路
<span class="hljs-number">1.</span>路过的节点都记录下来
<span class="hljs-number">2.</span>因为map是从前向后记录的，所以如果有出现访问过的节点
该节点一定是第入环的第一个节点
*/

<span class="hljs-keyword">var</span> detectCycle = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">head</span>) </span>&#123;
  <span class="hljs-comment">// 首先排除特殊条件例如： [] 或者 [1]</span>
  <span class="hljs-keyword">if</span> (head === <span class="hljs-literal">null</span> || head.next === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  &#125;

  <span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
  <span class="hljs-keyword">let</span> cur = head;
  <span class="hljs-keyword">while</span> (cur !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-comment">//如果存在 则一定是第一个节点</span>
    <span class="hljs-keyword">if</span> (map.get(cur)) &#123;
      <span class="hljs-keyword">return</span> map.get(cur);
    &#125;

    <span class="hljs-comment">// 记录每一个节点 从前往后</span>
    map.set(cur, cur);
    cur = cur.next;
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;;
<span class="hljs-comment">/* 复杂度
时间 O(n)
空间 O(n)
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/314c48b3959e43888b53d2d4cf2ed6a1~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">解法二：<em>双指针法</em></h4>
<p>代码借鉴 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Flinked-list-cycle-ii%2Fsolution%2Fhuan-xing-lian-biao-ii-by-leetcode-solution%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/" ref="nofollow noopener noreferrer">leetcode-cn.com/problems/li…</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">思路
假定从头到入口的距离是i步
从入口到快慢指针重合的位置是j步
从重合位置再走k步回到重合点

所以 从环内任何一个点出发走（j+k）都会回到原点

<span class="hljs-number">1.</span>首先快指针（f）的走的步数一定是 慢指针（s）的两倍
<span class="hljs-number">2.</span>当快指针f与s重合的时候
    <span class="hljs-number">1.</span>快指针走的距离是f=a+n(b+c)+b;
    <span class="hljs-number">2.</span>慢指针走的距离是s=a+k(b+c)+b;
    <span class="hljs-number">3.</span>由于快指针是慢指针距离的<span class="hljs-number">2</span>倍 
    所以可以得出 2a+2k(b+c)+2b=a+n(b+c)+<span class="hljs-function"><span class="hljs-params">b</span>=></span>  a=-(2k-n+<span class="hljs-number">1</span>)(b+c)+c
    <span class="hljs-number">4.</span>通过上面的等式我们可以得知，从头走a步的点=== s 从重合点走c步的点，但是a 和c是未知，
    所以我们可以利用重合相撞的办法得到入口点
    <span class="hljs-number">5.</span>放一个指针在头部，和s同时走，当相遇的时候就说明到达了环的入口点

*/
<span class="hljs-keyword">var</span> detectCycle = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">head</span>) </span>&#123;
  <span class="hljs-comment">// 首先排除特殊条件 [] [1]</span>
  <span class="hljs-keyword">if</span> (head === <span class="hljs-literal">null</span> || head.next === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  &#125;

  <span class="hljs-keyword">let</span> f = head;
  <span class="hljs-keyword">let</span> s = head;
  <span class="hljs-keyword">while</span> (f !== <span class="hljs-literal">null</span> && f.next !== <span class="hljs-literal">null</span>) &#123;
    f = f.next.next; <span class="hljs-comment">//快指针一次走2步</span>
    s = s.next; <span class="hljs-comment">//慢指针一次走一步</span>

    <span class="hljs-comment">// 如果相遇说明有环</span>
    <span class="hljs-keyword">if</span> (f === s) &#123;
      <span class="hljs-comment">// 设置一个指针指向头部</span>
      <span class="hljs-keyword">let</span> extra = head;
      <span class="hljs-comment">// 当重合相撞的时候就说明到达了环的入口点</span>
      <span class="hljs-keyword">while</span> (extra !== s) &#123;
        <span class="hljs-comment">//extra一步一步从头开始走</span>
        extra = extra.next;
        <span class="hljs-comment">// s 从重合点也一步一步走</span>
        s = s.next;
      &#125;
      <span class="hljs-keyword">return</span> s;
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;;

<span class="hljs-comment">/* 复杂度
时间 O(n)
空间 O(1)
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eafb82bfb2224d6e802fe86d38fae382~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">总结</h4>
<p>这道题是中等难度的题，Hash很好理解，但是双指针需要多推导。</p>
<p>大家可以看看我分享的一个专栏（<a href="https://juejin.cn/column/6984791578099335204" target="_blank" title="https://juejin.cn/column/6984791578099335204">前端搞算法</a>）里面有更多关于算法的题目的分享，希望能够帮到大家，我会尽量保持每天晚上更新，如果喜欢的麻烦帮我点个赞，十分感谢</p>
<p><em>文章内容目的在于学习讨论与分享学习算法过程中的心得体会，文中部分素材来源网络，如有侵权，请联系删除，邮箱 <a href="https://link.juejin.cn/?target=mailto%3A182450609%40qq.com" target="_blank" title="mailto:182450609@qq.com" ref="nofollow noopener noreferrer">182450609@qq.com</a></em></p>
<p><strong>昨天去支持了鸿星尔克和蜜雪冰城，今天又去支持了汇源果汁，哈哈哈，对于良心企业及必须得给他们打打广告。郑州加油！河南加油！中国加油！</strong></p></div>  
</div>
            