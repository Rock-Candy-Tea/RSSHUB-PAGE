
---
title: 'GoEdge CDN v0.4.8 发布，DDoS 防护及 40 多项改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-11013efd318958d10953915a0a191c62dce.png'
author: 开源中国
comments: false
date: Mon, 20 Jun 2022 09:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-11013efd318958d10953915a0a191c62dce.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333"><span> </span>是一款可以帮你快速构建 CDN & WAF 平台的工具，支持 HTTP、HTTPS、Websocket、TCP、TLS、UDP、PROXY Protocol、IPv6、WAF 等特性，支持多个第三方DNS服务。</span></p> 
<p>v0.4.8 发布，提供了基础的DDoS防护、缓存刷新预热任务管理及40多项其他改进。</p> 
<h3 style="text-align:start"><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-11013efd318958d10953915a0a191c62dce.png" width="600" referrerpolicy="no-referrer"></h3> 
<ul> 
 <li>安装 
  <ul> 
   <li>安装GoEdge过程中，如果数据库地址填写的是公网IP，则提示会影响系统运行性能</li> 
  </ul> </li> 
 <li>界面 
  <ul> 
   <li>优化网站服务下子菜单顺序</li> 
  </ul> </li> 
 <li>边缘节点 
  <ul> 
   <li><strong>实现基础的DDoS防护</strong>， 参考文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs%2FNode%2FDDoS-Protection.md" target="_blank">这里</a></li> 
   <li><strong>边缘节点设置中增加DNS解析库类型设置</strong>：可以在节点设置–系统设置–修改DNS解析库中修改，修复在Ubuntu部分版本上源站使用域名地址会导致边缘节点进程崩溃的Bug</li> 
   <li>集群节点列表可以使用”未分组“筛选</li> 
   <li>健康检查增加是否记录访问日志选项：可以在某个集群设置–健康检查–启用状态下–更多选项–选中或取消选中记录访问日志</li> 
   <li>发送远程指令时包括从节点：所以在缓存策略清理某个集群缓存时，也包含从节点</li> 
   <li>节点详情中提示边缘节点和API节点时间差，以提醒运维人员同步时间：在节点已在线的情况下，可以在节点详情–运行状态中查看”上次更新时间“，如果当前边缘节点和API节点之间有时间差，则会以红色字体提示时间差。</li> 
  </ul> </li> 
 <li>网站服务 
  <ul> 
   <li>创建网站服务时强制填写域名，避免因为未填写域名而导致的各种后续问题</li> 
   <li>创建网站服务时优化源站未填写时的交互，现在会自动弹出源站添加窗口</li> 
   <li>启用服务HTTP/HTTPS设置时如果没有设置端口，则自动添加80/443；防止管理员修改时忘记增加端口</li> 
   <li>添加源站时校验端口号，减少误操作</li> 
  </ul> </li> 
 <li>访问日志 
  <ul> 
   <li>访问日志查询增加requestPath:/hello、proto:HTTP/1.1、scheme:http等语法</li> 
  </ul> </li> 
 <li>缓存 
  <ul> 
   <li><strong>增加刷新、预热缓存任务管理</strong>，现在可以直接在菜单”刷新预热”中快速进行相关操作，相关的功能和API都已经改成异步任务管理</li> 
   <li>如果缓存条件支持206 Partial Content，则第一次加载时自动尝试从分片缓存中读取内容，常适用于音视频和文件下载</li> 
   <li>不限制206 Partial Content两次写入文件的时间差，增加分片写入效率，常适用于音视频和文件下载</li> 
   <li>优化缓存MaxOpenFiles算法</li> 
   <li>静态文件分发也支持缓存</li> 
  </ul> </li> 
 <li>WAF 
  <ul> 
   <li>WAF策略中增加验证码相关定制设置：可以在某个WAF策略中点”修改“–更多选项–验证码动作配置中配置相关选项</li> 
   <li>WAF规则中国家/地区、省份、城市、ISP增加候选项检索</li> 
   <li>WAF规则中增加完整URL（包含域名，代号<code>$&#123;requestURL&#125;</code>）参数</li> 
   <li><strong>尝试使用本地防火墙提升黑名单封锁效率</strong></li> 
   <li>白名单中IP不受请求限制（流量、连接数）等的影响</li> 
   <li>计算CC的时候不再跨时间范围累积</li> 
   <li>WAF验证码将刷新验证码页面计入校验失败次数，防止恶意无限刷新</li> 
   <li>自动将同集群节点IP加入白名单</li> 
  </ul> </li> 
 <li>域名解析 
  <ul> 
   <li>DNS服务商增加厂家筛选</li> 
   <li>阿里云DNS增加区域ID，对区域有特殊要求时可以填写</li> 
  </ul> </li> 
 <li>命令行 
  <ul> 
   <li>增加<code>edge-admin [dev|prod]</code>命令来切换环境：在dev环境下，修改模板文件、样式表文件时刷新会立即生效；否则默认在prod模式下，需要重启服务后才会生效</li> 
  </ul> </li> 
 <li>运维 
  <ul> 
   <li>增加管理平台所在服务器磁盘空间过小提醒</li> 
   <li>发生API连接错误时，提示更详细，更方便运维人员快速发现问题</li> 
  </ul> </li> 
 <li>性能 
  <ul> 
   <li>使用新的gzip库提升数倍性能</li> 
  </ul> </li> 
 <li>WebP 
  <ul> 
   <li>WebP判断长度内容时忽略ChunkEncoding传输的内容</li> 
   <li>静态文件分发也支持WebP转换</li> 
  </ul> </li> 
 <li>其他 
  <ul> 
   <li>取消IP库上传入口，防止用户误操作</li> 
   <li>DNS解析库默认使用Go原生库，如因此产生服务的不稳定，请及时向我们报告</li> 
   <li>在严格匹配域名模式下仍然可以通过节点IP进行健康检查</li> 
   <li>ACME申请证书时如果找不到Token，则直接跳过执行后面请求</li> 
   <li>缩短指标统计队列长度，防止同时提交的指标数过多</li> 
   <li>增加edge-node accesslog命令，用来在本地即时查看访问日志，具体用法参考<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs%2FNode%2FCommands.md%23%25E6%259C%25AC%25E5%259C%25B0%25E6%259F%25A5%25E8%25AF%25A2%25E8%25AE%25BF%25E9%2597%25AE%25E6%2597%25A5%25E5%25BF%2597" target="_blank">这里</a></li> 
   <li>忽略301, 302, 303, 307, 308响应中没有Location Header的错误提示</li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            