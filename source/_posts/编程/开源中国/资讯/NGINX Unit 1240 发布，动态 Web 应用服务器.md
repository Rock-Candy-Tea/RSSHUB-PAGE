
---
title: 'NGINX Unit 1.24.0 发布，动态 Web 应用服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1353'
author: 开源中国
comments: false
date: Sat, 29 May 2021 00:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1353'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2F%232021-05-27" target="_blank">NGINX Unit 1.24.0</a> 已发布，值得关注的更新内容包括：在静态媒体资源服务方面的改进、Node.js 的 "http" 和 "websocket" 模块支持自动重载、兼容 Ruby 3.0，以及支持应用 OpenSSL 配置命令等。</p> 
<p><strong>改进静态媒体资源服务</strong></p> 
<p>:: MIME Type Filtering ::</p> 
<p><span style="color:#000000">现在可以通过 MIME 类型限制文件服务：</span></p> 
<pre><code>  &#123;
      "share": "/www/data",
      "types": [ "image/*", "video/*" ]
  &#125;</code></pre> 
<p>上面的配置只允许请求有视频和图像扩展名的文件，所有其他请求将返回状态代码 403。</p> 
<pre><code> &#123;
      "share": "/www/data",
      "types": [ "!application/x-httpd-php" ],

      "fallback": &#123;
          "pass": "applications/php"
      &#125;
  &#125;
</code></pre> 
<p>上面这种情况<span style="color:#000000">除了“.php”之外的所有对现有文件的请求都将作为静态内容提供，而其余的将被传递给一个 PHP 应用程序。</span></p> 
<p>其他变化：</p> 
<ul> 
 <li>支持通过 OpenSSL 命令任意配置 TLS 连接</li> 
 <li>对于 Python 应用支持多 "target"</li> 
 <li>修复路由器进程可能会在关闭 TLS 连接时崩溃的错误</li> 
 <li>修复如果在启用 "auto_globals_jit" 选项的情况下使用 fastcgi_finish_request() ，则 PHP 模块中可能发生段错误的问题</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmailman.nginx.org%2Fpipermail%2Funit%2F2021-May%2F000265.html" target="_blank">详细更新内容点此查看</a>。</p> 
<p>NGINX Unit 是用于各种 Web 应用程序的轻量动态开源服务器。NGINX Unit 从头开始构建，可以一次运行多种语言版本的 Web 应用程序，它也可以在运行时完全配置为零中断，从而可以对工程和操作进行实时粒度管理。</p>
                                        </div>
                                      
</div>
            