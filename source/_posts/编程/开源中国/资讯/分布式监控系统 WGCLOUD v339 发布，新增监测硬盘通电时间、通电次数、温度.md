
---
title: '分布式监控系统 WGCLOUD v3.3.9 发布，新增监测硬盘通电时间、通电次数、温度'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b143a7ccd3a4136814d9cc6b84e6dfbe911.png'
author: 开源中国
comments: false
date: Wed, 29 Jun 2022 13:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b143a7ccd3a4136814d9cc6b84e6dfbe911.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.wgstart.com" target="_blank">WGCLOUD</a><span> </span>是一款集成度较高的分布式运维监控系统，具有集群监控，易部署、易上手使用、轻量、高效、自动化等特点，server 端基于<span style="background-color:#ffffff; color:#333333"><span> </span>springboot 开发，agent 端使用 go 编写。核心模块包括：<strong>主机系统信息监控，CPU 监控，CPU 温度监控，内存监控，网络流量监控，磁盘 IO 监控，磁盘空间监测，系统负载监控，硬盘 smart 健康检测，应用进程监控，端口监控，docker 监控，日志文件监控，文件防篡改保护，数据可视化监控，自动生成拓扑图、大屏可视化，数通设备监测，服务接口监测，web ssh 堡垒机，指令下发，告警信息（邮件、钉钉、微信等）推送</strong>。</span> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">码云仓库：</span><a href="https://gitee.com/wanghouhou/wgcloud">https://gitee.com/wanghouhou/wgcloud</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">GITHUB 仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftianshiyeben%2Fwgcloud" target="_blank">https://github.com/tianshiyeben/wgcloud</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">http://www.wgstart.com</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>WGCLOUD 支持监测的操作系统</strong></p> 
<blockquote> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持监测Linux系列：Debian、RedHat、CentOS、Ubuntu、Fedora、麒麟、统信、龙芯、树莓派等<br> 支持监测Windows系列：Windows Server 2008 R2，2012，2016，2019，2022，Windows 7，Windows 8，Windows 10，Windows 11<br> 支持监测Unix系列：solaris，FreeBSD，OpenBSD<br> 支持监测MacOS系列：macOS amd64<br> 支持监测Android（安卓）：arm64，arm32</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#212529">WGCLOUD-v3.3.9 更新说明，2022-06-29 发布</strong></p> 
<blockquote> 
 <p>1.新增，交换机监测流量改造为，每次可以添加多个入端口和多个出端口，来汇聚监测整体出入流量</p> 
 <p>2.新增，多用户管理，即每个用户可管理自己的主机和监控资源，支持给资源所属用户发送告警，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.wgstart.com%2Fhelp%2Fdocs66.html" target="_blank">查看使用说明</a></p> 
 <p>3.新增，web ssh 支持密钥文件登录</p> 
 <p>4.新增，告警通知支持时间段cron表达式配置，即在配置的时间段内发送告警，其他时间不发告警，默认为空即持续发送，</p> 
 <p>在配置文件server/config/application.yml修改，配置项warnCronTime:</p> 
 <p>5.新增，一套大屏，加上之前的大屏，一共两套大屏</p> 
 <p>6.新增，在硬盘SMART健康监测基础上，增加监测硬盘通电时间、通电次数、温度等指标</p> 
 <p>7.新增，监控概要页面环状图表增加SNMP数量</p> 
 <p>8.新增，数据表列表页面，增加查询条件数据表别名</p> 
 <p>9.新增，所有图表增加显示副标题，内容为图表趋势图数据的最大值、平均值、最小值</p> 
 <p>10.优化，新加入的主机发送通知</p> 
 <p>11.优化，基础组件升级，提升性能</p> 
 <p>12.优化，UI、程序结构</p> 
 <p>13.BUG，修复一些已知的bug</p> 
 <p>14.历史版本升级请点击，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.wgstart.com%2Fhelp%2Fdocs6.html" target="_blank">历史版本升级说</a></p> 
</blockquote> 
<p><img alt height="1389" src="https://oscimg.oschina.net/oscnet/up-b143a7ccd3a4136814d9cc6b84e6dfbe911.png" width="1338" referrerpolicy="no-referrer"> </p> 
<p><img alt height="1024" src="https://oscimg.oschina.net/oscnet/up-af46e856267bcb4b4d1ddbea6361e5c45cf.jpg" width="1364" referrerpolicy="no-referrer"></p> 
<p><img alt height="1800" src="https://oscimg.oschina.net/oscnet/up-4ebb3f587df1a30b3c6774646047cc4df6b.jpg" width="1344" referrerpolicy="no-referrer"></p> 
<p><img alt height="2493" src="https://oscimg.oschina.net/oscnet/up-80127a56aff5a1da18d29cc3a208115e715.jpg" width="1339" referrerpolicy="no-referrer"></p> 
<p><img alt height="768" src="https://oscimg.oschina.net/oscnet/up-183172f1f7e6b6a3ac3b5544d1b28189f65.png" width="1366" referrerpolicy="no-referrer"></p> 
<p><img alt height="750" src="https://oscimg.oschina.net/oscnet/up-412dfebfd70a94cfccbc4f9434d88923be4.jpg" width="1345" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            