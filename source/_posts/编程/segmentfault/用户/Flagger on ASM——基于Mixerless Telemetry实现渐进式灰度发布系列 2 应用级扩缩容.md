
---
title: 'Flagger on ASM——基于Mixerless Telemetry实现渐进式灰度发布系列 2 应用级扩缩容'
categories: 
 - 编程
 - segmentfault
 - 用户
headimg: 'https://segmentfault.com/img/bVcRoDX'
author: segmentfault
comments: false
date: 2021-04-21 12:10:38
thumbnail: 'https://segmentfault.com/img/bVcRoDX'
---

<div>   
<p>简介： 应用级扩缩容是相对于运维级而言的。像监控CPU/内存的利用率就属于应用无关的纯运维指标，针对这种指标进行扩缩容的HPA配置就是运维级扩缩容。而像请求数量、请求延迟、P99分布等指标就属于应用相关的，或者叫业务感知的监控指标。 本篇将介绍3种应用级监控指标在HPA中的配置，以实现应用级自动扩缩容。<br>应用级扩缩容是相对于运维级而言的。像监控CPU/内存的利用率就属于应用无关的纯运维指标，针对这种指标进行扩缩容的HPA配置就是运维级扩缩容。而像请求数量、请求延迟、P99分布等指标就属于应用相关的，或者叫业务感知的监控指标。</p><p>本篇将介绍3种应用级监控指标在HPA中的配置，以实现应用级自动扩缩容。</p><p>Setup HPA<br>1 部署metrics-adapter<br>执行如下命令部署kube-metrics-adapter(完整脚本参见：demo_hpa.sh)。：</p><p>helm --kubeconfig "$USER_CONFIG" -n kube-system install asm-custom-metrics \<br>  $KUBE_METRICS_ADAPTER_SRC/deploy/charts/kube-metrics-adapter \<br>  --set prometheus.url=<a href="http://prometheus.istio-system.svc:9090/" rel="nofollow">http://prometheus.istio-syste...</a><br>执行如下命令验证部署情况：</p><h1>验证POD</h1><p>kubectl --kubeconfig "$USER_CONFIG" get po -n kube-system | grep metrics-adapter</p><p>asm-custom-metrics-kube-metrics-adapter-6fb4949988-ht8pv   1/1     Running     0          30s</p><h1>验证CRD</h1><p>kubectl --kubeconfig "$USER_CONFIG" api-versions | grep "autoscaling/v2beta"</p><p>autoscaling/v2beta1<br>autoscaling/v2beta2</p><h1>验证CRD</h1><p>kubectl --kubeconfig "$USER_CONFIG" get --raw "/apis/external.metrics.k8s.io/v1beta1" | jq .</p><p>&#123;<br>  "kind": "APIResourceList",<br>  "apiVersion": "v1",<br>  "groupVersion": "external.metrics.k8s.io/v1beta1",<br>  "resources": []<br>&#125;<br>2 部署loadtester<br>执行如下命令部署flagger loadtester：</p><p>kubectl --kubeconfig "$USER_CONFIG" apply -f $FLAAGER_SRC/kustomize/tester/deployment.yaml -n test<br>kubectl --kubeconfig "$USER_CONFIG" apply -f $FLAAGER_SRC/kustomize/tester/service.yaml -n test<br>3 部署HPA<br>3.1 根据应用请求数量扩缩容<br>首先我们创建一个感知应用请求数量(istio_requests_total)的HorizontalPodAutoscaler配置：</p><p>apiVersion: autoscaling/v2beta2<br>kind: HorizontalPodAutoscaler<br>metadata:<br>  name: podinfo-total<br>  namespace: test<br>  annotations:</p><pre><code>metric-config.external.prometheus-query.prometheus/processed-requests-per-second: |
  sum(rate(istio_requests_total&#123;destination_workload_namespace="test",reporter="destination"&#125;[1m]))</code></pre><p>spec:<br>  maxReplicas: 5<br>  minReplicas: 1<br>  scaleTargetRef:</p><pre><code>apiVersion: apps/v1
kind: Deployment
name: podinfo</code></pre><p>metrics:</p><pre><code>- type: External
  external:
    metric:
      name: prometheus-query
      selector:
        matchLabels:
          query-name: processed-requests-per-second
    target:
      type: AverageValue
      averageValue: "10"</code></pre><p>执行如下命令部署这个HPA配置：</p><p>kubectl --kubeconfig "$USER_CONFIG" apply -f resources_hpa/requests_total_hpa.yaml<br>执行如下命令校验：</p><p>kubectl --kubeconfig "$USER_CONFIG" get --raw "/apis/external.metrics.k8s.io/v1beta1" | jq .<br>结果如下：</p><p>&#123;<br>  "kind": "APIResourceList",<br>  "apiVersion": "v1",<br>  "groupVersion": "external.metrics.k8s.io/v1beta1",<br>  "resources": [</p><pre><code>&#123;
  "name": "prometheus-query",
  "singularName": "",
  "namespaced": true,
  "kind": "ExternalMetricValueList",
  "verbs": [
    "get"
  ]
&#125;</code></pre><p>]<br>&#125;<br>类似地，我们可以使用其他维度的应用级监控指标配置HPA。举例如下，不再冗述。</p><p>3.2 根据平均延迟扩缩容<br>apiVersion: autoscaling/v2beta2<br>kind: HorizontalPodAutoscaler<br>metadata:<br>  name: podinfo-latency-avg<br>  namespace: test<br>  annotations:</p><pre><code>metric-config.external.prometheus-query.prometheus/latency-average: |
  sum(rate(istio_request_duration_milliseconds_sum&#123;destination_workload_namespace="test",reporter="destination"&#125;[1m]))
  /sum(rate(istio_request_duration_milliseconds_count&#123;destination_workload_namespace="test",reporter="destination"&#125;[1m]))</code></pre><p>spec:<br>  maxReplicas: 5<br>  minReplicas: 1<br>  scaleTargetRef:</p><pre><code>apiVersion: apps/v1
kind: Deployment
name: podinfo</code></pre><p>metrics:</p><pre><code>- type: External
  external:
    metric:
      name: prometheus-query
      selector:
        matchLabels:
          query-name: latency-average
    target:
      type: AverageValue
      averageValue: "0.005"</code></pre><p>3.3 根据P95分布扩缩容<br>apiVersion: autoscaling/v2beta2<br>kind: HorizontalPodAutoscaler<br>metadata:<br>  name: podinfo-p95<br>  namespace: test<br>  annotations:</p><pre><code>metric-config.external.prometheus-query.prometheus/p95-latency: |
  histogram_quantile(0.95,sum(irate(istio_request_duration_milliseconds_bucket&#123;destination_workload_namespace="test",destination_canonical_service="podinfo"&#125;[5m]))by (le))</code></pre><p>spec:<br>  maxReplicas: 5<br>  minReplicas: 1<br>  scaleTargetRef:</p><pre><code>apiVersion: apps/v1
kind: Deployment
name: podinfo</code></pre><p>metrics:</p><pre><code>- type: External
  external:
    metric:
      name: prometheus-query
      selector:
        matchLabels:
          query-name: p95-latency
    target:
      type: AverageValue
      averageValue: "4"</code></pre><p>验证HPA<br>1 生成负载<br>执行如下命令产生实验流量，以验证HPA配置自动扩容生效。</p><p>alias k="kubectl --kubeconfig $USER_CONFIG"<br>loadtester=$(k -n test get pod -l "app=flagger-loadtester" -o jsonpath='&#123;.items..metadata.name&#125;')<br>k -n test exec -it $&#123;loadtester&#125; -c loadtester -- hey -z 5m -c 2 -q 10 <a href="http://podinfo:9898/" rel="nofollow">http://podinfo:9898</a><br>这里运行了一个持续5分钟、QPS=10、并发数为2的请求。</p><p>hey命令详细参考如下：</p><p>Usage: hey [options...] <url></p><p>Options:<br>  -n  Number of requests to run. Default is 200.<br>  -c  Number of workers to run concurrently. Total number of requests cannot</p><pre><code>  be smaller than the concurrency level. Default is 50.</code></pre><p>-q  Rate limit, in queries per second (QPS) per worker. Default is no rate limit.<br>  -z  Duration of application to send requests. When duration is reached,</p><pre><code>  application stops and exits. If duration is specified, n is ignored.
  Examples: -z 10s -z 3m.</code></pre><p>-o  Output type. If none provided, a summary is printed.</p><pre><code>  "csv" is the only supported alternative. Dumps the response
  metrics in comma-separated values format.
</code></pre><p>-m  HTTP method, one of GET, POST, PUT, DELETE, HEAD, OPTIONS.<br>  -H  Custom HTTP header. You can specify as many as needed by repeating the flag.</p><pre><code>  For example, -H "Accept: text/html" -H "Content-Type: application/xml" .</code></pre><p>-t  Timeout for each request in seconds. Default is 20, use 0 for infinite.<br>  -A  HTTP Accept header.<br>  -d  HTTP request body.<br>  -D  HTTP request body from file. For example, /home/user/file.txt or ./file.txt.<br>  -T  Content-type, defaults to "text/html".<br>  -a  Basic authentication, username:password.<br>  -x  HTTP Proxy address as host:port.<br>  -h2 Enable HTTP/2.</p><p>-host HTTP Host header.</p><p>-disable-compression  Disable compression.<br>  -disable-keepalive    Disable keep-alive, prevents re-use of TCP</p><pre><code>                    connections between different HTTP requests.</code></pre><p>-disable-redirects    Disable following of HTTP redirects<br>  -cpus                 Number of used cpu cores.</p><pre><code>                    (default for current machine is 4 cores)</code></pre><p>2 自动扩容<br>执行如下命令观察扩容情况：</p><p>watch kubectl --kubeconfig $USER_CONFIG -n test get hpa/podinfo-total<br>结果如下：</p><p>Every 2.0s: kubectl --kubeconfig /Users/han/shop_config/ack_zjk -n test get hpa/podinfo                                            East6C16G: Tue Jan 26 18:01:30 2021</p><p>NAME      REFERENCE            TARGETS           MINPODS   MAXPODS   REPLICAS   AGE<br>podinfo   Deployment/podinfo   10056m/10 (avg)   1         5         2          4m45s<br>另外两个HPA类似，命令如下：</p><p>kubectl --kubeconfig $USER_CONFIG -n test get hpa</p><p>watch kubectl --kubeconfig $USER_CONFIG -n test get hpa/podinfo-latency-avg<br>watch kubectl --kubeconfig $USER_CONFIG -n test get hpa/podinfo-p95<br>3 监控指标<br>同时，我们可以实时在Prometheus中查看相关的应用级监控指标的实时数据。示意如下：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRoDX" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span><br><a href="https://developer.aliyun.com/article/783551?utm_content=g_1000264438" rel="nofollow">原文链接</a><br>本文为阿里云原创内容，未经允许不得转载。</p>  
</div>
            