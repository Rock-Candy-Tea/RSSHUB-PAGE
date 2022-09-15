
---
title: 'OpenSearch 2.3 发布，显著提升性能、可用性和数据持久性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0915/174515_uqZ1_2720166.gif'
author: 开源中国
comments: false
date: Thu, 15 Sep 2022 17:43:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0915/174515_uqZ1_2720166.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px; margin-right:0px; text-align:start">OpenSearch 2.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensearch.org%2Fblog%2Freleases%2F2022%2F09%2Fopensearch-2-3-is-ready-for-download%2F" target="_blank">已正式发布</a>。公告写道，此版本在性能、数据持久性和可用性方面获得了显著改进。</p> 
<blockquote> 
 <p style="margin-left:0px; margin-right:0px; text-align:start">OpenSearch 项目由 OpenSearch (fork Elasticsearch 7.10.2) 和 OpenSearch Dashboards (fork Kibana 7.10.2) 组成，包括企业安全、告警、机器学习、SQL、索引状态管理等功能。OpenSearch 项目中的所有软件均采用了 Apache License 2.0 开源许可协议。</p> 
</blockquote> 
<p><strong>新版本重要变化</strong></p> 
<ul> 
 <li><strong>段复制 (Segment replication)</strong></li> 
</ul> 
<p>段复制为用户提供了新的数据复制策略。通过段复制，OpenSearch 将 Lucene 文件分段从主分片复制到其副本，从而提升高吞吐工作负载的性能。虽然这种方法提升了索引吞吐量并降低了资源利用率，但代价是增加了网络利用率和刷新时间。</p> 
<ul> 
 <li><strong>远程存储</strong></li> 
</ul> 
<p>基于远程支持的存储允许用户部署云存储以提高数据的持久性。用户可以使用基于云的存储解决方案在每个索引的基础上备份和恢复集群中的数据。详见<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fopensearch.org%2Fdocs%2Flatest%2Fopensearch%2Fremote" target="_blank">功能文档</a>。</p> 
<ul> 
 <li><strong>引入拖放可视化工具</strong></li> 
</ul> 
<p>新的拖放可视化工具让用户可以更快速、更直观地生成不同类型的可视化。用户可以拖放数据字段以生成折线图、条形图、面状图和度量图。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0915/174515_uqZ1_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch-build%2Fblob%2Fmain%2Frelease-notes%2Fopensearch-release-notes-2.3.0.md" target="_blank">详情查看 Release Note</a>。</p>
                                        </div>
                                      
</div>
            