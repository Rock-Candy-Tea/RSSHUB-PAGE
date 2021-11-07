
---
title: 'GitLab +Jenkins+Kubernetes+Helm的自动化部署实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/537510eeedd6be0da563ac469ab3cda9.png'
author: Dockone
comments: false
date: 2021-11-07 01:53:36
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/537510eeedd6be0da563ac469ab3cda9.png'
---

<div>   
<br>本文从实践角度介绍如何结合我们常用的GitLab与Jenkins，通过Kubernetes来实现项目的自动化部署，示例将包括基于Spring Boot的服务端项目与基于Vue.js的Web项目。<br>
<br>本文涉及到的工具与技术包括：<br>
<ul><li>GitLab —— 常用的源代码管理系统</li><li>Jenkins，Jenkins Pipeline —— 常用的自动化构建、部署工具，Pipeline以流水线的方式将构建、部署的各个步骤组织起来</li><li>Docker，Dockerfile —— 容器引擎，所有应用最终都要以Docker容器运行，Dockerfile是Docker镜像定义文件</li><li>Kubernetes —— Google开源的容器编排管理系统</li><li>Helm —— Kubernetes的包管理工具，类似Linux的yum，apt，或Node的npm等包管理工具，能将Kubernetes中的应用及相关依赖服务以包（Chart）的形式组织管理</li></ul><br>
<br>环境背景：<br>
<ol><li>已使用GitLab做源码管理，源码按不同的环境建立了develop（对应开发环境），pre-release（对应测试环境），master（对应生产环境）分支</li><li>已搭建了Jenkins服务</li><li>已有Docker Registry服务，用于Docker镜像存储（基于Docker Registry或Harbor自建，或使用云服务，本文使用阿里云容器镜像服务）</li><li>已搭建了Kubernetes集群</li></ol><br>
<br>预期效果：<br>
<ol><li>分环境部署应用，开发环境、测试环境、生产环境分开来，部署在同一集群的不同namespace，或不同集群中（比如开发测试部署在本地集群的不同namespace中，生产环境部署在云端集群）</li><li>配置尽可能通用化，只需要通过修改少量配置文件的少量配置属性，就能完成新项目的自动化部署配置</li><li>开发测试环境在push代码时自动触发构建与部署，生产环境在master分支上添加版本tag并且push tag后触发自动部署</li><li>整体交互流程如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/537510eeedd6be0da563ac469ab3cda9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/537510eeedd6be0da563ac469ab3cda9.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
</li></ol><br>
<br><h3>项目配置文件</h3>首先我们需要在项目的根路径中添加一些必要的配置文件，如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/d0a6ead421fe02772bca6f4fce0fa7c3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/d0a6ead421fe02772bca6f4fce0fa7c3.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
包括：<br>
<ol><li>Dockerfile文件，用于构建Docker镜像的文件</li><li>Helm相关配置文件，Helm是Kubernetes的包管理工具，可以将应用部署相关的Deployment，Service，Ingress等打包进行发布与管理（Helm的具体介绍我们后面再补充）</li><li>Jenkinsfile文件，Jenkins的pipeline定义文件，定义了各个阶段需执行的任务</li></ol><br>
<br><h4>Dockerfile</h4>在项目根目录中添加一个Dockerfile文件（文件名就叫Dockerfile），定义如何构建Docker镜像，以Spring Boot项目为例：<br>
<pre class="prettyprint">FROM frolvlad/alpine-java:jdk8-slim<br>
<h1>在build镜像时可以通过 --build-args profile=xxx 进行修改</h1>ARG profile<br>
ENV SPRING_PROFILES_ACTIVE=$&#123;profile&#125;<br>
<h1>项目的端口</h1>EXPOSE 8000 <br>
WORKDIR /mnt<br>
<h1>修改时区</h1>RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \<br>
&& apk add --no-cache tzdata \<br>
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \<br>
&& echo "Asia/Shanghai" > /etc/timezone \<br>
&& apk del tzdata \<br>
&& rm -rf /var/cache/apk/* /tmp/* /var/tmp/* $HOME/.cache<br>
<br>
COPY ./target/your-project-name-1.0-SNAPSHOT.jar ./app.jar<br>
ENTRYPOINT ["java", "-jar", "/mnt/app.jar"] <br>
</pre><br>
将SPRING_PROFILES_ACTIVE通过参数profile暴露出来，在构建的时候可以通过--build-args profile=xxx来进行动态设定，以满足不同环境的镜像构建要求。<br>
<br><blockquote><br>SPRING_PROFILES_ACTIVE本可以在Docker容器启动时通过<code class="prettyprint">docker run -e SPRING_PROFILES_ACTIVE=xxx</code>来设定，因这里使用Helm进行部署不直接通过<code class="prettyprint">docker run</code>运行，因此通过ARG在镜像构建时指定</blockquote><h4>Helm配置文件</h4>Helm是Kubernetes的包管理工具，将应用部署相关的Deployment，Service，Ingress等打包进行发布与管理（可以像Docker镜像一样存储于仓库中）。如上图中Helm的配置文件包括：<br>
<pre class="prettyprint">helm                                    - chart包的目录名<br>
├── templates                           - Kubernetes配置模版目录<br>
│   ├── deployment.yaml                 - Deployment配置模板，定义如何部署Pod<br>
│   ├── _helpers.tpl                    - 以下划线开头的文件，Helm视为公共库定义文件，用于定义通用的子模版、函数、变量等<br>
│   ├── ingress.yaml                    - Ingress配置模板，定义外部如何访问Pod提供的服务，类似于Nginx的域名路径配置<br>
│   ├── NOTES.txt                       - chart包的帮助信息文件，执行helm install命令成功后会输出这个文件的内容<br>
│   └── service.yaml                    - Service配置模板，配置访问Pod的服务抽象，有NodePort与ClusterIp等<br>
|── values.yaml                         - chart包的参数配置文件，各模版文件可以引用这里的参数<br>
├── Chart.yaml                          - chart定义，可以定义chart的名字，版本号等信息<br>
├── charts                              - 依赖的子包目录，里面可以包含多个依赖的chart包，一般不存在依赖，我这里将其删除了<br>
</pre><br>
我们可以在Chart.yaml中定义每个项目的chart名称（类似安装包名），如：<br>
<pre class="prettyprint">apiVersion: v2<br>
name: your-chart-name<br>
description: A Helm chart for Kubernetes<br>
<br>
type: application<br>
version: 1.0.0<br>
appVersion: 1.16.0<br>
</pre><br>
在values.yaml中定义模板文件中需要用到的变量，如：<br>
<pre class="prettyprint">#部署Pod的副本数，即运行多少个容器<br>
replicaCount: 1<br>
<h1>容器镜像配置</h1>image:<br>
repository: registry.cn-hangzhou.aliyuncs.com/demo/demo<br>
pullPolicy: Always<br>
# Overrides the image tag whose default is the chart version.<br>
tag: "dev"<br>
<h1>镜像仓库访问凭证</h1>imagePullSecrets:<br>
- name: aliyun-registry-secret<br>
<h1>覆盖启动容器名称</h1>nameOverride: ""<br>
fullnameOverride: ""<br>
<h1>容器的端口暴露及环境变量配置</h1>container:<br>
port: 8000<br>
env: []<br>
<h1>ServiceAccount，默认不创建</h1>serviceAccount:<br>
# Specifies whether a service account should be created<br>
create: false<br>
# Annotations to add to the service account<br>
annotations: &#123;&#125;<br>
name: ""<br>
<br>
podAnnotations: &#123;&#125;<br>
<br>
podSecurityContext: &#123;&#125;<br>
# fsGroup: 2000<br>
<br>
securityContext: &#123;&#125;<br>
# capabilities:<br>
#   drop:<br>
#   - ALL<br>
# readOnlyRootFilesystem: true<br>
# runAsNonRoot: true<br>
# runAsUser: 1000<br>
<h1>使用NodePort的service，默认为ClusterIp</h1>service:<br>
type: NodePort<br>
port: 8000<br>
<h1>外部访问Ingress配置，需要配置hosts部分</h1>ingress:<br>
enabled: true<br>
annotations: &#123;&#125;<br>
# kubernetes.io/ingress.class: nginx<br>
# kubernetes.io/tls-acme: "true"<br>
hosts:<br>
- host: demo.com<br>
  paths: ["/demo"]<br>
tls: []<br>
#  - secretName: chart-example-tls<br>
#    hosts:<br>
#      - chart-example.local<br>
<br>
#.... 省略了其它默认参数配置<br>
</pre><br>
这里在默认生成的基础上添加了container部分，可以在这里指定容器的端口号而不用去改模板文件（让模板文件在各个项目通用，通常不需要做更改），同时添加env的配置，可以在helm部署时往容器里传入环境变量。将Service type从默认的ClusterIp改为了NodePort。部署同类型的不同项目时，只需要根据项目情况配置Chart.yaml与values.yaml两个文件的少量配置项，templates目录下的模板文件可直接复用。<br>
<br>部署时需要在Kubernetes环境中从Docker镜像仓库拉取镜像，因此需要在Kubernetes中创建镜像仓库访问凭证（imagePullSecrets）。<br>
<pre class="prettyprint"># 登录Docker Registry生成/root/.docker/config.json文件<br>
sudo docker login --username=your-username registry.cn-shenzhen.aliyuncs.com<br>
# 创建namespace develop（我这里是根据项目的环境分支名称建立namespace）<br>
kubectl create namespace develop<br>
# 在namespace develop中创建一个secret<br>
kubectl create secret generic aliyun-registry-secret --from-file=.dockerconfigjson=/root/.docker/config.json  --type=kubernetes.io/dockerconfigjson --namespace=develop<br>
</pre><br>
<h4>Jenkinsfile</h4>Jenkinsfile是Jenkins Pipeline配置文件，遵循Groovy语法，对于Spring Boot项目的构建部署， 编写Jenkinsfile脚本文件如下：<br>
<pre class="prettyprint">image_tag = "default"  //定一个全局变量，存储Docker镜像的tag（版本）<br>
pipeline &#123;<br>
agent any<br>
environment &#123;<br>
    GIT_REPO = "$&#123;env.gitlabSourceRepoName&#125;"  //从Jenkins GitLab插件中获取Git项目的名称<br>
    GIT_BRANCH = "$&#123;env.gitlabTargetBranch&#125;"  //项目的分支<br>
    GIT_TAG = sh(returnStdout: true,script: 'git describe --tags --always').trim()  //commit id或tag名称<br>
    DOCKER_REGISTER_CREDS = credentials('aliyun-docker-repo-creds') //docker registry凭证<br>
    KUBE_CONFIG_LOCAL = credentials('local-k8s-kube-config')  //开发测试环境的kube凭证<br>
    KUBE_CONFIG_PROD = "" //credentials('prod-k8s-kube-config') //生产环境的kube凭证<br>
<br>
    DOCKER_REGISTRY = "registry.cn-hangzhou.aliyuncs.com" //Docker仓库地址<br>
    DOCKER_NAMESPACE = "your-namespace"  //命名空间<br>
    DOCKER_IMAGE = "$&#123;DOCKER_REGISTRY&#125;/$&#123;DOCKER_NAMESPACE&#125;/$&#123;GIT_REPO&#125;" //Docker镜像地址<br>
<br>
    INGRESS_HOST_DEV = "dev.your-site.com"    //开发环境的域名<br>
    INGRESS_HOST_TEST = "test.your-site.com"  //测试环境的域名<br>
    INGRESS_HOST_PROD = "prod.your-site.com"  //生产环境的域名<br>
&#125;<br>
parameters &#123;<br>
    string(name: 'ingress_path', defaultValue: '/your-path', description: '服务上下文路径')<br>
    string(name: 'replica_count', defaultValue: '1', description: '容器副本数量')<br>
&#125;<br>
<br>
stages &#123;<br>
    stage('Code Analyze') &#123;<br>
        agent any<br>
        steps &#123;<br>
           echo "1. 代码静态检查"<br>
        &#125;<br>
    &#125;<br>
    stage('Maven Build') &#123;<br>
        agent &#123;<br>
            docker &#123;<br>
                image 'maven:3-jdk-8-alpine'<br>
                args '-v $HOME/.m2:/root/.m2'<br>
            &#125;<br>
        &#125;<br>
        steps &#123;<br>
            echo "2. 代码编译打包"<br>
            sh 'mvn clean package -Dfile.encoding=UTF-8 -DskipTests=true'<br>
        &#125;<br>
    &#125;<br>
    stage('Docker Build') &#123;<br>
        agent any<br>
        steps &#123;<br>
            echo "3. 构建Docker镜像"<br>
            echo "镜像地址： $&#123;DOCKER_IMAGE&#125;"<br>
            //登录Docker仓库<br>
            sh "sudo docker login -u $&#123;DOCKER_REGISTER_CREDS_USR&#125; -p $&#123;DOCKER_REGISTER_CREDS_PSW&#125; $&#123;DOCKER_REGISTRY&#125;"<br>
            script &#123;<br>
                def profile = "dev"<br>
                if (env.gitlabTargetBranch == "develop") &#123;<br>
                    image_tag = "dev." + env.GIT_TAG<br>
                &#125; else if (env.gitlabTargetBranch == "pre-release") &#123;<br>
                    image_tag = "test." + env.GIT_TAG<br>
                    profile = "test"<br>
                &#125; else if (env.gitlabTargetBranch == "master")&#123;<br>
                    // master分支则直接使用Tag<br>
                    image_tag = env.GIT_TAG<br>
                    profile = "prod"<br>
                &#125;<br>
                //通过--build-arg将profile进行设置，以区分不同环境进行镜像构建<br>
                sh "docker build  --build-arg profile=$&#123;profile&#125; -t $&#123;DOCKER_IMAGE&#125;:$&#123;image_tag&#125; ."<br>
                sh "sudo docker push $&#123;DOCKER_IMAGE&#125;:$&#123;image_tag&#125;"<br>
                sh "docker rmi $&#123;DOCKER_IMAGE&#125;:$&#123;image_tag&#125;"<br>
            &#125;<br>
        &#125;<br>
    &#125;<br>
    stage('Helm Deploy') &#123;<br>
        agent &#123;<br>
            docker &#123;<br>
                image 'lwolf/helm-kubectl-docker'<br>
                args '-u root:root'<br>
            &#125;<br>
        &#125;<br>
        steps &#123;<br>
            echo "4. 部署到Kubernetes"<br>
            sh "mkdir -p /root/.kube"<br>
            script &#123;<br>
                def kube_config = env.KUBE_CONFIG_LOCAL<br>
                def ingress_host = env.INGRESS_HOST_DEV<br>
                if (env.gitlabTargetBranch == "pre-release") &#123;<br>
                    ingress_host = env.INGRESS_HOST_TEST<br>
                &#125; else if (env.gitlabTargetBranch == "master")&#123;<br>
                    ingress_host = env.INGRESS_HOST_PROD<br>
                    kube_config = env.KUBE_CONFIG_PROD<br>
                &#125;<br>
                sh "echo $&#123;kube_config&#125; | base64 -d > /root/.kube/config"<br>
                //根据不同环境将服务部署到不同的namespace下，这里使用分支名称<br>
                sh "helm upgrade -i --namespace=$&#123;env.gitlabTargetBranch&#125; --set replicaCount=$&#123;params.replica_count&#125; --set image.repository=$&#123;DOCKER_IMAGE&#125; --set image.tag=$&#123;image_tag&#125; --set nameOverride=$&#123;GIT_REPO&#125; --set ingress.hosts[0].host=$&#123;ingress_host&#125; --set ingress.hosts[0].paths=&#123;$&#123;params.ingress_path&#125;&#125; $&#123;GIT_REPO&#125; ./helm/"<br>
            &#125;<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
Jenkinsfile定义了整个自动化构建部署的流程：<br>
<ol><li>Code Analyze，可以使用SonarQube之类的静态代码分析工具完成代码检查，这里先忽略</li><li>Maven Build，启动一个Maven的Docker容器来完成项目的maven构建打包，挂载maven本地仓库目录到宿主机，避免每次都需要重新下载依赖包</li><li>Docker Build，构建Docker镜像，并推送到镜像仓库，不同环境的镜像通过tag区分，开发环境使用dev.commitId的形式，如dev.88f5822，测试环境使用test.commitId，生产环境可以将webhook事件设置为tag push event，直接使用tag名称</li><li>Helm Deploy，使用helm完成新项目的部署，或已有项目的升级，不同环境使用不同的参数配置，如访问域名，Kubernetes集群的访问凭证kube_config等</li></ol><br>
<br><h3>Jenkins配置</h3><h4>Jenkins任务配置</h4>在Jenkins中创建一个Pipeline的任务，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/d9f2c9d467ca7c0ad111c1ad8aa01ea4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/d9f2c9d467ca7c0ad111c1ad8aa01ea4.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
配置构建触发器，将目标分支设置为develop分支，生成一个token，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/148d46cb4c3009555ab494768111c9cd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/148d46cb4c3009555ab494768111c9cd.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
记下这里的“GitLab webhook URL”及token值，在Gitlab配置中使用。<br>
<br>配置流水线，选择“Pipeline script from SCM”从项目源码中获取Pipeline脚本文件，配置项目Git地址，拉取源码凭证等，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/0996f7d602eb335184f791684673640e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/0996f7d602eb335184f791684673640e.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
保存即完成了项目开发环境的Jenkins配置。测试环境只需将对应的分支修改为pre-release即可<br>
<h4>Jenkins凭据配置</h4>在Jenkinsfile文件中，我们使用到了两个访问凭证——Docker Registry凭证与本地Kubernetes的kube凭证：<br>
<pre class="prettyprint">DOCKER_REGISTER_CREDS = credentials('aliyun-docker-repo-creds') //docker registry凭证<br>
KUBE_CONFIG_LOCAL = credentials('local-k8s-kube-config')  //开发测试环境的kube凭证<br>
</pre><br>
这两个凭证需要在Jenkins中创建。<br>
<br>添加Docker Registry登录凭证，在Jenkins凭据页面，添加一个用户名密码类型的凭据，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/b8cbc92db9b198e496891c386b07beea.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/b8cbc92db9b198e496891c386b07beea.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/0eb73055f028ae297d547d0fbd74fd53.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/0eb73055f028ae297d547d0fbd74fd53.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
添加Kubernetes集群的访问凭证，在master节点上将/root/.kube/config文件内容进行base64编码：<br>
<pre class="prettyprint">base64 /root/.kube/config > kube-config-base64.txt<br>
cat kube-config-base64.txt<br>
</pre><br>
使用编码后的内容在Jenkins中创建一个Secret text类型的凭据，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/35695de3a367b2610ae44e81b2532d8f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/35695de3a367b2610ae44e81b2532d8f.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在Secret文本框中输入base64编码后的内容。<br>
<h3>GitLab配置</h3>在GitLab项目的Settings - Integrations页面配置一个webhook，在URL与Secret Token中填入前面Jenkins触发器部分的“GitLab webhook URL”及token值，选中“Push events”作为触发事件，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/9c4ef9ae8fd2d94bdd58551d901739f9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/9c4ef9ae8fd2d94bdd58551d901739f9.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
开发、测试环境选择“Push events”则在开发人员push代码，或merge代码到develop，pre-release分支时，就会触发开发或测试环境的Jenkins pipeline任务完成自动化构建；生产环境选择“Tag push events”，在往master分支push tag时触发自动化构建。如图为pipeline构建视图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/69249f0b3e907650e0078dac154e4e59.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/69249f0b3e907650e0078dac154e4e59.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>本文介绍使用Gitlab+Jenkins Pipeline+Docker+Kubernetes+Helm来实现Spring Boot项目的自动化部署，只要稍加修改即可应用于其它基于Spring Boot的项目（具体修改的地方在源码的Readme文件中说明）。<br>
<br>原文链接：<a href="https://segmentfault.com/a/1190000022637144" rel="nofollow" target="_blank">https://segmentfault.com/a/1190000022637144</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            