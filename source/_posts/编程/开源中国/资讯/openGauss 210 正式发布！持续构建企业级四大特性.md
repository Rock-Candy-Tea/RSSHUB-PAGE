
---
title: 'openGauss 2.1.0 正式发布！持续构建企业级四大特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-18aaede60cc336edec29b5590309cdb45d5.png'
author: 开源中国
comments: false
date: Fri, 01 Oct 2021 07:29:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-18aaede60cc336edec29b5590309cdb45d5.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong style="color:#333333">openGauss 2.1.0版本正式上线！</strong><span style="background-color:#ffffff; color:#333333">openGauss 2.1.0 版本是openGauss社区继1.1.0之后发布的又一个创新版本。2.1.0版本持续在企业级能力构建上发力，在高性能、高安全、高可用和智能化方面都有重大突破。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-18aaede60cc336edec29b5590309cdb45d5.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px"><strong>稳定高性能 数据高效处理</strong></h3> 
<p style="margin-left:0; margin-right:0"><strong>1.鲲鹏单机性能持续优化</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">单机鲲鹏2P TPCC 180万tpmC。(每分钟处理交易量，被业界广泛用于衡量计算机系统的事务处理能力），满足1.5倍线性度，当前openGauss基于鲲鹏4路服务器的中国移动数据库性能测试排名绝对领先。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">长稳运行1h,性能劣化不超过5%。</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>2.支持In-place Update存储引擎</strong></p> 
<p style="margin-left:0; margin-right:0">In-place Update存储引擎（原地更新），是<span>openGaus内核新增的一种存储模式。openGauss 内核此前的版本使用的行存储引擎是AppendUpdate（追加更新）模式。追加更新对于业务中的增、删以及HOT(HeapOnlyTuple) Update(即同一页面内更新)有很好的表现，但对于跨数据页面的非HOTUPDATE场景，垃圾回收不够高效，In-place Update存储引擎可很好解决上述问题，同时可实现基于NUMA-Ware架构的高可扩展UNDO子系统以及基于多版本的索引技术。</span></p> 
<h3 style="margin-left:0px; margin-right:0px"><strong>安全可信 保护数据资产</strong></h3> 
<p style="margin-left:0; margin-right:0"><strong>1.原生多方共识，可信，防篡改</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">防篡改账本数据库，实现防篡改账本数据库,新增防篡改用户历史表和全局区块表,对指定防篡改Schema中的表进行操作审计；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">透明加密,对应用层无感知,相比不加密,性能劣化不超过10%；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">全密态数据库增强，密态等值查询支持JDBC、存储过程和函数。</p> </li> 
 <li> <p>支持国密算法认证，支持SM3国密算法，ODBC，JDBC支持SM3认证方式，提供国密SM4算法的加解密的API接口</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>2.可信构建，支持cmake脚本编译</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>Paxos进一步增强高可用能力</strong></p> 
<p style="margin-left:0; margin-right:0">基于Paxos分布式一致性协议的日志复制及选主框架。支持在线添加、删除节点，在线转让Leader能力，支持优先级选主和策略化多数派。支持节点角色多样性，拥有高效流控算法。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">通过自仲裁、多数派选主能力摆脱第三方仲裁组件，极大缩短RTO时间，且可预防任何故障下的脑裂双主；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持节点同步、同异步混合部署的多集群部署模式；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提升主备间节点日志复制效率，提升系统的最大吞吐能力。借助openGauss的DCF高可用组件，用户不仅可以免去系统脑裂的风险，还可以提升系统性能。</p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px"><strong>DB for AI 数据业务智能</strong></h3> 
<p style="margin-left:0; margin-right:0"><strong>1.内置多种ML算法</strong></p> 
<p style="margin-left:0; margin-right:0">openGauss AI能力增强:提供单语句慢SQL根因诊断能力，增强智能索引推荐、时序预测等能力。</p> 
<p style="margin-left:0; margin-right:0"><strong>2.库内训练推理，性能超MADlib 10倍</strong></p> 
<p style="margin-left:0; margin-right:0">DB4AI能力:提供fenced UDF能力;提供数据库原生DB4AI库内算法能力,包括库内执行计划、库内算子及SQL语法;</p> 
<p style="margin-left:0; margin-right:0">2.1.0版本除了在以上四大特性方面有持续创新升级以外，也新增众多其他新特性，积极完善相关生态工具。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">SQL引擎能力增强；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">存储过程兼容性增强；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持段页式存储；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JDBC客户端负载均衡及读写分离；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">列存支持主键唯一键约束；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持jsonb；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">自定义规则数据动态脱敏；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持Hash索引；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Data Studio工具提供多个支持；</p> <p style="margin-left:0; margin-right:0"><strong>......</strong></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">openGauss社区开源一年多以来，openGauss社区按照规划如期发布1.0.0、1.0.1、1.1.0、2.0.0和2.1.0版本 ，openGauss的企业级能力得到持续的发展和突破，这都是2026名开发者的不懈努力和奋斗的成果。此外，还有以GIS、AI、In-place Update、Infra等活跃的SIG，积极贡献相关能力，增强了openGauss整体竞争力。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-10b0260710e16423e509d3bf783b81445d9.png" referrerpolicy="no-referrer"></p> 
<p>9月25日，在华为全联接2021大会上，openGauss社区理事会正式宣布成立。openGauss 社区理事会作为社区的决策机构和领导机构，未来也将指导openGauss能力构建等事宜。以社区理事会的成立为新征程起点， openGauss将持续聚焦数据库根技术，以开源协作创新，为业界带来持续领先的数据库技术与产品。</p> 
<p style="margin-left:0; margin-right:0">在这普天同庆的日子里，openGauss社区祝大家国庆快乐!</p> 
<hr> 
<p><strong style="color:#333333">欢迎访问openGauss官方网站</strong></p> 
<p style="color:#a0a0a0; margin-left:0; margin-right:0; text-align:justify"><span style="color:#000000">openGauss开源社区官方网站：</span></p> 
<p style="color:#a0a0a0; margin-left:0; margin-right:0; text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopengauss.org" target="_blank">https://opengauss.org</a></p> 
<p style="color:#a0a0a0; margin-left:0; margin-right:0; text-align:justify"><span style="color:#000000">openGauss组织仓库：</span></p> 
<p style="color:#a0a0a0; margin-left:0; margin-right:0; text-align:justify"><a href="https://gitee.com/opengauss">https://gitee.com/opengauss</a></p> 
<p style="color:#a0a0a0; margin-left:0; margin-right:0; text-align:justify"><span style="color:#000000">openGauss镜像仓库：</span></p> 
<p style="color:#a0a0a0; margin-left:0; margin-right:0; text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopengauss-mirror" target="_blank">https://github.com/opengauss-mirror</a></p>
                                        </div>
                                      
</div>
            