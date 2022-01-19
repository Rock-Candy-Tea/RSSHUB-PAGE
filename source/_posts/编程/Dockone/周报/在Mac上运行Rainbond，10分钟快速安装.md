
---
title: '在Mac上运行Rainbond，10分钟快速安装'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://static.goodrain.com/wechat/Mac/signal.png'
author: Dockone
comments: false
date: 2022-01-19 07:06:22
thumbnail: 'https://static.goodrain.com/wechat/Mac/signal.png'
---

<div>   
<br><h2>前言</h2>以往安装部署 <a href="https://www.rainbond.com/?channel=dockone">Rainbond</a> 的方式都无法绕过 Kubernetes 集群的搭建，无论是作为开发环境还是用于生产交付，部署的过程都非常依赖于服务器或云主机。这在体验 Rainbond 云原生应用管理平台的过程中设置了较高的门槛。然而对于个人开发者而言，准备一台服务器甚至多台服务器，才可以体验到这种企业级产品，是非常奢侈的。从今天开始，Rainbond 开辟了一条可以快速体验的道路，借助常见的个人 PC 平台（诸如 MacOS、Windows 等操作系统）上的 Docker Desktop ，以启动一个容器作为代价，提供一个全功能的 Rainbond 体验环境。这个部署过程被压缩到了 <strong>一条命令</strong> 运行，<strong>10分钟</strong>就可以体验到最新版本的 Rainbond。 接下来，将为大家介绍如何在个人 MAC 笔记本上安装使用Rainbond。<br>
<br>MAC目前共分为两种芯片，一种是intel芯片，另外一种就是苹果最新的M1芯片（ARM版本），Rainbond目前不仅仅支持intel芯片，对于新款的M1也提供了支持，这次适配在任何一台MAC上都可以轻松启动Rainbond，这一体验尤其适合个人开发者。通过这种途径安装 Rainbond ，会在短时间内得到一整套开箱即用的单机环境，免去繁琐安装集群的痛苦，对接集群的痛苦，让你在任何笔记本上，台式机上都可以随时随地，实现高效开发测试。<br>
<br><h2>安装Docker Desktop</h2>安装 Rainbond 之前，我们需要在个人 PC 上安装<a href="https://docs.docker.com/desktop/mac/release-notes/">Docker Desktop</a> ，它可以帮助我们在MAC上运行容器。Rainbond 的控制台会以容器的方式运行起来，而在控制台容器中，会以 Docker In Docker 的形式，运行起所有支撑 Rainbond 高级功能的组件。同时在控制台容器中内置 K3s 来提供容器的调度编排能力。<br>
<br><img src="https://static.goodrain.com/wechat/Mac/signal.png" alt referrerpolicy="no-referrer"><br>
<br>安装的 Docker Desktop 对于版本，和资源限额有一定要求：<br>
<br>| Docker Desktop版本 | MAC 内存 | MAC CPU |<br>
| ------------------ | -------- | ------- |<br>
| 4.2及以下          | 8G预留   | 2预留   |<br>
<br><h2>安装Rainbond</h2>>  启动之前需要定义 Rainbond 网关工作的 IP 地址，确保外界可以访问内部应用组件。IP地址在MAC上可以通过在终端执行 <code class="prettyprint">ifconfig</code> 命令获得，或者按住 <code class="prettyprint">Option</code> 键的同时点击右上角 WIFI 图标即可。但注意的一点就是，除非你确定这个集群中部署的业务不会对除本机之外的其他人提供服务，否则不要填写127.0.0.1。<br>
<br>打开 MAC 终端，后续的指令都会在命令行界面下执行<br>
<br>设置IP变量<br>
<pre class="prettyprint">export EIP=IP地址<br>
</pre><br>
<br>Intel版本启动命令（与M1二选一执行）：<br>
<pre class="prettyprint">docker run --privileged -d -p 7070:7070 -p 80:80 -p 443:443 -p 6060:6060 -p 8443:8443 \<br>
--name=rainbond-allinone --restart=unless-stopped \<br>
-v ~/.ssh:/root/.ssh \<br>
-v ~/opt/rainbond:/opt/rainbond \<br>
-e ENABLE_CLUSTER=true \<br>
-e EIP=$EIP \<br>
registry.cn-hangzhou.aliyuncs.com/goodrain/rainbond:v5.5.0-dind-allinone \<br>
&& docker logs -f rainbond-allinone<br>
</pre><br>
<br>M1版本启动命令（与Intel二选一执行）：<br>
<pre class="prettyprint">docker run --privileged -d -p 7070:7070 -p 80:80 -p 443:443 -p 6060:6060 -p 8443:8443 \<br>
--name=rainbond-allinone --restart=unless-stopped \<br>
-v ~/.ssh:/root/.ssh \<br>
-v ~/opt/rainbond:/opt/rainbond \<br>
-e ENABLE_CLUSTER=true \<br>
-e EIP=$EIP \<br>
registry.cn-hangzhou.aliyuncs.com/goodrain/rainbond:v5.5.0-dind-arm64-allinone \<br>
&& docker logs -f rainbond-allinone<br>
</pre><br>
<br>启动成功后的会看到以下提示：<br>
<pre class="prettyprint">正在加载数据，预计3分钟，时间取决于磁盘性能...<br>
正在启动Rainbond，预计5分钟...<br>
Rainbond启动成功，可以通过访问: http://$EIP:7070 进入Rainbond控制台<br>
</pre><br>
<br>切换进容器，查看集群状态<br>
<pre class="prettyprint">docker exec -ti rainbond-allinone bash<br>
root@e600f21466b6:~# kubectl get po -n rbd-system<br>
</pre><br>
<br>获得以下返回，说明 Rainbond 已经安装完成<br>
<pre class="prettyprint">NAME                                         READY   STATUS    RESTARTS       AGE<br>
rbd-etcd-0                                   1/1     Running   2 (4d4h ago)   6d2h<br>
rbd-gateway-4l2l7                            1/1     Running   2 (4d4h ago)   6d2h<br>
dashboard-metrics-scraper-7db45b8bb4-5lsfv   1/1     Running   2 (4d4h ago)   6d2h<br>
rbd-webcli-6d64c66cb7-4g8bh                  1/1     Running   2 (4d4h ago)   6d2h<br>
kubernetes-dashboard-fbd4fb949-d6wbx         1/1     Running   2 (4d4h ago)   6d2h<br>
rbd-mq-c95cf9857-x4m5b                       1/1     Running   2 (4d4h ago)   6d2h<br>
rainbond-operator-7d8649cd8b-cbllk           1/1     Running   3 (4d4h ago)   6d2h<br>
rbd-db-0                                     2/2     Running   4 (4d4h ago)   6d2h<br>
rbd-hub-64777d89d8-sjhgt                     1/1     Running   2 (4d4h ago)   6d2h<br>
rbd-node-8nfmj                               1/1     Running   2 (4d4h ago)   6d2h<br>
rbd-monitor-0                                1/1     Running   2 (4d4h ago)   6d2h<br>
rbd-eventlog-0                               1/1     Running   2 (4d4h ago)   6d2h<br>
rbd-worker-85d4f9696c-lkjn6                  1/1     Running   2 (4d4h ago)   6d2h<br>
rbd-resource-proxy-67879f484-tlq26           1/1     Running   4 (4d4h ago)   6d2h<br>
rbd-chaos-2m7nt                              1/1     Running   2 (4d4h ago)   6d2h<br>
rbd-api-dff6bc49d-ttxrg                      1/1     Running   2 (4d4h ago)   6d2h<br>
</pre><br>
<br><h2>快速熟悉Rainbond</h2>为了让大家能够快速熟悉<a href="https://www.rainbond.com/?channel=dockone">Rainbond</a>，安装成功后，默认会有示例应用：<br>
<br>点击 团队界面 -> admin团队 -> 默认应用，即可查看Ghost示例，示例初次启动大概2分钟左右，待变成绿色，即可访问，如下图：<br>
<br><img src="https://static.goodrain.com/wechat/Mac/ghost.png" alt referrerpolicy="no-referrer"><br>
<br><h2>写在最后</h2>本文简要介绍了一种在 MAC 电脑环境中快速体验 Rainbond 的方式，这种方式对个人开发者，或者缺乏足够服务器硬件支持的小企业、小团队非常友好。Rainbond 目前已经全面适配了 Arm64 架构的芯片，对于最终用户环境为 Arm64 架构的开发者而言，可以借助 Rainbond 有针对性的搭建开发环境。<br>
<br>接下来还有文章介绍如何在 Windows 环境中快速体验 Rainbond 的方式，敬请期待。
                                
                                                              
</div>
            