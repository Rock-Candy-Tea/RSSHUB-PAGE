
---
title: 'openLooKeng v1.4.1 上线，OmniData Connector 来了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a98112dd5cabf1dc50436d9c533421334f7.jpg'
author: 开源中国
comments: false
date: Mon, 15 Nov 2021 10:38:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a98112dd5cabf1dc50436d9c533421334f7.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>前言</h2> 
<p>前不久，在Hadoop、openLooKeng联合发起的Apache Hadoop Meetup 2021上，社区 PMC 主席 Ken Zhang 分享了主题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU0MTQyMDc4OA%3D%3D%26mid%3D2247492976%26idx%3D1%26sn%3D7c8e8ae226ee63b02d2b615054e3ece2%26chksm%3Dfb2898ebcc5f11fdd7cb79f09be01e048b3418134c44d394449bd59ee7fc06d181fe5d8c5035%26token%3D670561351%26lang%3Dzh_CN%23rd" target="_blank">openLooKeng and the technical trend of big data（点此回顾）</a>，其中OmniRuntime 受到不少朋友的关注。11月12日，<strong>openLooKeng v1.4.1正式上线</strong>。除了对旧版本进行一些优化外，v1.4.1版本还引入了<strong>OmniData Connector</strong>。作为OmniRuntime的组件之一，OmniData 有什么作用？小助手将为大家娓娓道来。</p> 
<h2>关于 OmniData</h2> 
<p>OmniData 算子下推特性，适用于大数据存算分离场景或大规模融合部署场景。当大量计算节点从存储节点读取数据时，大量原始数据从存储节点通过网络传输到计算节点进行处理，有效数据占比低，极大浪费网络带宽。OmniData旨在减少数据存储层和计算层之间的数据传输。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a98112dd5cabf1dc50436d9c533421334f7.jpg" referrerpolicy="no-referrer"></p> 
<p>此外，OmniData算子下推特性将计算侧的Filter、Aggregation、Limit算子下推到存储节点执行，实现近数据计算，并利用多样算力缓解计算侧CPU的压力。OmniData服务将算子处理结果通过网络传输到计算节点，从而减少无效数据在网络上的传输，有效提升大数据计算性能。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e81570f7bcaff953268536ead3903afcbe0.jpg" referrerpolicy="no-referrer"></p> 
<h2>OmniData适用范围</h2> 
<ol> 
 <li> <p>支持openLooKeng v1.4.0和Spark 3.0.0，提供对应的引擎侧OmniData插件。</p> </li> 
 <li> <p>支持算子下推到HDFS，支持S3的存储访问接口。</p> </li> 
 <li> <p>支持数据格式包括：TXT、ORC、Parquet。</p> </li> 
 <li> <p>TaiShan服务器，支持鲲鹏处理器的体系架构。</p> </li> 
</ol> 
<p>OmniData在大数据存算分离场景或大规模融合场景的适用性，极大符合openLooKeng的愿景：让大数据更简单。OmniData特性的引入，将进一步提升openLooKeng引擎性能。</p> 
<p>OmniData Connector更多详情请参考：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenlookeng.io%2Fdocs%2Fdocs%2Fconnector%2Fomnidata.html" target="_blank">https://openlookeng.io/docs/docs/connector/omnidata.html</a></p> 
<p>OmniData更多详情请参考：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hikunpeng.com%2Fzh%2Fdeveloper%2Fboostkit%2Fbig-data%3Faccelerated%3D3" target="_blank">https://www.hikunpeng.com/zh/developer/boostkit/big-data?accelerated=3</a></p> 
<hr> 
<h2>openLooKeng v1.4.1 其他优化</h2> 
<p><strong>ARM 架构下支持JDK8</strong></p> 
<p>消除因JDK卡顿问题导致ARM架构下对java版本的强制要求，支持ARM架构下使用jdk1.8.262及以上版本。</p> 
<hr> 
<p>欢迎下载并使用openLooKeng新版本: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenlookeng.io%2Fzh-cn%2Fdownload.html" target="_blank">https://openlookeng.io/zh-cn/download.html</a></p> 
<p>如果您有任何体验感受与建议，欢迎在openLooKeng代码仓上提Issue，或发邮件至users@openlookeng.io告知我们。您的声音或将成为openLooKeng引擎性能提升的关键。</p> 
<p>openLooKeng代码仓地址: <a href="https://gitee.com/openlookeng">https://gitee.com/openlookeng</a></p> 
<p>openLooKeng, Make Big Data Simplified</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-65348f2becb8e1fa6352a3dfc655bde4a7d.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            