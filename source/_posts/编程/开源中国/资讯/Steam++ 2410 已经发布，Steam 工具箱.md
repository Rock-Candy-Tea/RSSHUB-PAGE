
---
title: 'Steam++ 2.4.10 已经发布，Steam 工具箱'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2415'
author: 开源中国
comments: false
date: Tue, 24 Aug 2021 15:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2415'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Steam++ 2.4.10 已经发布，Steam 工具箱 </p>
<p>此版本更新内容包括：</p>
<h3>新增内容</h3> 
<ol> 
 <li>Linux/macOS 版本中的 CLR 升级至 .NET 6 Preview 7</li> 
 <li>Desktop 现已适配 WinUI 3 / Windows 11 / Fluent Design System 样式风格</li> 
 <li>新增 Android 上从图库选择二维码图片导入令牌</li> 
 <li>新增 Android 上文件导入选择二维码图片导入令牌</li> 
 <li>新增 Desktop 上现可刷新头像</li> 
</ol> 
<h3>修复问题</h3> 
<ol> 
 <li>修复 Desktop 上账号切换功能</li> 
 <li>改进 Desktop 上受保护的成就不在支持勾选</li> 
 <li>修复 Linux 上因字体引发的启动时闪退</li> 
 <li>修复 Android 上扫码导入功能</li> 
 <li>修复 Android 上 Toast 不能正常显示</li> 
 <li>改进 Android 上的令牌导入方式</li> 
 <li>修复 Android 上导入带密码的令牌时不显示密码输入框</li> 
 <li>修复 导入带密码的令牌时密码输入文本框窗口不能正确取消</li> 
 <li>修复 Desktop 上使用火狐浏览器无法进行快速登录</li> 
 <li>修复 Android 8.0 以下启动时闪退</li> 
 <li>修复 Desktop 上部分用户库存游戏已安装游戏无法读取</li> 
 <li>尝试修复 Windows 上托盘菜单有时无法打开窗口</li> 
 <li>改进 Android 上确认交易页面上的显示隐藏逻辑</li> 
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
     <li>托盘不生效，这将影响程序不能正常退出</li> 
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
     <li>本地令牌倒计时存在误差不够精确，可能导致令牌值不一致</li> 
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
   <td></td> 
  </tr> 
  <tr> 
   <td>win-arm64</td> 
   <td>❌</td> 
   <td></td> 
  </tr> 
  <tr> 
   <td>ios-arm64</td> 
   <td>❌</td> 
   <td></td> 
  </tr> 
 </tbody> 
</table> 
<h2>下载指南</h2> 
<ul> 
 <li>Linux 
  <ul> 
   <li>如果你使用 Intel、AMD 芯片的 PC（较为<strong>普遍</strong>）则下载文件名中带有 <strong>linux_x64</strong> 的文件</li> 
   <li>如果你使用 ARM64 芯片的 PC（较为<strong>稀有</strong>）例如 <strong>Raspberry Pi Model 3+</strong>，则下载文件名中带有 <strong>linux_arm64</strong> 的文件</li> 
   <li>如果你使用 ARM 芯片的 PC（较为<strong>稀有</strong>）例如 <strong>Raspberry Pi Model 2+</strong>，则下载文件名中带有 <strong>linux_arm</strong> 的文件</li> 
  </ul> </li> 
 <li>Android 
  <ul> 
   <li>如果你使用 ARM64 芯片的设备（较为<strong>普遍</strong>）则下载文件名中带有 <strong>android_arm64_v8a</strong> 的文件</li> 
   <li>如果你使用 ARM 芯片的设备（较为<strong>稀有</strong>）通常为 <strong>14</strong> 年下半年之前生产的设备，则下载文件名中带有 <strong>android_armeabi_v7a</strong> 的文件</li> 
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
   <td>Steam++_win_x64_v2.4.10.7z</td> 
   <td>767FEC42DA14A632E92D517E96487F74184F55D6AFB7D95E57747E6AB3F4AC37</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_v2.4.10.exe</td> 
   <td>D598A9807F6325D2E07C1FF7CE4ADFC1605501E5115FC94014FEAF88FBCBEA1B</td> 
  </tr> 
  <tr> 
   <td></td> 
   <td></td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.4.10.7z</td> 
   <td>6C10CCA10A073321AED815491C8F05B79F2602AE7BB187470C1FCD7A05519187</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.4.10.7z</td> 
   <td>97AC7F2C5B7A369910B632CE0671B7BFF5BCD05598F5A44074F55E2BF5EED816</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm_v2.4.10.7z</td> 
   <td>F1E14F7BDB96BB9D86ACD0F94E11F4F565F3C13154711D69E5E9EAB18983FAE4</td> 
  </tr> 
  <tr> 
   <td></td> 
   <td></td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.4.10.app.zip</td> 
   <td>59166D17023333E24E5DA9D7B7920B5F67E3F3EE5CDD30F903422C48BF4405BD</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.4.10.7z</td> 
   <td>7B59A36E34829F4343FD2048CDD2E899478C77E4FFAEFD877B52AD0429CB5D7C</td> 
  </tr> 
  <tr> 
   <td></td> 
   <td></td> 
  </tr> 
  <tr> 
   <td>Steam++_android_arm64_v8a_v2.4.10.apk</td> 
   <td>432046DF7C9BBA5CCBD8AC476CE31C9A8022C3F46508F8A32E7D42081A29DDA3</td> 
  </tr> 
  <tr> 
   <td>Steam++_android_armeabi_v7a_v2.4.10.apk</td> 
   <td>25584531B040E2B50EB0855D1E3242978E37EF554019241E6C4FDB25E7B8533D</td> 
  </tr> 
 </tbody> 
</table> 
<p>详情查看：<a href="https://gitee.com/rmbgame/SteamTools/releases/2.4.10" blank="_target">https://gitee.com/rmbgame/SteamTools/releases/2.4.10</a></p>
                                        </div>
                                      
</div>
            