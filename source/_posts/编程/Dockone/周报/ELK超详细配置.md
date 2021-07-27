
---
title: 'ELK超详细配置'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/5b5d2cafe4bf6f15b0bc54b1c12b1965.jpg'
author: Dockone
comments: false
date: 2021-07-27 05:06:30
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/5b5d2cafe4bf6f15b0bc54b1c12b1965.jpg'
---

<div>   
<br><h3>ELK日志分析系统简介</h3>ELK日志分析系统是Logstash、Elasticsearch、Kibana开源软件的集合，对外是作为一个日志管理系统的开源方案，它可以从任何来源、任何格式进行日志搜索、分析与可视化展示。<br>
<h4>ELK日志分析系统组成</h4><ul><li>Elasticsearch（es）：通过搭建群集；存储日志数据，索引日志数据</li><li>Logstash ：收集日志，收集到了后给es存储</li><li>Kibana ：视图形式展现日志信息，更加人性化</li></ul><br>
<br><h4>日志处理步骤</h4><ul><li>将日志进行集中化管理</li><li>将日志格式化（Logstash）并输出到Elasticsearch</li><li>对格式化后的数据进行索引和存储（Elasticsearch）</li><li>前端数据的展示（Kibana）</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/5b5d2cafe4bf6f15b0bc54b1c12b1965.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/5b5d2cafe4bf6f15b0bc54b1c12b1965.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>三款软件各自概念</h3><h4>Elasticsearch介绍</h4><strong>Elasticsearch的概述</strong><br>
<br>提供了一个分布式多用户能力的全文搜索引擎。<br>
<br><strong>Elasticsearch核心概念</strong><br>
<ul><li>接近实时（NRT），Elasticsearch是一个接近实时的搜索平台，这意味着，从索引一个文档直到这个文档能够被搜索到有一个轻微的延迟（通常是1秒）</li><li>集群（cluster），一个集群就是由一个或多个节点组织在一起，它们共同持有你整个的数据，并一起提供索引和搜索功能。其中一个节点为主节点，这个主节点是可以通过选举产生的，并提供跨节点的联合索引和搜索的功能。集群有一个唯一性标示的名字，默认是Elasticsearch，集群名字很重要，每个节点是基于集群名字加入到其集群中的。因此，确保在不同环境中使用不同的集群名字。一个集群可以只有一个节点。强烈建议在配置Elasticsearch时，配置成集群模式。</li><li>节点（node），节点就是一台单一的服务器，是集群的一部分，存储数据并参与集群的索引和搜索功能。像集群一样，节点也是通过名字来标识，默认是在节点启动时随机分配的字符名。当然，你可以自己定义。该名字也很重要，在集群中用于识别服务器对应的节点。节点可以通过指定集群名字来加入到集群中。默认情况，每个节点被设置成加入到Elasticsearch集群。如果启动了多个节点，假设能自动发现对方，他们将会自动组建一个名为Elasticsearch的集群。</li><li>索引（type），在一个索引中，你可以定义一种或多种类型。一个类型是你的索引的一个逻辑上的分类/分区，其语义完全由你来定。通常，会为具有一组共同字段的文档定义一个类型。比如说，我们假设你运营一个博客平台并且将你所有的数据存储到一个索引中。在这个索引中，你可以为用户数据定义一个类型，为博客数据定义另一个类型，当然，也可以为评论数据定义另一个类型。</li></ul><br>
<br><strong>类型相对于关系型数据库的表</strong><br>
<br>索引（库）–》类型（表）–》文档（记录）<br>
<br><strong>分片和副本（shards&replicas）</strong><br>
<br>在实际情况下，索引存储的数据可能超过单个节点的硬件限制。如一个10亿文档需1TB空间可能不适合存储在单个节点的磁盘上，或者从单个节点搜索请求太慢了。为了解决这个问题，Elasticsearch提供将索引分成多个分片的功能。当在创建索引时，可以定义想要分片的数量。每一个分片就是一个全功能的独立的索引，可以位于集群中任何节点上。<br>
<br>每个索引可以被分成多个分片。一个索引也可以被复制0次（意思是没有复制）或多次。一旦复制了，每个索引就有了主分片（作为复制源的原来的分片）和复制分片（主分片的拷贝）之别。分片和副本的数量可以在索引创建的时候指定。<br>
<br>在索引创建之后，你可以在任何时候动态地改变副本的数量，但是你事后不能改变分片的数量。<br>
<br>默认情况下，Elasticsearch中的每个索引被分片5个主分片和1个副本，这意味着，如果你的集群中至少有两个节点，你的索引将会有5个主分片和另外5个副本分片（1个完全拷贝），这样的话每个索引总共就有10个分片。<br>
<h4>Logstash介绍</h4><ul><li>一款强大的数据处理工具</li><li>可实现数据传输、格式处理、格式化输出</li><li>数据输入（从业务输入）、数据加工（如过滤、改写等）以及数据输出（输出到Elasticsearch群集）</li><li><br>Logstash的主要组件：<br>
<ul><li>shipper：日志收集者，负责监控本地日志文件的变化，及时把日志文件的最新内容收集起来。通常，远程代理端（agent）只需要运行这个组件即可</li><li>indexer：日志存储者，负责接收日志并写入到本地文件</li><li>broker：日志hub，负责连接多个shipper和多个indexer</li><li>search and storage：允许对事件进行搜索和存储</li><li>web interface：基于Web的展示界面</li></ul></li></ul><br>
<br><h4>Kibana介绍</h4><ul><li>一个针对Elasticsearch的开源分析及可视化平台</li><li>搜索、查看存储在Elasticsearch索引中的数据</li><li>通过各种图表进行高级数据分析及展示</li><li><br>主要功能：<br>
<ul><li>Elasticsearch无缝之集成</li><li>整合数据，复杂数据分析</li><li>让更多团队成员收益</li><li>接口灵活，分享更容易</li><li>配置简单，可视化多数据源</li><li>简单数据导出</li></ul></li></ul><br>
<br><h3>ELK日志分析系统部署</h3><h4>实验环境及准备</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/35cbe7c2887b7a68b1e5b5245c2f6d92.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/35cbe7c2887b7a68b1e5b5245c2f6d92.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<pre class="prettyprint">[root@localhost ~]# hostnamectl set-hostname elk-1<br>
[root@localhost ~]# bash<br>
[root@elk-1 ~]# vim /etc/hosts   ###添加本地解析，识别集群主机名<br>
192.168.73.40 elk-1<br>
192.168.73.50 elk-2<br>
</pre><br>
<h4>实验步骤</h4><strong>elk-1和elk-2中部署Elasticsearch</strong><br>
<br>1、上传密钥，部署yum源，安装Elasticsearch及Java（两台节点）<br>
<pre class="prettyprint">[root@elk-1 ~]# rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch<br>
<br>
[root@elk-1 ~]# vim /etc/yum.repos.d/elasticsearch.repo<br>
[elasticsearch-2.x]<br>
name=Elasticsearch repository for 2.x packages<br>
baseurl=http://packages.elastic.co/elasticsearch/2.x/centos<br>
gpgcheck=1<br>
gpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch<br>
enable=1<br>
<br>
[root@elk-1 ~]# yum install -y elasticsearch java<br>
<br>
[root@elk-1 ~]# java -version  ###查看Java版本<br>
openjdk version "1.8.0_262"<br>
OpenJDK Runtime Environment (build 1.8.0_262-b10)<br>
OpenJDK 64-Bit Server VM (build 25.262-b10, mixed mode)<br>
</pre><br>
2、修改Elasticsearch主配置文件<br>
<pre class="prettyprint">[root@elk-1 ~]# vim /etc/elasticsearch/elasticsearch.yml<br>
17行 集群名称 ###两个节点一致<br>
cluster.name: abner<br>
<br>
23行 节点名称 ###两个节点不同<br>
node.name: elk-1<br>
<br>
33行 工作目录<br>
path.data: /data/es-data<br>
path.logs: /var/log/elasticsearch/<br>
<br>
43行 防止交换swap分区<br>
bootstrap.memory_lock: true<br>
<br>
54行 监听网络<br>
network.host: 0.0.0.0<br>
<br>
58行 端口<br>
http.port: 9200<br>
<br>
68行：discovery.zen.ping.unicast.hosts: ["elk-1", "elk-2"]    #集群发现通过单播实现，单播的主机名为"elk-1"，"elk-2"<br>
</pre><br>
3、创建工作目录并更改属主及属组，开启服务<br>
<pre class="prettyprint">[root@elk-1 ~]# mkdir -p /data/es-data<br>
[root@elk-1 ~]# chown -R elasticsearch.elasticsearch /data/es-data<br>
[root@elk-1 ~]# systemctl start elasticsearch.service<br>
[root@elk-1 ~]# netstat -anpt | grep 9200<br>
tcp6       0      0 :::9200                 :::*                    LISTEN      46814/java<br>
</pre><br>
<br>4、测试<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/6e76f83c755a062c7ed4ae0b073fabe5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/6e76f83c755a062c7ed4ae0b073fabe5.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/abb7cf8fdaee2b07257814bf39eb14b3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/abb7cf8fdaee2b07257814bf39eb14b3.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
5、两种方法和ES进行交互<br>
<ul><li>第一种：Java API</li><li>第二种：RESTful API （通过json格式交互）</li></ul><br>
<pre class="prettyprint">[root@elk-1 ~]# curl -i -XGET 'http://192.168.73.40:9200/_count?pretty' -d '&#123;<br>
> "query": &#123;<br>
>     "match_all": &#123;&#125;<br>
> &#125;<br>
> &#125;'<br>
HTTP/1.1 200 OK<br>
Content-Type: application/json; charset=UTF-8<br>
Content-Length: 95<br>
<br>
&#123;<br>
"count" : 0,<br>
"_shards" : &#123;<br>
"total" : 0,<br>
"successful" : 0,<br>
"failed" : 0<br>
&#125;<br>
&#125; <br>
</pre><br>
<br>6、两个节点安装elasticsearch-head插件（安装插件可以更加人性化的管理集群）<br>
<pre class="prettyprint">[root@elk-1 ~]# /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head<br>
……省略内容<br>
Installed head into /usr/share/elasticsearch/plugins/head ###安装位置<br>
</pre><br>
<br>7、测试——输入192.168.73.40:9200/_plugin/head/<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/2d29725bbac412cf275551cde934e096.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/2d29725bbac412cf275551cde934e096.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
8、复合查询<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/3bc441cea2319d6fde70c0350a13a36e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/3bc441cea2319d6fde70c0350a13a36e.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/4768568700c1f72181ff8d4ac14f6b27.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/4768568700c1f72181ff8d4ac14f6b27.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
9、删除<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/642d38d149bbe2431e368e054040d744.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/642d38d149bbe2431e368e054040d744.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
10、node-01和node-02日志提示不让锁内存<br>
<pre class="prettyprint">[root@elk-1 ~]# less /var/log/elasticsearch/abner.log<br>
# allow user 'elasticsearch' mlockall<br>
    elasticsearch soft memlock unlimited<br>
    elasticsearch hard memlock unlimited<br>
</pre><br>
<pre class="prettyprint">[root@elk-1 ~]# vim /etc/security/limits.conf  ###末尾插入<br>
[root@elk-1 ~]# systemctl stop elasticsearch.service<br>
[root@elk-1 ~]# systemctl start elasticsearch.service<br>
</pre><br>
11、安装监控组件<br>
<pre class="prettyprint">[root@elk-1 ~]# /usr/share/elasticsearch/bin/plugin install lmenezes/elasticsearch-kopf<br>
……省略内容<br>
Installed kopf into /usr/share/elasticsearch/plugins/kopf  ###安装路径<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/f2284d09d0549c1b3e8aee00f0493ec5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/f2284d09d0549c1b3e8aee00f0493ec5.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>Apache主机中安装Logstash并做日志搜集</strong><br>
<br>1、修改主机名<br>
<pre class="prettyprint">[root@localhost ~]# hostnamectl set-hostname apache<br>
[root@localhost ~]# bash<br>
</pre><br>
2、安装apache服务<br>
<pre class="prettyprint">[root@apache ~]# yum install -y httpd<br>
[root@apache ~]# systemctl start httpd<br>
</pre><br>
3、安装Java环境，没有自带安装使用yum -y install java安装<br>
<pre class="prettyprint">[root@apache ~]# yum install -y java<br>
已加载插件：fastestmirror, langpacks<br>
Loading mirror speeds from cached hostfile<br>
软件包 1:java-1.8.0-openjdk-1.8.0.131-11.b12.el7.x86_64 已安装并且是最新版本<br>
无须任何处理<br>
[root@apache ~]# java -version<br>
openjdk version "1.8.0_131"<br>
OpenJDK Runtime Environment (build 1.8.0_131-b12)<br>
OpenJDK 64-Bit Server VM (build 25.131-b12, mixed mode)<br>
</pre><br>
4、上传密钥，部署yum源，安装Logstash<br>
<pre class="prettyprint">[root@apache ~]# vi /etc/yum.repos.d/logstash.repo<br>
[logstash-2.1]<br>
name=Logstash repository for 2.1.x packages<br>
baseurl=http://packages.elastic.co/logstash/2.1/centos<br>
gpgcheck=1<br>
gpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch<br>
enable=1<br>
<br>
[root@apache ~]# yum install -y logstash<br>
[root@apache ~]# ln -s /opt/logstash/bin/* /usr/local/bin ###优化执行路径<br>
</pre><br>
5、Logstash（apache）与Elasticsearch（node）功能是否正常，做对接测试<br>
<pre class="prettyprint">Logstash命令选项解释：<br>
-f：指定logstash的配置文件，根据配置文件配置logstash<br>
-e：后面跟着字符串，该字符串可以被当做logstash的配置（如果是“ ”，则默认使用stdin做输入，stdout为输出）<br>
-t：测试配置文件是否正确，然后退出<br>
<h1>输入采用标准输入，输出采用标准输出</h1>定义输入和输出流，类似管道<br>
[root@apache ~]# logstash -e 'input &#123; stdin&#123;&#125; &#125; output &#123; stdout&#123;&#125; &#125;' <br>
</pre><br>
<br>6、使用rubydebug显示详细输出，codec为一种编解码器<br>
<pre class="prettyprint">[root@apache ~]# logstash -e 'input &#123; stdin&#123;&#125; &#125; output &#123; stdout&#123; codec => rubydeb<br>
</pre><br>
7、使用Logstash将信息输出给Elasticsearch<br>
<pre class="prettyprint">[root@apache ~]# logstash -e 'input &#123; stdin&#123;&#125; &#125; output &#123; elasticsearch &#123; hosts => ["192.168.73.40:9200"] &#125; &#125;'<br>
Settings: Default filter workers: 1<br>
Logstash startup completed<br>
<br>
abc123<br>
tom456<br>
123jerry<br>
</pre><br>
8、打开浏览器输入<a href="http://192.168.73.40:9100/" rel="nofollow" target="_blank">http://192.168.73.40:9100/</a>，查看索引信息，显示新的数据信息说明输出到Elasticsearch成功<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/f26801ca5030e29f7d749534a493682a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/f26801ca5030e29f7d749534a493682a.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
9、在Apache主机中做对接配置<br>
<pre class="prettyprint">[root@apache ~]# chmod o+r /var/log/messages  ###允许其他用户访问<br>
[root@apache ~]# ll /var/log/messages<br>
-rw----r--. 1 root root 439103 11月 18 15:20 /var/log/messages<br>
<br>
[root@apache ~]# vim /etc/logstash/conf.d/system.conf<br>
input &#123;                       ###Logstash输入：从/var/log/messages输入，类型为system，起始位<br>
    file &#123;<br>
      path => "/var/log/messages"<br>
      type => "system"<br>
      start_position => "beginning"<br>
    &#125;<br>
  &#125;<br>
<br>
output &#123;                      ###Logstash输出：输出给Elasticsearch（以IP地址指定位置）<br>
    elasticsearch &#123;<br>
    hosts => ["192.168.73.40:9200"]<br>
    index => "system-%&#123;+YYY.MM.dd&#125;"<br>
    &#125;<br>
  &#125;<br>
<br>
[root@apache ~]# systemctl restart logstash<br>
</pre><br>
10、打开浏览器输入<a href="http://192.168.73.40:9100/" rel="nofollow" target="_blank">http://192.168.73.40:9100/</a>，查看索引信息，显示新的索引信息代表Logstash搜集到的日志信息成功输出给Elasticsearch<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/1b631eade6ef4d0686c8f753f58256fd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/1b631eade6ef4d0686c8f753f58256fd.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>在node1主机安装Kibana</strong><br>
<br>1、在node1主机安装Kibana<br>
<pre class="prettyprint">[root@elk-1 ~]# tar zxf kibana-4.3.1-linux-x64.tar.gz<br>
[root@elk-1 ~]# vim kibana-4.3.1-linux-x64/config/kibana.yml<br>
//2行 <br>
server.port: 5601<br>
<br>
//5行<br>
server.host: "0.0.0.0"<br>
<br>
<br>
//12行 ES地址<br>
elasticsearch.url: "http://192.168.73.40:9200"<br>
<br>
//20行<br>
kibana.index: ".kibana"<br>
<br>
yum install screen -y<br>
<br>
<br>
[root@elk-1 ~]# kibana-4.3.1-linux-x64/bin/kibana  ###启动监听<br>
log   [15:43:45.084] [info][status][plugin:kibana] Status changed from uninitialized to green - Ready<br>
log   [15:43:45.105] [info][status][plugin:elasticsearch] Status changed from uninitialized to yellow - Waiting for Elasticsearch<br>
log   [15:43:45.113] [info][status][plugin:kbn_vislib_vis_types] Status changed from uninitialized to green - Ready<br>
log   [15:43:45.119] [info][status][plugin:markdown_vis] Status changed from uninitialized to green - Ready<br>
log   [15:43:45.123] [info][status][plugin:metric_vis] Status changed from uninitialized to green - Ready<br>
log   [15:43:45.125] [info][status][plugin:spyModes] Status changed from uninitialized to green - Ready<br>
log   [15:43:45.132] [info][status][plugin:statusPage] Status changed from uninitialized to green - Ready<br>
log   [15:43:45.135] [info][status][plugin:table_vis] Status changed from uninitialized to green - Ready<br>
log   [15:43:45.136] [info][status][plugin:elasticsearch] Status changed from yellow to green - Kibana index ready<br>
log   [15:43:45.146] [info][listening] Server running at http://0.0.0.0:5601<br>
</pre><br>
<br>2、浏览器中登录<a href="http://192.168.73.40:5601/" rel="nofollow" target="_blank">http://192.168.73.40:5601</a>，首次登录提示创建一个索引名字：填入system-*，即对接系统日志文件名。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/e647f383e63a42225065210c49d8221e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/e647f383e63a42225065210c49d8221e.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/5a9ce0aee45e98074644e2c4a5968c92.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/5a9ce0aee45e98074644e2c4a5968c92.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原文链接：<a href="https://blog.csdn.net/weixin_47403060/article/details/109758406" rel="nofollow" target="_blank">https://blog.csdn.net/weixin_4 ... 58406</a>，作者：wuhaihong17
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            