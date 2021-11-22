
---
title: 'GoEdge CDN v0.3.5 发布，实现缓存 LFU 算法、优化 IP 名单、增加迁移功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1500851a0ae913dbbf8ff8796d555d62328.png'
author: 开源中国
comments: false
date: Mon, 22 Nov 2021 09:17:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1500851a0ae913dbbf8ff8796d555d62328.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以帮你快速构建 CDN & WAF 平台的工具，支持HTTP、HTTPS、TCP、TLS、UDP、IPv6、WAF等特性。</span></p> 
<p><br> <img alt height="352" src="https://oscimg.oschina.net/oscnet/up-1500851a0ae913dbbf8ff8796d555d62328.png" width="600" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:rgba(0, 0, 0, 0.87)">v0.3.5 实现缓存LFU算法、优化IP名单、增加迁移功能，整体上：</span><br> 更快：轻松支持上百万域名、写缓存使用内存Buffer+定期Flush到磁盘<br> 更省：节点配置支持压缩传输，节省80%以上的带宽；节点配置生成速度更快<br> 更轻松：提供一个迁移引导程序，让迁移更多轻松，更少焦虑</p> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li>功能 
  <ul> 
   <li>公用IP名单可以选择是否为全局，如果是全局，则自动应用于所有服务<br> <img alt height="181" src="https://oscimg.oschina.net/oscnet/up-431a217e85b0589c2dad75774e224384e54.png" width="400" referrerpolicy="no-referrer"></li> 
   <li>增加查看、检索所有IP名单功能<br> <img alt height="233" src="https://oscimg.oschina.net/oscnet/up-0f70e4f7ebaa8247c757c9c8d5aa5794193.png" width="600" referrerpolicy="no-referrer"></li> 
   <li>IP名单中的IP增加添加日期、服务、WAF策略、规则集等信息 </li> 
   <li>支持批量删除IP名单中的IP<br> <img alt height="262" src="https://oscimg.oschina.net/oscnet/up-5d34f74b38f1b00de16f4ae5d525207d291.png" width="418" referrerpolicy="no-referrer"></li> 
   <li>实现迁移辅助功能（系统设置 – 高级设置 – 迁移）<br> <img alt height="150" src="https://oscimg.oschina.net/oscnet/up-d362fa59a94317bcf47122585620b2f6cf9.png" width="532" referrerpolicy="no-referrer"></li> 
   <li>当迁移了管理平台后，自动跳转到确认API节点地址确认页<br> <img alt height="246" src="https://oscimg.oschina.net/oscnet/up-0bfcacb2e440babce88aaebab66f19e2c93.png" width="550" referrerpolicy="no-referrer"></li> 
   <li>SSH登录支持Passphrase<br> <img alt height="188" src="https://oscimg.oschina.net/oscnet/up-0f2f8d84c2c9673b6394435629138210fdd.png" width="600" referrerpolicy="no-referrer"></li> 
   <li>域名解析中可以删除和恢复某个域名<br> <img alt height="212" src="https://oscimg.oschina.net/oscnet/up-f5276e067745c712c4611ee022dd3cf7321.png" width="600" referrerpolicy="no-referrer"></li> 
   <li>只有一个可用的API节点时不允许删除，防止误删而导致的系统错误<br> <img alt height="333" src="https://oscimg.oschina.net/oscnet/up-68a7b239c238c78b625c1f289bb903be9d7.png" width="559" referrerpolicy="no-referrer"></li> 
   <li>当证书被API节点或者用户节点使用时不允许删除，试图删除时将给予提示</li> 
   <li>安装时自动检查并填入服务器上安装的MySQL<br> <img alt height="150" src="https://oscimg.oschina.net/oscnet/up-fc8aad0db5473c6a58a61dfc9191a4f0a25.png" width="532" referrerpolicy="no-referrer"></li> 
   <li>编译时删除.js.map文件</li> 
  </ul> </li> 
 <li>Bug修复 
  <ul> 
   <li>修复时间输入组件时间戳总是多1秒的Bug</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li>功能 
  <ul> 
   <li>生成节点配置时进行压缩传输，至少减少80%的配置传输带宽</li> 
   <li>优化节点配置生成速度，平均节约50%的时间</li> 
   <li>SSH登录支持Passphrase</li> 
   <li>IP名单API增加IP添加时间</li> 
   <li>API取消对节点时钟的检查，意味着如果节点的时钟和API节点时钟不一致，需要自行校对</li> 
   <li>删除WAF策略和删除服务时同时也删除关联的IP名单</li> 
   <li>增加若干个API</li> 
   <li>开源版本编译时不再运行<code>sql.sh</code></li> 
   <li>节点监控数据只保留7天（先前是100天）</li> 
  </ul> </li> 
 <li>Bug修复 
  <ul> 
   <li>修复服务列表无法使用数字搜索的Bug</li> 
   <li>修复用户查询证书时返回其他证书的Bug</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li>功能 
  <ul> 
   <li>缓存策略实现LFU算法，可以根据需要及时清理冷数据</li> 
   <li>实现在硬盘+内存缓存的情况下，自动将内存缓存Flush到磁盘</li> 
   <li>X-Cache Header在有些情况下加入跳过缓存的原因</li> 
   <li>IP名单记录在本地的数据库（sqlite）中，下次启动的时候不再全部从API读取</li> 
   <li>增加IPSet中最大元素数量为1000000</li> 
   <li>在IPSet中的IP范围现在只支持D段，这是为了防止ipset很快被填满</li> 
   <li>删除IP名单中某个IP时，也会删除WAF保存在内存中的名单中的IP</li> 
   <li>IP名单中IP创建时保存相关节点、服务、WAF策略信息</li> 
   <li>接收请求时保留URL路径中多余的斜杠（/），比如新版本中<code>///hello</code>，将不会被自动跳转到<code>/hello</code></li> 
   <li>大幅提升域名匹配性能，支持上百万域名轻松匹配到对应服务</li> 
   <li>节点配置支持压缩格式</li> 
   <li>增加对任务的执行时间追踪工具，可以使用<code>bin/edge-node trackers</code>显示任务执行时间</li> 
   <li>优化运行日志上传功能，最近N条重复的不再上传</li> 
   <li>在开发环境下运行日志显示包名</li> 
   <li>实现修改API节点地址的指令，即管理员可以通过指令远程修改节点的API地址</li> 
   <li>访问日志简化requestId生成方法，从先前的70多位长度缩短到19位左右的长度</li> 
   <li>暂时不删除多余的*.cache.tmp，以防在节点启动的时候产生的性能问题</li> 
   <li>优化多个错误提示</li> 
   <li>反向代理源站错误时提示完整的URL</li> 
   <li>有些错误提示只显示一次</li> 
  </ul> </li> 
 <li>Bug修复 
  <ul> 
   <li>修复firewalld无法删除规则的Bug</li> 
   <li>修复IPTables+IPSet组合时在IPTables中生成了多个重复记录的Bug</li> 
   <li>修复RPC客户端管理没有加锁的问题</li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            