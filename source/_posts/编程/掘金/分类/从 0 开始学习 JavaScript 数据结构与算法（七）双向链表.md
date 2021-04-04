
---
title: '从 0 开始学习 JavaScript 数据结构与算法（七）双向链表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1142e49e4db4845badd63778caf7964~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 23:25:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1142e49e4db4845badd63778caf7964~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本专辑是根据 B 站 <a href="https://www.bilibili.com/video/BV1x7411L7Q7?p=1" target="_blank" rel="nofollow noopener noreferrer">《JavaScript 数据结构与算法》</a> 视频整理的学习笔记，本文作者已将笔记、源码、测试环境托管在 <a href="https://github.com/XPoet/js-data-structures-and-algorithms" target="_blank" rel="nofollow noopener noreferrer">GitHub</a>，欢迎同学们 Star 和 Fork。</p>
<p>推荐大家按照目录结构的顺序来学习，由浅入深，循序渐进，轻松搞定数据结构和算法。</p>
</blockquote>
<h2 data-id="heading-0">单向链表和双向链表</h2>
<h3 data-id="heading-1">单向链表</h3>
<ul>
<li>只能从头遍历到尾或者从尾遍历到头（一般从头到尾）。</li>
<li>链表相连的过程是单向的，实现原理是上一个节点中有指向下一个节点的引用。</li>
<li>单向链表有一个比较明显的缺点：可以轻松到达下一个节点，但回到前一个节点很难，在实际开发中, 经常会遇到需要回到上一个节点的情况。</li>
</ul>
<h3 data-id="heading-2">双向链表</h3>
<ul>
<li>既可以从头遍历到尾，也可以从尾遍历到头。</li>
<li>链表相连的过程是双向的。实现原理是一个节点既有向前连接的引用，也有一个向后连接的引用。</li>
<li>双向链表可以有效的解决单向链表存在的问题。</li>
<li>双向链表缺点：
<ul>
<li>每次在插入或删除某个节点时，都需要处理四个引用，而不是两个，实现起来会困难些。</li>
<li>相对于单向链表，所占内存空间更大一些。</li>
<li>但是，相对于双向链表的便利性而言，这些缺点微不足道。</li>
</ul>
</li>
</ul>
<h2 data-id="heading-3">双向链表结构</h2>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1142e49e4db4845badd63778caf7964~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>双向链表不仅有 head 指针指向第一个节点，而且有 tail 指针指向最后一个节点。</li>
<li>每一个节点由三部分组成：item 储存数据、prev 指向前一个节点、next 指向后一个节点。</li>
<li>双向链表的第一个节点的 prev 指向 null。</li>
<li>双向链表的最后一个节点的 next 指向 null。</li>
</ul>
<h2 data-id="heading-4">双向链表常见的操作</h2>
<ul>
<li><code>append(element)</code> 向链表尾部追加一个新元素。</li>
<li><code>insert(position, element)</code> 向链表的指定位置插入一个新元素。</li>
<li><code>getElement(position)</code> 获取指定位置的元素。</li>
<li><code>indexOf(element)</code> 返回元素在链表中的索引。如果链表中没有该元素就返回 -1。</li>
<li><code>update(position, element)</code> 修改指定位置上的元素。</li>
<li><code>removeAt(position)</code> 从链表中的删除指定位置的元素。</li>
<li><code>remove(element)</code> 从链表删除指定的元素。</li>
<li><code>isEmpty()</code> 如果链表中不包含任何元素，返回 <code>trun</code>，如果链表长度大于 0 则返回 <code>false</code>。</li>
<li><code>size()</code> 返回链表包含的元素个数，与数组的 <code>length</code> 属性类似。</li>
<li><code>toString()</code> 由于链表项使用了 Node 类，就需要重写继承自 JavaScript 对象默认的 <code>toString</code> 方法，让其只输出元素的值。</li>
<li><code>forwardString()</code> 返回正向遍历节点字符串形式。</li>
<li><code>backwordString()</code> 返回反向遍历的节点的字符串形式。</li>
</ul>
<h2 data-id="heading-5">双向链表的封装</h2>
<h3 data-id="heading-6">创建双向链表类 DoublyLinkedList</h3>
<ul>
<li>DoublyNode 类继承单向链表的 Node 类，新添加 <code>this.prev</code> 属性，该属性用于指向上一个节点。</li>
<li>DoublyLinkedList 类继承 LinkedList 类，新添加 <code>this.tail</code> 属性，该属性指向末尾的节点。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 双向链表的节点类（继承单向链表的节点类）</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DoublyNode</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Node</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">element</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(element);
    <span class="hljs-built_in">this</span>.prev = <span class="hljs-literal">null</span>;
  &#125;
&#125;

<span class="hljs-comment">// 双向链表类继承单向链表类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DoublyLinkedList</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">LinkedList</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
    <span class="hljs-built_in">this</span>.tail = <span class="hljs-literal">null</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">append(element)</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// append(element) 往双向链表尾部追加一个新的元素</span>
<span class="hljs-comment">// 重写 append()</span>
<span class="hljs-function"><span class="hljs-title">append</span>(<span class="hljs-params">element</span>)</span> &#123;

<span class="hljs-comment">// 1、创建双向链表节点</span>
<span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> DoublyNode(element);

<span class="hljs-comment">// 2、追加元素</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.head === <span class="hljs-literal">null</span>) &#123;
  <span class="hljs-built_in">this</span>.head = newNode;
  <span class="hljs-built_in">this</span>.tail = newNode;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// ！！跟单向链表不同，不用通过循环找到最后一个节点</span>
  <span class="hljs-comment">// 巧妙之处</span>
  <span class="hljs-built_in">this</span>.tail.next = newNode;
  newNode.prev = <span class="hljs-built_in">this</span>.tail;
  <span class="hljs-built_in">this</span>.tail = newNode;
&#125;

<span class="hljs-built_in">this</span>.length++;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">insert(position, element)</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// insert(position, data) 插入元素</span>
<span class="hljs-comment">// 重写 insert()</span>
<span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">position, element</span>)</span> &#123;
    <span class="hljs-comment">// 1、position 越界判断</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position > <span class="hljs-built_in">this</span>.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;

    <span class="hljs-comment">// 2、创建新的双向链表节点</span>
    <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> DoublyNode(element);

    <span class="hljs-comment">// 3、判断多种插入情况</span>
    <span class="hljs-keyword">if</span> (position === <span class="hljs-number">0</span>) &#123; <span class="hljs-comment">// 在第 0 个位置插入</span>

      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.head === <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-built_in">this</span>.head = newNode;
        <span class="hljs-built_in">this</span>.tail = newNode;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">//== 巧妙之处：相处腾出 this.head 空间，留个 newNode 来赋值 ==//</span>
        newNode.next = <span class="hljs-built_in">this</span>.head;
        <span class="hljs-built_in">this</span>.head.perv = newNode;
        <span class="hljs-built_in">this</span>.head = newNode;
      &#125;

    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (position === <span class="hljs-built_in">this</span>.length) &#123; <span class="hljs-comment">// 在最后一个位置插入</span>

      <span class="hljs-built_in">this</span>.tail.next = newNode;
      newNode.prev = <span class="hljs-built_in">this</span>.tail;
      <span class="hljs-built_in">this</span>.tail = newNode;
    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 在 0 ~ this.length 位置中间插入</span>

      <span class="hljs-keyword">let</span> targetIndex = <span class="hljs-number">0</span>;
      <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
      <span class="hljs-keyword">let</span> previousNode = <span class="hljs-literal">null</span>;

      <span class="hljs-comment">// 找到要插入位置的节点</span>
      <span class="hljs-keyword">while</span> (targetIndex++ < position) &#123;
        previousNode = currentNode;
        currentNode = currentNode.next;
      &#125;

      <span class="hljs-comment">// 交换节点信息</span>
      previousNode.next = newNode;
      newNode.prev = previousNode;

      newNode.next = currentNode;
      currentNode.prev = newNode;
    &#125;

    <span class="hljs-built_in">this</span>.length++;

    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">insert(position, element)</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// insert(position, data) 插入元素</span>
<span class="hljs-comment">// 重写 insert()</span>
  <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">position, element</span>)</span> &#123;
    <span class="hljs-comment">// 1、position 越界判断</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position > <span class="hljs-built_in">this</span>.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;

    <span class="hljs-comment">// 2、创建新的双向链表节点</span>
    <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> DoublyNode(element);

    <span class="hljs-comment">// 3、判断多种插入情况</span>
    <span class="hljs-keyword">if</span> (position === <span class="hljs-number">0</span>) &#123; <span class="hljs-comment">// 在第 0 个位置插入</span>

      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.head === <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-built_in">this</span>.head = newNode;
        <span class="hljs-built_in">this</span>.tail = newNode;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">//== 巧妙之处：相处腾出 this.head 空间，留个 newNode 来赋值 ==//</span>
        newNode.next = <span class="hljs-built_in">this</span>.head;
        <span class="hljs-built_in">this</span>.head.perv = newNode;
        <span class="hljs-built_in">this</span>.head = newNode;
      &#125;

    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (position === <span class="hljs-built_in">this</span>.length) &#123; <span class="hljs-comment">// 在最后一个位置插入</span>

      <span class="hljs-built_in">this</span>.tail.next = newNode;
      newNode.prev = <span class="hljs-built_in">this</span>.tail;
      <span class="hljs-built_in">this</span>.tail = newNode;
    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 在 0 ~ this.length 位置中间插入</span>

      <span class="hljs-keyword">let</span> targetIndex = <span class="hljs-number">0</span>;
      <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
      <span class="hljs-keyword">let</span> previousNode = <span class="hljs-literal">null</span>;

      <span class="hljs-comment">// 找到要插入位置的节点</span>
      <span class="hljs-keyword">while</span> (targetIndex++ < position) &#123;
        previousNode = currentNode;
        currentNode = currentNode.next;
      &#125;

      <span class="hljs-comment">// 交换节点信息</span>
      previousNode.next = newNode;
      newNode.prev = previousNode;

      newNode.next = currentNode;
      currentNode.prev = newNode;
    &#125;

    <span class="hljs-built_in">this</span>.length++;

    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">removeAt(position)</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// removeAt() 删除指定位置的节点</span>
  <span class="hljs-comment">// 重写 removeAt()</span>
  <span class="hljs-function"><span class="hljs-title">removeAt</span>(<span class="hljs-params">position</span>)</span> &#123;
    <span class="hljs-comment">// 1、position 越界判断</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position > <span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;

    <span class="hljs-comment">// 2、根据不同情况删除元素</span>
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">if</span> (position === <span class="hljs-number">0</span>) &#123; <span class="hljs-comment">// 删除第一个节点的情况</span>

      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.length === <span class="hljs-number">1</span>) &#123; <span class="hljs-comment">// 链表内只有一个节点的情况</span>
        <span class="hljs-built_in">this</span>.head = <span class="hljs-literal">null</span>;
        <span class="hljs-built_in">this</span>.tail = <span class="hljs-literal">null</span>;
      &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 链表内有多个节点的情况</span>
        <span class="hljs-built_in">this</span>.head = <span class="hljs-built_in">this</span>.head.next;
        <span class="hljs-built_in">this</span>.head.prev = <span class="hljs-literal">null</span>;
      &#125;

    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (position === <span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>) &#123; <span class="hljs-comment">// 删除最后一个节点的情况</span>

      currentNode = <span class="hljs-built_in">this</span>.tail;
      <span class="hljs-built_in">this</span>.tail.prev.next = <span class="hljs-literal">null</span>;
      <span class="hljs-built_in">this</span>.tail = <span class="hljs-built_in">this</span>.tail.prev;

    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 删除 0 ~ this.length - 1 里面节点的情况</span>

      <span class="hljs-keyword">let</span> targetIndex = <span class="hljs-number">0</span>;
      <span class="hljs-keyword">let</span> previousNode = <span class="hljs-literal">null</span>;
      <span class="hljs-keyword">while</span> (targetIndex++ < position) &#123;
        previousNode = currentNode;
        currentNode = currentNode.next;
      &#125;

      previousNode.next = currentNode.next;
      currentNode.next.perv = previousNode;

    &#125;

    <span class="hljs-built_in">this</span>.length--;
    <span class="hljs-keyword">return</span> currentNode.data;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">update(position, data)</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// update(position, data) 修改指定位置的节点</span>
  <span class="hljs-comment">// 重写 update()</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">position, data</span>)</span> &#123;
    <span class="hljs-comment">// 1、删除 position 位置的节点</span>
    <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">this</span>.removeAt(position);

    <span class="hljs-comment">// 2、在 position 位置插入元素</span>
    <span class="hljs-built_in">this</span>.insert(position, data);
    <span class="hljs-keyword">return</span> result;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">forwardToString()</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// forwardToString() 链表数据从前往后以字符串形式返回</span>
  <span class="hljs-function"><span class="hljs-title">forwardToString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">let</span> result = <span class="hljs-string">''</span>;

    <span class="hljs-comment">// 遍历所有的节点，拼接为字符串，直到节点为 null</span>
    <span class="hljs-keyword">while</span> (currentNode) &#123;
      result += currentNode.data + <span class="hljs-string">'--'</span>;
      currentNode = currentNode.next;
    &#125;

    <span class="hljs-keyword">return</span> result;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">backwardString()</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// backwardString() 链表数据从后往前以字符串形式返回</span>
  <span class="hljs-function"><span class="hljs-title">backwardString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.tail;
    <span class="hljs-keyword">let</span> result = <span class="hljs-string">''</span>;

    <span class="hljs-comment">// 遍历所有的节点，拼接为字符串，直到节点为 null</span>
    <span class="hljs-keyword">while</span> (currentNode) &#123;
      result += currentNode.data + <span class="hljs-string">'--'</span>;
      currentNode = currentNode.prev;
    &#125;

    <span class="hljs-keyword">return</span> result;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">其他方法的实现</h3>
<p>双向链表的其他方法通过继承单向链表来实现。</p>
<h3 data-id="heading-15">完整实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DoublyLinkedList</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">LinkedList</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
    <span class="hljs-built_in">this</span>.tail = <span class="hljs-literal">null</span>;
  &#125;

  <span class="hljs-comment">// ------------ 链表的常见操作 ------------ //</span>
  <span class="hljs-comment">// append(element) 往双向链表尾部追加一个新的元素</span>
  <span class="hljs-comment">// 重写 append()</span>
  <span class="hljs-function"><span class="hljs-title">append</span>(<span class="hljs-params">element</span>)</span> &#123;
    <span class="hljs-comment">// 1、创建双向链表节点</span>
    <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> DoublyNode(element);

    <span class="hljs-comment">// 2、追加元素</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.head === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-built_in">this</span>.head = newNode;
      <span class="hljs-built_in">this</span>.tail = newNode;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// ！！跟单向链表不同，不用通过循环找到最后一个节点</span>
      <span class="hljs-comment">// 巧妙之处</span>
      <span class="hljs-built_in">this</span>.tail.next = newNode;
      newNode.prev = <span class="hljs-built_in">this</span>.tail;
      <span class="hljs-built_in">this</span>.tail = newNode;
    &#125;

    <span class="hljs-built_in">this</span>.length++;
  &#125;

  <span class="hljs-comment">// insert(position, data) 插入元素</span>
  <span class="hljs-comment">// 重写 insert()</span>
  <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">position, element</span>)</span> &#123;
    <span class="hljs-comment">// 1、position 越界判断</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position > <span class="hljs-built_in">this</span>.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;

    <span class="hljs-comment">// 2、创建新的双向链表节点</span>
    <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> DoublyNode(element);

    <span class="hljs-comment">// 3、判断多种插入情况</span>
    <span class="hljs-keyword">if</span> (position === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 在第 0 个位置插入</span>

      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.head === <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-built_in">this</span>.head = newNode;
        <span class="hljs-built_in">this</span>.tail = newNode;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">//== 巧妙之处：相处腾出 this.head 空间，留个 newNode 来赋值 ==//</span>
        newNode.next = <span class="hljs-built_in">this</span>.head;
        <span class="hljs-built_in">this</span>.head.perv = newNode;
        <span class="hljs-built_in">this</span>.head = newNode;
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (position === <span class="hljs-built_in">this</span>.length) &#123;
      <span class="hljs-comment">// 在最后一个位置插入</span>

      <span class="hljs-built_in">this</span>.tail.next = newNode;
      newNode.prev = <span class="hljs-built_in">this</span>.tail;
      <span class="hljs-built_in">this</span>.tail = newNode;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 在 0 ~ this.length 位置中间插入</span>

      <span class="hljs-keyword">let</span> targetIndex = <span class="hljs-number">0</span>;
      <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
      <span class="hljs-keyword">let</span> previousNode = <span class="hljs-literal">null</span>;

      <span class="hljs-comment">// 找到要插入位置的节点</span>
      <span class="hljs-keyword">while</span> (targetIndex++ < position) &#123;
        previousNode = currentNode;
        currentNode = currentNode.next;
      &#125;

      <span class="hljs-comment">// 交换节点信息</span>
      previousNode.next = newNode;
      newNode.prev = previousNode;

      newNode.next = currentNode;
      currentNode.prev = newNode;
    &#125;

    <span class="hljs-built_in">this</span>.length++;

    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;

  <span class="hljs-comment">// getData() 继承单向链表</span>
  <span class="hljs-function"><span class="hljs-title">getData</span>(<span class="hljs-params">position</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">super</span>.getData(position);
  &#125;

  <span class="hljs-comment">// indexOf() 继承单向链表</span>
  <span class="hljs-function"><span class="hljs-title">indexOf</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">super</span>.indexOf(data);
  &#125;

  <span class="hljs-comment">// removeAt() 删除指定位置的节点</span>
  <span class="hljs-comment">// 重写 removeAt()</span>
  <span class="hljs-function"><span class="hljs-title">removeAt</span>(<span class="hljs-params">position</span>)</span> &#123;
    <span class="hljs-comment">// 1、position 越界判断</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position > <span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;

    <span class="hljs-comment">// 2、根据不同情况删除元素</span>
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">if</span> (position === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 删除第一个节点的情况</span>

      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.length === <span class="hljs-number">1</span>) &#123;
        <span class="hljs-comment">// 链表内只有一个节点的情况</span>
        <span class="hljs-built_in">this</span>.head = <span class="hljs-literal">null</span>;
        <span class="hljs-built_in">this</span>.tail = <span class="hljs-literal">null</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 链表内有多个节点的情况</span>
        <span class="hljs-built_in">this</span>.head = <span class="hljs-built_in">this</span>.head.next;
        <span class="hljs-built_in">this</span>.head.prev = <span class="hljs-literal">null</span>;
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (position === <span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>) &#123;
      <span class="hljs-comment">// 删除最后一个节点的情况</span>

      currentNode = <span class="hljs-built_in">this</span>.tail;
      <span class="hljs-built_in">this</span>.tail.prev.next = <span class="hljs-literal">null</span>;
      <span class="hljs-built_in">this</span>.tail = <span class="hljs-built_in">this</span>.tail.prev;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 删除 0 ~ this.length - 1 里面节点的情况</span>

      <span class="hljs-keyword">let</span> targetIndex = <span class="hljs-number">0</span>;
      <span class="hljs-keyword">let</span> previousNode = <span class="hljs-literal">null</span>;
      <span class="hljs-keyword">while</span> (targetIndex++ < position) &#123;
        previousNode = currentNode;
        currentNode = currentNode.next;
      &#125;

      previousNode.next = currentNode.next;
      currentNode.next.perv = previousNode;
    &#125;

    <span class="hljs-built_in">this</span>.length--;
    <span class="hljs-keyword">return</span> currentNode.data;
  &#125;

  <span class="hljs-comment">// update(position, data) 修改指定位置的节点</span>
  <span class="hljs-comment">// 重写 update()</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">position, data</span>)</span> &#123;
    <span class="hljs-comment">// 1、删除 position 位置的节点</span>
    <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">this</span>.removeAt(position);

    <span class="hljs-comment">// 2、在 position 位置插入元素</span>
    <span class="hljs-built_in">this</span>.insert(position, data);
    <span class="hljs-keyword">return</span> result;
  &#125;

  <span class="hljs-comment">// remove(data) 删除指定 data 所在的节点（继承单向链表）</span>
  <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">super</span>.remove(data);
  &#125;

  <span class="hljs-comment">// isEmpty() 判断链表是否为空</span>
  <span class="hljs-function"><span class="hljs-title">isEmpty</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">super</span>.isEmpty();
  &#125;

  <span class="hljs-comment">// size() 获取链表的长度</span>
  <span class="hljs-function"><span class="hljs-title">size</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">super</span>.size();
  &#125;

  <span class="hljs-comment">// forwardToString() 链表数据从前往后以字符串形式返回</span>
  <span class="hljs-function"><span class="hljs-title">forwardToString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">let</span> result = <span class="hljs-string">""</span>;

    <span class="hljs-comment">// 遍历所有的节点，拼接为字符串，直到节点为 null</span>
    <span class="hljs-keyword">while</span> (currentNode) &#123;
      result += currentNode.data + <span class="hljs-string">"--"</span>;
      currentNode = currentNode.next;
    &#125;

    <span class="hljs-keyword">return</span> result;
  &#125;

  <span class="hljs-comment">// backwardString() 链表数据从后往前以字符串形式返回</span>
  <span class="hljs-function"><span class="hljs-title">backwardString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.tail;
    <span class="hljs-keyword">let</span> result = <span class="hljs-string">""</span>;

    <span class="hljs-comment">// 遍历所有的节点，拼接为字符串，直到节点为 null</span>
    <span class="hljs-keyword">while</span> (currentNode) &#123;
      result += currentNode.data + <span class="hljs-string">"--"</span>;
      currentNode = currentNode.prev;
    &#125;

    <span class="hljs-keyword">return</span> result;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">代码测试</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> doublyLinkedList = <span class="hljs-keyword">new</span> DoublyLinkedList();

<span class="hljs-comment">// append() 测试</span>
doublyLinkedList.append(<span class="hljs-string">"ZZ"</span>);
doublyLinkedList.append(<span class="hljs-string">"XX"</span>);
doublyLinkedList.append(<span class="hljs-string">"CC"</span>);
<span class="hljs-built_in">console</span>.log(doublyLinkedList);

<span class="hljs-comment">// insert() 测试</span>
doublyLinkedList.insert(<span class="hljs-number">0</span>, <span class="hljs-string">"00"</span>);
doublyLinkedList.insert(<span class="hljs-number">2</span>, <span class="hljs-string">"22"</span>);
<span class="hljs-built_in">console</span>.log(doublyLinkedList);

<span class="hljs-comment">// getData() 测试</span>
<span class="hljs-built_in">console</span>.log(doublyLinkedList.getData(<span class="hljs-number">1</span>)); <span class="hljs-comment">//--> ZZ</span>

<span class="hljs-comment">// indexOf() 测试</span>
<span class="hljs-built_in">console</span>.log(doublyLinkedList.indexOf(<span class="hljs-string">"XX"</span>)); <span class="hljs-comment">//--> 3</span>
<span class="hljs-built_in">console</span>.log(doublyLinkedList);

<span class="hljs-comment">// removeAt() 测试</span>
doublyLinkedList.removeAt(<span class="hljs-number">0</span>);
doublyLinkedList.removeAt(<span class="hljs-number">1</span>);
<span class="hljs-built_in">console</span>.log(doublyLinkedList);

<span class="hljs-comment">// update() 测试</span>
doublyLinkedList.update(<span class="hljs-number">0</span>, <span class="hljs-string">"111111"</span>);
<span class="hljs-built_in">console</span>.log(doublyLinkedList);

<span class="hljs-comment">// remove() 测试</span>
<span class="hljs-built_in">console</span>.log(doublyLinkedList.remove(<span class="hljs-string">"111111"</span>));
<span class="hljs-built_in">console</span>.log(doublyLinkedList.remove(<span class="hljs-string">"22222"</span>));
<span class="hljs-built_in">console</span>.log(doublyLinkedList);

<span class="hljs-comment">// forwardToString() 测试</span>
<span class="hljs-built_in">console</span>.log(doublyLinkedList.forwardToString());

<span class="hljs-comment">// backwardString() 测试</span>
<span class="hljs-built_in">console</span>.log(doublyLinkedList.backwardString());
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果对你有帮助，点赞支持一下作者 ❤️</p>
</blockquote>
<h2 data-id="heading-17">专辑系列</h2>
<ul>
<li><a href="https://juejin.cn/post/6945415278343749639" target="_blank">从 0 开始学习 JavaScript 数据结构与算法（一）前言</a></li>
<li><a href="https://juejin.cn/post/6945415514139131918" target="_blank">从 0 开始学习 JavaScript 数据结构与算法（二）数组</a></li>
<li><a href="https://juejin.cn/post/6945415514139131918" target="_blank">从 0 开始学习 JavaScript 数据结构与算法（三）栈</a></li>
<li><a href="https://juejin.cn/post/6945638258105647118" target="_blank">从 0 开始学习 JavaScript 数据结构与算法（四）队列</a></li>
<li><a href="https://juejin.cn/post/6946363248220487711" target="_blank">从 0 开始学习 JavaScript 数据结构与算法（五）优先队列</a></li>
<li><a href="https://juejin.cn/post/6946849466569719816" target="_blank">从 0 开始学习 JavaScript 数据结构与算法（六）单向链表</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            