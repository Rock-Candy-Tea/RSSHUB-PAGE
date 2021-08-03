
---
title: 'GoEdge v0.2.6 发布，支持多集群共享节点、优化源站调度算法'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2539d845aa107a739e64c6c17f3cace712d.png'
author: 开源中国
comments: false
date: Tue, 03 Aug 2021 01:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2539d845aa107a739e64c6c17f3cace712d.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-2539d845aa107a739e64c6c17f3cace712d.png" width="600" referrerpolicy="no-referrer"><br> <br> <strong>GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以快速构建 CDN & WAF 平台的工具。</span><br> <br> v0.2.6版本主要支持多集群共享节点、优化源站调度算法、修复Bug。</p> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li><strong>实现多集群共享节点</strong></li> 
 <li>自动跳转到HTTPS可以设置允许和排除的域名</li> 
 <li>修复服务设置 – HTTP/HTTPS页面可能为空的Bug</li> 
 <li>网站服务显示服务错误的时候增加节点信息和链接</li> 
 <li>图表中攻击流量类型改为Line Area</li> 
 <li>指标图表可以设置忽略空值和其他对象值</li> 
 <li>各个线图改成圆滑曲线</li> 
 <li>URL跳转模式默认改成匹配前缀</li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li>增加内置统计指标：请求来源统计</li> 
 <li>修复指标数据可能重复的问题</li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li><strong>优化源站调度算法，可根据源站可用性动态调整</strong></li> 
 <li>修复IPv6访问可能导致进程异常退出的Bug</li> 
 <li>增加referer.host请求变量</li> 
 <li>WAF get302和post307只有在HTTP/1的情况下才在跳转前关闭连接</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">Demo演示：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.goedge.cn" target="_blank">http://demo.goedge.cn</a><br> <span style="background-color:#ffffff; color:#333333">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#333333">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            