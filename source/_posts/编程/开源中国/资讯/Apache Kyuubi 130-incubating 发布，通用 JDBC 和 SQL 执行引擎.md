
---
title: 'Apache Kyuubi 1.3.0-incubating 发布，通用 JDBC 和 SQL 执行引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic4.zhimg.com/80/v2-0b5460c76c8cd9f6d83dea668ba58e03_720w.jpg'
author: 开源中国
comments: false
date: Sat, 18 Sep 2021 16:04:00 GMT
thumbnail: 'https://pic4.zhimg.com/80/v2-0b5460c76c8cd9f6d83dea668ba58e03_720w.jpg'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div style="text-align:left"> 
  <div>
   <strong style="color:#000000">Kyuubi 进入 Apache 孵化器后首次发布大版本</strong>
  </div> 
  <div>
    
  </div> 
 </div> 
 <div style="text-align:left">
  9月14日，Apache Kyuubi (Incubating) 社区发布了进入 Apache 孵化器后的第一个公开发行的正式版本，该版本的代号为 v1.3.0-incubating。
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  对于作为新晋 Apache 孵化器项目的 Kyuubi 而言，成为 Apache Top Level Project（TLP） 是其目标， 对于正式版本的发布我们需要深刻地践行 Apache Way，遵循社区的 RELEASE POLICY。和 TLP 们不同的是，孵化器项目需要通过两轮投票才能正式完成版本发布，首先是项目社区 dev mailing lists 的投票，决议通过之后需要在 general mailing lists 中发起新一轮的投票并接受并通过 Apache IPMC Member 的检查。在 RC7 经历一点小挫折后，在 Kyuubi 社区的共同努力下，v1.3.0-incubating RC9 最终获得了 Apache IPMC 的肯定，成功完成孵化以来的首次发布。
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  <strong>新版本主要更新</strong>
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  此次发布带来了 Lakehouse、Serverless Spark 等方面的多项增强，主要包括：
 </div> 
 <div> 
  <ol style="margin-left:0; margin-right:0"> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">基于最新的 Spark 3.0/3.1 版本做了充分的验证</span></li> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">支持使用 JDK 8(默认)，JDK 11 构建</span></li> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">在 Kyuubi Spark Extensions 模块中提供了增强的 AQE (目前支持 Spark 3.1)</span></li> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">提供了一些辅助的 SQL 函数作为 Spark 内置函数的补充</span></li> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">显著增强了 Spark 与 Kubernetes 的集成，涵盖文档、集成测试、工具等</span></li> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">支持配置 Engine/Session 级别的初始化 SQL 语句列表</span></li> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">支持自定义认证插件</span></li> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">支持从 Spark Web UI 上关停 engine</span></li> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">支持单引擎共享 SparkSession 模式</span></li> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">提供更多的指标和事件输出，增强可观测性</span></li> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">在数据湖平台 Delta 和 Iceberg 之上进行了充分的测试</span></li> 
   <li style="list-style-type:decimal; text-align:left"><span style="background-color:#ffffff; color:#24292f">在 MiniYARNCluster 之上进行了充分的测试</span></li> 
  </ol> 
  <p style="text-align:left">更多详情见发布公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkyuubi.apache.org%2Frelease%2F1.3.0-incubating.html" target="_blank"><u>https://kyuubi.apache.org/release/1.3.0-incubating.html</u></a></p> 
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  <strong>践行社区驱动</strong>
 </div> 
 <div style="text-align:left">
  <img src="https://pic4.zhimg.com/80/v2-0b5460c76c8cd9f6d83dea668ba58e03_720w.jpg" width="2548" referrerpolicy="no-referrer">
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  Apache Kyuubi (Incubating) 是一款构建在 Apache Spark 之上的分布式多租户 Thrift JDBC/ODBC 服务，最初由网易数帆主导开源，并于今年6月21日正式进入 Apache 孵化器。自项目进入 Apache 孵化器并完成早期项目的迁库开始，Kyuubi 社区一方面在项目导师们的帮助下开始构建新版本的发布计划，完成了本次发布计划；另一方面也在 "Community Over Code" 理念指引下积极壮大社区，在这一个多月间，我们开发者人数完成了近倍数的增长。此外，在用户的驱动下，我们也完成了和其他 Apache 社区的初步合作，比如 Apache DolphinScheduler 及 Apache Iceberg 等，共同帮助用户解决问题。 
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  <strong>如何下载使用最新版本？</strong>
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  最新的 Apache Kyuubi (Incubating) 1.3.0-incubating 版本保持了对早期 Kyuubi 1.x （非 ASF release）的良好兼容性，用户可选择至官方下载连接
  <span style="color:#df402a"> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkyuubi.apache.org%2Frelease%2F1.3.0-incubating.html" target="_blank"><u>https://kyuubi.apache.org/release/1.3.0-incubating.html</u></a>
  <span style="color:#df402a"> </span>完成下载后，进行原地升级。
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  对于新接触 Apache Kyuubi (Incubating) 用户，可以参考我们的 Quick Start 指南进行技能解锁， 详见 
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkyuubi.apache.org%2Fdocs%2Fr1.3.0-incubating%2Fquick_start%2Findex.html" target="_blank"><u>https://kyuubi.apache.org/docs/r1.3.0-incubating/quick_start/index.html</u></a>
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  <strong>如何参与社区？</strong>
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  Apache Kyuubi (Incubating) 项目是社区驱动的，我们致力于在 Apache Way 的指导下，为用户提供简单易用的大数据产品，我们强调社区协作，互相帮助，共同成长。
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  首先，如果您在下载和使用 Apache Kyuubi (Incubating) 1.3.0-incubating 中发现任何问题，欢迎使用 Github Issues 功能，
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-kyuubi%2Fissues" target="_blank"><u>https://github.com/apache/incubator-kyuubi/issues</u></a>
  <span style="color:#393939">，将您遇到的问题和社区分享。</span>
 </div> 
 <div style="text-align:left">
  <img src="https://pic1.zhimg.com/80/v2-e16ec42627802dfa9aede051d3dbac48_720w.jpg" width="1542" referrerpolicy="no-referrer">
 </div> 
 <div style="text-align:left">
  121121如果您或者您的公司正在使用 Apache Kyuubi(Incubating) 并希望能够和社区和其他用户共享，可以在 
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-kyuubi%2Fdiscussions%2F925" target="_blank"><span style="color:#003884">Who is using Apache Kyuubi (Incubating)？</span></a>
  <span style="color:#393939">中进行留言。</span>
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  我们也接受其他任何形式的帮助，详见 
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-kyuubi%23contributing" target="_blank"><u>https://github.com/apache/incubator-kyuubi#contributing</u></a>
  <span style="color:#393939">，欢迎通过 dev-subscribe@kyuubi.apache.org 订阅我们的邮件列表，获取社区最新动向。</span>
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  <strong>致谢</strong>
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  在社区驱动的模式下，Apache Kyuubi (Incubating) 1.3.0-incubating 的正式发布，是在 Kyuubi 的 Apache 孵化器之旅上前进的一小步。真诚地感谢每一位项目导师、社区贡献者及用户的信任、支持和帮助。也感谢 Apache 本土社区 ALC Beijing 给国内开源项目开辟的良好开源环境。
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left">
  <strong>了解更多</strong>
 </div> 
 <div style="text-align:left">
   
 </div> 
 <div style="text-align:left"> 
  <div>
   Apache Kyuubi(Incubating)项目官方网站：
   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkyuubi.apache.org%2F" target="_blank">https://kyuubi.apache.org/</a>
  </div> 
  <div> 
   <div>
    Apache Kyuubi(Incubating)项目GitHub地址：
    <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-kyuubi" target="_blank">https://github.com/apache/incubator-kyuubi</a>
   </div> 
  </div> 
 </div> 
 <div style="text-align:left"> 
  <div>
   <a href="https://my.oschina.net/u/4565392/blog/5264848" target="_blank">Apache Kyuubi on Spark 在CDH上的深度实践</a>
  </div> 
 </div> 
 <div style="text-align:left">
  <a href="https://my.oschina.net/u/4565392/blog/5207333" target="_blank">Apache Kyuubi(Incubating)：网易对 Serverless Spark 的探索与实践</a>
 </div> 
 <div style="text-align:left">
  <a href="https://my.oschina.net/u/4565392/blog/5230928" target="_blank">Spark + Kyuubi + Iceberg = Lakehouse</a>
 </div> 
 <div style="text-align:left">
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.infoq.cn%2Farticle%2FrlVLvAVVxJ7ym4ytgFEk" target="_blank">Apache Kyuubi PPMC 燕青：为什么说这是开源最好的时代？</a>
 </div> 
 <div style="text-align:left">
  <a href="https://my.oschina.net/u/4565392/blog/5114734" target="_blank">全票通过！网易数帆开源项目Kyuubi进入Apache孵化器</a>
 </div> 
</div>
                                        </div>
                                      
</div>
            