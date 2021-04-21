
---
title: 'MySQL 8.0.24 GA'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3169'
author: 开源中国
comments: false
date: Wed, 21 Apr 2021 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3169'
---

<div>   
<div class="content">
                                                                    
                                                        <p>MySQL 8.0.24 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmysqlserverteam.com%2Fthe-mysql-8-0-24-maintenance-release-is-generally-available%2F" target="_blank">发布</a>。这是一个维护版本，修复了 219 个 Bug。其中有两位中国人的贡献（Yuxiang Jiang 和 Zhai Weixiang），他们发现 Bug 并贡献了修复的补丁程序。</p> 
<p>关于修复的具体内容，请参阅发行一览。除此之外，在下面所列的功能点进行了更新：</p> 
<ul> 
 <li> <p>MySQL Enterprise Audit 现在支持对审计日志进行删减。</p> </li> 
 <li> <p>服务器通过在关闭连接之前将原因写入连接的方法，使得客户端收到一个包含客户端超时内容的错误消息，解决了以往服务器关闭连接而客户端无法获得正确原因的问题。</p> </li> 
 <li> <p>客户端连接失败消息里添加了端口号信息。</p> </li> 
 <li> <p>MySQL Keyring 功能从插件过渡到服务器组件，包括一款社区版/企业版组件及两款企业版组件。</p> </li> 
 <li> <p>升级使用curl 7.74.0。</p> </li> 
 <li> <p>Performance Schema增加了一些新的性能指标，包括：memory/sql/dd::infrastructure，memory/sql/dd::object。并对一些已有的指标进行改进和重命名。</p> </li> 
 <li> <p>为认证插件增加了系统变量，允许配置caching_sha2_password插件运行哈希次数。</p> </li> 
 <li> <p>空间地理信息方面增加了新的函数 ST_LineInterpolatePoint() 、 ST_LineInterpolatePoints() 、ST_PointAtDistance()和ST_Collect() 。此外CAST() 和 CONVERT() 增加了对地理空间数据的支持扩展。</p> </li> 
 <li> <p> InnoDB的 AUTOEXTEND_SIZE最大值从64M 增至4GB.</p> </li> 
 <li> <p> clone_donor_timeout_after_network_failure配置的超时时间由之前的固定值5分钟扩展到最大30分钟，用以提供更多的时常去解决网络问题。</p> </li> 
 <li> <p>向MGR的allowlist里面增加新成员不再需要停止/再启动MGR。</p> </li> 
 <li> <p>使用--skip-slave-start启动从服务器不在需要登录数据库服务器的主机。</p> </li> 
</ul> 
<p>更多详情可查看官方<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmysqlserverteam.com%2Fthe-mysql-8-0-24-maintenance-release-is-generally-available%2F" target="_blank">发布说明</a>。</p> 
<p>稿源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Ftd5xbNBoM-QFFtps203EBg" target="_blank">https://mp.weixin.qq.com/s/td5xbNBoM-QFFtps203EBg</a></p>
                                        </div>
                                      
</div>
            