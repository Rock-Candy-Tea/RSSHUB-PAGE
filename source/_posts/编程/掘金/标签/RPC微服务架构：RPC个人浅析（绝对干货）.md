
---
title: 'RPC微服务架构：RPC个人浅析（绝对干货）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2438c05c8b894482a6c14ee72d00a0f7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 21:01:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2438c05c8b894482a6c14ee72d00a0f7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>温馨提示：下述内容多为个人理解，如有错误请指正！感谢</p>
<h2 data-id="heading-0">什么是RPC？</h2>
<ul>
<li><strong>RPC(Remote Procedure Call Protocol)远程过程调用：</strong>
<ul>
<li>我们有生产者服务器和消费者服务器，分别部署着不同的应用a、b。当我们想通过消费者服务器来调用生产者服务器的应用上提供的函数或方法时，由于这些应用不在同一个内存空间，不能够直接调用，这就需要通过借助网络来传输数据请求。就比如我们在自己的机器上写一个程序，别人是无法直接调用的，这个时候就需要通过远程服务调用，RPC应运而生了！</li>
</ul>
微服务架构是一种将单应用程序作为一套小型服务开发的方法。（因此我们可以知道，一般的小型企业是用不到微服务的）
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.sogou.com%2Fv35613.htm%3FfromTitle%3DRPC" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.sogou.com/v35613.htm?fromTitle=RPC" ref="nofollow noopener noreferrer">百科官方解答</a></p>
<blockquote>
<p>RPC是一种通过网络从远程计算机程序上请求服务，而不需要了解底层网络技术的协议。RPC协议假定某些传输协议的存在，如TCP或UDP，为通信程序之间携带信息数据。在OSI网络通信模型中，RPC跨越了传输层和应用层。RPC使得开发包括网络分布式多程序在内的应用程序更加容易。</p>
</blockquote>
</li>
</ul>
</li>
</ul>
<p>RPC采用客户机/服务器模式。请求程序就是一个客户机，而服务提供程序就是一个服务器。首先，客户机调用进程发送一个有进程参数的调用信息到服务进程，然后等待应答信息。在服务器端，进程保持睡眠状态直到调用信息到达为止。当一个调用信息到达，服务器获得进程参数，计算结果，发送答复信息，然后等待下一个调用信息，最后，客户端调用进程接收答复信息，获得进程结果，然后调用执行继续进行。</p>
<h2 data-id="heading-1">RPC解决了什么问题？</h2>
<p>偏技术的问题：
1.通讯问题 : 客户端和服务器端通过TCP协议进行数据的传输。
2.寻址问题 ： 服务器之间的应用如何调用，如何查找到对应应用所在的IP和端口。</p>
<p>优点：
1.解耦：把每个系统拆分开部署在不同的服务器上。
2.避免重复开发：避免对一个系统的重复开发，当有需要的时候可以直接调用
3.方便维护</p>
<h2 data-id="heading-2">RPC具体工作流程是怎么样的？（纯个人理解，待大佬指正）</h2>
<ul>
<li><strong>RPC需要有三方：生产者、消费者和中央管理中心。</strong> 生产者即服务提供方，消费者即服务请求方，中央管理中心（下面简称中央）是充当一个中间人的身份，可以理解为我们的房屋中介。</li>
<li><strong>当生产者想要使用微服务的时候，</strong> 需要<strong>先去中央注册身份</strong>，包括IP、端口号、包括哪些类或方法等信息都需要提供给中央做记录；同时，中央会根据自己的加密规则，生成一个密钥来唯一标志该生产者。</li>
<li>同理，<strong>当消费者想要使用微服务的时候，</strong> 也需要<strong>先去中央注册身份</strong>，包括IP、端口号、想要访问的方法等信息都需要提供给中央做记录；同时中央根据消费者提供的信息会给消费者提供一定的权限，并根据权限来判断该消费者可以去调用哪些生产者，也会对应生成密钥。</li>
<li>当<strong>消费者完成注册后</strong>，通过拿到的权限，来<strong>获取对应生产者的</strong>IP、端口号和密钥等<strong>信息，并将这些信息存放在本地缓存。</strong></li>
<li>当<strong>消费者发送请求时</strong>，消费者会从本地缓存读取有效数据信息，如携带着对应生产者的密钥，通过HTTP、TCP等协议<strong>进行数据传输</strong>（这里传输用到了流操作、序列化和反序列化技术，暂时不做讲解，可出门右拐进入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E5%25BA%258F%25E5%2588%2597%25E5%258C%2596%2F2890184%3Ffr%3Daladdin" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E5%BA%8F%E5%88%97%E5%8C%96/2890184?fr=aladdin" ref="nofollow noopener noreferrer">百度</a>），<strong>生产者接收到请求后，进行反射代理，</strong> 首先来比对密钥是否正确，正确则进行真正的请求处理工作。</li>
<li>到这里，一个正常简易的RPC流程算是走完了。</li>
</ul>
<p><strong>但是就怕意外啊，RPC还有一些保障性的工作</strong></p>
<ul>
<li><strong>心跳机制：</strong> 为防止生产者服务器突发心脏病宕机，或者某天心情不好闹小情绪导致发生异常而无法使用，我们强制规定生产者需要每隔几秒（可根据具体业务自行设计）向中央发送一次心跳，来证明生产者一切健康。如果说生产者一次没有发送心跳，中央可以原谅它的小调皮，但是如果连续三次都未发送心跳，中央就会主动标记该生产者有异常，同步到消费者缓存中进行信息的更新，并对该生产者服务器进行普通生病检查，同时触发报警机制来提醒正在改bug的程序猿来为其医治。</li>
<li><strong>同步机制：</strong> 当生产者服务器有新增服务器、生产者服务器减少或更换服务器的情况，中央会将生产者的信息同步到消费者缓存。</li>
<li><strong>反馈与检查机制：</strong> 由于心跳机制和同步机制没有即时性，那么很多时候，生产者服务器发生问题，往往是消费者先发现，当消费者连接生产者时，一次连接不成功，尝试重连，多次连接不成功后，会从本地缓存寻找其他可用生产者服务器信息进行数据的请求，同时会把连接失败的生产者服务器信息反馈上报给中央，说明该生产者服务器偷懒不工作；中央收到反馈后，立刻去检查该生产者服务器的异常原因并尝试触发报警机制。</li>
</ul>
<p>这样一个大体上的RPC思想算是出来了，文字不易理解，可参考下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2438c05c8b894482a6c14ee72d00a0f7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">RPC中有哪些方面可以提升性能优化？</h2>
<p><strong>1.缓存：</strong> 缓存技术有很多种，进程缓存有jdk自带的ConcurrentHashMap缓存、功能比较丰富的Ehcache缓存等；分布式缓存有Redis和Tair等。依据我们业务需要来选择合适的缓存可以很好的提升性能。</p>
<p><strong>2.数据传输流的操作：</strong> Netty作为高性能的NIO通信框架，在很多RPC框架中都有它的身影。我们也采用它当做通信服务器。
<strong>3.序列化和反序列化：</strong>
百科介绍：</p>
<blockquote>
<p>序列化
(Serialization)是将对象的状态信息转换为可以存储或传输的形式的过程。在序列化期间，对象将其当前状态写入到临时或持久性存储区。以后，可以通过从存储区中读取或反序列化对象的状态，重新创建该对象。</p>
</blockquote>
<p>目前互联网公司广泛使用Protobuf、Thrift、Avro等成熟的序列化解决方案来搭建RPC框架，这些都是久经考验的解决方案。当然具体使用哪种序列化还是要结合我们的业务来开展的。
<strong>4.通讯协议：</strong> 不同的通讯协议的在不同的数据结构和不同数据量时的传输性能都有所不同，也要我们看实际情况来定。我有一个想法是设计一个仿Tomcat的通讯协议，或许可以在某方面提升性能，还没实现过。</p>
<p><strong>推荐几篇不错的博客：</strong></p>
<ul>
<li><a href="https://juejin.im/post/5b849878e51d4538c77a974a" target="_blank" title="https://juejin.im/post/5b849878e51d4538c77a974a">如何优雅的设计和使用缓存？</a></li>
<li><a href="https://juejin.im/post/5c6d7640f265da2de80f5e9c" target="_blank" title="https://juejin.im/post/5c6d7640f265da2de80f5e9c">RPC基本原理以及如何用Netty来实现RPC</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FJohn8169%2Farticle%2Fdetails%2F80906755" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/John8169/article/details/80906755" ref="nofollow noopener noreferrer">Java序列化工具对比</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fshunzi1046%2Farticle%2Fdetails%2F56484008" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/shunzi1046/article/details/56484008" ref="nofollow noopener noreferrer">RPC中几种通讯协议的比较</a></li>
</ul>
<p>刚入驻掘金，敬请关注！</p></div>  
</div>
            