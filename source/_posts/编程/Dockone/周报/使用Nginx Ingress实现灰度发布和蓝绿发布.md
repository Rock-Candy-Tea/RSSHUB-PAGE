
---
title: '使用Nginx Ingress实现灰度发布和蓝绿发布'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/a8659acf17737889fca63b09dadea311.png'
author: Dockone
comments: false
date: 2021-12-29 02:29:10
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/a8659acf17737889fca63b09dadea311.png'
---

<div>   
<br>Ingress基于七层的HTTP和HTTPS协议进行转发，可以通过域名和路径对访问做到更细粒度的划分。Ingress作为kubernetes集群中一种独立的资源，需要通过创建它来制定外部访问流量的转发规则，并通过Ingress Controller将其分配到一个或多个Service中。Ingress Controller在不同厂商之间有着不同的实现方式，Kubernetes官方维护的Controller为Nginx Ingress。Nginx Ingress支持通过配置注解（Annotations）来实现不同场景下的发布和测试，可以满足灰度发布、蓝绿发布、A/B测试等业务场景。本文将介绍使用Nginx Ingress实现灰度发布和蓝绿发布的应用场景、用法详解及实践步骤。<br>
<h3>应用场景</h3>使用Nginx Ingress实现灰度发布适用场景主要取决于业务流量切分的策略，目前Nginx Ingress支持基于Header、Cookie和服务权重三种流量切分的策略，基于这三种策略可实现以下两种发布场景：<br>
<h4>场景一：切分部分用户流量到新版本</h4>假设线上已运行了一套对外提供七层服务的Service A，此时开发了一些新的特性，需要发布上线一个新的版本Service A'，但又不想直接替换原有的Service A，而是期望将Header中包含foo=bar或者Cookie中包含foo=bar的用户请求转发到新版本Service A'中。待运行一段时间稳定后，再逐步全量上线新版本，平滑下线旧版本。示意图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/a8659acf17737889fca63b09dadea311.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/a8659acf17737889fca63b09dadea311.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>场景二：切分一定比例的流量到新版本</h4>假设线上已运行了一套对外提供七层服务的Service B，此时修复了一些问题，需要发布上线一个新的版本Service B'，但又不想直接替换原有的Service B，而是期望将20%的流量切换到新版本Service B'中。待运行一段时间稳定后，再将所有的流量从旧版本切换到新版本中，平滑下线旧版本。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/2609843bd68904e9d6209ea649105b7f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/2609843bd68904e9d6209ea649105b7f.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>注解说明</h3>Nginx Ingress支持通过配置注解（Annotations）来实现不同场景下的发布和测试，可以满足灰度发布、蓝绿发布、A/B测试等业务场景。具体实现过程如下：为服务创建两个Ingress，一个为常规Ingress，另一个为带nginx.ingress.kubernetes.io/canary: "true"注解的Ingress，称为Canary Ingress；为Canary Ingress配置流量切分策略Annotation，两个Ingress相互配合，即可实现多种场景的发布和测试。Nginx Ingress的Annotation支持以下几种规则：<br>
<ul><li>nginx.ingress.kubernetes.io/canary-by-header，基1于Header的流量切分，适用于灰度发布。如果请求头中包含指定的header名称，并且值为“always”，就将该请求转发给Canary Ingress定义的对应后端服务。如果值为“never”则不转发，可用于回滚到旧版本。如果为其他值则忽略该annotation，并通过优先级将请求流量分配到其他规则。</li><li>nginx.ingress.kubernetes.io/canary-by-header-value，必须与canary-by-header一起使用，可自定义请求头的取值，包含但不限于“always”或“never”。当请求头的值命中指定的自定义值时，请求将会转发给Canary Ingress定义的对应后端服务，如果是其他值则忽略该annotation，并通过优先级将请求流量分配到其他规则。</li><li>nginx.ingress.kubernetes.io/canary-by-header-pattern，与8canary-by-header-value类似，唯一区别是该annotation用正则表达式匹配请求头的值，而不是某一个固定值。如果该annotation与canary-by-header-value同时存在，该annotation将被忽略。</li><li>nginx.ingress.kubernetes.io/canary-by-cookie，基于Cookie的流量切分，适用于灰度发布。与canary-by-header类似，该annotation用于cookie，仅支持“always”和“never”，无法自定义取值。</li><li>nginx.ingress.kubernetes.io/canary-weight，基于服务权重的流量切分，适用于蓝绿部署。表示Canary Ingress所分配流量的百分比，取值范围[0-100]。例如，设置为100，表示所有流量都将转发给Canary Ingress对应的后端服务。</li></ul><br>
<br><h3>操作说明</h3>1、文中的Kubernetes集群为华为云CCE所提供，与之关联的其他云服务也均来自华为云。<br>
<br>2、准备工作：<br>
<ul><li>使用Nginx Ingress实现灰度发布的集群，需安装nginx-ingress插件作为Ingress Controller，并且对外暴露统一的流量入口。</li><li>已上传Nginx镜像至容器镜像服务。为方便观测流量切分效果，Nginx镜像包含新旧两个版本，欢迎页分别为“Old Nginx”和“New Nginx”。</li></ul><br>
<br>3、资源创建方式说明：本文提供以下两种方式使用YAML部署Deployment和Service：<br>
<ul><li>方式1：在控制台创建无状态工作负载向导页面，单击右侧“YAML创建”，再将本文示例的YAML文件内容输入编辑窗中。</li><li>方式2：将本文的示例YAML保存为文件，再使用kubectl指定YAML文件进行创建。例如：kubectl create -f xxx.yaml。</li></ul><br>
<br><h3>部署两个版本的服务</h3>在集群中部署两个版本的Nginx服务，并通过Nginx Ingress对外提供七层域名访问。<br>
<br><strong>步骤1</strong>：创建第一个版本的Deployment和Service，本文以old-nginx为例。YAML示例如下：<br>
<pre class="prettyprint">apiVersion: apps/v1 <br>
kind: Deployment <br>
metadata: <br>
name: old-nginx <br>
spec: <br>
replicas: 2 <br>
selector: <br>
matchLabels: <br>
  app: old-nginx <br>
template: <br>
metadata: <br>
  labels: <br>
    app: old-nginx <br>
spec: <br>
  containers: <br>
  - image: swr.cn-east-3.myhuaweicloud.com/hwfstaff_pub_cbuinfo/nginx:old    # 容器使用的镜像为：nginx:old <br>
    name: container-0 <br>
    resources: <br>
      limits: <br>
        cpu: 100m <br>
        memory: 200Mi <br>
      requests: <br>
        cpu: 100m <br>
        memory: 200Mi <br>
  imagePullSecrets: <br>
  - name: default-secret <br>
<br>
--- <br>
<br>
apiVersion: v1 <br>
kind: Service <br>
metadata: <br>
name: old-nginx <br>
spec: <br>
selector: <br>
app: old-nginx <br>
ports: <br>
- name: service0 <br>
targetPort: 80 <br>
port: 8080 <br>
protocol: TCP <br>
type: NodePort<br>
</pre><br>
<strong>步骤2</strong>：创建第二个版本的Deployment和Service，本文以new-nginx为例。YAML示例如下：<br>
<pre class="prettyprint">apiVersion: apps/v1 <br>
kind: Deployment <br>
metadata: <br>
name: new-nginx <br>
spec: <br>
replicas: 2 <br>
selector: <br>
matchLabels: <br>
  app: new-nginx <br>
template: <br>
metadata: <br>
  labels: <br>
    app: new-nginx <br>
spec: <br>
  containers: <br>
  - image: swr.cn-east-3.myhuaweicloud.com/hwfstaff_pub_cbuinfo/nginx:new    # 容器使用的镜像为：nginx:new <br>
    name: container-0 <br>
    resources: <br>
      limits: <br>
        cpu: 100m <br>
        memory: 200Mi <br>
      requests: <br>
        cpu: 100m <br>
        memory: 200Mi <br>
  imagePullSecrets: <br>
  - name: default-secret <br>
<br>
--- <br>
<br>
apiVersion: v1 <br>
kind: Service <br>
metadata: <br>
name: new-nginx <br>
spec: <br>
selector: <br>
app: new-nginx <br>
ports: <br>
- name: service0 <br>
targetPort: 80 <br>
port: 8080 <br>
protocol: TCP <br>
type: NodePort<br>
</pre><br>
你可以登录云容器引擎控制台，在“工作负载 > 无状态负载 Deployment”页面查看部署情况。<br><br>
【1】<br>
<strong>步骤3</strong>：创建Ingress，对外暴露服务，指向old版本的服务。YAML示例如下：<br>
<pre class="prettyprint">apiVersion: networking.k8s.io/v1beta1 <br>
kind: Ingress <br>
metadata: <br>
name: gray-release <br>
namespace: default <br>
annotations: <br>
kubernetes.io/ingress.class: nginx    # 使用Nginx型Ingress <br>
kubernetes.io/elb.port: '80' <br>
spec: <br>
rules: <br>
- host: www.example.com <br>
  http: <br>
    paths: <br>
      - path: '/' <br>
        backend: <br>
          serviceName: old-nginx      # 指定后端服务为old-nginx <br>
          servicePort: 80<br>
</pre><br>
执行以下命令，进行访问验证。<br><br>
<pre class="prettyprint">curl -H "Host: www.example.com"  http://<EXTERNAL_IP><br>
</pre><br>
其中，为Nginx Ingress对外暴露的IP。<br>
<br>预期输出：<br>
<pre class="prettyprint">Old Nginx<br>
</pre><br>
----结束<br>
<h3>灰度发布新版本服务</h3>设置访问新版本服务的流量切分策略。云容器引擎CCE支持设置基于Header、Cookie和服务权重三种策略，来实现灰度发布和蓝绿发布，你可以根据实际情况进行选择：<br>
<br>基于Header、Cookie和服务权重三种流量切分策略均可实现灰度发布；基于服务权重的流量切分策略，调整新服务权重为100%，即可实现蓝绿发布。你可以在下述示例中了解具体使用方法。<br>
<h4>基于Header的流量切分</h4>以下示例仅Header中包含Region且值为bj或gz的请求才能转发到新版本服务，模拟灰度新版本给北京和广州地域的用户。<br>
<br>创建Canary Ingress，指向新版本的后端服务，并增加annotation。<br>
<pre class="prettyprint">apiVersion: networking.k8s.io/v1beta1 <br>
kind: Ingress <br>
metadata: <br>
name: canary-ingress <br>
namespace: default <br>
annotations: <br>
kubernetes.io/ingress.class: nginx <br>
nginx.ingress.kubernetes.io/canary: "true"                       # 启用Canary <br>
nginx.ingress.kubernetes.io/canary-by-header: "Region" <br>
nginx.ingress.kubernetes.io/canary-by-header-pattern: "bj|gz"    # Header中包含Region且值为bj或gz的请求转发到Canary Ingress <br>
kubernetes.io/elb.port: '80' <br>
spec: <br>
rules: <br>
- host: www.example.com <br>
  http: <br>
    paths: <br>
      - path: '/' <br>
        backend: <br>
          serviceName: new-nginx      # 指定后端服务为new-nginx <br>
          servicePort: 80<br>
</pre><br>
执行以下命令，进行访问测试。<br>
<pre class="prettyprint">$ curl -H "Host: www.example.com" -H "Region: bj" http://<EXTERNAL_IP> <br>
New Nginx <br>
$ curl -H "Host: www.example.com" -H "Region: sh" http://<EXTERNAL_IP> <br>
Old Nginx <br>
$ curl -H "Host: www.example.com" -H "Region: gz" http://<EXTERNAL_IP> <br>
New Nginx <br>
$ curl -H "Host: www.example.com" http://<EXTERNAL_IP> <br>
Old Nginx<br>
</pre><br>
其中，为Nginx Ingress对外暴露的IP。<br>
<br>可以看出，仅当Header中包含Region且值为bj或gz的请求才由新版本服务响应。<br>
<h4>基于Cookie的流量切分</h4>以下示例仅Cookie中包含user_from_bj的请求才能转发到新版本服务，模拟灰度新版本给北京地域的用户。  <br>
<br>创建Canary Ingress，指向新版本的后端服务，并增加annotation。<br>
<pre class="prettyprint">apiVersion: networking.k8s.io/v1beta1 <br>
kind: Ingress <br>
metadata: <br>
name: canary-ingress <br>
namespace: default <br>
annotations: <br>
kubernetes.io/ingress.class: nginx <br>
nginx.ingress.kubernetes.io/canary: "true"                      # 启用Canary <br>
nginx.ingress.kubernetes.io/canary-by-cookie: "user_from_bj"    # Cookie中包含user_from_bj的请求转发到Canary Ingress <br>
kubernetes.io/elb.port: '80' <br>
spec: <br>
rules: <br>
- host: www.example.com <br>
  http: <br>
    paths: <br>
      - path: '/' <br>
        backend: <br>
          serviceName: new-nginx      # 指定后端服务为new-nginx <br>
          servicePort: 80<br>
</pre><br>
执行以下命令，进行访问测试。<br>
<pre class="prettyprint">$ curl -s -H "Host: www.example.com" --cookie "user_from_bj=always" http://<EXTERNAL_IP> <br>
New Nginx <br>
$ curl -s -H "Host: www.example.com" --cookie "user_from_gz=always" http://<EXTERNAL_IP> <br>
Old Nginx <br>
$ curl -s -H "Host: www.example.com" http://<EXTERNAL_IP> <br>
Old Nginx<br>
</pre><br>
其中，为Nginx Ingress对外暴露的IP。  <br>
<br>可以看出，仅当Cookie中包含user_from_bj且值为always的请求才由新版本服务响应。<br>
<h4>基于服务权重的流量切分</h4><strong>示例1</strong>：仅允许20%的流量被转发到新版本服务中，实现灰度发布。<br>
<br>创建Canary Ingress，并增加annotation，将20%的流量导入新版本的后端服务。<br>
<pre class="prettyprint">apiVersion: networking.k8s.io/v1beta1 <br>
kind: Ingress <br>
metadata: <br>
name: canary-ingress <br>
namespace: default <br>
annotations: <br>
kubernetes.io/ingress.class: nginx <br>
nginx.ingress.kubernetes.io/canary: "true"         # 启用Canary <br>
nginx.ingress.kubernetes.io/canary-weight: "20"    # 将20%的流量转发到Canary Ingress <br>
kubernetes.io/elb.port: '80' <br>
spec: <br>
rules: <br>
- host: www.example.com <br>
  http: <br>
    paths: <br>
      - path: '/' <br>
        backend: <br>
          serviceName: new-nginx      # 指定后端服务为new-nginx <br>
          servicePort: 80<br>
</pre><br>
执行以下命令，进行访问测试。<br>
<pre class="prettyprint">$ for i in &#123;1..20&#125;; do curl -H "Host: www.example.com" http://<EXTERNAL_IP>; done; <br>
Old Nginx <br>
Old Nginx <br>
Old Nginx <br>
New Nginx <br>
Old Nginx <br>
New Nginx <br>
Old Nginx <br>
New Nginx <br>
Old Nginx <br>
Old Nginx <br>
Old Nginx <br>
Old Nginx <br>
Old Nginx <br>
New Nginx <br>
Old Nginx <br>
Old Nginx <br>
Old Nginx <br>
Old Nginx <br>
Old Nginx <br>
Old Nginx<br>
</pre><br>
其中，为Nginx Ingress对外暴露的IP。<br>
<br>可以看出，有4/20的几率由新版本服务响应，符合20%服务权重的设置。<br>
<br><strong>示例2</strong>：允许所有的流量被转发到新版本服务中，实现蓝绿发布。<br>
<br>创建Canary Ingress，并增加annotation，将100%的流量导入新版本的后端服务。<br>
<pre class="prettyprint">apiVersion: networking.k8s.io/v1beta1 <br>
kind: Ingress <br>
metadata: <br>
name: canary-ingress <br>
namespace: default <br>
annotations: <br>
kubernetes.io/ingress.class: nginx <br>
nginx.ingress.kubernetes.io/canary: "true"          # 启用Canary <br>
nginx.ingress.kubernetes.io/canary-weight: "100"    # 所有流量均转发到Canary Ingress <br>
kubernetes.io/elb.port: '80' <br>
spec: <br>
rules: <br>
- host: www.example.com <br>
  http: <br>
    paths: <br>
      - path: '/' <br>
        backend: <br>
          serviceName: new-nginx      # 指定后端服务为new-nginx <br>
          servicePort: 80<br>
</pre><br>
执行以下命令，进行访问测试。<br>
<pre class="prettyprint">$ for i in &#123;1..10&#125;; do curl -H "Host: www.example.com" http://<EXTERNAL_IP>; done; <br>
New Nginx <br>
New Nginx <br>
New Nginx <br>
New Nginx <br>
New Nginx <br>
New Nginx <br>
New Nginx <br>
New Nginx <br>
New Nginx <br>
New Nginx<br>
</pre><br>
其中，为Nginx Ingress对外暴露的IP。<br>
<br>可以看出，所有的访问均由新版本服务响应，成功实现了蓝绿发布。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/DhNq4Q4iagPna_tXCruxfg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/DhNq4Q4iagPna_tXCruxfg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            