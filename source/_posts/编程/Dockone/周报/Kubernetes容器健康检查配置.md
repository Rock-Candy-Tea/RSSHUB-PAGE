
---
title: 'Kubernetes容器健康检查配置'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=6341'
author: Dockone
comments: false
date: 2021-08-11 05:07:06
thumbnail: 'https://picsum.photos/400/300?random=6341'
---

<div>   
<br><h3>简介</h3>此文讲述如何配置容器的<code class="prettyprint">Liveness</code>、<code class="prettyprint">Readiness</code>、<code class="prettyprint">Startup</code>探针。<br>
<br><code class="prettyprint">kubelet</code>使用<code class="prettyprint">Liveness</code>探测器来知道什么时候要重启容器。例如，<code class="prettyprint">Liveness</code>探测器可以捕捉到死锁（应用程序在运行，但是无法继续执行后面的步骤）。这样的情况下重启容器有助于让应用程序在有问题的情况下更可用。<br>
<br><code class="prettyprint">kubelet</code>使用<code class="prettyprint">Readiness</code>探测器可以知道容器什么时候准备好了并可以开始接受请求流量， 当一个Pod内的所有容器都准备好了，才能把这个Pod看作就绪了。这种信号的一个用途就是控制哪个Pod作为Service的后端。在Pod还没有准备好的时候，会从Service的负载均衡器中被剔除的。<br>
<br><code class="prettyprint">kubelet</code>使用<code class="prettyprint">Startup</code>探测器可以知道应用程序容器什么时候启动了。如果配置了这类探测器，就可以控制容器在启动成功后再进行<code class="prettyprint">Liveness</code>和<code class="prettyprint">Readiness</code>检查，确保这些存活、就绪探测器不会影响应用程序的启动。这可以用于对慢启动容器进行存活性检测，避免它们在启动运行之前就被杀掉。<br>
<h3>定义一个Liveness探针</h3>许多长时间运行的应用程序最终会过渡到断开的状态，除非重新启动，否则无法恢复。Kubernetes提供了<code class="prettyprint">Liveness</code>探测器来发现并补救这种情况。<br>
<br>创建一个Pod，其中运行一个基于<code class="prettyprint">k8s.gcr.io/busybox</code>镜像的容器。配置文件如下。文件名：<code class="prettyprint">exec-liveness.yaml</code><br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Pod<br>
metadata:<br>
labels:<br>
test: liveness<br>
name: liveness-exec<br>
spec:<br>
containers:<br>
- name: liveness<br>
image: k8s.gcr.io/busybox<br>
args:<br>
- /bin/sh<br>
- -c<br>
- touch /tmp/healthy; sleep 30; rm -rf /tmp/healthy; sleep 600<br>
livenessProbe:<br>
  exec:<br>
    command:<br>
    - cat<br>
    - /tmp/healthy<br>
  initialDelaySeconds: 5<br>
  periodSeconds: 5<br>
</pre><br>
在配置文件中，可以看到Pod中只有一个容器。<code class="prettyprint">periodSeconds</code>字段指定了kubelet应该每5秒执行一次存活检测。<code class="prettyprint">initialDelaySeconds</code>字段告诉<code class="prettyprint">kubelet</code>在执行第一次探针前应该等待5秒。kubelet在容器中执行命令<code class="prettyprint">cat /tmp/healthy</code>来进行检测。如果命令执行成功并且返回值为0，kubelet会认为这个容器是健康存活的。如果这个命令返回非0值，kubelet会杀死这个容器并重新启动它。执行命令如下：<br>
<pre class="prettyprint">/bin/sh -c "touch /tmp/healthy; sleep 30; rm -rf /tmp/healthy; sleep 600"<br>
</pre><br>
这个容器生命的前30秒，<code class="prettyprint">/tmp/healthy</code>文件是存在的。执行命令<code class="prettyprint">cat /tmp/healthy</code>会返回成功码。30秒后，执行命令<code class="prettyprint">cat /tmp/healthy</code>就回返回失败码。<br>
<br>创建Pod：<br>
<pre class="prettyprint"># kubectl apply -f /root/k8s-example/probe/exec-liveness.yaml<br>
</pre><br>
在 30 秒内，查看Pod的事件：<br>
<pre class="prettyprint">kubectl describe pod liveness-exec<br>
</pre><br>
输出结果显示还没有存活探测器失败：<br>
<pre class="prettyprint">Events:<br>
Type    Reason     Age        From                 Message<br>
----    ------     ----       ----                 -------<br>
Normal  Scheduled  <unknown>  default-scheduler    Successfully assigned default/liveness-exec to k8s-node04<br>
Normal  Pulled     22s        kubelet, k8s-node04  Container image "k8s.gcr.io/busybox" already present on machine<br>
Normal  Created    22s        kubelet, k8s-node04  Created container liveness<br>
Normal  Started    22s        kubelet, k8s-node04  Started container liveness<br>
</pre><br>
30秒之后，再来看Pod的事件：<br>
<pre class="prettyprint">kubectl describe pod liveness-exec<br>
</pre><br>
在输出结果的最下面，有信息显示存活探测器失败了，这个容器被杀死并且被重建了。<br>
<pre class="prettyprint">Events:<br>
Type     Reason     Age               From                 Message<br>
----     ------     ----              ----                 -------<br>
Normal   Scheduled  <unknown>         default-scheduler    Successfully assigned default/liveness-exec to k8s-node04<br>
Normal   Pulled     47s               kubelet, k8s-node04  Container image "k8s.gcr.io/busybox" already present on machine<br>
Normal   Created    47s               kubelet, k8s-node04  Created container liveness<br>
Normal   Started    47s               kubelet, k8s-node04  Started container liveness<br>
Warning  Unhealthy  5s (x3 over 15s)  kubelet, k8s-node04  Liveness probe failed: cat: can't open '/tmp/healthy': No such file or directory<br>
Normal   Killing    5s                kubelet, k8s-node04  Container liveness failed liveness probe, will be restarted<br>
</pre><br>
再等另外30秒，检查看这个容器被重启了：<br>
<pre class="prettyprint">kubectl get pod liveness-exec<br>
NAME            READY   STATUS    RESTARTS   AGE<br>
liveness-exec   1/1     Running   2          3m10s<br>
</pre><br>
再查看Pod资源详情：<br>
<pre class="prettyprint">kubectl describe pod liveness-exec<br>
</pre><br>
输出结果如下，容器重启成功。<br>
<pre class="prettyprint">Events:<br>
Type     Reason     Age                 From                 Message<br>
----     ------     ----                ----                 -------<br>
Normal   Scheduled  <unknown>           default-scheduler    Successfully assigned default/liveness-exec to k8s-node04<br>
Warning  Unhealthy  35s (x6 over 2m)    kubelet, k8s-node04  Liveness probe failed: cat: can't open '/tmp/healthy': No such file or directory<br>
Normal   Killing    35s (x2 over 110s)  kubelet, k8s-node04  Container liveness failed liveness probe, will be restarted<br>
Normal   Pulled     5s (x3 over 2m32s)  kubelet, k8s-node04  Container image "k8s.gcr.io/busybox" already present on machine<br>
Normal   Created    5s (x3 over 2m32s)  kubelet, k8s-node04  Created container liveness<br>
Normal   Started    5s (x3 over 2m32s)  kubelet, k8s-node04  Started container liveness<br>
</pre><br>
<h3>定义一个存活态HTTP请求接口</h3>另外一种类型的<code class="prettyprint">Liveness</code>探测方式是使用HTTP GET请求。下面是一个Pod的配置文件，其中运行一个基于<code class="prettyprint">k8s.gcr.io/liveness</code>镜像的容器。<br>
<br>创建Pod：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Pod<br>
metadata:<br>
labels:<br>
test: liveness<br>
name: liveness-http<br>
spec:<br>
containers:<br>
- name: liveness<br>
image: k8s.gcr.io/liveness<br>
args:<br>
- /server<br>
livenessProbe:<br>
  httpGet:<br>
    path: /healthz<br>
    port: 8080<br>
    httpHeaders:<br>
    - name: X-Custom-Header<br>
      value: Awesome<br>
  initialDelaySeconds: 3<br>
  periodSeconds: 3<br>
</pre><br>
配置文件中，Pod中只有一个容器。<code class="prettyprint">periodSeconds</code>字段指定了kubelet每隔3秒执行一次检测。<code class="prettyprint">initialDelaySeconds</code>字段告诉kubelet在执行第一次探测前应该等待3秒。kubelet 会向容器内运行的服务（服务会监听 8080 端口）发送一个 <code class="prettyprint">HTTP GET</code> 请求来执行探测。如果服务上<code class="prettyprint">/healthz</code>路径下的处理程序返回成功码。则kubelet认为容器是健康存活的。如果处理程序返回失败码，则kubelet会杀死这个容器并且重新启动它。<br>
<br>任何大于或等于200并且小于400的返回码标示成功，其它返回码都标示失败。<br>
<br>可以在这里看到服务的源码：<a href="https://github.com/kubernetes/kubernetes/blob/master/test/images/agnhost/liveness/server.go" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... er.go</a><br>
<br>容器存活的最开始10秒中，<code class="prettyprint">/healthz</code>处理程序返回一个200的状态码。之后处理程序返回500的状态码。<br>
<pre class="prettyprint">http.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request) &#123;<br>
duration := time.Now().Sub(started)<br>
if duration.Seconds() > 10 &#123;<br>
    w.WriteHeader(500)<br>
    w.Write([]byte(fmt.Sprintf("error: %v", duration.Seconds())))<br>
&#125; else &#123;<br>
    w.WriteHeader(200)<br>
    w.Write([]byte("ok"))<br>
&#125;<br>
&#125;)<br>
</pre><br>
kubelet在容器启动之后3秒开始执行健康检测。所以前几次健康检查都是成功的。但是10秒之后，健康检查会失败，并且kubelet会杀死容器再重新启动容器。<br>
<pre class="prettyprint"># kubectl apply -f /root/k8s-example/probe/http-liveness.yaml<br>
</pre><br>
10秒之后，通过看Pod事件来检测存活探测器已经失败了并且容器被重新启动了。<br>
<pre class="prettyprint">Events:<br>
Type     Reason     Age              From                 Message<br>
----     ------     ----             ----                 -------<br>
Normal   Scheduled  <unknown>        default-scheduler    Successfully assigned default/liveness-http to k8s-node01<br>
Normal   Pulled     17s              kubelet, k8s-node01  Container image "k8s.gcr.io/liveness" already present on machine<br>
Normal   Created    17s              kubelet, k8s-node01  Created container liveness<br>
Normal   Started    16s              kubelet, k8s-node01  Started container liveness<br>
Warning  Unhealthy  1s (x2 over 4s)  kubelet, k8s-node01  Liveness probe failed: HTTP probe failed with statuscode: 500<br>
</pre><br>
<h3>定义TCP的存活探测</h3>第三种类型的<code class="prettyprint">liveness</code>探测是使用TCP套接字。通过配置，kubelet会尝试在指定端口和容器建立套接字链接。如果能建立链接，这个容器就被看作是健康的，如果不能则这个容器就被看作是有问题的。<br>
<br>创建一个Pod。文件名：<code class="prettyprint">tcp-liveness-readiness.yaml</code><br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Pod<br>
metadata:<br>
name: goproxy<br>
labels:<br>
app: goproxy<br>
spec:<br>
containers:<br>
- name: goproxy<br>
image: k8s.gcr.io/goproxy:0.1<br>
ports:<br>
- containerPort: 8080<br>
readinessProbe:<br>
  tcpSocket:<br>
    port: 8080<br>
  initialDelaySeconds: 5<br>
  periodSeconds: 10<br>
livenessProbe:<br>
  tcpSocket:<br>
    port: 8080<br>
  initialDelaySeconds: 15<br>
  periodSeconds: 20<br>
</pre><br>
TCP检测的配置和HTTP检测非常相似。下面这个例子同时使用就绪和存活探测器。kubelet会在容器启动5秒后发送第一个就绪探测。这会尝试连接goproxy容器的8080端口。如果探测成功，这个Pod会被标记为就绪状态，kubelet将继续每隔10秒运行一次检测。<br>
<br>除了<code class="prettyprint">readiness</code>探测，这个配置包括了一个<code class="prettyprint">Liveness</code>探测。kubelet会在容器启动15秒后进行第一次<code class="prettyprint">Liveness</code>探测。就像<code class="prettyprint">Readiness</code>探测一样，会尝试连接goproxy容器的8080端口。如果存活探测失败，这个容器会被重新启动。<br>
<pre class="prettyprint"># kubectl apply -f /root/k8s-example/probe/tcp-liveness-readiness.yaml<br>
</pre><br>
15秒之后，通过看Pod事件来检测存活探测器：<br>
<pre class="prettyprint"># kubectl describe pod goproxy<br>
</pre><br>
使用命名端口：<br>
<br>对于HTTP或者TCP存活检测可以使用命名的容器端口。<br>
<pre class="prettyprint">ports:<br>
- name: liveness-port<br>
containerPort: 8080<br>
hostPort: 8080<br>
​<br>
livenessProbe:<br>
httpGet:<br>
path: /healthz<br>
port: liveness-port<br>
</pre><br>
<h3>使用Startup探测器保护慢启动容器</h3>有时候，会有一些现有的应用程序在启动时需要较多的初始化时间。要不影响对引起探测死锁的快速响应，这种情况下，设置<code class="prettyprint">Liveness</code>探测参数是要技巧的。技巧就是使用一个命令来设置<code class="prettyprint">Startup</code>探测，针对HTTP或者TCP检测，可以通过设置<code class="prettyprint">failureThreshold * periodSeconds</code>参数来保证有足够长的时间应对糟糕情况下的启动时间。<br>
<br>所以，前面的例子就变成了：<br>
<pre class="prettyprint">ports:<br>
- name: liveness-port<br>
containerPort: 8080<br>
hostPort: 8080<br>
​<br>
livenessProbe:<br>
httpGet:<br>
path: /healthz<br>
port: liveness-port<br>
failureThreshold: 1<br>
periodSeconds: 10<br>
​<br>
startupProbe:<br>
httpGet:<br>
path: /healthz<br>
port: liveness-port<br>
failureThreshold: 30<br>
periodSeconds: 10<br>
</pre><br>
幸亏有<code class="prettyprint">Startup</code>探测，应用程序将会有最多<code class="prettyprint">5分钟（30*10=300s）</code>的时间来完成它的启动。 一旦<code class="prettyprint">Startup</code>探测成功一次，存活探测任务就会接管对容器的探测，对容器死锁可以快速响应。 如果<code class="prettyprint">Startup</code>探测一直没有成功，容器会在300秒后被杀死，并且根据<code class="prettyprint">restartPolicy</code>来设置Pod状态。<br>
<h3>定义<code class="prettyprint">Readliness</code>探测器</h3>有时候，应用程序会暂时性的不能提供通信服务。例如，应用程序在启动时可能需要加载很大的数据或配置文件，或是启动后要依赖等待外部服务。在这种情况下，既不想杀死应用程序，也不想给它发送请求。Kubernetes提供了就绪探测器来发现并缓解这些情况。容器所在Pod上报还未就绪的信息，并且不接受通过<code class="prettyprint">Kubernetes Service</code>的流量。<br>
<br><blockquote><br>注意：就绪探测器在容器的整个生命周期中保持运行状态。</blockquote>就绪探测器的配置和存活探测器的配置相似。唯一区别就是要使用<code class="prettyprint">readinessProbe</code>字段，而不是<code class="prettyprint">LivenessProbe</code>字段。<br>
<pre class="prettyprint">readinessProbe:<br>
exec:<br>
command:<br>
- cat<br>
- /tmp/healthy<br>
initialDelaySeconds: 5<br>
periodSeconds: 5<br>
</pre><br>
HTTP和TCP的<code class="prettyprint">Readliness</code>探测器配置也和<code class="prettyprint">Liveness</code>探测器的配置一样的。<br>
<br><code class="prettyprint">Readliness</code>和<code class="prettyprint">Liveness</code>探测可以在同一个容器上并行使用。两者都用可以确保流量不会发给还没有准备好的容器，并且容器会在它们失败的时候被重新启动。<br>
<h3>配置探测器</h3>探测器有很多配置字段，可以使用这些字段精确的控制存活和就绪检测的行为：<br>
<ul><li>initialDelaySeconds：容器启动后要等待多少秒后存活和就绪探测器才被初始化，默认是0秒，最小值是0。</li><li>periodSeconds：执行探测的时间间隔（单位是秒）。默认是10秒。最小值是1。</li><li>timeoutSeconds：探测的超时后等待多少秒。默认值是1秒。最小值是1。</li><li>successThreshold：探测器在失败后，被视为成功的最小连续成功数。默认值是1。存活探测的这个值必须是1。最小值是1。</li><li>failureThreshold：当Pod启动了并且探测到失败，Kubernetes的重试次数。存活探测情况下的放弃就意味着重新启动容器。就绪探测情况下的放弃Pod会被打上未就绪的标签。默认值是3。最小值是1。</li></ul><br>
<br>HTTP探测器可以在<code class="prettyprint">httpGet</code>上配置额外的字段：<br>
<ul><li>host：连接使用的主机名，默认是Pod的IP。也可以在HTTP头中设置“Host”来代替。</li><li>scheme：用于设置连接主机的方式（HTTP还是HTTPS）。默认是HTTP。</li><li>path：访问HTTP服务的路径。</li><li>httpHeaders：请求中自定义的HTTP头。HTTP头字段允许重复。</li><li>port：访问容器的端口号或者端口名。如果数字必须在1 ～ 65535之间。</li></ul><br>
<br>对于HTTP探测，kubelet发送一个HTTP请求到指定的路径和端口来执行检测。除非<code class="prettyprint">httpGet</code>中的<code class="prettyprint">host</code>字段设置了，否则kubelet默认是给Pod的IP地址发送探测。如果<code class="prettyprint">scheme</code>字段设置为了HTTPS，kubelet会跳过证书验证发送HTTPS请求。大多数情况下，不需要设置<code class="prettyprint">host</code>字段。这里有个需要设置<code class="prettyprint">host</code>字段的场景，假设容器监听<code class="prettyprint">127.0.0.1</code>，并且Pod的<code class="prettyprint">hostNetwork</code>字段设置为了<code class="prettyprint">true</code>。那么<code class="prettyprint">httpGet</code>中的<code class="prettyprint">host</code>字段应该设置为<code class="prettyprint">127.0.0.1</code>。可能更常见的情况是如果Pod依赖虚拟主机，你不应该设置<code class="prettyprint">host</code>字段，而是应该在<code class="prettyprint">httpHeaders</code>中设置Host。<br>
<br>对于一次探测，kubelet在节点上（不是在Pod里面）建立探测连接，这意味着你不能在<code class="prettyprint">host</code>参数上配置<code class="prettyprint">service name</code>，因为kubelet不能解析<code class="prettyprint">service name</code>。<br>
<br>原文链接：<a href="https://juejin.cn/post/6993457394827132964" rel="nofollow" target="_blank">https://juejin.cn/post/6993457394827132964</a>，作者：王骁
                                
                                                              
</div>
            