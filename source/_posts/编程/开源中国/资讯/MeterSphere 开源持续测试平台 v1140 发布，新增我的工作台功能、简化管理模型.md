
---
title: 'MeterSphere 开源持续测试平台 v1.14.0 发布，新增我的工作台功能、简化管理模型'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6eafd9a4f13abf17e54d9e006030348b3eb.jpg'
author: 开源中国
comments: false
date: Thu, 28 Oct 2021 19:40:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6eafd9a4f13abf17e54d9e006030348b3eb.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0"><img alt height="951" src="https://oscimg.oschina.net/oscnet/up-6eafd9a4f13abf17e54d9e006030348b3eb.jpg" width="1092" referrerpolicy="no-referrer"></p> 
<p>10月28日，MeterSphere一站式开源持续测试平台正式发布v1.14.0版本。</p> 
<p style="margin-left:0; margin-right:0">在这一版本中我们<span style="color:#783887"><strong>新增了“我的工作台”功能（X-Pack）</strong></span>。当前工作空间下，与登录账号所属人相关的内容都会展示在我的工作台中。同时，对于功能用例、接口定义及接口自动化场景，我们<span style="color:#783887"><strong>增加了依赖关系设置功能</strong><strong>，并可以以拓扑图的方式展示依赖关系（X-Pack）</strong></span>；除此之外，我们还简化了系统的管理模型，优化了部分菜单页面，让<span style="color:#783887"><strong>设置管理类功能用起来更加顺手</strong></span>。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<h2 style="margin-left:0px; margin-right:0px"><span style="color:#783887">■ </span><span style="color:#783887"><strong>我的工作台（X-Pack）</strong></span></h2> 
<p style="margin-left:0; margin-right:0">新版本增加了“我的工作台”功能。系统将展示出，在当前工作空间中，与登录用户有关的所有项目的内容。通过该功能，用户可以很方便地聚焦到与自己相关的工作，包括待办任务、自己关注和创建的各种用例等等。同时，用户可以点击某个资源快速跳转到对应项目的对应功能菜单当中。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-f643ccd8cedbc1129df1933790b321a7608.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><span style="color:#783887">■ <strong>简化管理模型，优化系统菜单</strong></span></p> 
<p style="margin-left:0; margin-right:0">之前版本的MeterSphere采用了“组织”-“工作空间”-“项目”三层管理结构。在v1.14.0版本中，我们简化了管理模型，移除了“组织”相关的概念。原本需要在“组织”层级配置的服务集成、消息设置等功能下放到了“工作空间”层；同时，项目设置的相关功能迁移到了独立的一级菜单当中。</p> 
<p style="margin-left:0; margin-right:0">优化后的管理结构更加简洁清晰，不同层级的角色也可以更便捷地找到对应功能的入口。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-8aae16ad242ab73c9fc5979558c29a0a4a0.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><span style="color:#783887">■<strong> Mock服务优化</strong></span></p> 
<p style="margin-left:0; margin-right:0">新版本还对接口定义中的Mock功能进行了优化，匹配条件可以按不同的参数类型分别进行配置。当所有条件都可以成功匹配时，系统便会返回指定的响应内容。此外，在响应内容方面，我们新增了跟随API定义和自定义脚本两种返回内容格式，通过自定义脚本方式，用户还可以引用请求中的各种参数，更加灵活地构建期望的返回内容。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-eddad44b81c72f488567bcc8bc8ea8c5d83.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><span style="color:#783887">■ <strong>依赖关系设置及拓扑图展示（X-Pack）</strong></span></p> 
<p style="margin-left:0; margin-right:0">对于功能用例及接口定义功能，MeterSphere v1.14.0版本增加了依赖关系设置功能。用户可以在用例或接口编辑页面为其添加前置及后置对象；同时在X-Pack增强包当中，我们还增加了依赖关系的拓扑图展示功能，用户可以选择单个对象或批量选择多个对象，查看他们之间的拓扑<span>依赖</span>关系。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-8e559c9985e4f7e2712ba7e9df82bb34b6d.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-a3896a41768ebbfeaed278ea5f8bb1fbcc3.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，MeterSphere v1.14.0版本还包含很多其他功能更新和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<h2 style="margin-left:0px; margin-right:0px"><span style="color:#783887">■ </span>测试跟踪：用例评审及测试计划增加关注人；</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>测试跟踪：缺陷列表增加创建人筛选；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>接口测试：优化接口变量历史查看页面，变更显示格式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>接口测试：首页展示卡片可配置；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>接口测试：优化环境配置中的数据库连接配置；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>接口测试：创建场景时默认优先级设为P0；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>性能测试：压力配置持续时间时、分、秒可同时配置；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>性能测试：性能测试报告数据保留小数点后三位有效数字；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>系统设置及其他：消息通知模板增加可用变量提示（X-Pack）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>系统设置及其他：安装时默认打开MySQL Binlog记录。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<h2 style="margin-left:0px; margin-right:0px"><span style="color:#783887">■ </span>fix（接口定义）：优化前端生成接口数据中一些无效字段的问题；</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口定义）：修复SQL类型结果只显示一个的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口定义）：修复复制接口问题（GitHub #6815）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口定义）：修复附件名称显示问题（GitHub #6821）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口定义）：用例执行状态优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口测试）：删除项目时，级联删除接口测试相关资源；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口自动化）：修复SQL请求引用步骤执行问题（GitHub #6716）;</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口自动化）：修复调试场景中复制其他项目单接口用例时，环境匹配错误的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口自动化）：修复自定义脚本无法加入到条件控制器的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（报表统计）：调整报表统计的柱状图宽度；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口定义）：修复用例操作按钮权限问题，修复用例列表刷新问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（文件管理）：修复上传文件后，上传窗口没有关闭的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（模板管理）：修复自定义字段用例模板和缺陷模板采用相同的名称不能共存的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（测试用例）：修改组合查询条件中创建人字段；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（测试计划）：修复关联接口测试用例时，根据ID搜索测试用例不生效的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（测试跟踪）：修复功能用例关联接口用例时，显示的用例不是当前项目的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（缺陷管理）：修复弹出窗口不显示模块的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复不配置通知模板时，发送的消息内容和默认模板不一致的问题（GitHub #6630）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复后，当消息为0时，通知显示为0/0，而不是0/1（GitHub #5743）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：接口测试请求体中带文件时，部分情况下找不到文件的问题（GitHub #6987）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：去掉查询中的follow_people；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：处理引用问题 (#6886)；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复导入用户时密码规则和实际不一致的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复接口自动化定时任务和API调用发送通知操作人变量不能获取的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复测试计划负责人查询问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复测试计划通知Operator变量不能获取的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：测试评审用例自定义顺序；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：自定义代码片段，按创建时间排序报错。</p>
                                        </div>
                                      
</div>
            