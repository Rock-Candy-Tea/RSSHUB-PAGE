
---
title: 'Kubernetes的namespace一直Terminating的完美解决方案'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=1508'
author: Dockone
comments: false
date: 2021-09-13 03:08:07
thumbnail: 'https://picsum.photos/400/300?random=1508'
---

<div>   
<br>在Kubernetes集群中进行测试删除namespace是经常的事件，而为了方便操作，一般都是直接对整个名称空间进行删除操作。<br>
<br>相信道友们在进行此步操作的时候，会遇到要删除的namespace一直处于Terminating。下面我将给出一个完美的解决方案。<br>
<h3>测试demo</h3><pre class="prettyprint">创建demo namespace<br>
# kubectl create ns test<br>
namespace/test created<br>
<br>
删除demo namespace<br>
# kubectl delete ns test<br>
namespace "test" deleted<br>
<br>
一直处于deleted不见exit<br>
查看状态，可见test namespace处于Terminating  <br>
# kubectl get ns -w<br>
NAME                STATUS        AGE<br>
test                Terminating   18s<br>
</pre><br>
<h4>下面给出一种完美的解决方案：调用接口删除</h4><pre class="prettyprint">开启一个代理终端<br>
# kubectl proxy<br>
Starting to serve on 127.0.0.1:8001<br>
<br>
再开启一个操作终端<br>
将test namespace的配置文件输出保存<br>
# kubectl get ns test -o json > test.json<br>
删除spec及status部分的内容还有metadata字段后的","号，切记！<br>
剩下内容大致如下：<br>
&#123;<br>
"apiVersion": "v1",<br>
"kind": "Namespace",<br>
"metadata": &#123;<br>
    "annotations": &#123;<br>
        "cattle.io/status": "&#123;\"Conditions\":[&#123;\"Type\":\"ResourceQuotaInit\",\"Status\":\"True\",\"Message\":\"\",\"LastUpdateTime\":\"2020-10-09T07:12:17Z\"&#125;,&#123;\"Type\":\"InitialRolesPopulated\",\"Status\":\"True\",\"Message\":\"\",\"LastUpdateTime\":\"2020-10-09T07:12:18Z\"&#125;]&#125;",<br>
        "lifecycle.cattle.io/create.namespace-auth": "true"<br>
    &#125;,<br>
    "creationTimestamp": "2020-10-09T07:12:16Z",<br>
    "deletionTimestamp": "2020-10-09T07:12:22Z",<br>
    "name": "test",<br>
    "resourceVersion": "471648079",<br>
    "selfLink": "/api/v1/namespaces/test",<br>
    "uid": "862d311e-d87a-48c2-bc48-332a4db9dbdb"<br>
&#125;<br>
&#125;<br>
<br>
调接口删除<br>
# curl -k -H "Content-Type: application/json" -X PUT --data-binary @test.json http://127.0.0.1:8001/api/v1/namespaces/test/finalize<br>
&#123;<br>
"kind": "Namespace",<br>
"apiVersion": "v1",<br>
"metadata": &#123;<br>
"name": "test",<br>
"selfLink": "/api/v1/namespaces/test/finalize",<br>
"uid": "862d311e-d87a-48c2-bc48-332a4db9dbdb",<br>
"resourceVersion": "471648079",<br>
"creationTimestamp": "2020-10-09T07:12:16Z",<br>
"deletionTimestamp": "2020-10-09T07:12:22Z",<br>
"annotations": &#123;<br>
  "cattle.io/status": "&#123;\"Conditions\":[&#123;\"Type\":\"ResourceQuotaInit\",\"Status\":\"True\",\"Message\":\"\",\"LastUpdateTime\":\"2020-10-09T07:12:17Z\"&#125;,&#123;\"Type\":\"InitialRolesPopulated\",\"Status\":\"True\",\"Message\":\"\",\"LastUpdateTime\":\"2020-10-09T07:12:18Z\"&#125;]&#125;",<br>
  "lifecycle.cattle.io/create.namespace-auth": "true"<br>
&#125;<br>
&#125;,<br>
"spec": &#123;<br>
<br>
&#125;,<br>
"status": &#123;<br>
"phase": "Terminating",<br>
"conditions": [<br>
  &#123;<br>
    "type": "NamespaceDeletionDiscoveryFailure",<br>
    "status": "True",<br>
    "lastTransitionTime": "2020-10-09T07:12:27Z",<br>
    "reason": "DiscoveryFailed",<br>
    "message": "Discovery failed for some groups, 1 failing: unable to retrieve the complete list of server APIs: metrics.k8s.io/v1beta1: the server is currently unable to handle the request"<br>
  &#125;,<br>
  &#123;<br>
    "type": "NamespaceDeletionGroupVersionParsingFailure",<br>
    "status": "False",<br>
    "lastTransitionTime": "2020-10-09T07:12:28Z",<br>
    "reason": "ParsedGroupVersions",<br>
    "message": "All legacy kube types successfully parsed"<br>
  &#125;,<br>
  &#123;<br>
    "type": "NamespaceDeletionContentFailure",<br>
    "status": "False",<br>
    "lastTransitionTime": "2020-10-09T07:12:28Z",<br>
    "reason": "ContentDeleted",<br>
    "message": "All content successfully deleted"<br>
  &#125;<br>
]<br>
&#125;<br>
&#125; <br>
</pre><br>
<h4>查看结果</h4><pre class="prettyprint">1、delete 状态终止<br>
kubectl delete ns test<br>
namespace "test" deleted<br>
<br>
2、Terminating状态终止<br>
kubectl get ns -w<br>
test                Terminating   18s<br>
test                Terminating   17m<br>
</pre><br>
名称空间被删除掉。<br>
<br>原文链接：<a href="https://www.cnblogs.com/zisefeizhu/p/13786053.html" rel="nofollow" target="_blank">https://www.cnblogs.com/zisefeizhu/p/13786053.html</a>
                                
                                                              
</div>
            