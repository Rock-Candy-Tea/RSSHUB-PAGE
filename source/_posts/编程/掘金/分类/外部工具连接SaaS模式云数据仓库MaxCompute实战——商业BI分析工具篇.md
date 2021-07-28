
---
title: '外部工具连接SaaS模式云数据仓库MaxCompute实战——商业BI分析工具篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de3293b0017a4936a4196d51dfa28451~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 18:39:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de3293b0017a4936a4196d51dfa28451~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> MaxCompute 是面向分析的企业级 SaaS 模式云数据仓库，以 Serverless 架构提供快速、全托管的在线数据仓库服务，消除了传统数据平台在资源扩展性和弹性方面的限制，最小化用户运维投入，帮助企业和大数据开发者经济并高效的分析处理海量数据。</p>
<p><strong>本文直播作者 木弈 阿里云智能 产品经理</strong></p>
<p>直播视频请点击 直播 观看。</p>
<p>本次分享将从四个方面讲解。</p>
<p>01 走进 MaxCompute 生态</p>
<p>02 商业智能（BI）分析工具概览</p>
<p>03 JDBC 简介</p>
<p>04 实操展示——快速接入 FineBI</p>
<p>下面开始我们第一部分的分享</p>
<h1 data-id="heading-0">一、走进 MaxCompute 生态</h1>
<p>首先来看下 MaxCompute 产品能支持的外部工具，大概可以分为商业智能、开发管理、传输调度、编程接口。本次分享主要关注商业智能（BI）工具这一板块，可以看到 MaxCompute 官方集成有Tableau、FineReport、FineBI、Quick BI。其中Tableau、FineBI、FineReport是在特定的版本会内置 MaxCompute 驱动，如果需要通过JDBC连接 MaxCompute ，还是需要手动加载 MaxCompute JDBC驱动，Quick BI作为阿里云的产品，是可以通过阿里云账号和AK信息直接连接的，同时在8.6及以上版本的Yonghong Desktop也是可以通过内置驱动连接 MaxCompute。在商业智能部分还有开源BI工具，Superset、Davinci也可以连接 MaxCompute。</p>
<p>在开发管理部分，是我们第二讲要讲的内容，包括DBeaver、DataGrip、SQL Workbench/J。</p>
<p>同时我们的产品还集成了 Kafka和Flink开源引擎。支持的ETL开源工具有Kettle、Airflow、Azkaban，这一部分是在本季直播的第三讲来介绍。支持的编程接口有Python、JDBC、SQLAlchemy。</p>
<p>除了支持的外部工具，MaxCompute 自身也有开放生态，包括内建开源引擎 Spark，迁移工具MMA，开发生态PyODPS、Mars，工具生态Web-Console等。同时 MaxCompute 也与阿里云内部产品共同构建了丰富的解决方案生态和数据应用生态。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de3293b0017a4936a4196d51dfa28451~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">二、商业智能（BI）分析工具概览</h1>
<p>商业智能 (BI) 工具支持将计算引擎得到的数据通过仪表板、图表和其他图形输出提供数据可视化，以直观的形式展示给决策者，帮助高管和经理做出更明智的业务决策。</p>
<p>本页所展示的都是经过 MaxCompute 团队成员测试，可以成功连接 MaxCompute 表数据并进行数据可视化的BI工具。 本次重点介绍商业型BI工具，其中Tableau、FineBI、FineReport都是需要通过 MaxCompute JDBC驱动连接 MaxCompute。Quick BI和 Yonghong Desktop 可以通过产品内置驱动连接 MaxCompute。这些BI工具成功连接 MaxCompute 数据源后，可以进行列举数据库、列举表、查看表结构、查询表数据、查询视图等相关操作，打造数据报表。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88e31b19342d425ba5cc2488e8993bfa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">三、JDBC 简介</h1>
<p><strong>JDBC</strong></p>
<p>JDBC（Java DataBase Connectivity）是一种用于执行SQL语句的Java API，可以为多种关系数据库提供统一访问，它由一组用Java语言编写的类和接口组成。简单来说就是用Java语言向数据库发送SQL语句来操作数据库。</p>
<p><strong>MaxCompute JDBC 驱动</strong></p>
<p>MaxCompute JDBC 驱动是 MaxCompute 提供的可以访问 MaxCompute 的JDBC接口。您可以通过标准的JDBC 接口基于 MaxCompute 执行海量数据的分布式计算查询。MaxCompute JDBC 驱动还可以用于连接MaxCompute 和支持 JDBC 的工具。</p>
<p><strong>MaxCompute 相关基本参数信息</strong></p>
<p>•URL：jdbc:odps:<MaxCompute_endpoint>?project=<MaxCompute_project_name></p>
<ul>
<li><MaxCompute_endpoint>：必填。MaxCompute项目所属区域的Endpoint。</li>
<li><MaxCompute_project_name>：必填。待连接的目标MaxCompute项目名称。此处为MaxCompute项目名称，非工作空间名称。</li>
</ul>
<p>•User：有访问指定项目权限的AccessKey ID。</p>
<p>•Password ：AccessKey ID对应的AccessKey Secret。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfe0d0a86533447a935c43ef0b223f82~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">四、实操展示——快速接入 FineBI</h1>
<p><strong>实操展示</strong></p>
<p>实操内容可点击下方 实操视频 进行查看。<br>
实操视频：<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftbm-auth.alicdn.com%2Fe99361edd833010b%2FbPtrVnKhAX2P1hCzj1c%2FG3YSuIpuma7bZuw1kvW%255C_318730152528%255C_hd%255C_hq.mp4%3Fauth%255C_key%3D1627442185-0-0-5f49d727f23a892032d1ed5b018880d9" target="_blank" rel="nofollow noopener noreferrer" title="https://tbm-auth.alicdn.com/e99361edd833010b/bPtrVnKhAX2P1hCzj1c/G3YSuIpuma7bZuw1kvW%5C_318730152528%5C_hd%5C_hq.mp4?auth%5C_key=1627442185-0-0-5f49d727f23a892032d1ed5b018880d9" ref="nofollow noopener noreferrer">tbm-auth.alicdn.com/e99361edd83…</a></p>
<p><strong>其他商业BI工具接入</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10d0c790e8b64626937ceb2cd147591a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000285938%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000285938/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            