
---
title: '从 0 开始学习 JavaScript 数据结构与算法（六）单向链表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a522e14bd854b78bb11814be7fa9bce~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 00:44:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a522e14bd854b78bb11814be7fa9bce~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本专辑是根据 B 站 <a href="https://www.bilibili.com/video/BV1x7411L7Q7?p=1" target="_blank" rel="nofollow noopener noreferrer">《JavaScript 数据结构与算法》</a> 视频整理的学习笔记，本文作者已将笔记、源码、测试环境托管在 <a href="https://github.com/XPoet/js-data-structures-and-algorithms" target="_blank" rel="nofollow noopener noreferrer">GitHub</a>，欢迎同学们 Star 和 Fork。</p>
<p>推荐大家按照目录结构的顺序来学习，由浅入深，循序渐进，轻松搞定数据结构和算法。</p>
</blockquote>
<h2 data-id="heading-0">认识链表</h2>
<h3 data-id="heading-1">链表和数组</h3>
<p>链表和数组一样，可以用于存储一系列的元素，但是链表和数组的实现机制完全不同。</p>
<h4 data-id="heading-2">数组</h4>
<ul>
<li>
<p>存储多个元素，数组（或列表）可能是最常用的数据结构。</p>
</li>
<li>
<p>几乎每一种编程语言都有默认实现数组结构，提供了一个便利的 <code>[]</code> 语法来访问数组元素。</p>
</li>
<li>
<p>数组缺点：</p>
<p>数组的创建需要申请一段连续的内存空间(一整块内存)，并且大小是固定的，当前数组不能满足容量需求时，需要扩容。 (一般情况下是申请一个更大的数组，比如 2 倍，然后将原数组中的元素复制过去)</p>
<p>在数组开头或中间位置插入数据的成本很高，需要进行大量元素的位移。</p>
</li>
</ul>
<h4 data-id="heading-3">链表</h4>
<ul>
<li>
<p>存储多个元素，另外一个选择就是使用链表。</p>
</li>
<li>
<p>不同于数组，链表中的元素在内存中不必是连续的空间。</p>
</li>
<li>
<p>链表的每个元素由一个存储元素本身的节点和一个指向下一个元素的引用(有些语言称为指针)组成。</p>
</li>
<li>
<p>链表优点：</p>
<p>内存空间不必是连续的，可以充分利用计算机的内存，实现灵活的内存动态管理。</p>
<p>链表不必在创建时就确定大小，并且大小可以无限延伸下去。</p>
<p>链表在插入和删除数据时，时间复杂度可以达到 O(1)，相对数组效率高很多。</p>
</li>
<li>
<p>链表缺点：</p>
<p>访问任何一个位置的元素时，需要从头开始访问。(无法跳过第一个元素访问任何一个元素)</p>
<p>无法通过下标值直接访问元素，需要从头开始一个个访问，直到找到对应的元素。</p>
<p>虽然可以轻松地到达下一个节点，但是回到前一个节点是很难的。</p>
</li>
</ul>
<h2 data-id="heading-4">单向链表</h2>
<p>单向链表类似于火车，有一个火车头，火车头会连接一个节点，节点上有乘客，并且这个节点会连接下一个节点，以此类推。</p>
<ul>
<li>
<p>链表的火车结构</p>
<p><img alt="链表的火车结构" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a522e14bd854b78bb11814be7fa9bce~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>链表的数据结构</p>
<p>head 属性指向链表的第一个节点。<br>
链表中的最后一个节点指向 <code>null</code>。
当链表中一个节点也没有的时候，head 直接指向 <code>null</code>。</p>
<p><img alt="链表的数据结构" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bd36f38ae2b4c67a1e7cfcdcaae3049~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>给火车加上数据后的结构</p>
<p><img alt="给火车加上数据后的结构" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0fed5e68334455d960a720bfdcdc011~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-5">链表中的常见操作</h3>
<ul>
<li><code>append(element)</code> 向链表尾部添加一个新的项。</li>
<li><code>insert(position, element)</code> 向链表的特定位置插入一个新的项。</li>
<li><code>get(position)</code> 获取对应位置的元素。</li>
<li><code>indexOf(element)</code> 返回元素在链表中的索引。如果链表中没有该元素就返回-1。</li>
<li><code>update(position, element)</code> 修改某个位置的元素。</li>
<li><code>removeAt(position)</code> 从链表的特定位置移除一项。</li>
<li><code>remove(element)</code> 从链表中移除一项。</li>
<li><code>isEmpty()</code> 如果链表中不包含任何元素，返回 trun，如果链表长度大于 0 则返回 false。</li>
<li><code>size()</code> 返回链表包含的元素个数，与数组的 length 属性类似。</li>
<li><code>toString()</code> 由于链表项使用了 Node 类，就需要重写继承自 JavaScript 对象默认的 toString 方法，让其只输出元素的值。</li>
</ul>
<h3 data-id="heading-6">单向链表的封装</h3>
<h4 data-id="heading-7">创建单向链表类</h4>
<p>先创建单向链表类 LinkedList，添加基本属性，再逐步实现单向链表的常用方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LinkedList</span> </span>&#123;
  <span class="hljs-comment">// 初始链表长度为 0</span>
  length = <span class="hljs-number">0</span>;

  <span class="hljs-comment">// 初始 head 为 null，head 指向链表的第一个节点</span>
  head = <span class="hljs-literal">null</span>;

  <span class="hljs-comment">// 内部类（链表里的节点 Node）</span>
  Node = <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123;
    data;
    next = <span class="hljs-literal">null</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">data</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.data = data;
    &#125;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">实现 append() 方法</h4>
<h5 data-id="heading-9">代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// append() 往链表尾部追加数据</span>
<span class="hljs-function"><span class="hljs-title">append</span>(<span class="hljs-params">data</span>)</span> &#123;

    <span class="hljs-comment">// 1、创建新节点</span>
    <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> <span class="hljs-built_in">this</span>.Node(data);

    <span class="hljs-comment">// 2、追加新节点</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.length === <span class="hljs-number">0</span>) &#123;

    <span class="hljs-comment">// 链表长度为 0 时，即只有 head 的时候</span>
    <span class="hljs-built_in">this</span>.head = newNode;

    &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 链表长度大于 0 时，在最后面添加新节点</span>
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;

    <span class="hljs-comment">// 当 currentNode.next 不为空时，</span>
    <span class="hljs-comment">// 循序依次找最后一个节点，即节点的 next 为 null 时</span>
    <span class="hljs-keyword">while</span> (currentNode.next !== <span class="hljs-literal">null</span>) &#123;
        currentNode = currentNode.next;
    &#125;

    <span class="hljs-comment">// 最后一个节点的 next 指向新节点</span>
    currentNode.next = newNode;
    &#125;

    <span class="hljs-comment">// 3、追加完新节点后，链表长度 + 1</span>
    <span class="hljs-built_in">this</span>.length++;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">过程图解</h5>
<ul>
<li>
<p>首先让 <code>currentNode</code> 指向第一个节点。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd7ce547333a453a99fc1540d1bfa075~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>通过 <code>while</code> 循环使 <code>currentNode</code> 指向最后一个节点，最后通过 <code>currentNode.next = newNode</code>，让最后一个节点指向新节点 <code>newNode</code>。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4295d9dbbbb94fee8cc58cb2d3c0e02e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h5 data-id="heading-11">代码测试</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> linkedList = <span class="hljs-keyword">new</span> LinkedList();
<span class="hljs-comment">// 测试 append 方法</span>
linkedList.append(<span class="hljs-string">"A"</span>);
linkedList.append(<span class="hljs-string">"B"</span>);
linkedList.append(<span class="hljs-string">"C"</span>);
<span class="hljs-built_in">console</span>.log(linkedList);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a0da9562fdf453bbc311c621a5bb21c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">实现 toString() 方法</h4>
<h5 data-id="heading-13">代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">let</span> result = <span class="hljs-string">''</span>;

    <span class="hljs-comment">// 遍历所有的节点，拼接为字符串，直到节点为 null</span>
    <span class="hljs-keyword">while</span> (currentNode) &#123;
    result += currentNode.data + <span class="hljs-string">' '</span>;
    currentNode = currentNode.next;
    &#125;

    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">代码测试</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 测试 toString 方法</span>
<span class="hljs-built_in">console</span>.log(linkedList.toString()); <span class="hljs-comment">//--> AA BB CC</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">实现 insert() 方法</h4>
<h5 data-id="heading-16">代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// insert() 在指定位置（position）插入节点</span>
<span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">position, data</span>)</span> &#123;
    <span class="hljs-comment">// position 新插入节点的位置</span>
    <span class="hljs-comment">// position = 0 表示新插入后是第一个节点</span>
    <span class="hljs-comment">// position = 1 表示新插入后是第二个节点，以此类推</span>

    <span class="hljs-comment">// 1、对 position 进行越界判断，不能小于 0 或大于链表长度</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position > <span class="hljs-built_in">this</span>.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;

    <span class="hljs-comment">// 2、创建新节点</span>
    <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> <span class="hljs-built_in">this</span>.Node(data);

    <span class="hljs-comment">// 3、插入节点</span>
    <span class="hljs-keyword">if</span> (position === <span class="hljs-number">0</span>) &#123; <span class="hljs-comment">// position = 0 的情况</span>
    <span class="hljs-comment">// 让新节点的 next 指向 原来的第一个节点，即 head</span>
    newNode.next = <span class="hljs-built_in">this</span>.head;

    <span class="hljs-comment">// head 赋值为 newNode</span>
    <span class="hljs-built_in">this</span>.head = newNode;
    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 0 < position <= length 的情况</span>

    <span class="hljs-comment">// 初始化一些变量</span>
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head; <span class="hljs-comment">// 当前节点初始化为 head</span>
    <span class="hljs-keyword">let</span> previousNode = <span class="hljs-literal">null</span>; <span class="hljs-comment">// head 的 上一节点为 null</span>
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; <span class="hljs-comment">// head 的 index 为 0</span>

    <span class="hljs-comment">// 在 0 ~ position 之间遍历，不断地更新 currentNode 和 previousNode</span>
    <span class="hljs-comment">// 直到找到要插入的位置</span>
    <span class="hljs-keyword">while</span> (index++ < position) &#123;
        previousNode = currentNode;
        currentNode = currentNode.next;
    &#125;

    <span class="hljs-comment">// 在当前节点和当前节点的上一节点之间插入新节点，即它们的改变指向</span>
    newNode.next = currentNode;
    previousNode.next = newNode;
    &#125;

    <span class="hljs-comment">// 更新链表长度</span>
    <span class="hljs-built_in">this</span>.length++;
    <span class="hljs-keyword">return</span> newNode;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">代码测试</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 测试 insert 方法</span>
linkedList.insert(<span class="hljs-number">0</span>, <span class="hljs-string">"123"</span>);
linkedList.insert(<span class="hljs-number">2</span>, <span class="hljs-string">"456"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.toString()); <span class="hljs-comment">//--> 123 AA 456 BB CC</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">实现 getData() 方法</h4>
<p>获取指定位置（position）的 data。</p>
<h5 data-id="heading-19">代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">getData</span>(<span class="hljs-params">position</span>)</span> &#123;
    <span class="hljs-comment">// 1、position 越界判断</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position >= <span class="hljs-built_in">this</span>.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;

    <span class="hljs-comment">// 2、获取指定 position 节点的 data</span>
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;

    <span class="hljs-keyword">while</span> (index++ < position) &#123;
    currentNode = currentNode.next;
    &#125;
    <span class="hljs-comment">// 3、返回 data</span>
    <span class="hljs-keyword">return</span> currentNode.data;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-20">代码测试</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 测试 getData 方法</span>
<span class="hljs-built_in">console</span>.log(linkedList.getData(<span class="hljs-number">0</span>)); <span class="hljs-comment">//--> 123</span>
<span class="hljs-built_in">console</span>.log(linkedList.getData(<span class="hljs-number">1</span>)); <span class="hljs-comment">//--> AA</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">实现 indexOf() 方法</h4>
<p>indexOf(data) 返回指定 data 的 index，如果没有，返回 -1。</p>
<h5 data-id="heading-22">代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">indexOf</span>(<span class="hljs-params">data</span>)</span> &#123;

    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;

    <span class="hljs-keyword">while</span> (currentNode) &#123;
    <span class="hljs-keyword">if</span> (currentNode.data === data) &#123;
        <span class="hljs-keyword">return</span> index;
    &#125;
    currentNode = currentNode.next;
    index++;
    &#125;

    <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-23">代码测试</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 测试 indexOf 方法</span>
<span class="hljs-built_in">console</span>.log(linkedList.indexOf(<span class="hljs-string">"AA"</span>)); <span class="hljs-comment">//--> 1</span>
<span class="hljs-built_in">console</span>.log(linkedList.indexOf(<span class="hljs-string">"ABC"</span>)); <span class="hljs-comment">//--> -1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">实现 update() 方法</h4>
<p>update(position, data) 修改指定位置节点的 data。</p>
<h5 data-id="heading-25">代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">position, data</span>)</span> &#123;
    <span class="hljs-comment">// 涉及到 position 都要进行越界判断</span>
    <span class="hljs-comment">// 1、position 越界判断</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position >= <span class="hljs-built_in">this</span>.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;

    <span class="hljs-comment">// 2、痛过循环遍历，找到指定 position 的节点</span>
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">while</span> (index++ < position) &#123;
    currentNode = currentNode.next;
    &#125;

    <span class="hljs-comment">// 3、修改节点 data</span>
    currentNode.data = data;

    <span class="hljs-keyword">return</span> currentNode;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-26">代码测试</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 测试 update 方法</span>
linkedList.update(<span class="hljs-number">0</span>, <span class="hljs-string">"12345"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.toString()); <span class="hljs-comment">//--> 12345 AA 456 BB CC</span>
linkedList.update(<span class="hljs-number">1</span>, <span class="hljs-string">"54321"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.toString()); <span class="hljs-comment">//--> 12345 54321 456 BB CC</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">实现 removeAt() 方法</h4>
<p>removeAt(position) 删除指定位置的节点。</p>
<h5 data-id="heading-28">代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">removeAt</span>(<span class="hljs-params">position</span>)</span> &#123;
    <span class="hljs-comment">// 1、position 越界判断</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position >= <span class="hljs-built_in">this</span>.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;

    <span class="hljs-comment">// 2、删除指定 position 节点</span>
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">if</span> (position === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-comment">// position = 0 的情况</span>
    <span class="hljs-built_in">this</span>.head = <span class="hljs-built_in">this</span>.head.next;

    &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// position > 0 的情况</span>
    <span class="hljs-comment">// 通过循环遍历，找到指定 position 的节点，赋值到 currentNode</span>

    <span class="hljs-keyword">let</span> previousNode = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;

    <span class="hljs-keyword">while</span> (index++ < position) &#123;
        previousNode = currentNode;
        currentNode = currentNode.next;
    &#125;

    <span class="hljs-comment">// 巧妙之处，让上一节点的 next 指向到当前的节点的 next，相当于删除了当前节点。</span>
    previousNode.next = currentNode.next;
    &#125;

    <span class="hljs-comment">// 3、更新链表长度 -1</span>
    <span class="hljs-built_in">this</span>.length--;

    <span class="hljs-keyword">return</span> currentNode;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-29">代码测试</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 测试 removeAt 方法</span>
linkedList.removeAt(<span class="hljs-number">3</span>);
<span class="hljs-built_in">console</span>.log(linkedList.toString()); <span class="hljs-comment">//--> 12345 54321 456 CC</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">实现 remove() 方法</h4>
<p>remove(data) 删除指定 data 所在的节点。</p>
<h5 data-id="heading-31">代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.removeAt(<span class="hljs-built_in">this</span>.indexOf(data));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-32">代码测试</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 测试 remove 方法</span>
linkedList.remove(<span class="hljs-string">"CC"</span>);
<span class="hljs-built_in">console</span>.log(linkedList.toString()); <span class="hljs-comment">//--> 12345 54321 456</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">实现 isEmpty() 方法</h4>
<p>isEmpty() 判断链表是否为空。</p>
<h5 data-id="heading-34">代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">isEmpty</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.length === <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-35">代码测试</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 测试 isEmpty 方法</span>
<span class="hljs-built_in">console</span>.log(linkedList.isEmpty()); <span class="hljs-comment">//--> false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-36">实现 size() 方法</h4>
<p>size() 获取链表的长度。</p>
<h5 data-id="heading-37">代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">size</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.length;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-38">代码测试</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 测试 size 方法</span>
<span class="hljs-built_in">console</span>.log(linkedList.size()); <span class="hljs-comment">//--> 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-39">完整实现</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LinkedList</span> </span>&#123;
  <span class="hljs-comment">// 初始链表长度为 0</span>
  length = <span class="hljs-number">0</span>;

  <span class="hljs-comment">// 初始 head 为 null，head 指向链表的第一个节点</span>
  head = <span class="hljs-literal">null</span>;

  <span class="hljs-comment">// 内部类（链表里的节点 Node）</span>
  Node = <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123;
    data;
    next = <span class="hljs-literal">null</span>;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">data</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.data = data;
    &#125;
  &#125;;

  <span class="hljs-comment">// ------------ 链表的常见操作 ------------ //</span>

  <span class="hljs-comment">// append() 往链表尾部追加数据</span>
  <span class="hljs-function"><span class="hljs-title">append</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-comment">// 1、创建新节点</span>
    <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> <span class="hljs-built_in">this</span>.Node(data);

    <span class="hljs-comment">// 2、追加新节点</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.length === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 链表长度为 0 时，即只有 head 的时候</span>
      <span class="hljs-built_in">this</span>.head = newNode;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 链表长度大于 0 时，在最后面添加新节点</span>
      <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;

      <span class="hljs-comment">// 当 currentNode.next 不为空时，</span>
      <span class="hljs-comment">// 循序依次找最后一个节点，即节点的 next 为 null 时</span>
      <span class="hljs-keyword">while</span> (currentNode.next !== <span class="hljs-literal">null</span>) &#123;
        currentNode = currentNode.next;
      &#125;

      <span class="hljs-comment">// 最后一个节点的 next 指向新节点</span>
      currentNode.next = newNode;
    &#125;

    <span class="hljs-comment">// 3、追加完新节点后，链表长度 + 1</span>
    <span class="hljs-built_in">this</span>.length++;
  &#125;

  <span class="hljs-comment">// insert() 在指定位置（position）插入节点</span>
  <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">position, data</span>)</span> &#123;
    <span class="hljs-comment">// position 新插入节点的位置</span>
    <span class="hljs-comment">// position = 0 表示新插入后是第一个节点</span>
    <span class="hljs-comment">// position = 1 表示新插入后是第二个节点，以此类推</span>

    <span class="hljs-comment">// 1、对 position 进行越界判断，不能小于 0 或大于链表长度</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position > <span class="hljs-built_in">this</span>.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;

    <span class="hljs-comment">// 2、创建新节点</span>
    <span class="hljs-keyword">const</span> newNode = <span class="hljs-keyword">new</span> <span class="hljs-built_in">this</span>.Node(data);

    <span class="hljs-comment">// 3、插入节点</span>
    <span class="hljs-keyword">if</span> (position === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// position = 0 的情况</span>
      <span class="hljs-comment">// 让新节点的 next 指向 原来的第一个节点，即 head</span>
      newNode.next = <span class="hljs-built_in">this</span>.head;

      <span class="hljs-comment">// head 赋值为 newNode</span>
      <span class="hljs-built_in">this</span>.head = newNode;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 0 < position <= length 的情况</span>

      <span class="hljs-comment">// 初始化一些变量</span>
      <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head; <span class="hljs-comment">// 当前节点初始化为 head</span>
      <span class="hljs-keyword">let</span> previousNode = <span class="hljs-literal">null</span>; <span class="hljs-comment">// head 的 上一节点为 null</span>
      <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; <span class="hljs-comment">// head 的 index 为 0</span>

      <span class="hljs-comment">// 在 0 ~ position 之间遍历，不断地更新 currentNode 和 previousNode</span>
      <span class="hljs-comment">// 直到找到要插入的位置</span>
      <span class="hljs-keyword">while</span> (index++ < position) &#123;
        previousNode = currentNode;
        currentNode = currentNode.next;
      &#125;

      <span class="hljs-comment">// 在当前节点和当前节点的上一节点之间插入新节点，即它们的改变指向</span>
      newNode.next = currentNode;
      previousNode.next = newNode;
    &#125;

    <span class="hljs-comment">// 更新链表长度</span>
    <span class="hljs-built_in">this</span>.length++;
    <span class="hljs-keyword">return</span> newNode;
  &#125;

  <span class="hljs-comment">// getData() 获取指定位置的 data</span>
  <span class="hljs-function"><span class="hljs-title">getData</span>(<span class="hljs-params">position</span>)</span> &#123;
    <span class="hljs-comment">// 1、position 越界判断</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position >= <span class="hljs-built_in">this</span>.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;

    <span class="hljs-comment">// 2、获取指定 position 节点的 data</span>
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;

    <span class="hljs-keyword">while</span> (index++ < position) &#123;
      currentNode = currentNode.next;
    &#125;

    <span class="hljs-comment">// 3、返回 data</span>
    <span class="hljs-keyword">return</span> currentNode.data;
  &#125;

  <span class="hljs-comment">// indexOf() 返回指定 data 的 index，如果没有，返回 -1。</span>
  <span class="hljs-function"><span class="hljs-title">indexOf</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;

    <span class="hljs-keyword">while</span> (currentNode) &#123;
      <span class="hljs-keyword">if</span> (currentNode.data === data) &#123;
        <span class="hljs-keyword">return</span> index;
      &#125;
      currentNode = currentNode.next;
      index++;
    &#125;

    <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
  &#125;

  <span class="hljs-comment">// update() 修改指定位置节点的 data</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">position, data</span>)</span> &#123;
    <span class="hljs-comment">// 涉及到 position 都要进行越界判断</span>
    <span class="hljs-comment">// 1、position 越界判断</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position >= <span class="hljs-built_in">this</span>.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;

    <span class="hljs-comment">// 2、痛过循环遍历，找到指定 position 的节点</span>
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">while</span> (index++ < position) &#123;
      currentNode = currentNode.next;
    &#125;

    <span class="hljs-comment">// 3、修改节点 data</span>
    currentNode.data = data;

    <span class="hljs-keyword">return</span> currentNode;
  &#125;

  <span class="hljs-comment">// removeAt() 删除指定位置的节点</span>
  <span class="hljs-function"><span class="hljs-title">removeAt</span>(<span class="hljs-params">position</span>)</span> &#123;
    <span class="hljs-comment">// 1、position 越界判断</span>
    <span class="hljs-keyword">if</span> (position < <span class="hljs-number">0</span> || position >= <span class="hljs-built_in">this</span>.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;

    <span class="hljs-comment">// 2、删除指定 position 节点</span>
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">if</span> (position === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// position = 0 的情况</span>
      <span class="hljs-built_in">this</span>.head = <span class="hljs-built_in">this</span>.head.next;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// position > 0 的情况</span>
      <span class="hljs-comment">// 通过循环遍历，找到指定 position 的节点，赋值到 currentNode</span>

      <span class="hljs-keyword">let</span> previousNode = <span class="hljs-literal">null</span>;
      <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;

      <span class="hljs-keyword">while</span> (index++ < position) &#123;
        previousNode = currentNode;
        currentNode = currentNode.next;
      &#125;

      <span class="hljs-comment">// 巧妙之处，让上一节点的 next 指向到当前的节点的 next，相当于删除了当前节点。</span>
      previousNode.next = currentNode.next;
    &#125;

    <span class="hljs-comment">// 3、更新链表长度 -1</span>
    <span class="hljs-built_in">this</span>.length--;

    <span class="hljs-keyword">return</span> currentNode;
  &#125;

  <span class="hljs-comment">// remove() 删除指定 data 的节点</span>
  <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.removeAt(<span class="hljs-built_in">this</span>.indexOf(data));
  &#125;

  <span class="hljs-comment">// isEmpty() 判断链表是否为空</span>
  <span class="hljs-function"><span class="hljs-title">isEmpty</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.length === <span class="hljs-number">0</span>;
  &#125;

  <span class="hljs-comment">// size() 获取链表的长度</span>
  <span class="hljs-function"><span class="hljs-title">size</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.length;
  &#125;

  <span class="hljs-comment">// toString() 链表数据以字符串形式返回</span>
  <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> currentNode = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">let</span> result = <span class="hljs-string">""</span>;

    <span class="hljs-comment">// 遍历所有的节点，拼接为字符串，直到节点为 null</span>
    <span class="hljs-keyword">while</span> (currentNode) &#123;
      result += currentNode.data + <span class="hljs-string">" "</span>;
      currentNode = currentNode.next;
    &#125;

    <span class="hljs-keyword">return</span> result;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果对你有帮助，点赞支持一下作者 ❤️</p>
</blockquote>
<h2 data-id="heading-40">专辑系列</h2>
<ul>
<li><a href="https://juejin.cn/post/6945415278343749639" target="_blank">从 0 开始学习 JavaScript 数据结构与算法（一）前言</a></li>
<li><a href="https://juejin.cn/post/6945415514139131918" target="_blank">从 0 开始学习 JavaScript 数据结构与算法（二）数组</a></li>
<li><a href="https://juejin.cn/post/6945415514139131918" target="_blank">从 0 开始学习 JavaScript 数据结构与算法（三）栈</a></li>
<li><a href="https://juejin.cn/post/6945638258105647118" target="_blank">从 0 开始学习 JavaScript 数据结构与算法（四）队列</a></li>
<li><a href="https://juejin.cn/post/6946363248220487711" target="_blank">从 0 开始学习 JavaScript 数据结构与算法（五）优先队列</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            