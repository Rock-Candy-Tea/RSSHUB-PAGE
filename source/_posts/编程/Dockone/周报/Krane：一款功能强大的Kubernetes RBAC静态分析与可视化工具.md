
---
title: 'Krane：一款功能强大的Kubernetes RBAC静态分析与可视化工具'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210808/d0f6ce8acfb6a1bab9517256c70fd35f.jpeg'
author: Dockone
comments: false
date: 2021-08-08 13:13:22
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210808/d0f6ce8acfb6a1bab9517256c70fd35f.jpeg'
---

<div>   
<br><h3>关于Krane</h3>Krane是一款功能强大的Kubernetes RBAC静态分析与可视化工具，该工具可以帮助广大研究人员分析Kubernetes RBAC设计中存在的安全隐患，并提供相应的安全防范措施及建议。Krane的仪表盘可以显示当前RBAC的安全态势，并允许我们查看其他相关详情。<br>
<h3>功能介绍</h3><ul><li>RBAC风险规则 - Krane可以评估一组内置的RBAC风险规则，并支持使用一组自定义规则修改或扩展这些规则。</li><li><br>便携性 - Krane能够以下列模式执行：<br>
<ul><li>命令行工具</li><li>Docker容器</li><li>CI/CD管道或单独服务</li></ul></li><li><br>报告 - Krane能够以机器可读的格式声称详细的RBAC风险评估报告。</li><li>仪表盘 - Krane提供了简单友好的仪表盘UI，帮助广大研究人员更好地了解目标Kubernetes RBAC的安全情况。</li><li>警报 - 如果检测到了中、高安全风险，Krane将会通过Slack向用户发出警报。</li><li>图形化RBAC - Krane可以将Kubernetes RBAC全部索引到一个本地图形数据库中，这使得RBAC数据的任何进一步的特殊查询都变得容易，支持使用任意CypherQL查询。</li></ul><br>
<br><h3>工具架构</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210808/d0f6ce8acfb6a1bab9517256c70fd35f.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210808/d0f6ce8acfb6a1bab9517256c70fd35f.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Krane本地运行</h3>Krane的功能依赖于RedisGraph，docker-compose栈定义了Krane服务本地构建和运行的所有依赖：<br>
<pre class="prettyprint">docker-compose up -d<br>
</pre><br>
注意，Krane的Docker镜像会自动进行预编译。<br>
<br>在本地运行docker-compose时，Krane不会自动开启RBAC报告和仪表盘，容器默认会休眠24小时，这个可以在docker-compose.override.yml中调整。<br>
<br>Krane执行：<br>
<pre class="prettyprint"># Exec into a running Krane container<br>
<br>
docker-compose exec krane bash<br>
<br>
# Once in the container you can start using `krane` commands. Try `krane -help`.<br>
<br>
$ krane -h<br>
</pre><br>
检查正在运行的服务以及相关端口：<br>
<pre class="prettyprint">docker-compose ps<br>
</pre><br>
停止Krane运行及其相关服务：<br>
<pre class="prettyprint">docker-compose down<br>
</pre><br>
<h3>Krane可用命令</h3><pre class="prettyprint">$ krane --help<br>
<br>
NAME:<br>
<br>
krane<br>
<br>
DESCRIPTION:<br>
<br>
Kubernetes RBAC static analysis & visualisation tool<br>
<br>
COMMANDS:<br>
<br>
dashboard Start K8s RBAC dashboard server<br>
help      Display global or [command] help documentation<br>
report    Run K8s RBAC report<br>
<br>
GLOBAL OPTIONS:<br>
<br>
-h, --help<br>
    Display help documentation<br>
<br>
-v, --version<br>
    Display version information<br>
<br>
-t, --trace<br>
    Display backtrace when an error occurs<br>
<br>
AUTHOR:<br>
<br>
Marcin Ciszak <marcin.ciszak@appvia.io> - Appvia Ltd <appvia.io><br>
</pre><br>
<h3>生成RBAC报告</h3>针对一个正在运行的集群，生成报告时需要提供一个kubectl上下文：<br>
<pre class="prettyprint">krane report -k <context><br>
</pre><br>
针对本地RBAC yaml/json文件运行，需要提供一个目录路径：<br>
<pre class="prettyprint">krane report -d </path/to/rbac-directory><br>
</pre><br>
针对一个正在Kubernetes集群中运行的容器生成报告：<br>
<pre class="prettyprint">krane report --incluster<br>
</pre><br>
<h3>可视化仪表盘</h3>查看RBAC数、网络图和最新的报告结果，首先需要启动仪表盘服务器：<br>
<pre class="prettyprint">krane dashboard<br>
</pre><br>
注意：本地Web服务器默认端口为8000，并且会显示仪表盘地址。<br>
<br>项目地址：<a href="https://github.com/appvia/krane" rel="nofollow" target="_blank">https://github.com/appvia/krane</a><br>
<br>原文链接：<a href="https://www.freebuf.com/articles/container/277697.html" rel="nofollow" target="_blank">https://www.freebuf.com/articl ... .html</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            