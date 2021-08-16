
---
title: 'CDN 搭建工具 GoEdge v0.2.9 发布，改进细节、修改 Bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-24eb0ac7507e9b4d4d67800ea614c6668d9.png'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 09:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-24eb0ac7507e9b4d4d67800ea614c6668d9.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start"><strong>GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以帮你快速构建 CDN & WAF 平台的工具，支持HTTP、HTTPS、TCP、TLS、UDP、IPv6、WAF等特性。</span></p> 
<p style="text-align:start"><span style="background-color:#ffffff; color:#333333"><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-24eb0ac7507e9b4d4d67800ea614c6668d9.png" width="600" referrerpolicy="no-referrer"></span></p> 
<p style="text-align:start">此版本主要改进细节、修复Bug。</p> 
<blockquote> 
 <p>注意：这个版本可能会重新记录一些统计数据。</p> 
</blockquote> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li>优化节点创建和安装流程</li> 
 <li>修复节点无法修改线路的Bug</li> 
 <li>优化代码/支持IP名单的更多格式的导入、导出</li> 
 <li>访问日志搜索增加域名和IP搜索</li> 
 <li>访问日志显示节点信息</li> 
 <li>增加全局服务访问日志</li> 
 <li>安全设置中增加允许记住登录选项</li> 
 <li>安全设置检查IP时同时也检查直接连接管理平台的上游IP</li> 
 <li>修复在MySQL8下安装提示无法创建edgeTest的问题</li> 
 <li>提升节点配置同步速度（从60秒提升到10秒以内）</li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li>修复多个表unique key无法升级到问题</li> 
 <li>修复WAF检查IP状态可能会出现panic错误的Bug</li> 
 <li>边缘节点没有集群的时候视为删除</li> 
 <li>运行日志只显示已经设置集群的节点<br> <br> <span style="background-color:#ffffff; color:#24292e">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292e">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></li> 
</ul>
                                        </div>
                                      
</div>
            