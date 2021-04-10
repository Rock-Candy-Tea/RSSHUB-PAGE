
---
title: 'Agileutil v0.0.14 发布，超简单、易用的轻量级 Python3 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9004'
author: 开源中国
comments: false
date: Fri, 09 Apr 2021 17:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9004'
---

<div>   
<div class="content">
                                                                                            <p>本次更新的版本是v0.0.14, 支持通过@rpc装饰器修饰一个类。</p> 
<p style="text-align:left">下面是一个TCP协议的服务端例子。</p> 
<ul> 
 <li>创建一个TcpRpcServer对象, 指定服务端监听地址和端口</li> 
 <li>通过@rpc装饰器注册需要被客户端请求的方法</li> 
 <li>调用serve()方法，开始处理客户端请求</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>from</strong> <strong>agileutil.rpc.server</strong> <strong>import</strong> TcpRpcServer, rpc

@rpc
<strong>class</strong> <strong>TestService</strong>:

    <strong>def</strong> <strong>hello</strong>(<span style="color:#003388">self</span>, name):
        <strong>return</strong> <span style="color:#dd2200">"Hello, &#123;&#125;!"</span>.<span style="color:#0086b3">format</span>(name)

    <strong>def</strong> <strong>add</strong>(<span style="color:#003388">self</span>, a, b, c):
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
 <div> 
  <pre><strong>from</strong> <strong>agileutil.rpc.client</strong> <strong>import</strong> TcpRpcClient

cli = TcpRpcClient(<span style="color:#dd2200">'127.0.0.1'</span>, <span style="color:#009999">9988</span>, timeout = <span style="color:#009999">2</span>)
resp = cli.call(<span style="color:#dd2200">'TestService.hello'</span>, args=(<span style="color:#dd2200">'xiaoming'</span>,))
<strong>print</strong>(resp)
resp = cli.call(<span style="color:#dd2200">'TestService.add'</span>, args=(<span style="color:#009999">1</span>, <span style="color:#009999">2</span>, <span style="color:#009999">3</span>))
<strong>print</strong>(resp)
resp = cli.call(<span style="color:#dd2200">'hello'</span>, args=(<span style="color:#dd2200">'xiaoming'</span>,))
<strong>print</strong>(resp)</pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            