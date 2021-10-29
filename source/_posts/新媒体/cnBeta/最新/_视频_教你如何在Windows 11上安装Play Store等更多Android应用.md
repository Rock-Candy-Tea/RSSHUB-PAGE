
---
title: '_视频_教你如何在Windows 11上安装Play Store等更多Android应用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1029/5b55c4aa565740a.jpg'
author: cnBeta
comments: false
date: Fri, 29 Oct 2021 03:34:16 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1029/5b55c4aa565740a.jpg'
---

<div>   
在日前更新的 Windows 11 预览版中，微软终于开放了 Windows SubSystem for Android（WSA）模块的体验。不过现阶段 WSA 官方仅支持亚马逊 AppStore 的 50 多款应用程序，<strong>但在大神 ADeltaX 破解下已能成功运行 Play Store，并安装使用更多 Android 应用。</strong><br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1029/5b55c4aa565740a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1029/5b55c4aa565740a.jpg" alt="sfwf8gsp.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">一个学生在 YouTube 上分享了一个关于如何在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 机器上运行 Play Store 的视频。这个过程涉及到 Windows Subsystem for Linux、Ubuntu，以及运行 Github 托管的代码。</p><p style="text-align: left;">这需要大约半个小时。一旦你完成了，你就能在Windows 11上获得完整的Google Play商店体验。一旦你安装了Google Play，你就可以下载任何Android应用。</p><p><iframe src="//player.bilibili.com/player.html?aid=721212299&bvid=BV1RQ4y1i7G1&cid=429592005&page=1" scrolling="no" border="0" framespacing="0" allowfullscreen="true" width="750" height="480" frameborder="no"> </iframe></p><p style="text-align: left;">ADeltaX 在 <a href="https://github.com/ADeltaX/WSAGAScript" target="_blank">GitHub </a>上分享了所有必要的文件和说明，但是需要一定的动手能力，而且整个操作也比较复杂。步骤如下：</p><blockquote style="text-align: left;"><p style="text-align: left;">1. 下载 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">MSI</a>XBUNDLE (使用商店rg-adguard下载msixbundle，软件包id：9P3395VX91NR)</p><p style="text-align: left;">2. 安装 WSL2（Ubuntu 或者 Debian，或者其他任何支持的 Linux 发行版本）</p><p style="text-align: left;">3. 安装 unzip lzip</p><p style="text-align: left;">4. 从 OPENGAPPS（x86_64, 11, PICO）中下载 GAPPS PICO</p><p style="text-align: left;">5. 提取 MSIXBUNDLE，提取 msix（你的版本）到一个文件夹，删除（appxmet<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://adata.jd.com/" target="_blank">ADATA</a>，appxblockmap，appxsignature，[content_types]）</p><p style="text-align: left;">6. 复制镜像（system.img, system_ext.img, product.img, vendor.img）到 #images</p><p style="text-align: left;">7. 复制 GAPPS PICO 压缩包到 #GAPPS</p><p style="text-align: left;">8. 编辑 VARIABLES.sh 并设置 ROOT 文件夹</p><p style="text-align: left;">9. 执行 extract_gapps_pico.sh、extend_and_mount_images.sh、apply.sh、unmount_images.sh</p><p style="text-align: left;">10. 从 #images 文件夹复制镜像到你提取的 msix 文件夹中</p><p style="text-align: left;">11. 以管理员身份打开 POWERSHELL（非核心），执行 Add-AppxPackage -Register PATH_TO_EXTRACTED_MSIX\AppxManifest.xml。</p><p style="text-align: left;">12. 用 gapps 运行 wsa</p></blockquote>   
</div>
            