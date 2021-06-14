
---
title: '入门指南丨上手理解Deployment、Services和Ingress'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210607210417210.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
author: Dockone
comments: false
date: 2021-06-14 06:07:45
thumbnail: 'https://img-blog.csdnimg.cn/20210607210417210.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
---

<div>   
<br>在之前的文章中，我们了解了Kubernetes中的基本概念，其硬件结构，不同的软件组件（例如Pod、Deployment、StatefulSet、Services、Ingress和Persistent Volumes），并了解了如何在服务之间与外部进行通信。<br>
<br>在本文中，我们将了解到：<br>
<ol><li><br>使用MongoDB数据库创建NodeJS后端</li><li><br>编写Dockerfile来容器化我们的应用程序</li><li><br>创建Kubernetes Deployment脚本以启动Pod</li><li><br>创建Kubernetes Service脚本以定义容器与外界之间的通信接</li><li><br>部署Ingress Controller以请求路由</li><li><br>编写Kubernetes Ingress脚本来定义与外界的通信。</li></ol><br>
<br><img src="https://img-blog.csdnimg.cn/20210607210417210.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="图片" referrerpolicy="no-referrer"><br>
<br>由于我们的代码可以从一个节点重定向到另一个节点（例如，一个节点没有足够的内存，所以工作将重新调度到另一个具有足够内存的节点上），因此保存在节点上的数据容易丢失 ，意味着MongoDB 数据不稳定。在下一篇文章中，我们将讨论数据持久性问题以及如何使用Kubernetes持久卷安全地存储我们的持久数据。<br>
<br>在本文中，我们将使用NGINX作为Ingress Controller和Azure容器镜像仓库来存储我们的自定义Docker镜像。文中编写所有脚本都可以在Stupid Simple Kubernetes git repo中找到，如有需要可访问链接获取:<br>
<br><a href="http://GitHub%20-%20CzakoZoltan08/StupidSimpleKubernetes-AKS"></a><a href="http://github/" rel="nofollow" target="_blank">http://GitHub</a> - CzakoZoltan08/StupidSimpleKubernetes-AKS<br>
<br>请注意：这些脚本不限定于某个平台，因此您可以使用其他类型的云提供程序或带有K3s的本地集群来实践本教程。我之所以建议使用K3s，因为它非常轻量，所有依赖项都被打包在一个小于100MB的单个二进制文件中。更重要的是，它是一种高可用的、经过CNCF认证的Kubernetes发行版，专门用于资源受限的环境中的生产工作负载。有关更多信息，您可以访问官方文档：<br>
<br><a href="https://docs.rancher.cn/k3s/"></a><a href="https://docs.rancher.cn/k3s/" rel="nofollow" target="_blank">https://docs.rancher.cn/k3s/</a><br>
<br><h2>前期准备</h2>在开始本教程之前，请确保您已安装Docker。同时也要安装kubectl。<br>
<br>Kubectl安装链接：<br>
<br><a href="https://kubernetes.io/docs/tasks/tools/#install-kubectl-on-windows"></a><a href="https://kubernetes.io/docs/tasks/tools/#install-kubectl-on-windows" rel="nofollow" target="_blank">https://kubernetes.io/docs/tas ... ndows</a><br>
<br>在本教程中使用的Kubectl命令可以在Kubectl  cheat sheet（<a href="https://kubernetes.io/docs/reference/kubectl/cheatsheet/"></a><a href="https://kubernetes.io/docs/reference/kubectl/cheatsheet/" rel="nofollow" target="_blank">https://kubernetes.io/docs/ref ... heet/</a>）中找到。<br>
<br>在本教程中，我们将使用Visual Studio Code，但这不是必要的，你也可以使用其他的编辑器。<br>
<br><h2>创建可用于生产的微服务架构</h2><strong>将应用程序容器化</strong><br>
<br>第一步，创建NodeJS后端的Docker镜像。创建镜像后，我们会将其推送到容器镜像仓库中，在该镜像仓库中可以访问它，并且可以通过Kubernetes服务（在本例中为Azure Kubernetes Service）拉取。<br>
<pre class="prettyprint">The Docker file for NodeJS:  <br>
FROM node:13.10.1  <br>
WORKDIR /usr/src/app  <br>
COPY package*.json ./  <br>
RUN npm install  <br>
<h1>Bundle app source</h1>COPY . .  <br>
EXPOSE 3000  <br>
CMD [ "node", "index.js" ]<br>
</pre><br>
<br>在第一行中，我们需要根据要创建后端服务的镜像进行定义。在这种情况下，我们将使用Docker Hub中13.10.1版的官方节点镜像。<br>
<br>在第3行中，我们创建一个目录来将应用程序代码保存在镜像中。这将是您的应用程序的工作目录。<br>
<br>该镜像已经安装了Node.js和NPM，因此下一步我们需要使用npm命令安装您的应用程序依赖项。<br>
<br>请注意，要安装必需的依赖项，我们不用复制整个目录，而只需复制package.json，这使我们可以利用缓存的Docker层。<br>
<br>有关高效Dockerfile的更多信息，请访问以下链接：<br>
<br><a href="http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-dot-js/"></a><a href="http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-dot-js/" rel="nofollow" target="_blank">http://bitjudo.com/blog/2014/0 ... t-js/</a><br>
<br>在第9行中，我们将源代码复制到工作目录中，在第11行中，将其暴露在端口3000上（如果需要，您可以选择另一个端口，但请确保同步更改Kubernetes Service脚本。）<br>
<br>最后，在第13行，我们定义了运行应用程序的命令（在Docker容器内部）。请注意，每个Dockerfile中应该只有一个CMD指令。如果包含多个，则只有最后一个才会生效。<br>
<br>现在，我们已经定义了Dockerfile，我们将使用以下Docker命令从该Dockerfile中构建镜像（使用Visual Studio Code的Terminal或在Windows上使用CMD）：<br>
<pre class="prettyprint">docker build -t node-user-service:dev .<br>
</pre><br>
<br>请注意Docker命令末尾的小圆点，这意味着我们正在从当前目录构建镜像，因此请确保您位于Dockerfile所在的同一文件夹中（在本例中，是repo的根文件夹）。<br>
<br>要在本地运行镜像，我们可以使用以下命令：<br>
<pre class="prettyprint">docker run -p 3000:3000 node-user-service:dev  <br>
</pre><br>
<br>若要将此镜像推送到我们的Azure容器镜像仓库，我们必须使用以下格式标记它<container-registry-login-service>/<image-name>:<tag>：，在本例中如下所示：<br>
<pre class="prettyprint">docker tag node-user-service:dev stupidsimplekubernetescontainerregistry.azurecr.io/node-user-service:dev<br>
</pre><br>
<br>最后一步是使用以下Docker命令将其推送到我们的容器镜像仓库中：<br>
<pre class="prettyprint">docker push stupidsimplekubernetescontainerregistry.azurecr.io/node-user-service:dev<br>
</pre><br>
<br><strong>使用部署脚本创建Pod</strong><br>
<br><strong>NodeJs后端</strong><br>
<br>接下来，定义Kubernetes Deployment脚本，该脚本将自动为我们管理Pod。<br>
<pre class="prettyprint">apiVersion: apps/v1  <br>
kind: Deployment  <br>
metadata:  <br>
name: node-user-service-deployment  <br>
spec:  <br>
selector:  <br>
matchLabels:  <br>
  app: node-user-service-pod  <br>
replicas: 3  <br>
template:  <br>
metadata:  <br>
  labels:  <br>
    app: node-user-service-pod  <br>
spec:  <br>
  containers:  <br>
    - name: node-user-service-container  <br>
      image: stupidsimplekubernetescontainerregistry.azurecr.io/node-user-service:dev  <br>
      resources:  <br>
        limits:  <br>
          memory: "256Mi"  <br>
          cpu: "500m"  <br>
      imagePullPolicy: Always  <br>
      ports:  <br>
        - containerPort: 3000<br>
</pre><br>
<br>Kubernetes API可以查询和操作Kubernetes集群中对象的状态（例如Pod、命名空间、ConfigMap等）。如第一行中所指定，这个API的当前稳定版本为1。<br>
<br>在每个Kubernetes .yml脚本中，我们必须使用kind关键字定义Kubernetes资源类型（Pods、Deployments、Service等）。因此，你可以看到，我们在第2行中定义了我们想使用Deployment资源。<br>
<br>Kubernetes允许您向资源中添加一些元数据。这样一来，您就可以更轻松地识别、过滤和参考资源。<br>
<br>在第5行中，我们定义了该资源的规范。在第8行中，我们指定此Deployment应仅应用于标签为app:node-user-service-pod的资源中，在第9行中可以看出我们想要创建同一Pod的3个副本。<br>
<br>Template（从第10行开始）定义了Pod。在这里，我们将标签app:node-user-service-pod添加到每个Pod。这样，Deployment将识别它们。在第16和17行中，我们定义了应在pod内部运行哪种Docker容器。如您在第17行中看到的那样，我们将使用Azure容器镜像仓库中的Docker镜像，该镜像是在上一节中构建并推送的。<br>
<br>我们还可以为Pod定义资源限制，避免Pod资源不足（当其中一个Pod使用所有资源而其他Pod无法使用它们时）。此外，当您为Pod中的容器指定资源请求时，调度程序将使用此信息来决定将Pod放置在哪个节点上。当您为容器指定资源限制时，kubelet会强制执行这些限制，从而不允许运行中的容器使用超出您设置的资源限制。kubelet还至少保留该系统资源的“请求”量。请注意，如果您没有足够的硬件资源（例如CPU或内存），则永远无法调度pod。<br>
<br>最后一步是定义用于通信的端口。在本例中，我们使用端口3000。此端口号应与Dockerfile中暴露的端口号相同。<br>
<br><strong>MongoDB</strong><br>
<br>MongoDB数据库的Deployment脚本非常相似。唯一的区别是我们必须指定卷挂载（数据会被保存到节点上的文件夹中）。<br>
<pre class="prettyprint">apiVersion: apps/v1  <br>
kind: Deployment  <br>
metadata:  <br>
name: user-db-deployment  <br>
spec:  <br>
selector:  <br>
matchLabels:  <br>
  app: user-db-app  <br>
replicas: 1  <br>
template:  <br>
metadata:  <br>
  labels:  <br>
    app: user-db-app  <br>
spec:  <br>
  containers:  <br>
    - name: mongo  <br>
      image: mongo:3.6.4  <br>
      command:  <br>
        - mongod  <br>
        - "--bind_ip_all"  <br>
        - "--directoryperdb"  <br>
      ports:  <br>
        - containerPort: 27017  <br>
      volumeMounts:  <br>
        - name: data  <br>
          mountPath: /data/db  <br>
      resources:  <br>
        limits:  <br>
          memory: "256Mi"  <br>
          cpu: "500m"  <br>
  volumes:  <br>
    - name: data  <br>
      persistentVolumeClaim:  <br>
        claimName: static-persistence-volume-claim-mongo<br>
</pre><br>
<br>在本例中，我们直接从DockerHub使用了官方MongoDB镜像（第17行）。在第24行中定义了卷安装。在讨论Kubernetes持久卷时，我们将在下一篇文章中解释最后四行。<br>
<br><strong>创建用于网络访问的服务</strong><br>
<br>现在我们已经启动了Pod，并开始定义容器之间以及与外部世界的通信。为此，我们需要定义一个服务。Service与Deployment之间的关系是一对一的，因此对于每个Deployment，我们都应该有一个Service。Deployment还可以管理Pod的生命周期，并且负责监控它们，而Service负责启用对一组Pod的网络访问。<br>
<pre class="prettyprint">apiVersion: v1  <br>
kind: Service  <br>
metadata:  <br>
name: node-user-service  <br>
spec:  <br>
type: ClusterIP  <br>
selector:  <br>
app: node-user-service-pod  <br>
ports:  <br>
- port: 3000  <br>
  targetPort: 3000<br>
</pre><br>
<br>这个.yml脚本的重要部分是selector，它定义了如何识别要从此Service引用的Pod（由Deployment创建）。在第8行中我们可以看到的，Selector 为app:node-user-service-pod，因为先前定义的Deployment中的Pod被标记为这样。另一个重要的事情是定义容器端口和服务端口之间的映射。在这种情况下，传入请求将使用第10行中定义的3000端口，并将它们路由到第11行中定义的端口。<br>
<br>MongoDB pod的Kubernetes Service脚本非常相似。我们只需要更新Selector和端口。<br>
<pre class="prettyprint">apiVersion: v1  <br>
kind: Service  <br>
metadata:  <br>
name: user-db-service  <br>
spec:  <br>
clusterIP: None  <br>
selector:  <br>
app: user-db-app  <br>
ports:  <br>
- port: 27017  <br>
  targetPort: 27017<br>
</pre><br>
<br><strong>配置外部流量</strong><br>
<br>为了与外界通信，我们需要定义一个Ingress Controller并使用Ingress Kubernetes资源指定路由规则。<br>
<br>要配置NGINX ingress controller，我们将使用可以以下链接中的脚本：<br>
<br><a href="https://github.com/CzakoZoltan08/StupidSimpleKubernetes-AKS/blob/master/manifest/ingress-controller/nginx-ingress-controller-deployment.yml"></a><a href="https://github.com/CzakoZoltan08/StupidSimpleKubernetes-AKS/blob/master/manifest/ingress-controller/nginx-ingress-controller-deployment.yml" rel="nofollow" target="_blank">https://github.com/CzakoZoltan ... t.yml</a><br>
<br>这是一个通用脚本，无需修改即可应用（详细解释NGINX Ingress Controller不在本文讨论范围之内）。<br>
<br>下一步是定义“负载均衡器”，该负载均衡器将用于使用公共IP地址路由外部流量（云提供商提供负载均衡器）。<br>
<pre class="prettyprint">kind: Service  <br>
apiVersion: v1  <br>
metadata:  <br>
name: ingress-nginx  <br>
namespace: ingress-nginx  <br>
labels:  <br>
app.kubernetes.io/name: ingress-nginx  <br>
app.kubernetes.io/part-of: ingress-nginx  <br>
spec:  <br>
externalTrafficPolicy: Local  <br>
type: LoadBalancer  <br>
selector:  <br>
app.kubernetes.io/name: ingress-nginx  <br>
app.kubernetes.io/part-of: ingress-nginx  <br>
ports:  <br>
- name: http  <br>
  port: 80  <br>
  targetPort: http  <br>
- name: https  <br>
  port: 443  <br>
  targetPort: https<br>
</pre><br>
<br>现在我们已经启动并运行了Ingress controller和负载均衡器，于是我们可以定义Ingress Kubernetes资源来指定路由规则。<br>
<pre class="prettyprint">apiVersion: extensions/v1beta1  <br>
kind: Ingress  <br>
metadata:  <br>
name: node-user-service-ingress  <br>
annotations:  <br>
kubernetes.io/ingress.class: "nginx"  <br>
nginx.ingress.kubernetes.io/rewrite-target: /$2  <br>
spec:  <br>
rules:  <br>
- host: stupid-simple-kubernetes.eastus2.cloudapp.azure.com  <br>
  http:  <br>
    paths:  <br>
      - backend:  <br>
          serviceName: node-user-service  <br>
          servicePort: 3000  <br>
        path: /user-api(/|$)(.*)  <br>
      # - backend:  <br>
      #     serviceName: nestjs-i-consultant-service  <br>
      #     servicePort: 3001  <br>
      #   path: /i-consultant-api(/|$)(.*)<br>
</pre><br>
<br>在第6行中，我们定义了Ingress Controller类型（这是Kubernetes的预定义值；Kubernetes当前支持和维护GCE和nginx controller）。<br>
<br>在第7行中，我们定义了重写目标规则，在第10行中，我们定义了主机名。<br>
<br>对于应该从外部访问的每个服务，我们应该在路径列表中添加一个条目（从第13行开始）。在此示例中，我们仅为NodeJS用户服务后端添加了一个条目，可通过端口3000对其进行访问。/ user-api唯一标识我们的服务，因此任何以stupid-simple-kubernetes.eastus2.cloudapp azure.com/user-api开头的请求将被路由到此NodeJS后端。如果要添加其他服务，则必须更新此脚本（请参见注释掉的代码）。<br>
<br><strong>应用.yml脚本</strong><br>
<br>要应用这些脚本，我们将使用kubectl。应用文件的kubectl命令如下：<br>
<pre class="prettyprint">kubectl apply -f<br>
</pre><br>
<br>在本例中，如果你在Stupid Simple Kubernetes  repo的根文件夹中，您需要执行以下命令：<br>
<pre class="prettyprint">kubectl apply -f .\manifest\kubernetes\deployment.yml  <br>
kubectl apply -f .\manifest\kubernetes\service.yml  <br>
kubectl apply -f .\manifest\kubernetes\ingress.yml  <br>
kubectl apply -f .\manifest\ingress-controller\nginx-ingress-controller-deployment.yml  <br>
kubectl apply -f .\manifest\ingress-controller\ngnix-load-balancer-setup.yml  <br>
</pre><br>
<br>应用这些脚本后，一切准备就绪，进而我们可以从外部调用后端（如使用Postman）。<br>
<br><h2>总结</h2>在本教程中，我们学习了如何在Kubernetes中创建各种资源，例如Pod、Deployment、Services、Ingress和Ingress Controller。我们使用MongoDB数据库创建了一个NodeJS后端，并使用3个pod的副本容器化并部署了NodeJS和MongoDB容器。<br>
<br>在下一篇文章中，我们将了解持久保存数据的问题，并将介绍Kubernetes中的持久卷。<br>
<blockquote><br>作者简介<br>
  <br>
  <br>Czako Zoltan，一位经验丰富的全栈开发人员，在前端，后端，DevOps，物联网和人工智能等多个领域都拥有丰富的经验。</blockquote>
                                
                                                              
</div>
            