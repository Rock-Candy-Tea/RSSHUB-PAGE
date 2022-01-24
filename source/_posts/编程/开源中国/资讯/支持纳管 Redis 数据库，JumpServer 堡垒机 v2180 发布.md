
---
title: '支持纳管 Redis 数据库，JumpServer 堡垒机 v2.18.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ab0fccc7b57518bd6079de96bded9d947e4.png'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 10:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ab0fccc7b57518bd6079de96bded9d947e4.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-ab0fccc7b57518bd6079de96bded9d947e4.png" width="1094" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">2022年1月24日，JumpServer开源堡垒机正式发布v2.18.0版本。在这一版本中，JumpServer新增支持纳管Redis数据库，支持查看、连接、操作和会话审计Kubernetes Pod，同时支持通过命令记录快速定位字符类会话录像。</p> 
<p style="margin-left:0; margin-right:0">X-Pack增强包方面，JumpServer支持对SQL Server数据库进行批量改密操作，支持对通过Web可视化方式连接的数据库进行SQL文件的导入和数据查询集的导出，同时支持管理员对资产、应用账号进行定时备份。工单系统方面，JumpServer支持复核人同意资产登录复核工单后对会话直接发起控制。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c"><strong>1. 支持纳管Redis数据库</strong></span></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.18.0版本中，数据库应用已支持对非关系型数据库Redis的添加、授权、连接以及会话审计。</p> 
<p style="margin-left:0; margin-right:0">Redis是一款开源、遵循BSD协议的高性能结构化存储中间件，可以满足目前企业大部分应用对于高性能数据存储的需求。同时，Redis也是NoSQL（Not Only SQL）数据库，即非关系型数据库的一种。<span>其内置了丰富的数据结构，例如字符串String、列表List、集合Set、散列Hash等，可以高效解决企业应用频繁读取数据库所带来的诸多问题。</span><span>基于对用户多种使用场景的综合考量，JumpServer在新版本中增加了对Redis数据库的纳管。</span></p> 
<p><img alt height="1642" src="https://oscimg.oschina.net/oscnet/up-b81efdbd9d5acbe8063e96901d25717fbb4.png" width="2876" referrerpolicy="no-referrer"></p> 
<p>                            ▲图1 在JumpServer中创建Redis数据库应用</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1640" src="https://oscimg.oschina.net/oscnet/up-84015cda4eb2ae0c340e0bb9617be16012d.png" width="2876" referrerpolicy="no-referrer"></p> 
<p>                                    ▲图2 创建Redis数据库应用授权</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1640" src="https://oscimg.oschina.net/oscnet/up-7f72026dc8c4a030fd0957570c4bda263a3.png" width="2876" referrerpolicy="no-referrer"></p> 
<p><span>                        ▲图3 在Web Terminal页面连接已授权的Redis数据库</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">2. 支持查看、连接和会话审计Kubernetes Pod</span></strong></p> 
<p style="margin-left:0; margin-right:0"><span>Kubernetes是一种可自动实施Linux容器操作的开源平台，它可以帮助用户省去应用容器化过程中的许多手动部署和扩展操作。也就是说，您可以将运行Linux容器的多组主机聚集在一起，由Kubernetes帮助您轻松、高效地管理这些集群。同时，这些集群还可以跨公有云、私有云或混合云部署主机。</span></p> 
<p style="margin-left:0; margin-right:0"><span>因此，对于要求快速扩展的云原生应用而言（例如借助Apache Kafka进行的实时数据流处理），Kubernetes是理想的托管平台。</span></p> 
<p style="margin-left:0; margin-right:0"><span>JumpServer早在v2.2.0版本中就已经支持对Kubernetes集群的管理、连接和会话审计。但是考虑到Kubernetes复杂的使用场景以及用户的实际需求，运维管理员只连接到集群是远远不够的。</span></p> 
<p style="margin-left:0; margin-right:0"><span>因此，在v2.18.0版本中，JumpServer新增支持查看、连接、命令过滤和会话审计Kubernetes Pod，以提升管理员和用户的使用便捷性。</span></p> 
<p style="margin-left:0; margin-right:0"><span>用户进入JumpServer的Web Terminal页面，可以看到左侧的应用授权树，所有授权的Kubernetes应用都将放置在“我的应用”→“组织名称”→“Cloud”→“Kubernetes”树节点之下。由于Kubernetes使用的特殊性，用户右击集群就可以进行直连；左击可以依次展开系统用户、Namespace、Pod和Container，左击“Container”便可以连接到容器进行操作。</span></p> 
<p><img alt height="1640" src="https://oscimg.oschina.net/oscnet/up-90e032232e2bbc686363dbc9740ef40b954.png" width="2876" referrerpolicy="no-referrer"></p> 
<p><span>                  ▲图4 在Web Terminal页面连接已授权的Kubernetes集群与容器</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">3. 支持通过选中命令来调整录像回放的起始时间（字符类会话录像）</span></strong></p> 
<p style="margin-left:0; margin-right:0"><span>在v2.17.0版本中，JumpServer就已经支持了通过鼠标及键盘事件快速定位Windows资产会话录像的播放位置。而在v2.18.0版本中，JumpServer新增支持对字符类会话录像的操作命令进行播放位置的跳转，这一改进可以极大地提升审计管理员对于用户操作行为的审查效率。</span></p> 
<p><img alt height="1640" src="https://oscimg.oschina.net/oscnet/up-c5f8e81189bca379464ac04f11a70e200cb.png" width="2876" referrerpolicy="no-referrer"></p> 
<p><span>                                             ▲图5 点击命令指定录像播放位置</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">4. 支持对资产、应用账号进行定时备份（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0"><span>为了防止不可控因素导致服务器出现异常，从而出现数据损坏、资源账号丢失等无法正常运营的情况，JumpServer v2.18.0版本在账号管理方面新增了账号备份功能，包括对资产账号、应用账号的备份，备份策略支持即时备份和定时备份两种策略。</span></p> 
<p><img alt height="1640" src="https://oscimg.oschina.net/oscnet/up-d6e2ba15eb1ded36f2ba983d385b9de7293.png" width="2876" referrerpolicy="no-referrer"></p> 
<p>                                                   ▲图6 账号备份</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1640" src="https://oscimg.oschina.net/oscnet/up-bf90be7117bc41125ae44219e2e74f1fd16.png" width="2876" referrerpolicy="no-referrer"></p> 
<p><span>                                             ▲图7 创建账号备份</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">5. 支持复核人审批同意资产登录复核工单后直接对会话发起控制（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0"><span>在v2.18.0版本中，对于登录资产复核工单，在审核人通过审批后，用户可以在工单详情页面直接对会话发起监控和终断操作。</span></p> 
<p><img alt height="1640" src="https://oscimg.oschina.net/oscnet/up-7dcbec3659a6de5f7f47a34037032b4c5ba.png" width="2876" referrerpolicy="no-referrer"></p> 
<p><span>                                          ▲图8 登录资产复核工单详情</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">6. 支持对SQL Server数据库进行批量改密（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0"><span>批量改密方面，JumpServer v2.18.0版本中新增了对SQL Server数据库的改密。目前JumpServer已经支持批量改密的数据库类型包括MySQL、Oracle、PostgreSQL、MariaDB和SQL Server。</span></p> 
<p><img alt height="1640" src="https://oscimg.oschina.net/oscnet/up-497bcbf065f57c977765c96fb3f7d598c9f.png" width="2876" referrerpolicy="no-referrer"></p> 
<p><span>                                               ▲图9 创建应用改密计划</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">7. 支持导入SQL文件和导出查询数据集（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0"><span>在JumpServer v2.18.0版本中，对于通过Web GUI方式连接的数据库，支持用户进行SQL文件的导入和数据查询集的导出，目前导出的文件格式支持CSV和XLSX两种格式。</span></p> 
<p><img alt height="1640" src="https://oscimg.oschina.net/oscnet/up-a16aed2b076320b6d972596d8eab0bd9485.png" width="2876" referrerpolicy="no-referrer"></p> 
<p>                                 ▲图10 Web GUI数据库导入SQL文件</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1640" src="https://oscimg.oschina.net/oscnet/up-56ad9ebb9dd8eaf2d9ab43d6d1149169104.png" width="2876" referrerpolicy="no-referrer"></p> 
<p>                                    ▲图11 Web GUI数据库查询数据</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1640" src="https://oscimg.oschina.net/oscnet/up-90fc3bbca958ba914fe42e6b145c3c16112.png" width="2876" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span>                             ▲图12 Web GUI数据库导出数据的查询集</span></p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化应用程序下载页面入口（Web Terminal页面）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>优化命令记录页面，增加显示执行命令的远端地址；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化RDP协议系统用户的用户名校验规则（支持输入特殊字符#%&~^）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化资产节点的创建，支持使用完整名称（通过API的创建方式）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化系统用户，支持填写自定义SSH Key passphrase；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化用户绑定第三方认证系统成功后，及时向用户发送相关消息通知，例如绑定企业微信、钉钉、飞书等；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化国际化问题（包括文件选择、任务名称、审计日志、Koko、文件管理页面等）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化工单信息，增加工单序列号的显示（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化青云私有云资产同步，支持自动解析API和使用自定义端口（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化应用授权，支持对Action进行控制（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化命令复核工单中显示解析后的完整命令（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 支持显示License中的Copyright信息（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>支持对Windows RemoteApp应用权限动作的单独控制，包括通过Web Terminal连接方式的文件上传、下载、复制、粘贴等（X-Pack增强包内）。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复在列表页面中，搜索框切换搜索字段后不能回车搜索的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复Celery异步任务中数据库连接数量会持续增加的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>修复删除用户失败的问题，解决“通过第三方模块创建的SSO Token信息提示包含关联对象，但实际已无关联对象”的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复用户即将过期提醒消息未发送的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复测试腾讯SMS平台验证码不通过的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复执行SQL命令时，光标移动可能会造成指令过滤匹配失败的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复强制启用用户MFA后，个人信息页面设置按钮被禁用的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复创建申请应用工单时点击“保存”按钮并继续添加后报错的问题（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复克隆应用授权规则失败的问题（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复云管中心同步资产报错后任务立即停止的问题（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复工单审批流程中复核人不能及时更新的问题（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复删除组织失败的问题，解决“提示包含关联对象，但实际已无关联对象”的问题（X-Pack增强包内）。</p>
                                        </div>
                                      
</div>
            