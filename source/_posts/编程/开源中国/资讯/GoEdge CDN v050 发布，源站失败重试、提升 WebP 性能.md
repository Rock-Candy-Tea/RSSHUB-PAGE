
---
title: 'GoEdge CDN v0.5.0 发布，源站失败重试、提升 WebP 性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-048dd84a0f53f6135311e7aa15160df054b.png'
author: 开源中国
comments: false
date: Mon, 15 Aug 2022 11:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-048dd84a0f53f6135311e7aa15160df054b.png'
---

<div>   
<div class="content">
                                                                                            <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333"><span> </span>是一款可以帮你快速构建 CDN & WAF 平台的工具，支持 HTTP、HTTPS、Websocket、TCP、TLS、UDP、PROXY Protocol、IPv6、WAF 等特性，支持多个第三方 DNS 服务。</span><br> <img alt height="352" src="https://oscimg.oschina.net/oscnet/up-048dd84a0f53f6135311e7aa15160df054b.png" width="600" referrerpolicy="no-referrer"><br> <br> <span style="background-color:#ffffff; color:#171717">GoEdge v0.5.0 主要改进源站失败自动重试、提升WebP性能等。</span></p> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li><strong>路由规则也支持请求限制设置</strong></li> 
 <li>TCP源站也支持专属域名设置项，可以依靠TLS域名决定使用哪个源站</li> 
 <li><strong>缓存条件增加If-None-Match和If-Modified-Since是否回源选项</strong>，默认不回源，避免因为这两项Header回源导致源站返回304而导致一直无法缓存的问题。</li> 
 <li>添加域名时自动将域名转换为小写，避免因为域名大小写引发问题</li> 
 <li>优化“IP名单”菜单和“运行日志”菜单数字获取方式，改成异步加载，避免因为数据量大而导致页面加载过慢</li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li>远程升级节点时，如果老的文件不存在，则直接创建，不再提示错误</li> 
 <li>删除集群的时候同时删除相关节点运行日志，避免集群删除了而统计数字还在的问题</li> 
 <li>服务带宽峰值统计API增加按月、按日查询接口</li> 
 <li>只有发送过离线通知的节点才会发送恢复在线通知，避免因为网络问题一直提示节点恢复在线的问题</li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li><strong>40x, 50x提示默认使用HTML</strong>；50x提示增加原因信息（仅包含简要信息，详细信息仍然需要查看访问日志）；并能自动切换中英文</li> 
 <li><strong>升级WebP库版本</strong>，性能和压缩效率有所提升</li> 
 <li><strong>第一次连接源站失败后，自动尝试下一个源站</strong>；如果主源站没有可用源站，则自动尝试备用源站；如果没有下一个源站，则连续尝试当前源站</li> 
 <li>TLS支持默认SNI回源：如果服务和源站都是TLS服务，那么就可以将TLS服务的域名传递到源站</li> 
 <li>edge-node pprof命令增加–addr参数，用来指定pprof信息获取地址</li> 
 <li>小幅度减少守护进程使用的内存</li> 
 <li><strong>UDP服务也记录带宽峰值</strong></li> 
 <li>修复节点自动升级时无法自动启动的Bug：以往版本中自动升级节点时需要启动两次，而且会产生.old和.dist文件进程，新版本修复了这个问题，但是需要在下次版本升级时才生效</li> 
 <li>优化忽略客户端关闭连接错误条件：对于若干个客户端关闭连接导致的网络错误不再提示</li> 
 <li>执行IP名单更新任务时防止阻塞</li> 
 <li>nftables封禁IP时默认使用异步操作，防止阻塞新连接</li> 
</ul> 
<h3 style="text-align:start">文档</h3> 
<p style="color:#171717; margin-left:0; margin-right:0; text-align:start">API文档增加角色标签，增加REST地址。</p> 
<p><span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            