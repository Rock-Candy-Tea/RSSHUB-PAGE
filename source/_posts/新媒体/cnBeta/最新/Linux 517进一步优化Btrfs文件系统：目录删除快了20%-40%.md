
---
title: 'Linux 5.17进一步优化Btrfs文件系统：目录删除快了20%-40%'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0111/675d901883cbfbb.webp'
author: cnBeta
comments: false
date: Tue, 11 Jan 2022 03:03:51 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0111/675d901883cbfbb.webp'
---

<div>   
随着 Btrfs 文件系统知名度的提升，这似乎有助于上游的热情和开发工作。<strong>在 Linux Kernel 5.17 版本中，已经为 Btrfs 准备了新一轮的性能优化。现在目录记录所需的元数据更少了，这意味着目录删除现在快了 20~40%。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0111/675d901883cbfbb.webp" alt="scb8j607.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Linux Kernel 5.17 的另一个重要胜利是，自由空间树条目（free space tree entries）现在也被索引并按大小搜索，这能让延迟减少 30%，搜索时间减少 30%。</p><p style="text-align: left;">对于那些在分区模式下使用Btrfs的人来说，分区信息现在在挂载过程中被缓存起来，以加快重复查询的速度，大约50%。另外，在插入钥匙时，树节点锁定代码的争论也减少了，而且不需要分割，在FS-Mark基准中产生了大约1~20%的改进。</p>   
</div>
            