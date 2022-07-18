
---
title: 'GoEdge CDN v0.4.9 发布，zstd压缩、端口跟随、SNI回源等'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b547f2de90cc8e6fac82df7499d05598fe4.png'
author: 开源中国
comments: false
date: Mon, 18 Jul 2022 09:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b547f2de90cc8e6fac82df7499d05598fe4.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333"><span> </span>是一款可以帮你快速构建 CDN & WAF 平台的工具，支持 HTTP、HTTPS、Websocket、TCP、TLS、UDP、PROXY Protocol、IPv6、WAF 等特性，支持多个第三方 DNS 服务。</span></p> 
<p><span style="background-color:#ffffff; color:rgba(0, 0, 0, 0.87)">v0.4.9 增加zstd压缩、端口跟随、TLS回源主机名等。<br> <br> <img alt height="352" src="https://oscimg.oschina.net/oscnet/up-b547f2de90cc8e6fac82df7499d05598fe4.png" width="600" referrerpolicy="no-referrer"></span><br>  </p> 
<h3 style="text-align:start">管理平台</h3> 
<h4 style="text-align:start">功能增强</h4> 
<ul> 
 <li>反向代理 
  <ul> 
   <li>TLS源站支持填写回源主机名。通过域名连接TLS服务，如果源站也是TLS协议的，那么可以在源站读取到域名信息</li> 
   <li>实现源站端口跟随功能。在源站设置中开启端口跟随，可以在用户访问某个端口时自动设置源站为对应端口</li> 
   <li>反向代理设置中增加移除回源主机名端口功能</li> 
  </ul> </li> 
 <li>压缩 
  <ul> 
   <li>支持zstd压缩。通过在Accept-Encoding中添加zstd，可以输出zstd格式的内容；也支持源站zstd格式的转换</li> 
  </ul> </li> 
 <li>访问日志 
  <ul> 
   <li>日志详情中增加源站信息。可以在日志详情中查看源站的地址（主机名和端口）。</li> 
  </ul> </li> 
 <li>WAF 
  <ul> 
   <li>WAF cc2规则中增加忽略常见文件扩展名选项</li> 
   <li>WAF策略增加记录请求Body选项。启用后，可以在访问日志详情”请求数据”中查看请求Body（最大不超过2MB），方便检查WAF匹配的内容。</li> 
   <li>WAF策略增加记录区域封禁日志选项。启用后，可以在访问日志中查看区域封禁的访问，包括地区封禁和省份封禁。</li> 
  </ul> </li> 
 <li>DNS 
  <ul> 
   <li>集群DNS设置增加允许通过CNAME访问网站服务选项</li> 
   <li>集群DNS设置可以设置不使用主域名</li> 
  </ul> </li> 
 <li>界面 
  <ul> 
   <li>修复弹窗中没有正确设置favicon的Bug</li> 
   <li>优化集群设置菜单，功能分区更加清晰</li> 
  </ul> </li> 
 <li>安全 
  <ul> 
   <li>在robots.txt中移除GoEdge标识，防止针对性扫描</li> 
   <li>安全设置中增加禁止搜索引擎、禁止爬虫、允许访问的域名等选项，提升管理系统安全性</li> 
  </ul> </li> 
</ul> 
<h4 style="text-align:start">Bug修复</h4> 
<ul> 
 <li>修复因为无法传递域名而导致无法HTTPS源站WebSocket的Bug</li> 
 <li>修复全局封锁名单不能创建IP的Bug</li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<h4 style="text-align:start">功能增强</h4> 
<ul> 
 <li>删除某个IP时更新IP版本，防止在某些情况下删除IP时不会同步到边缘节点</li> 
 <li>限制节点自动升级时的速度和并发数，防止同时升级时对API节点带来的带宽压力</li> 
 <li>删除节点时同时删除对应的运行日志</li> 
 <li>编译时去除amd64和arm64之外的边缘节点安装包文件；减小安装包尺寸</li> 
</ul> 
<h4 style="text-align:start">Bug修复</h4> 
<ul> 
 <li>修复删除用不过期IP时节点不同步的Bug</li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<h4 style="text-align:start">功能增强</h4> 
<ul> 
 <li>反向代理 
  <ul> 
   <li>访问TLS/HTTPS源站时自动携带ServerName信息（SNI）</li> 
   <li>限制源站错误检测最大并发数，防止源站数量较多时带来的资源利用压力过大</li> 
  </ul> </li> 
 <li>缓存 
  <ul> 
   <li>改进写缓存并发限制算法，提升写入缓存效率</li> 
   <li>缓存条件中启用客户端过期时间（Expires）后，自动删除源站的Cache-Control Header</li> 
  </ul> </li> 
 <li>其他 
  <ul> 
   <li>升级时备份可执行文件时将.old改成.dist，避免误解。以往版本中备份文件可能是edge-node.old，新版本中改成了edge-node.dist，避免因为进程名称而带来的恐慌</li> 
   <li>找不到匹配的域名时自动记录日志。以往版本如果找不到匹配的域名不会有任何提示，有可能会被攻击而无法察觉，新版本中增加了访问日志，管理员可以在管理系统中查看未绑定的域名访问情况，从而可以有针对性的操作</li> 
   <li>找不到匹配的域名时自动启用防CC攻击，提升系统安全性</li> 
  </ul> </li> 
</ul> 
<h4 style="text-align:start">Bug修复</h4> 
<ul> 
 <li>修复DDoS防护规则可能无法生成的Bug。以往版本中可能需要重启节点才可以使DDoS防护规则生效，而且可能在更新配置时删除已生成的nft规则，新版本中修复了这些问题</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            