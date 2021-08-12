
---
title: 'Jenkins for Kubernetes实现Slave动态伸缩'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/6d7fdfdde713954b7e6920dad3d1c248.png'
author: Dockone
comments: false
date: 2021-08-12 01:50:07
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/6d7fdfdde713954b7e6920dad3d1c248.png'
---

<div>   
<br>本文章案例可用于参考Jenkins for Kubernetes部署。因每个公司的架构和环境不一样，需要改变一些部署的方式。<br>
<br>Jenkins for Kubernetes的好处：<br>
<ul><li>Jenkins-Master的高可用。Kubernetes的RC或Deployment可以监控副本的存活状态（通过探针）和副本数量，如果Master出现无法提供服务的情况，就会重启或者迁移到其他节点。</li><li>Jenkins-Slave的动态伸缩。每次构建都会启动一个Pod用于部署Slave，构建完成后就会释放掉。那么Pod在创建的时候，Kubernetes就会选择集群内资源剩余较多的节点创建Slave的Pod，构建完成后Pod会自动删除。</li><li>扩展性好。 因为可以同时拥有很多个Slave，可以配置Jenkins同时执行很多构建操作，减少排队等待构建的时间。</li></ul><br>
<br><h3>部署思路</h3>首先在Kubernetes中部署Jenkins-Master然后使用Kubernetes Plugin插件进行Slave的动态伸缩。并且使用NFS作为后端存储的PersistentVolume来挂载Jenkins-Master的jenkins_home目录、构建时Slave的Maven缓存m2目录（可以利用缓存加快每次构建的速度）、保留Slave每次构建产生的数据（workspace目录中的每个Job）。<br>
<br>使用PersistentVolume的原因是Kubernetes任何节点都可以访问到挂载的目录，不会因为Master迁移节点导致数据丢失。NFS方便部署而且性能也满足Jenkins的使用需求所以选择了NFS，也可以使用其他的后端存储。<br>
<h3>部署</h3>部署方式可以自定义也可以使用Kubernetes Pugin官网提供的部署yml。自定义使用Deployment也是可以的，但是官网的部署方式使用了StatefulSet。Jenkins是一个有状态的应用，我感觉使用StatefulSet部署更加严谨一点。我这里使用了官网提供的文档进行部署的，但是也根据实际情况修改了一些东西。<br>
<br>首先需要在Kubernetes所有节点部署NFS客户端：<br>
<pre class="prettyprint">yum -y install nfs-utils<br>
systemctl start nfs-utils<br>
systemctl enable nfs-utils<br>
rpcinfo -p<br>
</pre><br>
NFS服务端配置文件增加配置：<br>
<pre class="prettyprint">/data/dev_jenkins       10.0.0.0/24(rw,sync,no_root_squash,no_subtree_check)<br>
<h1>dev环境Jenkins Slave节点挂载workspace</h1>/data/dev_jenkins/workspace  0.0.0.0/0(rw,sync,no_root_squash,no_subtree_check)<br>
<h1>dev环境Jenkins Slave节点挂载m2 Maven缓存目录</h1>/data/dev_jenkins/m2 0.0.0.0/0(rw,sync,no_root_squash,no_subtree_check)<br>
</pre><br>
共享目录一定要给777权限。不然容器内部会报错没有写入权限。<br>
<br>service-account.yml此文件用于创建Kubernetes的RBAC，授权给后面的Jenkins应用可以创建和删除Slave的Pod。<br>
<pre class="prettyprint"># In GKE need to get RBAC permissions first with<br>
# kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin [--user=<user-name>|--group=<group-name>]<br>
<br>
---<br>
apiVersion: v1<br>
kind: ServiceAccount<br>
metadata:<br>
name: jenkins<br>
<br>
---<br>
kind: Role<br>
apiVersion: rbac.authorization.k8s.io/v1beta1<br>
metadata:<br>
name: jenkins<br>
rules:<br>
- apiGroups: [""]<br>
resources: ["pods"]<br>
verbs: ["create","delete","get","list","patch","update","watch"]<br>
- apiGroups: [""]<br>
resources: ["pods/exec"]<br>
verbs: ["create","delete","get","list","patch","update","watch"]<br>
- apiGroups: [""]<br>
resources: ["pods/log"]<br>
verbs: ["get","list","watch"]<br>
- apiGroups: [""]<br>
resources: ["events"]<br>
verbs: ["watch"]<br>
- apiGroups: [""]<br>
resources: ["secrets"]<br>
verbs: ["get"]<br>
<br>
---<br>
apiVersion: rbac.authorization.k8s.io/v1beta1<br>
kind: RoleBinding<br>
metadata:<br>
name: jenkins             #与jenkins.yml中的serviceAccountName: jenkins相对应<br>
roleRef:<br>
apiGroup: rbac.authorization.k8s.io<br>
kind: Role<br>
name: jenkins<br>
subjects:<br>
- kind: ServiceAccount<br>
name: jenkins<br>
</pre><br>
jenkins-pv.yml和jenkins-pvc.yml用于创建挂载jenkins_home目录：<br>
<pre class="prettyprint">[root@dev-master1 kubernetes]# cat jenkins-pv.yml <br>
apiVersion: v1<br>
kind: PersistentVolume<br>
metadata:<br>
name: jenkins-home<br>
spec:<br>
capacity:  #指定容量<br>
storage: 20Gi<br>
accessModes:<br>
- ReadWriteOnce  #访问模式，还有ReadOnlyMany ##ReadOnlymany<br>
#  persistenVolumeReclaimPolicy: Recycle<br>
#  storageClassName: nfs  ##指定存储的类型<br>
nfs:<br>
path: /data/dev_jenkins  #指明NFS的路径<br>
server: 10.0.0.250  #指明NFS的IP<br>
<br>
[root@dev-master1 kubernetes]# cat jenkins-pvc.yml <br>
kind: PersistentVolumeClaim<br>
apiVersion: v1<br>
metadata:<br>
namespace: kubernetes-plugin<br>
name: jenkins-home<br>
spec:<br>
accessModes:<br>
- ReadWriteOnce<br>
resources:<br>
requests:<br>
    storage: 20Gi<br>
</pre><br>
创建Jenkins的Master，可以根据实际情况限制Jenkins的资源使用。<br>
<pre class="prettyprint">[root@dev-master1 kubernetes]# cat jenkins.yml <br>
# jenkins<br>
---<br>
apiVersion: apps/v1<br>
kind: StatefulSet<br>
metadata:<br>
name: jenkins<br>
labels:<br>
name: jenkins<br>
spec:<br>
selector:<br>
matchLabels:<br>
  name: jenkins<br>
serviceName: jenkins<br>
replicas: 1<br>
updateStrategy:<br>
type: RollingUpdate<br>
template:<br>
metadata:<br>
  name: jenkins<br>
  labels:<br>
    name: jenkins<br>
spec:<br>
  terminationGracePeriodSeconds: 10<br>
  serviceAccountName: jenkins<br>
  containers:<br>
    - name: jenkins<br>
      image: 10.0.0.59/jenkins/jenkins:lts-alpine #官方镜像为jenkins/jenkins:lts-alpine，为了节省下载时间已经push到自己到Harbor仓库<br>
      imagePullPolicy: Always<br>
      ports:<br>
        - containerPort: 8080<br>
        - containerPort: 50000<br>
      resources:<br>
        limits:<br>
          cpu: 1<br>
          memory: 1Gi<br>
        requests:<br>
          cpu: 0.5<br>
          memory: 500Mi<br>
      env:<br>
        - name: LIMITS_MEMORY<br>
          valueFrom:<br>
            resourceFieldRef:<br>
              resource: limits.memory<br>
              divisor: 1Mi<br>
        - name: JAVA_OPTS<br>
          # value: -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=1 -XshowSettings:vm -Dhudson.slaves.NodeProvisioner.initialDelay=0 -Dhudson.slaves.NodeProvisioner.MARGIN=50 -Dhudson.slaves.NodeProvisioner.MARGIN0=0.85<br>
          value: -Xmx$(LIMITS_MEMORY)m -XshowSettings:vm -Dhudson.slaves.NodeProvisioner.initialDelay=0 -Dhudson.slaves.NodeProvisioner.MARGIN=50 -Dhudson.slaves.NodeProvisioner.MARGIN0=0.85<br>
      volumeMounts:         #挂载PVC存储到Jenkins容器的/var/jenkins_home<br>
        - name: jenkinshome<br>
          mountPath: /var/jenkins_home<br>
      livenessProbe:<br>
        httpGet:<br>
          path: /login<br>
          port: 8080<br>
        initialDelaySeconds: 600        #存活探针时间改为600s，如果服务器配置低，Jenkins还没有启动成功就被重启了。<br>
        timeoutSeconds: 5<br>
        failureThreshold: 12 # ~2 minutes<br>
      readinessProbe:<br>
        httpGet:<br>
          path: /login<br>
          port: 8080<br>
        initialDelaySeconds: 60<br>
        timeoutSeconds: 5<br>
        failureThreshold: 12 # ~2 minutes<br>
  securityContext:<br>
    fsGroup: 1000<br>
  volumes:     #此处声明Jenkins的PVC存储<br>
    - name: jenkinshome<br>
      persistentVolumeClaim:<br>
        claimName: jenkins-home<br>
#      imagePullSecrets:                        如果使用私有仓库，并且仓库对镜像设置了访问权限，需要在Kubernetes Master创建一个secret<br>
#        - name: registry-secret<br>
</pre><br>
jenkins-sv.yml用于创建Jenkins的Service。<br>
<pre class="prettyprint">[root@dev-master1 kubernetes]# cat jenkins-sv.yml <br>
apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: jenkins<br>
spec:<br>
sessionAffinity: "ClientIP"<br>
type: NodePort<br>
selector:<br>
name: jenkins<br>
ports:<br>
-<br>
  name: http<br>
  port: 80<br>
  nodePort: 31006<br>
  protocol: TCP<br>
-<br>
  name: agent<br>
  port: 50000<br>
  nodePort: 31007<br>
  protocol: TCP<br>
</pre><br>
挂载Maven缓存目录。<br>
<pre class="prettyprint">[root@dev-master1 kubernetes]# cat m2-pv.yml <br>
<h1>m2是Maven的缓存，挂载以提高build速度</h1>apiVersion: v1<br>
kind: PersistentVolume<br>
metadata:<br>
name: maven-m2<br>
spec:<br>
capacity:  #指定容量<br>
storage: 200Gi<br>
accessModes:<br>
- ReadWriteOnce  #访问模式，还有ReadOnlyMany ##ReadOnlymany<br>
#  persistenVolumeReclaimPolicy: Recycle<br>
#  storageClassName: nfs  ##指定存储的类型<br>
nfs:<br>
path: /data/dev_jenkins/m2  #指明NFS的路径<br>
server: 10.0.0.250  #指明NFS的IP<br>
<br>
<br>
[root@dev-master1 kubernetes]# cat m2-pvc.yml <br>
kind: PersistentVolumeClaim<br>
apiVersion: v1<br>
metadata:<br>
namespace: kubernetes-plugin<br>
name: maven-m2<br>
spec:<br>
accessModes:<br>
- ReadWriteOnce<br>
resources:<br>
requests:<br>
    storage: 200Gi<br>
</pre><br>
挂载Slave节点保存构建结果的目录。<br>
<pre class="prettyprint">[root@dev-master1 kubernetes]# cat workspace-pv.yml <br>
<h1>m2是maven的缓存，挂载以提高build速度</h1>apiVersion: v1<br>
kind: PersistentVolume<br>
metadata:<br>
name: workspace<br>
spec:<br>
capacity:  #指定容量<br>
storage: 200Gi<br>
accessModes:<br>
- ReadWriteOnce  #访问模式，还有ReadOnlyMany ##ReadOnlymany<br>
#  persistenVolumeReclaimPolicy: Recycle<br>
#  storageClassName: nfs  ##指定存储的类型<br>
nfs:<br>
path: /data/dev_jenkins/workspace  #指明NFS的路径<br>
server: 10.0.0.250  #指明NFS的IP<br>
<br>
<br>
[root@dev-master1 kubernetes]# cat workspace-pvc.yml <br>
kind: PersistentVolumeClaim<br>
apiVersion: v1<br>
metadata:<br>
namespace: kubernetes-plugin<br>
name: workspace<br>
spec:<br>
accessModes:<br>
- ReadWriteOnce<br>
resources:<br>
requests:<br>
    storage: 200Gi<br>
</pre><br>
创建Jenkins的Ingress。因为我的Kubernetes集群里面使用的是Traefik，所以我把Traefik的配置文件和kubernetes-plugin官网给出的Ingress一起贴出来。<br>
<pre class="prettyprint">[root@dev-master1 kubernetes]# cat jenkins-traefik.yml <br>
apiVersion: extensions/v1beta1<br>
kind: Ingress<br>
metadata:<br>
name: jenkins<br>
namespace: kubernetes-plugin<br>
annotations:<br>
kubernetes.io/ingress.class: traefik<br>
spec:<br>
rules:<br>
- host: jenkins-dev.doudou.com<br>
http:<br>
  paths:<br>
  - path: /  <br>
    backend:<br>
      serviceName: jenkins<br>
      servicePort: 80<br>
<br>
<br>
[root@dev-master1 kubernetes]# cat jenkins-Ingress.yml <br>
<h1>因为集群使用Traefik所以此Ingress配置文件不创建，此文件为官方原版</h1>apiVersion: extensions/v1beta1<br>
kind: Ingress<br>
metadata:<br>
name: jenkins<br>
annotations:<br>
nginx.ingress.kubernetes.io/ssl-redirect: "true"<br>
kubernetes.io/tls-acme: "true"<br>
# "413 Request Entity Too Large" uploading plugins, increase client_max_body_size<br>
nginx.ingress.kubernetes.io/proxy-body-size: 50m<br>
nginx.ingress.kubernetes.io/proxy-request-buffering: "off"<br>
# For nginx-ingress controller < 0.9.0.beta-18<br>
ingress.kubernetes.io/ssl-redirect: "true"<br>
# "413 Request Entity Too Large" uploading plugins, increase client_max_body_size<br>
ingress.kubernetes.io/proxy-body-size: 50m<br>
ingress.kubernetes.io/proxy-request-buffering: "off"<br>
spec:<br>
rules:<br>
- http:<br>
  paths:<br>
  - path: /<br>
    backend:<br>
      serviceName: jenkins<br>
      servicePort: 80<br>
host: jenkins.example.com<br>
tls:<br>
- hosts:<br>
- jenkins.example.com<br>
secretName: tls-jenkins<br>
</pre><br>
创建以上的配置文件：<br>
<pre class="prettyprint">kubectl create namespace kubernetes-plugin   #创建kubernetes-plugin namespace，下面创建的所有东西都归属到这个namespace<br>
kubectl config set-context $(kubectl config current-context) --namespace=kubernetes-plugin  #修改Kubernetes默认的namespace为kubernetes-plugin，这样下面创建的都默认为kubernetes-plugin命名空间<br>
kubectl create -f service-account.yml<br>
<h1>kubectl create -f jenkins-Ingress.yml</h1>kubectl create -f jenkins-pv.yml<br>
kubectl create -f jenkins-pvc.yml<br>
kubectl create -f jenkins-sv.yml<br>
kubectl create -f jenkins.yml<br>
kubectl create -f m2-pvc.yml<br>
kubectl create -f m2-pv.yml<br>
kubectl create -f workspace-pvc.yml<br>
kubectl create -f workspace-pv.yml<br>
</pre><br>
查看创建状态：<br>
<pre class="prettyprint">[root@dev-master1 ~]# kubectl get service,pod,StatefulSet -o wide<br>
NAME              TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)                        AGE   SELECTOR<br>
service/jenkins   NodePort   10.105.123.193   <none>        80:31006/TCP,50000:31007/TCP   9d    name=jenkins<br>
<br>
NAME            READY   STATUS    RESTARTS   AGE    IP             NODE        NOMINATED NODE   READINESS GATES<br>
pod/jenkins-0   1/1     Running   0          6d5h   100.78.0.141   dev-node4   <none>           <none><br>
<br>
NAME                       READY   AGE   CONTAINERS   IMAGES<br>
statefulset.apps/jenkins   1/1     7d    jenkins      10.0.0.59/jenkins/jenkins:lts-alpine<br>
[root@dev-master1 ~]# kubectl get pv,pvc<br>
NAME                            CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                            STORAGECLASS   REASON   AGE<br>
persistentvolume/jenkins-home   20Gi       RWO            Retain           Bound    kubernetes-plugin/jenkins-home                           13d<br>
persistentvolume/maven-m2       200Gi      RWO            Retain           Bound    kubernetes-plugin/maven-m2                               7d5h<br>
persistentvolume/workspace      200Gi      RWO            Retain           Bound    kubernetes-plugin/workspace                              7d5h<br>
<br>
NAME                                           STATUS    VOLUME         CAPACITY   ACCESS MODES   STORAGECLASS   AGE<br>
persistentvolumeclaim/jenkins-home             Bound     jenkins-home   20Gi       RWO                           13d<br>
persistentvolumeclaim/maven-m2                 Bound     maven-m2       200Gi      RWO                           7d5h<br>
persistentvolumeclaim/workspace                Bound     workspace      200Gi      RWO                           7d5h<br>
</pre><br>
PV的状态为Bound状态表示已经绑定到对应的PVC上。Jenkins的Pod状态为1/1就说明启动成功了，可以通过绑定Ingress的域名访问了。或者使用Service配置中的nodePort端口访问Kubernetes任意节点IP：nodePort。<br>
<br>查看Jenkins密码：<br>
<pre class="prettyprint">kubectl exec -it jenkins-0 -n kubernetes-plugin -- cat /var/jenkins_home/secrets/initialAdminPassword<br>
</pre><br>
<h3>Jenkins配置</h3>Jenkins安装完成后进入UI界面，首先需要安装需要的插件。<br>
<br>Jenkins可以根据实际情况选择适合的源：<br>
<br>系统管理->插件管理->高级<br>
<pre class="prettyprint">https://updates.jenkins.io/update-center.json #官方源<br>
https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json #清华源<br>
</pre><br>
<br>然后安装需要的插件：<br>
* Git pPugin<br>
* Maven Integration Plugin<br>
* Docker Plugin<br>
* Kubernetes Continuous Deploy Plugin<br>
* Kubernetes Plugin<br>
* Publish Over SSH Plugin<br>
* SSH Agent Plugin<br>
* SSH Build Agents Plugin<br>
* promoted builds plugin<br>
* Promoted Builds (Simple)<br>
<br><h3>配置</h3>Kubernetes Plugin插件安装完成后在Jenkins设置里面点击【系统配置】拉到最下面就可以看到一个Cloud。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/6d7fdfdde713954b7e6920dad3d1c248.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/6d7fdfdde713954b7e6920dad3d1c248.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
单击之，添加一个云：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/9d323b97e7944edd8d91583309d49f8d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/9d323b97e7944edd8d91583309d49f8d.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>名称：名字随便取，后面连接云的时候需要这个名字。</li><li>Kubernetes地址：访问Kubernetes Master上kube-apiserver服务的地址。</li><li>Kubernetes命名空间：Jenkins部署在哪个命名空间里面了。</li><li>Jenkins地址：Jenkins访问地址。</li><li>Jenkins通道（这特么是一个大坑） ：访问Jenkins容器内50000端口地址。因为Jenkins的Service配置文件中我把50000端口映射为nodePort，再加上我配置了DNS所以我这里写了域名：端口号的格式，也可以使用IP地址+端口号。</li></ul><br>
<br>因为Jenkins-Master和Jenkins-Slave都在Kubernetes集群内部，所以写ClusterIP:端口号应该也是可以的，但是我没试过，略略略：），地址只要能访问到容器内部的50000端口就可以，但是有一点需要注意，这里的格式不能加http不能加/感觉应该是协议的问题，但是还没搞懂。<br>
<br>点击连接测试，是否能够成功。<br>
<h3>测试</h3>连接成功后，创建一个流水线Job进行测试使用。<br>
<pre class="prettyprint">podTemplate(label: 'jnlp-slave', cloud: 'kubernetes', containers: [<br>
containerTemplate(name: 'maven', image: '10.0.0.59/jenkins/maven:3.3.9-jdk-8-alpine', ttyEnabled: true, command: 'cat'),<br>
],<br>
volumes: [<br>
persistentVolumeClaim(mountPath: '/root/.m2', claimName: 'maven-m2'),<br>
persistentVolumeClaim(mountPath: '/home/jenkins/agent/workspace', claimName: 'workspace'),<br>
]<br>
)<br>
&#123;<br>
node("jnlp-slave")&#123;<br>
  stage('Build')&#123;<br>
      git branch: 'master', url: 'http://root:qrGw1S_azFE3F77Rs7tA@gitlab.gemantic.com/java/$JOB_NAME.git'<br>
      container('maven') &#123;<br>
          stage('Build a Maven project') &#123;<br>
              sh 'mvn clean package -U deploy'<br>
          &#125;<br>
      &#125;<br>
  &#125;<br>
  stage('deploy')&#123;<br>
      sshPublisher(publishers: [sshPublisherDesc(configName: '76', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '/data/script/jenkins.sh $JOB_NAME', execTimeout: 120000000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '/data/kubernetes/service/$JOB_NAME', remoteDirectorySDF: false, removePrefix: 'target', sourceFiles: 'target/$JOB_NAME*.jar')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])<br>
  &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
Pipeline解读：<br>
<ul><li>podTemplate创建了一个Pod模版。Cloud字段指定了连接哪个Kubernetes云，Kubernetes就是刚才创建一个一个Kubernetes，云的名字就是kubernetes。</li><li>Maven镜像为了加快下载速度，我传到了私有仓库，官方镜像就是把IP地址去掉对应的镜像。</li><li>persistentVolumeClaim定义了目录挂载，把Maven构建的缓存目录.m2和构建产生的数据目录workspace都挂载了一下</li><li>下面的Pipeline指定后面的操作在jnlp-slave中（也就是Pod模版同时也是Slave节点）</li><li>在build操作中，需要先拉取代码，GitLab拉取代码这里使用了GitLab的root token进行拉取的。GitLab用户获取Token方法：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/4393e613edf33186ec0a4292c4c318fb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/4393e613edf33186ec0a4292c4c318fb.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>下面就是开始编译啦～，因为是一个Java服务，编译完成后会生成一个jar包。</li><li>deploy步骤就是开始发布了，下面的Pipeline是用流水线语法自动生成的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/b3b6e21bdb946f6260630d55c46660a2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/b3b6e21bdb946f6260630d55c46660a2.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>然后点击构建进行测试。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/f1cd1bedc7a25e3dd162af43366c687d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/f1cd1bedc7a25e3dd162af43366c687d.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>构建过程中，可以看到Pod调度到master3上进行构建了。</li><li>构建过程中用到了两个镜像，一个Maven（已被上传到了私有仓库），一个inbound-agent镜像。inbound-agent镜像是官方的镜像，和Maven的关系是都在同一个Pod中共享数据，并和Jenkins-master进行交互。（inbound-agent镜像怎么修改为私有仓库镜像还没搞明白，总是去公网下载速度慢）</li><li>构建过程中不断的下载Java程序依赖的各种包，因为是第一次时间久了一点，但是我们已经把.m2缓存目录挂载出来了，下次再次构建的时候就可以大大缩减构建的时间。</li><li>workspace也被挂载了出来，每次构建的数据也会保留，以备不时之需。</li></ul><br>
<br>构建成功后查看NFS共享目录中的数据：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/e42304e056327798ac7852b6aae69fa3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/e42304e056327798ac7852b6aae69fa3.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<pre class="prettyprint">root@sa-storage:/data/dev_jenkins# du -sh m2/<br>
218M    m2/<br>
root@sa-storage:/data/dev_jenkins# du -sh workspace/<br>
65M workspace/<br>
</pre><br>
至此所有的需求都实现了，Slave实现了动态伸缩，相关的目录都被挂载出来了。<br>
<h3>排错</h3>kubectl get pod -n kubernetes-plugin -o wide命令可以查看Slave的Pod状态，如果出现问题Slave一直无限重启，需要查看Pod日志。<br>
<pre class="prettyprint">kubectl logs `kubectl get pod -n kubernetes-plugin -o wide|grep jnlp-slave|awk '&#123;print $1&#125;'` -n  kubernetes-plugin<br>
</pre><br>
每次重启Pod的名字都会重新生成，而且正在创建中的Pod是无法查看日志的，就算有问题Pod也是瞬间就重启了，所以只能上面的这个命令无限的刷。手速快的可以手动哦～手速跟不上的也可以写个循环哒。主要就是文中说的那个大坑，那个坑过去，小问题都可以通过看日志解决的。如果忘记大坑在哪里，可以ctrl+f搜索关键字 “大坑” 哦～<br>
<br>原文链接：<a href="https://blog.csdn.net/qq_36165389/article/details/106833259" rel="nofollow" target="_blank">https://blog.csdn.net/qq_36165 ... 33259</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            