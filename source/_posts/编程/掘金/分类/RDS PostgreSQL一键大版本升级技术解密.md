
---
title: 'RDS PostgreSQL一键大版本升级技术解密'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed497a8626d94e309b67ae20a89d5362~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 18:13:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed497a8626d94e309b67ae20a89d5362~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> 内容简要： 一、PostgreSQL行业位置 二、PostgreSQL版本升级背景 三、PostgreSQL版本升级解密 四、PostgreSQL版本升级成果。</p>
<p><strong>一、PostgreSQL行业位置</strong></p>
<p>（一）行业位置</p>
<p>在讨论PostgreSQL（下面简称为PG）在整个数据库行业的位置之前，我们先看一下阿里云数据库在全球的数据库行业里的位置。</p>
<ul>
<li><strong>魔力象限领导者</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed497a8626d94e309b67ae20a89d5362~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">*Gartner 2020，阿里云数据库挺进 全球数据库魔力象限领导者</p>
<ul>
<li><strong>PG年度最佳产品奖</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b611d6af367d41fb9a263b441bb654e5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">*2020 PG亚洲大会上，阿里云数据库专属集群MyBase荣膺“PG年度最佳产品奖”</p>
<p>接下来,我们看一下PG数据库在行业中的位置。</p>
<ul>
<li><strong>全球数据库排行</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68b240c6c2ee4ab583fddd262ff9b5fc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">*PostgreSQL连续3年获得的最佳数据库在开源数据库排名TOP2位置，全球流行度趋势排名TOP4</p>
<ul>
<li><strong>广泛应用</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2be14a0f2a2b44fc8d23bd626e290280~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">PG数据库运用于各行各业，如计算机软件、信息技术及服务、 医疗及健康、金融服务、高等教育、通讯服务等领域</p>
<p>（二）RDS PG VS 自建PG</p>
<p>在大致了解PG在行业的位置后，接下来再看看阿里云RDS PG和自建PG相比有哪些方面的优点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e8e16b0c6b34e71b3e1993ba02da9dc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，相对于自建PG，RDS PG的优势主要体现在可靠性、安全性、智能化和丰富插件四个方面</p>
<p><strong>1.可靠性</strong></p>
<p>RDS PG提供了Logical Slot Failover能力，在主备模式下，当实例发生HA切换以后，Logical Slot可以继续为用户提供数据同步，这解决了自建PG在HA切换时无法做到数据增量同步的问题。</p>
<p>RDS PG的Standby支持多上游结点，当HA切换以后，依然可以保持只读实例读写分离功能, 不影响只读节点的数据同步。</p>
<p>一键大版本升级使得我们的用户可以产品化地一键升级到更高版本的PG，享受PG更新版本的特性与稳定性。</p>
<p><strong>2.安全性</strong></p>
<p>安全性主要分为三个方面。</p>
<p>首先，RDS PG提供云盘加密功能，用户只需要提供一个Key，RDS PG就可以使用这个用户自定义的Key对数据进行落盘加密。</p>
<p>其次，我们发布了SSL自定义证书功能，提供客户端以及服务端的自定义证书，提供客户端和服务端防伪装,提升数据库安全性。</p>
<p>最后，RDS PG提供SGX全加密，这个功能是基于硬件的加密技术，使数据在全链路上进行加密。</p>
<p><strong>3.智能化</strong></p>
<p>阿里云RDS的整个产品系列都提供了DAS服务。帮助用户在使用数据库的过程提供诊断优化能力，DAS可以帮助用户自发现、自诊断、自优化、自决策地解决用户数据库的问题。</p>
<p><strong>4.丰富插件</strong></p>
<p>RDS PG的<strong>Ganos时空引擎插件</strong>提供了时空数据的存储、检索、查询以及分析能力。</p>
<p>第二个插件是<strong>PASE高效向量检索插件</strong>。</p>
<p>第三个插件是<strong>oss_fdw</strong>，实现数据冷热分离的场景，将冷数据存储在更为低价的OSS上，在RDS PG上可以对OSS上的数据进行查询分析。</p>
<p>通过以上可以发现，相较自建PG，RDS PG在可靠性、安全性、智能化、插件丰富度方面优势明显。</p>
<p><strong>二、PostgreSQL版本升级背景</strong></p>
<p>PostgreSQL的升级功能源于用户使用中遇到的一些问题，在升级中我们也面临许多挑战。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddbdcf0e40f84da9aad3bb3c1c17a2b2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.遇到的问题</strong></p>
<ul>
<li><strong>老版本：过时不维护</strong></li>
</ul>
<p>过低的数据库版本,稳定性挑战, 比如:</p>
<p>1）PG 9.4，版本过老2）低版本，供应链问题3）社区不维护，无人兜底</p>
<ul>
<li><strong>高版本：新特性</strong></li>
</ul>
<p>用户对于高版本、新特性的强力需求, 比如:</p>
<p>1）增量排序2）并行索引垃圾回收3）索引deduplicate能力4）分区表、聚合性能提升</p>
<p><strong>2.面临的挑战</strong></p>
<ul>
<li><strong>弹性能力：极致弹性</strong></li>
</ul>
<p>PG 9.4和PG 10.0本地盘版本是跑在物理机形态上的,导致弹性能力相对较弱,比如:</p>
<p>1）秒级快照2）弹性伸缩能力3）更大存储空间支持4）备份操作无性能损耗</p>
<ul>
<li><strong>平滑割接: 应用感知小</strong></li>
</ul>
<p>在一键大版本升级过程中,如何使得用户应用尽可能的感知小,平滑的割接是另外一个巨大的挑战, 比如:</p>
<p>1）保证插件兼容性</p>
<p>2）割接、非割接模式3）可回滚、可验证能力4）应用零改动、感知小5）一键大版本升级产品化能力</p>
<p>总结而言，我们期望RDS PG能够产品化一键大版本升级、平滑割接、提供可验证、可回滚能力。</p>
<p><strong>三、PostgreSQL版本升级解密</strong></p>
<p>（一）设计原则</p>
<p>基于以上对产品的思考，我们在设计RDS PG的过程中主要遵循以下四大原则。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d614c08ac8ed47e2aac50e00b04c21f4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.验证回滚：可验证、可回滚</strong>-版本回滚：大版本回滚-DNS地址：连接字符串回滚-可验证: 高版本可验证能力</p>
<p><strong>2.限制要少：场景全覆盖</strong>-DDL限制-表结构限制-数据类型限制-版本全系覆盖</p>
<p><strong>3.一键升级：一键升级产品化</strong>-拒绝升级手册-一键产品化能力-插件兼容性适配</p>
<p><strong>4.平滑割接：应用不停服零宕机</strong>-升级过程应用不停服-升级过程速度快-连接地址平滑割接</p>
<p>这四大设计原则的出发点在于，我们希望将复杂留给自己，把简单留给用户，为用户带去极致的产品使用体验。</p>
<p>（二）方案选择</p>
<p>基于上方的设计原则，我们就要对升级方案进行选择。对于PG大版本升级，行业内主要有如下存在<strong>三种方案</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f712bb9c534486aacb8e6900779a427~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>方案一：逻辑复制</p>
<ul>
<li><strong>优点：</strong></li>
</ul>
<p>兼容性好、平滑割接</p>
<ul>
<li><strong>缺点：</strong></li>
</ul>
<p>1）库级别的发布、订阅</p>
<p>2）表必须有PK / UK3）不支持DDL、大对象4）外键和触发器禁用5）可能导致到WAL日志堆积</p>
<p>方案二：pg_upgrade</p>
<ul>
<li><strong>优点：</strong></li>
</ul>
<p>1）不拷贝数据, 仅元数据升级</p>
<p>2）效率高, 2TB数据,升级 < 10s</p>
<ul>
<li><strong>缺点：</strong></li>
</ul>
<p>1）升级预检查</p>
<p>2）回滚验证策略3）参数、插件兼容性4）复杂度高、工作量大、挑战大</p>
<p>方案三：pg_dump</p>
<ul>
<li><strong>优点：</strong></li>
</ul>
<p>1）兼容性好</p>
<p>2）实现简单、工作量小</p>
<ul>
<li><strong>缺点：</strong></li>
</ul>
<p>1）仅适用全量迁移</p>
<p>2）效率低下3）应用停服时间长</p>
<p>RDS PG最终选择限制少、兼容性好、效率高、平滑割接的pg_upgrade方案。</p>
<p>（三）升级预检查</p>
<p>用户升级之前需要先对实例进行升级预检查，检查流程可以让用户知道实例是否可以升级，升级会存在什么问题，然后用户再根据错误的信息做相应的修改或适配，使得升级可以顺利完成。升级预检查流程如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bceba3b720fa4f139ed76dc23a89fe0f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">*升级预检查流程图</p>
<p>首先，用户到前端控制台，根据源端实例的版本选择目标实例的版本，然后提交升级预检查流程，我们的后台会创建一个升级检查报告。接着初始化用户选择的高版本数据目录，然后生成高版本参数模板。</p>
<p>然后执行pg_upgrade--check，最终上传检查报告到控制台上，用户在RDS控制台就可以查看报告，如下是一个典型的升级预检查报告。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e482a48045b941b8ae5ea35f249360df~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">*升级预检查结果</p>
<p>可以看到，报告包括非常多的检查项，是否可以升级结果一目了然，帮助用户升级前屏蔽升级风险。</p>
<p>（四）正式升级</p>
<p>升级预检查完成且无误后，就进入了正式升级流程，流程图如下所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/903307a0a38c4933a17098ab29289392~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，流程图的每个步骤都包含两个角色，分别是用户升级前的源实例和升级后的目标实例。</p>
<p>升级之前，用户通过DNS连接到源实例。当用户在控制台发起一个大版本升级以后，我们会在后台帮用户创建一个和源实例同版本的目标实例的master节点，并且搭建复制链路。等待复制链路搭建好了，所有的数据同步完毕以后，待用户的切换时间。时间点到了以后，我们就会对源实例做Readonly。</p>
<p>第4步是把源实例和目标实例进行断连，断连后把目标实例提升为主库。</p>
<p>第5步是进行pg_upgrade操作，做元数据的升级，所以效率非常高，然后把用户的DNS地址切到目标实例上，此时用户应用就可以进行读和写。</p>
<p>第6步重搭备库，利用秒级快照能力，可以快速搭建备库，最终将整个实例平滑升级到高版本。</p>
<p>整个升级流程有以下几个关键的地方：</p>
<ul>
<li><strong>应用不停服</strong></li>
</ul>
<p>1）不停服:用户应用全程可读</p>
<p>2）平滑性: 第5步，通过连接地址交换来实现，用户应用无需修改代码</p>
<ul>
<li><strong>可验证可回滚</strong></li>
</ul>
<p>1）可验证: 非割接模式，源实例零干预</p>
<p>2）可回滚: 第5步之前，零代价回滚，连接地址随时可回滚</p>
<ul>
<li><strong>效率高</strong></li>
</ul>
<p>1）速度快: 第5步pg_upgrade2T数据在10秒内可以升级完毕</p>
<p>2）重搭快: 秒级快照，10分钟左右重搭备库，与数据量大小无关</p>
<ul>
<li><strong>用户影响</strong></li>
</ul>
<p>1）第 3-5 步，仅分钟级RO时间</p>
<p>总结：应用不停服，零宕机，仅分钟级的RO。</p>
<p>（五）应用不停服零宕机</p>
<p>升级的过程做到应用不停服零宕机，主要是通过以下四点实现。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68ba666fbf2e40dc835dad527468806b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.克隆目标实例</strong>目标实例采用类克隆实例方案，源端实例一直可用。</p>
<p><strong>2.可验证、可回滚</strong>非割接模式提供验证能力，连接地址切换之前，均可回滚。</p>
<p><strong>3.DNS地址切换</strong>切换用户连接DNS地址到目标实例上，避免应用改动。</p>
<p><strong>4.pg_upgrade元数据升级</strong>pg_upgrade仅元数据升级，耗时与数据量大小无关，实测2TB数据，少于10秒。</p>
<p>通过以上四点，最终一键平滑地完成大版本升级。</p>
<p><strong>四、PostgreSQL版本升级成果</strong></p>
<p>（一）成果展示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88a23d7e08a340ab911395df95f5aacb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">*阿里云RDS PG大版本升级在覆盖面、可用性、效率、可验证可回滚能力方面取得显著成果。</p>
<p>（二）行业对比</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c9a27be330842eaa4d0fdcdd7fae72f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">*阿里云RDS PG一键大版本升级在产品化、用户体验、可验证可回滚能力上引领行业</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000283469%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000283469/" ref="nofollow noopener noreferrer">原文链接</a><br>
本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            