
---
title: 'Fiber架构'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/748c8b2727144a92852ffceb64665208~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 04:49:35 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/748c8b2727144a92852ffceb64665208~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一 Fiber之前的React</h2>
<p>下面代码实现了一个简单的react手写</p>
<pre><code class="copyable">let element = (
  <div id = "A1">
    <div id = "B1">
      <div id="C1"></div>
      <div id="C2"></div>
    </div>
    <div id="B2"></div>
  </div>
)

console.log(JSON.stringify(element, null, 2))
// 如果节点多，层级特别深
// 因为js是单线程，而且ui渲染和js执行是互斥的

function render(element, parentDom) &#123;
  // 创建DOM元素
  let dom = document.createElement(element.type);
  // 处理属性
  Object.keys(element.props)
  .filter(key => key !== 'children')
  .forEach(key => &#123;
    dom[key] = element.props[key];
  &#125;);
  if(Array.isArray(element.props.children)) &#123;
    // 把每个子虚拟DOM变成真实DOM插入到DOM节点里
    element.props.children.forEach(child => render(child, dom));
  &#125;
  parentDom.appendChild(dom);
&#125;

render(
  element,
  document.getElementById('root')
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印出的element如下：</p>
<pre><code class="copyable">&#123;
  "type": "div",
  "key": null,
  "ref": null,
  "props": &#123;
    "id": "A1",
    "children": [
      &#123;
        "type": "div",
        "key": null,
        "ref": null,
        "props": &#123;
          "id": "B1",
          "children": [
            &#123;
              "type": "div",
              "key": null,
              "ref": null,
              "props": &#123;
                "id": "C1"
              &#125;,
              "_owner": null,
              "_store": &#123;&#125;
            &#125;,
            &#123;
              "type": "div",
              "key": null,
              "ref": null,
              "props": &#123;
                "id": "C2"
              &#125;,
              "_owner": null,
              "_store": &#123;&#125;
            &#125;
          ]
        &#125;,
        "_owner": null,
        "_store": &#123;&#125;
      &#125;,
      &#123;
        "type": "div",
        "key": null,
        "ref": null,
        "props": &#123;
          "id": "B2"
        &#125;,
        "_owner": null,
        "_store": &#123;&#125;
      &#125;
    ]
  &#125;,
  "_owner": null,
  "_store": &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/748c8b2727144a92852ffceb64665208~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>jsx标签化是嵌套的结构，如代码所示，最终会编译成递归执行的代码，要想中断递归是很困难的。即react16之前的调度器为栈调度器，栈浅显易懂，代码量少，但不能随意break掉，continue掉，要维护一系列的栈上下文；</p>
<h2 data-id="heading-1">二 帧</h2>
<ul>
<li>目前大多数设备的屏幕刷新频率为60次/秒</li>
<li>当每秒绘制的帧数(FPS)达到60时，页面是流畅的，小于这个值时，用户会感觉到卡顿；</li>
<li>每个帧的预算时间是16.66毫秒(1秒/60)</li>
<li>每个帧的开头包括样式计算，布局和绘制</li>
<li>JavaScript执行JavaScript引擎和页面渲染引擎在同一个渲染线程，GUI渲染和JavaScript执行两者是互斥的</li>
<li>如果某个任务执行时间过长，浏览器就会推迟渲染；</li>
</ul>
<h2 data-id="heading-2">三 什么是Fiber</h2>
<p>我们可以通过某些调度策略合理分配CPU资源，从而提高用户的响应速度</p>
<p>通过Fiber架构，让自己的协调过程变成可被中断，适时地让出CPU执行权，可以让浏览器即使地响应用户的交互；</p>
<p>fiber:就是一个数据结构，它有很多属性，虚拟dom是对真实dom的一种简化；一些真实的dom都做不到的事情，那虚拟dom更做不到，于是就有了fiber，有很多属性，希望借由fiber上的这堆属性来做一些比较厉害的事情；</p>
<p><strong>fiber架构</strong></p>
<p>为了弥补一些不足，就设计了一些新的算法，而为了能让这些算法跑起来，所以出现了fiber这种数据结构； fiber数据结构+算法 = fiber架构；</p>
<p>react应用从始至终管理着基本的三样东西：</p>
<ol>
<li>
<p>Root(整个应用的根儿，一个对象，不是fiber，有个属性指向current树，同时也有个属性指向workInProgress树)</p>
</li>
<li>
<p>current树(树上的每一个节点都是fiber，保存的是上一次的状态 并且每个fiber节点，都对应着一个jsx节点)</p>
</li>
<li>
<p>workInProgress树(树上的每一个节点都是fiber，保存的是本次新的状态，并且每个fiber节点都对应一个jsx节点)</p>
</li>
</ol>
<p>初次渲染的时候，没有current树 react在一开始创建Root，就会同时创建一个unintialFiber的东西(未初始化的fiber) 让react的current指向了uninitialFiber 之后再去创建一个本次要用到的workInProgress</p>
<p><strong>react 中主要分两个阶段</strong></p>
<p><strong>render阶段(指的是创建fiber的过程)</strong></p>
<ol>
<li>
<p>为每个节点创建新的fiber(workInProgress)(可能是复用) 生成一颗有新状态的workInProgress树</p>
</li>
<li>
<p>初次渲染的时候(或新创建了某个节点的时候) 会将这个fiber创建真实的dom实例 并且对当前节点的子节点进行插入appendChildren，</p>
</li>
<li>
<p>如果不是初次渲染的话，就对比新旧的fiber的状态，将产生了更新的fiber节点，最终通过链表的形式，挂载到RootFiber</p>
</li>
</ol>
<p><strong>commit阶段****才是真正的要操作页面的阶段</strong></p>
<ol>
<li>
<p>执行生命周期</p>
</li>
<li>
<p>会从RootFiber上获取到那条链表，根据链表上的标识来操作页面；</p>
</li>
</ol>
<h3 data-id="heading-3">3.1 Fiber是一个执行单元</h3>
<p>Fiber是一个执行单元，每次执行完一个执行单元，React就会检查还剩下多少时间，如果没有时间就把控制权让出去</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6570c100bf654e48a95fa1c2a511fec7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">3.2 Fiber是一种数据结构</h3>
<p>react目前的做法是使用链表，每个虚拟节点内部表示为一个Fiber；</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e6221835eb74a508dabc88b5eb0cde5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>代码如下所示：</p>
<pre><code class="copyable">class FiberNode &#123;
  constructor(tag, key, pendingProps) &#123;
    this.tag = tag; // 表示当前fiber的类型
    this.key = key;
    this.type = null // 'div' || 'h1' || Ding
    this.stateNode = null; // 表示当前fiber的实例
    this.child = null; // 表示当前fiber的子节点 每一个fiber有且只有一个指向它的firstChild
    this.sibling = null; // 表示当前节点的兄弟节点 每个fiber有且只有一个属性指向隔壁的兄弟节点
    this.return = null; // 表示当前fiber的父节点
    this.index = 0;
    this.memoizedState = null; // 表示当前fiber的state
    this.memoizedProps = null; // 表示当前fiber的props
    this.pendingProps = pendingProps; // 表示新进来的props
    this.effecTag = null; // 表示当前节点要进行何种更新
    this.firstEffect = null; // 表示当前节点的有更新的第一个子节点
    this.lastEffect = null; // 表示当前节点的有更新的最后一个子节点
    this.nextEffect = null; // 表示下一个要更新的子节点

    this.alternate = null; // 用来连接current和workInProgress的
    this.updateQueue = null; // 一条链表上面挂载的是当前fiber的新状态

    // 其实还有很多其他的属性
    // expirationTime: 0
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">四 rAF</h2>
<p>requestAnimationFrame回调函数会在绘制之前执行</p>
<ul>
<li>
<p>requestAnimationFrame(callback)会在浏览器每次重绘前执行callback回调，每次callback执行的时机都是浏览器刷新下一帧渲染周期的起点上</p>
</li>
<li>
<p>requestAnimationFrame(callback)的回调callback回调参数timestamp是回调被调用的时间，也就是当前帧的起始时间</p>
</li>
<li>
<p>rAfTime performance.timing.navigationStart + performance.now()约等于Date.now();</p>
</li>
</ul>
<p>下面代码实现了一个绘制进度条的功能；</p>
<pre><code class="copyable"><script>
    let div = document.querySelector('div');
    let button = document.querySelector('button');
    let startTime;
    function progress() &#123;
      div.style.width = div.offsetWidth + 1 +'px';
      div.innerHTML = div.offsetWidth + '%';
      if(div.offsetWidth < 100) &#123;
        console.log(Date.now() - startTime + 'ms');
        startTime = Date.now();
        requestAnimationFrame(progress);
      &#125;
    &#125;
    button.onclick = function() &#123;
      div.style.width = 0;
      startTime = Date.now();
      // 浏览器会在每一帧渲染前执行progress
      requestAnimationFrame(progress);
    &#125;
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">五 requestIdleCallbac</h2>
<ul>
<li>
<p>我们希望快速响应用户，让用户觉得够快，不能阻塞用户的交互</p>
</li>
<li>
<p>requestIdleCallback使开发者能够在主事件循环上执行后台和低优先级工作，而不会影响延迟关键事件，如动画和输入响应</p>
</li>
<li>
<p>正常帧任务完成后没超过16ms，说明时间有富余，此时就会执行requestIdleCallback里注册的任务</p>
</li>
<li>
<p>requestAnimationFrame的回调会在每一帧确定执行，属于高优先级任务，而requestIdleCallback的回调则不一定，属于低优先级任务；</p>
</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09d5b59e16a141e18292517ad9a19590~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"><script type="text/javascript">
    function sleep(duration) &#123;
      let start = Date.now();
      while(start + duration > Date.now()) &#123;&#125;
    &#125;
    function progress() &#123;
      console.log('progress');
      requestAnimationFrame(progress);
    &#125;
    // requestAnimationFrame(progress);
    let channel = new MessageChannel();
    let activeFrameTime = 1000/60; // 16.6
    let frameDeadline; // 这一帧的截止时间
    let pendingCallback;
    let timeRemaining = () => frameDeadline - performance.now();
    channel.port2.onmessage = function() &#123;
      let currentTime = performance.now();
      // 如果帧的截止时间已经小于当前时间，说明已经过期了
      let didTimeout = frameDeadline <= currentTime;
      if(didTimeout || timeRemaining() > 0) &#123;
        if(pendingCallback) &#123;
          pendingCallback(&#123;didTimeout, timeRemaining&#125;);
        &#125;
      &#125;
    &#125;
    window.requestIdleCallback = (callback, options) => &#123;
      requestAnimationFrame((rafTime) => &#123;
        console.log('rafTime', rafTime);
        // 每一帧开始的时间加上16.6 就是一帧的截止时间了
        frameDeadline = rafTime + activeFrameTime;
        pendingCallback = callback;
        // 其实发消息只会，相当于添加一个宏任务
        channel.port1.postMessage('hello');
      &#125;);
    &#125;
    const works = [
      () => &#123;
        console.log('A1开始');
        sleep(20);
        console.log('A1结束');
      &#125;,
      () => &#123;
        console.log('B1开始');
        sleep(20);
        console.log('B1结束');
      &#125;,
      () => &#123;
        console.log('C1开始');
        sleep(20);
        console.log('C1结束');
      &#125;,
      () => &#123;
        console.log('C2开始');
        sleep(20);
        console.log('C2结束');
      &#125;,
      () => &#123;
        console.log('B2开始');
        sleep(20);
        console.log('B2结束');
      &#125;,
    ]
    // 告诉浏览器 你可以在空闲的时间执行任务，但是如果已经过期了 不管你有没有空 都要帮我执行
    requestIdleCallback(workLoop, &#123;timeout: 1000&#125;);
    // 循环执行工具
    function workLoop(deadline) &#123;
      console.log('本帧的剩余时间', parseInt(deadline.timeRemaining()));
      // 如果说还有剩余时间 并且还有没有完成的任务
      while((deadline.timeRemaining() > 0 || deadline.didTimeout) && works.length > 0)&#123;
        performUnitWork();
      &#125;
      if(works.length > 0) &#123;
        console.log(`只剩下$&#123;deadline.timeRemaining()&#125;, 时间片已经到期，等待下次调试`);
        requestIdleCallback(workLoop);
      &#125;
    &#125;
    function performUnitWork() &#123;
      let work = works.shift();
      work();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">六 MessageChannel</h2>
<ol>
<li>
<p>目前requestIdleCallback只要Chrome支持</p>
</li>
<li>
<p>所以目前React利用MessageChannel模拟了requestIdleCallback，将回调延迟到绘制操作只后执行</p>
</li>
<li>
<p>MessageChannel API允许我们创建一个新的消息通道，并通过它的两个MessagePort 属性发送数据；</p>
</li>
<li>
<p>MessageChannel创建了一个通信的管道，这个管道有两个端口，每个端口都可以通过postMessage发送数据，而一个端口只要绑定了，就能收到另一个端口传过来的数据</p>
</li>
<li>
<p>MessageChannel是一个宏任务；</p>

</li>
</ol>
<h2 data-id="heading-8">七 Fiber执行阶段</h2>
<p>每次渲染有两个阶段：Reconciliation(协调render阶段)和Commit(提交阶段)</p>
<ul>
<li>协调阶段：可以认为是diff阶段，这个阶段可以被中断，这个阶段会找出所有节点变更，例如节点新增，删除，属性变更等等，这些变更React称之为副作用；</li>
<li>提交阶段：将上一个阶段计算出来的需要处理的副作用(Effetcs)一次性执行了。这个阶段必须同步执行，不能被打断；</li>
</ul>
<h3 data-id="heading-9">7.1 render阶段</h3>
<ol>
<li>从顶点开始遍历</li>
<li>如果有第一个儿子，先遍历第一个儿子</li>
<li>如果没有第一个儿子，标志着此节点遍历完成</li>
<li>如果有弟弟遍历弟弟</li>
<li>如果没有下一个弟弟，返回父节点标志完成父节点遍历，如果有叔叔遍历叔叔</li>
<li>没有父节点遍历结束</li>
</ol>
<p>先儿子，后弟弟，再叔叔，辈分越小越优先</p>
<p>什么时候一个节点遍历完成，没有子节点，或者所有子节点都遍历完成了，没爹了就表示全部遍历完成了；</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ba22800f78546f7b672f90f832e346b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">7.2 commit阶段</h3>
<p>下面代码实现了一个简易的Fiber架构，只有初次render过程；</p>
<pre><code class="copyable">import element from './element.js';
let container = document.getElementById('root');
const PLACEMENT = 'PLACEMENT';

// 下一个工作单元
// fiber其实也是一个普通的JS对象
let workInProgressRoot = &#123;
  stateNode: container, // 此fiber对应的dom节点
  props: &#123;children: [element]&#125; // fiber的属性
&#125;

let nextUnitOfWork = workInProgressRoot;

function workLoop(deadline) &#123;
  // 如果有当前的工作单元，就执行它，并返回一个工作单元
  while(nextUnitOfWork && deadline.timeRemaining() > 0) &#123;
    nextUnitOfWork = performUnitOfWork(nextUnitOfWork);
  &#125;
  if(!nextUnitOfWork) &#123;
    commitRoot();
  &#125;
&#125;

function commitRoot() &#123;
  let currentFiber = workInProgressRoot.firstEffect;
  while(currentFiber) &#123;
    console.log('commitRoot', currentFiber.props.id);
    if(currentFiber.effectTag === 'PLACEMENT') &#123;
      currentFiber.return.stateNode.appendChild(currentFiber.stateNode);
    &#125;
    currentFiber = currentFiber.nextEffect;
  &#125;
  workInProgressRoot = null;
&#125;

function performUnitOfWork(workingProgressFiber) &#123;
  // 1 创建真实的dom, 并没有挂载 2，创建fiber子树
  beginWork(workingProgressFiber);
  if(workingProgressFiber.child) &#123;
    return workingProgressFiber.child; // 如果有儿子，返回儿子
  &#125;
  while(workingProgressFiber) &#123;
    // 如果没有儿子当前节点其实就结束完成了
    completeUnitOfWork(workingProgressFiber);
    if(workingProgressFiber.sibling) &#123; // 如果有弟弟，返回弟弟
      return workingProgressFiber.sibling;
    &#125;
    workingProgressFiber = workingProgressFiber.return; // 先指向父亲
  &#125;
&#125;

function beginWork(workingProgressFiber) &#123;
  console.log('beginWork', workingProgressFiber.props.id);
  if(!workingProgressFiber.stateNode) &#123;
    workingProgressFiber.stateNode = document.createElement(workingProgressFiber.type);
    for (let key in workingProgressFiber.props) &#123;
      if(key !== 'children') &#123;
        workingProgressFiber.stateNode[key] = workingProgressFiber.props[key];
      &#125;
    &#125;
  &#125;
  // 在beginwork里是不会挂载的
  let previousFiber;
  if(Array.isArray(workingProgressFiber.props.children)) &#123;
    workingProgressFiber.props.children.forEach((child, index) => &#123;
      let childFiber = &#123;
        type: child.type,
        props: child.props,
        return: workingProgressFiber,
        effectTag: 'PLACEMENT', // 这个fiber对应的dom节点需要被插入到页面中
      &#125;
      if(index === 0) &#123;
        workingProgressFiber.child = childFiber;
      &#125; else &#123;
        previousFiber.sibling = childFiber;
      &#125;
      previousFiber = childFiber;
    &#125;);
  &#125;

&#125;

function completeUnitOfWork(workingProgressFiber) &#123;
  console.log('completeUnitOfWork', workingProgressFiber.props.id);
  // 构建副作用链effectList 只有那些有副作用的节点
  let returnFiber = workingProgressFiber.return;
  if(returnFiber) &#123;
    // 把当前fiber的有副作用子链表挂到父亲身上
    if(!returnFiber.firstEffect) &#123;
      returnFiber.firstEffect = workingProgressFiber.firstEffect;
    &#125;
    if(workingProgressFiber.lastEffect) &#123;
      if(returnFiber.lastEffect) &#123;
        returnFiber.lastEffect.nextEffect = workingProgressFiber.firstEffect;
      &#125;
      returnFiber.lastEffect = workingProgressFiber.lastEffect;
    &#125;
    // 再把自己挂到后面
    if(workingProgressFiber.effectTag) &#123;
      if(returnFiber.lastEffect) &#123;
        returnFiber.lastEffect.nextEffect = workingProgressFiber;
      &#125; else &#123;
        returnFiber.firstEffect = workingProgressFiber;
      &#125;
      returnFiber.lastEffect = workingProgressFiber;
    &#125;
  &#125;
&#125;

// 告诉浏览器在空闲的时间执行workLoop
requestIdleCallback(workLoop);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码可以实现第一章的dom结构；</p>
<h2 data-id="heading-11">八 fiber架构本质</h2>
<p>循环条件：利用requestIdleCallback空闲时间递减</p>
<p>遍历过程：利用链表，找孩子找兄弟找父亲；</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            