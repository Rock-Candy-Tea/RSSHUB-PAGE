
---
title: 'react源码解析9.diff算法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/798f5ed215ee44e6b0bf8c5d0a8bba7d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 19:41:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/798f5ed215ee44e6b0bf8c5d0a8bba7d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">react源码解析9.diff算法</h2>
<h4 data-id="heading-1">视频课程（高效学习）：<a href="https://xiaochen1024.com/series/60b1b600712e370039088e24/60b1b636712e370039088e25" target="_blank" rel="nofollow noopener noreferrer">进入课程</a></h4>
<h4 data-id="heading-2">课程目录：</h4>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b311cf10a4003b634719" target="_blank" rel="nofollow noopener noreferrer">1.开篇介绍和面试题</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b31ccf10a4003b63471a" target="_blank" rel="nofollow noopener noreferrer">2.react的设计理念</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b328cf10a4003b63471b" target="_blank" rel="nofollow noopener noreferrer">3.react源码架构</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b32ecf10a4003b63471c" target="_blank" rel="nofollow noopener noreferrer">4.源码目录结构和调试</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b334cf10a4003b63471d" target="_blank" rel="nofollow noopener noreferrer">5.jsx&核心api</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b33acf10a4003b63471e" target="_blank" rel="nofollow noopener noreferrer">6.legacy和concurrent模式入口函数</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b340cf10a4003b63471f" target="_blank" rel="nofollow noopener noreferrer">7.Fiber架构</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b348cf10a4003b634720" target="_blank" rel="nofollow noopener noreferrer">8.render阶段</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b354cf10a4003b634721" target="_blank" rel="nofollow noopener noreferrer">9.diff算法</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b360cf10a4003b634722" target="_blank" rel="nofollow noopener noreferrer">10.commit阶段</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b367cf10a4003b634723" target="_blank" rel="nofollow noopener noreferrer">11.生命周期</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b36ecf10a4003b634724" target="_blank" rel="nofollow noopener noreferrer">12.状态更新流程</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b374cf10a4003b634725" target="_blank" rel="nofollow noopener noreferrer">13.hooks源码</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b37acf10a4003b634726" target="_blank" rel="nofollow noopener noreferrer">14.手写hooks</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b556cf10a4003b634727" target="_blank" rel="nofollow noopener noreferrer">15.scheduler&Lane</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b55ccf10a4003b634728" target="_blank" rel="nofollow noopener noreferrer">16.concurrent模式</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b564cf10a4003b634729" target="_blank" rel="nofollow noopener noreferrer">17.context</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b56ccf10a4003b63472a" target="_blank" rel="nofollow noopener noreferrer">18事件系统</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b57bcf10a4003b63472b" target="_blank" rel="nofollow noopener noreferrer">19.手写迷你版react</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b581cf10a4003b63472c" target="_blank" rel="nofollow noopener noreferrer">20.总结&第一章的面试题解答</a></p>
<p><a href="https://xiaochen1024.com/courseware/60b1b2f6cf10a4003b634718/60b1b587cf10a4003b63472d" target="_blank" rel="nofollow noopener noreferrer">21.demo</a></p>
<p>在render阶段更新Fiber节点时，我们会调用reconcileChildFibers对比current Fiber和jsx对象构建workInProgress Fiber，这里current Fiber是指当前dom对应的fiber树，jsx是class组件render方法或者函数组件的返回值。</p>
<p>在reconcileChildFibers中会根据newChild的类型来进入单节点的diff或者多节点diff</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//ReactChildFiber.old.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildFibers</span>(<span class="hljs-params">
  returnFiber: Fiber,
  currentFirstChild: Fiber | <span class="hljs-literal">null</span>,
  newChild: any,
</span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;

  <span class="hljs-keyword">const</span> isObject = <span class="hljs-keyword">typeof</span> newChild === <span class="hljs-string">'object'</span> && newChild !== <span class="hljs-literal">null</span>;

  <span class="hljs-keyword">if</span> (isObject) &#123;
    <span class="hljs-keyword">switch</span> (newChild.$$typeof) &#123;
      <span class="hljs-keyword">case</span> REACT_ELEMENT_TYPE:
<span class="hljs-comment">//单一节点diff</span>
        <span class="hljs-keyword">return</span> placeSingleChild(
            reconcileSingleElement(
              returnFiber,
              currentFirstChild,
              newChild,
              lanes,
            ),
          );
    &#125;
  &#125;
<span class="hljs-comment">//...</span>
  
  <span class="hljs-keyword">if</span> (isArray(newChild)) &#123;
     <span class="hljs-comment">//多节点diff</span>
    <span class="hljs-keyword">return</span> reconcileChildrenArray(
        returnFiber,
        currentFirstChild,
        newChild,
        lanes,
      );
  &#125;

  <span class="hljs-comment">// 删除节点</span>
  <span class="hljs-keyword">return</span> deleteRemainingChildren(returnFiber, currentFirstChild);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>diff过程的主要流程如下图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/798f5ed215ee44e6b0bf8c5d0a8bba7d~tplv-k3u1fbpfcp-zoom-1.image" alt="react源码9.5" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们知道对比两颗树的复杂度本身是O(n3)，对我们的应用来说这个是不能承受的量级，react为了降低复杂度，提出了三个前提：</p>
<ol>
<li>
<p>只对同级比较，跨层级的dom不会进行复用</p>
</li>
<li>
<p>不同类型节点生成的dom树不同，此时会直接销毁老节点及子孙节点，并新建节点</p>
</li>
<li>
<p>可以通过key来对元素diff的过程提供复用的线索，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></></span></span>
  );
<span class="hljs-keyword">const</span> b = (
  <span class="xml"><span class="hljs-tag"><></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​如果a和b里的元素都没有key，因为节点的更新前后文本节点不同，导致他们都不能复用，所以会销毁之前的节点，并新建节点，但是现在有key了，b中的节点会在老的a中寻找key相同的节点尝试复用，最后发现只是交换位置就可以完成更新，具体对比过程后面会讲到。</p>
</li>
</ol>
<h4 data-id="heading-3">单节点diff</h4>
<p>单点diff有如下几种情况：</p>
<ul>
<li>key和type相同表示可以复用节点</li>
<li>key不同直接标记删除节点，然后新建节点</li>
<li>key相同type不同，标记删除该节点和兄弟节点，然后新创建节点</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileSingleElement</span>(<span class="hljs-params">
  returnFiber: Fiber,
  currentFirstChild: Fiber | <span class="hljs-literal">null</span>,
  element: ReactElement
</span>): <span class="hljs-title">Fiber</span> </span>&#123;
  <span class="hljs-keyword">const</span> key = element.key;
  <span class="hljs-keyword">let</span> child = currentFirstChild;
  
  <span class="hljs-comment">//child节点不为null执行对比</span>
  <span class="hljs-keyword">while</span> (child !== <span class="hljs-literal">null</span>) &#123;

    <span class="hljs-comment">// 1.比较key</span>
    <span class="hljs-keyword">if</span> (child.key === key) &#123;

      <span class="hljs-comment">// 2.比较type</span>

      <span class="hljs-keyword">switch</span> (child.tag) &#123;
        <span class="hljs-comment">//...</span>
        
        <span class="hljs-attr">default</span>: &#123;
          <span class="hljs-keyword">if</span> (child.elementType === element.type) &#123;
            <span class="hljs-comment">// type相同则可以复用 返回复用的节点</span>
            <span class="hljs-keyword">return</span> existing;
          &#125;
          <span class="hljs-comment">// type不同跳出</span>
          <span class="hljs-keyword">break</span>;
        &#125;
      &#125;
      <span class="hljs-comment">//key相同，type不同则把fiber及和兄弟fiber标记删除</span>
      deleteRemainingChildren(returnFiber, child);
      <span class="hljs-keyword">break</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">//key不同直接标记删除该节点</span>
      deleteChild(returnFiber, child);
    &#125;
    child = child.sibling;
  &#125;
   
  <span class="hljs-comment">//新建新Fiber</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">多节点diff</h4>
<p>多节点diff比较复杂，我们分三种情况进行讨论，其中a表示更新前的节点，b表示更新后的节点</p>
<ul>
<li>
<p>属性变化</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">'0'</span>></span>0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></></span></span>
  );
  <span class="hljs-keyword">const</span> b = (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">'00'</span>></span>0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></></span></span>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>type变化</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></></span></span>
  );
  <span class="hljs-keyword">const</span> b = (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></></span></span>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>新增节点</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></></span></span>
  );
  <span class="hljs-keyword">const</span> b = (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"2"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></></span></span>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>节点删除</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"2"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></></span></span>
  );
  <span class="hljs-keyword">const</span> b = (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></></span></span>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>节点位置变化</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></></span></span>
  );
  <span class="hljs-keyword">const</span> b = (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"0"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></></span></span>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>在源码中多节点diff有三个for循环遍历（并不意味着所有更新都有经历三个遍历，进入循环体有条件，也有条件跳出循环），第一个遍历处理节点的更新（包括props更新和type更新和删除），第二个遍历处理其他的情况（节点新增），其原因在于在大多数的应用中，节点更新的频率更加频繁，第三个处理位节点置改变</p>
<ul>
<li>
<p>第一次遍历
因为老的节点存在于current Fiber中，所以它是个链表结构，还记得Fiber双缓存结构嘛，节点通过child、return、sibling连接，而newChildren存在于jsx当中，所以遍历对比的时候，首先让newChildren[i]<code>与</code>oldFiber对比，然后让i++、nextOldFiber = oldFiber.sibling。在第一轮遍历中，会处理三种情况，其中第1，2两种情况会结束第一次循环</p>
<ol>
<li>key不同，第一次循环结束</li>
<li>newChildren或者oldFiber遍历完，第一次循环结束</li>
<li>key同type不同，标记oldFiber为DELETION</li>
<li>key相同type相同则可以复用</li>
</ol>
<p>​    newChildren遍历完，oldFiber没遍历完，在第一次遍历完成之后将oldFiber中没遍历完的节点标记为DELETION，即删除的DELETION Tag</p>
</li>
<li>
<p>第二个遍历
第二个遍历考虑三种情况</p>
<ol>
<li>
<p>newChildren和oldFiber都遍历完：多节点diff过程结束</p>
</li>
<li>
<p>newChildren没遍历完，oldFiber遍历完，将剩下的newChildren的节点标记为Placement，即插入的Tag</p>
</li>
<li>
<p>newChildren和oldFiber没遍历完，则进入节点移动的逻辑</p>
</li>
</ol>
</li>
<li>
<p>第三个遍历
主要逻辑在placeChild函数中，例如更新前节点顺序是ABCD，更新后是ACDB</p>
<ol>
<li>
<p>newChild中第一个位置的A和oldFiber第一个位置的A，key相同可复用，lastPlacedIndex=0</p>
</li>
<li>
<p>newChild中第二个位置的C和oldFiber第二个位置的B，key不同跳出第一次循环，将oldFiber中的BCD保存在map中</p>
</li>
<li>
<p>newChild中第二个位置的C在oldFiber中的index=2 > lastPlacedIndex=0不需要移动，lastPlacedIndex=2</p>
</li>
<li>
<p>newChild中第三个位置的D在oldFiber中的index=3 > lastPlacedIndex=2不需要移动，lastPlacedIndex=3</p>
</li>
<li>
<p>newChild中第四个位置的B在oldFiber中的index=1 < lastPlacedIndex=3,移动到最后</p>
</li>
</ol>
<p><strong>看图更直观</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f84204fe5cf49f9a50c176aa0b79909~tplv-k3u1fbpfcp-zoom-1.image" alt="react源码9.6" loading="lazy" referrerpolicy="no-referrer"></p>
<p>例如更新前节点顺序是ABCD，更新后是DABC</p>
<ol>
<li>
<p>newChild中第一个位置的D和oldFiber第一个位置的A，key不相同不可复用，将oldFiber中的ABCD保存在map中，lastPlacedIndex=0</p>
</li>
<li>
<p>newChild中第一个位置的D在oldFiber中的index=3 > lastPlacedIndex=0不需要移动，lastPlacedIndex=3</p>
<ol start="3">
<li>newChild中第二个位置的A在oldFiber中的index=0 < lastPlacedIndex=3,移动到最后</li>
<li>newChild中第三个位置的B在oldFiber中的index=1 < lastPlacedIndex=3,移动到最后</li>
<li>newChild中第四个位置的C在oldFiber中的index=2 < lastPlacedIndex=3,移动到最后</li>
</ol>
</li>
</ol>
<p><strong>看图更直观</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4091bf615b1842cd9c88f3fbbd204cae~tplv-k3u1fbpfcp-zoom-1.image" alt="react源码9.7" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>​<strong>代码如下</strong>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//ReactChildFiber.old.js</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">placeChild</span>(<span class="hljs-params">newFiber, lastPlacedIndex, newIndex</span>) </span>&#123;
       newFiber.index = newIndex;
   
       <span class="hljs-keyword">if</span> (!shouldTrackSideEffects) &#123;
         <span class="hljs-keyword">return</span> lastPlacedIndex;
       &#125;
   
    <span class="hljs-keyword">var</span> current = newFiber.alternate;
 
       <span class="hljs-keyword">if</span> (current !== <span class="hljs-literal">null</span>) &#123;
         <span class="hljs-keyword">var</span> oldIndex = current.index;
   
         <span class="hljs-keyword">if</span> (oldIndex < lastPlacedIndex) &#123;
           <span class="hljs-comment">//oldIndex小于lastPlacedIndex的位置 则将节点插入到最后</span>
           newFiber.flags = Placement;
           <span class="hljs-keyword">return</span> lastPlacedIndex;
         &#125; <span class="hljs-keyword">else</span> &#123;
           <span class="hljs-keyword">return</span> oldIndex;<span class="hljs-comment">//不需要移动 lastPlacedIndex = oldIndex;</span>
         &#125;
       &#125; <span class="hljs-keyword">else</span> &#123;
         <span class="hljs-comment">//新增插入</span>
         newFiber.flags = Placement;
         <span class="hljs-keyword">return</span> lastPlacedIndex;
       &#125;
     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//ReactChildFiber.old.js</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildrenArray</span>(<span class="hljs-params">
    returnFiber: Fiber,<span class="hljs-comment">//父fiber节点</span>
    currentFirstChild: Fiber | <span class="hljs-literal">null</span>,<span class="hljs-comment">//childs中第一个节点</span>
    newChildren: <span class="hljs-built_in">Array</span><*>,<span class="hljs-comment">//新节点数组 也就是jsx数组</span>
    lanes: Lanes,<span class="hljs-comment">//lane相关 第12章介绍</span>
  </span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;

    <span class="hljs-keyword">let</span> resultingFirstChild: Fiber | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;<span class="hljs-comment">//diff之后返回的第一个节点</span>
    <span class="hljs-keyword">let</span> previousNewFiber: Fiber | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;<span class="hljs-comment">//新节点中上次对比过的节点</span>

    <span class="hljs-keyword">let</span> oldFiber = currentFirstChild;<span class="hljs-comment">//正在对比的oldFiber</span>
    <span class="hljs-keyword">let</span> lastPlacedIndex = <span class="hljs-number">0</span>;<span class="hljs-comment">//上次可复用的节点位置 或者oldFiber的位置</span>
    <span class="hljs-keyword">let</span> newIdx = <span class="hljs-number">0</span>;<span class="hljs-comment">//新节点中对比到了的位置</span>
    <span class="hljs-keyword">let</span> nextOldFiber = <span class="hljs-literal">null</span>;<span class="hljs-comment">//正在对比的oldFiber</span>
    <span class="hljs-keyword">for</span> (; oldFiber !== <span class="hljs-literal">null</span> && newIdx < newChildren.length; newIdx++) &#123;<span class="hljs-comment">//第一次遍历</span>
      <span class="hljs-keyword">if</span> (oldFiber.index > newIdx) &#123;<span class="hljs-comment">//nextOldFiber赋值</span>
        nextOldFiber = oldFiber;
        oldFiber = <span class="hljs-literal">null</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        nextOldFiber = oldFiber.sibling;
      &#125;
      <span class="hljs-keyword">const</span> newFiber = updateSlot(<span class="hljs-comment">//更新节点，如果key不同则newFiber=null</span>
        returnFiber,
        oldFiber,
        newChildren[newIdx],
        lanes,
      );
      <span class="hljs-keyword">if</span> (newFiber === <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">if</span> (oldFiber === <span class="hljs-literal">null</span>) &#123;
          oldFiber = nextOldFiber;
        &#125;
        <span class="hljs-keyword">break</span>;<span class="hljs-comment">//跳出第一次遍历</span>
      &#125;
      <span class="hljs-keyword">if</span> (shouldTrackSideEffects) &#123;<span class="hljs-comment">//检查shouldTrackSideEffects</span>
        <span class="hljs-keyword">if</span> (oldFiber && newFiber.alternate === <span class="hljs-literal">null</span>) &#123;
          deleteChild(returnFiber, oldFiber);
        &#125;
      &#125;
      lastPlacedIndex = placeChild(newFiber, lastPlacedIndex, newIdx);<span class="hljs-comment">//标记节点插入</span>
      <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
        resultingFirstChild = newFiber;
      &#125; <span class="hljs-keyword">else</span> &#123;
        previousNewFiber.sibling = newFiber;
      &#125;
      previousNewFiber = newFiber;
      oldFiber = nextOldFiber;
    &#125;

    <span class="hljs-keyword">if</span> (newIdx === newChildren.length) &#123;
      deleteRemainingChildren(returnFiber, oldFiber);<span class="hljs-comment">//将oldFiber中没遍历完的节点标记为DELETION</span>
      <span class="hljs-keyword">return</span> resultingFirstChild;
    &#125;

    <span class="hljs-keyword">if</span> (oldFiber === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">for</span> (; newIdx < newChildren.length; newIdx++) &#123;<span class="hljs-comment">//第2次遍历</span>
        <span class="hljs-keyword">const</span> newFiber = createChild(returnFiber, newChildren[newIdx], lanes);
        <span class="hljs-keyword">if</span> (newFiber === <span class="hljs-literal">null</span>) &#123;
          <span class="hljs-keyword">continue</span>;
        &#125;
        lastPlacedIndex = placeChild(newFiber, lastPlacedIndex, newIdx);<span class="hljs-comment">//插入新增节点</span>
        <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
          resultingFirstChild = newFiber;
        &#125; <span class="hljs-keyword">else</span> &#123;
          previousNewFiber.sibling = newFiber;
        &#125;
        previousNewFiber = newFiber;
      &#125;
      <span class="hljs-keyword">return</span> resultingFirstChild;
    &#125;

    <span class="hljs-comment">// 将剩下的oldFiber加入map中</span>
    <span class="hljs-keyword">const</span> existingChildren = mapRemainingChildren(returnFiber, oldFiber);

    <span class="hljs-keyword">for</span> (; newIdx < newChildren.length; newIdx++) &#123;<span class="hljs-comment">//第三次循环 处理节点移动</span>
      <span class="hljs-keyword">const</span> newFiber = updateFromMap(
        existingChildren,
        returnFiber,
        newIdx,
        newChildren[newIdx],
        lanes,
      );
      <span class="hljs-keyword">if</span> (newFiber !== <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">if</span> (shouldTrackSideEffects) &#123;
          <span class="hljs-keyword">if</span> (newFiber.alternate !== <span class="hljs-literal">null</span>) &#123;
            existingChildren.delete(<span class="hljs-comment">//删除找到的节点</span>
              newFiber.key === <span class="hljs-literal">null</span> ? newIdx : newFiber.key,
            );
          &#125;
        &#125;
        lastPlacedIndex = placeChild(newFiber, lastPlacedIndex, newIdx);<span class="hljs-comment">//标记为插入的逻辑</span>
        <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
          resultingFirstChild = newFiber;
        &#125; <span class="hljs-keyword">else</span> &#123;
          previousNewFiber.sibling = newFiber;
        &#125;
        previousNewFiber = newFiber;
      &#125;
    &#125;

    <span class="hljs-keyword">if</span> (shouldTrackSideEffects) &#123;
      <span class="hljs-comment">//删除existingChildren中剩下的节点</span>
      existingChildren.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> deleteChild(returnFiber, child));
    &#125;

    <span class="hljs-keyword">return</span> resultingFirstChild;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            