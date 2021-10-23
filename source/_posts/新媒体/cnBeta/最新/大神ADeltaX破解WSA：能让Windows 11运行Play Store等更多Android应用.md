
---
title: '大神ADeltaX破解WSA：能让Windows 11运行Play Store等更多Android应用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1023/e19614a3bf05853.jpg'
author: cnBeta
comments: false
date: Sat, 23 Oct 2021 00:59:39 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1023/e19614a3bf05853.jpg'
---

<div>   
最新发布的 Windows 11 预览版中，微软开放了 Windows SubSystem for Android（WSA）子模块。通过安装亚马逊的 AppStore，目前能够在 Windows 11 系统上运行 Kindle 在内的 50 款应用和游戏。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1023/e19614a3bf05853.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1023/e19614a3bf05853.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1023/689653ea56368ce.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1023/689653ea56368ce.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">虽然用户还可以通过侧载的方式运行任意 Android 应用程序，但由于缺乏 Google Play Services，因此多款应用程序实际上是不兼容 WSA 的。不过 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 破解大神 ADeltaX 解决了这个问题，能安装包括 Play Store 在内的很多应用。</p><p style="text-align: left;">他在 <a href="https://github.com/ADeltaX/WSAGAScript" target="_blank">GitHub </a>上分享了所有必要的文件和说明，但是需要一定的动手能力，而且整个操作也比较复杂。步骤如下：</p><blockquote style="text-align: left;"><p style="text-align: left;">1. 下载 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">MSI</a>XBUNDLE (使用商店rg-adguard下载msixbundle，软件包id：9P3395VX91NR)</p><p style="text-align: left;">2. 安装 WSL2（Ubuntu 或者 Debian，或者其他任何支持的 Linux 发行版本）</p><p style="text-align: left;">3. 安装 unzip lzip</p><p style="text-align: left;">4. 从 OPENGAPPS（x86_64, 11, PICO）中下载 GAPPS PICO</p><p style="text-align: left;">5. 提取 MSIXBUNDLE，提取 msix（你的版本）到一个文件夹，删除（appxmet<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://adata.jd.com/" target="_blank">ADATA</a>，appxblockmap，appxsignature，[content_types]）</p><p style="text-align: left;">6. 复制镜像（system.img, system_ext.img, product.img, vendor.img）到 #images</p><p style="text-align: left;">7. 复制 GAPPS PICO 压缩包到 #GAPPS</p><p style="text-align: left;">8. 编辑 VARIABLES.sh 并设置 ROOT 文件夹</p><p style="text-align: left;">9. 执行 extract_gapps_pico.sh、extend_and_mount_images.sh、apply.sh、unmount_images.sh</p><p style="text-align: left;">10. 从 #images 文件夹复制镜像到你提取的 msix 文件夹中</p><p style="text-align: left;">11. 以管理员身份打开 POWERSHELL（非核心），执行 Add-AppxPackage -Register PATH_TO_EXTRACTED_MSIX\AppxManifest.xml。</p><p style="text-align: left;">12. 用 gapps 运行 wsa</p></blockquote><p style="text-align: left;">登录问题的解决方法：</p><blockquote style="text-align: left;"><p style="text-align: left;">1. 使用 su 命令打开 ADB Shell ROOT</p><p style="text-align: left;">2. 将（内核文件）从（misc 文件夹）复制到（Tools 文件夹）中的 MSIX 文件中。</p><p style="text-align: left;">3. 现在你可以在 ADB SHELL 中使用 su，进入 ADB SHELL，输入 su，然后输入 setenforce 0，你现在可以登录了。</p></blockquote><p style="text-align: left;">然而，ADeltaX 承诺将很快重写这些指令，使其更容易安装。</p>   
</div>
            