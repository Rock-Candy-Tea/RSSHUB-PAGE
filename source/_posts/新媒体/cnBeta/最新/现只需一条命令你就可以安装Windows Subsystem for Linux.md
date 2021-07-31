
---
title: '现只需一条命令你就可以安装Windows Subsystem for Linux'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0731/1b7ff9c7349a8d0.jpg'
author: cnBeta
comments: false
date: Sat, 31 Jul 2021 02:11:49 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0731/1b7ff9c7349a8d0.jpg'
---

<div>   
今天，微软宣布 Windows 10 Version 2004 及更高版本，均可以通过“<strong>wsl.exe --install</strong>”命令来安装 WSL 所需内容。微软表示，之前设置 WSL 的过程过于复杂，涉及打开多个设计和安装多个包。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0731/1b7ff9c7349a8d0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0731/1b7ff9c7349a8d0.jpg" alt="n402f0kf.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">现在，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>已经将该流程简化为一个命令，<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 用户现在可以简单地打开具有管理员权限的命令提示符窗口并运行 wsl.exe --install。在敲击回车键之后，后台将会执行启用所需的 WSL 可选功能，默认安装 Ubuntu 发行版本，并将最新的 WSL Linux 内核版本安装到您的机器上。完成并重新启动机器后，您的分发将在您再次启动后启动，完成安装。</p><p style="text-align: left;">此外，您可以通过在 PowerShell 或 Windows 命令提示符中输入命令 <strong>wsl --list --online</strong> 来找到可供安装的 Linux 发行版列表。要安装除 Ubuntu 默认值之外的发行版，请使用以下命令：<strong> wsl --install -d < DistroName ></strong></p><p style="text-align: left;">将 <strong>< DistroName ></strong> 替换为在上一个 list 命令中找到的 Linux 发行版的名称。此安装命令可用于首次安装或在您已经使用默认 Ubuntu 发行版安装 WSL 后添加其他发行版。</p><p style="text-align: left;">Microsoft 还包含一些额外的命令来帮助您使用此向后移植管理 WSL 实例。您可以使用 <strong>wsl --update</strong> 手动更新 WSL Linux 内核，也可以使用<strong> wsl --update rollback</strong> 回滚到以前的 WSL Linux 内核版本。</p><p style="text-align: left;">最后，您可以使用 <strong>wsl --status</strong> 查看有关 WSL 配置的一般信息，例如默认发行版类型、默认发行版和内核版本。此更新是 KB5004296 的一部分，您可以在此处找到有关如何确保安装它及其更改的完整说明。</p>   
</div>
            