
---
title: 'Steam++ 2.7.0 发布，Steam 工具箱'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 15:51:00 GMT
thumbnail: 'https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb'
---

<div>   
<div class="content">
                                                                                            <p>Steam++ 2.7.0 已经发布，Steam 工具箱。</p> 
<p>此版本更新内容包括：</p> 
<h3>版本亮点</h3> 
<ol> 
 <li>新增 Steam 游戏信息编辑功能，可修改游戏名称、图片、启动项等数据并同步至 Steam 客户端生效</li> 
 <li>ASF 升级至 V5.2.5.4</li> 
 <li>优化了显示图片时 GPU 占用</li> 
 <li>优化库存游戏和脚本内存占用</li> 
 <li>库存游戏编辑功能支持从 SteamGridDB 匹配预览和下载图片</li> 
 <li>网络加速新增 MEGA 网盘反代服务</li> 
 <li>macOS 支持 Arm64(Apple Silicon)</li> 
</ol> 
<h3>修复问题</h3> 
<ol> 
 <li>修复 本地令牌 无令牌刷新时提示密码错误</li> 
 <li>改进 Android 端 本地令牌 列表样式第一条与最后一条的上下外边距</li> 
 <li>改进 俄语翻译，由 vanja-san 提供</li> 
 <li>改进 .NET 运行时升级至 6.0.4(仅 Desktop 端)</li> 
 <li>改进 脚本配置 未启动时的内存占用，以及减少总体内存占用率</li> 
 <li>修复 Hosts 加速模式下使用仅启用脚本功能导致死循环</li> 
 <li>改进 Linux 端 可监听 443 端口配置</li> 
 <li>修复 Windows 端，动态桌面背景窗口显示时一些可能导致闪退的潜在问题</li> 
 <li>修复 Android 端，因 CheckBox 导致在低于 6.0 Marshmallow 系统上引发的闪退</li> 
 <li>修复 Desktop 高 DPI 分辨率下菜单图标会显示模糊的问题</li> 
 <li>修复 Windows 端，切换至网络加速菜单时可能会出现 UI 错乱的问题</li> 
 <li>修复 Desktop 端，某些情况库存游戏会卡住无限加载的问题</li> 
 <li>修复 网络加速 Onedrive 加速失效问题</li> 
 <li>修复 消息框不再提醒复选框勾上可能不生效的问题</li> 
 <li>修复 Windows 端, JumpList 切换 Steam Beta 账号失效的问题</li> 
 <li>修复 ASF，当使用 IPC.config 时，程序内打开网页端口号值不正确</li> 
</ol> 
<h3>已知问题</h3> 
<ul> 
 <li>除 Windows 之外的平台此软件自动更新尚不可用</li> 
 <li>Desktop 
  <ul> 
   <li>macOS 
    <ul> 
     <li><a href="https://gitee.com/link?target=https%3A%2F%2Fsupport.apple.com%2Fzh-cn%2Fguide%2Fmac-help%2Fmh40616%2F10.15%2Fmac%2F10.15" target="_blank">尚未公证</a>，这会影响 macOS Catalina（版本 10.15）以上版本</li> 
    </ul> </li> 
   <li>Linux 
    <ul> 
     <li>窗口弹出位置不正确</li> 
     <li>鼠标指针浮动样式不正确</li> 
    </ul> </li> 
   <li>Windows 
    <ul> 
     <li>Windows 11 
      <ul> 
       <li>在 CPU 不受支持的 Win11 上无法启动，Windows 日志中显示 <code>Failed to create CoreCLR, HRESULT: 0x80004005</code></li> 
       <li>仅 .NET 6.0 受此影响，在内部版本 22509 中修复，见 <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Fissues%2F6733" target="_blank">issue</a></li> 
       <li><strong>解决方案：</strong> 可尝试使用旧版本 例如 v2.3.0</li> 
      </ul> </li> 
     <li>Windows 7 
      <ul> 
       <li>先决条件 
        <ul> 
         <li>需要安装 Extended Security Update</li> 
        </ul> </li> 
       <li>在不符合先决条件的情况下运行可能导致 
        <ul> 
         <li>程序无法正常运行 
          <ul> 
           <li><strong>解决方案</strong> 
            <ul> 
             <li>使用 Windows Update 更新系统补丁</li> 
            </ul> </li> 
          </ul> </li> 
         <li>运行程序时提示 计算机中丢失 api-ms-win-core-winrt-l1-1-0.dll 
          <ul> 
           <li><strong>解决方案</strong> 
            <ul> 
             <li>下载 api-ms-win-core-winrt-l1-1-0.dll 文件放入程序根目录(Steam++.exe 所在文件夹) 
              <ul> 
               <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FBeyondDimension%2FSteamTools%2Fraw%2Fdevelop%2Freferences%2Fruntime.win7-x64.Microsoft.NETCore.Windows.ApiSets%2Fapi-ms-win-core-winrt-l1-1-0.dll" target="_blank">从 Github 上直接下载</a></li> 
               <li><a href="https://gitee.com/rmbgame/SteamTools/raw/develop/references/runtime.win7-x64.Microsoft.NETCore.Windows.ApiSets/api-ms-win-core-winrt-l1-1-0.dll" target="_blank">从 Gitee 上直接下载</a></li> 
              </ul> </li> 
            </ul> </li> 
          </ul> </li> 
        </ul> </li> 
      </ul> </li> 
    </ul> </li> 
   <li>Android 
    <ul> 
     <li>本地加速 
      <ul> 
       <li>因 Android 7(Nougat API 24) 之后的版本不在信任用户证书，所以此功能已放弃继续开发，如仍想使用需要自行导入证书到系统目录，使用 adb 工具或 Magisk 之类的软件操作，未来会使用不需要证书的加速功能替换此功能</li> 
      </ul> </li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h2>文件校验</h2> 
<table> 
 <thead> 
  <tr> 
   <th>File</th> 
   <th>Checksum (SHA256)</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>Steam++_win_x64_msix_v2.7.0.7z</td> 
   <td>6930256617109C3414001472BB0BC1DBFC32D563B970C8E2F73BC04F7386950F</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_v2.7.0.7z</td> 
   <td>F02E78788023B4F23B83A541E31FF4891858B0BEB5B2D4A73EB5410FFE4EFEDC</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.7.0.7z</td> 
   <td>EBD516741BFD9C8B92D4E02AF3244969D5ACAB7365D6F71F449DA9896B85DE8B</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_v2.7.0.exe</td> 
   <td>AC26185C3ACF84EAA9FD8443D43675E66893F8E1BD20F381FF37405708DFE5D9</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.7.0.exe</td> 
   <td>AFB0B1998AF51ADBEE1ADDBE16BD02A6C4DDF68E81FABD6E0ADB796C97CBE808</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.7.0.tar.zst</td> 
   <td>E541A58757B76AC7B4CD3236FC6268BA9598FA13EECB1A8F03220AE2A2140467</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.7.0.tar.zst</td> 
   <td>0840DC181874D0282BAF7A72F86FBD27053FBB9DEF1C7FFA8D2D85387E110692</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.7.0.deb</td> 
   <td>545E40C7D24A51F7572362294190CD7265F5E58297180970B89313801D7BFCC8</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.7.0.deb</td> 
   <td>B330C7B7E30F95BA078D615EA987D0BA2C6EFA8A3D8B4934B09D7A7510AEBA4D</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.7.0.rpm</td> 
   <td>07BC6C71ACBBD3A3624962EB2D57CD079BF46979474EFD40753DA4EAF3753B12</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.7.0.rpm</td> 
   <td>B778AC4EEB6CC974582B4521C8DFDFAE6E41AF259484C192826C3C8058FEFB4C</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.7.0.dmg</td> 
   <td>C9D0E92D64A857FB0199E2E55CAD4FA82DD92C7F4989B52B918DB3F0DA62C3D6</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_arm64_v2.7.0.dmg</td> 
   <td>2EEDAB66805D621F4FE54617F7476A8FC7388C05E7710FEA0A999C57C86D84F6</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_android_v2.7.0.apk</td> 
   <td>6C23806E4F06465398C27813B3150E1C5D44341DB3B9CE4517B0ACBEF35E013A</td> 
  </tr> 
 </tbody> 
</table> 
<p><a href="https://gitee.com/link?target=https%3A%2F%2Fsteampp.net" target="_blank"><img alt="WebSite steampp.net" src="https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/news/193119"><img alt="Steam++ v2.7.0" src="https://img.shields.io/badge/Steam++-v2.7.0-brightgreen.svg?style=flat-square&color=512bd4" referrerpolicy="no-referrer"></a></p> 
<p><a href="https://gitee.com/rmbgame/SteamTools/blob/develop/download-guide.md" target="_blank">不知道该下载哪个文件?</a></p> 
<p>详情查看：<a href="https://gitee.com/rmbgame/SteamTools/releases/2.7.0">https://gitee.com/rmbgame/SteamTools/releases/2.7.0</a></p>
                                        </div>
                                      
</div>
            