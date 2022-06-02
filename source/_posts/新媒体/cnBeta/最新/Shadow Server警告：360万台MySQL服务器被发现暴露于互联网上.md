
---
title: 'Shadow Server警告：360万台MySQL服务器被发现暴露于互联网上'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0602/47842dd6043ced9.png'
author: cnBeta
comments: false
date: Thu, 02 Jun 2022 04:52:31 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0602/47842dd6043ced9.png'
---

<div>   
<strong>网络安全研究组织 Shadowserver Foundation 上周扫描发现，互联网上有近 360 万台 MySQL 服务器在使用默认的 3306 号 TCP 端口。</strong>报告写道：尽管其未深入分析数据库的访问级别 / 暴露程度，但这一潜在攻击面本该是可以轻松规避的。从地区来看，美国以 120 万+高居第一，其次是中国、德国、新加坡、荷兰、以及波兰。<br>
  <p><img src="https://static.cnbetacdn.com/article/2022/0602/47842dd6043ced9.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">IPv6 连接分布（来自：<a href="https://www.shadowserver.org/news/over-3-6m-exposed-mysql-servers-on-ipv4-and-ipv6/" target="_self">Shadow Server</a>）</p><p><a href="https://www.bleepingcomputer.com/news/security/over-36-million-mysql-servers-found-exposed-on-the-internet/" target="_self">Bleeping Computer</a> 指出：超过 360 万台暴露于互联网上的 MySQL 服务器会公开响应查询，使之成为了对黑客与勒索者极具吸引力的攻击目标。</p><p>此外在这些可访问的 MySQL 服务其中，有 230 万台基于 IPv4 连接、另有 130 万台设备采用了 IPv6 连接。</p><p>尽管 Web 服务器和应用程序连接到远端数据库的操作很是常见，但在合理的安全实践中，本该锁定相关实例、以只允许授权设备连接。</p><p>即使不得不暴露于互联网上，服务器端也该始终伴随着严格的用户策略、修改默认访问端口（3306）、启用二进制日志记录、以及密切监视所有查询并落实加密。</p><p><img src="https://static.cnbetacdn.com/article/2022/0602/594391e3b3c8a50.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">MySQL 版本分布</p><p><strong>详细的扫描结果如下：</strong></p><blockquote><p>● IPv4 总暴露量：395 万 7457 台服务器</p><p>● IPv6 总暴露量：142 万 1010 台服务器</p><p>● IPv4 服务器查询响应总数：227 万 9908 次</p><p>● IPv6 服务器查询响应总数：134 万 3993 次</p><p>● 此外在所有暴露的 MySQL 服务器中，有近 67% 都可通过互联网进行访问。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0602/b99dc66415dccb1.png" referrerpolicy="no-referrer"></p><p>据悉，数据盗窃的常见来源之一，就是安保失当的各类数据库。管理员应始终锁定数据库，以防止任何未经授权的远程访问。</p><p>除了灾难性的数据泄露，配置失误的数据库服务器还可能遭到破坏性攻击、勒索软件 / 远程访问木马（RAT）感染，甚至 Cobalt Strike 攻击。</p><p>想要了解如何如何安全地部署 MySQL 服务器、并消除潜在的系统安全漏洞，Shadow Server 建议管理员阅读 <a href="https://downloads.mysql.com/docs/mysql-secure-deployment-guide-5.7-en.a4.pdf" target="_self">5.7</a> / <a href="https://dev.mysql.com/doc/mysql-secure-deployment-guide/8.0/en/" target="_self">8.0</a> 版本的实施指南。</p>   
</div>
            