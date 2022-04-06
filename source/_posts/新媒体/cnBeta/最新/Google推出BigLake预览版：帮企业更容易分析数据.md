
---
title: 'Google推出BigLake预览版：帮企业更容易分析数据'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0406/cb35450899ec9bb.webp'
author: cnBeta
comments: false
date: Wed, 06 Apr 2022 06:30:54 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0406/cb35450899ec9bb.webp'
---

<div>   
<strong>在其 Cloud Data Summit 峰会上，Google 宣布推出 BigLake 预览版。</strong>通过这个新数据湖存储引擎，可帮助企业更容易分析其数据仓库（data warehouses）和数据湖（data lakes）中的数据。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0406/cb35450899ec9bb.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">BigLake 的核心是利用 Google 在运行和管理其 BigQuery 数据仓库方面的经验，并将其扩展到 Google Cloud Storage 上的数据湖，将数据湖和仓库的优点结合到一个单一的服务中，抽象出基础存储格式和系统。</p><p style="text-align: left;">值得注意的是，这些数据可以放在 BigQuery 中，也可以存放在 AWS S3 和 Azure Data Lake Storage Gen2 上。通过 BigLake，开发者将获得一个统一的存储引擎，并能够通过一个系统查询底层数据存储，而不需要移动或重复数据。</p><p style="text-align: left;">在今天的公告中，Google Cloud 的数据库、数据分析和商业智能副总裁兼总经理 Gerrit Kazmaier 表示：</p><blockquote style="text-align: left;"><p style="text-align: left;">在不同的数据湖和数据仓库中管理数据，会产生孤岛，增加风险和成本，特别是当数据需要移动时。BigLake允许公司统一他们的数据仓库和湖泊来分析数据，而不必担心底层的存储格式或系统，这消除了从源头上重复或移动数据的需要，减少了成本和低效率。</p></blockquote><p style="text-align: left;">使用策略标签，BigLake 允许管理员在表、行和列级别上配置他们的安全策略。这包括存储在 Google Cloud Storage 的数据，以及两个支持的第三方系统，其中Google的多云分析服务 BigQuery Omni 启用了这些安全控制。然后，这些安全控制也确保只有正确的数据流入 Spark、Presto、Trino和TensorFlow等工具。该服务还与Google的Dataplex工具整合，提供额外的数据管理功能。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0406/26912ebd49f15cc.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Google指出，BigLake 将提精细度的访问控制，其API将跨越Google云，以及开放的面向列的Apache Parquet等文件格式和Apache Spark等开源处理引擎。</p><p style="text-align: left;">Google Cloud 软件工程师 Justin Levandoski 和产品经理 Gaurav Saxena 在今天的公告中解释道</p><blockquote style="text-align: left;"><p style="text-align: left;">企业需要管理和分析的有价值的数据量正在以惊人的速度增长。这些数据越来越多地分布在许多地方，包括数据仓库、数据湖和NoSQL存储。随着企业的数据越来越复杂，并在不同的数据环境中扩散，孤岛出现了，造成风险和成本增加，特别是当这些数据需要移动时。我们的客户已经明确表示；他们需要帮助</p></blockquote>   
</div>
            