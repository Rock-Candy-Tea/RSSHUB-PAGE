
---
title: '分布式监控系统 WGCLOUD v3.3.1 发布，新增硬盘 smart 健康检测'
categories: 
 - 编程
 - 开源中国
 - — 资讯
headimg: 'https://static.oschina.net/uploads/img/202011/24100716_tEAP.jpg'
author: 开源中国
comments: false
date: Tue, 23 Mar 2021 13:54:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202011/24100716_tEAP.jpg'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <div style="text-align:left"> 
  <div style="text-align:start"> 
   <div style="text-align:left"> 
    <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">WGCLOUD</a>，server端基于<span style="background-color:#ffffff; color:#333333">springboot开发，agent端使用go编写。支持高并发高性能，核心模块包括：<strong>主机监控，ES集群管理，CPU监控，CPU温度监控，内存监控，数据监控，docker监控，网络流量监控，服务接口心跳检测，应用进程管理，磁盘IO监控，系统负载监控，端口监控，大屏可视化，日志文件监控，硬盘smart健康检测，监控告警信息（默认邮件，支持钉钉微信集成）推送</strong>。</span> </p> 
    <p style="text-align:left">另外我们计划在下个版本集成堡垒机能力，目前处于计划调研中。</p> 
    <p style="text-align:left"><strong>WGCLOUD-v3.3.1更新说明，2021-03-23：</strong></p> 
    <div style="text-align:left"> 
     <blockquote> 
      <div style="text-align:left"> 
       <div style="text-align:left"> 
        <div style="text-align:left"> 
         <p>1.新增，硬盘smart健康检测能力，需要在监控主机安装smartmontools工具</p> 
         <p>2.新增，可配置不需要告警的主机集合，在/server/config/application.yml配置选项blockIps</p> 
         <p>3.新增，改造【主机列表】，增加接收、发送KB/秒指标、主机画像</p> 
         <p>4.新增，端口监控机制优化，有些主机localhost未开启，所以增加配置选项，使用telnet ip 端口或telnet localhost 端口检测</p> 
         <p>5.新增，主机下线判定原来10分钟，提升为5分钟，更加灵敏，因此agent上报时间间隔不能超过5分钟</p> 
         <p>6.优化，删除菜单【主机画像】，将其合并到【主机列表】</p> 
         <p>7.优化，【监控主面板】，当没有数据表时候不显示数据监控图表</p> 
         <p>8.优化，磁盘空间、磁盘IO指标改为每30分钟上报一次，提升性能，因为此指标变动较缓慢，没必要实时上报</p> 
         <p>9.bug，修复主机列表磁盘空间百分比小数点后数字过长的问题</p> 
         <p>10.bug，修复服务接口监测不支持https问题，新增根据响应内容中的标识来判断接口是否正常，并行运算，优化性能</p> 
         <p>11.bug，大屏bug修复，新增吞吐量指标，请升级</p> 
         <p>12.bug，修复agent和数据开放接口根据ip获取监控进程、监控端口、监控docker、监控日志的模糊匹配ip问题，已改为完全匹配ip查询模式</p> 
         <p>13.bug，修复多个agent的bindIp相同时，同时上报，【主机列表】数据重复显示问题</p> 
         <p>14.底层架构重构、性能优化、UI整体优化</p> 
        </div> 
       </div> 
      </div> 
     </blockquote> 
    </div> 
    <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">码云源码下载：</span><a href="https://gitee.com/wanghouhou/wgcloud">https://gitee.com/wanghouhou/wgcloud</a></p> 
    <p style="text-align:left">GITHUB源码下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftianshiyeben%2Fwgcloud" target="_blank">https://github.com/tianshiyeben/wgcloud</a></p> 
    <p style="text-align:left">安装包下载：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.wgstart.com" target="_blank">http://www.wgstart.com</a></p> 
    <p style="text-align:left"><img alt="WGCLOUD安装手册" height="693" src="https://static.oschina.net/uploads/img/202011/24100716_tEAP.jpg" width="700" referrerpolicy="no-referrer"></p> 
    <p style="text-align:left"><img alt="up-682986605e1c2d01829a3ba795f21e0ec14.JPEG" src="https://oscimg.oschina.net/oscnet/up-682986605e1c2d01829a3ba795f21e0ec14.JPEG" referrerpolicy="no-referrer"></p> 
    <p style="text-align:left"><img alt="up-a23a1e36ca9604401a9fbe4baabf4a0f210.png" src="https://oscimg.oschina.net/oscnet/up-a23a1e36ca9604401a9fbe4baabf4a0f210.png" referrerpolicy="no-referrer"></p> 
    <p style="text-align:left"><img src="https://www.wgstart.com/wgcloud/images/daping.jpg" referrerpolicy="no-referrer"></p> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            