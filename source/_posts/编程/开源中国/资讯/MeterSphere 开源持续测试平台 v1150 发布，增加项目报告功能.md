
---
title: 'MeterSphere 开源持续测试平台 v1.15.0 发布，增加项目报告功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-494e781ffb90f51a3eb5364f4badaae58a1.png'
author: 开源中国
comments: false
date: Fri, 26 Nov 2021 14:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-494e781ffb90f51a3eb5364f4badaae58a1.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="816" src="https://oscimg.oschina.net/oscnet/up-494e781ffb90f51a3eb5364f4badaae58a1.png" width="1696" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">11月25日，MeterSphere一站式开源持续测试平台正式发布v1.15.0版本。</p> 
<p style="margin-left:0; margin-right:0">在这一版本中，我们新增了<strong><span style="color:#783887">项目报告（X-Pack）</span></strong>，用户可以自由组合已有报表创建报告，并通过邮件方式发送给指定用户；缺陷管理方面，<span style="color:#783887"><strong>增加了TAPD、Jira及禅道平台的双向同步</strong></span>；除此之外，我们还针对接口测试功能<strong><span style="color:#783887">增加了文档结构的断言规则</span></strong>，<span style="color:#783887"><strong>针对性能测试增加了更多的压力分配策略选择</strong></span>。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#783887">■ 项目报告（X-Pack）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在MeterSphere v1.15.0版本的报表统计功能模块中，新增了项目报告功能。通过该功能，用户可以对已有的项目内报表进行自由组合，并添加额外的富文本内容，生成整个项目的完整分析报告。目前，项目报告支持以邮件的方式发送给指定的用户及用户组，后续版本将在此基础上增加定时发送、导出等实用功能。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-43af260507bfcbf7b57b06e957fa14a0165.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ 缺陷双向同步（X-Pack，支持TAPD、Jira、禅道平台）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在之前的版本中，MeterSphere支持了与TAPD、Jira、禅道、Azure DevOps等平台进行对接，可以将在MeterSphere上创建的缺陷同步到对应的平台上，但是无法将对应平台上的已有缺陷同步到MeterSphere中。在v1.15.0版本中，我们针对TAPD、Jira及禅道平台增加了缺陷双向同步的功能，用户在上述平台上的已有缺陷也可以直接同步到MeterSphere平台中。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-6386e40c10931748b2b4f63a66fa719f839.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ 断言规则支持文档校验</span></strong></p> 
<p style="margin-left:0; margin-right:0">接口测试方面，v1.15.0版本针对JSON、XML这两种比较常见的结构化响应格式，提供了文档校验方式的断言规则。用户可以导入一段已有的JSON、XML内容，或者使用在接口定义中已经添加好的响应内容，针对响应体中的每个字段逐一添加校验规则。如果在接口定义中有维护响应内容字段的高级配置项，例如字符串长度的区间范围等，系统还将根据该信息自动添加对应的校验规则。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-d4921ae06289140a43f0bc07d374d6ee303.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ 性能测试支持多种压力配置策略</span></strong></p> 
<p style="margin-left:0; margin-right:0">为了提供更灵活的压力分配，新版本中针对每个线程组增加了压力分配策略的配置功能。目前提供了自动分配、固定节点及自定义三种分配策略。自动分配策略即为之前版本的分配策略，线程组会按照资源池节点配置的最大并发数，按比例进行并发用户数的拆分；固定节点策略允许用户指定资源池中的某个节点，使用该策略的线程组只运行在选定节点之上；自定义策略需要用户手动指定每个节点上的并发数占比。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-7fe19638008fded969068fbb9c7f109207b.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><span>除了上述提到的新增功能外，MeterSphere v1.15.0版本还包含很多其他功能更新和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</span></p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 测试跟踪：测试计划测试阶段支持添加选项；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 测试跟踪：用例脑图模式支持操作模块；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 测试跟踪：用例脑图模式支持创建、关联缺陷；</p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#783887">■ </span></strong>测试跟踪：测试计划报告新增高级搜索功能；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 测试跟踪：测试计划添加性能测试，支持重新配置高级配置；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>接口测试：POST请求参数增加编码设置；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 接口测试：增加环境组概念，支持将多个项目中的环境配置进行组合；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>接口测试：测试报告可以查看断言脚本内容；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>性能测试：优化压力配置页面布局及样式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 性能测试：优化多节点日志页面；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 性能测试：测试报告显示压力配置页面；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>性能测试：优化性能测试报告列表页面；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>系统设置及其他：优化关注功能交互方式，提供专门的关注按钮；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>系统设置及其他：个人信息页面优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>系统设置及其他：变更历史及保存按钮修改为悬浮模式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>系统设置及其他：优化环境编辑页面；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 系统设置及其他：项目设置新增用户组与权限；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 系统设置及其他：工作空间成员支持批量添加到项目；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 系统设置及其他：批量添加到工作空间可以指定用户组；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>系统设置及其他：批量添加到项目可以指定用户组；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>系统设置及其他：左侧菜单增加一键收起功能（包含功能用例、测试计划、用例评审、测试计划报告-接口用例统计分析、接口定义、接口自动化、场景全屏编辑）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 系统设置及其他：后台日志中记录接口调用；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>系统设置及其他：错误日志输出到日志文件，而非系统标准输出。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试计划）：计划场景串行按照顺序执行；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（X-Pack）：修复“我的工作台”权限问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（个人信息）：设定新旧密码不能相同；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（性能测试）：修复性能测试中重复名称的提示；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（性能测试）：修复查询已结束的报告时日志下拉框没有备选资源池的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（性能测试）：修复测试计划中性能测试批量添加监控时页面卡死的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（性能测试）：查看测试报告报错修改；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（报表统计）：修复已保存过的报表点击会报错的缺陷；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（报表统计）：修复项目无法正常进入页面的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口定义）：修复JMeter导入会生成一个空白模块的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口定义）：修复右上角运行环境下拉框无法点击的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口测试）：修复用例执行结果不实时同步的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（接口测试）：修复跟随API定义对Array类型处理的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口测试）：修复接口名称过长时、长度小于100时执行接口Test一直转圈的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口测试）：接口定义中环境选择框优化显示样式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口自动化）：解决场景导入显示ID失败页面报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口自动化）：解决编辑页面报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（权限设置）：修复顶部菜单报表统计权限设置的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试用例）：修复测试用例上传附件不能传txt文件的的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试计划）：修复因全局后置脚本导致的接口案例一直执行不结束的缺陷；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：报告高级搜索条件触发方式优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：测试计划关联性能测试时优化为显示ID列；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（环境设置）：修复环境设置时超时时间不能点加减号的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（系统设置）：修复切换项目时没有刷新顶部菜单的Bug；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（系统设置）：修复默认模版Title编辑状态的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix（配额管理）：修复接口测试没有验证配额的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复更新测试计划时，连续点击更新发送多条消息的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复TAPD提缺陷图片无法显示的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复性能测试自定义监控显示图表Bug（#7187）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复测试计划执行性能测试时trigger_mode对应不上的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复测试计划执行性能测试时资源池没有设置成功的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复接口定义页面前端报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复接口导入MS格式标签未被覆盖的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：解决“我创建的用例”查询错误的问题。</p>
                                        </div>
                                      
</div>
            