
---
title: 'Windows 11部分版本的任务管理器CPU使用率数据被认为是不准确的'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0522/0972accadcbeca1.jpg'
author: cnBeta
comments: false
date: Sun, 22 May 2022 02:24:07 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0522/0972accadcbeca1.jpg'
---

<div>   
虽然不是每个用户在游戏时都会主动监测硬件资源的使用情况，但发烧友和评论家经常打开统计数据，看看某些游戏和其他应用程序是如何被硬件处理的。在这样的测试运行中，开发了有用的帧时间分析工具的CapFrameX，在衡量Ryzen
7 5800X3D在《古墓丽影》（SotTR）上的性能时，注意到一个奇怪的异常情况。<br>
<p>在运行游戏的一个场景中，<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 build 22621上报告的处理器使用率似乎异常低，而这个场景通常对CPU来说是相当紧张的。16个线程中只有一个线程似乎报告了正确的使用率，而所有其他线程的使用率都低于10%。</p><p>CapFrameX注意到这个问题，尽管它不确定是什么原因造成的。</p><p>在Windows 11上的核心使用率报告完全不正确。对于SotTR+这个特定场景和设置，正常情况应该是>80%。发生了什么？最近的更新是否改变了处理器占用率监测的行为？</p><p><a href="https://static.cnbetacdn.com/article/2022/0522/0972accadcbeca1.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0522/0972accadcbeca1.jpg" title alt="1653146578_sottr_win_11_cpu_usage_5800x3d_(source-_capframex).jpg" referrerpolicy="no-referrer"></a></p><p>CapFrameX提供了一张有关场景的屏幕截图。统计数据是使用CapFrameX自己的工具在屏幕上显示的，并与显示类似数据的HWiNFO的快照一起附上。虽然这里注意到的错误有可能是一个特定的应用程序问题，但CapFrameX坚持认为它在所有测试的游戏中都是持续出现的。</p><p><img src="https://static.cnbetacdn.com/article/2022/0522/24d646582415222.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>值得注意的是，CapFrameX，可能还有HWiNFO，都是基于Windows事件追踪（ETW）的追踪机制。因此，有可能ETW中存在某种错误，导致这种误读。</p><p>在Google上快速搜索后，我们找到了<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>论坛上的一个主题，用户"AndreasRes"报告了一个类似的问题。在这种情况下，我们注意到任务管理器的使用率非常高，甚至达到了100%，而<a data-link="1" href="https://microsoft.pvxt.net/e4yLO" target="_blank">Xbox</a> Game Bar和<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">微星</a>主板实用工具Dragon Centre的使用率却低得多。</p><p><a href="https://static.cnbetacdn.com/article/2022/0522/b37d7e842aca482.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0522/b37d7e842aca482.jpg" title alt="1653150868_task_manager_cpu_usage_100_game_bar_usage_2_combined.jpg" referrerpolicy="no-referrer"></a></p><p>虽然该帖子是去年发起的，但最近在2022年也有更多的用户加入进来报告问题，最新的build 22621测试版是发生问题的主要场合。</p><p><img src="https://static.cnbetacdn.com/article/2022/0522/d5df6be8c631f6d.jpg" title alt="1653161766_sottr_win_11_cpu_usage_5800x3d_windows_builld_(source-_capframex).jpg" referrerpolicy="no-referrer"></p>   
</div>
            