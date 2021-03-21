
---
title: React源码分析 - 事件机制
categories: 
    - 编程
    - 掘金 - 收藏集
author: 掘金 - 收藏集
comments: false
date: Sun, 25 Feb 2018 08:16:45 GMT
thumbnail: https://user-gold-cdn.xitu.io/2018/2/26/161cdbf9593d78f9?imageView2/0/w/1280/h/960/ignore-error/1
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><p>React的事件机制还是很好玩的，其中模拟事件传递和利用document委托大部分事件的想法比较有意思。</p>
<h3 data-id="heading-0">事件机制流程图</h3>
<p></p><figure><img alt="event-react" class="lazyload" src="https://user-gold-cdn.xitu.io/2018/2/26/161cdbf9593d78f9?imageView2/0/w/1280/h/960/ignore-error/1" data-width="825" data-height="1280" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<h3 data-id="heading-1">代码分析</h3>
<p>（代码仅包含涉及事件参数的部分）</p>
<p>_updateDOMProperties是事件参数处理的入口，只要注意enqueuePutListener这个方法就好了，这是注册事件的入口函数。registrationNameModules变量保存事件类型和对应的方法的映射的一个对象，如图：</p>
<p align="center">
<img alt="registrationnamemodules" width="539" class="lazyload" src="https://user-gold-cdn.xitu.io/2018/2/26/161cdbf95a27460e?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1078" data-height="888" referrerpolicy="no-referrer">
</p>
<p>这些映射的初始化的地方在《React源码分析 - 组件初次渲染》解释过了。</p>
<pre><code lang="javascript" class="copyable">_updateDOMProperties: <span><span>function</span> (<span>lastProps, nextProps, transaction</span>) </span>{
  <span>var</span> propKey;
  <span>var</span> styleName;
  <span>var</span> styleUpdates;
  <span>for</span> (propKey <span>in</span> lastProps) {
    <span>if</span> (nextProps.hasOwnProperty(propKey) || !lastProps.hasOwnProperty(propKey) || lastProps[propKey] == <span>null</span>) {
      <span>continue</span>;
    }
    <span>if</span> (registrationNameModules.hasOwnProperty(propKey)) {
      <span>if</span> (lastProps[propKey]) {
        <span>// Only call deleteListener if there was a listener previously or</span>
        <span>// else willDeleteListener gets called when there wasn't actually a</span>
        <span>// listener (e.g., onClick={null})</span>
        deleteListener(<span>this</span>, propKey);
      }
    }
  }
  <span>for</span> (propKey <span>in</span> nextProps) {
    <span>var</span> nextProp = nextProps[propKey];
    <span>var</span> lastProp = propKey === STYLE ? <span>this</span>._previousStyleCopy : lastProps != <span>null</span> ? lastProps[propKey] : <span>undefined</span>;
    <span>if</span> (!nextProps.hasOwnProperty(propKey) || nextProp === lastProp || nextProp == <span>null</span> && lastProp == <span>null</span>) {
      <span>continue</span>;
    }
    <span>if</span> (registrationNameModules.hasOwnProperty(propKey)) { <span>// 处理事件参数。</span>
      <span>if</span> (nextProp) {
        enqueuePutListener(<span>this</span>, propKey, nextProp, transaction); <span>// 注册事件，委托到属于的document上</span>
      } <span>else</span> <span>if</span> (lastProp) {
        deleteListener(<span>this</span>, propKey);
      }
    }
  }
}
<span class="copy-code-btn">复制代码</span></code></pre><p><strong>enqueuePutListener</strong></p>
<ul>
<li>listenTo</li>
<li>putListener</li>
</ul>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>enqueuePutListener</span>(<span>inst, registrationName, listener, transaction</span>) </span>{
  <span>var</span> containerInfo = inst._nativeContainerInfo;
  <span>var</span> doc = containerInfo._ownerDocument; <span>// 大部分的事件都被到对应的document上</span>
  <span>if</span> (!doc) { <span>// ssr</span>
    <span>// Server rendering.</span>
    <span>return</span>;
  }
  listenTo(registrationName, doc);
  transaction.getReactMountReady().enqueue(putListener, {
    <span>inst</span>: inst,
    <span>registrationName</span>: registrationName,
    <span>listener</span>: listener
  });
}
<span class="copy-code-btn">复制代码</span></code></pre><p><strong>listenTo</strong>是将事件委托到document的方法，大部分事件是委托到document上的。但是因为document上能够catch的事件类型的限制(<a target="_blank" href="https://www.w3.org/TR/2000/REC-DOM-Level-2-Events-20001113/events.html#Events-DocumentEvent">Document Object Model Events</a>)，不是所有的事件类型都委托到document，少部分是直接委托到元素本身上的。</p>
<p><strong>putListener</strong>将对应的类型的事件、事件的目标对象和事件触发时执行的方法添加到listenerBank对象中。</p>
<pre><code lang="javascript" class="copyable">listenTo: <span><span>function</span> (<span>registrationName, contentDocumentHandle</span>) </span>{
  <span>var</span> mountAt = contentDocumentHandle;
  <span>var</span> isListening = getListeningForDocument(mountAt);
  <span>var</span> dependencies = EventPluginRegistry.registrationNameDependencies[registrationName];

  <span>var</span> topLevelTypes = EventConstants.topLevelTypes;
  <span>for</span> (<span>var</span> i = <span>0</span>; i < dependencies.length; i++) {
    <span>var</span> dependency = dependencies[i];
    <span>if</span> (!(isListening.hasOwnProperty(dependency) && isListening[dependency])) {
      <span>// 先判断先几个需要特殊处理的事件，主要都是兼容性的原因。</span>
      <span>if</span> (...) {
        ......
      } <span>else</span> <span>if</span> (topEventMapping.hasOwnProperty(dependency)) {
        ReactBrowserEventEmitter.ReactEventListener.trapBubbledEvent(dependency, topEventMapping[dependency], mountAt);
      }
      isListening[dependency] = <span>true</span>;
    }
  }
}

<span>// 冒泡阶段的触发的事件的委托</span>
trapBubbledEvent: <span><span>function</span> (<span>topLevelType, handlerBaseName, handle</span>) </span>{
  <span>return</span> ReactBrowserEventEmitter.ReactEventListener.trapBubbledEvent(topLevelType, handlerBaseName, handle);
},

<span>// 捕获阶段的触发的事件的委托</span>
trapCapturedEvent: <span><span>function</span> (<span>topLevelType, handlerBaseName, handle</span>) </span>{
  <span>return</span> ReactBrowserEventEmitter.ReactEventListener.trapCapturedEvent(topLevelType, handlerBaseName, handle);
},

<span>trapBubbledEvent</span>: <span><span>function</span> (<span>topLevelType, handlerBaseName, handle</span>) </span>{
  <span>return</span> EventListener.listen(element, handlerBaseName, ReactEventListener.dispatchEvent.bind(<span>null</span>, topLevelType));
},

<span>trapCapturedEvent</span>: <span><span>function</span> (<span>topLevelType, handlerBaseName, handle</span>) </span>{
  <span>return</span> EventListener.capture(element, handlerBaseName, ReactEventListener.dispatchEvent.bind(<span>null</span>, topLevelType));
},

<span>listen</span>: <span><span>function</span> <span>listen</span>(<span>target, eventType, callback</span>) </span>{
  <span>if</span> (target.addEventListener) {
    target.addEventListener(eventType, callback, <span>false</span>);
  }
},

<span>capture</span>: <span><span>function</span> <span>capture</span>(<span>target, eventType, callback</span>) </span>{
  <span>if</span> (target.addEventListener) {
    target.addEventListener(eventType, callback, <span>true</span>);
  }
},
<span class="copy-code-btn">复制代码</span></code></pre><p>重点在于所有的委托的事件的回调函数都是ReactEventListener.dispatchEvent。</p>
<pre><code lang="javascript" class="copyable">dispatchEvent: <span><span>function</span> (<span>topLevelType, nativeEvent</span>) </span>{
  <span>// bookKeeping的初始化使用了react在源码中用到的对象池的方法来避免多余的垃圾回收。</span>
  <span>// bookKeeping的作用看ta的定义就知道了，就是一个用来保存过程中会使用到的变量的对象。</span>
  <span>var</span> bookKeeping = TopLevelCallbackBookKeeping.getPooled(topLevelType, nativeEvent);
  <span>try</span> {
    ReactUpdates.batchedUpdates(handleTopLevelImpl, bookKeeping);
  } <span>finally</span> {
    TopLevelCallbackBookKeeping.release(bookKeeping);
  }
}
<span class="copy-code-btn">复制代码</span></code></pre><p>handleTopLevelImpl方法遍历事件触发对象以及其的父级元素（事件传递），对每个元素执行_handleTopLevel方法。</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>handleTopLevelImpl</span>(<span>bookKeeping</span>) </span>{
  <span>var</span> nativeEventTarget = getEventTarget(bookKeeping.nativeEvent);
  <span>var</span> targetInst = ReactDOMComponentTree.getClosestInstanceFromNode(nativeEventTarget);
  <span>var</span> ancestor = targetInst;
  <span>do</span> {
    bookKeeping.ancestors.push(ancestor);
    ancestor = ancestor && findParent(ancestor);
  } <span>while</span> (ancestor);

  <span>for</span> (<span>var</span> i = <span>0</span>; i < bookKeeping.ancestors.length; i++) {
    targetInst = bookKeeping.ancestors[i];
    ReactEventListener._handleTopLevel(bookKeeping.topLevelType, targetInst, bookKeeping.nativeEvent, getEventTarget(bookKeeping.nativeEvent));
  }
}
<span class="copy-code-btn">复制代码</span></code></pre><p>handleTopLevel根据事件对象以及触发的事件类型提取出所有需要被执行的事件以及对应的回调函数，统一由runEventQueueInBatch执行。</p>
<pre><code lang="javascript" class="copyable">handleTopLevel: <span><span>function</span> (<span>topLevelType, targetInst, nativeEvent, nativeEventTarget</span>) </span>{
  <span>var</span> events = EventPluginHub.extractEvents(topLevelType, targetInst, nativeEvent, nativeEventTarget);
  runEventQueueInBatch(events);
}
<span class="copy-code-btn">复制代码</span></code></pre><p>extractEvents方法调用了对应的plugin的extractEvents方法来获取对应的plugin类型的需要执行的事件，然后accumulateInto到一起。</p>
<pre><code lang="javascript" class="copyable">extractEvents: <span><span>function</span> (<span>topLevelType, targetInst, nativeEvent, nativeEventTarget</span>) </span>{
   <span>var</span> events;
   <span>var</span> plugins = EventPluginRegistry.plugins;
   <span>for</span> (<span>var</span> i = <span>0</span>; i < plugins.length; i++) {
     <span>// Not every plugin in the ordering may be loaded at runtime.</span>
     <span>var</span> possiblePlugin = plugins[i];
     <span>if</span> (possiblePlugin) {
       <span>var</span> extractedEvents = possiblePlugin.extractEvents(topLevelType, targetInst, nativeEvent, nativeEventTarget);
       <span>if</span> (extractedEvents) {
         events = accumulateInto(events, extractedEvents);
       }
     }
   }
   <span>return</span> events;
 }
<span class="copy-code-btn">复制代码</span></code></pre><p>plugin的extractEvents方法中的有意思的地方在于 <strong>EventPropagators.accumulateTwoPhaseDispatches(event)</strong> 。</p>
<p>EventPropagators.accumulateTwoPhaseDispatches中模拟了事件传递的过程即：capture -> target -> bubble 的过程，将这个路径上的所有的符合事件类型的回调函数以及对应的元素按照事件传递的顺序返回。</p>
<p align="center">
<img width="400" class="lazyload" src="https://user-gold-cdn.xitu.io/2018/2/26/161cdbf95a3f8121?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1004" data-height="1024" referrerpolicy="no-referrer">
</p>
<p>（图片来自<a target="_blank" href="https://www.w3.org/TR/DOM-Level-3-Events/#event-flow">Event dispatch and DOM event flow</a>）</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>traverseTwoPhase</span>(<span>inst, fn, arg</span>) </span>{
  <span>var</span> path = [];
  <span>while</span> (inst) {
    path.push(inst);
    inst = inst._nativeParent;
  }
  <span>var</span> i;
  <span>for</span> (i = path.length; i-- > <span>0</span>;) {
    fn(path[i], <span>false</span>, arg);
  }
  <span>for</span> (i = <span>0</span>; i < path.length; i++) {
    fn(path[i], <span>true</span>, arg);
  }
}
<span class="copy-code-btn">复制代码</span></code></pre><p>traverseTwoPhase方法模拟了事件传递的过程并且获取对应的回调函数和事件对象保存在react合成的event对象的_dispatchListeners和_dispatchInstances上</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>accumulateDirectionalDispatches</span>(<span>inst, upwards, event</span>) </span>{
  <span>var</span> phase = upwards ? PropagationPhases.bubbled : PropagationPhases.captured;
  <span>var</span> listener = listenerAtPhase(inst, event, phase);
  <span>if</span> (listener) {
    <span>// event._dispatchListeners结果就是这个event在event flow的过程中会触发那些listenter的callback【按照event flow的顺序push到一个数组中了】</span>
    event._dispatchListeners = accumulateInto(event._dispatchListeners, listener);
    event._dispatchInstances = accumulateInto(event._dispatchInstances, inst);
  }
}
<span class="copy-code-btn">复制代码</span></code></pre><p>查询listener和对应的inst使用的是事件的类型以及_rootNodeID，listenerBank中保存了对应一个类型下元素的回调函数：</p>
<p align="center">
<img alt="listenerBank" width="200" class="lazyload" src="https://user-gold-cdn.xitu.io/2018/2/26/161cdbf95a22ace2?imageView2/0/w/1280/h/960/ignore-error/1" data-width="402" data-height="268" referrerpolicy="no-referrer">
</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>listenerAtPhase</span>(<span>inst, event, propagationPhase</span>) </span>{
  <span>var</span> registrationName = event.dispatchConfig.phasedRegistrationNames[propagationPhase];
  <span>return</span> getListener(inst, registrationName);
}

getListener: <span><span>function</span> (<span>inst, registrationName</span>) </span>{
    <span>var</span> bankForRegistrationName = listenerBank[registrationName];
    <span>return</span> bankForRegistrationName && bankForRegistrationName[inst._rootNodeID];
  },
<span class="copy-code-btn">复制代码</span></code></pre><p>对于listenerBank内容的生成由之前说的第二个主要方法putListener完成。</p>
<p><strong>putListener</strong> 使用事务的方式统一在ReactMountReady阶段执行。</p>
<pre><code lang="javascript" class="copyable">putListener: <span><span>function</span> (<span>inst, registrationName, listener</span>) </span>{
  <span>var</span> bankForRegistrationName = listenerBank[registrationName] || (listenerBank[registrationName] = {});
  bankForRegistrationName[inst._rootNodeID] = listener;
}
<span class="copy-code-btn">复制代码</span></code></pre><p>在extractEvents了对应触发的事件类型的events后通过runEventQueueInBatch(events)将所有的合成事件放到事件队列里面，第二步是逐个执行</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>runEventQueueInBatch</span>(<span>events</span>) </span>{
  EventPluginHub.enqueueEvents(events);
  EventPluginHub.processEventQueue(<span>false</span>);
}

<span><span>function</span> <span>executeDispatchesInOrder</span>(<span>event, simulated</span>) </span>{
  <span>var</span> dispatchListeners = event._dispatchListeners;
  <span>var</span> dispatchInstances = event._dispatchInstances;
  <span>if</span> (process.env.NODE_ENV !== <span>'production'</span>) {
    validateEventDispatches(event);
  }
  <span>if</span> (<span>Array</span>.isArray(dispatchListeners)) {
    <span>for</span> (<span>var</span> i = <span>0</span>; i < dispatchListeners.length; i++) {
      <span>if</span> (event.isPropagationStopped()) {
        <span>break</span>;
      }
      <span>// Listeners and Instances are two parallel arrays that are always in sync.</span>
      executeDispatch(event, simulated, dispatchListeners[i], dispatchInstances[i]);
    }
  } <span>else</span> <span>if</span> (dispatchListeners) {
    executeDispatch(event, simulated, dispatchListeners, dispatchInstances);
  }
  event._dispatchListeners = <span>null</span>;
  event._dispatchInstances = <span>null</span>;
}

<span><span>function</span> <span>executeDispatch</span>(<span>event, simulated, listener, inst</span>) </span>{
  <span>var</span> type = event.type || <span>'unknown-event'</span>;
  event.currentTarget = EventPluginUtils.getNodeFromInstance(inst);
  <span>if</span> (simulated) {
    ReactErrorUtils.invokeGuardedCallbackWithCatch(type, listener, event);
  } <span>else</span> {
    ReactErrorUtils.invokeGuardedCallback(type, listener, event);
  }
  event.currentTarget = <span>null</span>;
}

<span><span>function</span> <span>invokeGuardedCallback</span>(<span>name, func, a, b</span>) </span>{
  <span>try</span> {
    <span>return</span> func(a, b);
  } <span>catch</span> (x) {
    <span>if</span> (caughtError === <span>null</span>) {
      caughtError = x;
    }
    <span>return</span> <span>undefined</span>;
  }
}
<span class="copy-code-btn">复制代码</span></code></pre><h3 data-id="heading-2">总结</h3>
<ul>
<li>统一的分发函数dispatchEvent。</li>
<li>React的事件对象是合成对象(SyntheticEvent)。</li>
<li>几乎所有的事件都委托到document，达到性能优化的目的。</li>
<li>合成事件与原生事件混用要注意React的事件基本都是委托到document。</li>
</ul>
<p>参考资料</p>
<ul>
<li><a target="_blank" href="http://zhenhua-lee.github.io/react/react-event.html">React源码解读系列 – 事件机制</a></li>
<li><a target="_blank" href="https://www.w3.org/TR/DOM-Level-3-Events/#ui-events-intro">UI Events</a></li>
<li><a target="_blank" href="https://www.w3.org/TR/2000/REC-DOM-Level-2-Events-20001113/events.html#Events-EventTarget">Document Object Model Events</a></li>
</ul>
</div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            