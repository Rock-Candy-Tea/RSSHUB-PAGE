
---
title: 'Zabbix 6.0 已发布，为 BSM、DevOps、ITOps 助力'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/c5b54285-d525-483d-8093-4364a86192e1.png'
author: 开源中国
comments: false
date: Mon, 21 Feb 2022 17:46:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/c5b54285-d525-483d-8093-4364a86192e1.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0">Zabbix 6.0 LTS 于2022年2月15日发布，为业务服务提供商、DevOps和ITOps团队提供了附加值，优化了整体监控工作流程，并在许多不同层面提供了新见解。Zabbix不断升级以满足日益增长的用户需求，有哪些值得关注的新功能？来一睹为快！</p> 
<p style="margin-left:0; margin-right:0"><strong>目录</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">业务服务监控达到全新高度</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">高阶业务服务SLA计算逻辑</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="background-color:rgba(254, 255, 255, 0)">通过根因分析增强业务服务监控能力</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">开箱即用的Zabbix server高可用群集</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">机器学习</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Kubernetes监控</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">详细高效的Zabbix审计日志模式</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">可视化数据的新方法</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Zabbix性能优化</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提升Zabbix Agent2模块化，新的Zabbix Agent 监控项和功能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">原生TLS/SSL网站证书监控</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">通用性改进</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">通过自定义密码复杂程度要求来保护您的Zabbix登录</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持定制前端展示品牌logo</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增模板和集成</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">其它新功能和优化</p> </li> 
</ol> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">01</span> BMS业务服务监控达到全新高度</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/c5b54285-d525-483d-8093-4364a86192e1.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">优化Services部分，显示业务服务的状态和当前SLA级别</p> 
<p style="margin-left:0; margin-right:0">通过对现有Services页面和功能的重大改进和优化，业务服务监控提升到了一个新高度。业务服务监控功能（BSM）非常适合多组件服务场景，例如服务器群集、负载平衡器和其它具有冗余组件的服务。</p> 
<p style="margin-left:0; margin-right:0">Zabbix 6.0提供多种功能自定义业务服务树实现BMS业务服务监控：</p> 
<p style="margin-left:0; margin-right:0">• 重新设计 Zabbix 6.0 Services页面和功能</p> 
<p style="margin-left:0; margin-right:0">• 支持单个Zabbix实例监控超过10万个业务服务</p> 
<p style="margin-left:0; margin-right:0">• 支持新的灵活服务状态计算逻辑</p> 
<p style="margin-left:0; margin-right:0">• 能够自定义业务服务的访问权限</p> 
<p style="margin-left:0; margin-right:0">• 能够为特定业务服务自定义只读和读写权限</p> 
<p style="margin-left:0; margin-right:0">• 业务服务权限既可以基于显式服务列表，也可以基于服务标签的访问限制</p> 
<p style="margin-left:0; margin-right:0">• 导出和导入业务服务树</p> 
<p style="margin-left:0; margin-right:0">• 新的Service动作类型能让用户接收告警并对业务服务状态更改作出反应</p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">02</span> 高阶业务服务SLA计算逻辑</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/c253c3a1-54a5-4054-bebd-940b0cc5b399.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span>提供大量可供选择的服务状态计算规则，能支持灵活的服务定义</span></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">业务服务状态计算逻辑在Zabbix 6.0中得到了极大扩展，增加了许多新功能，例如：</p> 
<p style="margin-left:0; margin-right:0">• 能够为每项业务服务分配权重</p> 
<p style="margin-left:0; margin-right:0">• 仅当N个子服务都处于X严重级别的问题状态时才更改状态</p> 
<p style="margin-left:0; margin-right:0">• 对处于问题状态下的子服务的权重进行分析并作出反应</p> 
<p style="margin-left:0; margin-right:0">• 仅当特定百分比的子服务处于问题状态时才作出反应</p> 
<p style="margin-left:0; margin-right:0">• 其它计算规则</p> 
<p style="margin-left:0; margin-right:0">用户还可以自定义和访问指定服务的SLA报告。</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">03</span> 通过根因分析增强业务服务监控能力</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/b665feac-4279-4e38-bef4-7865812f11d5.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span>根因问题会立即显示在service下</span></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">对业务服务执行根因分析。利用根因分析功能找出可能导致业务服务SLA下降的潜在问题列表：</p> 
<p style="margin-left:0; margin-right:0">• 在Zabbix前端Services页面查看根因问题列表</p> 
<p style="margin-left:0; margin-right:0">• 接收告警中的根因问题列表</p> 
<p style="margin-left:0; margin-right:0">• 通过Zabbix API收集根因问题信息</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">04</span> 开箱即用的Zabbix server高可用群集</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/19d2c962-c0f6-4c50-a11e-cf0548c2822c.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span>在系统信息组件中跟踪集群集节点状态</span></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">Zabbix server高可用防止硬件故障或计划维护期的停机：</p> 
<p style="margin-left:0; margin-right:0">• 原生选择加入HA群集配置</p> 
<p style="margin-left:0; margin-right:0">• 定义一个或多个备用节点</p> 
<p style="margin-left:0; margin-right:0">• 实时监控Zabbix server群集节点的状态</p> 
<p style="margin-left:0; margin-right:0">• 不需要外部工具即可将Zabbix server配置为HA群集模式</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">05</span> 机器学习</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/45366cbb-5d3e-499c-af47-a31d79f059ad.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span>使用新函数对意外异常率或与指标基准的偏差做出反应</span></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">新的基线监控和异常检测趋势功能以动态方式检测问题，而不是静态阈值方式：</p> 
<p style="margin-left:0; margin-right:0">• 新的趋势函数-baselinewma and baselinedev ，能计算指标基线和偏离值</p> 
<p style="margin-left:0; margin-right:0">• 新的趋势函数-trendstl，能检测异常指标行为</p> 
<p style="margin-left:0; margin-right:0">• 能够指定异常检测偏差算法及季节性</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">06</span> Kubernetes监控</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/51e3c91e-8547-4fdf-9ee6-1643a2e6a05b.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span>Zabbix 6.0 LTS添加了多个新模板，用于监控不同的Kubernetes组件</span></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">Zabbix 6.0 LTS新增Kubernetes监控功能，可以在Kubernetes系统从多个维度采集指标：</p> 
<p style="margin-left:0; margin-right:0">• Kubernetes节点和pods的自动发现和监控</p> 
<p style="margin-left:0; margin-right:0">• 无代理方式采集Kubernetes pods和节点的信息</p> 
<p style="margin-left:0; margin-right:0">• 获取Kubernetes节点主机高水平信息</p> 
<p style="margin-left:0; margin-right:0">Kubernetes监控还能够监控Kubernetes组件，例如</p> 
<p style="margin-left:0; margin-right:0">• kube-controller-manager</p> 
<p style="margin-left:0; margin-right:0">• kube-proxy</p> 
<p style="margin-left:0; margin-right:0">• kube-apiserver</p> 
<p style="margin-left:0; margin-right:0">• kube-scheduler</p> 
<p style="margin-left:0; margin-right:0">• kubelet</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">07</span> 详细高效的Zabbix审计日志模式</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/23b1a375-292f-416e-9d13-cac5e79d52fa.jpg" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">重新设计的审计日志能提供全新的详细信息，并优化筛选功能。</p> 
<p style="margin-left:0; margin-right:0">新的审计日志模式允许用户对Zabbix前端、Zabbix API和Zabbix server记录执行详细审计。通过修改审计日志，对Zabbix实例执行的所有更改都将记录在审计日志中：</p> 
<p style="margin-left:0; margin-right:0">• 创建、修改或删除新对象</p> 
<p style="margin-left:0; margin-right:0">• 通过LLD发现新实体</p> 
<p style="margin-left:0; margin-right:0">• API命令</p> 
<p style="margin-left:0; margin-right:0">• 定期登录/退出</p> 
<p style="margin-left:0; margin-right:0">• Zabbix实例中发生的所有其它事情</p> 
<p style="margin-left:0; margin-right:0">新的审计日志模式在设计时考虑了最佳性能，因此扩展的功能不会影响Zabbix实例的性能。审计日志模式的工作是一项持续的工作，会在后续Zabbix发布周期中持续进行。</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">08</span> 可视化数据的新方法</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/bf143011-3429-405e-b998-036f1a82c3d9.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span>主机排序组件可显示按监控项值排序的前N个或后N个主机的列表</span></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">Zabbix 6.0新增的构件提供了展示信息的许多新方法。</p> 
<p style="margin-left:0; margin-right:0">• 地理地图构件能在地图上显示主机和问题</p> 
<p style="margin-left:0; margin-right:0">• 数据表构件能创建有关主机指标状态的摘要视图</p> 
<p style="margin-left:0; margin-right:0">• 数据表构件的前N和后N函数能展示最高或最低的监控项值</p> 
<p style="margin-left:0; margin-right:0">• 单一监控项构件能展示单个指标的值</p> 
<p style="margin-left:0; margin-right:0">• 对现有矢量图的许多改进，例如新的矢量图类型、引用单一监控项等</p> 
<p style="margin-left:0; margin-right:0">• SLA构件能显示特定业务服务的当前SLA</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">09</span> Zabbix性能优化</strong></p> 
<p style="margin-left:0; margin-right:0">针对不同的Zabbix组件进行多项性能优化：</p> 
<p style="margin-left:0; margin-right:0">• 提升链接模板时的性能</p> 
<p style="margin-left:0; margin-right:0">• 提升Zabbix proxy性能和内存使用率</p> 
<p style="margin-left:0; margin-right:0">历史数据表使用主键，这有多种好处，例如：</p> 
<p style="margin-left:0; margin-right:0">• 提高Zabbix server和Zabbix前端的性能</p> 
<p style="margin-left:0; margin-right:0">• 减少历史数据表的大小</p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">10</span> 提升Zabbix Agent2模块化， 新的Zabbix Agent 监控项和功能</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/ea86ae82-f3dc-4154-93d3-525159d5094b.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center">优化的Zabbix agent现在能够开箱即用监控一组指标</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">Zabbix 6.0为Zabbix Agent和Agent2提供了一套新的监控项。支持以下功能：</p> 
<p style="margin-left:0; margin-right:0">• 获取额外文件信息，如文件所有者和文件权限</p> 
<p style="margin-left:0; margin-right:0">• 采集agent主机元数据作为指标</p> 
<p style="margin-left:0; margin-right:0">• 计数匹配的TCP/UDP sockets</p> 
<p style="margin-left:0; margin-right:0">某些已有的监控项支持新的功能：</p> 
<p style="margin-left:0; margin-right:0">• vfs.fs.discovery-在Windows上添加了对&#123;#FSLABEL&#125;宏的支持</p> 
<p style="margin-left:0; margin-right:0">• vfs.fs.get-在Windows上添加了对&#123;#FSLABEL&#125;宏的支持</p> 
<p style="margin-left:0; margin-right:0">• vfs.file.size-添加了一个新的模式参数。设置以字节数或行数为单位</p> 
<p style="margin-left:0; margin-right:0">Zabbix Agent2现在支持加载独立插件，而无需重新编译Agent2。</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">11</span> 原生TLS/SSL网站证书监控</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/db42aacc-d595-4bd3-a21f-bf2fe3c0dc3e.jpg" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span>使用新的Zabbix agent2 监控项监控SSL/TLS证书</span></p> 
<p style="margin-left:0; margin-right:0">支持使用新的Zabbix agent 2监控项来监控SSL/TLS证书。监控项可用于验证TLS/SSL证书，并提供其它证书详细信息。</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">12</span> 通用性改进</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/a0c0d2e7-9276-410f-aed5-ff0ea2a92197.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span>通过优化的创建主机UI，使创建新主机从未如此简单</span></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">Zabbix 6.0使Zabbix配置工作流程更精简！Zabbix用户现在可直接在Monitoring页面创建主机和监控项：</p> 
<p style="margin-left:0; margin-right:0">• 直接从Monitoring -Hosts页面创建主机</p> 
<p style="margin-left:0; margin-right:0">• 直接从Monitoring -Latest data页面创建监控项</p> 
<p style="margin-left:0; margin-right:0">• 删除了Monitoring -Overview页面。为了改善用户体验，现在只能通过仪表盘构件访问触发器和数据概览功能。</p> 
<p style="margin-left:0; margin-right:0">现在将根据监控项的键值自动选择监控项的默认信息类型。</p> 
<p style="margin-left:0; margin-right:0">拓扑图标签和图形名称中的简单宏已替换为表达式宏，以确保与新的触发器表达式语法一致。</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#42689e"><strong>13 </strong></span><strong>通过自定义密码复杂程度要求来保护您的Zabbix登录</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/d8f204dc-cbaf-429d-a682-03555270cca4.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span>设置密码复杂程度确保前端登录安全</span></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">Zabbix超级管理员现在能够定义密码复杂程度要求。现在可以：</p> 
<p style="margin-left:0; margin-right:0">• 设置最小密码长度</p> 
<p style="margin-left:0; margin-right:0">• 定义密码字符要求</p> 
<p style="margin-left:0; margin-right:0">• 通过禁止使用最常见的密码字符串来降低字典攻击的风险。</p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">14</span>支持定制前端展示品牌logo</strong></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">定制Zabbix实例代表您的公司。将现有的Zabbix品牌和帮助页面URL替换为您自己的公司品牌和自定义网站URL。</p> 
<p style="margin-left:0; margin-right:0">改名功能不会违反Zabbix许可协议-可以自由更换Zabbix品牌！</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">15</span> 新增模板和集成</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/b7a576d8-c553-40dd-a337-9b0e10b101dc.jpg" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">Zabbix 6.0为最受欢迎的供应商提供了许多新模板：</p> 
<p style="margin-left:0; margin-right:0">• f5 BIG-IP</p> 
<p style="margin-left:0; margin-right:0">• Cisco ASAv</p> 
<p style="margin-left:0; margin-right:0">• HPE ProLiant servers</p> 
<p style="margin-left:0; margin-right:0">• Cloudflare</p> 
<p style="margin-left:0; margin-right:0">• InfluxDB</p> 
<p style="margin-left:0; margin-right:0">• Travis CI</p> 
<p style="margin-left:0; margin-right:0">• Dell PowerEdge</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">Zabbix 6.0还带来了一个新的Github webhook集成，能基于Zabbix问题或恢复事件生成Github问题！</p> 
<p style="margin-left:0; margin-right:0">所有官方的Zabbix模板现在都是独立的，不需要依赖导入其他模板。</p> 
<p style="margin-left:0; margin-right:0">请查看当前可用集成的完整列表。</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#42689e">16</span></strong></p> 
<p style="margin-left:0; margin-right:0"><strong>其它新功能和优化</strong></p> 
<p style="margin-left:0; margin-right:0">更多改进功能（部分）：</p> 
<p style="margin-left:0; margin-right:0">• 使用新聚合函数计数返回值或匹配监控项的数量-count和item_count函数</p> 
<p style="margin-left:0; margin-right:0">• 在未配置交换空间的情况下提升system.swap监控项行为</p> 
<p style="margin-left:0; margin-right:0">• 使用新的单调历史函数检测连续增加或减少的值</p> 
<p style="margin-left:0; margin-right:0">• 支持两个新的Prometheus预处理标签匹配运算符！= 及 !~</p> 
<p style="margin-left:0; margin-right:0">• 当从构件链接导航到列表样式页面时，构件显示能更可靠地转换为不同的筛选器选项</p> 
<p style="margin-left:0; margin-right:0">• 使用新配置参数ListenBacklog为Zabbix server、Zabbix proxy、Zabbix agent配置TCP队列中挂起连接的最大数量</p> 
<p style="margin-left:0; margin-right:0">• 文档页面字体和可读性的改进</p> 
<p style="margin-left:0; margin-right:0">• 调整许多现有模板和修复小bug</p> 
<p style="margin-left:0; margin-right:0">• 新增utf8mb4作为受支持的MySQL字符集和校对集</p> 
<p style="margin-left:0; margin-right:0">• 新增对Webhook的额外HTTP方法的支持</p> 
<p style="margin-left:0; margin-right:0">• 对Zabbix命令行工具的超时设置</p> 
<p style="color:#000000; margin-left:0; margin-right:0">想了解更多，欢迎查看官网 升级体验 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zabbix.com%2Fcn%2Fwhats_new_6_0" target="_blank">https://www.zabbix.com/cn/whats_new_6_0</a>。</p>
                                        </div>
                                      
</div>
            