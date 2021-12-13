
---
title: '核弹级漏洞席卷全球！程序员都懵了 修改iPhone名就可触发'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211213/S8a9e76e4-c3c1-4ce2-b834-91c8870b23c5.png'
author: 快科技（原驱动之家）
comments: false
date: Mon, 13 Dec 2021 09:08:04 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211213/S8a9e76e4-c3c1-4ce2-b834-91c8870b23c5.png'
---

<div>   
<p>一时间，这个高危漏洞引发全球网络安全震荡！</p>
<p>CVE-2021-44228，又名Log4Shell 。</p>
<p>新西兰计算机紧急响应中心（CERT）、美国国家安全局、德国电信CERT、中国国家互联网应急中心（CERT/CC）等多国机构相继发出警告。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211213/8a9e76e4-c3c1-4ce2-b834-91c8870b23c5.png" target="_blank"><img alt="核弹级漏洞log4shell席卷全球！修改iPhone名称就可触发" h="332" src="https://img1.mydrivers.com/img/20211213/S8a9e76e4-c3c1-4ce2-b834-91c8870b23c5.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>已证实服务器易受到漏洞攻击的公司包括苹果、亚马逊、特斯拉、谷歌、百度、腾讯、网易、京东、Twitter、 Steam等。据统计，共有6921个应用程序都有被攻击的风险，其中《我的世界》首轮即被波及。</p>
<p>其危害程度之高，影响范围之大，以至于不少业内人士将其形容为“无处不在的零日漏洞”。</p>
<p>这究竟是怎么一回事？</p>
<p><strong>Java程序员都懵了</strong></p>
<p>这个漏洞最早是由阿里员工发现。11月24日，阿里云安全团队向Apache报告了Apache Log4j2远程代码执行（RCE)漏洞。12月9日，更多利用细节被公开。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211213/84bc71aa-bfb5-4913-ab4a-d1bacf4f9214.png" target="_blank"><img alt="核弹级漏洞log4shell席卷全球！修改iPhone名称就可触发" h="537" src="https://img1.mydrivers.com/img/20211213/S84bc71aa-bfb5-4913-ab4a-d1bacf4f9214.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>Apache，是当前全球最流行的跨平台Web服务器之一。</p>
<p>而作为当中的开源日志组件Apache Log4j2，被数百万基于Java的应用程序、网站和服务所使用。</p>
<p>据报道，此次漏洞是由于Log4j2在处理程序日志记录时存在JNDI注入缺陷。</p>
<p>（JNDI：Java命名和目录接口，是Java的一个目录服务应用程序接口，它提供一个目录系统，并将服务名称与对象关联起来，从而使得开发人员在开发过程中可以使用名称来访问对象。）</p>
<p>攻击者可利用该漏洞，向目标服务器发送恶意数据，当服务器在将数据写入日志时，触发Log4j2组件解析缺陷，进而在未经授权的情况下，实现远程执行任意代码。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211213/4e1aeb10-d440-4d83-9ac0-3a43528ac91c.png" target="_blank"><img alt="核弹级漏洞log4shell席卷全球！修改iPhone名称就可触发" h="230" src="https://img1.mydrivers.com/img/20211213/S4e1aeb10-d440-4d83-9ac0-3a43528ac91c.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>以最先受到影响的《我的世界》为例，攻击者只需在游戏聊天中，发送一条带触发指令的消息，就可以对收到该消息的用户发起攻击。</p>
<p>目前已经有网友证实，更改iPhone名称就可以触发漏洞。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211213/cb2d47c9-d98e-4bff-84b1-df0c818071b0.png" target="_blank"><img alt="核弹级漏洞log4shell席卷全球！修改iPhone名称就可触发" h="535" src="https://img1.mydrivers.com/img/20211213/Scb2d47c9-d98e-4bff-84b1-df0c818071b0.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>还有网友试了试百度搜索框、火狐浏览器里输入带$&#123;的特殊格式请求，就能造成网页劫持。</p>
<p>而像IT通信（互联网）、工业制造、金融、医疗卫生、运营商等各行各业都将受到波及，全球互联网大厂、游戏公司、电商平台等夜都有被影响的风险。</p>
<p>其中甚至包括美国国家安全局的逆向工程工具GHIDRA。</p>
<p>因此也就不奇怪，在9号当晚公开那天听说不少程序员半夜起来敲代码。</p>
<p>网络监控Greynoise表示，攻击者正在积极寻找易受Log4Shell攻击的服务器，目前大约有100个不同的主机正在扫描互联网，寻找利用 Log4j 漏洞的方法。</p>
<p>考虑到这个库无处不在、带来的影响以及触发难度较低，安全平台LunaSec将其称为Log4Shell漏洞，甚至警告说，任何使用Apache Struts的人都“可能容易受到攻击”。</p>
<p>不少网友对此惊叹于这史诗级别的漏洞，并担心恐要持续几个月甚至几年。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211213/c8f632fe-79de-4df9-bfaf-94252ac1a550.png" target="_blank"><img alt="核弹级漏洞log4shell席卷全球！修改iPhone名称就可触发" h="129" src="https://img1.mydrivers.com/img/20211213/Sc8f632fe-79de-4df9-bfaf-94252ac1a550.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>如何解决？</strong></p>
<p>2021年12月9日，Apache官方发布了紧急安全更新以修复该远程代码执行漏洞。但更新后的Apache Log4j 2.15.0-rc1 版本被发现仍存在漏洞绕过。</p>
<p>12月10日凌晨2点，Apache再度紧急发布log4j-2.15.0-rc2版本。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211213/6ab8a98f-42bd-4cd6-8e01-3d5ac91a4813.png" target="_blank"><img alt="核弹级漏洞log4shell席卷全球！修改iPhone名称就可触发" h="377" src="https://img1.mydrivers.com/img/20211213/S6ab8a98f-42bd-4cd6-8e01-3d5ac91a4813.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>与此同时，国家互联网应急中心还给出了如下措施以进行漏洞防范。</p>
<p>1）添加jvm启动参数-Dlog4j2.formatMsgNoLookups=true；</p>
<p>2）在应用classpath下添加log4j2.component.properties配置文件，文件内容为log4j2.formatMsgNoLookups=true；</p>
<p>3）JDK使用11.0.1、8u191、7u201、6u211及以上的高版本；</p>
<p>4）部署使用第三方防火墙产品进行安全防护。</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/pingguo.htm"><i>#</i>苹果</a><a href="https://news.mydrivers.com/tag/iphoneshouji.htm"><i>#</i>iPhone手机</a><a href="https://news.mydrivers.com/tag/loudong.htm"><i>#</i>漏洞</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/A2189DWR-7DyqUbBsIq3xg">量子位</a></span>
<span>责任编辑：随心</span>
</p>
        
</div>
            