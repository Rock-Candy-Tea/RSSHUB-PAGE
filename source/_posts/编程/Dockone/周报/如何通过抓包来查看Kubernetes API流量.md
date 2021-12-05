
---
title: '如何通过抓包来查看Kubernetes API流量'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211205/f5c152f99ab758d916a179a11a454233.png'
author: Dockone
comments: false
date: 2021-12-05 12:11:51
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211205/f5c152f99ab758d916a179a11a454233.png'
---

<div>   
<br>当我们通过kubectl来查看、修改Kubernetes资源时，有没有想过后面的接口到底是怎样的？有没有办法探查这些交互数据呢？<br>
<br>Kuberenetes客户端和服务端交互的接口，是基于http协议的。所以只需要能够捕捉并解析https流量，我们就能看到kubernetes的API流量。<br>
<br>但是由于kubenetes使用了客户端私钥来实现对客户端的认证，所以抓包配置要复杂一点。具体是如下的结构：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211205/f5c152f99ab758d916a179a11a454233.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211205/f5c152f99ab758d916a179a11a454233.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><em>如果想了解更多Kubernetes证书的知识，可以看下<a href="https://qingwave.github.io/k8s-tls/">这篇Kubernetes证书解析的文章</a></em><br>
<h3>从kubeconfig中提取出客户端证书和私钥</h3>kubeconfig中包含了客户端的证书和私钥，我们首先要把它们提取出来：<br>
<pre class="prettyprint"># 提取出客户端证书  <br>
grep client-certificate-data ~/.kube/config | \  <br>
awk '&#123; print $2 &#125;' | \  <br>
base64 --decode > client-cert.pem  <br>
# 提取出客户端私钥  <br>
grep client-key-data ~/.kube/config | \  <br>
awk '&#123; print $2 &#125;' | \  <br>
base64 --decode > client-key.pem  <br>
# 提取出服务端CA证书  <br>
grep certificate-authority-data ~/.kube/config | \  <br>
awk '&#123; print $2 &#125;' | \  <br>
base64 --decode > cluster-ca-cert.pem  <br>
</pre><br>
<em>参考自<a href="https://www.reddit.com/r/kubernetes/comments/h7wfnc/how_do_i_derive_certificate_pem_data_from/">Reddit</a></em><br>
<h3>配置Charles代理软件</h3>从第一张图可以看出，代理软件的作用有两个：一是接收https流量并转发，二是转发到kubernetes apiserver的时候，使用指定的客户端私钥。<br>
<br>首先配置Charles，让他拦截所有的https流量：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211205/7c8feb9fc66960150e53c5d7721f76b2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211205/7c8feb9fc66960150e53c5d7721f76b2.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
然后配置客户端私钥，即对于发送到apiserver的请求，统一使用指定的客户端私钥进行认证：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211205/51aa393305be9e96f80816136360d1e6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211205/51aa393305be9e96f80816136360d1e6.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>配置kubectl</h3>需要抓包kubectl的流量，需要两个条件：1. kubectl使用Charles作为代理，2. kubectl需要信任Charles的证书。<br>
<pre class="prettyprint"># Charles的代理端口是8888，设置https_proxy环境变量，让kubectl使用Charles代理  <br>
$ export https_proxy=http://127.0.0.1:8888/  <br>
# insecure-skip-tls-verify表示不校验服务端证书  <br>
$ kubectl --insecure-skip-tls-verify get pod  <br>
NAME                    READY   STATUS    RESTARTS   AGE  <br>
sc-b-7f5dfb694b-xtfrz   2/2     Running   0          2d20h  <br>
</pre><br>
<br>我们就可以看到<code class="prettyprint">get pod</code>的网络请求了：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211205/880da51195d24fbc5702072aedc515cd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211205/880da51195d24fbc5702072aedc515cd.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到，get pod的endpoint是<code class="prettyprint">GET /api/v1/namespaces/&lt;namespace>/pods</code>。<br>
让我们再尝试下创建pod的请求：<br>
<pre class="prettyprint">$ cat <<EOF >pod.yaml  <br>
apiVersion: v1  <br>
kind: Pod  <br>
metadata:  <br>
name: nginx-robberphex  <br>
spec:  <br>
containers:  <br>
- name: nginx  <br>
image: nginx:1.14.2  <br>
EOF  <br>
$ kubectl --insecure-skip-tls-verify apply -f pod.yaml  <br>
pod/nginx-robberphex created  <br>
</pre><br>
也同样可以抓到包：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211205/cb7ab74a3feec3d8bddb89a8cc9cf663.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211205/cb7ab74a3feec3d8bddb89a8cc9cf663.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
创建pod的endpoint是<code class="prettyprint">POST /api/v1/namespaces/&lt;namespace>/pods</code><br>
<h3>配置kubenetes client</h3>我们先从写一个用kubernetes go client来获取pod的例子（注意，代码中已经信任所有的证书，所以可以抓到包）：<br>
<pre class="prettyprint">package main  <br>
<br>
/*  <br>
require (  <br>
k8s.io/api v0.18.19  <br>
k8s.io/apimachinery v0.18.19  <br>
k8s.io/client-go v0.18.19  <br>
)  <br>
*/  <br>
import (  <br>
"context"  <br>
"flag"  <br>
"fmt"  <br>
"path/filepath"  <br>
<br>
apiv1 "k8s.io/api/core/v1"  <br>
metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"  <br>
"k8s.io/client-go/kubernetes"  <br>
"k8s.io/client-go/tools/clientcmd"  <br>
"k8s.io/client-go/util/homedir"  <br>
)  <br>
<br>
func main() &#123;  <br>
ctx := context.Background()  <br>
var kubeconfig *string  <br>
if home := homedir.HomeDir(); home != "" &#123;  <br>
kubeconfig = flag.String("kubeconfig", filepath.Join(home, ".kube", "config"), "(optional) absolute path to the kubeconfig file")  <br>
&#125; else &#123;  <br>
kubeconfig = flag.String("kubeconfig", "", "absolute path to the kubeconfig file")  <br>
&#125;  <br>
flag.Parse()  <br>
<br>
config, err := clientcmd.BuildConfigFromFlags("", *kubeconfig)  <br>
if err != nil &#123;  <br>
panic(err)  <br>
&#125;  <br>
// 让clientset信任所有证书  <br>
config.TLSClientConfig.CAData = nil  <br>
config.TLSClientConfig.Insecure = true  <br>
clientset, err := kubernetes.NewForConfig(config)  <br>
if err != nil &#123;  <br>
panic(err)  <br>
&#125;  <br>
podClient := clientset.CoreV1().Pods(apiv1.NamespaceDefault)  <br>
podList, err := podClient.List(ctx, metav1.ListOptions&#123;&#125;)  <br>
if err != nil &#123;  <br>
panic(err)  <br>
&#125;  <br>
<br>
for _, pod := range podList.Items &#123;  <br>
fmt.Printf("podName: %s\n", pod.Name)  <br>
&#125;  <br>
<br>
fmt.Println("done!")  <br>
&#125; <br>
</pre><br>
然后编译执行：<br>
<pre class="prettyprint">$ go build -o kube-client  <br>
$ export https_proxy=http://127.0.0.1:8888/  <br>
$ ./kube-client  <br>
podName: nginx-robberphex  <br>
podName: sc-b-7f5dfb694b-xtfrz  <br>
done!  <br>
</pre><br>
这时也可以抓到同样的结果：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211205/635198f1341090b85bf88968e8d7b3a1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211205/635198f1341090b85bf88968e8d7b3a1.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
基于此，我们就可以分析一个Kubernetes到底干了什么，也是我们分析Kubernetes​实现的入口。<br>
<br>原文链接：<a href="https://robberphex.com/how-to-inspect-kubernetes-api/" rel="nofollow" target="_blank">https://robberphex.com/how-to- ... -api/</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            