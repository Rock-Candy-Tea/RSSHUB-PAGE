
---
title: '轻量级日志分析平台Loki实战'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210408/87e1f89fb18a81b6d9175608ccbd63c6.png'
author: Dockone
comments: false
date: 2021-04-09 04:08:41
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210408/87e1f89fb18a81b6d9175608ccbd63c6.png'
---

<div>   
<br>Loki的第一个稳定版本于2019年11月19日发布，是Grafana Labs团队最新的开源项目，是一个水平可扩展，高可用性，多租户的日志聚合系统。Loki 是专门用于聚集日志数据，重点是高可用性和可伸缩性。与竞争对手不同的是，它确实易于安装且资源效率极高。<br>
<h3>特点</h3>优点：<br>
<ul><li>Loki的架构非常简单，使用了和Prometheus一样的标签来作为索引，通过这些标签既可以查询日志的内容也可以查询到监控的数据，不但减少了两种查询之间的切换成本，也极大地降低了日志索引的存储。</li><li>与ELK相比，消耗的成本更低，具有成本效益。</li><li>在日志的收集以及可视化上可以连用Grafana，实现在日志上的筛选以及查看上下行的功能。</li></ul><br>
<br>缺点：<br>
<ul><li>技术比较新颖，相对应的论坛不是非常活跃。</li><li>功能单一，只针对日志的查看，筛选有好的表现，对于数据的处理以及清洗没有ELK强大，同时与ELK相比，对于后期，ELK可以连用各种技术进行日志的大数据处理，但是Loki不行。</li></ul><br>
<br><h3>组成</h3><ul><li>Loki是主服务器，负责存储日志和处理查询。</li><li>Promtail是代理，负责收集日志并将其发送给Loki 。</li><li>Grafana用于UI展示。</li></ul><br>
<br>本次安装使用Docker部署。<br>
<h4>安装 docker-compose</h4><pre class="prettyprint">curl -L "https://github.com/docker/compose/releases/download/1.28.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose<br>
chmod +x /usr/local/bin/docker-compose<br>
</pre><br>
<h4>下载yaml文件</h4>wget <a href="https://raw.githubusercontent.com/grafana/loki/v2.2.0/production/docker-compose.yaml" rel="nofollow" target="_blank">https://raw.githubusercontent. ... .yaml</a> -O docker-compose.yaml<br>
<pre class="prettyprint">version: "3"<br>
<br>
networks:<br>
loki:<br>
<br>
services:<br>
loki:<br>
image: grafana/loki:2.0.0<br>
ports:<br>
  - "3100:3100"<br>
command: -config.file=/etc/loki/local-config.yaml<br>
networks:<br>
  - loki<br>
<br>
promtail:<br>
image: grafana/promtail:2.0.0<br>
volumes:<br>
  - /var/log:/var/log<br>
command: -config.file=/etc/promtail/config.yml<br>
networks:<br>
  - loki<br>
<br>
grafana:<br>
image: grafana/grafana:latest<br>
ports:<br>
  - "3000:3000"<br>
networks:<br>
  - loki<br>
</pre><br>
<h4>启动服务</h4><pre class="prettyprint">docker-compose -f docker-compose.yaml up<br>
</pre><br>
<h4>检查服务</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210408/87e1f89fb18a81b6d9175608ccbd63c6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210408/87e1f89fb18a81b6d9175608ccbd63c6.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>配置服务</h4><a href="http://192.168.106.202:3000/" rel="nofollow" target="_blank">http://192.168.106.202:3000/</a><br>
<br>默认Granfna密码admin/admin<br>
<br><strong>配置数据源</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210408/17c82e1309eb5768deb21312f92c3af9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210408/17c82e1309eb5768deb21312f92c3af9.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
配置IP和默认数据源，配置完成点击测试/保存。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210408/bb77e0f321d5109fdbca1735ae624f0b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210408/bb77e0f321d5109fdbca1735ae624f0b.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>配置数据源</strong><br>
<br>explore查询样例：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210408/78b7550ece23387912f49525bd9e3921.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210408/78b7550ece23387912f49525bd9e3921.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>输出匹配日志信息</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210408/2648e610df31ba30e6ef1aacb0d7779f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210408/2648e610df31ba30e6ef1aacb0d7779f.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
至此一次样例日志查询完成。<br>
<h4>Promtail配置详解</h4>Promtail容器为日志采集容器，配置文件在Promtail容器/etc/promtail/config.yml，将该容器部署在需要采集日志的服务器上就能正常采集日志传回Loki服务收集整理。<br>
<pre class="prettyprint">root@2a0cc144dd58:/#  cat  /etc/promtail/config.yml<br>
server:<br>
http_listen_port: 9080<br>
grpc_listen_port: 0<br>
<br>
positions:<br>
filename: /tmp/positions.yaml<br>
<br>
clients:<br>
- url: http://loki:3100/loki/api/v1/push     #这里配置的地址为loki服务器日志收集的信息<br>
<br>
scrape_configs:<br>
- job_name: system<br>
static_configs:<br>
- targets:<br>
  - localhost<br>
labels:<br>
  job: varlogs                       #这里为刚才选择job下子标签<br>
  __path__: /var/log/*log            #将采集的日志放在/var/log/*log下自动发现<br>
</pre><br>
<h4>增加一台服务器日志采集</h4><strong>编写Promtail的配置文件config.yml</strong><br>
<br>mkdir /root/promtail &&cd /root/promtail<br>
<pre class="prettyprint">[root@node2 promtail]# cat config.yml <br>
server:<br>
http_listen_port: 9080<br>
grpc_listen_port: 0<br>
<br>
positions:<br>
filename: /tmp/positions.yaml<br>
<br>
clients:<br>
- url: http://192.168.106.202:3100/loki/api/v1/push     #这里配置的地址为Loki服务器日志收集的信息<br>
<br>
scrape_configs:<br>
- job_name: mysql<br>
static_configs:<br>
- targets:<br>
  - localhost<br>
labels:<br>
  job: mysql                         #这里为刚才选择job下子标签<br>
  __path__: /var/log/*log            #将采集的日志放在/var/log/*log下自动发现<br>
</pre><br>
<strong>编写docker-compose.yaml配置文件</strong><br>
<pre class="prettyprint">[root@node2 promtail]# cat  docker-compose.yaml <br>
version: "v1"<br>
<br>
services:<br>
promtail:<br>
image: grafana/promtail:2.0.0               #拉去镜像<br>
container_name: promtail-node              #镜像名称<br>
volumes:<br>
  - /root/promtail/config.yml:/etc/promtail/config.yml    #挂载目录<br>
  - /var/log:/var/log           <br>
network_mode: 'host'<br>
</pre><br>
<strong>启动</strong><br>
<pre class="prettyprint">docker-compose up -d <br>
</pre><br>
<h4>去Loki上查看检索</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210408/ff5752584835938b10a44511b5ae226d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210408/ff5752584835938b10a44511b5ae226d.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210408/81f78fe583f8dfdf0e21eb44d5bf6125.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210408/81f78fe583f8dfdf0e21eb44d5bf6125.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210408/ffade514599ecf390b609e2d3a53fb89.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210408/ffade514599ecf390b609e2d3a53fb89.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以根据数据查询到相应日志信息。<br>
<br>原文链接：<a href="https://blog.csdn.net/weixin_43546282/article/details/115325468" rel="nofollow" target="_blank">https://blog.csdn.net/weixin_4 ... 25468</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            