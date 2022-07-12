
---
title: '工作流任务调度系统 Schedulis 0.7.0 新版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1431'
author: 开源中国
comments: false
date: Tue, 12 Jul 2022 17:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1431'
---

<div>   
<div class="content">
                                                                                            <p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>Schedulis简介</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>Schedulis 是一个基于LinkedIn 的开源项目 Azkaban 开发的工作流任务调度系统。该调度系统具备高性能，高可用（去中心化多调度中心和多执行器）和多租户资源隔离等金融级特性；现已被集成到数据应用开发门户 DataSphere Studio（以下简称DSS）。</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本次发布的 0.7.0 版本，与上个版本 0.6.2 相比，<strong>主要完成与DSS 1.1.0 以及Apache Linkis 1.1.1 的适配</strong>，修复用户在使用过程中出现的一些问题和优化文档。推荐用户升级到此版本。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2FWeBankFinTech%2FSchedulis" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>github.com/WeBankFinTec</span><span style="background-color:transparent; color:transparent">h/Schedulis</span></a></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>Schedulis 0.7.0 新版本特性</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>特性增强</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- 适配 DSS 1.1.0、Linkis Apache 1.1.1 版本</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>问题修复</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- 编译项目缺少 pentaho-aggdesigner-algorithm 依赖问题修复</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- 修复由于 session 失效时间过短导致点击跳转登录界面的问题</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">- 合并 GitHub PR</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>云资源</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">项目 jobtype 插件的依赖和配置，打包下载链接「Schedulis jobtypes」</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fshare.weiyun.com%2FRgAiieMx" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>share.weiyun.com/RgAiie</span><span style="background-color:transparent; color:transparent">Mx</span></a></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">密码：det7rf</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">具体使用说明可见项目部署手册：</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2FWeBankFinTech%2FSchedulis%2Fblob%2Fmaster%2Fdocs%2Fschedulis_deploy_cn.md" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>github.com/WeBankFinTec</span><span style="background-color:transparent; color:transparent">h/Schedulis/blob/master/docs/schedulis_deploy_cn.md</span></a></p> 
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
                                        </div>
                                      
</div>
            