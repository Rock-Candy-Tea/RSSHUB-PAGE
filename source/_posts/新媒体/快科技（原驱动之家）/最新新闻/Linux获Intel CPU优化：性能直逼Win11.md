
---
title: 'Linux获Intel CPU优化：性能直逼Win11'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220828/s_f7fc07868775427b8fadb1c5bf84e3b8.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sun, 28 Aug 2022 14:31:41 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220828/s_f7fc07868775427b8fadb1c5bf84e3b8.jpg'
---

<div>   
<p>近日，Intel的Linux工程师Ricardo Neri为Linux内核提交了补丁，<strong>针对Linux系统环境下，Intel CPU的性能核心（P核心）与能效核心（E核心）之间的任务调度做出了改进。</strong></p>
<p>优化后，在混合有较高频率SMT内核和较低频率非 SMT 内核的处理器上，如果多个SMT同级处理器处于忙碌状态，低优先级的CPU会从较高优先级的内核中提取任务。</p>
<p>此外，Ricardo Neri删除了人为的SMT优先级调整，而是通过调整asym_packing负载平衡器的方式，识别具有多个繁忙同级的SMT内核，并让低优先级 CPU 拉取任务。</p>
<p>通过这一方法，<span style="color:#ff0000;"><strong>Linux能够更好的发挥Intel CPU的性能，在表现上已经能够与Win11相提并论。</strong></span></p>
<p>事实上，这已经不是Linux第一次获得Intel的CPU优化，在此前的5.18版本中，Linux就引入了一次性能优化，有效缩短了系统在性能方面与Win11的差异，现在这一差异也被补齐了。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220828/f7fc07868775427b8fadb1c5bf84e3b8.jpg" target="_blank"><img alt="Linux获Intel CPU优化：性能直逼Win11" h="401" src="https://img1.mydrivers.com/img/20220828/s_f7fc07868775427b8fadb1c5bf84e3b8.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

            
 <div style="overflow: hidden;font-size:14px;padding-top:30px;border-bottom:1px solid #eee;">
           <p class="zhuanzai">【本文结束】如需转载请务必注明出处：快科技</p>  
          <p class="url"><span style="color:#666">责任编辑：乃河</span></p>
        </div>
     
        
</div>
            