
---
title: 'Apache Hop 2.0.0 正式 GA'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5bcb0996412cff90f83eaf5b0f701ad53a3.png'
author: 开源中国
comments: false
date: Fri, 10 Jun 2022 07:38:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5bcb0996412cff90f83eaf5b0f701ad53a3.png'
---

<div>   
<div class="content">
                                                                                            <p>Apache Hop 2.0.0 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhop.apache.org%2Fblog%2F2022%2F06%2Fhop-2.0.0%2F" target="_blank">发布</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Apache Hop（Hop 是 Hop Orchestration Platform 的缩写）是一个灵活、元数据驱动的数据编排、工程和集成平台。该项目起源于二十多年前的 ETL 平台 Kettle，经过几年的重构，于 2020 年 9 月进入 ASF 孵化器。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Kettle 是一款知名的开源 ETL 工具，抽取数据高效稳定，在执行 ETL 工具、ETL 数据抽取转换等批任务时，使用频率较高，包括电信、金融、银行在内的各行业都使用 Kettle 作为数据处理工具。但是由于各种因素，Kettle 近几年的发展还是较为缓慢，为了改变现况，从 2020 年 2 月份开始，Kettle 社区在 Kettle 8.2 的基础上创建了一个分支，Hop 正是基于这个分支构建的新项目，2020 年 9 月份，Hop 正式进入 ASF，成为孵化项目。 </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Apache Hop 基于 Java 的可视化设计器、服务器和配置工具易于在众多平台上设置、部署和维护，其被设计用于任何场景：本地、云、裸操作系统、容器、物联网环境、大型数据集等，并支持在 Windows、Linux 和 OSX 平台上运行。特点包括：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>轻量级的 “一次设计，处处运行” 架构</li> 
 <li>元数据驱动</li> 
 <li>可视化开发环境</li> 
 <li>集成丰富的插件</li> 
 <li>内置生命周期管理</li> 
</ul> 
<hr> 
<p><strong>2.0 更新亮点</strong></p> 
<h3>升级到 Java 11</h3> 
<p>发布公告写道，在 2.0 中，Hop 可以在 Java 11 上可靠地运行。因为新版本升级了所有 Apache Hop 代码，目前支持在 Java 11 和 Java 8 上正常构建和运行。</p> 
<p>官方称升级 Java 版本的工作进行了几个月，开发团队细致地修复和扩展了测试和代码问题。借此机会，他们还对代码进行了清理，同时对部分 API 进行了破坏兼容性的变更，开发者需要查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhop.apache.org%2Fdev-manual%2Flatest%2Fupgrading-to-20.html" target="_blank">文档</a>以了解如何才能将 Hop 插件升级到 2.0。</p> 
<h3>提供中文版本</h3> 
<p>Apache Hop 2.0 提供了中文版本，这项工作由中国开发者<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fshlxue" target="_blank">@Shl Xue</a>贡献。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5bcb0996412cff90f83eaf5b0f701ad53a3.png" referrerpolicy="no-referrer"></p> 
<h3>引入新的转换插件</h3> 
<p><span><span style="color:#0e3a5a"><strong><span><span><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Apache AVRO 文件输出</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <p style="margin-left:0; margin-right:0"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhop.apache.org%2Fmanual%2Fnext%2Fpipeline%2Ftransforms%2Favro-file-output.html" target="_blank">Apache Avro 文件输出</a>将写入转换为 Avro 二进制或 JSON 格式的二进制文件或字段。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
</div> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-3b5738a1bb73bc8cd8191222a8ee6e48706.png" referrerpolicy="no-referrer"></p> 
<p><strong>Apache Doris 批量加载程序</strong></p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <p style="margin-left:0; margin-right:0"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoris.apache.org%2F" target="_blank">Apache Doris</a> 是现代 MPP 分析数据库产品，可提供亚秒级查询和高效的实时数据分析。凭借其分布式架构，支持高达 10PB 级别的数据集，并且易于操作。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhop.apache.org%2Fmanual%2Fnext%2Fpipeline%2Ftransforms%2Fdorisbulkloader.html" target="_blank">Apache Doris Bulk Loader</a> 转换支持以高速和大容量将数据插入到 Apache Doris 中，使其成为比使用传统数据库插入语句更快的数据加载方式。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-dba71e22018b42a356c6f41d6757f45b38a.png" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0px; margin-right:0px; text-align:start"><span><span style="color:#0e3a5a"><strong><span><span><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Drools 规则执行器</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></p> 
 <div style="margin-left:0; margin-right:0; text-align:start"> 
  <p style="margin-left:0; margin-right:0"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhop.apache.org%2Fmanual%2Fnext%2Fpipeline%2Ftransforms%2Frulesexecutor.html" target="_blank">Drools Rule Executor</a> 转换可根据规则集执行传入行的字段。这对于确定附加信息，或将行路由到另一个转换很有用。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
  <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-83f792acbd90049fd4edbef596e9ec89251.png" referrerpolicy="no-referrer"></p> 
 </div> 
</div> 
<h3>升级 Apache Beam</h3> 
<p>Apache Beam是先进的统一编程模型，可用于在任何执行引擎上运行批量和流式数据处理作业。流行的执行引擎包括 Apache Spark、Apache Flink 或 Google Cloud Platform Dataflow。</p> 
<p>Apache Beam 一直是 Apache Hop 的一个重要插件，并随 Apache Spark 3.1.3 和 Apache Flink 1.14.4 升级到 2.38.0。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhop.apache.org%2Fblog%2F2022%2F06%2Fhop-2.0.0%2F" target="_blank">详情查看发布公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            