
---
title: 'NGINX Unit 1.25.0 发布，动态 Web 应用服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=144'
author: 开源中国
comments: false
date: Sat, 21 Aug 2021 23:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=144'
---

<div>   
<div class="content">
                                                                                            <p>NGINX Unit 1.25.0 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2F%232021-08-19" target="_blank">已发布</a>，主要变化包括新增 SSL/TLS 会话缓存和凭据管理、识别发送端 IP、支持手动重启应用，以及错误修复等。</p> 
<ul> 
 <li>特性：从指定的 HTTP header 字段替换客户端 IP 地址</li> 
 <li>特性：新增 TLS 会话缓存</li> 
 <li>特性：新增 TLS 会话凭据</li> 
 <li>特性：应用程序重启控制</li> 
 <li>特性：新增 Ruby 中的进程和线程生命周期钩子</li> 
 <li>Bugfix：当配置了多个具有 TLS 证书的监听器时，路由器进程可能会在 TLS 连接打开时崩溃；该错误有出现在 1.23.0</li> 
 <li>Bugfix：如果客户端没有使用 SNI，在监听器中有多个证书包的配置中，TLS 连接被拒绝</li> 
 <li>Bugfix：路由器进程在频繁的多线程应用程序重新配置时可能会崩溃</li> 
 <li>Bugfix：修复与某些 Python ASGI 应用程序的兼容性问题，尤其是基于 Starlette 框架</li> 
 <li>Bugfix：修复当一个应用程序进程停止或崩溃时，路由器进程会发生描述符和内存泄漏的错误</li> 
 <li>Bugfix：如果配置中的监听器地址包含完整格式的 IPv6，控制器或路由器进程可能崩溃</li> 
 <li>Bugfix：当一个请求被传递到一个空的使用可变的"pass"选项的"routes"或"upstreams"时，路由器进程会崩溃</li> 
 <li>Bugfix：当请求与一个空的源地址或目的地址模式数组相匹配时，路由器进程崩溃</li> 
</ul> 
<p>详情查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmailman.nginx.org%2Fpipermail%2Funit%2F2021-August%2F000278.html" target="_blank">发布公告</a>。</p> 
<p>NGINX Unit 是用于各种 Web 应用程序的轻量动态开源服务器。NGINX Unit 从头开始构建，可以一次运行多种语言版本的 Web 应用程序，它也可以在运行时完全配置为零中断，从而可以对工程和操作进行实时粒度管理。</p>
                                        </div>
                                      
</div>
            