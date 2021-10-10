
---
title: 'Win11 正式版预装 Linux 子系统，还可将图形应用添加到开始菜单'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202107/61056ae88e9f09462141182f_1024.jpg'
author: ZAKER
comments: false
date: Sat, 09 Oct 2021 16:52:22 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202107/61056ae88e9f09462141182f_1024.jpg'
---

<div>   
<p>IT 之家 10 月 10 日消息 微软此前在 Windows Insider Preview 构建版本中测试了 Windows 11 适用于 Linux 的子系统，安装您喜欢的 Linux 发行版就像从 Windows Terminal 直接键入 " wsl – install " 一样简单。</p><p>虽然 Windows 11 正式版中并没有带来大家期盼的 Android 子系统支持，但并不影响 Linux 子系统如期而至。这也给很多经常使用 Linux 应用的用户带来了方便。</p><p>默认情况下，该环境还支持图形和声音，这意味着你还可以轻松在 Windows 上安装图形 Linux 应用程序，然后与本机正常的 Windows 11 应用程序无缝并存运行。</p><p>IT 之家了解到，Windows 11 还支持将 Linux 应用程序的快捷方式添加到开始菜单，这意味着目前可用的 Linux 图形化程序与普通环境下的 PC 应用并无不同，您同样可以在 Windows 上流畅地运行。</p><p>此外， Windows 10 版本 2004 及以上版本的系统也同样支持这一功能，更多内容还需要大家自己去发现。</p><p>YouTuber @Scott Hanselman 为大家带来了一期视频，展示了多种 WSL 功能：</p><p><b>使用 wsl --install</b></p><p>微软表示，以前设置 WSL 的过程过于复杂，涉及到开启多个设置和安装多个软件包。该公司已将这一过程简化为只有一个命令。Windows 10 用户现在可以简单地用管理员权限打开一个命令提示符窗口，运行 wsl.exe --install。一旦你点击回车键，这个过程将自动启用 WSL 所需的可选功能，默认安装 Ubuntu 发行版，并在你的设备上安装最新的 WSL Linux 内核版本。当它完成后，重新启动你设备，发行版会在你再次启动后启动，完成安装。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202107/61056ae88e9f09462141182f_1024.jpg" data-height="395" data-width="924" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202107/61056ae88e9f09462141182f_1024.jpg" referrerpolicy="no-referrer"></div></div>此外，你可以通过在 PowerShell 或 Windows 命令提示符中输入 wsl --list --online 命令，找到可供安装的 Linux 发行版列表。要安装 Ubuntu 默认版本以外的发行版，使用这个命令：wsl --install -d <p></p><p>将 替换为之前列表命令中找到的 Linux 发行版的名称。这个安装命令可以用于第一次安装，或者在你已经安装了 WSL 和默认的 Ubuntu 发行版之后再添加其他发行版。</p><p>此外，微软还包括一些额外的命令来帮助你管理 WSL 实例的备份。</p><p>你可以使用 wsl --update 来手动更新你的 WSL Linux 内核，你也可以使用 wsl --update rollback 来回滚到之前的 WSL Linux 内核版本。</p><p>最后，你可以使用 wsl --status 查看关于 WSL 配置的一般信息，如默认发行版类型、默认发行版和内核版本。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            