
---
title: 'Druid 1.2.6 发布，增强 SQL Parser，修复连接池在特定场景异常的问题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6967'
author: 开源中国
comments: false
date: Mon, 10 May 2021 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6967'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Druid 1.2.6 版本现已发布，这又是一个 bug 修复版本，主要是修复连接池在特定场景的一些异常问题，还有 SQL Parser 的增强。</p> 
<p><strong>Issues</strong></p> 
<ol> 
 <li> <p>修复连接池LogFilter JDK 8日期类型LocalDateTime/LocalDate在日志输出时格式不对的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fpull%2F4174" target="_blank">#4174</a></p> </li> 
 <li>修复连接池在close后创建中的连接没有被关闭的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fpull%2F4196" target="_blank">#4196</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4195" target="_blank">#4195</a></li> 
 <li>修复连接池在MySQL服务器主动连接断开时keepAlive机制失效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4227" target="_blank">#4227</a></li> 
 <li>修复连接池在timeBetweenEvictionRunsMillis大于keepAliveBetweenTimeMillis时异步使用连接会导致连接池不可用的问题。</li> 
 <li>连接池和parser增加对trino的支持</li> 
 <li>SQL Parser增强快速识别SqlType的支持</li> 
 <li>SQL Parser增强对MySQL的语法支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4225" target="_blank">#4225</a></li> 
 <li>SQL Parser增强对PG的语法支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4221" target="_blank">#4221</a></li> 
 <li>SQL Parser增强对Hive的语法支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4231" target="_blank">#4231</a></li> 
</ol> 
<p><strong>相关连接</strong></p> 
<ul> 
 <li> <p>druid下载 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Fdruid%2F1.2.6%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/druid/1.2.6/</a></p> </li> 
 <li>druid-spring-booter下载 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Fdruid-spring-boot-starter%2F1.2.6%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/druid-spring-boot-starter/1.2.6/</a></li> 
 <li>文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fwiki%2F%25E5%25B8%25B8%25E8%25A7%2581%25E9%2597%25AE%25E9%25A2%2598" target="_blank">https://github.com/alibaba/druid/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98</a></li> 
 <li>源码 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Ftree%2F1.2.6" target="_blank">https://github.com/alibaba/druid/tree/1.2.6</a></li> 
 <li>内置监控演示 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F120.26.192.168%2Fdruid%2F" target="_blank">http://120.26.192.168/druid/</a></li> 
</ul> 
<p> 更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Freleases%2Ftag%2F1.2.6" target="_blank">https://github.com/alibaba/druid/releases/tag/1.2.6</a></p>
                                        </div>
                                      
</div>
            