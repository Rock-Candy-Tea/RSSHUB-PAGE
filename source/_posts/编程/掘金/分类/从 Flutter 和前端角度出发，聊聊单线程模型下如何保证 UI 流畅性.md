
---
title: '从 Flutter 和前端角度出发，聊聊单线程模型下如何保证 UI 流畅性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26e1419879944200b7f0e73f515e87c4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 06:40:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26e1419879944200b7f0e73f515e87c4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>文章主题是“单线程模型下如何保证 UI 的流畅性”。该话题针对的是 Flutter 性能原理展开的，但是 dart 语言就是 js 的延伸，很多概念和机制都是一样的。具体不细聊。此外 js 也是单线程模型，在界面展示和 IO 等方面和 dart 类似。所以结合对比讲一下，帮助梳理和类比，更加容易掌握本文的主题，和知识的横向拓展。</p>
<p>先从前端角度出发，分析下 event loop 和事件队列模型。再从 Flutter 层出发聊聊 dart 侧的事件队列和同步异步任务之间的关系。</p>
</blockquote>
<h2 data-id="heading-0">一、单线程模型的设计</h2>
<h3 data-id="heading-1">1. 最基础的单线程处理简单任务</h3>
<p>假设有几个任务：</p>
<ul>
<li>任务1: "姓名：" +  "杭城小刘"</li>
<li>任务2:  "年龄：" + "1995" + "02" + "20"</li>
<li>任务3:  "大小："  + (2021 - 1995 + 1)</li>
<li>任务4:  打印任务1、2、3 的结果</li>
</ul>
<p>在单线程中执行，代码可能如下：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-comment">//c</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">mainThread</span> <span class="hljs-params">()</span> </span>&#123;
  string name = <span class="hljs-string">"姓名："</span> + <span class="hljs-string">"杭城小刘"</span>;
  string birthday = <span class="hljs-string">"年龄："</span> + <span class="hljs-string">"1995"</span> + <span class="hljs-string">"02"</span> + <span class="hljs-string">"20"</span> 
  <span class="hljs-keyword">int</span> age = <span class="hljs-number">2021</span> - <span class="hljs-number">1995</span> + <span class="hljs-number">1</span>;
<span class="hljs-built_in">printf</span>(<span class="hljs-string">"个人信息为：%s, %s, 大小：%d"</span>, name.<span class="hljs-built_in">c_str</span>(), birthday.<span class="hljs-built_in">c_str</span>(), age);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>线程开始执行任务，按照需求，单线程依次执行每个任务，执行完毕后线程马上退出。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26e1419879944200b7f0e73f515e87c4~tplv-k3u1fbpfcp-zoom-1.image" alt="基础单线程模型" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">2. 线程运行过程中来了新的任务怎么处理？</h3>
<p>问题1 介绍的线程模型太简单太理想了，不可能从一开始就 n 个任务就确定了，大多数情况下，会接收到新的 m 个任务。那么 section1 中的设计就无法满足该需求。</p>
<p>**要在线程运行的过程中，能够接受并执行新的任务，就需要有一个事件循环机制。**最基础的事件循环可以想到用一个循环来实现。</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-comment">// c++</span>
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">getInput</span><span class="hljs-params">()</span> </span>&#123;
  <span class="hljs-keyword">int</span> input = <span class="hljs-number">0</span>;
  cout<< <span class="hljs-string">"请输入一个数"</span>;
  cin>>input;
  <span class="hljs-keyword">return</span> input;
&#125;

<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">mainThread</span> <span class="hljs-params">()</span> </span>&#123;
  <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>) &#123;
    <span class="hljs-keyword">int</span> input1 = <span class="hljs-built_in">getInput</span>();
    <span class="hljs-keyword">int</span> input2 = <span class="hljs-built_in">getInput</span>();
    <span class="hljs-keyword">int</span> sum = input1 + input2;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"两数之和为：%d"</span>, sum);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相较于第一版线程设计，这一版做了以下改进：</p>
<ul>
<li>引入了<strong>循环机制</strong>，线程不会做完事情马上退出。</li>
<li>引入了<strong>事件</strong>。线程一开始会等待用户输入，等待的时候线程处于暂停状态，当用户输入完毕，线程得到输入的信息，此时线程被激活。执行相加的操作，最终输出结果。不断的等待输入，并计算输出。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca46aa0dcd6f45ddad5e423643ff3237~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">3. 处理来自其他线程的任务</h3>
<p>真实环境中的线程模块远远没有这么简单。比如浏览器环境下，线程可能正在绘制，可能会接收到1个来自用户鼠标点击的事件，1个来自网络加载 css 资源完成的事件等等。第二版线程模型虽然引入了事件循环机制，可以接受新的事件任务，但是发现没？这些任务之来自线程内部，该设计是无法接受来自其他线程的任务的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09b5bf9bd00e433aaa4e86b2b7578788~tplv-k3u1fbpfcp-zoom-1.image" alt="第三版线程模型" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图可以看出，渲染主线程会频繁接收到来自于 IO 线程的一些事件任务，当接受到的资源加载完成后的消息，则渲染线程会开始 DOM 解析；当接收到来自鼠标点击的消息，渲染主线程则会执行绑定好的鼠标点击事件脚本（js）来处理事件。</p>
<p>需要一个合理的数据结构，来存放并获取其他线程发送的消息？</p>
<p><strong>消息队列</strong>这个词大家都听过，在 GUI 系统中，事件队列是一个通用解决方案。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32326829c0054c938e6c125069288bec~tplv-k3u1fbpfcp-zoom-1.image" alt="事件队列" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>消息队列（事件队列）是一种合理的数据结构。要执行的任务添加到队列的尾部，需要执行的任务，从队列的头部取出。</strong></p>
<p>有了消息队列之后，线程模型得到了升级。如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4ec4d54fe604cde962b076350bd0d4b~tplv-k3u1fbpfcp-zoom-1.image" alt="单线程模型第四版" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出改造分为3个步骤：</p>
<ul>
<li>构建一个消息队列</li>
<li>IO 线程产生的新任务会被添加到消息队列的尾部</li>
<li>渲染主线程会循环的从消息队列的头部读取任务，执行任务</li>
</ul>
<p>伪代码。构造队列接口部分</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TaskQueue</span> &#123;</span>
  <span class="hljs-keyword">public</span>:
  <span class="hljs-function">Task <span class="hljs-title">fetchTask</span> <span class="hljs-params">()</span></span>; <span class="hljs-comment">// 从队列头部取出1个任务</span>
  <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">addTask</span> <span class="hljs-params">(Task task)</span></span>; <span class="hljs-comment">// 将任务插入到队列尾部</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改造主线程</p>
<pre><code class="hljs language-c++ copyable" lang="c++">TaskQueue taskQueue;
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">processTask</span> <span class="hljs-params">()</span></span>;
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">mainThread</span> <span class="hljs-params">()</span> </span>&#123;
  <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
  Task task = taskQueue.<span class="hljs-built_in">fetchTask</span>();
  <span class="hljs-built_in">processTask</span>(task);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>IO 线程</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">handleIOTask</span> <span class="hljs-params">()</span> </span>&#123;
  Task clickTask;
  taskQueue.<span class="hljs-built_in">addTask</span>(clickTask);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Tips: 事件队列是存在多线程访问的情况，所以需要加锁。</p>
<h3 data-id="heading-4">4. 处理来自其他线程的任务</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab68174502d24eb594e7c6c5e9f09ee3~tplv-k3u1fbpfcp-zoom-1.image" alt="单线程模型+跨进程任务" loading="lazy" referrerpolicy="no-referrer"></p>
<p>浏览器环境中，　渲染进程经常接收到来自其他进程的任务，IO 线程专门用来接收来自其他进程传递来的消息。IPC 专门处理跨进程间的通信。</p>
<h3 data-id="heading-5">5. 消息队列中的任务类型</h3>
<p>消息队列中有很多消息类型。内部消息：如鼠标滚动、点击、移动、宏任务、微任务、文件读写、定时器等等。</p>
<p>消息队列中还存在大量的与页面相关的事件。如 JS 执行、DOM 解析、样式计算、布局计算、CSS 动画等等。</p>
<p>上述事件都是在渲染主线程中执行的，因此编码时需注意，尽量减小这些事件所占用的时长。</p>
<h3 data-id="heading-6">6. 如何安全退出</h3>
<p>Chrome 设计上，确定要退出当前页面时，页面主线程会设置一个退出标志的变量，每次执行完1个任务时，判断该标志。如果设置了，则中断任务，退出线程</p>
<h3 data-id="heading-7">7. 单线程的缺点</h3>
<p>事件队列的特点是先进先出，后进后出。那后进的任务也许会被前面的任务因为执行时间过长而阻塞，等待前面的任务执行完毕才可以执行后面的任务。这样存在2个问题。</p>
<ul>
<li>
<p>如何处理高优先级的任务</p>
<p>假如要监控 DOM 节点的变化情况（插入、删除、修改 innerHTML），然后触发对应的逻辑。最基础的做法就是设计一套监听接口，当 DOM 变化时，渲染引擎同步调用这些接口。不过这样子存在很大的问题，就是 DOM 变化会很频繁。如果每次 DOM 变化都触发对应的 JS 接口，则该任务执行会很长，导致<strong>执行效率</strong>的降低</p>
<p>如果将这些 DOM 变化做为异步消息，假如消息队列中。可能会存在因为前面的任务在执行导致当前的 DOM 消息不会被执行的问题，也就是影响了监控的<strong>实时性</strong>。</p>
<p>如何权衡效率和实时性？<strong>微任务</strong> 就是解决该类问题的。</p>
<p>通常，我们把消息队列中的任务成为<strong>宏任务</strong>，每个宏任务中都包含一个<strong>微任务队列</strong>，在执行宏任务的过程中，假如 DOM 有变化，则该变化会被添加到该宏任务的微任务队列中去，这样子效率问题得以解决。</p>
<p>当宏任务中的主要功能执行完毕欧，渲染引擎会执行微任务队列中的微任务。因此实时性问题得以解决</p>
</li>
<li>
<p>如何解决单个任务执行时间过长的问题</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/152f6953a87e40c6a818ba330f4a8cd1~tplv-k3u1fbpfcp-zoom-1.image" alt="卡顿" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出，假如 JS 计算超时导致动画 paint 超时，会造成卡顿。浏览器为避免该问题，采用 callback 回调的设计来规避，也就是让 JS 任务延后执行。</p>
</li>
</ul>
<h2 data-id="heading-8">二、 flutter 里的单线程模型</h2>
<h3 data-id="heading-9">1. event loop 机制</h3>
<p>Dart 是单线程的，也就是代码会有序执行。此外 Dart 作为 Flutter 这一 GUI 框架的开发语言，必然支持异步。</p>
<p>一个 Flutter 应用包含一个或多个 <strong>isolate</strong>，默认方法的执行都是在 <strong>main isolate</strong> 中；<strong>一个 isolate 包含1个 Event loop 和1个 Task queue。其中，Task queue 包含1个 Event queue 事件队列和1个 MicroTask queue 微任务队列</strong>。如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19d62960acce4fce8c6b4a36f74d60d8~tplv-k3u1fbpfcp-zoom-1.image" alt="Flutter Event Loop" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为什么需要异步？因为大多数场景下 应用都并不是一直在做运算。比如一边等待用户的输入，输入后再去参与运算。这就是一个 IO 的场景。所以单线程可以再等待的时候做其他事情，而当真正需要处理运算的时候，再去处理。因此虽是单线程，但是给我们的感受是同事在做很多事情（空闲的时候去做其他事情）</p>
<p>某个任务涉及 IO 或者异步，则主线程会先去做其他需要运算的事情，这个动作是靠 event loop 驱动的。和 JS 一样，dart 中存储事件任务的角色是事件队列 event queue。</p>
<p>Event queue 负责存储需要执行的任务事件，比如 DB 的读取。</p>
<p>Dart 中存在2个队列，一个微任务队列（Microtask Queue）、一个事件队列（Event Queue）。</p>
<p>Event loop 不断的轮询，先判断微任务队列是否为空，从队列头部取出需要执行的任务。如果微任务队列为空，则判断事件队列是否为空，不为空则从头部取出事件（比如键盘、IO、网络事件等），然后在主线程执行其回调函数，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a80f9633b445aeb63d63d6b53f1883~tplv-k3u1fbpfcp-zoom-1.image" alt="Flutter 单线程模型" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">2. 异步任务</h3>
<p>微任务，即在一个很短的时间内就会完成的异步任务。微任务在事件循环中优先级最高，只要微任务队列不为空，事件循环就不断执行微任务，后续的事件队列中的任务持续等待。微任务队列可由 <code>scheduleMicroTask</code> 创建。</p>
<p>通常情况，微任务的使用场景比较少。Flutter 内部也在诸如手势识别、文本输入、滚动视图、保存页面效果等需要高优执行任务的场景用到了微任务。</p>
<p>所以，一般需求下，异步任务我们使用优先级较低的 Event Queue。比如 IO、绘制、定时器等，都是通过事件队列驱动主线程来执行的。</p>
<p>Dart 为 Event Queue 的任务提供了一层封装，叫做 Future。把一个函数体放入 Future 中，就完成了同步任务到异步任务的包装（类似于 iOS 中通过 GCD 将一个任务以同步、异步提交给某个队列）。Future 具备链式调用的能力，可以在异步执行完毕后执行其他任务（函数）。</p>
<p>看一段具体代码：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> main() &#123;
  <span class="hljs-built_in">print</span>(<span class="hljs-string">'normal task 1'</span>);
  Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'Task1 Future 1'</span>));
  <span class="hljs-built_in">print</span>(<span class="hljs-string">'normal task 2'</span>);
  Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'Task1 Future 2'</span>))
      .then((value) => <span class="hljs-built_in">print</span>(<span class="hljs-string">"subTask 1"</span>))
      .then((value) => <span class="hljs-built_in">print</span>(<span class="hljs-string">"subTask 2"</span>));
&#125;
<span class="hljs-comment">//</span>
lbp<span class="hljs-meta">@MBP</span>  ~/Desktop  dart index.dart
normal task <span class="hljs-number">1</span>
normal task <span class="hljs-number">2</span>
Task1 Future <span class="hljs-number">1</span>
Task1 Future <span class="hljs-number">2</span>
subTask <span class="hljs-number">1</span>
subTask <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main 方法内，先添加了1个普通同步任务，然后以 Future 的形式添加了1个异步任务，Dart 会将异步任务加入到事件队列中，然后理解返回。后续代码继续以同步任务的方式执行。然后再添加了1个普通同步任务。然后再以 Future 的方式添加了1个异步任务，异步任务被加入到事件队列中。此时，事件队列中存在2个异步任务，Dart 在事件队列头部取出1个任务以同步的方式执行，全部执行（先进先出）完毕后再执行后续的 then。</p>
<p>Future 与 then 公用1个事件循环。如果存在多个 then，则按照顺序执行。</p>
<p>例2:</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> main() &#123;
  Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'Task1 Future 1'</span>));
  Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'Task1 Future 2'</span>));

  Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'Task1 Future 3'</span>))
      .then((_) => <span class="hljs-built_in">print</span>(<span class="hljs-string">'subTask 1 in Future 3'</span>));

  Future(() => <span class="hljs-keyword">null</span>).then((_) => <span class="hljs-built_in">print</span>(<span class="hljs-string">'subTask 1 in empty Future'</span>));
&#125;
lbp<span class="hljs-meta">@MBP</span>  ~/Desktop  dart index.dart
Task1 Future <span class="hljs-number">1</span>
Task1 Future <span class="hljs-number">2</span>
Task1 Future <span class="hljs-number">3</span>
subTask <span class="hljs-number">1</span> <span class="hljs-keyword">in</span> Future <span class="hljs-number">3</span>
subTask <span class="hljs-number">1</span> <span class="hljs-keyword">in</span> empty Future
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main 方法内，Task 1 添加到 Future 1中，被 Dart 添加到 Event Queue 中。Task 1 添加到 Future 2中，被 Dart 添加到 Event Queue 中。Task 1 添加到 Future 3中，被 Dart 添加到 Event Queue 中，subTask 1 和 Task 1 共用 Event Queue。Future 4中任务为空，所以 then 里的代码会被加入到 Microtask Queue，以便下一轮事件循环中被执行。</p>
<p>综合例子</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> main() &#123;
  Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'Task1 Future 1'</span>));
  Future fx = Future(() => <span class="hljs-keyword">null</span>);
  Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">"Task1 Future 3"</span>)).then((value) &#123;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"subTask 1 Future 3"</span>);
    scheduleMicrotask(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">"Microtask 1"</span>));
  &#125;).then((value) => <span class="hljs-built_in">print</span>(<span class="hljs-string">"subTask 3 Future 3"</span>));

  Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">"Task1 Future 4"</span>))
      .then((value) => Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">"sub subTask 1 Future 4"</span>)))
      .then((value) => <span class="hljs-built_in">print</span>(<span class="hljs-string">"sub subTask 2 Future 4"</span>));

  Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">"Task1 Future 5"</span>));

  fx.then((value) => <span class="hljs-built_in">print</span>(<span class="hljs-string">"Task1 Future 2"</span>));

  scheduleMicrotask(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">"Microtask 2"</span>));

  <span class="hljs-built_in">print</span>(<span class="hljs-string">"normal Task"</span>);
&#125;
lbp<span class="hljs-meta">@MBP</span>  ~/Desktop  dart index.dart
normal Task
Microtask <span class="hljs-number">2</span>
Task1 Future <span class="hljs-number">1</span>
Task1 Future <span class="hljs-number">2</span>
Task1 Future <span class="hljs-number">3</span>
subTask <span class="hljs-number">1</span> Future <span class="hljs-number">3</span>
subTask <span class="hljs-number">3</span> Future <span class="hljs-number">3</span>
Microtask <span class="hljs-number">1</span>
Task1 Future <span class="hljs-number">4</span>
Task1 Future <span class="hljs-number">5</span>
sub subTask <span class="hljs-number">1</span> Future <span class="hljs-number">4</span>
sub subTask <span class="hljs-number">2</span> Future <span class="hljs-number">4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解释：</p>
<ul>
<li>Event Loop 优先执行 main 方法同步任务，再执行微任务，最后执行 Event Queue 的异步任务。所以 normal Task 先执行</li>
<li>同理微任务  Microtask 2 执行</li>
<li>其次，Event Queue FIFO，Task1 Future 1 被执行</li>
<li>fx Future 内部为空，所以 then 里的内容被加到微任务队列中去，微任务优先级最高，所以 Task1 Future 2 被执行</li>
<li>其次，Task1 Future 3 被执行。由于存在2个 then，先执行第一个 then 中的 subTask 1 Future 3，然后遇到微任务，所以 Microtask 1 被添加到微任务队列中去，等待下一次 Event Loop 到来时触发。接着执行第二个 then 中的 subTask 3 Future 3。随着下一次 Event Loop 到来，Microtask 1 被执行</li>
<li>其次，Task1 Future 4 被执行。随后的第一个 then 中的任务又是被 Future 包装成一个异步任务，被添加到 Event Queue 中，第二个 then 中的内容也被添加到 Event Queue 中。</li>
<li>接着，执行 Task1 Future 5。本次事件循环结束</li>
<li>等下一轮事件循环到来，打印队列中的  sub subTask 1 Future 4、sub subTask 1 Future 5.</li>
</ul>
<h3 data-id="heading-11">3. 异步函数</h3>
<p>异步函数的结果在将来某个时刻才返回，所以需要返回一个 Future 对象，供调用者使用。调用者根据需求，判断是在 Future 对象上注册一个 then 等 Future 执行体结束后再进行异步处理，还是同步等到 Future 执行结束。Future 对象如果需要同步等待，则需要在调用处添加 <strong>await</strong>，且 Future 所在的函数需要使用 <strong>async</strong> 关键字。</p>
<p>await 并不是同步等待，而是异步等待。Event Loop 会将调用体所在的函数也当作异步函数，将等待语句的上下文整体添加到 Event Queue 中，一旦返回，Event Loop 会在 Event Queue 中取出上下文代码，等待的代码继续执行。</p>
<p>await 阻塞的是当前上下文的后续代码执行，并不能阻塞其调用栈上层的后续代码执行</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> main() &#123;
  Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'Task1 Future 1'</span>))
      .then((_) <span class="hljs-keyword">async</span> => <span class="hljs-keyword">await</span> Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">"subTask 1 Future 2"</span>)))
      .then((_) => <span class="hljs-built_in">print</span>(<span class="hljs-string">"subTask 2 Future 2"</span>));
  Future(() => <span class="hljs-built_in">print</span>(<span class="hljs-string">'Task1 Future 2'</span>));
&#125;
lbp<span class="hljs-meta">@MBP</span>  ~/Desktop  dart index.dart
Task1 Future <span class="hljs-number">1</span>
Task1 Future <span class="hljs-number">2</span>
subTask <span class="hljs-number">1</span> Future <span class="hljs-number">2</span>
subTask <span class="hljs-number">2</span> Future <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解析：</p>
<ul>
<li>Future 中的 Task1 Future 1 被添加到 Event Queue 中。其次遇到第一个 then，then 里面是 Future 包装的异步任务，所以 <code>Future(() => print("subTask 1 Future 2"))</code> 被添加到 Event Queue 中，所在的 await 函数也被添加到了 Event Queue 中。第二个 then 也被添加到 Event Queue 中</li>
<li>第二个 Future 中的 'Task1 Future 2 不会被 await 阻塞，因为 await 是异步等待（添加到 Event Queue）。所以执行 'Task1 Future 2。随后执行 "subTask 1 Future 2，接着取出 await 执行 subTask 2 Future 2</li>
</ul>
<h3 data-id="heading-12">4. Isolate</h3>
<p>Dart 为了利用多核 CPU，将 CPU 层面的密集型计算进行了隔离设计，提供了多线程机制，即 Isolate。每个 Isolate 资源隔离，都有自己的 Event Loop 和 Event Queue、Microtask Queue。Isolate 之间的资源共享通过消息机制通信（和进程一样）</p>
<p>使用很简单，创建时需要传递一个参数。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> coding(language) &#123;
  <span class="hljs-built_in">print</span>(<span class="hljs-string">"hello "</span> + language);
&#125;
<span class="hljs-keyword">void</span> main() &#123;
  Isolate.spawn(coding, <span class="hljs-string">"Dart"</span>);
&#125;
lbp<span class="hljs-meta">@MBP</span>  ~/Desktop  dart index.dart
hello Dart
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大多数情况下，不仅仅需要并发执行。可能还需要某个 Isolate 运算结束后将结果告诉主 Isolate。可以通过 Isolate 的管道（SendPort）实现消息通信。可以在主 Isolate 中将管道作为参数传递给子 Isolate，当子 Isolate 运算结束后将结果利用这个管道传递给主 Isolate</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> coding(SendPort port) &#123;
  <span class="hljs-keyword">const</span> sum = <span class="hljs-number">1</span> + <span class="hljs-number">2</span>;
  <span class="hljs-comment">// 给调用方发送结果</span>
  port.send(sum);
&#125;

<span class="hljs-keyword">void</span> main() &#123;
  testIsolate();
&#125;

testIsolate() <span class="hljs-keyword">async</span> &#123;
  ReceivePort receivePort = ReceivePort(); <span class="hljs-comment">// 创建管道</span>
  Isolate isolate = <span class="hljs-keyword">await</span> Isolate.spawn(coding, receivePort.sendPort); <span class="hljs-comment">// 创建 Isolate，并传递发送管道作为参数</span>
<span class="hljs-comment">// 监听消息</span>
  receivePort.listen((message) &#123;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"data: <span class="hljs-subst">$message</span>"</span>);
    receivePort.close();
    isolate?.kill(priority: Isolate.immediate);
    isolate = <span class="hljs-keyword">null</span>;
  &#125;);
&#125;
lbp<span class="hljs-meta">@MBP</span>  ~/Desktop  dart index.dart
data: <span class="hljs-number">3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外 Flutter 中提供了执行并发计算任务的快捷方式-<strong>compute 函数</strong>。其内部对 Isolate 的创建和双向通信进行了封装。</p>
<p>实际上，业务开发中使用 compute 的场景很少，比如 JSON 的编解码可以用 compute。</p>
<p>计算阶乘：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-built_in">int</span> testCompute() <span class="hljs-keyword">async</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> compute(syncCalcuateFactorial, <span class="hljs-number">100</span>);
&#125;

<span class="hljs-built_in">int</span> syncCalcuateFactorial(upperBounds) => upperBounds < <span class="hljs-number">2</span>
    ? upperBounds
    : upperBounds * syncCalcuateFactorial(upperBounds - <span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ul>
<li>Dart 是单线程的，但通过事件循环可以实现异步</li>
<li>Future 是异步任务的封装，借助于 await 与 async，我们可以通过事件循环实现非阻塞的同步等待</li>
<li>Isolate 是 Dart 中的多线程，可以实现并发，有自己的事件循环与 Queue，独占资源。Isolate 之间可以通过消息机制进行单向通信，这些传递的消息通过对方的事件循环驱动对方进行异步处理。</li>
<li>flutter 提供了 CPU 密集运算的 compute 方法，内部封装了 Isolate 和 Isolate 之间的通信</li>
<li>事件队列、事件循环的概念在 GUI 系统中非常重要，几乎在前端、Flutter、iOS、Android 甚至是 NodeJS 中都存在。</li>
</ul></div>  
</div>
            