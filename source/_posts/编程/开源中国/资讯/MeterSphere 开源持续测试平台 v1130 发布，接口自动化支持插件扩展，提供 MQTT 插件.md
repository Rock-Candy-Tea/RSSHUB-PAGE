
---
title: 'MeterSphere 开源持续测试平台 v1.13.0 发布，接口自动化支持插件扩展，提供 MQTT 插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b417bfca3524263a0c01821a91c747a7a58.png'
author: 开源中国
comments: false
date: Fri, 24 Sep 2021 10:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b417bfca3524263a0c01821a91c747a7a58.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="276" src="https://oscimg.oschina.net/oscnet/up-b417bfca3524263a0c01821a91c747a7a58.png" width="610" referrerpolicy="no-referrer"></p> 
<p>9月23日，MeterSphere一站式开源持续测试平台正式发布v1.13.0版本。</p> 
<p style="margin-left:0; margin-right:0">在这一版本中<span style="color:#783887"><strong>接口自动化支持了插件式扩展</strong></span>，并同时提供了<span style="color:#783887"><strong>Debug插件及MQTT协议插件（X-Pack）</strong></span>供大家使用；同时我们在接口测试的前后置脚本及自定义脚本中，<span style="color:#783887"><strong>增加了自定义代码片段的引用</strong></span>，用户可以将常用的脚本保存并在多处复用；除此之外，针对报表统计功能，<span style="color:#783887"><strong>我们增加了测试用例统计和测试用例趋势报表</strong></span>。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span style="color:#783887"><strong> 接口自动化支持插件扩展</strong></span></p> 
<p style="margin-left:0; margin-right:0">MeterSphere v1.13.0版本针对接口自动化支持了插件式扩展功能，用户在插件管理页面上传可用插件后，就可以在创建接口自动化场景时添加对应的步骤。伴随新增的插件管理功能，我们同时提供了Debug插件及MQTT协议插件（X-Pack）供大家使用。通过Debug插件用户可以添加Debug请求，查看执行过程中的变量值；通过MQTT插件，用户可以配置MQTT连接信息，发送或接收MQTT消息。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-a4aaf3f051bacd58ebbcb775a22677fa89b.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-716665d438c8974d954baea2ca0cdf07d38.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><span style="color:#783887">■ <strong>优化接口测试脚本模板，支持自定义代码片段</strong></span></p> 
<p style="margin-left:0; margin-right:0">在接口自动化中经常需要添加前后置脚本及自定义脚本，通过新增的自定义代码片段功能，用户可以保存常用的脚本，在需要使用的地方直接添加；同时在v1.13.0版本中，我们对添加脚本界面的模板引用进行了更加清晰的分类展示，并增加了发起接口测试相关的新模板供大家选择。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-f1efc6f4a8b6a603d5b025f1f46c7d718b3.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><span style="color:#783887">■ <strong>报表统计优化</strong></span></p> 
<p style="margin-left:0; margin-right:0">MeterSphere v1.13.0版本针对报表统计功能增加了新的测试用例统计报表。在用例统计报表中，用户可以根据创建人、用例状态、用例等级等维度对不同类型的测试用例进行统计。同时，本版本还支持将当前的统计选项进行保存或导出当前报表。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-0182267ee8ba26d49cfbe61c20ae64980e2.png" width="2560" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ <strong>接口测试自动生成测试用例数据（X-Pack）</strong></span></p> 
<p style="margin-left:0; margin-right:0">针对请求体为JSON格式的HTTP接口，MeterSphere v1.13.0版本提供了自动生成测试用例数据的功能。系统会根据JSON请求体的字段配置自动生成一组测试用例数据填充到请求体当中，便于用户构造随机用例数据。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-eeaae97abc1ab274e1b456b9542240f1bf3.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，MeterSphere v1.13.0版本还包含很多其他功能更新和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor（性能测试）：数据表里添加索引；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor（性能测试）：监控显示优化（#6152）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor（测试用例）：关联测试页面增加高级搜索（#1002993）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor（测试用例）：添加预览列（#1002986）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：环境配置-创建环境优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：功能测试用例中添加评论的编辑框调整为和用例评审中的评论编辑框一致；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：Swagger导入<em>body</em>参数的顺序不变；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：导入页面添加覆盖模式的说明（#1002975）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：执行接口用例通知跳转；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：批量添加资源池节点；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：接口用例和场景用例导入时判断ID是否存在；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：测试用例支持拖拽调整顺序代码优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：测试计划关联页添加高级搜索（#1002978）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：缺陷复制优化后，可以复制不是当前模板平台的用例；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：请求头增加描述；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>refactor：默认模块改为未规划的模块；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>style（接口定义）：任务中心样式优化。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（JSON-SCHEMA）：修复当接口参数中有空值时，运行json-schema，就会变成乱码的问题（#1006429）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（修复测试报表报错问题）：修复测试报表报错问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（功能案例XMind导出）：修复导出的测试用例XMind脑图没有优先级标签的问题（#1006333/GitHub#5823）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（性能测试）：修复后台查询监控空指针的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口测试）：修复导入接口定义时接口用例ID格式不正确的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口测试首页）：修复“接口测试-接口用例数量统计-已覆盖接口数”统计错误的问题，修复后将过滤已删除的接口用例（#1006467）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口用例）：修复接口用例创建性能测试失败、json-schema转换报错的问题</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口自动化）：修复添加认证报错问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口自动化）：修复导出接口场景（jmeter格式）时导出场景数量不正确的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口自动化）：修复使用两层事务控制器时，内层事务控制器下复制或引用的场景在报告中查看不了具体内容的问题（#1006462）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（查询历史报表报错的问题）：修复查询历史报表报错的问题，还原Log配置文件的设置；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（测试用例统计）：修复后，测试用例改成功能用例；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（测试计划）：解决点击“测试计划”列表更多操作时的操作报错问题（#5715）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（测试跟踪）：解决点击“测试计划”列表中的更多操作按钮进入测试计划导致的问题（#5701）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修改环境检查提示（#1002994）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复删除性能测试报告后依然被统计的问题 (#5698)；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复后，性能测试支持上传JavaScript资源文件；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复测试计划关联用例导入场景用例报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复高级搜索日期时间选择器未对齐的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复“系统设置”模块下操作日志界面，添加工作空间成员标题高亮可点击，但点击后无响应的问题。</p>
                                        </div>
                                      
</div>
            