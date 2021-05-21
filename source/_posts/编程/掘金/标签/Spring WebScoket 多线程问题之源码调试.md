
---
title: 'Spring WebScoket 多线程问题之源码调试'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab945eba01d54fbd9d150a77ce00bfd2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 22:14:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab945eba01d54fbd9d150a77ce00bfd2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近做链路追踪，然后在<code>WebScoket</code>的拦截器里面加了追踪ID，但是发现出现了数据错乱，A用户的信息出现在了B用户的会话里。于是开始解刨一下源码，看看到底问题出在哪里了。</p>
<h2 data-id="heading-0">背景</h2>
<p>在项目中，我们使用了<code>spring-boot-starter-websocket</code>做<code>websocket</code>通信服务。在<code>ShakeHandler</code>的实现类的<code>determineUser</code>中读取了用户的身份信息，同时我们创建了一个链路的<code>traceId</code>用作链路追踪，我们把<code>traceId</code>保存在了本地线程（<code>ThreadLocal</code>）中。</p>
<p>然后我们就很自然的在<code>TextWebSocketHandler</code>实现类中随意的使用了<code>ThreadLocal</code>中的<code>traceId</code>做处理。这些例子在<code>afterConnectionEstablished</code>接口、<code>afterConnectionClosed</code>接口、<code>handleMessage</code>接口随处可见。</p>
<p>在测试环境中，同一时间几乎没有并发的情况下，完全看不出来有什么问题，然后最后在没有压测的情况下我们上线了这一功能。</p>
<p>Oh my god!</p>
<p>上线后，很快就出现了数据错乱的情况。比如，A用户的<code>traceId</code>出现在了B用户的请求链路上。因为之前也处理过类似的情况，只不过是<code>Feign</code>相关的多线程问题。没想到在<code>WebSocket</code>上我们又沦陷了。所以，第一反应就是多线程的问题。</p>
<p>立马，我们转到测试环境，开始跑了100的并发，果然问题复现了。</p>
<h2 data-id="heading-1">分析</h2>
<p>那么，我们开始处理这个多线程问题吧。老规矩，先打印线程ID看看是不是真的复用了线程：</p>
<p>我们分别在<code>afterConnectionEstablished</code>、<code>afterConnectionClosed</code>、<code>handleTextMessage</code>中第一行打印线程日志</p>
<pre><code class="copyable"> @Override
  public void afterConnectionEstablished(WebSocketSession session) throws Exception &#123;
    log.info(
        "Thead afterConnectionEstablished &#123;&#125; -> &#123;&#125;",
        session.getId(),
        Thread.currentThread().getId());
  &#125;

  @Override
  public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception &#123;
    log.info(
        "Thead afterConnectionClosed &#123;&#125; -> &#123;&#125;", session.getId(), Thread.currentThread().getId());
  &#125;

  @Override
  protected void handleTextMessage(WebSocketSession session, TextMessage message) &#123;
    log.info("Thead handleTextMessage &#123;&#125; -> &#123;&#125;", session.getId(), Thread.currentThread().getId());
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后用<code>jemeter</code>跑压测脚本，果然出现了同一个线程ID（103）在多次出现，而且还出现了不同的<code>session</code>会话中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab945eba01d54fbd9d150a77ce00bfd2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f26a9a6a76ab4c07a96599a06ea6bf84~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么，很自然的想到，这应该是<code>tomcat</code>的多线程处理请求产生的。解决办法当然很简单，就是将<code>traceId</code>存放在<code>session.attributes</code>中，因为<code>session</code>内容不会变，然后在每一个<code>websocket</code>事件处理接口时先重置<code>traceId</code>为<code>session</code>中保存的值，然后再处理业务逻辑。</p>
<h2 data-id="heading-2">从源码验证</h2>
<p>这里我贴一下我们的<code>jemeter</code>测试脚本。目标是执行一次连接和发一次消息，最后断开，<code>jemeter</code>脚本如下图，使用<code>JMeterWebSocketSamplers-1.2.8.jar</code>插件（<a href="https://juejin.cn/post/undefined">安装教程</a>），分别打开一个<code>WebSocket Open Connection</code> + 固定延时 + <code>WebSocket Single Write Sampler</code> + <code>WebSocket Close</code>：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e1d45a3f49a48b0b0b9389098cf33f4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>分别说明几个脚本：</p>
<ul>
<li><code>WebSocket Open Connection</code> 用于开启一个websocket连接</li>
<li><code>固定延时</code> 延时是为了模拟连接后的消息推送，为了测试线程的复用，可以在这里配置<code>10ms</code>即可，不要超过后面做线程并发时的总时长</li>
<li><code>WebSocket Single Write Sampler</code> 模拟消息推送，<code>connection</code>选择<code>using exists connection</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce1ba4f73154d7da8452fe7a2b71810~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>WebSocket Close</code> 断开<code>websocket</code>连接</li>
</ul>
<p>配置好了测试脚本，立即以<code>程数=1</code>执行，后台输出日志：</p>
<pre><code class="copyable">INFO  c.f.l.w.h.a.AppBaseMessageHandler Thead afterConnectionEstablished fca7eba3-c5e2-a05e-73ed-08d144a021a9 -> 100
INFO  c.f.l.w.h.a.AppBaseMessageHandler Thead handleTextMessage fca7eba3-c5e2-a05e-73ed-08d144a021a9 -> 104
INFO  c.f.l.w.h.a.AppBaseMessageHandler Thead afterConnectionClosed fca7eba3-c5e2-a05e-73ed-08d144a021a9 -> 103
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，在连接、发送消息、断开连接这三个处理，后台使用了三个不同的线程。</p>
<p>那么线程来自哪儿，我们断点（例如断点放在<code>afterConnectionClosed</code>函数中）查看一下线程堆栈</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bec8031e27c14817b5127b7f106e2418~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到<code>afterConnectionClosed</code>所在的线程（ID=103）实际上来自于<code>http-nio-8840-exec-2</code>这个线程池，那么这个线程池是怎么来的呢？实际上<code>http-nio-xx</code>这是我们的<code>tomcat</code>的<code>NioEndpoint</code>维护的线程池。</p>
<pre><code class="copyable">class NioEndpoint extends AbstractJsseEndpoint<NioChannel,SocketChannel>  &#123;    
    @Override
    public void startInternal() throws Exception &#123;

        if (!running) &#123;
            running = true;
            paused = false;

            ...

            // Create worker collection
            if (getExecutor() == null) &#123;
                createExecutor();  // 这里创建了线程池
            &#125;

            ...
        &#125;
    &#125;
        
    ...
&#125;

class AbstractEndpoint &#123;

    // 我们再来看一下创建这个线程池的实现： 
    public void createExecutor() &#123;
        internalExecutor = true;
        TaskQueue taskqueue = new TaskQueue();
        TaskThreadFactory tf = new TaskThreadFactory(getName() + "-exec-", daemon, getThreadPriority());
        executor = new ThreadPoolExecutor(getMinSpareThreads(), getMaxThreads(), 60, TimeUnit.SECONDS,taskqueue, tf); // 这里就是我们进入`afterConnectionClosed`的线程来源
        taskqueue.setParent( (ThreadPoolExecutor) executor);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>NioEndpoint</code>是干什么的？<code>NioEndpoint</code>是<code>tomcat</code>用于处理<code>socket</code>通信的接口类，所有访问<code>tomcat</code>的请求都会由<code>NioEndpoint</code>处理，并启用一个独立线程（来自线程池中的），然后交给不同的<code>RequestHandler</code>处理，最后才会走到我们的<code>afterConnectionClosed</code>等接口上。具体原理可以查询<code>tomcat</code>相关知识，这里不详细介绍了。</p>
<p>这里有一个重点的点，就是<code>tomcat</code>会通过<code>Poller</code>调用<code>AbstractEndpoint</code>的<code>processSocket</code>来处理消息事件，那么我们看一下代码：</p>
<pre><code class="copyable">public boolean processSocket(SocketWrapperBase<S> socketWrapper,
            SocketEvent event, boolean dispatch) &#123;
        try &#123;
            if (socketWrapper == null) &#123;
                return false;
            &#125;
            SocketProcessorBase<S> sc = null;  // Runnable执行单元，也就是我们的worker
            if (processorCache != null) &#123;
                sc = processorCache.pop();
            &#125;
            if (sc == null) &#123;
                sc = createSocketProcessor(socketWrapper, event); // 没有worker缓存，新建一个worker
            &#125; else &#123;
                sc.reset(socketWrapper, event); // 重置worker的相关信息！！！
            &#125;
            Executor executor = getExecutor();
            if (dispatch && executor != null) &#123;  
                executor.execute(sc);  // 调用线程池执行worker的run方法
            &#125; else &#123;
                sc.run();
            &#125;
        &#125; catch (RejectedExecutionException ree) &#123;
            getLog().warn(sm.getString("endpoint.executor.fail", socketWrapper) , ree);
            return false;
        &#125; catch (Throwable t) &#123;
            ExceptionUtils.handleThrowable(t);
            // This means we got an OOM or similar creating a thread, or that
            // the pool and its queue are full
            getLog().error(sm.getString("endpoint.process.fail"), t);
            return false;
        &#125;
        return true;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，从源码上看，我们很清楚的知道，最终处理我们的<code>websocket</code>的线程在线程池中可能是会复用的，也就是我们的<code>SocketProcessorBase</code>工作单元，只是每次执行任务时都会重置<code>socket</code>相关信息。</p>
<p>那么，如果我们在可能被复用的线程（也就是<code>coreThreads</code>）上保存了一些个线程信息（放在<code>ThreadLocal</code>中），如果不做好及时重置，就会出现数据错乱的现象了。</p>
<p>归根到底还是在使用本地线程变量的时候没有重点考虑<code>tomcat</code>的多线程复用问题。</p></div>  
</div>
            