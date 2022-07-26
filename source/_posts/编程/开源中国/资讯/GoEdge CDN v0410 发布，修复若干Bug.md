
---
title: 'GoEdge CDN v0.4.10 发布，修复若干Bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f5827478a5f7a7e7407b0f0e223e995e114.png'
author: 开源中国
comments: false
date: Tue, 26 Jul 2022 08:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f5827478a5f7a7e7407b0f0e223e995e114.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333"><span> </span>是一款可以帮你快速构建 CDN & WAF 平台的工具，支持 HTTP、HTTPS、Websocket、TCP、TLS、UDP、PROXY Protocol、IPv6、WAF 等特性，支持多个第三方 DNS 服务。</span></p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start">v0.4.10 修复若干Bug。</p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start"><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-f5827478a5f7a7e7407b0f0e223e995e114.png" width="600" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">管理平台</h3> 
<h4 style="text-align:start">功能增强</h4> 
<ul> 
 <li>边缘节点详情中包含主程序位置，方便用户查找命令位置</li> 
 <li>API节点详情中增加主程序位置信息，方便用户查找命令位置</li> 
 <li>增加本地API节点需要升级提示，Dashboard中提供手动重启按钮</li> 
 <li>网站服务列表增加用户筛选</li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<h4 style="text-align:start">功能增强</h4> 
<ul> 
 <li>用户设置为未启用时，自动停用服务</li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<h4 style="text-align:start">功能增强</h4> 
<ul> 
 <li>优化Firewalld添加端口方法，自动聚合连续的端口号，比如<span> </span><code>8001</code>、<code>8002</code>、<code>8003</code><span> </span>会自动聚合为<span> </span><code>8001-8003/tcp</code></li> 
 <li>地区封禁也可以使用自定义的403页面</li> 
 <li>API RPC配置增加disableUpdate，可以停用自动更新API节点</li> 
 <li>WAF多个相同Key的cc2统计规则不再重复累加；以往多个规则中出现相同的cc2规则时，会出现单次请求多次累加计算的情况，在当前版本中，每个规则只会计算一次</li> 
 <li>关闭、重启进程时自动关闭IP名单本地缓存数据库，防止相关wal文件尺寸一直增长</li> 
</ul> 
<h4 style="text-align:start">Bug修复</h4> 
<ul> 
 <li>修复在Firewalld添加非常多端口（比如100个以上）而导致端口无法监听的Bug</li> 
 <li>修复连接数限制计算错误；0.4.9版本中如果开启了请求限制，会导致已记录的连接数无法减少，即使连接已经关闭，直至耗尽出现429提示</li> 
</ul> 
<h3 style="text-align:start">EdgeBoot</h3> 
<ul> 
 <li>现在可以从正在运行的进程中查找主程序路径，不需要组件安装在固定位置</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            