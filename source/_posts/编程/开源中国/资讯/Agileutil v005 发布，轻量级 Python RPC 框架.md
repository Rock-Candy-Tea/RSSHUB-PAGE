
---
title: 'Agileutil v0.0.5 发布，轻量级 Python RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=642'
author: 开源中国
comments: false
date: Wed, 24 Mar 2021 18:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=642'
---

<div>   
<div class="content">
                                                                                            <h4><strong><span style="background-color:#ffffff; color:#333333">本次更新的版本是v0.0.5：</span></strong></h4> 
<p>1.解决了TCP服务端由于未能发现客户端断开链接，线程不退出，导致机器负载飙高的问题</p> 
<p>2.去除了server端非必要的Queue等对象，减少了内存开销</p> 
<p>3.客户端支持通过servers参数，指定多个服务端地址，支持轮询的负载均衡策略和重试机制。</p> 
<p> </p> 
<h4 style="text-align:left">指定多个服务端地址</h4> 
<ul> 
 <li>通过servers参数，你也可以创建一个指定多个服务端地址的client对象，默认采用轮询的负载均衡策略，将请求转发到多个server上，如果请求其中一个server出现了失败，那么会自动重试。框架中所有TCP/UDP/HTTP的client都支持servers参数，都可以指定多个服务端地址，参考下面的例子:</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>from</strong> <strong>agileutil.rpc.client</strong> <strong>import</strong> TcpRpcClient

c = TcpRpcClient(servers = [<span style="color:#dd2200">'127.0.0.1:9988'</span>, <span style="color:#dd2200">'127.0.0.1:9989'</span>])
resp = c.call(func = <span style="color:#dd2200">'sayHello'</span>, args = (<span style="color:#dd2200">'zhangsan'</span>))
<strong>print</strong>(<span style="color:#dd2200">'resp'</span>, resp)</pre> 
 </div> 
</div> 
<blockquote> 
 <p>注意： 如果通过servers参数指定了多个服务端地址，又同时指定了服务发现的consul地址，那么实际请求的服务端节点是由server参数决定的，所以使用时请注意不要和服务发现同时使用。</p> 
</blockquote> 
<p>详情访问 </p> 
<p><a href="https://gitee.com/lycclsltt/agileutil">https://gitee.com/lycclsltt/agileutil</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flycclsltt%2Fagileutil" target="_blank">https://github.com/lycclsltt/agileutil</a></p>
                                        </div>
                                      
</div>
            