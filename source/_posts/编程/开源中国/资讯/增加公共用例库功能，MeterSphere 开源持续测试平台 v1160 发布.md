
---
title: '增加公共用例库功能，MeterSphere 开源持续测试平台 v1.16.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a2ba27a3e47ac705fb2ea9637df0bc70aa8.png'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 18:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a2ba27a3e47ac705fb2ea9637df0bc70aa8.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="818" src="https://oscimg.oschina.net/oscnet/up-a2ba27a3e47ac705fb2ea9637df0bc70aa8.png" width="1696" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">12月23日，MeterSphere一站式开源持续测试平台正式发布v1.16.0版本。</p> 
<p style="margin-left:0; margin-right:0">在这一版本中，我们新增了<strong><span style="color:#783887">公共用例库功能（X-Pack）</span></strong>，用户可以将部分功能用例添加到公共用例库中，位于公共用例库中的用例可以被工作空间下的其他项目所共享；针对上个版本发布的项目报告功能，新版本中支持了<strong><span style="color:#783887">项目报告的定时发送</span></strong>；除此之外，我们还针对<strong><span style="color:#783887">接口测试的执行及结果处理过程进行了重构优化</span></strong>，以解决批量执行过程中存在的各种问题。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887"><strong>■ 公共用例库（X-Pack）</strong></span></p> 
<p style="margin-left:0; margin-right:0">用户可以在测试跟踪模块选择项目中已有的功能用例，将其添加到公共用例库中。位于公共用例库中的用例，在整个工作空间下的所有项目中都可以看到，并且用户可以选择需要的用例复制到指定的项目中进行使用。</p> 
<p><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-88e489fdf20b1d289f2238b54b2eb8db6e2.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ 自动获取Jira缺陷模板</span></strong></p> 
<p style="margin-left:0; margin-right:0">在之前版本的MeterSphere中，用户可以通过自定义Jira缺陷模板的方式，将MeterSphere上提交的缺陷同步到Jira当中。但在配置过程中需要填写各种字段及选项值的ID等信息，配置一个完整的缺陷模板较为复杂。</p> 
<p style="margin-left:0; margin-right:0">针对这种情况，MeterSphere v1.16.0版本提供了自动获取Jira缺陷模板的功能，用户配置好Jira对接信息并开启该选项后，在创建缺陷时系统会通过Jira提供的API自动获取缺陷创建模板，不需要用户再一个字段一个字段地进行单独配置。</p> 
<p><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-e9379a920bd57de40c28f3951d03c9b12f0.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-355037b16c908f25328759c57e159e6f0df.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ 定时发送项目报告（X-Pack）</span></strong></p> 
<p style="margin-left:0; margin-right:0">针对上个大版本中新增的项目报告功能，这一版本的MeterSphere增加了项目报告的定时发送功能。用户在创建项目报告时，可以为其配置定时任务并进行周期发送，报告中的内容将根据发送时间动态更新。例如，报告中包含最近7天的缺陷统计图表时，报告发送时将以实际发送时间为截止时间进行统计。</p> 
<p><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-ec71593aa843ecb1731f2ed435582b90d14.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，MeterSphere v1.16.0版本还包含很多其他功能更新和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>测试跟踪：缺陷支持添加评论；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 测试跟踪：功能用例支持批量复制；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>测试跟踪：优化自定义模板布局及样式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>测试跟踪：功能用例列表增加最近结果列；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 测试跟踪：调整测试计划关联用例页面布局；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 测试跟踪：测试计划列表增加不同类型用例数量列；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>接口测试：测试执行及结果处理重构优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> 其他：更新JMeter至5.4.2版本，解决Log4j2漏洞问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>其他：优化消息通知模板，并增加固定的关键字“消息通知”；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>其他：优化任务中心样式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>其他：优化国际化翻译。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（Mock测试）：修复Mock测试自定义函数处理时，对Query参数中的JSON格式数据不支持的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（Mock测试）：解决Mock接口测试时部分Rest参数无法匹配的缺陷；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（场景自动化）：修复高级搜索问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（场景转性能测试）：场景转性能测试时去除Debug Sampler；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（性能测试）：修复性能测试多节点执行时页面卡在Starting的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口测试）：修复从接口自动化菜单跳转到测试报告菜单后，测试报告数据没有更新的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（接口测试）：修复接口用例在请求内容选择NO AUTH时报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（测试跟踪）：修复创建新的测试计划时会卡在“加载中”状态的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（消息通知）：模板增加跳转链接字段；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（系统设置）：修复新建项目后查看项目，用例模块只显示了Home页的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（项目报告）：项目报告展示优化，修复报表图片显示不全的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix（项目管理）：修复Jar包上传时，文件名过长上传报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：CSV下载接口可以访问到系统目录；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：Markdown图片上传接口支持匿名访问；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复order by sql注入的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复发送通知时没有获取到表里最新值的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复场景转换性能测试时名称长度过长的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复复制测试计划无消息通知的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复更新接口时通知信息不全的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复消息通知缺陷变量提示的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：去掉功能用例关联测试URL多余斜杠；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复测试用例无法展示关联缺陷的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：禅道path_info方式同步缺陷报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■ </span>fix：修复级联的自定义字段显示的是ID的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：优化脑图保存顺序；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复脑图编辑缺陷保存报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span> fix：修复部分缺陷不显示内容（扩充XSS白名单）的问题。</p> 
<h2 style="margin-left:0px; margin-right:0px">特别鸣谢</h2> 
<p style="margin-left:0; margin-right:0">感谢GitHub用户rainmanzzz反馈的若干安全漏洞。</p>
                                        </div>
                                      
</div>
            