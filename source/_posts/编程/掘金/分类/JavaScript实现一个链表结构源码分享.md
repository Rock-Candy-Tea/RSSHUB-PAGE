
---
title: 'JavaScript实现一个链表结构源码分享'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b68788a77bba47c7904958b9a4c085b0~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 22:44:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b68788a77bba47c7904958b9a4c085b0~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0"><a href="https://juejin.cn/post/6943478944347717662"></a>写在前面</h4>
<blockquote>
<p>刷题的时候看到一个关于链表的题目，写了一会发现写不出来，所以干脆就将链表的知识使用js重现一遍，这里写一个js实现的链表。</p>
</blockquote>
<h4 data-id="heading-1"><a href="https://juejin.cn/post/6943478944347717662"></a>链表结构介绍</h4>
<blockquote>
<p>没有写代码之前呢我们先简单的说一下什么是链表，我们都知道，在很多的数据结构中，有序的结构我们比较熟悉是数组，数组和链表还有一些不同，数组是内存空间按照挨个顺序来的，那么链表的话是可以不按照顺序来的,链表结构是当前元素（data），下一个元素(next)，上一个元素(pre)，第一位是head，最后一位的next指向null 链表分为下面几种常见的！</p>
</blockquote>
<ul>
<li>单向链表</li>
</ul>
<blockquote>
<p>每一个节点的next都指向下一个节点，最后一个节点的next指向的是null<br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b68788a77bba47c7904958b9a4c085b0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</blockquote>
<ul>
<li>双向链表</li>
</ul>
<blockquote>
<p>每一个节点都有一个next和pre，相互指向就形成了双向链表<br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bec03cbef2b4d4495425575243524b8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</blockquote>
<ul>
<li>单向循环链表</li>
</ul>
<blockquote>
<p>单向链表的最后一个节点指向了该链表的第一个节点<br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e24e5a4bf0d043c494a246ca8cb24542~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</blockquote>
<ul>
<li>双向循环链表</li>
</ul>
<blockquote>
<p>第一个节点的pre指向了该链表的最后一个，该链表的最后一个next指向了第一个节点<br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ca0aa74a953447dbadf6c5d742c0e55~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</blockquote>
<ul>
<li>环形链表</li>
</ul>
<blockquote>
<p>任意两个节点之间形成了pre和next相互指向的情况，都可以叫做环形链表<br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b048b100af2b48c5b601877d4fd6c645~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</blockquote>
<h4 data-id="heading-2"><a href="https://juejin.cn/post/6943478944347717662"></a>源码实现</h4>
<blockquote>
<p>我们使用js实现一个简单的单向链表，提供一种思路出来</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@class </span>Node   当前节点
 * <span class="hljs-doctag">@class </span>LinkedList 当前链表
 * <span class="hljs-doctag">@function </span>appendNode  添加节点
 * <span class="hljs-doctag">@function </span>getNode  根据索引查找节点元素
 * <span class="hljs-doctag">@function </span>appendAt  根据位置插入节点
 * <span class="hljs-doctag">@function </span>remove    移除节点
 * <span class="hljs-doctag">@function </span>searchCurrIndexof 根据元素查找索引
 * <span class="hljs-doctag">@function </span>sort  链表排序
 * <span class="hljs-doctag">@function </span>linkedToArr 链表转为数组
 * <span class="hljs-doctag">@function </span>arrToLinked 数组转为链表
 * 
 */</span>
<span class="hljs-comment">//声明一个Node节点</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Node</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">data</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.data = data
        <span class="hljs-built_in">this</span>.next = <span class="hljs-literal">null</span>
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LinkedList</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.size = <span class="hljs-number">0</span>
            <span class="hljs-built_in">this</span>.head = <span class="hljs-literal">null</span>
        &#125;
        <span class="hljs-comment">//增加一个节点</span>
    <span class="hljs-function"><span class="hljs-title">appendNode</span>(<span class="hljs-params">tempNode</span>)</span> &#123;
            <span class="hljs-keyword">let</span> node = <span class="hljs-keyword">new</span> Node(tempNode)
                <span class="hljs-comment">//判断一下当前的链表是不是一个空的 this.head === null 或者是当前的链表的长度为0</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.head === <span class="hljs-literal">null</span>) &#123;
                <span class="hljs-comment">//如果是空的，那么我们的当前的节点就是第一位</span>
                <span class="hljs-built_in">this</span>.head = node
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">//如果不是空的，我们要做的是，将当前的节点追加到当前链表的最后一位的后面，</span>
                <span class="hljs-comment">//也就是我们首先需要找到当前链表的最后一位，让后将他的next给当前的node</span>
                <span class="hljs-keyword">let</span> current = <span class="hljs-built_in">this</span>.getNode(<span class="hljs-built_in">this</span>.size - <span class="hljs-number">1</span>) <span class="hljs-comment">//找到当前的最后一位</span>
                current.next = node
            &#125;
            <span class="hljs-comment">//链表的长度追加</span>
            <span class="hljs-built_in">this</span>.size++
        &#125;
        <span class="hljs-comment">//找到当前一个 的节点</span>
    <span class="hljs-function"><span class="hljs-title">getNode</span>(<span class="hljs-params">index</span>)</span> &#123;
            <span class="hljs-keyword">if</span> (index < <span class="hljs-number">0</span> || index >= <span class="hljs-built_in">this</span>.size) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'error'</span>)
            &#125;
            <span class="hljs-keyword">let</span> current = <span class="hljs-built_in">this</span>.head
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < index; i++) &#123;
                current = current.next
            &#125;
            <span class="hljs-keyword">return</span> current
        &#125;
        <span class="hljs-comment">//按照指定位置增加</span>
    <span class="hljs-function"><span class="hljs-title">appendAt</span>(<span class="hljs-params">position, tempNode</span>)</span> &#123;
            <span class="hljs-comment">//首先要知道当前的位置是不是小于0  或者是大于当前链表的长度</span>
            <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position > <span class="hljs-built_in">this</span>.size) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'error'</span>)
            &#125;
            <span class="hljs-keyword">let</span> node = <span class="hljs-keyword">new</span> Node(tempNode)
            <span class="hljs-keyword">if</span> (position === <span class="hljs-number">0</span>) &#123;
                <span class="hljs-comment">//从第一位开始追加，说明我们需要将当前的node的下一位等于之前的第一位，再将head等于当前的node</span>
                node.next = <span class="hljs-built_in">this</span>.head
                <span class="hljs-built_in">this</span>.head = node
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">//如果当前位置插入一个节点，需要做的就是将插入位置的之前节点的位置找到即可</span>
                <span class="hljs-keyword">let</span> pre = <span class="hljs-built_in">this</span>.getNode(position - <span class="hljs-number">1</span>)
                node.next = pre.next
                pre.next = node
            &#125;
            <span class="hljs-built_in">this</span>.size++
        &#125;
        <span class="hljs-comment">//删除指定节点的元素</span>
    <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">position</span>)</span> &#123;
        <span class="hljs-comment">//首先要知道当前的位置是不是小于0  或者是大于当前链表的长度</span>
        <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position > <span class="hljs-built_in">this</span>.size) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'error'</span>)
        &#125;
        <span class="hljs-comment">//先将当前头部节点找到</span>
        <span class="hljs-keyword">let</span> currentHead = <span class="hljs-built_in">this</span>.head
        <span class="hljs-keyword">if</span> (position === <span class="hljs-number">0</span>) &#123;
            <span class="hljs-comment">//说明当前我要删除的是第一位的节点,那么更新头部的信息为之前的节点的next</span>
            <span class="hljs-built_in">this</span>.head = currentHead.next
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">//如果链表中的某一个节点的删除的时候，我们需要做的就是找到删除的节点的前一个节点，然后将前一个节点的next等于被删除的节点的next</span>
            <span class="hljs-keyword">let</span> pre = <span class="hljs-built_in">this</span>.getNode(position - <span class="hljs-number">1</span>)
            currentHead = pre.next
            pre.next = currentHead.next
        &#125;
        <span class="hljs-built_in">this</span>.size--
    &#125;

    <span class="hljs-comment">//按照指定元素的索引</span>
    <span class="hljs-function"><span class="hljs-title">searchCurrIndexof</span>(<span class="hljs-params">tempNode</span>)</span> &#123;
            <span class="hljs-comment">//从头部开始找</span>
            <span class="hljs-keyword">let</span> current = <span class="hljs-built_in">this</span>.head
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < <span class="hljs-built_in">this</span>.size; i++) &#123;
                <span class="hljs-keyword">if</span> (current.data === tempNode) &#123;
                    <span class="hljs-keyword">return</span> i
                &#125;
                current = current.next
            &#125;
            <span class="hljs-comment">//完全找不到的时候我们直接返回-1或者false都可以</span>
            <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
        &#125;
        <span class="hljs-comment">//排序</span>
    <span class="hljs-function"><span class="hljs-title">sort</span>(<span class="hljs-params">tempLinked</span>)</span> &#123;
            <span class="hljs-keyword">let</span> tempArr = <span class="hljs-built_in">this</span>.linkedToArr(tempLinked)
            <span class="hljs-keyword">let</span> maxL = tempArr.length - <span class="hljs-number">1</span>
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < maxL; ++j) &#123;
                <span class="hljs-keyword">let</span> flag = <span class="hljs-literal">true</span>
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < maxL - j; ++i) &#123;
                    <span class="hljs-keyword">if</span> (tempArr[i] > tempArr[i + <span class="hljs-number">1</span>]) &#123;
                        <span class="hljs-keyword">let</span> temp = tempArr[i]
                        tempArr[i] = tempArr[i + <span class="hljs-number">1</span>]
                        tempArr[i + <span class="hljs-number">1</span>] = temp
                        flag = <span class="hljs-literal">false</span>
                    &#125;
                &#125;
                <span class="hljs-keyword">if</span> (flag) &#123;
                    <span class="hljs-keyword">break</span>
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.arrToLinked(tempArr)
        &#125;
        <span class="hljs-comment">//链表转为数组</span>
    <span class="hljs-function"><span class="hljs-title">linkedToArr</span>(<span class="hljs-params">tempLinked</span>)</span> &#123;
            <span class="hljs-keyword">let</span> result = []
            <span class="hljs-keyword">let</span> headNode = tempLinked.head
            <span class="hljs-keyword">while</span> (headNode) &#123;
                result.push(headNode.data)
                headNode = headNode.next
            &#125;
            <span class="hljs-keyword">return</span> result
        &#125;
        <span class="hljs-comment">//数组转为链表</span>
    <span class="hljs-function"><span class="hljs-title">arrToLinked</span>(<span class="hljs-params">tempArr</span>)</span> &#123;
        <span class="hljs-keyword">let</span> ll = <span class="hljs-keyword">new</span> LinkedList()
        tempArr.map(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            ll.appendNode(res)
        &#125;)
        <span class="hljs-keyword">return</span> ll
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3"><a href="https://juejin.cn/post/6943478944347717662"></a>测试结果</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//测试</span>
<span class="hljs-keyword">let</span> ll = <span class="hljs-keyword">new</span> LinkedList()
ll.appendNode(<span class="hljs-number">1</span>)
ll.appendNode(<span class="hljs-number">2</span>)
ll.appendNode(<span class="hljs-number">3</span>)
ll.appendAt(<span class="hljs-number">3</span>, <span class="hljs-string">'jim'</span>)
ll.appendNode(<span class="hljs-number">4</span>)
<span class="hljs-comment">//这里是为了将结果全部展开，所以序列化一下</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.stringify(ll))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4"><a href="https://juejin.cn/post/6943478944347717662"></a>最后</h4>
<blockquote>
<p>链表可能说我们平常用的不是很多，但是这是一种很好的思路，我觉得还是很有必要了解和学习一下的，毕竟很多的数据结构都是从一些简单的结构进行开展思维的。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            