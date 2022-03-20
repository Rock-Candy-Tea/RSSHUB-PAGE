
---
title: 'RRQMSocket v7.0.1 发布，网络通信服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8032'
author: 开源中国
comments: false
date: Sun, 20 Mar 2022 10:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8032'
---

<div>   
<div class="content">
                                                                                            <p>RRQMSocket v7.0.1 已经发布，网络通信服务框架</p> 
<p>此版本更新内容包括：</p> 
<p>版本号:7.0</p> 
<p>更新日期：2022.2.20</p> 
<p>更新描述：本次升级兼容6.6版本，但请务必客户端同步更新，RPC代理请重新生成，部分类命名空间修改， 请智能提示。由于Token连接修改，RPC工具强制升级。</p> 
<p>【RRQMCore】</p> 
<ul> 
 <li>增加：AppConfigBase，更加方便的使用APP配置文件。</li> 
 <li>增加：FileLogger，将日志按日期在本地文件保存。</li> 
 <li>增加：LoggerGroup，能够在一个日志记录中，使用多个记录器。</li> 
 <li>修改：Log修改为ConsoleLogger，将日志进行控制台输出。</li> 
</ul> 
<p>【RRQMSocket】</p> 
<ul> 
 <li>增加：SocketClient可直接通过ID向同服务器的其他客户端发送数据。</li> 
 <li>增加：Token及其派生系，也可使用断线重连。</li> 
 <li>增加：TcpService系增加IDChanged事件。</li> 
 <li>修改：Token系的验证令箭方式，采用json字符验证，让常规TCP也能模仿鉴权。 优化：NATService，可转发至多个目标端口。</li> 
 <li>删除：客户端配置移除OnlySend属性，由ReceiveType.None代替。</li> 
</ul> 
<p>【RRQMSocket.RPC】</p> 
<ul> 
 <li>增加：InvokeAsync方法。</li> 
 <li>增加：RpcSocketClient可通过ID直接反向调用其他客户端RPC。</li> 
 <li>优化：生成代理的代码包含异常提示。</li> 
 <li>修改：EventBus，有ID代替发布者验证。</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/dotnetchina/RRQMSocket/releases/v7.0.1">https://gitee.com/dotnetchina/RRQMSocket/releases/v7.0.1</a></p>
                                        </div>
                                      
</div>
            