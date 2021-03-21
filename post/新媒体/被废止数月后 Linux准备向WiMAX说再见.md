
---
title: 被废止数月后 Linux准备向WiMAX说再见
categories: 
    - 新媒体
    - cnBeta - 最新
author: cnBeta - 最新
comments: false
date: Sun, 21 Mar 2021 13:50:57 GMT
thumbnail: https://static.cnbetacdn.com/article/2021/0321/cb6019e18f8d3ca.jpg
---

<div>   
<strong>Linux瘦身持续中，除了传统的IDE驱动代码准备从主线Linux内核中移除，现在接受最后审判的还有WiMAX通信网络支持。</strong>在Linux 5.11中，内核将WiMAX网络代码降级到了内核的"暂存"区域，并声明如果没有人站出来维护代码，就会将其删除。<br>
 <p>事实上WiMAX通信网络在世界上已经近乎消失，所以几乎可以肯定其内核支持将随着Linux 5.13被移除。</p><p><img src="https://static.cnbetacdn.com/article/2021/0321/cb6019e18f8d3ca.jpg" title alt="2.jpg" referrerpolicy="no-referrer"></p><p>在2008年的CES展会上，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>提出了自己的下一代无线广域网通信方案，在十多年前IEEE 802.16 / WiMAX被认为是有前途无线互联网接入技术，特别是在偏远地区和其他有趣的用例。但如今，除了一些机场采用的AeroMACS无线解决方案和一些偏远地区的WiMAX小众部署外，并没有多少人采用它。就连WiMAX论坛自己的认证产品注册材料也已经下架了一段时间。</p><p>在英特尔大力推广WiMAX的13年后，Linux内核对其的支持正在被取消。此前，Linux内核也在近期逐步取消了英特尔MID的支持。WiMAX基础架构和英特尔i2400m驱动已经在主线Linux内核中存在多年，尽管没有得到维护，英特尔也没有像曾经那样参与其中的努力。经过几个月在内核的暂存区，也没有感兴趣的人站出来处理，所以内核团队已经决定直接删除这段代码。</p><p>Linux内核维护者Greg Kroah-Hartman已经在Linux 5.13的staging-next中排好了删除WiMAX的任务队列。他在提交中写道："WiMAX代码已经死亡，没有已知的用户。它已经在staging列表中足足待了5个月，没有人愿意承担代码库的维护和支持，所以我们现在就把它完全删除吧。如果有人来恢复它，简单的安排补丁是一个好的开始。"</p><p>丢掉这段没有维护的代码，可以让Linux内核减轻大约一万五千行代码。</p><p><img src="https://static.cnbetacdn.com/article/2021/0321/7b94c691924ebc7.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p>   
</div>
            