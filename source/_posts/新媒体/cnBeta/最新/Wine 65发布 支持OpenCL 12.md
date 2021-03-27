
---
title: 'Wine 6.5发布 支持OpenCL 1.2'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://oscimg.oschina.net/oscnet/up-26755e0c4625d44a834855da073bfafd86b.png'
author: cnBeta
comments: false
date: Fri, 26 Mar 2021 23:22:29 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-26755e0c4625d44a834855da073bfafd86b.png'
---

<div>   
Wine
6.5，这款在Linux和macOS下运行的Windows应用和游戏的兼容层现在已经开始执行双周一版本的开发节奏。<strong>今日发布的6.5版最值得注意的是其针对OpenCL
1.2的支持进行了更新。此前Wine的OpenCL库(DLL)代码还停留在OpenCL 1.0，而Zebediah
Figura则负责让它满足OpenCL 1.1以及1.2的规范要求。</strong><br>
 <p><a href="https://oscimg.oschina.net/oscnet/up-26755e0c4625d44a834855da073bfafd86b.png" target="_blank"><img src="https://oscimg.oschina.net/oscnet/up-26755e0c4625d44a834855da073bfafd86b.png" referrerpolicy="no-referrer"></a></p><p>- OpenCL支持更新到1.2版本。</p><p>- 在MSHTML中增加了对IE兼容模式的支持。</p><p>- 更多的无窗口RichEdit工作。</p><p>- 增加了一些WinRT库存根。</p><p>- 各种bug修复。</p><p>Wine 6.5有25个已知的bug修复，影响了Guild Wars 2、Quicken、IDA Pro、.NET应用程序以及其他各种游戏和应用程序。</p><p><strong>关于Wine 6.5的下载和更多细节，请访问WineHQ.org：</strong></p><p><a href="https://www.winehq.org//announce/6.5" _src="https://www.winehq.org//announce/6.5" target="_blank">https://www.winehq.org//announce/6.5</a></p><p><strong>详细更新列表：</strong></p><p><strong>Bugs fixed in 6.5 (total 25):</strong></p><p>33375  Cannot test dlls with dashes in their name</p><p>34906  Multiple applications crash when trying to render in system memory (Zoo Tycoon, TOCA Touring Car Championship, The Sims, Conquest: Frontier Wars)</p><p>37488  Quicken 2014 reports error 0x0000054f on startup (NtAreMappedFilesTheSame fails to compare in-memory loader view of builtin dlls with mapped disk image)</p><p>37983  Jedi Knight: Dark Forces II, Outlaws (GOG.com versions) - music doesn't work</p><p>45032  WineTest does not run the vcomp tests</p><p>45567  League of Legends 8.12+ fails to start a game (anticheat engine, validation of WoW64 syscall dispatcher)</p><p>45685  Dragon NaturallySpeaking 12.5 does not run after training a new user</p><p>46817  Steam Big Picture needs d3d11_device_CreateDeviceContextState</p><p>47310  Canon TS3100 series full driver and software package refuses to install: "To install the software, you must be logged in to an administrator account."</p><p>50034  In font dialog's sample text, background changes color</p><p>50119  Dark Souls II: Scholar of the First Sin shows a white screen with vulkan renderer</p><p>50168  Error when running notepad.exe: Failed to start RpcSs service</p><p>50362  Fl Studio 20.8 crashes on startup</p><p>50411  Adobe Audition 2020 crashes on startup, reporting 'Direct2D Drawbot error' (d2d_geometry_group_GetBounds is a stub)</p><p>50721  IDA Pro 7.5: Lumina can't contact server, complains about Schannel security attributes</p><p>50738  Guild Wars 2 launcher can't login</p><p>50756  "Path is invalid." when using "SVN update" with SVN for <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>, which is used by TortoiseSVN</p><p>50783  WineTest declares dlls with dots in their name as missing</p><p>50790  No display found when using winemac.drv in a VM</p><p>50805  Win32_OperatingSystem class is missing 'ProductType' (affects Chocolatey)</p><p>50809  Multiple .NET 4.x application installers fail due to '<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">MSI</a>NetAssemblySupport' property returning incorrect version (IronPython 2.7.5)</p><p>50826  .NET applications fail to start with Wine-Mono: 'The file C:\windows\mono\mono-2.0\lib/mscorlib.dl</p>   
</div>
            