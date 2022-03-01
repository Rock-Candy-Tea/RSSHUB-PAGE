
---
title: '版本动态 _ 数据质量管理平台 Qualitis 0.9.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3058'
author: 开源中国
comments: false
date: Tue, 01 Mar 2022 17:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3058'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p><span style="color:#5c5c5c">Qualitis 是微众银行开源的一款数据质量管理系统，用于解决业务系统运行、数据中心建设及数据治理过程中的各种数据质量问题。它提供了一整套统一的流程来定义和检测数据集的质量并及时报告问题。</span></p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#5c5c5c">本次发布的 0.9.0 版本，与上一版本<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4MDkxNzUxMg%3D%3D%26mid%3D2247487048%26idx%3D1%26sn%3D5ad060bc82e7e933d3e1b952077d72bf%26chksm%3Debb06d2fdcc7e4398267d0ead9b69eb51acb1b58741a5b3722cc93709e7fd223270e5812ed04%26scene%3D21%23wechat_redirect" target="_blank">【重磅发布】Qualitis 0.8.0 版本发布</a>跨度较大，整合新增了<span style="background-color:#ffffff">更多</span>功能。</span><strong><span style="color:#021eaa">完成了 DSS 1.x 版本的适配，集成工作流的 Appjoint 已被 Appconn 取代；支持Linkis 0.x，也支持Linkis 1.0以上的提交执行</span></strong><span style="color:#5c5c5c">，需要在集群配置时指定集群的版本。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><strong><span style="color:#021eaa">增强了</span></strong></span><span style="color:#5c5c5c">任务管理和任务提交的定制化配置能力，校验任务的参数定制化，执行多集群切换，可以更好的解决校验效率与资源利用的问题。在配置规则方面，分模块配置优化，库级别对比配置，帮助提升配置效率。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><strong><span style="color:#021eaa">提供了</span></strong></span><span style="color:#5c5c5c">数据质量管理系统中必备的指标管理功能，支持多维度的指标校验，支持用户通过更灵活的自定义SQL计算统计指标，丰富数据治理校验场景。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#5c5c5c">支持关系型数据数据源，基于Linkis 1.0以上版本的Datasource服务，可以对主流的关系型数据进行数据质量校验。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#5c5c5c">开源项目地址：</span></p> 
<p style="color:#24292f; margin-left:0; margin-right:0">https://github.com/WeBankFinTech/Qualitis</p> 
<p style="color:#24292f; margin-left:0; margin-right:0">https://gitee.com/WeBank/Qualitis</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#5c5c5c">欢迎各位社区的小伙伴使用最新版本的Qualitis，也希望能一起合作共建Qualitis，构建更加强大完善的数据质量校验系统。具体内容如下。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#021eaa">特性增强</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#494949">新增关系型数据的质量校验 (需Linkis 1.0以上版本提供Datasource服务)；</span></p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0">新增数据源管理 (需Linkis 1.0以上版本提供Datasource服务)；</p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0">新增规则模板权限管理，系统管理员、部门管理员、普通用户可以新增权限范围内的模板；</p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0">新增数据质量业务指标管理功能；</p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0">新增多维度指标校验功能，支持自定义SQL校验；</p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0">新增引擎参数管理 (需接入Linkis 1.0 以上版本)，支持多 Linkis 集群切换；</p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0">新增任务执行参数配置管理；</p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0">支持数据质量分析统计结果导出到指定的存储目录；</p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0"><span style="color:#494949">支持库级数据全量一致性对比优化；</span></p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0">优化规则管理-规则查询实时统计库表规则部署数量情况；</p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0">优化任务提交前数据源校验；</p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0">适配 DataSphere Studio 1.x，Appjoint 升级为 Appconn 并实现三级规范；</p> </li> 
 <li> <p style="color:#494949; margin-left:0; margin-right:0">适配 Apache Linkis (Incubating) 1.x 版本。</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span style="color:#021eaa">BUG修复 </span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#5c5c5c">修复规则数据源配置，字段Decimal类型作为数值类型不可选的问题；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#5c5c5c">修改部分文档错误内容。</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span style="color:#021eaa">如何加入 W</span><span style="color:#021eaa">eDataSphere 社区共建</span></p> 
<p><span style="color:#5c5c5c">（1）新手任务：认领入门任务，详见https://github.com/apache/incubator-linkis/issues/1161；</span></p> 
<p><span style="color:#5c5c5c">（2）作品沉淀：发布WeDataSphere开源组建相关内容，包括但不限于安装部署教程、使用经验、案例实践等，形式不限，请投稿给小助手。如：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4MDkxNzUxMg%3D%3D%26mid%3D2247488005%26idx%3D1%26sn%3Ddf78dfb77f475c2d1ef7ee69568db5c7%26chksm%3Debb07162dcc7f8749a421038dd51abd7befb08aba8354846d87c61982db6a1ba520d99fd391b%26scene%3D21%23wechat_redirect" target="_blank"><span style="color:#5c5c5c">社区开发者专栏 | MariaCarrie：Linkis1.0.2安装及使用指南</span></a></p> 
<p><span style="color:#5c5c5c">（3）贡献代码：PR和Issue；</span></p> 
<p><span style="color:#5c5c5c">（4）答疑：热心为开发者答疑，如社区群回答开发者问题、issue答疑等；</span></p> 
<p><span style="color:#5c5c5c">（5）其他：沙箱体验、参与活动、成为社区志愿者等。</span></p>
                                        </div>
                                      
</div>
            