
---
title: '支持 Apache Impala，DataEase 开源数据可视化分析平台 v1.9.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fd81f5c2748383a33c023cf2a0a7d1b008a.png'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 05:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fd81f5c2748383a33c023cf2a0a7d1b008a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="678" src="https://oscimg.oschina.net/oscnet/up-fd81f5c2748383a33c023cf2a0a7d1b008a.png" width="1698" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">4月11日，DataEase开源数据可视化分析平台正式发布v1.9.0版本。在这一版本中，DataEase平台新增了对Apache Impala数据源的支持；仪表板方面，用户可以直接在仪表板页面对指定的视图进行相关设置，新增网页组件和流媒体组件；视图方面，增加高级选项支持，部分视图已添加阈值相关设置支持；X-Pack增强功能方面，行权限支持内置系统变量，可以更方便地对数据进行权限控制。另外，我们还对其他一些常用的功能进行了功能优化和问题修复。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#0a7be0">■ 新增Apache Impala数据源支持</span></strong></p> 
<p style="margin-left:0; margin-right:0">Impala是Apache旗下的开源项目，它提供SQL语义，能够查询存储在Hadoop的HDFS和HBase中的PB级大数据。已有的Hive系统虽然也提供了SQL语义，但由于Hive底层执行使用的是MapReduce引擎，仍然是一个批处理过程，难以满足查询的交互性。相比之下，Impala的最大特点兼卖点就是它的快速响应能力。</p> 
<p style="margin-left:0; margin-right:0">在v1.9.0版本中，DataEase新增Apache Impala数据源，用户可以将Impala相关连接信息加入到DataEase数据源中，在DataEase里对Impala数据进行展示和分析。</p> 
<p><img alt height="666" src="https://oscimg.oschina.net/oscnet/up-c6453a048df4da4d31c55757f05ff56380f.png" width="1280" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#0a7be0">■ 视图组件增加阈值相关功能</span></strong></p> 
<p style="margin-left:0; margin-right:0">一般在数据分析时可将数据与特定阈值进行对比分析，通过数据的对比来清晰准确地反映数据所处状态。在DataEase v1.9.0版本中，我们对部分视图类型增加了高级设置功能，其中包含了折线图、柱状图的辅助线设置，以及仪表盘的阈值区间设置的支持。</p> 
<p><img alt height="666" src="https://oscimg.oschina.net/oscnet/up-9f4872bb9be1da651068c9056fcef531359.png" width="1280" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0a7be0">■ 支持多种安装运行模式</span></strong></p> 
<p style="margin-left:0; margin-right:0">在v1.9.0版本之前，DataEase标准安装默认会部署运行DataEase、MySQL、Kettle、Apache Doris FE、Apache Doris BE五个组件。对于部分用户来说，他们需要分析和展示的数据量并不太大，Kettle和Apache Doris组件在此种场景下就显得不那么必要了；对于某些数据量特别大的用户来说，标准安装里以容器方式运行的Kettle和Apache Doris，又不能充分地提供用户所需的数据处理性能。</p> 
<p style="margin-left:0; margin-right:0">从v1.9.0版本开始，DataEase提供三种安装运行模式，分别是精简模式、本地模式和集群模式。</p> 
<p style="margin-left:0; margin-right:0">默认安装运行模式为精简模式，即仅启动DataEase和MySQL两个组件，但其依然可以提供API数据源和Excel数据集的使用支持；本地模式即为v1.9.0版本之前的默认安装方式，包含DataEase、MySQL、Kettle、Apache Doris FE、Apache Doris BE五个组件；集群模式则支持用户添加多个Kettle节点和Apache Doris集群的设置，以满足用户对处理性能的需求。</p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#0a7be0">■ 行权限支持内置系统变量（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">企业用户的数据在很多时候会带有企业的部门、用户的角色、邮箱等相关信息。在v1.9.0版本中，DataEase内置了对一些常见系统变量的支持，例如用户ID、用户名、用户邮箱、用户来源、用户角色、组织等。数据集的管理员可以在行权限中灵活地使用这些内置的系统变量，轻松快捷地实现不同的用户访问各自所属的数据资源。</p> 
<p><img alt height="605" src="https://oscimg.oschina.net/oscnet/up-e7235ba46c86c5144b419be8d25bff6cdae.png" width="1280" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，DataEase v1.9.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：仪表板模板创建的仪表板支持样式、模板数据的迁移；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■<span> </span></span>refactor（仪表板）：拥有移动端布局的仪表板在列表中增加区分标识；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>style（移动端）：移动端仪表板自适应屏幕；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（X-Pack）：关联数据集权限校验；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■<span> </span></span>refactor：记录各页面分割线的位置，刷新后不重置（#1390）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>perf：优化启动时，数据集初始化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor：清理官方仪表板未使用的视图；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor：缓存兼容Redis单机、哨兵和分片集群模式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor：加密公共链接中的用户ID（#1944）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor：增加公共链接密码强度（之前是4位随机数，现在是4位大小写字母和数字组成的随机字符串）。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#0a7be0">■</span> fix：修复Excel数据集新增字段后，无法追加数据的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复明细表数值排序会出现按文本顺序的问题（#1937）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：完善OIDC登录逻辑（1. OIDC用户不能使用默认密码以普通方式登录；2. OIDC用户登录后不会收到修改密码的提示）（#1939）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复移动端查看分享仪表板报权限错误的问题（#1891，#1935）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：升级有安全漏洞的MySQL驱动，从8.0.16升级至8.0.28；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复API数据集增量同步的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复关联数据集不支持API数据集的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复选项卡切换后过滤条件无效的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复仪表板导出为PDF后边框样式的问题（#1985）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复组件设置背景后其他的组件当时也能看到该图片的问题（#1986）。</p>
                                        </div>
                                      
</div>
            