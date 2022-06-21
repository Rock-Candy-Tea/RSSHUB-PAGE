
---
title: 'Pigsty v1.5.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5870be6c84e0221bb80b4e3c21c84e149d1.png'
author: 开源中国
comments: false
date: Tue, 21 Jun 2022 07:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5870be6c84e0221bb80b4e3c21c84e149d1.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Pigsty v1.5.1 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F3KcwPfxPs5UTgNY0tNx5ng" target="_blank">发布</a>，具体更新内容如下：</p> 
<h3><span><strong>内核</strong></span></h3> 
<p><span>在PostgreSQL 14.0 至 14.3 中，出现了一个BUG。当你使用​​​​</span></p> 
<pre><strong>CREATE INDEX CONCURRENTLY </strong>| <strong>REINDEX CONCURRENTLY</strong></pre> 
<p><span>在线重建索引时，有可能会导致静默的 <strong><span>索引数据腐坏</span></strong>。 在 2022.06.16日，PostgreSQL 全球开发组 Release 了 14.4 以解决这一问题。</span></p> 
<p><img height="273" src="https://oscimg.oschina.net/oscnet/up-5870be6c84e0221bb80b4e3c21c84e149d1.png" width="500" referrerpolicy="no-referrer"></p> 
<p><span style="color:#b2b2b2">https://www.postgresql.org/about/news/postgresql-14-out-of-cycle-release-coming-june-16-2022-</span><span style="color:#b2b2b2">2466/</span></p> 
<p><span>因为在线重建索引是一个非常重要的生产级运维功能，允许用户在不影响表读写的情况下建立新的索引。强烈建议所有使用 PG14 的用户</span><span style="color:#ab1942"><strong>尽快升级小版本至 14.4 </strong></span><span>。</span></p> 
<p><span><strong>Pigsty v1.5.0</strong> 默认使用 <strong>PostgreSQL</strong> <strong>14.3 </strong>，在<strong>v1.5.1</strong>中已经升级为<strong> PG 14.4</strong>。</span></p> 
<p><img height="499" src="https://oscimg.oschina.net/oscnet/up-8b012ebb3cb9426d0b8ba3013cc7697534c.png" width="500" referrerpolicy="no-referrer"></p> 
<h3><strong><span>扩展</span></strong></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty v1.5.1 对 Citus和TimescaleDB扩展插件进行了升级。</span></p> 
<h4><strong><span>Citus 11</span></strong></h4> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>https://www.citusdata.com/updates/v11-0</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span>Citus</span></strong><span> 于3天前紧跟着 PG 14.4 正式释出 v11，把所有企业版的特性都开源了，当然最重要的特性就是在线平衡数据分区（自动平滑扩缩容），可谓功德无量。Pigsty立刻就把它给搞进 v1.5.1 了。有了 <strong>Citus</strong> 企业版特性，这下PG真的成为了：分布式地理空间时序超融合数据库了。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><img alt height="1036" src="https://oscimg.oschina.net/oscnet/up-95b62545386c2e03c7cbe3b80882af02506.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span>Citus</span></strong><span> 是原生的PG插件扩展，主要针对的场景包括：</span></p> 
<ul> 
 <li><span>多租户，让数据按照租户自动分片。</span></li> 
 <li><span><strong><span>实时分析</span></strong></span><span>，并行加速实时聚合，压到秒级响应。</span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>它的主要应用场景与 <strong>TiDB</strong> 或 <strong>MyCat</strong>中间件类似。都是海量<strong>CRUD</strong>。核心能力是水平分片与并行计算，可自动对大表进行透明的水平分片，（e.g 支持到PB级）。在此基础上，通过多节点，多进程，多worker的方式，让 </span><span style="color:#000000">sum/avg/count/... </span> 这些聚合“分析”函数的响应时间进入“在线”业务的容忍范畴（例如1秒上下）。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty默认安装Citus，但默认不启用它。启用Citus非常简单，通常您需要修改两个参数：</span><span style="color:#000000">max_prepared_transaction </span><span>修改为一个大于 </span><span style="color:#000000">max_connections </span>的值以启用两阶段提交。<span> 并在 </span><span style="color:#000000">shared_preload_libraries </span><span>中填入 </span><span style="color:#000000">cit</span><span style="color:#000000">us</span><span> 并放置于首位。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>然后你只需  </span><strong>CREATE EXTENSION </strong><span style="color:#000000">citus </span>，即可使用此分布式扩展。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span>Citus </span></strong><span>可以与地理空间扩展 <strong>PostGIS</strong> 很好的共同配合，但与 <strong>TimescaleDB</strong> 相性不佳。您可以同时使用两种插件，但最好不要在同样的表上交叉使用，因为这是两种不同的数据分区方案。</span></p> 
<h4><strong><span>TimescaleDB</span></strong></h4> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>https://docs.timescale.com/timescaledb/latest/overview/release-notes/</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>TimescaleDB 也于近期（2022-05-24） 发布了2.7版本，该版本显著增强了 <strong><span>连续聚合</span></strong></span><span> 的能力，例如在连续聚合中使用 </span><strong>DISTINCT</strong><span style="color:#000000">, </span><strong>FILTER</strong><span style="color:#000000">, </span><strong>HAVING FILTER</strong><span style="color:#000000">, Ordered-</span><strong>Set </strong><span style="color:#000000">Agg, </span><strong>Hypothetical</strong><span style="color:#000000">-</span><strong>Set </strong><span style="color:#000000">Agg</span><span style="color:#000000">。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span>TimescaleDB</span></strong><span> 是一个原生的 PostgreSQL 插件，提供了强大的时序数据存储、处理、分析能力。它有一个商业的多节点集群版本，而单节点的版本作为PG插件的形式完全开源免费。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><span style="background-color:#ffffff">Pigsty的CMDB默认启用了 </span><strong>TimescaleDB</strong><span style="background-color:#ffffff"> ，它可以很好</span>地<span style="background-color:#ffffff">与 </span><strong>PostGIS </strong><span style="background-color:#ffffff">扩展插件提供的地理空间能力相互配合。</span><span style="background-color:#ffffff">但是和 </span><strong>Citus</strong><span style="background-color:#ffffff"> 的相</span>性<span style="background-color:#ffffff">不佳（</span><strong>Citus</strong><span style="background-color:#ffffff">针对业务字段进行水平分片，而 </span><strong>TimescaleDB </strong><span style="background-color:#ffffff">针对时间分区进行定制优化）。</span></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>尽管TimescaleDB与Citus可以在同一个数据库集簇中同时启用，但建议您还是根据自身的业务场景，在两者中选择一个启用。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img alt height="735" src="https://oscimg.oschina.net/oscnet/up-5a3a116122a347474b90a5fec2315e28c90.png" width="500" referrerpolicy="no-referrer"></p> 
<h4><strong><span>Patroni</span></strong></h4> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>https://patroni.readthedocs.io/en/latest/releases.html</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Patroni作为Pigsty使用的数据库高可用组建，于本月发布了 2.1.4 版本，此版本修复了一系列问题。</span></p> 
<p><img alt height="1214" src="https://oscimg.oschina.net/oscnet/up-72d35836edeb05506d6e47b320221dce574.png" width="500" referrerpolicy="no-referrer"></p> 
<h4><strong><span>HAProxy</span></strong></h4> 
<p><span>https://www.haproxy.com/blog/announcing-haproxy-2-6/</span></p> 
<p><span>HAproxy是Pigsty默认使用的负载均衡器，于本月释出了 2.6 版本。</span><span><span style="background-color:#ffffff">此版本</span>有<span style="background-color:#ffffff">大量有趣的新功能，例如用于精细控制流量的命令行工具，HTTP3支持，新的负载均衡算法，以及更稳定的在线配置重载。</span></span></p> 
<p><img height="236" src="https://oscimg.oschina.net/oscnet/up-8aed6ca01d909416f48f7f70d6ad8caeef5.png" width="500" referrerpolicy="no-referrer"></p> 
<h3><strong><span>基础设施升级</span></strong></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>https://grafana.com/docs/grafana/latest/release-notes/release-notes-9-0-0/</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span>Grafana</span></strong><span> 升级至 9.0，整体UI有了显著改善。9.0的统一告警功能有了显著增强并默认启用。针对 <strong>Prometheus </strong>与<strong>Loki</strong>，<strong>Grafana 9 </strong>提供了辅助编写查询的可视化工具（类似PromLens），能显著提升开发使用体验。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><img alt height="489" src="https://oscimg.oschina.net/oscnet/up-d0d9039bdf88a34ed3b8601d308701219e3.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">不过需要注意的是，例如 Auth Proxy 这样的功能现在变为了企业版特性。</p> 
<h3><span>新的应用</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty新增了两个 <strong>Docker </strong>应用：开箱即用的本地维基百科，以及为Postgres提供<strong>MongoDB</strong> <strong>API</strong> 能力的 <strong>FerretDB</strong>（原名叫 <strong>MangoDB</strong>，碰瓷 <strong>MongoDB</strong> 被呲了才改名的）</span></p> 
<h4><span>WIKI.js</span></h4> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>你自己的维基百科，数据使用Postgres存储，与Markdown互通。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>https://pigsty.cc/zh/docs/app/docker/wiki/</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><img alt height="424" src="https://oscimg.oschina.net/oscnet/up-66e8bd8a0040c3c17440e02cdd4a36747be.jpg" width="500" referrerpolicy="no-referrer"></span></p> 
<h4><strong><span>FerretDB</span></strong></h4> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>为PostgreSQL提供MongoDB兼容的API，您可以用MongoDB API来使用PG了</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="360" src="https://oscimg.oschina.net/oscnet/up-b4087bef30e0c6e1132e8bb7190263a27d3.png" width="500" referrerpolicy="no-referrer"></p> 
<h3><strong><span>后续工作</span></strong></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>公告指出，Pigsty v1.6 的开发正在筹划中，拟于7月释出一个Beta版本。1.6版本重点关注安全性，加密，证书。元节点上将默认创建一个本地 <strong>CA</strong>，每个节点，<strong>ETCD</strong>/Consul<strong>都会</strong>默认添加此 <strong>CA</strong>，并启用可选的SSL流量加密。此外，<strong>Postgres</strong>，<strong>Pgbouncer</strong>，<strong>PG Exporter</strong>，都将开始提供针对SSL加密的可选支持。默认的数据库密码认证方式将从 <strong>md5</strong> 升级至更安全的 <strong>SCRAM-SHA-256</strong>。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty v1.6 还将提供自动适配的参数模板。在先前版本中，如果用户需要在不同规格的机器上部署，通常需要自己选择对应规格的配置模板，例如：</span></p> 
<pre>tiny, mini, micro, small, medium, <strong>large</strong>, nxlarge....<span>，</span></pre> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>诸如此类。自动适配的模板将自动根据操作系统的配置规格进行适配，用户无需显式选择，通常只需要在功能上选择 <strong>OLTP</strong>，<strong>OLAP</strong>，<strong>CRIT</strong>，<strong>TINY </strong>四种模式之一即可。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>非常感谢用户 <strong>@Alemacci</strong>  提供了一系列关于安全与自动配置的功能实现，这些功能将在充分测试后于1.6.0释出。这位帅哥太高产了，一次性把一大堆功能都做了，包括：</span></p> 
<ul> 
 <li><span>可配置的日志目录</span></li> 
 <li><span>所有组件的<strong>SSL</strong>支持</span></li> 
 <li><strong><span>CA</span></strong><span>基础设施与证书签发</span></li> 
 <li><span>Postgres的 <strong>SCRAM-SHA-256</strong> 认证改造</span></li> 
 <li><span>自动适配机器的<strong>Patroni</strong>配置模板</span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>诸如此类，都是非常务实，迫切需要的功能。</span></p>
                                        </div>
                                      
</div>
            