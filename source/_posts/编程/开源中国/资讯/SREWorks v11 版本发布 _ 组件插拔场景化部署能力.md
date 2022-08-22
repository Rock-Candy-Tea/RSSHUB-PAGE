
---
title: 'SREWorks v1.1 版本发布 _ 组件插拔场景化部署能力'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cc7da2582818f5a289355415e62309ec340.png'
author: 开源中国
comments: false
date: Mon, 22 Aug 2022 15:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cc7da2582818f5a289355415e62309ec340.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>自SREWorks v1.0 版本在3月份开源以来，通过钉钉群、微信群、GitHub等渠道，团队陆续收到了各种反馈。随即团队开始了v1.1版本的功能优化迭代，优先解决用户反馈上来的TOP3问题:<strong>存储插拔、最小资源部署、存储类使用</strong>，同时针对用户使用过程中暴露出来的小问题也做了相应的优化。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>后续产品会持续保持较快的发布频率，快速解决各渠道用户反馈的痛点问题，帮助用户利用SREWorks更好地构建云原生下的数智运维平台。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>下面是本次 v1.1 版本发布的新功能介绍:</span></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:justify"><strong>1. 基础版/数智版</strong></h3> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>k8s集群的资源消耗让不少尝鲜用户望而却步，因此v1.1版本将基础应用和数智应用部署分离，让用户可以只体验SREWorks的底座平台，而不开启较占用资源的数智化应用。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>基础版SREWorks在<strong>单台4核16G</strong>机器上即可正常启动。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>基础应用包含8个应用: </span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span>运维中台</span></p> </li> 
 <li> <p><span>应用管理</span></p> </li> 
 <li> <p><span>团队管理</span></p> </li> 
 <li> <p><span>集群管理</span></p> </li> 
 <li> <p><span>模板中心</span></p> </li> 
 <li> <p><span>帮助中心</span></p> </li> 
 <li> <p><span>文件管理</span></p> </li> 
 <li> <p><span>系统设置</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>数智应用包含7个应用: </span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>数据运维平台</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>智能运维平台</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>故障自愈</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>健康管理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>运营中心</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>作业调度平台</span></p> </li> 
 <li> <p><span>运维搜索</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>在进行helm部署的时候，传入如下参数即可使用基础版(默认为数智版):</span></p> 
<pre><code>--set saas.onlyBase=true</code></pre> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><strong>2. 组件插拔: ElasticSearch/MySQL/MinIO</strong></h3> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>当前不少公司的生产环境下均包含可靠的存储模块，比如ES/MySQL/MinIO等，所以部分用户在部署应用时不希望使用SREWorks v1.0版本中自带的存储模块，而是希望将那些中间件的endpoint直接注入。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>团队经过整理和优化，将SREWorks中使用的各种存储模块，抽取出变量支持用户在部署时修改。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>在进行helm部署的时候，根据需求传入如下参数即可:</span></p> 
<pre><code>
# 替换基础应用的主MySQL数据库
# MySQL这块需要注意，通常将主MySQL数据库和数智化MySQL数据库(吞吐较大)分成两个

--set appmanager.server.database.host="*.mysql.rds.aliyuncs.com" 
--set appmanager.server.database.password="****"
--set appmanager.server.database.user="root"
--set appmanager.server.database.port=3306
--set appmanagerbase.mysql.enabled=false

# 替换数智化应用的MySQL数据库
--set saas.dataops.dbHost="*.mysql.rds.aliyuncs.com"
--set saas.dataops.dbUser=root
--set saas.dataops.dbPassword="*****"
--set saas.dataops.dbPort=3306

# 替换数智化应用的ElasticSearch
--set saas.dataops.esHost="*.public.elasticsearch.aliyuncs.com"
--set saas.dataops.esPort="9200"
--set saas.dataops.esUser="elastic"
--set saas.dataops.esPassword="*******"

# 替换基础应用的MinIO存储
--set global.minio.accessKey="*******"
--set global.minio.secretKey="*******"
--set appmanager.server.package.endpoint="minio.*.com:9000"
--set appmanagerbase.minio.enabled=false</code></pre> 
<h3><strong>3. 页面模板中心</strong></h3> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>低代码的前端开发模式，对于之前没有接触过相关应用的用户依然存在一定的门槛，于是团队借鉴了文档模板的这一概念，将前端组件按照常见的场景类别编排成模板，让用户可以快速导入一个现成的模板页面，在模板之上继续进行前端开发。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>同时v1.1版本也支持用户将自己常用的页面保存成模板，提升日常的页面开发效率。</span></p> 
<p style="text-align:center"><img height="467" src="https://oscimg.oschina.net/oscnet/up-cc7da2582818f5a289355415e62309ec340.png" width="1348" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><img height="703" src="https://oscimg.oschina.net/oscnet/up-fdafb14fd92333dc865d5f18ef531ee5bd0.png" width="1353" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><strong>4. 默认存储类支持</strong></h3> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>很多使用k8s的用户不太清楚StorageClass的使用逻辑，常在这个问题的排查上耗费较多时间。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>在综合分析比较了各种社区存储方案后，v1.1版本使用了基于OpenEBS的方案，给用户提供了一个默认的LocalPV方案，减少大家的使用成本。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span>用户在使用时务必注意，如果使用自己架设的存储集或该k8s集群已经有存储类，请务必将这个默认<span>存储</span><span>类</span>对应的存储供应openebs关闭，否则容易出现存储目录争抢的问题。</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>关闭SREWorks默认存储类方案的helm参数如下，以使用阿里云ACK集群的存储类alicloud-disk-available为例:</span></p> 
<pre><code>--set appmanagerbase.openebs.enabled=false
--set global.storageClass="alicloud-disk-available"</code></pre> 
<h3><strong>5. 其他优化</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span>解决后端微服务的编辑页面报错</span></p> </li> 
 <li> <p><span>增加后端微服务的默认鉴权开关</span></p> </li> 
 <li> <p><span>解决运维应用删除报错</span></p> </li> 
 <li> <p><span>解决appmanager多次初始化的幂等异常</span></p> </li> 
 <li> <p><span>解决在慢数据库场景下productopsv2导入时候的报错(针对NFS慢数据库场景同样有效)</span></p> </li> 
 <li> <p><span>数据源密码框采用密码输入</span></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><strong>6.如何从当前版本升级到v1.1</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span>升级包含底座，故可能页面会有5-10分钟的不可访问，请注意。</span></p> </li> 
 <li> <p><span>用户自行开发的云原生应用不会受影响(不重启)，SREWorks网关到应用的流量会有中断。</span></p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:justify"><code><span>git clone http://github.com/alibaba/sreworks.git -b v1.1 sreworks</span></code>
<code><span>cd sreworks</span></code><code><span>./sbin/upgrade-cluster.sh --kubeconfig="****"</span></code></pre> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>如在使用过程中遇到问题，欢迎各位在GitHub中提出Issues或Pull requests。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span>SREWorks开源地址：</span></strong></p> 
<p><span>https://github.com/alibaba/sreworks</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span>更多开源项目合集：</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>https://www.aliyun.com/activity/bigdata/opensource_bigdata__ai</span></p>
                                        </div>
                                      
</div>
            