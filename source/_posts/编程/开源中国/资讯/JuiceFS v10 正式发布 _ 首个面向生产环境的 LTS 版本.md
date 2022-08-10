
---
title: 'JuiceFS v1.0 正式发布 _ 首个面向生产环境的 LTS 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=592'
author: 开源中国
comments: false
date: Wed, 10 Aug 2022 10:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=592'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:left"> 
 <p style="margin-left:0; margin-right:0"><strong>今天，JuiceFS v1.0 发布了</strong><span> </span>🎉</p> 
 <p style="margin-left:0; margin-right:0">经过了 18 个月的持续迭代和大量生产环境的广泛验证，此版本将成为第一个被长期维护的稳定版（LTS）。同时，该版本提供完整的向前兼容，所有用户可以直接升级。</p> 
 <p style="margin-left:0; margin-right:0">JuiceFS 是为云环境设计的分布式文件系统，同时兼容 POSIX、HDFS、S3 访问协议，也可以使用 CSI 方式在 Kubernetes 中作为 PV 使用，在大数据、机器学习，和需要共享文件存储的场景中广泛使用。</p> 
 <h1 style="margin-left:0; margin-right:0">可用于生产环境</h1> 
 <p style="margin-left:0; margin-right:0">稳定可靠的软件离不开全面的质量管理体系，<strong>JuiceFS 的测试体系已经涵盖了每日进行的单元测试、基础功能测试、兼容性测试、第三方工具测试以及实际应用场景测试。</strong>每一个版本发布之前，还需要额外完成异常测试和压力测试。在这次 v1.0 正式版发布前，我们模拟了从 Redis 切换到 TiKV 再持续写入 100 亿小文件，来验证系统的扩展性。</p> 
 <p style="margin-left:0; margin-right:0">在过去的一年半里，来自不同行业、不同企业规模的社区用户尝试将 JuiceFS 应用到更为广泛的场景中：<strong>人工智能、大数据、云原生、数据共享、备份归档</strong>等。JuiceFS 的能力在应用中获得了持续改进，并上线到生产环境中，经受住了持续的稳定性和性能考验。</p> 
 <p style="margin-left:0; margin-right:0"><strong>有上千集群在持续使用 JuiceFS，最大集群规模超过 10PB 数据和数十亿文件</strong>。这些用户来自互联网和科技、电信运营商、生命医药、航天、气象、遥感等领域；包括有移动云、航天宏图、小米、vivio、携程旅行、大疆、理想汽车、上汽集团、地平线、云知声、深势科技、商汤、Shopee、知乎、网易游戏、一面数据等企业，还有济南超算中心、国家天文数据中心等。</p> 
 <p style="margin-left:0; margin-right:0">这些社区用户也分享了他们在不同场景的实践：</p> 
 <ul style="margin-left:.8em; margin-right:.8em"> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fblog%2Fcn%2Fposts%2Fjuicefs-support-hbase-at-chinamobile-cloud%2F" target="_blank">移动云使用 JuiceFS 支持 Apache HBase 增效降本的探索</a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fblog%2Fcn%2Fposts%2Fli-auto-with-juicefs%2F" target="_blank">理想汽车使用 JuiceFS 实现数据平台存算分离</a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fblog%2Fcn%2Fposts%2Fshopee-clickhouse-with-juicefs%2F" target="_blank">Shopee 使用JuiceFS 实现 ClickHouse 数据冷热分层</a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fblog%2Fcn%2Fposts%2Fjuicefs-support-ai-storage-at-unisound%2F" target="_blank">云知声使用 JuiceFS 建设超算平台分布式存储</a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fblog%2Fcn%2Fposts%2Fdptech-ai-storage-in-multi-cloud-practice%2F" target="_blank">深势科技使用 JuiceFS 实现多云 AI 科学计算平台建设</a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fblog%2Fcn%2Fposts%2Fzhihu-flink-with-juicefs%2F" target="_blank">知乎使用 JuiceFS 给 Flink 容器启动加速</a></li> 
 </ul> 
 <p style="margin-left:0; margin-right:0">点击<span> </span><em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fblog%2Fcn%2Ftags%2F%25E5%25AE%25A2%25E6%2588%25B7%25E6%25A1%2588%25E4%25BE%258B%2F" target="_blank">此处</a></em><span> </span>查看用户案例合集。</p> 
 <h1 style="margin-left:0; margin-right:0">功能快速浏览</h1> 
 <p style="margin-left:0; margin-right:0">JuiceFS 是第一个完全插件式的分布式文件系统，元数据和数据都可以借助已有的成熟组件来实现，以应对丰富多变的企业环境和数据存储需求，目前<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fdatabases_for_metadata" target="_blank">支持 10 种以上元数据引擎</a><span> </span>和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fhow_to_setup_object_storage%2F" target="_blank">30 种以上数据存储引擎</a><span> </span>。同时，JuiceFS 同时兼容 POSIX、<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fhadoop_java_sdk%2F" target="_blank">HDFS</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fs3_gateway%2F" target="_blank">S3</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fcommand_reference%2F%23juicefs-webdav" target="_blank">WebDAV</a><span> </span>等访问协议，让数据不再成为孤岛，可以自由地在所有应用中流通。</p> 
 <p style="margin-left:0; margin-right:0">除了稳定性之外，JuiceFS 还提升了<strong>全方面的数据安全保障</strong>：</p> 
 <ul style="margin-left:.8em; margin-right:.8em"> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fsecurity%2Fencrypt%2F" target="_blank">数据存储加密</a>，让文件内容加密存储在对象存储中，防止数据意外泄露</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fsecurity%2Ftrash" target="_blank">回收站</a>，防止手抖误删除</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fmetadata_dump_load" target="_blank">元数据导入 & 导出 工具</a>不仅方便备份，还可以做元数据引擎迁移</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fmetadata_dump_load%23%25E8%2587%25AA%25E5%258A%25A8%25E5%25A4%2587%25E4%25BB%25BD" target="_blank">元数据自动备份</a>，支持数据延迟删除，配合元数据备份，可以让数据「回到过去」，防止误更新</li> 
 </ul> 
 <p style="margin-left:0; margin-right:0"><strong>系统可观测性也在持续增强：</strong></p> 
 <ul style="margin-left:.8em; margin-right:.8em"> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fadministration%2Fmonitoring" target="_blank">提供丰富的系统指标监控系统运行状态</a>，通过 API 直接接入 Prometheus，预置的 Grafana 模版</li> 
  <li>通过<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Ffault_diagnosis_and_analysis%23%25E5%25AE%25A2%25E6%2588%25B7%25E7%25AB%25AF%25E6%2597%25A5%25E5%25BF%2597" target="_blank">客户端日志和访问日志</a>，可以了解系统详情</li> 
  <li>文件元数据索引分析工具<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fcommand_reference%2F%23juicefs-info" target="_blank">juicefs info</a></li> 
  <li>性能实时诊断工具<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Foperations_profiling" target="_blank">juicefs profile</a></li> 
  <li>性能统计监控工具<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fstats_watcher" target="_blank">juicefs stats</a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fadministration%2Fmonitoring%2F%23graphite" target="_blank">支持 Graphite 协议收集 Hadoop SDK 的监控数据</a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Ffault_diagnosis_and_analysis%23%25E4%25BD%25BF%25E7%2594%25A8-pyroscope-%25E8%25BF%259B%25E8%25A1%258C%25E6%2580%25A7%25E8%2583%25BD%25E5%2589%2596%25E6%259E%2590" target="_blank">内置 Pyroscope 进行性能分析</a></li> 
 </ul> 
 <p style="margin-left:0; margin-right:0">还有丰富的管理工具：</p> 
 <ul style="margin-left:.8em; margin-right:.8em"> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fcommand_reference%23juicefs-sync" target="_blank">juicefs sync</a><span> </span>在任意两个存储系统之间复制数据，相当于高性能 rsync／DistCp，支持丰富的访问协议</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fcommand_reference%23juicefs-warmup" target="_blank">juicefs warmup</a><span> </span>可以为指定路径预热数据，提升读取性能</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fcommand_reference%23juicefs-rmr" target="_blank">juicefs rmr</a><span> </span>快速删除指定目录</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fcommand_reference%23juicefs-config" target="_blank">juicefs config</a><span> </span>可以在线修改文件系统配置</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fcommand_reference%23juicefs-fsck" target="_blank">juicefs fsck</a><span> </span>可以检查文件系统完整性，找出可能损坏的文件</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fcommand_reference%23juicefs-gc" target="_blank">juicefs gc</a><span> </span>可以回收意外泄露的数据</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fcommand_reference%23juicefs-bench" target="_blank">juicefs bench</a><span> </span>简单的基准性能测试</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fcommand_reference%23juicefs-objbench" target="_blank">juicefs objbench</a><span> </span>测试对象存储的访问权限和基准性能</li> 
 </ul> 
 <h1 style="margin-left:0; margin-right:0">拥抱开源</h1> 
 <p style="margin-left:0; margin-right:0">JuiceFS 在 2017 年以云服务的形式发布，经过三年的持续打磨和稳健运后，为了能让更多的开发者体验到这款产品的便捷，我们在 2021 年 1 月 11 日发布了插件化架构的 JuiceFS 社区版，并以每月发布一个测试版的速度持续迭代。</p> 
 <p style="margin-left:0; margin-right:0">当听到一些社区用户反馈对 AGPLv3 的顾虑后，<strong>我们在2022年1月将 “AGPLv3 许可” 改为了 “Apache 2.0 许可”</strong>，让用户可以更放心地将 JuiceFS 应用于各种商业环境，并且根据自身的需要进行二次改进，也便于上下游的应用进行更进一步的融合，比如 Fluid 和 PaddlePaddle Operator 就已经将 JuiceFS 集成其中。</p> 
 <p style="margin-left:0; margin-right:0"><strong>开源软件的发展离不开社区用户的共同努力，包括参与提交 issue、贡献 PR、分享文章、回答问题的每一位成员，在此向每一位参与者表示感谢！</strong></p> 
 <h1 style="margin-left:0; margin-right:0">未来规划</h1> 
 <p style="margin-left:0; margin-right:0"><strong>JuiceFS v1.0 是第一个长期维护（ LTS）版本，我们会提供 24 个月的持续维护。</strong></p> 
 <p style="margin-left:0; margin-right:0">未来的版本会逐步实现以下这些功能（欢迎反馈）：</p> 
 <ul style="margin-left:.8em; margin-right:.8em"> 
  <li>支持 FoundationDB 做元数据引擎</li> 
  <li>录配额</li> 
  <li>用户和组配额</li> 
  <li>POSIX ACL</li> 
  <li>快照</li> 
  <li>WORM（Write Once Read Many）</li> 
 </ul> 
 <p style="margin-left:0; margin-right:0">在 JuiceFS 的持续迭代过程中，一直保持着向后兼容，希望新的改进能够更快地被用户使用，未来的版本发布也会兼容 v1.0 并提供平滑升级的方案。同时，JuiceFS v1.0 也为未来的版本做了一些向前兼容准备。</p> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            