
---
title: '愿不负努力，所愿皆所求  --shopee入职闲叙'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1148'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 20:03:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=1148'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">写于开头</h3>
<p>经过前段时间的准备，笔者最近已经成功入职shopee。所以最近没有更新内容，之后稳定下来之后会继续进行输出</p>
<h3 data-id="heading-1">写一写入职之后做的事</h3>
<p>入职shopee之后，导师有给到一个entry task，这个任务是实现一个事件机制。实现<code>addEventListener</code>，<code>removeEventListener</code>，<code>dispatchEvent</code>这三个方法。</p>
<p>要求是这个样子的：</p>
<ul>
<li>
<p>兼容 W3C 的事件冒泡和事件捕获模型（addEventListener 的 useCapture 参数）</p>
</li>
<li>
<p>每个事件将会有一个优先级（由开发者设置，最高为 0，数字越大则优先级越低，若未设置则默认为 0），若同一时刻有多个事件需要被执行，则按照优先级从高到低执行；若其中多个事件优先级相同，先被定义的事件先执行</p>
</li>
<li>
<p>在优先级与事件冒泡/捕获模型冲突时，优先保证事件冒泡/捕获的执行顺序</p>
</li>
<li>
<p>需要将你的代码写成一个 TypeScript 模块，引入方式和 API 请参考文档</p>
</li>
<li>
<p>若多次为同一元素绑定同一类型的同一 Listener，该事件在符合条件时只触发一次，事件触发优先级以最终注册的优先级为准。</p>
</li>
</ul>
<p>加分项有个比较有意思的东西：<code>尽可能保证一帧的时间（16ms）中所有事件的执行时间之和不超过 10ms（暂时无需考虑超过 10ms 的单个事件），需要把在这一帧来不及执行的事件放到下一帧执行（依旧需要按照优先级来执行）</code></p>
<h3 data-id="heading-2">我的思路</h3>
<p>W3C的事件模型是先捕获后冒泡</p>
<h4 data-id="heading-3"><strong>对于addEventListener：</strong></h4>
<p>入参为dom节点，监听方法名，回调方法，其他配置可以用...opt接受。</p>
<p><code>实现思路</code>：</p>
<p>将注册的事件同一处理，创建weakmap对象，数据结构如下：</p>
<pre><code class="copyable">&#123;
    Dom:&#123;
        handleName(监听方法名):&#123;
        // 存放处理捕获和冒泡的数组
            bubble:[&#123; // 冒泡数组
                cb:()=>void // 事件触发回调
                range:0 // 此事件优先级
                once:false // 兼容opt的once参数
            &#125;],
            capture:[] // 捕获数组，同上
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法内部还需要对原来的dom节点进行一次监听，用来在用户手动点击触发时的事件。这时候需要将此事件做一个缓存，以便在<code>removeEventListener</code>的时候去取消监听</p>
<h4 data-id="heading-4"><strong>对于removeEventListener：</strong></h4>
<p>入参为dom节点，监听方法名，回调，是否采用捕获模型（可选，默认false）</p>
<p><code>实现思路：</code></p>
<p>首先是健壮性处理，然后对weakmap对象中对应节点的对应事件做删除处理。然后把在<code>addEventListener</code>的时候添加的监听进行remove。</p>
<h4 data-id="heading-5"><strong>对于dispatchEvent：</strong></h4>
<p>这个方法应该算是关键，他的入参是dom节点和监听方法名。</p>
<p><code>实现思路：</code></p>
<ul>
<li>
<p>首先进行健壮性处理，然后递归的将当前节点，父节点的捕获和冒泡数组存入数组。</p>
</li>
<li>
<p>依次对数组中的回调进行调用。</p>
</li>
<li>
<p>10ms的实现，使用的api是requestAnimationFrame，rAF传入一个回调，回调中可以拿到一个time参数，time参数指示当前被 requestAnimationFrame() 排序的回调函数被触发的时间。在同一个帧中的多个回调函数，它们每一个都会接受到一个相同的时间戳，即使在计算上一个回调函数的工作负载期间已经消耗了一些时间。该时间戳是一个十进制数，单位毫秒，最小精度为1ms(1000μs)  （--来自MDN)。 再将performance.now()运行得到的时间戳和当前的rAF回调接受到的time进行对比，如果在10ms内可以继续从数组中取事件进行调用。反之，则放入下一帧</p>
</li>
<li>
<p>once 的实现，如果有once参数，就对当前的对象引用置为空对象</p>
</li>
</ul>
<p>这里可以提供一下我的思路，大家也可以自己尝试写一下。</p>
<pre><code class="copyable">// 递归的去将当前节点和父节点存入数组
function recurrenceFindNodeList(
  caps: callbackType[],
  bubs: callbackType[],
  node: nodeType,
  handleName: string
) &#123;
  const parent: any = node.parentNode;
  if (eventMap.has(parent)) &#123;
    const parentObj = eventMap.get(parent)[handleName];
    caps = [...parentObj.capture, ...caps];
    bubs = [...bubs, ...parentObj.bubble];
    recurrenceFindNodeList(caps, bubs, parent, handleName);
  &#125;
  return [...caps, ...bubs];
&#125;

// 对于10ms 的实现

requestAnimationFrame(handler);
function handler(time: number) &#123;
    let taskFinishTime: number = window.performance.now();
    while (taskFinishTime - time < 10) &#123;
      const nextTask = tasklist.shift();
      if (nextTask?.cb) &#123;
        nextTask.cb();
      &#125;
      taskFinishTime = window.performance.now();
    &#125;
    if (tasklist.length > 0) &#123;
      requestAnimationFrame(handler);
    &#125;
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">写于最后</h3>
<p>shopee是一个非常年轻化的公司，在这里从技术角度说，可以学习到很多新技术，并参加他们的项目从0到1的过程，相信在这里的进步会很大。如果大家想了解虾皮欢迎加我微信：zhi794855679 。</p>
<p>愿不负努力，所愿皆所求。</p></div>  
</div>
            