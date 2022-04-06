
---
title: '分布式监控系统代理 wgcloud-proxy-v1.0，实现数据转发上报'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-29a4db5cfebc3624c50da71068a1e6062bd.png'
author: 开源中国
comments: false
date: Wed, 06 Apr 2022 12:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-29a4db5cfebc3624c50da71068a1e6062bd.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">WGCLOUD是一款集成度较高的分布式运维监控系统，具有集群监控，部署操作方便、轻量、高效、自动化、完全私有部署等特点，server端基于<span style="background-color:#ffffff; color:#333333">springboot开发，agent端使用go编写。核心模块包括：<strong>主机系统信息监控，CPU监控，CPU温度监控，内存监控，网络流量监控，磁盘IO监控，磁盘空间监测，系统负载监控，硬盘smart健康检测，应用进程监控，端口监控，docker监控，日志文件监控，文件防篡改保护，数据可视化监控，自动生成拓扑图、大屏可视化，数通设备监测，服务接口监测，web ssh堡垒机，指令下发，告警信息（邮件、钉钉、微信等）推送</strong>。</span> </p> 
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
 <p>有一种场景，我们的server部署在公网，但我们局域网的主机都不能直连访问server，比如只有主机A可以连接访问server，那么就可以在主机A部署<strong>代理wgcloud-proxy</strong></p> 
 <p>然后内网中的主机agent都把请求数据发送到<strong>代理wgcloud-proxy</strong>，再由代理转发给server，如此就实现了agent给server上报数据</p> 
 <p><strong>1、首先下载代理wgcloud-proxy</strong></p> 
 <p>这个是一个支持http和https代理proxy，一般场景都可以使用，这个是我们自己开发的小工具。使用其他的http代理也可以的</p> 
 <p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.wgstart.com%2Fhelp%2Fdocs56.html" target="_blank">https://www.wgstart.com/help/docs56.html</a></p> 
 <p><strong>2、配置proxy，config/application.properties，把标红部分修改成自己的实际信息</strong></p> 
 <div style="text-align:left"> 
  <pre><code>#本代理程序的端口
proxyPort=8082

#wgcloud-server端访问地址，将下方替换为server主机IP和端口即可，端口一定要写，即使是80也要写哈
serverUrl=http://localhost:9999</code></pre> 
  <p><strong>3、配置内网中的agent，config/application.properties，这里把serverUrl改成代理wgcloud-proxy的url，比如我的代理在192.168.1.2上运行，配置如下</strong></p> 
  <div style="text-align:left"> 
   <pre><code>#改成代理proxy的url，将下方替换为proxy代理主机IP和端口即可，端口一定要写，即使是80也要写哈
serverUrl=http://192.168.1.2:8082</code></pre> 
   <p><strong>4、启动代理wgcloud-proxy</strong></p> 
   <p>linux通过wgcloud-proxy/start.sh启动，windows直接运行wgcloud-proxy/wgcloud-proxy-release.exe</p> 
   <p>可以仿照agent注册windows系统服务，将<strong>代理wgcloud-proxy</strong>注册为服务</p> 
   <p><strong>5、启动agent</strong></p> 
   <p>linux通过agent/start.sh启动，windows直接运行agent/wgcloud-agent-release.exe</p> 
   <p><strong style="color:#212529">6、proxy代理转发数据示意图</strong></p> 
   <p><img alt height="753" src="https://oscimg.oschina.net/oscnet/up-29a4db5cfebc3624c50da71068a1e6062bd.png" width="955" referrerpolicy="no-referrer"></p> 
   <p> </p> 
   <p>数据上报后的效果图如下：</p> 
   <p><img alt height="1389" src="https://oscimg.oschina.net/oscnet/up-4d5f63f815a78ca14e4b13d4a2739f23de4.png" width="1338" referrerpolicy="no-referrer"></p> 
   <p><img alt height="1024" src="https://oscimg.oschina.net/oscnet/up-26160616b6ed326e904327392b9122c95ce.jpg" width="1364" referrerpolicy="no-referrer"></p> 
   <p><img alt height="1615" src="https://oscimg.oschina.net/oscnet/up-0523f205af10228ad3620f1429c740f7d8a.jpg" width="1331" referrerpolicy="no-referrer"></p> 
   <p><img alt height="2438" src="https://oscimg.oschina.net/oscnet/up-dd80cea93d7225467e6f8f0cf5886170ff6.jpg" width="1364" referrerpolicy="no-referrer"></p> 
   <p><img alt height="579" src="https://oscimg.oschina.net/oscnet/up-d90c8e75ffa6cfeea227e690c951ec12ee9.jpg" width="935" referrerpolicy="no-referrer"></p> 
   <p><img alt height="768" src="https://oscimg.oschina.net/oscnet/up-a3cb1a6470121d3a58122d5633c49426e1f.png" width="1366" referrerpolicy="no-referrer"></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            