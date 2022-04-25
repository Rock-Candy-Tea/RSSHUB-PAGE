
---
title: 'GoEdge CDN v0.4.7 发布，40多项改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7deed1ee9d4b8301909ffef4d7a7a4e4b91.png'
author: 开源中国
comments: false
date: Mon, 25 Apr 2022 09:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7deed1ee9d4b8301909ffef4d7a7a4e4b91.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以帮你快速构建 CDN & WAF 平台的工具，支持HTTP、HTTPS、TCP、TLS、UDP、PROXY Protocol、IPv6、WAF等特性。</span></p> 
<p><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-7deed1ee9d4b8301909ffef4d7a7a4e4b91.png" width="600" referrerpolicy="no-referrer"></p> 
<p>v0.4.7提供了大量细节更新：</p> 
<ul> 
 <li>网站服务 
  <ul> 
   <li>服务列表中增加5分钟下行带宽一列，并可排序</li> 
   <li>服务列表选择分组中增加”[未分组]“选项</li> 
   <li>单个服务切换集群时可以选择是否保留节点上的配置</li> 
   <li>单个服务切换集群后，自动删除先前的相关解析记录</li> 
  </ul> </li> 
 <li>反向代理 
  <ul> 
   <li>将创建服务时的”反向代理”修改为”CDN加速”</li> 
   <li>将服务设置中”反向代理”修改为”源站”</li> 
   <li>创建服务时如果类型为CDN加速，则强制添加源站</li> 
  </ul> </li> 
 <li>WebP 
  <ul> 
   <li>默认只有满足缓存条件的图片内容才会被转换</li> 
   <li>在集群设置中可以修改WebP策略</li> 
  </ul> </li> 
 <li>访问日志 
  <ul> 
   <li>优化访问日志详情弹框界面，将Header、Cookie等排序显示</li> 
   <li>访问日志可以使用分表查询，大幅提升了查询速度</li> 
   <li>多个访问日志列表中增加WAF相关标签</li> 
   <li>支持使用完整的URL作为关键词搜索</li> 
   <li>修复访问日志可能显示重复的问题</li> 
  </ul> </li> 
 <li>WAF 
  <ul> 
   <li>默认记录WAF相关访问日志，即使服务访问日志没有开启，可以在WAF策略中修改此行为</li> 
  </ul> </li> 
 <li>缓存 
  <ul> 
   <li>缓存条件中增加暂停/恢复功能</li> 
   <li>缓存条件修改后自动保存</li> 
  </ul> </li> 
 <li>域名 
  <ul> 
   <li>在域名设置界面中搜索域名时只显示匹配的结果</li> 
  </ul> </li> 
 <li>IP名单 
  <ul> 
   <li>IP名单可以使用级别、名单类型筛选</li> 
   <li>IP名单增加区域和ISP显示</li> 
   <li>IP名单中白名单IP使用绿色显示</li> 
  </ul> </li> 
 <li>证书 
  <ul> 
   <li>证书在上传时检查有效期，防止有效期小于1970年</li> 
   <li>CA证书支持只有一级发行商的证书</li> 
  </ul> </li> 
 <li>统计 
  <ul> 
   <li>修复服务统计–流量统计–即时的tooltip错误</li> 
  </ul> </li> 
 <li>指标 
  <ul> 
   <li>缩短默认的指标数据保留周期</li> 
   <li>管理员可以自行设定指标数据保留周期</li> 
   <li>对指标数据进行分表，可以承载更大数据量</li> 
   <li>写入指标统计数据时忽略MySQL 1213错误</li> 
  </ul> </li> 
 <li>错误日志 
  <ul> 
   <li>使用单独页面展示服务相关运行错误日志，不再放在服务列表上面，并可以一键设为修复</li> 
  </ul> </li> 
 <li>边缘节点 
  <ul> 
   <li>增加全局的节点列表，可以显示所有集群的所有节点</li> 
   <li>节点列表增加负载显示，并显示1分钟平均带宽，并可排序</li> 
   <li>SSH认证相关创建和修改界面中自动填入SSH地址</li> 
  </ul> </li> 
 <li>集群 
  <ul> 
   <li>修复集群主域名或者子域名时，自动删除以前的相关解析记录</li> 
   <li>健康检查超时时提示错误</li> 
   <li>健康检查默认只做基础的请求</li> 
   <li>修复健康检查时无法根据检查结果自动上下线节点IP地址的Bug</li> 
  </ul> </li> 
 <li>域名解析 
  <ul> 
   <li>支持DNSPod国际版</li> 
   <li>可以使用域名搜索DNS账号</li> 
  </ul> </li> 
 <li>数据库 
  <ul> 
   <li>清理界面增加行数（只是粗略预估，非精确）</li> 
   <li>清理界面增加更多可以手动清理的数据表</li> 
   <li>优化max_prepared_stmt_count参数使用</li> 
  </ul> </li> 
 <li>界面 
  <ul> 
   <li>管理界面设置设置中可以修改显示的时区</li> 
   <li>服务设置中”特殊页面”修改为”自定义页面”</li> 
   <li>多个页面增加导航</li> 
  </ul> </li> 
 <li>API节点 
  <ul> 
   <li>启动时自动将相关端口加入到本地防火墙</li> 
   <li>可以设置单个API节点为主节点，设置后所有后台任务都会在主节点运行</li> 
  </ul> </li> 
 <li>其他 
  <ul> 
   <li>使用uglifyjs压缩js组件文件</li> 
   <li>启动时自动将相关端口加入到本地防火墙</li> 
   <li>多个选择时区的地方增加UTC选项</li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            