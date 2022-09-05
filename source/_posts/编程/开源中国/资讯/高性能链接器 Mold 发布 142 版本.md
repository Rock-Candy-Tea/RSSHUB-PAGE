
---
title: '高性能链接器 Mold 发布 1.4.2 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4170'
author: 开源中国
comments: false
date: Mon, 05 Sep 2022 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4170'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">Mold 是现有 Unix 链接器的快速替代品，它比 LLVM lld 链接器快几倍。</p> 
<p style="margin-left:0px">目前 Mold 发布了最新版本 1.4.2 ，此版本带来以下<span style="color:#24292f">新功能和各种错误修复：</span></p> 
<h2 style="margin-left:0px"><strong>新功能和错误修复</strong></h2> 
<ul> 
 <li>[RV32] 修复了 32 位 RISC-V 的几个问题。Mold 现在可以为目标构建复杂的程序，包括它自己。</li> 
 <li>[ARM32] Mold 获得了范围扩展 thunk，因此它可以链接 .text 大于 16 MiB 的程序。以前 Mold 无法链接这么大的程序。</li> 
 <li>还修复了 ARM32 的稳定性问题。</li> 
</ul> 
<p>创建 Mold 二进制包请注意：请静态链接捆绑的 libtbb（这是默认设置）或使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foneapi-src%2FoneTBB%2Fpull%2F824" target="_blank">补丁</a>重建发行版的 libtbb 包，以便 Mold 的链接时间优化（LTO）在重负荷下可靠地工作。</p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Freleases%2Ftag%2Fv1.4.2" target="_blank">https://github.com/rui314/mold/releases/tag/v1.4.2</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            