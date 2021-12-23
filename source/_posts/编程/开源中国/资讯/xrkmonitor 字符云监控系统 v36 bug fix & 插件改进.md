
---
title: 'xrkmonitor 字符云监控系统 v3.6 bug fix & 插件改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cors.zfour.workers.dev/?http://xrkmonitor.com/uploads/20211222/93d2bd96c2255ea84cc07feb1012e8d0.png'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 11:06:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://xrkmonitor.com/uploads/20211222/93d2bd96c2255ea84cc07feb1012e8d0.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0">该版本主要改进了插件机制，修复了部分bug 以及支持 c/c++ 插件开发，主要修改点如下：</p> 
<ol> 
 <li>优化内网模式下 udp 传输性能（响应包默认关闭，丢包时自动开启）</li> 
 <li>日志api 接口优化</li> 
 <li>新增插件 (内网穿透/网络监控/mysql监控等)</li> 
 <li>插件的表格名、字段名支持变量替换，变量可以是插件的配置项</li> 
 <li>修复部分 bug</li> 
</ol> 
<p>版本详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fxrkmonitor.com%2Fa%2Fxrk_news_v36.html" target="_blank">http://xrkmonitor.com/a/xrk_news_v36.htm</a> </p> 
<p style="margin-left:0; margin-right:0"><strong>UDP 传输性能优化说明：</strong></p> 
<p style="margin-left:0; margin-right:0">3.6 之前的版本使用的可靠upd 即agent 每发一个请求包 server 都会回复响应包，通常内网模式下 udp 丢包是比较少见的，改进后agent 的请求包中会携带自己发送的包量，server 会统计自己的收包量并比对agent 的发送包量，相差超过阀值则会发送响应包，agent 收到响应包会开启一段时间的可靠udp，该机制默认开启，如需关闭修改配置：UDP_ENABLE_AUTO_RETRY 0</p> 
<p style="margin-left:0; margin-right:0"><strong>插件实时表格名、字段名的变量替换功能</strong></p> 
<p style="margin-left:0; margin-right:0">插件实时表格用于体现插件的当前工作信息、状态等，表格的数据只在内存中保存，表格的名字和字段名在3.6之前的版本是插件编写时就已配置好，3.6改进了插件表格名和字段名，支持使用配置作为变量，展示时从插件的配置文件中提取配置值替换到表格名或字段名中，插件： “Linux 进程守护” 就用到了这个功能。</p> 
<p style="margin-left:0; margin-right:0"><strong>新增插件：mysql 主从同步监控</strong></p> 
<p style="margin-left:0; margin-right:0">mysql 主从同步插件，主要通过监控io/sql 线程状态以及同步文件的位置变化判断主从同步机制工作是否正常<img alt src="https://cors.zfour.workers.dev/?http://xrkmonitor.com/uploads/20211222/93d2bd96c2255ea84cc07feb1012e8d0.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>新增插件：内网穿透</strong></p> 
<p style="margin-left:0; margin-right:0">内网穿透插件包含内网端和访问端，内网穿透可将内网指定的服务映射到访问端所在的网络，支持访问端直连内网端， 支持穿透任何基于udp/tcp 的服务（包括但不限于：ftp, smtp, pop3, mysql,ssh, html, samba, 远程桌面等）。内网穿透插件可以以独立模式运行，以插件模式运行则可以监控流量穿透信息</p> 
<div>
 内网穿透在线文档：
</div> 
<div>
 内网端：
 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fxrkmonitor.com%2Fmonitor%2Fshowdoc%2Fshowdoc%2Fweb%2F%23%2F4%3Fpage_id%3D129" target="_blank">http://xrkmonitor.com/monitor/showdoc/showdoc/web/#/4?page_id=129</a>
</div> 
<div>
 访问端：
 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fxrkmonitor.com%2Fmonitor%2Fshowdoc%2Fshowdoc%2Fweb%2F%23%2F4%3Fpage_id%3D130" target="_blank">http://xrkmonitor.com/monitor/showdoc/showdoc/web/#/4?page_id=130</a>
</div> 
<div>
 p2p直连穿透演示：
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1544y177Th%2F" target="_blank">https://www.bilibili.com/video/BV1544y177Th/</a>
</div> 
<div> 
 <p> </p> 
</div>
                                        </div>
                                      
</div>
            