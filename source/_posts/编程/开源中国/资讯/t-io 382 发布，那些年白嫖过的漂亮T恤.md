
---
title: 't-io 3.8.2 发布，那些年白嫖过的漂亮T恤'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://res.tiocloud.com/202206/blog/upload/img/50/8931/1119484/88097537/74541310905/87/163215/1541700995829080064.jpg'
author: 开源中国
comments: false
date: Wed, 29 Jun 2022 09:47:00 GMT
thumbnail: 'https://res.tiocloud.com/202206/blog/upload/img/50/8931/1119484/88097537/74541310905/87/163215/1541700995829080064.jpg'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0px; margin-right:0px; text-align:left">关于标题</h1> 
<p><span style="background-color:#ffffff; color:#000000">为回馈广大用户对t-io的喜爱，t-io官方在2022年5月底免费赠送了一些t-io官方T恤，当时的活动链接：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tiocloud.com%2F1%2Factivity" target="_blank">https://www.tiocloud.com/1/activity</a><span style="background-color:#ffffff; color:#000000"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tiocloud.com%2F1%2Factivity" target="_blank"><span> </span></a>（PS：今年的活动已经结束，期待来年的吗？）。看看领到T恤的老板们、CTO们有多开心：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tiocloud.com%2F1541702143566815232" target="_blank">https://www.tiocloud.com/1541702143566815232</a></p> 
<p><img alt height="801" src="https://res.tiocloud.com/202206/blog/upload/img/50/8931/1119484/88097537/74541310905/87/163215/1541700995829080064.jpg" width="901" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">下面言归正传</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">本次更新内容</h1> 
<ol style="margin-left:0; margin-right:0"> 
 <li>去掉fastjson的依赖</li> 
 <li>完善http method</li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:left">最新POM 坐标</h1> 
<pre><code class="language-xml"><dependency>
    <groupId>org.t-io</groupId>
    <artifactId>tio-core</artifactId>
    <version>3.8.2.v20220628-RELEASE</version>
</dependency></code></pre> 
<h1 style="margin-left:0; margin-right:0; text-align:left">关于t-io</h1> 
<h1 style="margin-left:0; margin-right:0; text-align:left">为什么要开发t-io</h1> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">与其坐学厚厚的《xxx权威指南》，不如站着自主研发，创造更多人一眼就懂的编程API</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">t-io的前世今生</h1> 
<ol style="margin-left:0; margin-right:0"> 
 <li>2010年，talent-tan在某通讯大厂接手网管系统的通讯模块，老代码采用的是传统IO，一个client需要至少3个线程来守，经常性内存溢出和宕机。talent-tan临危受命，重写了通讯模块，解决了领导关注的全部问题</li> 
 <li>2012年，基于nio研发了talent-nio框架</li> 
 <li>2013年，用talent-nio写了mycat中的一个透传模块</li> 
 <li>2014年，用talent-nio实现了热波直播的IM模块</li> 
 <li>2015年，talent-tan开始关注aio技术，同时把talent-nio中的线程池、锁处理、并发数据结构进行了进一步抽象，使这些“王谢堂前燕”，飞入“广大码农家”</li> 
 <li>2016年，基于aio技术重写了talent-nio，命名为talent-aio，代码入驻码云，低调开源</li> 
 <li>2017年，talent-aio更名为t-io，开始在开源中国用新闻的形式传播t-io，同年t-io成为GVP项目，t-io收获大量用户</li> 
 <li>2018年，基于t-io实现了tio-http-server、tio-websocket-server、tio-webpack等周边产品，这些产品既验证了t-io的优秀，又反过来促进t-io的进步</li> 
 <li>2019年，华为某团队对基于t-io的某智慧产品进行了长达3~6个月的拷机极限压测，t-io经受住考验，为正式进入华为开源优选库做了扎实的铺垫</li> 
 <li>2020年，t-io正式入驻华为开源优选库，基于t-io开发的第一款商业IM谭聊正式上市，集群版t-io也正式完成研发并通过压测</li> 
 <li>2021年，客户反馈基于t-io研发的谭聊非常稳定</li> 
 <li>2022年，基于t-io研发的集群版本谭聊，获得用户极致的口碑，同时也为t-io的持续投入带来了相当长时间的资金保障</li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:left">t-io解决的痛点</h1> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">t-io的出发点是解决网络编程的用户痛点，其使命是让天下再也没有难开发的网络程序，且看t-io给用户带来的惊喜</p> 
<ol style="margin-left:0; margin-right:0"> 
 <li>易学易用，talent-tan之所以创造t-io，就是因为市面上同类产品学习成本大，所以在设计api时，特别关切用户的接受度。t-io第一批用户仅仅是看了t-io官方提供的示范工程就掌握了t-io</li> 
 <li>碾压全部知名同类产品的数据监控能力——既提供全面的监控数据，又保障性能的优异</li> 
 <li>内置心跳超时检查、心跳定时发送能力</li> 
 <li>极致打磨的底层集群能力，可无缝解决IM、物联网等大型产品的集群需求</li> 
 <li>掉线自动重连能力</li> 
 <li>t-io实测性能一：1.9G内存稳定支持30万TCP长连接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tiocloud.com%2F61" target="_blank">https://www.tiocloud.com/61</a></li> 
 <li>t-io实测性能二：用t-io跑出每秒1051万条聊天消息：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tiocloud.com%2F41" target="_blank">https://www.tiocloud.com/41</a></li> 
 <li>t-io实测性能三：netty和t-io对比测试结果：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tiocloud.com%2F154" target="_blank">https://www.tiocloud.com/154</a></li> 
 <li>内置ack消息能力</li> 
 <li>内置半包粘包处理</li> 
 <li>自创同步锁、同步安全线程池、同步数据结构等工具库，为业务应用提供丰富的开箱即用API</li> 
 <li>内置慢攻击防御机制，帮助应用自动拉黑嫌疑IP</li> 
 <li>丰富的生态，目前已经用t-io实现了http、websocket、mqtt及大量私有协议</li> 
 <li>对开发工程师要求低，为企业节约人工成本</li> 
 <li>性能卓越，为企业节约硬件部署成本</li> 
</ol> 
<h1>关注t-io后续生态</h1> 
<p>拥有强大集群能力的t-io，目前已经正式向IOT进军，<strong>mqtt broker</strong>已经实现，<strong>mqtt client</strong>已经在内测中，<strong>边缘接入平台</strong>也在规划中，有兴趣的同学可以适当关注</p> 
<p><img height="803" src="https://oscimg.oschina.net/oscnet/up-2a3d376ab680b949630f04218b1de5b7f0f.png" width="1003" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            