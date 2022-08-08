
---
title: 'SystemRescue 9.04 发布，Linux 系统修复盘'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9462'
author: 开源中国
comments: false
date: Mon, 08 Aug 2022 07:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9462'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">SystemRescue（以前被称为 SystemRescueCd）Linux 驱动的实时系统救援工具包已</span>更新<span style="background-color:#ffffff; color:#333333">至 9.00 版，这是一个带来新功能和技术的主要版本。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">该版本带来如下变更：</span></p> 
<ul> 
 <li>将内核更新为长期支持的 linux-5.15.58</li> 
 <li>“cow_label” 和 “cow_directory” 引导选项，现在可以通过 YAML 配置文件进行设置</li> 
 <li>新的“nomdlvm”引导选项不会激活 md raid 和 lvm 设备，防止磁盘写入 (#272)</li> 
 <li>使用预配置的 pacman 信任数据库加快启动过程并修复 pacman 使用 (#290)</li> 
 <li>改进“mountall”脚本：检测更多分区、忽略交换、LUKS 加密支持</li> 
 <li>改进“mountall”脚本：添加–readonly选项，重用空挂载点</li> 
 <li>在 initramfs 引导阶段修复 DNS 名称解析</li> 
 <li>“ca-trust”配置选项也适用于 Firefox</li> 
 <li>向 YAML 配置的“sysconfig”范围添加选项：时区、authorized_keys、书签</li> 
 <li>修复完全没有 YAML 文件时的配置（例如，通过 PXE 启动时）</li> 
 <li>添加的软件包：rclone、qemu-img、multipath-tools、unrar</li> 
</ul> 
<p>ChangeLog：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.system-rescue.org%2FChanges-x86%2F" target="_blank">https://www.system-rescue.org/Changes-x86/</a></p>
                                        </div>
                                      
</div>
            