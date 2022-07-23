
---
title: '支持生产级共享文件存储，Curve v2.3.0 版本发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4745'
author: 开源中国
comments: false
date: Fri, 22 Jul 2022 14:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4745'
---

<div>   
<div class="content">
                                                                                            <p style="color:rgba(0, 0, 0, 0.85); margin-left:0; margin-right:0; text-align:left"><span style="color:#424b5d">为了能让用户使用</span><span style="color:#424b5d">到稳定可靠的 Curve 存储系统，我们在 v2.2.0 版本的基础上，进行了全方位的常规功能测试、混沌测试、性能测试、压力测试、长期稳定性测试等工作，并且将 CurveFS 文件存储上线到网易内部业务生产环境，经过一段时间的稳定运行考验后，我们发布了 v2.3.0 版本。</span></p> 
<p><span style="color:#424b5d">版本地址：</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencurve%2Fcurve%2Freleases%2Ftag%2Fv2.3.0-rc0" target="_blank"><span style="color:#424b5d">https://github.com/opencurve/curve/releases/tag/v2.3.0-rc0</span></a></p> 
<p><span style="color:#424b5d">版本部署手册：</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencurve%2Fcurveadm%2Fwiki" target="_blank"><span style="color:#424b5d">https://github.com/opencurve/curveadm/wiki</span></a><span style="color:#424b5d">‍</span></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span style="color:#888888">Curve 是云原生计算基金会 (CNCF) Sandbox 项目，是网易主导自研和开源的高性能、易运维、云原生的分布式存储系统，由块存储 CurveBS 和文件系统 CurveFS 两部分组成。</span></p> 
</blockquote> 
<h2><span style="color:#0052ff"><strong>重点增强</strong></span></h2> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#424b5d">v2.3.0 版本相比上个版本主要新增了共享文件存储服务能力，另外</span><strong><span style="color:#0052ff">块存储</span></strong><span style="color:#424b5d">服务方面也有如下增强：</span></p> 
<ul style="list-style-type:disc"> 
 <li> <p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#424b5d">io路径上去掉一次io落盘，提升io性能，在4k随机写场景下有</span><em><span style="color:#0052ff"><strong>100%性能提升</strong></span></em><span style="color:#424b5d"><em><em><strong style="color:#424b5d">①；</strong></em></em></span></p> </li> 
 <li> <p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#424b5d">在块设备层面支持卷的读写</span><strong><em><span style="color:#0052ff">权限控制</span></em></strong><span style="color:#424b5d"><em><strong style="color:#222222"><span style="color:#424b5d">②</span></strong></em>；</span></p> </li> 
</ul> 
<p><span style="color:#424b5d">与 CurveFS-v0.1.0 版比较，v2.3.0 在</span><span style="color:#0052ff"><strong>共享文件存储</strong></span><span style="color:#424b5d">服务方面新增了如下重要能力：</span></p> 
<ul style="list-style-type:disc"> 
 <li> <p><span style="color:#424b5d">功能</span></p> 
  <ul> 
   <li> <p><span style="color:#424b5d">支持多挂载</span></p> </li> 
   <li> <p><span style="color:#424b5d">支持 close-to-open 数据一致性</span></p> </li> 
   <li> <p><span style="color:#424b5d">支持 CurveBS 后端</span></p> </li> 
   <li> <p><span style="color:#424b5d">支持元数据 rocksdb 持久化</span></p> </li> 
   <li> <p><span style="color:#424b5d">支持 rename 事务化</span></p> </li> 
   <li> <p><span style="color:#424b5d">支持元数据集群自动化调度</span></p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#424b5d">性能</span></p> 
  <ul> 
   <li> <p style="margin-left:0; margin-right:0"><span style="color:#424b5d">open、du、stat、ls 等元数据操作性能优化</span></p> </li> 
   <li> <p style="margin-left:0; margin-right:0"><span style="color:#424b5d">s</span><span style="color:#424b5d">3 后端缓存满的情况下数据性能优化</span></p> </li> 
   <li> <p style="margin-left:0; margin-right:0"><span style="color:#424b5d">当前版本</span><span style="color:#0052ff"><em><strong>数据性能</strong></em></span><span style="color:#424b5d"><em><span style="color:#333333"><em><strong><span style="color:#424b5d">③</span></strong></em></span></em></span></p> </li> 
   <li> <p style="margin-left:0; margin-right:0"><span style="color:#424b5d">当前版本</span><span style="color:#0052ff"><em><strong>元数据性能</strong></em></span><span style="color:#424b5d"><strong><span style="background-color:#f7f7f7; color:#000000">④</span></strong></span></p> </li> 
  </ul> </li> 
 <li> <p><span style="color:#424b5d">监控</span></p> 
  <ul> 
   <li> <p><span style="color:#424b5d">全链路 metric 完善</span></p> </li> 
   <li> <p><span style="color:#424b5d">提供 grafana+promethues 一件部署脚本</span></p> </li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#424b5d"><span style="background-color:#ffffff; color:#424b5d">📢 </span><strong>release Notes</strong>：</span></p> 
<p><span style="background-color:#ffffff; color:#424b5d">https://github.com/opencurve/curve/blob/master/CHANGELOG-2.3.md</span></p> 
<h2><span style="color:#0052ff"><strong>适用场景</strong></span></h2> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#424b5d">我们基于 v2.3.0 版本在网易内部与多个业务团队进行了联合测试，也与竞品进行了对比测试，Curve 表现较好，已有部分业务在生产环境落地使用，下面简单介绍下相关业务的测试场景和 Curve 表现，同时也欢迎广大 Curve 社区小伙伴探索更多适用场景。</span></p> 
<h3 style="margin-left:0px; margin-right:0px"><span style="color:#0052ff"><strong><span style="color:#0052ff">AI 训练</span></strong></span></h3> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><u><strong><u>场景简述</u></strong></u><span style="color:#424b5d">：受限于硬件条件，我们基于 CPU 做了简单的单训练节点对比测试。使用 ImageNet-2012 数据集，resnet50 模型，商汤的</span><em><strong><span style="color:#0052ff">训练框架</span></strong></em><span style="color:#424b5d"><span style="background-color:#f7f7f7; color:#000000">⑤</span>进行训练，分别在本地盘，CurveFS，CephFS 上做了对比测试。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><u><strong>测试对比数据</strong></u><span style="color:#424b5d"><span style="color:#424b5d">：</span>取第一个 epoch 中1000轮 iter 的训练时间做对比，数据如下：</span></p> 
<table border="1" cellpadding="1" cellspacing="1" style="width:500px"> 
 <tbody> 
  <tr> 
   <td>文件系统</td> 
   <td><span style="color:#424b5d">本地文件系统ext4</span></td> 
   <td><span style="color:#424b5d">CurveFS</span></td> 
   <td><span style="color:#424b5d">CephFS</span></td> 
  </tr> 
  <tr> 
   <td><span style="color:#424b5d">1000轮iter的训练时间</span></td> 
   <td><span style="color:#424b5d">37mins</span></td> 
   <td><strong><span style="color:#424b5d">54mins</span></strong></td> 
   <td><span style="color:#424b5d">127mins</span></td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#424b5d">CurveFS 得益于缓存盘的优势，性能优于 CephFS，但由于当前的 lru 缓存策略，CurveFS 的性能低于本地盘。</span></p> 
<p><u><strong><u>下一步计划</u></strong></u><span style="color:#424b5d">：</span><span style="background-color:#ffffff; color:#424b5d">AI 场景用户涉及到的 IO 流程主要体现在：数据集制作（数据导入）、数据集元数据信息提取（ls -R获取元数据信息）、数据集训练（写少读多）。后续 CurveFS 会在这几个方面做针对性的优化：</span></p> 
<ul style="list-style-type:disc"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#424b5d">提高小文件并发写的吞吐；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#424b5d">优化元数据操作 ls<span> </span></span><span style="color:#424b5d">-R 的性能；</span></p> </li> 
 <li> <p><span style="color:#424b5d">支持目录、文件的预读功能；</span></p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px"><span style="color:#0052ff"><strong><span style="color:#0052ff">数据备份</span></strong></span></h3> 
<p><u><strong><u>场景简述</u></strong></u><span style="color:#424b5d">：</span><span style="color:#424b5d">网易内部有大量的 GitLab 代码库、数据库等的数据备份需求，此类场景的需求非常简单，业务最关注的是单位存储成本，对 IOPS、时延等性能要求不高，对大文件写入读取的吞吐带宽比较关注，对数据可靠性要求比较高。</span></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff; color:#424b5d">对象存储通常有标准、低频、归档、冷归档等存储类型，费用依次降低，但归档和冷归档存储中的数据需要先解冻才能访问。因此我们将业务备份的数据保存到对象存储系统的低频存储中，进一步节省备份数据的存储成本。</span></p> 
<p><span style="background-color:#ffffff; color:#424b5d"><u><strong>测试对比数据</strong></u><span style="color:#424b5d"><span style="color:#424b5d">：</span></span></span><span style="background-color:#ffffff; color:#424b5d">原有的备份系统通常是 RAID10 + 运维自建 NFS 服务方案，RAID10 是2倍的数据冗余，低频存储通常使用 EC 纠删码存储数据，可以将备份数据的冗余度从2倍降低到1.2倍左右，使用 Curve 共享文件存储系统可节省40%的存储空间，同时也免去了业务自行运维 NFS 的麻烦。</span></p> 
<p><span style="background-color:#ffffff; color:#424b5d"><u><strong><u>下一步计划</u></strong></u><span style="color:#424b5d">：</span></span></p> 
<ul style="list-style-type:disc"> 
 <li> <p><span style="background-color:#ffffff; color:#424b5d">继续优化大文件吞吐；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff; color:#424b5d">集团内部业务推广；</span></p> </li> 
 <li> <p><span style="background-color:#ffffff; color:#424b5d">支持将访问频次极低的数据存储到归档存储中，进一步降低备份数据的存储成本；</span></p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px"><span style="color:#0052ff"><strong><span style="color:#0052ff">ES 冷数据存储</span></strong></span></h3> 
<p><u><strong><u>场景简述</u></strong></u><span style="color:#424b5d">：</span><span style="color:#424b5d">据了解，由于 ES 的历史数据量通常很大，占用存储资源较多，为了节约存储成本，原有的 ES 冷数存储方案有2种：</span></p> 
<ul style="list-style-type:disc"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#424b5d">将n月以上的冷数据导出备份到 RAID 盘上（一般数据冗余比例为2）；历史数据查询流程很长，要先将备份数据读取上来进行恢复后才能查询；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff; color:#424b5d">另外一种方案是 ES 计算节点和存储节点混部，ES 应用层利用数据生命周期管理功能对冷数据进行不同的存储介质和副本数配置，但一般存储容量是瓶颈导致服务器浪费严重；</span></p> </li> 
</ul> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff; color:#424b5d">而使用 Curve 共享文件存储作为保存 elastic search 的冷数据，数据存储在集团内部对象存储服务中，使用的是低频存储形态（冗余副本比例为1.2）以便进一步降低单位存储成本。ES 节点上使用 curve-fuse 挂载文件系统（也可配置一块本地缓存盘进一步提升吞吐）即可开箱即用，不再需要考虑备份数据的恢复、本地文件系统容量问题和运维问题，只需要最小规模的计算节点即可（并且可以随时弹性伸缩），非常的方便。</span></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff; color:#424b5d"><span style="background-color:#ffffff; color:#424b5d"><u><strong>测试对比数据</strong></u><span style="color:#424b5d"><span style="color:#424b5d">：</span></span></span></span><span style="background-color:#ffffff; color:#424b5d">性能指标完全可以满足冷数据需求，因此重点关注成本对比情况，经测算，第一种部署方案情况下可以节省40%的存储空间，同时也免去了业务自行运维存储系统的麻烦；第二种方案则可以节省大量的服务器资源和运维人力，成本节省更明显，以我们对接的业务为例，共800TB冷数据，2副本，单盘8T，每台服务器10块盘，考虑到集群水位和硬盘实际可用空间，共需要28台服务器，而使用Curve共享存储系统后，可以节约成本超100万（包含所有Curve所需资源和ES冷数据所需计算节点资源）。</span></p> 
<p><span style="background-color:#ffffff; color:#424b5d"><u><strong><u>下一步计划</u></strong></u><span style="color:#424b5d">：</span></span></p> 
<ul style="list-style-type:disc"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff; color:#424b5d">继续优化小文件吞吐</span></p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px"><span style="color:#0080ff"><strong>性能测试</strong></span></h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#0052ff"><strong>性能测试数据</strong></span></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:left"><span style="color:#424b5d">通过</span><span style="color:#0052ff"><em><strong>测试数据</strong></em></span><span style="color:#424b5d"><span style="background-color:#f7f7f7; color:#000000">⑥</span>可以看出，Curve 共享文件存储+对象存储数据后端场景下的性能已经处于</span><span style="color:#424b5d">开源存储系统</span><span style="color:#424b5d">领先水平，后续版本我</span><span style="color:#424b5d">们</span><span style="color:#424b5d">还会继</span><span style="color:#424b5d">续优</span><span style="color:#424b5d">化，为 Curve 社区提供更高性能的云原生存储系统。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0052ff"><strong>性能相关参数配置</strong></span></p> 
<table border="1" cellpadding="1" cellspacing="1" style="width:900px"> 
 <tbody> 
  <tr> 
   <td>配置项</td> 
   <td>所属配置文件/进程</td> 
   <td>说明</td> 
  </tr> 
  <tr> 
   <td> <p>fuseClient.enableMultiMountPointRename</p> </td> 
   <td>curve-fuse 进程<br> curvefs/conf/client.conf</td> 
   <td> <p>在不需要对同一文件系统多挂载并发rename场景可以设置该配置项为false来提高元数据性能，默认为false。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>braft.raft_sync</p> </td> 
   <td>curvefs-metaserver 进程<br> curvefs/conf/metaserver.conf</td> 
   <td> <p>每次写raft wal 是否sync，默认为false，只在close时sync，用于保证更高的元数据性能。但在三副本同时掉电的情况下存在数据丢失的可能，若要保证该情况下的数据可靠性则需要设置为true。</p> </td> 
  </tr> 
  <tr> 
   <td>s3.async_thread_num;s3.max_connections；</td> 
   <td> <p>curve-fuse 进程</p> <p>curvefs/conf/client.conf</p> </td> 
   <td>AWS S3 C++ SDK使用这两个参数来实现多线程，但是线程是同步的，如果每个请求后端处理时间为10ms，那么一个线程1秒最多可以处理100个请求，n个线程最多可处理100*n个请求，调大这两个参数可以提升吞吐带宽（两个参数值配置为相同值即可）</td> 
  </tr> 
 </tbody> 
</table> 
<p style="margin-left:0; margin-right:0">其他重要配置</p> 
<table border="1" cellpadding="1" cellspacing="1" style="width:900px"> 
 <tbody> 
  <tr> 
   <td>配置项</td> 
   <td>所属配置文件/进程</td> 
   <td>说明</td> 
  </tr> 
  <tr> 
   <td>fuseClient.cto</td> 
   <td> <p>curve-fuse 进程</p> <p>curvefs/conf/client.conf</p> </td> 
   <td>在多挂载情况下，默认为false。请根据业务需要确定是否开启cto。</td> 
  </tr> 
  <tr> 
   <td>diskCache.maxUsableSpaceBytes <p> </p> </td> 
   <td> <p>curve-fuse 进程</p> <p>curvefs/conf/client.conf</p> </td> 
   <td> <p>缓存盘大小，默认200GB。请根据缓存盘的实际大小进行配置。</p> </td> 
  </tr> 
  <tr> 
   <td>enableSumInDir</td> 
   <td> <p>curvefs 工具</p> <p>curvefs/conf/tools.conf</p> </td> 
   <td>统计xattr中的信息，可以加速du。该选项打开后不支持硬链接。</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#0080ff"><strong>致谢</strong></span></h2> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#424b5d">感谢以下 Curve 开源社区同伴为 Curve v2系列版本作出的贡献（按字母序排列）：</span></p> 
<table border="1" cellpadding="1" cellspacing="1" style="width:500px"> 
 <tbody> 
  <tr> 
   <td><span style="color:#424b5d">baijiaruo</span></td> 
   <td><span style="color:#424b5d">chengyi01</span></td> 
   <td><span style="color:#424b5d">cw123</span></td> 
   <td><span style="background-color:#ffffff; color:#424b5d">SiKu</span></td> 
   <td><span style="background-color:#ffffff; color:#424b5d">fan</span></td> 
  </tr> 
  <tr> 
   <td>h0hmj</td> 
   <td>Hanqing,Wu</td> 
   <td>hzwuhongsong</td> 
   <td>ilixiaocui</td> 
   <td>locallocal</td> 
  </tr> 
  <tr> 
   <td><span style="background-color:#ffffff; color:#424b5d">wanghai01</span></td> 
   <td><span style="background-color:#ffffff; color:#424b5d">Wangpan</span></td> 
   <td><span style="background-color:#ffffff; color:#424b5d">Wine93</span></td> 
   <td><span style="background-color:#ffffff; color:#424b5d">xuchaojie</span></td> 
   <td><span style="background-color:#ffffff; color:#424b5d">yfxu</span></td> 
  </tr> 
  <tr> 
   <td>YunhuiChen</td> 
   <td>yuxubinchen</td> 
   <td><span style="color:#424b5d">wav</span><span style="color:#424b5d">emomo</span></td> 
   <td>YhhHaa <p> </p> </td> 
   <td> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#424b5d">我们将为以上小伙伴提供 Curve 社区周边大礼包～也欢迎更多小伙伴参与到 Curve 开源社区，不仅是提交代码，还可以讨论需求、交流建议、反馈问题、完善文档、分享落地实践等。</span></p> 
<h2 style="margin-left:0px; margin-right:0px"><span style="color:#0080ff"><strong>后续版本规划</strong></span></h2> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#424b5d">后续版本我们将持续提升 Curve 块存储和共享文件存储性能，并增强 Curve 共享文件存储的功能，下个大版本规划的主要功能有：</span></p> 
<ul style="list-style-type:disc"> 
 <li> <p><span style="color:#424b5d">块存储：</span><span style="color:#424b5d">支持 NVMe 场景下的 SPDK 能力，升级替换块存储的 ext4 引擎；</span></p> </li> 
 <li> <p><span style="color:#424b5d">共享文件存储：</span></p> 
  <ul style="list-style-type:square"> 
   <li> <p><span style="color:#424b5d">支持数据预热功能；</span></p> </li> 
   <li> <p><span style="color:#424b5d">支持使用 Curve 块存储集群作为高性能数据存储后端并支持生产环境使用；</span></p> </li> 
   <li> <p><span style="color:#424b5d">支持冷热数据分层存储和数据生命周期管理；</span></p> </li> 
   <li> <p><span style="color:#424b5d">支持文件回收站、文件系统配额功能；</span></p> </li> 
  </ul> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><em><em>参考<strong style="color:#424b5d">①</strong>：</em></em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><em>https://github.com/opencurve/curve/blob/master/docs/cn/CurveBS%E5%86%99%E6%97%B6%E5%BB%B6%E4%BC%98%E5%8C%96.md</em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><em>参考<strong style="color:#222222"><span style="color:#424b5d">②</span></strong>：</em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><em>https://github.com/opencurve/curve/commit/5f5220c618aa726c777dddf94a32bef8fd5f0dcd</em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><em><span style="color:#333333"><em>参</em></span></em></span><span><em><span style="color:#333333"><em>考<strong><span style="background-color:#ffffff; color:#424b5d">③</span></strong>：</em></span></em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><em>https://github.com/opencurve/curve/blob/master/CHANGELOG-2.3.md#data-performance</em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><em><span style="color:#333333"><em><span style="color:#333333"><em>参</em></span></em></span><span style="color:#333333"><em><span style="color:#333333"><em>考<span style="background-color:#f7f7f7; color:#000000">④</span>：</em></span></em></span></em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><em>https://github.com/opencurve/curve/blob/master/CHANGELOG-2.3.md#metadata-performance</em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><em><em><span style="color:#333333"><em><span style="color:#333333"><em>参</em></span></em></span><span style="color:#333333"><em><span style="color:#333333"><em>考<span style="background-color:#f7f7f7; color:#000000">⑤</span>：</em></span></em></span></em></em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><em>https://github.com/open-mmlab/mmclassification</em></span></p> 
<p><span><span style="color:#333333"><em><span><em>参</em></span></em></span><em>考<span style="background-color:#f7f7f7; color:#000000">⑥</span></em><em>：</em></span></p> 
<p><span><em>https://github.com/opencurve/curve/blob/master/CHANGELOG-2.3.md</em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"> </p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span><strong style="color:#8d8d8d">GitHub</strong><span style="background-color:#ffffff; color:#8d8d8d">：https://github.com/opencurve/curve</span></span></p> </li> 
 <li> <p><strong style="color:#8d8d8d">官网</strong>：<span style="background-color:#ffffff; color:#8d8d8d">https://opencurve.io/</span></p> </li> 
 <li> <p><strong style="color:#8d8d8d">用户论坛</strong><span style="background-color:#ffffff; color:#8d8d8d">：https://ask.opencurve.io/</span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            