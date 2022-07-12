
---
title: '流式应用开发管理系统 Streamis 0.2.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9683'
author: 开源中国
comments: false
date: Tue, 12 Jul 2022 17:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9683'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0"><strong>Streamis 简介</strong></p> 
<p style="margin-left:0; margin-right:0">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2FWeBankFinTech%2FStreamis" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>github.com/WeBankFinTec</span><span style="background-color:transparent; color:transparent">h/Streamis</span></a></p> 
<p style="margin-left:0; margin-right:0"><strong>Streamis是一个基于开源社区联合共建的流式应用开发管理系统，初期版本由微众银行、天翼云、仙翁科技和萨摩耶云参与共建开发。</strong></p> 
<p style="margin-left:0; margin-right:0">Streamis在框架层面直接接壤DataSphere Studio，同时底层引擎层面又直接对接了Linkis的Flink引擎，可以让用户低成本完成流式应用的开发、调试、发布和生产管理。同时随着Linkis和DataSphereStudio开源版本的发布迭代，对Streamis的功能特性也是持续地优化和增强。</p> 
<p style="margin-left:0; margin-right:0">Streamis 0.2.0版本发布，<strong>主要增加了对架构的优化和调整，并提供了一些重要功能特性，为后续版本迭代打下基础</strong>。</p> 
<p style="margin-left:0; margin-right:0">新增的核心功能特性主要包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>流式任务状态（Checkpoint和Savepoint）管理，使得用户可以为Flink应用程序做快照处理并具备从快照中恢复的能力；</li> 
 <li>新的流式任务配置模块，支持弹性增删流式任务的配置定义项；</li> 
 <li>Streamis AppConn, 数据层面打通和DataSphereStudio的同步；</li> 
 <li>流式作业批量管理（如批量启动和批量暂停），让用户可以对流式任务进行批操作，结合任务状态管理功能，从而做到任务异常自恢复；</li> 
</ul> 
<p style="margin-left:0; margin-right:0">缩写列表：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>SJL: Stream Job Launcher Module</li> 
 <li>SJDA: Stream Job Deploy API Module</li> 
 <li>SJHV: Stream Job History And Version Module</li> 
 <li>SBO: Stream Bulk Operation Module</li> 
 <li>SA: Stream AppConn Module</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>版本新特性</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>SJL: 添加任务作业状态管理模块，并提供状态获取器JobStateFetcher来获取作业状态信息(包括checkpoint/savepoint).[Streamis-23]</li> 
 <li>SJL: 能够自动重启失败的流式任务作业，并自动恢复其状态.[Streamis-22]</li> 
 <li>SBO: 任务作业批量操作接口集合. [Streamis-19]</li> 
 <li>SJDA: 能够获取任务作业对应的Yarn应用日志 (该特性依赖Linkis版本>=1.1.2). [Streamis-27]</li> 
 <li>SA: Streamis AppConn 同步项目和权限信息(该特性依赖DSS版本>=1.1.0). [Streamis-24]</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>功能增强</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>SJHV: 重构作业配置模块，提供新的作业配置获取和添加接口.[Streamis-21]</li> 
 <li>SJDA: 增加两种停止作业的方式：“直接停止”和“快照并停止” [Streamis-20]</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>修复功能</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>SJDA: 修复流式作业出现异常，但无法查看错误日志的问题 [Streamis-17]</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>云资源</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>前端编译包：</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fosp-1257653870.cos.ap-guangzhou.myqcloud.com%2FWeDatasphere%2FStreamis%2F0.2.0%2Fstreamis-0.2.0-dist.zip" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>osp-1257653870.cos.ap-guangzhou.myqcloud.com</span><span style="background-color:transparent; color:transparent">/WeDatasphere/Streamis/0.2.0/streamis-0.2.0-dist.zip</span></a></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>后端编译包：</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fosp-1257653870.cos.ap-guangzhou.myqcloud.com%2FWeDatasphere%2FStreamis%2F0.2.0%2Fwedatasphere-streamis-0.2.0-dist.tar.gz" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>osp-1257653870.cos.ap-guangzhou.myqcloud.com</span><span style="background-color:transparent; color:transparent">/WeDatasphere/Streamis/0.2.0/wedatasphere-streamis-0.2.0-dist.tar.gz</span></a></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>项目部署安装手册：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2FWeBankFinTech%2FStreamis%2Fblob%2Fmain%2Fdocs%2Fzh_CN%2F0.2.0%2FStreamis%2525E5%2525AE%252589%2525E8%2525A3%252585%2525E6%252596%252587%2525E6%2525A1%2525A3.md" target="_blank"><span style="color:#2980b9"><span style="background-color:transparent">https://</span></span><span>github.com/WeBankFinTec</span><span style="background-color:transparent; color:transparent">h/Streamis/blob/main/docs/zh_CN/0.2.0/Streamis%E5%AE%89%E8%A3%85%E6%96%87%E6%A1%A3.m</span></a></li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>— END —</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>如何成为社区贡献者</strong></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong>1<span> </span></strong>► 官方文档贡献。发现文档的不足、优化文档，持续更新文档等方式参与社区贡献。通过文档贡献，让开发者熟悉如何提交PR和真正参与到社区的建设。参考攻略：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488838%2526idx%253D1%2526sn%253D3599cbb009751af44ba46720b0b60cf7%2526chksm%253Debb07621dcc7ff37405c5c7ab36193c44ba543d4854b01a23cbc66a12440472a3a0adbc85c5b%2526scene%253D21%2523wechat_redirect" target="_blank">保姆级教程：如何成为Apache Linkis文档贡献者</a></p> 
<p style="margin-left:0; margin-right:0"><strong>2<span> </span></strong>►代码贡献。我们梳理了社区中简单并且容易入门的的任务，非常适合新人做代码贡献。请查阅新手任务列表：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fapache%2Fincubator-linkis%2Fissues%2F1161" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>github.com/apache/incub</span><span style="background-color:transparent; color:transparent">ator-linkis/issues/1161</span></a></p> 
<p style="margin-left:0; margin-right:0"><strong>3<span> </span></strong>►内容贡献：发布WeDataSphere开源组件相关的内容，包括但不限于安装部署教程、使用经验、案例实践等，形式不限，请投稿给小助手。例如：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488722%2526idx%253D1%2526sn%253D6069ac14a2e0ec6f09acb8c8a471914f%2526chksm%253Debb077b5dcc7fea3fcb2df95de0b3a99ecf1f73a86b8c036f1c36c17cce30c1d36b38866fec0%2526scene%253D21%2523wechat_redirect" target="_blank">技术干货 | Linkis实践：新引擎实现流程解析</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488695%2526idx%253D1%2526sn%253D4020e1bccb565d518c0731b26b9a76ac%2526chksm%253Debb077d0dcc7fec65c3052051f3a7d6d51b160fa82b5b89c06e1e0180080bb85949683f31a32%2526scene%253D21%2523wechat_redirect" target="_blank">技术干货 | Prophecis保姆级部署教程</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488005%2526idx%253D1%2526sn%253Ddf78dfb77f475c2d1ef7ee69568db5c7%2526chksm%253Debb07162dcc7f8749a421038dd51abd7befb08aba8354846d87c61982db6a1ba520d99fd391b%2526scene%253D21%2523wechat_redirect" target="_blank">社区开发者专栏 | MariaCarrie：Linkis1.0.2安装及使用指南</a></li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>4<span> </span></strong>►社区答疑：积极在社区中进行答疑、分享技术、帮助开发者解决问题等；</p> 
<p style="margin-left:0; margin-right:0"><strong>5<span> </span></strong>►其他：积极参与社区活动、成为社区志愿者、帮助社区宣传、为社区发展提供有效建议等；</p>
                                        </div>
                                      
</div>
            