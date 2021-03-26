
---
title: '使用 JS 实现单链表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de110224489846e598587aa05b72f558~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 19:29:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de110224489846e598587aa05b72f558~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>实现单链表中的节点应该具有两个属性：<code>ele</code>  和 <code>next</code>。<code>ele</code>  是当前节点的值，<code>next</code> 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 <code>prev</code> 以指示链表中的上一个节点。文本主要实现一个单链表。</p>
<h3 data-id="heading-0">要在链表类中实现这些功能</h3>
<ul>
<li><code>push(ele)</code>: 向链表尾部添加一个新元素</li>
<li><code>insert(ele, index)</code>: 向链表的特定位置插入一个新元素</li>
<li><code>removeAt(index)</code>: 根据特定位置，从链表中移除元素</li>
<li><code>remove(ele)</code>: 根据元素值，从链表中移除元素</li>
<li><code>getNodeAt(index)</code>: 通用方法，返回链表中特定位置的元素</li>
<li><code>getIndexOf(ele)</code>: 返回元素在链表中的索引</li>
<li><code>isEmpty()</code>: 判断链表是否为空</li>
<li><code>getHead()</code>: 获取链表第一个元素</li>
<li><code>toString()</code>: 返回表示整个链表的字符串</li>
<li><code>getSize()</code>: 返回链表包含的元素个数</li>
</ul>
<img width="70%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de110224489846e598587aa05b72f558~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h3 data-id="heading-1">实现</h3>
<h4 data-id="heading-2">1. 首先定义两个公共方法</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 创建节点
 * 表示我们想要添加到链表中的项
 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CreateNode</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">ele</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.ele = ele; <span class="hljs-comment">// 要加入链表元素的值</span>
    <span class="hljs-comment">// 当一个 Node 实例被创建时，它的 next 指针总是 undefined, 因为我们知道它会是链表的最后一项（push）</span>
    <span class="hljs-built_in">this</span>.next = <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// 指向链表中下一个元素的指针</span>
  &#125;
&#125;
<span class="hljs-comment">/**
 * 比较链表中的元素是否相等
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defaultEquals</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a === b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2. 下面就是链表的核心实现啦</h4>
<pre><code class="hljs language-js copyable" lang="js">**
 * 创建链表
 * <span class="hljs-number">1.</span> head 头指针
 * <span class="hljs-number">2.</span> 最后一个节点的next始终指向 <span class="hljs-literal">undefined</span> 或 <span class="hljs-literal">null</span>
 * <span class="hljs-number">3.</span> 始终只有第一个元素的引用，没有index，需要循环访问列表
 */
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LinkedList</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">equalsFn = defaultEquals</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.count = <span class="hljs-number">0</span>; <span class="hljs-comment">// 链表中元素数量，链表的长度</span>
    <span class="hljs-built_in">this</span>.head = <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// 第一个元素的引用</span>
    <span class="hljs-built_in">this</span>.equalsFn = equalsFn;
  &#125;
  <span class="hljs-comment">/**
   * 向链表尾部添加一个新元素
   */</span>
  <span class="hljs-function"><span class="hljs-title">push</span>(<span class="hljs-params">ele</span>)</span> &#123;
    <span class="hljs-keyword">const</span> node = <span class="hljs-keyword">new</span> CreateNode(ele); <span class="hljs-comment">// CreateNode &#123;ele:123,next:undefined&#125;</span>
    <span class="hljs-comment">// 定义一个当前指针</span>
    <span class="hljs-keyword">let</span> current;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.head === <span class="hljs-literal">undefined</span> || <span class="hljs-built_in">this</span>.head === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-comment">// 链表为空，添加的是第一个元素</span>
      <span class="hljs-built_in">this</span>.head = node;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 链表不为空，向其追加元素</span>
      <span class="hljs-comment">// 因为我们始终只有第一个元素的引用，因此需要循环访问列表，直到找到最后一项</span>
      current = <span class="hljs-built_in">this</span>.head;
      <span class="hljs-keyword">while</span> (current.next !== <span class="hljs-literal">undefined</span> && current.next !== <span class="hljs-literal">null</span>) &#123;
        current = current.next;
      &#125;
      current.next = node;
    &#125;
    <span class="hljs-built_in">this</span>.count++;
  &#125;
  <span class="hljs-comment">/**
   * 根据特定位置，从链表中移除元素
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">index</span></span>
   * <span class="hljs-doctag">@returns </span>返回移除的元素，未找到返回undefined
   */</span>
  <span class="hljs-function"><span class="hljs-title">removeAt</span>(<span class="hljs-params">index</span>)</span> &#123;
    <span class="hljs-comment">// 检查越界值</span>
    <span class="hljs-keyword">if</span> (index >= <span class="hljs-number">0</span> && index < <span class="hljs-built_in">this</span>.count) &#123;
      <span class="hljs-keyword">let</span> current = <span class="hljs-built_in">this</span>.head;
      <span class="hljs-comment">// 移除第一项</span>
      <span class="hljs-keyword">if</span> (index === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">this</span>.head = current.next;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">const</span> previous = <span class="hljs-built_in">this</span>.getNodeAt(index - <span class="hljs-number">1</span>);
        current = previous.next;
        <span class="hljs-comment">// 将previous与current的下一项链接起来，跳过current，从而移除它</span>
        <span class="hljs-comment">// 当前节点就会被丢弃在计算机内存中，等着被垃圾回收器清除</span>
        previous.next = current.next;
      &#125;
      <span class="hljs-built_in">this</span>.count--;
      <span class="hljs-keyword">return</span> current.ele;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>;
  &#125;

  <span class="hljs-comment">/**
   * 返回链表中特定位置的元素(通用)
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">index</span></span>
   * <span class="hljs-doctag">@returns </span>节点元素
   */</span>
  <span class="hljs-function"><span class="hljs-title">getNodeAt</span>(<span class="hljs-params">index</span>)</span> &#123;
    <span class="hljs-comment">// 检查越界值</span>
    <span class="hljs-keyword">if</span> (index >= <span class="hljs-number">0</span> && index <= <span class="hljs-built_in">this</span>.count) &#123;
      <span class="hljs-comment">// 定义一个当前指针</span>
      <span class="hljs-keyword">let</span> current = <span class="hljs-built_in">this</span>.head;
      <span class="hljs-comment">// 遍历节点，直到目标位置</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < index; i++) &#123;
        current = current.next;
      &#125;
      <span class="hljs-keyword">return</span> current;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>;
  &#125;
  <span class="hljs-comment">/**
   * 向链表的特定位置插入一个新元素
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">ele</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">index</span></span>
   * <span class="hljs-doctag">@returns </span>true或false
   */</span>
  <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">ele, index</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (index >= <span class="hljs-number">0</span> && index <= <span class="hljs-built_in">this</span>.count) &#123;
      <span class="hljs-keyword">let</span> newNode = <span class="hljs-keyword">new</span> CreateNode(ele);
      <span class="hljs-keyword">if</span> (index === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-comment">// 注意需要中间变量current</span>
        <span class="hljs-keyword">const</span> current = <span class="hljs-built_in">this</span>.head;
        newNode.next = current;
        <span class="hljs-built_in">this</span>.head = newNode;
        <span class="hljs-comment">// 注意直接这么写是错的</span>
        <span class="hljs-comment">// newNode.next = this.head</span>
        <span class="hljs-comment">// this.head = newNode;</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 也需要中间变量current</span>
        <span class="hljs-keyword">const</span> previous = <span class="hljs-built_in">this</span>.getNodeAt(index - <span class="hljs-number">1</span>);
        <span class="hljs-keyword">const</span> current = previous.next;
        previous.next = newNode;
        newNode.next = current;
      &#125;
      <span class="hljs-built_in">this</span>.count++;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
  <span class="hljs-comment">/**
   * 返回元素在链表中的索引
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">ele</span></span>
   * <span class="hljs-doctag">@returns </span>返回元素的位置，否则返回-1
   */</span>
  <span class="hljs-function"><span class="hljs-title">getIndexOf</span>(<span class="hljs-params">ele</span>)</span> &#123;
    <span class="hljs-keyword">let</span> current = <span class="hljs-built_in">this</span>.head;
    <span class="hljs-keyword">if</span> (current !== <span class="hljs-literal">undefined</span> && current !== <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.count; i++) &#123;
        <span class="hljs-comment">// 此处ele可能不是简单数据类型。如果元素是一个复杂对象的话，允许开发者向 LinkedClass 中传入自定义的函数来判断元素是否相等</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.equalsFn(ele, current.ele)) &#123;
          <span class="hljs-keyword">return</span> i;
        &#125; <span class="hljs-keyword">else</span> &#123;
          current = current.next;
        &#125;
      &#125;
      <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * 根据元素值，从链表中移除元素
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">ele</span></span>
   * <span class="hljs-doctag">@returns </span>返回移除的元素，未找到返回undefined
   */</span>
  <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">ele</span>)</span> &#123;
    <span class="hljs-keyword">const</span> index = <span class="hljs-built_in">this</span>.getIndexOf(ele);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.removeAt(index);
  &#125;
  <span class="hljs-comment">/**
   * 判断链表是否为空
   * <span class="hljs-doctag">@returns </span>true/false
   */</span>
  <span class="hljs-function"><span class="hljs-title">isEmpty</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getSize() === <span class="hljs-number">0</span>;
  &#125;
  <span class="hljs-comment">/**
   * 返回链表包含的元素个数，与数组的 length 属性类似
   * <span class="hljs-doctag">@returns <span class="hljs-variable">number</span></span>
   */</span>
  <span class="hljs-function"><span class="hljs-title">getSize</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.count;
  &#125;
  <span class="hljs-comment">/**
   * 获取链表第一个元素
   * 因为head 变量是 LinkedList 类的私有变量
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-function"><span class="hljs-title">getHead</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.head;
  &#125;
  <span class="hljs-comment">/**
   * 返回表示整个链表的字符串
   * 由于列表项使用了 Node 类，就需要重写继承自 JavaScript 对象默认的 toString 方法，让其只输出元素的值。
   * <span class="hljs-doctag">@returns <span class="hljs-variable">str</span></span>
   */</span>
  <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isEmpty()) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">""</span>;
    &#125;
    <span class="hljs-keyword">let</span> objString = <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.head.ele&#125;</span>`</span>;
    <span class="hljs-keyword">let</span> current = <span class="hljs-built_in">this</span>.head.next;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < <span class="hljs-built_in">this</span>.getSize() && current != <span class="hljs-literal">null</span>; i++) &#123;
      objString = <span class="hljs-string">`<span class="hljs-subst">$&#123;objString&#125;</span>,<span class="hljs-subst">$&#123;current.ele&#125;</span>`</span>;
      current = current.next;
    &#125;
    <span class="hljs-keyword">return</span> objString;
  &#125;
&#125;

<span class="hljs-comment">// 创建一个链表实例，并添加一些数据</span>
<span class="hljs-keyword">let</span> link = <span class="hljs-keyword">new</span> LinkedList();
link.push(<span class="hljs-number">100</span>);
link.push(<span class="hljs-number">200</span>);
link.push(<span class="hljs-number">300</span>);
link.push(<span class="hljs-number">400</span>);
<span class="hljs-comment">// 打印看一下效果，如下面。</span>
<span class="hljs-built_in">console</span>.log(link); <span class="hljs-comment">// 可以看出是一个嵌套的树状结构，链表的最后一个节点指向undefined/null</span>

<span class="hljs-comment">// 继续操作，可以正确获取想要的效果。</span>
link.removeAt(<span class="hljs-number">1</span>); <span class="hljs-comment">// 200</span>
link.insert(<span class="hljs-number">200</span>, <span class="hljs-number">1</span>); <span class="hljs-comment">// true</span>
link.getIndexOf(<span class="hljs-number">200</span>); <span class="hljs-comment">// 1</span>
link.toString(); <span class="hljs-comment">// "100,200,300,400"</span>


<span class="copy-code-btn">复制代码</span></code></pre>
<img width="60%" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6278afaceb24fc794ce3a352f85622c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h3 data-id="heading-4">说明</h3>
<ol>
<li>
<p>使用变量引用我们需要控制的节点非常重要，这样就不会丢失节点之间的链接。 如果我们可以只使用一个变量(previous)，但那样会很难控制节点之间的链接。因此，最好声明一个额外的变量来帮助我们处理这些引用。如例子中的中间变量 <code>current</code>!</p>
</li>
<li>
<p>通过指针的改变，未使用的变量会被自动回收。<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Memory_Management" target="_blank" rel="nofollow noopener noreferrer">理解 JavaScript 垃圾回收器如何工作</a>。</p>
</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            