
---
title: '报告：微软 Win11 默认预装应用约占 1.6GB 磁盘空间'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202204/6265e2f58e9f09577c666beb_1024.jpg'
author: ZAKER
comments: false
date: Sun, 24 Apr 2022 18:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202204/6265e2f58e9f09577c666beb_1024.jpg'
---

<div>   
<p>IT 之家 4 月 25 日消息，与许多操作系统一样，微软也在其 Windows 11、Windows 10 和其他产品中提供了一堆默认应用。Oofhours 的一份新报告就揭开了 Windows 11 中的默认应用有多大。</p><p>如下图所示，使用 PowerShell 提供的查询功能，我们能够计算出 Windows 11 默认应用的大小。这些应用已按大小（以字节为单位）降序排序，可以看到 Microsoft Teams 是最大的应用，占用了大约 91MB 的空间。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202204/6265e2f58e9f09577c666beb_1024.jpg" data-height="811" data-width="1440" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202204/6265e2f58e9f09577c666beb_1024.jpg" referrerpolicy="no-referrer"></div></div>然而，该查询只是指向了 XML 文件位置，而部分应用有另一个文件夹，需要额外计算大小。比如 Microsoft Store Purchase 显示大小为 11KB，但实际大小为 37MB。<p></p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres1.myzaker.com/202204/6265e2f58e9f09577c666bec_1024.jpg" data-height="466" data-width="1296" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202204/6265e2f58e9f09577c666bec_1024.jpg" referrerpolicy="no-referrer"></div></div>对列出的每一个应用进行检查后发现，Windows 11 的默认预装应用大小约为 1.6GB，IT 之家小伙伴觉得多不多？<p></p><p></p><div class="img_box" id="id_imagebox_2" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_2" data-original="http://zkres1.myzaker.com/202204/6265e2f58e9f09577c666bed_1024.jpg" data-height="200" data-width="788" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202204/6265e2f58e9f09577c666bed_1024.jpg" referrerpolicy="no-referrer"></div></div>以下是在 PowerShell 中查看所有 Windows 应用大小的脚本，包括默认应用和从 Microsoft Store 下载的应用（需要先取消隐藏 WindowsApps 文件夹）：<p></p><p>Get-AppxProvisionedPackage -online | % &#123; # Get the main package location using the manifest $loc = Split-Path ( [ Environment ] ::ExpandEnvironmentVariables ( $_.InstallLocation ) ) -Parent If ( ( Split-Path $loc -Leaf ) -ieq 'AppxMetadata' ) &#123; $loc = Split-Path $loc -Parent &#125; # Get a pattern for finding related folders $matching = Join-Path -Path ( Split-Path $loc -Parent ) -ChildPath "$ ( $_.DisplayName ) *" $size = ( Get-ChildItem $matching -Recurse -ErrorAction Ignore | Measure-Object -Property Length -Sum ) .Sum # Add the results to the output $_ | Add-Member -NotePropertyName Size -NotePropertyValue $size $_ | Add-Member -NotePropertyName InstallFolder -NotePropertyValue $loc $_ &#125; | Select DisplayName, PackageName, Version, InstallFolder, Size</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            