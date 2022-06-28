
---
title: '跑分低了6%：微软免费杀软Defender被曝影响Intel处理器性能'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220628/s_cf330cdb8bc6432eae868005c5ca54ba.png'
author: 快科技（原驱动之家）
comments: false
date: Tue, 28 Jun 2022 15:09:04 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220628/s_cf330cdb8bc6432eae868005c5ca54ba.png'
---

<div>   
<p>近日，有开发者在调试软件的过程中发现，微软于Win10/11系统中自带的Windows Defender杀毒软件，会对Intel处理器的性能造成影响。</p>
<p>以5GHz全核运行的i9-10850K为例，<span style="color:#ff0000;"><strong>在开启Windows Defender后，Cinebench的跑分成绩降低了约1000分，损失了6%左右的性能。</strong></span></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220628/cf330cdb8bc6432eae868005c5ca54ba.png" target="_blank"><img alt="跑分低了6%：微软免费杀软Defender被曝影响Intel处理器性能" h="478" src="https://img1.mydrivers.com/img/20220628/s_cf330cdb8bc6432eae868005c5ca54ba.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>据悉，<strong>在Win10/11上使用Intel酷睿第8代到第11代的用户都出现了类似的问题，而AMD处理器则没有受到影响。</strong></p>
<p>该Bug出现的原因，是由于Windows Defender会随机调用Intel酷睿处理器包括三个固定功能计数器在内的，所有七个硬件性能计数器。</p>
<p>在调用计数器的同时，Windows Defender会将这些计数器设置为“mode 2”，<strong>导致其他程序无法正常使用，造成计数器控制寄存器在0x222和0x332之间不断变化，继而影响性能。</strong></p>
<p>目前，微软官方尚未公布该问题的处理方法，用户可以手动覆盖计数器配置，或启用第三方杀毒软件。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220628/cc01dec66f8f402fa7b939c8867a14d1.jpg" target="_blank"><img alt="跑分低了6%：微软免费杀软Defender被曝影响Intel处理器性能" h="400" src="https://img1.mydrivers.com/img/20220628/s_cc01dec66f8f402fa7b939c8867a14d1.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：乃河</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/windows_11.htm">Windows 11</a><a href="https://news.mydrivers.com/tag/windows_defender.htm">Windows Defender</a><a href="https://news.mydrivers.com/tag/weiruan.htm">微软</a>  </p>
        
</div>
            