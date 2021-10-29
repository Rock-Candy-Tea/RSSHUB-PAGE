
---
title: '大神ADeltaX简化WSA破解步骤：在Windows 11上更容易安装Play Store'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1029/bb3fe247b32f10e.png'
author: cnBeta
comments: false
date: Fri, 29 Oct 2021 07:44:55 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1029/bb3fe247b32f10e.png'
---

<div>   
大约 1 周前，本站曾报道大神 ADeltaX 成功破解 Windows SubSystem For Android（WSA），使其能够安装 Play Store 应用商城和其他更多 Android 应用。<strong>不过整个破解过程需要一定的动手能力，现在该大神对部分操作进行了简化，并创建了 GitHub Actions 来定制 WSA。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1029/bb3fe247b32f10e.png" alt="QQ截图20211029154314.png" referrerpolicy="no-referrer"></p><p style="text-align: left;">新的操作步骤如下：</p><p style="text-align: left;">1. Fork 这个 repo</p><p style="text-align: left;">2. 进入 Action 标签，选择工作流 Magisk，点击运行按钮，输入所需信息（<a href="https://raw.githubusercontent.com/LSPosed/MagiskOnWSA/main/magisk.apk" target="_blank">Magisk apk下载链接</a>）</p><p style="text-align: left;">3. 等待 Action 完成并下载相关文件</p><p style="text-align: left;">4. 卸载 WSA</p><p style="text-align: left;">5. 在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 上启用开发者模式</p><p style="text-align: left;">6. 以管理员权限打开 PowerShell，在解压后的工件目录下运行 Add-AppxPackage -Register .\AppxManifest.xml。</p><p style="text-align: left;">7. 启动 WSA 并启用开发者模式，启动文件管理器，并等待文件管理器弹出。</p><p style="text-align: left;">8. 运行 adb connect localhost:58526 连接到 WSA，安装 Magisk 应用（你用来构建的那个）并启动它</p><p style="text-align: left;">9. 修复环境，因为 Magisk 应用程序会提示并重新启动</p><p style="text-align: left;">10.通过安装 Riru 和 LSPosed，完成</p>   
</div>
            