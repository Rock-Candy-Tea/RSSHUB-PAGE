
---
title: '分布式监控系统 WGCLOUD v3.3.3 发布，新增支持数通设备监测'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c4b685cc09b32cb0605be6b911d1ce01f31.JPEG'
author: 开源中国
comments: false
date: Tue, 01 Jun 2021 05:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c4b685cc09b32cb0605be6b911d1ce01f31.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">WGCLOUD</a>，server端基于<span style="background-color:#ffffff; color:#333333">springboot开发，agent端使用go编写。支持高并发高性能，核心模块包括：<strong>主机监控，ES集群管理，CPU监控，CPU温度监控，内存监控，数据监控，docker监控，网络流量监控，服务接口心跳检测，应用进程管理，磁盘IO监控，系统负载监控，端口监控，大屏可视化，日志文件监控，硬盘smart健康检测，web版ssh工具，堡垒机，监控告警信息（默认邮件，支持钉钉微信集成）推送</strong>。</span> </p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">码云源码下载：</span><a href="https://gitee.com/wanghouhou/wgcloud">https://gitee.com/wanghouhou/wgcloud</a></p> 
<p style="text-align:left">GITHUB源码下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftianshiyeben%2Fwgcloud" target="_blank">https://github.com/tianshiyeben/wgcloud</a></p> 
<p style="text-align:left">安装包下载：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">http://www.wgstart.com</a></p> 
<p style="text-align:left"><strong>WGCLOUD-v3.3.3更新说明，2021-06-02：</strong></p> 
<blockquote> 
 <div style="text-align:left"> 
  <p>1.新增，数通设备监测（如路由器、交换机、打印机等）</p> 
  <p>2.修复，修复虚拟机下linux系统cpu逻辑核数统计不准确问题</p> 
  <p>3.优化，分页显示组件</p> 
  <p>4.优化，数据统计模块sql关键字过滤机制优化，如DELETED等关键字误报情况修复</p> 
  <p>5.优化，web ssh中文乱码bug修复</p> 
  <p>6.优化，规范数据开放接口返回报文结构，在原来返回报文外包了一层&#123;"msg":"错误信息","code":"状态码","data":&#123;原来数据&#125;&#125;，data即是原来返回报文不变</p> 
  <p>7.性能调优，所有主键改造为雪花算法生成自增主键，大幅提升server和数据库吞吐量。原表结构不用修改</p> 
  <p>8.新增，每个主机支持自定义告警开关及告警值</p> 
  <p>9.大屏上下行带宽bug修复</p> 
  <p>10.其他bug修复</p> 
  <p> </p> 
 </div> 
</blockquote> 
<p><img alt height="1454" src="https://oscimg.oschina.net/oscnet/up-c4b685cc09b32cb0605be6b911d1ce01f31.JPEG" width="1364" referrerpolicy="no-referrer"><img alt height="1024" src="https://oscimg.oschina.net/oscnet/up-4d14d70d1b62503285e200654c67720848a.JPEG" width="1364" referrerpolicy="no-referrer"><img alt height="2438" src="https://oscimg.oschina.net/oscnet/up-e611329184fc057ede9ae043d9d186047ef.JPEG" width="1364" referrerpolicy="no-referrer"> </p> 
<p><img alt height="554" src="https://oscimg.oschina.net/oscnet/up-170cada0af18c9c04ba42a0842a1dcb1f8a.png" width="1336" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            