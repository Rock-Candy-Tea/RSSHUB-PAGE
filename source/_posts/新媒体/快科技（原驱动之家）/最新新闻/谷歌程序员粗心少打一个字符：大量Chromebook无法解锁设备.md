
---
title: '谷歌程序员粗心少打一个字符：大量Chromebook无法解锁设备'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210724/S65fdf45f-ec72-4123-ad73-5dca226c4bcf.png'
author: 快科技（原驱动之家）
comments: false
date: Sat, 24 Jul 2021 16:43:31 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210724/S65fdf45f-ec72-4123-ad73-5dca226c4bcf.png'
---

<div>   
<p>近日，谷歌为Chromebook推送了ChromeOS 91，具体版本号为91.0.4772.165。</p>
<p>但是，这次更新出现重大Bug，导致用户的ChromeBook无法正常解锁，官方已经紧急撤销更新。</p>
<p>多数用户反馈，在更新到此版本后，在登录时即便输入了正确的密码，但还是卡在了锁屏界面，无法正常进入桌面，有的设备甚至会循环重启。</p>
<p>而开发者从谷歌官网的源码中发现，这个问题是由一个低级错误引发的。</p>
<p>从下图可以看出，判断两个条件之间“&&”，但是程序员漏打了一个“&”，导致系统无法正常对设备解密登陆。</p>
<p style="text-align: center"><img alt="谷歌程序员粗心少打一个字符：大量Chromebook无法解锁设备" h="202" src="https://img1.mydrivers.com/img/20210724/S65fdf45f-ec72-4123-ad73-5dca226c4bcf.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>现在谷歌已经紧急发布修复补丁，解决了这个低级错误。</p>
<p style="text-align: center"><img alt="谷歌程序员粗心少打一个字符：大量Chromebook无法解锁设备" h="273" src="https://img1.mydrivers.com/img/20210724/S8f5351f4-252c-4fc5-bf45-b00cb35bb520.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p align="center"> </p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/guge.htm"><i>#</i>谷歌</a><a href="https://news.mydrivers.com/tag/chromebook.htm"><i>#</i>chromebook</a></p>
<p class="url">
     
<span>责任编辑：祥云</span>
</p>
        
</div>
            