
---
title: 'Apache Dolphin Scheduler 2.0.6 发布，新增 Master 召回策略'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-be2fb3dc03a9b3ac3112ef0a30ba6a95751.png'
author: 开源中国
comments: false
date: Wed, 13 Jul 2022 10:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-be2fb3dc03a9b3ac3112ef0a30ba6a95751.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:center"><img height="383" src="https://oscimg.oschina.net/oscnet/up-be2fb3dc03a9b3ac3112ef0a30ba6a95751.png" width="900" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span><strong>版本发布</strong></span><span style="background-color:#5f91b7"> 2022/7/12 </span></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>近日，Apache Dolphin Scheduler 迎来了 2.0.6 版本发布。新版本对依赖和任务分布功能进行了重要改动，并针对 2.0.5 进行了 bug 修复，具体更新详见下文。</span></p> 
</blockquote> 
<h2 style="margin-left:0px; margin-right:0px"><span><strong>1</strong> 重大改动</span></h2> 
<p style="margin-left:0; margin-right:0"><span>Significant changes </span></p> 
<p><span>首先，此版本针对依赖和任务分布不均衡的问题进行了改动。</span></p> 
<h3 style="margin-left:0px; margin-right:0px"><span>01 </span><span><strong>依赖相关问题</strong></span></h3> 
<p><span>在上个版本，当依赖整个工作流时，如果启动工作流中一个任务，任务运行结束且成功，此时会判定整个工作流成功，这就缺乏对该工作流中其他任务的判断；当依赖具体任务时，如果启动工作流中其他一个任务，任务运行结束且成功，此时依赖因找不到最后启动工作流中的所依赖的任务而会卡住等待，而且用户也不知等待的原因。在这个版本，我们对依赖判定逻辑进行了重写：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span>新增了每 5s 检测依赖是否完成的逻辑</span></p> </li> 
 <li> <p><span>打印出依赖等待和失败的原因</span></p> </li> 
 <li> <p><span>当依赖整个工作流时，无论最后一个工作流启动多少个任务，会判定依赖周期内该工作流中所有任务最后一个状态。共有以下几种情况：当有任务未运行时，依赖失败；当有任务失败时，依赖失败；有任务正在运行时，依赖等待。</span></p> </li> 
 <li> <p><span>当依赖工作流中某个任务时，会直接根据依赖周期内所依赖任务最后一个状态进行判断</span></p> </li> 
</ul> 
<p style="text-align:center"><img height="305" src="https://oscimg.oschina.net/oscnet/up-0dfbeb4a9ec533ee9ed34cfa0616cee9655.png" width="1310" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px"><span>02 </span><span><strong>任务分布不均衡问题</strong></span></h3> 
<p><span>在上个版本，当有多个 worker 节点时，比如 3 个 worker 节点，所对应的负载分别是 0.1, 0.2, 0.2，如果按照默认的以负载来分配任务的逻辑，若一次启动 100 个任务，在启动任务的心跳周期内，可能任务会直接分配到负载为 0.1 的 worker 中，而其他两个 worker 分配不到任务，当 worker 的并发是 10 个任务时，另外 90 个任务在同一个节点排队，这就拉长了任务整体运行的时间。基于此问题，新版本增加了 Master 召回策略。</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span>在 worker 端，队列有等待分配队列（该队列会延迟执行队列）、等待执行队列、执行队列，在上个版本中，等待分配队列和等待执行队列是无限队列，限制其和执行队列相等。</span></p> </li> 
 <li> <p><span>master 在选择 worker 时，如果 worker 的等待执行队列为空，则将任务分配给负载最小的 worker；如果 worker 的等待队列不为空，则将任务分配给等待队列最小的 worker，若等待队列不为空且相等，就根据负载进行选择 worker；如果所有 worker 的等待队列已满，则阻塞 1 秒后再次选择 worker。</span></p> </li> 
 <li> <p><span>由于 worker 每次心跳会在 zk 中更新一次等待队列大小，如果在一次心跳周期内启动了大量的任务（本次心跳周期内等待队列还未更新），worker 获取到任务时先放到等待分配队列，等待分配队列会将任务给执行队列，执行队列满时，会放到等待执行队列，当执行队列、等待执行队列都满时，等待分配队列会每隔 1 秒尝试分配一次任务。当等待分配队列也满时，就会触发 master 召回策略，worker 把任务返回给 master，master 会重新分配。</span></p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px"><span><strong>2</strong> Bug 修复</span></h2> 
<p style="margin-left:0; margin-right:0"><span>Bug Fix</span></p> 
<p><span>其次，2.0.6 版本还重点针对上一版本的遗留问题进行了修复，主要包括：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span>修复资源重新上传提示名称重复问题</span></p> </li> 
 <li> <p><span>修复工作流保存后直接跳转到列表页的问题</span></p> </li> 
 <li> <p><span>修复资源名称比较长时保存失败问题</span></p> </li> 
 <li> <p><span>修复 LDAP 登录失败问题</span></p> </li> 
 <li> <p><span>修复邮件告警模板分隔线问题</span></p> </li> 
 <li> <p><span>修复发生 failover 时任务重试不起作用的问题</span></p> </li> 
 <li> <p><span>修复工作流有失败任务而恢复失败时工作流成功的问题</span></p> </li> 
 <li> <p><span>修复 master/worker 重复日志打印比较频繁问题</span></p> </li> 
 <li> <p><span>修复工作流停止时，子工作流和依赖节点不能停止的问题</span></p> </li> 
 <li> <p><span>修复偶发性不能获取任务执行状态的问题</span></p> </li> 
 <li> <p><span>修复偶发性工作流执行完成，子工作流卡住的问题</span></p> </li> 
 <li> <p><span>修复任务强制成功，而工作流状态不改变的问题</span></p> </li> 
 <li> <p><span>修复依赖相关问题</span></p> </li> 
 <li> <p><span>修复多个 worker 节点时，任务分布非常不均衡问题</span></p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px"><span><strong>3</strong> Release Note</span></h2> 
<p><span>https://github.com/apache/dolphinscheduler/releases/tag/2.0.6</span></p> 
<h2 style="margin-left:0px; margin-right:0px"><span><strong>4</strong> 资源下载</span></h2> 
<p style="margin-left:0; margin-right:0"><span>Resource download</span></p> 
<p><span>https://dolphinscheduler.apache.org/zh-cn/download/download.html</span></p> 
<h2 style="margin-left:0px; margin-right:0px"><span><strong>5</strong> 致谢</span></h2> 
<p style="margin-left:0; margin-right:0"><span>Acknowledgement</span></p> 
<p><span>Apache DolphinScheduler 2.0.6 版本在政采云生产环境历经近四个月的实践考验，政采云大数据平台组修复了一系列核心问题并提交了对应 PR(https://github.com/apache/dolphinscheduler/pull/10541)。在此，社区对政采云及政采云大数据平台组表示感谢，同时也感谢所有 2.0.6 版本的贡献者（按首字母排序），是你们的不懈努力让社区不断进步！</span></p> 
<blockquote> 
 <p style="margin-left:0px; margin-right:0px; text-align:center"><span style="color:#333333">Amy0104, calvinjiang, caishunfeng, JinyLeeChina, liqingwang, Hou-Shuaishuai, songjianet, Tianqi-Dotes, weeway, zhanqian-1993, zwZjut</span></p> 
</blockquote> 
<h2 style="margin-left:0px; margin-right:0px"><span><strong>参与贡献</strong></span></h2> 
<p style="margin-left:0px; margin-right:0px"><span style="background-color:#feffff">随着国内开源的迅猛崛起，Apache DolphinScheduler 社区迎来蓬勃发展，为了做更好用、易用的调度，真诚欢迎热爱开源的伙伴加入到开源社区中来，为中国开源崛起献上一份自己的力量，让本土开源走向全球。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">参与 DolphinScheduler 社区有非常多的参与贡献的方式，包括：</span></p> 
<p><img height="39" src="https://oscimg.oschina.net/oscnet/up-a583ab3215ed787457c0409c9066f9c84d2.png" width="833" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">贡献第一个PR(文档、代码) 我们也希望是简单的，第一个PR用于熟悉提交的流程和社区协作以及感受社区的友好度。</span></p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;"><span style="color:#000000">社区汇总了以下适合新手的问题列表：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdolphinscheduler%2Fissues%2F5689" target="_blank">https://github.com/apache/dolphinscheduler/issues/5689</a></span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span style="color:#000000">非新手问题列表：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdolphinscheduler%2Fissues%3Fq%3Dis%253Aopen%2Bis%253Aissue%2Blabel%253A%2522volunteer%2Bwanted%2522" target="_blank">https://github.com/apache/dolphinscheduler/issues?q=is%3Aopen+is%3Aissue+label%3A%22volunteer+wanted%22</a></span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span style="color:#000000">如何参与贡献链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdolphinscheduler.apache.org%2Fzh-cn%2Fdocs%2Fdevelopment%2Fcontribute.html" target="_blank">https://dolphinscheduler.apache.org/zh-cn/docs/development/contribute.html</a></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">来吧，DolphinScheduler开源社区需要您的参与，为中国开源崛起添砖加瓦吧，哪怕只是小小的一块瓦，汇聚起来的力量也是巨大的。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">来吧，开源社区非常期待您的参与。</span></p>
                                        </div>
                                      
</div>
            