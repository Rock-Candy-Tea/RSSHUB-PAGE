
---
title: '5实用的Kubectl使用技巧'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/ce53ccf8b0016670f041e39108e49dfb.png'
author: Dockone
comments: false
date: 2021-09-15 02:20:33
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/ce53ccf8b0016670f041e39108e49dfb.png'
---

<div>   
<br>kubectl是Kubernetes官方附带的命令行工具，可以方便的操作Kubernetes集群。这篇文章主要介绍一些kubectl的别样用法，希望读者有基础的Kubernetes使用经验。<br>
<br>有一篇文章也介绍了一些技巧，写博客的时候正好搜到了，正好也分享出来吧。<br>
<br><a href="https://blog.flant.com/ready-to-use-commands-and-tips-for-kubectl/" rel="nofollow" target="_blank">https://blog.flant.com/ready-t ... ectl/</a><br>
<h3>打印当前使用的API</h3><pre class="prettyprint"># kubectl 的主要作用就是与ApiServer进行交互，而交互的过程，我们可以通过下面的方式来打印<br>
# 这个命令尤其适合调试自己的API接口时使用<br>
kubectl get ns -v=9<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/ce53ccf8b0016670f041e39108e49dfb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/ce53ccf8b0016670f041e39108e49dfb.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>按状态筛选容器以及删除</h3>我在这里学到的命令：<a href="https://computingforgeeks.com/force-delete-evicted-terminated-pods-in-kubernetes/" rel="nofollow" target="_blank">https://computingforgeeks.com/ ... etes/</a><br>
<pre class="prettyprint">kubectl get pods --all-namespaces --field-selector status.phase=Pending -o json | \<br>
jq '.items[] | "kubectl delete pods \(.metadata.name) -n \(.metadata.namespace)"' | \<br>
xargs -n 1 bash -c<br>
<br>
<br>
# 这个命令要拆开来看<br>
# 首先，获取所有NS中状态为Pending的pods，并以json形式输出<br>
# 这个语句其实由很多变体，比如，我想查找Failed的状态，或是某个deployment<br>
kubectl get pods --all-namespaces --field-selector status.phase=Pending -o json <br>
<br>
# 针对json变量进行处理，生成可用的脚本<br>
# 这里是我想介绍的重点，利用jq以及kubectl的输出，构建出可用的命令<br>
jq '.items[] | "kubectl delete pods \(.metadata.name) -n \(.metadata.namespace)"'<br>
<br>
# 执行每一条命令<br>
# 注意，这种命令一定要好好调试，删掉预期之外的Pod就不好了<br>
xargs -n 1 bash -c<br>
<br>
<br>
# 例如，下面的语句可以找到所有的Pods并打印可以执行的语句<br>
kubectl get pods --all-namespaces --field-selector status.phase=Running -o json | \<br>
jq '.items[] | "kubectl get pods \(.metadata.name) -o wide -n \(.metadata.namespace)"'<br>
<br>
"kubectl get pods metrics-server-6d684c7b5-gtd6q -o wide -n kube-system"<br>
"kubectl get pods local-path-provisioner-58fb86bdfd-98frc -o wide -n kube-system"<br>
"kubectl get pods nginx-deployment-574b87c764-xppmx -o wide -n default"<br>
<br>
# 当然，如果只是删除单个NS下面的一些pods，我会选择下面的方法，但是它操作多个NS就很不方便了<br>
kubectl -n default get pods  | grep Completed | awk '&#123;print $1&#125;' | xargs kubectl -n default delete pods<br>
</pre><br>
<h3>统计具体某台机器上运行的所有Pod</h3>kubectl可以使用两种选择器，一种是label，一种是field，可以看官网的介绍：<br>
<ul><li><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/">Labels and Selectors</a></li><li><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/">Field Selectors</a></li></ul><br>
<br><pre class="prettyprint"># 它是一种选择器，可以与上面的awk或者xargs配合使用<br>
# 我个人平时都不喜欢用这个，直接get全部pods，然后grep查找感觉更快<br>
kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=pve-node1<br>
</pre><br>
<h3>统计Pod在不同机器的具体数量分布</h3>不知道有读者看过我的这篇文章：《<a href="http://dockone.io/article/2434592">基于Kubernetes的PaaS平台中细力度控制Pod方案的实现</a>》，均衡分布的工作前提是得知Pod在各个机器的分布情况，最好的办法就是我们得到Pod信息之后进行简单的统计，这个工作可以使用<code class="prettyprint">awk</code>实现。<br>
<pre class="prettyprint">kubectl -n default get pods -o wide -l app="nginx" | awk '&#123;print $7&#125;'|\<br>
awk '&#123; count[$0]++  &#125; <br>
END &#123; <br>
printf("%-35s: %s\n","Word","Count");<br>
for(ind in count)&#123;<br>
printf("%-35s: %d\n",ind,count[ind]);<br>
&#125;<br>
&#125;'<br>
<br>
# 执行结果如下<br>
Word                               : Count<br>
NODE                               : 1<br>
pve-node1                          : 1<br>
pve-node2                          : 1<br>
<br>
<br>
# awk的语法我没深入了解，有兴趣的读者可以研究看看，这里我就不求甚解了<br>
</pre><br>
<h3>kubectl proxy的使用</h3>你可以理解为这个命令为Kubernetes的ApiServer做了一层代理，使用该代理，你可以直接调用API而不需要经过鉴权。启动之后，甚至可以实现<code class="prettyprint">kubectl</code>套娃，下面是一个例子：<br>
<pre class="prettyprint"># 当你没有设置kubeconfig而直接调用kubectl时<br>
kubectl get ns -v=9<br>
# 可以打印出下面类似的错误<br>
curl -k -v -XGET  -H "Accept: application/json, */*" -H "User-Agent: kubectl/v1.21.3 (linux/amd64) kubernetes/ca643a4" 'http://localhost:8080/api?timeout=32s'<br>
skipped caching discovery info due to Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused                     <br>
# 也就是说当你不指定kubeconfig文件时，kubectl会默认访问本机的8080端口<br>
# 那么我们先启动一个kubectl proxy，然后指定监听8080，再使用kubectl直接访问，是不是就可行了呢<br>
# 事实证明，安全与预想一致<br>
KUBECONFIG=~/.kube/config-symv3 kubectl proxy  -p 8080<br>
kubectl get ns<br>
NAME                           STATUS   AGE<br>
default                        Active   127d<br>
</pre><br>
默认启动的proxy是屏蔽了某些API的，并且有一些限制，例如无法使用exec进入Pod之中，可以使用<code class="prettyprint">kubectl proxy --help</code>来看，例如：<br>
<pre class="prettyprint"># 仅允许本机访问<br>
--accept-hosts='^localhost$,^127\.0\.0\.1$,^\[::1\]$': Regular expression for hosts that the proxy should accept.<br>
# 不允许访问下面的API，也就是说默认没法exec进入容器<br>
--reject-paths='^/api/.*/pods/.*/exec,^/api/.*/pods/.*/attach': Regular expression for paths that the proxy should reject. Paths specified here will be rejected even accepted by --accept-paths.<br>
<br>
# 想跳过exec的限制也很简单，把reject-paths去掉就可以了<br>
kubectl proxy -p 8080 --keepalive 3600s --reject-paths='' -v=9<br>
</pre><br><br>
有人说这个kubectl proxy可能没什么作用，那可能仅仅是你还没有实际的应用场景。例如当我想要调试<code class="prettyprint">Kubernetes dashboard</code>代码的时候，如果直接使用kubeconfig文件，我没法看到具体的请求过程，如果你加上一层proxy转发，并且设置<code class="prettyprint">-v=9</code>的时候，你就自动获得了一个日志记录工具，在调试时相当有用。<br>
<h3>总结</h3>kubectl是一个强大的命令行工具，上面我只是介绍了我工作中对其用法的一点探索，也并不鼓励大家非要记住这些命令，只是希望当读者需要的时候，能够想起来kubectl可以有类似的功能，就不需要针对几个临时需求去研读client-api了。<br>
<br>原文链接：<a href="https://corvo.myseu.cn/2021/08/16/2021-08-16-kubectl" rel="nofollow" target="_blank">https://corvo.myseu.cn/2021/08 ... bectl</a>的多样用法/，作者：corvofeng
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            