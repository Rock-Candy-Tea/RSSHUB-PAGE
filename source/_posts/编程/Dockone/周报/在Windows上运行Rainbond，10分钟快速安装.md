
---
title: '在Windows上运行Rainbond，10分钟快速安装'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://static.goodrain.com/wechat/Mac/signal.png'
author: Dockone
comments: false
date: 2022-01-14 13:18:26
thumbnail: 'https://static.goodrain.com/wechat/Mac/signal.png'
---

<div>   
<br><h2>前言</h2>Windows 桌面运行 <a href="https://www.rainbond.com/?channel=dockone">Rainbond</a>，Windows 开发者的新选择。<br>
<br>经过适配Mac以后，Windows的适配也是成为了近期的小目标，经过不断地测试，不断地研究。最后也是达成了完美运行的效果，实现了真正意义上的任何场景，多种架构的完美适配，让手里的电脑真正称的上是生产力工具。<br>
<br>借助 Docker Desktop for win，可以快速的在 Windows 运行 Rainbond 开发测试环境， 接下来为大家介绍如何在 Windows 桌面上安装使用Rainbond。<br>
<br><h2>安装Docker Desktop</h2>Docker Desktop 是一款适用于Mac 或Windows 环境的易于安装的应用程序，使您能够在几分钟内开始编码和容器化。可以帮助我们在Windows上运行容器。Rainbond 的控制台会以容器的方式运行起来，而在控制台容器中，会以 Docker In Docker 的形式，运行起所有支撑 Rainbond 高级功能的组件。同时在控制台容器中内置 K3s 来提供容器的调度编排能力：<br>
<br><img src="https://static.goodrain.com/wechat/Mac/signal.png" alt referrerpolicy="no-referrer"><br>
<br>Windows Docker Desktop 资源限额：<br>
<br>| Docker Desktop版本 | Windows  内存 | Windows CPU |<br>
| ------------------ | ------------- | ----------- |<br>
| 4.2及以下          | 8G            | 2           |<br>
<br><h2>安装Rainbond</h2>> 启动之前需要定义 Rainbond 网关工作的 IP 地址，确保外界可以访问内部应用组件，IP地址为必填项，可以通过<code class="prettyprint">ipconfig</code>命令，或者点击右下角网络图标>查看其属性获得IP地址，但注意的一点就是，除非你确定这个集群中部署的业务不会对除本机之外的其他人提供服务，否则不要填写127.0.0.1。<br>
><br>
<blockquote><br>-e EIP=IP地址 为必填项</blockquote>打开 Windows终端(CMD)，后续的指令都会在命令行界面下执行<br>
<br>Windows 启动命令：<br>
<pre class="prettyprint">docker run --privileged -d  -p 7070:7070 -p 80:80 -p 443:443 -p 6060:6060 -p 8443:8443 ^<br>
--name=rainbond-allinone --restart=unless-stopped ^<br>
-v ~/.ssh:/root/.ssh ^<br>
-v ~/rainbonddata:/app/data ^<br>
-v ~/opt/rainbond:/opt/rainbond ^<br>
-e ENABLE_CLUSTER=true ^<br>
-e EIP=IP地址 ^<br>
registry.cn-hangzhou.aliyuncs.com/goodrain/rainbond:v5.5.0-dind-allinone ^<br>
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
<br><h2>写在最后</h2>本文简要介绍了一种在 Windows 电脑环境中快速体验 Rainbond 的方式，这种方式对个人开发者，或者缺乏足够服务器硬件支持的小企业、小团队非常友好。Rainbond 目前已经全面适配了 x86，对于最终用户环境为 x86架构的开发者而言，可以借助 Rainbond 有针对性的搭建开发环境。<br>
<br>对于在Mac环境下的安装适配，可以参考上文。
                                
                                                              
</div>
            