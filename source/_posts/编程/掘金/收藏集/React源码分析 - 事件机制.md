
---
title: 'React源码分析 - 事件机制'
categories: 
 - 编程
 - 掘金
 - 收藏集
headimg: 'https://user-gold-cdn.xitu.io/2018/2/26/161cdbf9593d78f9?imageView2/0/w/1280/h/960/ignore-error/1'
author: 掘金
comments: false
date: Sun, 25 Feb 2018 08:16:45 GMT
thumbnail: 'https://user-gold-cdn.xitu.io/2018/2/26/161cdbf9593d78f9?imageView2/0/w/1280/h/960/ignore-error/1'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>React的事件机制还是很好玩的，其中模拟事件传递和利用document委托大部分事件的想法比较有意思。</p>
<h3 data-id="heading-0">事件机制流程图</h3>
<p></p><figure><img alt="event-react" src="https://user-gold-cdn.xitu.io/2018/2/26/161cdbf9593d78f9?imageView2/0/w/1280/h/960/ignore-error/1" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<h3 data-id="heading-1">代码分析</h3>
<p>（代码仅包含涉及事件参数的部分）</p>
<p>_updateDOMProperties是事件参数处理的入口，只要注意enqueuePutListener这个方法就好了，这是注册事件的入口函数。registrationNameModules变量保存事件类型和对应的方法的映射的一个对象，如图：</p>
<p align="center">
<img src="https://user-gold-cdn.xitu.io/2018/2/26/161cdbf95a27460e?imageView2/0/w/1280/h/960/ignore-error/1" alt="registrationnamemodules" width="539" loading="lazy" referrerpolicy="no-referrer">
</p>
<p>这些映射的初始化的地方在《React源码分析 - 组件初次渲染》解释过了。</p>
<pre><code lang="javascript" class="copyable">_updateDOMProperties: <span><span>function</span> (<span>lastProps, nextProps, transaction</span>) </span>&#123;
  <span>var</span> propKey;
  <span>var</span> styleName;
  <span>var</span> styleUpdates;
  <span>for</span> (propKey <span>in</span> lastProps) &#123;
    <span>if</span> (nextProps.hasOwnProperty(propKey) || !lastProps.hasOwnProperty(propKey) || lastProps[propKey] == <span>null</span>) &#123;
      <span>continue</span>;
    &#125;
    <span>if</span> (registrationNameModules.hasOwnProperty(propKey)) &#123;
      <span>if</span> (lastProps[propKey]) &#123;
        <span>// Only call deleteListener if there was a listener previously or</span>
        <span>// else willDeleteListener gets called when there wasn't actually a</span>
        <span>// listener (e.g., onClick=&#123;null&#125;)</span>
        deleteListener(<span>this</span>, propKey);
      &#125;
    &#125;
  &#125;
  <span>for</span> (propKey <span>in</span> nextProps) &#123;
    <span>var</span> nextProp = nextProps[propKey];
    <span>var</span> lastProp = propKey === STYLE ? <span>this</span>._previousStyleCopy : lastProps != <span>null</span> ? lastProps[propKey] : <span>undefined</span>;
    <span>if</span> (!nextProps.hasOwnProperty(propKey) || nextProp === lastProp || nextProp == <span>null</span> && lastProp == <span>null</span>) &#123;
      <span>continue</span>;
    &#125;
    <span>if</span> (registrationNameModules.hasOwnProperty(propKey)) &#123; <span>// 处理事件参数。</span>
      <span>if</span> (nextProp) &#123;
        enqueuePutListener(<span>this</span>, propKey, nextProp, transaction); <span>// 注册事件，委托到属于的document上</span>
      &#125; <span>else</span> <span>if</span> (lastProp) &#123;
        deleteListener(<span>this</span>, propKey);
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p><strong>enqueuePutListener</strong></p>
<ul>
<li>listenTo</li>
<li>putListener</li>
</ul>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>enqueuePutListener</span>(<span>inst, registrationName, listener, transaction</span>) </span>&#123;
  <span>var</span> containerInfo = inst._nativeContainerInfo;
  <span>var</span> doc = containerInfo._ownerDocument; <span>// 大部分的事件都被到对应的document上</span>
  <span>if</span> (!doc) &#123; <span>// ssr</span>
    <span>// Server rendering.</span>
    <span>return</span>;
  &#125;
  listenTo(registrationName, doc);
  transaction.getReactMountReady().enqueue(putListener, &#123;
    <span>inst</span>: inst,
    <span>registrationName</span>: registrationName,
    <span>listener</span>: listener
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p><strong>listenTo</strong>是将事件委托到document的方法，大部分事件是委托到document上的。但是因为document上能够catch的事件类型的限制(<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2F2000%2FREC-DOM-Level-2-Events-20001113%2Fevents.html%23Events-DocumentEvent" title="https://www.w3.org/TR/2000/REC-DOM-Level-2-Events-20001113/events.html#Events-DocumentEvent" ref="nofollow noopener noreferrer">Document Object Model Events</a>)，不是所有的事件类型都委托到document，少部分是直接委托到元素本身上的。</p>
<p><strong>putListener</strong>将对应的类型的事件、事件的目标对象和事件触发时执行的方法添加到listenerBank对象中。</p>
<pre><code lang="javascript" class="copyable">listenTo: <span><span>function</span> (<span>registrationName, contentDocumentHandle</span>) </span>&#123;
  <span>var</span> mountAt = contentDocumentHandle;
  <span>var</span> isListening = getListeningForDocument(mountAt);
  <span>var</span> dependencies = EventPluginRegistry.registrationNameDependencies[registrationName];

  <span>var</span> topLevelTypes = EventConstants.topLevelTypes;
  <span>for</span> (<span>var</span> i = <span>0</span>; i < dependencies.length; i++) &#123;
    <span>var</span> dependency = dependencies[i];
    <span>if</span> (!(isListening.hasOwnProperty(dependency) && isListening[dependency])) &#123;
      <span>// 先判断先几个需要特殊处理的事件，主要都是兼容性的原因。</span>
      <span>if</span> (...) &#123;
        ......
      &#125; <span>else</span> <span>if</span> (topEventMapping.hasOwnProperty(dependency)) &#123;
        ReactBrowserEventEmitter.ReactEventListener.trapBubbledEvent(dependency, topEventMapping[dependency], mountAt);
      &#125;
      isListening[dependency] = <span>true</span>;
    &#125;
  &#125;
&#125;

<span>// 冒泡阶段的触发的事件的委托</span>
trapBubbledEvent: <span><span>function</span> (<span>topLevelType, handlerBaseName, handle</span>) </span>&#123;
  <span>return</span> ReactBrowserEventEmitter.ReactEventListener.trapBubbledEvent(topLevelType, handlerBaseName, handle);
&#125;,

<span>// 捕获阶段的触发的事件的委托</span>
trapCapturedEvent: <span><span>function</span> (<span>topLevelType, handlerBaseName, handle</span>) </span>&#123;
  <span>return</span> ReactBrowserEventEmitter.ReactEventListener.trapCapturedEvent(topLevelType, handlerBaseName, handle);
&#125;,

<span>trapBubbledEvent</span>: <span><span>function</span> (<span>topLevelType, handlerBaseName, handle</span>) </span>&#123;
  <span>return</span> EventListener.listen(element, handlerBaseName, ReactEventListener.dispatchEvent.bind(<span>null</span>, topLevelType));
&#125;,

<span>trapCapturedEvent</span>: <span><span>function</span> (<span>topLevelType, handlerBaseName, handle</span>) </span>&#123;
  <span>return</span> EventListener.capture(element, handlerBaseName, ReactEventListener.dispatchEvent.bind(<span>null</span>, topLevelType));
&#125;,

<span>listen</span>: <span><span>function</span> <span>listen</span>(<span>target, eventType, callback</span>) </span>&#123;
  <span>if</span> (target.addEventListener) &#123;
    target.addEventListener(eventType, callback, <span>false</span>);
  &#125;
&#125;,

<span>capture</span>: <span><span>function</span> <span>capture</span>(<span>target, eventType, callback</span>) </span>&#123;
  <span>if</span> (target.addEventListener) &#123;
    target.addEventListener(eventType, callback, <span>true</span>);
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre><p>重点在于所有的委托的事件的回调函数都是ReactEventListener.dispatchEvent。</p>
<pre><code lang="javascript" class="copyable">dispatchEvent: <span><span>function</span> (<span>topLevelType, nativeEvent</span>) </span>&#123;
  <span>// bookKeeping的初始化使用了react在源码中用到的对象池的方法来避免多余的垃圾回收。</span>
  <span>// bookKeeping的作用看ta的定义就知道了，就是一个用来保存过程中会使用到的变量的对象。</span>
  <span>var</span> bookKeeping = TopLevelCallbackBookKeeping.getPooled(topLevelType, nativeEvent);
  <span>try</span> &#123;
    ReactUpdates.batchedUpdates(handleTopLevelImpl, bookKeeping);
  &#125; <span>finally</span> &#123;
    TopLevelCallbackBookKeeping.release(bookKeeping);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>handleTopLevelImpl方法遍历事件触发对象以及其的父级元素（事件传递），对每个元素执行_handleTopLevel方法。</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>handleTopLevelImpl</span>(<span>bookKeeping</span>) </span>&#123;
  <span>var</span> nativeEventTarget = getEventTarget(bookKeeping.nativeEvent);
  <span>var</span> targetInst = ReactDOMComponentTree.getClosestInstanceFromNode(nativeEventTarget);
  <span>var</span> ancestor = targetInst;
  <span>do</span> &#123;
    bookKeeping.ancestors.push(ancestor);
    ancestor = ancestor && findParent(ancestor);
  &#125; <span>while</span> (ancestor);

  <span>for</span> (<span>var</span> i = <span>0</span>; i < bookKeeping.ancestors.length; i++) &#123;
    targetInst = bookKeeping.ancestors[i];
    ReactEventListener._handleTopLevel(bookKeeping.topLevelType, targetInst, bookKeeping.nativeEvent, getEventTarget(bookKeeping.nativeEvent));
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>handleTopLevel根据事件对象以及触发的事件类型提取出所有需要被执行的事件以及对应的回调函数，统一由runEventQueueInBatch执行。</p>
<pre><code lang="javascript" class="copyable">handleTopLevel: <span><span>function</span> (<span>topLevelType, targetInst, nativeEvent, nativeEventTarget</span>) </span>&#123;
  <span>var</span> events = EventPluginHub.extractEvents(topLevelType, targetInst, nativeEvent, nativeEventTarget);
  runEventQueueInBatch(events);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>extractEvents方法调用了对应的plugin的extractEvents方法来获取对应的plugin类型的需要执行的事件，然后accumulateInto到一起。</p>
<pre><code lang="javascript" class="copyable">extractEvents: <span><span>function</span> (<span>topLevelType, targetInst, nativeEvent, nativeEventTarget</span>) </span>&#123;
   <span>var</span> events;
   <span>var</span> plugins = EventPluginRegistry.plugins;
   <span>for</span> (<span>var</span> i = <span>0</span>; i < plugins.length; i++) &#123;
     <span>// Not every plugin in the ordering may be loaded at runtime.</span>
     <span>var</span> possiblePlugin = plugins[i];
     <span>if</span> (possiblePlugin) &#123;
       <span>var</span> extractedEvents = possiblePlugin.extractEvents(topLevelType, targetInst, nativeEvent, nativeEventTarget);
       <span>if</span> (extractedEvents) &#123;
         events = accumulateInto(events, extractedEvents);
       &#125;
     &#125;
   &#125;
   <span>return</span> events;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>plugin的extractEvents方法中的有意思的地方在于 <strong>EventPropagators.accumulateTwoPhaseDispatches(event)</strong> 。</p>
<p>EventPropagators.accumulateTwoPhaseDispatches中模拟了事件传递的过程即：capture -> target -> bubble 的过程，将这个路径上的所有的符合事件类型的回调函数以及对应的元素按照事件传递的顺序返回。</p>
<p align="center">
<img src="https://user-gold-cdn.xitu.io/2018/2/26/161cdbf95a3f8121?imageView2/0/w/1280/h/960/ignore-error/1" width="400" loading="lazy" referrerpolicy="no-referrer">
</p>
<p>（图片来自<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-3-Events%2F%23event-flow" title="https://www.w3.org/TR/DOM-Level-3-Events/#event-flow" ref="nofollow noopener noreferrer">Event dispatch and DOM event flow</a>）</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>traverseTwoPhase</span>(<span>inst, fn, arg</span>) </span>&#123;
  <span>var</span> path = [];
  <span>while</span> (inst) &#123;
    path.push(inst);
    inst = inst._nativeParent;
  &#125;
  <span>var</span> i;
  <span>for</span> (i = path.length; i-- > <span>0</span>;) &#123;
    fn(path[i], <span>false</span>, arg);
  &#125;
  <span>for</span> (i = <span>0</span>; i < path.length; i++) &#123;
    fn(path[i], <span>true</span>, arg);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>traverseTwoPhase方法模拟了事件传递的过程并且获取对应的回调函数和事件对象保存在react合成的event对象的_dispatchListeners和_dispatchInstances上</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>accumulateDirectionalDispatches</span>(<span>inst, upwards, event</span>) </span>&#123;
  <span>var</span> phase = upwards ? PropagationPhases.bubbled : PropagationPhases.captured;
  <span>var</span> listener = listenerAtPhase(inst, event, phase);
  <span>if</span> (listener) &#123;
    <span>// event._dispatchListeners结果就是这个event在event flow的过程中会触发那些listenter的callback【按照event flow的顺序push到一个数组中了】</span>
    event._dispatchListeners = accumulateInto(event._dispatchListeners, listener);
    event._dispatchInstances = accumulateInto(event._dispatchInstances, inst);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>查询listener和对应的inst使用的是事件的类型以及_rootNodeID，listenerBank中保存了对应一个类型下元素的回调函数：</p>
<p align="center">
<img src="https://user-gold-cdn.xitu.io/2018/2/26/161cdbf95a22ace2?imageView2/0/w/1280/h/960/ignore-error/1" alt="listenerBank" width="200" loading="lazy" referrerpolicy="no-referrer">
</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>listenerAtPhase</span>(<span>inst, event, propagationPhase</span>) </span>&#123;
  <span>var</span> registrationName = event.dispatchConfig.phasedRegistrationNames[propagationPhase];
  <span>return</span> getListener(inst, registrationName);
&#125;

getListener: <span><span>function</span> (<span>inst, registrationName</span>) </span>&#123;
    <span>var</span> bankForRegistrationName = listenerBank[registrationName];
    <span>return</span> bankForRegistrationName && bankForRegistrationName[inst._rootNodeID];
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre><p>对于listenerBank内容的生成由之前说的第二个主要方法putListener完成。</p>
<p><strong>putListener</strong> 使用事务的方式统一在ReactMountReady阶段执行。</p>
<pre><code lang="javascript" class="copyable">putListener: <span><span>function</span> (<span>inst, registrationName, listener</span>) </span>&#123;
  <span>var</span> bankForRegistrationName = listenerBank[registrationName] || (listenerBank[registrationName] = &#123;&#125;);
  bankForRegistrationName[inst._rootNodeID] = listener;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>在extractEvents了对应触发的事件类型的events后通过runEventQueueInBatch(events)将所有的合成事件放到事件队列里面，第二步是逐个执行</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>runEventQueueInBatch</span>(<span>events</span>) </span>&#123;
  EventPluginHub.enqueueEvents(events);
  EventPluginHub.processEventQueue(<span>false</span>);
&#125;

<span><span>function</span> <span>executeDispatchesInOrder</span>(<span>event, simulated</span>) </span>&#123;
  <span>var</span> dispatchListeners = event._dispatchListeners;
  <span>var</span> dispatchInstances = event._dispatchInstances;
  <span>if</span> (process.env.NODE_ENV !== <span>'production'</span>) &#123;
    validateEventDispatches(event);
  &#125;
  <span>if</span> (<span>Array</span>.isArray(dispatchListeners)) &#123;
    <span>for</span> (<span>var</span> i = <span>0</span>; i < dispatchListeners.length; i++) &#123;
      <span>if</span> (event.isPropagationStopped()) &#123;
        <span>break</span>;
      &#125;
      <span>// Listeners and Instances are two parallel arrays that are always in sync.</span>
      executeDispatch(event, simulated, dispatchListeners[i], dispatchInstances[i]);
    &#125;
  &#125; <span>else</span> <span>if</span> (dispatchListeners) &#123;
    executeDispatch(event, simulated, dispatchListeners, dispatchInstances);
  &#125;
  event._dispatchListeners = <span>null</span>;
  event._dispatchInstances = <span>null</span>;
&#125;

<span><span>function</span> <span>executeDispatch</span>(<span>event, simulated, listener, inst</span>) </span>&#123;
  <span>var</span> type = event.type || <span>'unknown-event'</span>;
  event.currentTarget = EventPluginUtils.getNodeFromInstance(inst);
  <span>if</span> (simulated) &#123;
    ReactErrorUtils.invokeGuardedCallbackWithCatch(type, listener, event);
  &#125; <span>else</span> &#123;
    ReactErrorUtils.invokeGuardedCallback(type, listener, event);
  &#125;
  event.currentTarget = <span>null</span>;
&#125;

<span><span>function</span> <span>invokeGuardedCallback</span>(<span>name, func, a, b</span>) </span>&#123;
  <span>try</span> &#123;
    <span>return</span> func(a, b);
  &#125; <span>catch</span> (x) &#123;
    <span>if</span> (caughtError === <span>null</span>) &#123;
      caughtError = x;
    &#125;
    <span>return</span> <span>undefined</span>;
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
            