
---
title: 'Win10 20H1_20H2更新翻车：不装新Edge浏览器所致'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210514/s_db9abc63f9c141f48f321cd7e3403126.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 14 May 2021 10:43:44 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210514/s_db9abc63f9c141f48f321cd7e3403126.jpg'
---

<div>   
<p>本周，微软面向Windows 10 20H1/20H2功能更新发布了累积更新 KB5003173。不过用户反馈在安装过程中出现了神秘的“0x800f0922”错误代码，而且Windows 10会自动回滚到此前版本中。</p>
<p><strong>一位受到影响的用户反馈，DISM方式并不能解决这个问题，只有重新安装微软Edge浏览器之后更新才可以成功安装。</strong></p>
<p>根据 Reddit 上用户的反馈，Windows 10 的错误 0x800f0922 主要影响的设备是那些移除基于 Chromium 的新版 Edge 浏览器，而使用经典版Edge浏览器的用户。</p>
<p>在安装 KB5003173 过程中，该更新就会试图安装Chromium Edge。然而，当它检测到系统驱动器（C:\Program Files (x86)\Microsoft\Edge\）中的一个空Edge文件夹时，更新安装失败。这可能发生在Microsoft Edge文件夹没有被正确删除的情况下。</p>
<p>有两个解决方法--从微软的网站上手动重新安装Microsoft Edge，并重新尝试累积更新安装。或者干脆通过导航到C:\Program Files (x86)\Microsoft\删除Edge文件夹。这将使累积更新成功恢复浏览器，并继续安装，受影响的用户证实了这一点。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210514/db9abc63f9c141f48f321cd7e3403126.jpg" target="_blank"><img alt="Win10 20H1/20H2更新翻车：不装新Edge浏览器所致" h="400" src="https://img1.mydrivers.com/img/20210514/s_db9abc63f9c141f48f321cd7e3403126.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/windows_10.htm"><i>#</i>Windows 10</a></p>
<p class="url">
     
<span>责任编辑：雪花</span>
</p>
        
</div>
            