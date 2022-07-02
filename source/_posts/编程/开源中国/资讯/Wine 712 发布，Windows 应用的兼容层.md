
---
title: 'Wine 7.12 发布，Windows 应用的兼容层'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2486'
author: 开源中国
comments: false
date: Sat, 02 Jul 2022 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2486'
---

<div>   
<div class="content">
                                                                                            <p>Wine（Wine Is Not an Emulator）是一个能够在多种兼容 POSIX 接口的操作系统（诸如 Linux、macOS 与 BSD 等）上运行 Windows 应用的兼容层。它不是像虚拟机或者模拟器一样模仿内部的 Windows 逻辑，而是将 Windows API 调用翻译成为动态的 POSIX 调用，免除了性能和其它一些行为的内存占用，让你能够干净地整合 Windows 应用到桌面。</p> 
<p>Wine 7.12 已经正式发布，该版本中值得关注的更新内容包括：</p> 
<ul> 
 <li>对 Qt5 应用程序的主题支持</li> 
 <li>捆绑的 vkd3d 升级到了 1.4 版本</li> 
 <li>改进了 Direct2D 中的效果支持</li> 
 <li>在注册表工具中支持 QWORD</li> 
 <li>各种错误修复 
  <ul> 
   <li>Star Citizen：没有麦克风输入音频（用于 voip）</li> 
   <li>Star Citizen：启动器在启动时崩溃并出现 winmm 错误</li> 
   <li>Shogun Total War 2 在启动时崩溃</li> 
   <li>aria2 需要 QueryContextAttributes(SECPKG_ATTR_CIPHER_INFO)来返回一个有效的版本</li> 
   <li>在浅色主题中，所选按钮的显示不正确</li> 
   <li>如果启用浅色主题，Wireshark 在不同地方显示黑色矩形</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.winehq.org%2Fannounce%2F7.12" target="_blank">https://www.winehq.org/announce/7.12</a></p>
                                        </div>
                                      
</div>
            