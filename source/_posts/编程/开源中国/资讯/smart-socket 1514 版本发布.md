
---
title: 'smart-socket 1.5.14 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2882'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 09:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2882'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">smart-socket 是一款极简、易用、高性能的国产开源 AIO 通信框架，旨在帮助开发人员轻松打造企业级通信应用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>此版本主要变化</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">客户端新增异步启动方式，满足用户的响应式编程需求。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">执行<span> </span><span style="color:#000000">SocketChannel</span>#register 的同时注入附件对象。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">WriteBuffer采用<code>synchronized</code>替换原先的<code>ReentrantLock</code>。考虑到WriteBuffer 的极端应用场景为低并发高IO，故采用<span> </span><code>synchronized</code><span> </span>有一定机会享受到 JVM 偏向锁带来的性能红利，同时还能简化代码复杂度。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 DelimiterFrameDecoder 特定情况下的解码失效问题【Issues#I4H4YB】</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复几处单词拼写错误问题。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">补充单测及示例代码。</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>maven坐标</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:justify"><dependency>
    <groupId>org.smartboot.socket</groupId>
    <artifactId>aio-core</artifactId>
    <version>1.5.14</version>
</dependency>
</pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">想要进一步了解 smart-socket，请移步以下链接不迷路：</p> 
<ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>文档</span></p> <p style="margin-left:0; margin-right:0"><a href="https://smartboot.gitee.io/book/smart-socket/">https://smartboot.gitee.io/book/smart-socket/</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Gitee仓库</span></p> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/smartboot/smart-socket">https://gitee.com/smartboot/smart-socket</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Github仓库</span></p> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsmartboot%2Fsmart-socket" target="_blank">https://github.com/smartboot/smart-socket</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            