
---
title: 'Magisk 25.0 发布，Android 自定义套件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2429'
author: 开源中国
comments: false
date: Thu, 09 Jun 2022 07:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2429'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Magisk 是一套开放源代码的 Android（5.0 以上版本）自定义工具套件，内置了 Magisk Manager（图形化管理界面）、Root、启动脚本、SElinux 补丁和启动时认证 /dm-verity/ 强制加密移除功能。Magisk 同时提供了在无需修改系统文件的情况下更改 /system 或 /vendor 分区内容的接口，利用与 Xposed 类似的模块系统，开发者可以对系统进行修改或对所安装的软件功能进行修改等。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Magisk 25.0 发布，更新内容如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[MagiskInit] 更新 2SI 的实现，大大提高了设备的兼容性（例如索尼 Xperia 设备）</li> 
 <li>[MagiskInit] 引入新的<span> </span><code>sepolicy</code><span> </span>注入机制</li> 
 <li>[MagiskInit] 支持 Oculus Go</li> 
 <li>[MagiskInit] 支持 Android 13 GKIs（Pixel 6）</li> 
 <li>[MagiskBoot] 修复 vbmeta 提取实现</li> 
 <li>[App] 修复旧版 Android 上的 stub 应用程序</li> 
 <li>[App] [MagiskSU] 正确支持使用<span> </span><code>sharedUserId</code><span> </span>的应用</li> 
 <li>[MagiskSU] 修复<span> </span><code>magiskd</code><span> </span>中可能出现的崩溃问题</li> 
 <li>[MagiskSU] 在<span> </span><code>system_server</code><span> </span>重新启动时，修剪未使用的 UID，以防止 UID 重复使用攻击</li> 
 <li>[MagiskSU] 验证并执行已安装的 Magisk 应用程序的证书，使其与分销商的签名相匹配。</li> 
 <li>[MagiskSU] [Zygisk] 正确的软件包管理和检测</li> 
 <li>[Zygisk] 修复 Zygisk 的自代码卸载实现</li> 
 <li>[DenyList] 修复共享 UID 应用程序上的 DenyList</li> 
 <li>[BusyBox] 为运行旧内核的设备添加解决方案</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftopjohnwu%2FMagisk%2Freleases%2Ftag%2Fv25.0" target="_blank">https://github.com/topjohnwu/Magisk/releases/tag/v25.0</a></p>
                                        </div>
                                      
</div>
            