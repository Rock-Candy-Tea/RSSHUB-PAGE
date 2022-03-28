
---
title: '接口自动化场景优化，MeterSphere 开源持续测试平台 v1.19.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7aa013c204c8f97a0fc28cd30074dbaf9a4.png'
author: 开源中国
comments: false
date: Mon, 28 Mar 2022 11:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7aa013c204c8f97a0fc28cd30074dbaf9a4.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="638" src="https://oscimg.oschina.net/oscnet/up-7aa013c204c8f97a0fc28cd30074dbaf9a4.png" width="1498" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span>3月28日，MeterSphere一站式开源持续测试平台正式发布v1.19.0版本。</span></p> 
<p style="margin-left:0; margin-right:0"><span>在这一版本中，我们重点围绕接口测试模块的体验性和数据一致性进行了深度改善。首先，我们<span style="color:#783887"><strong>优化了接口自动化中场景编排的交互</strong></span>，使单个场景页面更加简单明了，降低用户交互的频次，提升用户体验；接口测试方面，<strong><span style="color:#783887">针对包含引用关系的接口自动化用例，涉及跨项目、跨工作空间导入导出时支持保留引用关系</span></strong>，从而保障数据的一致性，方便用户进行数据迁移等操作；在接口测试报告中，新版本的MeterSphere<strong><span style="color:#783887">增加了“未执行”用例的统计及分类展示</span></strong>，提升了整个测试报告的准确性；此外，在这一版本中，我们<span style="color:#783887"><strong>将工作空间中的“消息设置”与“模板管理”下沉至“项目设置”菜单</strong></span>，以满足用户项目维度的个性化配置需要。</span></p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#783887">■</span><span style="color:#783887"><strong> 接口自动化场景编排交互优化</strong></span></p> 
<p style="margin-left:0px; margin-right:0px">接口自动化场景编排功能作为MeterSphere的核心功能之一，一直是接口测试用户使用频率最高的功能。在MeterSphere v1.19.0版本中，我们主要从“提升编排效率”、“减少交互频次”两个方面对该功能进行了优化：</p> 
<p style="margin-left:0; margin-right:0">1. 将“基础信息”标签页移至左侧（原模块树位置）进行展示，进一步增加了右侧场景步骤的编排空间，便于以后对基础信息自定义字段的扩展。</p> 
<p><img alt height="1334" src="https://oscimg.oschina.net/oscnet/up-86b41e15efd8a2a08abe0d176dd2e9b2baa.png" width="2872" referrerpolicy="no-referrer"></p> 
<p><span>2. 请求参数增加“前置操作”（内含前置脚本、前置SQL）、“后置操作”（内含后置脚本、后置SQL、提取参数）和“断言规则”3个标签页，将请求关联的操作聚合在一个操作区域。</span></p> 
<p style="margin-left:0; margin-right:0"><span>经过对比，“给请求添加断言”这一操作由之前的4步提升至1步即可完成。同时，实现了请求参数和响应内容的一屏尽览，无需上下滑动及反复展开折叠操作，大大提升了场景编排的体验及效率。</span></p> 
<p><img alt height="1366" src="https://oscimg.oschina.net/oscnet/up-b1b143dd39618bc812b6a129f23e5988645.png" width="2878" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ 接口场景自动化跨项目导入支持保留引用关系</span></strong></p> 
<p style="margin-left:0; margin-right:0">随着用户对MeterSphere大规模的使用及推广，对于测试用例支持跨项目、跨工作空间，甚至跨服务的需求也随之而来。</p> 
<p style="margin-left:0; margin-right:0">为了更好地解决团队协作问题，在MeterSphere v1.19.0版本中，我们实现了在最为复杂的场景自动化用例下，能够在保留自身引用关系的同时进行数据的导入/导出，即使跨服务迁移数据也能保证数据的完整性和一致性。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1338" src="https://oscimg.oschina.net/oscnet/up-a9adda27ecc4c7f4bc443a768b3f42ce4f3.png" width="2878" referrerpolicy="no-referrer"></p> 
<p><img alt height="1340" src="https://oscimg.oschina.net/oscnet/up-8fa31a94ddf2105f59a9b6b262811f8c254.png" width="2876" referrerpolicy="no-referrer"></p> 
<p><img alt height="1350" src="https://oscimg.oschina.net/oscnet/up-1562d3378327b6da9fa330a04f9901c5409.png" width="2878" referrerpolicy="no-referrer"></p> 
<p><span style="color:#783887">■ </span><strong><span style="color:#783887">接口测试报告新增“未执行”类别展示</span></strong></p> 
<p style="margin-left:0; margin-right:0">MeterSphere在批量执行接口/场景用例过程中提供了是否“失败继续”的配置项，当用户配置了“失败不继续”则可能会产生“未执行”的请求。</p> 
<p style="margin-left:0; margin-right:0">在MeterSphere v1.19.0版本中，我们在报告统计里进一步细分了请求可能产生的全部执行状态，增加了“未执行”状态数据统计，同时在请求详情列表中增加了“未执行”分类，以展示所有未执行的请求供用户查看。</p> 
<p><img alt height="1372" src="https://oscimg.oschina.net/oscnet/up-9b5bc723ee1c5551d0c26c35b1544387968.png" width="2878" referrerpolicy="no-referrer"></p> 
<p><span style="color:#783887">■ <strong>支持项目维度的消息通知及应用模板配置</strong></span></p> 
<p style="margin-left:0; margin-right:0">在过往版本中，“消息设置”与“模板管理”一直是隶属于工作空间级别的。这样设计的初衷是，希望实现配置一次就能在整个工作空间范围内生效。但用户在实际使用过程中发现存在一些弊端，“消息通知”和“应用模板”的设计因项目/团队而异，共性较少，个性化居多。</p> 
<p style="margin-left:0; margin-right:0">在MeterSphere v1.19.0版本中，我们将“消息设置”页面与“模板管理”页面迁移至“项目设置”菜单内，满足了用户从项目维度进行个性化配置的需求，也更加全面地实现了项目间的隔离。</p> 
<p><img alt height="1384" src="https://oscimg.oschina.net/oscnet/up-2694d806c83987a4960edccf54e8a47426f.png" width="2878" referrerpolicy="no-referrer"></p> 
<p><img alt height="1370" src="https://oscimg.oschina.net/oscnet/up-e58e00563d4b6d4cd88d354fcea69770482.png" width="2878" referrerpolicy="no-referrer"></p> 
<h2>功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>测试跟踪：用例评审关联用例支持列表选择；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>测试跟踪：测试计划和用例评审页面优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>测试跟踪：测试计划中接口用例执行顺序与添加顺序保持一致；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>测试跟踪：缺陷管理删除缺陷增加了二次确认；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>接口测试：接口测试支持保存上一次选择的协议；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>接口测试：场景自动化报告统计优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>性能测试：性能测试列表操作新增执行按钮；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>性能测试：性能测试列表新增批量删除性能测试；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>项目设置：项目环境HTTP配置增加批量添加请求头功能；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>系统设置（X-Pack）：模块管理新增“我的工作台”启用开关；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>通用功能（X-Pack）：统一消息设置与定时任务通知的模板。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>fix（安全漏洞）：修复未授权XXE漏洞（使用SAXReader导致的未授权XXE攻击漏洞）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>fix（安全漏洞）：修复Prometheus未授权访问漏洞（Prometheus组件未授权访问导致的敏感信息泄漏）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>fix（安全漏洞）：修复getMdImage函数未授权调用的漏洞；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（测试跟踪）：修复测试跟踪的报告列表中，能够编辑但是不能保存的问题（GitHub #11636）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（测试跟踪）：修复测试计划中场景读取CSV的顺序和报告实际读取顺序不一致的问题（GitHub #11630）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（测试跟踪）：修复Track-Review中，Batch Unlink有时会导致SQLSyntaxErrorException的问题（GitHub #11342）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（测试跟踪）：修复在脑图模式下保存子节点为新模块时，出现报错的问题（GitHub #10347）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（接口测试）：修复Mock服务选择相应为XML格式时，version="1.0" encoding="UTF-8"无法修改或删除的问题（GitHub #11597）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（接口测试）：修复后置脚本批量执行多条SQL时报错的问题（GitHub #11564）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（接口测试）：解决v1.16.6升级到v1.18.3后，原有场景中的QUERY参数没有拼接到URL上的问题（GitHub #11687）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（接口测试）：修复JMeter里设置的断言规则和数量导入到MeterSphere后显示不正确的问题（GitHub #11700）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（接口测试）：修复接口责任人相关SQL错误的问题（GitHub #11607）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（接口测试）：修复接口测试执行无法正常结束的问题（GitHub #11197）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（接口测试）：修复了在循环控制器内嵌套另一个循环控制器后，每次外面的循环控制器再次循环时，里面的循环控制器的超时时间不是重置而是累加，保存场景也会报错的问题（GitHub #11628）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（接口测试）：修复运行Mock服务，配置的响应状态码和响应结果不起作用问题（GitHub #11609）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（性能测试）：修复脚本使用CSV分割多节点压测异常，每个节点目前都会从头开始重复取值CSV中的数据，通过数据库错误日志查看，同一值被重复多次调用的问题（GitHub #11235）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>fix（项目设置）：修复新的工作空间里没有项目，点击项目设置时弹出框报错的问题（GitHub #11603）。</p>
                                        </div>
                                      
</div>
            