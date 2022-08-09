
---
title: 'Rescuezilla 2.4 发布，系统救援型 Linux 发行'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4851'
author: 开源中国
comments: false
date: Tue, 09 Aug 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4851'
---

<div>   
<div class="content">
                                                                                            <p>Rescuezilla 是基于 Ubuntu 的专业 Linux 发行版，主要用于系统修复等救援工作。它有极其易于使用的图形环境，包括完整的系统备份、裸机恢复、分区编辑、取消删除文件、Web 浏览等功能。</p> 
<p>目前，Rescuezilla 2.4 发布了，该版本带来如下更改：</p> 
<ul> 
 <li>用基于 Ubuntu 22.04 (Jammy) 的构建替换 Ubuntu 21.10 (Impish) 构建，以获得对新硬件的最佳支持</li> 
 <li>从源代码构建最新版本的 partclone <code>v0.3.20</code>，而不是 OS 包（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frescuezilla%2Frescuezilla%2Fissues%2F168" target="_blank">#168</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frescuezilla%2Frescuezilla%2Fissues%2F309" target="_blank">#309</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frescuezilla%2Frescuezilla%2Fissues%2F335" target="_blank">#335</a>）</li> 
 <li>为压缩 BTRFS 文件系统（例如 Fedora Workstation 33 和更新版本）的用户修复了“不支持的功能”错误</li> 
 <li>删除了旧的 partclone v0.2.43，最大限度地提高旧版重做备份的兼容性</li> 
 <li>修复了 Clonezilla EFI NVRAM 脚本的执行，更好地正确处理 EFI 系统上的重启 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frescuezilla%2Frescuezilla%2Fissues%2F348" target="_blank">#348</a> )</li> 
 <li>将 Firefox 切换到使用 Mozilla Team PPA 存储库，因为新的打包与 Rescuezilla 的构建脚本不兼容</li> 
 <li>添加了使用 bzip2 算法压缩图像的功能 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frescuezilla%2Frescuezilla%2Fissues%2F290" target="_blank">#290</a> )</li> 
 <li>添加了设置自定义 SSH 端口的功能（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frescuezilla%2Frescuezilla%2Fissues%2F336" target="_blank">#336</a>）</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frescuezilla%2Frescuezilla%2Freleases%2Ftag%2F2.4" target="_blank">https://github.com/rescuezilla/rescuezilla/releases/tag/2.4</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            