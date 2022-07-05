
---
title: '开源里程碑_ 数据应用开发管理集成框架 DataSphere Studio 1.1.0 新版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic1.zhimg.com/80/v2-5154180a194e73bdd86b9e452faf09f0_720w.jpg'
author: 开源中国
comments: false
date: Tue, 05 Jul 2022 11:41:00 GMT
thumbnail: 'https://pic1.zhimg.com/80/v2-5154180a194e73bdd86b9e452faf09f0_720w.jpg'
---

<div>   
<div class="content">
                                                                                            <blockquote>
 DataSphereStudio1.1.0 是践行数据应用开发管理框架的里程碑，集成了 WeDataSphere 已开源的所有生态组件，并带来了一系列强大的全新特性，以及更加精简、易于对接的数据应用开发集成架构设计和实现。
</blockquote> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>DataSphere Studio 简介</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>DataSphere Studio（简称 DSS）是微众银行自研的数据应用开发管理集成框架。基于插拔式的集成框架设计，及计算中间件 Linkis ，可轻松接入上层各种数据应用系统，让数据开发变得简洁又易用。</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在统一的 UI 下，DataSphere Studio 以工作流式的图形化拖拽开发体验，将满足从数据交换、脱敏清洗、分析挖掘、质量检测、可视化展现、定时调度到数据输出应用等，数据应用开发全流程场景需求。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">DSS 通过插拔式的集成框架设计，让用户可以根据需要，简单快速替换 DSS 已集成的各种功能组件，或新增功能组件。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2FWeBankFinTech%2FDataSphereStudio" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>github.com/WeBankFinTec</span><span style="background-color:transparent; color:transparent">h/DataSphereStudio</span></a></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>DSS1.1.0 版本说明</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>DSS1.1.0 主要特性如下：</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- 已集成 WeDataSphere 已开源的所有生态组件，包括 Apache Linkis1.1.1、Exchangis1.0.0、Schedulis0.7.0、Qualitis0.9.2、Visualis1.0.0、Streamis0.2.0 和 Prophecis0.3.2。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- 集成了 Apache DolphinScheduler1.3.X。支持将 DSS 工作流一键发布为 DolphinScheduler 工作流，为工作流调度设计并开发了全新的调度中心。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- 用户体验优化。如支持换肤、顶部导航栏改版、DSS 开发中心改版等。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- 帮助手册和新手指引。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- 安装部署优化。进一步简化 DSS&Linkis 全家桶一键安装部署流程，让 DSS 和 Linkis 的安装在半个小时内完成。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- 支持优雅升级。提供了如何从DSS1.0.1升级到DSS1.1.0，以及DSS0.9如何迁移到DSS1.1.0的详细升级流程。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- AppConn 架构优化。架构更加简化清晰，文档更加全面细腻，手把手教您如何实现一个新的AppConn，以及添加一个新的工作流节点。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">缩写：</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- DSS: DataSphereStudio</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- DAS: Data Api Service</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>已集成的数据应用组件</strong></p> 
<p><img src="https://pic1.zhimg.com/80/v2-5154180a194e73bdd86b9e452faf09f0_720w.jpg" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>新特性</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-AppConn] 集成了 Apache DolphinScheduler1.3.X，设计并开发了全新的调度中心</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Commons] 适配了 Apache Linkis1.1.1</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-AppConn] 集成了 Exchangis1.0.0</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-AppConn] 集成了 Schedulis0.7.0</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-AppConn] 集成了 Qualitis0.9.2</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-AppConn] 集成了 Visualis1.0.0</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-AppConn] 集成了 Streamis0.2.0</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-AppConn] 集成了 Prophecis0.3.2</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-AppConn] AppConn 架构优化</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Deployment] AppConn 插件安装支持热更新，无需重启所有服务</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Deployment] 支持优雅升级</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 新增帮助手册和新手指引</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-UI] 开发中心用户体验优化，如支持换肤、顶部导航栏改版等</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 新增工作流版本的脚本文件下载功能</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>功能增强</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 精简工作空间的部分接口，同时去掉无用的部分接口</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 新建工作空间时增加工作空间类型选项；工作空间首页右侧新增管理台功能；右下角新增帮助按钮</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 原先工作空间的应用商店去掉，组件访问入口统一从左上角菜单栏进入</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 首页下方应用开发流程demo案例优化，将demo案例的按钮去掉，改为敬请期待</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-UI] 资源管理器按钮样式变化、增加换肤功能、工程项目列表UI变动；应用商店UI样式变化；右上角导航栏UI改动</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-DAS] 下载功能限制5000条，并且每次下载操作都要向用户弹出操作风险提示</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-DAS] 结果集可视化页面的优化调整；优化结果集分页排序；支持结果集及日志部分下拉；结果集表格宽度支持拉长</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 新增工作流基础属性展示</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 新建工作流时自动将工作流模式和工作流方式勾选</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 新建工作流时增加工作流重要性级别特性</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] datachecker支持run_date变量</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Scriptis] 支持拖动代码tab到任意位置</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Scriptis] Sql和Hql支持文件类型相互修改</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Scriptis] 工作空间代码文件支持复制粘贴</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Scriptis] 前端查看数据库表时支持只看自己创建的表</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Commons] 用户登录之后，帮助用户清理缓存</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-AppConn] 补充Schedulis AppConn的Update和Delete 操作，并添加对应接口</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>Bug修复</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 修复在删除项目时无法同步删除所有第三方系统项目的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 修复工作空间管理-用户管理，编辑用户接口报400 bad request的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 修复用户管理页面用户数据显示异常的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 修复创建项目页面中发布权限、编辑权限和查看权限的下拉框无法获取该工作空间全部用户的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 修复切换代理用户后，前端工作空间展示的文件目录不正确问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 修复点击可视化按钮后界面没有显示可视化界面的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 修复脚本选择右键打开到侧边控制台报错的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 修复脚本复制粘贴到首次打开的文件夹下报错的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 修复用户在新建工程后授予其他用户权限，结果其他用户权限异常的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 修复工程复制功能按钮未展示的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workspace] 修复创建工程时向第三方应用发出检测工程名是否重复的请求失败问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复eventsender和eventreceiver节点传参失败的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复datachecker里的run_year等新增内置参数不生效的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复在有subflow的情况下，导出数据错乱或丢失的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复sendmail节点运行失败的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复开发中心的工作流回滚失败问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复datachecker、eventsender、eventreceiver节点运行时显示Failed to async get EngineNode AMErrorException</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复工作流暂停执行接口显示404的异常</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复工作流节点在右键关键脚本时，目录不能展示最新的异常</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复运行有结果集节点时，管理台结果集展示不全的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复datachecker在eventreceiver后面运行失败的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复工作流实时执行时部分节点已成功但状态未翻转导致工作流卡死的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Workflow] 修复在实时执行工作流中代理用户设置为非系统用户名后工作流执行失败的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Scriptis] 修复工作空间导入文件到HDFS失败的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Scriptis] 修复IDE中引用全局变量无效的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-DAS] 修复数据服务执行失败异常</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-DAS] 修复结果集下载报错异常</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-DAS] 修复选择多个结果集时，上个结果集的翻页会带过来的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-DAS] 修复导出CSV格式的结果集显示无权限问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-DAS] 修复导出结果集后运行日志页面内容显示不全的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-DAS] 修复运行有结果集的脚本可视化报错的异常</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-DAS] 修复结果集排序问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Commons] 修复shell中调用sqoop和script code中的代码与脚本中不一致问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Commons] 修复shell节点输入vi a.txt命令会导致脚本一直运行且引擎处于繁忙的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Commons] 修复接口/api/rest_j/v1/dss/datapipe/backgroundservice将代理用户设置为空导致报错的异常</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Commons] 修复hadoop用户创建项目时未赋予A用户任何权限，但A用户工作空间仍显示该项目的异常</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-AppConn] 修复AppConn启动时偶现zip失败的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- [DSS-Engine] 修复Python 3引擎被Kill后，运行节点显示为Python 2的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>贡献者</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">DSS 1.1.0 的发布离不开DSS社区的贡献者，感谢所有的社区贡献者，包括但不仅限于以下贡献者：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>rootljw、teenwolf0910、njnu-seafish</li> 
 <li>luban08、HanTang1、det101</li> 
 <li>KidUncle、mingfengwang</li> 
</ul> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>安装包</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">DSS1.1.0&Linkis1.1.1一键安装包：</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fosp-1257653870.cos.ap-guangzhou.myqcloud.com%2FWeDatasphere%2FDataSphereStudio%2Fdss_linkis_one-click_install_20220704.zip" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>osp-1257653870.cos.ap-guangzhou.myqcloud.com</span><span style="background-color:transparent; color:transparent">/WeDatasphere/DataSphereStudio/dss_linkis_one-click_install_20220704.zip</span></a></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>— END —</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>如何成为社区贡献者</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>1<span> </span></strong>► 官方文档贡献。发现文档的不足、优化文档，持续更新文档等方式参与社区贡献。通过文档贡献，让开发者熟悉如何提交PR和真正参与到社区的建设。参考攻略：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488838%2526idx%253D1%2526sn%253D3599cbb009751af44ba46720b0b60cf7%2526chksm%253Debb07621dcc7ff37405c5c7ab36193c44ba543d4854b01a23cbc66a12440472a3a0adbc85c5b%2526scene%253D21%2523wechat_redirect" target="_blank">保姆级教程：如何成为Apache Linkis文档贡献者</a></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>2<span> </span></strong>►代码贡献。我们梳理了社区中简单并且容易入门的的任务，非常适合新人做代码贡献。请查阅新手任务列表：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fapache%2Fincubator-linkis%2Fissues%2F1161" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>github.com/apache/incub</span><span style="background-color:transparent; color:transparent">ator-linkis/issues/1161</span></a></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>3<span> </span></strong>►内容贡献：发布WeDataSphere开源组件相关的内容，包括但不限于安装部署教程、使用经验、案例实践等，形式不限，请投稿给小助手。例如：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488722%2526idx%253D1%2526sn%253D6069ac14a2e0ec6f09acb8c8a471914f%2526chksm%253Debb077b5dcc7fea3fcb2df95de0b3a99ecf1f73a86b8c036f1c36c17cce30c1d36b38866fec0%2526scene%253D21%2523wechat_redirect" target="_blank">技术干货 | Linkis实践：新引擎实现流程解析</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488695%2526idx%253D1%2526sn%253D4020e1bccb565d518c0731b26b9a76ac%2526chksm%253Debb077d0dcc7fec65c3052051f3a7d6d51b160fa82b5b89c06e1e0180080bb85949683f31a32%2526scene%253D21%2523wechat_redirect" target="_blank">技术干货 | Prophecis保姆级部署教程</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488005%2526idx%253D1%2526sn%253Ddf78dfb77f475c2d1ef7ee69568db5c7%2526chksm%253Debb07162dcc7f8749a421038dd51abd7befb08aba8354846d87c61982db6a1ba520d99fd391b%2526scene%253D21%2523wechat_redirect" target="_blank">社区开发者专栏 | MariaCarrie：Linkis1.0.2安装及使用指南</a></li> 
</ul> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>4<span> </span></strong>►社区答疑：积极在社区中进行答疑、分享技术、帮助开发者解决问题等；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>5<span> </span></strong>►其他：积极参与社区活动、成为社区志愿者、帮助社区宣传、为社区发展提供有效建议等；</p> 
<p> </p>
                                        </div>
                                      
</div>
            