
---
title: 'Linux Kernel 5.19将优化exFAT、EXT4 和 XFS 文件系统'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png'
author: cnBeta
comments: false
date: Thu, 26 May 2022 07:36:35 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png'
---

<div>   
<strong>除了针对 Btrfs 文件系统更新之外，正在开发中的 Linux Kernel 5.19 对 exFAT、EXT4 和 XFS 文件系统也有优化。</strong>在合并窗口期内，Linux 团队明确将修复 EXT4、exFAT 和 EROFS 文件系统的多处错误，并添加一些有趣的功能。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">其中针对 exFAT 文件系统的更新主要有 2 个。其一是 Sony 工程师在通过减少块请求的数量来处理对集群进行归零时贡献了大约 73% 的性能提升。这对 exFAT 来说是一个很大的改进。</p><p style="text-align: left;">而针对 exFAT 的另一项改进是新的“sys_tz”挂载选项。这是为了在处理被视为当前本地时间的 UTC 偏移量的 exFAT 时间戳时使用系统时区作为时间偏移量。</p><p style="text-align: left;">接下来是一些 Android 设备使用的、最初由<a data-link="1" href="https://c.duomai.com/track.php?k=WP0ZSPklWdlZyN4MTPklWYmYDO5IDNy0DZp9VZ0l2cmYiRyUSbvNmLsxWYtZnL3d3dGJTJGJTJBNTJzBHd0h" target="_blank">华为</a>开发的只读 Linux 文件系统的 EROFS 更新。 Linux 5.19 对 EROFS 的重大更改是使用 FSCACHE/CacheFiles 基础架构对 EROFS 进行按需加载。这引入了新的基于文件的后端和其他改进。有关所有详细信息，请参阅前面链接的 Git 合并。</p><p style="text-align: left;">除了 EROFS 现在支持 FSCACHE 上的按需加载支持之外，Linux 5.19 现在还支持 IDMAPPED 挂载、支持 NFS 导出和各种修复。</p><p style="text-align: left;">EXT4 更新侧重于各种错误修复和清理。错误修复包括通过不同的模糊器和错误注入工具找到的项目。总体而言，这个广泛使用的 Linux 文件系统的周期相对较轻。</p>   
</div>
            