
---
title: '高性能消息中间件 NSQ 解析-nsqlookupd 实现细节介绍'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00e13f9a7d064ba4bc104a2da5e6a7c6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 08:36:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00e13f9a7d064ba4bc104a2da5e6a7c6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我们在 <a href="http://blueskykong.com/2021/03/14/nsq-2/" target="_blank" rel="nofollow noopener noreferrer">前面</a> 介绍了 nsq 的相关概念以及 nsq 的安装与应用以及 nsqd 的实现原理。从本篇将会结合源码介绍 nsqlookupd 的实现细节。</p>
<p>nsqlookupd 主要流程与上一篇文章介绍的 nsqd 执行逻辑相似，区别在于具体运行的任务不同。</p>
<h4 data-id="heading-0">入口函数</h4>
<p>在 nsq/apps/nsqlookupd/main.go 可以找到执行入口文件。</p>
<pre><code class="copyable">// 位于apps/nsqlookupd/main.go:45
func main() &#123;
  prg := &program&#123;&#125;
  if err := svc.Run(prg, syscall.SIGINT, syscall.SIGTERM); err != nil &#123;
    logFatal("%s", err)
  &#125;
&#125;

func (p *program) Init(env svc.Environment) error &#123;
  if env.IsWindowsService() &#123;
    dir := filepath.Dir(os.Args[0])
    return os.Chdir(dir)
  &#125;
  return nil
&#125;

func (p *program) Start() error &#123;
  opts := nsqlookupd.NewOptions()

  flagSet := nsqlookupdFlagSet(opts)
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样，通过第三方 svc 包进行优雅的后台进程管理，svc.Run() -> svc.Init() -> svc.Start()，启动 nsqlookupd 实例。</p>
<pre><code class="copyable">// 位于 apps/nsqlookupd/main.go:80
options.Resolve(opts, flagSet, cfg)
  nsqlookupd, err := nsqlookupd.New(opts)
  if err != nil &#123;
    logFatal("failed to instantiate nsqlookupd", err)
  &#125;
  p.nsqlookupd = nsqlookupd

  go func() &#123;
    err := p.nsqlookupd.Main()
    if err != nil &#123;
      p.Stop()
      os.Exit(1)
    &#125;
  &#125;()

<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化配置参数(优先级：flagSet-命令行参数 > cfg-配置文件 > opts-默认值)，开启协程，进入 nsqlookupd.Main() 主函数。</p>
<h4 data-id="heading-1">监听请求</h4>
<p>我们来看下 nsqlookupd 是如何监听请求的，代码实现如下：</p>
<pre><code class="copyable">// 位于 nsqlookupd/nsqlookupd.go:53
func (l *NSQLookupd) Main() error &#123;
  ctx := &Context&#123;l&#125;

  exitCh := make(chan error)
  var once sync.Once
  exitFunc := func(err error) &#123;
    once.Do(func() &#123;
      if err != nil &#123;
        l.logf(LOG_FATAL, "%s", err)
      &#125;
      exitCh <- err
    &#125;)
  &#125;

  tcpServer := &tcpServer&#123;ctx: ctx&#125;
  l.waitGroup.Wrap(func() &#123;
    exitFunc(protocol.TCPServer(l.tcpListener, tcpServer, l.logf))
  &#125;)
  httpServer := newHTTPServer(ctx)
  l.waitGroup.Wrap(func() &#123;
    exitFunc(http_api.Serve(l.httpListener, httpServer, "HTTP", l.logf))
  &#125;)

  err := <-exitCh
  return err
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开启 goroutine 执行 tcpServer, httpServer，分别监听 nsqd, nsqadmin 的客户端请求。</p>
<h4 data-id="heading-2">处理请求</h4>
<pre><code class="copyable">// 位于 internal/protocol/tcp_server.go:17
func TCPServer(listener net.Listener, handler TCPHandler, logf lg.AppLogFunc) error &#123;
  logf(lg.INFO, "TCP: listening on %s", listener.Addr())

  for &#123;
    clientConn, err := listener.Accept()
    if err != nil &#123;
      if nerr, ok := err.(net.Error); ok && nerr.Temporary() &#123;
        logf(lg.WARN, "temporary Accept() failure - %s", err)
        runtime.Gosched()
        continue
      &#125;
      // theres no direct way to detect this error because it is not exposed
      if !strings.Contains(err.Error(), "use of closed network connection") &#123;
        return fmt.Errorf("listener.Accept() error - %s", err)
      &#125;
      break
    &#125;
    go handler.Handle(clientConn)
  &#125;

  logf(lg.INFO, "TCP: closing %s", listener.Addr())

  return nil
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>TCPServer 循环监听客户端请求，建立长连接进行通信，并开启 handler 处理每一个客户端 conn。</p>
<h4 data-id="heading-3">装饰 http 路由</h4>
<p>httpServer 通过 http_api.Decorate 装饰器实现对各 http 路由进行 handler 装饰，如加 log 日志、V1 协议版本号的统一格式输出等；</p>
<pre><code class="copyable">func newHTTPServer(ctx *Context) *httpServer &#123;
  log := http_api.Log(ctx.nsqlookupd.logf)

  router := httprouter.New()
  router.HandleMethodNotAllowed = true
  router.PanicHandler = http_api.LogPanicHandler(ctx.nsqlookupd.logf)
  router.NotFound = http_api.LogNotFoundHandler(ctx.nsqlookupd.logf)
  router.MethodNotAllowed = http_api.LogMethodNotAllowedHandler(ctx.nsqlookupd.logf)
  s := &httpServer&#123;
    ctx:    ctx,
    router: router,
  &#125;

  router.Handle("GET", "/ping", http_api.Decorate(s.pingHandler, log, http_api.PlainText))
  router.Handle("GET", "/info", http_api.Decorate(s.doInfo, log, http_api.V1))

  // v1 negotiate
  router.Handle("GET", "/debug", http_api.Decorate(s.doDebug, log, http_api.V1))
  router.Handle("GET", "/lookup", http_api.Decorate(s.doLookup, log, http_api.V1))
  router.Handle("GET", "/topics", http_api.Decorate(s.doTopics, log, http_api.V1))
  router.Handle("GET", "/channels", http_api.Decorate(s.doChannels, log, http_api.V1))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">处理客户端命令</h4>
<p>tcp 解析 V1 协议，内部协议封装的 prot.IOLoop(conn) 进行循环处理客户端命令，直到客户端命令全部解析处理完毕才关闭连接。</p>
<pre><code class="copyable">var prot protocol.Protocol
  switch protocolMagic &#123;
  case "  V1":
    prot = &LookupProtocolV1&#123;ctx: p.ctx&#125;
  default:
    protocol.SendResponse(clientConn, []byte("E_BAD_PROTOCOL"))
    clientConn.Close()
    p.ctx.nsqlookupd.logf(LOG_ERROR, "client(%s) bad protocol magic '%s'",
      clientConn.RemoteAddr(), protocolMagic)
    return
  &#125;

  err = prot.IOLoop(clientConn)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">执行命令</h4>
<p>通过内部协议进行 p.Exec(执行命令)、p.SendResponse(返回结果)，保证每个 nsqd 节点都能正确的进行服务注册(register)与注销(unregister)，并进行心跳检测(ping)节点的可用性，确保客户端取到的 nsqd 节点列表都是最新可用的。</p>
<pre><code class="copyable">for &#123;
    line, err = reader.ReadString('\n')
    if err != nil &#123;
      break
    &#125;

    line = strings.TrimSpace(line)
    params := strings.Split(line, " ")

    var response []byte
    response, err = p.Exec(client, reader, params)
    if err != nil &#123;
      ctx := ""
      if parentErr := err.(protocol.ChildErr).Parent(); parentErr != nil &#123;
        ctx = " - " + parentErr.Error()
      &#125;
      _, sendErr := protocol.SendResponse(client, []byte(err.Error()))
      if sendErr != nil &#123;
        p.ctx.nsqlookupd.logf(LOG_ERROR, "[%s] - %s%s", client, sendErr, ctx)
        break
      &#125;
      continue
    &#125;

    if response != nil &#123;
      _, err = protocol.SendResponse(client, response)
      if err != nil &#123;
        break
      &#125;
    &#125;
  &#125;

  conn.Close()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>nsqlookupd 服务同时开启 tcp 和 http 两个监听服务，nsqd 会作为客户端，连上 nsqlookupd 的 tcp 服务，并上报自己的 topic 和 channel 信息，以及通过心跳机制判断 nsqd 状态；还有个 http 服务提供给 nsqadmin 获取集群信息。</p>
<h3 data-id="heading-6">小结</h3>
<p>本文主要介绍 nsqlookupd 的实现，nsqlookupd 同样是一个守护进程，负责管理拓扑信息。客户端通过查询 nsqlookupd 来发现指定话题（ topic ）的生产者，并且 nsqd 节点广播话题（topic）和通道（ channel ）信息。有两个接口： TCP 接口， nsqd 用它来广播。 HTTP 接口，客户端用它来发现和管理。</p>
<p>下一篇文章，将会继续介绍 nsq 中其他模块实现的细节。</p>
<h4 data-id="heading-7">推荐阅读</h4>
<p><a href="http://blueskykong.com/2021/03/25/nsq-3/" target="_blank" rel="nofollow noopener noreferrer">高性能消息中间件 NSQ 解析-nsqd 实现细节介绍</a></p>
<p><a href="http://blueskykong.com/2021/03/03/nsq-1/" target="_blank" rel="nofollow noopener noreferrer">高性能消息中间件 NSQ 解析-整体介绍</a></p>
<p><a href="http://blueskykong.com/2021/03/14/nsq-2/" target="_blank" rel="nofollow noopener noreferrer">高性能消息中间件 NSQ 解析-应用实践</a></p>
<p><a href="http://blueskykong.com/2020/11/03/elkb/" target="_blank" rel="nofollow noopener noreferrer">微服务架构中使用 ELK 进行日志采集以及统一处理</a></p>
<p><a href="http://blueskykong.com/2020/12/16/go-errors/" target="_blank" rel="nofollow noopener noreferrer">没有 try-catch，该如何处理 Go 错误异常？</a></p>
<h4 data-id="heading-8">订阅最新文章，欢迎关注我的公众号</h4>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00e13f9a7d064ba4bc104a2da5e6a7c6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            