
---
title: 'Win11 正式版预装 Linux 子系统，还可将图形应用添加到开始菜单'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/7/e0cc3cb1-b75b-4fe1-8e8c-bddd24611612.png'
author: IT 之家
comments: false
date: Sun, 10 Oct 2021 00:14:52 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/7/e0cc3cb1-b75b-4fe1-8e8c-bddd24611612.png'
---

<div>   
<p data-vmark="a23c"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 10 月 10 日消息 微软此前在 Windows Insider Preview 构建版本中测试了 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Windows 11</a> 适用于 Linux 的子系统，安装您喜欢的 Linux 发行版就像从 Windows Terminal 直接键入“ wsl –install ”一样简单。</p><p data-vmark="0f24">虽然 Windows 11 正式版中并没有带来大家期盼的 <a class="s_tag" href="https://android.ithome.com/" target="_blank">Android</a> 子系统支持，但并不影响 Linux 子系统如期而至。这也给很多经常使用 Linux 应用的用户带来了方便。</p><p data-vmark="74cd">默认情况下，该环境还支持图形和声音，这意味着你还可以轻松在 Windows 上安装图形 Linux 应用程序，然后与本机正常的 Windows 11 应用程序无缝并存运行。</p><p data-vmark="5beb">IT之家了解到，Windows 11 还支持将 Linux 应用程序的快捷方式添加到开始菜单，这意味着目前可用的 Linux 图形化程序与普通环境下的 PC 应用并无不同，您同样可以在 Windows 上流畅地运行。</p><p data-vmark="7d9d">此外， <a class="s_tag" href="https://win10.ithome.com/" target="_blank">Windows 10</a> 版本 2004 及以上版本的系统也同样支持这一功能，更多内容还需要大家自己去发现。</p><p data-vmark="9448">YouTuber @Scott Hanselman 为大家带来了一期视频，展示了多种 WSL 功能：</p><p data-vmark="c03f"><a class="ithome_super_player" contenteditable="false" target="_blank" data-timestamp="1633824708705" data-vpreview-url="http://fb.video.weibocdn.com/qtgXI9PWlx07QtzTCexa01041202IZWL0E018.mp4?label=mp4_720p&template=1280x720.25.0&trans_finger=1f0da16358befad33323e3a1b7f95fc9&ori=0&ps=1BThihd3VLAY5R&Expires=1633828308&ssig=ZzWlt5cFAU&KID=unistore,video" href="https://weibo.com/6897433335/KC25hdPkF"></a></p><h2 data-vmark="9abf">使用 wsl --install</h2><p data-vmark="8815">微软表示，以前设置 WSL 的过程过于复杂，涉及到开启多个设置和安装多个软件包。该公司已将这一过程简化为只有一个命令。Windows 10 用户现在可以简单地用管理员权限打开一个命令提示符窗口，运行 wsl.exe --install。一旦你点击回车键，这个过程将自动启用 WSL 所需的可选功能，默认安装 Ubuntu 发行版，并在你的设备上安装最新的 WSL Linux 内核版本。当它完成后，重新启动你设备，发行版会在你再次启动后启动，完成安装。</p><p data-vmark="2642"><img src="https://img.ithome.com/newsuploadfiles/2021/7/e0cc3cb1-b75b-4fe1-8e8c-bddd24611612.png" w="924" h="395" title="Win11 正式版预装 Linux 子系统，还可将图形应用添加到开始菜单" width="924" height="351" referrerpolicy="no-referrer"></p><p data-vmark="2058">此外，你可以通过在 PowerShell 或 Windows 命令提示符中输入 wsl --list --online 命令，找到可供安装的 Linux 发行版列表。要安装 Ubuntu 默认版本以外的发行版，使用这个命令：wsl --install -d <DistroName></p><p data-vmark="993d">将 <DistroName> 替换为之前列表命令中找到的 Linux 发行版的名称。这个安装命令可以用于第一次安装，或者在你已经安装了 WSL 和默认的 Ubuntu 发行版之后再添加其他发行版。</p><p data-vmark="a9de">此外，微软还包括一些额外的命令来帮助你管理 WSL 实例的备份。</p><p data-vmark="3fc9">你可以使用 wsl --update 来手动更新你的 WSL Linux 内核，你也可以使用 wsl --update rollback 来回滚到之前的 WSL Linux 内核版本。</p><p data-vmark="97fc">最后，你可以使用 wsl --status 查看关于 WSL 配置的一般信息，如默认发行版类型、默认发行版和内核版本。</p>
          
</div>
            