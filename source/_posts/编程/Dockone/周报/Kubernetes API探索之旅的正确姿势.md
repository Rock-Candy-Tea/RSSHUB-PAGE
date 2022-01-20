
---
title: 'Kubernetes API探索之旅的正确姿势'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://iximiuz.com/kubernetes-api-call-simple-http-client/kdpv.png'
author: Dockone
comments: false
date: 2022-01-20 00:32:06
thumbnail: 'https://iximiuz.com/kubernetes-api-call-simple-http-client/kdpv.png'
---

<div>   
<br>【编者的话】本文带你打开Kubernetes API的探索之旅的正确姿势，快来一睹为快吧！<br>
<br>使用CLI（如curl）或GUI（如postman）HTTP客户端调用Kubernetes API有很多理由。例如，你可能需要对Kubernetes 对象进行比kubectl提供的更细粒度的控制，或者只是想在尝试从代码访问API之前探索它。<br>
<br>本文不仅仅是一个方便的命令列表，而是一个深思熟虑的演练，揭示了一些你在从命令行调用Kubernetes API时可能会偶然发现的有趣问题。它涵盖以下主题：<br>
<ul><li>如何获取Kubernetes API服务器地址</li><li>如何向客户端验证API服务器</li><li>如何使用证书向API服务器验证客户端</li><li>如何使用令牌向API服务器验证客户端</li><li>奖励：如何从Pod内部调用Kubernetes API</li><li>如何使用curl对Kubernetes对象执行基本的CRUD操作</li><li>如何使用kubectl的raw模式直接访问Kubernetes API</li><li>奖励：如何查看哪些API请求kubectl命令（如apply发送）</li></ul><br>
<br>享受本次阅读！<br>
<br><img src="https://iximiuz.com/kubernetes-api-call-simple-http-client/kdpv.png" alt referrerpolicy="no-referrer"><br>
<br><h2>设置 Kubernetes 游乐场</h2>如果你没有Kubernetes集群可以玩，下面是如何使用<a href="https://github.com/alexellis/arkade">arkade</a>快速创建本地游乐场：<br>
<br><code class="prettyprint">$ curl -sLS https://get.arkade.dev | sudo sh<br>
$ arkade get minikube kubectl<br>
$ minikube start --profile cluster1</code><br>
<br><blockquote><br><code class="prettyprint">curl | sudo sh</code>模式很吓人。从 Internet 获取软件包并在笔记本电脑上运行它们的想法也是如此。由于我没有时间检查我使用的每一段开源代码，我更喜欢隔离和一次性的开发环境。你可以在<a href="https://iximiuz.com/en/posts/how-to-setup-development-environment/">此处</a>阅读有关我的开发程序的更多信息。</blockquote><h2>如何获取Kubernetes API主机和端口</h2>要调用任何API，你首先需要知道其服务器地址。对于Kubernetes，每个集群都有一个API服务器。因此，查找API主机和端口的最简单方法是查看<code class="prettyprint">kubectl cluster-info</code>输出。例如，在我的Vagrant盒子上，它会产生以下几行：<br>
<br><code class="prettyprint">$ kubectl cluster-info<br>
Kubernetes control plane is running at https://192.168.58.2:8443<br>
...</code><br>
<br>该cluster-info命令显示在当前上下文中选择的集群的API地址。但是，如果你有多个集群怎么办？<br>
<br>查找Kubernetes API服务器地址的另一种方法是查看kubeconfig内容：<br>
<br><code class="prettyprint">$ kubectl config view<br>
apiVersion: v1<br>
clusters:<br>
- name: cluster1<br>
  cluster:<br>
    ...<br>
    server: https://192.168.58.2:8443<br>
- name: cluster2<br>
  cluster:<br>
    ...<br>
    server: https://192.168.59.2:8443<br>
...</code><br>
<br><blockquote><br>默认情况下，kubectl查找目录中命名config的<code class="prettyprint">$HOME/.kube</code>文件。那么，为什么不直接从这个文件中获取API地址呢？<br>
  原因是潜在的配置合并。KUBECONFIG通过将env var设置为以冒号分隔的位置列表，可以指定多个kubeconfig文件。kubectl在访问集群之前，会尝试将所有 kubeconfig文件的内容合并到一个配置中。</blockquote>因此，从上面的列表中选择正确的集群，让我们尝试向其API服务器发送请求：<br>
<br><code class="prettyprint">$ KUBE_API=$(kubectl config view -o jsonpath='&#123;.clusters[0].cluster.server&#125;')</code><br>
<br><h2>如何使用curl调用Kubernetes API</h2>实际上，任何HTTP客户端（curl、httpie、wget甚至postman）都可以，但我将在本节中坚持使用curl，因为我已经习惯了。<br>
<br><h2>向客户端验证API服务器</h2>让我们从查询API的/version端点开始：<br>
<br>```<br>
$ curl $KUBE_API/version<br>
curl: (60) SSL certificate problem: unable to get local issuer certificate<br>
More details here: <a href="https://curl.haxx.se/docs/sslcerts.html" rel="nofollow" target="_blank">https://curl.haxx.se/docs/sslcerts.html</a><br>
<br>curl failed to verify the legitimacy of the server and therefore could not<br>
establish a sec<br>
<br>ure connection to it. To learn more about this situation and<br>
how to fix it, please visit the web page mentioned above.<br>
```<br>
<br>额……行不通！<br>
<br>当我第一次偶然发现类似的错误时，我真的很困惑。但仔细想想，上述错误实际上是有道理的。默认情况下，Kubernetes通过HTTPS公开其API，特别是为了向客户端保证API服务器的强身份。但是，minikube使用自签名证书引导我的本地集群。因此，Kubernetes API服务器的TLS证书原来是由curl未知的证书颁发机构 (CA) minikubeCA签名的。由于curl无法信任它，因此请求失败。<br>
<br><blockquote><br>默认情况下，curl信任底层操作系统所信任的同一组CA。例如，在Ubuntu或Debian上，受信任的CA列表可以在<code class="prettyprint">/etc/ssl/certs/ca-certificates.crt</code>。 显然，minikube不会将其证书添加到此文件中。</blockquote>幸运的是，minikube周到地将CA证书保存到了<code class="prettyprint">~/.minikube/ca.crt</code>：<br>
<br><code class="prettyprint">$ cat ~/.minikube/ca.crt | openssl x509 -text<br>
Certificate:<br>
    Data:<br>
        Version: 3 (0x2)<br>
        Serial Number: 1 (0x1)<br>
        Signature Algorithm: sha256WithRSAEncryption<br>
        Issuer: CN = minikubeCA<br>
        Validity<br>
            Not Before: Dec 15 20:46:36 2021 GMT<br>
            Not After : Dec 14 20:46:36 2031 GMT<br>
        Subject: CN = minikubeCA<br>
        Subject Public Key Info:</code><br>
<br>因此，要修复该GET /version请求，我只需要通过手动将其指向minikube CA证书来使curl信任API服务器证书的颁发者：<br>
<br><code class="prettyprint">$ curl --cacert ~/.minikube/ca.crt $KUBE_API/version<br>
&#123;<br>
  &quot;major&quot;: &quot;1&quot;,<br>
  &quot;minor&quot;: &quot;22&quot;,<br>
  &quot;gitVersion&quot;: &quot;v1.22.3&quot;,<br>
  &quot;gitCommit&quot;: &quot;c92036820499fedefec0f847e2054d824aea6cd1&quot;,<br>
  &quot;gitTreeState&quot;: &quot;clean&quot;,<br>
  &quot;buildDate&quot;: &quot;2021-10-27T18:35:25Z&quot;,<br>
  &quot;goVersion&quot;: &quot;go1.16.9&quot;,<br>
  &quot;compiler&quot;: &quot;gc&quot;,<br>
  &quot;platform&quot;: &quot;linux/amd64&quot;<br>
&#125;</code><br>
耶！<br>
<br><blockquote><br>提示 或者，你可以通过使用<code class="prettyprint">--insecure</code>标志或其短别名<code class="prettyprint">-k</code>来使用curl。在安全的环境中，我更喜欢不安全模式——它比试图找到颁发者证书更简单。</blockquote><h2>使用证书向API服务器验证客户端</h2>好吧，让我们尝试一些更复杂的东西。列出集群中的所有部署怎么样？<br>
<br>```<br>
$ curl --cacert ~/.minikube/ca.crt $KUBE_API/apis/apps/v1/deployments<br>
&#123;<br>
  "kind": "Status",<br>
  "apiVersion": "v1",<br>
  "metadata": &#123;<br>
<br>  &#125;,<br>
  "status": "Failure",<br>
  "message": "deployments.apps is forbidden: User \"system:anonymous\" cannot list resource \"deployments\" in API group \"apps\" at the cluster scope",<br>
  "reason": "Forbidden",<br>
  "details": &#123;<br>
    "group": "apps",<br>
    "kind": "deployments"<br>
  &#125;,<br>
  "code": 403<br>
&#125;<br>
```<br>
<br>额......再次行不通！<br>
<br>与明显未受保护的/version端点不同，Kubernetes通常会限制对其API端点的访问。<br>
<br>从错误消息中可以清楚地看出，该请求已通过身份验证User "system:anonymous"，并且显然，该用户未授权列出部署资源。<br>
<br>失败的请求不包括任何身份验证方式（尽管如此，它已经过身份验证，但作为匿名用户），所以我需要提供一些额外的信息来获得所需的访问级别。<br>
<br>Kubernetes支持<a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/">多种身份验证机制</a>，我将从使用客户端证书对请求进行身份验证开始。<br>
<br>但是等一下！什么是客户证书？<br>
<br>当minikube引导集群时，它还创建了一个user。该用户获得了由同一个minikube CA颁发机构签署的证书。由于Kubernetes API服务器信任此 CA，因此在请求中提供此证书将使其作为所述用户进行身份验证。<br>
<br><blockquote><br>Kubernetes 没有代表用户的对象。即，不能通过API调用将用户添加到集群中。但是，任何提供由集群的证书颁发机构签名的有效证书的用户都被视为已通过身份验证。Kubernetes从证书主题中的通用名称字段中获取用户名（例如，CN = minikube-user）。然后，Kubernetes RBAC子系统判断用户是否有权对资源执行特定操作。</blockquote>用户证书通常可以在我们已经熟悉的<code class="prettyprint">kubectl config view</code>输出中找到：<br>
<br><code class="prettyprint">$ kubectl config view -o jsonpath='&#123;.users[0]&#125;' | python -m json.tool<br>
&#123;<br>
  &quot;name&quot;: &quot;cluster1&quot;,<br>
  &quot;user&quot;: &#123;<br>
    &quot;client-certificate&quot;: &quot;/home/vagrant/.minikube/profiles/cluster1/client.crt&quot;,<br>
    &quot;client-key&quot;: &quot;/home/vagrant/.minikube/profiles/cluster1/client.key&quot;<br>
  &#125;<br>
&#125;</code><br>
<br>让我们快速检查证书内容以确保它是由同一个 CA 签名的：<br>
<br><code class="prettyprint">$ cat ~/.minikube/profiles/cluster1/client.crt | openssl x509 -text<br>
Certificate:<br>
    Data:<br>
        Version: 3 (0x2)<br>
        Serial Number: 2 (0x2)<br>
        Signature Algorithm: sha256WithRSAEncryption<br>
        Issuer: CN = minikubeCA<br>
        Validity<br>
            Not Before: Dec 26 06:35:56 2021 GMT<br>
            Not After : Dec 26 06:35:56 2024 GMT<br>
        Subject: O = system:masters, CN = minikube-user</code><br>
<br>以下是如何使用curl向Kubernetes API服务器发送由该证书认证的请求：<br>
<br><code class="prettyprint">$ curl $KUBE_API/apis/apps/v1/deployments \<br>
  --cacert ~/.minikube/ca.crt \<br>
  --cert ~/.minikube/profiles/cluster1/client.crt \<br>
  --key ~/.minikube/profiles/cluster1/client.key<br>
&#123;<br>
  &quot;kind&quot;: &quot;DeploymentList&quot;,<br>
  &quot;apiVersion&quot;: &quot;apps/v1&quot;,<br>
  &quot;metadata&quot;: &#123;<br>
    &quot;resourceVersion&quot;: &quot;654514&quot;<br>
  &#125;,<br>
  &quot;items&quot;: [...]<br>
&#125;</code><br>
<br>干得漂亮！<br>
<br><h2>使用服务帐户令牌向API服务器验证客户端</h2>另一种验证API请求的方法是使用包含有效服务帐户JWT令牌的不记名标头。<br>
<br>与用户非常相似，不同的服务帐户将具有不同级别的访问权限。让我们看看使用默认命名空间中的默认服务帐户可以实现什么：<br>
<br><code class="prettyprint">$ JWT_TOKEN_DEFAULT_DEFAULT=$(kubectl get secrets \<br>
    $(kubectl get serviceaccounts/default -o jsonpath='&#123;.secrets[0].name&#125;') \<br>
    -o jsonpath='&#123;.data.token&#125;' | base64 --decode)</code><br>
<br>从一个简单的任务开始——列出apps/v1组中已知的 API 资源类型：<br>
<br><code class="prettyprint">$ curl $KUBE_API/apis/apps/v1/ \<br>
  --cacert ~/.minikube/ca.crt  \<br>
  --header &quot;Authorization: Bearer $JWT_TOKEN_DEFAULT_DEFAULT&quot;<br>
&#123;<br>
  &quot;kind&quot;: &quot;APIResourceList&quot;,<br>
  &quot;apiVersion&quot;: &quot;v1&quot;,<br>
  &quot;groupVersion&quot;: &quot;apps/v1&quot;,<br>
  &quot;resources&quot;: [...]<br>
&#125;</code><br>
<br>提高标准 - 让我们尝试在默认命名空间中列出实际的部署对象：<br>
<br>```<br>
$ curl $KUBE_API/apis/apps/v1/namespaces/default/deployments \<br>
  --cacert ~/.minikube/ca.crt  \<br>
  --header "Authorization: Bearer $JWT_TOKEN_DEFAULT_DEFAULT"<br>
&#123;<br>
  "kind": "Status",<br>
  "apiVersion": "v1",<br>
  "metadata": &#123;<br>
<br>  &#125;,<br>
  "status": "Failure",<br>
  "message": "deployments.apps is forbidden: User \"system:serviceaccount:default:default\" cannot list resource \"deployments\" in API group \"apps\" in the namespace \"default\"",<br>
  "reason": "Forbidden",<br>
  "details": &#123;<br>
    "group": "apps",<br>
    "kind": "deployments"<br>
  &#125;,<br>
  "code": 403<br>
&#125;<br>
```<br>
<br>显然，用户<code class="prettyprint">system:serviceaccount:default:default</code>甚至没有足够的能力在自己的命名空间中列出Kubernetes对象。<br>
<br>让我们尝试一个强大的kube-system服务帐户：<br>
<br><code class="prettyprint">$ JWT_TOKEN_KUBESYSTEM_DEFAULT=$(kubectl -n kube-system get secrets \<br>
    $(kubectl -n kube-system get serviceaccounts/default -o jsonpath='&#123;.secrets[0].name&#125;') \<br>
    -o jsonpath='&#123;.data.token&#125;' | base64 --decode)</code><br>
<br>强大的帐户值得一项具有挑战性的任务 - 列出集群级资源：<br>
<br><code class="prettyprint">$ curl $KUBE_API/apis/apps/v1/deployments \<br>
  --cacert ~/.minikube/ca.crt  \<br>
  --header &quot;Authorization: Bearer $JWT_TOKEN_KUBESYSTEM_DEFAULT&quot;<br>
&#123;<br>
  &quot;kind&quot;: &quot;DeploymentList&quot;,<br>
  &quot;apiVersion&quot;: &quot;apps/v1&quot;,<br>
  &quot;metadata&quot;: &#123;<br>
    &quot;resourceVersion&quot;: &quot;656580&quot;<br>
  &#125;,<br>
  &quot;items&quot;: [...]<br>
&#125;</code><br>
<br>是的，按预期工作!<br>
<br><h2>奖励：如何从Pod内部调用Kubernetes API</h2>与任何其他Kubernetes服务非常相似，Kubernetes API服务地址可通过环境变量提供给Pod：<br>
<br><code class="prettyprint">$ kubectl run -it --image curlimages/curl --restart=Never mypod -- sh<br>
$ env | grep KUBERNETES<br>
KUBERNETES_SERVICE_PORT=443<br>
KUBERNETES_PORT=tcp://10.96.0.1:443<br>
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1<br>
KUBERNETES_PORT_443_TCP_PORT=443<br>
KUBERNETES_PORT_443_TCP_PROTO=tcp<br>
KUBERNETES_SERVICE_PORT_HTTPS=443<br>
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443<br>
KUBERNETES_SERVICE_HOST=10.96.0.1</code><br>
<br>Pod通常还会将Kubernetes CA证书和服务帐户机密材料安装在<code class="prettyprint">/var/run/secrets/kubernetes.io/serviceaccount/</code>。因此，应用以上部分的知识，curl从 Pod调用Kubernetes API服务器的命令如下所示：<br>
<br><code class="prettyprint">$ curl https://$&#123;KUBERNETES_SERVICE_HOST&#125;:$&#123;KUBERNETES_SERVICE_PORT&#125;/apis/apps/v1 \<br>
  --cacert /var/run/secrets/kubernetes.io/serviceaccount/ca.crt \<br>
  --header &quot;Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)&quot;</code><br>
<br><h2>创建、读取、观看、更新、修补和删除对象</h2>Kubernetes API支持对Kubernetes Objects进行以下操作：<br>
<br><code class="prettyprint">GET    /&lt;resourcePlural>            -  Retrieve a list of type &lt;resourceName>.<br>
POST   /&lt;resourcePlural>            -  Create a new resource from the JSON<br>
                                       object provided by the client.<br>
GET    /&lt;resourcePlural>/&lt;name>     -  Retrieves a single resource with the<br>
                                       given name.<br>
DELETE /&lt;resourcePlural>/&lt;name>     -  Delete the single resource with the<br>
                                       given name.<br>
DELETE /&lt;resourcePlural>            -  Deletes a list of type &lt;resourceName>.<br>
PUT    /&lt;resourcePlural>/&lt;name>     -  Update or create the resource with the given<br>
                                       name with the JSON object provided by client.<br>
PATCH  /&lt;resourcePlural>/&lt;name>     -  Selectively modify the specified fields of<br>
                                       the resource.<br>
GET    /&lt;resourcePlural>?watch=true -  Receive a stream of JSON objects <br>
                                       corresponding to changes made to any<br>
                                       resource of the given kind over time.</code><br>
<br>API是RESTful的，因此上述HTTP方法在资源操作上的映射应该看起来很熟悉。<br>
<br><blockquote><br>即使文档仅提及JSON对象，如果Content-Type标头设置为application/yaml.</blockquote>以下是使用curl和YAML清单创建新对象的方法：<br>
<br><code class="prettyprint">$ curl $KUBE_API/apis/apps/v1/namespaces/default/deployments \<br>
  --cacert ~/.minikube/ca.crt \<br>
  --cert ~/.minikube/profiles/cluster1/client.crt \<br>
  --key ~/.minikube/profiles/cluster1/client.key \<br>
  -X POST \<br>
  -H 'Content-Type: application/yaml' \<br>
  -d '---<br>
apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
  name: sleep<br>
spec:<br>
  replicas: 1<br>
  selector:<br>
    matchLabels:<br>
      app: sleep<br>
  template:<br>
    metadata:<br>
      labels:<br>
        app: sleep<br>
    spec:<br>
      containers:<br>
      - name: sleep<br>
        image: curlimages/curl<br>
        command: [&quot;/bin/sleep&quot;, &quot;365d&quot;]</code><br>
<br>以下是如何获取默认命名空间中的所有对象：<br>
<br><code class="prettyprint">$ curl $KUBE_API/apis/apps/v1/namespaces/default/deployments \<br>
  --cacert ~/.minikube/ca.crt \<br>
  --cert ~/.minikube/profiles/cluster1/client.crt \<br>
  --key ~/.minikube/profiles/cluster1/client.key</code><br>
<br>以及如何通过名称和命名空间获取对象：<br>
<br><code class="prettyprint">$ curl $KUBE_API/apis/apps/v1/namespaces/default/deployments/sleep \<br>
  --cacert ~/.minikube/ca.crt \<br>
  --cert ~/.minikube/profiles/cluster1/client.crt \<br>
  --key ~/.minikube/profiles/cluster1/client.key</code><br>
<br>一种更高级的检索Kubernetes资源的方法是持续观察它们的变化：<br>
<br><code class="prettyprint">$ curl $KUBE_API/apis/apps/v1/namespaces/default/deployments?watch=true \<br>
  --cacert ~/.minikube/ca.crt \<br>
  --cert ~/.minikube/profiles/cluster1/client.crt \<br>
  --key ~/.minikube/profiles/cluster1/client.key</code><br>
<br><blockquote><br>请注意，只能监视一组资源。但是，你可以通过提供标签或字段选择器将结果集缩小到单个资源。</blockquote>以下是更新现有对象的方法：<br>
<br><code class="prettyprint">$ curl $KUBE_API/apis/apps/v1/namespaces/default/deployments/sleep \<br>
  --cacert ~/.minikube/ca.crt \<br>
  --cert ~/.minikube/profiles/cluster1/client.crt \<br>
  --key ~/.minikube/profiles/cluster1/client.key \<br>
  -X PUT \<br>
  -H 'Content-Type: application/yaml' \<br>
  -d '---<br>
apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
  name: sleep<br>
spec:<br>
  replicas: 1<br>
  selector:<br>
    matchLabels:<br>
      app: sleep<br>
  template:<br>
    metadata:<br>
      labels:<br>
        app: sleep<br>
    spec:<br>
      containers:<br>
      - name: sleep<br>
        image: curlimages/curl<br>
        command: [&quot;/bin/sleep&quot;, &quot;730d&quot;]  # &lt;-- Making it sleep twice longer</code><br>
<br>以下是如何修补现有对象：<br>
<br><code class="prettyprint">$ curl $KUBE_API/apis/apps/v1/namespaces/default/deployments/sleep \<br>
  --cacert ~/.minikube/ca.crt \<br>
  --cert ~/.minikube/profiles/cluster1/client.crt \<br>
  --key ~/.minikube/profiles/cluster1/client.key \<br>
  -X PATCH \<br>
  -H 'Content-Type: application/merge-patch+json' \<br>
  -d '&#123;<br>
  &quot;spec&quot;: &#123;<br>
    &quot;template&quot;: &#123;<br>
      &quot;spec&quot;: &#123;<br>
        &quot;containers&quot;: [<br>
          &#123;<br>
            &quot;name&quot;: &quot;sleep&quot;,<br>
            &quot;image&quot;: &quot;curlimages/curl&quot;,<br>
            &quot;command&quot;: [&quot;/bin/sleep&quot;, &quot;1d&quot;]<br>
          &#125;<br>
        ]<br>
      &#125;<br>
    &#125;<br>
  &#125;<br>
&#125;'</code><br>
<br><blockquote><br>请注意UPDATE和PATCH是相当棘手的操作。第一个受到各种版本冲突的影响，第二个的行为因使用的补丁策略而异。</blockquote>最后但同样重要的是 - 以下是如何删除对象集合：<br>
<code class="prettyprint">$ curl $KUBE_API/apis/apps/v1/namespaces/default/deployments \<br>
  --cacert ~/.minikube/ca.crt \<br>
  --cert ~/.minikube/profiles/cluster1/client.crt \<br>
  --key ~/.minikube/profiles/cluster1/client.key \<br>
  -X DELETE</code><br>
<br>以下是如何删除单个对象：<br>
<code class="prettyprint">$ curl $KUBE_API/apis/apps/v1/namespaces/default/deployments/sleep \<br>
  --cacert ~/.minikube/ca.crt \<br>
  --cert ~/.minikube/profiles/cluster1/client.crt \<br>
  --key ~/.minikube/profiles/cluster1/client.key \<br>
  -X DELETE</code><br>
<br><h2>使用 kubectl 调用 Kubernetes API</h2>上面带有证书和令牌的诡计很有趣。至少经历一次是一个很好的练习，可以巩固对客户端和服务器移动部件的理解。但是，当你有一个可以使用的kubectl时，每天都这样做可能会有点矫枉过正。<br>
<br><h2>使用kubectl代理调用Kubernetes API</h2>使用正确配置的kubectl工具，你可以通过使用kubectl proxy命令大大简化API访问。<br>
<br><blockquote><br>如果你已经使用可工作的kubectl，为什么还要直接调用Kubernetes API呢？<br>
  <br>
  <br>嗯，原因有很多。例如，你可能正在开发一个控制器并希望在不编写额外代码的情况下使用API查询。或者，你可能对kubectl操纵资源时的幕后操作不满意，这使你希望对Kubernetes对象上的操作进行更细粒度的控制。</blockquote>该命令在你的localhost和Kubernetes API服务器kubectl proxy之间创建一个代理服务器（或应用程序级网关）。但它必须不止于此。不然怎么会这么方便？<br>
<br>代理kubectl从调用者那里卸载了相互的客户端-服务器身份验证责任。由于调用者和代理之间的通信是通过localhost进行的，因此它被认为是安全的。代理本身使用kubeconfig文件中选择的当前上下文中的信息来处理客户端-服务器身份验证。<br>
<br>```<br>
$ kubectl config current-context<br>
cluster1<br>
<br>$ kubectl proxy --port=8080 &<br>
```<br>
<br>启动代理服务器后，调用 Kubernetes API 服务器就变得简单多了：<br>
<br><code class="prettyprint">$ curl localhost:8080/apis/apps/v1/deployments<br>
&#123;<br>
  &quot;kind&quot;: &quot;DeploymentList&quot;,<br>
  &quot;apiVersion&quot;: &quot;apps/v1&quot;,<br>
  &quot;metadata&quot;: &#123;<br>
    &quot;resourceVersion&quot;: &quot;660883&quot;<br>
  &#125;,<br>
  &quot;items&quot;: [...]<br>
&#125;</code><br>
<br>使用kubectl raw模式调用Kubernetes API我最近学到的另一个很酷的技巧是一些kubectl命令支持的原始模式：<br>
<br>```<br>
<h1>Sends HTTP GET request</h1>$ kubectl get --raw /api/v1/namespaces/default/pods<br>
<br><h1>Sends HTTP POST request</h1>$ kubectl create --raw /api/v1/namespaces/default/pods -f file.yaml<br>
<br><h1>Sends HTTP PUT request</h1>$ kubectl replace --raw /api/v1/namespaces/default/pods/mypod -f file.json<br>
<br><h1>Sends HTTP DELETE request</h1>$ kubectl delete --raw /api/v1/namespaces/default/pods<br>
```<br>
<br>kubectl是一个非常先进的工具，即使是简单的命令，比如kubectl get背后也有大量的代码。但是，当使用该--raw标志时，实现归结为将唯一的参数转换为API端点URL并调用原始REST API客户端。<br>
<br>这种方法的一些优点是：<br>
<br><blockquote><br>原始REST API客户端使用相同的身份验证意味着烘焙命令将使用（在 kubeconfig 文件中配置的任何内容）<br>
  -f这些命令通过标志支持传统的基于文件的清单输入。</blockquote>但也有一个缺点——我找不到任何PATCH或WATCH支持，因此curl访问为你提供了更多功能。<br>
<br><h2>奖励：Kubernetes API调用等效于kubectl命令</h2>我已经多次提到你可能对特定kubectl命令发出的请求的实际顺序不满意。但是你不读代码怎么能知道这个序列呢？<br>
<br>这是一个不错的技巧 - 你可以将<code class="prettyprint">-v 6</code>标志添加到任何kubectl命令，日志将变得如此冗长，以至于你将开始看到向Kubernetes API服务器发出的HTTP请求。<br>
<br>例如，你可以通过这种方式了解到该<code class="prettyprint">kubectl scale deployment</code>命令是通过对子资源的PATCH请求实现的<code class="prettyprint">/deployments/&lt;name>/scale</code>：<br>
<br><code class="prettyprint">$ kubectl scale deployment sleep --replicas=2 -v 6<br>
I0116 ... loader.go:372] Config loaded from file:  /home/vagrant/.kube/config<br>
I0116 ... cert_rotation.go:137] Starting client certificate rotation controller<br>
I0116 ... round_trippers.go:454] GET https://192.168.58.2:8443/apis/apps/v1/namespaces/default/deployments/sleep 200 OK in 14 milliseconds<br>
I0116 ... round_trippers.go:454] PATCH https://192.168.58.2:8443/apis/apps/v1/namespaces/default/deployments/sleep/scale 200 OK in 12 milliseconds deployment.apps/sleep scaled</code><br>
<br>看看<code class="prettyprint">kubectl apply -v 6</code>，结果可能非常有见地??<br>
<br><blockquote><br>想查看实际的请求和响应主体吗？将日志详细程度增加到8。</blockquote><h2>封装起来</h2>第一次访问Kubernetes API的需求可能很可怕 - 有很多新概念，如资源、API 组、种类、对象、集群、上下文、证书，哦，天哪！<br>
<br>但是一旦你在构建块上分解它并通过执行一些琐碎的任务（比如找出API服务器地址或使用curl调用一堆端点）获得一些实践经验，你很快就会意识到这个想法集群并不是真的一些新的东西——它只是多年来为我们服务的众所周知的机制的组合——REST架构风格、TLS 证书、JWT 令牌、对象方案等。<br>
<br>所以，不要害怕并运行一些查询！<br>
<br><strong>原文链接</strong>：<a href="https://iximiuz.com/en/posts/kubernetes-api-call-simple-http-client/">How To Call Kubernetes API using Simple HTTP Client</a><br>
<br><strong>译者</strong>：Mr.lzc，高级工程师、DevOpsDays、HDZ深圳核心组织者，目前供职于华为，从事云计算工作，专注于K8s、微服务领域。
                                
                                                              
</div>
            