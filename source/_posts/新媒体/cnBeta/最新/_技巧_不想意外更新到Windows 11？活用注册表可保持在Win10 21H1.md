
---
title: '_技巧_不想意外更新到Windows 11？活用注册表可保持在Win10 21H1'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1108/e32c8625f7eb51e.png'
author: cnBeta
comments: false
date: Mon, 08 Nov 2021 01:27:04 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1108/e32c8625f7eb51e.png'
---

<div>   
尽管与 Windows 10 21H1 相比，21H2 版本的 Windows 11 操作系统已在功能和体验上做出了重大改进 —— 比如全新的“开始”菜单和可运行 Android 应用程序的能力 —— 还是有不少用户希望暂时停留于相对兼容、稳定、习惯的旧系统生态之中。<strong>如果你不想某天开机时意外迎来自动升级到 Windows 11 操作系统的惊喜，那不妨参考下 News Block 分享的这一方法。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1108/e32c8625f7eb51e.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1108/e32c8625f7eb51e.png" referrerpolicy="no-referrer"></a></p><p>据悉，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>将很快开始向硬件符合升级条件的 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 用户推送系统更新，但鉴于 Windows 7 / 8.x 的诱骗式更新黑历史，这次还是有不少老用户担心自己意外中招。</p><p>MSPU 指出，微软早在 Windows 1803 中就引入了一个新的“目标发布版本”（TargetReleaseVersion）规范，允许用户设置期望的 OS 更新、或保持在哪一个 Windows 10 版本。</p><p><a href="https://static.cnbetacdn.com/article/2021/1108/f886870854c15b3.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1108/f886870854c15b3.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">操作有风险，责任需自负，请注意做好备份。</p><p><strong>基于此，我们也可利用它来实施一些注册表编辑，方法如下：</strong></p><blockquote><p>（1）在管理员账户权限下，使用 WinKey + R 组合键，运行 regedit 以打开注册表编辑器。</p><p>（2）找到 计算机 -> HKEY_LOCAL_MACHINE -> Software -> Policies -> Microsoft -> Windows -> WindowsUpdate 路径。</p><p>（3）创建一个名为 TargetReleaseVersion 的新 DWORD（32 位）值，并赋值为 1 。</p><p>（4）创建另一个名为 TargetReleaseVersionInfo 的 DWORD（32 位）值，并赋值为 21H1 。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2021/1108/6be8a6776e580e1.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1108/6be8a6776e580e1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">非管理员请慎重操作</p><p><strong>对于 Windows 10 专业版操作系统的用户，也可通过组策略编辑器（gpedit.msc）实施相同的操作：</strong></p><blockquote><p>● 转至《本地计算机 策略》下的《计算机配置》。</p><p>● 选择 管理模板 → Windows 组件 → Windows 更新 → 管理从 Windows 更新提供的更新。</p><p>● 双击 选择目标功能更新版本，输入 21H1 并点击确定，然后重新启动计算机。</p></blockquote><p>通过上述措施，Windows 10 会在当前版本服务终止 60 天后，自动将 PC 更新至指定的系统版本。</p><p>虽然距离服务终止还有数年的时间，但我们相信，届时微软已将 Windows 11 打磨得更加完善。</p>   
</div>
            