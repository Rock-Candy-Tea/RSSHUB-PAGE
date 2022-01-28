
---
title: 't-io 3.8.0 发布，网络编程很苦，用 t-io 后会很甜'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://whnb.wang/stars/tywo45/t-io'
author: 开源中国
comments: false
date: Fri, 28 Jan 2022 08:06:00 GMT
thumbnail: 'https://whnb.wang/stars/tywo45/t-io'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0px; margin-right:0px; text-align:left">修改点</h1> 
<p>本次发版主要是类名调整</p> 
<pre><code class="language-bash"> ServerAioListener-->TioServerListener
 ClientAioListener-->TioClientListener
 ServerAioHandler-->TioServerHandler
 ClientAioHandler-->TioClientHandler
 DefaultAioListener-->DefaultTioListener
 AioHandler-->TioHandler
 AioListener-->TioListener
 WsClientAioHander-->WsTioClientHander
 AioDecodeException-->TioDecodeException
 ClientTio-->TioClient
 ServerTio-->TioServer</code></pre> 
<h1>POM坐标</h1> 
<pre><code class="language-xml"><dependency>
    <groupId>org.t-io</groupId>
    <artifactId>tio-core</artifactId>
    <version>3.8.0.v20220128-RELEASE</version>
</dependency></code></pre> 
<h1 style="margin-left:0px; margin-right:0px; text-align:left">后续计划</h1> 
<p>借助netty，用t-io实现mqtt协议，方便大家用t-io打造自家的<strong>IoT</strong>平台（为了更好地照顾netty用户，t-io版mqtt将会在命名上尽量用netty-mqtt原版的）</p> 
<hr> 
<h1 style="margin-left:0px; margin-right:0px; text-align:left">网络编程很苦，用t-io后会很甜</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">t-io是未华钛特云（WA Talent Cloud，简称<span> </span><strong>WTC</strong><span> </span>）基于Java开发的一款高性能网络编程框架。t-io强大的并发处理能力、高稳定性使其成为广大企业开发工程项目和应用的首选；t-io简单易学，专为解决网络编程痛点而生，使其被众多新老开发者所喜爱</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fwhnb.wang%2Fstars%2Ftywo45%2Ft-io"><img alt="Stargazers over time" src="https://whnb.wang/stars/tywo45/t-io" referrerpolicy="no-referrer"></a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">源代码仓库</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/tywo45/t-io"><img alt="t-io gitee" src="https://www.tiocloud.com/2/imgs/product/tio/mayun.png" referrerpolicy="no-referrer"><span> </span></a><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftywo45%2Ft-io"><img alt="t-io github" src="https://www.tiocloud.com/2/imgs/product/tio/Github.png" referrerpolicy="no-referrer"></a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">为什么要开发t-io</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">与其坐学厚厚的《xxx权威指南》，不如站着自主研发，创造更多人一眼就懂的编程API</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">t-io的前世今生</h1> 
<ol> 
 <li>2010年，t-io的原创作者talent-tan在某通讯大厂接手网管系统的通讯模块，老代码采用的是传统IO，一个client需要有3个线程来守，经常内存溢出和宕机。talent-tan临危受命，重写了通讯模块。随即萌生了构思一套新框架的想法，专门解决网络编程痛点</li> 
 <li>2012年，经过两年的琢磨，基于nio写了talent-nio</li> 
 <li>2013年，用talent-nio写了mycat中的一个透传模块</li> 
 <li>2014年，用talent-nio实现了热波直播的IM模块</li> 
 <li>2015年，talent-tan开始关注aio技术，同时把talent-nio中的线程池、锁处理、并发数据结构进行了进一步抽象</li> 
 <li>2015年，开始关注aio技术，同时把talent-nio中的线程池、锁处理、并发数据结构进行了进一步抽象</li> 
 <li>2016年，基于aio技术重写了talent-nio，命名为talent-aio，代码入驻码云，正式开源</li> 
 <li>2017年，talent-aio更名为t-io，同年t-io成为GVP项目，t-io收获大量用户</li> 
 <li>2018年，基于t-io实现了tio-http-server、tio-websocket-server、tio-webpack等周边产品</li> 
 <li>2019年，华为某测试团队对基于t-io的某智慧产品进行了长达3~6个月的拷机极限压测，t-io经受住考验，为正式进入华为开源优选库做了扎实的铺垫</li> 
 <li>2020年，t-io正式入驻华为开源优选库，t-io官网注册人数破万，基于t-io开发的第一款商业IM谭聊正式上市，集群版t-io也正式完成研发并通过压测</li> 
 <li>2021年，客户反馈基于t-io研发的谭聊非常稳定</li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:left">t-io解决的痛点</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">t-io的出发点是解决网络编程的用户痛点，其使命是让天下再也没有难开发的网络程序，且看t-io给用户带来的惊喜</p> 
<ol> 
 <li>易学易用，talent-tan之所以创造t-io，就是因为市面上同类产品学习成本大，所以在设计api时，特别关切用户的接受度。t-io第一批用户仅仅是看了t-io官方提供的示范工程就掌握了t-io</li> 
 <li>全方位的数据监控能力：org.tio.core.stat.ChannelStat</li> 
 <li>内置心跳超时检查、心跳定时发送能力</li> 
 <li>极致打磨的底层集群能力，可无缝解决IM、物联网等大型产品的集群需求</li> 
 <li>掉线自动重连能力</li> 
 <li>t-io实测性能一：1.9G内存稳定支持30万TCP长连接：<a href="https://gitee.com/link?target=https%3A%2F%2Fwww.tiocloud.com%2F61">https://www.tiocloud.com/61</a></li> 
 <li>t-io实测性能二：用t-io跑出每秒1051万条聊天消息：<a href="https://gitee.com/link?target=https%3A%2F%2Fwww.tiocloud.com%2F41">https://www.tiocloud.com/41</a></li> 
 <li>t-io实测性能三：netty和t-io对比测试结果：<a href="https://gitee.com/link?target=https%3A%2F%2Fwww.tiocloud.com%2F154">https://www.tiocloud.com/154</a></li> 
 <li>内置ack消息能力</li> 
 <li>内置半包粘包处理</li> 
 <li>自创同步锁、同步安全线程池、同步数据结构等工具库，为业务应用提供丰富的开箱即用API</li> 
 <li>内置慢攻击防御机制，帮助应用自动拉黑嫌疑IP</li> 
 <li>丰富的生态，目前已经用t-io实现了http、websocket、mqtt及大量私有协议</li> 
 <li>对开发工程师要求低，为企业节约人工成本</li> 
 <li>性能卓越，为企业节约硬件部署成本</li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:left">t-io文档</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.tiocloud.com%2Fdoc%2Ftio%2F85">https://www.tiocloud.com/doc/tio/85</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">t-io技术白皮书</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.tiocloud.com%2Ftio.pdf">《t-io技术白皮书》</a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.tiocloud.com%2Ftio.pdf"><img alt="t-io技术白皮书" src="https://images.gitee.com/uploads/images/2021/1123/155602_fde63447_355738.jpeg" referrerpolicy="no-referrer"></a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">t-io口碑</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="t-io用户口碑(一)" src="https://res.tiocloud.com/202111/blog/upload/img/50/8931/1119484/88097537/74541310905/47/165441/1465242802995732480_sm.jpeg" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="t-io用户口碑(二)" src="https://res.tiocloud.com/202111/blog/upload/img/50/8931/1119484/88097537/74541310905/30/165441/1465242803872342016_sm.jpeg" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="t-io用户口碑(三)" src="https://res.tiocloud.com/202111/blog/upload/img/50/8931/1119484/88097537/74541310905/20/165442/1465242804337909760_sm.jpeg" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="t-io用户口碑(四)" src="https://res.tiocloud.com/202111/blog/upload/img/50/8931/1119484/88097537/74541310905/90/165441/1465242803121561600_sm.jpeg" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="t-io用户口碑(五)" src="https://res.tiocloud.com/202111/blog/upload/img/50/8931/1119484/88097537/74541310905/29/165441/1465242803469688832_sm.jpeg" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="t-io用户口碑(六)" src="https://res.tiocloud.com/202111/blog/upload/img/50/8931/1119484/88097537/74541310905/41/165441/1465242802333032448_sm.jpeg" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">t-io使用案例</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.tiocloud.com%2F2%2Fcase%2Findex.html"><img alt="t-io使用案例" src="https://images.gitee.com/uploads/images/2021/1123/155431_8a7ea725_355738.jpeg" referrerpolicy="no-referrer"></a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">t-io见证历史</h1> 
<p> </p>
                                        </div>
                                      
</div>
            