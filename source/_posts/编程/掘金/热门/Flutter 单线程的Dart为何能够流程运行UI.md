
---
title: 'Flutter 单线程的Dart为何能够流程运行UI'
categories: 
    - 编程
    - 掘金
    - 热门

author: 掘金
comments: false
date: Wed, 24 Feb 2021 19:51:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fb48e4227064f48b9aaa57a18ba34af~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Dart异步原理</h1>
<p>Dart 是一门单线程编程语言。对于平时用 iOS 的同学，首先可能会反应：那如果一个操作耗时特别长，不会一直卡住主线程吗？比如iOS，为了不阻塞UI主线程，我们不得不通过另外的线程来发起耗时操作（网络请求/访问本地文件等），然后再通过Handler来和UI线程沟通。Dart 究竟是如何做到的呢？</p>
<p>先给答案：<strong>异步 IO + 事件循环</strong></p>
<h2 data-id="heading-1">1、I/O 模型</h2>
<p>我们先来看看阻塞IO是什么样的：</p>
<pre><code class="copyable">String text = io.read(buffer); //阻塞等待
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注： IO 模型是操作系统层面的，这一小节的代码都是伪代码，只是为了方便理解。</p>
</blockquote>
<p>当相应线程调用了<code>read</code>之后，它就会一直在那里等着结果返回，什么也不干，这是阻塞式的IO</p>
<p><strong>这里普及两个概念：阻塞式调用和非阻塞式调用</strong></p>
<p>阻塞和非阻塞关注的是程序在等待调用结果（消息，返回值）时的状态</p>
<ul>
<li><strong>阻塞式调用</strong>： 调用结果返回之前，当前线程会被挂起，调用线程只有在得到调用结果之后才会继续执行。</li>
<li><strong>非阻塞式调用</strong>： 调用执行之后，当前线程不会停止执行，只需要过一段时间来检查一下有没有结果返回即可。</li>
</ul>
<p>但我们的应用程序经常是要同时处理好几个IO的，即便一个简单的手机App，同时发生的IO可能就有：用户手势（输入），若干网络请求(输入输出)，渲染结果到屏幕（输出）；更不用说是服务端程序，成百上千个并发请求都是家常便饭</p>
<p>有人说，这种情况可以使用多线程啊。这确实是个思路，但受制于CPU的实际并发数，每个线程只能同时处理单个IO，性能限制还是很大，而且还要处理不同线程之间的同步问题，程序的复杂度大大增加。</p>
<p>如果进行IO的时候不用阻塞，那情况就不一样了：</p>
<pre><code class="copyable">while(true)&#123;
  for(io in io_array)&#123;
      status = io.read(buffer);// 不管有没有数据都立即返回
      if(status == OK)&#123;
       
      &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了非阻塞IO，通过轮询的方式，我们就可以对多个IO进行同时处理了，但这样也有一个明显的缺点：在大部分情况下，IO都是没有内容的（CPU的速度远高于IO速度），这样就会导致CPU大部分时间在空转，计算资源依然没有很好得到利用。</p>
<p>为了进一步解决这个问题，人们设计了IO多路转接（IO multiplexing），可以对多个IO监听和设置等待时间：</p>
<pre><code class="copyable">while(true)&#123;
    //如果其中一路IO有数据返回，则立即返回；如果一直没有，最多等待不超过timeout时间
    status = select(io_array, timeout); 
    if(status  == OK)&#123;
      for(io in io_array)&#123;
          io.read() //立即返回，数据都准备好了
      &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了IO多路转接，CPU资源利用效率又有了一个提升。</p>
<p>在上面的代码中，线程依然是可能会阻塞在 select 上或者产生一些空转的，有没有一个更加完美的方案呢？</p>
<p>答案就是异步IO了：</p>
<pre><code class="copyable">io.async_read((data) => &#123;
  // dosomething
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决了Dart单线程进行IO也不会卡的疑问，但主线程如何和大量异步消息打交道呢？接下来我们继续讨论Dart的事件循环机制（Event Loop）。</p>
<h2 data-id="heading-2">2、事件循环（Event Loop）</h2>
<p>Event Loop 完整版的流程图</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fb48e4227064f48b9aaa57a18ba34af~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从上图可知，Dart事件循环机制由一个消息循环(event looper)和两个消息队列构成，其中，两个消息队列是指事件队列(event queue)和微任务队列(Microtask queue)。该机制运行原理为：</p>
<ul>
<li>首先，Dart程序从main函数开始运行，待main函数执行完毕后，event looper开始工作；</li>
<li>然后，event looper优先遍历执行Microtask队列所有事件，直到Microtask队列为空；</li>
<li>接着，event looper才遍历执行Event队列中的所有事件，直到Event队列为空；</li>
<li>最后，视情况退出循环。</li>
</ul>
<h3 data-id="heading-3">微任务</h3>
<p>微任务顾名思义，表示一个短时间内就会完成的异步任务。从上面的流程图可以看到，微任务队列在事件循环中的优先级是最高的，只要队列中还有任务，就可以一直霸占着事件循环。</p>
<p>微任务是由<code>scheduleMicroTask</code>建立的</p>
<pre><code class="copyable">scheduleMicrotask(() => print('This is a microtask'));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过，一般的异步任务通常也很少必须要在事件队列前完成，所以也不需要太高的优先级，因此我们通常很少会直接用到微任务队列，就连 Flutter 内部，也只有 7 处用到了而已（比如，手势识别、文本输入、滚动视图、保存页面效果等需要高优执行任务的场景）。</p>
<h3 data-id="heading-4">Event Queue</h3>
<p>Dart 为 Event Queue 的任务建立提供了一层封装，叫作 Future。从名字上也很容易理解，它表示一个在未来时间才会完成的任务。</p>
<h2 data-id="heading-5">3、Isolate</h2>
<p>尽管 Dart 是基于单线程模型的，但为了进一步利用多核 CPU，将 CPU 密集型运算进行隔离，Dart 也提供了多线程机制，即 Isolate。在 Isolate 中，资源隔离做得非常好，每个 Isolate 都有自己的 Event Loop 与 Queue，Isolate 之间不共享任何资源，只能依靠消息机制通信，因此也就没有资源抢占问题。</p>
<p>假如不同的Isolate需要通信(单向/双向)，就只能通过向对方的事件循环队列里写入任务，并且它们之间的通讯方式是通过port(端口)实现的，其中，Port又分为<code>receivePort(接收端口)和sendPort(发送端口)</code>，它们是成对出现的。Isolate之间通信过程：</p>
<ul>
<li>首先，当前Isolate创建一个ReceivePort对象，并获得对应的SendPort对象；</li>
</ul>
<pre><code class="copyable"> var receivePort = ReceivePort();
 var sendPort = receivePort.sendPort;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>其次，创建一个新的Isolate，并实现新Isolate要执行的异步任务，同时，将当前Isolate的SendPort对象传递给新的Isolate，以便新Isolate使用这个SendPort对象向原来的Isolate发送事件；</li>
</ul>
<pre><code class="copyable">// 调用Isolate.spawn创建一个新的Isolate
// 这是一个异步操作，因此使用await等待执行完毕
var anotherIsolate = await Isolate.spawn(otherIsolateInit, receivePort.sendPort);

// 新Isolate要执行的异步任务
// 即调用当前Isolate的sendPort向其receivePort发送消息
void otherIsolateInit(SendPort sendPort) async &#123;
  value = "Other Thread!";
  sendPort.send("BB");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>然后，调用当前Isolate#receivePort的listen方法监听新的Isolate传递过来的数据。Isolate之间什么数据类型都可以传递，不必做任何标记</li>
</ul>
<pre><code class="copyable">receivePort.listen((date) &#123;
    print("Isolate 1 接受消息：data = $date");
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>最后，消息传递完毕，关闭新创建的Isolate。</li>
</ul>
<pre><code class="copyable">anotherIsolate?.kill(priority: Isolate.immediate);
anotherIsolate =null;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">Future异步详解</h1>
<h2 data-id="heading-7">Future的介绍</h2>
<p>在写程序的过程中，肯定会有一部分比较耗时代码是需要异步执行的。比如网络操作，我们需要异步去请求数据，并且还需要处理请求成功和请求失败的两种情况。</p>
<p>在Flutter中，使用Future来执行耗时操作，表示在未来会返回某个值，并可以使用then（）方法和catchError（）来注册callback来监听Future的处理结果。</p>
<pre><code class="copyable">Future<Response> respFuture = http.get('https://example.com'); //发起请求
respFuture.then((response) &#123; //成功，匿名函数
  if (response.statusCode == 200) &#123;
    var data = reponse.data;
  &#125;
&#125;).catchError((error) &#123; //失败
   handle(error);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种模式简化和统一了异步的处理</p>
<p>Future 对象封装了Dart 的异步操作，它有未完成（uncompleted）和已完成（completed）两种状态。</p>
<p>在Dart中，所有涉及到IO的函数都封装成Future对象返回，在你调用一个异步函数的时候，在结果或者错误返回之前，你得到的是一个uncompleted状态的Future。</p>
<p><strong>一个Future对象会有以下两种状态</strong></p>
<ul>
<li>pending：表示Future对象的计算过程仍在执行中，这个时候还没有可以用的result。</li>
<li>completed：表示Future对象已经计算结束了，可能会有两种情况，一种是正确的结果，一种是失败的结果。</li>
</ul>
<h2 data-id="heading-8">构造方法</h2>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f4690d863e04f3a9a5e8a433d1bbfd9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我看查看API发现Future总共有6个构造函数</p>
<ul>
<li>1、默认构造方法<code>Future(FutureOr<T> computation())</code></li>
<li>2、<code>Future.micortask</code>构造方法</li>
<li>3、<code>Future.sync(FutureOr<T> computation())</code>构造方法</li>
<li>4、<code>Future.value([FutureOr<T>? value])</code>构造方法</li>
<li>5、<code>Future.error(Object error, [StackTrace? stackTrace])</code>构造方法</li>
<li>6、<code>Future.delayed(Duration duration, [FutureOr<T> computation()?])</code>构造方法</li>
</ul>
<h3 data-id="heading-9">1、默认构造方法</h3>
<p>通过Future的默认构造方法可以创建一个Future对象,。默认构造方法的签名如下</p>
<pre><code class="copyable">factory Future(FutureOr<T> computation()) &#123;
    _Future<T> result = new _Future<T>();
    Timer.run(() &#123;
      try &#123;
        result._complete(computation());
      &#125; catch (e, s) &#123;
        _completeWithErrorCallback(result, e, s);
      &#125;
    &#125;);
    return result;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数类型是<code>FutureOr<T> computation()</code>，表示返回值是<code>FutureOr<T></code>类型的函数。</p>
<p>通过这个方法创建的<code>Future</code>，<code>computation函数</code>会被添加到event队列中执行。</p>
<h3 data-id="heading-10">2、<code>Future.micortask</code>构造方法</h3>
<pre><code class="copyable">factory Future.microtask(FutureOr<T> computation()) &#123;
    _Future<T> result = new _Future<T>();
    scheduleMicrotask(() &#123;
      try &#123;
        result._complete(computation());
      &#125; catch (e, s) &#123;
        _completeWithErrorCallback(result, e, s);
      &#125;
    &#125;);
    return result;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<code>scheduleMicrotask</code>方法将computation函数添加到microtask队列中，优先于event队列执行。</p>
<pre><code class="copyable">    Future(() &#123;
      print("default fauture");
    &#125;);

    Future.microtask(() &#123;
      print("microtask future");
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>譬如上面方法会优先打印<code>microtask future</code></p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8858f9ca0474df88da4f1fb1c1154f1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">3、<code>Future.sync</code>构造方法</h3>
<pre><code class="copyable">factory Future.sync(FutureOr<T> computation()) &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将会在当前task执行computation计算，而不是将计算过程添加到任务队列中。</p>
<h3 data-id="heading-12">4、<code>Future.value()</code>构造方法</h3>
<p>创建一个返回指定value值的Future</p>
<pre><code class="copyable">factory Future.value([FutureOr<T>? value]) &#123;
    return new _Future<T>.immediate(value == null ? value as T : value);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">var future = Future.value(1);
var future1 = Future.value('1');
print(future);
print(future1);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7ec1200291b43c889b64ff353687c8a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">5、<code>Future.error</code>构造方法</h3>
<pre><code class="copyable">factory Future.error(Object error, [StackTrace? stackTrace]) &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<code>error对象</code>和可选的stackTrace创建Future,可以使用该方法创建个一个状态为failed的Future对象。</p>
<h3 data-id="heading-14">6、<code>Future.delayed（）</code>构造方法</h3>
<pre><code class="copyable">factory Future.delayed(Duration duration, [FutureOr<T> computation()?]) &#123;
    if (computation == null && !typeAcceptsNull<T>()) &#123;
      throw ArgumentError.value(
          null, "computation", "The type parameter is not nullable");
    &#125;
    _Future<T> result = new _Future<T>();
    new Timer(duration, () &#123;
      if (computation == null) &#123;
        result._complete(null as T);
      &#125; else &#123;
        try &#123;
          result._complete(computation());
        &#125; catch (e, s) &#123;
          _completeWithErrorCallback(result, e, s);
        &#125;
      &#125;
    &#125;);
    return result;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建一个延迟执行的future。 例如下面的例子，利用Future延迟两秒后可以打印出字符串。</p>
<pre><code class="copyable">var futureDelayed = Future.delayed(Duration(seconds: 2), () &#123;
  print("Future.delayed");
  return 2;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">静态方法</h2>
<h3 data-id="heading-16">1、wait</h3>
<pre><code class="copyable">static Future<List<T>> wait<T>(Iterable<Future<T>> futures,
      &#123;bool eagerError = false, void cleanUp(T successValue)?&#125;)&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>wait静态方法可以等待多个Future执行完成，并通过List获取所有Future的结果。如果其中一个Future对象发生异常，会导致最终结果为failed</code></p>
<p>可选参数</p>
<ul>
<li>1、<code>eagerError</code>:eagerError默认值为false，当某一个Future发生异常时，默认不会立刻使Future处于failed状态，而是等待所有Future都有结果后，改变状态为failed。如果设置为true，当其中一个Future发生异常时，会立刻导致最终结果为failed</li>
<li>2、<code>cleanUp</code>：如果设置了cleanUp参数，当多个Future中的一个发生异常时，其他成功的Future的(非null)结果会传递给cleanUp参数。如果没有发生异常cleanUp函数不会被调用。</li>
</ul>
<h3 data-id="heading-17">2、forEach</h3>
<pre><code class="copyable">static Future forEach<T>(Iterable<T> elements, FutureOr action(T element)) &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>forEach</code>静态方法可以遍历<code>Iterable</code>中的每个元素执行一个操作，如果遍历操作返回的是Future对象，则在该Future完成后再进行下一次遍历，全部完成后返回null。如果在某一次操作中发生异常，会停止遍历，最终的Future的状态为failed。</p>
<p>比如下面的例子，根据&#123;1,2,3&#125;创建3个延迟对应秒数的Future。执行结果为1秒后打印1，再过2秒打印2，再过3秒打印3，总时间为6秒。</p>
<pre><code class="copyable">Future.forEach(&#123;1,2,3&#125;, (num)&#123;
      return Future.delayed(Duration(seconds: num),()&#123;print(num);&#125;);
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2036e937f864ae4b50f4654c2f8bf1a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">3、any</h3>
<pre><code class="copyable">static Future<T> any<T>(Iterable<Future<T>> futures) &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回的是第一个执行完成的future的结果，不会管这个结果是正确的还是error的</p>
<h3 data-id="heading-19">4、doWhile</h3>
<p>重复性地执行某一个动作，直到返回false或者Future，退出循环</p>
<pre><code class="copyable">static Future doWhile(FutureOr<bool> action()) &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用场景:适用于一些需要递归操作的场景。</p>
<p>例如下面的例子，生成一个随机数进行等待，直到十秒之后，操作结束。</p>
<pre><code class="copyable">void futureDoWhile()&#123;
  var random = new Random();
  var totalDelay = 0;
  Future
      .doWhile(() &#123;
    if (totalDelay > 10) &#123;
      print('total delay: $totalDelay seconds');
      return false;
    &#125;
    var delay = random.nextInt(5) + 1;
    totalDelay += delay;
    return new Future.delayed(new Duration(seconds: delay), () &#123;
      print('waited $delay seconds');
      return true;
    &#125;);
  &#125;)
      .then(print)
      .catchError(print);
&#125;
//输出结果：
I/flutter (11113): waited 5 seconds
I/flutter (11113): waited 1 seconds
I/flutter (11113): waited 3 seconds
I/flutter (11113): waited 2 seconds
I/flutter (11113): total delay: 12 seconds
I/flutter (11113): null
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">处理结果</h2>
<h3 data-id="heading-21">1、then</h3>
<p>创建完成Future对象后，可以通过then方法接收Future的结果。</p>
<pre><code class="copyable">Future<R> then<R>(FutureOr<R> onValue(T value), &#123;Function onError&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">Future<Response> respFuture = http.get('https://example.com'); //发起请求
respFuture.then((response) &#123; //成功，匿名函数
  if (response.statusCode == 200) &#123;
    var data = reponse.data;
  &#125;
&#125;).catchError((error) &#123; //失败
   handle(error);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">2、catchError</h3>
<p>如果Future内的函数执行发生异常，可以通过Future.catchError来处理异常：</p>
<pre><code class="copyable">Future<void> fetchUserOrder() &#123;
  return Future.delayed(Duration(seconds: 3),
  () => throw Exception('Logout failed: user ID is invalid'));
&#125;
void main() &#123;
  fetchUserOrder().catchError((err, s)&#123;print(err);&#125;);
  print('Fetching user order...');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果：</p>
<pre><code class="copyable">Fetching user order...
Exception: Logout failed: user ID is invalid
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">3、whenComplete</h3>
<p>Future.whenComplete总是在Future完成后调用，不管Future的结果是正确的还是错误的。</p>
<pre><code class="copyable">Future<T> whenComplete(FutureOr<void> action());
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">4、timeout方法</h3>
<pre><code class="copyable">Future<T> timeout(Duration timeLimit, &#123;FutureOr<T> onTimeout()&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>timeout方法创建一个新的Future对象，接收一个Duration类型的timeLimit参数来设置超时时间。如果原Future在超时之前完成，最终的结果就是该原Future的值；如果达到超时时间后还未完成，就会产生TimeoutException异常。
该方法有一个onTimeout可选参数，如果设置了该参数，当发生超时时会调用该函数，该函数的返回值为Future的新的值，而不会产生TimeoutException。</p>
<h2 data-id="heading-25">async 和 await</h2>
<p>想象一个这样的场景：</p>
<ul>
<li>
<ol>
<li>先调用登录接口；</li>
</ol>
</li>
<li>
<ol start="2">
<li>根据登录接口返回的token获取用户信息；</li>
</ol>
</li>
<li>
<ol start="3">
<li>最后把用户信息缓存到本机。</li>
</ol>
</li>
</ul>
<p>接口定义：</p>
<pre><code class="copyable">Future<String> login(String name,String password)&#123;
  //登录
&#125;
Future<User> fetchUserInfo(String token)&#123;
  //获取用户信息
&#125;
Future saveUserInfo(User user)&#123;
  // 缓存用户信息
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用Future大概可以这样写：</p>
<pre><code class="copyable">login('name','password')
.then((token) => fetchUserInfo(token))
 .then((user) => saveUserInfo(user));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>换成<code>async 和await</code>则可以这样：</p>
<pre><code class="copyable">void doLogin() async &#123;
  String token = await login('name','password'); //await 必须在 async 函数体内
  User user = await fetchUserInfo(token);
  await saveUserInfo(user);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>声明了<code>async</code>的函数，返回值是必须是Future对象。即便你在async函数里面直接返回T类型数据，编译器会自动帮你包装成<code>Future<T></code>类型的对象，如果是void函数，则返回<code>Future<void></code>对象。在遇到<code>await</code>的时候，又会把Futrue类型拆包，又会原来的数据类型暴露出来，请注意，await所在的函数必须添加async关键词</p>
<p>await的代码发生异常，捕获方式跟同步调用函数一样：</p>
<pre><code class="copyable">void doLogin() async &#123;
  try &#123;
    var token = await login('name','password');
    var user = await fetchUserInfo(token);
    await saveUserInfo(user);
  &#125; catch (err) &#123;
    print('Caught error: $err');
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>得益于async 和await 这对语法糖，你可以用同步编程的思维来处理异步编程，大大简化了异步代码的处理</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            