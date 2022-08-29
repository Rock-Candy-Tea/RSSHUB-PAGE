
---
title: 'SREWorks v1.2 版本发布 _ 运维市场能力发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://intranetproxy.alipay.com/skylark/lark/0/2022/jpeg/2748/1655376291778-6df6b01c-32f4-460d-a5d7-83e46ffadf15.jpeg'
author: 开源中国
comments: false
date: Mon, 29 Aug 2022 02:58:00 GMT
thumbnail: 'https://intranetproxy.alipay.com/skylark/lark/0/2022/jpeg/2748/1655376291778-6df6b01c-32f4-460d-a5d7-83e46ffadf15.jpeg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">在v1.1版本发布之后，SREWorks团队开始了常态化的功能版本迭代，v1.1提供了组件插拔能力，v1.2更进一步，将会发布规划已久的<strong>运维市场</strong>，助力团队构筑运维生态，也会发布诸多企业用户关注的<strong>纯内网源码构建</strong>方案。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">切入正题，下面是本次 v1.2 版本的<strong>新功能解读</strong>。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">1. 应用市场</h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">SREWorks团队参考helm/rpm等常见软件仓库模型，设计了SREWorks的市场分发机制如下图所示:</p> 
<p style="color:#24292e; margin-left:0px; margin-right:0px; text-align:center"><img alt src="https://intranetproxy.alipay.com/skylark/lark/0/2022/jpeg/2748/1655376291778-6df6b01c-32f4-460d-a5d7-83e46ffadf15.jpeg" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">该市场分发机制具有如下特点:</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="list-style-type:disc !important">公共市场理论上可以基于任何<strong>静态存储服务</strong>搭建，并且可以支持<strong>缓存加速</strong>，当前支持阿里云OSS，后续会支持 MinIO/S3 等常见存储服务。</li> 
 <li style="list-style-type:disc !important">支持多个SREWorks平台向同一个市场发布包，也支持一个SREWorks平台同时订阅多个市场。</li> 
</ul> 
<p style="color:#24292e; margin-left:0px; margin-right:0px; text-align:center"><img alt src="https://intranetproxy.alipay.com/skylark/lark/0/2022/png/2748/1655644911998-adaa3879-3815-44bf-97bc-c0e04dd1ebbe.png" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">SREWorks团队欢迎用户在应用市场之上构建自己公司内部的<strong>私有市场</strong>，后续也会在公共市场上线更多的运维应用，方便用户<strong>开箱即用</strong>享受更多的功能和特性。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">2. 纯内网源码构建部署</h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">本次版本迭代，SREWorks团队将源码构建依赖资源进行了整理和分类，用户可自行选择或替换对应的资源，进行内网或特殊环境的源码构建部署。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">底座源码构建</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">在执行<span> </span><code><span class="ne-text">./build.sh</span</code><span> </span>命令前可传入下列的环境变量来改变资源地址，如不传入则使用默认值</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><em># 容器镜像</em>
<span style="color:#0086b3">export</span> SW_<span class=<span style="color:#dd1144">"k_pendant"</span> data-id=<span style="color:#dd1144">"6"</span>>Python</span>3_IMAGE=<span style="color:#dd1144">"python:3.9.12-alpine"</span>
<span style="color:#0086b3">export</span> MIGRATE_IMAGE=<span style="color:#dd1144">"migrate/migrate"</span>
<span style="color:#0086b3">export</span> MAVEN_IMAGE=<span style="color:#dd1144">"maven:3.8.3-adoptopenjdk-11"</span>
<span style="color:#0086b3">export</span> GOLANG_IMAGE=<span style="color:#dd1144">"golang:alpine"</span>
<span style="color:#0086b3">export</span> GOLANG_BUILD_IMAGE=<span style="color:#dd1144">"golang:1.16"</span>
<span style="color:#0086b3">export</span> DISTROLESS_IMAGE=<span style="color:#dd1144">"sreworks-registry.cn-beijing.cr.aliyuncs.com/mirror/distroless-static:nonroot"</span>

<em># 软件仓库</em>
<span style="color:#0086b3">export</span> APK_REPO_DOMAIN=<span style="color:#dd1144">"mirrors.tuna.tsinghua.edu.cn"</span>
<span style="color:#0086b3">export</span> PYTHON_PIP=<span style="color:#dd1144">"http://mirrors.aliyun.com/pypi/simple"</span>
<span style="color:#0086b3">export</span> GOPROXY=<span style="color:#dd1144">"https://goproxy.cn"</span>
<span style="color:#0086b3">export</span> MAVEN_SETTINGS_XML=<span style="color:#dd1144">"https://sreworks.oss-cn-beijing.aliyuncs.com/resource/settings.xml"</span>

<em># 二进制命令</em>
<span style="color:#0086b3">export</span> HELM_BIN_URL=<span style="color:#dd1144">"https://abm-storage.oss-cn-zhangjiakou.aliyuncs.com/lib/helm"</span>
<span style="color:#0086b3">export</span> KUSTOMIZE_BIN_URL=<span style="color:#dd1144">"https://abm-storage.oss-cn-zhangjiakou.aliyuncs.com/lib/kustomize"</span>
<span style="color:#0086b3">export</span> MINIO_CLIENT_URL=<span style="color:#dd1144">"https://sreworks.oss-cn-beijing.aliyuncs.com/bin/mc-linux-amd64"</span>

<em># SREWorks内置应用包</em>
<span style="color:#0086b3">export</span> SREWORKS_BUILTIN_PACKAGE_URL=<span style="color:#dd1144">"https://sreworks.oss-cn-beijing.aliyuncs.com/packages"</span>

...
</code></pre> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">完整资源清单请访问<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fsreworks-doc%2Fdocs%2Fmzz07m" target="_blank">https://www.yuque.com/sreworks-doc/docs/mzz07m</a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">运维应用源码构建</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">在执行helm install/upgrade 命令的时候，可以选择性传入以下参数，使得运维应用可以在内网进行构建及部署。</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><strong style="color:#999999"># 容器镜像</strong>
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.mavenImage=<span style="color:#dd1144">"sreworks-registry.cn-beijing.cr.aliyuncs.com/mirror/maven:3.8.3-adoptopenjdk-11"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.openjdk8Image=<span style="color:#dd1144">"sreworks-registry.cn-beijing.cr.aliyuncs.com/mirror/openjdk8:alpine-jre"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.openjdk11Image=<span style="color:#dd1144">"sreworks-registry.cn-beijing.cr.aliyuncs.com/mirror/openjdk:11.0.10-jre"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.openjdk11AlpineImage=<span style="color:#dd1144">"sreworks-registry.cn-beijing.cr.aliyuncs.com/mirror/openjdk11:alpine-jre"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.alpineImage=<span style="color:#dd1144">"sreworks-registry.cn-beijing.cr.aliyuncs.com/mirror/alpine:latest"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.nodeImage=<span style="color:#dd1144">"sreworks-registry.cn-beijing.cr.aliyuncs.com/mirror/node:10-alpine"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.migrateImage=<span style="color:#dd1144">"sw-migrate"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.postrunImage=<span style="color:#dd1144">"sw-postrun"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.python3Image=<span style="color:#dd1144">"sreworks-registry.cn-beijing.cr.aliyuncs.com/mirror/python:3.9.12-alpine"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.bentomlImage=<span style="color:#dd1144">"sreworks-registry.cn-beijing.cr.aliyuncs.com/mirror/bentoml-model-server:0.13.1-py37"</span> \

<strong style="color:#999999"># 软件仓库</strong>
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.apkRepoDomain=<span style="color:#dd1144">"mirrors.tuna.tsinghua.edu.cn"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.mavenSettingsXml=<span style="color:#dd1144">"https://sreworks.oss-cn-beijing.aliyuncs.com/resource/settings.xml"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.npmRegistryUrl=<span style="color:#dd1144">"https://registry.npmmirror.com"</span> \
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.pythonPip=<span style="color:#dd1144">"http://mirrors.aliyun.com/pypi/simple"</span> \

<strong style="color:#999999"># 二进制命令</strong>
--<strong style="color:#333333">set</strong> <strong style="color:#333333">global</strong>.artifacts.minioClientUrl=<span style="color:#dd1144">"https://sreworks.oss-cn-beijing.aliyuncs.com/bin/mc-linux-amd64"</span> \

...
</code></pre> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">完整资源清单请访问<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fsreworks-doc%2Fdocs%2Fmzz07m" target="_blank">https://www.yuque.com/sreworks-doc/docs/mzz07m</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">3. 数据平台能力增强</h2> 
<h4 style="margin-left:0; margin-right:0; text-align:start">指标采集能力增强</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">纳管集群通过<strong>metricbeat</strong>支持采集prometheus exporter能力，默认Pod(exporter)标签满足 sreworks-prometheus-scrape-metric: enable 和 sreworks-prometheus-io-scrape: enable 具备服务自动发现能力。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">前序版本默认仅支持针对Service标签满足<span> </span><code><span class="ne-text">sreworks-telemetry-metric: enable</span</code>**<span> </span><strong>具备服务自动发现和指标接口定时pull能力，考虑到</strong>Prometheus**已经成为云原生领域监控的事实标准，因此在v1.2版本中增强指标采集能力，即支持从用户服务中主动pull指标数据，也支持主动从prometheus exporter pull指标数据。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">数据消费能力增强</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">新增<strong>logstash</strong>数据服务组件，支持对运维数据多管道分发。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">前序版本默认数据落地到Elasticsearch存储，对数据加工处理主要依赖作业平台的数据处理任务，但作业平台对时序数据处理的时效性较弱。v1.2版本支持采集的用户运维数据（主要指Metric数据）主动流入消息队列服务Kafka，用户可通过VVP平台对时序数据进行<strong>自定义加工处理</strong>。</p> 
<p style="color:#24292e; margin-left:0px; margin-right:0px; text-align:center"><img alt src="https://intranetproxy.alipay.com/skylark/lark/0/2022/png/227744/1655295130365-a69cab01-d0bf-460a-86dd-26c061e3d0ed.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">4. 其他优化</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="list-style-type:disc !important">优化应用卸载时service未回收的问题</li> 
 <li style="list-style-type:disc !important">优化代码依赖，去除工程中对python2.7的依赖</li> 
 <li style="list-style-type:disc !important">运维应用部署时支持命名空间(namespace)自定义</li> 
 <li style="list-style-type:disc !important">站点搜索服务支持实例详情页索引</li> 
 <li style="list-style-type:disc !important">前端组件文档补齐</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">如何从当前版本升级到v1.2</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="list-style-type:disc !important">升级包含底座，页面可能会有5-10分钟的不可访问，请注意。</li> 
 <li style="list-style-type:disc !important">用户自行开发的云原生应用不会受影响(不重启)，SREWorks网关到应用的流量会有中断。</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>git <span style="color:#0086b3">clone</span> http://github.com/alibaba/sreworks.git -b v1.2 sreworks

<span style="color:#0086b3">cd</span> sreworks
./sbin/upgrade-cluster.sh --kubeconfig=<span style="color:#dd1144">"****"</span>
</code></pre> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">如在使用过程中遇到问题，欢迎各位在GitHub中提出Issues或Pull requests。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">SREWorks开源地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fsreworks" target="_blank">https://github.com/alibaba/sreworks</a></p>
                                        </div>
                                      
</div>
            