
---
title: 'nginx 1.21.1 主线版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=355'
author: 开源中国
comments: false
date: Thu, 08 Jul 2021 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=355'
---

<div>   
<div class="content">
                                                                    
                                                        <p>nginx 1.21.1 主线版已发布，此版本包含许多变更和 Bugfix，主要如下：</p> 
<ul> 
 <li>Change：nginx 现在对 CONNECT 方法会返回错误</li> 
 <li>Change：如果请求中同时出现 "Content-Length" 和 "Transfer-Encoding" header line，nginx 现在会返回错误</li> 
 <li>Change：如果请求行中使用空格或控制字符，nginx 现在会返回错误</li> 
 <li>Change：如果在 header name 中使用空格或控制字符，nginx 现在会返回错误</li> 
 <li>Change：如果在 "Host" 请求 header 行中使用空格或控制字符，nginx 现在会返回错误</li> 
 <li>Change：优化了使用许多监听套接字时的配置测试</li> 
 <li>Bugfix：修复代理使用修改后的 URL 时，nginx 没有对 """, "<", ">", "\", "^", "`", "&#123;", "|", 和 "&#125;" 字符进行转义的错误</li> 
 <li>Bugfix：修复 SSL 变量在日志中使用时可能为空的错误</li> 
 <li>Bugfix：修复与 gRPC 后端建立的 keepalive 连接在收到 GOAWAY 帧后可能不会被关闭的问题</li> 
 <li>Bugfix：当代理的缓冲区超过 64 buffer 时，减少长寿命请求的内存消耗</li> 
</ul> 
<p>更多内容查看 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2FCHANGES" target="_blank">Changelog</a>。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdownload.html" target="_blank">http://nginx.org/en/download.html</a></p>
                                        </div>
                                      
</div>
            