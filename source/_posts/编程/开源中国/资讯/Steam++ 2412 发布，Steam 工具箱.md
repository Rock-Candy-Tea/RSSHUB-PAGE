
---
title: 'Steam++ 2.4.12 发布，Steam 工具箱'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7192'
author: 开源中国
comments: false
date: Mon, 06 Sep 2021 22:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7192'
---

<div>   
<div class="content">
                                                                                            <p>Steam++ 2.4.12 已经发布，Steam 工具箱。</p> 
<p>此版本更新内容包括：</p> 
<h3>新增内容</h3> 
<ol> 
 <li>新增 Desktop 上网络加速代理设置</li> 
 <li>新增 Android 上屏幕捕获设置项，用于允许截图或录制视频</li> 
 <li>新增 Windows 托盘菜单支持切换账号与复制令牌</li> 
 <li>新增 Linux/macOS 托盘菜单改进与完善</li> 
</ol> 
<h3>修复问题</h3> 
<ol> 
 <li>修复 Desktop 上用户头像应当为圆形而不是方形</li> 
 <li>修复 Android 上切换系统语言可能引发的闪退</li> 
 <li>修复 Windows 10 上启动时可能出现的网络连接中断提示</li> 
 <li>修复 Android 上令牌倒计时可能引发的闪退</li> 
 <li>修复 Desktop 上库存游戏刷新可能引发的闪退</li> 
 <li>修复 Desktop 上可能少加载了部分已安装游戏</li> 
 <li>修复 Android 上暗色模式下某些区域背景为白色</li> 
 <li>改进 Android 上令牌刷新倒计时</li> 
 <li>改进 本地令牌名称最大长度限制 32 个字符</li> 
 <li>改进 Desktop 上网络加速 UI</li> 
 <li>修复 Desktop 上默认头像可能引发的闪退</li> 
 <li>改进 Desktop 上左侧菜单图标</li> 
</ol> 
<h3>已知问题</h3> 
<ul> 
 <li>Desktop 
  <ul> 
   <li>macOS 
    <ul> 
     <li>尚未公证，这会影响 macOS Catalina（版本 10.15）以上</li> 
     <li>某些窗口顶部会有两个标题栏</li> 
     <li>自动更新不可用</li> 
    </ul> </li> 
   <li>Linux 
    <ul> 
     <li>当使用 root 权限运行时托盘不生效，可通过 Exit.sh 退出程序</li> 
     <li>窗口弹出位置不正确</li> 
     <li>窗口顶部会有两个标题栏</li> 
     <li>自动更新不可用</li> 
    </ul> </li> 
   <li>Shared 
    <ul> 
     <li>主题切换需重启软件后生效，且跟随系统暂不可用</li> 
    </ul> </li> 
  </ul> </li> 
 <li>Mobile 
  <ul> 
   <li>Android 
    <ul> 
     <li>确认交易列表刷新后数据显示不正确</li> 
     <li>自动更新暂不可用</li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<hr> 
<table> 
 <thead> 
  <tr> 
   <th>RuntimeIdentifier</th> 
   <th>Available</th> 
   <th>Edition</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>win-x64</td> 
   <td>✅</td> 
   <td>Stable</td> 
  </tr> 
  <tr> 
   <td>osx-x64</td> 
   <td>✅</td> 
   <td>β</td> 
  </tr> 
  <tr> 
   <td>linux-x64</td> 
   <td>✅</td> 
   <td>α</td> 
  </tr> 
  <tr> 
   <td>android-arm64</td> 
   <td>✅</td> 
   <td>α</td> 
  </tr> 
  <tr> 
   <td>android-arm</td> 
   <td>✅</td> 
   <td>α</td> 
  </tr> 
  <tr> 
   <td>linux-arm64</td> 
   <td>✅</td> 
   <td>α</td> 
  </tr> 
  <tr> 
   <td>linux-arm</td> 
   <td>✅</td> 
   <td>α</td> 
  </tr> 
  <tr> 
   <td>osx-arm64</td> 
   <td>❌</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>win-arm64</td> 
   <td>❌</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>ios-arm64</td> 
   <td>❌</td> 
   <td> </td> 
  </tr> 
 </tbody> 
</table> 
<h2>下载指南</h2> 
<ul> 
 <li>Windows 
  <ul> 
   <li>如果你使用 Intel、AMD 的 x64 芯片的 Mac（较为<strong>普遍</strong>），则下载文件名中带有 <strong>win_x64</strong> 的文件</li> 
  </ul> </li> 
 <li>macOS 
  <ul> 
   <li>如果你使用 Intel、AMD 的 x64 芯片的 Mac（较为<strong>普遍</strong>），则下载文件名中带有 <strong>macos_x64</strong> 的文件</li> 
   <li>如果你使用 ARM64 芯片的 Mac（较为<strong>稀有</strong>），例如 <strong>M1</strong>，则下载文件名中带有 <strong>macos_x64</strong> 的文件可通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsupport.apple.com%2Fzh-cn%2FHT211861" target="_blank">Rosetta 2</a> 运行</li> 
  </ul> </li> 
 <li>Linux 
  <ul> 
   <li>如果你使用 Intel、AMD 的 x64 芯片的 PC（较为<strong>普遍</strong>）则下载文件名中带有 <strong>linux_x64</strong> 的文件</li> 
   <li>如果你使用 ARM64 芯片的 PC（较为<strong>稀有</strong>）例如 <strong>Raspberry Pi Model 3+</strong>，则下载文件名中带有 <strong>linux_arm64</strong> 的文件</li> 
   <li>如果你使用 ARM32 芯片的 PC（较为<strong>稀有</strong>）例如 <strong>Raspberry Pi Model 2+</strong>，则下载文件名中带有 <strong>linux_arm</strong> 的文件</li> 
  </ul> </li> 
 <li>Android 
  <ul> 
   <li>如果你使用 ARM64 芯片的设备（较为<strong>普遍</strong>）则下载文件名中带有 <strong>android_arm64_v8a</strong> 的文件</li> 
   <li>如果你使用 ARM32 芯片的设备（较为<strong>稀有</strong>）通常为 <strong>14</strong> 年下半年之前生产的设备，则下载文件名中带有 <strong>android_armeabi_v7a</strong> 的文件</li> 
  </ul> </li> 
</ul> 
<table> 
 <thead> 
  <tr> 
   <th>File</th> 
   <th>Checksum (SHA256)</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>Steam++_win_x64_v2.4.12.7z</td> 
   <td>30C6FBD285EEB5EABE64BA8AAD6576234EA11897A29BA84EF590CF9DCB4AC7E4</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_v2.4.12.exe</td> 
   <td>30C8625BF73D80A611B2F0DD04B3CE70364818CB1A2B5004074639A72D679B88</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.4.12.7z</td> 
   <td>3A47E0BBC5B7DE5C11566EEF2E959850667C68FCAB6D9ABC657007EA097DD2B0</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.4.12.7z</td> 
   <td>A65842BF3A0FB9EC06A1B4CAA8710C092426FE32309512A8247D9E465224121B</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm_v2.4.12.7z</td> 
   <td>777AF29137C93F90F9477C6D9F62D7D55ABA7873C3FB5335C003953CC01857B7</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.4.12.dmg</td> 
   <td>1740F3CF154202BC7E2FB101187404637CE622D88A1528CE0F40517A3FD967FC</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.4.12.app.zip</td> 
   <td>35139413AB7694CD730A26836D825057D50C2D80FE6A4CB36B4F15E3A3652BEB</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.4.12.7z</td> 
   <td>E450102A5F5AFFF170C82836064B0EE97E03E0501B246F62E1B494392E0523D1</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_android_arm64_v8a_v2.4.12.apk</td> 
   <td>A854FB5D69AA5FD86C8092C5DD7D923BD34DA6C1EB9120675667D5D91E83FA8F</td> 
  </tr> 
  <tr> 
   <td>Steam++_android_armeabi_v7a_v2.4.12.apk</td> 
   <td>F510D114B21D323576D8ACED296D20227BBA48053DC047C92B2BA260447FEF08</td> 
  </tr> 
 </tbody> 
</table> 
<p>详情查看：<a href="https://gitee.com/rmbgame/SteamTools/releases/2.4.12">https://gitee.com/rmbgame/SteamTools/releases/2.4.12</a></p>
                                        </div>
                                      
</div>
            