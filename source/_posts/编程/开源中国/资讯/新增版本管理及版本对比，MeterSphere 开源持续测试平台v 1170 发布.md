
---
title: '新增版本管理及版本对比，MeterSphere 开源持续测试平台v 1.17.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-72fd4c7750c13a101d5f83989d8bbb7d68f.png'
author: 开源中国
comments: false
date: Thu, 27 Jan 2022 12:14:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-72fd4c7750c13a101d5f83989d8bbb7d68f.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="820" src="https://oscimg.oschina.net/oscnet/up-72fd4c7750c13a101d5f83989d8bbb7d68f.png" width="1694" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">2022年1月27日，MeterSphere一站式开源持续测试平台正式发布v1.17.0版本。</p> 
<p style="margin-left:0; margin-right:0">在这一版本中，我们新增了<span style="color:#783887"><strong>版本管理及版本对比相关功能（X-Pack）</strong></span>，用户可以为功能用例、接口定义、接口自动化场景及性能测试创建多个版本并进行对比；接口测试方面，<strong><span style="color:#783887">增加误报标记功能（X-Pack）</span></strong>，系统可以根据用户配置的误报匹配规则将特定结果的请求标记为误报状态；同时，针对长时间使用积攒了过多的测试报告，占用大量磁盘空间的情况，我们还<strong><span style="color:#783887">新增了测试报告定时清理功能</span></strong>。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#783887">■ 版本管理及版本对比（X-Pack）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在MeterSphere v1.17.0版本中，用户可以在“项目设置”菜单中的“版本管理”页面中选择是否启用版本管理功能，并在当前项目中新建版本或对已有的版本进行管理。在项目下启用版本管理功能后，便可以在功能用例、接口定义、接口自动化场景及性能测试的编辑页面中进行版本的切换、对比等操作。同时，在相应的列表中，用户也可以通过“版本切换”下拉框展示指定版本下的内容。</p> 
<p><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-47a803e53768f503995d885c6d87d698615.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><img alt height="1439" src="https://oscimg.oschina.net/oscnet/up-27b5422e96aa2f330cab4c3ac1645cbbd1f.png" width="2559" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ 接口测试结果增加误报标记（X-Pack）</span></strong></p> 
<p style="margin-left:0; margin-right:0">MeterSphere原有的接口测试请求结果只有成功及失败两种情况。但在实际测试场景中，测试人员可能会遇到一些因网络异常、环境未就绪等非应用原因导致的失败。针对这些特殊情况，MeterSphere v1.17.0版本增加了误报标记功能，用户可以根据自身需求配置自己的误报库规则，当请求结果与某条误报规则匹配时便会被标记为误报状态。</p> 
<p><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-4234b2cc462f2537939c26f24472c6c43f3.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-deed683ddbef91f2e353cd2063f82c0e9d2.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ 定时清理测试报告</span></strong></p> 
<p style="margin-left:0; margin-right:0">随着使用时间越来越长，接口测试、性能测试等在执行过程中产生的报告数据逐渐积累增多。如果用户没有及时清理的话，可能会导致磁盘空间不足、系统响应变慢等情况。在 MeterSphere v1.17.0版本中，用户可以在“项目设置”菜单下的“应用管理”页面，针对每个功能模块配置测试报告保留策略，超出指定保留时间的报告系统将自动清除。</p> 
<p><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-6628ccafcaac5eaae59ee277517fb0fa56d.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，MeterSphere v1.17.0版本还包含很多其他功能更新和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>测试跟踪：测试跟踪报告列表增加运行耗时和成功率字段显示；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>测试跟踪：优化“功能用例”页面性能；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>接口测试：接口定义及场景新增支持批量复制；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>接口测试：内置函数构造器优化，参数设置支持选择提取参数；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>接口测试：优化接口定义、接口用例、接口自动化场景查询效率；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>性能测试：支持上传SSL证书；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>性能测试：优化校验资源池时的超时时间问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>性能测试：重构性能测试解析JMX的方式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>性能测试：保存性能测试后不跳转到列表页面；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>性能测试：优化性能测试查询效率；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>系统设置及其他：后台日志保留天数可配置；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>系统设置及其他：LDAP用户邮箱属性为空时自动生成邮箱；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>系统设置及其他：项目设置中用户组与权限列表增加查看权限按钮；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>系统设置及其他（X-Pack）：优化单点登录重定向URL配置方式。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口测试）：修复接口场景最后一次执行失败的情况下，测试计划中的最后执行结果不显示的问题 ；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口测试）：修复Swagger导入Case为空的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口测试）：修复用例不选环境执行，结果状态就不更新的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口测试）：修复场景引用Postman导入用例显示错误的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：修复功能用例首页与模块统计不一致的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：修复复制的功能用例/接口定义的创建和更新时间是原用例的创建和更新时间的缺陷；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：修复启用自定义ID时脑图可重复导入相同ID的Bug；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：修复报告分享页面缺陷描述的预览不生效的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：修复统计用例数量不一致的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：修复Jira勾选模板缺陷图片显示相关的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：修复测试计划进度显示错误的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（项目报告）：修复项目报告无法选择当前日期的问题。</p>
                                        </div>
                                      
</div>
            