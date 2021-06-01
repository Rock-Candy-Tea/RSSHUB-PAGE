
---
title: '苹果M1用着舒服的原因找到了 Intel：下次我也用'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210601/S9f686d43-c01a-4dbd-ae33-69104c6fc84a.png'
author: 快科技（原驱动之家）
comments: false
date: Tue, 01 Jun 2021 20:01:42 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210601/S9f686d43-c01a-4dbd-ae33-69104c6fc84a.png'
---

<div>   
<p>苹果M1又快又省电，除了跑分很高之外，实际体验上也有一种流畅感。</p>
<p><strong>苹果到底怎么做到的？</strong></p>
<p>原来除了硬件性能强大以外，软件层面也有优化技巧。</p>
<p>一位名叫Hoakley的程序员偶然发现了其中的秘密。</p>
<p>这老哥总之是有钱，M1和英特尔版的iMac都买了。业余时间他喜欢自己开发点实用小工具，比如压缩软件。</p>
<p>老哥在后台测试自己的压缩程序时发现，M1上只有4个核心在跑，还有4个闲着。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210601/9f686d43-c01a-4dbd-ae33-69104c6fc84a.png" target="_blank"><img alt="苹果M1用着舒服的原因找到了 Intel：下次我也用" h="243" src="https://img1.mydrivers.com/img/20210601/S9f686d43-c01a-4dbd-ae33-69104c6fc84a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>换到英特尔上试试，因为还没用到虚拟核心，是由8个真实核心共同承担了工作。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210601/cc015a3b-7799-4d21-b827-987317b075b0.png" target="_blank"><img alt="苹果M1用着舒服的原因找到了 Intel：下次我也用" h="122" src="https://img1.mydrivers.com/img/20210601/Scc015a3b-7799-4d21-b827-987317b075b0.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>回到M1里仔细一看，使用率高的还不是性能高的那4个，而是“效率核心”。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210601/65536060-42a9-46b5-bfcf-ef0bf8bda27c.png" target="_blank"><img alt="苹果M1用着舒服的原因找到了 Intel：下次我也用" h="303" src="https://img1.mydrivers.com/img/20210601/S65536060-42a9-46b5-bfcf-ef0bf8bda27c.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
△4核有难，4核围观</p>
<p>在M1芯片的8个CPU核心里，有4个被称作“Firestorm”的性能核心，另外4个是“Icestorm”效率核心，性能弱一些，不过功耗更低。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210601/7c73ac04-87c0-4275-82a5-98268943622b.png" target="_blank"><img alt="苹果M1用着舒服的原因找到了 Intel：下次我也用" h="366" src="https://img1.mydrivers.com/img/20210601/S7c73ac04-87c0-4275-82a5-98268943622b.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>研究了一下，老哥发现是自己把任务优先级设低了，提高以后，就能让4个性能核心参与进来。</p>
<p>老哥恍然大悟，原来这就是苹果的策略。</p>
<p>让优先度低的任务只占用效率核心，慢点就慢点吧，谁让你优先度低呢。</p>
<p>性能核心保持空闲状态，随时应对突发的高优先度任务。</p>
<p>App启动速度快，切换流畅的原因找到了：4个高性能的核心一直候着呢。</p>
<p><strong>非对称核心</strong></p>
<p>MacOS给开发者提供了4种优先级，分别是后台 (background)、实用 (utility)、用户发起的 (userInitiated)、用户交互的 (userInteractive)。</p>
<p>如果不指定的话就归为默认，由操作系统自己安排。</p>
<p>Hoakley老哥把自己的压缩软件改造成可以随时调整优先级的，然后准备了一个10GB的文件开始测试。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210601/9f584d2d-7d5d-4514-9002-6c19e4d1d976.png" target="_blank"><img alt="苹果M1用着舒服的原因找到了 Intel：下次我也用" h="85" src="https://img1.mydrivers.com/img/20210601/S9f584d2d-7d5d-4514-9002-6c19e4d1d976.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>在英特尔CPU上，最高优先级完成压缩需要23.3秒，调成最低优先级需要26秒。</p>
<p>在M1上，最高优先级运行只要14.1秒，调成后台优先级直接涨到101秒。</p>
<p>老哥认为，牺牲一些不重要任务的运行速度，换来的使用体验上的流畅，太值了。</p>
<p>比如备份文件就不用着急，即使慢到用15分钟备份不到1G也无所谓。</p>
<p>历史上也有这样一个反面教材。</p>
<p>2006年的时候Linux内核引入了一种叫完全公平队列 (Completely Fair Queuing)的I/O调度机制。</p>
<p>虽然在理论上能提升总体的运行效率，但用户正需要完成的任务总是有一些延迟才能执行。</p>
<p>因为用户体验太差，最终完全公平队列被大多数Linux发行版放弃了。</p>
<p>不过也有人不喜欢M1的这种机制，他认为在笔记本上这样做可以延长续航。但台式的iMac上真的要牺牲运行速度吗？反正都是插电源的。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210601/5936c30e-978b-42f5-ae52-5feaf858bd4c.png" target="_blank"><img alt="苹果M1用着舒服的原因找到了 Intel：下次我也用" h="211" src="https://img1.mydrivers.com/img/20210601/S5936c30e-978b-42f5-ae52-5feaf858bd4c.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>英特尔：在学了在学了</strong></p>
<p>其实CPU内核分性能核心和效率核心这件事，手机上的Arm芯片早就在做了。</p>
<p>甚至高通还在研发中的骁龙875，被曝光在这种架构基础上还增加了一个“超大核心”Cortex X1。总共1+3+4构成8个核心。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210601/fb3a685d-4996-477b-98ef-e815f668ca10.png" target="_blank"><img alt="苹果M1用着舒服的原因找到了 Intel：下次我也用" h="237" src="https://img1.mydrivers.com/img/20210601/Sfb3a685d-4996-477b-98ef-e815f668ca10.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>苹果M1将Arm平台带到了PC市场，让英特尔开了眼。</p>
<p>在CES2021上曝光的12代酷睿Alder Lake，英特尔也宣布要区分两种核心了。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210601/13b81917-a491-46f8-8150-bf34ab082a6c.png" target="_blank"><img alt="苹果M1用着舒服的原因找到了 Intel：下次我也用" h="337" src="https://img1.mydrivers.com/img/20210601/S13b81917-a491-46f8-8150-bf34ab082a6c.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>AMD知道了这个消息后，直接把挤牙膏的Zen3+项目给取消了，转而全力研发下一代Zen4架构处理器，代号Raphael，预计2022年发布。</p>
<p>不知道AMD会不会选择跟上这个潮流。</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/pingguom1.htm"><i>#</i>苹果M1</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/suVonokTaXjyK507s7AUcQ">量子位</a></span>
<span>责任编辑：万南</span>
</p>
        
</div>
            