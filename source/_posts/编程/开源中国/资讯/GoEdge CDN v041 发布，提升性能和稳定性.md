
---
title: 'GoEdge CDN v0.4.1 发布，提升性能和稳定性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0de8f852115f9c8f2b442836d0d866335e7.png'
author: 开源中国
comments: false
date: Mon, 21 Feb 2022 10:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0de8f852115f9c8f2b442836d0d866335e7.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start"><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以帮你快速构建 CDN & WAF 平台的工具，支持HTTP、HTTPS、TCP、TLS、UDP、PROXY Protocol、IPv6、WAF等特性。</span></p> 
<p><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-0de8f852115f9c8f2b442836d0d866335e7.png" width="600" referrerpolicy="no-referrer"><br>  </p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start">v0.4.1 主要提升系统性能和稳定性。</p> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li>功能增强： 
  <ul> 
   <li>URL跳转可以设置是否保留URL查询参数</li> 
   <li>部分地方输入域名支持连续的连字符</li> 
   <li>优化IP名单气泡数字显示</li> 
   <li>提升网站服务菜单打开速度</li> 
   <li>增加API方法调用耗时统计，可以使用<span> </span><code>api-node debug</code><span> </span>开启</li> 
   <li>优化demo模式进入命令</li> 
  </ul> </li> 
 <li>Bug修复 
  <ul> 
   <li>修复单个服务访问日志不能使用集群、节点筛选的Bug</li> 
   <li>修复版本更新检查配置不起作用的Bug</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li>功能增强： 
  <ul> 
   <li>服务配置变化时只发送单个服务配置变化通知（以前是发送所有服务配置）</li> 
   <li>自动清理N天之前过期的IP条目</li> 
   <li>优化节点离线通知</li> 
   <li>增加<span> </span><code>api-node debug</code><span> </span>命令，执行后，可以在管理平台查看API方法耗时统计</li> 
  </ul> </li> 
 <li>Bug修复 
  <ul> 
   <li>修复域名统计数据无法自动清理的Bug</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li>功能增强： 
  <ul> 
   <li>重构HTTP相关处理功能：缓存、压缩、WebP、限速，以提升稳定性</li> 
   <li>WAF规则提示错误时增加分组ID、规则集ID、规则描述</li> 
   <li>检查是否压缩的时候，如果content-type为空，则默认为text/html</li> 
   <li>读取缓存错误更详细</li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdoc" target="_blank">https://goedge.cn/doc</a></p>
                                        </div>
                                      
</div>
            