
---
title: 'Netty 4.1.77.Final 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6703'
author: 开源中国
comments: false
date: Mon, 09 May 2022 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6703'
---

<div>   
<div class="content">
                                                                                            <p>Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。</p> 
<p>Netty 4.1.77.Final 是一个错误修复版本，它包含一个只影响用户运行 Java 6 的 CVE 修复，此外还修复了一个可能导致本地 epoll 传输在没有实现 epoll_pwait2 的系统上无法使用的错误。具体更新内容如下：</p> 
<ul> 
 <li>由于 io.netty:netty-codec-http 中的 Java 6 和更低版本的临时文件，Unix-like 系统上的 Netty 存在局部信息泄露漏洞（CVE-2022-24823）</li> 
 <li>将可选的 <code>netty-tcnative</code> 依赖升级到 2.0.52.Final 版本</li> 
 <li>修复了 Netty 无法加载着色的本地库的错误</li> 
 <li>在 Automatic-Module-Name 中加入分类器</li> 
 <li>检查 epoll_pwait2 是否实现</li> 
 <li>不要在 packagePrefix 上调用 strdup</li> 
 <li>在 Intellij 中启用异步任务的调试</li> 
 <li>在 glibc 缺失的情况下抛出一个异常，而不是让 JVM 发生崩溃</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2022%2F05%2F06%2F2-1-77-Final.html" target="_blank">https://netty.io/news/2022/05/06/2-1-77-Final.html</a></p>
                                        </div>
                                      
</div>
            