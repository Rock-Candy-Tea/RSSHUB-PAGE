
---
title: 'Kubernetes Pod探针健康检查和服务可用性检查'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=2788'
author: Dockone
comments: false
date: 2021-08-12 12:11:10
thumbnail: 'https://picsum.photos/400/300?random=2788'
---

<div>   
<br><h3>探针分为两类</h3>LivenessProbe探针：用于判断容器是否存活（running状态），如果探测到容器不健康，则kubelet将会杀掉该容器，然后根据重启策略进行重启。如果没有定义LivenessProbe探针，那么kubelet认为该容器永远正常。<br>
<br>ReadinessProbe探针：用于判断容器服务是否可用（Ready状态），达到Ready状态的Pod才会加入到Endpoint列表中，如果运行状态中Ready状态变为False，那么就会从Endpoint列表删除掉。<br>
<br>LivenessProbe和ReadinessProbe探针都可以配置以下三种方式：<br>
<ul><li>ExecAction：在容器内执行一个命令，如果该命令的返回码为0，则表明容器健康。</li><li>TCPSocketAction：通过容器的IP地址和端口号执行TCP检查，如果能够建立TCP连接，则表明容器健康。</li><li>HTTPGetAction：通过容器的IP地址、端口号及路径调用HTTPGet方法，如果响应码大于200且小于400，则认为容器健康。</li></ul><br>
<br>注意：initialDelaySeconds首次探测的时间很重要，时间过长（ExecAction案例）、过短（服务还没启动完成）都会导致容器一直重启无法提供服务，所以参数的值需要结合实际情况设置。<br>
<h3>案例</h3><h4>ExecAction案例</h4>在容器中执行cat/tmp/health命令来判断一个容器运行是否正常：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Pod<br>
metadata:<br>
labels:<br>
test: liveness<br>
name: liveness-exec<br>
spec:<br>
containers:<br>
- name: liveness<br>
image: gcr.io/google_containers/busybox<br>
args:<br>
- /bin/sh<br>
- -c<br>
- echo ok > /tmp/health; sleep 10; rm -rf /tmp/health; sleep 600    #Pod创建运行后，文件10s后删除导致首次健康检查的时候没有探测到，容器会被杀掉并重启，如此往复。<br>
livenessProbe:<br>
  exec:<br>
    command:<br>
    - cat<br>
    - /tmp/health<br>
  initialDelaySeconds: 15   #启动容器后进行首次健康检查的等待时间，单位为s。<br>
  timeoutSeconds: 1 #健康检查发送请求后等待响应的超时时间，单位为s。如果超时则kubelet会重启容器。<br>
</pre><br>
<h4>TCPSocketAction案例</h4>与容器内的localhost:80建立TCP连接进行监控检查：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Pod<br>
metadata:<br>
name: pod-with-healthcheck<br>
spec:<br>
containers:<br>
- name: nginx<br>
image: nginx<br>
ports:<br>
- containerPort: 80<br>
livenessProbe:<br>
  tcpSocket:<br>
    port: 80<br>
  initialDelaySeconds: 30   #启动容器后进行首次健康检查的等待时间，单位为s。<br>
  timeoutSeconds: 1 #健康检查发送请求后等待响应的超时时间，单位为s。如果超时则kubelet会重启容器。<br>
</pre><br>
<h4>HTTPGetAction案例</h4>kubelet定时发送HTTP请求到localhost:80/_status/healthz来进行容器应用的健康检查：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Pod<br>
metadata:<br>
name: pod-with-healthcheck<br>
spec:<br>
containers:<br>
- name: nginx<br>
image: nginx<br>
ports:<br>
- containerPort: 80<br>
livenessProbe:<br>
  httpGet:<br>
    path: /_status/healthz<br>
    port: 80<br>
  initialDelaySeconds: 30   #启动容器后进行首次健康检查的等待时间，单位为s。<br>
  timeoutSeconds: 1 #健康检查发送请求后等待响应的超时时间，单位为s。如果超时则kubelet会重启容器。<br>
</pre><br>
<br>原文链接：<a href="https://blog.csdn.net/qq_36165389/article/details/108262167" rel="nofollow" target="_blank">https://blog.csdn.net/qq_36165 ... 62167</a>
                                
                                                              
</div>
            