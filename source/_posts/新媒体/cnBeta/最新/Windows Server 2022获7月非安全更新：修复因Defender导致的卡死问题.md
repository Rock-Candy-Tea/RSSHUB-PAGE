
---
title: 'Windows Server 2022获7月非安全更新：修复因Defender导致的卡死问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0720/3b2ce4d3a771acd.webp'
author: cnBeta
comments: false
date: Wed, 20 Jul 2022 02:44:45 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0720/3b2ce4d3a771acd.webp'
---

<div>   
<strong>微软今天发布了适用于 Windows Server 2022 的 7 月累积更新 KB501579，在安装后版本号升至 Build 20348.859。</strong>该更新属于 C 类，也就是说是个非安全更新，主要对系统的细节进行优化。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0720/3b2ce4d3a771acd.webp" alt="p1yp1kfy.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">和最新的 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 Release Preview Build 19044.1862 (KB5015878) 不同，该 Windows Server 2022 更新提升了 input-output operations per second (IOPs)，修复了由于 Defender 导致 Windows 系统卡死的问题等。</p><p style="text-align: left;">完整更新日志如下</p><blockquote style="text-align: left;"><p style="text-align: left;">包括质量改进的非安全更新内容如下</p><p style="text-align: left;">非安全更新包括质量改进。主要变化包括：</p><p style="text-align: left;">● 提高了操作系统升级后一键重置的可靠性。</p><p style="text-align: left;">● 修复了在删除 EN-US 语言包时导致租户限制事件日志记录通道无法访问的问题。</p><p style="text-align: left;">● 更新 Remove-Item cmdlet 以正确与 Microsoft OneDrive 文件夹交互。</p><p style="text-align: left;">● 修复了阻止某些故障排除工具打开的问题。</p><p style="text-align: left;">● 修复了导致容器端口映射冲突的问题。</p><p style="text-align: left;">● 修复了导致代码完整性在文件被修改后继续信任文件的问题。</p><p style="text-align: left;">● 修复了在启用智能安全图功能的情况下启用 Windows Defender 应用程序控制时可能导致 Windows 停止工作的问题。</p><p style="text-align: left;">● 修复了当您使用远程桌面协议 (RDP) 和快速重新连接并禁用网络级身份验证 (NLA) 时更快地触发锁定策略的问题。当您使用空白密码调用 LogonUser() 时，会出现此问题。</p><p style="text-align: left;">● 提供为本地方案的 Azure 多重身份验证 (MFA) Active Directory 联合身份验证服务 (AD FS) 适配器配置备用登录 ID 的选项。您可以根据需要禁用备用登录 ID。若要将 Azure MFA ADFS 适配器配置为忽略备用登录 ID，请运行以下 PowerShell 命令：</p><p style="text-align: left;"> ★ Set-AdfsAzureMfaTenant -TenantId '' -ClientId '' -IgnoreAlternateLoginId $true。</p><p style="text-align: left;"> ★ 要在场中的每台服务器上重新启动 ADFS 服务，请使用 Restart-Service adfssrv PowerShell 命令。</p><p style="text-align: left;"> ★ 默认情况下，适配器配置不会忽略备用登录 ID (IgnoreAlternateLoginId = $false)，除非在上面的命令中明确设置为 $true。</p><p style="text-align: left;">● 减少在具有多个线程争用单个文件的高每秒输入/输出操作 (IOPS) 场景中的资源争用开销。</p><p style="text-align: left;">● 修复了阻止存储迁移服务 (SMS) 在具有许多共享的服务器上完成清单的问题。系统在 Microsoft-Windows-StorageMigrationService/Admin 通道中记录错误事件 2509 (ErrorId=-2146233088/ErrorMessage="Invalid table id")。</p><p style="text-align: left;">● 修复了导致 Windows 配置文件服务偶尔失败的问题。登录时可能会发生故障。错误消息是“gpsvc 服务登录失败。访问被拒绝”。</p></blockquote><p>下载：<a href="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/updt/2022/07/windows10.0-kb5015879-x64_d3d21b35480b32403c84cccc9ed0ede3c4009ccc.msu"><strong>Download KB5015879 MSU for Windows Server 2022 21H2 64-bit (x64) - 254.6 MB</strong></a></p>   
</div>
            