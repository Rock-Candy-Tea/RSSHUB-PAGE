
---
title: '分布式监控平台 WGCLOUD 新增支持监测 RISC-V 和 s390x'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-503ea5277221517b61a7830922c3d08ce50.jpg'
author: 开源中国
comments: false
date: Tue, 30 Aug 2022 10:39:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-503ea5277221517b61a7830922c3d08ce50.jpg'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">WGCLOUD</a><span> </span>是一款集成度较高的分布式运维监控系统，具有集群监控，易部署、易上手使用、轻量、高效、自动化等特点，server 端基于<span style="background-color:#ffffff; color:#333333"><span> </span>springboot 开发，agent 端使用 go 编写。核心模块包括：<strong>主机系统信息监控，CPU 监控，CPU 温度监控，内存监控，网络流量监控，磁盘 IO 监控，磁盘空间监测，系统负载监控，硬盘 smart 健康检测，应用进程监控，端口监控，docker 监控，日志文件监控，文件防篡改保护，数据可视化监控，自动生成拓扑图、大屏可视化，数通设备监测，服务接口监测，web ssh 堡垒机，指令下发，告警信息（邮件、钉钉、微信等）推送</strong>。</span> </p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">码云仓库：</span><a href="https://gitee.com/wanghouhou/wgcloud">https://gitee.com/wanghouhou/wgcloud</a></p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">GITHUB 仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftianshiyeben%2Fwgcloud" target="_blank">https://github.com/tianshiyeben/wgcloud</a></p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">http://www.wgstart.com</a></p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>WGCLOUD 支持监测的操作系统平台</strong></p> 
   <blockquote>
    支持监测 Linux 系列：Debian、RedHat、CentOS、ubuntu、麒麟、统信、龙芯、树莓派、凝思等
    <br> 支持监测 windows 系列：Windows Server 2008 R2，2012，2016，2019，Windows 7，Windows 8，Windows 10
    <br> 支持监测 unix 系列：solaris，FreeBSD，OpenBSD
    <br> 支持监测 macOS 系列：macOS amd64，macOS arm64
   </blockquote> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#212529">WGCLOUD-v3.4.0 更新说明，2022-08-18 发布</strong></p> 
   <blockquote> 
    <p style="margin-left:0; margin-right:0">1. 新增，支持 oracle 数据源</p> 
    <p style="margin-left:0; margin-right:0">2. 新增，进程监控列表，新增采集进程的启动时间指标</p> 
    <p style="margin-left:0; margin-right:0">3. 改造，图表趋势图时间段查询，改造为最近 1 小时，最近 2 小时，最近 6 小时，最近 12 小时，最近 24 小时，自定义选择时间段查询选项</p> 
    <p style="margin-left:0; margin-right:0">4. 改造，统计分析菜单，改造为统计报表，内容为所有主机最近 24 小时，最近一周，最近 15 天，最近 30 天的 cpu、内存、告警、负载、上下行传输速率、连接数量等分析报表，并支持导出 Excel</p> 
    <p style="margin-left:0; margin-right:0">5. 改造，系统日志菜单，列表增加字段日志类型：业务告警，系统操作，告警恢复</p> 
    <p style="margin-left:0; margin-right:0">6. 改造，菜单用户账号管理，名称改为成员账号，其功能没有任何变化，只是为了避免混淆叫法，修改了菜单名称</p> 
    <p style="margin-left:0; margin-right:0">7. 改造，完善和重构系统操作审计日志，对用户所有操作的记录进行日志记录</p> 
    <p style="margin-left:0; margin-right:0">8. 改造，服务接口监测，POST 接口，可支持设置多个 header</p> 
    <p style="margin-left:0; margin-right:0">9. 新增，主机列表，鼠标移到系统 logo 上面时候，增加显示主机名称和系统运行时间</p> 
    <p style="margin-left:0; margin-right:0">10. 新增，系统日志数据开放接口，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.wgstart.com%2Fhelp%2Fdocs9_16.html" target="_blank">查看使用说明</a></p> 
    <p style="margin-left:0; margin-right:0">11. 新增，文件防篡改列表，增加显示文件最后修改时间</p> 
    <p style="margin-left:0; margin-right:0">12. 优化，端口监控，Telnet IP 长度改为 300，这样就可以支持很长的 IP 或域名</p> 
    <p style="margin-left:0; margin-right:0">13. 新增，页面告警声音提示（默认关闭，开启点击页面右上角喇叭即可），有新告警消息时候，会提示嘟的一声</p> 
    <p style="margin-left:0; margin-right:0">14. 新增，账号登录连续输入密码错误次数超过 5 次，则禁止该账号 10 分钟内不能再次登录系统，10 分钟后恢复登录</p> 
    <p style="margin-left:0; margin-right:0">15. 新增，下发指令，取消了【重复下发】，定时下发改造为可选择任意时间下发，不再局限于今天、明天下发</p> 
    <p style="margin-left:0; margin-right:0">16. 新增，下发指令，增加发送通知开关，默认开启，若不需要通知，可在 server/config/application.yml，修改配置项 shellWarnMail 为 no</p> 
    <p style="margin-left:0; margin-right:0">17.bug，统一升级依赖的 jquery 库包至最新 v3.6.0，修复 jquery xss 漏洞</p> 
    <p style="margin-left:0; margin-right:0">18. 两个大屏显示优化和改造</p> 
    <p style="margin-left:0; margin-right:0">19. 一些已知的 bug 修复，代码结构重构优化，提升系统运行性能，更加安全和稳定</p> 
   </blockquote> 
   <p style="margin-left:0; margin-right:0"><img alt height="1454" src="https://oscimg.oschina.net/oscnet/up-503ea5277221517b61a7830922c3d08ce50.jpg" width="1364" referrerpolicy="no-referrer"><img alt height="1024" src="https://oscimg.oschina.net/oscnet/up-5d05b799c457a2c5b248098be5306e334ab.jpg" width="1364" referrerpolicy="no-referrer"><img alt height="3004" src="https://oscimg.oschina.net/oscnet/up-68ed16f42997041425c06b84c463b030019.jpg" width="1339" referrerpolicy="no-referrer"><img alt height="768" src="https://oscimg.oschina.net/oscnet/up-cf627a1aaf3092c04e47371c4013e12543e.jpg" width="1366" referrerpolicy="no-referrer"><img alt height="1800" src="https://oscimg.oschina.net/oscnet/up-4709e12b84adc3b38bd0e21771828a9c7e9.jpg" width="1344" referrerpolicy="no-referrer"> </p> 
   <p style="margin-left:0; margin-right:0"><img alt height="750" src="https://oscimg.oschina.net/oscnet/up-b8bab57b79819b751b2da9935699c45c7ea.jpg" width="1345" referrerpolicy="no-referrer"></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            