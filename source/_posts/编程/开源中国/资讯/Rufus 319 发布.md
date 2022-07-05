
---
title: 'Rufus 3.19 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5932'
author: 开源中国
comments: false
date: Tue, 05 Jul 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5932'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Rufus 是一个可以帮助格式化和创建可引导 USB 闪存盘的工具，它可以快速把 ISO 格式的系统镜像文件快速制作成可引导的 USB 启动安装盘，支持 Windows 或 Linux 启动。3.19 版本更新内容如下： </span></p> 
<ul> 
 <li>为 Windows 11 设置自定义添加新的选择对话框： 
  <ul> 
   <li>安全启动和 TPM 绕过现已移至此对话框</li> 
   <li>还允许绕过对 Windows 11 22H2 上的 Microsoft 帐户的强制要求<br> （注意：<strong>必须</strong>暂时禁用网络才能提议创建本地帐户）</li> 
   <li>还添加一个选项以跳过所有收集问题（将所有答案设置为“不允许”）</li> 
   <li>还添加了一个用于为 Windows To Go 设置内部驱动器脱机的选项</li> 
  </ul> <strong>注意：</strong>仅在使用 Windows 11 镜像时建议使用这些自定义选项。</li> 
 <li>添加对使用非标准 GRUB 2.0 前缀目录（openSUSE Live、GeckoLinux）的发行版的支持</li> 
 <li>添加忽略 USB 的功能（可参见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpbatard%2Frufus%2Fblob%2Fmaster%2Fres%2Frufus.ini" target="_blank">此处</a>）</li> 
 <li>将驱动器列表更改为始终按大小递增顺序列出</li> 
 <li>更新 Red Hat 和衍生产品在 9.x 版本中所需的例外情况</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpbatard%2Fuefi-ntfs" target="_blank">将 UEFI:NTFS</a> 驱动程序更新到最新版本</li> 
 <li>为没有 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FEFI_system_partition" target="_blank">ESP</a> 的 DD 模式写入的驱动器重新分配一个字母（例如 CoreELEC）</li> 
 <li>修复 Windows refusing 在 FIXED 驱动器上挂载 Linux MBR 分区的问题</li> 
 <li>修复了在使用 Joliet 时对 multiextent files 的支持</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frufus.ie%2Fzh%2F" target="_blank">https://rufus.ie/zh/</a></p>
                                        </div>
                                      
</div>
            