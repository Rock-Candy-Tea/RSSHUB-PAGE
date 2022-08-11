
---
title: '龙芯中科在LibreOffice中增加了对LoongArch架构的支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0811/20ef6b9c7c9b8ad.webp'
author: cnBeta
comments: false
date: Thu, 11 Aug 2022 11:18:58 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0811/20ef6b9c7c9b8ad.webp'
---

<div>   
继今年早些时候GCC 12引入LoongArch支持，Linux 5.19添加了最初的LoongArch端口，以及Glibc
2.36添加了LoongArch支持之后，LibreOffice作为具有较高知名度的开源项目，也添加了对龙芯这种中国处理器ISA的支持，该处理器的架构最初源自MIPS64。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0811/20ef6b9c7c9b8ad.webp" title alt="image.webp" referrerpolicy="no-referrer"></p><p>Loongson作为LoongArch指令集架构背后的公司，为在LoongArch 64位硬件上运行Libre<a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a>开源办公套件提供了本地支持。</p><p>将LoongArch支持添加到LibreOffice开源办公套件需要1630行新的代码，包括从构建系统到数百行新的C++代码的变化。目前这个LoongArch LibreOffice只支持在Linux上构建。</p><p>Loongson的3A5000是龙芯中科的第一款LoongArch 64位CPU，虽然暂时性能还算不上突出，但未来几代的LoongArch处理器和拥有成熟的软件堆栈值得期待，应用支持的完善能否使这种基于RISC的处理器架构对Arm、x86_64和RISC-V体系显现出竞争力，这将是很有趣的。</p><p>那些对LibreOffice的LoongArch支持感到好奇的人可以通过今天早上合并到主线的这个Git提交来找到它：</p><p><a href="https://cgit.freedesktop.org/libreoffice/core/commit/?id=d3625d968901eb93a9680db8d1165f70de3fd64e&utm_source=anzwix" _src="https://cgit.freedesktop.org/libreoffice/core/commit/?id=d3625d968901eb93a9680db8d1165f70de3fd64e&utm_source=anzwix" target="_blank">https://cgit.freedesktop.org/libreoffice/core/commit/?id=d3625d968901eb93a9680db8d1165f70de3fd64e&utm_source=anzwix</a><br></p>   
</div>
            