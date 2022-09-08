
---
title: 'React源码分析 - 事件机制'
categories: 
 - 编程
 - 掘金
 - 收藏集
headimg: 'https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/2/26/161cdbf9593d78f9~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sun, 25 Feb 2018 08:16:45 GMT
thumbnail: 'https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/2/26/161cdbf9593d78f9~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body html"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>React的事件机制还是很好玩的，其中模拟事件传递和利用document委托大部分事件的想法比较有意思。</p>
<h3 data-id="heading-0">事件机制流程图</h3>
<p></p><figure><img alt="event-react" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/2/26/161cdbf9593d78f9~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<h3 data-id="heading-1">代码分析</h3>
<p>（代码仅包含涉及事件参数的部分）</p>
<p>_updateDOMProperties是事件参数处理的入口，只要注意enqueuePutListener这个方法就好了，这是注册事件的入口函数。registrationNameModules变量保存事件类型和对应的方法的映射的一个对象，如图：</p>
<p align="center">
<img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/2/26/161cdbf95a27460e~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp" alt="registrationnamemodules" width="539" loading="lazy" referrerpolicy="no-referrer">
</p>
<p>这些映射的初始化的地方在《React源码分析 - 组件初次渲染》解释过了。</p>
<pre><code lang="kotlin" class="hljs language-kotlin copyable">_updateDOMProperties: function (lastProps, nextProps, transaction) &#123;
  <span class="hljs-keyword">var</span> propKey;
  <span class="hljs-keyword">var</span> styleName;
  <span class="hljs-keyword">var</span> styleUpdates;
  <span class="hljs-keyword">for</span> (propKey <span class="hljs-keyword">in</span> lastProps) &#123;
    <span class="hljs-keyword">if</span> (nextProps.hasOwnProperty(propKey) || !lastProps.hasOwnProperty(propKey) || lastProps[propKey] == <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">continue</span>;
    &#125;
    <span class="hljs-keyword">if</span> (registrationNameModules.hasOwnProperty(propKey)) &#123;
      <span class="hljs-keyword">if</span> (lastProps[propKey]) &#123;
        <span class="hljs-comment">// Only call deleteListener if there was a listener previously or</span>
        <span class="hljs-comment">// else willDeleteListener gets called when there wasn't actually a</span>
        <span class="hljs-comment">// listener (e.g., onClick=&#123;null&#125;)</span>
        deleteListener(<span class="hljs-keyword">this</span>, propKey);
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">for</span> (propKey <span class="hljs-keyword">in</span> nextProps) &#123;
    <span class="hljs-keyword">var</span> nextProp = nextProps[propKey];
    <span class="hljs-keyword">var</span> lastProp = propKey === STYLE ? <span class="hljs-keyword">this</span>._previousStyleCopy : lastProps != <span class="hljs-literal">null</span> ? lastProps[propKey] : undefined;
    <span class="hljs-keyword">if</span> (!nextProps.hasOwnProperty(propKey) || nextProp === lastProp || nextProp == <span class="hljs-literal">null</span> && lastProp == <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">continue</span>;
    &#125;
    <span class="hljs-keyword">if</span> (registrationNameModules.hasOwnProperty(propKey)) &#123; <span class="hljs-comment">// 处理事件参数。</span>
      <span class="hljs-keyword">if</span> (nextProp) &#123;
        enqueuePutListener(<span class="hljs-keyword">this</span>, propKey, nextProp, transaction); <span class="hljs-comment">// 注册事件，委托到属于的document上</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (lastProp) &#123;
        deleteListener(<span class="hljs-keyword">this</span>, propKey);
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p><strong>enqueuePutListener</strong></p>
<ul>
<li>listenTo</li>
<li>putListener</li>
</ul>
<pre><code lang="php" class="hljs language-php copyable"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">enqueuePutListener</span>(<span class="hljs-params">inst, registrationName, listener, transaction</span>) </span>&#123;
  <span class="hljs-keyword">var</span> containerInfo = inst._nativeContainerInfo;
  <span class="hljs-keyword">var</span> doc = containerInfo._ownerDocument; <span class="hljs-comment">// 大部分的事件都被到对应的document上</span>
  <span class="hljs-keyword">if</span> (!doc) &#123; <span class="hljs-comment">// ssr</span>
    <span class="hljs-comment">// Server rendering.</span>
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-title function_ invoke__">listenTo</span>(registrationName, doc);
  transaction.<span class="hljs-title function_ invoke__">getReactMountReady</span>().<span class="hljs-title function_ invoke__">enqueue</span>(putListener, &#123;
    <span class="hljs-attr">inst</span>: inst,
    <span class="hljs-attr">registrationName</span>: registrationName,
    <span class="hljs-attr">listener</span>: listener
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p><strong>listenTo</strong>是将事件委托到document的方法，大部分事件是委托到document上的。但是因为document上能够catch的事件类型的限制(<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2F2000%2FREC-DOM-Level-2-Events-20001113%2Fevents.html%23Events-DocumentEvent" title="https://www.w3.org/TR/2000/REC-DOM-Level-2-Events-20001113/events.html#Events-DocumentEvent" ref="nofollow noopener noreferrer">Document Object Model Events</a>)，不是所有的事件类型都委托到document，少部分是直接委托到元素本身上的。</p>
<p><strong>putListener</strong>将对应的类型的事件、事件的目标对象和事件触发时执行的方法添加到listenerBank对象中。</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-attr">listenTo</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">registrationName, contentDocumentHandle</span>) &#123;
  <span class="hljs-keyword">var</span> mountAt = contentDocumentHandle;
  <span class="hljs-keyword">var</span> isListening = <span class="hljs-title function_">getListeningForDocument</span>(mountAt);
  <span class="hljs-keyword">var</span> dependencies = <span class="hljs-title class_">EventPluginRegistry</span>.<span class="hljs-property">registrationNameDependencies</span>[registrationName];

  <span class="hljs-keyword">var</span> topLevelTypes = <span class="hljs-title class_">EventConstants</span>.<span class="hljs-property">topLevelTypes</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < dependencies.<span class="hljs-property">length</span>; i++) &#123;
    <span class="hljs-keyword">var</span> dependency = dependencies[i];
    <span class="hljs-keyword">if</span> (!(isListening.<span class="hljs-title function_">hasOwnProperty</span>(dependency) && isListening[dependency])) &#123;
      <span class="hljs-comment">// 先判断先几个需要特殊处理的事件，主要都是兼容性的原因。</span>
      <span class="hljs-keyword">if</span> (...) &#123;
        ......
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (topEventMapping.<span class="hljs-title function_">hasOwnProperty</span>(dependency)) &#123;
        <span class="hljs-title class_">ReactBrowserEventEmitter</span>.<span class="hljs-property">ReactEventListener</span>.<span class="hljs-title function_">trapBubbledEvent</span>(dependency, topEventMapping[dependency], mountAt);
      &#125;
      isListening[dependency] = <span class="hljs-literal">true</span>;
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// 冒泡阶段的触发的事件的委托</span>
<span class="hljs-attr">trapBubbledEvent</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">topLevelType, handlerBaseName, handle</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-title class_">ReactBrowserEventEmitter</span>.<span class="hljs-property">ReactEventListener</span>.<span class="hljs-title function_">trapBubbledEvent</span>(topLevelType, handlerBaseName, handle);
&#125;,

<span class="hljs-comment">// 捕获阶段的触发的事件的委托</span>
<span class="hljs-attr">trapCapturedEvent</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">topLevelType, handlerBaseName, handle</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-title class_">ReactBrowserEventEmitter</span>.<span class="hljs-property">ReactEventListener</span>.<span class="hljs-title function_">trapCapturedEvent</span>(topLevelType, handlerBaseName, handle);
&#125;,

<span class="hljs-attr">trapBubbledEvent</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">topLevelType, handlerBaseName, handle</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-title class_">EventListener</span>.<span class="hljs-title function_">listen</span>(element, handlerBaseName, <span class="hljs-title class_">ReactEventListener</span>.<span class="hljs-property">dispatchEvent</span>.<span class="hljs-title function_">bind</span>(<span class="hljs-literal">null</span>, topLevelType));
&#125;,

<span class="hljs-attr">trapCapturedEvent</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">topLevelType, handlerBaseName, handle</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-title class_">EventListener</span>.<span class="hljs-title function_">capture</span>(element, handlerBaseName, <span class="hljs-title class_">ReactEventListener</span>.<span class="hljs-property">dispatchEvent</span>.<span class="hljs-title function_">bind</span>(<span class="hljs-literal">null</span>, topLevelType));
&#125;,

<span class="hljs-attr">listen</span>: <span class="hljs-keyword">function</span> <span class="hljs-title function_">listen</span>(<span class="hljs-params">target, eventType, callback</span>) &#123;
  <span class="hljs-keyword">if</span> (target.<span class="hljs-property">addEventListener</span>) &#123;
    target.<span class="hljs-title function_">addEventListener</span>(eventType, callback, <span class="hljs-literal">false</span>);
  &#125;
&#125;,

<span class="hljs-attr">capture</span>: <span class="hljs-keyword">function</span> <span class="hljs-title function_">capture</span>(<span class="hljs-params">target, eventType, callback</span>) &#123;
  <span class="hljs-keyword">if</span> (target.<span class="hljs-property">addEventListener</span>) &#123;
    target.<span class="hljs-title function_">addEventListener</span>(eventType, callback, <span class="hljs-literal">true</span>);
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre><p>重点在于所有的委托的事件的回调函数都是ReactEventListener.dispatchEvent。</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-attr">dispatchEvent</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">topLevelType, nativeEvent</span>) &#123;
  <span class="hljs-comment">// bookKeeping的初始化使用了react在源码中用到的对象池的方法来避免多余的垃圾回收。</span>
  <span class="hljs-comment">// bookKeeping的作用看ta的定义就知道了，就是一个用来保存过程中会使用到的变量的对象。</span>
  <span class="hljs-keyword">var</span> bookKeeping = <span class="hljs-title class_">TopLevelCallbackBookKeeping</span>.<span class="hljs-title function_">getPooled</span>(topLevelType, nativeEvent);
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-title class_">ReactUpdates</span>.<span class="hljs-title function_">batchedUpdates</span>(handleTopLevelImpl, bookKeeping);
  &#125; <span class="hljs-keyword">finally</span> &#123;
    <span class="hljs-title class_">TopLevelCallbackBookKeeping</span>.<span class="hljs-title function_">release</span>(bookKeeping);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>handleTopLevelImpl方法遍历事件触发对象以及其的父级元素（事件传递），对每个元素执行_handleTopLevel方法。</p>
<pre><code lang="ini" class="hljs language-ini copyable">function handleTopLevelImpl(bookKeeping) &#123;
  var <span class="hljs-attr">nativeEventTarget</span> = getEventTarget(bookKeeping.nativeEvent)<span class="hljs-comment">;</span>
  var <span class="hljs-attr">targetInst</span> = ReactDOMComponentTree.getClosestInstanceFromNode(nativeEventTarget)<span class="hljs-comment">;</span>
  var <span class="hljs-attr">ancestor</span> = targetInst<span class="hljs-comment">;</span>
  do &#123;
    bookKeeping.ancestors.push(ancestor)<span class="hljs-comment">;</span>
    <span class="hljs-attr">ancestor</span> = ancestor && findParent(ancestor)<span class="hljs-comment">;</span>
  &#125; while (ancestor)<span class="hljs-comment">;</span>

  for (var <span class="hljs-attr">i</span> = <span class="hljs-number">0</span><span class="hljs-comment">; i < bookKeeping.ancestors.length; i++) &#123;</span>
    <span class="hljs-attr">targetInst</span> = bookKeeping.ancestors[i]<span class="hljs-comment">;</span>
    ReactEventListener._handleTopLevel(bookKeeping.topLevelType, targetInst, bookKeeping.nativeEvent, getEventTarget(bookKeeping.nativeEvent))<span class="hljs-comment">;</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>handleTopLevel根据事件对象以及触发的事件类型提取出所有需要被执行的事件以及对应的回调函数，统一由runEventQueueInBatch执行。</p>
<pre><code lang="ini" class="hljs language-ini copyable">handleTopLevel: function (topLevelType, targetInst, nativeEvent, nativeEventTarget) &#123;
  var <span class="hljs-attr">events</span> = EventPluginHub.extractEvents(topLevelType, targetInst, nativeEvent, nativeEventTarget)<span class="hljs-comment">;</span>
  runEventQueueInBatch(events)<span class="hljs-comment">;</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>extractEvents方法调用了对应的plugin的extractEvents方法来获取对应的plugin类型的需要执行的事件，然后accumulateInto到一起。</p>
<pre><code lang="ini" class="hljs language-ini copyable">extractEvents: function (topLevelType, targetInst, nativeEvent, nativeEventTarget) &#123;
   var events<span class="hljs-comment">;</span>
   var <span class="hljs-attr">plugins</span> = EventPluginRegistry.plugins<span class="hljs-comment">;</span>
   for (var <span class="hljs-attr">i</span> = <span class="hljs-number">0</span><span class="hljs-comment">; i < plugins.length; i++) &#123;</span>
     // Not every plugin in the ordering may be loaded at runtime.
     var <span class="hljs-attr">possiblePlugin</span> = plugins[i]<span class="hljs-comment">;</span>
     if (possiblePlugin) &#123;
       var <span class="hljs-attr">extractedEvents</span> = possiblePlugin.extractEvents(topLevelType, targetInst, nativeEvent, nativeEventTarget)<span class="hljs-comment">;</span>
       if (extractedEvents) &#123;
         <span class="hljs-attr">events</span> = accumulateInto(events, extractedEvents)<span class="hljs-comment">;</span>
       &#125;
     &#125;
   &#125;
   return events<span class="hljs-comment">;</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>plugin的extractEvents方法中的有意思的地方在于 <strong>EventPropagators.accumulateTwoPhaseDispatches(event)</strong> 。</p>
<p>EventPropagators.accumulateTwoPhaseDispatches中模拟了事件传递的过程即：capture -> target -> bubble 的过程，将这个路径上的所有的符合事件类型的回调函数以及对应的元素按照事件传递的顺序返回。</p>
<p align="center">
<img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/2/26/161cdbf95a3f8121~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp" width="400" loading="lazy" referrerpolicy="no-referrer">
</p>
<p>（图片来自<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-3-Events%2F%23event-flow" title="https://www.w3.org/TR/DOM-Level-3-Events/#event-flow" ref="nofollow noopener noreferrer">Event dispatch and DOM event flow</a>）</p>
<pre><code lang="ini" class="hljs language-ini copyable">function traverseTwoPhase(inst, fn, arg) &#123;
  var <span class="hljs-attr">path</span> = []<span class="hljs-comment">;</span>
  while (inst) &#123;
    path.push(inst)<span class="hljs-comment">;</span>
    <span class="hljs-attr">inst</span> = inst._nativeParent<span class="hljs-comment">;</span>
  &#125;
  var i<span class="hljs-comment">;</span>
  for (<span class="hljs-attr">i</span> = path.length<span class="hljs-comment">; i-- > 0;) &#123;</span>
    fn(path<span class="hljs-section">[i]</span>, false, arg)<span class="hljs-comment">;</span>
  &#125;
  for (<span class="hljs-attr">i</span> = <span class="hljs-number">0</span><span class="hljs-comment">; i < path.length; i++) &#123;</span>
    fn(path<span class="hljs-section">[i]</span>, true, arg)<span class="hljs-comment">;</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>traverseTwoPhase方法模拟了事件传递的过程并且获取对应的回调函数和事件对象保存在react合成的event对象的_dispatchListeners和_dispatchInstances上</p>
<pre><code lang="ini" class="hljs language-ini copyable">function accumulateDirectionalDispatches(inst, upwards, event) &#123;
  var <span class="hljs-attr">phase</span> = upwards ? PropagationPhases.bubbled : PropagationPhases.captured<span class="hljs-comment">;</span>
  var <span class="hljs-attr">listener</span> = listenerAtPhase(inst, event, phase)<span class="hljs-comment">;</span>
  if (listener) &#123;
    // event._dispatchListeners结果就是这个event在event flow的过程中会触发那些listenter的callback【按照event flow的顺序push到一个数组中了】
    <span class="hljs-attr">event._dispatchListeners</span> = accumulateInto(event._dispatchListeners, listener)<span class="hljs-comment">;</span>
    <span class="hljs-attr">event._dispatchInstances</span> = accumulateInto(event._dispatchInstances, inst)<span class="hljs-comment">;</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>查询listener和对应的inst使用的是事件的类型以及_rootNodeID，listenerBank中保存了对应一个类型下元素的回调函数：</p>
<p align="center">
<img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/2/26/161cdbf95a22ace2~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp" alt="listenerBank" width="200" loading="lazy" referrerpolicy="no-referrer">
</p>
<pre><code lang="ini" class="hljs language-ini copyable">function listenerAtPhase(inst, event, propagationPhase) &#123;
  var <span class="hljs-attr">registrationName</span> = event.dispatchConfig.phasedRegistrationNames[propagationPhase]<span class="hljs-comment">;</span>
  return getListener(inst, registrationName)<span class="hljs-comment">;</span>
&#125;

getListener: function (inst, registrationName) &#123;
    var <span class="hljs-attr">bankForRegistrationName</span> = listenerBank[registrationName]<span class="hljs-comment">;</span>
    return bankForRegistrationName && bankForRegistrationName<span class="hljs-section">[inst._rootNodeID]</span><span class="hljs-comment">;</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre><p>对于listenerBank内容的生成由之前说的第二个主要方法putListener完成。</p>
<p><strong>putListener</strong> 使用事务的方式统一在ReactMountReady阶段执行。</p>
<pre><code lang="css" class="hljs language-css copyable">putListener: function (inst, registrationName, listener) &#123;
  <span class="hljs-selector-tag">var</span> bankForRegistrationName = listenerBank<span class="hljs-selector-attr">[registrationName]</span> || (listenerBank<span class="hljs-selector-attr">[registrationName]</span> = &#123;&#125;);
  bankForRegistrationName<span class="hljs-selector-attr">[inst._rootNodeID]</span> = listener;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>在extractEvents了对应触发的事件类型的events后通过runEventQueueInBatch(events)将所有的合成事件放到事件队列里面，第二步是逐个执行</p>
<pre><code lang="ini" class="hljs language-ini copyable">function runEventQueueInBatch(events) &#123;
  EventPluginHub.enqueueEvents(events)<span class="hljs-comment">;</span>
  EventPluginHub.processEventQueue(false)<span class="hljs-comment">;</span>
&#125;

function executeDispatchesInOrder(event, simulated) &#123;
  var <span class="hljs-attr">dispatchListeners</span> = event._dispatchListeners<span class="hljs-comment">;</span>
  var <span class="hljs-attr">dispatchInstances</span> = event._dispatchInstances<span class="hljs-comment">;</span>
  if (process.env.NODE_ENV !== 'production') &#123;
    validateEventDispatches(event)<span class="hljs-comment">;</span>
  &#125;
  if (Array.isArray(dispatchListeners)) &#123;
    for (var <span class="hljs-attr">i</span> = <span class="hljs-number">0</span><span class="hljs-comment">; i < dispatchListeners.length; i++) &#123;</span>
      if (event.isPropagationStopped()) &#123;
        break<span class="hljs-comment">;</span>
      &#125;
      // Listeners and Instances are two parallel arrays that are always in sync.
      executeDispatch(event, simulated, dispatchListeners<span class="hljs-section">[i]</span>, dispatchInstances<span class="hljs-section">[i]</span>)<span class="hljs-comment">;</span>
    &#125;
  &#125; else if (dispatchListeners) &#123;
    executeDispatch(event, simulated, dispatchListeners, dispatchInstances)<span class="hljs-comment">;</span>
  &#125;
  <span class="hljs-attr">event._dispatchListeners</span> = null<span class="hljs-comment">;</span>
  <span class="hljs-attr">event._dispatchInstances</span> = null<span class="hljs-comment">;</span>
&#125;

function executeDispatch(event, simulated, listener, inst) &#123;
  var <span class="hljs-attr">type</span> = event.type || <span class="hljs-string">'unknown-event'</span><span class="hljs-comment">;</span>
  <span class="hljs-attr">event.currentTarget</span> = EventPluginUtils.getNodeFromInstance(inst)<span class="hljs-comment">;</span>
  if (simulated) &#123;
    ReactErrorUtils.invokeGuardedCallbackWithCatch(type, listener, event)<span class="hljs-comment">;</span>
  &#125; else &#123;
    ReactErrorUtils.invokeGuardedCallback(type, listener, event)<span class="hljs-comment">;</span>
  &#125;
  <span class="hljs-attr">event.currentTarget</span> = null<span class="hljs-comment">;</span>
&#125;

function invokeGuardedCallback(name, func, a, b) &#123;
  try &#123;
    return func(a, b)<span class="hljs-comment">;</span>
  &#125; catch (x) &#123;
    if (<span class="hljs-attr">caughtError</span> === null) &#123;
      <span class="hljs-attr">caughtError</span> = x<span class="hljs-comment">;</span>
    &#125;
    return undefined<span class="hljs-comment">;</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><h3 data-id="heading-2">总结</h3>
<ul>
<li>统一的分发函数dispatchEvent。</li>
<li>React的事件对象是合成对象(SyntheticEvent)。</li>
<li>几乎所有的事件都委托到document，达到性能优化的目的。</li>
<li>合成事件与原生事件混用要注意React的事件基本都是委托到document。</li>
</ul>
<p>参考资料</p>
<ul>
<li><a target="_blank" href="https://link.juejin.cn/?target=http%3A%2F%2Fzhenhua-lee.github.io%2Freact%2Freact-event.html" title="http://zhenhua-lee.github.io/react/react-event.html" ref="nofollow noopener noreferrer">React源码解读系列 – 事件机制</a></li>
<li><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-3-Events%2F%23ui-events-intro" title="https://www.w3.org/TR/DOM-Level-3-Events/#ui-events-intro" ref="nofollow noopener noreferrer">UI Events</a></li>
<li><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2F2000%2FREC-DOM-Level-2-Events-20001113%2Fevents.html%23Events-EventTarget" title="https://www.w3.org/TR/2000/REC-DOM-Level-2-Events-20001113/events.html#Events-EventTarget" ref="nofollow noopener noreferrer">Document Object Model Events</a></li>
</ul>
</div>  
</div>
            