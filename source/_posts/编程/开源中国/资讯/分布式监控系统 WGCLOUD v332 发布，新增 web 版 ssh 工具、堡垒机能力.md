
---
title: '分布式监控系统 WGCLOUD v3.3.2 发布，新增 web 版 ssh 工具、堡垒机能力'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c552b937b784c5df5151841040eef344930.JPEG'
author: 开源中国
comments: false
date: Thu, 29 Apr 2021 13:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c552b937b784c5df5151841040eef344930.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">WGCLOUD</a>，server端基于<span style="background-color:#ffffff; color:#333333">springboot开发，agent端使用go编写。支持高并发高性能，核心模块包括：<strong>主机监控，ES集群管理，CPU监控，CPU温度监控，内存监控，数据监控，docker监控，网络流量监控，服务接口心跳检测，应用进程管理，磁盘IO监控，系统负载监控，端口监控，大屏可视化，日志文件监控，硬盘smart健康检测，web版ssh工具，堡垒机，监控告警信息（默认邮件，支持钉钉微信集成）推送</strong>。</span> </p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">码云源码下载：</span><a href="https://gitee.com/wanghouhou/wgcloud">https://gitee.com/wanghouhou/wgcloud</a></p> 
<p style="text-align:left">GITHUB源码下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftianshiyeben%2Fwgcloud" target="_blank">https://github.com/tianshiyeben/wgcloud</a></p> 
<p style="text-align:left">安装包下载：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">http://www.wgstart.com</a></p> 
<p style="text-align:left"><strong>WGCLOUD-v3.3.2更新说明，2021-04-29：</strong></p> 
<blockquote> 
 <div style="text-align:left">
  <strong>WGCLOUD-v3.3.2更新说明，2021-04-29发布</strong> 
  <p>1.新增，web shh终端，相当于堡垒机（跳板机），在浏览器即可通过ssh连接到主机，进行shell指令执行。在浏览器远程连接windows，需要在windows安装远程连接服务，如：Myrtille工具、Remote desktop web connection工具</p> 
  <p>2.新增，大屏展板是否开启配置项，在/server/config/application.yml配置选项dapingView，之前版本和公众看板共用配置项dashView</p> 
  <p>3.新增，DOCKER下线告警配置项，之前版本和进程下线告警共用配置项appDownWarnMail</p> 
  <p>4.新增，主机的上行带宽速率和下行带宽速率告警</p> 
  <p>5.新增，主机的网络传输丢包数量指标图表</p> 
  <p>6.新增，数据开放接口：获取主机cpu状态数据、获取主机系统负载数据、获取主机内存状态数据、获取主机磁盘容量数据、获取主机磁盘io数据、获取主机cpu温度数据、获取主机上下行带宽数据</p> 
  <p>7.新增，日志文件监控扫描间隔可配置，之前版本默认10分钟扫描一次日志文件，在agent/config/application.properties下配置</p> 
  <p>8.优化，agent采用新版本golang v1.15.11编译打包（之前使用v1.13.8），优化提升agent性能</p> 
  <p>9.优化，agent引入自动清理日志文件机制，节省磁盘空间，可在agent/config/application.properties配置日志文件保留天数</p> 
  <p>10.优化，图表渲染速度、显示及配色</p> 
  <p>11.优化，改造优化大屏展示</p> 
  <p>12.优化，对下线的进程、端口、docker、主机信息不再自动删除（之前版本会和历史数据一起清除），用户可以手动删除。但是监控指标的历史数据依然自动清除</p> 
  <p>13.bug，修复未登录时跳转到404页面，会显示导航菜单的问题</p> 
  <p>14.底层架构重构、性能优化、UI整体优化</p> 
  <p>15.历史版本升级请点击，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.wgstart.com%2Fhelp%2Fdocs6.html" target="_blank">历史版本升级说明</a></p> 
 </div> 
</blockquote> 
<p><img alt height="1454" src="https://oscimg.oschina.net/oscnet/up-c552b937b784c5df5151841040eef344930.JPEG" width="1364" referrerpolicy="no-referrer"> </p> 
<p><img alt height="1024" src="https://oscimg.oschina.net/oscnet/up-86f436e9061ead32d94dea0d4e9f243fc52.JPEG" width="1364" referrerpolicy="no-referrer"></p> 
<p><img alt height="2438" src="https://oscimg.oschina.net/oscnet/up-a6a971c647d291756a7f6a90723373ec680.JPEG" width="1364" referrerpolicy="no-referrer"></p> 
<p><img alt height="768" src="https://oscimg.oschina.net/oscnet/up-3335153828e01c99eaac442bd66d8126a2d.JPEG" width="1366" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            