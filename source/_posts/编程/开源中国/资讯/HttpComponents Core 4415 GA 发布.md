
---
title: 'HttpComponents Core 4.4.15 GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1463'
author: 开源中国
comments: false
date: Fri, 10 Dec 2021 06:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1463'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#000000">HttpComponents Core 4.4.15 GA 现</span>已发布<span style="background-color:#ffffff; color:#000000">，这是一个维护版本，修复了 4.4.14 发布后出现的错误。请注意，从 4.4 开始，HttpCore 需要 Java 1.6 或更新版本。</span></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">主要更新内容</span></strong></p> 
<ul> 
 <li>修复在 processPendingInterestOps 过程中未处理的 CancelledKeyException 导致底层 IOReactor 关闭的问题</li> 
 <li>如果 SSL 会话被协议层关闭，而协议会话缓冲区中仍有未处理的数据，那么非阻塞的 SSL I/O 会话就会进入一个紧循环</li> 
 <li>将 SSLSetupHandler#verify 抛出的 RuntimeExceptions 转换为 SSLExceptions</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202112.mbox%2F%253C3e931d1ee524dd5ea767ccded0b6c5e00e73cb9b.camel%40apache.org%253E" target="_blank">更新公告</a>。</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            