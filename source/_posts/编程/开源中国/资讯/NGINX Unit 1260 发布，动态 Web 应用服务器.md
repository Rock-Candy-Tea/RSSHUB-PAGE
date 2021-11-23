
---
title: 'NGINX Unit 1.26.0 发布，动态 Web 应用服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1720'
author: 开源中国
comments: false
date: Tue, 23 Nov 2021 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1720'
---

<div>   
<div class="content">
                                                                    
                                                        <p>NGINX Unit 1.26.0 已发布，此版本在静态内容服务、应用程序范围的 PHP opcache 方面有多项改进，此外还修复了部分错误。</p> 
<ul> 
 <li>Change："share" 选项现在会指定它所服务的文件的整个路径，而不是在请求 URI 中预置一个文件根目录</li> 
 <li>Feature：当从旧版本进行更新时，自动调整现有的配置到新的 "share" 行为</li> 
 <li>Feature：在 "share" 选项中支持变量</li> 
 <li>Feature：在 "share" 选项中支持多路径</li> 
 <li>Feature：在 "chroot" 选项中支持变量</li> 
 <li>Feature：支持在应用程序进程之间共享 PHP opcache</li> 
 <li>Feature：通过查询字符串进行请求路由</li> 
 <li>Bugfix：修复当异步或多线程应用程序达到请求限制时，路由和应用程序进程可能崩溃的问题</li> 
 <li>Bugfix：修复已建立的 WebSocket 连接在相应的监听器被重新配置后可能停止从客户端读取帧的问题</li> 
 <li>Bugfix：修复使用 glibc 2.34 进行构建时的问题，特别是在 Fedora 35 中</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmailman.nginx.org%2Fpipermail%2Funit%2F2021-November%2F000288.html" target="_blank">详情查看发布公告</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">NGINX Unit 是用于各种 Web 应用程序的轻量动态开源服务器。NGINX Unit 从头开始构建，可以一次运行多种语言版本的 Web 应用程序，它也可以在运行时完全配置为零中断，从而可以对工程和操作进行实时粒度管理。</p>
                                        </div>
                                      
</div>
            