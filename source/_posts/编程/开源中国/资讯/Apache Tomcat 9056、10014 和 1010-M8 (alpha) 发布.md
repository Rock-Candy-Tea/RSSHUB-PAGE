
---
title: 'Apache Tomcat 9.0.56、10.0.14 和 10.1.0-M8 (alpha) 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5016'
author: 开源中国
comments: false
date: Sun, 12 Dec 2021 08:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5016'
---

<div>   
<div class="content">
                                                                                            <p>Apache Tomcat 的三个分支发布了更新，分别是 9.0.56、10.0.14 和 10.1.0-M8 (alpha)。</p> 
<p><strong>9.0.56 和 10.0.14 的主要更新内容</strong></p> 
<ul> 
 <li>提供针对导致接受器多次报告传入连接的已知操作系统错误的保护</li> 
 <li>为 JVM 错误实现解决方法，该错误在使用分段上传时可能触发文件描述符泄漏，并且应用程序未明确关闭缓存在磁盘上的上传文件的输入流</li> 
 <li>修复启用安全管理器并且启动后收到的第一个请求是对启用 TLS 的 NIO2 连接器的 HTTP 请求时的异常</li> 
</ul> 
<p>详情查看 Changelog：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2Ftomcat-9.0-doc%2Fchangelog.html%23Tomcat_9.0.56_%28remm%29" target="_blank">Tomcat 9 changelog</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2Ftomcat-10.0-doc%2Fchangelog.html%23Tomcat_10.0.14_%28markt%29" target="_blank">Tomcat 10 changelog</a><span style="color:#000000">。</span></p> 
<p><strong>10.1.0-M8 (alpha) 更新内容</strong></p> 
<ul> 
 <li>将 cookie 支持限制为 RFC 6265，以与 Servlet 规范的最新更新保持一致</li> 
 <li>更新 WebSocket API 打包以从服务器 API 中删除客户端 API 的副本，并将其替换为对客户端 API 的依赖项。这使 Tomcat 与 WebSocket 2.1 规范中的更改保持一致</li> 
 <li>提供针对导致接受器多次报告传入连接的已知操作系统错误的保护</li> 
</ul> 
<p>详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2Ftomcat-10.1-doc%2Fchangelog.html%23Tomcat_10.1.0-M8_%28markt%29" target="_blank">Tomcat 10.1<span> </span><strong>(alpha)</strong><span> </span>changelog</a><span style="color:#000000">。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftomcat.apache.org%2F" target="_blank">下载地址</a>。</p>
                                        </div>
                                      
</div>
            