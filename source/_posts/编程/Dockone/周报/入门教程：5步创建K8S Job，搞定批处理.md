
---
title: '入门教程：5步创建K8S Job，搞定批处理'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210331102149178.gif#pic_center'
author: Dockone
comments: false
date: 2021-04-05 12:10:30
thumbnail: 'https://img-blog.csdnimg.cn/20210331102149178.gif#pic_center'
---

<div>   
<br>Kubernetes jobs主要是针对短时和批量的工作负载。它是为了结束而运行的，而不是像deployment、replicasets、replication controllers和DaemonSets等其他对象那样持续运行。<br>
<br>本文将介绍如何创建Kubernetes jobs和cronjobs，以及一些小技巧。<br>
<br>Kubernetes Jobs会一直运行到Job中指定的任务完成。也就是说，如果pods给出退出代码0，那么Job就会退出。而在正常的Kubernetes中，无论退出代码是什么，deployment对象在终止或出现错误时都会创建新的pod，以保持deployment的理想状态。<br>
<br>在job运行过程中，如果托管pod的节点发生故障，Job pod将被自动重新安排到另一个节点。<br>
<h2>Kubernetes Jobs用例</h2>对于Kubernetes Jobs最好的用例实践是：<br>
<ol><li><br><strong>批处理任务</strong>：比如说你想每天运行一次批处理任务，或者在指定日程中运行。它可能是像从存储库或数据库中读取文件那样，将它们分配给一个服务来处理文件。</li><li><br><strong>运维/ad-hoc任务</strong>：比如你想要运行一个脚本/代码，该脚本/代码会运行一个数据库清理活动，甚至备份一个Kubernetes集群。<br>
<h2>如何创建Kubernetes Job</h2>在本例中，我们将使用Ubuntu 容器来运行一个带有for循环的shell脚本，并根据你传递给容器的参数来呼应消息。这个参数是一个数字，决定shell脚本循环应该运行多少次。</li></ol><br>
<br>例如，如果你传递了参数100，那么shell脚本将呼应消息100次然后容器将会退出。<br>
<br>你可以访问以下链接查看Dockerfile和shell脚本：<br>
<a href="https://github.com/devopscube/Kubernetes-jobs-example/tree/master/Docker" rel="nofollow" target="_blank">https://github.com/devopscube/ ... ocker</a><br>
<br>我们先从一个简单设置的job开始。<br>
<br><strong>Step1</strong>：使用自定义的Docker镜像创建一个job.yaml文件，命令参数为100。100将会作为参数传递给docker ENTRYPOINT脚本。<br>
<br><code class="prettyprint">apiVersion: batch/v1  kind: Job  metadata:      name: kubernetes-job-example      labels:     <br>
    jobgroup: jobexample  spec:      template:     <br>
    metadata:       <br>
      name: kubejob       <br>
      labels:         <br>
        jobgroup: jobexample     <br>
    spec:       <br>
      containers:       <br>
      - name: c         <br>
        image: devopscube/kubernetes-job-demo:latest         <br>
        args: [&quot;100&quot;]       <br>
      restartPolicy: OnFailure</code><br>
<br><strong>Step2</strong> ：使用kubectl创建一个job.yaml文件的job<br>
<br><code class="prettyprint">kubectl apply -f job.yam</code><br>
<br><strong>Step3</strong>：使用kubectl检查job的状态<br>
<br><code class="prettyprint">kubectl get jobs</code><br>
<strong>Step4</strong>：使用kubectl获取pod列表<br>
<br><code class="prettyprint">kubectl get po</code><br>
<strong>Step5</strong>：使用kubectl获取job pod 日志。使用你在输出中看到的Pod名称替换原本的Pod名称。<br>
<br><code class="prettyprint">kubectl logs kubernetes-job-example-bc7s9 -f</code><br>
<img src="https://img-blog.csdnimg.cn/20210331102149178.gif#pic_center" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<h2>并行运行多Job pods</h2>当一个job被部署后，你可以让它在多个Pod上并行运行。例如，在一个job中如果你想要运行6个 pods，同时并行运行2个pods，你需要添加以下2个参数到你的job manifets中：<br>
<br><code class="prettyprint">completions: 6<br>
parallelism: 2</code><br>
以下是带有那些参数的manifest：<br>
<br>```<br>
<br>apiVersion: batch/v1<br>
kind: Job<br>
metadata:<br>
  name: kubernetes-parallel-job<br>
  labels:<br>
    jobgroup: jobexample<br>
spec:<br>
  completions: 5<br>
  parallelism: 2<br>
  template:<br>
    metadata:<br>
      name: kubernetes-parallel-job<br>
      labels:<br>
        jobgroup: jobexample<br>
    spec:<br>
      containers:<br>
      - name: c<br>
        image: devopscube/kubernetes-job-demo:latest<br>
        args: ["100"]<br>
      restartPolicy: OnFailure<br>
```<br>
<h2>为Kubernetes Job生成随机名称</h2>你不能从一个job manifest文件中创建多个job，因为Kubernetes会报错，说存在一个同名的job。为了规避这个问题，你可以在元数据中添加 <strong>generateName</strong> 名称参数。<br>
<br>例如：<br>
<br>```<br>
<br>apiVersion: batch/v1<br>
kind: Job<br>
metadata:<br>
  generateName: kube-job-<br>
  labels:<br>
    jobgroup: jobexample<br>
```<br>
在上方示例中，每次你运行该manifest，job将以kube-job-作为前缀，后面跟着一个随机字符串来创建。<br>
<h2>如何创建Kubernetes CronJob</h2>如果你想按照特定的时间表运行批处理job，例如，每2个小时运行一次。你可以用cron表达式创建一个<strong>Kubernetes cronjob</strong>。Job会按照你在job中提到的时间表自动启动。<br>
<br>下面我们将介绍如何指定一个cron计划，你可以使用crontab生成器（<a href="https://crontab-generator.org/"></a><a href="https://crontab-generator.org/" rel="nofollow" target="_blank">https://crontab-generator.org/</a>）来生成自己的时间计划。<br>
<br><code class="prettyprint">schedule: &quot;0,15,30,45 * * * *&quot;</code><br>
下图显示了Kubernetes cronjob schedule语法。<img src="https://img-blog.csdnimg.cn/2021033110270199.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
如果我们以cronjob的形式每15分钟运行一次我们之前的job，manifest应该如下所示。创建一个名为<strong>cron-job.yaml</strong>的文件，并复制以下manifest：<br>
<br>```<br>
<br>apiVersion: batch/v1beta1<br>
kind: CronJob<br>
metadata:<br>
    name: kubernetes-cron-job<br>
spec:<br>
  schedule: "0,15,30,45 * * * *"<br>
  jobTemplate:<br>
    spec:<br>
      template:<br>
        metadata:<br>
          labels:<br>
            app: cron-batch-job<br>
        spec:<br>
          restartPolicy: OnFailure<br>
          containers:<br>
          - name: kube-cron-job<br>
            image: devopscube/kubernetes-job-demo:latest<br>
            args: ["100"]<br>
```<br>
让我们使用kubectl部署cronjob。<br>
<code class="prettyprint">kubectl create -f cron-job.yaml</code><br>
列出cronjobs：<br>
<br><code class="prettyprint">kubectl get cronjobs</code><br>
你可以列出cronjob pod并从处于运行状态或完成状态的pods中获取日志来检查Cronjob日志。<br>
<h2>手动运行Kubernetes CronJob</h2>在某些情况下，你可能希望以临时的方式执行cronjob。你可以通过从现有的cronjob创建一个job来实现。<br>
<br>例如，如果你想手动触发一个cronjob，我们应该这样做：<br>
<br>```<br>
<br>kubectl create job --from=cronjob/kubernetes-cron-job manual-cron-job<br>
```<br>
<strong>--from=cronjob/kubernetes-cron-job</strong>将复制cronjob模板并创建一个名为<strong>manual-cron-job</strong>的job。<br>
<h2>Kubernetes Job的关键参数</h2>根据你的需求，你还可以使用kubernetes jobs/cronjobs的几个关键参数：<br>
<ol><li><br>failedJobHistoryLimit &<br>
successfulJobsHistoryLimit：根据你提供的保留数量删除失败和成功的job历史记录。当你尝试列出job时，这对于减少所有失败的条目非常有用。例如：</li><li><br>   backoffLimit：如果你的Pod失败，重试的总次数。</li><li><br>  activeDeadlineSeconds：如果你想对cronjob的运行时间进行硬性限制，可以使用此参数。例如，如果你想只运行1分钟的cronjob，你可以将其设置为60。</li></ol><br>
<br>通过本文我们了解了创建Job以及Cron Job的步骤并且一些详细的配置过程和关键参数，希望藉由本文可以帮助你开始上手了解K8S Job和Cron Job，轻松搞定批处理任务！<br>
<blockquote><br>原文链接：<br>
  <a href="https://devopscube.com/create-kubernetes-jobs-cron-jobs/" rel="nofollow" target="_blank">https://devopscube.com/create- ... jobs/</a></blockquote>
                                
                                                              
</div>
            