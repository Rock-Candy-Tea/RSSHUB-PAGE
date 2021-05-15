
---
title: 'K8S CronJob简单入门，和手动重复操作Say Goodbye！'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210514110850250.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
author: Dockone
comments: false
date: 2021-05-15 08:03:03
thumbnail: 'https://img-blog.csdnimg.cn/20210514110850250.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
---

<div>   
<br>有时，调度一个应用程序进程、一些重复的操作（如发送邮件、告警、验证等）是极为必要的。在server上，我们通常使用一个cron，它极易设置和维护。如果你对此还不甚了解，可以访问以下链接，你需要知道的所有关于cron的信息都在此：<br>
<a href="https://en.wikipedia.org/wiki/Cron"></a><a href="https://en.wikipedia.org/wiki/Cron" rel="nofollow" target="_blank">https://en.wikipedia.org/wiki/Cron</a><br>
<br>在使用Docker的时候，你可以运行crontab来完成以上操作，但当你使用Kubernetes应该使用什么组件来进行上述操作呢？<br>
<br>实际上，Kubernetes的运行方式有所不同，因为在负载均衡的情况下可能有一个或多个相同服务的实例，而不管启动多少个实例crontab仅运行一次。另一方面，我们需要crontab为一个或多个pod的每个进程都运行一次。在Kubernetes中有一个称为CronJob的特性解决了这一问题。<br>
<br>本文将介绍CronJob如何工作及其限制条件，最后给出几个tips来帮助你避免常见错误。<br>
<br>以下示例均基于kind。<br>
<br><h2>如何创建CronJob：</h2><code class="prettyprint">apiVersion: batch/v1beta1<br>
kind: CronJob<br>
metadata:<br>
  name: my-cron-job<br>
spec:<br>
  schedule: &quot;*/1 * * * *&quot;<br>
  jobTemplate:<br>
    spec:<br>
      template:<br>
        spec:<br>
          containers:<br>
          - name: my-cron-job<br>
            image: curlimages/curl<br>
            resources:<br>
              limits:<br>
                cpu: &quot;1&quot;<br>
                memory: &quot;300Mi&quot;<br>
              requests:<br>
                cpu: &quot;1&quot;<br>
                memory: &quot;300Mi&quot;<br>
            args:<br>
            - /bin/sh<br>
            - -c<br>
            - date; echo &quot;Starting an example of CronJob&quot;; resp=$(curl -I --http2 https://www.google.com) ; echo $resp; exit 0<br>
          restartPolicy: Never<br>
  successfulJobsHistoryLimit: 3<br>
  failedJobsHistoryLimit: 3</code><br>
<br>CronJob已经创建，它每分钟运行一个curl镜像。<br>
<br>同时，你需要设置资源限制（如CPU和内存），如果你将AWS、Azure或GCP实例作为args，最好的可视化方式是在Google上进行简单的curl即可。<br>
<br>这一实例永远不会重启，而且成功和失败的历史job都有一个限制，在本例中这一次数设置为3。<br>
<ul><li>spec.successfulJobsHistoryLimit：要保留的成功完成的cronjob的数量</li><li>spec.failedJobsHistoryLimit：要保留的失败的cronjob的数量</li></ul><br>
<br>如果你想了解更多关于CronJob API的信息，我强烈建议你阅读以下链接中的内容：<br>
<a href="https://docs.koki.io/short/resources/cron-job"></a><a href="https://docs.koki.io/short/resources/cron-job" rel="nofollow" target="_blank">https://docs.koki.io/short/resources/cron-job</a><br>
<br>现在，运行以下命令以在Kubernetes中应用你的CronJob。<br>
<br><code class="prettyprint">$ kubectl apply -f cronjob.yml</code><br>
<br>如果没有错误发生，你能使用以下命令看到你最近配置的cronjob：<br>
<br><code class="prettyprint">$ kubectl get cronjob</code><br>
<br>我使用Lens来可视化所有可用的cronjob，它对Kubernetes中的跟踪和监控都非常有用。<br>
<br><img src="https://img-blog.csdnimg.cn/20210514110850250.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="图片" referrerpolicy="no-referrer"><br>
<br>查看日志：<br>
<br><img src="https://img-blog.csdnimg.cn/2021051411090160.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="图片" referrerpolicy="no-referrer"><br>
<br>运行以下命令即可删除这一条目：<br>
<br><code class="prettyprint">$ kubectl delete cronjob my-cron-job</code><br>
<br>在本例中运行了一个简单的Cron以及一个实例。<br>
<br>我发现CronJob有一个局限性是需要通过在每个进程中添加一行来为同一进程调度多个CronJob。但是，Kubernetes 1.8 beta中不提供CronJob，你必须使用并行机制（parallelism）复制相同的CronJob。对于另一个调度，你需要创建另一个cron条目。我期待着将来有机会为同一进程调度多个模式。<br>
<br><h2>结  论</h2>Kubernetes CronJob非常有用并且易于学习，你可访问以下链接阅读和了解有关API参数的更多信息，并运行一些测试以更好地了解其工作原理：<br>
<a href="https://docs.koki.io/short/resources/cron-job/" rel="nofollow" target="_blank">https://docs.koki.io/short/resources/cron-job/</a><br>
<blockquote><br>原文链接： <a href="https://dzone.com/articles/kubernetes-cronjob-an-introduction" rel="nofollow" target="_blank">https://dzone.com/articles/kub ... ction</a></blockquote>
                                
                                                              
</div>
            