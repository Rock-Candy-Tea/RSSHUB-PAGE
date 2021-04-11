
---
title: 'Agileutil v0.0.15 发布，支持异步的 RPC 框架！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1124'
author: 开源中国
comments: false
date: Sat, 10 Apr 2021 19:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1124'
---

<div>   
<div class="content">
                                                                                            <p>本次更新的版本是v0.0.15。在原有基础上，开发者可通过async关键字，轻松实现异步，但异步不作为强制要求。使用async标记的方法中可配合await实现异步调用，未使用async标记的方法是同步调用，开发者自行选择。 同时优化了TCP服务端的性能，借助于asyncio, 由多线程修改为单线程异步服务器。</p> 
<h3 style="text-align:left">TCP RPC 服务端</h3> 
<p style="text-align:left">下面是一个TCP协议的服务端例子。</p> 
<ul> 
 <li>创建一个TcpRpcServer对象, 指定服务端监听地址和端口</li> 
 <li>通过@rpc装饰器注册需要被客户端请求的方法</li> 
 <li>调用serve()方法，开始处理客户端请求</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>from</strong> <strong>agileutil.rpc.server</strong> <strong>import</strong> TcpRpcServer, rpc
<strong>import</strong> <strong>asyncio</strong>

@rpc
<strong>class</strong> <strong>TestService</strong>:

    <strong>def</strong> <strong>hello</strong>(<span style="color:#003388">self</span>, name):
        <strong>return</strong> <span style="color:#dd2200">"Hello, &#123;&#125;!"</span>.<span style="color:#0086b3">format</span>(name)

    <strong>async</strong> <strong>def</strong> <strong>add</strong>(<span style="color:#003388">self</span>, a, b, c):
        asyncio.sleep(<span style="color:#009999">1</span>)
        <strong>return</strong> a + b + c

@rpc
<strong>def</strong> <strong>hello</strong>(name):
    <strong>return</strong> <span style="color:#dd2200">"Hello, &#123;&#125;!"</span>.<span style="color:#0086b3">format</span>(name)

server = TcpRpcServer(<span style="color:#dd2200">'0.0.0.0'</span>, <span style="color:#009999">9988</span>)
server.serve()</pre> 
 </div> 
</div> 
<h3 style="text-align:left">TCP RPC 客户端</h3> 
<ul> 
 <li>创建TcpRpcClient对象，指定RPC服务端地址</li> 
 <li>通过call()方法，指定服务端方法名称和参数（注意：如果方法名不存在，或者服务端未调用@rpc装饰器注册，那么call()方法将抛出异常）</li> 
 <li>call() 方法的返回值和在本地调用一样，原来是什么返回类型，就还是什么（例如返回字典、列表、对象甚至内置类型，经过序列化后，不会发生改变）</li> 
</ul> 
<div style="text-align:left"> 
 <pre><strong>from</strong> <strong>agileutil.rpc.client</strong> <strong>import</strong> TcpRpcClient

cli = TcpRpcClient(<span style="color:#dd2200">'127.0.0.1'</span>, <span style="color:#009999">9988</span>, timeout = <span style="color:#009999">2</span>)

resp = cli.call(<span style="color:#dd2200">'TestService.hello'</span>, args=(<span style="color:#dd2200">'xiaoming'</span>,))

resp = cli.call(<span style="color:#dd2200">'TestService.add'</span>, args=(<span style="color:#009999">1</span>, <span style="color:#009999">2</span>, <span style="color:#009999">3</span>))

resp = cli.call(<span style="color:#dd2200">'hello'</span>, args=(<span style="color:#dd2200">'xiaoming'</span>,))
</pre> 
</div>
                                        </div>
                                      
</div>
            