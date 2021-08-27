
---
title: 'MeterSphere 开源持续测试平台 v1.12.0 发布，增加消息通知，支持 TCP 协议 Mock 服务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f0a6233cb1f4a65b8b2427bb8ab61757b78.png'
author: 开源中国
comments: false
date: Fri, 27 Aug 2021 12:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f0a6233cb1f4a65b8b2427bb8ab61757b78.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://oscimg.oschina.net/oscnet/up-f0a6233cb1f4a65b8b2427bb8ab61757b78.png" referrerpolicy="no-referrer"></p> 
<p>8月26日，MeterSphere一站式开源持续测试平台正式发布v1.12.0版本。</p> 
<p><span style="color:null">在这一版本中我们<strong>新增了消息中心功能</strong>，并支持对更多事件类型进行通知；测试跟踪中的<strong>测试计划报告进行了整体优化</strong>，可以更加完整、直观地展现整个测试计划的执行情况；在接口测试方面，v1.12版本<strong>新增了TCP协议的Mock功能</strong>，并对接口定义相关功能页面进行了布局优化，让用户使用起来更加清晰直观；除此之外，我们还对性能测试的数据处理方式进行了优化，以便<strong>更好地支持高并发场景下的性能测试</strong>。</span></p> 
<h2>新增功能</h2> 
<p><span style="color:#783887">■</span><span style="color:#783887"><strong> 优化完善消息通知，新增消息中心功能</strong></span></p> 
<p>MeterSphere v1.12.0版本在消息通知配置中新增了站内通知类型的接收方式，用户可以点击系统右上角的消息中心查看相关通知内容。同时在该版本中我们还支持对更多的事件类型进行通知，例如新建、更新接口定义等。所有事件目前均支持站内通知、邮件、钉钉机器人、企业微信机器人及飞书机器人多种通知方式，用户可根据自身需求自由选择。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-778b0aaa7a327df0bca29f3544602815922.png" referrerpolicy="no-referrer"></p> 
<p><span style="color:#783887">■ </span><span style="color:#783887"><strong>测试计划报告优化，支持导出HTML报告</strong></span></p> 
<p><span style="color:null">MeterSphere v1.12.0版本对测试计划报告进行了重构，用户可以在测试计划报告中更加完整、直观地查看到整个测试计划的执行结果，包括接口测试的详细请求响应内容、性能测试的报告等。此外，v1.12.0版本的报告导出功能改为了<strong>使用HTML格式</strong>而非之前的PDF格式，导出的报告与页面查看报告体验一致。同时增加了报告分享功能，<strong>通过分享得到的链接可以无需登录直接查看报告内容</strong>。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1b596b696ce3798b6b0fcf45c7e1a17f539.png" referrerpolicy="no-referrer"></p> 
<p><span style="color:#783887">■ </span><span style="color:#783887"><strong>支持TCP协议Mock服务</strong></span></p> 
<p>与HTTP接口的Mock服务功能类似，在MeterSphere v1.12.0版本中TCP协议接口也支持配置Mock了。TCP接口Mock功能采用每个项目配置一个TCP监听端口的方式，在访问该端口的请求内容与接口Mock配置中的期望匹配时，即可返回对应的响应内容。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-89f79bfacb54045e5f6dfaa6087134c3dca.png" referrerpolicy="no-referrer"></p> 
<p><span style="color:#783887"><strong>■ 高并发性能测试优化</strong></span></p> 
<p>之前版本的MeterSphere使用了JMeter的Kafka Backend Listener插件来完成对测试结果的收集，并通过DataStreaming节点进行汇总及后续的结果计算和处理。当整个测试的节点较多，单节点TPS较大时，Kafka集群及DataStreaming节点容易成为整个系统的瓶颈，影响测试结果的准确性及实时性。</p> 
<p><span style="color:null">MeterSphere v1.12.0版本中针对性能测试增加了不使用Backend Listener的方案，各个压测节点启动JMeter后由各节点上的额外进程负责实时处理本地JMeter产生的结果数据，生成性能测试报告中的各项指标后上传到指定的Kafka Topic中，再由DataStreaming对各个节点的数据进行汇总。与之前方案相比，原本DataStreaming需要承载的计算汇总结果的压力被分散到各个独立的压测节点上，每个压测节点的压力较之前有所增加，但整体上对并发量较大情况下的结果处理能力大大提升。本次优化后，<strong>我们已经在实测中达到100万+TPS（Transactions Per Second）</strong>，如下图所示。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0e178c00e7554c4b309319f24561f33f440.png" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，MeterSphere v1.12.0版本还包含很多其他功能更新和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</p> 
<h2>功能优化</h2> 
<p><span style="color:#783887">■ </span>测试跟踪：测试计划场景用例列表增加环境列；</p> 
<p><span style="color:#783887">■ </span>测试跟踪：测试计划接口用例列表增加环境列；</p> 
<p><span style="color:#783887">■ </span>测试跟踪：测试计划接口用例批量执行可选环境；</p> 
<p><span style="color:#783887">■ </span>测试跟踪：测试用例导入模版优化；</p> 
<p><span style="color:#783887">■ </span>测试跟踪：测试用例支持导出XMind文件；</p> 
<p><span style="color:#783887">■ </span>测试跟踪：场景用例批量执行可选环境；</p> 
<p><span style="color:#783887">■ </span>测试跟踪：计划列表增加执行按钮；</p> 
<p><span style="color:#783887">■ </span>测试跟踪：测试计划支持复制；</p> 
<p><span style="color:#783887">■ </span>接口测试：调试、执行接口用例和场景用例时支持手动停止；</p> 
<p><span style="color:#783887">■ </span>接口测试：环境配置通用配置增加超时时间配置；</p> 
<p><span style="color:#783887">■ </span>接口测试：接口定义和接口Case高级搜索中提供已被场景引用的筛选条件；</p> 
<p><span style="color:#783887">■ </span>接口测试：接口定义支持全局环境设置；</p> 
<p><span style="color:#783887">■ </span>接口测试：接口用例及场景用例支持查看执行、调试历史；</p> 
<p><span style="color:#783887">■ </span>接口测试：接口自动化报告增加结束时间；</p> 
<p><span style="color:#783887">■ </span>接口测试：结果中增加断言名称显示；</p> 
<p><span style="color:#783887">■ </span>接口测试：优化接口类型/请求路径变更时用例同步变更；</p> 
<p><span style="color:#783887">■ </span>性能测试：资源池节点添加时默认端口和并发数；</p> 
<p><span style="color:#783887">■ </span>系统设置及其他：切换组织/工作空间/项目时添加Loading；</p> 
<p><span style="color:#783887">■ </span>系统设置及其他：添加成员时可根据ID或Name过滤选项；</p> 
<p><span style="color:#783887">■ </span>系统设置及其他：用户列表搜索改为按照ID/名称搜索；</p> 
<p><span style="color:#783887">■ </span>系统设置及其他：优化用户组列表排序。</p> 
<h2>Bug修复</h2> 
<p><span style="color:#783887">■ </span>fix（接口定义）：修复执行接口定义相关优化问题；</p> 
<p><span style="color:#783887">■ </span>fix（接口定义）：用例执行刷新优化；</p> 
<p><span style="color:#783887">■ </span>fix（接口自动化）：SQL请求执行失败结果不显示问题；</p> 
<p><span style="color:#783887">■ </span>fix（接口自动化）：优化同一个场景只能打开一个Tab的问题；</p> 
<p><span style="color:#783887">■ </span>fix（接口自动化）：修复场景导入模式默认值选择问题；</p> 
<p><span style="color:#783887">■ </span>fix（接口自动化）：修复导入场景数据缺失问题；</p> 
<p><span style="color:#783887">■ </span>fix（接口自动化）：导入JMX TCP协议处理问题修复；</p> 
<p><span style="color:#783887">■ </span>fix（接口自动化）：执行序列号显示NAN问题修复；</p> 
<p><span style="color:#783887">■ </span>fix（性能测试）：修复保存并执行后台接口修改导致的Bug；</p> 
<p><span style="color:#783887">■ </span>fix（接口测试首页）：修复删除场景报告，影响到首页历史总执行次数的缺陷 #1005966；</p> 
<p><span style="color:#783887">■ </span>fix（测试报告）：修复运行中的测试报告打开过慢的问题；</p> 
<p><span style="color:#783887">■ </span>fix（测试用例）：修复未获取Jira全部需求的问题；</p> 
<p><span style="color:#783887">■ </span>fix：修复接口执行空指针异常的问题；</p> 
<p><span style="color:#783887">■ </span>fix：用例名称列宽调整#1005639。</p>
                                        </div>
                                      
</div>
            