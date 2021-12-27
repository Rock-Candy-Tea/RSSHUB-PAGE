
---
title: '俄罗斯自主芯片Elbrus-8C未通过SberTech评估'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1227/75a51ac4102f91d.webp'
author: cnBeta
comments: false
date: Mon, 27 Dec 2021 03:35:43 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1227/75a51ac4102f91d.webp'
---

<div>   
<strong>俄罗斯联邦储蓄银行（Sberbank）旗下技术部门 SberTech 在多个工作负载中评估了俄罗斯自主的制造的 MCST Elbrus-8C 处理器，但结果完全令人失望，该处理器未能通过测试</strong>。在谈及失败的原因，测试人员表示主要有“内存不足，内存速度慢，核心少，频率低。功能要求完全没有得到满足”等。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1227/75a51ac4102f91d.webp" alt="5r3dctqm.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">据悉 Elbrus-8C 处理器于 2009 年开始研发，2014 年官方公开了相关信息。它是一枚十分强大的 8 核 64 位处理器， 采用 28nm 工艺打造，默认主频率为 1.3GHz，频率并不算高，不过其浮点运算性能可以达到 250 GFLOPS。</p><p style="text-align: left;">Elbrus-8C 处理器还拥有 4M 的二级缓存和 16M 三级缓存，每个时钟周期每个内核可以执行 25 条指令，支持动态二进制翻译技术，支持多线程编程技术，确保有效执行的应用程序和操作系统，并集成了特殊模式的硬件安全技术，支持 C、C + +、 Java、 Fortran 77、 Fortran 90 等多种编程语言。</p><p style="text-align: left;">在本月初的 Elbrus 合作伙伴日会议上，SberTech 的代表 Anton Zhbankov 表示：“与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>至强‘Cascade Lake’相比，Elbrus-8C 服务器处理器非常弱，内存不足[256MB]，内存速度慢，核心少，频率低。功能要求完全没有得到满足”。</p><p style="text-align: left;">事实上，SberTech的评估是对Elbrus-8C平台在银行应用中的首次深入测试。评估人员将双插槽和四插槽Elbrus-8C机器（每箱16-32个核心）与该公司目前使用的基于英特尔 Xeon Gold 6230 处理器的双处理器服务器进行了比较。SberTech 无法测试更强大的 Elbrus-8CB，因为它尽管已经正式推出，但仍未上市。</p><p style="text-align: left;">作为欧洲最大的银行之一，Sberbank 提供的服务不仅仅是银行业务，它对硬件有一定的要求，并有自己的测试方法来评估它考虑部署的机器。这个方法包括以下内容。</p><blockquote style="text-align: left;"><p style="text-align: left;">● 功能测试（44个参数，以确保一个平台可以运行Sber需要的东西，并且可以按照Sber的需要进行管理）。</p><p style="text-align: left;">● 合成测试（使用PostreSQL套件的PGbench以及SPEC CPU 2017）。</p><p style="text-align: left;">● 应用测试（使用Java应用程序）。</p></blockquote><p style="text-align: left;"><strong>Elbrus-8C 评估总结</strong></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1227/bf5606088f541dd.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1227/bf5606088f541dd.png" alt="QQ截图20211227112850.png" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">SPEC CPU 2017 基准测试的情况看起来稍微好一些，四芯片 Elbrus-8C 比双英特尔 Xeon Gold 6230 机器慢 2.62（基础）~3.15（峰值）倍，这并不糟糕，因为 SberTech 工程师预计会有 20 倍到 30 倍的差异。然而，应该注意的是，X86系统和Elbrus机器都没有达到服务器制造商提交给Spec.org的峰值性能数据。</p><p style="text-align: left;">同时，在PGbench/PostreSQL测试中，Xeon Gold 6230 机器比 Elbrus-8C 服务器好1.7（只读配置文件）~3.3（读写配置文件）倍（以每10万美元的交易量计算），具体取决于工作负载，这很重要，但并没有大幅降低。</p><p style="text-align: left;">对于Java应用程序或模拟Java工作负载，Elbrus-8C平台的情况变得更加糟糕，其响应时间高出23倍至26倍，并且不符合Sber的任何服务质量要求。</p>   
</div>
            