
---
title: 'lighttpd 1.4.65 发布，支持基于 HTTP_2 的 WebSockets'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8078'
author: 开源中国
comments: false
date: Sat, 11 Jun 2022 07:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8078'
---

<div>   
<div class="content">
                                                                                            <p>lighttpd 发布了 1.4.65 版本，lighttpd 是开源 Web 服务器，专门针对高性能环境进行了优化，具有安全、快速、兼容性好且灵活的特点。lighttpd 可有效地使用内存和 CPU，并且比其他流行的 Web 服务器具有更低的资源使用率。它的高级功能集包括 FastCGI、CGI、Auth、输出压缩和 URL 重写等。</p> 
<p><strong>新版本亮点特性</strong></p> 
<ul> 
 <li>支持基于 HTTP/2 的 WebSockets<br> RFC 8441 Bootstrapping WebSockets with HTTP/2</li> 
 <li>支持 HTTP/2 PRIORITY_UPDATE<br> RFC 9218 Extensible Prioritization Scheme for HTTP</li> 
 <li>为 lighttpd.conf 引入前缀/后缀条件</li> 
 <li>mod_webdav safe partial-PUT<br> webdav.opts += (“partial-put-copy-modify” => “enable”)</li> 
 <li>mod_accesslog option: accesslog.escaping = “json”</li> 
 <li>mod_deflate libdeflate build option</li> 
 <li>通过 HTTP/2 的 "PRIORITY_UPDATE" 提升 request body 上传速度</li> 
</ul> 
<p><strong>部分改动</strong></p> 
<ul> 
 <li>更改默认的 server.max-keep-alive-requests = 1000，以适应增加的 HTTP/2 使用和 web2/web3 应用程序使用（之前的默认值为 100）<br> mod_status HTML 现在在输出中引入HTTP/2 control stream id 0，其中包含 HTTP/2 连接的聚合计数<br> MIME 类型 application/javascript 被转换为 text/javascript (RFC 9239)</li> 
</ul> 
<p><strong>未来计划</strong></p> 
<ul> 
 <li>TLS 模块将默认使用更强大的现代密码，并且默认允许客户端选择密码。</li> 
 <li>不推荐使用的 <span style="color:#333333">TLS </span>选项将被删除</li> 
 <li>逐步弃用“mini-application” lighttpd 模块，替代方案 mod_magnet lua 具有更好的实现和灵活性</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.lighttpd.net%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            