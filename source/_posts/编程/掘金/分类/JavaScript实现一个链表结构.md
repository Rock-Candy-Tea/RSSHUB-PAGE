
---
title: 'JavaScript实现一个链表结构'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=863'
author: 掘金
comments: false
date: Thu, 27 May 2021 00:25:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=863'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​前言：</p>
<p>很感谢每一位关注二哥的朋友，在各位朋友的帮助下，二哥也学到了非常多的东西。也希望通过自己的学习到的知识，分享给每个需要的朋友。如果在文章中写的有错误的地方，还希望各位朋友多多指出。有更好的思路，想法也可以留言或者私聊我。不甚感激。</p>
<p>简介：</p>
<p>链表在数据结构中，是一个非常基础也是比较好理解的一个数据结构。每个不同的语言实现起来有细微差距，但是总体思路还是一样的。今天给大家介绍的是单向链表，单向链表和双向链表的区别就是少了一个父节点的引用。</p>
<p>链表的结构是由一个根节点包含两个字段，一个value当前节点的值，next下一个节点的引用。数组与链表非常相似，但是数组的结构是在内存中开辟出一整块空间，根据内容长度的不同来对这块空间进行扩容和减少空间。数组是紧密型的数据结构。通过索引对数据的存储，是一个有序的排列。相比链表，数组对了很多方法，也可以对数据进行不同的操作。</p>
<p>链表是对内存的堆中的一些引用进行串联成一个链子一样。不是有序的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 链表数据结构 [1, 2, 3 ]</span>
<span class="hljs-keyword">let</span> linkedList = &#123;
  <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">next</span>: &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">next</span>: &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-number">3</span>,
      <span class="hljs-attr">next</span>: <span class="hljs-literal">null</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在JavaScript中是不提供原生链表结构的，我们可以用代码自己模拟一个链表，链表需要有一个头部节点 head， 默认是null。我们要对这个链表添加一个节点，那就需要一个添加节点的方法，同时我们想知道这个链表是否包含某个节点，删除一个节点等等的一些功能，我列举一些常见的方法。</p>
<ol>
<li>addLast // 尾部添加一个节点</li>
<li>addFirst // 添加一个头部节点</li>
<li>isEmpty // 判断当前列表是否为空</li>
<li>find // 查找指定元素</li>
<li>findLast // 获取最后一个节点</li>
<li>removeLast // 删除最后一个节点</li>
<li>removeFirst // 删除第一个节点</li>
<li>remove // 删除一个指定节点</li>
<li>insert // 指定位置插入</li>
<li>dir // 展开这个链表</li>
</ol>
<p>现在我们知道了我们要实现的这个链表包含了那些功能，我们一个一个的来实现，首先我们需要一个链表的构造函数，成为一个容器来承载我们的链表也承载对应的方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LinkedList</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 添加一个长度属性</span>
    <span class="hljs-built_in">this</span>.size = <span class="hljs-number">0</span>;
    <span class="hljs-comment">// 声明一个头部节点</span>
    <span class="hljs-built_in">this</span>.head = <span class="hljs-literal">null</span>;
    <span class="hljs-comment">// 维护一个尾部节点（添加的时候非常便利）</span>
    <span class="hljs-built_in">this</span>.tail = <span class="hljs-literal">null</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们的链表基本结构就有了，我们还需要一个生成节点的构造函数，来辅助我们每次生成一个节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Node</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"> data </span>)</span> &#123;
    <span class="hljs-comment">// 节点的value</span>
     <span class="hljs-built_in">this</span>.value = data;
     <span class="hljs-comment">// 节点的下一个引用指向</span>
     <span class="hljs-built_in">this</span>.next = <span class="hljs-literal">null</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们现在准备工作已经差不多了。我们的链表也已经有了。但是就好像设计好了一个机器人，还没有给它设计动作指令，还只能看不能使用。那么我们从添加一个节点开始。</p>
<p>尾部添加节点，我们刚刚在设计linkedList的时候就预留了一个尾部节点的引用，这样在链表数据庞大的时候，我们不用遍历整个列表到最后一个节点去添加，这就会显得非常快捷，但是它初始值是null。证明还没有尾部节点。也就是我们根节点都还不存在，所以在添加节点的这个方法里。我们要做的事情是判断是否有根节点，有就用尾部节点去添加，没有就直接添加在根节点上，并且维护一下尾部节点，更新一下链表长度。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">addLast</span>(<span class="hljs-params"> item </span>)</span> &#123;
  <span class="hljs-comment">// 对参数做一个非空验证</span>
  <span class="hljs-keyword">if</span> ( !item ) &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请输入一个正确的节点！'</span>) &#125;
  <span class="hljs-comment">// 创建一个节点</span>
  <span class="hljs-keyword">let</span> node = <span class="hljs-keyword">new</span> Node(item);
  <span class="hljs-comment">// 判断链表是否为空</span>
  <span class="hljs-keyword">if</span> ( <span class="hljs-built_in">this</span>.size === <span class="hljs-number">0</span> ) &#123;
    <span class="hljs-comment">// 更新尾部节点，更新头部节点</span>
    <span class="hljs-built_in">this</span>.tail = <span class="hljs-built_in">this</span>.head = node;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 设置尾部节点的引用</span>
    <span class="hljs-built_in">this</span>.tail.next = node;
    <span class="hljs-comment">// 将最新的尾部节点更新到tail</span>
    <span class="hljs-built_in">this</span>.tail = node
  &#125;
  <span class="hljs-comment">// 更新一下长度</span>
  <span class="hljs-built_in">this</span>.size++;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>刚刚实现了在链表的尾部添加一个节点，对应我们还可以在头部添加一个节点。思路和刚刚相差不大，因为我们有头部节点，能够直接获取到。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">addFirst</span>(<span class="hljs-params"> item </span>)</span> &#123;
  <span class="hljs-comment">// 对参数做一个非空验证</span>
  <span class="hljs-keyword">if</span> ( !item ) &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请输入一个正确的节点！'</span>) &#125;
  <span class="hljs-comment">// 创建一个node节点</span>
  <span class="hljs-keyword">let</span> node = <span class="hljs-keyword">new</span> Node(item);
  <span class="hljs-comment">// 判断当前链表是否为空</span>
  <span class="hljs-keyword">if</span> ( <span class="hljs-built_in">this</span>.size === <span class="hljs-number">0</span> ) &#123;
     <span class="hljs-built_in">this</span>.head = <span class="hljs-built_in">this</span>.tail = node;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 将整个链表作为新节点的next引用 </span>
    node.next = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-comment">// 将node赋值给head</span>
    <span class="hljs-built_in">this</span>.head = node;
  &#125;
  <span class="hljs-comment">// 更新一下长度</span>
  <span class="hljs-built_in">this</span>.size++
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>头部添加一个节点也实现了。尾部添加一个节点也实现了。这个时候我们可以实现一下查找的方法。查找方法的主要作用是查看当前链表中是否包含某个节点，如果需要实现一个没有重复节点的链表，也可也在每次添加之前调用查找方法，看看添加的节点是否存在。我们这里就没有做类似的限制。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">find</span>(<span class="hljs-params"> item </span>)</span> &#123;
  <span class="hljs-comment">// 对参数做一个非空验证</span>
  <span class="hljs-keyword">if</span> ( !item ) &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请输入一个正确的节点！'</span>) &#125;
  <span class="hljs-comment">// 获取到整个节点</span>
  <span class="hljs-keyword">let</span> linkedList = <span class="hljs-built_in">this</span>.head;
  <span class="hljs-comment">// 循环判断</span>
  <span class="hljs-keyword">while</span> ( linkedList && linkedList.next && linkedList.value !== item )&#123;
    linkedList = linkedList.next;
  &#125;
  <span class="hljs-keyword">return</span> linkedList
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了添加，查找。可以实现一下删除的功能首先实现一下头部删除，头部删除是比较简单的，找到第一个头部节点的引用返回，然后将头部指向头部节点的next引用就可以删除头部节点了。</p>
<pre><code class="hljs language-js copyable" lang="js">removeFirst ()&#123;
  <span class="hljs-comment">// 定义一个返回值</span>
  <span class="hljs-keyword">let</span> res = <span class="hljs-literal">null</span>;
  <span class="hljs-comment">// 判断当前链表不为空</span>
  <span class="hljs-keyword">if</span> ( <span class="hljs-built_in">this</span>.size !== <span class="hljs-number">0</span> ) &#123;
    res = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-comment">// 跳过head节点，将head指向head的next</span>
    <span class="hljs-built_in">this</span>.head = <span class="hljs-built_in">this</span>.head.next;
    res.next = <span class="hljs-literal">null</span>;
    <span class="hljs-comment">// 维护一下长度</span>
    <span class="hljs-built_in">this</span>.size--;
    <span class="hljs-comment">// 判断删除完，链表为空，清空一下尾部节点的引用</span>
    <span class="hljs-built_in">this</span>.tail = <span class="hljs-built_in">this</span>.size ? <span class="hljs-built_in">this</span>.tail : <span class="hljs-literal">null</span>;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 如果链表为空，调用删除操作，就报一个警告</span>
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'链表为空，不能执行删除操作！'</span>)
  &#125;
  <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除头部节点实现了以后，可以把删除尾部节点也实现一下，删除尾部节点，需要先遍历到尾部节点的父级，然后更新尾部节点的引用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">removerLast</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-comment">// 定义一个返回值</span>
  <span class="hljs-keyword">let</span> res = <span class="hljs-literal">null</span>;
  <span class="hljs-comment">// 拿到所有节点</span>
  <span class="hljs-keyword">let</span> linkedList = <span class="hljs-built_in">this</span>.head;
  <span class="hljs-comment">// 判断当前链表是否只有一个节点</span>
  <span class="hljs-keyword">if</span> ( <span class="hljs-built_in">this</span>.size === <span class="hljs-number">1</span> ) &#123;
    res = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-built_in">this</span>.head = <span class="hljs-built_in">this</span>.tail = <span class="hljs-literal">null</span>;
    res.next = <span class="hljs-literal">null</span>;
  &#125;
  <span class="hljs-comment">// 判断是链表为为空</span>
  <span class="hljs-keyword">if</span> ( <span class="hljs-built_in">this</span>.size === <span class="hljs-number">0</span> ) &#123;
   <span class="hljs-comment">// 如果链表为空，调用删除操作，就报一个警告</span>
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'链表为空，不能执行删除操作！'</span>)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 循环找倒数第二个节点</span>
    <span class="hljs-keyword">while</span> ( linkedList && linkedList.next && linkedList.next.next )&#123;
      linkedList = linkedList.next;
    &#125;
    res = linkedList.next;
    <span class="hljs-comment">// 将最后一个引用置为空</span>
    linkedList.next = <span class="hljs-literal">null</span>;
    <span class="hljs-comment">// 维护一下尾部节点</span>
    <span class="hljs-built_in">this</span>.tail = linkedList;
    <span class="hljs-comment">// 维护一下长度</span>
    <span class="hljs-built_in">this</span>.size--;
  &#125;
  <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了前两个删除的方法的经验，我们来实现一下指定节点的删除。删除指定节点也是需要遍历链表，获取到指定元素的父级，跟删除最后一个节点有点相似。只是不判断下下级，而是判断下下级是否等于指定删除的元素。由于我们今天分享的这个版本，并没有对唯一性限制，所以删除的时候，默认删除在找到的第一个元素删除。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">remover</span>(<span class="hljs-params"> item </span>)</span>&#123;
  <span class="hljs-comment">// 定义一个返回值</span>
  <span class="hljs-keyword">let</span> res = <span class="hljs-literal">null</span>;
  <span class="hljs-comment">// 对参数做一个非空验证</span>
  <span class="hljs-keyword">if</span> ( !item ) &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请输入一个正确的节点！'</span>) &#125;
  <span class="hljs-comment">// 拿到整个链表</span>
  <span class="hljs-keyword">let</span> linkedList = <span class="hljs-built_in">this</span>.head;
  <span class="hljs-comment">// 判断链表只有一个节点</span>
  <span class="hljs-keyword">if</span> ( <span class="hljs-built_in">this</span>.size === <span class="hljs-number">1</span> && linkedList.value === item ) &#123;
    res = linkedList;
    <span class="hljs-comment">// 维护一下头部节点和尾部节点</span>
    <span class="hljs-built_in">this</span>.head = <span class="hljs-built_in">this</span>.tail =  <span class="hljs-literal">null</span>;
    
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 循环找到指定节点的父级</span>
    <span class="hljs-keyword">while</span> ( linkedList && linkedList.next && linkedList.next.value !== item ) &#123;
      linkedList = linkedList.next;
    &#125;
    <span class="hljs-comment">// 判断是否存在</span>
    <span class="hljs-keyword">if</span> ( linkedList && linkedList.next ) &#123;
      <span class="hljs-comment">// 存下删除节点</span>
      res = linkedList.next;
      <span class="hljs-comment">// 删除指定节点</span>
      linkedList.next = linkedList.next.next;    
     
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'链表中没有该节点，不能执行删除操作！'</span>)
    &#125;
  &#125;
  
  <span class="hljs-comment">// 判断一下删除节点是否为最后一个节点</span>
  <span class="hljs-built_in">this</span>.tail = linkedList.next ? <span class="hljs-built_in">this</span>.tail : <span class="hljs-literal">null</span>;
  <span class="hljs-comment">// 删除节点的next指向清空</span>
  res.next = <span class="hljs-literal">null</span>;
   <span class="hljs-comment">// 维护一下</span>
   <span class="hljs-built_in">this</span>.size--;
   <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有时候我们可能需要判断一下这个链表是否为空，我们实现一下 isEmpty 方法，这个方法比较讨巧。因为只需要判断一下我们维护的size属性，就能知道是否为空了。虽然说我们这里构建的链表其实可以在整个链表的属性中找到size属性。这个验证是否为空的函数是可以不用出的。但是在真实开发过程中用到的时候，其实是不希望size属性被修改的。也不会被暴露出来。JavaScript中比较灵活，很多限制没有像java那么好做。我们这里就没有去对其做限制。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">isEmpty</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.size === <span class="hljs-number">0</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们的链表其实基本功能都能够满足了。一般对一个数据的操作无非增删改查，目前我们都已经实现了。还可以增加一个插入的功能，插入是指定位置插入，如果找不到该位置，抛错，如果位置正确，插入的节点不正确也抛错。</p>
<pre><code class="hljs language-js copyable" lang="js">insert ( item, ele ) &#123;
  <span class="hljs-comment">// 验证两个参数不能为空</span>
  <span class="hljs-keyword">if</span> ( !item || !ele ) &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请输入一个正确的节点或者查找元素！'</span>) &#125;
  <span class="hljs-comment">// 拿到整个链表</span>
  <span class="hljs-keyword">let</span> linkedList = <span class="hljs-built_in">this</span>.head;
  <span class="hljs-comment">// 循环查找匹配</span>
  <span class="hljs-keyword">while</span> ( linkedList  && linkedList.value !== item ) &#123;
    linkedList = linkedList.next;
  &#125;
  <span class="hljs-comment">// 验证结果，结果只能是两个，找到，没找到</span>
  <span class="hljs-keyword">if</span> ( linkedList ) &#123;
    <span class="hljs-comment">// 生成一个节点</span>
    <span class="hljs-keyword">let</span> node = <span class="hljs-keyword">new</span> Node(ele);
    <span class="hljs-comment">// 将匹配到的节点的next引用指向新节点的next引用</span>
    node.next = linkedList.next;
    <span class="hljs-comment">// 将新节点赋值给 匹配到的节点</span>
    linkedList.next = node;
    <span class="hljs-comment">// 判断一下是否是插入到了最后一个元素</span>
    <span class="hljs-built_in">this</span>.tail = node.next ? <span class="hljs-built_in">this</span>.tail : node;
    <span class="hljs-comment">// 维护一下长度</span>
    <span class="hljs-built_in">this</span>.size++;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'没有匹配到需要插入位置的元素！'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在平时也会关注到链表的第一项和链表的最后一项。在双向链表中，可以从头往后遍历，也可以从尾部朝前遍历。就需要直接拿到尾部节点，我们这个示例中没有涉及到双向链表。但是我们维护了一个尾部节点，获取链表最后一项还是比较方便的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">findLast</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.tail
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于整个链表的结构比较复杂。查看起来并不是特别的方便，在文章开头的时候简单讲解了一下3个节点的展开面结构。已经不太利于阅读了。那如果我们链表长度是30，可能展开面就非常大了。这个时候我们就需要有一个方法来查看一下整个链表的数据了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">dir</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// 定义一个返回值</span>
  <span class="hljs-keyword">let</span> res = <span class="hljs-string">''</span>;
  <span class="hljs-comment">// 获取整个链表</span>
  <span class="hljs-keyword">let</span> linkedList = <span class="hljs-built_in">this</span>.head;
  res = linkedList ? linkedList.value : <span class="hljs-string">''</span>;
  <span class="hljs-comment">// 循环获取整个链表的数据</span>
  <span class="hljs-keyword">while</span> ( linkedList.next ) &#123;
      res += <span class="hljs-string">'->'</span> + linkedList.next.value;
      linkedList = linkedList.next;
  &#125;
  <span class="hljs-comment">// 返回数据</span>
  <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>链表可以实现的东西很多。是个非常不错的数据结构。比如可以用链表来实现一个微型的JavaScript中的数组，实现一个栈，实现一个队列。后期如果有空我再更新一章关于链表实现一个微型数组的文章。</p>
<p>关于链表的介绍和一些功能的实现就已经结束了，讲的不是很详细，如果有讲的不对的地方。代码规范，代码逻辑错误的地方，希望您可以多多指教。</p>
<p>关于上面介绍的链表的源代码我放到了gitee上，本来想放github上，不知道为啥今天上不去。我在上面也分享了一些在力扣上刷题的题解，今天分享了链表，我也对应找了一道 力扣上关于链表的中等题来实现。有兴趣的可以去看看，顺便点个小星星呀。谢谢</p>
<p>刚到掘金来。其他历史文章在公众号分享的，感兴趣的朋友可以关注一波公众号。以后也会同步更新公众号和掘金</p>
<pre><code class="copyable">    gitee地址：https://gitee.com/chengxinyingtianxia/leetcode
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            