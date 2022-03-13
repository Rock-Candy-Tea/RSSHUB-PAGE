
---
title: 'Magisk 24.3 发布，定制 Android 的开源软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8338'
author: 开源中国
comments: false
date: Sun, 13 Mar 2022 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8338'
---

<div>   
<div class="content">
                                                                                            <p>Magisk 是一套开放源代码的 Android（5.0 以上版本）自定义工具套组，内置了 Magisk Manager（图形化管理界面）、Root、启动脚本、SElinux 补丁和启动时认证 /dm-verity/ 强制加密移除功能。Magisk 同时提供了在无需修改系统文件的情况下更改 /system 或 /vendor 分区内容的接口，利用与 Xposed 类似的模块系统，开发者可以对系统进行修改或对所安装的软件功能进行修改等。</p> 
<p>Magisk 24.3 发布，更新内容如下：</p> 
<ul> 
 <li>[General] 停止使用 <code>getrandom</code> 系统调用</li> 
 <li>[Zygisk] 更新 API 至 v3，为 <code>AppSpecializeArgs</code> 添加新字段</li> 
 <li>[App] 改进应用重新打包的安装工作流程</li> 
 <li>[MagiskSU] 修复缓冲区溢出问题</li> 
 <li>[MagiskSU] 修正所有者管理的多用户超级用户设置</li> 
 <li>[MagiskSU] 修正使用 <code>su -c <cmd></code> 时的命令记录</li> 
 <li>[MagiskSU] 防止 su 请求无限期阻塞</li> 
 <li>[MagiskBoot] 修复 <code>lz4_lg</code> 压缩</li> 
 <li>[DenyList] 允许定位以系统 UID 身份运行的进程</li> 
 <li>[Zygisk] 改进 Zygisk 加载机制</li> 
 <li>[Zygisk] 修复应用程序 UID 跟踪</li> 
 <li>[Zygisk] 修复在 zygote 中设置的不正确的 <code>umask</code></li> 
 <li>[App] 修复 BusyBox 执行测试</li> 
 <li>[App] 改进存根加载机制</li> 
 <li>[App] 主要的应用升级流程改进</li> 
 <li>[General] 改进命令行错误处理和信息传递</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftopjohnwu%2FMagisk%2Freleases" target="_blank">https://github.com/topjohnwu/Magisk/releases</a></p>
                                        </div>
                                      
</div>
            