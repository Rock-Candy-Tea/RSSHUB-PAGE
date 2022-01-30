
---
title: 'Kubernetes API之资源、种类和对象'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220118/8522b872d0156018a1ff8a0cc13950f6.jpg'
author: Dockone
comments: false
date: 2022-01-30 05:07:42
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220118/8522b872d0156018a1ff8a0cc13950f6.jpg'
---

<div>   
<br>【编者的话】本文通过Kubernetes API的方式，详细介绍了Kubernetes三大核心概念，资源、种类和对象，跟随作者，快来一睹为快吧。<br>
<br>这是关于如何从代码中使用Kubernetes API系列文章的第一篇。Kubernetes API比一堆简单的HTTP方法要高级一些。<br>
<br>因此，在试图使用Kubernetes API之前，理解Kubernetes API结构并熟悉术语是至关重要的。要不然，官方的Go客户端带有很多花哨的东西，如果你试图同时理解客户端和API的概念，可能会很快就会让你不知所措。  <br>
<br>Kubernetes API是巨大的——它有数百个端点。幸运的是，它是相当一致的，所以我们只需要理解有限数量的思想，然后将这些知识外推到API的其余部分。在这里，我将尝试触及我发现的最基本的概念。<br>
<br>我喜欢简单和易于消化的，而不是学术正确性和材料的完整性。和往常一样，我只是分享我对事物的理解和我对这个主题的思考方式——所以，这不是一个API指南，而是一个个人经验分享。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220118/8522b872d0156018a1ff8a0cc13950f6.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220118/8522b872d0156018a1ff8a0cc13950f6.jpg" class="img-polaroid" title="01.jpg" alt="01.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>资源和动词</h3>由于这是一个RESTful的领域，我们将根据资源（松散地说，特定结构的对象）和动词（对这些对象的操作）来操作。<br>
<br>在讨论资源时，重要的是要将资源区分为特定类型的对象和特定类型的实例。因此，Kubernetes API端点被正式命名为<a href="https://kubernetes.io/docs/reference/using-api/api-concepts/#standard-api-terminology">资源类型</a>，以避免与资源实例产生歧义。然而，在自然场景下，端点通常被称为资源，这个词的实际含义来自上下文。<br>
<br>出于可扩展性的原因，资源类型被组织到<a href="https://kubernetes.io/docs/reference/using-api/#api-groups">API组</a>中，这些组的版本是相互独立的：<br>
<pre class="prettyprint">$ kubectl api-resources<br>
NAME                     SHORTNAMES   APIVERSION   NAMESPACED   KIND<br>
bindings                              v1           true         Binding<br>
componentstatuses        cs           v1           false        ComponentStatus<br>
configmaps               cm           v1           true         ConfigMap<br>
endpoints                ep           v1           true         Endpoints<br>
events                   ev           v1           true         Event<br>
limitranges              limits       v1           true         LimitRange<br>
namespaces               ns           v1           false        Namespace<br>
nodes                    no           v1           false        Node<br>
persistentvolumeclaims   pvc          v1           true         PersistentVolumeClaim<br>
persistentvolumes        pv           v1           false        PersistentVolume<br>
pods                     po           v1           true         Pod<br>
...<br>
</pre><br>
Kubernetes的API是元数据。通过读取或创建其他资源，可以列出现有资源类型或注册新资源类型。例如，上面的列表是通过调用一个特殊的/apis资源获得的。<br>
<br><blockquote><br>实际上，有两种资源——核心资源（pods、secrets、configmaps 等）的遗留资源和其余资源的更通用<code class="prettyprint">/api</code>的资源，包括用户定义的自定义资源，<code class="prettyprint">/apis/&lt;resource-name></code>。</blockquote>下面是一个很好的技巧，可以让你看到<code class="prettyprint">kubectl</code>工具在运行命令时调用了哪些API：<br>
<pre class="prettyprint">$ kubectl api-resources -v 6  # -v 6 means "extra verbose logging"<br>
...<br>
I0108 ... GET https://192.168.58.2:8443/api?timeout=32s 200 OK in 10 milliseconds<br>
I0108 ... GET https://192.168.58.2:8443/apis?timeout=32s 200 OK in 1 milliseconds<br>
I0108 ... GET https://192.168.58.2:8443/apis/apiregistration.k8s.io/v1?timeout=32s 200 OK in 7 milliseconds<br>
I0108 ... GET https://192.168.58.2:8443/api/v1?timeout=32s 200 OK in 13 milliseconds<br>
I0108 ... GET https://192.168.58.2:8443/apis/authentication.k8s.io/v1?timeout=32s 200 OK in 13 milliseconds<br>
I0108 ... GET https://192.168.58.2:8443/apis/events.k8s.io/v1?timeout=32s 200 OK in 15 milliseconds<br>
I0108 ... GET https://192.168.58.2:8443/apis/apps/v1?timeout=32s 200 OK in 14 milliseconds<br>
I0108 ... GET https://192.168.58.2:8443/apis/autoscaling/v2beta1?timeout=32s 200 OK in 16 milliseconds<br>
I0108 ... GET https://192.168.58.2:8443/apis/policy/v1beta1?timeout=32s 200 OK in 14 milliseconds<br>
I0108 ... GET https://192.168.58.2:8443/apis/scheduling.k8s.io/v1?timeout=32s 200 OK in 14 milliseconds<br>
I0108 ... GET https://192.168.58.2:8443/apis/batch/v1?timeout=32s 200 OK in 13 milliseconds<br>
I0108 ... GET https://192.168.58.2:8443/apis/batch/v1beta1?timeout=32s 200 OK in 43 milliseconds<br>
...<br>
</pre><br>
你可以使用标准的HTTP客户端（如curl）轻松地调用上述资源（即API端点），并检查返回的资源（即JSON对象，双关语）：<br>
<pre class="prettyprint"># Make Kubernetes API available on localhost:8080<br>
# to bypass the auth step in subsequent queries:<br>
$ kubectl proxy --port=8080 &<br>
<br>
# List all known API paths<br>
$ curl http://localhost:8080/<br>
# List known versions of the `core` group<br>
$ curl http://localhost:8080/api<br>
# List known resources of the `core/v1` group<br>
$ curl http://localhost:8080/api/v1<br>
# Get a particular Pod resource<br>
$ curl http://localhost:8080/api/v1/namespaces/default/pods/sleep-7c7db887d8-dkkcg<br>
<br>
# List known groups (all but `core`)<br>
$ curl http://localhost:8080/apis<br>
# List known versions of the `apps` group <br>
$ curl http://localhost:8080/apis<br>
# List known resources of the `apps/v1` group<br>
$ curl http://localhost:8080/apis/apps/v1<br>
# Get a particular Deployment resource<br>
$ curl http://localhost:8080/apis/apps/v1/namespaces/default/deployments/sleep<br>
</pre><br>
<br><blockquote><br>有一种更简单的方法来检查Kubernetes API：<code class="prettyprint">kubectl get --raw /SOME/API/PATH</code>。但是，上面的练习是为了说明Kubernetes API并没有什么神奇之处——拥有一个未经测试的HTTP客户端就足以开始使用它了。</blockquote>说到动词，也就是资源上的操作，所有标准的CRUD操作都有传统的映射到HTTP方法上。此外，还支持对资源进行修补（可选择的字段修改）和监视（类似流的集合的读取）。来自<a href="https://github.com/kubernetes/community/blob/7f3f3205448a8acfdff4f1ddad81364709ae9b71/contributors/devel/sig-architecture/api-conventions.md#verbs-on-resources">sig-architecture/api-conventions.md</a>：<br>
<pre class="prettyprint">API resources should use the traditional REST pattern:<br>
<br>
GET /<resourceNamePlural> - Retrieve a list of type <resourceName>, e.g. GET /pods returns a list of Pods.<br>
POST /<resourceNamePlural> - Create a new resource from the JSON object provided by the client.<br>
GET /<resourceNamePlural>/<name> - Retrieves a single resource with the given name, e.g. GET /pods/first returns a Pod named 'first'. Should be constant time, and the resource should be bounded in size.<br>
DELETE /<resourceNamePlural>/<name> - Delete the single resource with the given name. DeleteOptions may specify gracePeriodSeconds, the optional duration in seconds before the object should be deleted. Individual kinds may declare fields which provide a default grace period, and different kinds may have differing kind-wide default grace periods. A user provided grace period overrides a default grace period, including the zero grace period ("now").<br>
DELETE /<resourceNamePlural> - Deletes a list of type <resourceName>, e.g. DELETE /pods a list of Pods.<br>
PUT /<resourceNamePlural>/<name> - Update or create the resource with the given name with the JSON object provided by the client.<br>
PATCH /<resourceNamePlural>/<name> - Selectively modify the specified fields of the resource. See more information below.<br>
GET /<resourceNamePlural>?watch=true - Receive a stream of JSON objects corresponding to changes made to any resource of the given kind over time.<br>
</pre><br>
<h3>种类（Kinds，又称对象模式）</h3>kind这个词会时不时地出现在这里和那里。例如，在<code class="prettyprint">kubectl api-resources</code>输出中，你可以看到该<code class="prettyprint">persistentvolumes</code>资源具有相应的<code class="prettyprint">PersistentVolume</code>种类。<br>
<br>很长一段时间以来，我与Kubernetes的交互仅限于盲目地使用<code class="prettyprint">kubectl apply</code>。 这让我认为kind总是包含资源的CamelCase名称，如Pod，Service，Deployment等。<br>
<pre class="prettyprint">$ cat <<EOF | kubectl apply -f -<br>
apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
name: my-deployment<br>
spec:<br>
replicas: 1<br>
selector:<br>
...<br>
EOF<br>
</pre><br>
但实际上，不是资源的Kubernetes数据结构也可以有kind：<br>
<pre class="prettyprint">apiVersion: audit.k8s.io/v1<br>
kind: Policy<br>
rules:<br>
- level: Metadata<br>
</pre><br>
不是Kubernetes对象（即持久实体）的资源也有kind：<br>
<pre class="prettyprint">$ kubectl get --raw /api | python -m json.tool<br>
&#123;<br>
"kind": "APIVersions",    <br>
"versions": [<br>
    "v1"<br>
],<br>
...<br>
&#125; <br>
</pre><br>
那么，什么是种类？<br>
<br><blockquote><br>所有资源类型都有一个具体的表示，称为一个kind——<a href="https://kubernetes.io/docs/reference/using-api/api-concepts/#standard-api-terminology">Kubernetes API参考</a>。好吧，这个解释不是特别有用。</blockquote>事实证明，在Kubernetes中，一种是对象模式的名称。就像你通常使用JSON模式词汇表描述的那样。换句话说，种类是指特定的数据结构，即属性和属性的某种组合。<br>
<br>根据<a href="https://github.com/kubernetes/community/blob/7f3f3205448a8acfdff4f1ddad81364709ae9b71/contributors/devel/sig-architecture/api-conventions.md#types-kinds">sig-architecture/api-conventions.md</a>，kind分为三类：<br>
<ul><li>对象（Pod，Service等）：系统中的持久实体。</li><li>列表（PodList，APIResourceList等）：一种或多种资源的集合。</li><li>status对对象（status、scale等）或非持久性辅助实体（ListOptions、Policy等）的简单特定操作。</li></ul><br>
<br>Kubernetes中使用的大多数对象，包括API返回的所有JSON对象，都有kind字段。它允许客户端和服务器在通过网络发送它们或将它们存储在磁盘上之前正确地序列化和反序列化这些对象。<br>
<h3>Kubernetes对象</h3>就像资源一样，Kubernetes用语中的对象这个词是重载的。从广义上讲，对象可以指任何数据结构——资源类型的实例（如APIGroup）、配置（如审计策略）或持久实体（如Pod）。但是，在本节中，我将在狭义的、明确定义的意义上讨论对象。所以，我将使用大写的词Object来代替。<br>
<br>像ReplicaSet、Namespace或的实体ConfigMap被称为Kubernetes对象。对象是Kubernetes系统中的持久实体，代表集群的意图（期望状态）和状态（实际状态）。<br>
<br><blockquote><br>例如，一旦你创建了一个Pod对象，Kubernetes将不断地工作以确保相应的容器集合正在运行。</blockquote>大多数Kubernetes API资源代表对象。与其他形式的资源只要求kind字段不同，对象必须定义更多字段：<br>
<ul><li>kind：标识此对象应具有的架构的字符串</li><li>apiVersion：一个字符串，用于标识对象应具有的架构版本</li><li>metadata.namespace：带有命名空间的字符串（默认为“default”）</li><li>metadata.name：在当前命名空间中唯一标识此对象的字符串</li><li>metadata.uid：一个唯一的时间和空间值，用于区分已删除和重新创建的同名对象。</li></ul><br>
<br>此外，元数据字典可能包括<code class="prettyprint">labels</code>和<code class="prettyprint">annotations</code>字段，以及一些版本控制和时间戳信息。<br>
<br><blockquote><br>有趣的事实：该<code class="prettyprint">kubectl api-resources</code>命令实际上列出的不是API资源，而是已知类型的Kubernetes对象。要列出真正的API资源，你需要运行一个完整的发现周期，以<code class="prettyprint">kubectl get --raw /</code>递归方式查询每个返回的路径。</blockquote>示例：Pod 对象（截断输出）<br>
<pre class="prettyprint">$ kubectl get --raw /api/v1/namespaces/default/pods/sleep-7c7db887d8-dkkcg | python -m json.tool<br>
&#123;<br>
"apiVersion": "v1",<br>
"kind": "Pod",<br>
"metadata": &#123;<br>
    "namespace": "default",<br>
    "name": "sleep-7c7db887d8-dkkcg",        <br>
    "uid": "32bf410a-0009-484e-adac-21179ec28f0f",<br>
    "labels": &#123;<br>
        "app": "sleep",<br>
        "pod-template-hash": "7c7db887d8"<br>
    &#125;,        <br>
    "creationTimestamp": "2022-01-08T18:10:04Z",<br>
    "resourceVersion": "465766"        <br>
&#125;,<br>
"spec": &#123; ... &#125;,<br>
"status": &#123; ... &#125;<br>
&#125; <br>
</pre><br>
<br><blockquote><br>有趣的事实：Kubernetes被称为生产级容器编排系统。但是，Container不是Kubernetes对象——它只是一种简单的对象，但是Pod是一个成熟的持久对象。</blockquote>如上例所示，Kubernetes对象通常具有spec（期望状态）和status（实际状态）字段。但情况并非总是如此。将上面的输出与下面的ConfigMap对象进行比较：<br>
<pre class="prettyprint">$ kubectl get --raw /api/v1/namespaces/default/configmaps/informer-dynamic-simple-wzgmx | python -m json.tool<br>
&#123;<br>
"apiVersion": "v1",<br>
"kind": "ConfigMap",<br>
"data": &#123;<br>
    "foo": "bar"<br>
&#125;,    <br>
"metadata": &#123;<br>
    "namespace": "default",<br>
    "name": "informer-dynamic-simple-wzgmx",<br>
    "uid": "74471398-0244-4686-b490-7007f6246a63",<br>
    "creationTimestamp": "2022-01-06T21:45:04Z",<br>
    "generateName": "informer-dynamic-simple-",<br>
    "resourceVersion": "418185"        <br>
&#125;<br>
&#125; <br>
</pre><br>
从代码中处理Kubernetes API涉及到大量的对象操作，因此必须对常见的对象结构有扎实的理解。该<code class="prettyprint">kubectl explain</code>命令可以帮助你。它最酷的部分是它不仅可以在资源上调用，还可以在嵌套字段上调用：<br>
<pre class="prettyprint">$ kubectl explain deployment.spec.template<br>
KIND:     Deployment<br>
VERSION:  apps/v1<br>
<br>
RESOURCE: template <Object><br>
<br>
DESCRIPTION:<br>
 Template describes the pods that will be created.<br>
<br>
 PodTemplateSpec describes the data a pod should have when created from a<br>
 template<br>
<br>
FIELDS:<br>
metadata <Object><br>
 Standard object's metadata. More info:<br>
 https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata<br>
<br>
spec <Object><br>
 Specification of the desired behavior of the pod. More info:<br>
 https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status<br>
</pre><br>
<h3>总结</h3>Kubernetes用语中的资源可以指资源类型和资源实例。资源类型被组织成API组，并且API组是版本化的。每个资源表都遵循由其kind定义的特定模式。虽然每个资源都遵循其类型定义的具体结构，但并非每个资源都代表一个Kubernetes对象。对象是一种持久性实体，用于表达对意图的记录。不同种类的对象具有不同的结构，但所有对象都带有共同的元数据属性，例如命名空间、名称、uid或创建时间戳。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220118/9d6546e2952dd4419b0928e36566ffe0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220118/9d6546e2952dd4419b0928e36566ffe0.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>敬请关注</h3>下一篇文章将概述<code class="prettyprint">k8s.io/api</code>和<code class="prettyprint">k8s.io/apimachinery</code>包——官方Go客户端的两个主要依赖项。我将展示Kubernetes API对象如何映射到Go结构，Go结构如何被序列化和反序列化，并涉及一些其他常见的（在客户端和服务器之间）API机制，不要错过哦！<br>
<br><strong>原文链接：<a href="https://iximiuz.com/en/posts/kubernetes-api-structure-and-terminology/">Working with Kubernetes API - Resources, Kinds, and Objects</a></strong><br>
<br><strong>译者</strong>：Mr.lzc，高级工程师、DevOpsDays、HDZ深圳核心组织者，目前供职于华为，从事云计算工作，专注于K8s、微服务领域。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            