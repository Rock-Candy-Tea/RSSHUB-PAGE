
---
title: '研华基于NXP i．MX8M Mini 处理器开发ROM-5721 SMARC核心模块'
categories: 
 - 新媒体
 - 高科技行业门户
 - 新闻
headimg: 'https://mp.ofweek.com/Upload/News/Img/member33423/202108/wx_article__4569d1dda2876c898d6043fffc4cfe70.jpg'
author: 高科技行业门户
comments: false
date: Thu, 12 Aug 2021 10:20:00 GMT
thumbnail: 'https://mp.ofweek.com/Upload/News/Img/member33423/202108/wx_article__4569d1dda2876c898d6043fffc4cfe70.jpg'
---

<div>   
<p style="text-indent: 2em; text-align: left;">即时检测(Point of Care Testing, POCT)是一种在采样现场进行、 利用便携式分析仪器及配套试剂快速得到结果的检测方式。随着POCT技术愈发成熟,其被广泛应用于临床检验、检验检疫、传染病监测、应急反恐、慢性病监测、食品安全、毒品检验、灾害医学救援等公共卫生领域。近些年POCT市场规模快速扩大,对行业技术平台更新与升级的要求也相应提高。</p><p style="text-indent: 2em; text-align: left;">研华基于NXP i．MX8M Mini 处理器开发的ROM-5721 SMARC 核心模块,兼顾性能、功耗与性价比,是POCT设备理想的升级方案。</p><p style="text-align:center"><img src="https://mp.ofweek.com/Upload/News/Img/member33423/202108/wx_article__4569d1dda2876c898d6043fffc4cfe70.jpg" referrerpolicy="no-referrer"></p><p style="text-indent: 2em; text-align: left;">01POCT设备设计难点</p><p style="text-indent: 2em; text-align: left;">国内某大型医疗设备企业,是国内重要的头部POCT设备商之一,为实现旧产品升级换代,规划新式便携式POCT设备。客户设备为便携式,设备内部电池供电,需要持续48小时待机或连续测试50个标本,因此对主控板的功耗有着极高的需求。另外,该设备拥有较多的外设,需要能够提供丰富I/O接口的平台。且客户具有一系列的功能定制需求,如产品远程OTA升级、启动时长优化、以太网功能设置、超低功耗休眠模式、屏幕唤醒等功能。除此之外,由于行业的特殊性,客户对主控板的成本预算有限。</p><p style="text-indent: 2em; text-align: left;">面临的挑战</p><p style="text-indent: 2em; text-align: left;">实现设备待机48小时或连续测试50个标本的超低功耗方案</p><p style="text-indent: 2em; text-align: left;">在Android操作系统下多种软件定制功能的实现</p><p style="text-indent: 2em; text-align: left;">方案成本考量,要求高性价比</p><p style="text-indent: 2em; text-align: left;">医疗长生命周期供货</p><p style="text-indent: 2em; text-align: left;">02研华解决方案</p><p style="text-align:center"><img src="https://mp.ofweek.com/Upload/News/Img/member33423/202108/wx_article__276cf5c30a73bb2536c2beac4c6f0a9a.jpg" referrerpolicy="no-referrer"></p><p style="text-indent: 2em; text-align: center;">研华ROM-5721 POCT应用场景图</p><p style="text-indent: 2em; text-align: left;">硬件方案</p><p style="text-indent: 2em; text-align: left;">研华ROM-5721 SMARC 2．1核心模块,基于全新NXP i．MX8M Mini高效能Arm平台,支持4*Arm Cortex-A53 主频1．8GHz,拥有1*Arm Cortex-M4内核,可处理实时控制程序。并且ROM-5721拥有丰富的I/O扩展接口,如4*USB*UART*I2C*I2S*SPI*PCIe*GPIO等,满足客户应用的外设需求。并且研华技术团队还针对客户的软件功能需求,进行了及时响应,帮助客户全面测试评估该产品性能、功能及功耗数据。</p><p style="text-indent: 2em; text-align: left;">Android/Linux下休眠(suspend)及唤醒方案</p><p style="text-indent: 2em; text-align: left;">很多客户存在误解,认为LCD背光关掉,即进入休假模式。其实这是假休眠,因为CPU等主要的器件都仍在运行中,功耗减少有限。</p><p style="text-indent: 2em; text-align: left;">真正的休眠,是指系统进入Suspend Mode。研华的ROM-5721核心模块,经过测试,进入Suspend模式后,功耗仅为0．8W,成功解决客户担心的便携设备待机时长问题。</p><p style="text-indent: 2em; text-align: left;">此外,进入Suspend后再唤醒,需要保证USB, LAN,UART等接口的数据恢复,这也给软件带来了很大的挑战。研华的软件团队,则能协助客户克服唤醒后的数据恢复难题。</p><p style="text-indent: 2em; text-align: left;">底板的开发设计服务</p><p style="text-indent: 2em; text-align: left;">在开发设计中,研华还为客户载板设计提供参考服务,提供研华标准评估板原理图、设计指南与检查表来协助客户载板开发。除了设计文档外,研华还提供分享包括收发器和发射器IC推荐选项在内的设计参考。客户完成载板原理图后,研华还会帮助客户进行审查,提出载板设计的相关建议,帮助客户产品快速上市。</p><p style="text-indent: 2em; text-align: left;">另外该产品提供10年以上的供货生命周期,具有高性价比。研华以优质的服务满足该医疗客户需求,最终赢得客户合作。</p><p style="text-indent: 2em; text-align: left;">研华ROM-5721核心模块已经量产和成熟应用</p><p style="text-indent: 2em; text-align: left;">欢迎POCT行业应用用户咨询</p> 
  
</div>
            