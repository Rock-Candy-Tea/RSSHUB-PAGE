
---
title: 'WGCLOUD 监控系统，v3.3.4 增强版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-15c61b93995008ffe85ca2063a9cacdd768.png'
author: 开源中国
comments: false
date: Tue, 14 Sep 2021 14:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-15c61b93995008ffe85ca2063a9cacdd768.png'
---

<div>   
<div class="content">
                                                                                            <p>v3.3.4增强版百度网盘下载，请在v3.3.4版基础上更新：</p> 
<div>
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpan.baidu.com%2Fs%2F1L0yxDBjnvcgR6sqjoPFxLw%23list%2Fpath%3D%252Fwgcloud%25E4%25B8%258B%25E8%25BD%25BD%252Fv3.3.5-pre" target="_blank">https://pan.baidu.com/s/1L0yxDBjnvcgR6sqjoPFxLw#list/path=%2Fwgcloud%E4%B8%8B%E8%BD%BD%2Fv3.3.5-pre</a>
</div> 
<div>
  
</div> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <div style="text-align:start"> 
    <div> 
     <div style="text-align:left"> 
      <p style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">WGCLOUD</a>是一款集成度较高的分布式运维监控系统，具有易部署、易上手使用、轻量、高效等特点，server端基于<span style="background-color:#ffffff; color:#333333">springboot开发，agent端使用go编写。核心模块包括：<strong>主机系统信息监控，CPU监控，CPU温度监控，内存监控，网络流量监控，磁盘IO监控，磁盘空间监测，系统负载监控，硬盘smart健康检测，应用进程监控，端口监控，docker监控，日志文件监控，数据可视化监控，自动生成拓扑图、大屏可视化，数通设备监测，服务接口监测，web ssh堡垒机，指令下发，告警信息（邮件、钉钉、微信等）推送</strong>。</span> </p> 
      <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">码云源码下载：</span><a href="https://gitee.com/wanghouhou/wgcloud">https://gitee.com/wanghouhou/wgcloud</a></p> 
      <p style="margin-left:0; margin-right:0; text-align:left">GITHUB源码下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftianshiyeben%2Fwgcloud" target="_blank">https://github.com/tianshiyeben/wgcloud</a></p> 
      <p style="margin-left:0; margin-right:0; text-align:left">官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">http://www.wgstart.com</a></p> 
      <p style="margin-left:0; margin-right:0; text-align:left"><strong>支持运行系统</strong></p> 
      <blockquote> 
       <div>
        支持监测Linux系列：Debian、RedHat、CentOS、ubuntu、麒麟、统信、龙芯、树莓派等
        <br> 支持监测windows系列：windows server2003以上(不含2003)，win7，win8，win10等
        <br> 支持监测unix系列：solaris，FreeBSD，OpenBSD
        <br> 支持监测macOS系列：macOS amd64
       </div> 
      </blockquote> 
      <div>
       <strong>WGCLOUD-v3.3.4 增强版更新说明，2021-09-14：</strong>
      </div> 
      <blockquote> 
       <div style="text-align:left"> 
        <div> 
         <p>1.新增，agent端可自定义开启/关闭执行下发指令，默认关闭<br> 2.新增，批量删除主机、端口、进程、docker、日志监控功能等<br> 3.新增，批量添加进程、端口、docker、日志文件监控<br> 4.新增，数据表统计导出excel<br> 5.新增，日志监控告警内容列表导出excel<br> 6.新增，server支持在JDK11运行，原JDK1.8依然支持<br> 7.优化，大屏展示<br> 8.新增，使用https时候，web socket使用443端口，如wss://domain:443/ws<br> 9.新增，守护进程(wgcloud-daemon-release)端口9997，再也不用开启给agent主机访问了，agent会通过server中转和守护进程通信<br> 10.bug，修复进程、docker趋势图导出excel的bug</p> 
        </div> 
       </div> 
      </blockquote> 
      <p style="margin-left:0; margin-right:0"><img src="https://oscimg.oschina.net/oscnet/up-15c61b93995008ffe85ca2063a9cacdd768.png" referrerpolicy="no-referrer"></p> 
      <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-0dcb8624d74dff0779887a486f5e363f308.JPEG" referrerpolicy="no-referrer"></p> 
      <p style="margin-left:0; margin-right:0"><img src="https://oscimg.oschina.net/oscnet/up-cf1e23392dfd1542489ebc35d9068c82080.png" referrerpolicy="no-referrer"></p> 
      <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-76d4f20abe4582872065f185cbc55c2231b.JPEG" referrerpolicy="no-referrer"></p> 
      <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-778611bea405bfc79e5148aa2a0be4fccaf.JPEG" referrerpolicy="no-referrer"></p> 
      <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-11ad4c9c709263dc394e4df4babd92d0e60.png" referrerpolicy="no-referrer"></p> 
      <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-466fd07804d20885f0795f3cde175eee5c3.JPEG" referrerpolicy="no-referrer"></p> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            