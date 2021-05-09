
---
title: '微软Edge意外阻止了Firefox浏览器安装程序 并将其标记为有害'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0509/ab65fdf35154bea.png'
author: cnBeta
comments: false
date: Sun, 09 May 2021 07:40:50 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0509/ab65fdf35154bea.png'
---

<div>   
<strong>一些用户报告说，当试图下载Firefox安装程序时，Microsoft
Edge正在阻止它的所有版本，如正式版、Beta版、Dev版和nightly版。Edge下载页会提示说Firefox的安装程序<strong>“</strong>被阻止，因为它可能伤害你的设备<strong>”</strong>。</strong>这是因为微软Edge使用SmartScreen来实现提前保护用户免受恶意网站和文件的侵害，但似乎这中间遇到了问题。<br>
<p>Edge中的Microsoft Defender SmartScreen会根据已知的文件列表分析用户下载的文件，如果它遇到用户不熟悉或不常下载的应用程序或应用程序安装程序，就会阻止文件下载并显示警告。该保护功能默认在设置>隐私、搜索和服务>"Microsoft Defender SmartScreen"中启用。</p><p>Edge还提供了一个可选的功能来阻止潜在不需要的程序下载。你可以通过切换 "阻止可能不需要的程序"设置将其打开。</p><p><img src="https://static.cnbetacdn.com/article/2021/0509/ab65fdf35154bea.png" title alt="Edge-says-Firefox-installer.exe-was-blocked-because-it-could-harm-your-device..png" referrerpolicy="no-referrer"></p><p>回到事件中，在Firefox浏览器被阻拦的案例中，根据Reddit的帖子[<a href="https://www.reddit.com/r/firefox/comments/n7gige/ms_edge_blocking_firefox_installer_download/">1</a>] [<a href="https://www.reddit.com/r/firefox/comments/n749u5/firefox_nightly_installer_can_harm_your_device_i/">2</a>]，一些用户证实Edge在下载Firefox浏览器时发出警告，说安装程序可能损害他们的设备。你可以在上面的截图中看到Edge从下载浮框中显示的警告:"Firefox installer.exe被阻止了，因为它可能伤害你的设备"。</p><p>一些受影响的用户说，他们在禁用Microsoft Defender SmartScreen后成功下载并安装了Firefox，截止发稿，问题已经被<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>从服务器端修复，这一误判问题已经无法重现。</p><p>禁用Defender SmartScreen设置使Edge错误地将Firefox的下载视为不安全，不过这倒是可以被看成是正常的，当关闭安全浏览功能时，Google Chrome也会这样做。</p><p>如果你现在面临这个问题，关闭SmartScreen是不明智的，最好的方法是先使用其他浏览器下载Firefox或者其它被误判的应用。</p><p>事实上，过去有一次Bing搜索引擎就曾将流行的VLC播放器官网标记为危险，过了很短的时间，提示就被取消了。</p>   
</div>
            