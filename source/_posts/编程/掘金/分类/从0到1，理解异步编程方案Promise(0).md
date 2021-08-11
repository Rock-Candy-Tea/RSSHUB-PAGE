
---
title: '从0到1，理解异步编程方案Promise(0)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/925048c37ac3416fadcb50bf3e60f239~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 00:12:26 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/925048c37ac3416fadcb50bf3e60f239~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<ol>
<li>理解什么是观察者模式</li>
<li>理解什么是发布订阅模式</li>
<li>理解什么是<code>queueMicrotask()</code></li>
</ol>
</blockquote>
<p>本篇是<code>Promise</code>的基本前置知识，让手写一个<code>Promise</code>变的不在困难！！！，这是构建<code>Promise</code>的0</p>
<h2 data-id="heading-0">1. 观察者模式</h2>
<h3 data-id="heading-1">1.1 基本理解</h3>
<p>如图【观察者模式简图】：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/925048c37ac3416fadcb50bf3e60f239~tplv-k3u1fbpfcp-watermark.image" alt="观察者模式简图.png" loading="lazy" referrerpolicy="no-referrer">
观察者模式讲述的是一对多的关系，简单的来说就是一个对象的状态改变，触发不同观察者动作回应，在《图解设计模式》一书当中，观察者模式就是做状态管理的一种</p>
<p>按图，我们开始实现一个观察者模式</p>
<h3 data-id="heading-2">1.2 实现一个简单的观察者模式示例</h3>
<ol>
<li>创建一个<code>Observer</code>的类</li>
<li>创建一个被观察的类</li>
<li>被观察的类需要添加一个方法<code>addObserver</code>，来收集实例化的<code>Observer</code></li>
<li>状态改变，通知实例化的<code>Observer</code></li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建一个Observer的类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name,action = ()=>&#123;&#125;</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
<span class="hljs-built_in">this</span>.action = action
&#125;
<span class="hljs-function"><span class="hljs-title">runAction</span>(<span class="hljs-params">state</span>)</span>&#123;
<span class="hljs-built_in">this</span>.action(state,<span class="hljs-built_in">this</span>.name)
&#125;
&#125;
<span class="hljs-comment">// 创建一个被观察的类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subject</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name,state</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
<span class="hljs-built_in">this</span>.nowState = state;

<span class="hljs-built_in">this</span>.oldState = <span class="hljs-literal">null</span>;
<span class="hljs-built_in">this</span>.obseverList = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
&#125;
<span class="hljs-comment">// 被观察的类需要添加一个方法addObserver，来收集实例化的Observer</span>
<span class="hljs-function"><span class="hljs-title">addObserve</span>(<span class="hljs-params">obsever</span>)</span>&#123;
<span class="hljs-built_in">this</span>.obseverList.add(obsever)
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
&#125;
<span class="hljs-comment">// 状态改变，通知实例化的Observer</span>
<span class="hljs-function"><span class="hljs-title">notifyObserve</span>(<span class="hljs-params">state</span>)</span>&#123;
<span class="hljs-built_in">this</span>.nowState = state;
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.oldState!==<span class="hljs-built_in">this</span>.nowState)&#123;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.obseverList)&#123;
item.runAction(<span class="hljs-built_in">this</span>.nowState)
&#125;
<span class="hljs-built_in">this</span>.oldState = <span class="hljs-built_in">this</span>.nowState
&#125;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
&#125;
&#125;
<span class="hljs-keyword">const</span> teacherA = <span class="hljs-keyword">new</span> Observer(<span class="hljs-string">'老师A'</span>,<span class="hljs-function">(<span class="hljs-params">state,name</span>)=></span>&#123;
<span class="hljs-keyword">if</span>(state === <span class="hljs-string">'playing'</span>)&#123;
<span class="hljs-built_in">console</span>.log( name+<span class="hljs-string">'发现你在玩，打电话找你家长'</span> )
&#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>( state === <span class="hljs-string">'studying'</span>)&#123;
<span class="hljs-built_in">console</span>.log( name+<span class="hljs-string">'狠狠的表扬了你'</span> )
&#125;
&#125;)

<span class="hljs-keyword">const</span> teacherB = <span class="hljs-keyword">new</span> Observer(<span class="hljs-string">'老师B'</span>, <span class="hljs-function">(<span class="hljs-params">state,name</span>)=></span>&#123;
<span class="hljs-keyword">if</span>(state === <span class="hljs-string">'playing'</span>)&#123;
<span class="hljs-built_in">console</span>.log( name+<span class="hljs-string">'发现你在玩，罚站30分钟'</span> )
&#125;
&#125;)

<span class="hljs-keyword">const</span> deskmateA = <span class="hljs-keyword">new</span> Observer(<span class="hljs-string">'小明'</span>,<span class="hljs-function">(<span class="hljs-params">state,name</span>)=></span>&#123;
<span class="hljs-keyword">if</span>(state === <span class="hljs-string">'eating'</span>)&#123;
<span class="hljs-built_in">console</span>.log( name+<span class="hljs-string">'发现你在吃东西，因此他也开始吃'</span> )
&#125;
&#125;)

<span class="hljs-keyword">const</span> deskmateB = <span class="hljs-keyword">new</span> Observer(<span class="hljs-string">'小f'</span>,<span class="hljs-function">(<span class="hljs-params">state,name</span>)=></span>&#123;
<span class="hljs-keyword">if</span>(state === <span class="hljs-string">'eating'</span>)&#123;
<span class="hljs-built_in">console</span>.log( name+<span class="hljs-string">'发现你在吃东西，因此他也开始吃'</span> )
&#125;
&#125;)
<span class="hljs-keyword">const</span> You = <span class="hljs-keyword">new</span> Subject(<span class="hljs-string">'你'</span>,<span class="hljs-string">'studying'</span>)
You.addObserve(deskmateA).addObserve(teacherA).addObserve(teacherB)
You.notifyObserve(<span class="hljs-string">'playing'</span>)
You.notifyObserve(<span class="hljs-string">'eating'</span>)
You.notifyObserve(<span class="hljs-string">'studying'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面就是一个非常简单的观察者模式的实现。</p>
<p>从中可以清楚的看到，<code>Subject</code>和各个<code>Observer</code>是松耦合关系。当<code>state</code>改变的时候，统一调取各个实例化<code>Observer</code>的<code>runAction</code>去根据状态执行相应的逻辑就好了。</p>
<h2 data-id="heading-3">2 发布订阅模式</h2>
<h3 data-id="heading-4">2.1 基本理解</h3>
<p>发布订阅模式和观察者模式，大体上很像(比如尤大大就认为发布订阅模式和观察者模式就是一样的)。这里就不讨论大佬的思想，毕竟我们都还不到掌控代码的程度。不过可以用观察者模式去类比发布订阅模式(发布订阅模式里的<code>Publisher</code>，就是观察者模式里的<code>Subject</code>,而<code>Subscriber</code>，就是<code>Observer</code>),只不过在发布订阅模式里面多了一个第三方<code>Observer</code>来转发,而不是<code>Subscriber</code>直接<code>notify</code>状态给<code>Publisher</code></p>
<p>在前端中，其实浏览器监听事件就是一个典型的发布订阅模式。例如，<code>document.addEventListener('click',()=>&#123;&#125;)</code>, <code>document</code>就是被监听也就是<code>Publisher</code>,'click'代表发布内容<code>Subject</code>,后面的函数的意思就是，订阅到这个事件是<code>click</code>那就执行这个函数。顺着这个来，就能出图了</p>
<p>如图【发布订阅模式】：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10186c15b79a45d58d7517d22aca7c28~tplv-k3u1fbpfcp-watermark.image" alt="发布订阅模式.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">2.2 实现一个简单的发布订阅模式示例</h3>
<ol>
<li>创建一个第三方观察者<code>Observer</code>类</li>
<li>给第三方的观察者一个<code>addEventListener</code>来添加订阅某消息和订阅该消息的<code>Subscriber</code>行为，只是这里要注意的是，同一个消息不止一个<code>Subscriber</code>的行为可以定，继续添加<code>Subscriber</code>的行为</li>
<li>给第三方的观察者一个<code>removeEventListener</code>可以订阅解除，解除分两种一种是解除单个<code>Subscriber</code>对某个消息的订阅，和直接解除对某个消息的订阅</li>
<li>给第三方的观察者一个<code>notify</code>方法接受到<code>Publisher</code>的状态，触发<code>Subscriber</code>行为</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observe</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.publisherMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
&#125;
<span class="hljs-comment">/* 
* @param &#123; String &#125; type 订阅消息的类型
* @param &#123; Function &#125; actionfn 相应的Subscriber的动作,也是推送消息的目标的动作(Subscriber)
**/</span>
<span class="hljs-function"><span class="hljs-title">addEventListener</span>(<span class="hljs-params">type,actionfn</span>)</span>&#123;
<span class="hljs-keyword">if</span>( !actionfn )&#123;
<span class="hljs-built_in">console</span>.error(<span class="hljs-string">'绑定失败'</span>)
&#125;
<span class="hljs-keyword">let</span> actionfnList = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.publisherMap.has(type))&#123;
actionfnList = <span class="hljs-built_in">this</span>.publisherMap.get(type)
&#125;
actionfnList.add(actionfn)
<span class="hljs-built_in">this</span>.publisherMap.set(type,actionfnList)
&#125;
<span class="hljs-comment">// 取消订阅 Publisher</span>
<span class="hljs-function"><span class="hljs-title">removeEventListener</span>(<span class="hljs-params">type,actionfn</span>)</span>&#123;
<span class="hljs-keyword">if</span>( <span class="hljs-built_in">this</span>.publisherMap.has(type) && actionfn)&#123;
<span class="hljs-keyword">const</span> actionfnList = <span class="hljs-built_in">this</span>.publisherMap.get(type)
<span class="hljs-keyword">if</span>(actionfnList.size)&#123;
actionfnList.delete(actionfn)
&#125;<span class="hljs-keyword">else</span>&#123;
<span class="hljs-built_in">this</span>.publisherMap.delete(type)
&#125;
&#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>( <span class="hljs-built_in">this</span>.publisherMap.has(type) && !actionfn)&#123;
<span class="hljs-built_in">this</span>.publisherMap.delete(type)
&#125;<span class="hljs-keyword">else</span>&#123;
<span class="hljs-built_in">console</span>.error(<span class="hljs-string">'暂无这个消息队列'</span>)
&#125;
&#125;
<span class="hljs-comment">// 触发 Subscriber 的动作,也叫发布通知消息</span>
<span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params">type</span>)</span>&#123;
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.publisherMap.has(type))&#123;
<span class="hljs-keyword">const</span> actionfnList = <span class="hljs-built_in">this</span>.publisherMap.get(type)
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> subscriberAction <span class="hljs-keyword">of</span> actionfnList)&#123;
subscriberAction(<span class="hljs-built_in">this</span>);
&#125;
&#125;
&#125;
&#125;
<span class="hljs-comment">// 老师任命班长来监听你的状态</span>
<span class="hljs-keyword">const</span> monitor = <span class="hljs-keyword">new</span> Observe()
<span class="hljs-keyword">const</span> yourState = [<span class="hljs-string">'studying'</span>,<span class="hljs-string">'eating'</span>]
<span class="hljs-keyword">const</span> teacherAction = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'要很很的表扬你'</span>)
&#125;
<span class="hljs-keyword">const</span> deskmeatAction = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'一起吃东西'</span>,e)
&#125;
monitor.addEventListener(yourState[<span class="hljs-number">0</span>],teacherAction)
monitor.addEventListener(yourState[<span class="hljs-number">0</span>],<span class="hljs-function">()=></span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'给你一朵大大的红花'</span>)
&#125;)
monitor.addEventListener(yourState[<span class="hljs-number">1</span>],deskmeatAction)
monitor.notify(yourState[<span class="hljs-number">0</span>])
monitor.notify(yourState[<span class="hljs-number">1</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从中可以发现，发布订阅模式里，<code>发布者</code>和<code>订阅者</code>，不是松耦合，而是完全解耦的。他们之间的联系由第三方的<code>Observer</code>来协调。从代码实现上来看，必要的构造函数只实现第三方的<code>Observer</code>即可</p>
<p>从中也能发现，发布订阅模式和观察者模式最大的区别在于，在发布订阅模式里，发布者，并不会直接通知订阅者，换句话说，发布者和订阅者，彼此互不相识。这也是完全解耦的特点</p>
<h2 data-id="heading-6">3. 你所不知道的<code>queueMicrotask()</code></h2>
<p>在<code>JavaScript</code> 中通过 <code>queueMicrotask()</code>使用微任务</p>
<p>这里不对微任务宏任务做深入研究，只简单说明一下：任务可以看成一条一条的执行语句。，一般情况下是同步运行的，从上而下，当遇到异步的事件，就需要将异步事件推入事件循环队列，而事件循环队列有两种，一种是微任务循环队列，一种是宏任务循环队列。微任务先于宏任务执行。</p>
<p>简单使用如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>)
<span class="hljs-built_in">window</span>.queueMicrotask(<span class="hljs-function">()=></span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'c'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>掌握上面的内容，手写<code>Promise</code>将变的异常轻松。完全不需要死记硬背了!!!</p>
<h2 data-id="heading-7">参考资料</h2>
<ol>
<li><a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">观察者模式 vs 发布订阅模式h</a></li>
<li>图解设计模式</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWindowOrWorkerGlobalScope%2FqueueMicrotask" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/WindowOrWorkerGlobalScope/queueMicrotask" ref="nofollow noopener noreferrer">queueMicrotask</a></li>
</ol></div>  
</div>
            