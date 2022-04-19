
---
title: 'Win11为何不显示秒针？真相揭开'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220419/1165c9ef-660e-4f2f-b88b-d6226116ff95.jpg'
author: 快科技（原驱动之家）
comments: false
date: Tue, 19 Apr 2022 06:30:53 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220419/1165c9ef-660e-4f2f-b88b-d6226116ff95.jpg'
---

<div>   
<p>和前代Windows相比，Win11作了很多大改动，但其中一些被人们认为是退步。</p>
<p>例如Win11的任务栏，功能相比Windows 10大幅削弱，无法直接拖动图标到任务栏中固定，无法移动任务栏位置，甚至时间不能显示秒数。</p>
<p>在Win10中，<span style="color:#ff0000;"><strong>尽管默认也不会显示时间秒数，但通过注册表可以实现这一功能，但该途径在Win11当中也走不通了。</strong></span></p>
<p style="text-align: center"><img alt="系统竟会变卡？微软解释为何Win11不显示秒针" h="886" src="https://img1.mydrivers.com/img/20220419/1165c9ef-660e-4f2f-b88b-d6226116ff95.jpg" style="border: black 1px solid" w="592" referrerpolicy="no-referrer"></p>
<p>微软官方确认了这一情况。微软表示，在Win11中不可能通过编辑注册表来启动任务栏显示的秒针，微软已经完全删除了该功能，原因是性能相关的问题。</p>
<p style="text-align: center"><img alt="系统竟会变卡？微软解释为何Win11不显示秒针" h="39" src="https://img1.mydrivers.com/img/20220419/00534d55-2b31-4e72-9a7d-6f5b5d262175.jpg" style="border: black 1px solid" w="535" referrerpolicy="no-referrer"><br>
在Win10中，修改注册表后任务栏可以显示秒数</p>
<p style="text-align: center"><img alt="系统竟会变卡？微软解释为何Win11不显示秒针" h="276" src="https://img1.mydrivers.com/img/20220419/88247580-e0c3-48f8-8fa4-7c3fb42b24ee.jpg" style="border: black 1px solid" w="338" referrerpolicy="no-referrer"><br>
Win7任务栏的时间浮窗可以显示秒针</p>
<p>微软在用户反馈下回应，称Win11的时钟不会在浮窗等区域显示秒针。</p>
<p>需要注意的是，在之前的Windows系统中，任务栏显示秒针也并不是默认选项，而是需要手动开启的可选项。</p>
<p>在之前，该特性曾经导致过内存相关的问题，远古的PC内存只有4MB，秒针会对性能造成显著影响。但这显然不是Win11不显示秒针的理由，大多数PC的内存已经超过了8GB。</p>
<p>那么为什么微软决定在Win11取消秒针呢？根据微软开发博客上的一篇新文章，原因仍然是性能。</p>
<p><span style="color:#ff0000;"><strong>虽然系统内存不再是主要问题，现在所有设备的内存都比4MB多得多，但在任务栏上显示秒针所需的频繁更新，仍然会使设备比平时更慢。</strong></span></p>
<p>以支持多用户配置的环境，如终端服务器为例。在支持多用户的服务器中，系统将尝试每秒更新一次任务栏时钟，而每个登录的用户都有自己的任务栏时钟。这意味着服务器将为一百个堆栈，绘制一百个任务栏时钟。</p>
<p>由于这个特殊的原因，服务器管理员通常会禁用“caret blinking”来减少CPU的使用，因为上百个用户的caret blinking会增加CPU的使用。事实上，许多服务器管理员完全禁用了任务栏时钟，以减少对处理能力的负荷。</p>
<p>同样的理论也适用于非终端服务器的系统，这包括个人电脑。</p>
<p>在性能的角度来看，如果任务栏显示秒针，那么Windows将需要花费额外的时间来更新时钟，而且“周期性活动”会阻止CPU进入低功耗状态，从而影响整体性能。</p>
<p>微软指出，周期性活动会阻止CPU进入低功耗状态，任何速率超过一分钟的周期性活动都会引起Windows性能团队的注意。</p>
<p>微软一直在努力减少周期性活动，如果周期性时间的最小周期为一分钟，对性能或电池备份有好处。</p>
<p>当然，对于用户而言，禁止通过修改注册表在任务栏显示秒针，并不是好消息，毕竟这少了一个选择。<strong>但根据微软的声明，目前微软的确没打算恢复注册表的该功能，至少目前如此。</strong></p>
<p>同时，微软也不打算在Win11恢复某些任务栏的相关功能。微软证实，不会恢复可移动任务栏等功能，因为仅有少数用户将任务栏设置在顶部、右侧或左侧。</p>
<p>但人们不能确定微软官方引用的数据，因为反馈中心中要求最多的功能之一就是可移动任务栏。在反馈中心中，可移动的任务栏是要求最多的功能之一，有多达6000次的投票。</p>
<p>不过，微软并没有说Win11中缺失的功能以后永远也不会恢复，但像可移动任务栏这样的功能并不是优先项，微软当前正在专注于拖放等平板电脑体验的相关改进。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220419/d882fa7b012d4d088cc986d046b071f9.jpg" target="_blank"><img alt="Win11为何不显示秒针？真相揭开" h="337" src="https://img1.mydrivers.com/img/20220419/s_d882fa7b012d4d088cc986d046b071f9.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：振亭</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm">Windows操作系统</a><a href="https://news.mydrivers.com/tag/weiruan.htm">微软</a><a href="https://news.mydrivers.com/tag/zhinengshouji.htm">智能手机</a>  </p>
        
</div>
            