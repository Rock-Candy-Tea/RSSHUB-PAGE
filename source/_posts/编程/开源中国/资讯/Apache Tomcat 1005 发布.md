
---
title: 'Apache Tomcat 10.0.5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8477'
author: 开源中国
comments: false
date: Fri, 09 Apr 2021 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8477'
---

<div>   
<div class="content">
                                                                                            <p>Tomcat 10.0.x 系列的目标平台是 Jakarta EE 9。官方表示，Tomcat 10 及更高版本的用户应注意，作为从 Java EE 迁移到 Eclipse Foundation 的的一部分，从 Java EE 迁移到 Jakarta EE 的结果是所有已实现 API 的主要软件包已从 javax. 改为 jakarta.，因此部分项目会需要更改代码，以使应用程序能够从 Tomcat 9 及更低版本迁移到 Tomcat 10 及更高版本。官方表示正在开发一种迁移工具来辅助此过程。</p> 
<p>与 10.0.4 相比，显著的变化包括：</p> 
<ul> 
 <li>修复了 10.0.4 中的回归，这意味着异步读取期间的错误破坏了与同一请求实例关联的所有将来的异步读取；</li> 
 <li>防止对 ServletInputStream.isReady() 的并发调用破坏输入缓冲区；</li> 
 <li>将 Tomcat Native 的打包版本更新为 1.2.27，以获取使用 OpenSSL 1.1.1k 构建的二进制文件。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2Ftomcat-10.0-doc%2Fchangelog.html" target="_blank">https://tomcat.apache.org/tomcat-10.0-doc/changelog.html</a></p>
                                        </div>
                                      
</div>
            