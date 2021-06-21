
---
title: '写给进阶玩家的 React 事件系统原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be23a7ffcf4542e98e4aa0e175575c98~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 05:01:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be23a7ffcf4542e98e4aa0e175575c98~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><em>【 简介 】</em></h2>
<p>React 合成事件是 React <strong>模拟原生 DOM 事件所有能力的一个对象</strong>，它根据 W3C规范来定义合成事件，<strong>兼容所有浏览器</strong>，<strong>拥有与浏览器原生事件相同的接口</strong>。</p>
<p><strong>react官方描述</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be23a7ffcf4542e98e4aa0e175575c98~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>分别打印出合成事件对象e和原生对象e.nativeEvent</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc80c697735b43a0b054d73a5e9548f8~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1"><em>【 React 事件系统架构 】</em></h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf8360a059ac4be59e4a5426533c2384~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">_【 核心代码 】// _我们可以将react系统分成注册和执行两部分去理解：</h2>
<h3 data-id="heading-3">一、注册：</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// </span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">enqueuePutListener</span>(<span class="hljs-params">inst, registrationName, listener, transaction</span>) </span>&#123;
    ...
  <span class="hljs-keyword">var</span> isDocumentFragment = containerInfo._node && containerInfo._node.nodeType === DOC_FRAGMENT_TYPE;
  <span class="hljs-number">1.</span> 找到<span class="hljs-built_in">document</span>
  <span class="hljs-keyword">var</span> doc = isDocumentFragment ? containerInfo._node : containerInfo._ownerDocument;
  <span class="hljs-number">2.</span> 注册事件，将事件注册到<span class="hljs-built_in">document</span>上
  <span class="hljs-number">3.</span> listenTo(registrationName, doc);
  存储事件,放入事务队列中
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>react事件系统内部对事件在不同浏览器上的执行做了兼容因此无需使用者考虑浏览器相关情况：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts">  listen: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">listen</span>(<span class="hljs-params">target, eventType, callback</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (target.addEventListener) &#123;
      将原生事件添加到target这个dom上,也就是上边传递的<span class="hljs-built_in">document</span>上
      这就是只有<span class="hljs-built_in">document</span>这个DOM节点上有原生事件的原因
      target.addEventListener(eventType, callback, <span class="hljs-literal">false</span>);
      ...
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (target.attachEvent) &#123;
      target.attachEvent(<span class="hljs-string">'on'</span> + eventType, callback);
      ...
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">二、执行：</h3>
<h4 data-id="heading-5"><strong>事件分发dispatchEvent（react合成事件的冒泡机制）</strong></h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleTopLevelImpl</span>(<span class="hljs-params">bookKeeping</span>) </span>&#123;
  <span class="hljs-number">1.</span> 找到事件触发的DOM和React Component
  <span class="hljs-keyword">var</span> nativeEventTarget = getEventTarget(bookKeeping.nativeEvent);
  <span class="hljs-keyword">var</span> targetInst = ReactDOMComponentTree.getClosestInstanceFromNode(nativeEventTarget);

  <span class="hljs-number">2.</span> 执行事件回调前,先由当前组件向上遍历它的所有父组件。
  得到ancestors这个数组，这个数组同时也是冒泡顺序。
  <span class="hljs-keyword">var</span> ancestor = targetInst;
  <span class="hljs-keyword">do</span> &#123;
    bookKeeping.ancestors.push(ancestor);
    ancestor = ancestor && findParent(ancestor);
  &#125; <span class="hljs-keyword">while</span> (ancestor);

  这个顺序就是冒泡的顺序,并且我们发现不能通过stopPropagation来阻止<span class="hljs-string">'冒泡'</span>。
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < bookKeeping.ancestors.length; i++) &#123;
    targetInst = bookKeeping.ancestors[i];
    ReactEventListener._handleTopLevel(bookKeeping.topLevelType, targetInst, bookKeeping.nativeEvent, getEventTarget(bookKeeping.nativeEvent));
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6"><strong>handleTopLevel 构造合成事件并执行（依赖EventPluginHub）</strong></h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-number">1.</span> 初始化时将eventPlugin注册到EventPluginHub中，不同plugin分别构造不同类型的合成事件
  ReactInjection.EventPluginHub.injectEventPluginsByName(&#123;
    ...不同插件
  &#125;);
  
<span class="hljs-number">2.</span> 将事件放入事件池：
   EventPluginHub.enqueueEvents(events);
<span class="hljs-number">3.</span> 再处理队列中的事件,包括之前未处理完的：
   EventPluginHub.processEventQueue(<span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7"><em>【 合成事件、原生事件混用demo】</em></h2>
<p>刚接触react的同学，往往在react事件使用时会与原生事件混合（这里并非指责这种混用行为，只是在混用阶段需要区分出react时间系统和js本身事件的执行差异），时常会有事件执行出现不符合预期的情况，这里我们用一个小demo来感受下二者执行的差异：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf4670065dda43c99c847f85909a0f8f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76269b52d10541fdaa551a025a5d7b81~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
打印出执行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eede971cb36c4237a7607837a1284f02~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">由此我们可以了解到如下原生事件、react事件、document上挂载事件执行顺序：</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4adc56dcae044223ad7682ca765097a3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9"><em>【 合成事件存在意义 】</em></h2>
<h3 data-id="heading-10">1.统一管理（document）</h3>
<p>react事件集中在document上集中管理</p>
<h3 data-id="heading-11">2.不同浏览器兼容问题</h3>
<h3 data-id="heading-12">3.减少事件创建销毁的性能损耗（避免频繁的垃圾回收机制）</h3>
<p>react事件队列的存储和取出使用缓解了dom元素注册销毁所消耗的性能</p>
<h3 data-id="heading-13">4.利用合成事件的冒泡从document中触发的特性</h3>
<h2 data-id="heading-14"><em>【 合成事件中存在的问题 】</em></h2>
<h4 data-id="heading-15">1.原生事件和合成事件混用时原生事件对入react合成事件的影响</h4>
<ul>
<li>原生事件中禁止冒泡会阻止react合成事件的执行</li>
<li>react合成事件禁止冒泡不会对原生生效</li>
</ul>
<h4 data-id="heading-16">2.事件池中中事件处理函数全部被调用之后，所有属性都会被置为 null</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20b97d6ebb8a48529288615318ff5373~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ea7e8f469ab4f5faca084927b91f0ed~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-17">避免方法：</h5>
<ul>
<li><code>e.persist()</code> //可以阻止事件池清掉取出事件</li>
<li>17版本react会有废弃事件池等更改，此现象也不会存在</li>
</ul>
<h4 data-id="heading-18">3.不同版本的 React 组件嵌套使用时，e.stopPropagation无法正常工作（两个不同版本的事件系统是独立的，都注册到document时的时间不相同）</h4>
<h2 data-id="heading-19"><em>【 相关参考 】</em></h2>
<ul>
<li><a href="https://react.docschina.org/" target="_blank" rel="nofollow noopener noreferrer">react.docschina.org/</a></li>
<li><a href="https://github.com/facebook/react/" target="_blank" rel="nofollow noopener noreferrer">github.com/facebook/re…</a></li>
<li><a href="https://www.cnblogs.com/ayqy/p/react-17.html" target="_blank" rel="nofollow noopener noreferrer">React 17 要来了，非常特别的一版 - 梦烬 - 博客园</a></li>
</ul></div>  
</div>
            