
---
title: 'Steam++ 2.8.1 发布，Steam 工具箱'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb'
author: 开源中国
comments: false
date: Sat, 23 Jul 2022 22:45:00 GMT
thumbnail: 'https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb'
---

<div>   
<div class="content">
                                                                                            <p>Steam++ 2.8.1 已经发布，Steam 工具箱。</p> 
<p>此版本更新内容包括：</p> 
<h3>公告</h3> 
<ol> 
 <li>非简中语言将默认隐藏加速和脚本功能，仅能通过切换语言并重启程序的方式还原被隐藏的功能</li> 
 <li>因经济状况原因，现已停止短信服务节约开销，后续会推出邮箱注册登录，对于仅使用手机号登录的用户请绑定第三方快速登录，否则注销后将无法再次登录，需要等待至邮箱服务推出后支持会暂时在开放短信服务提供换绑邮箱。</li> 
 <li>自动更新目前仅 Windows 端可用，且由于下载渠道限速可能导致无法更新成功，推荐在官网链接的网盘或群文件中下载压缩包解压覆盖更新(应用商店版由商店更新不受此影响)</li> 
 <li>在 Android 上因系统限制，目前的加速功能无法正常使用，所以此功能已放弃继续开发，如仍想使用需要自行导入证书到系统目录，使用 adb 工具或 Magisk 之类的软件操作，未来会使用不需要证书的加速功能替换此功能</li> 
 <li>fde 版本需要安装 <a href="https://gitee.com/link?target=https%3A%2F%2Fdotnet.microsoft.com%2Fzh-cn%2Fdownload%2Fdotnet%2F6.0" target="_blank">ASP.NET Core 运行时 6.0.7 (x64) 与 .NET Core 运行时 6.0.7 (x64)</a></li> 
 <li>Windows x86 与 x64 版本令牌本机加密互不兼容，使用两者版本时注意令牌加密后的文件不能共用。</li> 
 <li>由于新版本加速功能重构，调整了部分加速项目，这会影响旧版本程序使用加速功能</li> 
 <li>为了能继续维持开发，从此版本开始将会添加程序内广告，赞助用户可以在设置中关闭所有广告</li> 
</ol> 
<h3>版本亮点</h3> 
<ol> 
 <li>新增 Steam 云存档管理功能，可自行上传或删除 Steam 云存档</li> 
 <li>库存游戏支持筛选支持 Steam 云存档的游戏</li> 
 <li>ASF 升级至 V5.2.7.7</li> 
 <li>.NET 运行时升级至 6.0.7，使用 fde 版本需要升级运行时</li> 
 <li>库存游戏中解锁成就与挂时长支持 macOS 与 Linux 系统</li> 
 <li>在设置中可关闭托盘，关闭托盘后关闭主窗口即退出程序</li> 
 <li>使用 Yarp.ReverseProxy 重写了反代加速和脚本功能，大幅提升稳定性与性能</li> 
 <li>Windows 新增 DNS 驱动拦截模式进行本地加速</li> 
 <li>令牌交易现在支持查看交易详情，可以确认交易方的Steam注册时间等信息</li> 
 <li>恢复 Windows x86(32 位) 版本发布</li> 
</ol> 
<h3>修复问题</h3> 
<ol> 
 <li>修复 窗口在某些情况下最大化或最小化恢复时窗口大小会变化的问题</li> 
 <li>修复 库存游戏 编辑 Steam 游戏封面时选择自定义图片失败的问题</li> 
 <li>修复 程序内在显示某些图片时会出现错乱马赛克的问题</li> 
 <li>修复 Linux 上点击关于页面可能因字体引发闪退</li> 
 <li>修复 MIUI Android 11 ~ 12 中绑定或换绑手机号页面闪退</li> 
 <li>修复 Android 本地加速中已知问题弹窗显示时不应同时跳转引导证书页</li> 
 <li>修复 令牌交易确认要求输本地令牌密钥时点击取消也能进行交易确认的问题</li> 
 <li>修复 令牌加载输入密码解密时点击取消或输入错误密码没有移除此前的数据问题</li> 
 <li>修复 2.8.0 中出现因脚本导致的启动加速服务失败</li> 
 <li>修复 网络加速中图标在跟随系统的浅色模式下字体颜色不应为白色</li> 
 <li>修复 系统代理模式与 PAC 代理模式中监听地址为 0.0.0.0 时出现的错误</li> 
 <li>修复 切换页面 UI 布局错乱</li> 
</ol> 
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
   <td>Steam++_win_x64_v2.8.1.7z</td> 
   <td>46F0D1E5F5DFAF114FC80A1060FD11455877B799A38807B1123B1865CFA543DF</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.8.1.7z</td> 
   <td>BB164743905A345FB5BEDF254FE5FE0A44A0309C3B0D51A348358A6143464920</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_v2.8.1.exe</td> 
   <td>363A8948B2B4665FE0777BBE54318BEE16F834BC56BF24A125149B07CD72DF6D</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.8.1.exe</td> 
   <td>3D36B2AC91025D804846C8CECB0D290824B2780D4E5E992361F93EC4FEEEB736</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x86_v2.8.1.7z</td> 
   <td>3B416AEAB2B473372E2B0BFB7B71F04EA92774E314AED848F9C5ABB6F1B85A5B</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x86_fde_v2.8.1.7z</td> 
   <td>FEDCC1A106B1925DF78154192A6499D7C51CB91F14C41C3F7F325C4398BA3E63</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x86_v2.8.1.exe</td> 
   <td>992C8B40E97FD852BFBDBA7FD0F5E677675C19DF64B5BD7108AA394A0DC8337A</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x86_fde_v2.8.1.exe</td> 
   <td>90FB6658721F57234C8D7C1C5852FBB459817696B2C742D15FF87D188C30DDBF</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.8.1.tar.zst</td> 
   <td>67D6889C07AB49D37194C8D6C22761CD1B6FB319CCB79F83847AB8F281F4FCDD</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.8.1.tar.zst</td> 
   <td>4146ABFFD4E6B8A6D47179CBFB7F24C25622B97E751BEBDFB0A6C0F5DF082E14</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.8.1.deb</td> 
   <td>4456A32AEB705B868257DC7DD97D6B194A486C7011ECBE351CD8759DF72E1C35</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.8.1.deb</td> 
   <td>B7C78E180B04763A6768F8F1F57EF164A16687B53068E9A2C6AF5A358F6ADC42</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.8.1.rpm</td> 
   <td>B1FD2FDEFC2837881DF43774F99DC1CB93C8479CF00CDED9DA2E4A9F382B19CF</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.8.1.rpm</td> 
   <td>01A4BB38CD41EE2EB1800EBCA69CFB43B59EF8E1BAF422A488CF9C9EB27ED406</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.8.1.dmg</td> 
   <td>02FEDEEF0DC691A374445E63994CF221FC9B3881F4EA49627FF0C858ACB31EE3</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_arm64_v2.8.1.dmg</td> 
   <td>DA52C130AF85D722528F313BD58C443F564B863BF045A85BD6C5426718AFBC3D</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_android_v2.8.1.apk</td> 
   <td>247C351BA62F8D7C53BB82B49051FDBBFA1018944C2BDD83C076B0973561D352</td> 
  </tr> 
 </tbody> 
</table> 
<p><a href="https://gitee.com/link?target=https%3A%2F%2Fsteampp.net" target="_blank"><img alt="WebSite steampp.net" src="https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/news/203934"><img alt="Steam++ v2.8.1" src="https://img.shields.io/badge/Steam++-v2.8.1-brightgreen.svg?style=flat-square&color=512bd4" referrerpolicy="no-referrer"></a></p> 
<p><a href="https://gitee.com/rmbgame/SteamTools/blob/develop/download-guide.md" target="_blank">不知道该下载哪个文件?</a></p> 
<p>详情查看：<a href="https://gitee.com/rmbgame/SteamTools/releases/2.8.1">https://gitee.com/rmbgame/SteamTools/releases/2.8.1</a></p>
                                        </div>
                                      
</div>
            