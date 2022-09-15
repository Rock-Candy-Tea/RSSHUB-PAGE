
---
title: 'TLS指纹分析研究（上） (blog.nsfocus.net)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=9037'
author: 技术头条
comments: false
date: 2022-09-15 11:09:02
thumbnail: 'https://picsum.photos/400/300?random=9037'
---

<div>   
TLS协议已经成为互联网上最流行的协议，以确保网络通信免受干扰和窃听。TLS被用于加载Firefox浏览器中超过70%的网页，随着越来越多的网站、服务和应用程序切换到TLS，其应用将继续增长。

由于网络管理人员可以识别和阻止自定义协议，很多恶意工具已经转向使用现有协议，TLS的流行为这些恶意工具提供了一个很好的选择，使用TLS协议的恶意工具可以将其流量隐藏在大量web浏览器和其他TLS的合法覆盖流量中以逃避检测。

本文分享一篇指纹数据分析的论文，通过收集和分析9个月内超过110亿个真实的TLS连接流量，从白流量的角度给出一些结论，希望给研究人员带来一些思考。
    
</div>
            