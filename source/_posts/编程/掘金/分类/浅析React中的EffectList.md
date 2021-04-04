
---
title: '浅析React中的EffectList'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2252'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 21:22:24 GMT
thumbnail: 'https://picsum.photos/400/300?random=2252'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>React中，会遍历EffectList来执行节点操作、生命周期方法、Effect方法，可以把EffectList比作圣诞树上挂的彩灯，而这颗圣诞树就是Fiber树。</p>
<p>为什么会存在EffectList呢？打个比方来说，一颗Fiber树中有一些Fiber节点需要执行<code>componentDidMount</code>方法，如果在Fiber树构建完成后，再遍历一次Fiber树，找到需要执行<code>componentDidMount</code>方法的Fiber节点，这是非常低效的。</p>
<p>而EffectList就解决了这个问题，在Fiber树构建过程中，每当一个Fiber节点的<code>flags</code>字段不为<code>NoFlags</code>时（代表需要执行副作用），就把该Fiber节点添加到EffectList，在Fiber树构建完成后，由Fiber节点串成的彩灯也构建完成了，这样仅仅需要遍历彩灯就行了。</p>
<h2 data-id="heading-0">EffectList的收集</h2>
<p>EffectList是一个单向链表，<code>firstEffect</code>代表链表中的第一个Fiber节点，<code>lastEffect</code>代表链表中的最后一个Fiber节点。</p>
<p>Fiber树的构建是深度优先的，也就是先向下构建子级Fiber节点，子级节点构建完成后，再向上构建父级Fiber节点，所以EffectList中总是子级Fiber节点在前面。</p>
<p>Fiber节点构建完成的操作执行在<code>completeUnitOfWork</code>方法，在这个方法里，不仅会对节点完成构建，也会将有<code>flags</code>的Fiber节点添加到EffectList。</p>
<p>简化代码如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">completeUnitOfWork</span>(<span class="hljs-params">unitOfWork: Fiber</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">let</span> completedWork = unitOfWork;
  <span class="hljs-keyword">do</span> &#123;
    <span class="hljs-keyword">const</span> current = completedWork.alternate;
    <span class="hljs-keyword">const</span> returnFiber = completedWork.return;
    
    <span class="hljs-keyword">let</span> next= completeWork(current, completedWork, subtreeRenderLanes);

    <span class="hljs-comment">// effect list构建</span>
    <span class="hljs-keyword">if</span> (
      returnFiber !== <span class="hljs-literal">null</span> &&
      (returnFiber.flags & Incomplete) === NoFlags
    ) &#123;
      <span class="hljs-comment">// 层层拷贝</span>
      <span class="hljs-keyword">if</span> (returnFiber.firstEffect === <span class="hljs-literal">null</span>) &#123;
        returnFiber.firstEffect = completedWork.firstEffect;
      &#125;
      <span class="hljs-keyword">if</span> (completedWork.lastEffect !== <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// 说明当前节点是兄弟节点，子节点有effect，已经给returnFiber.lastEffect赋值过了</span>
        <span class="hljs-keyword">if</span> (returnFiber.lastEffect !== <span class="hljs-literal">null</span>) &#123;
          <span class="hljs-comment">// 连接兄弟节点的effect</span>
          returnFiber.lastEffect.nextEffect = completedWork.firstEffect;
        &#125;
        returnFiber.lastEffect = completedWork.lastEffect;
      &#125;
      
      <span class="hljs-keyword">const</span> flags = completedWork.flags;
      
      <span class="hljs-comment">// 该fiber节点有effect</span>
      <span class="hljs-keyword">if</span> (flags > PerformedWork) &#123;
        <span class="hljs-comment">// 当前节点有effect连接上effect list</span>
        <span class="hljs-keyword">if</span> (returnFiber.lastEffect !== <span class="hljs-literal">null</span>) &#123;
          returnFiber.lastEffect.nextEffect = completedWork;
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// returnFiber没有firstEffect的情况是第一次遇见有effect的节点</span>
          returnFiber.firstEffect = completedWork;
        &#125;
        returnFiber.lastEffect = completedWork;
      &#125;
    &#125;

    <span class="hljs-comment">// 兄弟元素遍历再到返返回父级</span>
    <span class="hljs-keyword">const</span> siblingFiber = completedWork.sibling;
    <span class="hljs-keyword">if</span> (siblingFiber !== <span class="hljs-literal">null</span>) &#123;
      workInProgress = siblingFiber;
      <span class="hljs-keyword">return</span>;
    &#125;
    completedWork = returnFiber;
    workInProgress = completedWork;
  &#125; <span class="hljs-keyword">while</span> (completedWork !== <span class="hljs-literal">null</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>EffectList实际是像冒泡一样，一层一层不断向上层收集，从第一个有<code>flags</code>的节点开始记录，每层的新节点都会将上一个节点的<code>firstEffect</code>和<code>lastEffect</code>拷贝到自身身上，再供上层节点再次拷贝。</p>
<p>如以下结构，假如每一个<code>div</code>都有<code>flags</code>。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div id=<span class="hljs-string">"1"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"4"</span>/></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"2"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"3"</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终形成的EffectList为</p>
<pre><code class="copyable">firstEffect => div4
lastEffect  => div1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为Fiber树的构建深度优先，所有<code>div4</code>先完成<code>completeWork</code>，构建<code>firstEffect</code>。</p>
<p>EffectList遍历是从<code>firstEffect</code>开始，通过每一个节点的<code>nextEffect</code>找到下一个节点。</p>
<pre><code class="copyable">firstEffect => div4
div4.nextEffect => div3
div3.nextEffect => div2
div2.nextEffect => div1
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">初次Render时的EffectList</h2>
<p>在React中，会对初次Mount有一个性能优化，其中的Fiber节点的<code>flags</code>不会包含<code>placement</code>，对应的DOM节点不会遍历加入DOM树，而是在创建DOM节点时就已经加入DOM树了，只有<code>root</code>Fiber节点<code>FiberRootNode</code>的<code>flags</code>会包含<code>placement</code>。</p>
<p>EffectList是不会包含<code>root</code>节点的，所以需要将<code>root</code>节点也添加到EffectList，这样才会正确的执行<code>placement</code>，让DOM树在页面呈现 。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">let</span> firstEffect;
  <span class="hljs-comment">// 把根节点finishedWork也连接进去</span>
  <span class="hljs-keyword">if</span> (finishedWork.flags > PerformedWork) &#123;
    <span class="hljs-keyword">if</span> (finishedWork.lastEffect !== <span class="hljs-literal">null</span>) &#123;
      finishedWork.lastEffect.nextEffect = finishedWork;
      firstEffect = finishedWork.firstEffect;
    &#125; <span class="hljs-keyword">else</span> &#123;
      firstEffect = finishedWork;
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 根节点没有effect.</span>
    firstEffect = finishedWork.firstEffect;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">EffectList的遍历</h2>
<p>EffectList的主要是用于Layout阶段生命周期方法的执行和DOM的操作。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 处理getSnapshotBeforeUpdate,调度useEffect</span>
nextEffect = firstEffect;
<span class="hljs-keyword">do</span> &#123;
  commitBeforeMutationEffects();
&#125; <span class="hljs-keyword">while</span> (nextEffect !== <span class="hljs-literal">null</span>);
<span class="hljs-comment">// DOM操作</span>
nextEffect = firstEffect;
<span class="hljs-keyword">do</span> &#123;
  commitMutationEffects(root, renderPriorityLevel);
&#125; <span class="hljs-keyword">while</span> (nextEffect !== <span class="hljs-literal">null</span>);
<span class="hljs-comment">// 生命周期方法的执行</span>
nextEffect = firstEffect;
<span class="hljs-keyword">do</span> &#123;
  commitLayoutEffects(root, lanes);
&#125; <span class="hljs-keyword">while</span> (nextEffect !== <span class="hljs-literal">null</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这Layout阶段的这3个方法里，会遍历<code>nextEffect</code>，每执行完一个，就重新指向<code>firstEffect</code>。Layout阶段具体操作就不细讲了。</p>
<h2 data-id="heading-3">总结</h2>
<p>EffectList不是全局变量，只是在Fiber树创建过程中，一层层向上收集有<code>effect</code>的Fiber节点，最终的<code>root</code>节点就会收集到所有有<code>effect</code>到Fiber节点，我们就把这条包含<code>effect</code>节点的链表叫做EffectList。</p>
<p>由于收集的过程是深度优先，子级会先被收集，所以遍历的时候也会先操作子级，所以如果有面试官问子级和父级的生命周期或者<code>useEffect</code>谁先执行，就很清楚的知道会先执行子级操作了。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            