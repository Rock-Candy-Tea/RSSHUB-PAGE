
---
title: '如何保护Kubernetes的机密信息'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=6935'
author: Dockone
comments: false
date: 2021-08-08 05:06:39
thumbnail: 'https://picsum.photos/400/300?random=6935'
---

<div>   
<br>现如今开发的大多数应用程序，或多或少都会用到一些敏感信息，用于执行某些业务逻辑。比如使用用户名密码去连接数据库，或者使用秘钥连接第三方服务。在代码中直接使用这些密码或者秘钥是最直接的方式，但同时也带来了很大的安全问题，如何保证密码、秘钥不被泄露。<br>
<br>如果你的应用程序已经被容器化，且使用Kubernetes（k8s），那情况会好很多。Kubernetes提供了一个原生资源，称为“Secret”，可用于管理和存储敏感信息。敏感信息被编码为未加密的Base64格式，并被存储在Secret对象中。Secret可以作为环境变量被注入到Pod内部的容器中，也可以作为数据卷挂载到容器内部。<br>
<br><blockquote><br>为了保证敏感信息的安全性，Secret对象应该被加密，并且应该使用Kubernetes RBAC机制对访问进行控制。如果你正在使用AWS公有云来托管Kubernetes集群，则可以利用AWS密钥管理服务（KMS）对静态数据进行加密。</blockquote>Kubernetes的清单文件通常被提交到代码仓库中以进行版本控制。但是你可能不希望将敏感信息以纯文本或Base64编码字符串的形式提交到Git代码仓库中。我们都应该知道为什么，这不安全！但是，你在Kubernetes集群之外将敏感数据保存在何处，以确保它们是安全的？<br>
<br>有很多方法可以解决这个问题。下面列出了其中几个：<br>
<h3>选项1：加密纯文本敏感数据，然后再提交到Git代码仓库中</h3><ol><li>使用对称或非对称算法加密纯文本敏感数据。</li><li>使用Kubernetes Custom Resource Definition（CRD）创建自定义的Secret对象，以使用加密的文本数据。</li><li>创建一个自定义Kubernetes控制器，该控制器读取自定义Secret对象中的加密信息，并在运行时解密，并创建一个原生的Secret对象。</li></ol><br>
<br>使用这种方法，你可以将加密的数据提交到Git代码仓库中。而且它没有风险，因为数据是加密的，只能用你的私钥解密。但是你把私钥放在哪里？<br>
<br>如何存储加密密钥和管理整个加解密过程，可以使用Bitnami的<a href="https://github.com/bitnami-labs/sealed-secrets">Sealed Secrets</a>。<br>
<h3>选择2：使用第三方服务来存储敏感数据</h3><ol><li>你可以将敏感数据存储到第三方服务中，如AWS Secrets Manager或HashiCorp Vault。</li><li>创建自定义Kubernetes控制器，基于配置从这些服务中获取机密信息，并在运行时创建Kubernetes Secret对象。</li></ol><br>
<br><a href="https://github.com/external-secrets/kubernetes-external-secrets">External Secrets</a>项目可以帮助你实现选项2。<br>
<br><blockquote><br>你还可以增强应用程序逻辑，以便在应用程序启动时从第三方服务读取机密信息，但这里的整体思想是将机密信息管理与应用程序业务逻辑分离开来，并利用Kubernetes的功能来进行相同的管理。</blockquote><h3>快速概览Sealed Secrets</h3>在Sealed Secret开源项目中，你可以将你的Secret加密为一个SealedSecret，这样就可以安全地存储，甚至可以存储到公共存储库中。SealedSecret只能由运行在目标集群中的控制器解密，其他人，甚至包括原始作者，都无法从SealedSecret获得原始的Secret。<br>
<br><strong>Sealed Secrets</strong>由两部分组成：<br>
<ol><li>服务器端的控制器</li><li>客户端工具：<code class="prettyprint">kubeseal</code></li></ol><br>
<br><code class="prettyprint">kubeseal</code>使用非对称加密来加密数据，然后只有服务端的控制器才能解密数据。<br>
<br>这些加密数据被编码在SealedSecret资源中，你可以将其视为创建Secret的配方。<br>
<br>下面是如何使用Sealed Secrets来管理Secret的具体步骤。<br>
<br>1、安装<code class="prettyprint">kubeseal</code>，这是一个客户端工具，可以帮助你创建SealedSecret<br>
<pre class="prettyprint">> wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.15.0/kubeseal-linux-amd64 -O kubeseal<br>
<br>
> sudo install -m 755 kubeseal /usr/local/bin/kubeseal<br>
</pre><br>
2、安装服务器端控制器，为SealedSecret创建Custom Resource Definition（CRD）<br>
<pre class="prettyprint">> kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.15.0/controller.yaml<br>
<br>
rolebinding.rbac.authorization.k8s.io/sealed-secrets-service-proxier created<br>
role.rbac.authorization.k8s.io/sealed-secrets-key-admin created<br>
clusterrole.rbac.authorization.k8s.io/secrets-unsealer created<br>
deployment.apps/sealed-secrets-controller created<br>
customresourcedefinition.apiextensions.k8s.io/sealedsecrets.bitnami.com created<br>
service/sealed-secrets-controller created<br>
clusterrolebinding.rbac.authorization.k8s.io/sealed-secrets-controller created<br>
serviceaccount/sealed-secrets-controller created<br>
role.rbac.authorization.k8s.io/sealed-secrets-service-proxier created<br>
rolebinding.rbac.authorization.k8s.io/sealed-secrets-controller created<br>
</pre><br>
3、验证sealed-secret controller Pod是否运行<br>
<pre class="prettyprint">> kubectl get pods -n kube-system -l name=sealed-secrets-controller<br>
<br>
NAME                                         READY   STATUS RESTARTS   AGE<br>
sealed-secrets-controller-7c766b885b-d5r2r   1/1     Running   0          7m39s<br>
</pre><br>
如果你查看Pod的日志，你将看到控制器为自己创建的一对秘钥，这对秘钥将被用于加解密过程。<br>
<pre class="prettyprint">> kubectl logs sealed-secrets-controller-7c766b885b-d5r2r -n kube-system<br>
<br>
controller version: v0.15.0<br>
2021/05/01 20:13:34 Starting sealed-secrets controller version: v0.15.0<br>
2021/05/01 20:13:34 Searching for existing private keys<br>
2021/05/01 20:13:35 New key written to kube-system/sealed-secrets-keymt6dg<br>
2021/05/01 20:13:35 Certificate is <br>
-----BEGIN CERTIFICATE-----<br>
MIIErjCCApagAwIBAgIRAJqYfaZsali26I8pvBXoFGYwDQYJKoZIhvcNAQELBQAw<br>
ADAeFw0yMTA1MDEyMDEzMzVaFw0zMTA0MjkyMDEzMzVaMAAwggIiMA0GCSqGSIb3<br>
DQEBAQUAA4ICDwAwggIKAoICAQDp/yO5PY8ACHBDuguhtfpOwlbScK9hZorJloyx<br>
ixVCc57j1zMSX0pSVcrk1Yuyf6sYvBQtDi16kM70z6y/ODiz+9g87K/jY7B0UAoi<br>
mpzM/T0tWJiG9ixyNMZhHoNREauokSlbERq3Jl8ZNTfmxHWhLH7DhkJ7MdpQfMpK<br>
a3XHcSZyz1mXFqv+OSCCwllWCRHmHgp/vqudAv8+NYm0gnAxKt2fjlv/ObX8J1RI<br>
CtLnlsCpp/9SyVcSTeYYaqjUsI7fTUZ7tkTE/bdQHwf3xe4DhUty7xLqMF1OPSPw<br>
EetL8fGO0VqoSQFKQ0Bf78+8vhAA2cwkuqB6vQQm9pT3yC5niSCUo+jwFcfyknjr<br>
yx8DINbq6K9B40EXh8X7w4I6zwYpyT0GoNU54wW0ki8pHRm7EnFeBOkUvNspzmKn<br>
t/EZEDVq74Kkl/BRNRvKHYlwudSoJuvvX6JM8DVvRp0lMPnXnG3RLSmCP3gEFQBZ<br>
DhbnkwO+6ADX9Q4vyqelWoHWdVGVULDlMDhSzvEhFFgPcZXzWTShH81vfl8M6lpT<br>
U0ysZkA6i3A29XEJpPj35yWPBDWmKF5fLM3ChMt/NSJEeoJN1RboPDAgVUTxEW59<br>
q+Tq09/zlYD7Ch8PNc3IWNXjFNXmCAAOw9Z1VBbD8p6LrC5JvBtPoWYqufWVXQD9<br>
KDe+6wIDAQABoyMwITAOBgNVHQ8BAf8EBAMCAAEwDwYDVR0TAQH/BAUwAwEB/zAN<br>
BgkqhkiG9w0BAQsFAAOCAgEAvu//VzDREYZPPIW1maTxo9C/nHEEuOP0rQU3zVQr<br>
bBYf8N0b5wpCllESCgi0JDJJXrE8KrjfdtawjoBrBlHOdWHF+fIot2KbrC/i37em<br>
/ulMAgiiJzrKM/ExJuCuH60fsSIx4wrg46tQpU8jHFWq7nGnsaE+UN3QPjuvQ+qo<br>
KKDSBLDxLx+q9vBfaXElblh4okUI8Pr4UEEJrYiPzPM6nA9EPpy53N3si4jyDJJb<br>
2IsCUa2bW6iBhpyZOQQUPn22ziWRQ/sYYNmtP/gX0rwtk+Rr8TTdzPYGZcYfMQ6O<br>
TFq4Zo2/TnpCL/CUr2DiSuF2qdWGGvbQOENYq2FNuDI4zeljElcZHXA8nhpbNSJs<br>
7VNqqz5ZTFCKyL0Gn6SawGT7EdwBT2AD3F33Qd/7bXG/On7KdVw6FKHbZOR2RcoS<br>
YFQv7Xr8g/4atQjxDa7R5+zkxd5unsvpFhYM1UfNJc4cjJ7SmfCCHoPGiwZ0OgqB<br>
6SvUVU64QmMMJ/jYAJkYMOakSHaRITHAvvBjpAMKxSjjb7qZD5FnpXLhRY9lNiY6<br>
MnnQRxJskCw+R6geIAHTMzAofMfc1haIEr+3oMFZfyh1LFFsz3B4hMxXYKrWYDje<br>
+96bhAY9X7L0UfREjmw8HCeZneEuBJjX9z/PyIeMdhViLh9uO/MAL1MBxdBVA55+<br>
LW8=<br>
-----END CERTIFICATE-----<br>
<br>
2021/05/01 20:13:35 HTTP server serving on :8080<br>
</pre><br>
运行以下命令查看公钥/私钥信息。<br>
<pre class="prettyprint">> kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key -o yaml<br>
</pre><br>
4、创建一个名为secrets.yaml的Secret清单文件<br>
<pre class="prettyprint">apiVersion: v1<br>
data:<br>
DB_PWD: cGFzc3dvcmQ= //base64 encoded<br>
DB_USER: cm9vdA==    //base64 encoded<br>
kind: Secret<br>
metadata:<br>
name: db-secrets<br>
</pre><br>
现在让我们使用<code class="prettyprint">kubeseal</code>命令，将secrets.yaml转变为SealedSecret资源清单文件。<br>
<pre class="prettyprint">> kubeseal --format=yaml < secret.yaml > sealed-secret.yaml<br>
<br>
> cat sealed-secret.yaml <br>
<br>
apiVersion: bitnami.com/v1alpha1<br>
kind: SealedSecret<br>
metadata:<br>
creationTimestamp: null<br>
name: db-secrets<br>
namespace: default<br>
spec:<br>
encryptedData:<br>
DB_PWD: AgDaCRi27RV4/sVI2ok7JlqBSKT5+c7gGJog+...<br>
DB_USER: AgAZG67CrrOBnyKIKha7xhJulr+CQGPaE/PpsjvY8jJR0IDO2...<br>
template:<br>
metadata:<br>
  creationTimestamp: null<br>
  name: db-secrets<br>
  namespace: default<br>
</pre><br>
在上面的步骤中，<code class="prettyprint">kubeseal</code>从Kubernetes集群获取公钥并使用该公钥加密数据。<br>
<br>5、让我们使用SealedSecret资源清单文件，在Kubernetes中创建资源。<br>
<pre class="prettyprint">> kubectl apply -f sealed-secret.yaml<br>
</pre><br>
如果你再次检查控制器的日志，你将看到控制器拦截了请求，并解密来自SealedSecret的加密数据，数据被解密后，将创建Kubernetes的Secret对象。<br>
<pre class="prettyprint">> kubectl logs sealed-secrets-controller-7c766b885b-d5r2r -n kube-system<br>
<br>
2021/05/01 20:38:06 Updating default/db-secrets<br>
2021/05/01 20:38:06 Event(v1.ObjectReference&#123;Kind:"SealedSecret", Namespace:"default", Name:"db-secrets", UID:"fd89a7e7-c81a-4110-9de6-6b65195169d3", APIVersion:"bitnami.com/v1alpha1", ResourceVersion:"19365", FieldPath:""&#125;): type: 'Normal' reason: 'Unsealed' SealedSecret unsealed successfully<br>
</pre><br>
一旦创建了Kubernetes Secret对象，就可以将它作为环境变量注入到容器中，或者作为数据卷挂载。<br>
<br>上面步骤4中创建的SealedSecret资源清单文件可以被提交到Git代码仓库中。secrets.yaml文件可以丢弃，因为它不再需要了。被存储在sealed-secret.yaml文件中的数据是安全的，它是被加密的，且只能由运行在k8s集群中的Controller解密。<br>
<br>希望这篇文章能让你知道如何保护Kubernetes的机密信息。<br>
<br><strong>原文链接：<a href="https://waswani.medium.com/securing-secrets-in-kubernetes-c78c7bcd433">Securing Secrets in Kubernetes</a>  （翻译：钟涛）</strong>
                                
                                                              
</div>
            