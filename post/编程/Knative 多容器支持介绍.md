
---
title: Knative 多容器支持介绍
categories: 
    - 编程
    - segmentfault - 用户
author: segmentfault - 用户
comments: false
date: 2021-03-21 16:41:00
thumbnail: https://segmentfault.com/img/remote/1460000039674778
---

<div>   
<p>微服务和容器化带来了将应用程序分解成可重复使用的小型单元的诉求，这些单元通常作为单独的进程运行，或者在单独的容器运行。 Kubernetes的Pod模型允许用户创建一个部署单元，该单元可以打包多个容器作为应用程序的单个实例。</p><p>Knative 用户当前同样存在将多个容器部署到一个Pod中对诉求。支持多个容器的能力将有利于把更广泛的工作负载部署到Knative Serving模型中。因此 Knative 从 0.16.0 版本开始提供多个容器的能力。</p><h2>多容器支持</h2><p><strong>单容器介绍</strong></p><p>Knative 0.16.0之前的版本，仅支持设置一个业务容器，也就是在Knative Service中只能设置一个容器。在服务创建的过程中，会默认在POD中加上一个 QUEUE 容器，该容器主要用户接管入口流量，用于基于流量的KPA指标收集。典型的一个Knative Service 如下：</p><pre><code class="text">apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: helloworld-go
spec:
  template:
    spec:
      containers:
      - image: registry.cn-hangzhou.aliyuncs.com/knative-sample/helloworld-go:73fbdd56
        env:
        - name: TARGET
          value: "Knative"</code></pre><p>创建完成运行中POD示意图如下：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039674778" alt title referrerpolicy="no-referrer"></span></p><p>如果我们想要加上一个自定义的SideCar容器(一般用于网络互通，文件下载拷贝等辅助功能)，是没有办法去支持的，也就限制了实际的使用场景。</p><p><strong>多容器介绍</strong></p><p>Knative 从 0.16.0 版本开始也支持了多容器（没什么好说的，k8s pod天然的特性必须要支持）</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039674777" alt title referrerpolicy="no-referrer"></span></p><p>那么如何使用多容器呢？很简单，其实就是在containers属性中配置多个即可，示例如下：</p><pre><code class="text">apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: multi-container
  namespace: default
spec:
  template:
    spec:
      containers:
      - image: docker.io/savita3020/servingcontainer
        ports:
          - containerPort: 8881
      - image: docker.io/savita3020/sidecarcontainer</code></pre><p><strong>开启多容器特性</strong></p><ul><li>阿里云 Knative v0.18.3 已经默认开启。</li><li>社区 Knative 0.16.0 默认未开启, 从0.17.0 开始默认开启，执行下面操作可查看是否开启：</li></ul><pre><code class="text">$ kubectl -n knative-serving get configmap config-features -oyaml
 ......
 multi-container: "enabled"
 ......</code></pre><h2>多容器实践</h2><p><strong>前提条件</strong></p><ul><li>创建Kubernetes托管版集群</li><li>一键部署Knative</li></ul><p><strong>创建服务</strong></p><p>接下来我们创建多容器的一个服务，该服务包括两个容器：</p><ul><li>servingcontainer 容器</li><li>sidecarcontainer 容器</li></ul><p>servingcontainer调用sidecarcontainer， 示例代码如下：</p><pre><code class="text">package main   
import (
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
)
func handler(w http.ResponseWriter, r *http.Request) {
    log.Println("serving container received a request.")
    res, err := http.Get("http://127.0.0.1:8882")
    if err != nil {
        log.Fatal(err)
    }
    resp, err := ioutil.ReadAll(res.Body)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Fprintln(w, string(resp))
}
func main() {
    log.Print("serving container started...")
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8881", nil))
}</code></pre><p>sidecarcontainer 容器用于打印信息“Yay!! multi-container works”，示例代码如下：</p><pre><code class="text">package main
import (
    "fmt"
    "log"
    "net/http"
)
func handler(w http.ResponseWriter, r *http.Request) {
    log.Println("sidecar container received a request.")
    fmt.Fprintln(w, "Yay!! multi-container works")
}
func main() {
    log.Print("sidecar container started...")
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8882", nil))
}</code></pre><p>我们创建multi-container的服务</p><pre><code class="text">apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: multi-container
  namespace: default
spec:
  template:
    spec:
      containers:
      - image: registry.cn-hangzhou.aliyuncs.com/knative-sample/servingcontainer:v1
        ports:
          - containerPort: 8881
      - image: registry.cn-hangzhou.aliyuncs.com/knative-sample/sidecarcontainer:v1</code></pre><p>执行部署命令：</p><pre><code class="text">kubectl apply -f multi-container.yaml</code></pre><p>查看pod信息，发现一个 3 个容器（queue容器、servingcontainer 容器、sidecarcontainer 容器）：</p><pre><code class="text">richard@B-N3TEMD6P-1650 multi-container % kubectl get po
NAME                                                READY   STATUS    RESTARTS   AGE
multi-container-dfqtv-deployment-799c4f694c-bkc8t   3/3     Running   0          9s</code></pre><p>访问服务：</p><pre><code class="text">richard@B-N3TEMD6P-1650 multi-container % curl -H "host: multi-container.default.example.com" http://182.92.208.172
Yay!! multi-container works</code></pre><p>我们可以看到多容器访问已经生效。</p><h2>总结</h2><p>本文介绍了从 Knative 0.16.0 版本支持的多容器特性，以及如何在Knative Service 中使用多个容器。</p><p><strong><a href="https://link.zhihu.com/?target=https%3A//developer.aliyun.com/article/782390%3Futm_content%3Dg_1000254188" rel="nofollow">原文链接</a></strong></p><p>本文为阿里云原创内容，未经允许不得转载。</p>  
</div>
            