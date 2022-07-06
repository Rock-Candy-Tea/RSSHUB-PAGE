
---
title: 'Zabbix 6.2 正式发布，特别优化中大型环境部署的性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-76590dfcc851db68aadf60fd993d0330584.png'
author: 开源中国
comments: false
date: Wed, 06 Jul 2022 11:38:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-76590dfcc851db68aadf60fd993d0330584.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">Zabbix 6.2将又一次提升新用户和资深用户的用户体验，主要通过一系列的UI/UX优化、新监控项和配置选项以及中大型环境部署的性能优化。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">快速了解Zabbix6.2中最值得关注的新功能！</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">通过抑制不相关的Zabbix问题减少不必要的噪声</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">在CyberArk vault中存储机密信息，确保安全</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">AWS EC 2官方模板</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">从Zabbix前端同步Zabbix proxy配置</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">对发现的主机进行更多控制</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">扩展VMware监控</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">跟踪 active checks</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Zabbix性能优化和内部更改</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化execute now的可用性和行为</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">单独的主机组和模板组</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持多个LDAP servers进行用户身份验证</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更多模板和集成</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">其他新功能和优化</p> </li> 
</ol> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#42689e">01</span> 通过抑制不相关的Zabbix问题减少不必要的噪声</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">Zabbix管理员现在可以通过抑制不相关的问题来隐藏它们：</p> 
<ul> 
 <li style="color: rgb(0, 0, 0); margin-left: 0px; margin-right: 0px; text-align: justify;">在特定时间点之前抑制问题</li> 
 <li style="color: rgb(0, 0, 0); margin-left: 0px; margin-right: 0px; text-align: justify;">无限期抑制问题，直到手动删除</li> 
 <li style="color: rgb(0, 0, 0); margin-left: 0px; margin-right: 0px; text-align: justify;">与抑制的问题相关的动作操作将暂停，直到问题解除抑制为止</li> 
 <li style="color: rgb(0, 0, 0); margin-left: 0px; margin-right: 0px; text-align: justify;">在 Problems 页面中选择隐藏或显示抑制的问题</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-76590dfcc851db68aadf60fd993d0330584.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#42689e">02</span> 在CyberArk vault中存储机密信息确保安全</strong></p> 
<p style="margin-left:0; margin-right:0">除了以前支持的HashiCorp vault之外，Zabbix 6.2还官方支持在CyberArk vault中存储机密信息：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">可在CyberArk和HashiCorp vault之间选择</li> 
 <li style="margin-left: 0px; margin-right: 0px;">使用vault证书加密与CyberArk vault的连接</li> 
 <li style="margin-left: 0px; margin-right: 0px;">保护数据库证书和用户宏的安全</li> 
 <li style="margin-left: 0px; margin-right: 0px;">可以通过Zabbix API配置和检索Zabbix vault供应商</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#42689e">03</span> AWS EC2 官方模板</strong></p> 
<p style="margin-left:0; margin-right:0">使用正式的Zabbix AWS EC2模板监控AWS EC2实例和附加的AWS EBS volumes：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">监控AWS EC2 CPU、网络、磁盘、状态和许多其他指标</li> 
 <li style="margin-left: 0px; margin-right: 0px;">发现和监控AWS EBS volumes</li> 
 <li style="margin-left: 0px; margin-right: 0px;">发现和监控AWS EC2告警，并对告警状态变化作出反应</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c82f52a169a3456f3d65afe3c3448815491.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#42689e">04</span> 从Zabbix前端同步Zabbix proxy配置</strong></p> 
<p style="margin-left:0; margin-right:0">Zabbix proxy管理从未如此简单！现在，proxy配置可以立即从Zabbix前端重新加载：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">现在可以从Administration - Proxies 页面刷新Zabbix proxy配置</li> 
 <li style="margin-left: 0px; margin-right: 0px;">可以直接从Zabbix server上的命令行刷新Zabbix proxy配置</li> 
 <li style="margin-left: 0px; margin-right: 0px;">可以使用Zabbix API刷新Zabbix proxy配置</li> 
 <li style="margin-left: 0px; margin-right: 0px;">主动proxy和被动proxy都支持集中配置刷新</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5454908cd114c2438fdde15ee8daee4aa76.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#42689e">05</span> 对发现的主机进行更多控制</strong></p> 
<p style="margin-left:0; margin-right:0">从主机原型中发现的主机现在支持手动编辑模板、标签和用户宏：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">手动将模板链接到从主机原型中发现的主机</li> 
 <li style="margin-left: 0px; margin-right: 0px;">能够在从主机原型创建的主机上创建和修改用户宏</li> 
 <li style="margin-left: 0px; margin-right: 0px;">现在可以在从主机原型创建的主机上创建其他标签</li> 
 <li style="margin-left: 0px; margin-right: 0px;">API host 方法已扩展，可支持模板与主机原型创建的主机之间的手动链接</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f3dcc7feef89431ca9e53d9e83e31aad14f.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#42689e">06</span> 扩展VMware监控</strong></p> 
<p style="margin-left:0; margin-right:0">现在可以进一步修改使用Zabbix VMware监控功能创建的主机：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">手动为发现的VMware主机分配其他模板</li> 
 <li style="margin-left: 0px; margin-right: 0px;">在发现的VMware主机上创建和修改用户宏</li> 
 <li style="margin-left: 0px; margin-right: 0px;">在发现的VMware主机上创建其他标签</li> 
</ul> 
<p style="margin-left:0; margin-right:0">VMware 监控已扩展到支持许多新监控项和低级别自动发现规则。这可以监控新的指标，例如：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">VMware告警状态</li> 
 <li style="margin-left: 0px; margin-right: 0px;">VMware快照的数量和时间戳</li> 
 <li style="margin-left: 0px; margin-right: 0px;">Hyperviso网络接口指标</li> 
 <li style="margin-left: 0px; margin-right: 0px;">VMware vSphere分布式交换机端口指标</li> 
 <li style="margin-left: 0px; margin-right: 0px;">数据存储IOPS读/写指标</li> 
 <li style="margin-left: 0px; margin-right: 0px;">数据存储性能计数器</li> 
 <li style="margin-left: 0px; margin-right: 0px;">VMware guest 状态</li> 
 <li style="margin-left: 0px; margin-right: 0px;">及其他更多监控项</li> 
</ul> 
<p style="margin-left:0; margin-right:0">现在可以根据VMware主机的电源状态对其进行筛选。</p> 
<p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-d8bc5b5487c56da61bd6f8b0b6bbdf0e970.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#42689e">07</span> 跟踪 active checks</strong></p> 
<p style="margin-left:0; margin-right:0">当鼠标悬停在Zabbix agent界面图标上时，现在可以观察到Zabbix active agent检查状态：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">直接从Zabbix前端跟踪被动和主动 agent 检查的可用性</li> 
 <li style="margin-left: 0px; margin-right: 0px;">agent配置文件中提供了可定制的Zabbix agent心跳周期</li> 
 <li style="margin-left: 0px; margin-right: 0px;">新的内部监控项可用于active agent检查状态监控</li> 
 <li style="margin-left: 0px; margin-right: 0px;">Zabbix API还可以检索Zabbix active agent检查状态</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f5720a1f8194497d277e731e0b3fdaf672f.png" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#42689e">08</span> Zabbix性能优化和内部更改</strong></p> 
<p style="margin-left:0; margin-right:0">Zabbix server现在只接收最新的配置更改，而不是定期重新加载完整的Zabbix配置数据：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">配置缓存将支持增量更新</li> 
 <li style="margin-left: 0px; margin-right: 0px;">新的配置同步逻辑大大提高了大型Zabbix实例的性能</li> 
</ul> 
<p style="margin-left:0; margin-right:0">初始监控项检查逻辑已得到优化，新创建的监控项在创建后一分钟内收到其第一个指标，而不是在监控项更新间隔内的随机时间点进行检查：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">新监控项在创建后一分钟内进行检查</li> 
</ul> 
<p style="margin-left:0; margin-right:0">新引入的用户宏缓存减少了配置缓存锁定，因此提高了Zabbix的总体性能：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">新建用户宏缓存</li> 
</ul> 
<p style="margin-left:0; margin-right:0">Zabbix库结构的多项更改：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">优化Zabbix库结构</li> 
 <li style="margin-left: 0px; margin-right: 0px;">删除循环Zabbix库依赖项</li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#42689e">09</span> 优化execute now的可用性和行为</strong></p> 
<p style="margin-left:0; margin-right:0">之前用于立即检索指标的execute now（立即执行）按钮，现在可从Latest data （最新数据）页面获得：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">Execute now按钮添加到 Latest data 页面</li> 
 <li style="margin-left: 0px; margin-right: 0px;">不支持立即执行的监控项将被忽略，而不会显示错误消息</li> 
 <li style="margin-left: 0px; margin-right: 0px;">如果用户试图在不支持立即执行功能的监控项上使用该功能，将显示警告</li> 
 <li style="margin-left: 0px; margin-right: 0px;">“立即执行”权限已添加到自定义Zabbix角色时可用的权限列表中</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px"><img alt src="https://oscimg.oschina.net/oscnet/up-dcc2a110f9a9f5ac1d1cc9059d358a958e9.png" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#42689e">10</span> 单独的主机组和模板组</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">为了简化主机和模板筛选，模板现在分组在模板组中，而不是主机组中：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">配置菜单下的新建模板组页面</li> 
 <li style="margin-left: 0px; margin-right: 0px;">在升级过程中，现有模板将移动到模板组</li> 
 <li style="margin-left: 0px; margin-right: 0px;">完全支持从以前的Zabbix版本导入模板和主机，并将从导入文件中创建适当的组</li> 
 <li style="margin-left: 0px; margin-right: 0px;">可以为模板组页面分配基于角色的访问权限</li> 
 <li style="margin-left: 0px; margin-right: 0px;">新的模板组API方法可用于创建、修改和检索模板组</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px"><img alt src="https://oscimg.oschina.net/oscnet/up-d92fe8186865ad2fd60667def348eca12cc.png" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#42689e">11</span> 支持多个LDAP servers进行用户身份验证</strong></p> 
<p style="margin-left:0; margin-right:0">现在可以在Authentication - LDAP settings定义和保存多个LDAP servers：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">优化安全性并符合公司策略，其中组织单位通过不同的LDAP servers进行身份验证</li> 
 <li style="margin-left: 0px; margin-right: 0px;">在LDAP servers迁移或更新后，在LDAP servers 之间无缝切换用户身份验证</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px"><img alt src="https://oscimg.oschina.net/oscnet/up-554ac50cccf2a8041c80894bb69745c7fde.png" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#42689e">12</span> 更多模板和集成</strong></p> 
<p style="margin-left:0; margin-right:0">Zabbix 6.2为最受欢迎的供应商提供了许多新模板：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">Envoy proxy</li> 
 <li style="margin-left: 0px; margin-right: 0px;">HashiCorp Consul</li> 
 <li style="margin-left: 0px; margin-right: 0px;">AWS EC2 Template</li> 
 <li style="margin-left: 0px; margin-right: 0px;">Proxmox</li> 
 <li style="margin-left: 0px; margin-right: 0px;">CockroachDB</li> 
 <li style="margin-left: 0px; margin-right: 0px;">TrueNAS</li> 
 <li style="margin-left: 0px; margin-right: 0px;">HPE MSA 2060 & 2040</li> 
 <li style="margin-left: 0px; margin-right: 0px;">HPE Primera</li> 
 <li style="margin-left: 0px; margin-right: 0px;">优化的S.M.A.R.T.监控模板</li> 
</ul> 
<p style="margin-left:0; margin-right:0">Zabbix 6.2为GLPI IT资产管理解决方案引入了webhook集成。此webhook可用于将Zabbix中创建的问题转发给GLPi帮助页面。</p> 
<p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-c6305b60e3e3b230d1c323697f8e4651cb7.png" referrerpolicy="no-referrer"></p> 
<p><span style="color:#42689e"><strong>13 </strong></span><strong>其他新功能和优化</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">更多改进功能（部分）：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">数字时钟仪表盘小组件</li> 
 <li style="margin-left: 0px; margin-right: 0px;">仪表盘矢量图的堆叠图选项</li> 
 <li style="margin-left: 0px; margin-right: 0px;">全局视图默认仪表盘已重新设计</li> 
 <li style="margin-left: 0px; margin-right: 0px;">对脚本类型监控项和手动脚本支持&#123;INVENTORY.*&#125;宏</li> 
 <li style="margin-left: 0px; margin-right: 0px;">新的Windows注册表监控项</li> 
 <li style="margin-left: 0px; margin-right: 0px;">用于监控和发现Windows、Linux和BSD操作系统上的OS进程和进程参数的新监控项</li> 
 <li style="margin-left: 0px; margin-right: 0px;">删除了对Zabbix数据库MD5 hashes的支持</li> 
 <li style="margin-left: 0px; margin-right: 0px;">将“文档”按钮添加到所有Zabbix部分</li> 
 <li style="margin-left: 0px; margin-right: 0px;">“文档”按钮能打开相关的Zabbix文档页面</li> 
 <li style="margin-left: 0px; margin-right: 0px;">针对XSS攻击优化了Zabbix前端保护</li> 
</ul>
                                        </div>
                                      
</div>
            