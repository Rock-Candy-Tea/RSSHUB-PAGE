
---
title: 'openGauss 3.0.0 版本正式发布！立即体验社区首个轻量版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/20d82580-7333-4d43-b351-d7de6db0c1bb.jpg'
author: 开源中国
comments: false
date: Sat, 02 Apr 2022 17:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/20d82580-7333-4d43-b351-d7de6db0c1bb.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#7d32ea"><strong>今日，openGauss 3.0.0版本正式上线！</strong></span>openGauss 3.0.0 版本是openGauss社区继2.0.0之后发布的又一个Release版本，版本维护生命周期为3.5年。3.0.0版本在高性能、高可用、高安全、高智能、工具链等方面都有持续创新和突破。3.0.0版本除了包含企业版外同时发布了openGauss社区首个轻量版（Lite 版）。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/20d82580-7333-4d43-b351-d7de6db0c1bb.jpg" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#9b59b6"><strong>一、高性能</strong></span></p> 
<p style="margin-left:0; margin-right:0"><strong>1. </strong><strong>鲲鹏单机性能持续保持领先</strong></p> 
<p style="margin-left:0; margin-right:0">单机鲲鹏64核2P TPCC满足150万tpmC之后，3.0.0版本持续性能优化，支持行存转向量化、外键锁优化等技术，同时单机鲲鹏32核2P TPCC达到100万tpmC。</p> 
<p style="margin-left:0; margin-right:0"><strong>2. </strong><strong>In-place Update存储引擎</strong></p> 
<p style="margin-left:0; margin-right:0">openGauss支持In-place Update存储引擎（原地更新），实现基于NUMA-Ware架构的高可扩展UNDO子系统、基于多版本的索引及闪回等关键技术，实现稳定场景下高性能。</p> 
<p style="margin-left:0; margin-right:0"><strong>3. </strong><strong>并行逻辑解码</strong></p> 
<p style="margin-left:0; margin-right:0">在使用JDBC或pg_recvlogical解码时，通过设置parallel-decode-num参数来开启并行解码特性，数据库内核通过一个读取线程、多个解码线程以及一个发送线程之间的流水线协同运行进行逻辑解码操作，解码速度<span>显著</span><span>提升</span>。</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#9b59b6"><strong>二、高可用</strong></span></p> 
<p style="margin-left:0; margin-right:0"><strong>1. CM（Cluster Manager）</strong></p> 
<p style="margin-left:0; margin-right:0">实现企业级集群管理能力，支持自定义资源监控，提供了数据库主备的状态监控、网络通信故障监控、文件系统故障监控、故障自动主备切换等能力。</p> 
<p style="margin-left:0; margin-right:0"><strong>2. </strong><strong>Paxos分布式一致性协议</strong></p> 
<p style="margin-left:0; margin-right:0">实现基于Paxos分布式一致性协议的日志复制及选主框架，支持在线添加、删除节点，在线转让Leader能力，通过自仲裁、多数派选主、优先级选主能力摆脱第三方仲裁组件，极大缩短RTO时间，且可预防任何故障下的脑裂双主。</p> 
<p style="margin-left:0; margin-right:0"><strong>3. Global SysCache</strong></p> 
<p style="margin-left:0; margin-right:0">将系统缓存与会话解耦，绑定到线程上，结合线程池特性达到降低内存占用的目的，同时结合全局缓存，提升缓存命中率，保持性能稳定</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#9b59b6"><strong>三、高安全</strong></span></p> 
<p style="margin-left:0; margin-right:0"><strong>1. 原生多方共识，账本数据库</strong></p> 
<p style="margin-left:0; margin-right:0">融合区块链中的密码学校验技术，对用户指定的防篡改表中数据进行修改时，突破传统链式生成校验信息的串行化限制，高效生成、记录篡改校验信息，且内置高性能篡改校验接口供用户调用。</p> 
<p style="margin-left:0; margin-right:0"><strong>2. 全密态数据库能力持续增强</strong></p> 
<p style="margin-left:0; margin-right:0">密态等值查询能力扩展支持JDBC开发接口，并支持存储过程和函数中的密态等值查询能力，使得存储过程和函数中的数据也可以以密文形态参与运算。</p> 
<p style="margin-left:0; margin-right:0"><strong>3. 支持国密算法体系</strong></p> 
<p style="margin-left:0; margin-right:0">口令登录认证支持使用SM3国密算法，加解密函数API接口支持使用SM4国密算法，密态等值查询支持使用SM4加密算法存储数据并运算。</p> 
<p style="margin-left:0; margin-right:0"><strong>4. 支持ANY权限管理</strong></p> 
<p style="margin-left:0; margin-right:0">新增支持数据库级别的ANY权限管理，即对数据库内的某一类对象的所有实体具有特定的操作权限，新增语法GRANT/REVOKE ANY权限TO/FROM user 来执行ANY权限授予和回收，同时新增系统表gs_db_privilege来记录用户的数据库级ANY权限。</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#9b59b6"><strong>四、高智能</strong></span></p> 
<p style="margin-left:0; margin-right:0"><strong>1. AI4DB自治运维平台DBMind</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">实现DBMind系统组件化，支持通过组件命令执行方式，实现AI自治功能的调用；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">集成基于openGauss exporter的采集能力，实现监控、采集、诊断和优化端到端能力。慢SQL根因分析实现基于KNN算法和根因特征权重矩阵的慢SQL根因分析召回，覆盖20+慢SQL场景；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持分区表索引推荐能力；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">实现轻量化趋势预测能力，实现线性时序、非线性时间和周期时序多种场景下的预测能力。</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>2. DB4AI库内AI引擎</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">提供原生SQL语法（Create Model、Predict By），实现简易AI训练和推理执行；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">通过内置AI原生算子方式，与优化器、执行器完美融合，实现性能超越MADlib 10倍；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持10种常用机器学习算法，包括线性回归、逻辑回归、SVM、KMeans、XGBoost、PCA等，实现普惠AI。</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span style="color:#9b59b6"><strong>五、分布式解决方案</strong></span></p> 
<p style="margin-left:0; margin-right:0"><strong>1. 支持使用中间件ShardingSphere构建分布式数据库</strong></p> 
<p style="margin-left:0; margin-right:0">基于分布式中间件ShardingSphere使openGauss具备分布式数据库能力。使用16个鲲鹏920 节点组网完美sharding性能>1000万tpmc。</p> 
<p style="margin-left:0; margin-right:0"><strong>2. 支持Kubernetes部署分布式数据库</strong></p> 
<p style="margin-left:0; margin-right:0">支持一键式部署分布式数据库，通过patroni实现计划内switchover和故障场景自动failover, 通过haproxy实现openGauss主备节点读写负载均衡，通过ShardingSphere实现分布式能力，所有功能打包至镜像并提供一键式部署脚本。</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#9b59b6"><strong>六、轻量版</strong></span></p> 
<p style="margin-left:0; margin-right:0">轻量版定位是在软硬件资源受限场景下仍可应用openGauss，例如边缘场景。其保留了企业版大部分的特性。轻量版的特点如下：</p> 
<p style="margin-left:0; margin-right:0">（1） 占用资源少：本次发布轻量化版本安装包实际大小小于30MB，空载内存小于250MB。</p> 
<p style="margin-left:0; margin-right:0">（2）易安装：相比于企业版，其安装流程更简单快捷。</p> 
<p style="margin-left:0; margin-right:0">（3）轻量版与之前版本大部分特性功能保持兼容。</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#9b59b6"><strong>七、工具链</strong></span></p> 
<p style="margin-left:0; margin-right:0"><strong>1. Data Studio工具代码正式开源</strong></p> 
<p style="margin-left:0; margin-right:0">DataStudio 是面向开发人员和数据库管理员的图形化通用集成开发环境。它简化了openGauss数据库的开发和管理，支持如下功能：</p> 
<p style="margin-left:0; margin-right:0">（1）管理和创建数据库、模式、表、索引等各类数据库对象。</p> 
<p style="margin-left:0; margin-right:0">（2）执行SQL语句或SQL脚本，高效进行SQL开发。</p> 
<p style="margin-left:0; margin-right:0">（3）创建和执行PL/SQL语句，支持存储过程调试。</p> 
<p style="margin-left:0; margin-right:0">（4）表数据增、删、改、查操作，导入和导出表数据、DDL、连接信息。</p> 
<p style="margin-left:0; margin-right:0">（5）支持SQL执行历史记录查询，显示执行计划、ER图。</p> 
<p style="margin-left:0; margin-right:0"><strong>2. MySQL到openGauss的迁移工具chameleon</strong></p> 
<p style="margin-left:0; margin-right:0">chameleon工具是一个基于Python语言的MySQL到openGauss的实时复制工具。该工具提供了初始全量数据的复制以及增量数据的实时复制能力，可实现数据从MySQL迁移至openGauss。</p> 
<p style="margin-left:0; margin-right:0"><span><strong>八、其他企业级特性</strong></span></p> 
<p style="margin-left:0; margin-right:0"><strong>1. 发布订阅</strong></p> 
<p style="margin-left:0; margin-right:0">企业版支持发布订阅，此特性基于逻辑复制实现，其中有一个或者更多订阅者订阅一个发布者节点上的一个或者更多发布。订阅者从它们所订阅的发布节点拉取数据。实现跨数据库集群的数据实时同步。</p> 
<p style="margin-left:0; margin-right:0"><strong>2. 行存表压缩</strong></p> 
<p style="margin-left:0; margin-right:0">支持行存表数据压缩，提供通用压缩算法，通过对表和索引数据页的透明页压缩和维护页面存储位置的方式，做到高压缩、高性能。磁盘持久化用2个文件存储，分别是压缩地址文件（扩展名.pca）和压缩数据文件（扩展名.pcd）。</p> 
<p style="margin-left:0; margin-right:0"><strong>3. Libpq支持ipv6和多IP</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">Libpq驱动支持IPV6能力；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Libpq支持多IP能力，外部使用Libpq库时，可配置主备多个IP，在连接字符串中， host、hostaddr和port选项接受以‘,’分割的字符串。</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span><strong>开放治理，共建、共享、共治最具创新力的数据库开源社区</strong></span></p> 
<p style="margin-left:0; margin-right:0">作为一个开源社区，openGauss秉承共建、共享、共治的理念。通过开放、成熟的治理，与企业、伙伴、开发者，共同建设开源社区。截至目前，全球下载量超过57万，遍布全球85个国家，608个城市，110家企业签署企业贡献者协议CLA加入到社区，来自企业和高校的2800名开发者积极参与openGauss社区贡献，同时openGauss已经在政府、金融、能源、教育、制造等行业规模商用落地。未来openGauss将围绕客户场景和需求持续构建更多竞争力，打造最具创新力的数据库开源社区。</p> 
<p style="margin-left:0; margin-right:0"><strong>感谢openGauss社区所有贡献者！</strong></p> 
<p><img src="https://oscimg.oschina.net/oscnet/7bd61db0-93ff-4667-bd74-6d449d06868d.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            