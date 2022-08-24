
---
title: '重磅发布 _ 汉得 iPaaS 全域集成平台 集星獭 1.5.0 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-215391d77227db8ca50959856cb05db2052.gif'
author: 开源中国
comments: false
date: Wed, 24 Aug 2022 05:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-215391d77227db8ca50959856cb05db2052.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="图片" src="https://oscimg.oschina.net/oscnet/up-215391d77227db8ca50959856cb05db2052.gif" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#2463ff"><strong>2022 年 08 月 19 日，汉得集成平台集星獭 1.5.0.RELEASE 正式发布。</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">汉得企业级系统集成平台（中文名集星獭，英文名 JeeStar），是一站式<strong><span style="color:#2463ff">多系统集成、多云集成、多端集成、多协议集成、多设备集成、数据集成、页面集成</span></strong>的全域集成解决方案。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">集成平台沉淀了汉得多年 ToB 项目实施的系统集成经验，在消除企业信息孤岛、数据孤立、打通多源多端的数据断链及混合云对接等场景中提供了高效便捷的功能及策略方案。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><strong>重点内容抢先看</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#2463ff"><strong>1、接口服务</strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#6e6e6e">新增支持一键注册外部透传接口</span></p> </li> 
</ul> 
<p style="color:#3e3e3e; margin-left:0; margin-right:0; text-align:left"><span style="color:#2463ff"><strong>2、服务编排</strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#6e6e6e">新增单元调试功能；编排无需上线即可运行，可选择某几个节点调试运行；模拟节点响应结果，检验表达式正确与否；快速查看响应结果和运行日志；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#6e6e6e">新增 Shell/Bat 脚本节点；支持本地模式和远程模式，可自定义脚本内容或者选择脚本文件执行；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#6e6e6e">新增 DATAX 节点；支持 MqSQL、Oracle、SQL Server、PostgreSQL 数据源之间的数据同步；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#6e6e6e">新增规则引擎类节点：公式计算、关联映射、分组聚合、数据入库；用于将一批数据经过计算、值集映射、分组聚合等操作，最后将处理好的数据进行入库。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#6e6e6e">编排节点表达式内置常用函数；前端组件支持选取；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#808080"><span style="color:#6e6e6e">优化子编排参数取值模式；循环节点、MQ 消费者节点、子编排节点等存在选取子编排配置的节点，通过带出子编排的全局参数和维护参数值，子编排中的节点通过 Global 关键字取父编排的数据、监听的消息数据。</span></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>— 下面为大家介绍本次更新的详细情况 —</strong></p> 
<h4 style="margin-left:0; margin-right:0; text-align:center"><strong>新增特性</strong></h4> 
<blockquote> 
 <h4 style="margin-left:0; margin-right:0"><span><strong>接口平台</strong></span></h4> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>01 一键注册外部透传接口</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一键快速获取外部系统的透传接口，可选择性地注册需要的接口，实现快速集成调用外部系统接口的能力。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="390" src="https://oscimg.oschina.net/oscnet/up-8fbebaa58b3a4d2d43c71833af7563bce8b.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<blockquote> 
 <h4 style="margin-left:0; margin-right:0"><span><strong>服务编排</strong></span></h4> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>01 单元调试</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">你还在为做好一个编排流程反复的上下线，反复的修改表达式、配置项吗？</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">单元调试可以使编排无需上线即可运行，可选择某几个节点调试运行；支持快速模拟节点响应结果，检验表达式正确与否；快速查看响应结果和运行日志。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="391" src="https://oscimg.oschina.net/oscnet/up-d0a603f56353757c9422503b3d4efd7f38b.png" width="800" referrerpolicy="no-referrer"><img alt height="391" src="https://oscimg.oschina.net/oscnet/up-23f1837d0bfb558018b57725ac209ef30bf.png" width="800" referrerpolicy="no-referrer"><img alt height="391" src="https://oscimg.oschina.net/oscnet/up-e2ca1f750a21cdfdef39270de3eecdb2ebc.png" width="800" referrerpolicy="no-referrer"><img alt height="432" src="https://oscimg.oschina.net/oscnet/up-0e213a257f1174a0ee63ace69cbf22c0f54.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>02 任务节点 - Shell/Bat</strong><strong><span> </span>节点</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:rgba(1, 0, 0, 0)">Shell/Bat 节点使您能够连接到本地或远程的任何机器，以在这些机器上执行脚本文件和命令。要使用该节点您必须首先在 Windows 或 Linux 机器上安装 SSH 服务器。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>脚本执行模式分为本地模式和远程模式；本地模式即脚本会在节点运行的机器上执行，远程模式即脚本在指定的远程机器上执行。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><img alt height="613" src="https://oscimg.oschina.net/oscnet/up-288d6970a1cdbca75f98a3051098d38d154.png" width="800" referrerpolicy="no-referrer"></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><img alt height="540" src="https://oscimg.oschina.net/oscnet/up-d96d6a4c040532ec50549259f4d62486a39.png" width="800" referrerpolicy="no-referrer"></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>03 任务节点 - DataX 节点</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">用于数据同步，支持 MqSQL、Oracle、SQL Server、PostgreSQL 数据源之间的数据同步；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持原生的 Json 文件配置，也提供界面操作指导自动生成配置文件，减少配置理解成本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="746" src="https://oscimg.oschina.net/oscnet/up-98d0195b8640a1189f0a5624df5083bd480.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="615" src="https://oscimg.oschina.net/oscnet/up-b5f9a3bd158099282757d0fb1c5ec780e5a.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>04 任务节点 - 规则引擎类节点</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">可用于将一批数据经过公式计算、值集映射、分组聚合等操作，最后将处理好的数据进行入库。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#2463ff"><strong>公式计算</strong>：</span>用于对来源数据集中指定的字段进行公式计算处理，并将公式计算的结果生成新的字段</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="图片" height="288" src="https://oscimg.oschina.net/oscnet/up-de8dff59133639a7a8a3294c9bdc060f37b.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#2463ff"><strong>关联映射</strong>：</span>用于将来源数据集和指定值集视图数据集进行条件关联做值集映射，并给来源数据集扩展新字段。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="图片" height="461" src="https://oscimg.oschina.net/oscnet/up-2d8fd78bc8dc5ece9e7c9299d04c6f91d30.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#2463ff"><strong>分组聚合</strong>：</span>用于将来源数据进行分组和聚合操作，包括最大值、最小值、求和、平均；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="图片" height="501" src="https://oscimg.oschina.net/oscnet/up-b059641608c1a72cec9b14c2457abefe4ef.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#2463ff"><strong>数据入库</strong>：</span>用于将来源数据进行入库处理，通过配置入库规则的方式可将来源数据配置到指定的表和字段中；支持头行数据入库。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="360" src="https://oscimg.oschina.net/oscnet/up-703f2041d2f2230233a48fd01b0c913fbeb.png" width="800" referrerpolicy="no-referrer"><img alt height="557" src="https://oscimg.oschina.net/oscnet/up-31a060c09abbf0e9a469abcce53570fbdb5.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>05 子编排传参、表达式取值优化</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:rgba(1, 0, 0, 0)">循环节点、MQ 消费者节点、子编排节点等存在选取子编排配置的节点，通过带出子编排的全局参数和维护参数值，子编排中的节点通过 Global 关键字取父编排的数据、循环迭代节点每次循环的数据、MQ 消费节点监听的消息数据。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:rgba(1, 0, 0, 0)">同时为了兼容老版本，以前的表达式取值配置保留。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="图片" height="353" src="https://oscimg.oschina.net/oscnet/up-fdc322ef5c3fd5fe89699257814b1a68d4b.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h4 style="margin-left:0; margin-right:0; text-align:center"><strong>功能优化</strong></h4> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span><strong>01</strong></span><span> <span><strong>接口平台</strong></span></span></p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="background-color:rgba(1, 0, 0, 0)">修复创建集成系统派生创建角色的功能故障，添加异步初始化角色功能及界面按钮</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 V2p 透传接口，请求参数 Key 全部变为小写的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">整体修复部分 SQL 在 Oracle 环境下不适配的问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复获取文档 Header 时，存在多个相同键值的 Header 时合并错误问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化去除业务对象接口新增保存加解密逻辑</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化调整 Poi、Xmlbean 版本解决服务导入无数据或无反应问题，最新选配即可支持依赖调整</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化文档导出的 Word 版本格式（V2P）- 全新的板式，更专业、美观</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 V2 接口透传文件逻辑</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化通过透传发布的 Url 方式调用接口，日志存储支持直接 Db 存储、Redis 队列、MQ 模式；默认使用 Redis 模式，可提升透传的性能和 TPS</p> </li> 
</ul> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span><strong>02</strong></span><span> <span><strong>服务编排</strong></span></span></p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">前端表达式控件选取优化，增强用户体验性</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">脚本类节点增加模板选取功能，便于用户理解快速编写脚本</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">编排部分节点性能优化</p> </li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>联系我们</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span>产品试用</span></strong><span>请登录开放平台。请在 PC 端打开：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.hand-china.com%2Fmarket-home%2Ftrial-center%2F" target="_blank"><span style="color:#497c9b">https://open.hand-china.com/market-home/trial-center/</span></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#497c9b"><span>产品详情</span></span></strong><span style="color:#497c9b"><span>请登录开放平台：</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.hand-china.com%2Fdocument-center%2F" target="_blank"><span>https://open.hand-china.com/document-center/</span></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#497c9b"><span>如有疑问登录开放平台<strong>提单反馈</strong>：</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.hand-china.com%2F" target="_blank"><span>https://open.hand-china.com/</span></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fweixin.hscvdemo.saas.hand-china.com%2Ffree-trial" target="_blank"><span><img alt="图片" height="210" src="https://oscimg.oschina.net/oscnet/up-64ae8d93ab88119d539e38c3df1f1a31677.png" width="800" referrerpolicy="no-referrer"></span></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="图片" height="222" src="https://oscimg.oschina.net/oscnet/up-521ba1ac78da94b7a7395d6e37e9faa5d46.jpg" width="800" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#999999">▲ 更多精彩内容，扫码关注 <strong>“四海汉得”</strong> 公众号</span></p>
                                        </div>
                                      
</div>
            