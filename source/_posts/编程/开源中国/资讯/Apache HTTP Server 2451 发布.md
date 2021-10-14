
---
title: 'Apache HTTP Server 2.4.51 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7537'
author: 开源中国
comments: false
date: Thu, 14 Oct 2021 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7537'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache HTTP Server 2.4.51 已发布，2.4.51 主要是修复了在 2.4.50 中发现的安全问题，因此主要的变动是在 2.4.50 中，包括修复安全问题和部分 bug，以及增强功能。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhttpd.apache.org%2Fdownload.cgi" target="_blank">https://httpd.apache.org/download.cgi</a></p> 
<ul> 
 <li>mod_rewrite: 修复 [P] 规则的 UDS ("unix:") scheme</li> 
 <li>event mpm: 如果子进程由于 MaxConnectionsPerChild 而死亡，可正确地计算父进程中的活动子进程</li> 
 <li>mod_http2: 当一个服务器被优雅地重新启动时，任何空闲的 h2 worker 线程都会被立即关闭。另外，针对 OpenSSL 3.0 中的弃用情况，改变了 OpenSSL API 的使用方式，增加了所有其他的、从未提议过的代码修改，以便对 http2 源进行干净的同步</li> 
 <li>mod_dav: 正确处理由 dav providers 在 REPORT 请求中返回的错误</li> 
 <li>core: 不在二级连接上安装核心输入/输出过滤器</li> 
 <li>core: 添加 ap_pre_connection() 作为 ap_run_pre_connection() 的封装器，用它来防止运行 pre_connection 钩子的失败导致事后崩溃</li> 
 <li>mod_speling: 添加 CheckBasenameMatch PR 44221</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlcdn.apache.org%2F%2Fhttpd%2FCHANGES_2.4.50" target="_blank">详情查看 Changelog</a>。    </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Apache HTTP Server（简称 Apache）是开源的 Web 服务器，可以在大多数计算机操作系统中运行，由于其多平台和安全性被广泛使用，是最流行的 Web 服务器端软件之一。它快速、可靠并且可通过简单的 API 扩展，将 Perl/Python 等解释器编译到服务器中。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Apache HTTP Server 2.4.x 需要 Apache Portable Runtime（APR）最低版本 1.5.x 和 APR-Util 最低版本 1.5.x. 某些功能可能需要 APR 和 APR-Util 的 1.6.x 版本， 必须升级 APR 库才能使 httpd 的所有功能正常运行。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本基于并扩展了 Apache 2.2 API。 为 Apache 2.2 运行需要重新编译为 Apache 2.2 编写的模块，并且需要很少或不需要更改源代码。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在升级或安装此版本时，请记住，如果你打算将它与其中一个线程 MPM（Prefork MPM 除外）一起使用，则必须确保你将使用的任何模块（以及它们所依赖的库）是线程安全的。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.2.x 分支现在已经过了 Apache HTTP Server 项目的生命周期，并且不会再发生任何变动，包括安全补丁。用户必须及时完成对 httpd 的 2.4.x 版本的过渡，以便从进一步的错误修复或新功能中受益。</p>
                                        </div>
                                      
</div>
            