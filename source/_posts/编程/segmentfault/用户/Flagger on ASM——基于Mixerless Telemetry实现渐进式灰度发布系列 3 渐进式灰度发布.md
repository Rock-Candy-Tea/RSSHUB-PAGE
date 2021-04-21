
---
title: 'Flagger on ASM——基于Mixerless Telemetry实现渐进式灰度发布系列 3 渐进式灰度发布'
categories: 
 - 编程
 - segmentfault
 - 用户
headimg: 'https://segmentfault.com/img/bVcRoT5'
author: segmentfault
comments: false
date: 2021-04-21 12:10:38
thumbnail: 'https://segmentfault.com/img/bVcRoT5'
---

<div>   
<p>简介： 作为CNCF<a href="https://landscape.cncf.io/card-mode?category=continuous-integration-delivery&grouping=category&selected=weave-flagger" rel="nofollow">成员</a>，<a href="https://segmentfault.com/a/undefined">Weave Flagger</a>提供了持续集成和持续交付的各项能力。Flagger将渐进式发布总结为3类： - <strong>灰度发布/金丝雀发布(Canary)</strong>：用于渐进式切流到灰度版本(progressive traffic shifting) - <strong>A/B测试(A/B Testing)</strong>：用于根据请求信息将<br>作为CNCF成员，Weave Flagger提供了持续集成和持续交付的各项能力。Flagger将渐进式发布总结为3类：</p><p>灰度发布/金丝雀发布(Canary)：用于渐进式切流到灰度版本(progressive traffic shifting)<br>A/B测试(A/B Testing)：用于根据请求信息将用户请求路由到A/B版本(HTTP headers and cookies traffic routing)<br>蓝绿发布(Blue/Green)：用于流量切换和流量复制 (traffic switching and mirroring)<br>本篇将介绍Flagger on ASM的渐进式灰度发布实践。</p><p>Setup Flagger<br>1 部署Flagger<br>执行如下命令部署flagger(完整脚本参见：demo_canary.sh)。</p><p>alias k="kubectl --kubeconfig $USER_CONFIG"<br>alias h="helm --kubeconfig $USER_CONFIG"</p><p>cp $MESH_CONFIG kubeconfig<br>k -n istio-system create secret generic istio-kubeconfig --from-file kubeconfig<br>k -n istio-system label secret istio-kubeconfig istio/multiCluster=true</p><p>h repo add flagger <a href="https://flagger.app/" rel="nofollow">https://flagger.app</a><br>h repo update<br>k apply -f $FLAAGER_SRC/artifacts/flagger/crd.yaml<br>h upgrade -i flagger flagger/flagger --namespace=istio-system \</p><pre><code>--set crd.create=false \
--set meshProvider=istio \
--set metricsServer=http://prometheus:9090 \
--set istio.kubeconfig.secretName=istio-kubeconfig \
--set istio.kubeconfig.key=kubeconfig</code></pre><p>2 部署Gateway<br>在灰度发布过程中，Flagger会请求ASM更新用于灰度流量配置的VirtualService，这个VirtualService会使用到命名为public-gateway的Gateway。为此我们创建相关Gateway配置文件public-gateway.yaml如下：</p><p>apiVersion: networking.istio.io/v1alpha3<br>kind: Gateway<br>metadata:<br>  name: public-gateway<br>  namespace: istio-system<br>spec:<br>  selector:</p><pre><code>istio: ingressgateway</code></pre><p>servers:</p><pre><code>- port:
    number: 80
    name: http
    protocol: HTTP
  hosts:
    - "*"</code></pre><p>执行如下命令部署Gateway：</p><p>kubectl --kubeconfig "$MESH_CONFIG" apply -f resources_canary/public-gateway.yaml<br>3 部署flagger-loadtester<br>flagger-loadtester是灰度发布阶段，用于探测灰度POD实例的应用。</p><p>执行如下命令部署flagger-loadtester：</p><p>kubectl --kubeconfig "$USER_CONFIG" apply -k "https://github.com/fluxcd/flagger//kustomize/tester?ref=main"<br>4 部署PodInfo及其HPA<br>我们首先使用Flagger发行版自带的HPA配置(这是一个运维级的HPA)，待完成完整流程后，我们再使用应用级的HPA。</p><p>执行如下命令部署PodInfo及其HPA：</p><p>kubectl --kubeconfig "$USER_CONFIG" apply -k "https://github.com/fluxcd/flagger//kustomize/podinfo?ref=main"<br>渐进式灰度发布<br>1 部署Canary<br>Canary是基于Flagger进行灰度发布的核心CRD，详见How it works。我们首先部署如下Canary配置文件podinfo-canary.yaml，完成完整的渐进式灰度流程，然后在此基础上引入应用维度的监控指标，来进一步实现应用有感知的渐进式灰度发布。</p><p>apiVersion: flagger.app/v1beta1<br>kind: Canary<br>metadata:<br>  name: podinfo<br>  namespace: test<br>spec:<br>  # deployment reference<br>  targetRef:</p><pre><code>apiVersion: apps/v1
kind: Deployment
name: podinfo</code></pre><p># the maximum time in seconds for the canary deployment<br>  # to make progress before it is rollback (default 600s)<br>  progressDeadlineSeconds: 60<br>  # HPA reference (optional)<br>  autoscalerRef:</p><pre><code>apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
name: podinfo</code></pre><p>service:</p><pre><code># service port number
port: 9898
# container port number or name (optional)
targetPort: 9898
# Istio gateways (optional)
gateways:
- public-gateway.istio-system.svc.cluster.local
# Istio virtual service host names (optional)
hosts:
- '*'
# Istio traffic policy (optional)
trafficPolicy:
  tls:
    # use ISTIO_MUTUAL when mTLS is enabled
    mode: DISABLE
# Istio retry policy (optional)
retries:
  attempts: 3
  perTryTimeout: 1s
  retryOn: "gateway-error,connect-failure,refused-stream"</code></pre><p>analysis:</p><pre><code># schedule interval (default 60s)
interval: 1m
# max number of failed metric checks before rollback
threshold: 5
# max traffic percentage routed to canary
# percentage (0-100)
maxWeight: 50
# canary increment step
# percentage (0-100)
stepWeight: 10
metrics:
- name: request-success-rate
  # minimum req success rate (non 5xx responses)
  # percentage (0-100)
  thresholdRange:
    min: 99
  interval: 1m
- name: request-duration
  # maximum req duration P99
  # milliseconds
  thresholdRange:
    max: 500
  interval: 30s
# testing (optional)
webhooks:
  - name: acceptance-test
    type: pre-rollout
    url: http://flagger-loadtester.test/
    timeout: 30s
    metadata:
      type: bash
      cmd: "curl -sd 'test' http://podinfo-canary:9898/token | grep token"
  - name: load-test
    url: http://flagger-loadtester.test/
    timeout: 5s
    metadata:
      cmd: "hey -z 1m -q 10 -c 2 http://podinfo-canary.test:9898/"</code></pre><p>执行如下命令部署Canary：</p><p>kubectl --kubeconfig "$USER_CONFIG" apply -f resources_canary/podinfo-canary.yaml<br>部署Canary后，Flagger会将名为podinfo的Deployment复制为podinfo-primary，并将podinfo-primary扩容至HPA定义的最小POD数量。然后逐步将名为podinfo的这个Deployment的POD数量将缩容至0。也就是说，podinfo将作为灰度版本的Deployment，podinfo-primary将作为生产版本的Deployment。</p><p>同时，创建3个服务——podinfo、podinfo-primary和podinfo-canary，前两者指向podinfo-primary这个Deployment，最后者指向podinfo这个Deployment。</p><p>2 升级podinfo<br>执行如下命令，将灰度Deployment的版本从3.1.0升级到3.1.1：</p><p>kubectl --kubeconfig "$USER_CONFIG" -n test set image deployment/podinfo podinfod=stefanprodan/podinfo:3.1.1<br>3 渐进式灰度发布<br>此时，Flagger将开始执行如本系列第一篇所述的渐进式灰度发布流程，这里再简述主要流程如下：</p><p>逐步扩容灰度POD、验证<br>渐进式切流、验证<br>滚动升级生产Deployment、验证<br>100%切回生产<br>缩容灰度POD至0<br>我们可以通过如下命令观察这个渐进式切流的过程：</p><p>while true; do kubectl --kubeconfig "$USER_CONFIG" -n test describe canary/podinfo; sleep 10s;done<br>输出的日志信息示意如下：</p><p>Events:<br>  Type     Reason  Age                From     Message<br>  ----     ------  ----               ----     -------<br>  Warning  Synced  39m                flagger  podinfo-primary.test not ready: waiting for rollout to finish: observed deployment generation less then desired generation<br>  Normal   Synced  38m (x2 over 39m)  flagger  all the metrics providers are available!<br>  Normal   Synced  38m                flagger  Initialization done! podinfo.test<br>  Normal   Synced  37m                flagger  New revision detected! Scaling up podinfo.test<br>  Normal   Synced  36m                flagger  Starting canary analysis for podinfo.test<br>  Normal   Synced  36m                flagger  Pre-rollout check acceptance-test passed<br>  Normal   Synced  36m                flagger  Advance podinfo.test canary weight 10<br>  Normal   Synced  35m                flagger  Advance podinfo.test canary weight 20<br>  Normal   Synced  34m                flagger  Advance podinfo.test canary weight 30<br>  Normal   Synced  33m                flagger  Advance podinfo.test canary weight 40<br>  Normal   Synced  29m (x4 over 32m)  flagger  (combined from similar events): Promotion completed! Scaling down podinfo.test<br>相应的Kiali视图(可选)，如下图所示：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRoT5" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>到此，我们完成了一个完整的渐进式灰度发布流程。如下是扩展阅读。</p><p>灰度中的应用级扩缩容<br>在完成上述渐进式灰度发布流程的基础上，我们接下来再来看上述Canary配置中，关于HPA的配置。</p><p>autoscalerRef:</p><pre><code>apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
name: podinfo</code></pre><p>这个名为podinfo的HPA是Flagger自带的配置，当灰度Deployment的CPU利用率达到99%时扩容。完整配置如下：</p><p>apiVersion: autoscaling/v2beta2<br>kind: HorizontalPodAutoscaler<br>metadata:<br>  name: podinfo<br>spec:<br>  scaleTargetRef:</p><pre><code>apiVersion: apps/v1
kind: Deployment
name: podinfo</code></pre><p>minReplicas: 2<br>  maxReplicas: 4<br>  metrics:</p><pre><code>- type: Resource
  resource:
    name: cpu
    target:
      type: Utilization
      # scale up if usage is above
      # 99% of the requested CPU (100m)
      averageUtilization: 99</code></pre><p>我们在前面一篇中讲述了应用级扩缩容的实践，在此，我们将其应用于灰度发布的过程中。</p><p>1 感知应用QPS的HPA<br>执行如下命令部署感知应用请求数量的HPA，实现在QPS达到10时进行扩容(完整脚本参见：advanced_canary.sh)：</p><p>kubectl --kubeconfig "$USER_CONFIG" apply -f resources_hpa/requests_total_hpa.yaml<br>相应地，Canary配置更新为：</p><p>autoscalerRef:</p><pre><code>apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
name: podinfo-total</code></pre><p>2 升级podinfo<br>执行如下命令，将灰度Deployment的版本从3.1.0升级到3.1.1：</p><p>kubectl --kubeconfig "$USER_CONFIG" -n test set image deployment/podinfo podinfod=stefanprodan/podinfo:3.1.1<br>3 验证渐进式灰度发布及HPA<br>命令观察这个渐进式切流的过程：</p><p>while true; do k -n test describe canary/podinfo; sleep 10s;done<br>在渐进式灰度发布过程中(在出现Advance podinfo.test canary weight 10信息后，见下图)，我们使用如下命令，从入口网关发起请求以增加QPS：</p><p>INGRESS_GATEWAY=$(kubectl --kubeconfig $USER_CONFIG -n istio-system get service istio-ingressgateway -o jsonpath='&#123;.status.loadBalancer.ingress[0].ip&#125;')<br>hey -z 20m -c 2 -q 10 <a href="http://$ingress_gateway/" rel="nofollow">http://$INGRESS_GATEWAY</a><br>使用如下命令观察渐进式灰度发布进度：</p><p>watch kubectl --kubeconfig $USER_CONFIG get canaries --all-namespaces<br>使用如下命令观察hpa的副本数变化：</p><p>watch kubectl --kubeconfig $USER_CONFIG -n test get hpa/podinfo-total<br>结果如下图所示，在渐进式灰度发布过程中，当切流到30%的某一时刻，灰度Deployment的副本数为4：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRoUE" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>灰度中的应用级监控指标<br>在完成上述灰度中的应用级扩缩容的基础上，最后我们再来看上述Canary配置中，关于metrics的配置：</p><p>analysis:</p><pre><code>metrics:
- name: request-success-rate
  # minimum req success rate (non 5xx responses)
  # percentage (0-100)
  thresholdRange:
    min: 99
  interval: 1m
- name: request-duration
  # maximum req duration P99
  # milliseconds
  thresholdRange:
    max: 500
  interval: 30s
# testing (optional)</code></pre><p>1 Flagger内置监控指标<br>到目前为止，Canary中使用的metrics配置一直是Flagger的两个内置监控指标：请求成功率(request-success-rate)和请求延迟(request-duration)。如下图所示，Flagger中不同平台对内置监控指标的定义，其中，istio使用的是本系列第一篇介绍的Mixerless Telemetry相关的遥测数据。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRoUZ" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>2 自定义监控指标<br>为了展示灰度发布过程中，遥测数据为验证灰度环境带来的更多灵活性，我们再次以istio_requests_total为例，创建一个名为not-found-percentage的MetricTemplate，统计请求返回404错误码的数量占请求总数的比例。</p><p>配置文件metrics-404.yaml如下(完整脚本参见：advanced_canary.sh)：</p><p>apiVersion: flagger.app/v1beta1<br>kind: MetricTemplate<br>metadata:<br>  name: not-found-percentage<br>  namespace: istio-system<br>spec:<br>  provider:</p><pre><code>type: prometheus
address: http://prometheus.istio-system:9090</code></pre><p>query: |</p><pre><code>100 - sum(
    rate(
        istio_requests_total&#123;
          reporter="destination",
          destination_workload_namespace="&#123;&#123; namespace &#125;&#125;",
          destination_workload="&#123;&#123; target &#125;&#125;",
          response_code!="404"
        &#125;[&#123;&#123; interval &#125;&#125;]
    )
)
/
sum(
    rate(
        istio_requests_total&#123;
          reporter="destination",
          destination_workload_namespace="&#123;&#123; namespace &#125;&#125;",
          destination_workload="&#123;&#123; target &#125;&#125;"
        &#125;[&#123;&#123; interval &#125;&#125;]
    )
) * 100</code></pre><p>执行如下命令创建上述MetricTemplate：</p><p>k apply -f resources_canary2/metrics-404.yaml<br>相应地，Canary中metrics的配置更新为：</p><p>analysis:</p><pre><code>metrics:
  - name: "404s percentage"
    templateRef:
      name: not-found-percentage
      namespace: istio-system
    thresholdRange:
      max: 5
    interval: 1m</code></pre><p>3 最后的验证<br>最后，我们一次执行完整的实验脚本。脚本advanced_canary.sh示意如下：</p><h1>!/usr/bin/env sh</h1><p>SCRIPT_PATH="$(</p><pre><code>cd "$(dirname "$0")" >/dev/null 2>&1
pwd -P</code></pre><p>)/"<br>cd "$SCRIPT_PATH" || exit</p><p>source config<br>alias k="kubectl --kubeconfig $USER_CONFIG"<br>alias m="kubectl --kubeconfig $MESH_CONFIG"<br>alias h="helm --kubeconfig $USER_CONFIG"</p><p>echo "#### I Bootstrap ####"<br>echo "1 Create a test namespace with Istio sidecar injection enabled:"<br>k delete ns test<br>m delete ns test<br>k create ns test<br>m create ns test<br>m label namespace test istio-injection=enabled</p><p>echo "2 Create a deployment and a horizontal pod autoscaler:"<br>k apply -f $FLAAGER_SRC/kustomize/podinfo/deployment.yaml -n test<br>k apply -f resources_hpa/requests_total_hpa.yaml<br>k get hpa -n test</p><p>echo "3 Deploy the load testing service to generate traffic during the canary analysis:"<br>k apply -k "https://github.com/fluxcd/flagger//kustomize/tester?ref=main"</p><p>k get pod,svc -n test<br>echo "......"<br>sleep 40s</p><p>echo "4 Create a canary custom resource:"<br>k apply -f resources_canary2/metrics-404.yaml<br>k apply -f resources_canary2/podinfo-canary.yaml</p><p>k get pod,svc -n test<br>echo "......"<br>sleep 120s</p><p>echo "#### III Automated canary promotion ####"</p><p>echo "1 Trigger a canary deployment by updating the container image:"<br>k -n test set image deployment/podinfo podinfod=stefanprodan/podinfo:3.1.1</p><p>echo "2 Flagger detects that the deployment revision changed and starts a new rollout:"</p><p>while true; do k -n test describe canary/podinfo; sleep 10s;done<br>使用如下命令执行完整的实验脚本：</p><p>sh progressive_delivery/advanced_canary.sh<br>实验结果示意如下：</p><h4>I Bootstrap</h4><p>1 Create a test namespace with Istio sidecar injection enabled:<br>namespace "test" deleted<br>namespace "test" deleted<br>namespace/test created<br>namespace/test created<br>namespace/test labeled<br>2 Create a deployment and a horizontal pod autoscaler:<br>deployment.apps/podinfo created<br>horizontalpodautoscaler.autoscaling/podinfo-total created<br>NAME            REFERENCE            TARGETS              MINPODS   MAXPODS   REPLICAS   AGE<br>podinfo-total   Deployment/podinfo   <unknown>/10 (avg)   1         5         0          0s<br>3 Deploy the load testing service to generate traffic during the canary analysis:<br>service/flagger-loadtester created<br>deployment.apps/flagger-loadtester created<br>NAME                                      READY   STATUS     RESTARTS   AGE<br>pod/flagger-loadtester-76798b5f4c-ftlbn   0/2     Init:0/1   0          1s<br>pod/podinfo-689f645b78-65n9d              1/1     Running    0          28s</p><p>NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE<br>service/flagger-loadtester   ClusterIP   172.21.15.223   <none>        80/TCP    1s<br>......<br>4 Create a canary custom resource:<br>metrictemplate.flagger.app/not-found-percentage created<br>canary.flagger.app/podinfo created<br>NAME                                      READY   STATUS    RESTARTS   AGE<br>pod/flagger-loadtester-76798b5f4c-ftlbn   2/2     Running   0          41s<br>pod/podinfo-689f645b78-65n9d              1/1     Running   0          68s</p><p>NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE<br>service/flagger-loadtester   ClusterIP   172.21.15.223   <none>        80/TCP    41s<br>......</p><h4>III Automated canary promotion</h4><p>1 Trigger a canary deployment by updating the container image:<br>deployment.apps/podinfo image updated<br>2 Flagger detects that the deployment revision changed and starts a new rollout:</p><p>Events:<br>  Type     Reason  Age                  From     Message<br>  ----     ------  ----                 ----     -------<br>  Warning  Synced  10m                  flagger  podinfo-primary.test not ready: waiting for rollout to finish: observed deployment generation less then desired generation<br>  Normal   Synced  9m23s (x2 over 10m)  flagger  all the metrics providers are available!<br>  Normal   Synced  9m23s                flagger  Initialization done! podinfo.test<br>  Normal   Synced  8m23s                flagger  New revision detected! Scaling up podinfo.test<br>  Normal   Synced  7m23s                flagger  Starting canary analysis for podinfo.test<br>  Normal   Synced  7m23s                flagger  Pre-rollout check acceptance-test passed<br>  Normal   Synced  7m23s                flagger  Advance podinfo.test canary weight 10<br>  Normal   Synced  6m23s                flagger  Advance podinfo.test canary weight 20<br>  Normal   Synced  5m23s                flagger  Advance podinfo.test canary weight 30<br>  Normal   Synced  4m23s                flagger  Advance podinfo.test canary weight 40<br>  Normal   Synced  23s (x4 over 3m23s)  flagger  (combined from similar events): Promotion completed! Scaling down podinfo.test<br><a href="https://developer.aliyun.com/article/783553?utm_content=g_1000264439" rel="nofollow">原文链接</a><br>本文为阿里云原创内容，未经允许不得转载。</p>  
</div>
            