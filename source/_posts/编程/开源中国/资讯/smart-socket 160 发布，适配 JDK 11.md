
---
title: 'smart-socket 1.6.0 发布，适配 JDK 11'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2795'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 09:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2795'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">smart-socket 是一款极简、易用、高性能的国产开源 AIO 通信框架，旨在帮助开发人员轻松打造企业级通信应用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">这个版本犹豫了许久，没有别的新特性加入，仅仅是将JDK版本适配至 11，看似为了发版而发版。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">为了避免对老用户造成困扰，先在此作一下澄清：<span style="color:#ffffff"><span style="background-color:#ff6827; color:#ffffff">1.5.x 系列的版本会依旧以 JDK 1.8 版本继续维护下去。</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">至于 1.6.0 决定升级至 JDK 11，也是无奈之举。关注 smart 系列作品的朋友应该清楚，我们目前维护的开源项目除了这款 AIO 通信框架，还有 smart-http、smart-servet，以及现阶段重点投入的 smart-mqtt。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">对于smart-mqtt，我们规划通过 GraalVM 将 Java 应用编译成原生镜像，使其更好的部署于边缘场景。该设想存在较多的技术难题需要攻克，而当下面临的问题便是新版 GraalVM 已不再支持 JDK 1.8。Java 1.8 与 11 存在某些 API 的不兼容，会导致镜像编译失败，所以需要先对 smart-socket 进行 JDK 的适配升级。况且，如今业界很多项目已逐渐放弃 Java 8，或许我们应该尝试拥抱高版本JDK。 </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>此版本主要变化</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">适配 JDK 11，不再兼容 Java 8。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">合并用户提交的PR，修复错误注释。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">升级 SSL 插件以支持更高级别、更安全的加密通信（已同步更新至v1.5.19版本）。</p> </li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>maven 坐标</strong></p> 
<pre><code class="language-xml"><dependency>
    <groupId>org.smartboot.socket</groupId>
    <artifactId>aio-core</artifactId>
    <version>1.6.0</version>
</dependency></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">想要进一步了解 smart-socket，请移步以下链接不迷路：</p> 
<ul style="list-style-type:none; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>文档</span></p> <p style="margin-left:0; margin-right:0"><a href="https://smartboot.gitee.io/book/smart-socket/">https://smartboot.gitee.io/book/smart-socket/</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Gitee 仓库</span></p> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/smartboot/smart-socket">https://gitee.com/smartboot/smart-socket</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Github 仓库</span></p> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsmartboot%2Fsmart-socket" target="_blank">https://github.com/smartboot/smart-socket</a></p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            