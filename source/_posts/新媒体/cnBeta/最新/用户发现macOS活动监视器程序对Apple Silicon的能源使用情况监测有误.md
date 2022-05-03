
---
title: '用户发现macOS活动监视器程序对Apple Silicon的能源使用情况监测有误'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0503/358fd6a743ce923.jpg'
author: cnBeta
comments: false
date: Tue, 03 May 2022 14:53:37 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0503/358fd6a743ce923.jpg'
---

<div>   
macOS中的活动监视器程序向Apple Silicon用户提供的数据可能不那么准确，一份报告称，该工具不能正确区分性能和效率核心的区别。活动监视器为用户和开发者提供了一种方法，告诉他们哪些应用程序在执行任务时占用的资源最多，能量最大。<br>
<p>在运行Apple Silicon的Mac上测试该工具的功能要素时，似乎核心识别方面的一个小错误可能使一些结果大打折扣。</p><p><a href="https://static.cnbetacdn.com/article/2022/0503/358fd6a743ce923.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0503/358fd6a743ce923.jpg" title alt="48221-94196-Activity-Monitor-xl.jpg" referrerpolicy="no-referrer"></a></p><p>使用活动监视器的CPU和能源数字，用户可以看到，据报道，在完成一项任务时，仅在效率核心上运行的应用程序代码比性能核心消耗更多的能量。由于效率核心的目的是要比性能核心更慢，但功耗更低，这个结果是相当矛盾的。</p><p>The Electric Light Company在配备M1 Max的Mac Studio上进行的测试涉及在8个性能核心和2个效率核心上运行测试程序。当每个核心类型的8个浮点计算线程，每个线程有10亿个循环时，8个性能线程在6.6秒内完成任务，而2个效率核心需要40.4秒。</p><p>然而，检查活动监视器的能量标签显示，性能核心持续的能量值为800，每个线程660，总共使用了5280个单元。同时，效率核心的能量值为194，总共消耗了7838个单位，每个线程980个。</p><p>如果从表面上看，这将推断出，在效率核心上运行这些特定的线程原来比性能核心的效率要低。报告称，这个问题是由活动监视器造成的，因为它无法区分具有固定频率的相同核心和具有可变频率的两种不同核心类型。</p><p>报告还发现，它在如何报告内核之间的负载方面也存在问题。一项测试确定在两个效率核心上运行两倍的代码量，在活动监视器中被报告为使用与一半的代码量相同的能量。</p><p>据认为，由于macOS如何控制效率核心的频率，不同的M1芯片的结果也是不一致的，所以M1处理报告的方式与M1 Pro也有可能有极大的不同。</p><p>报告补充说："在<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>更新活动监测器为M1芯片返回的数字之前，核心类型和频率的混淆使得它不仅没有用，而且实际上对比较CPU占用率或能量消耗具有误导性。相反，开发者应该考虑Powermetrics等工具，因为它提供了关于集群频率和功率使用的信息，以及活动驻留时间。"</p><p>目前还不清楚苹果是否有更新活动监视器的打算，在Apple Silicon发布后至今的时间里没有看到任何明显的改进。</p>   
</div>
            