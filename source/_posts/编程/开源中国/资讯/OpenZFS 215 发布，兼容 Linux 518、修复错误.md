
---
title: 'OpenZFS 2.1.5 发布，兼容 Linux 5.18、修复错误'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6478'
author: 开源中国
comments: false
date: Tue, 28 Jun 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6478'
---

<div>   
<div class="content">
                                                                                            <p>OpenZFS 2.1.5 已发布，这是开源 ZFS 文件系统实现的最新版本，与现代 Linux 和 FreeBSD 系统兼容。</p> 
<p>新版本主要是修复错误，此外还包括面向 Linux 5.18 的兼容性更新，这意味着 OpenZFS 已官方支持最新的稳定版 Linux 内核，同时也保留对 Linux 3.10 的支持。</p> 
<p>OpenZFS 2.1.5 还包含针对 Linux 5.19 兼容性的补丁，不过这些补丁仍处于发布候选阶段，因此在下个月稳定发布之前仍可能出现破坏性变更。但无论如何，这至少说明 OpenZFS 已经开始测试下一个内核版本。</p> 
<p>至于 FreeBSD，目前兼容 FreeBSD 12.2-RELEASE 以及更新的版本。</p> 
<p>总结如下：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong>Linux：</strong>兼容 3.10 - 5.18 内核</li> 
 <li><strong>FreeBSD：</strong>兼容自 12.2-RELEASE 以来的系统</li> 
</ul> 
<p>OpenZFS 2.1.5 其他变化</p> 
<ul> 
 <li>优化 sorted scan memory accounting</li> 
 <li>针对 RHEL 的变更</li> 
 <li>在 FreeBSD 上实现对 hole-punching 的支持</li> 
 <li>删除 dracut 的 zfs-load-module.service 安装</li> 
 <li>……</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Freleases%2Ftag%2Fzfs-2.1.5" target="_blank">详情查看 release note</a>。</p> 
<p>延伸阅读</p> 
<ul> 
 <li><a href="https://www.oschina.net/news/170252/openzsf-3-0-plus-windows-work" target="_blank">OpenZFS 3.0 有望支持 macOS 和 DirectIO，继续优化 Window 版本</a></li> 
</ul>
                                        </div>
                                      
</div>
            