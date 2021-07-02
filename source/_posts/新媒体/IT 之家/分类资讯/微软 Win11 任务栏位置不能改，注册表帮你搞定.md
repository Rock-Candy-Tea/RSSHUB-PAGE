
---
title: '微软 Win11 任务栏位置不能改，注册表帮你搞定'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/6/6823ff96-8832-4d72-8030-03235419fbdd.png'
author: IT 之家
comments: false
date: Fri, 02 Jul 2021 01:51:13 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/6/6823ff96-8832-4d72-8030-03235419fbdd.png'
---

<div>   
<p><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 7 月 2 日消息 微软近日发布了全新的 Windows 11 操作系统，将在圣诞节期间推出正式版，并表示用户可于 2022 年免费升级到 Win11。</p><p>IT之家此前报道，Win11 去掉了任务栏的<span class="accentTextColor">停靠位置选项</span>，用户无法像在 Win10 中那样自由拖动或者在设置中进行选择。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/6/6823ff96-8832-4d72-8030-03235419fbdd.png" title="微软 Win11 任务栏位置不能改，注册表帮你搞定" referrerpolicy="no-referrer"></p><p>然而，据 B 站 UP 主 @咬勾，Win11 任务栏位置依然可以在<span class="accentTextColor">注册表</span>中进行修改，用户需打开注册表编辑器，定位到：</p><blockquote><p>\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3</p></blockquote><p>然后双击 <span class="accentTextColor">Settings</span> 打开。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/1dda8bb1-17f6-4c9d-a147-3c20983aefc5.png" w="969" h="231" title="微软 Win11 任务栏位置不能改，注册表帮你搞定" width="969" height="195" referrerpolicy="no-referrer"></p><p>在打开的二进制编辑器中，找到<span class="accentTextColor">红框标注的 03</span>（FE 下方的那个），将其修改为 <span class="accentTextColor">00（左）、01（上）、02（右）</span>，接着使用软媒魔方重启 Windows 资源管理器，即可改变任务栏位置。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/9eaf5416-0f3a-4b60-98d1-78b4b077ce00.png" w="770" h="477" title="微软 Win11 任务栏位置不能改，注册表帮你搞定" width="770" height="477" referrerpolicy="no-referrer"></p><p>IT之家测试，修改后确实可以改变任务栏位置，只不过体验并不怎么好。放在左右两侧会不停闪烁，放在上方虽然可以正常显示，但开始菜单会<span class="accentTextColor">从下往上打开</span>，而且只能在最左边显示。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/91a000bc-b1d4-4cdf-a69c-676d75228c8c.png" w="1440" h="557" title="微软 Win11 任务栏位置不能改，注册表帮你搞定" width="1440" height="317" referrerpolicy="no-referrer"></p><p>目前，Reddit 上已有用户针对 Win11 任务栏表示了自己的不满，@TPGJosh 发文要求微软重新考虑，并引起网友热议。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/6/fdd7aa43-8f72-4372-b362-accc12367a56.png" w="731" h="861" title="微软 Win11 任务栏位置不能改，注册表帮你搞定" width="731" height="861" referrerpolicy="no-referrer"></p>
          
</div>
            