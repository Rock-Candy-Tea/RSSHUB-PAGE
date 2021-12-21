
---
title: 'helloSystem 0.7.0 发布，旨在成为 BSD 中的 macOS'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-41274f602eb57fe33c582b88f31f0666d8a.png'
author: 开源中国
comments: false
date: Tue, 21 Dec 2021 08:07:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-41274f602eb57fe33c582b88f31f0666d8a.png'
---

<div>   
<div class="content">
                                                                                            <p>helloSystem 最新版本 0.7.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FhelloSystem%2FISO%2Freleases%2Ftag%2Fr0.7.0" target="_blank">已发布</a>，新版本主要变化是升级底层系统、优化启动时间、初步支持 exFAT 文件系统、完全重写 live 系统的架构。</p> 
<ul> 
 <li>底层系统从 FreeBSD 12 升级到 FreeBSD 13.0-RELEASE</li> 
 <li>完全重写的 live 系统架构 
  <ul> 
   <li>live 系统的启动时间提高了 3 倍</li> 
   <li>ISO 文件大小已减少到 800 MB 以下（适合 CD-ROM）</li> 
   <li>不再将整个文件系统复制到 RAM</li> 
   <li>不再需要初始 ramdisk，不再需要重新 root</li> 
   <li>在 live 系统中使用 uzip 压缩 ufs 文件系统镜像，而不是 zfs</li> 
   <li>在引导过程的早期可启动图形桌面</li> 
  </ul> </li> 
 <li>helloSystem 现在与 Ventoy 兼容，这意味着它可以从使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fventoy" target="_blank">Ventoy</a> 与磁盘上其他 ISO 文件一起存储的 ISO 文件启动</li> 
 <li>开发者文件（包括编译器、头文件、目标代码文件、开发人员文档等）现在可以单独下载</li> 
 <li>通过提供多版本的 NVIDIA 驱动程序提升与旧版 NVIDIA 显卡的兼容性</li> 
 <li>初步支持 exFAT 文件系统</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-41274f602eb57fe33c582b88f31f0666d8a.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FhelloSystem%2FISO%2Freleases%2Ftag%2Fr0.7.0" target="_blank">详情查看 release note</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">helloSystem 是热度颇高的 BSD 桌面发行版之一，它提供了精良的桌面体验，希望成为 BSD 中的 macOS。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">helloSystem 项目具有与 macOS 相似的设计目标，即“能够正常工作”，不需要太多配置就可以带来良好的开箱即用的桌面体验。helloSystem 基于 FreeBSD，除了设计理念，helloSystem 桌面环境也已被配置为看起来像早期 MacOS X 的桌面。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-dfbc41a41b6051eb5ffed69db628375a141.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">helloSystem 的开发人员不是要创建一个 macOS 的 1:1 副本，而是要与 macOS 的用户体验理念保持一致。因此 helloSystem 不能直接重新打包现有软件，为此他们还在开发更多专门用于 helloSystem 的桌面应用程序，其中许多应用程序都是用 PyQt 编写的。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-59e1f65b22a6ee9af06055a6bd9662eeec5.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            