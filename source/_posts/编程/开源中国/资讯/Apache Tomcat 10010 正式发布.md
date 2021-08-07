
---
title: 'Apache Tomcat 10.0.10 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5491'
author: 开源中国
comments: false
date: Sat, 07 Aug 2021 07:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5491'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Tomcat 10.0.10 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2F" target="_blank">发布</a>，此版本实现了作为 Jakarta EE 9 平台一部分的规范。</p> 
<p>在 Tomcat 9 和更早版本上运行的应用程序，如果不做修改，将无法在 Tomcat 10 上运行。为 Tomcat 9 和更早版本设计的基于 Java EE 的应用程序可以放在<code>$CATALINA_BASE/webapps-javaee</code>目录下，Tomcat 会自动将其转换为 Jakarta EE 并复制到 webapps 目录。这种转换是通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftomcat-jakartaee-migration" target="_blank">Apache Tomcat 的 Jakarta EE 迁移工具</a>进行的，此工具也可以单独下载，供离线使用。</p> 
<p>值得关注的变化：</p> 
<ul> 
 <li>修复先前版本 HTTP/2 流控制窗口管理中的回归问题</li> 
 <li>修复使用 NIO 时可能导致某些 TLS 连接挂起的回归问题</li> 
 <li>使用 GraalVM 原生镜像不再自动禁用 JMX 支持</li> 
</ul> 
<p>详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2Ftomcat-10.0-doc%2Fchangelog.html%23Tomcat_10.0.10_%28markt%29" target="_blank">Changelog</a>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2Fdownload-10.cgi" target="_blank">下载地址</a></p>
                                        </div>
                                      
</div>
            