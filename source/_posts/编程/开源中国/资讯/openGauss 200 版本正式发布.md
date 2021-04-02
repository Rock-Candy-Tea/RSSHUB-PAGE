
---
title: 'openGauss 2.0.0 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/ad978659-81c1-4fda-b169-4f0dc795bd37.png'
author: 开源中国
comments: false
date: Fri, 02 Apr 2021 15:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/ad978659-81c1-4fda-b169-4f0dc795bd37.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>2.0.0版本来啦！</strong></p> 
<p>3月31日，openGauss 2.0.0 版本正式上线！</p> 
<p>openGauss 2.0.0 是openGauss社区发布的第一个Release版本。2.0.0版本与之前版本保持兼容的同时，也新增了众多特性，特别是在高性能、高安全和智能化的打造上有了更大的突破。</p> 
<h1><strong>01 鲲鹏NUMA架构优化，实现性能业界领先</strong></h1> 
<table cellspacing="0"> 
 <tbody> 
  <tr> 
   <td style="vertical-align:center"> <p><strong>openGauss</strong></p> </td> 
   <td style="vertical-align:center"> <p><strong>2P</strong></p> </td> 
   <td style="vertical-align:center"> <p><strong>4P</strong></p> </td> 
   <td style="vertical-align:center"> <p><strong>线性度</strong></p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:center"> <p><strong>架构优化后</strong></p> </td> 
   <td style="vertical-align:center"> <p><strong>150</strong></p> </td> 
   <td style="vertical-align:center"> <p><strong>230</strong></p> </td> 
   <td style="vertical-align:center"> <p><strong>150%</strong></p> </td> 
  </tr> 
 </tbody> 
</table> 
<p>4P鲲鹏性能达到230万tpmC（每分钟处理交易量，被业界广泛用于衡量计算机系统的事务处理能力），满足1.5倍线性度，单机TP性能保持业界领先，同时也证明了openGauss足以支撑金融行业新核心业务系统场景。</p> 
<ul> 
 <li> <p>openGauss根据鲲鹏处理器的多核NUMA架构特点，进行了一系列针对NUMA架构特性的相关优化。一方面降低了跨核内存访问的时延问题，另一方面充分发挥了鲲鹏多核算力优势，通过日志无锁并行插入、SQL ByPass、动态剪枝等关键技术，大幅提升交易型负载系统的处理性能。</p> </li> 
 <li> <p>openGauss基于鲲鹏920所使用的架构利用LSE扩展指令集实现高效的原子操作，有效提升CPU利用率，从而提升线程间同步性能、XLog写入性能等。</p> </li> 
 <li> <p>openGauss基于鲲鹏920提供的L3缓存CacheLine，实现热点数据访问优化，有效提高缓存访问命中率，降低Cache缓存一致性维护开销，大幅提升系统整体的数据访问性能。</p> </li> 
</ul> 
<h1><strong>02 全密态、AI特性加持，引领数据库发展新方向</strong></h1> 
<h2><strong>2.1 </strong><strong>突破纯软数据密文查询和计算关键技术，提供性能更优的全密态检索方案</strong></h2> 
<ul> 
 <li> <p>全密态数据处理(含数据密态插入、更新、表达式等值过滤），性能劣化不超过5%。</p> </li> 
 <li> <p>密态等值查询落地openGauss，全面推进全密态技术标准行业落地，开放机密计算生态。</p> </li> 
</ul> 
<h2><strong>2.2 强化AI4DB的数据库自调优、自诊断能力，突破DB4AI原生库内机器学习机制</strong></h2> 
<ul> 
 <li> <p>索引推荐</p> </li> 
</ul> 
<p>有效解决90%以上因索引配置不当导致的慢查询；TPC-DS标准benchmark数据集下有60%的SQL语句可获得不同程度的性能提升。</p> 
<ul> 
 <li> <p>监控与异常检测</p> </li> 
</ul> 
<p>问题发现效率相比人工on-call提升1倍，在TPC-C标准benchmark数据集上验证发现人工注入故障场景下的问题召回率高达到90%以上。</p> 
<ul> 
 <li> <p>MADLib兼容</p> </li> 
</ul> 
<p>支持60+ MADLib生态的算法。</p> 
<h1><strong>03 新增众多企业级特性，持续构建openGauss数据库竞争力</strong></h1> 
<ul> 
 <li> <p>极简安装</p> </li> 
</ul> 
<p>极简版省去集群管理工具，直接提供数据库内核二进制文件，可以快速的启动数据库实例，安装配置简单，适合个人开发者使用。</p> 
<ul> 
 <li> <p>支持延迟备库</p> </li> 
</ul> 
<p>支持在备机延时指定的时间后恢复主机发来的XLOG日志，延时后的备机相当于提供了一份可查询的指定时间段前的数据副本，方便纠正过程操作错误。</p> 
<ul> 
 <li> <p>备机支持逻辑复制</p> </li> 
</ul> 
<p>支持外部DRS连接备机进行逻辑解码，降低主机压力。</p> 
<ul> 
 <li> <p>扩容工具优化</p> </li> 
</ul> 
<p>支持不停服在线扩容，同时支持备机和级联备扩容。</p> 
<ul> 
 <li> <p>灰度升级</p> </li> 
</ul> 
<p>优化升级工具，增加灰度升级能力，支持业务在线升级。可支持社区1.1.0版本灰度升级到2.0.0版本。</p> 
<ul> 
 <li> <p>备机IO写放大优化</p> </li> 
</ul> 
<p>优化备机IO，降低单次检查点刷盘IO量，有效解决auto vacuum/vacuum慢问题。</p> 
<ul> 
 <li> <p>WDR诊断报告</p> </li> 
</ul> 
<p>WDR诊断报告新增“Effective CPU”、“WalWrite NoWait”、“Soft Parse”、“Non-Parse CPU”四个数据库运行指标，提升系统DFx分析能力。</p> 
<ul> 
 <li> <p>Data Studio客户端工具特性</p> </li> 
</ul> 
<p>Data Studio对openGauss多个内核特性提供支持，包括：</p> 
<ul> 
 <li> <p>增加pldebugger调试功能。</p> </li> 
 <li> <p>增加pldebugger调试功能的回滚，在使用Data Studio调试前增加选项来保证调试函数在修改完数据后回退。</p> </li> 
 <li> <p>支持xml和serial(big|normal|small)类型。</p> </li> 
 <li> <p>支持在Data Studio中创建和展示外表对象。</p> </li> 
 <li> <p>列存表增加支持partial_cluster_key约束。</p> </li> 
 <li> <p>全局临时表支持DDL的展示和导出。</p> </li> 
 <li> <p>创建分区表支持LOCAL和GLOBAL标记。</p> </li> 
 <li> <p>增加MOT表的展示。</p> </li> 
</ul> 
<h1><strong>04 开放治理，多个伙伴加入社区，社区组织架构更加完善</strong></h1> 
<p>北京超图软件股份有限公司、北京优炫软件股份有限公司、北京快立方科技有限公司等公司已经签署CLA，正式加入openGauss社区，越来越多的力量加入到社区建设中来。</p> 
<p>截止目前openGauss已经成立包括OM、In-place Update、IoT、AI等11个专项兴趣小组（简称SIG），包括海量数据、云和恩墨、工商银行、清华大学等多个组织的成员发起或参与到社区的各个SIG小组，带领小组成员拓展技术方向，贡献新特性，实现下一个版本的技术规划。同时社区技术委员也开始运作，openGauss社区开放治理成架构日趋完善。</p> 
<p>经过半年多的发展和沉淀，openGauss无论从技术演进、社区生态建立、商业落地均已进入快速成长期，未来openGauss将围绕客户场景和需求持续构建更多竞争力，打造企业级数据库开源社区。</p> 
<h1><strong>05 感谢openGauss社区贡献者，让我们一起打造一个有温度的社区</strong></h1> 
<h1><img src="https://oscimg.oschina.net/oscnet/ad978659-81c1-4fda-b169-4f0dc795bd37.png" referrerpolicy="no-referrer"></h1> 
<p><strong>欢迎访问openGauss官方网站</strong></p> 
<ul> 
 <li>openGauss开源社区官方网站：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopengauss.org" target="_blank">https://opengauss.org</a></li> 
 <li>openGauss组织仓库：<a href="https://gitee.com/opengauss" target="_blank">https://gitee.com/opengauss</a></li> 
 <li>openGauss镜像仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopengauss-mirror" target="_blank">https://github.com/opengauss-mirror</a></li> 
</ul>
                                        </div>
                                      
</div>
            