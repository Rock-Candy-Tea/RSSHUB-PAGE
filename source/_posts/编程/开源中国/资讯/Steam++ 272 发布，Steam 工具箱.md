
---
title: 'Steam++ 2.7.2 发布，Steam 工具箱'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb'
author: 开源中国
comments: false
date: Sat, 30 Apr 2022 17:18:00 GMT
thumbnail: 'https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb'
---

<div>   
<div class="content">
                                                                                            <p>Steam++ 2.7.2 已经发布，Steam 工具箱。</p> 
<p>此版本更新内容包括：</p> 
<h3>版本亮点</h3> 
<ol> 
 <li>ASF 升级至 V5.2.5.5</li> 
</ol> 
<h3>修复问题</h3> 
<ol> 
 <li>修复 判断 Administrator 或 Root 权限函数错误，例如导致 Windows 上开机自启失效等其他问题</li> 
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
   <td>Steam++_win_x64_v2.7.2.7z</td> 
   <td>636CDBB82A3F9C4CCE061E44A3D94D3D184A59211A135E82500072393DF5526C</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.7.2.7z</td> 
   <td>B0BA27A8B0C627B3F009D13BD09ED25D415AB07DFB51F18ACCDD969136B8676E</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_msix_v2.7.2.7z</td> 
   <td>F2E13286C3A85CA48F281F9C87B31EFF3A03BDF6EE2D1ACB8414E66994EC37DE</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_v2.7.2.exe</td> 
   <td>48C72D522E5E04A98697E833D9535FB4CB816B8D633AA47C3C9A0842B97535BE</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.7.2.exe</td> 
   <td>FBEB9F0651F66D691FDE04E56B703087101E47B837E88717C8181FF334E989EE</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.7.2.tar.zst</td> 
   <td>D30E07147D54FE1727DF23DD09CAAF657CC9A71A88536CEF6ECB005CF0930191</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.7.2.tar.zst</td> 
   <td>8709D03A23193F3DA5B5F9BC65962817A5BEE21B3AA74C3D968BCF495650CE54</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.7.2.deb</td> 
   <td>21DF72949070FFFC2367F8B47CD355A96C45B0DB5375802B03C8B45F84A46462</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.7.2.deb</td> 
   <td>D3E5E70EEF3D8810898E9092ED3CE7909A3CD8C9BEBD1A3644C550313A8AF761</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.7.2.rpm</td> 
   <td>34861E36B41D1626DAE6445C07134887EB1D945DBF4CC4EA88C8BF04126A5F52</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.7.2.rpm</td> 
   <td>E7188BB4E50318F96B9DC8240C6AA5D628A910FDD7E436156646D1A2C7059EB5</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.7.2.dmg</td> 
   <td>F31FE7ECDA1B84ACA2CDEEABBB5FC1F3C8C533B1A1A2877BA3DA5228068B4CE8</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_arm64_v2.7.2.dmg</td> 
   <td>143A42787341BEBF849A9CE754BA2758267B399A394ADC016D398E7E81120355</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_android_v2.7.2.apk</td> 
   <td>68DAA679DD631C20814475A93DE1CF4674C299B1B130FD409D72405DBE4B1177</td> 
  </tr> 
 </tbody> 
</table> 
<p><a href="https://gitee.com/link?target=https%3A%2F%2Fsteampp.net" target="_blank"><img alt="WebSite steampp.net" src="https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/news/193763"><img alt="Steam++ v2.7.2" src="https://img.shields.io/badge/Steam++-v2.7.2-brightgreen.svg?style=flat-square&color=512bd4" referrerpolicy="no-referrer"></a></p> 
<p><a href="https://gitee.com/rmbgame/SteamTools/blob/develop/download-guide.md" target="_blank">不知道该下载哪个文件?</a></p> 
<p>详情查看：<a href="https://gitee.com/rmbgame/SteamTools/releases/2.7.2">https://gitee.com/rmbgame/SteamTools/releases/2.7.2</a></p>
                                        </div>
                                      
</div>
            