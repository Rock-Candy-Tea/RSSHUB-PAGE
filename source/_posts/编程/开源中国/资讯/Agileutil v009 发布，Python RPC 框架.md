
---
title: 'Agileutil v0.0.9 发布，Python RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8015'
author: 开源中国
comments: false
date: Tue, 30 Mar 2021 11:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8015'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">本次更新的版本是v0.0.9, 支持通过@rpc 注册方法。</span></p> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>from</strong> <strong>agileutil.rpc.server</strong> <strong>import</strong> TcpRpcServer
from agileutil.rpc import rpc

@rpc
<strong>def</strong> <strong>sayHello</strong>(name):
    <strong>return</strong> <span style="color:#dd2200">'hello '</span> + name

nationServer = TcpRpcServer(<span style="color:#dd2200">'0.0.0.0'</span>, <span style="color:#009999">9988</span>, workers=<span style="color:#009999">4</span>)
nationServer.serve()</pre> 
 </div> 
</div> 
<blockquote> 
 <p>除了使用@rpc注册方法，还可以使用regist()方法，参考下面的例子</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>from</strong> <strong>agileutil.rpc.server</strong> <strong>import</strong> TcpRpcServer

<strong>def</strong> <strong>sayHello</strong>(name):
    <strong>return</strong> <span style="color:#dd2200">'hello '</span> + name

nationServer = TcpRpcServer(<span style="color:#dd2200">'0.0.0.0'</span>, <span style="color:#009999">9988</span>, workers=<span style="color:#009999">4</span>)
nationServer.regist(sayHello)
nationServer.serve()</pre> 
 </div> 
</div> 
<p><span style="background-color:#ffffff; color:#333333"> 详情: </span></p> 
<p><span style="background-color:#ffffff; color:#333333"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flycclsltt%2Fagileutil" target="_blank">Github</a></span> </p> 
<p><a href="https://gitee.com/lycclsltt/agileutil">Gitee</a></p>
                                        </div>
                                      
</div>
            