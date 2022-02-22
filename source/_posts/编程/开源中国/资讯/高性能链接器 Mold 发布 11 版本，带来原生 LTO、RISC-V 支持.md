
---
title: '高性能链接器 Mold 发布 1.1 版本，带来原生 LTO、RISC-V 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2841'
author: 开源中国
comments: false
date: Tue, 22 Feb 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2841'
---

<div>   
<div class="content">
                                                                                            <p>Mold 是一种高性能的现代链接器，旨在与 GNU 的 Gold 和 LLVM 的 LLD 竞争。该项目由最初从事 LLVM LLD 工作的 Rui Ueyama 发起，并一直积极致力于性能优化。目前 <a href="https://www.oschina.net/news/176194/gcc-add-mold-linker"><strong>GCC 12 已添加对 Mold 链接器的支持</strong></a><strong>。</strong></p> 
<p>Mold 发布了 1.1 版本，该版本提供本机链接时间优化 (LTO) 支持。LTO 支持通过类似于 GNU ld 和 GNU gold 的链接器插件接口实现。目前 Mold 的 LTO 支持侧重于完整性而不是性能，但这意味着它仅比 LTO 构建的其他链接器快“稍微快一点”。</p> 
<p>该版本另一大新增功能是添加了 RISC-V CPU 架构支持，其中 RV64 代码已被合并，且已成功测试 RISC-V 64 位上的各种程序。</p> 
<p>该版本还包含其他特性和修复项，有关 Mold 1.1 的更多详细信息，请参阅 GitHub 上的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Freleases%2Ftag%2Fv1.1" target="_blank">发行公告</a>。</p>
                                        </div>
                                      
</div>
            