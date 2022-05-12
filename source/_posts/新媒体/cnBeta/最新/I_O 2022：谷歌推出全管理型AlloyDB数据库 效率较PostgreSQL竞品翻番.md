
---
title: 'I_O 2022：谷歌推出全管理型AlloyDB数据库 效率较PostgreSQL竞品翻番'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0512/714f3281a958ef0.jpg'
author: cnBeta
comments: false
date: Thu, 12 May 2022 05:50:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0512/714f3281a958ef0.jpg'
---

<div>   
在 I/O 2022 开发者大会首日，Google 隆重推出了名为 AlloyDB 的全托管式 PostgreSQL 数据库。<strong>与亚马逊云服务（AWS）的 Aurora PostgreSQL 竞品相比，Google 宣称 AlloyDB 具有翻倍的效率。</strong>此外在相同的工作负载下，AlloyDB 的运行效率可达标准 PostgreSQL 的四倍、分析查询的速度也快了百倍。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0512/714f3281a958ef0.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>熟悉 Google Cloud 生态的开发者，或许不会对全管型 PostgreSQL 数据库服务感到陌生。</p><p>此前该公司已经为 PostgreSQL 和 Spanner 提供了 CloudSQL，且 Google Cloud 的全管理关系数据库服务也提供了 PostgreSQL 兼容接口。</p><p>AlloyDB 的核心，仍基于标准的 PostgreSQL 数据库来实现。只是为了能够充分发挥谷歌自家基础设施的实力，开发团队才对于其内核进行了修改、同时努力保持在最新的版本状态。</p><p><img src="https://static.cnbetacdn.com/article/2022/0512/5ab5ba3e1581cd9.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>在 AWS 工作了很长一段事件后，Andi Gutmans 于 2020 年跳槽到了 Google、并担任数据库产品的主管兼工程副总裁。</p><p>他表示，尽管 Google 在帮助企业将 MySQL 和 PostgreSQL 迁移到云端的工作中提供了很大的帮助，但还是未能充分照顾到那些想要迁移其遗留数据库（比如 Oracle）到开源服务的部分客户。</p><p>究其原因，是因为许多企业用到了不止一个云服务提供商，同时希望能够尽可能灵活地在任何地方运行。在拖延了多年后，目前正有越来越多的客户愿意投入资源来摆脱相关束缚。</p><p>随着 Postgres 的崛起（以及 MySQL 的衰落）、并逐渐成为开源关系数据库的事实标准，Google 推动客户向专用的高性能 PostgreSQL 服务迁移的动力也变得更加充足。</p><p><img src="https://static.cnbetacdn.com/article/2022/0512/823f8117fdab05e.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p>Gutmans 补充道：许多 Google 客户正希望将他们的关系数据库用于分析用例，因而该 AlloyDB 开发团队耗费了大量的精力来确保 Postgres 能够为这部分用户带来更好的性能体验。</p><p>在 AWS 工作期间，他曾带领过 AWS 诸多分析服务的管理工作，有机会了解到数据对客户的重要性和关键性、并且积攒下了深厚的技术背景。</p><p>不过随着行业风向的转变，与之交谈的不再一定是一线开发人员 —— 甚至不少客户来自业务部门、或以分析师的身份来接洽。</p><p>在看到现实世界在如此融合的同时，他也切实感受到了用户希望从他们的数据中获得实时的洞察力。</p><p><img src="https://static.cnbetacdn.com/article/2022/0512/8e2162d2fdcd1e6.jpg" alt="4.jpg" referrerpolicy="no-referrer"></p><p>回到技术底层，可知 AlloyDB 建立在 Google 现有的基础架构之上、可将计算和存储剥离开来 —— 与运行 Spanner、BigQuery 和几乎所有 Google 服务的基础架构层类似。</p><p>除了专注于 PostgreSQL 的 AlloyDB，相关服务也已在竞争中占据了相当大的优势。然而在努力支持多个数据库引擎 / 查询语言的时候，你并不总能开展面面俱到的优化。</p><p>鉴于企业要求使用 Postgre 来迁移这些遗留数据，Google 最终决定在该领域做到顶尖。通过内核级的更改，该团队已实现超过 64 个虚拟内核的线性扩展。</p><p>而在分析方面，AlloyDB 团队也打造了一套基于机器学习的定制缓存服务来学习客户的访问模式。然后将 Postgres 的行格式转换为内存中的列格式，以显着提升执行的效率。</p>   
</div>
            