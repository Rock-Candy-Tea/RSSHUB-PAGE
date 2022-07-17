
---
title: 'Win11新Bug导致任务栏图标离奇消失：微软发布临时修复方法'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220717/s_6c8fda3ef3d349c9a5de8aa52500f3bc.png'
author: 快科技（原驱动之家）
comments: false
date: Sun, 17 Jul 2022 15:38:18 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220717/s_6c8fda3ef3d349c9a5de8aa52500f3bc.png'
---

<div>   
<p>近日，有用户在微软反馈中心提交了新的Bug，表示自己的Win11系统任务栏图标因为不明原因“离奇消失”，并且找不到修复方法。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220717/6c8fda3ef3d349c9a5de8aa52500f3bc.png" target="_blank"><img alt="Win11新Bug导致任务栏图标离奇消失：微软发布临时修复方法" h="337" src="https://img1.mydrivers.com/img/20220717/s_6c8fda3ef3d349c9a5de8aa52500f3bc.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>目前，<span style="color:#ff0000;"><strong>微软已经对该Bug做出了回应，明确Bug原因的同时，给出了临时修复方法。</strong></span></p>
<p>据悉，该Bug的罪魁祸首是Win11的IRIS服务，该服务疑似与Windows聚焦等功能有关，但微软从未明确承认过。</p>
<p>想要修复该Bug，需要用管理员模式打开命令符管理器（CMD），然后输入命令<strong>“reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\IrisService /f && shutdown -r -t 0”</strong>。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220717/b529e632c0be41838098f712e8130649.jpg" target="_blank"><img alt="Win11新Bug导致任务栏图标离奇消失：微软发布临时修复方法" h="198" src="https://img1.mydrivers.com/img/20220717/s_b529e632c0be41838098f712e8130649.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>该命令会删除IRIS服务的注册表值，从而解决问题。</p>
<p>一般来说，在输入该命令后，系统会自动重启，在开机后问题就会得到解决。</p>
<p>值得一提的是，<strong>早在2020年，Win10就曾出现过任务栏不显示图标的Bug</strong>，不过当时出现问题的诱因是设备内存不足。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220717/9e07bb7a9af044cfab36375c84872075.jpg" target="_blank"><img alt="Win11新Bug导致任务栏图标离奇消失：微软发布临时修复方法" h="400" src="https://img1.mydrivers.com/img/20220717/s_9e07bb7a9af044cfab36375c84872075.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：乃河</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/windows_11.htm">Windows 11</a><a href="https://news.mydrivers.com/tag/tubiao.htm">图标</a><a href="https://news.mydrivers.com/tag/bug.htm">Bug</a>  </p>
        
</div>
            