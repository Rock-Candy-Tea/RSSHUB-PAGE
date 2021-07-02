
---
title: '不符合Win11硬件标准？教你如何照样升级Win11'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210702/Sdadd6cdc-0937-4676-a7c6-c65284a2fef6.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 02 Jul 2021 00:21:24 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210702/Sdadd6cdc-0937-4676-a7c6-c65284a2fef6.jpg'
---

<div>   
<p>微软在6月24日公布了下一代Windows系统Win11，现在微软通过Insider通道，推送Win11的预览版了。</p>
<p>不过，Win11是存在硬件配置要求的，如果你的电脑不符合标准，且在6月24日之前没有进入到Insider通道，那么就无法升级到Win11预览版！</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210702/dadd6cdc-0937-4676-a7c6-c65284a2fef6.jpg" target="_blank"><img alt="不符合Win11硬件标准？教你如何照样升级Win11" h="269" src="https://img1.mydrivers.com/img/20210702/Sdadd6cdc-0937-4676-a7c6-c65284a2fef6.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>然而，办法总是比问题多。现在，网络上流传出了绕过微软限制、强行升级到Win11预览版的方法，一起来看看吧！</p>
<p><strong>一、注册表修改法</strong></p>
<p>通过修改注册表，可以让不符合硬件标准的电脑也收到Win11预览版的推送。在修改前，稳妥起见请先备份注册表，这通过很多第三方工具都可以实现，这里就不展开介绍了。</p>
<p>在修改注册表前，需要先确认电脑是不是无法收到Win11预览版的推送。在Win10设置中，进入Insider计划，并选择“Dev”通道，重启电脑后检查更新，如果没有Win11预览版的推送，即可按照以下步骤修改注册表。</p>
<p>1、通过开始菜单，输入“regedit”找到注册表并开启；</p>
<p>2、在注册表中，定位到以下目录</p>
<p>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsSelfHost\UI\Selection</p>
<p>3、找到“UIBranch”键值，如果没有则新建一个，新建类型选择“字符串值”（以下操作皆如此），开启它的编辑框后，将键值修改为“Dev”；</p>
<p>4、同样，修改或者新建“ContentType”，编辑其键值为“Mainline”；</p>
<p>5、修改或者新建“Ring”，键值为“External”；</p>
<p>6、修改或者新建“UIRing”，键值为“External”；</p>
<p>7、修改或者新建“UIContentType”，键值为“Mainline”；</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210702/fcc5056d-c719-44b7-99e0-b5d455fd6990.jpg" target="_blank"><img alt="不符合Win11硬件标准？教你如何照样升级Win11" h="200" src="https://img1.mydrivers.com/img/20210702/Sfcc5056d-c719-44b7-99e0-b5d455fd6990.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>8、在注册表定位到以下目录：</p>
<p>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsSelfHost\Applicability</p>
<p>9、修改或者新建“BranchName”，键值为“Dev”</p>
<p>10、修改或者新建“ContentType”，键值为“Mainline”；</p>
<p>11、修改或者新建“Ring”，键值为“External”；</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210702/b8a61124-fb6b-4c0c-8025-6426525df2c1.jpg" target="_blank"><img alt="不符合Win11硬件标准？教你如何照样升级Win11" h="302" src="https://img1.mydrivers.com/img/20210702/Sb8a61124-fb6b-4c0c-8025-6426525df2c1.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>12、保存并关闭注册表，重启电脑，再开启设置面板，确认进入了Insider计划的Dev通道，然后再通过Windows Update检查更新。如无意外，应该就可以收到Win11预览版的推送了。</p>
<p>二、脚本修改法</p>
<p>实际上脚本法的本质也是修改注册表，不过有人将这些步骤做成了CMD运行的脚本，并放置在GitHub上开源。在修改前，最好也先备份一下注册表，下面是详细步骤。</p>
<p>1、通过以下地址，从GitHub相关页面的“Asset”中，下载Source code文件；</p>
<p><strong>下载地址：<a class="f14_link" href="https://github.com/abbodi1406/offlineinsiderenroll/releases" target="_blank">https://github.com/abbodi1406/offlineinsiderenroll/releases</a></strong></p>
<p>2、解压压缩包，从中找到“OfflineInsiderEnroll.cmd”,右键点击使用管理员权限运行；</p>
<p>3、在命令行窗口中，选择“1”Dev通道，并按下回车键确认；</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210702/9c0d22ce-1dcb-4394-bf63-6d87eb2ae326.jpg" target="_blank"><img alt="不符合Win11硬件标准？教你如何照样升级Win11" h="221" src="https://img1.mydrivers.com/img/20210702/S9c0d22ce-1dcb-4394-bf63-6d87eb2ae326.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>4、重启电脑，随后到设置面板中的Windows Update检查更新，应该就可以收到Win11预览版的推送了。</p>
<p>Win11无疑是近年来Windows最大的更新，按照计划，Win11将会在今年下半年发布正式版，期待Win11的正式到来吧。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210702/44e827f17aaa4cc89bc87b6f1816e528.png" target="_blank"><img alt="不符合Win11硬件标准？教你如何照样升级Win11" h="399" src="https://img1.mydrivers.com/img/20210702/s_44e827f17aaa4cc89bc87b6f1816e528.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.pconline.com.cn/win10/1430/14304864.html">太平洋电脑网</a></span>
<span>责任编辑：陈驰</span>
</p>
        
</div>
            