
---
title: 'OpenZFS 2.1.0-rc2 发布，进行了一些 bug 修复'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4619'
author: 开源中国
comments: false
date: Fri, 09 Apr 2021 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4619'
---

<div>   
<div class="content">
                                                                                            <p>OpenZFS 2.1.0-rc2 现已发布。OpenZFS（原名 ZFS）是 Linux、FreeBSD 与 macOS 平台上的文件系统。该版本主要更新内容如下：</p> 
<p><strong>Supported Platforms</strong></p> 
<ul> 
 <li><strong>Linux</strong>： 与 3.10-5.11 内核兼容</li> 
 <li><strong>FreeBSD</strong>：Release 12.2、stable/12、13.0 (HEAD)</li> 
</ul> 
<p><strong>Changes</strong></p> 
<ul> 
 <li>修复 kmod-preamble 中 misplaced quotes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11851" target="_blank">＃11851</a></li> 
 <li>由于版本升级，早期的软件包已经过时 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fissues%2F11844" target="_blank">＃11844 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11847" target="_blank">＃11847</a></li> 
 <li>i-t：修复  root=zfs:AUTO <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fissues%2F11278" target="_blank">＃11278 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11838" target="_blank">＃11838</a></li> 
 <li>如果“clones”属性为空，则 zfs get -p 仅输出 3 列<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11837" target="_blank">＃11837</a></li> 
 <li>zpool-features.5：删除“booting not possible with this feature” <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11842" target="_blank">＃11842</a></li> 
 <li>man：修复错误的 .Xr 宏用法<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11845" target="_blank">＃11845</a></li> 
 <li>libzutil：zfs_isnumber(): 如果输入为空，则返回 false <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fissues%2F11841" target="_blank">＃11841 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11843" target="_blank">＃11843</a></li> 
 <li>ZTS：pool_checkpoint 改进<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11832" target="_blank">＃</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11832" target="_blank">11832</a></li> 
 <li>修复各种错字<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11774" target="_blank">＃11774</a></li> 
 <li>bash_completion.d：始终直接调用zfs/zpool二进制文件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11828" target="_blank">＃11828</a></li> 
 <li>添加 RELEASES.md 文件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11821" target="_blank">＃11821</a></li> 
 <li>......</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Freleases%2Ftag%2Fzfs-2.1.0-rc2" target="_blank">https://github.com/openzfs/zfs/releases/tag/zfs-2.1.0-rc2</a></p>
                                        </div>
                                      
</div>
            