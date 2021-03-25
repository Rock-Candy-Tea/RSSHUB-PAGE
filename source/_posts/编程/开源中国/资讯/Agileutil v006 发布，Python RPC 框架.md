
---
title: 'Agileutil v0.0.6 发布，Python RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=36'
author: 开源中国
comments: false
date: Thu, 25 Mar 2021 17:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=36'
---

<div>   
<div class="content">
                                                                                            <h4 style="text-align:left"><strong><span style="background-color:#ffffff; color:#333333">本次更新的版本是v0.0.6：</span></strong></h4> 
<p style="text-align:left">1.TCP/HTTP/UDP client 都支持了设置timeout</p> 
<p style="text-align:left">2.<span style="background-color:#f7f7f7; color:#262626">解决了客户端请求UDP协议RPC服务端时，请求失败情况下，客户端不能正常抛出异常的问题</span></p> 
<p style="text-align:left"><span style="background-color:#f7f7f7; color:#262626">3.解决timeout场景下，由于tcp粘包，超时后的新请求，接收到之前请求结果数据的bug. </span></p> 
<p style="text-align:left"> </p> 
<p style="text-align:left">客户端指定超时时间：</p> 
<pre style="text-align:left"><strong><span style="color:#d73a49">from</span></strong> <strong>agileutil.rpc.client</strong> <strong><span style="color:#d73a49">import</span></strong> TcpRpcClient

c = TcpRpcClient(servers = [<span style="color:#dd2200"><span style="color:#032f62">'127.0.0.1:9988'</span></span>, <span style="color:#dd2200"><span style="color:#032f62">'127.0.0.1:9989'</span></span>], timeout=4)
resp = c.call(func = <span style="color:#dd2200"><span style="color:#032f62">'sayHello'</span></span>, args = (<span style="color:#dd2200"><span style="color:#032f62">'zhangsan'</span></span>))
<strong>print</strong>(<span style="color:#dd2200"><span style="color:#032f62">'resp'</span></span>, resp)</pre>
                                        </div>
                                      
</div>
            