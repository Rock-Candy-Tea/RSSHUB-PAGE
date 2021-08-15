
---
title: '理论修炼之RPC，微服务高效通讯的首选'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87b5a2abb74f4f5e8aa590d821b11e52~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 07:26:11 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87b5a2abb74f4f5e8aa590d821b11e52~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>RPC，字面直译是远程过程调用，该项技术并不是现在才开始出现的，之前的net remoting、web service甚至DCom，都或多或少的实现了类似的功能，只不过它们或者没重视数据的编解码，或者每重视通讯协议的通用性，因此在它们流行的时候，总给人感觉或者性能没那么理想，或者难以应用。</p>
<p>而目前流行的RPC技术，例如Thrift、GRPC、Dubbo等均为互联网电商的高并发，高性能的分布式应用通讯而设计，其编解码性能都非常优秀，通讯的效率也都不错。</p>
<h1 data-id="heading-1">🎏 01. 为啥用RPC？</h1>
<p>很多朋友对于微服务采用RPC通讯都带很大的疑问，难道直接使用webApi他不香吗？</p>
<p>是的，什么事情都不是绝对的，当你的业务性能要求并不是很高的情况下，的确http的webapi已经足够了吧，毕竟抠那么一点性能，不如更快完成业务的好。</p>
<p>从拆分为微服务的角度来看，由于拆分的业务粒度问题，不可避免的会导致以前一个服务搞定的功能，现在是由多个服务联合完成的。我们画个图看看到底发生了什么？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87b5a2abb74f4f5e8aa590d821b11e52~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是的，之前的业务A如果是各个数据需要调用数据库，假设需要3次，那么拆分为微服务后，需要通过网络分别调用各个微服务的接口，这些接口再通过网络调用各自的数据库。</p>
<p>这只是一般复杂的场景，还有很多复杂的业务，可能调用链更长。</p>
<p>那么这多出来的网络调用，每个都会有延迟，加起来可能就比较客观了。当然这就是你提高了扩展性而付出的代价。</p>
<h1 data-id="heading-2">🎏 02. RPC的调用环节</h1>
<ol>
<li>RPC按照规定的协议序列化二进制流</li>
<li>网络传送（tcp或者 http2）</li>
<li>反序列化二进制流，按照指定的方法等参数交给动态代理处理，并得到返回值（有些协议可以定义没有返回值）</li>
<li>返回值进行序列化，通过网络传回调用方。</li>
<li>调用方反序列化，得到返回值。</li>
</ol>
<p>因此从上面的环节也可以看出，主要的性能可以优化的地方就是网络传输和序列化、反序列化。</p>
<p>在网络传输方面，目前比较优秀的库有netty，有能力的童鞋可以在这个基础上定义自己的协议来实现通讯底层。</p>
<p>当然目前已经存在的也比较优秀，例如：thrift，dubbo，grpc。</p>
<p>如果我们进行协议封装，推荐的做法是支持异步IO，c#下支持async模式，这样可以极大提高吞吐量。</p>
<p>在序列化性能方面，有个基本的优先级： xml < json < protobuf、thrift。</p>
<p>在数据量稍微大点的情况下，序列化json是一个很大的性能损耗，这个在之前的项目中有做过性能测试。</p>
<p>当然这些协议在使用中还有一些特性需要注意选择合适的场景。比如简单的可以采用json，因为对于protobuf、thrift，它们都需要定义idl，相对麻烦些，当然这些麻烦就是为了性能设计。</p>
<h1 data-id="heading-3">🎏 03. Thrift介绍</h1>
<p>Thrift 是一个软件框架，用来进行可扩展且跨语言的服务的开发。它结合了功能强大的软件堆栈和代码生成引擎，以构建在 C++, Java, Python, PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa, JavaScript, Node.js, Smalltalk, and OCaml 这些编程语言间无缝结合的、高效的服务。</p>
<p>thrift最初由facebook开发，目前是 Apache基金会的顶级项目。</p>
<p>thrift允许你定义一个简单的数据类型和服务接口的idl接口文件，以作为输入文件，编译器生成代码用来方便地生成RPC客户端和服务器通信的编程语言。</p>
<h1 data-id="heading-4">🎏 04. grpc介绍</h1>
<p>gRPC由 google 开发，是一款语言中立、平台中立、开源的远程过程调用(RPC)系统。</p>
<p>gRPC采用protobuf来定义接口，从而有更加严格的接口约束条件，通过protobuf可以将数据序列化为二进制编码，这会大幅减少需要传输的数据量，从而大幅提高性能。</p>
<p>gRPC采用Http 2.0协议，在通讯效率上相比采用Http协议的webapi还是有一定的优势的。</p>
<h1 data-id="heading-5">🎏 05. 小结</h1>
<p>其实还有很多内容，我想写的更多，可是实力和时间不允许，暂时到这吧，后续有什么不妥的还可以修改追加，感谢你看到这里！</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            