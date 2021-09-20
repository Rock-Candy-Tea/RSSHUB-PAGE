
---
title: 'Apache HTTP Server 2.4.49 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4937'
author: 开源中国
comments: false
date: Mon, 20 Sep 2021 08:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4937'
---

<div>   
<div class="content">
                                                                                            <div>
 Apache HTTP Server 2.4.49 已发布，此版本修复了安全问题和部分 bug，以及增强功能。
</div> 
<div>
  
</div> 
<div>
 下载地址：
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhttpd.apache.org%2Fdownload.cgi" target="_blank">https://httpd.apache.org/download.cgi</a>
</div> 
<div> 
 <p><br> SECURITY: CVE-2021-40438 (cve.mitre.org)<br> mod_proxy: 修复 Server Side Request Forgery (SSRF) 的安全漏洞</p> 
 <p>SECURITY: CVE-2021-39275 (cve.mitre.org)<br> core: 修复 ap_escape_quotes 的缓存移除问题</p> 
 <p>SECURITY: CVE-2021-36160 (cve.mitre.org)<br> mod_proxy_uwsgi: 修复超出边界的读取漏洞</p> 
 <p>SECURITY: CVE-2021-34798 (cve.mitre.org)<br> core: malformed 请求中的<span style="background-color:#ffffff; color:#000000">空指针解除引用</span></p> 
 <p>SECURITY: CVE-2021-33193 (cve.mitre.org)<br> mod_http2: 使用 mod_proxy 时出现的请求拆分漏洞 (Request splitting)</p> 
 <div> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlcdn.apache.org%2F%2Fhttpd%2FCHANGES_2.4.49" target="_blank">https://dlcdn.apache.org//httpd/CHANGES_2.4.49</a></p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Apache HTTP Server（简称 Apache）是开源的 Web 服务器，可以在大多数计算机操作系统中运行，由于其多平台和安全性被广泛使用，是最流行的 Web 服务器端软件之一。它快速、可靠并且可通过简单的 API 扩展，将 Perl/Python 等解释器编译到服务器中。</p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Apache HTTP Server 2.4.x 需要 Apache Portable Runtime（APR）最低版本 1.5.x 和 APR-Util 最低版本 1.5.x. 某些功能可能需要 APR 和 APR-Util 的 1.6.x 版本， 必须升级 APR 库才能使 httpd 的所有功能正常运行。</p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本基于并扩展了 Apache 2.2 API。 为 Apache 2.2 运行需要重新编译为 Apache 2.2 编写的模块，并且需要很少或不需要更改源代码。</p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在升级或安装此版本时，请记住，如果你打算将它与其中一个线程 MPM（Prefork MPM 除外）一起使用，则必须确保你将使用的任何模块（以及它们所依赖的库）是线程安全的。</p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.2.x 分支现在已经过了 Apache HTTP Server 项目的生命周期，并且不会再发生任何变动，包括安全补丁。用户必须及时完成对 httpd 的 2.4.x 版本的过渡，以便从进一步的错误修复或新功能中受益。</p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            