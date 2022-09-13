
---
title: 'Druid 1.2.12 发布，连接池默认指定 socketTimeout，增强 SQL Parser Latest'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1489'
author: 开源中国
comments: false
date: Tue, 13 Sep 2022 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1489'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#24292f">数据库连接池 Druid 1.2.12 现已</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Freleases%2Ftag%2F1.2.12" target="_blank"><span style="color:#2980b9">发布</span></a><span style="background-color:#ffffff; color:#24292f">。</span>这个版本连接池默认增加配置connectTimeout和socketTimeout，增强了SQL Parser。</p> 
<h4>Issues</h4> 
<ol> 
 <li>连接池DruidDataSource支持新的配置connectTimeout和socketTimeout，分别都是10秒。这个默认值会减少因为网络丢包时导致的连接池无法创建链接。</li> 
 <li>修复连接池DruidDataSource#handleFatalError方法判断是否关闭逻辑不对的问题</li> 
 <li>修复StatFilter统计Statement执行SQL只记录第一条SQL的问题</li> 
 <li>修复ParameterizedOutputVisitorUtils#restore结果不对的问题</li> 
 <li>SQL Parser增强对PolarDB-X的支持</li> 
 <li>SQL Parser增强对Oceanbase的支持</li> 
 <li>SQL Parser增强对MySQL的支持</li> 
 <li>SQL Parser增强对Clickhouse的支持</li> 
 <li>SQL Parser增强对DB2的支持</li> 
 <li>SQL Parser增强对Oracle的支持</li> 
</ol> 
<h4>相关连接</h4> 
<ul> 
 <li>druid下载<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Fdruid%2F1.2.12%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/druid/1.2.12/</a></li> 
 <li>druid-spring-booter下载<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Fdruid-spring-boot-starter%2F1.2.12%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/druid-spring-boot-starter/1.2.12/</a></li> 
 <li>文档<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Fwiki%2F%25E5%25B8%25B8%25E8%25A7%2581%25E9%2597%25AE%25E9%25A2%2598" target="_blank">https://github.com/alibaba/druid/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98</a></li> 
 <li>源码<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid%2Ftree%2F1.2.12" target="_blank">https://github.com/alibaba/druid/tree/1.2.12</a></li> 
 <li>内置监控演示<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F120.26.192.168%2Fdruid%2F" target="_blank">http://120.26.192.168/druid/</a></li> 
</ul>
                                        </div>
                                      
</div>
            