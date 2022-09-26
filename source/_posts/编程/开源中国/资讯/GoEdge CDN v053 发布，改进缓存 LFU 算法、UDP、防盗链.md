
---
title: 'GoEdge CDN v0.5.3 发布，改进缓存 LFU 算法、UDP、防盗链'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8b5a294792ebf8ae18839d75dbc7c507b50.png'
author: 开源中国
comments: false
date: Mon, 26 Sep 2022 08:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8b5a294792ebf8ae18839d75dbc7c507b50.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333"><span> </span>是一款可以帮你快速构建 CDN & WAF 平台的工具，支持 HTTP、HTTPS、Websocket、TCP、TLS、UDP、PROXY Protocol、IPv6、WAF 等特性，支持多个第三方 DNS 服务。</span></p> 
<p><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-8b5a294792ebf8ae18839d75dbc7c507b50.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; text-align:start">v0.5.3 版本主要改进缓存LFU算法、中文域名、UDP、防盗链、自动化。</p> 
<h2 style="text-align:start">EdgeAdmin</h2> 
<ul> 
 <li>细节优化 
  <ul> 
   <li>API节点在启动时页面提示“API节点正在启动，请耐心等待完成”，让用户知道正在发生什么</li> 
   <li><strong>增加edge-admin upgrade命令</strong>，用来联网升级管理系统</li> 
   <li>节点即使离线后仍然在运行状态中显示版本、主程序位置等信息</li> 
   <li><strong>集群增加是否远程启动选项</strong>，可以在集群基础设置--更多选项中设置，默认开启；开启后，当节点离线时，自动尝试通过SSH远程启动edge-node进程</li> 
   <li>在节点手动安装页显示节点安装文件下载链接</li> 
   <li><strong>增加防盗链功能</strong>，以往只能在WAF中设置，现在在服务设置中也可以直接使用</li> 
   <li>证书申请任务不再区分管理员，即一个管理员创建的证书申请任务，另外一个管理员也可以运行</li> 
   <li>BugFix: 修复读取上月带宽错误的问题</li> 
  </ul> </li> 
 <li>自动化 
  <ul> 
   <li><strong>集群增加自动同步时钟选项</strong>，可以在集群基础设置--更多选项中设置，默认开启</li> 
   <li><strong>集群增加自动安装nftables选项</strong>，可以在集群基础设置--更多选项中设置，默认不开启；这个选项也可以在创建集群时选择</li> 
   <li>修改管理界面设置中的时区时同时也会应用到API节点，即API节点的日志等相关日期格式化都会遵循管理界面的时区设置</li> 
   <li>创建节点时尝试自动从节点名称中读取IP，现在可以只填写一个名称，只要包含IP就可以直接进入下一步</li> 
  </ul> </li> 
 <li>域名 
  <ul> 
   <li><strong>域名和记录名中可以使用中文、大写</strong></li> 
   <li>添加域名窗口中提示可以添加泛域名</li> 
   <li><strong>创建集群时增加“只允许绑定的域名访问”选项</strong></li> 
   <li>健康检查设置域名时检查域名是否存在</li> 
  </ul> </li> 
 <li>访问日志 
  <ul> 
   <li>访问日志里以标签的形式显示中文域名</li> 
   <li>访问日志中增加源站状态码</li> 
   <li>集群设置中增加统一的服务设置，包括域名和日志相关配置；现在可以设置不记录服务错误日志到节点运行日志</li> 
   <li>缓存条件增加”忽略URI参数“选项</li> 
  </ul> </li> 
 <li>域名解析 
  <ul> 
   <li>创建集群的时候可以设置DNS记录的默认TTL</li> 
   <li><strong>域名解析增加EdgeDNS API</strong>，可以通过API对接别的GoEdge系统提供的智能DNS服务</li> 
   <li>DNS域名增加分页，可以在域名解析--单个服务商账号中查看</li> 
   <li>集群设置--DNS设置页显示DNS账号名</li> 
  </ul> </li> 
 <li>缓存 
  <ul> 
   <li>各缓存条件默认支持206 Partial Content</li> 
   <li>缓存条件增加”忽略URI参数“选项</li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:start">EdgeAPI</h2> 
<ul> 
 <li>启动时尝试自动设置binlog过期时间、binlog缓存等相关参数</li> 
 <li>优化接口权限，部分接口不允许普通用户（注意：非管理员用户）通过REST方式调用</li> 
 <li>用户端刷新预热缓存超过5分钟自动认为已完成</li> 
 <li>BugFix:<span> </span><strong>修复DNSPod只能取前100个域名的问题</strong></li> 
 <li>同步域名解析时不再强制要求修复节点问题</li> 
 <li>REST 接口接收内容为空时，默认为<span> </span><code>&#123;&#125;</code></li> 
 <li><strong>服务流量接口增加5分钟查询接口</strong></li> 
 <li><strong>使用并发队列安装和升级数据表，避免安装或升级耗时过长</strong></li> 
 <li>BugFix:<span> </span><strong>修复多个日志数据库节点分布不平均的问题</strong></li> 
 <li>自动调整写入单次数据库事务写入访问日志数量</li> 
</ul> 
<h2 style="text-align:start">EdgeNode</h2> 
<ul> 
 <li><strong>改进缓存LFU算法</strong>，现在如果缓存文件尺寸达到容量限制时，先清理过期的缓存，再清理旧缓存；<strong>修复了以往错误删除热点文件的Bug</strong></li> 
 <li>可以使用EdgeRecover环境变量指示恢复数据库，启动时使用env EdgeREcover=on edge-node start 即可</li> 
 <li>访问日志因尺寸过大无法提交到API节点时，自动去除requestBody后再次尝试，以提升访问日志记录成功比率</li> 
 <li>BugFix:<span> </span><strong>修复有多个网络出口时，可能无法正确转发UDP消息的问题</strong></li> 
 <li>检查synflood时忽略IP白名单和局域网连接</li> 
 <li><strong>Websocket也支持失败自动重试</strong></li> 
 <li><strong>Websocket支持自定义响应Header</strong></li> 
 <li>BugFix: 修复RPC选项没有生效的Bug，现在在HTTP传输时也可以使用压缩、最大消息尺寸等选项</li> 
 <li>服务配置只初始化一次，防止在配置变更时发生冲突</li> 
 <li>部分页面文字支持繁体中文（正体）</li> 
 <li>IP名单支持定时清理</li> 
 <li>已删除的IP不再写入本地数据库</li> 
 <li>优化服务相关错误信息提示，避免因错误提示过多而造成的困扰</li> 
</ul> 
<p style="color:#24292f; text-align:start"><span style="background-color:#ffffff; color:#24292f">完整变更说明：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs%2FReleases%2FIndex.md" target="_blank">https://goedge.cn/docs/Releases/Index.md</a><br> <span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/download</a></p>
                                        </div>
                                      
</div>
            