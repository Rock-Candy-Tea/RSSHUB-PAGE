
---
title: 'webOS OSE 2.10.0 发布，开源版 webOS'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7498'
author: 开源中国
comments: false
date: Sat, 10 Apr 2021 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7498'
---

<div>   
<div class="content">
                                                                                            <p>webOS 是一个以网络为中心、以可用性为核心的智能设备软件平台，其性能和稳定性已经在超过 7000 万台 LG 智能电视上得到了验证。自适应显示产品以来，webOS 已经走过了漫长的道路，并发展成为适用于更多产品的软件平台。</p> 
<p>2018 年 3 月，在开放平台、开放合作、开放连接的理念下，webOS 的开源项目被称为 webOS 开源版（OSE）。在 webOS 的核心架构之上，webOS OSE 提供了更多的功能，可以扩展到更多样的行业垂直领域。</p> 
<p>webOS OSE 2.10.0 正式发布，本次更新内容如下：</p> 
<ul> 
 <li> <p>存储访问框架</p> <p>存储访问服务提供了一个界面来控制各种存储。使用此框架，用户可以使用标准的易于使用的UI浏览和打开所有已配置的存储提供程序中的文档，图像或文件。</p> <p>目前，存储访问框架支持以下存储：</p> 
  <ul> 
   <li>内部存储器</li> 
   <li>USB存储</li> 
   <li>云端存储（Google Drive）</li> 
  </ul> </li> 
 <li> <p>启用 Blink 的 cookie 加密 Cookie 存储了客户端和服务器之间的登录和会话信息。未加密的 Cookie 可能会给攻击者提供窃取或使用信息的机会。在这个版本中，用户可以使用 cookie 加密，从平台安全的角度保护用户数据。</p> </li> 
 <li> <p>外设管理器服务 外设管理器服务是新引入的支持各种外围设备（GPIO、SPI、I2C、UART）的服务。该服务可以在不改变平台源代码的情况下，轻松控制外围设备。</p> </li> 
 <li> <p>ACG 的改进 ACG（Access Control Groups）是一种安全模型，它为运行在 Luna Bus 上的服务提供安全权限的访问控制。</p> </li> 
 <li> <p>ACG 迁移</p> 
  <ul> 
   <li>修正了与 GSlice 内存问题有关的崩溃问题；</li> 
   <li>修改了 trustLevel 语法；</li> 
   <li>修改了.perm.json 文件的语法；</li> 
   <li>迁移了 bugreportd 到 ACG 模型；</li> 
   <li>为测试 WebRTC 应用添加了 ACG 权限；</li> 
  </ul> </li> 
 <li> <p>核心应用</p> 
  <ul> 
   <li> <p>示例应用程序</p> <p>添加了一个 MediaGallery 应用程序；</p> </li> 
  </ul> </li> 
 <li> <p>应用框架</p> 
  <ul> 
   <li>SDK 发布命令行界面（CLI）2.1.0；</li> 
  </ul> </li> 
 <li> <p>管理和服务</p> 
  <ul> 
   <li> <p>应用</p> <p>SAM：为 configdata 添加了 .yaml 文件；</p> </li> 
   <li> <p>显示 LSM 清理 maliit-framework-webos 中未使用的文件； 修正了 VKB 位置不正确的问题； 键盘视图动画； 升级 Qt 版本至 v5.12.10； 更新了 Qt 和 MaliitServer 的 initscripts；</p> </li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.webosose.org%2Fabout%2Frelease-notes%2Fwebos-ose-2-10-0-release-notes%2F" target="_blank">https://www.webosose.org/about/release-notes/webos-ose-2-10-0-release-notes/</a></p>
                                        </div>
                                      
</div>
            