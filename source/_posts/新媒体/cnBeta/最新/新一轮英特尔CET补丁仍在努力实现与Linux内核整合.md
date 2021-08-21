
---
title: '新一轮英特尔CET补丁仍在努力实现与Linux内核整合'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0821/86418f037c82f87.jpg'
author: cnBeta
comments: false
date: Sat, 21 Aug 2021 11:25:57 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0821/86418f037c82f87.jpg'
---

<div>   
虽然英特尔通常非常准时地为Linux下的主要新CPU功能提供支持，并经常在一般硬件发布到市场之前提前登陆，<strong>但他们围绕控制流执行技术（CET）的工作比正常时间长，并且仍在经历新一轮的代码审查，以获得对Linux主线内核的认可。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0821/86418f037c82f87.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>支持CET的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>Tiger Lake SoC现在已经有一年左右的时间，而英特尔针对Linux的CET工作可以追溯到2017年。英特尔控制流执行技术旨在通过间接分支跟踪和影子堆栈来防止ROP和COP/JOP式攻击。编译器侧的CET补丁很快就落地了，但Linux内核对这一安全功能的支持长期以来一直在进行，截至昨天已经到了第29轮审查。</p><p>上周五，第29轮CET影子堆栈补丁和CET间接分支跟踪补丁被发布。</p><p>32个支持CET影子堆栈的Linux补丁中的大部分变化是各种低级别的代码改进和调整，以及针对最新的上游内核状态的重新定位。CET间接分支追踪的10个补丁只是针对上游内核状态重新打了补丁。</p><p>一些Linux发行版和供应商的内核已经在使用英特尔CET补丁的树外形式，而我们还需要再等待看看这些补丁现在是否被认为已经准备好在下一周期的主线上使用，或者仍然需要更多轮的审查...... 希望它不像英特尔SGX那样需要40多轮的审查才可以进入主线内核。</p>   
</div>
            