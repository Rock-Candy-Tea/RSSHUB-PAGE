
---
title: react源码-事件监听
categories: 
    - 编程
    - 掘金 - 收藏集
author: 掘金 - 收藏集
comments: false
date: Mon, 13 May 2019 23:57:10 GMT
thumbnail: https://user-gold-cdn.xitu.io/2019/5/14/16ab505e4e6299f3?imageView2/0/w/1280/h/960/ignore-error/1
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><p>本文以 React v16.5.2 为基础进行源码分析</p>
<p><strong>基本流程</strong></p>
<p>在 react源码的 react-dom/src/events/ReactBrowserEventEmitter.js文件的开头，有这么一大段注释：</p>
<p></p><figure><img class="lazyload" src="https://user-gold-cdn.xitu.io/2019/5/14/16ab505e4e6299f3?imageView2/0/w/1280/h/960/ignore-error/1" data-width="988" data-height="1280" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<p>事件委托是很常用的一种浏览器事件优化策略，于是 React就接管了这件事情，并且还贴心地消除了浏览器间的差异，赋予开发者跨浏览器的开发体验，主要是使用 EventPluginHub这个东西来负责调度事件的存储，合成事件并以对象池的方式实现创建和销毁，至于下面的结构图形，则是对事件机制的一个图形化描述</p>
<ul>
<li>React事件使用了事件委托的机制，一般事件委托的作用都是为了减少页面的注册事件数量，减少内存开销，优化浏览器性能，React这么做也是有这么一个目的，除此之外，也是为了能够更好的管理事件，实际上，React中所有的事件最后都是被委托到了 document这个顶级DOM上</li>
<li>既然所有的事件都被委托到了 document上，那么肯定有一套管理机制，所有的事件都是以一种先进先出的队列方式进行触发与回调</li>
<li>既然都已经接管事件了，那么不对事件做些额外的事情未免有些浪费，于是 React中就存在了自己的 合成事件(SyntheticEvent)，合成事件由对应的 EventPlugin负责合成，不同类型的事件由不同的 plugin合成，例如 SimpleEvent Plugin、TapEvent Plugin等</li>
<li>为了进一步提升事件的性能，使用了 EventPluginHub这个东西来负责合成事件对象的创建和销毁</li>
</ul>
<p>#开始</p>
<pre><code lang="bash" class="copyable"><button onClick={this.autoFocus}>点击聚焦</button>
<span class="copy-code-btn">复制代码</span></code></pre><p>这是我们在React中绑定事件的常规写法。经由JSX解析，button会被当做组件挂载。而onClick这时候也只是一个普通的props。
ReactDOMComponent在进行组件加载(mountComponent)、更新(updateComponent)的时候，需要对props进行处理(_updateDOMProperties):</p>
<h2 data-id="heading-0">事件注册</h2>
<pre><code lang="bash" class="copyable">ReactDOMComponent.Mixin = {
    mountComponent:<span><span>function</span></span>(){},
    _createOpenTagMarkupAndPutListeners:<span><span>function</span></span>(){},
    ....,
    
    // 方法中有指向上次属性值得lastProp,
    // nextProp是当前属性值，这里nextProp是我们绑定给组件的onclick事件处理函数。
  //  nextProp 不为空调用enqueuePutListener绑定事件,为空则注销事件绑定。
     _updateDOMProperties:<span>function</span>(lastProps, nextProps, transaction){
         <span>for</span> (propKey <span>in</span> lastProps) {}   //省略。。。
         <span>for</span> (propKey <span>in</span> nextProps) {
         // 判断是否为事件属性
             <span>if</span> (registrationNameModules.hasOwnProperty(propKey))  {
          enqueuePutListener(this, propKey, nextProp, transaction);
              }
         }
         
     }
}


//这里进行事件绑定

首先判断了 rootContainerElement是不是一个 document或者 Fragment(文档片段节点)

enqueuePutListener 这个方法只在浏览器环境下执行，传给listenTo参数分别是事件名称<span>'onclick'</span>和代理事件的绑
     定dom。如果是fragement 就是根节点（在reactDom.render指定的），不是的话就是document。listenTo
     用于绑定事件到 document ，下面交由事务处理的是回调函数的存储，便于调用。
     ReactBrowserEventEmitter 文件中的 listenTo 看做事件处理的源头。
     这里获取了当前组件（其实这时候就是button）所在的document
     
     
<span>function</span> enqueuePutListener(inst, registrationName, listener, transaction) {
    ...
    var containerInfo = inst._hostContainerInfo;
    var isDocumentFragment = containerInfo._node && containerInfo._node.nodeType === DOC_FRAGMENT_TYPE;
    var doc = isDocumentFragment ? containerInfo._node : containerInfo._ownerDocument;
    
     
     
      listenTo(registrationName, doc);
      
     ...
}
<span class="copy-code-btn">复制代码</span></code></pre><p>绑定的重点是这里的listenTo方法。看源码(ReactBrowerEventEmitter)</p>
<pre><code lang="bash" class="copyable">//registrationName:需要绑定的事件
//当前component所属的document，即事件需要绑定的位置

    listenTo: <span>function</span> (registrationName, contentDocumentHandle) {
    var mountAt = contentDocumentHandle;
       //获取当前document上已经绑定的事件
    var isListening = getListeningForDocument(mountAt);
    // 获取 registrationName（注册事件名称）的topLevelEvent（顶级事件类型）
    var dependencies = EventPluginRegistry.registrationNameDependencies[registrationName];

    <span>for</span> (var i = 0; i < dependencies.length; i++) {
      var dependency = dependencies[i];
      <span>if</span> (!(isListening.hasOwnProperty(dependency) && isListening[dependency])) {
        <span>if</span> (dependency === <span>'topWheel'</span>) {
           ...         
        } <span>else</span> <span>if</span> (dependency === <span>'topScroll'</span>) {
               ...
        } <span>else</span> <span>if</span> (dependency === <span>'topFocus'</span> || dependency === <span>'topBlur'</span>) {
                ...
        } <span>else</span> <span>if</span> (topEventMapping.hasOwnProperty(dependency)) {
        // 获取 topLevelEvent 对应的浏览器原生事件
          //冒泡处理  
          ReactBrowserEventEmitter.ReactEventListener.trapBubbledEvent(dependency, topEventMapping[dependency], mountAt);
        }
        isListening[dependency] = <span>true</span>;
      }
    }
  },

<span class="copy-code-btn">复制代码</span></code></pre><p>对于同一个事件，例如click有两个事件 onClick（在冒泡阶段触发） onClickCapture（在捕获阶段触发）两个事件名，这个冒泡和捕获都是react事件模拟出来的。绑定到 document上面的事件基本上都是在冒泡阶段（对 whell, focus, scroll 有额外处理）,如下图 click 事件绑定执行的如下。</p>
<p>最后处理（EventListener的listen和capture中）</p>
<pre><code lang="bash" class="copyable">//eventType:事件类型,target: document对象，
//callback:是固定的，始终是ReactEventListener的dispatch方法
<span>if</span> (target.addEventListener) {
      target.addEventListener(eventType, callback, <span>false</span>);
      <span>return</span> {
        remove: <span>function</span> <span><span>remove</span></span>() {
          target.removeEventListener(eventType, callback, <span>false</span>);
        }
      };
    }
<span class="copy-code-btn">复制代码</span></code></pre><p>所有事件绑定在document上</p>
<p>所以事件触发的都是ReactEventListener的dispatch方法</p>
<h2 data-id="heading-1">回调储存</h2>
<p>看到这边你可能疑惑，所有回调都执行的ReactEventListener的dispatch方法，那我写的回调干嘛去了。别急，接着看：</p>
<pre><code lang="bash" class="copyable"><span>function</span> enqueuePutListener(inst, registrationName, listener, transaction) {
  ...
  //注意这里！！！！！！！！！
  //这里获取了当前组件（其实这时候就是button）所在的document
  var doc = isDocumentFragment ? containerInfo._node : containerInfo._ownerDocument;
  //事件绑定
  listenTo(registrationName, doc);
 //这段代码表示将putListener放入回调序列，当组件挂载完成是会依次执行序列中的回调。putListener也是在那时候执行的。
 //不明白的可以看看本专栏中前两篇关于transaction和挂载机制的讲解
  transaction.getReactMountReady().enqueue(putListener, {
    inst: inst,
    registrationName: registrationName,
    listener: listener
  });
  //保存回调
  <span>function</span> <span><span>putListener</span></span>() {
    var listenerToPut = this;
    EventPluginHub.putListener(listenerToPut.inst, listenerToPut.registrationName, listenerToPut.listener);
  }
}
<span class="copy-code-btn">复制代码</span></code></pre><p>还是这段代码，事件绑定我们介绍过，主要是listenTo方法。
当绑定完成以后会执行putListener。该方法会在ReactReconcileTransaction事务的close阶段执行，具体由EventPluginHub来进行管理</p>
<pre><code lang="bash" class="copyable">//
var listenerBank = {};
var getDictionaryKey = <span>function</span> (inst) {
//inst为组建的实例化对象
//_rootNodeID为组件的唯一标识
  <span>return</span> <span>'.'</span> + inst._rootNodeID;
}
var EventPluginHub = {
//inst为组建的实例化对象
//registrationName为事件名称
//listner为我们写的回调函数，也就是列子中的this.autoFocus
  putListener: <span>function</span> (inst, registrationName, listener) {
    ...
    var key = getDictionaryKey(inst);
    var bankForRegistrationName = listenerBank[registrationName] || (listenerBank[registrationName] = {});
    bankForRegistrationName[key] = listener;
    ...
  }
}
<span class="copy-code-btn">复制代码</span></code></pre><p>EventPluginHub在每个项目中只实例化一次。也就是说，项目组所有事件的回调都会储存在唯一的listenerBank中。</p>
<p>是不是有点晕，放上流程图，仔细回忆一下</p>
<p></p><figure><img class="lazyload" src="https://user-gold-cdn.xitu.io/2019/5/14/16ab5481db9ffc4c?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="769" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<h2 data-id="heading-2">事件触发</h2>
<p>注册事件时我们说过，所有的事件都是绑定在Document上。回调统一是ReactEventListener的dispatch方法。
由于冒泡机制，无论我们点击哪个DOM，最后都是由document响应（因为其他DOM根本没有事件监听）。也即是说都会触发dispatch</p>
<pre><code lang="bash" class="copyable">dispatchEvent: <span>function</span>(topLevelType, nativeEvent) {
    //实际触发事件的DOM对象
    var nativeEventTarget = getEventTarget(nativeEvent);
    //nativeEventTarget对应的virtual DOM
    var targetInst = ReactDOMComponentTree.getClosestInstanceFromNode(
      nativeEventTarget,
    );
    ...
    //创建bookKeeping实例，为handleTopLevelImpl回调函数传递事件名和原生事件对象
    //其实就是把三个参数封装成一个对象
    var bookKeeping = getTopLevelCallbackBookKeeping(
      topLevelType,
      nativeEvent,
      targetInst,
    );

    try {
    //这里开启一个transactIon，perform中执行了
    //handleTopLevelImpl(bookKeeping)
      ReactGenericBatching.batchedUpdates(handleTopLevelImpl, bookKeeping);
    } finally {
      releaseTopLevelCallbackBookKeeping(bookKeeping);
    }
  },
<span class="copy-code-btn">复制代码</span></code></pre><pre><code lang="bash" class="copyable"><span>function</span> handleTopLevelImpl(bookKeeping) {
//触发事件的真实DOM
  var nativeEventTarget = getEventTarget(bookKeeping.nativeEvent);
  //nativeEventTarget对应的ReactElement
  var targetInst = ReactDOMComponentTree.getClosestInstanceFromNode(nativeEventTarget);
  //bookKeeping.ancestors保存的是组件。
  var ancestor = targetInst;
  <span>do</span> {
    bookKeeping.ancestors.push(ancestor);
    ancestor = ancestor && findParent(ancestor);
  } <span>while</span> (ancestor);

  <span>for</span> (var i = 0; i < bookKeeping.ancestors.length; i++) {
    targetInst = bookKeeping.ancestors[i];
    //具体处理逻辑
    ReactEventListener._handleTopLevel(bookKeeping.topLevelType, targetInst, bookKeeping.nativeEvent, getEventTarget(bookKeeping.nativeEvent));
  }
}
<span class="copy-code-btn">复制代码</span></code></pre><pre><code lang="bash" class="copyable">//这就是核心的处理了
handleTopLevel: <span>function</span> (topLevelType, targetInst, nativeEvent, nativeEventTarget) {
//首先封装event事件
    var events = EventPluginHub.extractEvents(topLevelType, targetInst, nativeEvent, nativeEventTarget);
    //发送包装好的event
    runEventQueueInBatch(events);
  }
<span class="copy-code-btn">复制代码</span></code></pre><h2 data-id="heading-3">事件封装</h2>
<p>首先是EventPluginHub的extractEvents</p>
<pre><code lang="bash" class="copyable">extractEvents: <span>function</span> (topLevelType, targetInst, nativeEvent, nativeEventTarget) {
    var events;
    var plugins = EventPluginRegistry.plugins;
    <span>for</span> (var i = 0; i < plugins.length; i++) {
      // Not every plugin <span>in</span> the ordering may be loaded at runtime.
      var possiblePlugin = plugins[i];
      <span>if</span> (possiblePlugin) {
      //主要看这边
        var extractedEvents = possiblePlugin.extractEvents(topLevelType, targetInst, nativeEvent, nativeEventTarget);
        ......
      }
    }
    <span>return</span> events;
  },
<span class="copy-code-btn">复制代码</span></code></pre><p>接着看SimpleEventPlugin的方法</p>
<pre><code lang="bash" class="copyable">extractEvents: <span>function</span> (topLevelType, targetInst, nativeEvent, nativeEventTarget) {
    ......
    //这里是对事件的封装，但是不是我们关注的重点
    var event = EventConstructor.getPooled(dispatchConfig, targetInst, nativeEvent, nativeEventTarget);
    //重点看这边
    EventPropagators.accumulateTwoPhaseDispatches(event);
    <span>return</span> event;
}
<span class="copy-code-btn">复制代码</span></code></pre><p>接下来是方法中的各种引用，跳啊跳，转啊转，我们来到了ReactDOMTraversal中的traverseTwoPhase方法</p>
<pre><code lang="bash" class="copyable">//inst是触发事件的target的ReactElement
//fn：EventPropagator的accumulateDirectionalDispatches
//arg: 就是之前部分封装好的event（之所以说是部分，是因为现在也是在处理Event，这边处理完才是封装完成）
<span>function</span> traverseTwoPhase(inst, fn, arg) {
  var path = [];
  <span>while</span> (inst) {
   //注意path，这里以ReactElement的形式冒泡着，
   //把触发事件的父节点依次保存下来
    path.push(inst);
    //获取父节点
    inst = inst._hostParent;
  }
  var i;
  //捕捉，依次处理
  <span>for</span> (i = path.length; i-- > 0;) {
    fn(path[i], <span>'captured'</span>, arg);
  }
  //冒泡，依次处理
  <span>for</span> (i = 0; i < path.length; i++) {
    fn(path[i], <span>'bubbled'</span>, arg);
  }
}

<span class="copy-code-btn">复制代码</span></code></pre><pre><code lang="bash" class="copyable">//判断父组件是否保存了这一类事件
<span>function</span> accumulateDirectionalDispatches(inst, phase, event) {
//获取到回调
  var listener = listenerAtPhase(inst, event, phase);
  <span>if</span> (listener) {
  //如果有回调，就把包含该类型事件监听的DOM与对应的回调保存进Event。
  //accumulateInto可以理解成_.assign
  //记住这两个属性，很重要。
    event._dispatchListeners = accumulateInto(event._dispatchListeners, listener);
    event._dispatchInstances = accumulateInto(event._dispatchInstances, inst);
  }
}

<span class="copy-code-btn">复制代码</span></code></pre><p>listenerAtPhase里面执行的是EventPluginHub的getListener函数</p>
<pre><code lang="bash" class="copyable">getListener: <span>function</span> (inst, registrationName) {
    //还记得之前保存回调的listenerBank吧？
    var bankForRegistrationName = listenerBank[registrationName];
    <span>if</span> (shouldPreventMouseEvent(registrationName, inst._currentElement.type, inst._currentElement.props)) {
      <span>return</span> null;
    }
    //获取inst的_rootNodeId
    var key = getDictionaryKey(inst);
    //获取对应的回调
    <span>return</span> bankForRegistrationName && bankForRegistrationName[key];
  },
<span class="copy-code-btn">复制代码</span></code></pre><h2 data-id="heading-4">事件分发</h2>
<p>runEventQueueInBatch主要进行了两步操作</p>
<pre><code lang="bash" class="copyable"><span>function</span> runEventQueueInBatch(events) {
//将event事件加入processEventQueue序列
  EventPluginHub.enqueueEvents(events);
  //前一步保存好的processEventQueue依次执行
//executeDispatchesAndRelease
  EventPluginHub.processEventQueue(<span>false</span>);
}

  processEventQueue: <span>function</span> (simulated) {
    var processingEventQueue = eventQueue;
    eventQueue = null;
    <span>if</span> (simulated) {
      <span>for</span>EachAccumulated(processingEventQueue, executeDispatchesAndReleaseSimulated);
    } <span>else</span> {
    //重点看这里
    //<span>for</span>EachAccumulated可以看成<span>for</span>Each的封装
    //那么这里就是processingEventQueue保存的event依次执行executeDispatchesAndReleaseTopLevel（event）
      <span>for</span>EachAccumulated(processingEventQueue, executeDispatchesAndReleaseTopLevel);
    }
  },
<span class="copy-code-btn">复制代码</span></code></pre><p>executeDispatchesAndReleaseTopLevel（event）又是各种函数包装，最后干活的是</p>
<pre><code lang="bash" class="copyable"><span>function</span> executeDispatchesInOrder(event, simulated) {
  //对应的回调函数数组
  var dispatchListeners = event._dispatchListeners;
  //有eventType属性的ReactElement数组
  var dispatchInstances = event._dispatchInstances;
  
  ......
  
  <span>if</span> (Array.isArray(dispatchListeners)) {
    <span>for</span> (var i = 0; i < dispatchListeners.length; i++) {
      <span>if</span> (event.isPropagationStopped()) {
        <span>break</span>;
      }
      executeDispatch(event, simulated, dispatchListeners[i], dispatchInstances[i]);
    }
  } <span>else</span> <span>if</span> (dispatchListeners) {
    executeDispatch(event, simulated, dispatchListeners, dispatchInstances);
  }
  event._dispatchListeners = null;
  event._dispatchInstances = null;
}
<span class="copy-code-btn">复制代码</span></code></pre><p>OK，这里总算出现了老熟人，在封装nativeEvent时我们保存在event里的两个属性，dispatchListeners与dispatchInstances，在这里起作用。
代码很简单，如果有处理这个事件的回调函数，就一次进行处理。细节我们稍后讨论，先看看这里是怎么处理的吧</p>
<pre><code lang="bash" class="copyable"><span>function</span> executeDispatch(event, simulated, listener, inst) {
//<span>type</span>是事件类型
  var <span>type</span> = event.type || <span>'unknown-event'</span>;
  //这是触发事件的真实DOM，也就是列子中的button
  event.currentTarget = EventPluginUtils.getNodeFromInstance(inst);
  <span>if</span> (simulated) {
    ReactErrorUtils.invokeGuardedCallbackWithCatch(<span>type</span>, listener, event);
  } <span>else</span> {
  //看这里看这里
    ReactErrorUtils.invokeGuardedCallback(<span>type</span>, listener, event);
  }
  event.currentTarget = null;
}

<span class="copy-code-btn">复制代码</span></code></pre><p>终于来到最后了,代码位于ReactErrorUtil中
（为了帮助开发，React通过模拟真正的浏览器事件来获得更好的devtools集成。这段代码在开发模式下运行）</p>
<pre><code lang="bash" class="copyable">    //创造一个临时DOM
    var fakeNode = document.createElement(<span>'react'</span>);
    ReactErrorUtils.invokeGuardedCallback = <span>function</span> (name, func, a) {
    //绑定回调函数的上下文
      var boundFunc = func.bind(null, a);
      //定义事件类型
      var evtType = <span>'react-'</span> + name;
      //绑定事件
      fakeNode.addEventListener(evtType, boundFunc, <span>false</span>);
      //生成原生事件
      var evt = document.createEvent(<span>'Event'</span>);
      //将原生事件处理成我们需要的类型
      evt.initEvent(evtType, <span>false</span>, <span>false</span>);
      //发布事件---这里会执行回调
      fakeNode.dispatchEvent(evt);
      //移出事件监听
      fakeNode.removeEventListener(evtType, boundFunc, <span>false</span>);
    };

<span class="copy-code-btn">复制代码</span></code></pre><h2 data-id="heading-5">流程图</h2>
<p></p><figure><img class="lazyload" src="https://user-gold-cdn.xitu.io/2019/5/14/16ab557e7313cf2e?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1100" data-height="1280" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
</div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            