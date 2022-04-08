
---
title: 'Fedora计划放弃对非UEFI BIOS系统的支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0408/90fb066723c8a3d.jpg'
author: cnBeta
comments: false
date: Fri, 08 Apr 2022 13:07:44 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0408/90fb066723c8a3d.jpg'
---

<div>   
<strong>Fedora 37开发团队正在考虑放弃对非UEFI
BIOS的支持。统一可扩展固件接口(UEFI)是一种处理启动过程的现代方法。UEFI与传统Legacy BIOS的方式类似；但是，启动数据是被存储在一个.efi文件中，而不是固件中。</strong>就Fedora而言，虽然这种改变可能需要一些时间，但新的Fedora
x86_64安装将不再能在非UEFI平台上工作。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0408/90fb066723c8a3d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0408/90fb066723c8a3d.jpg" title alt="legacy-bios.jpg" referrerpolicy="no-referrer"></a></p><p>在x86_64架构上，Fedora 37将把传统BIOS安装标记为弃用，以支持UEFI。虽然已经使用 Legacy BIOS 启动的系统将继续得到支持，但在这些架构上安装新的 Legacy BIOS 将是无法做到的。</p><p>许多理想的功能需要UEFI，例如应用固件更新（fwupd）和支持SecureBoot。一个独立的改变减少了每个运行Fedora安装程序的用户的支持负担，因为现在每个平台只有一种方法可以做到这一点。</p><p>最重要的是，由于每个架构只需要一种启动方式，它简化了Fedora安装/实时媒体。</p><p>所以，这个想法并不是说取消BIOS支持可以直接改善UEFI。然而，使用老式BIOS会带来一系列古老而奇怪的约定，需要修改复杂的代码来维持与UEFI的功能一致。虽然许多操作都是现成的，但它们从整体上看仍然是必须维护的额外代码路径。</p><p>一个版本的标准定义了UEFI，它可以被测试和认证。另一方面，每个传统的BIOS都是独一无二的。因此，传统BIOS被广泛认为是过时的，即将被淘汰。</p><p>可维护性随着它的老化而下降，目前永久维护这两个堆栈的现状对从事这项工作的人来说不再可行。</p><p><strong>以下是UEFI相对于传统BIOS的优势总结：</strong></p><p><a href="https://static.cnbetacdn.com/article/2022/0408/397233b7f3fd8da.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0408/397233b7f3fd8da.png" title alt="图片.png" referrerpolicy="no-referrer"></a><br></p><p>因此，正如你所看到的，UEFI相对于传统BIOS的优势是相当显著的。</p><p>同时，很多人已经评论说，现在的世界上依然有不少活跃的计算机只支持BIOS而不支持UEFI。所以，当然，目前在x86_64上使用Legacy BIOS启动的Fedora系统将继续这样做。然而，在未来的Fedora版本中，Legacy BIOS支持将被完全移除。</p><p><strong>更多信息，我们推荐您参考Fedora官方公告：</strong></p><p><a href="https://fedoraproject.org/wiki/Changes/DeprecateLegacyBIOS" _src="https://fedoraproject.org/wiki/Changes/DeprecateLegacyBIOS" target="_blank">https://fedoraproject.org/wiki/Changes/DeprecateLegacyBIOS</a><br></p>   
</div>
            