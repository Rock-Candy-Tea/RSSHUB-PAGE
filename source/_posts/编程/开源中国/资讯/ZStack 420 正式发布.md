
---
title: 'ZStack 4.2.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e5660de8901462818bc72424fdc2d67ebf4.png'
author: 开源中国
comments: false
date: Tue, 10 Aug 2021 01:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e5660de8901462818bc72424fdc2d67ebf4.png'
---

<div>   
<div class="content">
                                                                                            <p>2021年8月3日，ZStack正式发布最新版本——ZStack4.2.0，涵盖一系列重要功能，以下为您进行详细介绍。</p> 
<p><strong>ZStack4.2.0新功能概览</strong></p> 
<p><strong>1、云主机新增故障检测功能</strong></p> 
<ul> 
 <li>支持检测云主机故障（Windows蓝屏/Linux死机）并告警</li> 
 <li>支持设置故障策略，有效提高运维效率</li> 
</ul> 
<p><strong>2、弹性裸金属管理增强</strong></p> 
<ul> 
 <li>弹性裸金属管理支持多租户</li> 
 <li>支持对弹性裸金属实例进行计费</li> 
</ul> 
<p><strong>3、ZStack Cloud云平台新增支持异构集群管理<br> 4、负载均衡新增支持域名转发功能<br> 5、Ceph类型的镜像服务器增强</strong></p> 
<ul> 
 <li>Ceph类型的镜像服务器支持云主机整机克隆</li> 
 <li>支持导出存储在Ceph类型镜像服务器上的镜像文件</li> 
</ul> 
<p><strong>6、添加云主机镜像支持指定操作系统类型<br> 7、支持免密跳转至ZStackCeph企业版存储的管理节点<br> 8、可视化展示报警消息统计<br> 9、其他功能和优化</strong></p> 
<p><strong>1、云主机新增故障检测功能</strong><br> ZStackCloud 4.2.0新增云主机故障检测功能，提供更精细的云主机状态监控和故障预警。</p> 
<p><strong>1）支持检测云主机故障（Windows蓝屏/Linux死机）并告警</strong><br> ZStackCloud 4.2.0新增了用于检测云主机常见故障的默认事件报警器。当云主机出现故障时将及时发出告警，运维人员可以快速响应并处理，保证业务系统始终处于健康状态。同时支持手动创建云主机故障报警器，通过自定义接收端掌握关键业务云主机健康信息，保证业务稳定运行。</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-e5660de8901462818bc72424fdc2d67ebf4.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">新增云主机故障默认报警器</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-c6be01c66e49f918b53b7a2f25810201eec.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">创建云主机故障报警器</p> 
<p><strong>2）支持设置故障策略，有效提高运维效率</strong></p> 
<p>ZStackCloud 4.2.0支持自动处理云主机故障，用户可在云平台中按需配置云主机的故障处理策略，当云主机出现故障时，系统将按照已配置的策略自动处理，节省运维人力，保证云主机正常运行。</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-1190efb6957c7ac32acbfd8ff9bd2e7a603.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">全局设置云主机故障策略</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-97d676529ce4786548303cf681666361e46.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">云主机独立设置故障策略</p> 
<p><strong>2、弹性裸金属管理增强</strong></p> 
<p>ZStack Cloud 4.2.0基于用户实际使用场景，对弹性裸金属管理功能进行增强。</p> 
<p><strong>1）弹性裸金属管理支持多租户</strong></p> 
<p>ZStack Cloud 4.2.0开始，弹性裸金属管理支持多租户。针对企业管理中的项目成员（项目负责人/项目管理员/普通项目成员）开放弹性裸金属管理模块使用权限，项目成员可通过管理员共享的弹性裸金属规格创建弹性裸金属实例。</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-448e272bbe801dc34814c7abe2545db4042.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">弹性裸金属管理支持多租户</p> 
<p><strong>2）支持对弹性裸金属实例进行计费</strong></p> 
<p>ZStack Cloud支持将各资源计费单价汇总为一张价目表，提供准公有云计费方式体验。通过价目表形式，用户可对一组资源的计费单价进行集中高效管理。之前版本已经支持的计费资源包括：CPU、内存、根云盘、数据云盘、GPU设备、公网IP（云主机IP）、公网IP（虚拟IP）。</p> 
<p>ZStack Cloud 4.2.0新增支持弹性裸金属实例计费。以弹性裸金属规格粒度设置计费单价，即可对使用该规格裸金属节点的弹性裸金属实例进行计费，满足用户对不同资源计费场景的需求。</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-7aeb60ced44be10900a20672d1e6c5dc4b5.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">弹性裸金属实例计费</p> 
<p><strong>3、ZStack Cloud</strong><strong>云平台新增支持异构集群管理</strong></p> 
<p>在实际业务场景中，用户会使用到多种CPU架构的硬件设备，统一管控较为困难。ZStackCloud 4.2.0新增支持异构集群管理功能，一朵云即可添加多种CPU架构的集群，满足企业多种硬件设备的异构需求。</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-57c66b94b518f15b29fd5b8da5b8aaba639.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">集群设置CPU架构</p> 
<p><strong>4、负载均衡新增支持域名转发功能</strong></p> 
<p>ZStack Cloud 4.2.0开始，负载均衡新增支持域名转发功能。七层负载均衡服务（HTTPS或HTTP协议）支持配置域名或者URL路径转发策略，将来自不同域名或者URL路径的请求转发给不同的后端服务器处理。</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-63ac99b6d6a555da85308fb8a2dbb7ba679.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">公有网络负载均衡</p> 
<p>为负载均衡对应的监听器添加转发规则即可使用此功能，同一监听器最多支持加载40条转发规则，同一条转发规则支持关联多个后端服务器组。</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-8bfa1aa40e84884d360bcb27946527f1a10.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">添加转发规则</p> 
<p><strong>5、Ceph</strong><strong>类型的镜像服务器增强</strong></p> 
<p>ZStackCloud 4.2.0对Ceph类型的镜像服务器进行了以下增强：</p> 
<p><strong>1）Ceph</strong><strong>类型的镜像服务器支持云主机整机克隆</strong></p> 
<p>在实际业务场景中，Ceph通常使用固定机型和超融合方式交付，缺少硬盘或服务器作为ImageStore镜像服务器，云主机整机克隆等功能无法实现。ZStackCloud 4.2.0支持Ceph镜像服务器的云主机整机克隆功能，用户可以根据自己的实际业务场景灵活部署镜像服务器，满足相关业务需求。</p> 
<p><strong>2）支持导出存储在Ceph类型镜像服务器上的镜像文件</strong></p> 
<p>ZStackCloud 4.2.0支持UI方式导出Ceph镜像服务器中的镜像文件，将原本复杂的命令行导出方式优化为UI操作按钮，用户只需在UI界面轻轻一点，即可快速获取到镜像的URL链接，极大地简化了操作流程和运维步骤。</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-e80cdf40a58120d782cfafa3d490c784636.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">支持导出Ceph镜像服务器上的镜像文件</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-4bd7a148e2f70b9f4e23e6990bbfc39ebcb.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">已导出镜像URL</p> 
<p><strong>6、添加云主机镜像支持指定操作系统类型</strong></p> 
<p>ZStackCloud 4.2.0提供了更丰富的GuestOS版本适配，在添加云主机镜像时，支持指定操作系统类型，对不同版本的镜像提供更全面和细粒度的功能适配与支持，满足用户多种操作系统的差异化功能需求。</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-d0ac4a19202d3f7e0c486c5db674467811b.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">云主机镜像指定操作系统</p> 
<p><strong>7、支持免密跳转至ZStackCeph企业版存储的管理节点</strong></p> 
<p>ZStackCloud 4.2.0支持免密跳转至ZStackCeph企业版存储的管理节点界面，用户只需在应用中心配置正确的用户名、密码和跳转链接，即可快速切换云平台页面和ZStackCeph企业版存储管理页面，避免二次登录，使用更加方便快捷。</p> 
<p><strong>8、可视化展示报警消息统计</strong></p> 
<p>ZStack Cloud 4.2.0对云平台报警消息增加可视化统计图表。不仅支持以柱状图方式可视化展示近一周内不同级别报警消息的统计情况，而且支持以饼图方式可视化展示近一周内不同资源的报警分布。方便运维人员快速了解云平台健康状况，提高运维效率。</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-96ac5edc9106efc1ffd9aecca12ce4319c8.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">报警消息统计</p> 
<p><strong>9、其他功能和优化</strong></p> 
<ul> 
 <li>支持智能网卡功能：VPC网络支持通过CLI命令行使用智能网卡功能，网络服务。</li> 
 <li>ZStackCeph企业版存储新增心跳检查。</li> 
 <li>创建V2V迁移任务时，增加缺少源集群和源主机的提示。</li> 
 <li>优化灾备恢复资源的性能，有效缩短恢复时间。</li> 
 <li>取消TUI支持。</li> 
 <li>HA模式下，双管理节点失联时，新增告警提示。</li> 
 <li>新增全局设置自主控制云盘扩容是否创建快照。</li> 
 <li>新增负载均衡 HTTPS 协议监听器“TLS安全策略”功能。</li> 
 <li>弹性裸金属实例和弹性裸金属节点主列表新增控制台快捷按钮。</li> 
 <li>调整二层网络删除策略：删除二层网络将同时删除物理机上关联网桥和VLAN。</li> 
 <li>ZStackCloud老版本升级到4.2.0版本，依然可以保留原主题外观配置。</li> 
 <li>优化物理机异常重启后（例如：异常断电）物理机重连时间。</li> 
 <li>优化企业管理项目回收策略，禁止已过期项目修改回收策略。</li> 
 <li>优化ZStack Cloud登录体验，按“ENTER”键可直接登录。</li> 
 <li>将 “高性能实例型”负载均衡类型名称修改为“性能独享型”。</li> 
 <li>敏感操作优化：设置/取消VPC路由器密码且勾选“重启VPC路由器”时，提高安全等级，需输入用户登录密码才可继续执行操作。</li> 
 <li>合并GPU设备的就绪状态：将原“未加载”和“系统”状态合并成“未加载”状态。</li> 
</ul>
                                        </div>
                                      
</div>
            