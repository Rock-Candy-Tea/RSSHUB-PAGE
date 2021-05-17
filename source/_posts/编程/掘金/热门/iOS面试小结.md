
---
title: 'iOS面试小结'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c5455c5b1ec4f13a6ec50655c1fcae9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 17:55:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c5455c5b1ec4f13a6ec50655c1fcae9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>面试是职场中必经的一个步骤，在短短的几十分钟内去考察一个人的各项能力与综合素质，判断候选人与团队和团队匹配程度。从技术角度来看，面试更像是针对某些知识的讨论，寻求面试官和候选人的知识共通点，从而判断候选人是否满足团队需要。<strong>一个恰当的面试不是要难倒候选人，而是要引导候选人展示长处；从候选人熟悉的内容入手，考察技术细节和背后思考。</strong>
本文便谈一谈我对iOS面试的一些思考。</p>
<h3 data-id="heading-1">正文</h3>
<p>iOS的面试大致包括三大部分：<strong>基础知识、项目经历、代码考察</strong>。</p>
<p><strong>基础知识</strong>可以分为：
a.计算机基本知识：网络原理、操作系统、编译原理、数据结构、数据库等；
b.平台相关知识：OC基础、Runtime、内存管理、RunLoop、多线程、Xcode等；</p>
<p><strong>项目经历</strong>指的是做过的项目以及特定知识的积累，包括Crash分析、性能优化、持久化、代码架构、Pod化、模块化、组件化、持续集成等。</p>
<p><strong>代码考察</strong>是观察候选人在遇到问题如何理解题目、分析问题、实现过程，通常一些解题思路有贪心、动态规划、数据结构、递归、二分、排序等。</p>
<h4 data-id="heading-2">一、基础知识</h4>
<h5 data-id="heading-3">1、Objective-C基础</h5>
<p>为了切合iOS面试的主题，面试官通常都会从这一块知识开始入手。OC的知识非常庞杂，有时候遇到熟悉的内容就很了解，如果没有接触过可能就没有印象。比如说：<code>viewDidLoad</code> 的触发时机是发生在什么时候？以及延伸的问题，<code>viewDidLoad</code> 与loadView的关系以及先后顺序。</p>
<p>所以这部分知识，更合适问一些基础、共性的问题。比如说：</p>
<ul>
<li>常见的property有哪些属性？各自的属性应用场景有哪些？</li>
<li>介绍KVO和KVC的区别？KVO是否会引起循环引用？如果观察对象已经释放，会导致什么现象？用NSNotification 替代KVO，观察对象已释放会如何？如何手动实现KVO？</li>
<li>如何创建一个字符串常量？在.h声明并且实现会有什么问题？</li>
<li>category和extension的区别？category的实现原理？extension是否可以和category写在同一个文件？</li>
</ul>
<h5 data-id="heading-4">2、内存管理</h5>
<p>ARC和MRC，iOS开发者需要对两种内存管理方式都熟悉。一个了解MRC的开发者，遇到CF开头的函数怎么办？
很常见的面试切入点是从ARC的实现原理开始，引入<code>__strong/__weak/__unsafe_unretained/__autoreleasing</code>多个关键词的区别，再联想到循环引用，block实现原理，block持有外部的局部变量，autoReleasePool的使用，autoReleasePool与MRC的autorelease区别。</p>
<h5 data-id="heading-5">3、Runtime</h5>
<ul>
<li>Runtime机制介绍；</li>
<li>介绍isa、属性列表、方法列表、协议列表；</li>
<li>消息传递机制如何查找方法；</li>
<li>Category实现原理；</li>
<li>method swizzling原理；</li>
<li>imp和selector；</li>
</ul>
<h4 data-id="heading-6">4、RunLoop</h4>
<ul>
<li>unloop概述；</li>
<li>与线程的关系；</li>
<li>与FPS的关系；</li>
<li>RunLoop的实际应用；</li>
</ul>
<h5 data-id="heading-7">5、iOS系统</h5>
<ul>
<li>介绍scheme原理；</li>
<li>微信如何实现呼起第三方app？网页又如何呼起APP？</li>
<li>Push通知实现原理？客户端A直接向客户端B发Push是否可行？</li>
<li>代码签名；</li>
<li>沙盒机制；</li>
<li>地址空间随机化；</li>
</ul>
<h5 data-id="heading-8">6、编译原理</h5>
<ul>
<li>介绍整个编译的流程；</li>
<li>静态库、动态库的区别；</li>
<li>静态连接、动态链接的过程和区别；</li>
<li>在VC.h文件引入VC+Test.h(Category)会如何；</li>
</ul>
<h5 data-id="heading-9">7、多线程</h5>
<ul>
<li>多线程有哪些实现方式 ？</li>
<li>pthread、NSThread、GCD、NSOperationQueue有哪些应用场景？</li>
<li>多线程如何进行线程同步？</li>
<li>信号量、锁、代码块、原子变量常见有哪些应用场景？</li>
<li>实现一个变量的读写锁：读共享，写互斥；</li>
<li>如何用GCD实现100个任务执行，但是最高并发为10个任务？</li>
<li>GCD和线程的关系？GCD并发队列的线程爆炸？</li>
</ul>
<h5 data-id="heading-10">8、网络原理</h5>
<ul>
<li>介绍TCP三次握手？</li>
<li>socket编程中，何时进行三次握手？如何用socket发送数据？</li>
<li>HTTP协议中request和response有哪些数据组成部分？</li>
<li>在浏览器输入URL到页面加载发生了什么？</li>
<li>HTTP断点续传；</li>
<li>HTTP中间人攻击；（重点）</li>
<li>HTTPS实现原理；（加密通信原理）</li>
<li>HTTPS中间人攻击；</li>
<li>DNS劫持；</li>
</ul>
<h5 data-id="heading-11">9、Xcode</h5>
<ul>
<li>LLDB调试技巧：如何查看堆栈、修改内存、监控内存值变化、执行语句；</li>
<li>Xcode中的scheme配置是什么？</li>
<li>General中的Project和Target用处？</li>
<li>Certificate、Provisioning Profile、App ID的关系；</li>
<li>Image Assets Catalogs是什么？</li>
</ul>
<blockquote>
<p>以上是几点是对基础知识的一个简单梳理，虽不全面也能提供一个学习方向。</p>
</blockquote>
<p><strong>面试中遇到不会的知识点是很正常，只要能把自己所了解的知识完全表达出来就很好。</strong><br>
有两个亮点可以培养：<br>
1、广度，方方面面的知识都涉及，特别是基础知识要很牢固；<br>
2、深度，对常见问题能深入学习，经得起3、4次追问；</p>
<h4 data-id="heading-12">二、项目经历</h4>
<p>项目是能力的体现，实际项目中遇到的问题，可以分为几大类。</p>
<h5 data-id="heading-13">1、性能优化</h5>
<p>性能测试是优化的前提，如何发现存在的性能问题？</p>
<ul>
<li>怎么监控FPS降低？如何监控内存、CPU、GPU、加载速度、磁盘、崩溃等等；</li>
<li>如何进行电量优化？</li>
<li>Xcode 有哪些工具可以进行检查？</li>
<li>UITableView如何进行优化？</li>
<li>图片加载/下载的过程？怎么优化加载速度和内存占用？</li>
</ul>
<h5 data-id="heading-14">2、持久化</h5>
<p>数据库是App必不可少的组成部分。</p>
<ul>
<li>常见的数据库有哪些选择？</li>
<li>如何处理数据库的版本迁移、损坏保护、体积控制、大小统计？</li>
<li>序列化和反序列化；</li>
</ul>
<h5 data-id="heading-15">3、Crash分析</h5>
<ul>
<li>崩溃日志的地址如何还原成代码？</li>
<li>举一个最近遇到的崩溃，如何发现、定位、解决；</li>
<li>常见Crash类型有哪些？</li>
</ul>
<p>这是非常重要的一部分，没有处理过Crash的iOS工程师，怎么让人相信其能力？</p>
<h5 data-id="heading-16">4、代码架构</h5>
<p>这是非常不好考察的一个方向，但同样要有所准备。</p>
<ul>
<li>常见的设计模式有哪些？举个具体应用例子；</li>
<li>App的网络层如何设计？任务并发、回调处理、任务取消等；</li>
<li>MVVM是什么？有什么特点？</li>
<li>MVC框架怎么保证VC代码不膨胀？</li>
</ul>
<h5 data-id="heading-17">5、进阶知识点</h5>
<p>根据每个人的工作经历，可以挖掘自己进阶部分的知识点：</p>
<ul>
<li>逆向；</li>
<li>Pod库实现组件化；</li>
<li>跨平台：ReactNative、hybrid封装、jsbridge；</li>
<li>持续继承CI：脚本能力，工程理解；</li>
<li>质量体系：各种监控，实时告警处理；</li>
<li>音视频相关：AudioUnit、OpenGL ES、GPUImage、Metal、AVFoundation；</li>
</ul>
<h4 data-id="heading-18">三、代码考察</h4>
<p>简单的以LeetCode为标准，大部分公司的要求是在easy难度，进阶要求也只到medium难度。<br>
实际面试过程中，可能是长时间没有做面试题并且没有事先准备，也可能刚好考察到思维盲区，能顺利完成easy难度的题目都是凤毛麟角。<br>
<strong>做题并不是为了把题目解决，而是从做题过程去分析思考面试者遇到问题是如何思考解决，以及能否把代码用实现想法。</strong></p>
<p>选择性针对某些考察点去用对应题目也是一种方向，比如说：
1、对于一个整数m，计算其二进制表示有多少个1，并分析其复杂度；<br>
2、计算1~1000中，有多少个数字7；<br>
3、有两个很大的整数是用字符串来表示，实现一个函数加法，输出这两个字符串数字相加的结果；（大数加法）<br>
...</p>
<p>分享一些做题要点：<br>
1、快速理解题意，对于不清楚的条件及时提出疑问；<br>
2、三思而后行，先分析题目考察点，再进行方案分析，最后做复杂度分析；<br>
3、先讲思路，再进行coding；</p>
<p>理想结果：<br>
1、思路顺畅，实现过程简单清晰；<br>
2、边界处理完善，考虑周全；<br>
3、代码可读性强，具有一定的抽象和扩展；</p>
<h3 data-id="heading-19">总结</h3>
<p>每个面试官的经历不同，所擅长的方向也不一样。<br>
求职者会海投，而公司招聘也是海选，面试官的面试也会比较多。如果面试中能有部分知识在深度或者广度产生亮点，可以给面试官留下深刻的映象，从而更容易通过面试。</p>
<p>从我的视角去看iOS，把一些常见知识点给列出来：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c5455c5b1ec4f13a6ec50655c1fcae9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>题目只是一个引导，有经验的面试官往往会追问更深层次的问题，作为一个知识深度的考察。在根据上面的知识点去查漏补缺时，可以适当选择一些模块，更深入地去了解具体的实现。<br>
比如说：ARC/MRC => weak/strong 区别 => 循环引用 => weak实现原理 => runtime源码，<strong>不断追问自己其中的实现，直到网上查不到资料。</strong></p></div>  
</div>
            