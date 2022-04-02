
---
title: 'Linux 5.18合并窗口期将整合两项重要exFAT增强功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1026/8dcb75b2f481229.jpg'
author: cnBeta
comments: false
date: Sat, 02 Apr 2022 00:13:26 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1026/8dcb75b2f481229.jpg'
---

<div>   
<strong>Linux 5.18 的合并窗口期将于本周末结束，在此之前微软的 exFAT 文件系统收到了 Pull Request 请求。</strong>本周期只有两个针对 exFAT 的补丁，但两个变化都很重要。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/thumb/article/2021/1026/8dcb75b2f481229.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1026/8dcb75b2f481229.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">首先，Linux 5.18+ 上的 exFAT 增加了一个选项，允许访问带有尾部点的路径。到目前为止，exFAT 驱动无条件地剔除了路径组件中的尾部句号，而在 Linux 5.18 中，这一做法被放宽了。</p><p style="text-align: left;">这个补丁增加了一个exFAT的"keep_last_dots"挂载选项，以控制是否剥离尾部的句子。这项工作的动机是发现 FUSE exFAT 驱动允许尾部的点，但 Linux 内核驱动不允许。更多细节见此补丁。</p><p style="text-align: left;">另一个针对 Linux 5.18 的补丁在回写时不再清除 VolumeDirty，这是避免缩短存储设备寿命的重要变化。在这次提交之前，如果没有启用'dirsync'或'sync'，VolumeDirty 会在回写时先被清除。如果在清除 VolumeDirty 后突然断电，但其他更新没有被写入，exFAT 文件系统将无法在下次挂载时检测到断电。</p><p style="text-align: left;">而在更新父目录时，VolumeDirty将再次被设置但不被清除。这意味着BootSector将在每次回写时至少被写入一次，这将缩短设备的寿命。</p>   
</div>
            