
---
title: '分布式监控系统 WGCLOUD v3.3.7 发布，新增数据告警'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b5f7561d73cfe0b41e45bd16a4e71bffd4f.png'
author: 开源中国
comments: false
date: Tue, 22 Mar 2022 09:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b5f7561d73cfe0b41e45bd16a4e71bffd4f.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.wgstart.com" target="_blank">WGCLOUD</a>是一款集成度较高的分布式运维监控系统，具有集群监控，易部署、易上手使用、轻量、高效、自动化等特点，server端基于<span style="background-color:#ffffff; color:#333333">springboot开发，agent端使用go编写。核心模块包括：<strong>主机系统信息监控，CPU监控，CPU温度监控，内存监控，网络流量监控，磁盘IO监控，磁盘空间监测，系统负载监控，硬盘smart健康检测，应用进程监控，端口监控，docker监控，日志文件监控，文件防篡改保护，数据可视化监控，自动生成拓扑图、大屏可视化，数通设备监测，服务接口监测，web ssh堡垒机，指令下发，告警信息（邮件、钉钉、微信等）推送</strong>。</span> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">码云仓库：</span><a href="https://gitee.com/wanghouhou/wgcloud">https://gitee.com/wanghouhou/wgcloud</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">GITHUB仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftianshiyeben%2Fwgcloud" target="_blank">https://github.com/tianshiyeben/wgcloud</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">http://www.wgstart.com</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>WGCLOUD支持监测的操作系统</strong></p> 
<blockquote>
 支持监测Linux系列：Debian、RedHat、CentOS、ubuntu、麒麟、统信、龙芯、树莓派、凝思等
 <br> 支持监测windows系列：Windows Server 2008 R2，2012，2016，2019，Windows 7，Windows 8，Windows 10
 <br> 支持监测unix系列：solaris，FreeBSD，OpenBSD
 <br> 支持监测macOS系列：macOS amd64，macOS arm64 
 <p style="margin-left:0; margin-right:0"> </p> 
</blockquote> 
<div style="text-align:left">
 <strong>WGCLOUD-v3.3.7 更新说明，2022-03-22：</strong>
</div> 
<div style="text-align:left"> 
 <blockquote> 
  <p>1.新增，可自定义每页显示数据条数，在server/config/application.yml配置，pageSize: 20</p> 
  <p>2.新增，磁盘smart健康检测为FAILED时，执行发送告警通知</p> 
  <p>3.新增，数据表监控告警表达式，表达式成立时即发送告警通知</p> 
  <p>4.新增，新增是否显示页面底部版权、网址信息配置项，在server/config/application.yml配置，copyRight: yes</p> 
  <p>5.新增，数通设备数据开放接口</p> 
  <p>6.新增，数通设备可以进行分组</p> 
  <p>7.新增，监测交换区内存信息</p> 
  <p>8.新增，监测进程使用线程数量指标</p> 
  <p>9.新增，拓扑图渲染增加数通设备</p> 
  <p>10.bug，端口告警次数点击bug修改</p> 
  <p>11.优化，告警缓存（静默）机制性能优化</p> 
  <p>12.优化，对所有分页列表的排序进行优化（主机、进程、数通等），默认按照资源的初始添加时间来倒序排列展示，不再按照更新时间排序了</p> 
  <p>13.优化，监控概要页面顶部两行模块，当监控资源下线时，长方块变为红色（准确说是紫褐色，褐红色）</p> 
  <p>14.优化，数通设备、服务接口、数据源、进程、端口等资源，下线后，更新时间不再变化，最后更新时间即为最后在线时间，但监控扫描工作仍会继续</p> 
  <p>15.优化，从本版本开始支持，agent依赖server分发文件方式进行升级（目前只支持linux的agent），查看下方历史版本升级说明链接</p> 
  <p>16.修复一些已知的bug</p> 
  <p>17.其他优化</p> 
 </blockquote> 
 <p> </p> 
</div> 
<p><img alt height="1389" src="https://oscimg.oschina.net/oscnet/up-b5f7561d73cfe0b41e45bd16a4e71bffd4f.png" width="1338" referrerpolicy="no-referrer"></p> 
<p><img alt height="1024" src="https://oscimg.oschina.net/oscnet/up-ed1add6052c4a6ff98d4046ef34d54a4365.jpg" width="1364" referrerpolicy="no-referrer"></p> 
<p><img alt height="1615" src="https://oscimg.oschina.net/oscnet/up-052065642e23901388afc79976df8d832ed.jpg" width="1331" referrerpolicy="no-referrer"></p> 
<p><img alt height="2438" src="https://oscimg.oschina.net/oscnet/up-a6e977e91b40a8cc8c1acda0dd5dadfc704.jpg" width="1364" referrerpolicy="no-referrer"></p> 
<p><img alt height="768" src="https://oscimg.oschina.net/oscnet/up-d354602ab47083b1b4fbec6304da0c7952f.png" width="1366" referrerpolicy="no-referrer"></p> 
<p><img alt height="554" src="https://oscimg.oschina.net/oscnet/up-c88c46d70a83d1468f893620e20a8969717.png" width="1336" referrerpolicy="no-referrer"></p> 
<p><img alt height="1463" src="https://oscimg.oschina.net/oscnet/up-a84b2b327274d8f9661b9ca10f85c8d95f7.jpg" width="1338" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            