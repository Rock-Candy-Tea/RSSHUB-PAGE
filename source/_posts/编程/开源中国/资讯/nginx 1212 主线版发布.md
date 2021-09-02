
---
title: 'nginx 1.21.2 主线版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9436'
author: 开源中国
comments: false
date: Thu, 02 Sep 2021 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9436'
---

<div>   
<div class="content">
                                                                                            <p>nginx 1.21.2 主线版已发布，此版本引入了许多新特性、变更，以及 Bugfix，主要如下：</p> 
<ul> 
 <li>Change: nginx 现在会拒绝带有"Transfer-Encoding" header line 的 HTTP/1.0 请求</li> 
 <li>Change: 不再支持导出密码</li> 
 <li>Feature: 兼容 OpenSSL 3.0</li> 
 <li>Feature: "Auth-SSL-Protocol" 和 "Auth-SSL-Cipher" header lines 现在会被传递到邮件代理身份验证服务器</li> 
 <li>Feature: 请求正文过滤器 API 现在允许缓冲正在处理的数据</li> 
 <li>Bugfix: 修复 stream 模块中的后端 SSL 连接可能会在 SSL 握手后挂起的问题</li> 
 <li>Bugfix: 当在"ssl_ciphers"指令中设置"@SECLEVEL=N"时，OpenSSL 1.1.0 或更高版本中的安全级别不影响服务器证书的加载</li> 
 <li>Bugfix: 如果使用 select、poll 或/dev/poll 方法，包含 gRPC 后端的 SSL 连接可能会挂起</li> 
 <li>Bugfix: 使用 HTTP/2 客户端时，如果请求中不存在"Content-Length" header line，则请求正文会被写入磁盘</li> 
</ul> 
<p>更多内容查看 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2FCHANGES" target="_blank">Changelog</a>。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdownload.html" target="_blank">http://nginx.org/en/download.html</a></p>
                                        </div>
                                      
</div>
            