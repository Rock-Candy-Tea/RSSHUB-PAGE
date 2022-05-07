
---
title: 'Linux内核更新加入Rust语言支持 并开始提供网络和异步功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0507/cb3afa476cae928.jpg'
author: cnBeta
comments: false
date: Sat, 07 May 2022 10:27:52 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0507/cb3afa476cae928.jpg'
---

<div>   
在一个激动人心的周六早晨，Miguel Ojeda发布了最新的补丁系列，历史性地将Rust语言支持纳入Linux内核。"Rust for the
Linux
kernel"补丁现在已经到了第六个版本，它为这种第二种可选语言添加了必要的支撑，并继续添加更多的示例代码/基本功能，以展示这种注重内存安全的语言在内核中的应用。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0507/cb3afa476cae928.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>与此同时，Rust for Linux的努力仍在继续，许多开发者和组织有兴趣看到在内核中开始使用Rust代码的能力，特别是在容易出现内存安全问题的领域。在今天发布的v6补丁中，工具链支持已经针对Rust 1.60进行了更新，支持在内核中运行文档测试，以及其他Rust基础设施的改进。</p><p>说到Rust代码在内核中的使用，在这个补丁系列中可以看到网络支持的开始。net"模块支持Namespace、SkBuff、Ipv4Addr、SocketAddrV4、TcpListener等类型。还有"async"开始支持异步的内核编程。目前的状态已经在为允许异步TCP套接字代码工作。新的Rust代码还增加了对网络包过滤器和其他新功能的支持。</p><p>从这个Rust for Linux v6系列来看，Rust支持仍然被认为是"实验性的"，但表现已经足够好，如果需要的话，内核开发者可以开始为其他内核子系统开发Rust抽象，并将更多的驱动移植到Rust上。</p><p>更多关于Linux内核更新的Rust代码的细节，请看这个补丁系列：</p><p><a href="https://lore.kernel.org/lkml/20220507052451.12890-1-ojeda@kernel.org/" _src="https://lore.kernel.org/lkml/20220507052451.12890-1-ojeda@kernel.org/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="2a181a18181a1f1a1d1a1f181e1f1b041b1812131a071b0745404f4e4b6a414f58444f460445584d">[email protected]</span>/</a><br></p><p>目前Rust内核的努力达到了37.9万行代码，包括底层、到目前为止开始的子系统抽象、样本代码，以及将一些Android和GPIO驱动代码转换为Rust作为额外的例子。</p>   
</div>
            