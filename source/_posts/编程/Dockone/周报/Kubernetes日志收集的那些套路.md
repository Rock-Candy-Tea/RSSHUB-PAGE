
---
title: 'Kubernetes日志收集的那些套路'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210404/4d6dd6f083fbabaf5fbdb9b797ce7c02.jpeg'
author: Dockone
comments: false
date: 2021-04-06 00:27:01
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210404/4d6dd6f083fbabaf5fbdb9b797ce7c02.jpeg'
---

<div>   
<br><h3>准备</h3><h4>关于容器日志</h4>Docker的日志分为两类，一类是Docker引擎日志；另一类是容器日志。引擎日志一般都交给了系统日志，不同的操作系统会放在不同的位置。本文主要介绍容器日志，容器日志可以理解是运行在容器内部的应用输出的日志，默认情况下，docker logs显示当前运行的容器的日志信息，内容包含 STOUT（标准输出）和STDERR（标准错误输出）。日志都会以json-file的格式存储于 <strong>/var/lib/docker/containers/<容器id>/<容器id>-json.log</strong>，不过这种方式并不适合放到生产环境中。<br>
<ul><li>默认方式下容器日志并不会限制日志文件的大小，容器会一直写日志，导致磁盘爆满，影响系统应用。（docker log-driver支持log文件的rotate）</li><li>Docker Daemon收集容器的标准输出，当日志量过大时会导致Docker Daemon成为日志收集的瓶颈，日志的收集速度受限。</li><li>日志文件量过大时，利用docker logs -f查看时会直接将Docker Daemon阻塞住，造成docker ps等命令也不响应。</li></ul><br>
<br>Docker提供了logging drivers配置，用户可以根据自己的需求去配置不同的log-driver，可参考官网<a href="https://docs.docker.com/v17.09/engine/admin/logging/overview/">Configure logging drivers</a>。但是上述配置的日志收集也是通过Docker Daemon收集，收集日志的速度依然是瓶颈。<br>
<br><blockquote><br>log-driver 日志收集速度<br><br>
  syslog 14.9 MB/s<br><br>
  json-file 37.9 MB/s</blockquote>能不能找到不通过Docker Daemon收集日志直接将日志内容重定向到文件并自动rotate的工具呢？答案是肯定的采用<a href="http://skarnet.org/software/s6/">S6</a>基底镜像。<br>
<br>S6-log将CMD的标准输出重定向到/.../default/current，而不是发送到 Docker Daemon，这样就避免了Docker Daemon收集日志的性能瓶颈。本文就是采用<a href="http://skarnet.org/software/s6/">S6</a>基底镜像构建应用镜像形成统一日志收集方案。<br>
<h4>关于Kubernetes日志</h4>Kubernetes日志收集方案分成三个级别：<br>
<br><strong>应用（Pod）级别</strong><br>
<br>Pod级别的日志，默认是输出到标准输出和标志输入，实际上跟Docker容器的一致。使用kubectl logs pod-name -n namespace查看，具体参考：<a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs" rel="nofollow" target="_blank">https://kubernetes.io/docs/ref ... 3logs</a>。<br>
<br><strong>节点级别</strong><br>
<br>Node级别的日志 , 通过配置容器的<a href="https://docs.docker.com/config/containers/logging/configure/">log-driver</a>来进行管理，这种需要配合<a href="https://linux.die.net/man/8/logrotate">logrotare</a>来进行，日志超过最大限制，自动进行rotate操作。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210404/4d6dd6f083fbabaf5fbdb9b797ce7c02.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210404/4d6dd6f083fbabaf5fbdb9b797ce7c02.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>集群级别</strong><br>
<br>集群级别的日志收集，有三种。<br>
<br><strong>节点代理</strong>方式，在Node级别进行日志收集。一般使用DaemonSet部署在每个Node中。这种方式优点是耗费资源少，因为只需部署在节点，且对应用无侵入。缺点是只适合容器内应用日志必须都是标准输出。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210404/58bec065779ff06c99b5630b3067bdb1.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210404/58bec065779ff06c99b5630b3067bdb1.jpeg" class="img-polaroid" title="2.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
使用<strong>sidecar container</strong>作为容器日志代理，也就是在Pod中跟随应用容器起一个日志处理容器，有两种形式：<br>
<br>一种是直接将应用容器的日志收集并输出到标准输出（叫做<strong>Streaming sidecar container</strong>），但需要注意的是，这时候，宿主机上实际上会存在两份相同的日志文件：一份是应用自己写入的；另一份则是sidecar的stdout和stderr对应的JSON文件。这对磁盘是很大的浪费，所以说，除非万不得已或者应用容器完全不可能被修改。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210404/d9c7e9ae68c6cf8eabcb09ff30b76d29.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210404/d9c7e9ae68c6cf8eabcb09ff30b76d29.jpeg" class="img-polaroid" title="3.jpeg" alt="3.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
另一种是每一个Pod中都起一个<strong>日志收集agent</strong>（比如Logstash或Fluebtd）也就是相当于把方案一里的logging agent放在了Pod里。但是这种方案资源消耗（CPU，内存）较大，并且日志不会输出到标准输出，kubectl logs会看不到日志内容。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210404/66feb1dfb67d9361a240a89d7aec73c5.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210404/66feb1dfb67d9361a240a89d7aec73c5.jpeg" class="img-polaroid" title="4.jpeg" alt="4.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>应用容器中直接将日志推到存储后端</strong>，这种方式就比较简单了，直接在应用里面将日志内容发送到日志收集服务后端。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210404/e4161b9e79a36c7aec3489075e7de99d.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210404/e4161b9e79a36c7aec3489075e7de99d.jpeg" class="img-polaroid" title="5.jpeg" alt="5.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>日志架构</h3>通过上文对Kubernetes日志收集方案的介绍，要想设计一个统一的日志收集系统，可以采用<strong>节点代理</strong>方式收集每个节点上容器的日志，日志的整体架构如图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210404/7ac9528de2f5c75d0df35ef8fad8236e.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210404/7ac9528de2f5c75d0df35ef8fad8236e.jpeg" class="img-polaroid" title="6.jpeg" alt="6.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
解释如下：<br>
<ol><li>所有应用容器都是基于S6基底镜像的，容器应用日志都会重定向到宿主机的某个目录文件下比如/data/logs/namespace/appname/podname/log/xxxx.log</li><li>log-agent内部包含<a href="https://github.com/elastic/beats/tree/master/filebeat">Filebeat</a>，Logrotate等工具，其中Filebeat是作为日志文件收集的agent</li><li>通过Filebeat将收集的日志发送到Kafka</li><li>Kafka在讲日志发送的ES日志存储/kibana检索层</li><li>Logstash作为中间工具主要用来在ES中创建index和消费Kafka的消息</li></ol><br>
<br>整个流程很好理解，但是需要解决的是：<br>
<ol><li>用户部署的新应用，如何动态更新Filebeat配置</li><li>如何保证每个日志文件都被正常的rotate</li><li>如果需要更多的功能则需要二次开发Filebeat，使Filebeat支持更多的自定义配置</li></ol><br>
<br><h3>付诸实践</h3><strong>解决上述问题，就需要开发一个log-agent应用以DaemonSet形式运行在Kubernetes集群的每个节点上，应用内部包含Filebeat，Logrotate和需要开发的功能组件。</strong><br>
<br>第一个问题，如何动态更新Filebeat配置，可以利用<a href="http://github.com/fsnotify/fsnotify" rel="nofollow" target="_blank">http://github.com/fsnotify/fsnotify</a>工具包监听日志目录变化create、delete事件，利用模板渲染的方法更新Filebeat配置文件。<br>
<br>第二个问题，利用<a href="http://github.com/robfig/cron" rel="nofollow" target="_blank">http://github.com/robfig/cron</a>工具包创建CronJob，定期rotate日志文件，注意应用日志文件所属用户，如果不是root用户所属，可以在配置中设置切换用户。<br>
<pre class="prettyprint">/var/log/xxxx/xxxxx.log &#123;<br>
  su www-data www-data<br>
  missingok<br>
  notifempty<br>
  size 1G<br>
  copytruncate<br>
&#125; <br>
</pre><br>
第三个问题，关于二次开发filebeat，可以参考博文：<a href="https://www.jianshu.com/p/fe3ac68f4a7a" rel="nofollow" target="_blank">https://www.jianshu.com/p/fe3ac68f4a7a</a><br>
<h3>总结</h3>本文只是对Kubernetes日志收集提供了一个简单的思路，关于日志收集可以根据公司的需求，因地制宜。<br>
<br>参考文献：<br>
<ul><li><a href="https://kubernetes.io/docs/concepts/cluster-administration/logging/" rel="nofollow" target="_blank">https://kubernetes.io/docs/con ... ging/</a></li><li><a href="https://support.rackspace.com/how-to/understanding-logrotate-utility/" rel="nofollow" target="_blank">https://support.rackspace.com/ ... lity/</a></li><li><a href="https://github.com/elastic/beats/tree/master/filebeat" rel="nofollow" target="_blank">https://github.com/elastic/bea ... ebeat</a></li><li><a href="http://skarnet.org/software/s6/" rel="nofollow" target="_blank">http://skarnet.org/software/s6/</a></li></ul><br>
<br>原文链接：<a href="https://zhuanlan.zhihu.com/p/70662744" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/70662744</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            