
---
title: 'Win 11又出新Bug 搜索邮件也会卡死 微软：将解决'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211206/s_ea9fc41b60af484cbbc1d15c09afb726.png'
author: 快科技（原驱动之家）
comments: false
date: Mon, 06 Dec 2021 10:31:32 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211206/s_ea9fc41b60af484cbbc1d15c09afb726.png'
---

<div>   
<p>近日，Win 11又出现了一个新的Bug，<span style="color:#ff0000;"><strong>有用户发现在使用Outlook搜索旧邮件的时候，有可能会出现无法检索甚至直接卡死的情况。</strong></span></p>
<p>当前，<strong>微软已经确认并承认了这个Bug，并表示将在之后的版本中修复这一问题。</strong></p>
<p>据悉，<strong>该问题是由于微软在将系统升级至Win 11的过程中，删除了Windows搜索索引文件导致的</strong>，因此几乎所有版本的Outlook都将会受到这个Bug的影响。</p>
<p><strong>在微软推送更新前，用户可以通过绕过Windows搜索索引的方式来解决Outlook的卡死问题。</strong></p>
<p>用户可以在按Win+R打开运行窗口，输入<strong>regedit</strong>进入注册表编辑器，并找到<strong>“HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows”</strong>子项。</p>
<p>在该子项下，新建项，并重命名为<strong>“Windows Search”</strong>。</p>
<p>在完成“Windows Search”项的创建后，<strong>在该项下新建DWORD值，并命名为“PreventIndexingOutlook”，且将“PreventIndexingOutlook”的数值修改为1。</strong></p>
<p>在完成该修改后，<strong>关闭注册表编辑器并重启Outlook即可生效</strong>，从而解决Outlook搜索邮件时的卡死问题。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211206/ea9fc41b60af484cbbc1d15c09afb726.png" target="_blank"><img alt="Win 11又出新Bug 搜索邮件也会卡死 微软：将解决" h="399" src="https://img1.mydrivers.com/img/20211206/s_ea9fc41b60af484cbbc1d15c09afb726.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/weiruan.htm"><i>#</i>微软</a><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     
<span>责任编辑：乃河</span>
</p>
        
</div>
            