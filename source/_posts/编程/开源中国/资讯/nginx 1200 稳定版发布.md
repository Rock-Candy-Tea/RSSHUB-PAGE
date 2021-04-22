
---
title: 'nginx 1.20.0 稳定版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5145'
author: 开源中国
comments: false
date: Wed, 21 Apr 2021 23:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5145'
---

<div>   
<div class="content">
                                                                    
                                                        <p>nginx 最新稳定分支 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2F%232021-04-20" target="_blank">1.20</a> 已发布，新版本引入了来自 1.19.x 主线分支的新功能和错误修复，其中包括：</p> 
<ul> 
 <li>使用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_ssl_module.html%23ssl_ocsp" target="_blank">OCSP</a> 进行客户端 SSL 证书验证</li> 
 <li>引入 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_ssl_module.html%23ssl_reject_handshake" target="_blank">ssl_reject_handshake</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_ssl_module.html%23ssl_conf_command" target="_blank">ssl_conf_command</a> 指令</li> 
 <li>使用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_core_module.html%23lingering_close" target="_blank">lingering_close</a>, <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_core_module.html%23keepalive_timeout" target="_blank">keepalive_timeout</a>, <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_core_module.html%23keepalive_time" target="_blank">keepalive_time</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_core_module.html%23keepalive_requests" target="_blank">keepalive_requests</a> 指令简化和提升对 HTTP/2 连接的处理</li> 
 <li>以严格模式处理上游服务器的响应</li> 
 <li>支持处理 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_proxy_module.html%23proxy_cookie_flags" target="_blank">cookie flags</a></li> 
 <li>基于<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_proxy_module.html%23proxy_cache_path_max_size" target="_blank">最小可用空间</a>的缓存清除</li> 
 <li>从客户端和邮件代理的后端服务器均支持 PROXY 协议</li> 
 <li>支持在 SMTP 代理后端启用用户身份验证</li> 
 <li>stream 模块新增 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fstream%2Fngx_stream_set_module.html" target="_blank">set</a> 指令</li> 
 <li>……</li> 
</ul> 
<p>具体每个指令的介绍，访问<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2F%232021-04-20" target="_blank">此链接</a>进行查看。</p> 
<p>nginx 1.20.0 下载地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdownload.html" target="_blank">http://nginx.org/en/download.html</a></p> 
<p>根据 nginx 发布新版的策略，<strong>“稳定”指的是功能和更新频率，它与软件质量无关</strong>。稳定分支在其生命周期中从不接收新功能，并且通常仅接收一个或两个更新，用于修复严重的错误。另外，稳定版本通常 fork 自最新的 mainline 版本，它继承了过去一年中最新 mainline 分支的所有 bugfix 补丁、新增功能和其他变更。</p>
                                        </div>
                                      
</div>
            