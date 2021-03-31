
---
title: 'nginx 1.19.9 主线版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4868'
author: 开源中国
comments: false
date: Tue, 30 Mar 2021 23:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4868'
---

<div>   
<div class="content">
                                                                    
                                                        <p>nginx 1.19.9 主线版已发布，更新内容主要是 bugfix，具体如下：</p> 
<ul> 
 <li>Bugfix: 修复 nginx 在使用邮件代理模块 (mail proxy module) 时无法构建的问题，使用 ngx_mail_ssl_module 则正常。这个错误出现在 1.19.8 中</li> 
 <li>Bugfix: 修复当与 gRPC 后端搭配使用时，可能出现"upstream sent response body larger than indicated content length"错误。这个问题出现在 1.91.1 中</li> 
 <li>Bugfix: 如果客户端在丢弃请求体的同时关闭了连接，nginx 可能在 keepalive 超时前不会关闭连接</li> 
 <li>Bugfix: 当等待 auth_delay 或 limit_req 延迟时，或者与后端一起搭配使用时，nginx 可能无法检测到客户端已经关闭的连接</li> 
 <li>Bugfix: 修复 eventport 方法中的错误</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdownload.html" target="_blank">下载地址</a> | <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2FCHANGES" target="_blank">更新说明</a></p>
                                        </div>
                                      
</div>
            