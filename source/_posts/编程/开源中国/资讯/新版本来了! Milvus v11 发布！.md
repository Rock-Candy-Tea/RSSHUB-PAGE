
---
title: '新版本来了! Milvus v1.1 发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/d824a195-8909-4ffb-a7d6-03ec91052016.jpg'
author: 开源中国
comments: false
date: Mon, 17 May 2021 14:15:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/d824a195-8909-4ffb-a7d6-03ec91052016.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img src="https://oscimg.oschina.net/oscnet/d824a195-8909-4ffb-a7d6-03ec91052016.jpg" referrerpolicy="no-referrer"></p> 
<p>在 Milvus 1.0 版本发布后的 2 个月，2021 年 5 月 7 日，Milvus 正式发布了 1.1 版本！</p> 
<p>Milvus 1.1 版本新增诸多优化改进，修复大量漏洞，进一步丰富和完善了 Milvus 第一个长期支持（LTS）版本[1]。 以下是 Milvus 1.1 发版说明，想了解更多详情，请见 Milvus GitHub： https://github.com/milvus-io/milvus/releases/tag/v1.1.0 。如需做数据迁移的朋友，可使用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMDI5OTA5NQ%3D%3D%26mid%3D2247488167%26idx%3D1%26sn%3D6ad455b6e442d0685f73232f5978dd6f%26chksm%3Dfa52b31fcd253a0971a8880e0b6281ea05fb59877881978917b570cee9406885af3828844654%26scene%3D21%23wechat_redirect" target="_blank">Milvus 数据迁移工具 -- Milvusdm</a>。</p> 
<p>特别感谢以下社区贡献者，为此版本添砖加瓦：</p> 
<p><strong> </strong><strong>@BossZou</strong><strong> </strong><strong>@shengjun1985</strong><strong> </strong><strong>@op-hunter</strong><strong> </strong> <strong>@matrixji</strong><strong> </strong><strong>@yhmo</strong><strong> </strong> <strong>@ericsyh</strong><strong> </strong><strong>@LocoRichard</strong><strong> </strong><strong>@del-zhenwu</strong><strong> </strong><strong>@XuanYang-cn</strong><strong> </strong> <strong>@fishpenguin</strong></p> 
<h1><strong>发版说明</strong></h1> 
<p><img src="https://oscimg.oschina.net/oscnet/0a2ae9d5-0517-4b25-9224-65c28db4c1ee.png" referrerpolicy="no-referrer"></p> 
<p><strong>New Features</strong></p> 
<ul> 
 <li> <p>#4564 Supports specifying partition in a get_entity_by_id() method call.</p> </li> 
 <li> <p>#4806 Supports specifying partition in a delete_entity_by_id() method call.</p> </li> 
 <li> <p>#4905 Adds the release_collection() method, which unloads a specific collection from cache.</p> </li> 
</ul> 
<p><strong>Improvements</strong></p> 
<ul> 
 <li> <p>#4756 Improves the performance of the get_entity_by_id() method call.</p> </li> 
 <li> <p>#4856 Upgrades hnswlib to v0.5.0.</p> </li> 
 <li> <p>#4958 Improves the performance of IVF index training.</p> </li> 
</ul> 
<p><strong>Fixed issues</strong></p> 
<ul> 
 <li> <p>#4778 Fails to access vector index in Mishards.</p> </li> 
 <li> <p>#4797 The system returns false results after merging search requests with different topK parameters.</p> </li> 
 <li> <p>#4838 The server does not respond immediately to an index building request on an empty collection.</p> </li> 
 <li> <p>#4858 For GPU-enabled Milvus, the system crashes on a search request with a large topK (> 2048).</p> </li> 
 <li> <p>#4862 A read-only node merges segments during startup.</p> </li> 
 <li> <p>#4894 The capacity of a Bloom filter does not equal to the row count of the segment it belongs to.</p> </li> 
 <li> <p>#4908 The GPU cache is not cleaned up after a collection is dropped.</p> </li> 
 <li> <p>#4933 It takes a long while for the system to build index for a small segment.</p> </li> 
 <li> <p>#4952 Fails to set timezone as "UTC + 5:30".</p> </li> 
 <li> <p>#5008 The system crashes randomly during continuous, concurrent delete, insert, and search operations.</p> </li> 
 <li> <p>#5010 For GPU-enabled Milvus, query fails on IVF_PQ if nbits ≠ 8.</p> </li> 
 <li> <p>#5050 get_collection_stats() returns false index type for segments still in the process of index building.</p> </li> 
 <li> <p>#5063 The system crashes when an empty segment is flushed.</p> </li> 
 <li> <p>#5078 For GPU-enabled Milvus, the system crashes when creating an IVF index on vectors of 2048, 4096, or 8192 dimensions.</p> </li> 
</ul> 
<h2><strong>备注</strong></h2> 
<h2>[1] Milvus 长期版本定义：https://milvus.io/cn/docs/v1.1.0/announcement.md</h2> 
<h2><strong>About Zilliz</strong></h2> 
<p>Zilliz 以重新定义数据科学为愿景，致力于打造一家全球领先的开源技术创新公司，并通过开源和云原生解决方案为企业解锁非结构化数据的隐藏价值。 </p> 
<p>Zilliz 构建了 Milvus 向量相似度搜索引擎，以加快下一代数据平台的发展。Milvus 目前是 LF AI & Data 基金会的孵化阶段项目，能够管理大量非结构化数据集。我们的技术在新药发现、计算机视觉、推荐引擎、聊天机器人等方面具有广泛的应用。 </p>
                                        </div>
                                      
</div>
            