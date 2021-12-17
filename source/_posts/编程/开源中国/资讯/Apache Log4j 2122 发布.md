
---
title: 'Apache Log4j 2.12.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=706'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 08:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=706'
---

<div>   
<div class="content">
                                                                                            <p>Apache Log4j 2.12.2<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202112.mbox%2F%253CCACZkXPy6RzwAFj4CyFDqvi3p%3Dhze-PZtRtj6YUg-eeU%2BnP8cMA%40mail.gmail.com%253E" target="_blank"> 已发布</a>。Log4j 是一个日志记录框架，Log4j 2 是对 Log4j 的升级，提供了重大改进，超越其前身 Log4j 1.x，并提供许多其它现代功能 ，例如对标记的支持、使用查找的属性替换、lambda 表达式与日志记录时无垃圾等。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flogging.apache.org%2Flog4j%2Flog4j-2.12.2%2Fdownload.html" target="_blank">https://logging.apache.org/log4j/log4j-2.12.2/download.html</a></p> 
<p>此版本的变化只针对 CVE-2021-44228 和 CVE-2021-45046 漏洞，适用于仍使用 Java 7 的开发者。</p> 
<ul> 
 <li>移除 PatternLayout 中的消息查找 (Message Lookups) 功能，"%m&#123;lookup&#125;", "%m&#123;nolookup&#125;" 及其变种仍可作为转换模式被接受，但不会产生影响</li> 
 <li>默认禁用 JNDI，且当启用时只允许 "java" 协议</li> 
 <li>使 JNDI 查找无法运行，并删除消息查找功能</li> 
</ul> 
<p>由于 Log4j 2.12.2 的 API，以及许多核心组件，保持了与以前版本的二进制兼容性，推荐开发者升级至此版本。</p> 
<p>最后，Apache Log4j 2.12.2 至少需要 Java 7 才能构建和运行。<a href="https://www.oschina.net/news/173618/log4j-2-16-0-released" target="news">Apache Log4j 2.16.0</a> 是最新的 Log4j 版本，鼓励用户升级至此版本，因为 Java 7 已经不再受 Log4j 团队的支持。</p>
                                        </div>
                                      
</div>
            