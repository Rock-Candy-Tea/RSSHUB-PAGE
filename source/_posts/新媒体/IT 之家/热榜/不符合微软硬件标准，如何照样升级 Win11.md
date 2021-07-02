
---
title: '不符合微软硬件标准，如何照样升级 Win11'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/7/28430292-c4d2-40be-9887-288b0f6658cf.jpg'
author: IT 之家
comments: false
date: Thu, 01 Jul 2021 16:36:48 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/7/28430292-c4d2-40be-9887-288b0f6658cf.jpg'
---

<div>   
<p>微软在 6 月 24 日公布了下一代 Windows 系统 Win11，现在微软通过 Insider 通道，推送 Win11 的预览版了。不过，Win11 是存在硬件配置要求的，如果你的电脑不符合标准，且在 6 月 24 日之前没有进入到 Insider 通道，那么就无法升级到 Win11 预览版！</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/28430292-c4d2-40be-9887-288b0f6658cf.jpg" w="700" h="314" title="不符合微软硬件标准，如何照样升级 Win11" width="700" height="314" referrerpolicy="no-referrer"></p><p>然而，办法总是比问题多。现在，网络上流传出了绕过微软限制、强行升级到 Win11 预览版的方法，一起来看看吧！</p><h2>一、注册表修改法</h2><p>通过修改注册表，可以让不符合硬件标准的电脑也收到 Win11 预览版的推送。在修改前，稳妥起见请先备份注册表，这通过很多第三方工具都可以实现，这里就不展开介绍了。</p><p>在修改注册表前，需要先确认电脑是不是无法收到 Win11 预览版的推送。在 Win10 设置中，进入 Insider 计划，并选择“Dev”通道，重启电脑后检查更新，如果没有 Win11 预览版的推送，即可按照以下步骤修改注册表。</p><p>1、通过开始菜单，输入“regedit”找到注册表并开启；</p><p>2、在注册表中，定位到以下目录</p><pre class="brush:javascript;toolbar:false">HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsSelfHost\UI\Selection</pre><p>3、找到“UIBranch”键值，如果没有则新建一个，新建类型选择“字符串值”（以下操作皆如此），开启它的编辑框后，将键值修改为“Dev”；</p><p>4、同样，修改或者新建“ContentType”，编辑其键值为“Mainline”；</p><p>5、修改或者新建“Ring”，键值为“External”；</p><p>6、修改或者新建“UIRing”，键值为“External”；</p><p>7、修改或者新建“UIContentType”，键值为“Mainline”；</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/7fc58b61-1e6f-44c9-9957-85a848e530f6.jpg" w="700" h="234" title="不符合微软硬件标准，如何照样升级 Win11" width="700" height="234" referrerpolicy="no-referrer"></p><p>8、在注册表定位到以下目录：</p><pre class="brush:javascript;toolbar:false ai-word-checked">HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsSelfHost\Applicability</pre><p>9、修改或者新建“BranchName”，键值为“Dev”</p><p>10、修改或者新建“ContentType”，键值为“Mainline”；</p><p>11、修改或者新建“Ring”，键值为“External”；</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/bee404fd-39ad-4dab-9dd8-c909c9dde30f.jpg" w="700" h="353" title="不符合微软硬件标准，如何照样升级 Win11" width="700" height="353" referrerpolicy="no-referrer"></p><p>12、保存并关闭注册表，重启电脑，再开启设置面板，确认进入了 Insider 计划的 Dev 通道，然后再通过 Windows Update 检查更新。如无意外，应该就可以收到 Win11 预览版的推送了。</p><h2>二、脚本修改法</h2><p>实际上脚本法的本质也是修改注册表，不过有人将这些步骤做成了 CMD 运行的脚本，并放置在 GitHub 上开源。在修改前，最好也先备份一下注册表，下面是详细步骤。</p><p>1、通过以下地址，从 GitHub 相关页面的“Asset”中，下载 Source code 文件；</p><p>下载地址：</p><p><a href="https://github.com/abbodi1406/offlineinsiderenroll/releases" target="_blank">https://github.com/abbodi1406/offlineinsiderenroll/releases</a></p><p>2、解压压缩包，从中找到“OfflineInsiderEnroll.cmd”, 右键点击使用管理员权限运行；</p><p>3、在命令行窗口中，选择“1”Dev 通道，并按下回车键确认；</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/573eb32f-8b27-4c81-89fd-6b526146d138.jpg" w="700" h="258" title="不符合微软硬件标准，如何照样升级 Win11" width="700" height="258" referrerpolicy="no-referrer"></p><p>4、重启电脑，随后到设置面板中的 Windows Update 检查更新，应该就可以收到 Win11 预览版的推送了。</p><p>Win11 无疑是近年来 Windows 最大的更新，按照计划，Win11 将会在今年下半年发布正式版，期待 Win11 的正式到来吧。</p>
          
</div>
            