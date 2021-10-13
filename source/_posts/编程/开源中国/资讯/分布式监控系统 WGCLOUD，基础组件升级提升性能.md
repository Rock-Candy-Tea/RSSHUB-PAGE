
---
title: '分布式监控系统 WGCLOUD，基础组件升级提升性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-388093f84d8081094a519c96c9ef5797635.png'
author: 开源中国
comments: false
date: Wed, 13 Oct 2021 03:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-388093f84d8081094a519c96c9ef5797635.png'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">WGCLOUD</a>是一款集成度较高的分布式运维监控系统，具有易部署、易上手使用、轻量、高效等特点，server端基于<span style="background-color:#ffffff; color:#333333">springboot开发，agent端使用go编写。核心模块包括：<strong>主机系统信息监控，CPU监控，CPU温度监控，内存监控，网络流量监控，磁盘IO监控，磁盘空间监测，系统负载监控，硬盘smart健康检测，应用进程监控，端口监控，docker监控，日志文件监控，文件防篡改保护，数据可视化监控，自动生成拓扑图、大屏可视化，数通设备监测，服务接口监测，web ssh堡垒机，指令批量下发执行，告警信息（邮件、钉钉、微信等）推送</strong>。</span> </p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">码云源码下载：</span><a href="https://gitee.com/wanghouhou/wgcloud">https://gitee.com/wanghouhou/wgcloud</a></p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">GITHUB源码下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftianshiyeben%2Fwgcloud" target="_blank">https://github.com/tianshiyeben/wgcloud</a></p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">http://www.wgstart.com</a></p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>支持运行系统</strong></p> 
   <blockquote> 
    <div>
     支持监测Linux系列：Debian、RedHat、CentOS、ubuntu、麒麟、统信、龙芯、树莓派等
     <br> 支持监测windows系列：windows server2003以上(不含2003)，win7，win8，win10等
     <br> 支持监测unix系列：solaris，FreeBSD，OpenBSD
     <br> 支持监测macOS系列：macOS amd64
    </div> 
   </blockquote> 
   <div style="text-align:start"> 
    <div> 
     <div style="text-align:left"> 
      <div style="text-align:left">
       <strong>WGCLOUD-v3.3.5 更新说明，2021-09-26：</strong>
      </div> 
      <blockquote> 
       <div style="text-align:left"> 
        <p style="margin-left:0; margin-right:0">1.新增，agent端可自定义开启/关闭执行下发指令，默认关闭</p> 
        <p style="margin-left:0; margin-right:0">2.新增，批量删除主机、端口、进程、docker、日志监控等</p> 
        <p style="margin-left:0; margin-right:0">3.新增，批量添加端口、进程、docker、日志监控监控</p> 
        <p style="margin-left:0; margin-right:0">4.新增，文件防篡改保护机制，监测主机上的文件是否被篡改，发现篡改时发送告警通知</p> 
        <p style="margin-left:0; margin-right:0">5.新增，数据表统计导出excel</p> 
        <p style="margin-left:0; margin-right:0">6.新增，server支持在JDK11运行，原JDK1.8依然支持</p> 
        <p style="margin-left:0; margin-right:0">7.新增，一个只读账号，登陆后只能浏览查看，没有新增、修改、删除权限</p> 
        <p style="margin-left:0; margin-right:0">8.新增，统计分析报表，多维度图表分析所有主机整体运行状态</p> 
        <p style="margin-left:0; margin-right:0">9.新增，支持数据库连接状态指标监测，如用户数量、当前连接数量等</p> 
        <p style="margin-left:0; margin-right:0">10.优化，大屏展示</p> 
        <p style="margin-left:0; margin-right:0">11.新增，使用https时候，web ssh前端页面web socket使用443端口，如wss://domain:443/ws</p> 
        <p style="margin-left:0; margin-right:0">12.新增，守护进程(wgcloud-daemon-release)端口9997，再也不用开启给agent主机访问了，能让server访问到守护进程就可以了，server和守护进程在一个主机，就是本机访问，不存在防火墙开启端口的问题了，就是agent->server->守护进程</p> 
        <p style="margin-left:0; margin-right:0">13.bug，修复进程、docker导出excel的bug</p> 
        <p style="margin-left:0; margin-right:0">14.优化，对server基础架构组件进行了整体升级</p> 
        <p style="margin-left:0; margin-right:0">15.bug，修复一些已知的bug</p> 
       </div> 
      </blockquote> 
      <p style="margin-left:0; margin-right:0"><img alt height="1477" src="https://oscimg.oschina.net/oscnet/up-388093f84d8081094a519c96c9ef5797635.png" width="1348" referrerpolicy="no-referrer"><img alt height="1024" src="https://oscimg.oschina.net/oscnet/up-32e13b07e8b44534af3364ba5280b017c8b.jpg" width="1364" referrerpolicy="no-referrer"><img alt height="1152" src="https://oscimg.oschina.net/oscnet/up-a504954236a6da6e497fbc85ad54598dac6.png" width="1339" referrerpolicy="no-referrer"><img alt height="2438" src="https://oscimg.oschina.net/oscnet/up-d32484697cf6d0ef680b1865f705375e5d8.jpg" width="1364" referrerpolicy="no-referrer"><img alt height="579" src="https://oscimg.oschina.net/oscnet/up-23942869c7af23f9b7be084ebe7b2a65575.jpg" width="935" referrerpolicy="no-referrer"><img alt height="554" src="https://oscimg.oschina.net/oscnet/up-42b3d9ee18d2adeb6eca9309657c36f48bb.png" width="1336" referrerpolicy="no-referrer"><img alt height="1463" src="https://oscimg.oschina.net/oscnet/up-33f3c8edf74acd1a7487289734b9cec87ea.jpg" width="1338" referrerpolicy="no-referrer"></p> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            