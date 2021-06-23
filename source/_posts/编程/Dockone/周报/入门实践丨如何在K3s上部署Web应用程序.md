
---
title: '入门实践丨如何在K3s上部署Web应用程序'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210622211502230.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70'
author: Dockone
comments: false
date: 2021-06-23 00:21:56
thumbnail: 'https://img-blog.csdnimg.cn/20210622211502230.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70'
---

<div>   
<br>在本文中，我们将使用Flask和JavaScript编写的、带有MongoDB数据库的TODO应用程序，并学习如何将其部署到Kubernetes上。这篇文章是针对初学者的，如果你之前没有深度接触过Kubernetes集群，也不要担心！<br>
<br>我们将使用K3s，这是一个轻量级的Kubernetes发行版，非常适合快速入门。但首先让我们谈谈我们想要实现的目标。<br>
<br>首先，我将介绍示例应用程序。这其实已经简化了许多细节，但它说明了常见的用例。然后我们将熟悉了解容器化应用程序的过程。在我们继续之前，我会讨论我们如何使用容器来让我们的开发更加轻松，特别是如果我们在一个团队中工作，或者是当我们在一个新的环境中工作时，希望减轻开发人员的负担。<br>
<br>一旦我们将应用程序容器化，下一步就是将它们部署到Kubernetes上。虽然我们可以手动创建服务、Ingress和网关，但我们可以使用Knative以在任何时候都支持我们的应用程序。<br>
<br><h2>设置应用程序</h2>我们将使用一个简单的TODO应用程序来演示前端、REST API后端和MongoDB协同工作。这要归功于Prashant Shahi提出的这个例子。我做了一些小改动，纯粹是为了教学的目的：<br>
<br><a href="https://github.com/prashant-shahi"></a><a href="https://github.com/prashant-shahi" rel="nofollow" target="_blank">https://github.com/prashant-shahi</a><br>
<br>首先，git clone代码库：<br>
<pre class="prettyprint">git clone https://github.com/benjamintanweihao/Flask-MongoDB-K3s-KNative-TodoApp<br>
</pre><br>
<br>接下来，我们将检查目录，了解情况：<br>
<pre class="prettyprint">cd Flask-MongoDB-K3s-KNative-TodoApp<br>
tree<br>
</pre><br>
<br>该文件夹结构是一个典型的Flask应用程序。Entry point是app.py，它还包含REST APIs。Templates文件夹包含了将被渲染成HTML的文件：<br>
<br>打开 app.py，我们可以看到所有的主要部分：<br>
<pre class="prettyprint">├── app.py<br>
├── requirements.txt<br>
├── static<br>
│   ├── assets<br>
│   │   ├── style.css<br>
│   │   ├── twemoji.js<br>
│   │   └── twemoji.min.js<br>
└── templates<br>
├── index.html<br>
└── update.html<br>
</pre><br>
<br>从上面的代码段，您可以看到应用程序需要MongoDB作为数据库。使用lists()方法，您可以看到如何定义路由（即@ app.route（“/ list”））、如何从MongoDB获取数据，以及模板是如何呈现的示例。<br>
<pre class="prettyprint">mongodb_host = os.environ.get('MONGO_HOST', 'localhost')<br>
mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))<br>
client = MongoClient(mongodb_host, mongodb_port)<br>
db = client.camp2016<br>
todos = db.todo <br>
<br>
app = Flask(__name__)<br>
title = "TODO with Flask"<br>
<br>
@app.route("/list")<br>
def lists ():<br>
#Display the all Tasks<br>
todos_l = todos.find()<br>
a1="active"<br>
return render_template('index.html',a1=a1,todos=todos_l,t=title,h=heading)<br>
<br>
if __name__ == "__main__":<br>
env = os.environ.get('APP_ENV', 'development')<br>
port = int(os.environ.get('PORT', 5000))<br>
debug = False if env == 'production' else True<br>
app.run(host='0.0.0.0', port=port, debug=debug)<br>
</pre><br>
<br>这里需要注意的另一件事是使用了MONGO_HOST和MONGO_PORT的环境变量和Flask相关的环境变量。其中，最重要的是debug。当变量设置为True时，Flask服务器会在检测到和发生更改时自动重新加载。这在开发过程中特别方便，也是我们要充分利用的特性。<br>
<br><h2>用Docker容器开发</h2>在处理应用程序时，我曾经花费大量时间设置环境并安装所有依赖项。在那之后，我可以通过添加新功能来启动和运行。然而，这仅仅描述了一个理想的场景，对吗？<br>
<br>你有多少次回到你已经开发的应用程序（比如六个月前），却发现自己正在慢慢陷入依赖项地狱？依赖项通常是一个灵活的目标，除非您采取措施锁定对象，否则您的应用程序可能无法正常工作。解决这个问题的方法之一是将所有依赖项打包到Docker容器中。<br>
<br>Docker带来的另一件特性是自动化。这意味着不再需要复制和粘贴命令，也不再需要设置数据库之类的东西。<br>
<br><strong>Docker化 Flask程序</strong><br>
<br>以下是Dockerfile：<br>
<pre class="prettyprint">FROM alpine:3.7<br>
COPY . /app<br>
WORKDIR /app<br>
<br>
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python py2-pip \<br>
&& pip2 install --upgrade pip \<br>
&& pip2 install -r requirements.txt \<br>
&& rm -rf /var/cache/apk/*<br>
<br>
EXPOSE 5000<br>
ENTRYPOINT ["python"]<br>
</pre><br>
<br>我们从一个最小的（在大小和功能方面）基础镜像开始。然后，应用程序的内容进入容器中的/app目录。接下来，我们执行一系列命令来安装Python、Nginx web server和Flask应用程序的所有需求。这些正是在新系统上设置应用程序所需的步骤。<br>
<br>您可以这样构建Docker容器：<br>
<pre class="prettyprint">% docker build -t <yourusername>/todo-app .<br>
</pre><br>
<br>你将看到这样如下输出：<br>
<pre class="prettyprint"># ...<br>
Successfully built c650af8b7942<br>
Successfully tagged benjamintanweihao/todo-app:latest<br>
</pre><br>
<br><strong>那 MongoDB 呢？</strong><br>
<br>您是否应该经历为MongoDB创建Dockerfile的相同过程？在此之前，已经有人做过这样的尝试，具体演示请查看案例链接：<a href="https://hub.docker.com/_/mongo." rel="nofollow" target="_blank">https://hub.docker.com/_/mongo.</a>不过现在您有两个容器，其中Flask容器依赖于MongoDB容器。<br>
<br>一种方法是先启动MongoDB容器，然后启动Flask容器。但是，假设您想添加缓存并决定引入Redis容器。那么启动每个容器的过程会很快变枯燥繁琐。解决方案是Docker Compose，这是一个允许您定义和运行多个Docker容器的工具，正符合我们当前面临的情况。<br>
<br><strong>Docker Compose</strong><br>
<br>以下是Docker compose文件，docker-compose.yaml：<br>
<pre class="prettyprint">services:<br>
flaskapp:<br>
build: .<br>
image: benjamintanweihao/todo-app:latest<br>
ports:<br>
  - 5000:5000<br>
container_name: flask-app<br>
environment:<br>
  - MONGO_HOST=mongo<br>
  - MONGO_PORT=27017<br>
networks:<br>
  - todo-net<br>
depends_on:<br>
  - mongo<br>
volumes:<br>
  - .:/app # <--- <br>
mongo:<br>
image: mvertes/alpine-mongo<br>
ports:<br>
  - 27017:27017<br>
networks:<br>
  - todo-net<br>
<br>
networks:<br>
todo-net:<br>
driver: bridge<br>
</pre><br>
<br>即使您不熟悉Docker Compose，这里的YAML文件也并不复杂。让我们看一下重要的部分。<br>
<br>在最开头，这个文件定义了由flaskapp和mongo组成的服务，以及指定桥接连接的网络。这将创建一个网络连接，以便服务中定义的容器可以相互通信。<br>
<br>每个服务都定义镜像、端口映射和前面定义的网络。在flaskapp中也定义了环境变量（请查看app.py，看看它们是否确实是相同的）。<br>
<br>我想提醒您注意flask应用程序中指定的volume。我们在这里所做的是将主机的当前目录（应该是包含app.py的项目目录）映射到容器的/app目录 我们为什么要这样做？回想一下，在Dockerfile中，我们将app复制到/app目录中，如下所示：<br>
<pre class="prettyprint">COPY . /app<br>
</pre><br>
<br>假设你想对应用程序做一个更改。你不可能轻易改变容器中的app.py。通过对本地目录的映射，你基本上是在用你目录中的本地副本覆盖容器中的app.py。因此，假设Flask应用程序处于调试模式（如果你在这一点上没有改变任何东西的话，它就是调试模式），当你启动容器并做出改变时，渲染的输出会反映出这个改变。<br>
<br>但是，重要的是要意识到容器中的app.py仍然是旧版本，您仍然需要记住构建新镜像(希望您已将CI/CD设置为自动执行此操作）<br>
<br>让我们看看这是怎么回事。运行以下命令：<br>
<pre class="prettyprint">docker-compose up<br>
</pre><br>
<br>接下来你将看到：<br>
<pre class="prettyprint">Creating network "flask-mongodb-k3s-knative-todoapp_my-net" with driver "bridge"<br>
Creating flask-mongodb-k3s-knative-todoapp_mongo_1 ... done<br>
Creating flask-app                                 ... done<br>
Attaching to flask-mongodb-k3s-knative-todoapp_mongo_1, flask-app<br>
<h1>... more output truncated</h1>flask-app   |  * Serving Flask app "app" (lazy loading)<br>
flask-app   |  * Environment: production<br>
flask-app   |    WARNING: Do not use the development server in a production environment.<br>
flask-app   |    Use a production WSGI server instead.<br>
flask-app   |  * Debug mode: on<br>
flask-app   |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)<br>
flask-app   |  * Restarting with stat<br>
mongo_1     | 2021-05-15T15:41:37.993+0000 I NETWORK  [listener] connection accepted from 172.23.0.1:48844 #2 (2 connections now open)<br>
mongo_1     | 2021-05-15T15:41:37.993+0000 I NETWORK  [conn2] received client metadata from 172.23.0.1:48844 conn2: &#123; driver: &#123; name: "PyMongo", version: "3.11.4" &#125;, os: &#123; type: "Linux", name: "", architecture: "x86_64", version: "5.8.0-53-generic" &#125;, platform: "CPython 2.7.15.final.0" &#125;<br>
flask-app   |  * Debugger is active!<br>
flask-app   |  * Debugger PIN: 183-021-098<br>
</pre><br>
<br>现在开始在浏览器中访问：<a href="http://localhost:5000/"></a><a href="http://localhost:5000/" rel="nofollow" target="_blank">http://localhost:5000</a><br>
<br><img src="https://img-blog.csdnimg.cn/20210622211502230.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70" alt="图片" referrerpolicy="no-referrer"><br>
<br>如果你看到这个，恭喜你！Flask和Mongo在一起正常工作了。您可以随意使用应用程序来感受它。<br>
<br>现在让我们对应用程序标题中的app.py做一个小小的改动：<br>
<pre class="prettyprint">index d322672..1c447ba 100644<br>
--- a/app.py<br>
+++ b/app.py<br>
-heading = "tOdO Reminder"<br>
+heading = "TODO Reminder!!!!!"<br>
</pre><br>
<br>保存文件并重新加载应用程序：<br>
<br><img src="https://img-blog.csdnimg.cn/20210622211557956.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70" alt="图片" referrerpolicy="no-referrer"><br>
<br>完成后，您可以输入以下命令：<br>
<pre class="prettyprint">docker-compose down<br>
</pre><br>
<br><h2>将应用程序部署到Kubernetes上</h2>截至目前，我们已将我们的应用程序及其支持服务（现在只是MongoDB）容器化。我们如何开始将我们的应用程序部署到Kubernetes？<br>
<br>在此之前，让我们安装Kubernetes。为此，我选择了K3s，因为它是安装Kubernetes和启动和运行的最简单方法。<br>
<pre class="prettyprint">% curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --no-deploy=traefik"  sh -s -<br>
</pre><br>
<br>过一会儿，你就可以安装 Kubernetes了:<br>
<pre class="prettyprint">[INFO]  Finding release for channel stable<br>
[INFO]  Using v1.20.6+k3s1 as release<br>
[INFO]  Downloading hash https://github.com/k3s-io/k3s/releases/download/v1.20.6+k3s1/sha256sum-amd64.txt<br>
<h1>truncated ...</h1>[INFO]  systemd: Starting k3s<br>
</pre><br>
<br>验证是否已正确设置K3s：<br>
<pre class="prettyprint">% kubectl get no<br>
NAME      STATUS   ROLES                  AGE     VERSION<br>
artemis   Ready    control-plane,master   2m53s   v1.20.6+k3s1<br>
</pre><br>
<br><strong>MongoDB</strong><br>
<br>有多种方法可以完成这一操作。您可以使用我们创建的镜像，MongoDB operator或Helm：<br>
<pre class="prettyprint">helm install mongodb-release bitnami/mongodb --set architecture=standalone --set auth.enabled=false<br>
</pre><br>
<pre class="prettyprint">Please be patient while the chart is being deployed <br>
<br>
MongoDB(R) can be accessed on the following DNS name(s) and ports from within your cluster:<br>
<br>
mongodb-release.default.svc.cluster.local<br>
<br>
To connect to your database, create a MongoDB(R) client container:<br>
<br>
kubectl run --namespace default mongodb-release-client --rm --tty -i --restart='Never' --env="MONGODB_ROOT_PASSWORD=$MONGODB_ROOT_PASSWORD" --image docker.io/bitnami/mongodb:4.4.6-debian-10-r0 --command -- bash<br>
<br>
Then, run the following command:<br>
mongo admin --host "mongodb-release"<br>
<br>
To connect to your database from outside the cluster execute the following commands:<br>
<br>
kubectl port-forward --namespace default svc/mongodb-release 27017:27017 &<br>
mongo --host 127.0.0.1<br>
</pre><br>
<br><strong>安装Knative和Istio</strong><br>
<br>在本文中，我们将使用Knative。Knative构建在Kubernetes之上，使得开发人员可以很容易地部署和运行应用程序，而不必知道Kubernetes的很多细节。 <br>
<br>Knative由两部分组成：Serving和Eventing。在本节中，我们将讨论Serving部分。使用Knative Serving，您可以在几秒钟内创建可弹性伸缩的、安全的和无状态的服务，这就是我们需要对TODO应用程序做的！在此之前，我们先安装Knative：<br>
<br>以下说明基于：<br>
<br><a href="https://knative.dev/docs/install/install-serving-with-yaml/"></a><a href="https://knative.dev/docs/install/install-serving-with-yaml/" rel="nofollow" target="_blank">https://knative.dev/docs/insta ... yaml/</a><br>
<pre class="prettyprint">kubectl apply -f https://github.com/knative/serving/releases/download/v0.22.0/serving-crds.yaml<br>
kubectl apply -f https://github.com/knative/serving/releases/download/v0.22.0/serving-core.yaml<br>
kubectl apply -f https://github.com/knative/net-istio/releases/download/v0.22.0/istio.yaml<br>
kubectl apply -f https://github.com/knative/net-istio/releases/download/v0.22.0/net-istio.yaml<br>
</pre><br>
<br>这设置了Knative和istio。你可能想知道为什么我们需要Istio。原因是Knative需要一个Ingress Controller，使其可以执行流量分发（例如， Todo应用程序的版本1和版本2需要同时运行）和自动HTTP请求重试。<br>
<br>Istio有替代方案吗？或许可以考虑Gloo（<a href="https://docs.solo.io/gloo-edge/master/installation/knative/"></a><a href="https://docs.solo.io/gloo-edge/master/installation/knative/" rel="nofollow" target="_blank">https://docs.solo.io/gloo-edge ... tive/</a>）。但当前不支持Traefik，这就是为什么我们在安装K3s时必须禁用它。由于Istio是默认且最受支持的，我们将使用它。<br>
<br>现在等待所有的knative-serving 的pod运行：<br>
<br>k<br>
<pre class="prettyprint">ubectl get pods --namespace knative-serving -w<br>
NAME                                READY   STATUS    RESTARTS   AGE<br>
controller-57956677cf-2rqqd         1/1     Running   0          3m39s<br>
webhook-ff79fddb7-mkcrv             1/1     Running   0          3m39s<br>
autoscaler-75895c6c95-2vv5b         1/1     Running   0          3m39s<br>
activator-799bbf59dc-t6v8k          1/1     Running   0          3m39s<br>
istio-webhook-5f876d5c85-2hnvc      1/1     Running   0          44s<br>
networking-istio-6bbc6b9664-shtd2   1/1     Running   0          44s<br>
</pre><br>
<br><strong>设置自定义域</strong><br>
<br>默认情况下，Knative Serving使用example.com作为默认域。如果您按照说明设置了K3s，则应该安装负载均衡器。这意味着通过一些设置，您可以使用sslip.io之类的DNS服务创建自定义域。 <br>
<br>sslip.io是一种服务，当使用带有嵌入式IP地址的主机名进行查询时，它会返回该IP地址。例如，192.168.0.1.sslip.io等URL将指向192.168.0.1。这是极好的服务，你不必去买你自己的域名。<br>
<br>继续并应用以下manifest：<br>
<pre class="prettyprint">kubectl apply -f https://storage.googleapis.com/knative-nightly/serving/latest/serving-default-domain.yaml<br>
</pre><br>
<br>如果您打开 serving-default-domain. yaml，您需要在 spec 中注意到以下内容：<br>
<pre class="prettyprint"># other parts truncated     <br>
spec:<br>
serviceAccountName: controller<br>
containers:<br>
    - name: default-doma<br>
      image: ko://knative.dev/serving/cmd/default-domain<br>
      args: ["-magic-dns=sslip.io"]<br>
</pre><br>
<br>这将启用您将在下一步中需要使用的DNS。<br>
<br><strong>测试是否一切正常</strong><br>
<br>下载kn二进制文件。您可以查阅链接：<a href="https://knative.dev/development/client/install-kn/"></a><a href="https://knative.dev/development/client/install-kn/" rel="nofollow" target="_blank">https://knative.dev/development/client/install-kn/</a>。一定要重命名二进制文件 kn然后把它放在$PATH的某个地方。一旦解决了这个问题，就继续创建示例Hello World服务。我已经将benjamintanweihao/helloworld python镜像推送到Docker Hub：<br>
<pre class="prettyprint">% kn service create helloworld-python --image=docker.io/benjamintanweihao/helloworld-python --env TARGET="Python Sample v1"<br>
</pre><br>
<br>这将产生以下输出：<br>
<pre class="prettyprint">Creating service 'helloworld-python' in namespace 'default':<br>
<br>
0.037s The Route is still working to reflect the latest desired specification.<br>
0.099s Configuration "helloworld-python" is waiting for a Revision to become ready.<br>
29.277s ...<br>
29.314s Ingress has not yet been reconciled.<br>
29.446s Waiting for load balancer to be ready<br>
29.605s Ready to serve.<br>
<br>
Service 'helloworld-python' created to latest revision 'helloworld-python-00001' is available at URL:<br>
http://helloworld-python.default.192.168.86.26.sslip.io<br>
</pre><br>
<br>输入以下代码即可列出所有命名空间中所有已部署的Knative服务：<br>
<pre class="prettyprint">% kn service  list -A<br>
</pre><br>
<br>如果有kubectl，这就变成：<br>
<pre class="prettyprint">% kubectl get ksvc -A<br>
</pre><br>
<br>要删除服务，只需执行以下操作：<br>
<pre class="prettyprint">kn service delete helloworld-python # or kubectl delete ksvc helloworld-python<br>
</pre><br>
<br>如果您还没有这样做，请确保TODO应用程序镜像已推送到DockerHub。记住用DockerHub ID替换&#123;username&#125;：<br>
<pre class="prettyprint">% docker push &#123;username&#125;/todo-app:latest<br>
</pre><br>
<br>推送镜像后，可以使用kn命令创建TODO服务。记住用DockerHub ID替换&#123;username&#125;：<br>
<pre class="prettyprint">kn service create todo-app --image=docker.io/&#123;username&#125;/todo-app --env MONGO_HOST="mongodb-release.default.svc.cluster.local" <br>
</pre><br>
<br>如果一切运行顺利，你将看到：<br>
<pre class="prettyprint">Creating service 'todo-app' in namespace 'default':<br>
<br>
0.022s The Route is still working to reflect the latest desired specification.<br>
0.085s Configuration "todo-app" is waiting for a Revision to become ready.<br>
4.586s ...<br>
4.608s Ingress has not yet been reconciled.<br>
4.675s Waiting for load balancer to be ready<br>
4.974s Ready to serve.<br>
<br>
Service 'todo-app' created to latest revision 'todo-app-00001' is available at URL:<br>
http://todo-app.default.192.168.86.26.sslip.io<br>
</pre><br>
<br>现在访问<a href="http://todo-app.default.192.168.86.26.sslip.io/"></a><a href="http://todo-app.default.192.168.86.26.sslip.io/" rel="nofollow" target="_blank">http://todo-app.default.192.168.86.26.sslip.io</a> （或者在上一个输出的最后一行的内容）您应该可以看到应用程序！现在我们来看看Knative为你做了什么。KNative仅需一行命令就可以为您启动一个服务，并且为您提供了一个可以从集群访问的URL。<br>
<br>我对Knative的了解仅仅停留于表面，但我希望这个教程可以激励你更多地了解它！当我开始看Knative的时候，我不太明白它做了什么。希望这个例子能让我们看到Knative的惊人之处和它的便利性。<br>
<br><h2>结 论</h2>在本文中，我们简要介绍了使用Python构建的web应用程序并需要MongoDB，并学习了如何：<br>
<ul><li>使用Docker容器化TODO应用程序</li><li>使用Docker减轻依赖项</li><li>使用Docker进行开发</li><li>使用Docker Compose打包多个容器</li><li>安装K3s</li><li>安装Knative（Serving）和Istio</li><li>使用Helm署MongoDB</li><li>使用Knative部署TODO应用程序</li></ul><br>
<br>虽然将应用程序迁移到 Kubernetes 当然不是一项简单的任务，但是将应用程序容器化通常会让你成功一半。当然，本文还有很多东西没有涉及，比如安全性和可扩展性。<br>
<br>K3s 是轻量级的Kubernetes发行版，可以极其轻松地使用笔记本/台式机测试和运行 Kubernetes 工作负载，对个人开发者来说十分友好。同时，也十分适合企业在边缘端大规模部署集群。<br>
<br>当我开始研究 Knative 的时候，我并不十分理解它的作用。希望这个例子能够帮助我们理解 Knative 的魅力及其带来的便利。实际上，Knative 的亮点之一就是“在几秒钟之内就能启动一个可扩展的、安全的、无状态的服务”。<br>
<br>我将在以后的文章中更多地介绍 Knative，并更深入地探讨其核心特征。我希望你能通过这篇教程，将它们应用到你的应用程序中！
                                
                                                              
</div>
            