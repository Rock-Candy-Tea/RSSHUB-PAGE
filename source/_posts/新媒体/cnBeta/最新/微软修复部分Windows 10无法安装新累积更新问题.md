
---
title: '微软修复部分Windows 10无法安装新累积更新问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0825/e9a5f91cec13f8a.jpg'
author: cnBeta
comments: false
date: Wed, 25 Aug 2021 00:03:26 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0825/e9a5f91cec13f8a.jpg'
---

<div>   
<strong>部分 Windows 10 用户自今年 5 月的补丁星期二活动日开始，就一直无法安装最新的 Windows 10 累积更新，升级过程中会遇到“PSFX_E_MATCHING_BINARY_MISSING”。</strong>这个问题是安装了 2021 年 5 月 25 日（KB5003214）和 2021 年 6 月 21 日（KB5003690）累积更新之后开始的。<br>
 <p>微软目前已经承认了这个问题，并表示：“这个问题发生在已经被自动清扫以删除过时的资源记录的设备上。当一个系统被清扫时，最近安装的最新累积更新（LCU）被标记为永久性的，旧的组件被从系统中删除。在清扫完成后，设备处于这种状态，你不能卸载KB5003214或KB5003690，也不能安装未来的LCU（最新的累积更新）”。</p><p style="text-align: left;">现在，微软发布了“<a href="https://support.microsoft.com/en-us/topic/kb5005322-some-devices-cannot-install-new-updates-after-installing-kb5003214-may-25-2021-and-kb5003690-june-21-2021-66edf7cf-5d3c-401f-bd32-49865343144f" target="_blank">KB5005932 </a><a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Setup Update”，通过配置注册表设置来手动执行升级。微软表示：“这一兼容性修复能够在无法完成最新累积更新（LCU）安装的设备上运行”。一旦更新被安装，Windows 用户可以通过使用以下说明创建一个特殊的注册表键来启动原地升级。</p><p style="text-align: left;">手动升级</p><blockquote style="text-align: left;"><p style="text-align: left;">1. 在搜索框中输入“cmd”或者“command prompt”，打开命令提示符</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0825/e9a5f91cec13f8a.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">2. 选择以管理员身份运行</p><p style="text-align: left;">3. 接下来，你将生成注册表键值，这是设备就地升级的目标所需的。 在命令提示符下，键入以下内容：</p><p style="text-align: left;">Reg.exe Add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion /v AllowInplaceUpgrade /t REG_DWORD /f /d 1</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0825/ac6546bd4e5213a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0825/ac6546bd4e5213a.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">4. 按回车键</p></blockquote><p style="text-align: left;">注意 一旦就地升级完成，这个注册表值将被删除。就地升级可能需要48小时才能提供给设备。一旦提供，设备将更新到当前机器上的操作系统的一个干净版本。它也会有最新的月度安全质量更新。就地升级后，设备将能够正常采取新的更新。</p>   
</div>
            