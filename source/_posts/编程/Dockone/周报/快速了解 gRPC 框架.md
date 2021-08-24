
---
title: '快速了解 gRPC 框架'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/a3f69f2486f280998188d6d4e0f9e129.png'
author: Dockone
comments: false
date: 2021-08-24 14:07:34
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/a3f69f2486f280998188d6d4e0f9e129.png'
---

<div>   
<br><blockquote><br>本文主要以 Python 作为基础进行演示和说明！</blockquote><code class="prettyprint">gRPC</code> 是一个高性能、通用的开源 <code class="prettyprint">RPC</code> 框架，基于 <code class="prettyprint">HTTP2</code> 协议标准设计开发，默认采用 <code class="prettyprint">Protocol Buffers</code> 数据序列化协议，支持多种开发语言。<br>
<h3>什么 gRPC 框架</h3><em>New to gRPC? Start with the following pages.</em><br>
<br><code class="prettyprint">RPC</code> 框架的目标就是让远程服务调用更加简单、透明，其负责屏蔽底层的传输方式（<code class="prettyprint">TCP</code>/<code class="prettyprint">UDP</code>）、序列化方式（<code class="prettyprint">XML</code>/<code class="prettyprint">Json</code>）和通信细节。服务调用者可以像调用本地接口一样调用远程的服务提供者，而不需要关心底层通信细节和调用过程。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/a3f69f2486f280998188d6d4e0f9e129.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/a3f69f2486f280998188d6d4e0f9e129.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
常见 <code class="prettyprint">gRPC</code> 的应用场景，主要侧重于后端服务之间进行调用，当然也可以使用于移动端。<br>
<br>gRPC 的功能优点：<br>
<ul><li>高兼容性、高性能、使用简单</li></ul><br>
<br>gRPC 的组成部分：<br>
<ul><li>使用 <code class="prettyprint">http2</code> 作为网络传输层</li><li>使用 <code class="prettyprint">protobuf</code> 这个高性能的数据包序列化协议</li><li>通过 <code class="prettyprint">protoc gprc</code> 插件生成易用的 <code class="prettyprint">SDK</code></li></ul><br>
<br>gRPC 的通信方式：<br>
<ul><li>客服端一次请求, 服务器一次应答</li><li>客服端一次请求, 服务器多次应答（流式）</li><li>客服端多次请求（流式），服务器一次应答</li><li>客服端多次请求（流式），服务器多次应答（流式）</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/b7faad867148c47e13b64827d121cb33.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/b7faad867148c47e13b64827d121cb33.jpeg" class="img-polaroid" title="2.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>使用 http2 协议</h3><em>为什么会选用 http2 作为 gRPC 的传输协议？</em><br>
<br>除了速度之外，最大的原因就是最大程度的服务兼容性。因为 <code class="prettyprint">gRPC</code> 基于 <code class="prettyprint">http2</code> 协议，加之市面上主流的代理工具也都支持 <code class="prettyprint">http2</code> 协议，所以自然就支持 <code class="prettyprint">gRPC</code> 了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/a042ba6a3bc8c342b1663c061e5b269e.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/a042ba6a3bc8c342b1663c061e5b269e.jpeg" class="img-polaroid" title="3.jpeg" alt="3.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
我们都知道 <code class="prettyprint">http</code> 协议的几个重要版本，随着不断更新迭代而来，也解决了不同的问题。比如，在 <code class="prettyprint">http1.0</code> 中最大的槽点就是短连接，随着 <code class="prettyprint">http1.1</code> 的出世解决了该性能问题，并且增加了丰富的 <code class="prettyprint">header</code> 语义。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/5a6e6309f7df465e0bdeba30edcbca06.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/5a6e6309f7df465e0bdeba30edcbca06.jpeg" class="img-polaroid" title="4.jpeg" alt="4.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
在前几年，网站基本都是使用的 <code class="prettyprint">http1.1</code> 协议。但是，该协议也是存在着很多问题，比如队头阻塞，即一个连接只能跑一个请求，在这个请求没返回数据之前，其他请求就不能占用该连接。通常来说，我们使用的 <code class="prettyprint">chrome</code> 浏览器默认会并发发起六个连接，如果请求太多的话，就需要等待了。虽然 <code class="prettyprint">http1.1</code> 支持 <code class="prettyprint">pipeline</code>，同时也有一些解决方案，但是还是不够优秀，所以就有了 <code class="prettyprint">http2</code> 协议。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/90fe6b901e825192be0c74d67b00a006.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/90fe6b901e825192be0c74d67b00a006.jpeg" class="img-polaroid" title="5.jpeg" alt="5.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/1ffac1c6ed8a623ff0c20831f9249506.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/1ffac1c6ed8a623ff0c20831f9249506.jpeg" class="img-polaroid" title="6.jpeg" alt="6.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<code class="prettyprint">http2</code> 协议最大的优点在于多路复用，这里的多路复用不是指传统类似 <code class="prettyprint">epoll</code> 对 <code class="prettyprint">tcp</code> 连接的复用，而是协议层的多路复用，把一个个的请求封装成 <code class="prettyprint">stream</code> 流，这些流是可以并发交错请求，没有 <code class="prettyprint">http1.1</code> 那种队头阻塞问题。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/47a9238b6d0dbfb18b9047a20618d780.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/47a9238b6d0dbfb18b9047a20618d780.jpeg" class="img-polaroid" title="7.jpeg" alt="7.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/06ee02b7f94cf8253724aa386df396e8.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/06ee02b7f94cf8253724aa386df396e8.jpeg" class="img-polaroid" title="8.jpeg" alt="8.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/c8c26d079db820407a7fff2ca4cf3497.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/c8c26d079db820407a7fff2ca4cf3497.jpeg" class="img-polaroid" title="9.jpeg" alt="9.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
当然，未来还会有更好的，<code class="prettyprint">http3</code> 协议。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/91f69b1522a3313287605110b1cfb7eb.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/91f69b1522a3313287605110b1cfb7eb.jpeg" class="img-polaroid" title="10.jpeg" alt="10.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>gRPC 的核心概念</h3><em>An introduction to gRPC and protocol buffers.</em><br>
<br><code class="prettyprint">ProtoBuf buffer</code> 是一种数据表达方式，以 <code class="prettyprint">.proto</code> 结尾的数据文件，我们可以将其类比为 <code class="prettyprint">json</code>、<code class="prettyprint">xml</code> 等文件。针对 <code class="prettyprint">ProtoBuf buffer</code> 数据源，可以利用 <code class="prettyprint">protoc</code> 工具来生成各种语言的访问类。其优点在于，编解码速度更快且传输的数据更小。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/5b1c61a08b0279e464bb761059db0ec6.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/5b1c61a08b0279e464bb761059db0ec6.jpeg" class="img-polaroid" title="11.jpeg" alt="11.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/aa7c8b26575d1794d53f24189f9377b5.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/aa7c8b26575d1794d53f24189f9377b5.jpeg" class="img-polaroid" title="12.jpeg" alt="12.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/7dbfccdafbbc01eb8d3375814f56c075.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/7dbfccdafbbc01eb8d3375814f56c075.jpeg" class="img-polaroid" title="13.jpeg" alt="13.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/78922fca8ab8871f4aa7b3b29bda360d.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/78922fca8ab8871f4aa7b3b29bda360d.jpeg" class="img-polaroid" title="14.jpeg" alt="14.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>编写 proto 文件</h4>编写 <code class="prettyprint">helloworld.proto</code> 文件:<br>
<pre class="prettyprint">// 指定使用协议语法<br>
syntax = "proto3";<br>
<br>
// 定义一个包<br>
package greeterpb;<br>
<br>
// 关键字 server 来定一个服务<br>
// gRPC 的服务是通过参数和返回类型来指定可以远程调用的方法<br>
service Greeter &#123;<br>
rpc SayHello(HelloRequest) returns (HelloReply) &#123;&#125;<br>
rpc SayHelloAgain(HelloRequest) returns (HelloReply) &#123;&#125;<br>
&#125;<br>
<br>
// 定义消息请求<br>
// 关键字 message 来定义请求或相应需要使用的消息格式<br>
message HelloRequest &#123;<br>
string name = 1;<br>
&#125;<br>
<br>
// 定义消息响应<br>
// 关键字 message 来定义请求或相应需要使用的消息格式<br>
message HelloReply &#123;<br>
string message = 1;<br>
&#125; <br>
</pre><br>
<h4>使用 protoc 编译</h4><ul><li><code class="prettyprint">--python_out</code>：编译生成处理 <code class="prettyprint">protobuf</code> 相关的代码的路径</li><li><code class="prettyprint">--grpc_python_out</code>：编译生成处理 <code class="prettyprint">gRPC</code> 相关的代码的路径</li><li><code class="prettyprint">-I</code>：指定 <code class="prettyprint">proto</code> 的文件路径</li></ul><br>
<br><pre class="prettyprint"># 编译 proto 文件<br>
$ python -m grpc_tools.protoc \<br>
--python_out=. --grpc_python_out=. -I. \<br>
helloworld.proto<br>
<br>
# 编译后生成的代码<br>
helloworld_pb2.py<br>
helloworld_pb2_grpc.py<br>
</pre><br>
<h4>添加 protobuf 运行时</h4>编写 <code class="prettyprint">helloworld</code> 的 <code class="prettyprint">gRPC</code> 实现：<br>
<pre class="prettyprint"># 服务器端<br>
# helloworld_grpc_server.py<br>
<br>
from concurrent import futures<br>
import time<br>
import grpc<br>
import helloworld_pb2<br>
import helloworld_pb2_grpc<br>
<br>
# 实现 proto 文件中定义的 GreeterServicer<br>
class Greeter(helloworld_pb2_grpc.GreeterServicer):<br>
# 实现 proto 文件中定义的 RPC 调用<br>
def SayHello(self, request, context):<br>
    return helloworld_pb2.HelloReply(message = 'hello &#123;msg&#125;'.format(msg = request.name))<br>
<br>
def SayHelloAgain(self, request, context):<br>
    return helloworld_pb2.HelloReply(message='hello &#123;msg&#125;'.format(msg = request.name))<br>
<br>
def serve():<br>
# 启动 RPC 服务<br>
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))<br>
helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)<br>
server.add_insecure_port('[::]:50051')<br>
server.start()<br>
try:<br>
    while True:<br>
        time.sleep(60*60*24)<br>
except KeyboardInterrupt:<br>
    server.stop(0)<br>
<br>
if __name__ == '__main__':<br>
serve()<br>
</pre><br>
<pre class="prettyprint"># 客户端<br>
# helloworld_grpc_client.py<br>
<br>
import grpc<br>
import helloworld_pb2<br>
import helloworld_pb2_grpc<br>
<br>
def run():<br>
# 连接 RPC 服务器<br>
channel = grpc.insecure_channel('localhost:50051')<br>
# 调用 RPC 服务<br>
stub = helloworld_pb2_grpc.GreeterStub(channel)<br>
response = stub.SayHello(helloworld_pb2.HelloRequest(name='czl'))<br>
print("Greeter client received: " + response.message)<br>
response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='daydaygo'))<br>
print("Greeter client received: " + response.message)<br>
<br>
if __name__ == '__main__':<br>
run() <br>
</pre><br>
<h4>项目中集成</h4><pre class="prettyprint"># 运行启动服务端<br>
$ python3 helloworld_grpc_server.py<br>
<br>
# 运行启动客户端<br>
$ python3 helloworld_grpc_client.py<br>
</pre><br>
<h3>快速使用 gRPC 框架</h3><em>This guide gets you started with gRPC in Python with a simple working example.</em><br>
<h4>构建基础环境</h4>创建虚拟环境：<br>
<pre class="prettyprint"># need python3.5+<br>
$ python -m pip install virtualenv<br>
$ virtualenv venv<br>
$ source venv/bin/activate<br>
$ python -m pip install --upgrade pip<br>
</pre><br>
<h4>安装 gRPC 包</h4><code class="prettyprint">grpcio-tools</code> 包含了生成对应的程序代码。<br>
<pre class="prettyprint"># install gRPC<br>
$ python -m pip install grpcio<br>
$ python -m pip install grpcio-tools<br>
<br>
# install it system wide<br>
$ sudo python -m pip install grpcio<br>
</pre><br>
<h4>下载示例程序</h4>仓库非常大，不太好下载，需要梯子强壮。<br>
<pre class="prettyprint"># clone the repository<br>
$ git clone -b v1.37.1 https://github.com/grpc/grpc<br>
<br>
# say "hello, world"<br>
$ cd grpc/examples/python/helloworld<br>
</pre><br>
<h4>运行示例程序</h4>运行了一个客户机-服务器应用程序。<br>
<pre class="prettyprint"># run the server<br>
$ python greeter_server.py<br>
<br>
# run the client<br>
$ python greeter_client.py<br>
</pre><br>
<h4>更新 gRPC 服务</h4>即对现有的服务进行更新，来提供不一样的特性。<br>
<pre class="prettyprint"># examples/protos/helloworld.proto<br>
// The greeting service definition.<br>
service Greeter &#123;<br>
// Sends a greeting<br>
rpc SayHello (HelloRequest) returns (HelloReply) &#123;&#125;<br>
// Sends another greeting<br>
rpc SayHelloAgain (HelloRequest) returns (HelloReply) &#123;&#125;<br>
&#125;<br>
<br>
// The request message containing the user's name.<br>
message HelloRequest &#123;<br>
string name = 1;<br>
&#125;<br>
<br>
// The response message containing the greetings<br>
message HelloReply &#123;<br>
string message = 1;<br>
&#125; <br>
</pre><br>
<pre class="prettyprint"># 进入对应目录<br>
cd examples/python/helloworld<br>
<br>
# 重新生成代码<br>
$ python -m grpc_tools.protoc -I../../protos \<br>
--python_out=. --grpc_python_out=. \<br>
../../protos/helloworld.proto<br>
<br>
# 生成文件 - 用来和 protobuf 进行数据交互<br>
helloworld_pb2.py<br>
# 生成文件 - 用来和 gRPC 进行数据交互<br>
helloworld_pb2_grpc.py<br>
</pre><br>
<pre class="prettyprint"># 调整客户端代码 - greeter_client.py<br>
def run():<br>
channel = grpc.insecure_channel('localhost:50051')<br>
stub = helloworld_pb2_grpc.GreeterStub(channel)<br>
response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))<br>
print("Greeter client received: " + response.message)<br>
response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))<br>
print("Greeter client received: " + response.message)<br>
<br>
# 调整服务端代码 - greeter_server.py<br>
class Greeter(helloworld_pb2_grpc.GreeterServicer):<br>
def SayHello(self, request, context):<br>
return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)<br>
<br>
def SayHelloAgain(self, request, context):<br>
return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.name)<br>
...<br>
</pre><br>
<pre class="prettyprint"># run the server<br>
$ python greeter_server.py<br>
<br>
# run the client<br>
$ python greeter_client.py<br>
</pre><br>
<h3>gRPC 的应用场景</h3><em>RPC 的使用场景：分布式系统</em><br>
<br>随着微服务的不断发展，基于语言中立性的原则构建微服务，逐渐成为一种主流设计模式。例如对于后端并发处理要求高的微服务，比较适合采用 <code class="prettyprint">Go</code> 语言构建，而对于前端的 <code class="prettyprint">Web</code> 界面，则更适合 <code class="prettyprint">JavaScript</code>。因此，基于多语言的 <code class="prettyprint">gRPC</code> 框架来构建微服务，是一种比较好的技术选择。<br>
<h4>gRPC Microservice</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/08ba1b66c5833e804602203e9c7e83ad.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/08ba1b66c5833e804602203e9c7e83ad.jpeg" class="img-polaroid" title="15.jpeg" alt="15.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>gRPC Kubernetes</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/8878ff5bc3a18964f3aab3512b4574e1.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/8878ff5bc3a18964f3aab3512b4574e1.jpeg" class="img-polaroid" title="16.jpeg" alt="16.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
原文链接：<a href="https://www.escapelife.site/posts/395e12c9.html" rel="nofollow" target="_blank">https://www.escapelife.site/posts/395e12c9.html</a>，作者：Escape
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            