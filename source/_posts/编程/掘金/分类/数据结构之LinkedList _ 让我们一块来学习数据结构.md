
---
title: '数据结构之LinkedList _ 让我们一块来学习数据结构'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1db262a0ba5c4f4194410db0bd0d3836~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Apr 2021 17:34:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1db262a0ba5c4f4194410db0bd0d3836~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://juejin.cn/post/6955266491012874270" target="_blank">数据结构之List | 让我们一块来学习数据结构</a>中使用列表对数据排序，当时底层储存数据的数据结构是数组。本文将讨论另外一种列表：链表。我们会解释为什么有时链表优于数组，还会实现一个基于对象的链表。下面让我们一起来学习<code>LinkedList</code>。</p>
<ul>
<li><a href="https://juejin.cn/post/6955266491012874270" target="_blank">数据结构之List | 让我们一块来学习数据结构</a></li>
<li><a href="https://juejin.cn/post/6955309635804856357" target="_blank">数据结构之Stack | 让我们一块来学习数据结构</a></li>
<li><a href="https://juejin.cn/post/6955640098687811620" target="_blank">数据结构之Queue | 让我们一块来学习数据结构</a></li>
</ul>
<h1 data-id="heading-0">数组的缺点</h1>
<p>在很多编程语言中，数组的长度是固定的，所以当数组已被数据填满时，再要加入新的元素就会非常困难。在数组中，添加和删除元素也很麻烦，因为需要将数组中的其他元素向前或向后平移，以反映数组刚刚进行了添加或删除操作。然而，JavaScript 的数组并不存在上述问题，因为使用 <code>split()</code> 方法不需要再访问数组中的其他元素了。</p>
<p>avaScript 中数组的主要问题是，它们被实现成了对象，与其他语言（比如 C++ 和 Java）的数组相比，效率很低。</p>
<h1 data-id="heading-1">定义链表</h1>
<p>链表是由一组节点组成的集合。每个节点都使用一个对象的引用指向它的后继。指向另一个节点的引用叫做链。下图展示了一个链表。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1db262a0ba5c4f4194410db0bd0d3836~tplv-k3u1fbpfcp-watermark.image" alt="企业微信截图_20210429090547.png" loading="lazy" referrerpolicy="no-referrer">
数组元素靠它们的位置进行引用，链表元素则是靠相互之间的关系进行引用。在上图中，我们说 <code>李四</code> 跟在 <code>张三</code> 后面，而不说 <code>李四</code> 是链表中的第二个元素。遍历链表，就是跟着链接，从链表的首元素一直走到尾元素（但这不包含链表的头节点，头节点常常用来作为链表的接入点）。图中另外一个值得注意的地方是，链表的尾元素指向一个 <code>null</code> 节点。</p>
<p>然而要标识出链表的起始节点却有点麻烦，许多链表的实现都在链表最前面有一个特殊节点，叫做头节点。经过改造之后，上图中的链表成了下面的样子。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71d956d7d85b4305a016184efa18d976~tplv-k3u1fbpfcp-watermark.image" alt="企业微信截图_20210429091827.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">设计一个基于对象的链表</h1>
<h2 data-id="heading-3">Node类</h2>
<p><code>Node</code> 类包含两个属性：<code>element</code> 用来保存节点上的数据，<code>next</code> 用来保存指向下一个节点的
链接。我们使用一个<code>class</code>来创建节点：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Node</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">element</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.element = element;
        <span class="hljs-built_in">this</span>.next = <span class="hljs-literal">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">LinkedList类</h2>
<p>LList 类提供了对链表进行操作的方法。该类的功能包括插入删除节点、在列表中查找给
定的值。该类也有一个构造函数，链表只有一个属性，那就是使用一个 Node 对象来保存该
链表的头节点。
该类如下所示</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LinkedList</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.head = <span class="hljs-keyword">new</span> Node(<span class="hljs-string">"head"</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-title">find</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">findPrevious</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">display</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>head</code> 节点的 <code>next</code> 属性被初始化为 <code>null</code>，当有新元素插入时，<code>next</code> 会指向新的元素，所以在这里我们没有修改 <code>next</code> 的值。</p>
</blockquote>
<h2 data-id="heading-5">插入新节点</h2>
<p>该方法向链表中插入一个节点。向链表中插入新节点时，需要明确指出要在哪个节点前面或后面插入。首先介绍如何在一个已知节点后面插入元素。</p>
<p>在一个已知节点后面插入元素时，先要找到“后面”的节点。为此，创建一个辅助方法<code>find()</code>，该方法遍历链表，查找给定数据。如果找到数据，该方法就返回保存该数据的节点。<code>find()</code> 方法的实现代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">find</span>(<span class="hljs-params">element</span>)</span> &#123;
    <span class="hljs-keyword">let</span> current = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">while</span> (current.element !== element) &#123;
        current = current.next;
    &#125;
    <span class="hljs-keyword">return</span> current;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>find()</code> 方法演示了如何在链表上进行移动。首先，创建一个新节点，并将链表的头节点赋给这个新创建的节点。然后在链表上进行循环，如果当前节点的 <code>element</code> 属性和我们要找的信息不符，就从当前节点移动到下一个节点。如果查找成功，该方法返回包含该数据的节点；否则，返回 <code>null</code>。</p>
<p>一旦找到<code>“后面”</code>的节点，就可以将新节点插入链表了。首先，将新节点的 <code>next</code> 属性设置为<code>“后面”</code>节点的 <code>next</code> 属性对应的值。然后设置<code>“后面”</code>节点的 <code>next</code> 属性指向新节点。</p>
<p><code>insert()</code> 方法的定义如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">element</span>)</span> &#123;
    <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> Node(element);
    <span class="hljs-keyword">const</span> curNode = <span class="hljs-built_in">this</span>.find(element);

    newNode.next = cur.next;
    curNode.next = newNode;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">移除节点</h2>
<p>在之前我们已经可以实现插入节点了，有添加自然就有移除。现在让我们来实现<code>remove()</code>方法。</p>
<p>从链表中删除节点时，需要先找到待删除节点前面的节点。找到这个节点后，修改它的
<code>next</code> 属性，使其不再指向待删除节点，而是指向待删除节点的下一个节点。我们可以定义
一个方法 <code>findPrevious()</code>，来做这件事。该方法遍历链表中的元素，检查每一个节点的下
一个节点中是否存储着待删除数据。如果找到，返回该节点（即“前一个”节点），这样
就可以修改它的 <code>next</code> 属性了。<code>findPrevious()</code> 方法的定义如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">findPrevious</span>(<span class="hljs-params">item</span>)</span> &#123;
    <span class="hljs-keyword">let</span> curNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">while</span> (curNode.next !== <span class="hljs-literal">null</span> && curNode.next.element !== item) &#123;
        curNode = curNode.next;
    &#125;
    <span class="hljs-keyword">return</span> curNode;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在就可以开始写 <code>remove()</code> 方法了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">item</span>)</span> &#123;
    <span class="hljs-keyword">const</span> prevNode = <span class="hljs-built_in">this</span>.findPrevious(item);
    <span class="hljs-keyword">if</span> (prevNode.next !== <span class="hljs-literal">null</span>) &#123;
        prevNode.next = prevNode.next.next;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">查看链表内的元素</h2>
<p>现在已经可以开始测试我们的链表实现了。然而在测试之前，先来定义一个 <code>display()</code> 方法，该方法用来显示链表中的元素：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">display</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> target = [];
    <span class="hljs-keyword">let</span> curNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">while</span> (curNode.next !== <span class="hljs-literal">null</span>) &#123;
        target.push(curNode.next.element);
        curNode = curNode.next;
    &#125;
    <span class="hljs-keyword">return</span> target.join();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">测试代码</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30c2532d43c842b7a377d36f52ff4fa5~tplv-k3u1fbpfcp-watermark.image" alt="测试代码.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">双向链表</h1>
<p>尽管从链表的头节点遍历到尾节点很简单，但反过来，从后向前遍历则没那么简单。通过给 <code>Node</code> 对象增加一个属性，该属性存储指向前驱节点的链接，这样就容易多了。此时向链表插入一个节点需要更多的工作，我们需要指出该节点正确的前驱和后继。但是在从链表中删除节点时，效率提高了，不需要再查找待删除节点的前驱节点了。图 6-5 演示了双向链表的工作原理。</p>
<h2 data-id="heading-10">修改Node类</h2>
<p>首当其冲的是要为 Node 类增加一个 previous 属性：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Node</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">element</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.element = element;
        <span class="hljs-built_in">this</span>.previous = <span class="hljs-literal">null</span>;
        <span class="hljs-built_in">this</span>.next = <span class="hljs-literal">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">修改<code>insert()</code>方法</h2>
<p>双向链表的 <code>insert()</code> 方法和单向链表的类似，但是需要设置新节点的 <code>previous</code> 属性，使其指向该节点的前驱。该方法的定义如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">element, item</span>)</span> &#123;
    <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> Node(element);
    <span class="hljs-keyword">const</span> curNode = <span class="hljs-built_in">this</span>.find(item);
    newNode.next = curNode.next;
    newNode.previous = curNode; <span class="hljs-comment">// 令新节点的previous指向当前节点</span>
    curNode.next = newNode;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>双向链表的 <code>remove()</code> 方法比单向链表的效率更高，因为不需要再查找前驱节点了。首先需要在链表中找出存储待删除数据的节点，然后设置该节点前驱的 <code>next</code> 属性，使其指向待删除节点的后继；设置该节点后继的 <code>previous</code> 属性，使其指向待删除节点的前驱。图 6-6 直观地展示了该过程。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5b416a6d6c64dacb57a0dee6455a5db~tplv-k3u1fbpfcp-watermark.image" alt="企业微信截图_20210429093227.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">新的remove() 方法的定义</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">item</span>)</span> &#123;
    <span class="hljs-keyword">const</span> curNode = <span class="hljs-built_in">this</span>.find(item);
    <span class="hljs-keyword">if</span> (curNode.next !== <span class="hljs-literal">null</span>) &#123;
        curNode.previous.next = curNode.next;
        curNode.next.previous = curNode.previous;
        curNode.previous = <span class="hljs-literal">null</span>;
        curNode.next = <span class="hljs-literal">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">反向显示链表中的元素</h2>
<p>为了完成以反序显示链表中元素这类任务，需要给双向链表增加一个工具方法，用来查找最后的节点。<code>findLast()</code> 方法找出了链表中的最后一个节点，同时免除了从前往后遍历链表之苦：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">findLast</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> curNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">while</span> (curNode.next !== <span class="hljs-literal">null</span>) &#123;
        curNode = curNode.next;
    &#125;
    <span class="hljs-keyword">return</span> curNode;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了这个工具方法，就可以写一个方法，反序显示双向链表中的元素。<code>dispReverse()</code> 方法如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">displayReverse</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> target = [];
    <span class="hljs-keyword">let</span> currNode = <span class="hljs-built_in">this</span>.findLast();
    <span class="hljs-keyword">while</span> (currNode.previous !== <span class="hljs-literal">null</span>) &#123;
        target.push(currNode.element);
        currNode = currNode.previous;
    &#125;
    <span class="hljs-keyword">return</span> target.join();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">完整的双向链表实现及测试代码</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Node</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">element</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.element = element;
        <span class="hljs-built_in">this</span>.previous = <span class="hljs-literal">null</span>;
        <span class="hljs-built_in">this</span>.next = <span class="hljs-literal">null</span>;
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LinkedList</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.head = <span class="hljs-keyword">new</span> Node(<span class="hljs-string">"head"</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-title">find</span>(<span class="hljs-params">item</span>)</span> &#123;
        <span class="hljs-keyword">let</span> current = <span class="hljs-built_in">this</span>.head;
        <span class="hljs-keyword">while</span> (current.element !== item) &#123;
            current = current.next;
        &#125;
        <span class="hljs-keyword">return</span> current;
    &#125;
    <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">element, item</span>)</span> &#123;
        <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> Node(element);
        <span class="hljs-keyword">const</span> curNode = <span class="hljs-built_in">this</span>.find(item);
        newNode.next = curNode.next;
        newNode.previous = curNode;
        curNode.next = newNode;
    &#125;
    <span class="hljs-function"><span class="hljs-title">findLast</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> curNode = <span class="hljs-built_in">this</span>.head;
        <span class="hljs-keyword">while</span> (curNode.next !== <span class="hljs-literal">null</span>) &#123;
            curNode = curNode.next;
        &#125;
        <span class="hljs-keyword">return</span> curNode;
    &#125;
    <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">item</span>)</span> &#123;
        <span class="hljs-keyword">const</span> curNode = <span class="hljs-built_in">this</span>.find(item);
        <span class="hljs-keyword">if</span> (curNode.next !== <span class="hljs-literal">null</span>) &#123;
            curNode.previous.next = curNode.next;
            curNode.next.previous = curNode.previous;
            curNode.previous = <span class="hljs-literal">null</span>;
            curNode.next = <span class="hljs-literal">null</span>;
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">display</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> target = [];
        <span class="hljs-keyword">let</span> curNode = <span class="hljs-built_in">this</span>.head;
        <span class="hljs-keyword">while</span> (curNode.next !== <span class="hljs-literal">null</span>) &#123;
            target.push(curNode.next.element);
            curNode = curNode.next;
        &#125;
        <span class="hljs-keyword">return</span> target.join();
    &#125;
    <span class="hljs-function"><span class="hljs-title">displayReverse</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> target = [];
        <span class="hljs-keyword">let</span> currNode = <span class="hljs-built_in">this</span>.findLast();
        <span class="hljs-keyword">while</span> (currNode.previous !== <span class="hljs-literal">null</span>) &#123;
            target.push(currNode.element);
            currNode = currNode.previous;
        &#125;
        <span class="hljs-keyword">return</span> target.join();
    &#125;
&#125;

<span class="hljs-comment">// test code</span>

<span class="hljs-keyword">const</span> linkedList = <span class="hljs-keyword">new</span> LinkedList();
linkedList.insert(<span class="hljs-string">"张三"</span>, <span class="hljs-string">"head"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.display()); <span class="hljs-comment">// 张三</span>
linkedList.insert(<span class="hljs-string">"李四"</span>, <span class="hljs-string">"张三"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.display()); <span class="hljs-comment">// 张三,李四</span>
linkedList.insert(<span class="hljs-string">"王五"</span>, <span class="hljs-string">"李四"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.display()); <span class="hljs-comment">// 张三,李四,王五</span>
linkedList.remove(<span class="hljs-string">"李四"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.display()); <span class="hljs-comment">// 张三,王五</span>
<span class="hljs-built_in">console</span>.log(linkedList.displayReverse()); <span class="hljs-comment">// 王五,张三</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-15">循环链表</h1>
<p>循环链表和单向链表相似，节点类型都是一样的。唯一的区别是，在创建循环链表时，让其头节点的 <code>next</code> 属性指向它本身，即：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">head.next = head
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种行为会传导至链表中的每个节点，使得每个节点的 next 属性都指向链表的头节点。换句话说，链表的尾节点指向头节点，形成了一个循环链表，如图 6-7 所示。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3a6898a292645c6b06bb4a5f49b2184~tplv-k3u1fbpfcp-watermark.image" alt="企业微信截图_20210429092257.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建循环链表，只需要修改 <code>LinkedList</code> 类的构造方法(<code>constructor</code>)：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LinkedList</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.head = <span class="hljs-keyword">new</span> Node(<span class="hljs-string">"head"</span>);
        <span class="hljs-built_in">this</span>.head.next = <span class="hljs-built_in">this</span>.head;
    &#125;
    <span class="hljs-function"><span class="hljs-title">find</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">findPrevious</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">display</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只需要修改一处，就将单向链表变成了循环链表。但是其他一些方法需要修改才能工作正常。比如，<code>display()</code> 就需要修改，原来的方式在循环链表里会陷入死循环。<code>while</code> 循环的循环条件需要修改，需要检查<code>head</code>节点，当循环到<code>head</code>节点时退出循环。</p>
<p>循环链表的<code>display()</code>方法如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">display</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> target = [];
    <span class="hljs-keyword">let</span> curNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">while</span> (curNode.next !== <span class="hljs-literal">null</span> && curNode.next.element !== <span class="hljs-string">"head"</span>) &#123;
        target.push(curNode.next.element);
        curNode = curNode.next;
    &#125;
    <span class="hljs-keyword">return</span> target.join();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">完整的循环链表实现及测试代码</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Node</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">element</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.element = element;
        <span class="hljs-built_in">this</span>.next = <span class="hljs-literal">null</span>;
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LinkedList</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.head = <span class="hljs-keyword">new</span> Node(<span class="hljs-string">"head"</span>);
        <span class="hljs-built_in">this</span>.head.next = <span class="hljs-built_in">this</span>.head;
    &#125;
    <span class="hljs-function"><span class="hljs-title">find</span>(<span class="hljs-params">item</span>)</span> &#123;
        <span class="hljs-keyword">let</span> current = <span class="hljs-built_in">this</span>.head;
        <span class="hljs-keyword">while</span> (current.element !== item) &#123;
            current = current.next;
        &#125;
        <span class="hljs-keyword">return</span> current;
    &#125;
    <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">element, item</span>)</span> &#123;
        <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> Node(element);
        <span class="hljs-keyword">const</span> curNode = <span class="hljs-built_in">this</span>.find(item);
        newNode.next = curNode.next;
        curNode.next = newNode;
    &#125;
    <span class="hljs-function"><span class="hljs-title">findPrevious</span>(<span class="hljs-params">item</span>)</span> &#123;
        <span class="hljs-keyword">let</span> curNode = <span class="hljs-built_in">this</span>.head;
        <span class="hljs-keyword">while</span> (curNode.next !== <span class="hljs-literal">null</span> && curNode.next.element !== item) &#123;
            curNode = curNode.next;
        &#125;
        <span class="hljs-keyword">return</span> curNode;
    &#125;
    <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">item</span>)</span> &#123;
        <span class="hljs-keyword">const</span> prevNode = <span class="hljs-built_in">this</span>.findPrevious(item);
        <span class="hljs-keyword">if</span> (prevNode.next !== <span class="hljs-literal">null</span>) &#123;
            prevNode.next = prevNode.next.next;
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">display</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> target = [];
        <span class="hljs-keyword">let</span> curNode = <span class="hljs-built_in">this</span>.head;
        <span class="hljs-keyword">while</span> (curNode.next !== <span class="hljs-literal">null</span> && curNode.next.element !== <span class="hljs-string">"head"</span>) &#123;
            target.push(curNode.next.element);
            curNode = curNode.next;
        &#125;
        <span class="hljs-keyword">return</span> target.join();
    &#125;
&#125;

<span class="hljs-comment">// test code</span>

<span class="hljs-keyword">const</span> linkedList = <span class="hljs-keyword">new</span> LinkedList();
linkedList.insert(<span class="hljs-string">"张三"</span>, <span class="hljs-string">"head"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.display()); <span class="hljs-comment">// 张三</span>
linkedList.insert(<span class="hljs-string">"李四"</span>, <span class="hljs-string">"张三"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.display()); <span class="hljs-comment">// 张三,李四</span>
linkedList.insert(<span class="hljs-string">"王五"</span>, <span class="hljs-string">"李四"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.display()); <span class="hljs-comment">// 张三,李四,王五</span>
linkedList.remove(<span class="hljs-string">"李四"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.display()); <span class="hljs-comment">// 张三,王五</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-17">参考资料</h1>
<ul>
<li>数据结构与算法JavaScript描述</li>
<li>学习JavaScript数据结构与算法 第3版</li>
</ul>
<blockquote>
<p>如果觉得对您有帮助,动动小手点个赞；您的点赞就是对我最大的认可。</p>
</blockquote></div>  
</div>
            