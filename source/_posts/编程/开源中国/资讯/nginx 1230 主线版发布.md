
---
title: 'nginx 1.23.0 主线版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6113'
author: 开源中国
comments: false
date: Thu, 23 Jun 2022 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6113'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">nginx 1.23.0 主线版已发布。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">主要变化</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>内部 API 变化：header 头现在以链表 (linked lists) 形式展示。</li> 
 <li>nginx 将数据发送到 FastCGI、SCGI 和 uwsgi 后端时，在 ngx_http_perl_module 的 $r->header_in() 方法中，以及在查找 "$http_...", "$sent_http_...", "$sent_trailer_...", "$upstream_http_..." 和 "$upstream_trailer_..." 变量期间，会组合具有完全相同名称的任意 header 头。</li> 
 <li>Bugfix：如果后端响应中有多个 "Vary" header 头，nginx 仅在缓存时使用最后一个。</li> 
 <li>Bugfix：如果后端响应中有多个 "WWW-Authenticate" header 头，并且代码 401 的错误被拦截或使用了“auth_request”指令，则 nginx 仅将第一个 header 头发送到客户端。</li> 
 <li>Change: the logging level of the "application data after close notify" SSL errors has been lowered from "crit" to "info".</li> 
 <li>"application data after close notify" SSL 的错误日志记录级别已从 "crit" 降低到 "info"。</li> 
 <li>Bugfix：如果 nginx 是在 Linux 2.6.17 或更高版本上构建的，但在不支持 EPOLLRDHUP 的系统上使用，尤其是在具有 epoll 仿真层的系统上使用时，连接可能会挂起；该错误已在 1.17.5 中复现。</li> 
 <li>Bugfix：如果"Expires"响应 header 头禁用缓存，nginx 不会缓存响应，但会遵循 "Cache-Control" header 头启用缓存</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2FCHANGES" target="_blank">Changelog</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdownload.html" target="_blank">下载地址</a></p>
                                        </div>
                                      
</div>
            