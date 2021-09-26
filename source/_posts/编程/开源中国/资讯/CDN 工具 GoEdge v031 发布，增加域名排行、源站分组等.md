
---
title: 'CDN 工具 GoEdge v0.3.1 发布，增加域名排行、源站分组等'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-831f30a90a6ba2882a7ff9b1b2c069e0993.png'
author: 开源中国
comments: false
date: Sun, 26 Sep 2021 09:20:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-831f30a90a6ba2882a7ff9b1b2c069e0993.png'
---

<div>   
<div class="content">
                                                                                            <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以帮你快速构建 CDN & WAF 平台的工具，支持HTTP、HTTPS、TCP、TLS、UDP、IPv6、WAF等特性。</span><br> <br> <img alt height="352" src="https://oscimg.oschina.net/oscnet/up-831f30a90a6ba2882a7ff9b1b2c069e0993.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start">v0.3.1版本主要增强源站按域名分组、域名排行等功能细节。</p> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">功能</p> 
  <ul> 
   <li>Dashboard增加域名排行、缓存流量趋势、攻击流量趋势</li> 
   <li>反向代理增加使用域名分组功能</li> 
   <li>在集群中可以设置自动加入DNS的CNAME记录</li> 
   <li>可以设置集群的DNS记录TTL</li> 
   <li>在域名解析–集群详情中显示正在执行的任务</li> 
   <li>可以在服务分组中设置一些全局配置选项，这些选项自动应用到其下的所有服务上</li> 
   <li>新建WAF策略时，在IP+URL请求数限制外，增加IP对象请求数限制规则集</li> 
   <li>优化节点设置交互</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">Bug修复</p> 
  <ul> 
   <li>修复当集群没有绑定DNS域名时无法修改节点DNS信息的Bug</li> 
   <li>修复日期控件初始化格式可能错误的问题</li> 
   <li>修改生成的YAML配置中可能含有tab的Bug</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li>功能 
  <ul> 
   <li>对域名统计进行分表处理，避免因数据量过大导致的查询慢的问题</li> 
   <li>通过DNS方式申请ACME证书时支持二级域名</li> 
   <li>边缘节点健康检查支持IPv6地址的节点</li> 
  </ul> </li> 
 <li>Bug修复 
  <ul> 
   <li>修复创建默认集群时没有写入API令牌的Bug</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li>功能 
  <ul> 
   <li>配置加载成功后才启动某些任务</li> 
   <li>特殊页面中支持请求变量</li> 
  </ul> </li> 
 <li>Bug修复 
  <ul> 
   <li>修复反向代理Sticky和Hash调度算法无法生效的Bug</li> 
   <li>修复当缓存内容为空时无法响应缓存的Bug</li> 
   <li>提升内存缓存的缓存数容量</li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292e">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292e">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            