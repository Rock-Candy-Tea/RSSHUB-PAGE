
---
title: '分布式监控系统 WGCLOUD v3.3.6 全新发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-14ca97a77e5d203c2319a55fba817a2c2bc.png'
author: 开源中国
comments: false
date: Mon, 17 Jan 2022 03:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-14ca97a77e5d203c2319a55fba817a2c2bc.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">WGCLOUD</a>是一款集成度较高的分布式运维监控系统，具有易部署、易上手使用、轻量、高效等特点，server端基于<span style="background-color:#ffffff; color:#333333">springboot开发，agent端使用go编写。核心模块包括：<strong>主机系统信息监控，CPU监控，CPU温度监控，内存监控，网络流量监控，磁盘IO监控，磁盘空间监测，系统负载监控，硬盘smart健康检测，应用进程监控，端口监控，docker监控，日志文件监控，文件防篡改保护，数据可视化监控，自动生成拓扑图、大屏可视化，数通设备监测，服务接口监测，web ssh堡垒机，指令下发，告警信息（邮件、钉钉、微信等）推送</strong>。</span> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">码云源码下载：</span><a href="https://gitee.com/wanghouhou/wgcloud">https://gitee.com/wanghouhou/wgcloud</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">GITHUB源码下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftianshiyeben%2Fwgcloud" target="_blank">https://github.com/tianshiyeben/wgcloud</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官网下载：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">http://www.wgstart.com</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>WGCLOUD支持监测的操作系统</strong></p> 
<blockquote>
 支持监测Linux系列：Debian、RedHat、CentOS、ubuntu、麒麟、统信、龙芯、树莓派等
 <br> 支持监测windows系列：Windows Server 2008 R2，2012，2016，2019，Windows 7，Windows 8，Windows 10
 <br> 支持监测unix系列：solaris，FreeBSD，OpenBSD
 <br> 支持监测macOS系列：macOS amd64 
 <p> </p> 
</blockquote> 
<div style="text-align:left">
 <strong>WGCLOUD-v3.3.6 更新说明，2022-01-16：</strong>
</div> 
<blockquote> 
 <div style="text-align:left"> 
  <p>1.新增，主机分组功能，默认关闭，可在server/config/application.yml，通过配置项hostGroup开启使用</p> 
  <p>2.新增，主机列表【显示所有主机】,主机列表导出excel</p> 
  <p>3.新增，主机列表【自动刷新】功能，点击开启后，页面主机指标数据每30秒自动刷新</p> 
  <p>4.新增，邮件告警的标题前缀，正文签名后缀，可以自定义配置，在server/config/application.yml配置</p> 
  <p>5.新增，磁盘空间总使用率%，历史趋势图表</p> 
  <p>6.新增，主机列表，主机及其监控资源的告警次数（进程、端口、文件防篡改、docker、服务接口、数据源、数通监测等列表都已加），系统负载</p> 
  <p>7.新增，监控概要页面，系统核心配置信息及告警总次数</p> 
  <p>8.优化，web ssh前端展示UI及库包升级</p> 
  <p>9.优化，agent采用新版本golang v1.16开发编译（之前使用v1.15），提升agent性能20%</p> 
  <p>10.优化，数通设备响应时间，算法调整和优化，使之更精确</p> 
  <p>11.优化，网络带宽速率，算法调整和优化，使之更精确</p> 
  <p>12.优化，服务接口监测响应时间，算法调整和优化，使之更精确</p> 
  <p>13.优化，缩短主机下线告警通知时间（之前5分钟，此次优化到2-3分钟）</p> 
  <p>14.新增，日志文件监控，新增根据文件名称里的关键字过滤（适用于当文件夹下存在不同应用来源打印的日志文件），当监控日志为文件夹时候生效</p> 
  <p>15.新增，服务接口监测，当包含设置的关键字时候告警</p> 
  <p>16.新增，大屏展示增加显示存贮状态</p> 
  <p>17.新增，agent可监测指定网卡的传输速率指标，在agent/config/application.properties，修改配置项netInterface，默认监测所有网卡(含虚拟网卡)</p> 
  <p>18.新增，docker监控，新增支持根据docker name监测，原来contaner id方式依然支持</p> 
  <p>19.新增，服务接口监控，新增【响应内容不能包含的关键字】，含此关键字则返回500错误</p> 
  <p>20.新增，系统负载告警开关和告警值配置项，以5分钟系统负载值为准进行告警</p> 
  <p>21.新增，登录账号密码错误，在日志中记录IP</p> 
  <p>22.新增，支持PostgreSQL作为WGCLOUD数据库，原MySQL数据库依然支持</p> 
  <p>23.新增，采集主机连接数量指标，包括tcp、udp、inet</p> 
  <p>24.修复，当server部署在windows系统时，使用告警脚本发送微信、钉钉消息重复发送问题，请参考最新的告警脚本修改下即可，比之前更简单了，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fwanghouhou%2Fp%2F15351988.html" target="_blank">微信告警</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fwanghouhou%2Fp%2F13957336.html" target="_blank">钉钉告警</a></p> 
  <p>25.优化，缩短主机下线告警通知时间（之前5分钟，本版本优化到2-3分钟）</p> 
  <p>26.修复一些已知的bug，UI优化调整（比如查询框、去掉logo跳转链接等），缩短主机下线告警通知时间（之前5分钟，本版本优化到2-3分钟）</p> 
  <p> </p> 
 </div> 
</blockquote> 
<p><img alt height="1389" src="https://oscimg.oschina.net/oscnet/up-14ca97a77e5d203c2319a55fba817a2c2bc.png" width="1338" referrerpolicy="no-referrer"><img alt height="1024" src="https://oscimg.oschina.net/oscnet/up-32d44d8857bd8906b70c0a85b2339c42a3a.jpg" width="1364" referrerpolicy="no-referrer"><img alt height="1152" src="https://oscimg.oschina.net/oscnet/up-c46c4d3ad446ff420258841d8c5f3e660c8.png" width="1339" referrerpolicy="no-referrer"><img alt height="2438" src="https://oscimg.oschina.net/oscnet/up-91cfa6ef3502d517f733d5002cffee2791a.jpg" width="1364" referrerpolicy="no-referrer"><img alt height="579" src="https://oscimg.oschina.net/oscnet/up-445e47023ddfd56df3a6ab992bb49b362fe.jpg" width="935" referrerpolicy="no-referrer"><img alt height="554" src="https://oscimg.oschina.net/oscnet/up-61f0643316376794fb72f3ef985b11976f1.png" width="1336" referrerpolicy="no-referrer"> </p> 
<p><img alt height="768" src="https://oscimg.oschina.net/oscnet/up-85b7de023964351fd33b2bcd55701130c8c.png" width="1366" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            