
---
title: '新增 Mock 触发条件，MeterSphere 开源持续测试平台 v1.18.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f7a20a824f6d5d0b8cb2917687f2445c9ba.png'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 19:29:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f7a20a824f6d5d0b8cb2917687f2445c9ba.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="824" src="https://oscimg.oschina.net/oscnet/up-f7a20a824f6d5d0b8cb2917687f2445c9ba.png" width="1698" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">2月28日，MeterSphere一站式开源持续测试平台正式发布v1.18.0版本。</p> 
<p style="margin-left:0; margin-right:0">在这一版本中，我们主要对系统已有功能进行进一步的完善和优化。在测试跟踪模块中，<strong><span style="color:#783887">将测试计划关联缺陷与用例关联缺陷隔离</span></strong>，从而更加直观地反映测试计划的执行质量；在接口测试模块中，<strong><span style="color:#783887">批量执行单接口CASE支持生成集合报告</span></strong>；<strong><span style="color:#783887">Mock服务全新升级</span></strong>，在降低了匹配门槛的同时提升了Mock的灵活性；在性能测试模块中，<strong><span style="color:#783887">性能测试报告新增了分享报告功能</span></strong>，用户可以一键分享测试报告链接，并且支持用户自主设置链接的有效时长；在X-Pack增强包中， <span style="color:#783887"><strong>MQTT Sub新增单位时间内按接收数量结束消息订阅的功能</strong></span>。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#783887">■ Mock触发条件新增规则匹配与逻辑判断</span></strong></p> 
<p style="margin-left:0; margin-right:0">MeterSphere提供的Mock功能可以根据用户输入的请求参数、返回数据生成Mock接口，这些接口会自动生成模拟数据，以覆盖用户的一些测试需求。而Mock期望则是根据设置的请求触发条件来进行过滤，然后返回期望的数据。</p> 
<p style="margin-left:0; margin-right:0">在MeterSphere v1.18.0版本中，我们主要在请求触发条件这部分进行了调整：请求参数新增了规则匹配，可以根据参数设定的值、长度、正则表达式Mock出相应的请求参数，同时参数与参数之间新增了逻辑判断（AND/OR），以提升触发条件的灵活性。</p> 
<p><img alt height="1392" src="https://oscimg.oschina.net/oscnet/up-7e3fc90116681ab66cb79265d8e9b624d6d.png" width="2850" referrerpolicy="no-referrer"></p> 
<p>针对一些特定测试场景需要对返回信息进一步处理的情况，比如加解密操作、调用第三方JAR包等，MeterSphere在v1.18.0版本中Mock提供了对后置脚本的支持，用户可以通过编写脚本或添加系统已有的自定义代码片段来实现对返回信息的处理。</p> 
<p><img alt height="1394" src="https://oscimg.oschina.net/oscnet/up-696d88c5cd4d79ee0f494dd1a2e4dd62294.png" width="2852" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ 接口CASE支持生成集合报告</span></strong></p> 
<p style="margin-left:0; margin-right:0">在回归测试阶段，测试人员会通过批量执行接口CASE或场景自动化CASE来确保核心功能的稳定性。</p> 
<p style="margin-left:0; margin-right:0">自MeterSphere v1.12.0版本起，场景自动化在批量执行的模式下，MeterSphere可以提供“独立报告”和“集合报告”两种类型的报告形式供用户选择。在v1.18.0版本中，批量执行接口CASE也可以选择生成“独立报告”或“集合报告”了。集合报告将多个接口CASE整合到一个报告中，以方便用户使用，报告展示方式与场景自动化集合报告保持一致。</p> 
<p><img alt height="1390" src="https://oscimg.oschina.net/oscnet/up-2756cb4838986e007d990cba5fbaf1bc242.png" width="2848" referrerpolicy="no-referrer"></p> 
<p><img alt height="1358" src="https://oscimg.oschina.net/oscnet/up-c8d2e6bfc4270e2ed42c1e516d66a5f55b9.png" width="2874" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ 性能测试报告新增分享报告功能</span></strong></p> 
<p style="margin-left:0; margin-right:0">被测系统的性能评估往往需要研发、测试、运维多方参与。为了提升团队的协作能力，MeterSphere v1.18.0版本新增了性能测试报告分享功能。用户选择“性能测试”→“报告”，打开任一性能测试的报告页面，点击“分享报告”按钮，系统即会生成该报告对应的链接。接下来，点击“复制”按钮就可以分享给需要查看报告的用户。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9552d0cb90b6a1fdc8934fd686ae5ae19d4.png" referrerpolicy="no-referrer"></p> 
<p>性能测试报告的链接有效时长默认为24小时，用户可以选择“项目设置”→“应用管理”→“性能测试”，根据需要自定义该链接的有效时长。</p> 
<p><img alt height="872" src="https://oscimg.oschina.net/oscnet/up-19fe8360905f20c37daf2a9e3d1681a11cf.png" width="2878" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ MQTT Sub新增单位时间内按接收数量结束订阅（X-Pack）</span></strong></p> 
<p style="margin-left:0; margin-right:0">MeterSphere企业版已支持MQTT协议的接口自动化，v1.18.0版本主要针对MQTT协议测试的用户反馈的需求进行了功能上的优化。当MQTT Sub（订阅数据）结束接收的方式为“按持续时间（ms）”时，为了避免持续时间耗时过长，新增加了按接收数量来标识接收结束。</p> 
<p><img alt height="1272" src="https://oscimg.oschina.net/oscnet/up-909cf076effdc08de1da3943a6e166db71e.png" width="2878" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，MeterSphere v1.18.0版本还包含很多其他功能更新和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>测试跟踪：测试计划关联缺陷与用例关联缺陷隔离；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>测试跟踪：测试计划新增批量“开启/停止”定时任务；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>测试跟踪：测试报告支持修改报告名称；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>测试跟踪：测试用例关联需求支持模糊搜索；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>接口测试：接口自动化“复制/引用”场景支持配置是否启用原场景变量；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>接口测试：优化用例和场景批量执行；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>接口测试：优化接口自动化插件，支持联动；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>性能测试：修改性能测试报告页面报错的弹出框；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>系统设置及其他：个人信息中的邮箱支持修改；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>系统设置及其他：权限管理新增个人信息管控；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>系统设置及其他：全局前后置脚本新增变更历史；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>系统设置及其他：变更历史分表查询优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>系统设置及其他（X-Pack）：消息通知模板新增“通过率”和“运行时间”变量。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（接口测试）：修复Mock匹配设置不等于时匹配失误的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口测试）：修复Mock编辑页面不会随着浏览器窗口自动调整大小的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（性能测试）：修复性能测试变更历史JSON对比的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（性能测试）：修复性能测试分享报告下载详细日志报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试计划）：关联Dubbo接口用例时提示选择运行环境；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试计划）：定时任务开关提醒优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试计划）：优化测试计划定时任务权限问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：获取Jira模板时优先使用个人信息中的配置；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：修复首页失败用例TOP10所属测试计划跳转问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（系统设置）：修复环境组中的环境预览时，显示信息跟环境域名里不一致的问题。</p> 
<h2 style="margin-left:0px; margin-right:0px">特别鸣谢</h2> 
<p style="margin-left:0; margin-right:0">感谢深圳开源互联网安全技术有限公司反馈的若干安全漏洞。</p>
                                        </div>
                                      
</div>
            