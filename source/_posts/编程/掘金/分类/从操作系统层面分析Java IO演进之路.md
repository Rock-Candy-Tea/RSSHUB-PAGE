
---
title: '从操作系统层面分析Java IO演进之路'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6fd04698f324521bcdbb5620f1cdccc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 18:25:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6fd04698f324521bcdbb5620f1cdccc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> 本文从操作系统实际调用角度（以CentOS Linux release 7.5操作系统为示例），力求追根溯源看IO的每一步操作到底发生了什么。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6fd04698f324521bcdbb5620f1cdccc~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作者 | 道坚<br>
来源 | 阿里技术公众号</p>
<h3 data-id="heading-0">前言</h3>
<p>本文从操作系统实际调用角度（以CentOS Linux release 7.5操作系统为示例），力求追根溯源看IO的每一步操作到底发生了什么。</p>
<p>关于如何查看系统调用，Linux可以使用 strace 来查看任何软件的系统调动（这是个很好的分析学习方法）：strace -ff -o ./out java TestJava</p>
<h3 data-id="heading-1">一 BIO</h3>
<pre><code class="copyable">/**
 * Alipay.com Inc. Copyright (c) 2004-2020 All Rights Reserved.
 */
package io; 

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author xiangyong.ding
 * @version $Id: TestSocket.java, v 0.1 2020年08月02日 20:56 xiangyong.ding Exp $
 */
public class BIOSocket &#123;
    public static void main(String[] args) throws IOException &#123;
        ServerSocket serverSocket = new ServerSocket(8090);
        System.out.println("step1: new ServerSocket ");
        while (true) &#123;
            Socket client = serverSocket.accept();
            System.out.println("step2: client\t" + client.getPort());
            new Thread(() -> &#123;
                try &#123;
                    InputStream in = client.getInputStream();
                    BufferedReader reader = new BufferedReader(new InputStreamReader(in));
                    while (true) &#123;
                        System.out.println(reader.readLine());
                    &#125;
                &#125; catch (IOException e) &#123;
                    e.printStackTrace();
                &#125;
            &#125;).start();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">1 发生的系统调用</h4>
<p><strong>启动时</strong></p>
<pre><code class="copyable">socket(AF_INET, SOCK_STREAM, IPPROTO_IP) = 5
bind(5, &#123;sa_family=AF_INET, sin_port=htons(8090), sin_addr=inet_addr("0.0.0.0")&#125;, 16) = 0
listen(5, 50)                           = 0
poll([&#123;fd=5, events=POLLIN|POLLERR&#125;], 1, -1) = 1 ([&#123;fd=5, revents=POLLIN&#125;])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>poll函数会阻塞直到其中任何一个fd发生事件。</p>
<p><strong>有客户端连接后</strong></p>
<pre><code class="copyable">accept(5, &#123;sa_family=AF_INET, sin_port=htons(10253), sin_addr=inet_addr("42.120.74.252")&#125;, [16]) = 6
clone(child_stack=0x7f013e5c4fb0, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7f013e5c59d0,         tls=0x7f013e5c5700, child_tidptr=0x7f013e5c59d0) = 13168
poll([&#123;fd=5, events=POLLIN|POLLERR&#125;], 1, -1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>抛出线程（即我们代码里的 new Thread() ）后，继续poll阻塞等待连接。</p>
<p><strong>clone出来的线程</strong></p>
<pre><code class="copyable">recvfrom(6, "hello,bio\n", 8192, 0, NULL, NULL) =
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于对recvfrom函数的说明，其中第四个参数0 表示这是一个阻塞调用。</p>
<p><strong>客户端发送数据后</strong></p>
<pre><code class="copyable">recvfrom(6, "hello,bio\n", 8192, 0, NULL, NULL) = 10
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2 优缺点</h4>
<p><strong>优点</strong></p>
<p>代码简单，逻辑清晰。</p>
<p><strong>缺点</strong></p>
<ul>
<li>由于stream的read操作是阻塞读，面对多个连接时 每个连接需要每线程。无法处理大量连接（C10K问题）。</li>
<li>误区：可见JDK1.8中对于最初的BIO，在Linux OS下仍然使用的poll，poll本身也是相对比较高效的多路复用函数（支持非阻塞、多个socket同时检查event），只是限于JDK最初的stream API限制，无法支持非阻塞读取。</li>
</ul>
<h3 data-id="heading-4">二 NIO（non block）</h3>
<p>改进：使用NIO API，将阻塞变为非阻塞， 不需要大量线程。</p>
<pre><code class="copyable">/**
 * Alipay.com Inc. Copyright (c) 2004-2020 All Rights Reserved.
 */
package io;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;
import java.util.LinkedList;

/**
 * @author xiangyong.ding
 * @version $Id: NioSocket.java, v 0.1 2020年08月09日 11:25 xiangyong.ding Exp $
 */
public class NIOSocket &#123;
    private static LinkedList< SocketChannel> clients = new LinkedList<>();

    private static void startClientChannelHandleThread()&#123;
        new Thread(() -> &#123;
            while (true)&#123;
                ByteBuffer buffer = ByteBuffer.allocateDirect(4096);

                //处理客户端连接
                for (SocketChannel c : clients) &#123;
                    // 非阻塞, >0 表示读取到的字节数量, 0或-1表示未读取到或读取异常
                    int num = 0;
                    try &#123;
                        num = c.read(buffer);
                    &#125; catch (IOException e) &#123;
                        e.printStackTrace();
                    &#125;

                    if (num > 0) &#123;
                        buffer.flip();
                        byte[] clientBytes = new byte[buffer.limit()];
                        //从缓冲区 读取到内存中
                        buffer.get(clientBytes);

                        System.out.println(c.socket().getPort() + ":" + new String(clientBytes));

                        //清空缓冲区
                        buffer.clear();
                    &#125;
                &#125;
            &#125;
        &#125;).start();
    &#125;

    public static void main(String[] args) throws IOException &#123;
        //new socket,开启监听
        ServerSocketChannel socketChannel = ServerSocketChannel.open();
        socketChannel.bind(new InetSocketAddress(9090));
        //设置阻塞接受客户端连接
        socketChannel.configureBlocking(true);

        //开始client处理线程
        startClientChannelHandleThread();

        while (true) &#123;
            //接受客户端连接; 非阻塞，无客户端返回null(操作系统返回-1)
            SocketChannel client = socketChannel.accept();

            if (client == null) &#123;
                //System.out.println("no client");
            &#125; else &#123;
                //设置读非阻塞
                client.configureBlocking(false);

                int port = client.socket().getPort();
                System.out.println("client port :" + port);

                clients.add(client);
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">1 发生的系统调用</h4>
<p><strong>主线程</strong></p>
<pre><code class="copyable">socket(AF_INET, SOCK_STREAM, IPPROTO_IP) = 4
bind(4, &#123;sa_family=AF_INET, sin_port=htons(9090), sin_addr=inet_addr("0.0.0.0")&#125;, 16) = 0
listen(4, 50)                           = 0
fcntl(4, F_SETFL, O_RDWR|O_NONBLOCK)    = 0
accept(4, 0x7fe26414e680, 0x7fe26c376710) = -1 EAGAIN (Resource temporarily unavailable)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>有连接后，子线程</strong></p>
<pre><code class="copyable">read(6, 0x7f3f415b1c50, 4096)           = -1 EAGAIN (Resource temporarily unavailable)
read(6, 0x7f3f415b1c50, 4096)           = -1 EAGAIN (Resource temporarily unavailable)
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>资源使用情况：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08cb74839e784f4d816d5694b3e9d380~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">2 优缺点</h4>
<p><strong>优点</strong></p>
<p>线程数大大减少。</p>
<p><strong>缺点</strong></p>
<p>需要程序自己扫描 每个连接read，需要 O(n)时间复杂度系统调用 （此时可能只有一个连接发送了数据），高频系统调用（导致CPU 用户态内核态切换）高。导致CPU消耗很高。</p>
<h3 data-id="heading-7">三 多路复用器（select、poll、epoll）</h3>
<p>改进：不需要用户扫描所有连接，由kernel 给出哪些连接有数据，然后应用从有数据的连接读取数据。</p>
<h4 data-id="heading-8">1 epoll</h4>
<pre><code class="copyable">import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Set;

/**
 * 多路复用socket
 *
 * @author xiangyong.ding
 * @version $Id: MultiplexingSocket.java, v 0.1 2020年08月09日 12:19 xiangyong.ding Exp $
 */
public class MultiplexingSocket &#123;

    static ByteBuffer buffer = ByteBuffer.allocateDirect(4096);

    public static void main(String[] args) throws Exception &#123;

        LinkedList< SocketChannel> clients = new LinkedList<>();

        //1.启动server
        //new socket,开启监听
        ServerSocketChannel socketChannel = ServerSocketChannel.open();
        socketChannel.bind(new InetSocketAddress(9090));
        //设置非阻塞，接受客户端
        socketChannel.configureBlocking(false);

        //多路复用器（JDK包装的代理，select /poll/epoll/kqueue）
        Selector selector = Selector.open(); //java自动代理，默认为epoll
        //Selector selector = PollSelectorProvider.provider().openSelector();//指定为poll

        //将服务端socket 注册到 多路复用器
        socketChannel.register(selector, SelectionKey.OP_ACCEPT);

        //2. 轮训多路复用器
        // 先询问有没有连接,如果有则返回数量以及对应的对象(fd)
        while (selector.select() > 0) &#123;
            System.out.println();
            Set< SelectionKey> selectionKeys = selector.selectedKeys();
            Iterator< SelectionKey> iter = selectionKeys.iterator();

            while (iter.hasNext()) &#123;
                SelectionKey key = iter.next();
                iter.remove();

                //2.1 处理新的连接
                if (key.isAcceptable()) &#123;
                    //接受客户端连接; 非阻塞，无客户端返回null(操作系统返回-1)
                    SocketChannel client = socketChannel.accept();
                    //设置读非阻塞
                    client.configureBlocking(false);

                    //同样，把client也注册到selector
                    client.register(selector, SelectionKey.OP_READ);
                    System.out.println("new client : " + client.getRemoteAddress());
                &#125;
                //2.2 处理读取数据
                else if (key.isReadable()) &#123;
                    readDataFromSocket(key);
                &#125;
            &#125;
        &#125;
    &#125;

    protected static void readDataFromSocket(SelectionKey key) throws Exception &#123;
        SocketChannel socketChannel = (SocketChannel) key.channel();
        // 非阻塞, >0 表示读取到的字节数量, 0或-1表示未读取到或读取异常
        // 请注意：这个例子降低复杂度，不考虑报文大于buffer size的情况
        int num = socketChannel.read(buffer);

        if (num > 0) &#123;
            buffer.flip();
            byte[] clientBytes = new byte[buffer.limit()];
            //从缓冲区 读取到内存中
            buffer.get(clientBytes);

            System.out.println(socketChannel.socket().getPort() + ":" + new String(clientBytes));

            //清空缓冲区
            buffer.clear();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">2 发生的系统调用</h4>
<p><strong>启动</strong></p>
<pre><code class="copyable">socket(AF_INET, SOCK_STREAM, IPPROTO_IP) = 4
bind(4, &#123;sa_family=AF_INET, sin_port=htons(9090), sin_addr=inet_addr("0.0.0.0")&#125;, 16) = 0
listen(4, 50)
fcntl(4, F_SETFL, O_RDWR|O_NONBLOCK)    = 0
epoll_create(256)                       = 7
epoll_ctl(7, EPOLL_CTL_ADD, 5, &#123;EPOLLIN, &#123;u32=5, u64=4324783852322029573&#125;&#125;) = 0
epoll_ctl(7, EPOLL_CTL_ADD, 4, &#123;EPOLLIN, &#123;u32=4, u64=158913789956&#125;&#125;) = 0
epoll_wait(7
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于对epoll_create（对应着Java的 Selector selector = Selector.open()） 的说明，本质上是在内存的操作系统保留区，创建一个epoll数据结构。用于后面当有client连接时，向该epoll区中添加监听。</p>
<p><strong>有连接</strong></p>
<pre><code class="copyable">epoll_wait(7,[&#123;EPOLLIN, &#123;u32=4, u64=158913789956&#125;&#125;], 8192, -1) = 1
accept(4, &#123;sa_family=AF_INET, sin_port=htons(29597), sin_addr=inet_addr("42.120.74.252")&#125;, [16]) = 8
fcntl(8, F_SETFL, O_RDWR|O_NONBLOCK)    = 0
epoll_ctl(7, EPOLL_CTL_ADD, 8, &#123;EPOLLIN, &#123;u32=8, u64=3212844375897800712&#125;&#125;) = 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于epoll_ctl （对应着Java的 client.register(selector, SelectionKey.OP_READ) ）。其中 EPOLLIN 恰好对应着Java的 SelectionKey.OP_READ 即监听数据到达读取事件。</p>
<p><strong>客户端发送数据</strong></p>
<pre><code class="copyable">epoll_wait(7,[&#123;EPOLLIN, &#123;u32=8, u64=3212844375897800712&#125;&#125;], 8192, -1) = 1
read(8, "hello,multiplex\n", 4096)      = 16
epoll_wait(7,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>note：epoll_wait第四个参数-1表示block。</p>
</blockquote>
<p><strong>poll 和 epoll 对比</strong></p>
<p>根据“1.BIO”中的poll函数调用和epoll函数对比如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b45b1f9b4d3a4ae881ee2097c14d88e1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30c6fd3534b64205b5563be90e71cde5~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>poll和epoll本质上都是同步IO， 区别于BIO的是 多路复用充分降低了 system call，而epoll更进一步，再次降低了system call的时间复杂度。</p>
<h4 data-id="heading-10">3 优缺点</h4>
<p><strong>优点</strong></p>
<ul>
<li>线程数同样很少，甚至可以把acceptor线程和worker线程使用同一个。</li>
<li>时间复杂度低，Java实现的Selector（在Linux OS下使用的epoll函数）支持多个clientChannel事件的一次性获取，且时间复杂度维持在O(1)。</li>
<li>CPU使用低：得益于Selector，我们不用向 “2.NIO”中需要自己一个个ClientChannel手动去检查事件，因此使得CPU使用率大大降低。</li>
</ul>
<p><strong>缺点</strong></p>
<ul>
<li>
<p>数据处理麻烦：目前socketChannel.read 读取数据完全是基于字节的，当我们需要需要作为HTTP服务网关时，对于HTTP协议的处理完全需要自己解析，这是个庞大、烦杂、容易出错的工作。</p>
</li>
<li>
<p>性能</p>
<ul>
<li>现有socket数据的读取（socketChannel.read(buffer)）全部通过一个buffer 缓冲区来接受，一旦连接多起来，这无疑是一个单线程读取，性能无疑是个问题。</li>
<li>那么此时buffer我们每次读取都重新new出来呢？如果每次都new出来，这样的内存碎片对于GC无疑是一场灾难。如何平衡地协调好buffer的共享，既保证性能，又保证线程安全，这是个难题。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-11">四 Netty</h3>
<h4 data-id="heading-12">1 研究的目标源码（netty提供的入门example）</h4>
<p><strong>TelnetServer</strong></p>
<pre><code class="copyable">package telnet;

import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.logging.LogLevel;
import io.netty.handler.logging.LoggingHandler;
import io.netty.handler.ssl.SslContext;
import io.netty.handler.ssl.SslContextBuilder;
import io.netty.handler.ssl.util.SelfSignedCertificate;

/**
 * Simplistic telnet server.
 */
public final class TelnetServer &#123;

    static final boolean SSL = System.getProperty("ssl") != null;
    static final int PORT = Integer.parseInt(System.getProperty("port", SSL? "8992" : "8023"));

    public static void main(String[] args) throws Exception &#123;
        // Configure SSL.
        final SslContext sslCtx;
        if (SSL) &#123;
            SelfSignedCertificate ssc = new SelfSignedCertificate();
            sslCtx = SslContextBuilder.forServer(ssc.certificate(), ssc.privateKey()).build();
        &#125; else &#123;
            sslCtx = null;
        &#125;

        EventLoopGroup bossGroup = new NioEventLoopGroup(1);
        EventLoopGroup workerGroup = new NioEventLoopGroup();
        try &#123;
            ServerBootstrap b = new ServerBootstrap();
            b.group(bossGroup, workerGroup)
             .channel(NioServerSocketChannel.class)
             .handler(new LoggingHandler(LogLevel.INFO))
             .childHandler(new TelnetServerInitializer(sslCtx));

            b.bind(PORT).sync().channel().closeFuture().sync();
        &#125; finally &#123;
            bossGroup.shutdownGracefully();
            workerGroup.shutdownGracefully();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>TelnetServerHandler</strong></p>
<p>package telnet;</p>
<pre><code class="copyable">import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelFutureListener;
import io.netty.channel.ChannelHandler.Sharable;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;

import java.net.InetAddress;
import java.util.Date;

/**
 * Handles a server-side channel.
 */
@Sharable
public class TelnetServerHandler extends SimpleChannelInboundHandler< String> &#123;

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception &#123;
        // Send greeting for a new connection.
        ctx.write("Welcome to " + InetAddress.getLocalHost().getHostName() + "!\r\n");
        ctx.write("It is " + new Date() + " now.\r\n");
        ctx.flush();
    &#125;

    @Override
    public void channelRead0(ChannelHandlerContext ctx, String request) throws Exception &#123;
        // Generate and write a response.
        String response;
        boolean close = false;
        if (request.isEmpty()) &#123;
            response = "Please type something.\r\n";
        &#125; else if ("bye".equals(request.toLowerCase())) &#123;
            response = "Have a good day!\r\n";
            close = true;
        &#125; else &#123;
            response = "Did you say '" + request + "'?\r\n";
        &#125;

        // We do not need to write a ChannelBuffer here.
        // We know the encoder inserted at TelnetPipelineFactory will do the conversion.
        ChannelFuture future = ctx.write(response);

        // Close the connection after sending 'Have a good day!'
        // if the client has sent 'bye'.
        if (close) &#123;
            future.addListener(ChannelFutureListener.CLOSE);
        &#125;
    &#125;

    @Override
    public void channelReadComplete(ChannelHandlerContext ctx) &#123;
        ctx.flush();
    &#125;

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) &#123;
        cause.printStackTrace();
        ctx.close();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>TelnetServerInitializer</strong></p>
<pre><code class="copyable">package telnet;

import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.socket.SocketChannel;
import io.netty.handler.codec.DelimiterBasedFrameDecoder;
import io.netty.handler.codec.Delimiters;
import io.netty.handler.codec.string.StringDecoder;
import io.netty.handler.codec.string.StringEncoder;
import io.netty.handler.ssl.SslContext;

/**
 * Creates a newly configured &#123;@link ChannelPipeline&#125; for a new channel.
 */
public class TelnetServerInitializer extends ChannelInitializer< SocketChannel> &#123;

    private static final StringDecoder DECODER = new StringDecoder();
    private static final StringEncoder ENCODER = new StringEncoder();

    private static final TelnetServerHandler SERVER_HANDLER = new TelnetServerHandler();

    private final SslContext sslCtx;

    public TelnetServerInitializer(SslContext sslCtx) &#123;
        this.sslCtx = sslCtx;
    &#125;

    @Override
    public void initChannel(SocketChannel ch) throws Exception &#123;
        ChannelPipeline pipeline = ch.pipeline();

        if (sslCtx != null) &#123;
            pipeline.addLast(sslCtx.newHandler(ch.alloc()));
        &#125;

        // Add the text line codec combination first,
        pipeline.addLast(new DelimiterBasedFrameDecoder(8192, Delimiters.lineDelimiter()));
        // the encoder and decoder are static as these are sharable
        pipeline.addLast(DECODER);
        pipeline.addLast(ENCODER);

        // and then business logic.
        pipeline.addLast(SERVER_HANDLER);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">2 启动后的系统调用</h4>
<p><strong>主线程(23109)</strong></p>
<pre><code class="copyable">## 256无实际作用，这里只为了兼容旧版kernel api
epoll_create(256)                       = 7epoll_ctl(7, EPOLL_CTL_ADD, 5, &#123;EPOLLIN, &#123;u32=5, u64=5477705356928876549&#125;&#125;) = 0

epoll_create(256)                       = 10epoll_ctl(10, EPOLL_CTL_ADD, 8, &#123;EPOLLIN, &#123;u32=8, u64=17041805914081853448&#125;&#125;) = 0

epoll_create(256)                       = 13
epoll_ctl(13, EPOLL_CTL_ADD, 11, &#123;EPOLLIN, &#123;u32=11, u64=17042151607409573899&#125;&#125;) = 0

epoll_create(256)                       = 16
epoll_ctl(16, EPOLL_CTL_ADD, 14, &#123;EPOLLIN, &#123;u32=14, u64=17042497300737294350&#125;&#125;) = 0

epoll_create(256)                       = 19
epoll_ctl(19, EPOLL_CTL_ADD, 17, &#123;EPOLLIN, &#123;u32=17, u64=17042561450368827409&#125;&#125;) = 0

epoll_create(256)                       = 10
socket(AF_INET, SOCK_STREAM, IPPROTO_IP) = 20
clone(child_stack=0x7fc3c509afb0, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7fc3c509b9d0, tls=0x7fc3c509b700, child_tidptr=0x7fc3c509b9d0) = 23130
<span class="copy-code-btn">复制代码</span></code></pre>
<p>概括为：</p>
<ul>
<li>向OS新建socket，并开启clone boss线程23130。</li>
<li>为BOSS创建了一个epoll（论证参见下面“boss”），每个worker创建一个epoll数据结构（本质上是在kernel内存区创建了一个数据结构，用于后续监听）。</li>
<li>创建boss线程监听的socket（本质上在kernel中创建一个数据结构）。</li>
</ul>
<p><strong>boss（23130）</strong></p>
<pre><code class="copyable">bind(20, &#123;sa_family=AF_INET, sin_port=htons(8023), sin_addr=inet_addr("0.0.0.0")&#125;, 16) = 0
listen(20, 128)                         = 0
getsockname(20, &#123;sa_family=AF_INET, sin_port=htons(8023), sin_addr=inet_addr("0.0.0.0")&#125;, [16]) = 0
getsockname(20, &#123;sa_family=AF_INET, sin_port=htons(8023), sin_addr=inet_addr("0.0.0.0")&#125;, [16]) = 0 

##将fd为7号epoll和fd为20号的socket绑定，事件：epoll_ctl_add和epoll_ctl_mod
epoll_ctl(7, EPOLL_CTL_ADD, 20, &#123;EPOLLIN, &#123;u32=20, u64=14198059139132817428&#125;&#125;) = 0
epoll_ctl(7, EPOLL_CTL_MOD, 20, &#123;EPOLLIN, &#123;u32=20, u64=20&#125;&#125;) = 0
epoll_wait(7, [&#123;EPOLLIN, &#123;u32=5, u64=17295150779149058053&#125;&#125;], 8192, 1000) = 1
epoll_wait(7, [], 8192, 1000)           = 0(不断轮训，1S超时一次)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>概括为：</p>
<ul>
<li>将上一步中main线程创建的fd：20绑定端口8023，并开启监听（网卡负责监听和接受连接和数据，kernel则负责路由到具体进程，具体参见：关于socket和bind和listen，TODO ）。</li>
<li>将7号socket对应的fd绑定到20号对应的epoll数据结构上去（都是操作kernel中的内存）。</li>
<li>开始1S中一次阻塞等待epoll有任何连接或数据到达。</li>
</ul>
<h4 data-id="heading-14">3 客户端连接</h4>
<p><strong>boss (23130)</strong></p>
<pre><code class="copyable">accept(20, &#123;sa_family=AF_INET, sin_port=htons(11144), sin_addr=inet_addr("42.120.74.122")&#125;, [16]) = 24
getsockname(24, &#123;sa_family=AF_INET, sin_port=htons(8023), sin_addr=inet_addr("192.168.0.120")&#125;, [16]) = 0
getsockname(24, &#123;sa_family=AF_INET, sin_port=htons(8023), sin_addr=inet_addr("192.168.0.120")&#125;, [16]) = 0
setsockopt(24, SOL_TCP, TCP_NODELAY, [1], 4) = 0
getsockopt(24, SOL_SOCKET, SO_SNDBUF, [87040], [4]) = 0
getsockopt(24, SOL_SOCKET, SO_SNDBUF, [87040], [4]) = 0
##抛出 work线程
clone(child_stack=0x7fc3c4c98fb0, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7fc3c4c999d0, tls=0x7fc3c4c99700, child_tidptr=0x7fc3c4c999d0) = 2301
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>worker (2301)</strong></p>
<pre><code class="copyable">writev(24, [&#123;"Welcome to iZbp14e1g9ztpshfrla9m"..., 37&#125;, &#123;"It is Sun Aug 23 15:44:14 CST 20"..., 41&#125;], 2) = 78
epoll_ctl(13, EPOLL_CTL_ADD, 24, &#123;EPOLLIN, &#123;u32=24, u64=24&#125;&#125;) = 0
epoll_ctl(13, EPOLL_CTL_MOD, 24, &#123;EPOLLIN, &#123;u32=24, u64=14180008216221450264&#125;&#125;) = 0
epoll_wait(13, [&#123;EPOLLIN, &#123;u32=11, u64=17042151607409573899&#125;&#125;], 8192, 1000) = 1 
read(11, "\1", 128)                     = 1
##开始无限loop
epoll_wait(13, [], 8192, 1000)          = 0
epoll_wait(13, [&#123;EPOLLIN, &#123;u32=24, u64=24&#125;&#125;], 8192, 1000) = 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>概括：</p>
<ul>
<li>当BOSS轮训epoll_wait等到了连接后，首先accept得到该socket对应的fd。</li>
<li>连接建立后 BOSS立马抛出一个线程（clone函数）。</li>
<li>worker（即新建的线程）写入了一段数据（这里是业务逻辑）。</li>
<li>worker将该client对应的fd绑定到了13号epoll上。</li>
<li>worker继续轮训监听13号epoll。</li>
</ul>
<h4 data-id="heading-15">4 客户端主动发送数据</h4>
<p><strong>worker（2301）</strong></p>
<pre><code class="copyable">read(24, "i am daojian\r\n", 1024)      = 14
write(24, "Did you say 'i am daojian'?\r\n", 29) = 29
##继续无限loop
epoll_wait(13, [], 8192, 1000)          = 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>概括为：</p>
<ul>
<li>wait到数据后，立即read到用户控件内存中（读取1024个字节到 用户控件某个buff中）。</li>
<li>写入数据（业务逻辑，不必太关注）。</li>
<li>继续轮训等待13号epoll。</li>
</ul>
<h4 data-id="heading-16">5 客户端发送bye报文，服务器断开TCP连接</h4>
<p><strong>worker（2301）</strong></p>
<pre><code class="copyable">read(24, "bye\r\n", 1024)               = 5
write(24, "Have a good day!\r\n", 18)   = 18
getsockopt(24, SOL_SOCKET, SO_LINGER, &#123;onoff=0, linger=0&#125;, [8]) = 0
dup2(25, 24)                            = 24
##从epoll数据结构中（OS）中删除fd为24的socket
epoll_ctl(13, EPOLL_CTL_DEL, 24, 0x7f702dd531e0) = -1 ENOENT
##关闭24 socket
close(24)                               = 0
##继续等待13 epoll数据
epoll_wait(13, [], 8192, 1000)          = 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>断开客户端连接概括为：</p>
<ul>
<li>从epoll中删除该客户端对应的fd（这里触发源头没找到，可能是boss）。</li>
<li>close关闭客户端24号fd。</li>
<li>继续轮训epoll。</li>
</ul>
<h4 data-id="heading-17">6 五个客户端同时连接</h4>
<p><strong>boss线程（23130）</strong></p>
<pre><code class="copyable">accept(20, &#123;sa_family=AF_INET, sin_port=htons(1846), sin_addr=inet_addr("42.120.74.122")&#125;, [16]) = 24
clone(child_stack=0x7f702cc51fb0, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7f702cc529d0, tls=0x7f702cc52700, child_tidptr=0x7f702cc529d0) = 10035

accept(20, &#123;sa_family=AF_INET, sin_port=htons(42067), sin_addr=inet_addr("42.120.74.122")&#125;, [16]) = 26
clone(child_stack=0x7f702cb50fb0, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7f702cb519d0, tls=0x7f702cb51700, child_tidptr=0x7f702cb519d0) = 10067

...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>woker线程（10035，第一个连接）</strong></p>
<pre><code class="copyable">epoll_ctl(13, EPOLL_CTL_ADD, 24, &#123;EPOLLIN, &#123;u32=24, u64=24&#125;&#125;) = 0
epoll_ctl(13, EPOLL_CTL_MOD, 24, &#123;EPOLLIN, &#123;u32=24, u64=3226004877247250456&#125;&#125;) = 0
epoll_wait(13, [&#123;EPOLLIN, &#123;u32=11, u64=17042151607409573899&#125;&#125;], 8192, 1000) = 1                  = 1
epoll_wait(13, [], 8192, 1000)          = 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>worker线程（10067，第二个连接）</strong></p>
<pre><code class="copyable">epoll_ctl(16, EPOLL_CTL_ADD, 26, &#123;EPOLLIN, &#123;u32=26, u64=26&#125;&#125;) = 0
epoll_ctl(16, EPOLL_CTL_MOD, 26, &#123;EPOLLIN, &#123;u32=26, u64=3221483685433835546&#125;&#125;) = 0
epoll_wait(16, [&#123;EPOLLIN, &#123;u32=14, u64=17042497300737294350&#125;&#125;], 8192, 1000) = 1
epoll_wait(16, [], 8192, 1000)          = 0
epoll_wait(16, [], 8192, 1000)          = 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>worker线程（10067，第二个连接）</strong></p>
<pre><code class="copyable">epoll_ctl(19, EPOLL_CTL_ADD, 27, &#123;EPOLLIN, &#123;u32=27, u64=27&#125;&#125;) = 0
epoll_ctl(19, EPOLL_CTL_MOD, 27, &#123;EPOLLIN, &#123;u32=27, u64=3216966479350071323&#125;&#125;) = 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>worker线程(8055，第四个连接)</strong></p>
<pre><code class="copyable">epoll_ctl(10, EPOLL_CTL_ADD, 28, &#123;EPOLLIN, &#123;u32=28, u64=28&#125;&#125;) = 0
epoll_ctl(10, EPOLL_CTL_MOD, 28, &#123;EPOLLIN, &#123;u32=28, u64=3302604828697427996&#125;&#125;) = 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>worker线程（10035，第五个连接，不在clone线程，而是复用了第一个epoll对应的worker）</strong></p>
<pre><code class="copyable">epoll_ctl(13, EPOLL_CTL_ADD, 29, &#123;EPOLLIN, &#123;u32=29, u64=29&#125;&#125;) = 0
epoll_ctl(13, EPOLL_CTL_MOD, 29, &#123;EPOLLIN, &#123;u32=29, u64=29&#125;&#125;) = 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>概括为：</p>
<ul>
<li>epoll和boss、worker之间的关系：一共有4个worker对应着4个epoll对象，boss和每个worker都有对应自己的epoll。</li>
<li>boss根据epoll数量，平衡分配连接到每个worker对应的epoll中。</li>
</ul>
<h4 data-id="heading-18">7 总结</h4>
<p>下图通过对系统调用的调查得出 netty 和 kernel 交互图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41a9f946f8ab4057ab4dd880d779187c~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>初始化直接创建5个epoll，其中7号为boss使用，专门用于处理和客户端连接；其余4个用来给worker使用，用户处理和客户端的数据交互。</p>
<p>work的线程数量，取决于初始化时创建了几个epoll，worker的复用本质上是epoll的复用。</p>
<p>work之间为什么要独立使用epoll？为什么不共享？</p>
<ul>
<li>为了避免各个worker之间发生争抢连接处理，netty直接做了物理隔离，避免竞争。各个worker只负责处理自己管理的连接，并且后续该worker中的每个client的读写操作完全由 该线程单独处理，天然避免了资源竞争，避免了锁。</li>
<li>worker单线程，性能考虑：worker不仅仅要epoll_wait，还是处理read、write逻辑，加入worker处理了过多的连接，势必造成这部分消耗时间片过多，来不及处理更多连接，性能下降。</li>
</ul>
<h4 data-id="heading-19">8 优缺点</h4>
<p><strong>优点</strong></p>
<ul>
<li>数据处理：netty提供了大量成熟的数据处理组件（ENCODER、DECODER），HTTP、POP3拿来即用。</li>
<li>编码复杂度、可维护性：netty充分使得业务逻辑与网络处理解耦，只需要少量的BootStrap配置即可，更多的集中在业务逻辑处理上。</li>
<li>性能：netty提供了的ByteBuf(底层Java原生的ByteBuffer)，提供了池化的ByteBuf，兼顾读取性能和ByteBuf内存分配（在后续文档中会再做详解）。</li>
</ul>
<p><strong>缺点</strong></p>
<ul>
<li>入门有一定难度。</li>
</ul>
<h3 data-id="heading-20">五 AIO</h3>
<h4 data-id="heading-21">1 启动</h4>
<p><strong>main线程</strong></p>
<pre><code class="copyable">epoll_create(256)                       = 5
epoll_ctl(5, EPOLL_CTL_ADD, 6, &#123;EPOLLIN, &#123;u32=6, u64=11590018039084482566&#125;&#125;) = 0

##创建BOSS 线程(Proactor)
clone(child_stack=0x7f340ac06fb0, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7f340ac079d0, tls=0x7f340ac07700, child_tidptr=0x7f340ac079d0) = 22704

socket(AF_INET6, SOCK_STREAM, IPPROTO_IP) = 8
setsockopt(8, SOL_IPV6, IPV6_V6ONLY, [0], 4) = 0
setsockopt(8, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0
bind(8, &#123;sa_family=AF_INET6, sin6_port=htons(9090), inet_pton(AF_INET6, "::", &sin6_addr), sin6_flowinfo=0, sin6_scope_id=0&#125;, 28) = 0
listen(8, 50)

accept(8, 0x7f67d01b3120, 0x7f67d9246690) = -1
epoll_ctl(5, EPOLL_CTL_MOD, 8, &#123;EPOLLIN|EPOLLONESHOT, &#123;u32=8, u64=15380749440025362440&#125;&#125;) = -1 ENOENT (No such file or directory)
epoll_ctl(5, EPOLL_CTL_ADD, 8, &#123;EPOLLIN|EPOLLONESHOT, &#123;u32=8, u64=15380749440025362440&#125;&#125;) = 0
read(0,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>22704(BOSS 线程(Proactor))</strong></p>
<pre><code class="copyable">epoll_wait(5,  < unfinished ...>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">2 请求连接</h4>
<pre><code class="copyable">**22704(BOSS 线程(Proactor))处理连接**

epoll_wait(5,[&#123;EPOLLIN, &#123;u32=9, u64=4294967305&#125;&#125;], 512, -1) = 1
accept(8, &#123;sa_family=AF_INET6, sin6_port=htons(55320), inet_pton(AF_INET6, "::ffff:36.24.32.140", &sin6_addr), sin6_flowinfo=0, sin6_scope_id=0&#125;, [28]) = 9
clone(child_stack=0x7ff35c99ffb0, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7ff35c9a09d0, tls=0x7ff35c9a0700, child_tidptr=0x7ff35c9a09d0) = 26241
epoll_wait(5,  < unfinished ...>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>26241</strong></p>
<pre><code class="copyable">#将client 连接的FD加入到BOSS的epoll中，以便BOSS线程监听网络事件
epoll_ctl(5, EPOLL_CTL_MOD, 9, &#123;EPOLLIN|EPOLLONESHOT, &#123;u32=9, u64=4398046511113&#125;&#125;) = -1 ENOENT (No such file or directory)
epoll_ctl(5, EPOLL_CTL_ADD, 9, &#123;EPOLLIN|EPOLLONESHOT, &#123;u32=9, u64=4398046511113&#125;&#125;) = 0
accept(8, 0x7ff3440008c0, 0x7ff35c99f4d0) = -1 EAGAIN (Resource temporarily unavailable)
epoll_ctl(5, EPOLL_CTL_MOD, 8, &#123;EPOLLIN|EPOLLONESHOT, &#123;u32=8, u64=8&#125;&#125;) = 0
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">3 客户端发送数据</h4>
<p><strong>22704(BOSS 线程(Proactor))处理连接</strong></p>
<pre><code class="copyable">epoll_wait(5,[&#123;EPOLLIN, &#123;u32=9, u64=4294967305&#125;&#125;], 512, -1) = 1
##数据读出
read(9, "daojian111\r\n", 1024)         = 12
##数据处理交给其他线程，这里由于线程池为空，需要先clone线程
clone(child_stack=0x7ff35c99ffb0, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7ff35c9a09d0, tls=0x7ff35c9a0700, child_tidptr=0x7ff35c9a09d0) = 26532
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复制线程处理，线程号26532</strong></p>
<pre><code class="copyable">write(1, "pool-1-thread-2-10received : dao"..., 41) = 41
write(1, "\n", 1)
accept(8, 0x7f11c400b5f0, 0x7f11f42fd4d0) = -1 EAGAIN (Resource temporarily unavailable)
epoll_ctl(5, EPOLL_CTL_MOD, 8, &#123;EPOLLIN|EPOLLONESHOT, &#123;u32=8, u64=8&#125;&#125;) = 0
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">4 总结</h4>
<ul>
<li>从系统调用角度，Java的AIO事实上是以多路复用（Linux上为epoll）等同步IO为基础，自行实现了异步事件分发。</li>
<li>BOSS Thread负责处理连接，并分发事件。</li>
<li>WORKER Thread只负责从BOSS接收的事件执行，不负责任何网络事件监听。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb91e9d9a0924157bfe25741a203fece~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-25">5 优缺点</h4>
<p><strong>优点</strong></p>
<p>相比于前面的BIO、NIO，AIO已经封装好了任务调度，使用时只需关心任务处理。</p>
<p><strong>缺点</strong></p>
<ul>
<li>事件处理完全由Thread Pool完成，对于同一个channel的多个事件可能会出现并发问题。</li>
<li>相比netty，buffer API不友好容易出错；编解码工作复杂。</li>
</ul>
<p><a href="https://developer.aliyun.com/article/784933?utm_content=g_1000280794" target="_blank" rel="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            