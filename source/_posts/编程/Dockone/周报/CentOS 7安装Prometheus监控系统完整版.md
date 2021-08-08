
---
title: 'CentOS 7安装Prometheus监控系统完整版'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/894c57ade666b43a4ac89851d684d745.png'
author: Dockone
comments: false
date: 2021-08-08 01:49:39
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/894c57ade666b43a4ac89851d684d745.png'
---

<div>   
<br><h3>普罗米修斯概述</h3>Prometheus（由Go语言开发）是一套开源的监控&报警&时间序列数据库的组合。适合监控Docker容器。因为Kubernetes（俗称K8s）的流行带动了Prometheus的发展。<br>
<h3>时间序列数据</h3><h4>什么是序列数据</h4>时间序列数据（TimeSeries Data）: 按照时间顺序记录系统、设备状态变化 的数据被称为时序数据。<br>
<br>应用的场景很多，如：<br>
<ul><li>无人驾驶车辆运行中要记录的经度，纬度，速度，方向，旁边物体的距离等等。每时每刻都要将数据记录下来做分析。</li><li>某一个地区的各车辆的行驶轨迹数据</li><li>传统证券行业实时交易数据</li><li>实时运维监控数据等</li></ul><br>
<br><h4>时间序列数据特点</h4><ul><li>性能好，关系型数据库对于大规模数据的处理性能糟糕。NoSQL可以比较好的处理大规模数据，但依然比不上时间序列数据库。</li><li>存储成本低，高效的压缩算法，节省存储空间，有效降低IO</li></ul><br>
<br>Prometheus有着非常高效的时间序列数据存储方法，每个采样数据仅仅占 用3.5byte左右空间，上百万条时间序列，30秒间隔，保留60天，大概花了 200多G（来自官方数据）。<br>
<h4>Prometheus的主要特征</h4><ul><li>多维度数据模型。</li><li>灵活的查询语言。</li><li>不依赖分布式存储，单个服务器节点是自主的。</li><li>通过基于HTTP的pull方式采集时序数据。</li><li>可以通过中间网关进行时序列数据推送。</li><li>通过服务发现或者静态配置来发现目标服务对象。</li><li>支持多种多样的图表和界面展示，比如Grafana等。</li></ul><br>
<br><h4>普罗米修斯原理架构图</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/894c57ade666b43a4ac89851d684d745.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/894c57ade666b43a4ac89851d684d745.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>实验环境准备</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/800a3334d5706495149e17e8b77cafff.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/800a3334d5706495149e17e8b77cafff.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
教程使用的软件：<br>
<br>下载链接：<a href="https://pan.baidu.com/s/1Y-BN3ZWaUCnlVO4woZYhOg" rel="nofollow" target="_blank">https://pan.baidu.com/s/1Y-BN3ZWaUCnlVO4woZYhOg</a>，提取码：h6wn<br>
<br>1、静态IP（要求能上外网）<br>
<br>2、主机名<br>
<pre class="prettyprint">各自配置好主机名 <br>
# hostnamectl set-hostname --static server.cluster.com <br>
三台都互相绑定IP与主机名 <br>
# vim /etc/hosts            <br>
192.168.116.129  master<br>
192.168.116.130  node1<br>
192.168.116.131  node2<br>
</pre><br>
<pre class="prettyprint">echo "192.168.116.129 master<br>
192.168.116.130 node1<br>
192.168.116.131 node2">>/etc/hosts<br>
</pre><br>
3、时间同步（时间同步一定要确认一下）<br>
<pre class="prettyprint">yum install -y  ntpdate && ntpdate time.windows.com<br>
</pre><br>
4、关闭防火墙，SELinux<br>
<pre class="prettyprint"># systemctl stop firewalld <br>
# systemctl disable firewalld <br>
# iptables -F<br>
</pre><br>
<h4>安装prometheus</h4>从<a href="https://prometheus.io/download/" rel="nofollow" target="_blank">https://prometheus.io/download/</a>下载相应版本，安装到服务器上。<br>
<br>官网提供的是二进制版，解压就能用，不需要编译。<br>
<br>上传prometheus-2.5.0.linux-amd64.tar.gz。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/9fe9defaca32f87651efd286b0ee9bd1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/9fe9defaca32f87651efd286b0ee9bd1.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<pre class="prettyprint">tar -zxvf prometheus-2.5.0.linux-amd64.tar.gz -C /usr/local/<br>
mv /usr/local/prometheus-2.5.0.linux-amd64/  /usr/local/prometheus<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/563e02abe201a899661dc57d1fb1fc44.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/563e02abe201a899661dc57d1fb1fc44.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
直接使用默认配置文件启动。<br>
<pre class="prettyprint">/usr/local/prometheus/prometheus --config.file="/usr/local/prometheus/prometheus.yml" &<br>
</pre><br>
确认端口（9090）。<br>
<pre class="prettyprint">ss -anltp | grep 9090<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/7e589dee1aa59b4c3039bbed8dd786b0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/7e589dee1aa59b4c3039bbed8dd786b0.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Prometheus界面</h4>通过浏览器访问http://服务器IP:9090就可以访问到Prometheus的主界面。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/f19ae997e771a3a70cd1d0ad4b533915.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/f19ae997e771a3a70cd1d0ad4b533915.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
默认只监控了本机一台，点Status --》点Targets --》可以看到只监控了本 机。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/c688b1008cbe980f112feccdcf0daa2d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/c688b1008cbe980f112feccdcf0daa2d.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>主机数据展示</h4>通过http://服务器IP:9090/metrics可以查看到监控的数据。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/f79bcade8b56d217d84dbb89215299dc.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/f79bcade8b56d217d84dbb89215299dc.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
在Web主界面可以通过关键字查询监控项。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/6b60ba13a11aab1574b161987a760fd6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/6b60ba13a11aab1574b161987a760fd6.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>监控远程Linux主机</h4>1、在远程Linux主机（被监控端agent1）上安装node_exporter组件。<br>
<br>下载地址：<a href="https://prometheus.io/download/" rel="nofollow" target="_blank">https://prometheus.io/download/</a><br>
<br>上传node_exporter-0.16.0.linux-amd64.tar.gz。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/d1d2be52337b17c06e883d5872ab59c6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/d1d2be52337b17c06e883d5872ab59c6.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<pre class="prettyprint">tar -zxvf node_exporter-0.16.0.linux-amd64.tar.gz -C /usr/local/<br>
mv /usr/local/node_exporter-0.16.0.linux-amd64/ /usr/local/node_exporter<br>
</pre><br>
里面就一个启动命令node_exporter，可以直接使用此命令启动。<br>
<pre class="prettyprint">nohup /usr/local/node_exporter/node_exporter & <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/b5e2334ed2236722a60012e4845ed004.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/b5e2334ed2236722a60012e4845ed004.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
确认端口（9100）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/7513bc998fec4635a09c2bf7bc3e3429.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/7513bc998fec4635a09c2bf7bc3e3429.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
扩展：nohup命令：如果把启动node_exporter的终端给关闭，那么进程也会随之关闭。nohup命令会帮你解决这个问题。<br>
<br>2、通过浏览器访问http://被监控端IP:9100/metrics就可以查看到 node_exporter在被监控端收集的监控信息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/2e1dad1313252d32beec98462b1511dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/2e1dad1313252d32beec98462b1511dc.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
3、回到Prometheus服务器的配置文件里添加被监控机器的配置段。<br>
<br>在主配置文件最后加上下面三行。<br>
<pre class="prettyprint">vim /usr/local/prometheus/prometheus.yml <br>
</pre><br>
<pre class="prettyprint">- job_name: 'node1'<br>
static_configs:<br>
- targets: ['192.168.116.130:9100'] <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/c69fcd59b92367541a5585679d56d960.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/c69fcd59b92367541a5585679d56d960.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<pre class="prettyprint">- job_name: 'agent1'                   # 取一个job名称来代表被监控的机器   <br>
static_configs:   <br>
- targets: ['10.1.1.14:9100']        # 这里改成被监控机器的IP，后面端口接9100<br>
</pre><br>
改完配置文件后，重启服务。<br>
<pre class="prettyprint">pkill prometheus <br>
</pre><br>
确认端口没有进程占用。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/ab4dd75e2ebf0ab9a423555eae19b5b5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/ab4dd75e2ebf0ab9a423555eae19b5b5.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<pre class="prettyprint">/usr/local/prometheus/prometheus --config.file="/usr/local/prometheus/prometheus.yml" &<br>
</pre><br>
确认端口被占用，说明重启成功。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/e9cd96a66aefb59f7fb07cfe74c74c03.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/e9cd96a66aefb59f7fb07cfe74c74c03.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
4、回到Web管理界面 --》点Status --》点Targets --》可以看到多了一台监 控目标。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/62ade599aede4942b2156ca399a2390b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/62ade599aede4942b2156ca399a2390b.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>原文链接：<a href="https://blog.csdn.net/heian_99/article/details/103952955" rel="nofollow" target="_blank">https://blog.csdn.net/heian_99 ... 52955</a>，作者：南宫乘风
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            