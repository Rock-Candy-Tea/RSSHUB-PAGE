
---
title: 'GoEdge CDN v0.4.5 发布，大幅提升性能、区间缓存、OCSP Stapling'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f9bbb1e140d178f1657a70aab50cdb456b5.png'
author: 开源中国
comments: false
date: Mon, 21 Mar 2022 08:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f9bbb1e140d178f1657a70aab50cdb456b5.png'
---

<div>   
<div class="content">
                                                                                            <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以帮你快速构建 CDN & WAF 平台的工具，支持HTTP、HTTPS、TCP、TLS、UDP、PROXY Protocol、IPv6、WAF等特性。</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-f9bbb1e140d178f1657a70aab50cdb456b5.png" width="600" referrerpolicy="no-referrer"></span></p> 
<p style="color:#24292f; text-align:start">v0.4.5 大幅度提升性能、支持区间内容缓存、实现OCSP Stapling。</p> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li>功能增强： 
  <ul> 
   <li>HTTPS/TLS 
    <ul> 
     <li><strong>支持OCSP Stapling功能，可以在HTTPS设置中开启</strong></li> 
    </ul> </li> 
   <li>访问日志 
    <ul> 
     <li><strong>增加对访问日志自动分表配置</strong>，以提升查询速度</li> 
     <li>支持使用小时筛选访问日志</li> 
     <li>访问日志慢的时候增加指定域名查询建议</li> 
    </ul> </li> 
   <li>缓存 
    <ul> 
     <li><strong>实现基础的区间内容缓存配置（试验功能）</strong></li> 
     <li>增加是否同步写入压缩缓存设置，可以设置是否在写入原始内容的同时写入压缩内容</li> 
     <li>单个网站服务缓存可以设置是否使用系统默认设置</li> 
     <li>缓存策略列表可以使用存储类型筛选</li> 
     <li>创建文件类型的缓存策略默认分配1G内存</li> 
     <li>节点可以单独设置缓存目录</li> 
    </ul> </li> 
   <li>反向代理 
    <ul> 
     <li><strong>实现回源跟随功能，可以在源站信息中设置</strong></li> 
     <li>源站支持单独自定义回源主机名</li> 
    </ul> </li> 
   <li>WAF 
    <ul> 
     <li>IPSet支持IPv6黑/白名单</li> 
    </ul> </li> 
   <li>界面 
    <ul> 
     <li>可以在集群列表中置顶集群</li> 
     <li>可以在管理界面设置里设置默认每页显示数</li> 
    </ul> </li> 
   <li>其他 
    <ul> 
     <li>使用edge-boot安装后EdgeAdmin自动注册systemd服务</li> 
    </ul> </li> 
  </ul> </li> 
 <li>Bug修复： 
  <ul> 
   <li>修复选择集群弹窗页面可能只显示前6个集群的Bug</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li>功能增强： 
  <ul> 
   <li>域名操作错误时显示具体的域名、记录信息等</li> 
   <li>HTTP DNS QueryRecord动作支持返回null</li> 
   <li>GRPC通讯启用gzip压缩，减少带宽使用</li> 
  </ul> </li> 
 <li>Bug修复： 
  <ul> 
   <li>修复审计日志无法自动清理的Bug</li> 
   <li><strong>修复节点/服务配置无法更新的Bug</strong></li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li>功能增强： 
  <ul> 
   <li><strong>大幅提升缓存、压缩相关性能</strong>，在不修改任何配置的情况下，综合性能至少提升一倍</li> 
   <li>实现基础的206 partial content缓存，即可以缓存<code>Range</code>查询的内容</li> 
   <li>支持分片内容直接写入内存缓存</li> 
   <li>缓存策略变更时减少重启缓存服务几率</li> 
  </ul> </li> 
 <li>Bug修复： 
  <ul> 
   <li>修复添加到白名单动作可能不起作用的Bug</li> 
  </ul> </li> 
</ul> 
<p style="color:#24292f; text-align:start">下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> 文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            