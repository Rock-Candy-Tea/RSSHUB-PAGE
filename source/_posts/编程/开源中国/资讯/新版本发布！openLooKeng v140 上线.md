
---
title: '新版本发布！openLooKeng v1.4.0 上线'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=737'
author: 开源中国
comments: false
date: Fri, 22 Oct 2021 16:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=737'
---

<div>   
<div class="content">
                                                                    
                                                        <p>朋友们</p> 
<p>openLooKeng 新版本 v1.4.0 正式上线啦！</p> 
<p>2020年6月开源以来，每一次的迭代更新，openLooKeng均为用户提供了更为简单与可靠的数据分析体验。这也使得搭载openLooKeng的用户伙伴越来越多。也因为有来自ISV、政府，金融、互联网多个行业的支持，社区才愈加有活力。我们感谢用户与社区小伙伴的支持。</p> 
<p>金秋10月， openLooKeng 新版本 v1.4.0 正式发布。基于社区用户和开发者的体验和建议，新版本在原基础上进行了一些优化，以提升引擎性能。欢迎大家下载体验。</p> 
<h1>openLooKeng v1.4.0</h1> 
<h2>l Star Tree索引</h2> 
<p>Star Tree 索引提供一种预聚合技术，通过创建和管理用户所需要的不同的Cubes（多维数据集）来优化冰山查询的延时。在支持对大型Cubes的创建（10 Billion基数）的基础上，新版本1.4.0更新了APIs 接口，使得其能够支持 JDBC Connector使用 Cube，比如Clickhouse Connector。其它JDBC Connector 将陆续支持。</p> 
<h2>l 启发式索引</h2> 
<p>对启发式索引，新版本1.4.0 做了如下一些优化：</p> 
<p>a. 支持UPDATE INDEX。以往更改index时需要将其删除再创建。新版本1.4.0支持在原有的index上进行update操作；</p> 
<p>b. SHOW INDEX中增加index大小，内存和磁盘占用信息，以便用户更加合理地使用索引；</p> 
<p>c. Bloom index增加nmap cache来减少内存使用；</p> 
<p>d. 支持DROP TABLE的同时删除index；</p> 
<p>e. 支持创建index后自动加载index。</p> 
<h2>l Memory 连接器</h2> 
<p>修复了几个重要的错误，以解决大型数据集和特定运算符偶尔发生的错误结果。</p> 
<h2>l Task Recovery</h2> 
<p>修复了几个重要的错误，以解决高并发和worker节点故障期间偶尔发生的数据不一致问题。</p> 
<h2>l 低时延</h2> 
<p>a. 优化不包含join的点查sql的stats计算，加快查询速度；</p> 
<p>b. 新增自适应分片分组，提升高并发查询吞吐量；</p> 
<p>c. 支持非等式动态筛选器，以加快具有<、>、<= & >=等谓词的查询速度。</p> 
<h2>l 新增Kylin Connector</h2> 
<p>支持对Kylin数据源的访问查询。</p> 
<h2>l Yarn上部署openLooKeng</h2> 
<p>支持在Yarn容器上部署openLooKeng集群，当前支持部署单coordinator和多worker节点部署。</p> 
<hr> 
<p>以上便是新版本1.4.0 的优化。作为大数据的关键项目，openLooKeng一直致力于为用户提供极速极简的数据体验。如果您也关注大数据，欢迎下载体验openLooKeng。</p> 
<p>openLooKeng v1.4.0 下载地址</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenlookeng.io%2Fzh-cn%2Fdownload.html" target="_blank">https://openlookeng.io/zh-cn/download.html</a></p> 
<hr> 
<p>欢迎在openLooKeng gitee仓上提Issue，分享您的体验感受与建议，您的声音或将成为openLooKeng引擎性能提升的关键。</p> 
<p>· openLooKeng代码仓地址</p> 
<p><a href="https://gitee.com/openlookeng">https://gitee.com/openlookeng</a></p> 
<p>· 如果您对新版本V1.4.0有任何建议，欢迎发邮件至 <em><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ausers%40openlookeng.io" target="_blank">users@openlookeng.io</a></em> 告知我们。</p> 
<p>· openLooKeng社区官网</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenlookeng.io%2Fzh-cn%2F" target="_blank">https://openlookeng.io/zh-cn/</a></p>
                                        </div>
                                      
</div>
            