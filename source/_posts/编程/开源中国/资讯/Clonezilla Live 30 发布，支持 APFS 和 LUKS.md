
---
title: 'Clonezilla Live 3.0 发布，支持 APFS 和 LUKS'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7456'
author: 开源中国
comments: false
date: Sat, 28 May 2022 07:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7456'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Clonezilla Live 是一个小型的可启动 GNU/Linux 发行版，适用于基于 x86/amd64 的计算机。Clonezilla Live 可以使用 CD/DVD 或 USB 闪存对单个计算机进行镜像或克隆。Clonezilla Live 的主要优势是不需要提前设置 DRBL 服务器，也不需要被部署的计算机从网络上启动。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Clonezilla Live 3.0 更新内容包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>底层的 GNU/Linux 操作系统进行了升级。该版本基于 Debian Sid 仓库（截至 2022 年 5 月 22 日）</li> 
 <li>Linux 内核更新至 5.17.6-1</li> 
 <li>Partclone 更新到了 0.3.20</li> 
 <li>该版本现在支持 APFS（苹果文件系统）镜像/克隆</li> 
 <li>增加了对 LUKS 的支持</li> 
 <li>更新德语、法语、葡萄牙语、日语等语言文件</li> 
 <li>在 Live 系统中添加 wavemon、memtester、edac-utils、shc 和 uml-utilities。</li> 
 <li>从 Live 系统中移除 s3ql</li> 
 <li>实施了一个更好的机制来检查磁盘的 GPT/MBR 格式</li> 
 <li>在 uEFI 启动菜单中添加 memtester</li> 
 <li>启动参数<span> </span><code>use_os_prober="no"</code><span> </span>现在可以跳过运行<span> </span><code>os-prober</code></li> 
 <li>增加一个机制来跳过使用设备列表缓存。如果启动参数中的<span> </span><code>use_dev_list_cache=no</code>，那么就不会使用设备列表缓存机制</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fclonezilla.org%2F" target="_blank">https://clonezilla.org/</a></p>
                                        </div>
                                      
</div>
            