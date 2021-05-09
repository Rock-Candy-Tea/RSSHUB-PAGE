
---
title: 'Netbox 2.11.3 发布，IP 地址与数据中心管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3546'
author: 开源中国
comments: false
date: Sat, 08 May 2021 23:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3546'
---

<div>   
<div class="content">
                                                                    
                                                        <p>NetBox 是一个 IP 地址管理（IP address management，IPAM）和数据中心基础设施管理（data center infrastructure management，DCIM）工具。   </p> 
<p>Netbox 2.11.3 现已完成发布，具体更新内容如下：</p> 
<p><strong>Enhancements</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6197" target="_blank">＃6197-</a>引入了<code>SESSION_COOKIE_NAME</code>配置参数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6318" target="_blank">＃6318-</a>添加 OM5 MMF cable 类型</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6351" target="_blank">＃6351-</a>将聚合计数添加到 tenant 视图</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6359" target="_blank">＃6359-</a>为组织和嵌套组模型启用自定义链接</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6240" target="_blank">＃6240-</a>修复了 VLAN 组视图下可用 VLAN 范围的显示</p> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6308" target="_blank">＃6308-</a>修复 VLAN 组视图中可用 VLAN 的链接</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6309" target="_blank">＃6309-</a>将 parent VM 接口分配限制在 parent VM 上</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6312" target="_blank">＃6312-</a>接口设备过滤器仅在设备为主设备时才应返回所有虚拟机箱接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6313" target="_blank">＃6313-</a>在 manufacturer 视图下修复设备类型实例计数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6321" target="_blank">＃6321-</a>恢复 prefix IP 视图下的“add an IP”按钮</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6333" target="_blank">＃6333-</a>通过主键修复对电路终端的过滤</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6339" target="_blank">＃6339-</a>在查看虚拟机箱主机时改进接口的顺序</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6350" target="_blank">＃6350-</a>通过 REST API 分配可用的 IPv6 地址时，请包含第一个和最后一个 IP 地址</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6355" target="_blank">＃6355-</a>修复交换 A/Z 电路终端时的缓存错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6357" target="_blank">＃6357-</a>修复 ProviderNetwork 嵌套的 API 序列化程序</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6363" target="_blank">＃6363-</a>创建 cluster 时，正确填充 cluster 组</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F6369" target="_blank">＃6369-</a>修复 non-scoped groups 中 VLAN 的接口分配</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Freleases%2Ftag%2Fv2.11.3" target="_blank">https://github.com/netbox-community/netbox/releases/tag/v2.11.3</a></p>
                                        </div>
                                      
</div>
            