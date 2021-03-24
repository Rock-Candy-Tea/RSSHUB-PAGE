
---
title: 'Nebula Graph v2.0 GA，支持全文索引和 String 类型 VID'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7019'
author: 开源中国
comments: false
date: Wed, 24 Mar 2021 11:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7019'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">Nebula Graph v2.0 GA 发布了。该版本增强了 nGQL 表达能力，提高了带索引数据插入性能，逐步兼容 openCypher。</p> 
<h2 style="text-align:start">Nebula Graph</h2> 
<h3 style="text-align:start">New Features</h3> 
<ul> 
 <li>vertexID 支持 Integer 和 String 类型</li> 
 <li>新增数据类型 
  <ul> 
   <li>NULL：支持 NULL，支持为属性增加 NOT NULL 约束</li> 
   <li>复合类型：List，Set 和 Map（不支持定义为属性类型）</li> 
   <li>时间类型：DATE 和 DATETIME</li> 
  </ul> </li> 
 <li>全文索引</li> 
 <li>Explain & Profile 执行计划分析</li> 
 <li>子图</li> 
 <li>支持对图空间进行数据统计</li> 
 <li>OpenCypher 
  <ul> 
   <li>部分支持 MATCH 语句</li> 
   <li>支持 RETURN, WITH, UNWIND, LIMIT & SKIP 等语句</li> 
  </ul> </li> 
 <li>支持更多内置函数 
  <ul> 
   <li>谓词函数，聚合函数，标量函数，List 函数，数学函数，字符串函数和时间函数等</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">Improvement</h3> 
<ul> 
 <li>提升了带索引数据的插入、删除、更新性能</li> 
 <li>增强路径查找能力：支持正向、反向、双向查找，支持去除环路。</li> 
 <li>增强运维操作。支持查看 graph/meta/storage 服务信息</li> 
</ul> 
<h3 style="text-align:start">Changelog</h3> 
<ul> 
 <li>创建图空间时需指定 vertexID 类型</li> 
 <li>FETCH PROP ON 返回复合结构</li> 
 <li>metad、graphd 和 storaged 默认端口发生了变化</li> 
 <li>重构了 metrics，监控项更合理</li> 
</ul> 
<h2 style="text-align:start">Nebula-graph Console</h2> 
<ul> 
 <li>支持 local command 模式，比如，:set csv 命令可将查询结果导出为 CSV 文件。详情请参见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-console" target="_blank">nebula-console</a></li> 
</ul> 
<h3 style="text-align:start">Clients</h3> 
<p style="text-align:start">客户端支持连接池和负载均衡</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-cpp" target="_blank">CPP client</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-java" target="_blank">Java client</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-python" target="_blank">Python client</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-go" target="_blank">Go client</a></li> 
</ul> 
<h2 style="text-align:start">Nebula Graph Studio</h2> 
<p style="text-align:start">支持可视化建模、数据导入、图探索和控制台查询。详情请见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-web-docker" target="_blank">nebula-web-docker</a></p> 
<h2 style="text-align:start">已知问题</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fissues%2F860" target="_blank">#860</a></li> 
</ul> 
<h2 style="text-align:start">如何升级</h2> 
<p style="text-align:start">请参见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-docs-cn%2Fblob%2Fmaster%2Fdocs-2.0%2F4.deployment-and-installation%2F3.upgrade-nebula-graph.md" target="_blank">https://github.com/vesoft-inc/nebula-docs-cn/blob/master/docs-2.0/4.deployment-and-installation/3.upgrade-nebula-graph.md</a></p>
                                        </div>
                                      
</div>
            