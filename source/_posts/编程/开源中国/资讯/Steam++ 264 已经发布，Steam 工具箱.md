
---
title: 'Steam++ 2.6.4 已经发布，Steam 工具箱'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7033'
author: 开源中国
comments: false
date: Wed, 05 Jan 2022 16:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7033'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Steam++ 2.6.4 已经发布，Steam 工具箱</p> 
<p>此版本更新内容包括：</p> 
<h2>版本亮点</h2> 
<ol> 
 <li>CLR 升级至 6.0.1，Avalonia 升级至 0.10.11，等其他依赖项升级</li> 
 <li>新增 macOS ARM64 包，用于 M1 系列设备</li> 
 <li>改进 本地令牌-确认交易 窗口标题中显示令牌名称</li> 
 <li>新增 Android x64 架构包，适用于 Intel、AMD 芯片的设备或虚拟机</li> 
 <li>新增 Android ASF 本地挂卡功能 (Beta)</li> 
 <li>新增 Android 网络加速功能 (Alpha)</li> 
 <li>改进 Android 冷启动速度</li> 
 <li>改进 Android 导入令牌成功后回到列表页</li> 
</ol> 
<h2>修复问题</h2> 
<ol> 
 <li>修复 Linux / macOS 因默认字体导致启动时崩溃(core dumped) #827</li> 
 <li>修复 ASF Json 配置文件改变时引发闪退 #793</li> 
 <li>修复 macOS 系统代理</li> 
 <li>修复 Android 屏幕捕获设置项不生效</li> 
 <li>修复 Android 令牌列表有时不显示值</li> 
 <li>修复 Android 确认交易 全选/全不选 复选框勾选时逻辑不正确执行</li> 
</ol> 
<h3>已知问题</h3> 
<ul> 
 <li>除 Windows 之外的平台此软件自动更新尚不可用</li> 
 <li>Android 
  <ul> 
   <li>本地加速 
    <ul> 
     <li>VPN 模式不能正常工作</li> 
     <li>需要在 Wifi 或 流量 上手动设置代理地址，关闭时手动清除设置</li> 
     <li>Android 7+ 不信任用户证书</li> 
    </ul> </li> 
  </ul> </li> 
 <li>Desktop 
  <ul> 
   <li>macOS 
    <ul> 
     <li><a href="https://gitee.com/link?target=https%3A%2F%2Fsupport.apple.com%2Fzh-cn%2Fguide%2Fmac-help%2Fmh40616%2F10.15%2Fmac%2F10.15" target="_blank">尚未公证</a>，这会影响 macOS Catalina（版本 10.15）以上版本</li> 
    </ul> </li> 
   <li>Linux 
    <ul> 
     <li><strong>Hosts 代理模式</strong>可能无法配置成功，推荐使用<strong>系统代理模式</strong></li> 
     <li>系统代理模式下discord更新下载加速有问题暂不可用</li> 
     <li>窗口弹出位置不正确</li> 
     <li>鼠标指针浮动样式不正确</li> 
    </ul> </li> 
   <li>Windows 
    <ul> 
     <li>Windows 11 
      <ul> 
       <li>在 CPU 不受支持的 Win11 上无法启动，Windows 日志中显示 <code>Failed to create CoreCLR, HRESULT: 0x80004005</code></li> 
       <li>仅 .NET 6.0 受此影响，在几周后的 Insider 中会修复，见 <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Fissues%2F6733" target="_blank">issue</a></li> 
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
         <li>程序无法正常运行</li> 
         <li>运行程序时提示 计算机中丢失 api-ms-win-core-winrt-l1-1-0.dll</li> 
        </ul> </li> 
       <li><strong>解决方案</strong> 
        <ul> 
         <li>因 <a href="https://gitee.com/link?target=https%3A%2F%2Fsupport.microsoft.com%2Fzh-cn%2Fwindows%2Fwindows-7-%25E6%2594%25AF%25E6%258C%2581%25E4%25BA%258E-2020-%25E5%25B9%25B4-1-%25E6%259C%2588-14-%25E6%2597%25A5%25E7%25BB%2588%25E6%25AD%25A2-b75d4580-2cc7-895a-2c9c-1466d9a53962" target="_blank">Windows 7 延长结束日期</a>以于 2020 年 1 月 14 日结束支持 
          <ul> 
           <li>所以必须安装 <a href="https://gitee.com/link?target=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Ftroubleshoot%2Fwindows-client%2Fwindows-7-eos-faq%2Fwindows-7-extended-security-updates-faq" target="_blank">Extended Security Update</a> 支持，在安装第三年的补丁后<a href="https://gitee.com/link?target=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Flifecycle%2Fproducts%2Fwindows-7" target="_blank">结束支持日期</a>可延长至 2023 年 1 月 10 日</li> 
           <li>可安装 <em>第三方</em> 补丁整合包例如 <strong><a href="https://gitee.com/link?target=https%3A%2F%2Fcn.bing.com%2Fsearch%3Fq%3DUpdatePack7R2" target="_blank">UpdatePack7R2</a></strong> <em>或</em> 购买官方 ESU 产品密钥 解决</li> 
          </ul> </li> 
         <li>下载 api-ms-win-core-winrt-l1-1-0.dll 文件放入程序根目录(Steam++.exe 所在文件夹) 
          <ul> 
           <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FBeyondDimension%2FSteamTools%2Fraw%2Fdevelop%2Freferences%2Fruntime.win7-x64.Microsoft.NETCore.Windows.ApiSets%2Fapi-ms-win-core-winrt-l1-1-0.dll" target="_blank">从 Github 上直接下载</a></li> 
           <li><a href="https://gitee.com/rmbgame/SteamTools/raw/develop/references/runtime.win7-x64.Microsoft.NETCore.Windows.ApiSets/api-ms-win-core-winrt-l1-1-0.dll" target="_blank">从 Gitee 上直接下载</a></li> 
           <li><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fapi%2Fv2%2Fpackage%2Fruntime.win7-x64.Microsoft.NETCore.Windows.ApiSets%2F1.0.1" target="_blank">从 NuGet 上下载后提取</a> 
            <ul> 
             <li>.nupkg 文件可使用解压工具打开或解压，找到此文件复制即可</li> 
            </ul> </li> 
          </ul> </li> 
        </ul> </li> 
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
   <td>Steam++_win_x64_v2.6.4.7z</td> 
   <td>A76694636920AABBBC7D73B4DAE15279D9FEFFA6E15E9D37470545CBAC996347</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.6.4.7z</td> 
   <td>CE0B3793B8D53784C310D01F94E02A9F9E207E4893F6CA1DBBEB3E19AFEBBCA8</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_v2.6.4.exe</td> 
   <td>3BFDB622376AD344E7EBA6FFB720B6AA9BC2148FE70F23B7D669C76CF24FD434</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.6.4.exe</td> 
   <td>1C5FBDF3081B54E47A006BA7AC894530905CF064D2047A0F3736AF27E7D776A2</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.6.4.7z</td> 
   <td>69502C158D00B4BBC497F335C67B54494992E5B9742B13BC766EFAE2DAB19D91</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.6.4.7z</td> 
   <td>CE376B05676DB330670D927D10B0BAA632B6E5754152BBADC8DAD9ACD164F950</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.6.4.deb</td> 
   <td>A8BF8FAE9833BF550D8ED5779FA7E568970B9D9932CB3F52171AE34AA1DF69D6</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.6.4.deb</td> 
   <td>29C45A2AA6911A6554A884F3FF05409E3C063F3BA1405BCD8DF90EA247533246</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.6.4.rpm</td> 
   <td>3DFC553BAB33025EB08EE8267BDD1656F59E4611E6B8E0AE9388EA68C938DBFE</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.6.4.rpm</td> 
   <td>BA3D8680D248E93748783E44C7A11F52521844F21A242C283EAF0F720276587E</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.6.4.dmg</td> 
   <td>3BF9EDC4053BA08B706EE47234A8B4A3C73FEB1A952289E82D029BB17217219D</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_arm64_v2.6.4.dmg</td> 
   <td>B69C718F631605514513C40C78B749AB11625E5C9EFD43190E33D774DD50482B</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_android_arm64_v8a_v2.6.4.apk</td> 
   <td>542A6902282C2F315330B4288E8A952F1B35A1F6181B65E04D05B5B591ABD369</td> 
  </tr> 
  <tr> 
   <td>Steam++_android_armeabi_v7a_v2.6.4.apk</td> 
   <td>7D2F65D94D5EAC00CE42761C17E2CEBFF91671C85F66F52CFE21B3A4F03EC845</td> 
  </tr> 
  <tr> 
   <td>Steam++_android_x64_v2.6.4.apk</td> 
   <td>B91986EA5C5F69C311088B7B613CF4947AA814077FB909AEC634FFA9BEC0ACE9</td> 
  </tr> 
 </tbody> 
</table> 
<p>详情查看：<a href="https://gitee.com/rmbgame/SteamTools/releases/2.6.4">https://gitee.com/rmbgame/SteamTools/releases/2.6.4</a></p>
                                        </div>
                                      
</div>
            