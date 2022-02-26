
---
title: 'Win11最新开发版出现重大程序Bug：解决方法已经出炉'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202202/6219ec86b15ec05e2d203db2_1024.jpg'
author: ZAKER
comments: false
date: Sat, 26 Feb 2022 01:09:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202202/6219ec86b15ec05e2d203db2_1024.jpg'
---

<div>   
<p>近日，微软面向 Dev 频道推送了 Windows 11 Build 22563 版本更新，<strong>但有用户反馈，此次更新后，出现了较为严重的程序崩溃 Bug。</strong></p><p>据悉，在 Build 22563 版本中，当用户用右键单机开始按钮，或使用 Win+X 快捷键调出菜单时，系统的资源管理器 "explorer.exe" 会崩溃并重启。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202202/6219ec86b15ec05e2d203db2_1024.jpg" data-height="337" data-width="600" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202202/6219ec86b15ec05e2d203db2_1024.jpg" referrerpolicy="no-referrer"></div></div>从反馈情况来看，该 Bug 有较高的触发概率，但好在已经有用户发现了解决这一 Bug 的方法。<p></p><p>在此次更新中，<strong>微软为 Win11 加入了新的可折叠式任务栏，开启后即可解决资源管理器的崩溃问题。</strong></p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres2.myzaker.com/202202/6219ec86b15ec05e2d203db3_1024.jpg" data-height="383" data-width="600" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202202/6219ec86b15ec05e2d203db3_1024.jpg" referrerpolicy="no-referrer"></div></div>用户可以在 ViveTool 中，通过输入<strong>"vivetool addconfig 26008830 2"</strong>命令行来开启该任务栏，而想要回到旧版则需输入 "vivetool delconfig 26008830 2"。<p></p><p>目前，该 Bug 的具体原因尚不清楚，但有观点认为，这个能够解决 Bug 的新版任务栏，就是导致程序崩溃的 " 罪魁祸首 "。</p><p>有网友分析后认为，此次更新后，右键单击或 Win+X 调出菜单时，系统会监测任务栏是否进行折叠，<strong>但旧版任务栏不存在折叠功能，这会导致空指针引用，继而导致程序崩溃。</strong></p><p>不过目前，这一推断尚未得到微软官方的承认或回应。</p><p></p><div class="img_box" id="id_imagebox_2" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_2" data-original="http://zkres1.myzaker.com/202202/6219ec86b15ec05e2d203db4_1024.jpg" data-height="399" data-width="600" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202202/6219ec86b15ec05e2d203db4_1024.jpg" referrerpolicy="no-referrer"></div></div><p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            