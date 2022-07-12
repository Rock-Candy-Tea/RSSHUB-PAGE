
---
title: '开源数据交换工具Exchangis 1.0.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3140'
author: 开源中国
comments: false
date: Tue, 12 Jul 2022 17:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3140'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0"><strong>Exchangis简介</strong></p> 
<p style="margin-left:0; margin-right:0">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2FWeBankFinTech%2FExchangis" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>github.com/WeBankFinTec</span><span style="background-color:transparent; color:transparent">h/Exchangis</span></a></p> 
<p style="margin-left:0; margin-right:0"><strong>Exchangis1.0.0是微众银行联合中国电信天翼云和仙翁科技共建的全新数据交换工具，支持异构数据源之间的结构化和非结构化数据传输同步。</strong></p> 
<p style="margin-left:0; margin-right:0">Exchangis1.0.0 还抽象了一套统一的数据源和同步作业定义插件，允许用户快速接入新的数据源，允许用户快速集成对接 Apache Linkis 新的数据同步引擎，用户只需在数据库中简单配置即可在页面中使用新的数据源和数据同步引擎。</p> 
<p style="margin-left:0; margin-right:0">借助于Linkis计算中间件的连接、复用和简化能力，Exchangis天生具备了高并发、高可用、多租户隔离和资源管控的金融级数据同步能力。</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong>新版本内容</strong></p> 
<p style="margin-left:0; margin-right:0">Exchangis-1.0.0正式版本相比于Exchangis1.0.0-RC1版本，本次1.0.0正式版最大的特点就是与DataSphereStudio里程碑式的1.1.0版本集成对接，并支持Exchangis数据同步任务复制功能。</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">缩写：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>EJS: Exchangis Job Server</li> 
 <li>EJB: Exchangis Job Builder</li> 
 <li>EP: Exchangis Project</li> 
 <li>EDS: Exchangis Datasource Server</li> 
 <li>EXAPP: Exchangis Appconn</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>新特性</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[EXAPP] Exchangis-306 适配DSS 1.1.0版本新的exchangis-appconn模块。</li> 
 <li>[EXAPP] Exchangis-306 增加Exchangis任务复制功能，能够在DSS端将工作流节点回滚到其他历史版本。</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>功能增强</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[EXAPP] Exchangis-313 Appconn导入sqoop任务的命名优化，加上工作流版本号。</li> 
 <li>[EJS] Exchangis-313 执行启动脚本时打印出Eureka地址。</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>Bug修复</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[EJS] Exchangis-315 修复了字段映射无法保存成功的问题。</li> 
 <li>[EXAPP] Exchangis-316 修复了sqoop工作流节点删除失败的问题。</li> 
 <li>[EXAPP] Exchangis-317 修复了Appconn中转发POST请求时服务错误的问题，以及labels标签未正确获取的问题。</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>贡献者</strong></p> 
<p style="margin-left:0; margin-right:0">Exchangis-1.0.0发布离不开Exchangis社区的贡献者，感谢所有的社区贡献者！包括但不仅限于以下Contributors：wushengyeyouya、Dlimeng、Davidhua1996、mingfengwang、yuxin-No1、ryanqin01、 lucaszhu2zgf、FinalTarget、Liveipool、gjy1043、jefftlin。</p> 
<p style="margin-left:0; margin-right:0"> </p> 
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
            