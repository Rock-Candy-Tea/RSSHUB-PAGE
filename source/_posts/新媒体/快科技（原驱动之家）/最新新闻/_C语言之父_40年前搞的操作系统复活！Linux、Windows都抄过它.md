
---
title: '_C语言之父_40年前搞的操作系统复活！Linux、Windows都抄过它'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://icons.mydrivers.com/2021/news/ayun72890.png'
author: 快科技（原驱动之家）
comments: false
date: Wed, 24 Mar 2021 20:11:20 GMT
thumbnail: 'https://icons.mydrivers.com/2021/news/ayun72890.png'
---

<div>   
<p align="center"><a href="http://click.aliyun.com/m/1000253340/" target="_blank" rel="nofollow"><img src="https://icons.mydrivers.com/2021/news/ayun72890.png" width="600" height="74" referrerpolicy="no-referrer"></a>
           </p><p>Plan 9操作系统？没听说过….</p>
<p>但事实是，连Linux、Windows都得叫它一声“老大哥”！</p>
<p>没错，这套40年前由“C语言之父”开发的操作系统，如今仍然在深刻影响着Linux、Windows。</p>
<p>最新消息的消息是，拥有Plan 9版权的美国贝尔实验室，刚刚宣布下放版权给开发者社区。</p>
<p>就是说，Plan 9这个在幕后默默影响行业40年的分布式操作系统，要正式“复活”了。</p>
<p><strong>Plan 9系统是干什么的？</strong></p>
<p>大名鼎鼎的贝尔实验室，是C语言，以及Linux系统的前身Unix诞生地。</p>
<p>当然，这里也诞生了晶体管、激光器、太阳能电池、发光二极管、数字交换机 、通信卫星、电子数字计算机、蜂窝移动通信设备、长途电视传送、仿真语言、有声电影、立体声录音等等重大发明。</p>
<p>而Unix和C语言核心开发者，大家肯定不陌生，Ken Thompson和Dennis Ritchie，都是如雷贯耳的big name，且都获得因为这两项成就获得图灵奖。</p>
<p>但是外界鲜有人知的是，他俩80年代在贝尔实验室还开发了另外一套操作系统Plan 9。</p>
<p>其实，Plan 9一开始并不是这个系统的名字，只是这个项目的代号，名字来源于电影史上因为“烂到极致”而备受追捧的科幻片《外星9号计划》。</p>
<p>看来，C语言之父们，也是骨灰级科幻影迷~</p>
<p>之后，贝尔实验室因为种种原因停止了对这个项目的投资，早期研发工作完成后，这个项目就搁置了起来，“Plan 9”渐渐就变成了这个系统的名字。</p>
<p>为什么要开发这样一套系统？当时，Ken和Dannis意识到，分布式的数据存储调用方式日后会成为主流，所以需要做一套简洁优雅实用的系统来服务这种需求。</p>
<p>Plan 9的开发，没有依赖任何Unix已有的基础，而是完全另起炉灶。</p>
<p>以当时的眼光来看，Plan 9十分先进超前，模式与传统操作系统完全不同。</p>
<p>Plan 9的结构是一个松散耦合的服务集合，这些服务可能被托管在不同的机器上。</p>
<p>设计的关键概念是每个进程的名称空间：即服务可以映射到固定的本地名称上，因此，即使当前的服务被提供相同功能的其他服务所取代，使用这些服务的程序也不用改变。</p>
<p>Plan 9是真正的分布式操作系统，而不仅仅是集成了几个Unix功能这么简单。你可以毫不费力地在网络上的多台主机上执行任何程序，可以使用网络上任何主机的任何资源，包括文件、进程、图形、网络、磁盘。</p>
<p>如果Linux也能这样工作，那么就没人需要Kubernetes了。</p>
<p>通俗的说，如果Unix或Linux中 “一切都是文件”，那么Plan 9则是 “一切都是网络文件系统”。</p>
<p>如果你有一台笔记本和一台台式机，而连接了打印机的却只有台式机，那使用笔记本能不能直接打印？</p>
<p>在Linux中，你必须设置CUPS，打开网络端口，下载驱动程序，设置两台机器都能和打印机通信。</p>
<p>而在在Plan 9中，你的笔记本电脑只需要通过网络打开桌面的打印机文件就可以打印了。</p>
<p>Plan 9到底有多先进？尽管他本身被贝尔实验室雪藏起来，但是，Plan 9中的很多经典设计和思路，一直沿用至今。</p>
<p><strong>Linux、Windows、5G，都借鉴Plan 9</strong></p>
<p>Eric S. Raymond在他的著作中分析了为何Plan 9最终下马。</p>
<p>他认为，Plan 9最后会失败单纯只是因为它的完善程度不够大。当时，虽然Unix看来破破烂烂又有明显缺失，但是它还是能把工作完成，这就足以保住它的地位了。</p>
<p>开创性的Plan 9最终没能“起飞”，但它的创新却被许多商业操作系统所采用。</p>
<p>比如，Linux中广泛普及的通过文件系统提供操作系统服务的概念就出自Plan 9。</p>
<p>此外，Plan 9极简主义窗口系统设计已经被无数系统借鉴，包括Windows：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210324/b9ceb39d-cc9b-4c90-8e0e-e278ea6d2e03.png" target="_blank"><img alt="“C语言之父”40年前搞的操作系统复活！Linux、Windows都抄过它" h="450" src="https://img1.mydrivers.com/img/20210324/Sb9ceb39d-cc9b-4c90-8e0e-e278ea6d2e03.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>而今天在浏览器中普遍使用的UTF-8字符编码，最初就是为Plan 9发明的，并在Plan 9中首次实现。</p>
<p>Plan 9的分布式设计也在诺基亚-贝尔实验室的项目中得以延续，比如World Wide Streams，这套流处理程序今天部署在地理上相隔甚远的多个5G边缘云和核心云的计算节点上。</p>
<p>可以说，今天流行的微服务架构，早在几十年前，Plan 9就已经提出了。</p>
<p>从这个角度来看，Plan 9其实从来没有真正“隐退”过。</p>
<p>几十年来，一直有民间的爱好者自发组成社区对Plan 9进行开发，而最近，贝尔实验室则官宣完全“复活”Plan 9，直接将版权下放给开发者社区。</p>
<p><strong>Plan 9复活后要做什么？</strong></p>
<p>获得贝尔实验室官方认可的开发者社区，名字叫Plan 9基金会，是爱好者们自下而上组织起来的，2020年9月刚刚成立。</p>
<p>基金会的主页上，只写明了将来会致力于Plan 9的开发和应用，具体的工作计划还没有出台。</p>
<p>而贝尔实验室对于Plan 9能日后能发挥多大作用似乎也没有把握。</p>
<p>他们在官方声明中说：</p>
<p>贝尔实验室十分支持开源社区，而Plan 9可能使全球软件开发社区受益。</p>
<p>谁知道呢，也许Plan 9会成为新兴的分布式云基础设施的一部分，支撑着即将到来的工业革命。</p>
<p>好吧，看来贝尔实验室打算彻底“放生”Plan 9。</p>
<p>只是不知道，假如日后Plan 9真的能成气候，变成有巨大影响力的操作系统，贝尔实验室会不会后悔今天的决定呢？</p>
<p>最后，献上彩蛋一枚。</p>
<p>Plan 9的开发者之一，同时也是C语言最主要的发明者Dennis Ritchie，是一个十分传奇的计算机科学家。</p>
<p>有多传奇？在一众计算机大佬中，他是独一份没有博士学位的。</p>
<p>并且，他是出于一个“十分任性”的原因，自己放弃了博士学位。</p>
<p>想看他的故事，在后台回复“想看”，我们马上安排！</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/caozuoxitong.htm"><i>#</i>操作系统</a><a href="https://news.mydrivers.com/tag/biancheng.htm"><i>#</i>编程</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/3ZszI7PupWsuTvy69BwPnw">量子位</a></span>
<span>责任编辑：万南</span>
</p>
        
</div>
            