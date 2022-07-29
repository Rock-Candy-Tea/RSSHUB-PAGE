
---
title: 'Apache Tomcat 10.0.23 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8280'
author: 开源中国
comments: false
date: Fri, 29 Jul 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8280'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Apache Tomcat 10.0.23 现已</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2F" target="_blank"><span style="color:#000000">发布</span></a><span style="color:#000000">，此版本实现了作为 Jakarta EE 9 平台一部分的规范。</span></p> 
<p style="margin-left:0"><span style="color:#000000">在 Tomcat 9 和更早版本上运行的应用程序，如果不做修改，将无法在 Tomcat 10 上运行。为 Tomcat 9 和更早版本设计的基于 Java EE 的应用程序可以放在<code>$CATALINA_BASE/webapps-javaee</code>目录下，Tomcat 会自动将其转换为 Jakarta EE 并复制到 webapps 目录。此转换是通过 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftomcat-jakartaee-migration" target="_blank">Apache Tomcat 的 Jakarta EE 迁移工具</a><span style="color:#000000">进行的，此工具也可以单独</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2Fdownload-migration.cgi" target="_blank"><span style="color:#000000">下载</span></a><span style="color:#000000">，供离线使用。</span></p> 
<p style="margin-left:0"><span style="color:#000000">此版本中一些值得关注的变化有：</span></p> 
<ul> 
 <li>实现对可重复构建的支持</li> 
 <li>将 Tomcat Native Library 的打包版本更新为 1.2.35。这包括使用 OpenSSL 1.1.1q 构建的 Windows 二进制文件。</li> 
 <li>修复 Form 认证示例中的低严重性 XSS 漏洞 CVE-2022-34305</li> 
</ul> 
<p style="margin-left:0">更多详情可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2Ftomcat-10.0-doc%2Fchangelog.html%23Tomcat_10.0.23_%28markt%29" target="_blank">changelog</a>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2Fdownload-10.cgi" target="_blank">Download</a></p>
                                        </div>
                                      
</div>
            