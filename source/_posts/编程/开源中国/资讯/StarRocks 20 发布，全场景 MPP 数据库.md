
---
title: 'StarRocks 2.0 发布，全场景 MPP 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0105/102138_UmfA_5430600.png'
author: 开源中国
comments: false
date: Wed, 05 Jan 2022 02:30:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0105/102138_UmfA_5430600.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>2021年1月底，StarRocks 向量化1.0版本首次面市，新产品刚“呱呱坠地”，就具备了和全球最快开源系统不相上下的单表查询性能。而新版本的 StarRocks 2.0 又具备哪些特性呢？一起来看一下：</p> 
<h2>单表极速查询</h2> 
<p>最近一年，StarRocks一直在致力于重新定义单表极速查询速度，在 2.0 版本中，StarRocks 创新性的实现了基于全局字典的低基数字符串查询优化，进行了大量 CPU 指令级优化，等等。<strong>在单表查询场景下，2.0版本的性能可以达到老版本的2倍左右</strong>，也实现了对原有“世界最快开源系统”的大幅超越。</p> 
<p><img alt height="343" src="https://static.oschina.net/uploads/space/2022/0105/102138_UmfA_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p><strong>*测试环境：StarRocks 1FE 3BE ，版本1.19及2.0；ClickHouse 同等配置的3节点，版本21.9</strong></p> 
<h2>CBO 优化器</h2> 
<p>2019年12月，为了让用户无需复杂预处理，直接基于多表数据获取极速分析体验，StarRocks 开启了自我颠覆之路：全新编写一个 CBO 优化器（基于代价的优化器）。</p> 
<p>经过一年多的攻坚克难，2.0 版本的 CBO 优化器已经基本成熟，对更多的多表复杂查询类型可以实现2倍性能提升，完善性和稳定性也大幅提升。相比其他开源系统，可以实现5-10倍的性能优势。</p> 
<h2>Primay Key 实时更新</h2> 
<p>之前 OLAP 系统往往采用 merge-on-read 的模式来完成数据更新，但这种大幅牺牲了查询性能去换取较好的导入性能做法并不是最佳方案。于是 Primary Key 模型闪亮登场！新的存储引擎采用了 delete-and-insert 的方式完成数据更新，可以在实时更新场景下带来了 3-10 倍的查询性能提升。</p> 
<p>经过 6 个月的打磨，2.0 版本正式发布 Primay Key 实时更新特性。用户再也不用为“实时更新”而头痛不已！</p> 
<h2>稳定性问题</h2> 
<p>稳定性是用户大规模使用的根基，近半年来， StarRocks 一直在不遗余力的全面解决稳定性问题。在 2.0 版本中重新设计了内存管理模式，将根本性解决了 BE OOM 的问题。</p>
                                        </div>
                                      
</div>
            