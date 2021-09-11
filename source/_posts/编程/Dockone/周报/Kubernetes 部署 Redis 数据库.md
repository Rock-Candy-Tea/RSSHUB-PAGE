
---
title: 'Kubernetes 部署 Redis 数据库'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=2200'
author: Dockone
comments: false
date: 2021-09-11 13:13:20
thumbnail: 'https://picsum.photos/400/300?random=2200'
---

<div>   
<br><h3>Redis 简介</h3>Redis 是我们常用的非关系型数据库，在项目开发、测试、部署到生成环境时，经常需要部署一套 Redis 来对数据进行缓存。这里介绍下如何在 Kubernetes 环境中部署用于开发、测试的环境的 Redis 数据库，当然，部署的是单节点模式，并非用于生产环境的主从、哨兵或集群模式。单节点的 Redis 部署简单，且配置存活探针，能保证快速检测 Redis 是否可用，当不可用时快速进行重启。<br>
<h4>Redis 参数配置</h4>在使用 Kubernetes 部署应用后，一般会习惯与将应用的配置文件外置，用 ConfigMap 存储，然后挂载进入镜像内部。这样，只要修改 ConfigMap 里面的配置，再重启应用就能很方便就能够使应用重新加载新的配置，很方便。<br>
<h3>部署 Redis</h3><h4>创建 ConfigMap 存储 Redis 配置文件</h4>redis-config.yaml<br>
<pre class="prettyprint">kind: ConfigMap<br>
apiVersion: v1<br>
metadata:<br>
name: redis-config<br>
namespace: zisefeizhu<br>
labels:<br>
app: redis<br>
data:<br>
redis.conf: |-<br>
dir /data<br>
port 6379<br>
bind 0.0.0.0<br>
appendonly yes<br>
protected-mode no<br>
requirepass zisefeizhu<br>
pidfile /data/redis-6379.pid<br>
</pre><br>
<h4>Redis 数据存储</h4>Kubernetes 部署的应用一般都是无状态应用，部署后下次重启很可能会漂移到不同节点上，所以不能使用节点上的本地存储，而是使用网络存储对应用数据持久化，PV 和 PVC 是 Kubernetes 用于与储空关联的资源，可与不同的存储驱动建立连接，存储应用数据，所以接下来我们要创建 Kubernetes PV、PVC 资源。<br>
<br>请参考：<a href="https://www.cnblogs.com/zisefeizhu/p/13564547.html" rel="nofollow" target="_blank">https://www.cnblogs.com/zisefeizhu/p/13564547.html</a><br>
<h4>创建 Deployment 部署 Redis</h4>创建用于 Kubernetes Deployment 来配置部署 Redis 的参数，需要配置 Redis 的镜像地址、名称、版本号，还要配置其 CPU 与 Memory 资源的占用，配置探针监测应用可用性，配置 Volume 挂载之前创建的 PV、PVC、ConfigMap 资源等等，内容如下： <br>
<br>redis-deployment.yaml<br>
<pre class="prettyprint">---<br>
apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: redis<br>
labels:<br>
app: redis<br>
spec:<br>
type: ClusterIP<br>
ports:<br>
- name: redis<br>
  port: 6379<br>
selector:<br>
app: redis<br>
---<br>
apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
name: redis<br>
namespace: production-pppharmapack<br>
labels:<br>
app: redis<br>
spec:<br>
replicas: 1<br>
selector:<br>
matchLabels:<br>
  app: redis<br>
template:<br>
metadata:<br>
  labels:<br>
    app: redis<br>
spec:<br>
  # 进行初始化操作，修改系统配置，解决 Redis 启动时提示的警告信息<br>
  initContainers:<br>
    - name: system-init<br>
      image: busybox:1.32<br>
      imagePullPolicy: IfNotPresent<br>
      command:<br>
        - "sh"<br>
        - "-c"<br>
        - "echo 2048 > /proc/sys/net/core/somaxconn && echo never > /sys/kernel/mm/transparent_hugepage/enabled"<br>
      securityContext:<br>
        privileged: true<br>
        runAsUser: 0<br>
      volumeMounts:<br>
      - name: sys<br>
        mountPath: /sys<br>
  containers:<br>
    - name: redis<br>
      image: redis:5.0.8<br>
      command:<br>
        - "sh"<br>
        - "-c"<br>
        - "redis-server /usr/local/etc/redis/redis.conf"<br>
      ports:<br>
        - containerPort: 6379<br>
      resources:<br>
        limits:<br>
          cpu: 1000m<br>
          memory: 1024Mi<br>
        requests:<br>
          cpu: 1000m<br>
          memory: 1024Mi<br>
      livenessProbe:<br>
        tcpSocket:<br>
          port: 6379<br>
        initialDelaySeconds: 300<br>
        timeoutSeconds: 1<br>
        periodSeconds: 10<br>
        successThreshold: 1<br>
        failureThreshold: 3<br>
      readinessProbe:<br>
        tcpSocket:<br>
          port: 6379<br>
        initialDelaySeconds: 5<br>
        timeoutSeconds: 1<br>
        periodSeconds: 10<br>
        successThreshold: 1<br>
        failureThreshold: 3<br>
      volumeMounts:<br>
        - name: data<br>
          mountPath: /data<br>
        - name: config<br>
          mountPath: /usr/local/etc/redis/redis.conf<br>
          subPath: redis.conf<br>
  volumes:<br>
    - name: data<br>
      persistentVolumeClaim:<br>
        claimName: zisefeizhu<br>
    - name: config<br>
      configMap:<br>
        name: redis-config<br>
    - name: sys<br>
      hostPath:<br>
        path: /sys<br>
</pre><br>
<h3>测试 Redis 是否可以正常使用</h3><pre class="prettyprint"># ctl get pod -n production-pppharmapack | grep redis<br>
redis-7768dc9c56-4kp8l                    1/1     Running   0          8m43s<br>
ctl exec -it  redis-7768dc9c56-4kp8l -n production-pppharmapack -- /bin/sh<br>
# redis-cli<br>
127.0.0.1:6379> auth zisefeizhu<br>
OK<br>
127.0.0.1:6379> config get requirepass<br>
1) "requirepass"<br>
2) "zisefeizhu"<br>
</pre><br>
过手如登山，一步一重天！<br>
<br>原文链接：<a href="https://www.cnblogs.com/zisefeizhu/p/14282299.html" rel="nofollow" target="_blank">https://www.cnblogs.com/zisefeizhu/p/14282299.html</a>
                                
                                                              
</div>
            