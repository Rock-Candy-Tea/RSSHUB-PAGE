
---
title: 'GNU Parted 3.5 发布，硬盘分区编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4988'
author: 开源中国
comments: false
date: Wed, 20 Apr 2022 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4988'
---

<div>   
<div class="content">
                                                                                            <p>GNU Parted 是一个硬盘分区编辑器，用于创建和删除分区。GParted 以及 KDE Partition Manager 皆为使用 GNU Parted 库的图形前端 。</p> 
<p>GNU Parted 3.5 正式发布，更新内容如下：</p> 
<h3>新功能</h3> 
<ul> 
 <li>在 -script 模式中增加 -fix，以自动修复备份 GPT header 不在磁盘末端等问题</li> 
 <li>在标记为 MSDOS 的磁盘上增加使用交换分区标志</li> 
 <li>在 script 模式下设置时，允许分区名称为空字符串</li> 
 <li>增加 -json 命令行开关，将磁盘的细节输出为 JSON</li> 
 <li>增加对使用 linux-home 标志的 Linux home GUID 的支持</li> 
</ul> 
<h3>错误修正</h3> 
<ul> 
 <li>减少了测试中使用的磁盘大小，使其更容易在存储较少的系统上运行测试套件</li> 
 <li>增加了对 aarch64 和 mips64 架构的支持</li> 
 <li>在机器输出中避免了冒号和反斜线，现在它们将被用反斜杠转义。</li> 
 <li>在设备处于 BUSY 状态时使用 libdevmapper 的 retry remove 选项。这可以防止 libdevmapper 在试图移除一个繁忙的分区时打印出混乱的输出。</li> 
 <li>在写入 GPT header 时保留 GUID 特定属性，之前它们被设置为 0</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.gnu.org%2Farchive%2Fhtml%2Finfo-gnu%2F2022-04%2Fmsg00010.html" target="_blank">https://lists.gnu.org/archive/html/info-gnu/2022-04/msg00010.html</a></p>
                                        </div>
                                      
</div>
            