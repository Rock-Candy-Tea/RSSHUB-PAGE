
---
title: 'nginx 1.21.4 主线版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3935'
author: 开源中国
comments: false
date: Thu, 04 Nov 2021 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3935'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">nginx 1.21.4 主线版已发布，此版本引入了许多新特性、变化，以及错误修复，更新内容如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Change：支持 NPN 而不是 ALPN 来建立 HTTP/2 连接已被删除；</li> 
 <li>Change：如果客户端使用 ALPN，现在 nginx 会拒绝 SSL 连接；</li> 
 <li>Change："sendfile_max_chunk" 指令的默认值被改为 2 兆字节；</li> 
 <li>Feature：Stream 模块中新增 "proxy_half_close" 指令；</li> 
 <li>Feature：Stream 模块中新增 "ssl_alpn" 指令；</li> 
 <li>Feature：新增 $ssl_alpn_protocol 变量；</li> 
 <li>Feature：在使用 OpenSSL 3.0 时支持 SSL_sendfile()；</li> 
 <li>Feature：在 ngx_http_mp4_module 中新增 "mp4_start_key_frame" 指令；</li> 
 <li>Bugfix：修复在使用分块传输编码时在 $content_length 变量中的错误；</li> 
 <li>Bugfix：从代理后端收到一个长度不正确的响应后，nginx 可能会缓存连接；</li> 
 <li>Bugfix：来自后端的无效 headers 信息被记录在 "info" 而不是 "error" 中，这个问题在 1.21.1 版本中出现；</li> 
 <li>Bugfix：使用 HTTP/2 和 "aio_write" 指令时，请求可能会挂起；</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnginx.org%2Fen%2FCHANGES" target="_blank">https://nginx.org/en/CHANGES</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            