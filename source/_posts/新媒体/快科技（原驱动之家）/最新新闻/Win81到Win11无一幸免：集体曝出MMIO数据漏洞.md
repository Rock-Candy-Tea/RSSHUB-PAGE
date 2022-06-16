
---
title: 'Win8.1到Win11无一幸免：集体曝出MMIO数据漏洞'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220616/s_c67719e6d3924ed4ae392162b035a055.jpg'
author: 快科技（原驱动之家）
comments: false
date: Thu, 16 Jun 2022 19:30:50 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220616/s_c67719e6d3924ed4ae392162b035a055.jpg'
---

<div>   
<p>今天，微软和Intel发布公告，<span style="color:#ff0000;"><strong>表示在多款Intel处理器中存在一系列MMIO漏洞，这些漏洞可能会影响到从Win8.1到Win11的大部分Windows系统。</strong></span></p>
<p>根据微软在ADV220002安全公告中的描述，攻击者可能会利用这些漏洞跨过信任边界读取特权数据。</p>
<p>在云服务配置中，<strong>这一行为会导致一个虚拟机不正当的访问另一个虚拟机的信息；而在独立系统中，攻击者也能够通过运行特定程序，利用漏洞。</strong></p>
<p>而在Intel发布的INTEL-SA-00615安全公告中，则更为详细的描述了该漏洞是如何被利用的。</p>
<p>根据官方的介绍，处理器MMIO陈旧数据漏洞，是一类可以暴露数据的内存映射I/O（MMIO）的漏洞。</p>
<p>这类漏洞会导致陈旧数据被直接读取到架构，<strong>在攻击场景中，这些陈旧的数据可能驻留在微架构缓冲区中，恶意行为者或混淆的代理代码会借此传播数据。</strong></p>
<p>目前，<strong>微软和Intel已经对该漏洞执行了缓解措施</strong>，以便用户和管理员在启用决定措施之前将继续对影响和危险性能进行评估。</p>
<p>值得一提的是，此次漏洞同样波及了Linux系统，但已经进行了修补。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220616/c67719e6d3924ed4ae392162b035a055.jpg" target="_blank"><img alt="Win8.1到Win11无一幸免：集体曝出MMIO数据漏洞" h="320" src="https://img1.mydrivers.com/img/20220616/s_c67719e6d3924ed4ae392162b035a055.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：乃河</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/windows_11.htm">Windows 11</a><a href="https://news.mydrivers.com/tag/windows_10.htm">Windows 10</a><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm">Windows操作系统</a>  </p>
        
</div>
            