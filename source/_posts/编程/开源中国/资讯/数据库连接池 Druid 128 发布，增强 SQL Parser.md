
---
title: '数据库连接池 Druid 1.2.8 发布，增强 SQL Parser'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=257'
author: 开源中国
comments: false
date: Mon, 04 Oct 2021 06:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=257'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#24292f; text-align:start">数据库连接池 Druid 1.2.8 已发布，这个版本修复了连接池在KeepAlive打开时导致连接池连接状态不对的问题，建议KeepAlive打开的用户升级到最新版本。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start">Issues</h1> 
<ol> 
 <li>修复连接池在KeepAlive=true时，会导致连接池状态不对的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4438" target="_blank">#4438</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4316" target="_blank">#4316</a></li> 
 <li>连接池ExceptionSorter增强对Oceanbase的支持<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4322" target="_blank">#4322</a></li> 
 <li>连接池增强对友商数据库的支持，包括人大金仓、华为gaussdb、greenplum的支持</li> 
 <li>增强SQL Parser，增强了对MaxCompute、Oracle、SQL Server、MySQL的语法支持<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fpull%2F4399" target="_blank">#4399</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4332" target="_blank">#4332</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4434" target="_blank">#4434</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4442" target="_blank">#4442</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4444" target="_blank">#4444</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4454" target="_blank">#4454</a></li> 
 <li>修复DruidDataSourceWrapper不是public无法创建CGLIB代理的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fissues%2F4481" target="_blank">#4481</a></li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:start">相关连接</h1> 
<ul> 
 <li>druid下载<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Fdruid%2F1.2.8%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/druid/1.2.8/</a></li> 
 <li>druid-spring-booter下载<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Fdruid-spring-boot-starter%2F1.2.8%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/druid-spring-boot-starter/1.2.8/</a></li> 
 <li>文档<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fwiki%2F%25E5%25B8%25B8%25E8%25A7%2581%25E9%2597%25AE%25E9%25A2%2598" target="_blank">https://github.com/alibaba/druid/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98</a></li> 
 <li>源码<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Ftree%2F1.2.8" target="_blank">https://github.com/alibaba/druid/tree/1.2.8</a></li> 
 <li>内置监控演示<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F120.26.192.168%2Fdruid%2F" target="_blank">http://120.26.192.168/druid/</a></li> 
</ul>
                                        </div>
                                      
</div>
            