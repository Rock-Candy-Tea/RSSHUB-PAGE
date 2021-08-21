
---
title: '一篇文章看明白nginx-ingress控制器'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/0b81726417650eaec4d0a9c53accf466.png'
author: Dockone
comments: false
date: 2021-08-21 07:07:53
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/0b81726417650eaec4d0a9c53accf466.png'
---

<div>   
<br><h3>主机Nginx</h3>一般Nginx做主机反向代理（网关）有以下配置：<br>
<pre class="prettyprint">upstream order&#123;<br>
server 192.168.1.10:5001;<br>
server 192.168.1.11:5001;<br>
&#125;<br>
<br>
server &#123;<br>
listen 80;<br>
server_name  order.example.com;<br>
access_log     /var/log/nginx/order.example.com-access.log;<br>
error_log     /var/log/nginx/order.example.com-error.log;<br>
location / &#123;<br>
    proxy_pass_header Server;<br>
    proxy_set_header Host $http_host;<br>
    proxy_set_header X-Real-IP $remote_addr;<br>
    proxy_set_header X-Scheme $scheme;<br>
    proxy_pass http://order;<br>
&#125;<br>
&#125; <br>
</pre><br>
其中<code class="prettyprint">192.168.1.10:5001</code>，<code class="prettyprint">192.168.1.10:5001</code>我们把他们称为Endpoint，就是所谓的具体的服务，比如order订单服务。<br>
<h3>Pod nginx-ingress</h3>nginx-ingress也是一种代理，是一个Pod，外部的数据统一经过（必经）这个Pod，然后通过该Pod内部的Nginx方向代理到各个服务（Endpoint）。nginx-ingress是Ingress控制器插件的一种，这些插件有很多，比如istio-ingressgateway。<br>
<h4>Pod</h4>nginx-ingress Pod有两个功能，Controller和Nginx：<br>
<ul><li>Controller：和Kubernetes API通讯实时更新Nginx配置（就是ingress yaml资源了）</li><li>Nginx：正常的反向代理</li></ul><br>
<br>与主机Nginx的区别是，该Pod nginx-ingress是运行在Pod里。主机在定义反向代理配置文件时，需要监听一个对外开放的端口，比如上边的80端口。那么Pod中的Nginx端口是如何配置的呢？  <br>
<br>我们在GitHub上找到了nginx-ingress的deployment.yaml：<br>
<br><a href="https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/mandatory.yaml" rel="nofollow" target="_blank">https://raw.githubusercontent. ... .yaml</a><br>
<br>其中一段：<br>
<pre class="prettyprint">apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
name: nginx-ingress-controller<br>
namespace: ingress-nginx<br>
labels:<br>
app.kubernetes.io/name: ingress-nginx<br>
app.kubernetes.io/part-of: ingress-nginx<br>
spec:<br>
replicas: 1<br>
selector:<br>
matchLabels:<br>
  app.kubernetes.io/name: ingress-nginx<br>
  app.kubernetes.io/part-of: ingress-nginx<br>
template:<br>
metadata:<br>
  labels:<br>
    app.kubernetes.io/name: ingress-nginx<br>
    app.kubernetes.io/part-of: ingress-nginx<br>
  annotations:<br>
    prometheus.io/port: "10254"<br>
    prometheus.io/scrape: "true"<br>
spec:<br>
  # wait up to five minutes for the drain of connections<br>
  terminationGracePeriodSeconds: 300<br>
  serviceAccountName: nginx-ingress-serviceaccount<br>
  containers:<br>
    - name: nginx-ingress-controller<br>
      image: quay.io/kubernetes-ingress-controller/nginx-ingress-controller:0.26.1<br>
      ...<br>
      ...<br>
      ...<br>
      ports:<br>
        - name: http<br>
          containerPort: 80<br>
        - name: https<br>
          containerPort: 443<br>
</pre><br>
我们看到：<br>
<pre class="prettyprint">- name: http<br>
containerPort: 80<br>
- name: https<br>
containerPort: 443<br>
</pre><br>
默认对外监听了两个端口80和443，也就是说，有这两个端口对外就可以Web服务了。<br>
<h4>Ingress资源</h4>Ingress资源通过yaml进行管理的，比如以下：<br>
<pre class="prettyprint">apiVersion: extensions/v1beta1<br>
kind: Ingress<br>
metadata:<br>
name: order<br>
spec: <br>
rules:<br>
- host: order.example.com<br>
http:<br>
  paths: /<br>
  backend: <br>
    serviceName: order<br>
    servicePort: 80<br>
</pre><br>
以上我们定义了一个单一规则的Ingress，该Pod（nginx-ingress）接收到外部所有的请求，将被发送到内部order服务的80端口上。接下来我们看Pod（nginx-ingress）如何把Ingress资源转化为该Pod中的Nginx反向代理配置文件。<br>
<pre class="prettyprint">upstream order&#123;<br>
server order:80;<br>
&#125;<br>
<br>
server &#123;<br>
listen 80;<br>
server_name  order.example.com;<br>
...<br>
...<br>
location / &#123;<br>
    proxy_pass_header Server;<br>
    proxy_set_header Host $http_host;<br>
    proxy_set_header X-Real-IP $remote_addr;<br>
    proxy_set_header X-Scheme $scheme;<br>
    proxy_pass http://order; # 对应ingress 资源 name: order<br>
&#125;<br>
&#125; <br>
</pre><br>
当然Ingress如果包含https，那么会转化Nginx对应的443端口及证书的配置文件内容，这里就不写了。<br>
<br><blockquote><br>那么，单一个规则的Ingress资源代理多个服务（比如order服务，product服务）或者多个Ingress资源文件如何转化为Nginx配置？ 猜测，其实就是转化成了多个。</blockquote><pre class="prettyprint">upstream order&#123;<br>
server order:80;<br>
&#125; <br>
</pre><br>
当然，被转化的nginx配置文件要比这些复杂的多，据说还是用lua脚本写的，灵活如openresty。<br>
<h4>nginx-ingress对外提供服务</h4>一般来讲，Pod直接对外提供服务就只有两种方式：<br>
<ul><li>create一个service，该service暴漏nodePort</li><li>forward映射</li></ul><br>
<br>我们一般采用第一种。  <br>
<br>nginx-ingress也是一个Pod，所以，为了能使外部通过该Pod代理访问，还需要nginx-ingress对外提供一个nodePort的Service。这个Service这里也不再写了。<br>
<h4>nginx-ingress工作流程</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/0b81726417650eaec4d0a9c53accf466.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/0b81726417650eaec4d0a9c53accf466.png" class="img-polaroid" title="16d9afd9301961e2~tplv-t2oaga2asx-watermark.image_.png" alt="16d9afd9301961e2~tplv-t2oaga2asx-watermark.image_.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们可以看到，因为nginx-ingress这个Pod做了所有Service的代理，在高并发情况下将承受巨大压力，我们可以增加多个Pod实例。<br>
<br>链接：<a href="https://juejin.cn/post/6844903957479817230" rel="nofollow" target="_blank">https://juejin.cn/post/6844903957479817230</a>，作者：dakesolo
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            