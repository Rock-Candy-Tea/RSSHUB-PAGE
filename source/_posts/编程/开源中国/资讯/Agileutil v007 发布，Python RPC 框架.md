
---
title: 'Agileutil v0.0.7 发布，Python RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8799'
author: 开源中国
comments: false
date: Sat, 27 Mar 2021 16:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8799'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">        本次更新的版本是v0.0.7, 在v0.0.6的基础上，添加了TCP服务端的keepalive timeout设置。如果客户端长时间没有活动，达到超时时间后，服务端会主动关闭客户端连接，减少性能开销，节省系统资源，防止内存泄漏。</span></p> 
<p style="text-align:left">       当服务端主动关闭客户端连接后，如果客户端的client对象，后面继续调用call()方法请求，此时由于连接已被服务端关闭，已不可用，客户端会自动判断进行重连，对用户是透明的，因此用户可以无需关心连接被关闭的问题。</p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">       默认的keepalive timeout时间设置为和Nginx相同的75s 。</span>也支持自定义keepalive timeout时间，用户可以通调用setKeepaliveTime() 方法，参考下面的例子：</p> 
<pre><code class="language-python">from agileutil.rpc.server import TcpRpcServer

def sayHello(name):
    return 'hello ' + name

s = TcpRpcServer('0.0.0.0', 9988)
s.setKeepaliveTimeout(10) #那么客户端连接如果10秒内没有活动，将会被服务端主动关闭
s.regist(sayHello)
s.serve()</code></pre> 
<p>客户端</p> 
<pre><code class="language-python">from agileutil.rpc.client import TcpRpcClient
import time

cli = TcpRpcClient('127.0.0.1', 9988, timeout = 2)
resp = cli.call(func = 'sayHello', args=('zhangsan'))
print('resp', resp)
time.sleep(15)
resp = cli.call(func = 'sayHello', args=('zhangsan'))  #此时客户端会自动进行重连
print('resp', resp)</code></pre> 
<p style="text-align:left"> </p> 
<p style="text-align:left">详情访问</p> 
<p style="text-align:left">github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flycclsltt%2Fagileutil" target="_blank">https://github.com/lycclsltt/agileutil</a></p> 
<p style="text-align:left">gitee:   <a href="https://gitee.com/lycclsltt/agileutil">https://gitee.com/lycclsltt/agileutil</a></p>
                                        </div>
                                      
</div>
            