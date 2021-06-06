
---
title: 'Kubernetes认证入门指南'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=3315'
author: Dockone
comments: false
date: 2021-06-06 00:39:15
thumbnail: 'https://picsum.photos/400/300?random=3315'
---

<div>   
<br>Kubernetes用来执行安全访问和权限的步骤有3个——认证（Authentication）、授权（Authorization）和准入（Admission）。在本文中，我们先开始了解认证（Authentication）。<br>
<br>在认证中第一个需要考虑的是身份认证（Identity）。<br>
<br><h2>身份认证简介</h2>Kubernetes假设“user”是在Kubernetes之外管理的。在生产环境中，可以采用LDAP（轻量级目录访问协议）、SSO（单点登录）、Kerberos或SAML（安全断言置标语言）进行身份认证管理。在开发或测试环境中，其他的认证策略也有可能会被使用到。<br>
<br>在Kubernetes中没有表达普通用户的对象，因此不能通过API将普通用户添加到集群中。<br>
<br><h2>认证策略概览</h2>Kubernetes通过认证插件使用认证代理、bearer token、客户端证书或HTTP基本授权来认证API请求。当向API server发出HTTP请求时，插件会尝试将以下属性与请求关联起来：<br>
<ul><li>Username：识别最终用户的字符串</li><li>UID：识别最终用户的字符串，并试图比username格式更为一致，同时每个UID都是独特的。</li><li>Groups：一组字符串，将用户与一组常见的分组用户关联起来</li><li>Extra fields：字符串的映射，保存着授权者认为可能有用的额外信息。</li></ul><br>
<br>所有这些值对认证系统来说都是不透明的，只有在authorizer对其进行解释时才有意义。Kubernetes管理员通常会启用多种认证方法。所需的两种最基本的方法是——服务账户的service account token再加上至少一种其他的用户认证方法。<br>
<br><h2>X509客户端证书</h2><ul><li>从Kubernetes 1.4开始，客户端证书可以使用证书组织字段来表明用户的组成员资格。</li><li>要让一个用户拥有多个组成员资格，需要在证书中包含多个组织字段。</li><li>通过向API server传递 --client-ca-file=<FILE>选项来启用客户端证书认证。</li><li>引用的文件必须包含一个或多个证书颁发机构，用于验证提交给API server的客户证书。</li><li>如果出示客户端证书并进行验证，则使用主体的通用名作为请求的用户名。</li></ul><br>
<br>例如，使用openssl命令行工具来生成证书签名请求：<br>
<pre class="prettyprint">openssl req -new -key <pem_file>.pem -out <out-csr-file>.pem -subj "/CN=admin/O=prod/O=dev/O=uat"<br>
</pre><br>
<br>这将为用户名admin创建一个CSR（证书签名请求），该用户名属于以下3个组：prod、dev和uat。<br>
<br><h2>静态Token文件</h2>当在命令行中给出--token-auth-file=<FILENAME>选项时，API Server会从文件中读取bearer token。如今，token无限期存在，如果不重启API Server，就无法更改token列表。Token文件是一个csv文件，至少有3列：token、用户名、user uid，后面可能还会有组名（这是可选的）。<br>
<pre class="prettyprint">token, user, uid,"prod,dev,uat"<br>
</pre><br>
<br>请注意：如果你有超过1个组，该列必须使用双引号。<br>
<br><h2>在请求中放入一个bearer token</h2>当使用来自HTTP客户端的bearer token认证时，API server期望授权请求头的值为Bearer <Token>。bearer token必须是一个字符序列，可以只需使用HTTP的编码和引用功能就可以将其放在HTTP请求头的值中。例如，如果Bearer Token是ad644f3f-bfch-295b-75bk-h9g8ngf36hb6，那么它将出现在HTTP请求头中，如下所示：<br>
<pre class="prettyprint">Authorization: Bearer ad644f3f-bfch-295b-75bk-h9g8ngf36hb6<br>
</pre><br>
<br><h2>静态密码文件</h2>通过向API server传递--basic-auth-file=<FILENAME>选项来启用基本认证。现在，基本的认证凭证将无限期地持续下去，而且如果不重新启动 API server，就无法更改密码。<br>
<br>基本的 auth 文件是一个 csv 文件，至少有 3 列：密码、用户名、用户 ID。在Kubernetes 1.6及以后的版本中，你可以指定一个可选的第4列，包含逗号分隔的组名。如果你有多个组，你必须用双引号(")括住第4列的值。<br>
<pre class="prettyprint">password,user,uid,"group1,group2,group3"<br>
</pre><br>
<br>当使用来自HTTP客户端的基本认证时，API server期望Authorizationheader的值为：<br>
<pre class="prettyprint">Basic BASE64ENCODED(USER:PASSWORD)<br>
</pre><br>
<br><h2>服务账户Token</h2>服务账户是一个自动启用的身份认证器，它使用签名的bearer token来验证请求。该插件需要2个可选的标志：<br>
<pre class="prettyprint">--service-account-key-file<br>
</pre><br>
<br>一个包含PEM编码密钥的文件，用于签署bearer token。如果没有指定，将使用API server的TLS密钥。<br>
<pre class="prettyprint">--service-account-lookip<br>
</pre><br>
<br>如果启用了，从API sever上删除的token将被撤销。<br>
<br>服务账户通常由API server自动创建，并通过ServiceAccount 准入控制器与集群中运行的Pod相关联。<br>
<br>Bearer Token会被挂载到众所周知的位置的Pod中，并允许集群内进程与API Server对话。账户可以使用PodSpec的serviceAccountName字段与Pod显式关联。<br>
<br>注意，serviceAccountName通常会被省略，因为这是自动完成的。<br>
<br><h2>练习实践：使用ServiceAccount Token</h2>使用以下命令可以创建ServiceAccount：<br>
<pre class="prettyprint">kubectl create serviceaccount testuser<br>
</pre><br>
<br>创建的密钥包含API server的公共CA和签名的JSON web Token（JWT）。以下命令可以显示出揭示相关密钥的yaml：<br>
<pre class="prettyprint">kubectl get serviceaccount testuser -o yaml<br>
</pre><br>
<br>以下命令可以显示可用Token：<br>
<pre class="prettyprint">kubectl get secrets<br>
</pre><br>
<br>要获得编码的token数据，请输入：<br>
<pre class="prettyprint">kubectl get secret testuser-token-mgtnp -o yaml<br>
</pre><br>
<br>你可以将编码后的token数据复制并粘贴到<a href="https://jwt.io/" rel="nofollow" target="_blank">https://jwt.io/</a> 以查看有效载荷。使用你选择的编辑器输入以下yaml文件（test-pod.yaml），以运行一个pod：<br>
<pre class="prettyprint">apiVersion: v1 <br>
kind: pod <br>
metadata:  <br>
name: test-pod <br>
spec:  <br>
serviceAccountName: testuser  <br>
container:  <br>
- name: alpine:3.7    <br>
command:    <br>
- "sh"    <br>
- "-c"    <br>
- "sleep 100"<br>
</pre><br>
<br>然后使用以下命令启动pod：<br>
<pre class="prettyprint">kubectl apply -f test-pod.yaml<br>
</pre><br>
<br>使用describe可以查看更详细的内容：<br>
<pre class="prettyprint">kubectl describe test-pod<br>
</pre><br>
<br>现在，我们有一个正在运行的pod，名为test-pod，让我们进入交互模式并运行一个shell：<br>
<pre class="prettyprint">kubectl exec -it test-pod -- sh<br>
</pre><br>
<br>如果你想在docker容器内运行shell，所使用的命令与docker命令类似。这时，我们将会收到一个提示，然后进入Alpine Linux系统，该系统是在pod中的一个容器内运行的。为了打开被复制到容器中的token，你需要运行以下命令：<br>
<pre class="prettyprint">cat /var/run/sercrets/kubernetes.io/serviceaccount/token<br>
</pre><br>
<br>复制输出并将该token粘贴在<a href="https://jwt.io/" rel="nofollow" target="_blank">https://jwt.io/</a>上Encoded部分。在另一边你会得到token的类型、命名空间、ServiceAccount名称、密钥名称等。<br>
<br>这几乎以一种十分直观的方式向你说明了Kubernetes如何在token中进行身份验证有效载荷。<br>
<blockquote><br>作者：<br>
  Sudip Sengupta<br>
  链接：<br>
  <a href="https://dzone.com/articles/kubernetes-authentication" rel="nofollow" target="_blank">https://dzone.com/articles/kub ... ation</a></blockquote>
                                
                                                              
</div>
            