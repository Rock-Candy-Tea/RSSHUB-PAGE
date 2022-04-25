
---
title: '报告：微软 Win11 默认预装应用约占 1.6GB 磁盘空间'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/4/b24fa361-f283-44e9-9625-df921fc5595c.png'
author: IT 之家
comments: false
date: Sun, 24 Apr 2022 23:32:41 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/4/b24fa361-f283-44e9-9625-df921fc5595c.png'
---

<div>   
<p data-vmark="021a"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 4 月 25 日消息，与许多操作系统一样，微软也在其 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Windows 11</a>、<a class="s_tag" href="https://win10.ithome.com/" target="_blank">Windows 10</a> 和其他产品中提供了一堆默认应用。Oofhours 的一份新报告就揭开了 <span class="accentTextColor">Windows 11 中的默认应用有多大</span>。</p><p data-vmark="f1bf">如下图所示，使用 PowerShell 提供的查询功能，我们能够计算出 Windows 11 默认应用的大小。这些应用已按大小（以字节为单位）降序排序，可以看到 <span class="accentTextColor">Microsoft Teams 是最大的应用</span>，占用了大约 91MB 的空间。</p><p data-vmark="2143" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/4/b24fa361-f283-44e9-9625-df921fc5595c.png" w="1440" h="811" title="报告：微软 Win11 默认预装应用约占 1.6GB 磁盘空间" width="1440" height="462" referrerpolicy="no-referrer"></p><p data-vmark="9a7c">然而，该查询只是指向了 XML 文件位置，而部分应用有另一个文件夹，<span class="accentTextColor">需要额外计算大小</span>。比如 Microsoft Store Purchase 显示大小为 11KB，但实际大小为 37MB。</p><p data-vmark="36af" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/4/8dd57c52-403e-4713-ac6d-72668dbedafa.png" w="1296" h="466" title="报告：微软 Win11 默认预装应用约占 1.6GB 磁盘空间" width="1296" height="295" referrerpolicy="no-referrer"></p><p data-vmark="df8e">对列出的每一个应用进行检查后发现，<span class="accentTextColor">Windows 11 的默认预装应用大小约为 1.6GB</span>，IT之家小伙伴觉得多不多？</p><p data-vmark="cf3b" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/4/b371258e-2321-4e0e-8356-6115d53d347a.png" w="788" h="200" title="报告：微软 Win11 默认预装应用约占 1.6GB 磁盘空间" width="788" height="200" referrerpolicy="no-referrer"></p><p data-vmark="bb4f">以下是在 PowerShell 中查看所有 Windows 应用大小的脚本，包括默认应用和从 Microsoft Store 下载的应用（需要先取消隐藏 WindowsApps 文件夹）：</p><pre>Get-AppxProvisionedPackage -online | % &#123;
# Get the main  package location using the manifest
$loc = Split-Path ( [Environment]::ExpandEnvironmentVariables($_.InstallLocation) ) -Parent
If ((Split-Path $loc -Leaf) -ieq 'AppxMetadata') &#123;
$loc = Split-Path $loc -Parent
&#125;
# Get a pattern for finding related folders
$matching = Join-Path -Path (Split-Path $loc -Parent) -ChildPath "$($_.DisplayName)*"
$size = (Get-ChildItem $matching -Recurse -ErrorAction Ignore | Measure-Object -Property Length -Sum).Sum
# Add the results to the output
$_ | Add-Member -NotePropertyName Size -NotePropertyValue $size
$_ | Add-Member -NotePropertyName InstallFolder -NotePropertyValue $loc
$_
&#125; | Select DisplayName, PackageName, Version, InstallFolder, Size</pre>
          
</div>
            