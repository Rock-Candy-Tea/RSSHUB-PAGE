
---
title: '3步搭建局域网公共网盘 其实你根本不需要NAS'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211101/ebb043c0-9b50-4f86-946e-383b7d9ca072.png'
author: 快科技（原驱动之家）
comments: false
date: Mon, 01 Nov 2021 19:14:58 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211101/ebb043c0-9b50-4f86-946e-383b7d9ca072.png'
---

<div>   
<p>工作中，经常有大量图片、视频、文件的存储与分享需求。</p>
<p>以前，最简单的解决办法就是使用U盘拷贝，不仅效率慢，而且U盘传着传着就容易丢失。另外，U盘读写速度慢，如传输几十GB视频文件，仅拷贝可能就需要数小时。</p>
<p>像笔者的工作就会生产大量产品图片、视频等，这些素材需要存储与分享，如果每次都通过U盘分享过于繁琐，由此便考虑在公司内部搭建一个局域网共享网盘。</p>
<p>局域网共享网盘不同于NAS，NAS的释义为网络附属存储，其实与局域网共享网盘的概念相似，不过两者有一个较为明显的区别，即前者是局域网，后者是互联网。</p>
<p>闲话不多说，我们直接开始搭建。搭建局域网公共网盘有多种实现方式，笔者选用闲置PC+外置磁盘阵列方式实现(PC充当服务器)，这样不仅兼容性强，不需硬件改造，还可移动。</p>
<p>硬盘方面，笔者推荐使用西部数据红盘，<span style="color:#ff0000;"><strong>红盘是针对NAS设计，可满足24x7全天候运行，寿命和可靠性都有保证，</strong></span>在这方面大家千万不要省钱，否则得不偿失。</p>
<p>新盘入手，我们来试试西部数据红盘的性能，<strong>使用CrystalDiskMark 8进行测试，顺序读写速度都超过了220MB/s，完全够用。</strong></p>
<p style="text-align: center"><img alt="3步搭建局域网公共网盘 其实你根本不需要NAS" h="352" src="https://img1.mydrivers.com/img/20211101/ebb043c0-9b50-4f86-946e-383b7d9ca072.png" style="border: black 1px solid" w="482" referrerpolicy="no-referrer"></p>
<p>磁盘阵列使用笔者闲置的奥睿科双盘阵列，可选择存储模式或RAID 1阵列模式。</p>
<p>根据需求，笔者选择存储模式，即使用2块6TB西部数据红盘搭建12TB存储空间。接口为USB3.0规格，理论支持5Gbps传输速率。</p>
<p>另外，<span style="color:#ff0000;"><strong>闲置笔记本电脑一台，充当服务器，拥有USB3.0接口（保证传输速度）。</strong></span></p>
<p>软件方面，使用青阳网络文件系统，即kiftd。之前曾考虑使用chfs，但后者曾出现过安全问题。下面，正式开始搭建：</p>
<p><strong>第一步，安装JAVA</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211101/6e246363-1ddb-4f80-b5a2-cfcd55ff084b.png" target="_blank"><img alt="3步搭建局域网公共网盘 其实你根本不需要NAS" h="408" src="https://img1.mydrivers.com/img/20211101/S6e246363-1ddb-4f80-b5a2-cfcd55ff084b.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>通过JAVA官网下载安装即可，傻瓜式，无需介绍（如果这个步骤都不会，本文可放弃了）；</p>
<p><strong>第二步，安装及配置kiftd</strong></p>
<p>Kiftd(青阳网络文件系统)是免费开源的网盘服务器项目，通过搜索便可找到资源。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211101/df286ab1-d149-4015-be73-e26022d2d5d3.png" target="_blank"><img alt="3步搭建局域网公共网盘 其实你根本不需要NAS" h="396" src="https://img1.mydrivers.com/img/20211101/Sdf286ab1-d149-4015-be73-e26022d2d5d3.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>这是一个压缩文件，解压后，安装kiftd.jar文件。</p>
<p style="text-align: center"><img alt="3步搭建局域网公共网盘 其实你根本不需要NAS" h="677" src="https://img1.mydrivers.com/img/20211101/3684c618-2454-4604-a6a5-359ed6e6d40d.png" style="border: black 1px solid" w="346" referrerpolicy="no-referrer"></p>
<p>安装成功后，开启kiftd服务。</p>
<p><strong>第三步，账户设置与上传分享</strong></p>
<p>使用常见的浏览器(搜狗、Edge等均可)，在地址栏输入http://127.0.0.1:8080/，即可访问资源管理界面，默认的管理员账户为“admin”，密码为“000000”。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211101/7a643069-5684-4fa9-9f6b-2f2a72c3d193.png" target="_blank"><img alt="3步搭建局域网公共网盘 其实你根本不需要NAS" h="264" src="https://img1.mydrivers.com/img/20211101/S7a643069-5684-4fa9-9f6b-2f2a72c3d193.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>登录后可进行资源的管理，如上传、删除、创建文件夹等。已上传的文件，支持视频在线播放、图片查看等。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211101/bdcfa73f-6596-4bdd-b6ff-6327e5e7becb.png" target="_blank"><img alt="3步搭建局域网公共网盘 其实你根本不需要NAS" h="584" src="https://img1.mydrivers.com/img/20211101/Sbdcfa73f-6596-4bdd-b6ff-6327e5e7becb.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>如其他人使用该局域网，需修改地址，改为使用服务器PC的网络IP地址，即为http://192.168.0.2:8080/，通过查看网络设备属性可找到。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211101/e92608ce-f930-4fe8-b958-be44df352d49.png" target="_blank"><img alt="3步搭建局域网公共网盘 其实你根本不需要NAS" h="359" src="https://img1.mydrivers.com/img/20211101/Se92608ce-f930-4fe8-b958-be44df352d49.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>使用另一台电脑进行实测，在地址栏输入http://192.168.0.2:8080/后，顺利打开，可查阅公共网盘内容，下载速度大约在100MB/s。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211101/bf751427-8e8a-429f-b552-e3a9b875858e.png" target="_blank"><img alt="3步搭建局域网公共网盘 其实你根本不需要NAS" h="337" src="https://img1.mydrivers.com/img/20211101/Sbf751427-8e8a-429f-b552-e3a9b875858e.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>以上，就是搭建局域网公共网盘的步骤，可以说过程非常的简单。</p>
<p>另外，还有几点需要提示：</p>
<p><strong>1）用于充当服务器的PC，网卡速率会限制共享速度，请优先选择千兆网卡；</strong></p>
<p>2）如遇公司网络限速，可添加一台路由器，创建一个新的网络，亦可实现；</p>
<p><strong>3）选择可靠性高的硬盘，如本文使用的西部数据红盘，确保运行稳定与安全；</strong></p>
<p>4）是否可以访问互联网？可以，不过需要你有一个公网IP，或者使用内网穿透工具来实现。</p>
<p>*注：本文中涉及的视频内容，仅为测试体验使用，未进行任何传播，请大家尊重影视版权，从正规渠道购买、观看影视内容，拒绝盗版。</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/wangpan.htm"><i>#</i>网盘</a><a href="https://news.mydrivers.com/tag/nas.htm"><i>#</i>NAS</a></p>
<p class="url">
     <span>原文链接：<a href="https://network.pconline.com.cn/1463/14631984.html">太平洋电脑网</a></span>
<span>责任编辑：振亭</span>
</p>
        
</div>
            