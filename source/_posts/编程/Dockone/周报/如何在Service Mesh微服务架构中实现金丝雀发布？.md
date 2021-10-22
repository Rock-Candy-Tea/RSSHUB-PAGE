
---
title: '如何在Service Mesh微服务架构中实现金丝雀发布？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211015/347ba8318e96fc619db0cc7bd3e21dda.png'
author: Dockone
comments: false
date: 2021-10-22 10:08:31
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211015/347ba8318e96fc619db0cc7bd3e21dda.png'
---

<div>   
<br>今天的文章聊聊有关Service Mesh微服务架构的话题，如果对之前的聊过的话题还不了解，可以参考文末的推荐阅读。本文主要讲的话题是：<strong>如何在Service Mesh微服务架构中实现“金丝雀发布”？</strong><br>
<h3>什么是金丝雀发布</h3>既然要聊具体的实现，那么在开始之前，先科普下什么是“金丝雀发布”。金丝雀发布也叫“<strong>灰度发布</strong>”，具体来说就是在发布线上版本时，先将少量的生产流量打到服务的新版本，以验证新版本的准确性和可靠性，待发布的新版本得到线上流量的全面验证后，在逐步将所有流量放入新版本，以实现生产服务版本的稳定更新。  <br>
<br><blockquote><br>为什么叫金丝雀发布呢，是因为金丝雀对矿场中的毒气比较敏感，所以在矿场开工前工人们会放一只金丝雀进去，以验证矿场是否存在毒气，这便是金丝雀发布名称的由来。</blockquote>在不同技术栈场景中，金丝雀发布的实现方式也不尽相同：有通过nginx实现的、也有借助<strong>A/B测试</strong>实现的。而随着以Kubernetes为代表的云原生基础设施的普及，金丝雀发布作为一项基本的服务发布功能，其实现方式也有了一些新的趋势——<strong>那就是逐步与云原生基础设施融为一体，成为基础设施服务的一部分</strong>。<br><br>
<h3>Kubernetes中的金丝雀（灰度）发布</h3>接下来，先看看在Kubernetes中是如何实现版本更新的。以下内容假设你已经有了一套可用的Kubernetes环境，如果没有可以查看文末推荐阅读的文章链接，参考相关分享自行部署。<br>
<h4>滚动更新</h4>在介绍Kubernetes中的金丝雀（灰度）发布之前，先来了解下Kubernetes中最重要的应用部署方式——“滚动升级”。  <br>
<br>所谓“<strong>滚动升级</strong>”：是指当更新了Kubernetes中Deployment编排资源的Pod模版（例如更新镜像版本号）之后，Deployment就需要遵循一种叫做“滚动更新（rolling update）”的方式，来升级现有的容器，从而实现应用对外服务的“不中断更新部署”。Kubernetes实现“滚动升级”的示意图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211015/347ba8318e96fc619db0cc7bd3e21dda.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211015/347ba8318e96fc619db0cc7bd3e21dda.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如上图所示，滚动升级的过程为：<br><br>
<ol><li>当容器开始升级时，集群中会先启动一个新版本的Pod，并终止一个旧版本的Pod。</li><li>如果此时，新版本的Pod有问题启动不了，那么“滚动升级”就会停止，并允许开发和运维人员介入。而在这个过程中，由于应用本身还有两个旧版本的Pod在线，所以服务并不会受到太大的影响。  </li><li>而如果新版本的Pod启动成功，且服务访问正常，则继续滚动升级，直至按照Deployment编排器设置的副本数量，完成后续旧版本Pod的升级。</li></ol><br>
<br>在Kubernetes中Deployment还可以通过相应地“滚动升级”策略，来控制Pod的滚动升级行为，以进一步保证服务的连续性。例如：“<strong>在任何时间窗口内，只有指定比例的Pod处于离线状态；在任何时间窗口内，只有指定比例的新Pod被创建出来</strong>”。可以通过相应地控制参数进行设置，如下：<br>
<pre class="prettyprint">...<br>
spec:<br>
selector:<br>
matchLabels:<br>
  app: micro-api<br>
replicas: 3<br>
#设置滚动升级策略<br>
#Kubernetes在等待设置的时间后才开始进行升级，例如5秒<br>
minReadySeconds: 5<br>
strategy:<br>
type: RollingUpdate<br>
rollingUpdate:<br>
  #升级过程中最多可以比原先设置多出的Pod数量<br>
  maxSurge: 1<br>
  #升级过程中Deployment控制器最多可以删除多少个旧Pod，主要用于提供缓冲时间<br>
  maxUnavailable: 1<br>
...<br>
</pre><br>
在上面RollingUpdate Strategy（滚动升级策略）的配置中：<br>
<ul><li>maxSurge：指定的是，除了设定的Pod副本数量之外，在一次“滚动”中，Deployment控制器还可以创建多少个新的Pod。</li><li>maxUnavailable：指的是，在一次“滚动”中，Deployment控制器可以删除多少个旧Pod。</li></ul><br>
<br><blockquote><br>通过这种精确的“滚动升级”策略，可以使得Kubernetes服务版本发布的过程更加平滑。此外，这两个配置还可以通过百分比的方式来表示，比如“<strong>maxUnavailable=50%</strong>”，指的是Deployment控制器最多可以一次删除“50%*设定Pod副本数”个Pod。</blockquote>接下来具体演示下在Kubernetes中进行服务滚动升级的详细过程。<br>
<br>该项目以Spring Boot编写的Java服务为主，在体验上更接近真实的项目开发场景。项目的结构如下：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211015/a8e6778f05168b080e68d230c2a449d7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211015/a8e6778f05168b080e68d230c2a449d7.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
该项目所在的GitHub地址为：<a href="https://github.com/manongwudi/istio-micro-service-demo" rel="nofollow" target="_blank">https://github.com/manongwudi/ ... -demo</a><br>
<br>“滚动升级”演示：<br>
<br>这里先借助示例项目中的“micro-api”服务来演示其在Kubernetes中进行“滚动升级”的过程，步骤如下：  <br>
<br>1、首先准备“micro-api”服务的k8s发布文件（如：micro-api.yaml）。代码如下：<br><br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: micro-api<br>
spec:<br>
type: ClusterIP<br>
ports:<br>
- name: http<br>
  port: 19090<br>
  targetPort: 9090<br>
selector:<br>
app: micro-api<br>
<br>
---<br>
apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
name: micro-api<br>
spec:<br>
selector:<br>
matchLabels:<br>
  app: micro-api<br>
replicas: 3<br>
#设置滚动升级策略<br>
#Kubernetes在等待设置的时间后才开始进行升级，例如5秒<br>
minReadySeconds: 5<br>
strategy:<br>
type: RollingUpdate<br>
rollingUpdate:<br>
  #升级过程中最多可以比原先设置多出的Pod数量<br>
  maxSurge: 1<br>
  #升级过程中Deployment控制器最多可以删除多少个旧Pod<br>
  maxUnavailable: 1<br>
template:<br>
metadata:<br>
  labels:<br>
    app: micro-api<br>
spec:<br>
  #设置的阿里云私有镜像仓库登陆信息的secret（对应2.1.2的设置）<br>
  imagePullSecrets:<br>
    - name: regcred<br>
  containers:<br>
    - name: micro-api<br>
      image: registry.cn-hangzhou.aliyuncs.com/wudimanong/micro-api:1.0-SNAPSHOT<br>
      imagePullPolicy: Always<br>
      tty: true<br>
      ports:<br>
        - name: http<br>
          protocol: TCP<br>
          containerPort: 19090<br>
</pre><br>
上述部署文件设置了“micro-api”服务的Pod副本个数为“3”，并且设置了相应地滚动升级策略。  <br>
<br>2、接下来执行Kubernetes部署命令，如下：<br><br>
<pre class="prettyprint">$ kubectl apply -f micro-api.yaml<br>
</pre><br>
成功后，查看Deployment创建后的状态信息，命令效果如下：<br>
<pre class="prettyprint">$ kubectl get deployments<br>
NAME          READY   UP-TO-DATE   AVAILABLE   AGE<br>
micro-api     3/3     3            3           190d<br>
</pre><br>
从上述命令的返回结果中，可以看到三个状态字段，它们的含义如下所示：<br><br>
<ul><li>READY：表示用户期望的Pod副本个数，以及当前处于Running状态的Pod个数。  </li><li>UP-TO-DATE：当前处于最新版本的Pod个数。所谓最新版本，指的是Pod的Spec部分与Deployment中Pod模版里定义的完全一致。  </li><li>AVAILABLE：当前已经可用的Pod的个数——既是Running状态，又是最新版本，并且已经处于Ready（监控检查正确）状态的Pod个数。</li></ul><br>
<br>3、模拟服务版本升级，触发滚动升级。  <br>
<br>接下来重新构建“micro-api”服务的版本，并将其上传至私有镜像仓库。之后，通过命令修改“micro-api”的Deployment所使用的镜像，并触发滚动升级。  <br>
<br>修改Deployment所使用的镜像的命令如下：<br><br>
<pre class="prettyprint">$ kubectl set image deployment/micro-api micro-api=registry.cn-hangzhou.aliyuncs.com/wudimanong/micro-api:1.1-SNAPSHOT<br>
deployment.apps/micro-api image updated<br>
</pre><br>
这里使用了“kubectl set image”指令，主要是为了方便操作，也可以直接在Kubernetes部署文件中进行镜像版本的修改。  <br>
<br>修改完Deployment的镜像版本后，Kubernetes会立即触发“滚动升级”的过程。可以通过“kubectl rollout status”指令来查看Deployment资源的状态变化。具体如下：<br><br>
<pre class="prettyprint">$ kubectl rollout status deployment/micro-api<br>
<br>
Waiting for deployment "micro-api" rollout to finish: 2 out of 3 new replicas have been updated...<br>
Waiting for deployment "micro-api" rollout to finish: 2 out of 3 new replicas have been updated...<br>
<br>
Waiting for deployment "micro-api" rollout to finish: 2 out of 3 new replicas have been updated...<br>
Waiting for deployment "micro-api" rollout to finish: 2 of 3 updated replicas are available...<br>
Waiting for deployment "micro-api" rollout to finish: 2 of 3 updated replicas are available...<br>
deployment "micro-api" successfully rolled out<br>
</pre><br>
这时，也可以通过查看Deployment的Events，看到这个“滚动升级”的过程。具体如下：<br>
<pre class="prettyprint">$ kubectl describe deployment micro-api<br>
...<br>
OldReplicaSets:  <none><br>
NewReplicaSet:   micro-api-d745d8649 (3/3 replicas created)<br>
Events:<br>
Type    Reason             Age   From                   Message<br>
----    ------             ----  ----                   -------<br>
Normal  ScalingReplicaSet  12m   deployment-controller  Scaled up replica set micro-api-677dd4d5b6 to 1<br>
Normal  ScalingReplicaSet  12m   deployment-controller  Scaled down replica set micro-api-57c7cb5b74 to 2<br>
Normal  ScalingReplicaSet  12m   deployment-controller  Scaled up replica set micro-api-677dd4d5b6 to 2<br>
Normal  ScalingReplicaSet  5m1s  deployment-controller  Scaled down replica set micro-api-677dd4d5b6 to 0<br>
Normal  ScalingReplicaSet  5m    deployment-controller  Scaled up replica set micro-api-d745d8649 to 2<br>
Normal  ScalingReplicaSet  56s   deployment-controller  Scaled down replica set micro-api-57c7cb5b74 to 0<br>
Normal  ScalingReplicaSet  56s   deployment-controller  Scaled up replica set micro-api-d745d8649 to 3<br>
</pre><br>
可以看到，当你修改了Deployment里的Pod定义后，“Deployment Controller”会使用这个修改后的Pod模版，创建一个新的ReplicaSet，这个新的ReplicaSet的初始Pod副本数是：0。  <br>
<br>然后在Age=12 m的位置，开始将这个新的ReplicaSet所控制的Pod副本数从0个变成1个。  <br>
<br>紧接着，在Age=12 m的位置，又将旧ReplicaSet所控制的Pod副本数减少1个，即“<strong>水平收缩</strong>”成两个副本。  <br>
<br><strong>如此交替进行，新ReplicaSet所管理的Pod的副本数，从0个变成1个，再变成2个，最后变成3个；而旧ReplicaSet所管理的Pod的副本数则从3个变成2个，最后变成0个</strong>。<br>
<br>这样，就完成了一组Pod的版本升级过程。而像这样<strong>将一个Kubernetes集群中正在运行的多个Pod版本，交替逐一升级的过程，就是“滚动升级”</strong>。<br>
<h4>金丝雀（灰度）发布</h4>上面内容比较详细的演示了Kubernetes的“滚动升级”的方式，<strong>虽然通过滚动升级的方式可以方便、平滑的实现版本更新，但是这个过程，并没有灰度功能</strong>。滚动升级的方式，虽然中间有缓冲交替的过程，但<strong>这种过程是自动的、迅速的，滚动升级过程结束就相当于直接进行了新版本的全量发布</strong>。  <br>
<br>而对于需要进行金丝雀（灰度）发布的场景，“滚动升级”的方式很显然是不够用的。那么，<strong>在Kubernetes中应该如何结合版本更新做到金丝雀（灰度）发布呢？</strong>  <br>
<br>具体步骤如下：<br>
<br>1、编写实现新版本灰度发布的部署文件。<br>
<br>为了实现在Kubernetes中的金丝雀（灰度）发布过程的可观测，我们重新定义下具体的Kubernetes发布文件（如：micro-api-canary.yaml）的内容如下：<br>
<pre class="prettyprint">...<br>
spec:<br>
selector:<br>
matchLabels:<br>
  app: micro-api<br>
replicas: 3<br>
#设置滚动升级策略<br>
#Kubernetes在等待设置的时间后才开始进行升级，例如5秒<br>
minReadySeconds: 5<br>
strategy:<br>
type: RollingUpdate<br>
rollingUpdate:<br>
  #升级过程中最多可以比原先设置多出的Pod数量<br>
  maxSurge: 1<br>
  #升级过程中Deployment控制器最多可以删除多少个旧Pod，主要用于提供缓冲时间<br>
  maxUnavailable: 1<br>
...<br>
</pre><br>
上述发布文件与上一小节中演示滚动升级时，发布文件的内容一致，只是<strong>为了方便观察灰度发布过程的实现，这里通过“track: canary”对新发布的Pod版本进行标记</strong>。<br>
<br>设置新版本的镜像为：“micro-api:1.3-SNAPSHOT”。并且通过“spec.selector.matchLabels.app:micro-api”与历史版本Pod所对应的Service（micro-api.yaml文件中定义的Service）资源定义匹配。<br>
<br>2、执行“滚动升级”发布命令，实现“灰度发布”效果。<br>
<pre class="prettyprint">$ kubectl apply -f micro-api-canary.yaml && kubectl rollout pause deployment/micro-api<br>
</pre><br>
上面通过“kubectl rollout pause”命令实现对Deployment的金丝雀（灰度发布）。执行发布命令之后的运行效果如下：<br>
<pre class="prettyprint">$ kubectl get pods --show-labels -o wide<br>
NAME                         READY   STATUS    RESTARTS   AGE     IP          NODE         NOMINATED NODE   READINESS GATES   LABELS<br>
micro-api-57c7cb5b74-mq7m9   1/1     Running   0          6m20s   10.32.0.3   kubernetes   <none>           <none>            app=micro-api,pod-template-hash=57c7cb5b74<br>
micro-api-57c7cb5b74-ptptj   1/1     Running   0          6m20s   10.32.0.4   kubernetes   <none>           <none>            app=micro-api,pod-template-hash=57c7cb5b74<br>
micro-api-7dbb6c5d66-4rbdc   1/1     Running   0          5m33s   10.32.0.6   kubernetes   <none>           <none>            app=micro-api,pod-template-hash=7dbb6c5d66,track=canary<br>
micro-api-7dbb6c5d66-cfk9l   1/1     Running   0          5m33s   10.32.0.5   kubernetes   <none>           <none>            app=micro-api,pod-template-hash=7dbb6c5d66,track=canary<br>
</pre><br>
查看Deployment的滚动升级情况，命令如下：<br>
<pre class="prettyprint">$ kubectl get deployments<br>
NAME            READY   UP-TO-DATE   AVAILABLE   AGE<br>
micro-api       4/3     2            4           194d<br>
</pre><br>
可以看到此时“micro-api” ready的数量为4，其中两个旧版本Pod，两个新版本Pod。<br>
<br>3、接下来进行流量测试。<br>
<br>查询两组Pod版本所对应的Service资源的IP，命令如下：<br>
<pre class="prettyprint"># kubectl get svc micro-api<br>
NAME        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)     AGE<br>
micro-api   ClusterIP   10.110.169.161   <none>        19090/TCP   194d<br>
</pre><br>
接下来，模拟对服务的接口进行批量访问，命令如下：<br><br>
<pre class="prettyprint">$ for i in &#123;1..10&#125;; do curl 10.110.169.161:19090/test/test; done<br>
<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125; <br>
</pre><br>
可以看到，此时流量会随机的流向旧版本和新版本（日志标记为V3）的服务。<br>
<br>4、将服务版本升级为新版本。<br>
<br>如果新版本的服务经过线上流量测试验证没有问题，则可以通过“rollout resume”命令将整体服务的版本升级为新版本。命令如下：<br>
<pre class="prettyprint">$ kubectl rollout resume deployment micro-api<br>
deployment.apps/micro-api resumed<br>
</pre><br>
升级后的效果如下：<br>
<pre class="prettyprint">$ kubectl get pods --show-labels -o wide<br>
NAME                         READY   STATUS    RESTARTS   AGE   IP          NODE         NOMINATED NODE   READINESS GATES   LABELS<br>
micro-api-7dbb6c5d66-4rbdc   1/1     Running   0          18m   10.32.0.6   kubernetes   <none>           <none>            app=micro-api,pod-template-hash=7dbb6c5d66,track=canary<br>
micro-api-7dbb6c5d66-bpjtg   1/1     Running   0          84s   10.32.0.3   kubernetes   <none>           <none>            app=micro-api,pod-template-hash=7dbb6c5d66,track=canary<br>
micro-api-7dbb6c5d66-cfk9l   1/1     Running   0          18m   10.32.0.5   kubernetes   <none>           <none>            app=micro-api,pod-template-hash=7dbb6c5d66,track=canary<br>
</pre><br>
可以看到，此时目标服务已经通过“滚动升级”的方式完成了全量更新。而如果存在问题，则通过“kubectl rollout undo”命令进行回滚即可！<br>
<br>从上述过程可以看到，Kubernetes中的金丝雀（灰度发布）主要是通过操纵（如：pause）“滚动升级”的过程来实现的——通过发布一定数量的新版本Pod，并利用Service资源类型本身的负载均衡能力来实现流量在新/旧Pod之间的随机交替。<br>
<br>这样的方式虽然已经可以满足一些简单的场景，但是没有办法做到<strong>更精准的灰度流量控制</strong>。这时候就需要借助 Service Mesh 中的解决方案了，下面我们来看看在 Istio 中如何做到精准流量的金丝雀（灰度）发布。<br>
<h3>Istio中的金丝雀（灰度）发布</h3>以下内容默认你已经在Kubernetes中安装了Istio环境，如果还没有安装可以参考《<a href="http://dockone.io/article/2125233">干货|如何步入Service Mesh微服务架构时代</a>》中分享的内容。<br>
<br>Istio与Kubernetes实现金丝雀（灰度）发布的方式不一样，<strong>Istio通过Envoy（SideCar）强大的路由规则管理能力，可以非常灵活地控制对应版本的流量占比，从而实现具备精准流量控制能力的金丝雀（灰度）发布功能</strong>。<br>
<br>Istio通过Envoy（SideCar）实现金丝雀（灰度）发布的流量路由示意图如下（继续以“micro-api”服务为例）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211015/4dcb9e588f9fe1bc3775618600f9b89e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211015/4dcb9e588f9fe1bc3775618600f9b89e.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从上图中可以大致看出，Istio具备强大的流量管理能力，而这种能力对于实现流量精准控制的金丝雀（灰度）发布功能来说，自然是水到渠成的。  <br>
<br>具体来说，在Istio中是通过<strong>VirtualService（虚拟服务）</strong>这种特定的资源在服务网格中实现流量路由的。通过VirtualService可以方便地定义流量路由规则，并在客户端试图连接到服务时应用这些规则，并最终到达目标服务。<br>
<br>接下来，具体演示如何在Istio中通过VirtualService实现金丝雀（灰度）发布。步骤如下：  <br>
<br>1、首先发布一个v1版本的服务。  <br>
<br>要在Istio中实现更精准的版本控制，需要在发布Pod资源时，通过明确的<strong>“版本标签”</strong>进行指定。准备“micro-api”服务v1版本的Kubernetes部署文件（micro-api-canary-istio-v1.yaml）：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: micro-api<br>
spec:<br>
type: ClusterIP<br>
ports:<br>
- name: http<br>
  port: 19090<br>
  targetPort: 9090<br>
selector:<br>
app: micro-api<br>
<br>
---<br>
<br>
apiVersion: apps/v1<br>
kind: Deployment<br>
meta data:<br>
name: micro-api-v1<br>
spec:<br>
selector:<br>
matchLabels:<br>
  app: micro-api<br>
  #这里是关键，需要设置版本标签，以便实现灰度发布<br>
  version: v1<br>
replicas: 3<br>
#设置滚动升级策略<br>
#Kubernetes在等待设置的时间后才开始进行升级，例如5秒<br>
minReadySeconds: 5<br>
strategy:<br>
type: RollingUpdate<br>
rollingUpdate:<br>
  #升级过程中最多可以比原先设置多出的Pod数量<br>
  maxSurge: 1<br>
  #升级过程中Deployment控制器最多可以删除多少个旧Pod，主要用于提供缓冲时间<br>
  maxUnavailable: 1<br>
template:<br>
metadata:<br>
  labels:<br>
    app: micro-api<br>
    #设置版本标签，便于灰度发布<br>
    version: v1<br>
spec:<br>
  #设置的阿里云私有镜像仓库登陆信息的secret<br>
  imagePullSecrets:<br>
    - name: regcred<br>
  containers:<br>
    - name: micro-api<br>
      image: registry.cn-hangzhou.aliyuncs.com/wudimanong/micro-api:1.1-SNAPSHOT<br>
      imagePullPolicy: Always<br>
      tty: true<br>
      ports:<br>
        - name: http<br>
          protocol: TCP<br>
          containerPort: 19090<br>
</pre><br>
“spec.selector.matchLabels.version:v1”标签用来标注服务的版本，该标签是后续Istio的流量管理规则中，识别服务版本的主要依据。<br>
<br>准备好发布文件后，执行发布命令：<br>
<pre class="prettyprint">$ kubectl apply -f micro-api-canary-istio-v1.yaml<br>
</pre><br>
此时，一个低版本的服务就运行成功了！接下来我们模拟对其实施金丝雀（灰度）发布。  <br>
<br>2、发布一个v2版本的服务（升级的目标版本）。  <br>
<br>与v1版本服务一样，发布的v2版本的服务也需要明确版本标签，其发布文件（micro-api-canary-istio-v2.yaml）的内容如下：<br><br>
<pre class="prettyprint">apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
name: micro-api-v2<br>
spec:<br>
selector:<br>
matchLabels:<br>
  app: micro-api<br>
  #设置好版本标签，便于灰度发布<br>
  version: v2<br>
replicas: 3<br>
#设置滚动升级策略<br>
#Kubernetes在等待设置的时间后才开始进行升级，例如5秒<br>
minReadySeconds: 5<br>
strategy:<br>
type: RollingUpdate<br>
rollingUpdate:<br>
  #升级过程中最多可以比原先设置多出的Pod数量<br>
  maxSurge: 1<br>
  #升级过程中Deployment控制器最多可以删除多少个旧Pod，主要用于提供缓冲时间<br>
  maxUnavailable: 1<br>
template:<br>
metadata:<br>
  labels:<br>
    app: micro-api<br>
    #设置好版本标签，便于灰度发布<br>
    version: v2<br>
spec:<br>
  #设置的阿里云私有镜像仓库登陆信息的secret<br>
  imagePullSecrets:<br>
    - name: regcred<br>
  containers:<br>
    - name: micro-api<br>
      image: registry.cn-hangzhou.aliyuncs.com/wudimanong/micro-api:1.3-SNAPSHOT<br>
      imagePullPolicy: Always<br>
      tty: true<br>
      ports:<br>
        - name: http<br>
          protocol: TCP<br>
          containerPort: 19090<br>
</pre><br>
执行发布命令：<br>
<pre class="prettyprint">$ kubectl apply -f micro-api-canary-istio-v2.yaml <br>
deployment.apps/micro-api-v2 created<br>
</pre><br>
此时，系统中就存在了<strong>两组版本</strong>的Pod资源，具体如下：<br><br>
<pre class="prettyprint"># kubectl get pods<br>
NAME                            READY   STATUS    RESTARTS   AGE<br>
micro-api-v1-565d749dd4-7c66z   1/1     Running   2          13h<br>
micro-api-v1-565d749dd4-7dqfb   1/1     Running   2          13h<br>
micro-api-v1-565d749dd4-l62wc   1/1     Running   2          13h<br>
micro-api-v2-6f98c598c9-5stlw   1/1     Running   0          82s<br>
micro-api-v2-6f98c598c9-f2ntq   1/1     Running   0          82s<br>
micro-api-v2-6f98c598c9-l8g4j   1/1     Running   0          82s<br>
</pre><br>
接下来将演示如何利用Istio强大的流量管理功能，来实现流量在这两组版本Pod资源之间的精确控制！ <br>
<br>3、创建Istio网关资源。<br>
<br>在Istio中要实现流量的精确控制，需要<strong>将VirtualService绑定到具体的Ingressgateway（入口网关）资源</strong>。因此在创建VirtualService资源实现流量路由及控制前，需要创建一个Istio网关。部署文件（micro-gateway.yaml）的内容如下：<br>
<pre class="prettyprint">apiVersion: networking.istio.io/v1alpha3<br>
kind: Gateway<br>
metadata:<br>
name: micro-gateway<br>
spec:<br>
selector:<br>
istio: ingressgateway<br>
servers:<br>
- port:<br>
    number: 80<br>
    name: http<br>
    protocol: HTTP<br>
  hosts:<br>
    - "*"<br>
</pre><br>
上述部署文件执行后将创建一个名称为“micro-gateway”的Istio网关，并允许所有主机（hosts:"*"指定）通过该网关。  <br>
<br>4、创建Istio虚拟服务资源VirtualService。<br>
<br>前面提到过<strong>在Istio中主要是通过VirtualService（虚拟服务）来实现服务网格内的流量路由及控制</strong>。接下来我们看看VirtualService资源的具体创建方式，准备资源文件（如virtual-service-all.yaml），内容如下：<br><br>
<pre class="prettyprint">apiVersion: networking.istio.io/v1alpha3<br>
kind: VirtualService<br>
metadata:<br>
name: micro-api-route<br>
spec:<br>
#用于定义流量被发送到的目标主机（这里为部署在Kubernetes中的micro-api服务）<br>
hosts:<br>
- micro-api.default.svc.cluster.local<br>
#将VirtualService绑定到Istio网关，通过网关来暴露路由目标<br>
gateways:<br>
- micro-gateway<br>
http:<br>
- route:<br>
    #设置旧版本（V1）版本的流量占比为70%<br>
    - destination:<br>
        host: micro-api.default.svc.cluster.local<br>
        subset: v1<br>
      #通过权重值来设置流量占比<br>
      weight: 70<br>
    #设置新版本（V2）版本的流量占比为30%<br>
    - destination:<br>
        host: micro-api.default.svc.cluster.local<br>
        subset: v2<br>
      weight: 30<br>
</pre><br>
如上所示，<strong>VirtualService资源具备针对http的精准流量控制能力，可以将指定占比的流量路由到特定的“subset”指定的版本。而为了实现这一能力，VirtualService资源还需要与Istio网关绑定，通过Istio网关来暴露路由目标</strong>。<br>
<br>5、创建Istio目标路由规则资源。  <br>
<br>虚拟服务VirtualService在Istio中主要用于控制流量的行为，而定义流量行为的路由规则则需要通过“<strong>DestinationRule</strong>”路由规则资源来定义。创建路由规则文件（destination-rule-all.yaml），具体内容如下：<br>
<pre class="prettyprint">apiVersion: networking.istio.io/v1alpha3<br>
kind: DestinationRule<br>
metadata:<br>
name: micro-api-destination<br>
spec:<br>
#与Deployment资源对应的Service资源名称关联<br>
host: micro-api<br>
#流量策略设置：负载均衡策略、连接池大小、局部异常检测等，在路由发生后作用于流量<br>
trafficPolicy:<br>
#限流策略<br>
connectionPool:<br>
  tcp:<br>
    maxConnections: 10<br>
  http:<br>
    http1MaxPendingRequests: 1<br>
    maxRequestsPerConnection: 1<br>
#设置目的地的负债均衡算法<br>
loadBalancer:<br>
  simple: ROUND_ROBIN<br>
#目的地指的是不同的子集（subset）或服务版本。通子集（subset），可以识别应用程序的不同版本，以实现流量在不同服务版本之间的切换<br>
subsets:<br>
- name: v1<br>
  labels:<br>
    version: v1<br>
- name: v2<br>
  labels:<br>
    version: v2<br>
</pre><br>
如上所示，通过subsets属性，定义了VirtualService资源用于路由的具体版本标签匹配信息。至此，针对两个版本服务的灰度流量控制规则就设置好了，接下来测试具体的金丝雀（灰度）发布效果。  <br>
<br>6、测试Istio实现金丝雀（灰度）发布的流量控制效果。<br>
<br>在正式测试之前，可以通过命令查看下当前的部署资源情况：<br><br>
<pre class="prettyprint">#查看部署的Deployment资源<br>
kubectl get deploy  | grep micro-api<br>
<br>
micro-api-v1             3/3     3            3           21h<br>
micro-api-v2             3/3     3            3           8h<br>
</pre><br>
<pre class="prettyprint">#查看两组版本Pod资源对应的K8s-Service的服务IP<br>
kubectl get svc micro-api<br>
<br>
NAME        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)     AGE<br>
micro-api   ClusterIP   10.110.169.161   <none>        19090/TCP   205d<br>
</pre><br>
<pre class="prettyprint">#查看VirtualService资源定义<br>
kubectl get vs<br>
<br>
NAME              GATEWAYS          HOSTS                                   AGE<br>
micro-api-route   [micro-gateway]   [micro-api.default.svc.cluster.local]   7h34m<br>
</pre><br>
<pre class="prettyprint">#查看定义的路由规则资源<br>
kubectl get dr<br>
<br>
NAME                    HOST        AGE<br>
micro-api-destination   micro-api   7h27m<br>
</pre><br>
通过上面的资源信息查看，这里我们已经可以查到Deployments对应的K8s-Service资源的IP，但如果<strong>通过K8s-Service资源来进行测试的话，会发现流量的控制并不精准，并不能达到我们设置的70%流量流向v1，30%的流量流向v2（因为这是随机流量）</strong>。<br>
<br>因此，<strong>要使用Istio的精准流量控制功能，还需要使用Istio的Ingressgateway</strong>。查看Istio的Ingressgateway资源IP的命令如下：<br><br>
<pre class="prettyprint">#查看ingress的IP<br>
kubectl get svc -n istio-system | grep ingress<br>
<br>
istio-ingressgateway   LoadBalancer   10.98.178.61     <pending>     15021:31310/TCP,80:32113/TCP,443:31647/TCP,31400:30745/TCP,15443:30884/TCP   7h54m<br>
</pre><br>
接下来，通过Ingress的IP来访问“micro-api”服务，命令及效果如下：<br><br>
<pre class="prettyprint"># for i in &#123;1..10&#125;; do curl -H "Host:micro-api.default.svc.cluster.local" 10.98.178.61:80/test/test; done<br>
<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125; <br>
</pre><br>
如上所示，流量按照设定的比例（v1:70%;v2:30%）进行了分流。  <br>
<br>7、测试将流量全部切向新版本。  <br>
<br>为了更明显地验证Istio的流量控制效果，接下来，我们通过变更VirtualService资源的流量设置占比，将流量全部切到新版本。变更后的VirtualService资源的配置文件内容如下：<br>
<pre class="prettyprint">apiVersion: networking.istio.io/v1alpha3<br>
kind: VirtualService<br>
metadata:<br>
name: micro-api-route<br>
spec:<br>
#用于定义流量被发送到的目标主机（这里为部署在Kubernetes中的micro-api服务）<br>
hosts:<br>
- micro-api.default.svc.cluster.local<br>
#将VirtualService绑定到Istio网关，通过网关来暴露路由目标<br>
gateways:<br>
- micro-gateway<br>
http:<br>
- route:<br>
    #设置旧版本（V1）版本的流量占比为70%<br>
    - destination:<br>
        host: micro-api.default.svc.cluster.local<br>
        subset: v1<br>
      #通过权重值来设置流量占比<br>
      weight: 0<br>
    #设置新版本（V2）版本的流量占比为30%<br>
    - destination:<br>
        host: micro-api.default.svc.cluster.local<br>
        subset: v2<br>
      weight: 100<br>
</pre><br>
继续通过Istio网关访问目标服务，命令如下：<br><br>
<pre class="prettyprint"># for i in &#123;1..10&#125;; do curl -H "Host:micro-api.default.svc.cluster.local" 10.98.178.61:80/test/test; done<br>
<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125;<br>
&#123;"code":0,"data":"V3|无依赖测试接口返回->OK!","message":"成功"&#125; <br>
</pre><br>
可以观察到，此时流量已经全部切换到了新版本服务！<br><br>
<h3>后记</h3>在微服务时代，不同的服务之间相互联系，关系错综复杂，部署升级一个服务，可能造成整个系统的瘫痪，因此，需要选择合适的部署方式，从而将风险降到最低。金丝雀（灰度）发布只是多种部署方式的一种，还有蓝绿部署、滚动部署（如K8s的滚动升级）等，可以根据不同的业务场景选择不同的发布形式。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/a8OLm7udd0T0PY2TskZELw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/a8OLm7udd0T0PY2TskZELw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            