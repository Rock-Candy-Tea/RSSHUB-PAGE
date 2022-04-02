
---
title: '持续精进，性能突破，openGauss 3.0 社区版正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0402/175115_hXWX_5430600.png'
author: 开源中国
comments: false
date: Sat, 02 Apr 2022 09:53:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0402/175115_hXWX_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0; text-align:left"><span><span><span>4</span><span>月1日，openGauss 开源数据库社区，发布了最新 3.0 社区版，并同步开放供业界下载。它是继2.0版本后，又一个面向行业客户核心业务场景提供的具有里程碑意义的版本。</span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><span>本次3.0版本历时半年，openGauss社区生态紧密合作，协同研发，累计收到超过1600个PR，3500次代码提交，其中社区贡献占比已超过45%，优化和新增上百项新特性和能力，标志着openGauss社区开源协同又上一个新台阶。此外，3.0版本首次把openGauss架构由集中式扩展到分布式，16节点达到1000万tpmC，突破单机性能；增加轻量化部署能力，应对资源受限的应用环境，同时保留大部分服务器版本能力，为行业客户提供更多选择。</span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><strong><span><span>1</span></span></strong><strong><span><span>．从集中式走向分布式，性能突破，16节点1000万tpmC</span></span></strong> </span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><span>3.0</span><span>版本进一步加强社区生态伙伴合作，与Apache基金会的ShardingSphere 联合研发，推出openGauss分布式解决方案，双方在系统架构，数据分片效率，弹性伸缩等方面紧密合作，深度优化，充分释放openGauss性能潜力，最终达成在鲲鹏服务器上，16节点性能超过1000万tpmC的优异成绩。实现计算与存储能力线性扩展，数据节点平滑扩容，智能负载均衡等能力。此外还支持K8S一键批量部署、管理、运维和升级，支持微服务和云原生。</span></span></span></p> 
<p><img height="394" src="https://static.oschina.net/uploads/space/2022/0402/175115_hXWX_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><strong><span><span>2. </span></span></strong><strong><span><span>轻量化面向边缘应用场景，云边数据协同</span></span></strong></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><span>openGauss 3.0</span><span>版本把能力进一步下沉到边缘，带来<strong>轻量化</strong>部署能力，匹配计算资源受限的场景。轻量化版本在保留“四高”大部分核心能力的同时，大幅降低安装部署门槛。安装包缩小到50M，內存底噪下降66%。引入的多模态引擎插件框架，使未来支持更多种数据模型处理成为可能，同时提供的内存管理优化算法，可以高效使用内存资源，提升openGauss适应复杂边缘场景的能力。openGauss轻量化与服务器版本同內核、同架构，在实际应用中可以形成云边协同，数据无需转换，高效流转，端到端数据保密安全。</span></span></span></p> 
<p><img height="394" src="https://static.oschina.net/uploads/space/2022/0402/175142_DhPV_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><strong><span><span>3. </span></span></strong><strong><span><span>「四高」能力持续提升</span></span></strong></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><span>除以上分布式和轻量化以外，在“<strong>四高</strong>”（高性能、高可用、高安全、高智能）优势领域持续增强。以下为本次版本中发布的能力亮点。</span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><strong><span>高性能 创新舒心</span></strong><span>：</span></span></span></p> 
<ol start="12" style="list-style-type:lower-alpha"> 
 <li style="text-align:left" value="50"><span><span><span><span>分布式解决方案达成16节点1000万tpmC，性能业界领先</span></span></span></span></li> 
 <li style="text-align:left" value="50"><span><span><span><span>行存转向量化等技术引入，支持混合负载性能提升30%</span></span></span></span></li> 
 <li style="text-align:left" value="50"><span><span><span><span>多表关联处理时，外键增强，并发能力提升1倍</span></span></span></span></li> 
</ol> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><strong><span>高可用 业务安心</span></strong><span>：</span></span></span></p> 
<ol start="12" style="list-style-type:lower-alpha"> 
 <li style="text-align:left" value="50"><span><span><span><span>开源发布最佳匹配openGauss的集群管理软件</span></span></span></span></li> 
 <li style="text-align:left" value="50"><span><span><span><span>系统表全局syscache, 降低高负载时內存占用率80%</span></span></span></span></li> 
 <li style="text-align:left" value="50"><span><span><span><span>支持备机归档备份，降低主机负载，提升业务稳定性</span></span></span></span></li> 
</ol> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><strong><span>高安全 数据安心</span></strong><span>：</span></span></span></p> 
<ol start="12" style="list-style-type:lower-alpha"> 
 <li style="text-align:left" value="50"><span><span><span><span>符合数据库评级EAL4+最高安全标准</span></span></span></span></li> 
 <li style="text-align:left" value="50"><span><span><span><span>支持国密算法，符合国家信息安全规范与要求</span></span></span></span></li> 
 <li style="text-align:left" value="50"><span><span><span><span>细粒度、精细化权限控制，审计功能增强</span></span></span></span></li> 
</ol> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><strong><span>高智能 管理省心</span></strong><span>：</span></span></span></p> 
<ol start="12" style="list-style-type:lower-alpha"> 
 <li style="text-align:left" value="50"><span><span><span><span>提供业界领先的AI能力，让数据更智能</span></span></span></span></li> 
 <li style="text-align:left" value="50"><span><span><span><span>AI4DB</span></span><span><span>慢SQL诊断，稳定性、分析粒度算法增强，支持高效调优</span></span></span></span></li> 
 <li style="text-align:left" value="50"><span><span><span><span>DB4AI</span></span><span><span>增加更多算法支持，提升ML，数据分析与挖掘等综合表现</span></span></span></span></li> 
</ol> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><strong><span><span>4. </span></span></strong><strong><span><span>工具链持续丰富和兼容性进一步提升</span></span></strong></span></span></p> 
<ol start="12" style="list-style-type:lower-alpha"> 
 <li style="text-align:left" value="50"><span><span><span><span>首推SQL引擎插件化框架，提升对主流数据库兼容性，降低开发者开发难度</span></span></span></span></li> 
 <li style="text-align:left" value="50"><span><span><span><span>可视化openGauss管理工具Data Studio正式开源，最佳支持openGauss內核特色能力，提升管理效率与使用体验</span></span></span></span></li> 
 <li style="text-align:left" value="50"><span><span><span><span>数据迁移能力提升，保持数据完整性、准确性，同时提升迁移性能100%</span></span></span></span></li> 
</ol> 
<p style="margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><span>万物智能，数字原生正在重构物理世界，数据库作为数字世界的基础软件，面临前所未有的挑战。openGauss旨在联合产业链上下游，共同打造面向数字世界的开源数据库。3.0的发布是发展历程中重要版本，也是向下一个更高目标前进的起点。相信在openGauss社区的大平台上，在生机勃勃的openGauss开源生态中，openGauss未来将会在广阔的数字世界大有可为。</span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><span>openGauss</span><span>持续精进，向上生长！</span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><span>openGauss3.0</span><span>版本下载地址：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhttps%3A%2F%2Fopengauss.org%2Fzh%2Fdownload.html" target="_blank"> https://opengauss.org/zh/download.html</a></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><img height="150" src="https://static.oschina.net/uploads/space/2022/0402/175221_dcLt_5430600.png" width="150" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><span>openGauss3.0</span><span>版本发布说明：</span><span style="color:#0563c1"><u><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopengauss.org%2Fzh%2Fdocs%2F3.0.0%2Fdocs%2FReleasenotes%2FReleasenotes.html" target="_blank">https://opengauss.org/zh/docs/3.0.0/docs/Releasenotes/Releasenotes.html</a></u></span></span></span></p> 
<p><img height="150" src="https://static.oschina.net/uploads/space/2022/0402/175233_l15u_5430600.png" width="150" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><strong><span>关于openGauss社区</span></strong></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><span>openGauss</span><span>是一款开源关系型通用数据库，源于华为在数据库领域十几年的积累，面向企业核心业务场景，除提供企业级数据库能力，还提供极致的业务处理性能，业界领先的数据安全保护能力，金融级可靠性和数据智能，并已在电信、金融、能源等关键行业的核心系统中得到广泛应用。</span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><span>开源社区是openGauss的重要创新平台，提供openGauss与开发者、用户、产业伙伴联接的桥梁。欢迎加入社区，通过协同贡献、积极探索、共同打造世界级的企业级开源数据库。</span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><strong><span><span><span>社区二维码</span></span></span></strong></p> 
<p><img height="150" src="https://static.oschina.net/uploads/space/2022/0402/175257_cpzH_5430600.png" width="150" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            