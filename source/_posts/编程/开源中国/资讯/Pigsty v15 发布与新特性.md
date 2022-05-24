
---
title: 'Pigsty v1.5 发布与新特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f030781feed93ac3e632197e234cf8c3eaa.png'
author: 开源中国
comments: false
date: Tue, 24 May 2022 07:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f030781feed93ac3e632197e234cf8c3eaa.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Pigsty v1.5 现已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FW8Ap9Xb2i19bFWaxpTdq2g" target="_blank">发布</a>。此版本包含完整的 Docker 支持，无数使用数据库的软件均可开箱即用。其他改进包括：基础设施自我监控、更好的冷备份支持、兼容 Redis 与 GP 的新 CMDB、ETCD 作为高可用 DCS、更好的日志收集与呈现。Github Star 突破 500。</p> 
<p><img height="339" src="https://oscimg.oschina.net/oscnet/up-f030781feed93ac3e632197e234cf8c3eaa.png" width="500" referrerpolicy="no-referrer"></p> 
<h2><strong><span>v1.5 亮点</span></strong></h2> 
<ul> 
 <li><span>完善的Docker支持：在管理节点上默认启用并提供诸多开箱即用的软件模板：gitea,bytebase, pgadmin, pgweb, postgrest, minio等。</span></li> 
 <li><span>基础设施自我监控：Nginx， ETCD， Consul， Prometheus， Grafana， Loki 自我监控</span></li> 
 <li><span>CMDB升级：兼容性改善，支持Redis集群/Greenplum集群元数据，配置文件可视化。</span></li> 
 <li><span>服务发现改进：可以使用Consul自动发现所有待监控对象，并纳入Prometheus中。</span></li> 
 <li><span>更好的冷备份支持：默认定时备份任务，添加<code>pg_probackup</code>备份工具，一键创建延时从库。</span></li> 
 <li><span>ETCD现在可以用作PostgreSQL/Patroni的DCS服务，作为Consul的备选项。</span></li> 
 <li><span>Redis剧本/角色改善：现在允许对单个Redis实例，而非整个Redis节点进行初始化与移除。</span></li> 
</ul> 
<h2><span>Docker 支持</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty v1.5中最激动人心的特性莫过于Docker（以及k8s）支持，无数软件与工具都可以通过Docker的方式开箱即用：开箱即用的数据库 + 开箱即用的应用 = 开箱即用的软件解决方案。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>很多软件都需要用到数据库，但数据库放入容器中仍然是一个充满争议的问题，基于Docker镜像的玩具数据库仍与生产级的数据库差着十万八千里。Pigsty可以将两者的优势融合：有状态的数据库使用Pigsty管理，运行于标准的物理机或虚拟机上，例如PGSQL与Redis；而无状态的应用使用Docker运行，这些应用的状态存储在Pigsty托管的外部数据库中。</span></p> 
<p style="color:#222222; margin-left:0px; margin-right:0.8em; text-align:start"><span>在Pigsty v1.4.1中，Docker作为一种实验特性被加入，在1.5中，Docker将作为Pigsty默认的组件，在元节点上默认启用。普通的节点默认关闭，但您可以通过一个配置项，在所有节点上配置并启动Docker。</span></p> 
<h2><span>应用生态</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Docker很棒，但重要的不是Docker或者Kubernetes本身，而是Docker所代表的巨大<strong><span>应用生态</span></strong></span><span>！</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty挑选了一些常用软件，特别是那些使用PostgreSQL与Redis的软件，制作了一键拉起的教程与快捷方式，并提供了可以离线使用自动加载的镜像软件包 </span><span><code>docker.tgz</code></span><span>。部署您自己的软件，从未如此简单！</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="145" src="https://oscimg.oschina.net/oscnet/up-a4d339053bb87c91bd60efbb8d790c0ebad.png" width="500" referrerpolicy="no-referrer"></p> 
<h3><span>代码托管平台</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>例如，Github被墙，而墙内的Gitee最近又搞了中国特色的开源审批制，让很多人都产生了自建Git代码托管服务的需求。如果您想要启动一个私有的代码托管服务，可以使用以下命令一键拉起 Gitea：</span></p> 
<pre><span style="color:#0073bf">cd </span>~/pigsty~app/gitea; <span style="color:#0073bf">make </span>up</pre> 
<p><img height="500" src="https://oscimg.oschina.net/oscnet/up-f986bcbea4cbe0515c2a99217793ee0a9e9.png" width="448" referrerpolicy="no-referrer"></p> 
<p><span>该命令将使用以下的Docker Compose配置文件拉起Gitea镜像，并使用外部Pigsty默认的CMDB：<code>pg-meta.gitea</code></span><span> 作为自己的元数据存储。访问配置文件指定的域名或端口，即可访问你自己的代码托管服务！</span></p> 
<pre><strong>version</strong>: <strong>"3"
</strong><strong>services</strong>:
  <strong>gitea</strong>:
    <strong>image</strong>: gitea/gitea
    <strong>container_name</strong>: gitea
    <strong>restart</strong>: always
    <strong>environment</strong>:
      <strong>DB_TYPE</strong>: postgres
      <strong>DB_HOST</strong>: 10.10.10.10:5432
      <strong>DB_NAME</strong>: meta
      <strong>DB_USER</strong>: dbuser_meta
      <strong>DB_PASSWD</strong>: DBUser.Meta
      <strong>USER_UID</strong>: 1000
      <strong>USER_GID</strong>: 1000
      <strong>HTTP_PORT</strong>: 8889
    <strong>volumes</strong>:
      - /data/gitea:/var/lib/gitea
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    <strong>ports</strong>:
      - <strong>"8889:8889"   </strong><em># web
</em><em>      </em>- <strong>"222:2222"    </strong><em># ssh</em></pre> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span>拉起的Gitea代码托管服务，试试从这里，而不是Github克隆Pigsty的源代码：</span></span></p> 
<pre><span style="color:#0073bf">git </span>clone http://git.pigsty.cc/vonng/pigsty
</pre> 
<p style="color:#222222; margin-left:0; margin-right:.8em; text-align:start"><span>当然，你也可以使用同样的方式拉起其他的代码托管平台，例如Gogs或Gitlab。公开Demo地址：</span><span>http://git.pigsty.cc</span></p> 
<h3><span>数据库管控平台</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>PgAdmin4是老牌的PostgreSQL管控工具，提供了很多实用有趣的功能，虽说对专家相当鸡肋，但对于新手还是很好用的一款管控软件。Pigsty提供了最新的6.9版本Pgadmin4支持，只需一行命令，即可启动镜像，并自动加载 Pigsty 中所有托管数据库实例列表。</span></p> 
<pre><span style="color:#0073bf">cd </span>~/pigsty/app/pgadmin; <span style="color:#0073bf">make </span>up ; <span style="color:#0073bf">make </span>conf</pre> 
<p><img height="441" src="https://oscimg.oschina.net/oscnet/up-f3ece2488d18aaf7bbf6479d995fce854eb.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:.8em; text-align:start"><span>你可以直接访问 </span><span>http://adm.pigsty.cc</span><span> ，用户名 </span><span>admin@pigsty.cc</span><span> ，密码 pigsty，看看PGAdmin4的功能。</span></p> 
<h3><span>模式变更工具</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Bytebase是一款为PostgreSQL设计的模式变更管理工具，采用Git工作流，工单-审批的方式来对数据库模式进行版本控制。而Bytebase本身的元数据也使用PostgreSQL存储。所以在Pigsty v1.5中集成了Bytebase的支持，使用以下命令一键拉起Bytebase：</span></p> 
<pre><span style="color:#0073bf">cd </span>~/pigsty/app/bytebase; <span style="color:#0073bf">make </span>up;</pre> 
<p><img height="685" src="https://oscimg.oschina.net/oscnet/up-99aae919cf6c59cf9b15a85f51e5c106f7c.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:.8em; text-align:start"><span>你可以直接访问 </span><span>http://ddl.pigsty.cc</span><span> ，用户名 </span><span>admin@pigsty.cc</span><span> ，密码 pigsty，自行尝试一下ByteBase的功能。</span></p> 
<h3><span>网页客户端工具</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>有时候，用户想使用个人账号从生产数据库中小批量的查询一些数据，这时候基于浏览器的PostgreSQL客户端就会很好用。PGWEB就是这样的一个组件，你可以将其部署在元节点或专用堡垒机上，并设置特定的HBA规则来允许个人用户查询生产只读实例。使用以下命令拉起PGWEB镜像：</span></p> 
<pre><span style="color:#0073bf">cd </span>~/pigsty/app/pgweb; <span style="color:#0073bf">make </span>up;</pre> 
<p><img height="347" src="https://oscimg.oschina.net/oscnet/up-a18141e5490bb958fbe2c2319c90d9dbb40.png" width="500" referrerpolicy="no-referrer"></p> 
<p>你<span>可以直接访问 http://cli.pigsty.cc</span><span> ，并使用以下连接串连接至测试数据库：</span></p> 
<pre>postgres://test:test@10.10.10.11:5432/test?sslmode=disable</pre> 
<h3><span>对象存储Minio</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>对象存储是云厂商提供的基础服务，在私有部署条件下，可以使用Minio快速搭建您自己的对象存储。他可以用于存储文档，图像，视频，备份，自动进行冗余备份与容灾。并对外提供标准的，S3兼容的API。</span></p> 
<pre>cd ~/pigsty/app/minio; make up;</pre> 
<p><img height="446" src="https://oscimg.oschina.net/oscnet/up-ccd1bb846a15bf757552c9397700ea48ec7.png" width="500" referrerpolicy="no-referrer"></p> 
<p><span>你可以直接访问 http://sss.pigsty.cc</span><span> ，用户名 admin ，密码 pigsty.minio，自行尝试一下Minio控制台的功能。</span></p> 
<p><span>或者，你也可以试试，直接从Minio下载最新的Pigsty v1.5 源代码：</span></p> 
<pre>http://sss.pigsty.cc/pigsty/v1.5.0/pigsty.tgz</pre> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>（非常不推荐从这里下载，这是个公开的Bucket，试试就行了）</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>在Minio的基础上，你可以进一步使用JuiceFS，将对象存储提供的大规模分布式对象存储转换为文件系统，供其他服务使用。</span></p> 
<h2><span>数据分析环境：Jupyter</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty提供了一个趁手的的数据分析工具：Jupyter Lab，你可以基于此，使用Python与SQL进行组合数据处理与分析。Jupyter Lab默认并不是通过Docker启动的，而是由元节点受限的操作系统用户直接运行，以便于与数据库交互。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="288" src="https://oscimg.oschina.net/oscnet/up-05aab94690db95f5b82e06bda00cbf3b178.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:.8em; text-align:start"><span>Demo网址，</span><span>http://lab.pigsty.cc/</span><span> ， 密码 pigsty ，使用 </span><span><span>infra-jupyter.yml</span></span><span> 在管理节点裸机上启用Jupyter Notebook。</span></p> 
<h3><span>数据库模式报表SchemaSPY</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>此外，还有一些趁手的工具也可以使用Docker或包装脚本，方便地使用。例如，当您想生成某一个数据库模式的详情报表时，不妨试试 SchemaSPY，例如，以下命令将生成Pigsty元数据库的模式报表</span></p> 
<pre><span style="color:#0073bf">bin/schemaspy </span>10.10.10.10 meta pigsty</pre> 
<p><img height="539" src="https://oscimg.oschina.net/oscnet/up-3da6c2b3b440ea6dcea6f1459b2ee87a360.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:.8em; text-align:start"><span>公开Demo地址：</span><span>http://home.pigsty.cc/schema/meta/pigsty/</span></p> 
<h3><span>数据库日志分析报表</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>当你想查阅数据库日志的汇总摘要信息时，可以试试Pgbadger，以下命令将生成某节点PG实例日志的汇总摘要：</span></p> 
<pre><span style="color:#0073bf">bin/</span>pglog-summary 10.10.10.10</pre> 
<p><img height="603" src="https://oscimg.oschina.net/oscnet/up-e45ba105e4ce6f2434beaf1d380d0567dc9.png" width="500" referrerpolicy="no-referrer"></p> 
<p><span>公开Demo地址，http://home.pigsty.cc/report</span></p> 
<h3><span>其他应用</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>此外，还有很多知名的软件应用都可以使用Pigsty + Docker一键拉起，后续将不断补充更多的教程与模板。</span></p> 
<ul> 
 <li><span><span>Gitlab</span></span><span>：使用PG的开源代码托管平台。</span></li> 
 <li><span><span>Habour</span></span><span>：使用PG的开源镜像仓库</span></li> 
 <li><span><span>Jira</span></span><span>：使用PG的开源项目管理平台。</span></li> 
 <li><span><span>Confluence</span></span><span>：使用PG的开源知识托管平台。</span></li> 
 <li><span><span>Odoo</span></span><span>：使用PG的开源ERP</span></li> 
 <li><span><span>Mastodon</span></span><span>：基于PG的社交网络</span></li> 
 <li><span><span>Discourse</span></span><span>：基于PG与Redis的开源论坛</span></li> 
 <li><span>KeyCloak：开源SSO单点登录解决方案</span></li> 
</ul> 
<h2><span>更好的冷备份</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>数据故障大体可以分为两类<strong><span>：硬件故障/资源不足</span></strong></span><span>（坏盘/宕机），</span><span><strong><span>软件缺陷/人为错误</span></strong></span><span>（删库/删表）。</span><span><strong><span>基于主从复制的物理复制用于应对前者，延迟从库与冷备份通常用于应对后者</span></strong></span><span>。因为误删数据的操作会立刻被复制到从库上执行，所以热备份与温备份都无法解决诸如 DROP DATABASE，DROP TABLE这样的错误，需要使用</span><span><strong><span>冷备份</span></strong></span><span>或</span><span><strong><span>延迟从库</span></strong></span><span>。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>在Pigsty 1.5中，对冷备份机制进行了改善：添加了定时任务机制每天制作全量冷备份（以前是给用户脚本自己做，现在想想还是送佛送到西比较好）；改善了延迟从库的创建机制，只需声明即可自动创建；对于专家用户，还提供了<code>pg_probackup</code></span><span>作为备份解决方案。此外，内置的minio Docker镜像将为后续的开箱即用的异地灾备中心奠定基础。</span></p> 
<h3><span>定时任务</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty v1.5 支持了为节点配置定时任务，包括追加与覆盖 <code>/etc/crontab</code></span><span> 两种模式。你可以将制作基础物理冷备份，日志分析，模式转储，垃圾回收，分析统计任务以统一的，声明式的方式管理起来。例如，Pigsty Demo的管理节点上就配置有以下的定时任务。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="138" src="https://oscimg.oschina.net/oscnet/up-7c6ec217c78535f9d7ce48b580b217d2e14.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:.8em; text-align:start"><span>其中最重要的就是第一条，默认在每天凌晨1点制作一个全量备份，加上Pigsty默认自带的最近一天WAL日志归档，您可以将数据库恢复至1天内的任意状态，为软件缺陷，人为故障导致的删库删表提供了有力的兜底。</span></p> 
<h3><span>延迟从库</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>在Pigsty v1.5中，创建延迟从库不再需要手工执行 </span><span style="color:#0073bf">patronictl </span><span style="color:#000000">edit-config </span>调整集群配置了，您只需像下面这样声明，即可为集群创建一个延迟从库（集群）。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="190" src="https://oscimg.oschina.net/oscnet/up-7515ef2eb8d913b4f2869a0d269c9658f2d.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:.8em; text-align:start">关于Pigsty对于冷备份的支持，可以参考前一篇文章：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODAyNTM5Ng%3D%3D%26mid%3D2247485093%26idx%3D1%26sn%3D5815f71f1d832101d35a75f5aa4acd3c%26chksm%3Dfe4b337ec93cba68fbf30eb0ed50d052c6e8972d42cf506051b5016668f4555edaa0756688dc%26scene%3D21%23wechat_redirect" target="_blank">云RDS：从删库到跑路</a></p> 
<h2><span>CMDB兼容性改进</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty有一个可选的CMDB，允许您用元节点上的默认PostgreSQL数据库存储配置，而不是默认的配置文件 <code>pigsty.yml</code></span><span>。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty CMDB最早于0.8版本引入，当时只是为了支持PostgreSQL而设计，当Pigsty开始支持Redis、GPSQL，以及更多种类的数据库时，就开始显得不合时宜了。因此在Pigsty v1.5中， 对CMDB进行了重新的设计。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="521" src="https://oscimg.oschina.net/oscnet/up-0c8ad3cb6ad98de065b4c8c88902426b421.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#222222">你只要使用</span><span style="color:#222222"><code>bin/inventory_load</code></span><span style="color:#222222"> 即可将当前使用的配置文件加载入CMDB中，使用</span><span style="color:#222222"><code>bin/inventory_cmdb</code></span><span style="color:#222222">切换为CMDB模式。使用CMDB时，您可以直接通过Grafana的CMDB Overview面板，查阅可视化的配置清单：</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="489" src="https://oscimg.oschina.net/oscnet/up-3c1068625ce11d733922c2c77dacb2fef5b.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">你<span style="background-color:#ffffff; color:#222222">可以从CMDB Overview中看到PGSQL，REDIS，以及Greenplum/MatrixDB集群的成员信息。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#222222"><img alt height="731" src="https://oscimg.oschina.net/oscnet/up-1c581eb1a49d31c5965c2153f8ebaaccb24.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>你可以直接通过SQL来调整配置，但也可以通过另一种方式：即由PostgREST暴露的API来调整配置，例如创建新的集群，扩容缩容等。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>PostgREST是一个自动根据 PostgreSQL 数据库模式生成 REST API的二进制组件。打包在Pigsty v1.5自带的Docker镜像包中。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>例如，以下命令将使用docker拉起 postgrest ，监听本地 8884 端口，使用默认管理员用户，暴露Pigsty CMDB模式。</span></p> 
<pre><span style="color:#0073bf">cd </span>~/pigsty/app/postgrest; <span style="color:#0073bf">make </span>up;
</pre> 
<p><span style="background-color:#ffffff; color:#222222">更有趣的是，它还可以通过Swagger OpenAPI Spec自动生成API的定义，并自动使用 Swagger Editor暴露API文档，生成不同编程语言的客户端存根。</span></p> 
<p><img height="679" src="https://oscimg.oschina.net/oscnet/up-7d23ada7bf7b18e8ce161fd1ba85c2c8475.png" width="500" referrerpolicy="no-referrer"></p> 
<p><span>PostgREST不仅仅可以用来暴露CMDB的增删改查接口。如果你已经有了一个设计得当的数据库模式，那么使用PostgREST可以立即构建出一个后端REST API服务，无需手工编写繁琐重复的增删改查逻辑，复杂的逻辑可以通过存储过程对外暴露。</span></p> 
<p><span>PostgREST暴露的API提供了简单的JWT认证功能，虽然大多数时候已然足够，但如果您需要更强大的API支持，可以考虑API网关Kong。它可以让任何已有API变成功能完备的接口服务。它可以为API启用多种认证签名机制，自动记录日志，设置Trace，进行限流与容端。Kong基于Nginx + Lua （OpenResty）实现，使用PostgreSQL与Redis存储元数据，使用以下命令，即可在Pigsty中启用Kong：</span></p> 
<pre><span style="color:#0073bf">cd </span>~/pigsty/app/kong; <span style="color:#0073bf">make </span>up;</pre> 
<p><img height="267" src="https://oscimg.oschina.net/oscnet/up-62205cf54055a71384abdcd6c620fcf2edd.png" width="500" referrerpolicy="no-referrer"></p> 
<h2><span>基础设施监控</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>在Pigsty v1.5中，基础设施本身的监控进行了重大改进：INFRA，和NODES，PGSQL与REDIS现在采用一样的管理模式：基础设施通过<code>infra_register</code></span><span> 角色完成自身的服务注册，将自己添加到Prometheus的监控对象中。Grafana中相应添加了监控面板。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="456" src="https://oscimg.oschina.net/oscnet/up-7b32feec4ce22d45a8281a1cc5efd449ed6.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#222222">Pigsty v1.5的Home监控，基础设施作为嫩绿色的组件，与NODES，REDIS，PGSQL采用同种方式列入Instance中。此外，Infra服务也会注册至Service Registry（Consul），并可通过服务发现自动管理。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#222222"><img alt height="542" src="https://oscimg.oschina.net/oscnet/up-6a4535bf0c1a8c3ac736af8dfb0af7462f3.png" width="500" referrerpolicy="no-referrer"></span></p> 
<blockquote> 
 <p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#777777">INFRA Overview 提供了所有基础设施组件基本状态与快速导航</span></p> 
</blockquote> 
<p><img alt height="781" src="https://oscimg.oschina.net/oscnet/up-f12ad1e814b3db3f52dad657cee77b64a95.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p><span style="background-color:#ffffff; color:#777777">Prometheus Overview：时序数据库自监控</span> </p> 
</blockquote> 
<p><img alt height="654" src="https://oscimg.oschina.net/oscnet/up-32bebc38c64e371dc5b87fac169ea89c6fb.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p><span style="background-color:#ffffff; color:#777777">Grafana Overview：监控面板自监控</span> </p> 
</blockquote> 
<p><img alt height="609" src="https://oscimg.oschina.net/oscnet/up-54581363b1b655accc601c49cb9c6c27ce9.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>Loki Overview：日志收集组件自监控</span></p> 
</blockquote> 
<h2><span>ETCD作为DCS</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>在Pigsty v1.5中，你可以使用ETCD作为Consul的替代，用于PostgreSQL数据库高可用所需的DCS。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>与Consul相比，ETCD少了服务发现，内建DNS，健康检查，以及开箱即用的UI，但是ETCD无需Agent部署简单，依托K8s生态的流行度更高，比Consul少一个失效点，更好的指标可观测性。只需指定 <code>pg_dcs_type: etcd</code></span><span>，即可使用ETCD作为DCS。此外，您可以同时使用Consul与Etcd，两者并行不悖：例如使用ETCD作为DCS，而使用Consul进行服务发现。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty 1.5针对ETCD与Consul进行了开箱即用的监控面板：DCS Overview</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><img alt height="738" src="https://oscimg.oschina.net/oscnet/up-a94441e8f8413a5fd90e23fa8caede0b830.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="color:#222222; margin-left:0; margin-right:.8em; text-align:start"><span>目前ETCD作为DCS属于最小可用功能实现，并没有添加CA证书与TLS支持，将在后续版本安全性加固专项中补充。</span></p> 
<h2><span>更好的日志收集与呈现</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>在Pigsty v1.5中，默认为每一个上游服务启用单独的访问日志，所有字段均由Loki解析，可以直接进行分析。如果您有网站挂在Pigsty上，可以立刻进行交互式日志流量分析与统计。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><img alt height="674" src="https://oscimg.oschina.net/oscnet/up-dba462b4d017ccc623c3a89ac5b44219a49.png" width="500" referrerpolicy="no-referrer"></span></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>NGINX Overview：展示Nginx指标与日志</span></p> 
</blockquote> 
<h2><span>其他改进</span></h2> 
<h3><span>监控系统</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><strong><span>监控面板</span></strong></span></p> 
<ul> 
 <li><span>CMDB Overview：可视化Pigsty CMDB Inventory。</span></li> 
 <li><span>DCS Overview：查阅Consul与ETCD集群的监控指标。</span></li> 
 <li><span>Nginx Overview：查阅Pigsty Web访问指标与访问日志。</span></li> 
 <li><span>Grafana Overview：Grafana自我监控</span></li> 
 <li><span>Prometheus Overview：Prometheus自我监控</span></li> 
 <li><span>INFRA Dashboard进行重制，反映基础设施整体状态</span></li> 
</ul> 
<p style="margin-left:.5rem; margin-right:0"><span><strong><span>监控架构</span></strong></span></p> 
<ul> 
 <li><span>现在允许使用 Consul 进行服务发现（当所有服务注册至Consul时）</span></li> 
 <li><span>现在所有的Infra组件会启用自我监控，并通过</span><span><code>infra_register</code></span><span>角色注册至Prometheus与Consul中。</span></li> 
 <li><span>指标收集器 pg_exporter 更新至 v0.5.0，添加新功能，</span><span><code>scale</code></span><span> 与 </span><span><code>default</code></span><span>，允许为指标指定一个倍乘因子，以及指定默认值。</span></li> 
 <li><span><code>pg_bgwriter</code></span><span>, </span><span><code>pg_wal</code></span><span>, </span><span><code>pg_query</code></span><span>, </span><span><code>pg_db</code></span><span>, </span><span><code>pgbouncer_stat</code></span><span> 关于时间的指标，单位由默认的毫秒或微秒统一缩放至秒。</span></li> 
 <li><span><code>pg_table</code></span><span> 中的相关计数器指标，现在配置有默认值 </span><span><code>0</code></span><span>，替代原有的</span><span><code>NaN</code></span><span>。</span></li> 
 <li><span><code>pg_class</code></span><span>指标收集器默认移除，相关指标添加至 </span><span><code>pg_table</code></span><span> 与 </span><span><code>pg_index</code></span><span> 收集器中。</span></li> 
 <li><span><code>pg_table_size</code></span><span> 指标收集器现在默认启用，默认设置有300秒的缓存时间。</span></li> 
</ul> 
<h3><span>部署方案</span></h3> 
<ul> 
 <li><span>新增可选软件包 </span><span><code>docker.tgz</code></span><span>，带有常用应用镜像：Pgadmin, Pgweb, Postgrest, ByteBase, Kong, Minio等。</span></li> 
 <li><span>新增角色ETCD，可以在DCS Servers指定的节点上自动部署ETCD服务，并自动纳入监控。</span></li> 
 <li><span>允许通过 </span><span><code>pg_dcs_type</code></span><span> 指定PG高可用使用的DCS服务，Consul（默认），ETCD（备选）</span></li> 
 <li><span>允许通过 </span><span><code>node_crontab</code></span><span> 参数，为节点配置定时任务，例如数据库备份、VACUUM，统计收集等。</span></li> 
 <li><span>新增了 </span><span><code>pg_checksum</code></span><span>  选项，启用时，数据库集群将启用数据校验和（此前只有</span><span><code>crit</code></span><span>模板默认启用）</span></li> 
 <li><span>新增了</span><span><code>pg_delay</code></span><span>选项，当实例为Standby Cluster Leader时，此参数可以用于配置一个</span><span><strong><span>延迟从库</span></strong></span></li> 
 <li><span>新增了软件包 </span><span><code>pg_probackup</code></span><span>，默认角色</span><span><code>replicator</code></span><span>现在默认赋予了备份相关函数所需的权限。</span></li> 
 <li><span>Redis部署现在拆分为两个部分：Redis节点与Redis实例，通过</span><span><code>redis_port</code></span><span>参数可以精确控制一个具体实例。</span></li> 
 <li><span>Loki 与 Promtail 现在使用 </span><span><code>frpm</code></span><span> 制作的 RPM软件包进行安装。</span></li> 
 <li><span>DCS3配置模板现在使用一个3节点的</span><span><code>pg-meta</code></span><span>集群，与一个单节点的延迟从库。</span></li> 
</ul> 
<h3><span>软件升级</span></h3> 
<ul> 
 <li><span>升级 PostgreSQL 至 14.3</span></li> 
 <li><span>升级 Redis 至 6.2.7</span></li> 
 <li><span>升级 PG Exporter 至 0.5.0</span></li> 
 <li><span>升级 Consul 至 1.12.0</span></li> 
 <li><span>升级 vip-manager 至 v1.0.2</span></li> 
 <li><span>升级 Grafana 至 v8.5.2</span></li> 
 <li><span>升级 Loki & Promtail 至 v2.5.0，使用frpm打包。</span></li> 
</ul> 
<h3><span>问题修复</span></h3> 
<ul> 
 <li><span>修复了Loki 与 Promtail 默认配置文件名的问题</span></li> 
 <li><span>修复了Loki 与 Promtail 环境变量无法正确展开的问题</span></li> 
 <li><span>对英文文档进行了一次完整的翻译与修缮，文档依赖的JS资源现在直接从本地获取，无需互联网访问。</span></li> 
</ul> 
<h2><span>API变化</span></h2> 
<p><strong><span>New Variable</span></strong></p> 
<ul> 
 <li><span><code>node_data_dir</code></span><span> : major data mount path, will be created if not exist.</span></li> 
 <li><span><code>node_crontab_overwrite</code></span><span> : overwrite </span><span><code>/etc/crontab</code></span><span> instead of append</span></li> 
 <li><span><code>node_crontab</code></span><span>: node crontab to be appended or overwritten</span></li> 
 <li><span><code>nameserver_enabled</code></span><span>: enable nameserver on this meta node?</span></li> 
 <li><span><code>prometheus_enabled</code></span><span>: enable Prometheus on this meta node?</span></li> 
 <li><span><code>grafana_enabled</code></span><span>: enable grafana on this meta node?</span></li> 
 <li><span><code>loki_enabled</code></span><span>: enable Loki on this meta node?</span></li> 
 <li><span><code>docker_enable</code></span><span>: enable docker on this node?</span></li> 
 <li><span><code>consul_enable</code></span><span>: enable consul server/agent?</span></li> 
 <li><span><code>etcd_enable</code></span><span>: enable etcd server/clients?</span></li> 
 <li><span><code>pg_checksum</code></span><span>: enable pg cluster data-checksum?</span></li> 
 <li><span><code>pg_delay</code></span><span>: recovery min apply delay for standby leader</span></li> 
</ul> 
<p style="margin-left:0.5rem; margin-right:0px"><span><strong><span>Reforge</span></strong></span></p> 
<p style="margin-left:.5rem; margin-right:0"><span>Now <code>*_clean</code></span><span> are boolean flags to clean up existing instances during init.</span></p> 
<p style="margin-left:.5rem; margin-right:0"><span>Now <code>*_safeguard</code></span><span> are boolean flags to avoid purging running instances when executing any playbook.</span></p> 
<ul> 
 <li><span><code>pg_exists_action</code></span><span> -> </span><span><code>pg_clean</code></span></li> 
 <li><span><code>pg_disable_purge</code></span><span> -> </span><span><code>pg_safeguard</code></span></li> 
 <li><span><code>dcs_exists_action</code></span><span> -> </span><span><code>dcs_clean</code></span></li> 
 <li><span><code>dcs_disable_purge</code></span><span> -> </span><span><code>dcs_safeguard</code></span></li> 
</ul> 
<p style="margin-left:.5rem; margin-right:0"><span><strong><span>Rename</span></strong></span></p> 
<ul> 
 <li><span><code>node_ntp_config</code></span><span> -> </span><span><code>node_ntp_enabled</code></span></li> 
 <li><span><code>node_admin_setup</code></span><span> -> </span><span><code>node_admin_enabled</code></span></li> 
 <li><span><code>node_admin_pks</code></span><span> -> </span><span><code>node_admin_pk_list</code></span></li> 
 <li><span><code>node_dns_hosts</code></span><span> -> </span><span><code>node_etc_hosts_default</code></span></li> 
 <li><span><code>node_dns_hosts_extra</code></span><span> -> </span><span><code>node_etc_hosts</code></span></li> 
 <li><span><code>node_dns_server</code></span><span> -> </span><span><code>node_dns_method</code></span></li> 
 <li><span><code>node_local_repo_url</code></span><span> -> </span><span><code>node_repo_local_urls</code></span></li> 
 <li><span><code>node_packages</code></span><span> -> </span><span><code>node_packages_default</code></span></li> 
 <li><span><code>node_extra_packages</code></span><span> -> </span><span><code>node_packages</code></span></li> 
 <li><span><code>node_packages_meta</code></span><span> -> </span><span><code>node_packages_meta</code></span></li> 
 <li><span><code>node_meta_pip_install</code></span><span> -> </span><span><code>node_packages_meta_pip</code></span></li> 
 <li><span><code>node_sysctl_params</code></span><span> -> </span><span><code>node_tune_params</code></span></li> 
 <li><span><code>app_list</code></span><span> -> </span><span><code>nginx_indexes</code></span></li> 
 <li><span><code>grafana_plugin</code></span><span> -> </span><span><code>grafana_plugin_method</code></span></li> 
 <li><span><code>grafana_cache</code></span><span> -> </span><span><code>grafana_plugin_cache</code></span></li> 
 <li><span><code>grafana_plugins</code></span><span> -> </span><span><code>grafana_plugin_list</code></span></li> 
 <li><span><code>grafana_git_plugin_git</code></span><span> -> </span><span><code>grafana_plugin_git</code></span></li> 
 <li><span><code>haproxy_admin_auth_enabled</code></span><span> -> </span><span><code>haproxy_auth_enabled</code></span></li> 
 <li><span><code>pg_shared_libraries</code></span><span> -> </span><span><code>pg_libs</code></span></li> 
 <li><span><code>dcs_type</code></span><span> -> </span><span><code>pg_dcs_type</code></span></li> 
</ul> 
<h2><span>后续计划</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>后续有几件工作有着较高优先级：</span></p> 
<ol> 
 <li><span>基于 Minio 与 JuiceFS 的对象存储与备份基础设施</span></li> 
 <li><span>基于 </span><span><code>pg_probackup</code></span><span> 的进阶冷备份管理方案</span></li> 
 <li><span>自签名百年证书，针对ETCD与各路HTTP API可选启用</span></li> 
 <li><span>Pigsty精简版：基于DockerCompose的单机镜像（有监控无高可用，docker一键拉起）</span></li> 
 <li><span>Pigsty API，使用CMDB，PostgREST与Kong共同打造管控接口</span></li> 
 <li><span>Pigsty CLI，使用Pigsty API的二进制命令行工具</span></li> 
</ol>
                                        </div>
                                      
</div>
            