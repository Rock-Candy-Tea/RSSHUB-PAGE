
---
title: '微软 Win11_Win10 一个命令安装 Windows Linux 子系统（WSL）'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/7/e0cc3cb1-b75b-4fe1-8e8c-bddd24611612.png'
author: IT 之家
comments: false
date: Sat, 31 Jul 2021 15:11:26 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/7/e0cc3cb1-b75b-4fe1-8e8c-bddd24611612.png'
---

<div>   
<p><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 7 月 31 日消息 外媒报道，在最新的 Windows Insider Preview 构建版本中，你只需运行 wsl.exe --install 就可以安装运行 WSL 所需的一切。</p><p>今天，微软宣布这一功能现在已经正式回传到 <a class="s_tag" href="https://win10.ithome.com/" target="_blank">Windows 10</a> 版本 2004 及以上版本的系统。</p><p><strong>使用 wsl --install</strong></p><p>微软表示，以前设置 WSL 的过程过于复杂，涉及到开启多个设置和安装多个软件包。该公司已将这一过程简化为只有一个命令。Windows 10 用户现在可以简单地用管理员权限打开一个命令提示符窗口，运行 wsl.exe --install。一旦你点击回车键，这个过程将自动启用 WSL 所需的可选功能，默认安装 Ubuntu 发行版，并在你的设备上安装最新的 WSL Linux 内核版本。当它完成后，重新启动你设备，发行版会在你再次启动后启动，完成安装。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/e0cc3cb1-b75b-4fe1-8e8c-bddd24611612.png" w="924" h="395" title="微软 Win11/Win10 一个命令安装 Windows Linux 子系统（WSL）" width="924" height="351" referrerpolicy="no-referrer"></p><p style="margin-top: 0px; max-width: calc(100% - 10px); white-space: normal;">此外，你可以通过在 PowerShell 或 Windows 命令提示符中输入 wsl --list --online 命令，找到可供安装的 Linux 发行版列表。要安装 Ubuntu 默认版本以外的发行版，使用这个命令：wsl --install -d <DistroName></p><p style="max-width: calc(100% - 10px); white-space: normal;">将 <DistroName> 替换为之前列表命令中找到的 Linux 发行版的名称。这个安装命令可以用于第一次安装，或者在你已经安装了 WSL 和默认的 Ubuntu 发行版之后再添加其他发行版。</p><p><strong>额外命令</strong></p><p>IT之家获悉，微软还包括一些额外的命令来帮助你管理 WSL 实例的备份。</p><p>你可以使用 wsl --update 来手动更新你的 WSL Linux 内核，你也可以使用 wsl --update rollback 来回滚到之前的 WSL Linux 内核版本。</p><p>最后，你可以使用 wsl --status 查看关于 WSL 配置的一般信息，如默认发行版类型、默认发行版和内核版本。</p><p>更新你的 windows 10 版本以支持这些命令</p><p>你可以像平常一样通过更新 Windows 来获得这个后端。可以手动打开 Windows 设置，进入“更新和安全”，点击“检查更新”。</p><p>该更新是 KB5004296 的一部分，当你点击“检查更新”时，你可能会看到一个可用的可选更新，确保它的编号与 KB5004296 相同，安装它，你将获得 wsl --update 的权限。</p>
          
</div>
            