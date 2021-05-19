
---
title: 'macFUSE 4.1.2 发布，通过第三方文件系统扩展 macOS'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7024'
author: 开源中国
comments: false
date: Wed, 19 May 2021 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7024'
---

<div>   
<div class="content">
                                                                    
                                                        <p>macFUSE 软件包为开发 macOS 10.12 至 macOS 11 的文件系统提供了多种 API。你可以使用所提供的 API 来开发许多类型的文件系统，其内容可以来自本地磁盘、网络、内存或任何其他来源。这些 API 是 FUSE API 的超集，它起源于 Linux。</p> 
<p>由于 FUSE 文件系统是普通的应用程序（而不是内核扩展），你在编程工具、调试器和库方面拥有和开发标准 macOS 应用程序一样的灵活性和选择。</p> 
<p>macFUSE 4.1.2 正式发布，自 4.1.0 以来的变化包括：</p> 
<ul> 
 <li>在更新器中添加原生 Apple Silicon 支持。</li> 
 <li>修复了挂载卷时的一个问题，在极少数情况下，该问题可能导致文件系统进程崩溃。DADiskCreateFromVolumePath() 可能会返回 NULL，所以我们需要确保防止在 NULL 上调用CFRelease()。</li> 
 <li>修复了使用 macFUSE.framework 时的 "框架 header 中包含双引号"的警告。</li> 
 <li>修复偏好面板中的竞赛条件（race condition），该条件可能导致偏好面板在检查可用更新时崩溃。</li> 
 <li>为偏好面板生成调试符号并将其添加到调试存档中。</li> 
 <li>增加了对在 Apple Silicon 上构建 macFUSE 的支持。</li> 
 <li>macFUSE 在 Apple Silicon Macs 上不再需要 Rosetta 2。将原生 Apple Silicon 支持添加到下载器和卸载程序。</li> 
 <li>放弃对 macOS 10.9、10.10 和 10.11 的支持。由于使用了 SHA-256 签名而非 SHA-1 签名，在 Apple Silicon Mac 上构建的安装程序包在 10.12 之前的 macOS 版本上无法使用。</li> 
 <li>修复 auto_cache 文件修改检测。在启用 auto_cache 的情况下，内核扩展会留意远程修改时间的变化。如果检测到一个远程修改，文件的缓存就会失效。我们需要确保在修改时间因本地写入而改变的情况下不使文件的缓存失效。</li> 
 <li>移除查找中的文件名长度检查。这改善了对非拉丁语的支持。文件名是以 NFD 形式传递的，因此可能比其 NFC 表示法长。NFC 表示不得超过 255 字节。</li> 
 <li>在安装程序插件中增加对黑暗模式的支持。</li> 
 <li>许可证已经改变。从 4.0.0 版本开始，未经特定的事先书面许可，不允许与商业软件捆绑在一起重新分发。这包括在商业软件背景下的自动下载或安装。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fosxfuse%2Fosxfuse%2Freleases" target="_blank">https://github.com/osxfuse/osxfuse/releases</a></p>
                                        </div>
                                      
</div>
            