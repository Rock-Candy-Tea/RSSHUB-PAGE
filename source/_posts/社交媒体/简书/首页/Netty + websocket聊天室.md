
---
title: 'Netty + websocket聊天室'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/5653258-81f119e44b2c3d8e.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/5653258-81f119e44b2c3d8e.png'
---

<div>   
<h1>Netty + websocket聊天室</h1>
<h2>程序处理逻辑</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="980" data-height="749"><img data-original-src="//upload-images.jianshu.io/upload_images/5653258-81f119e44b2c3d8e.png" data-original-width="980" data-original-height="749" data-original-format="image/png" data-original-filesize="81996" src="https://upload-images.jianshu.io/upload_images/5653258-81f119e44b2c3d8e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">图1.png</div>
</div>
<h2>启用websocket</h2>
<p>从标准的HTTP或者HTTPS协议切换到WebSocket时，将会使用一种称为升级握手的机制。因此，使用WebSocket的应用程序将始终以HTTP/S作为开始，然后再执行升级。这个升级动作发生的确切时刻特定于应用程序；它可能会发生在启动时，也可能会发生在请求了某个特定的URL之后</p>
<p>约定：</p>
<ul>
<li><p>如果被请求的 URL 以/ws 结尾，那么我们将会把该协议升级为 WebSocket；</p></li>
<li><p>否则，服务器将使用基本的 HTTP/S</p></li>
</ul>
<p>服务器逻辑:</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1057" data-height="746"><img data-original-src="//upload-images.jianshu.io/upload_images/5653258-f05a84f0f44d2c33.png" data-original-width="1057" data-original-height="746" data-original-format="image/png" data-original-filesize="108158" src="https://upload-images.jianshu.io/upload_images/5653258-f05a84f0f44d2c33.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">图2.png</div>
</div>
<h3>处理http请求以及websocket</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1289" data-height="651"><img data-original-src="//upload-images.jianshu.io/upload_images/5653258-38b0def3abf7e80e.png" data-original-width="1289" data-original-height="651" data-original-format="image/png" data-original-filesize="82765" src="https://upload-images.jianshu.io/upload_images/5653258-38b0def3abf7e80e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">图3.png</div>
</div>
<pre><code class="Java">
//扩展 SimpleChannel-InboundHandler 以处理FullHttpRequest 消息
public class HttpRequestHandler extends SimpleChannelInboundHandler<FullHttpRequest> &#123;

    private final String wsUri;
    private static final File INDEX;

    static &#123;
        URL location = HttpRequestHandler.class.getProtectionDomain().getCodeSource().getLocation();
        try &#123;
            String path = location.toURI() + "index.html";
            path = !path.contains("file:") ? path : path.substring(5);
            INDEX = new File(path);
        &#125; catch (URISyntaxException e) &#123;
            throw new IllegalStateException("Unable to locate WebsocketChatClient.html", e);
        &#125;
    &#125;

    public HttpRequestHandler(String wsUri) &#123;
        this.wsUri = wsUri;
    &#125;

    @Override
    public void channelRead0(ChannelHandlerContext ctx, FullHttpRequest request) throws Exception &#123;

        if (wsUri.equalsIgnoreCase(request.uri())) &#123;//如果请求了 WebSocket协议升级，则增加引用 计数（调用retain()方法），并将它传递给下一个ChannelInboundHandler
            ctx.fireChannelRead(request.retain()); //
        &#125; else &#123;
            if (HttpUtil.is100ContinueExpected(request)) &#123;//处理 100 Continue请求以符合 HTTP 1.1 规范
                send100Continue(ctx); //
            &#125;

            RandomAccessFile file = new RandomAccessFile(INDEX, "r");//

            HttpResponse response = new DefaultHttpResponse(request.protocolVersion(), HttpResponseStatus.OK);
            response.headers().set(HttpHeaderNames.CONTENT_TYPE, "text/html; charset=UTF-8");

            boolean keepAlive = HttpUtil.isKeepAlive(request);

            if (keepAlive) &#123; //如果请求了keep-alive，则添加所需要的HTTP 头信息
                response.headers().set(HttpHeaderNames.CONTENT_LENGTH, file.length());
                response.headers().set(HttpHeaderNames.CONNECTION, HttpHeaderValues.KEEP_ALIVE);
            &#125;
            ctx.write(response); //将 HttpResponse写到客户端

            if (ctx.pipeline().get(SslHandler.class) == null) &#123; //将 index.html写到客户端
                ctx.write(new DefaultFileRegion(file.getChannel(), 0, file.length()));
            &#125; else &#123;
                ctx.write(new ChunkedNioFile(file.getChannel()));
            &#125;
            ChannelFuture future = ctx.writeAndFlush(LastHttpContent.EMPTY_LAST_CONTENT);//写LastHttpContent并冲刷至客户端
            if (!keepAlive) &#123;//如果没有请求keep-alive，则在写操作完成后关闭 Channel
                future.addListener(ChannelFutureListener.CLOSE); //
            &#125;

            file.close();
        &#125;
    &#125;

    private static void send100Continue(ChannelHandlerContext ctx) &#123;
        FullHttpResponse response = new DefaultFullHttpResponse(HttpVersion.HTTP_1_1, HttpResponseStatus.CONTINUE);
        ctx.writeAndFlush(response);
    &#125;

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception &#123;
        Channel incoming = ctx.channel();
        System.out.println("Client:" + incoming.remoteAddress() + "异常");
        // 当出现异常就关闭连接
        cause.printStackTrace();
        ctx.close();
    &#125;
&#125;



</code></pre>
<pre><code class="Java">
public class TextWebSocketFrameHandler extends SimpleChannelInboundHandler<TextWebSocketFrame> &#123;


    public static ChannelGroup channels = new DefaultChannelGroup(GlobalEventExecutor.INSTANCE);

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, TextWebSocketFrame msg) throws Exception &#123; // 
        Channel incoming = ctx.channel();
        for (Channel channel : channels) &#123;
            if (channel != incoming) &#123;
                channel.writeAndFlush(new TextWebSocketFrame("[" + incoming.remoteAddress() + "]" + msg.text()));
            &#125; else &#123;
                channel.writeAndFlush(new TextWebSocketFrame("[you]" + msg.text()));
            &#125;
        &#125;
    &#125;

    @Override
    public void handlerAdded(ChannelHandlerContext ctx) throws Exception &#123; // 
        Channel incoming = ctx.channel();

        // 广播
        channels.writeAndFlush(new TextWebSocketFrame("[SERVER] - " + incoming.remoteAddress() + " 加入"));

        channels.add(incoming);
        System.out.println("Client:" + incoming.remoteAddress() + "加入");
    &#125;

    @Override
    public void handlerRemoved(ChannelHandlerContext ctx) throws Exception &#123; // 
        Channel incoming = ctx.channel();

        // 广播
        channels.writeAndFlush(new TextWebSocketFrame("[SERVER] - " + incoming.remoteAddress() + " 离开"));

        System.out.println("Client:" + incoming.remoteAddress() + "离开");
    &#125;

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception &#123; // 
        Channel incoming = ctx.channel();
        System.out.println("Client:" + incoming.remoteAddress() + "在线");
    &#125;

    @Override
    public void channelInactive(ChannelHandlerContext ctx) throws Exception &#123; // 
        Channel incoming = ctx.channel();
        System.out.println("Client:" + incoming.remoteAddress() + "掉线");
    &#125;

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) // 
            throws Exception &#123;
        Channel incoming = ctx.channel();
        System.out.println("Client:" + incoming.remoteAddress() + "异常");
        // 当出现异常就关闭连接
        cause.printStackTrace();
        ctx.close();
    &#125;


&#125;


</code></pre>
<pre><code class="Java">public class WebSocketChatServerInitializer extends ChannelInitializer<SocketChannel> &#123;


    @Override
    public void initChannel(SocketChannel ch) throws Exception &#123;//（2）
        ChannelPipeline pipeline = ch.pipeline();

        pipeline.addLast(new HttpServerCodec());
        pipeline.addLast(new HttpObjectAggregator(64*1024));
        pipeline.addLast(new ChunkedWriteHandler());
        pipeline.addLast(new HttpRequestHandler("/ws"));
        pipeline.addLast(new WebSocketServerProtocolHandler("/ws"));
        pipeline.addLast(new TextWebSocketFrameHandler());

    &#125;
&#125;


</code></pre>
<h2>Netty文档</h2>
<h4>ChannelGroup</h4>
<p>线程安全的Set，包含开放的Channel，并在其上提供各种批量操作。 使用ChannelGroup，您可以将Channels划分为有意义的组（例如，基于每个服务或每个状态）。一个封闭的Channels会自动从集合中删除，因此您不必担心它的生命周期。 添加频道。 一个Channel可以属于多个ChannelGroup。</p>
<h3>将消息广播到多个频道</h3>
<p>如果需要将消息广播到多个频道，则可以添加与收件人关联的频道并调用write（Object）：</p>
<pre><code class="Java"> ChannelGroup recipients =
         new DefaultChannelGroup(GlobalEventExecutor.INSTANCE);
 recipients.add(channelA);
 recipients.add(channelB);
 ..
 recipients.write(Unpooled.copiedBuffer(
         "Service will shut down for maintenance in 5 minutes.",
         CharsetUtil.UTF_8));

</code></pre>
<p>使用ChannelGroup简化关机过程</p>
<p>如果ServerChannels和非ServerChannels都存在于同一ChannelGroup中，则首先对ServerChannels执行此组上所有请求的I / O操作，然后对其他Channels执行。</p>
<p>一次关闭服务器时，此规则非常有用：</p>
<pre><code class="Java"> ChannelGroup allChannels =
         new DefaultChannelGroup(GlobalEventExecutor.INSTANCE);

 public static void main(String[] args) throws Exception &#123;
     ServerBootstrap b = new ServerBootstrap(..);
     ...
     b.childHandler(new MyHandler());

     // Start the server
     b.getPipeline().addLast("handler", new MyHandler());
     Channel serverChannel = b.bind(..).sync();
     allChannels.add(serverChannel);

     ... Wait until the shutdown signal reception ...

     // Close the serverChannel and then all accepted connections.
     allChannels.close().awaitUninterruptibly();
 &#125;

 public class MyHandler extends ChannelInboundHandlerAdapter &#123;
      @Override
     public void channelActive(ChannelHandlerContext ctx) &#123;
         // closed on shutdown.
         allChannels.add(ctx.channel());
         super.channelActive(ctx);
     &#125;
 &#125;

</code></pre>
<h2>参考</h2>
<p><< Netty实战 >></p>
  
</div>
            