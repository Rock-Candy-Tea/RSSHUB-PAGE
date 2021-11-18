
---
title: 'nginx 1.20.2 稳定版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7713'
author: 开源中国
comments: false
date: Thu, 18 Nov 2021 08:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7713'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">nginx 1.20.2 稳定版的变化如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>特性：兼容 OpenSSL 3.0</li> 
 <li>错误修正：SSL 变量在日志中使用时可能为空，该错误在 1.19.5 版本中出现过</li> 
 <li>错误修正：与 gRPC 后端建立的 keepalive 连接在收到 GOAWAY 帧后可能不会被关闭</li> 
 <li>错误修正：流模块中的后端 SSL 连接可能在 SSL 握手后挂起</li> 
 <li>错误修正：如果使用 select、poll 或 /dev/poll 方法，与 gRPC 后端的 SSL 连接可能会挂起</li> 
 <li>错误修正：当使用 HTTP/2 和 "aio_write" 指令时，请求可能会挂起</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnginx.org%2Fen%2FCHANGES-1.20" target="_blank">https://nginx.org/en/CHANGES-1.20</a></p>
                                        </div>
                                      
</div>
            