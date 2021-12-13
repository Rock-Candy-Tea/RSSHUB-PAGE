
---
title: 't-io 3.7.6 发布，网络编程很苦，用 t-io 后会很甜'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/1123/155602_fde63447_355738.jpeg'
author: 开源中国
comments: false
date: Mon, 13 Dec 2021 10:02:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/1123/155602_fde63447_355738.jpeg'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="margin-left:0px; margin-right:0px; text-align:left">网络编程很苦，用t-io后会很甜</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">t-io是<a href="https://gitee.com/tywo45/t-io">talent-tan</a>采用java语言开发的一款网络编程框架</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">为什么要开发t-io</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">在t-io之前，已经有mina,netty这样的网络编程框架了，talent-tan出于什么考虑要重新发明轮子呢？原因很奇葩：</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">talent-tan学习能力太差，在看了些《netty权威指南》后，觉得自己很难hold住netty，或者说要想hold住netty需要花上大量精力和记忆力</p> 
</blockquote> 
<h1 style="margin-left:0; margin-right:0; text-align:left">t-io的前世今生</h1> 
<ol> 
 <li>2010年，talent-tan在某通讯大厂接手网管系统的通讯模块，老代码采用的是传统IO，一个client需要有3个线程来守，经常内存溢出和宕机。talent-tan临危受命，重写了通讯模块</li> 
 <li>2012年，talent-tan利用业余时间基于nio写talent-nio</li> 
 <li>2013年，talent-tan短暂参与了mycat项目，用talent-nio写了mycat中的一个透传模块</li> 
 <li>2014年，用talent-nio实现了热波直播的IM模块</li> 
 <li>2015年，talent-tan开始关注aio技术，同时把talent-nio中的线程池、锁处理、并发数据结构进行了进一步抽象</li> 
 <li>2016年，基于aio技术重写了talent-nio，命名为talent-aio，代码入驻码云，正式开源</li> 
 <li>2017年，talent-aio更名为t-io，同年t-io成为GVP项目，t-io收获大量用户</li> 
 <li>2018年，基于t-io实现了tio-http-server、tio-websocket-server、tio-webpack等周边产品</li> 
 <li>2019年，华为业软某测试团队对基于t-io的某智慧产品进行了长达3~6个月的拷机极限压测，t-io经受住考验，为正式进入华为开源优选库做了扎实的铺垫</li> 
 <li>2020年，t-io正式入驻华为开源优选库，t-io官网注册人数破万，基于t-io开发的第一款商业IM谭聊正式上市，集群版t-io也正式完成研发和通过压测</li> 
 <li>2021年，客户反馈基于t-io研发的谭聊非常稳定</li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:left">t-io解决的痛点</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">任何作品都应该有其使命和价值，t-io的使命是解决网络编程方面的用户痛点，且看t-io给用户带来的惊喜</p> 
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
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.tiocloud.com%2Fdoc%2Ftio%2F85">https://www.tiocloud.com/tio/</a></p> 
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
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:left"><img alt="t-io见证历史" src="https://images.gitee.com/uploads/images/2021/1123/155507_3cff18d2_355738.jpeg" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h1 style="text-align:justify"><span><span><span><span>本次更新内容</span></span></span></span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次主要是更新pom依赖，毕竟最近有个知名开源框架有点火，t-io本身没有使用该日志框架，但是t-io的依赖管理里面有它，所以及时更新发版，让使用t-io依赖管理的用户及时避坑</p> 
<h1>t-io新的纯净官网</h1> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tiocloud.com%2Ftio" target="_blank">https://www.tiocloud.com/tio</a>，里面的纯纯的t-io内容，该网站使用了<a href="https://gitee.com/monksoul/Furion">furion</a>官网的源代码，感谢@百小僧 大佬的亲手指点</p> 
<p><img height="1319" src="https://oscimg.oschina.net/oscnet/up-d80be271381eb361b72aabc4c69214d5340.png" width="1207" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">最新maven坐标</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">tio-core</h2> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.t-io<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>tio-core<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>3.7.6.v20211212-RELEASE<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span> </span>tio-http </h2> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.t-io<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>tio-http-server<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>3.7.6.v20211212-RELEASE<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">tio-websocket </h2> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.t-io<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>tio-websocket-server<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>3.7.6.v20211212-RELEASE<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></code>
</pre>
                                        </div>
                                      
</div>
            