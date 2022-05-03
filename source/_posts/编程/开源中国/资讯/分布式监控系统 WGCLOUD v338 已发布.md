
---
title: '分布式监控系统 WGCLOUD v3.3.8 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b911ebed468e1ce057fe69b7b54da56b2fb.png'
author: 开源中国
comments: false
date: Mon, 02 May 2022 12:08:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b911ebed468e1ce057fe69b7b54da56b2fb.png'
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
</blockquote> 
<p><strong style="color:#212529">WGCLOUD-v3.3.8更新说明，2022-05-02发布</strong></p> 
<blockquote> 
 <p><strong style="color:#212529">WGCLOUD-v3.3.8更新说明，2022-05-02发布</strong></p> 
 <p>1.新增，SNMP监控交换机流量</p> 
 <p>2.新增，docker监控支持采集容器NAMES、容器端口、Image、创建时间、运行状态等指标，不再监测CPU系统时间和CPU用户时间这两个指标</p> 
 <p>3.新增，进程、端口、docker、数通PING，支持一次批量添加多个</p> 
 <p>4.新增，端口监控可以监控指定目标主机的端口，由agent执行<code>telnet 目标IP 目标端口</code>来测试端口连通性，原agent配置文件中的telnetIp配置项不再使用</p> 
 <p>5.新增，进程监控添加采集PID指标，这样可以更清晰的识别进程</p> 
 <p>6.新增，进程、端口、docker可以进行分组，依然在系统管理菜单中维护分组</p> 
 <p>7.新增，服务接口监测，当接口为POST时，支持设置header的键值对信息</p> 
 <p>8.新增，指令下发，支持立即下发和定时下发两种模式。新增【已下发】状态，主要用于支持重启agent、关闭agent等指令</p> 
 <p>9.优化，公众看板页面，未登录时，对主机IP进行脱敏显示，可在server/config/application.yml自定义是否开启脱敏，配置项dashViewIpHide: yes</p> 
 <p>10.优化，列表页面的【告警次数】该列默认不再展示，若想展示，可在server/config/application.yml中开启，配置项showWarnCount: no</p> 
 <p>11.优化，主机上下行传输速率告警通知，由KB转为MB/s显示</p> 
 <p>12.优化，数据监控的自定义sql语句，不能编写出现的敏感字符，改为可以在配置文件在server/config/application.yml自定义，配置项sqlInKeys，已有默认值，和之前版本相同</p> 
 <p>13.优化，分页组件底部增加显示共多少条</p> 
 <p>14.优化，日志文件监控，改造为提取显示包含设置告警关键字的整行日志内容，不再只显示包含告警关键字的行数</p> 
 <p>15.bug修复，docker bug修改，修改docker信息时候，初始用container id 修改为初始用container name，修改完后 自动又变成id</p> 
 <p>16.对基础架构及依赖库进行升级，提升性能、安全性、稳定性</p> 
 <p>17.UI、程序等优化，修复一些已知的bug</p> 
</blockquote> 
<p><img alt height="1389" src="https://oscimg.oschina.net/oscnet/up-b911ebed468e1ce057fe69b7b54da56b2fb.png" width="1338" referrerpolicy="no-referrer"></p> 
<p><img alt height="1024" src="https://oscimg.oschina.net/oscnet/up-0211c057fd7e75d3a10fceee6e53ef7e558.jpg" width="1364" referrerpolicy="no-referrer"></p> 
<p><img alt height="1615" src="https://oscimg.oschina.net/oscnet/up-9201837657fc3ec802173cd503bdd83a608.jpg" width="1331" referrerpolicy="no-referrer"></p> 
<p><img alt height="2438" src="https://oscimg.oschina.net/oscnet/up-3d4ebac7de86737c00f31502241728b6fef.jpg" width="1364" referrerpolicy="no-referrer"></p> 
<p><img alt height="768" src="https://oscimg.oschina.net/oscnet/up-d338d54673983c1f4f38db9db35e4a4c74c.png" width="1366" referrerpolicy="no-referrer"></p> 
<p><img alt height="554" src="https://oscimg.oschina.net/oscnet/up-a6682df30ab8c25999cd14c7a1019c24e31.png" width="1336" referrerpolicy="no-referrer"></p> 
<p><img alt height="579" src="https://oscimg.oschina.net/oscnet/up-95c75702988b845e51fe8bc2e815a44a46a.jpg" width="935" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            