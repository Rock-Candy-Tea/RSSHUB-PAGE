
---
title: 'Steam++ 2.6.2 已经发布，Steam 工具箱'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb'
author: 开源中国
comments: false
date: Sat, 11 Dec 2021 16:52:00 GMT
thumbnail: 'https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb'
---

<div>   
<div class="content">
                                                                                            <p>Steam++ 2.6.2 已经发布，Steam 工具箱</p> 
<p>此版本更新内容包括：</p> 
<h3>版本亮点</h3> 
<ol> 
 <li>ASF 升级至 <strong>V5.2.0.10</strong></li> 
 <li>新增 ASF 控制台字体大小、最大行数设置项</li> 
 <li>新增 Steam 下载完成定时关机、睡眠功能</li> 
 <li>新增 代理设置可自定义 DNS</li> 
 <li>新增 ASF 编辑/移除 Bot 功能</li> 
 <li>新增 Microsoft/Xbox 相关加速服务 (需要升级到 <strong>2.6.2</strong> 之后可用)</li> 
 <li>新增 Uplay 相关加速服务 (需要升级到 <strong>2.6.2</strong> 之后可用)</li> 
 <li>新增 OneDrive 等更多相关加速服务 (需要升级到 <strong>2.6.2</strong> 之后可用)</li> 
 <li>优化 Desktop 加速代理性能</li> 
 <li>优化 Desktop 脚本注入打包的性能</li> 
 <li>优化 Desktop 已安装游戏加载性能</li> 
 <li>从此版本开始将使用 Github Action 自动化部署发布</li> 
</ol> 
<h3>修复问题</h3> 
<ol> 
 <li>改进 Desktop 网络加速现默认使用阿里 DNS(223.5.5.5, 223.6.6.6)</li> 
 <li>改进 自动更新包文件校验失败时提示</li> 
 <li>改进 自动更新失败时将自动跳转官网</li> 
 <li>改进 ASF IPC 默认端口号由 1242 改为 6242</li> 
 <li>修复 Linux 与 macOS 中 ASF-UI 解压包文件夹分隔符不正确</li> 
 <li>修复 Windows Hosts 只读时尝试取消只读属性的操作没有正确执行</li> 
 <li>修复 Windows 此软件自动更新删除更新包缓存时因文件占用引发的中断</li> 
 <li>修复 Desktop 高 DPI 下动态桌面错位</li> 
 <li>修复 本地令牌确认交易在登录时可能会卡住</li> 
 <li>修复 Windows 启用动态桌面后全屏可能导致窗口冻结无法操作</li> 
 <li>修复 Windows 动态背景有时会被其他窗口遮挡</li> 
 <li>改进 本地令牌 登录验证码无法加载时可点击在浏览器中查看验证码图片</li> 
 <li>修复 Desktop 加速代理中可能出现的一些错误</li> 
 <li>改进 Desktop 令牌详情 UI</li> 
 <li>改进 Desktop 账号切换中的用户名信息现在默认隐藏</li> 
 <li>改进 Desktop 深色模式与浅色模式的视觉效果</li> 
 <li>修复 Pixiv 加速不能登录的问题</li> 
 <li>修复 Twitch 加速不计算掉宝进度的问题</li> 
 <li>修复 Discord 加速检测更新失败导致无法启动客户端的问题</li> 
 <li>修复 Windows 因添加 JumpList 时可能导致的闪退</li> 
 <li>修复 Desktop 本地令牌 点击锁定后输入密码按回车解锁会循环无限触发锁定的问题</li> 
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
   <td>Steam++_win_x64_v2.6.2.7z</td> 
   <td>E4CB2714EF540816C475DF128FC551D35E94830C452A66748055FFC286BEE7AE</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.6.2.7z</td> 
   <td>43A0BD54B26574C00F62126C080FAA05B1E27BB6A89419168860CF2E1503F627</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_v2.6.2.exe</td> 
   <td>FBB23D4256DD409CEB4D199C04CDC8863CE1173F3AC88E0C7BD9B8778120955C</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.6.2.exe</td> 
   <td>8D2D68EC2FD8036DCD1B283A0EA142FBF877D42A70E3C1AC10A4B4C5F23EAD48</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.6.2.7z</td> 
   <td>DC5EBA3C61E46506C9D8A1C0831E825FBA8EF5D4B0CFA0D7EB5BC44602F46572</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.6.2.7z</td> 
   <td>DAA1B783484FE5AA0F1D1395CC6AEC620A85D485F59A9C06D97A2F646304D34D</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.6.2.deb</td> 
   <td>EE3FCB74B9641C4F6D5A945AC91F0CDD2167A94735F0B7416E2A2397DA255BC4</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.6.2.deb</td> 
   <td>6322EA41DE16A776C30292B529817F87977A27676FBEF38462F4023FAA1E5F42</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.6.2.rpm</td> 
   <td>AD624EBB94CA0562984562734BC803A24550647B4DD69693A1E8079DF86B7378</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.6.2.rpm</td> 
   <td>E326685A891EFD12E1A772B8BDF7EF222F02BE5C420BAC13FD416684C6660979</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.6.2.dmg</td> 
   <td>AD48998969D6324EB1BE878F79DA967C7EAA387DB02B6D75E9D9D23F88A80741</td> 
  </tr> 
 </tbody> 
</table> 
<p><a href="https://gitee.com/link?target=https%3A%2F%2Fsteampp.net" target="_blank"><img alt="WebSite steampp.net" src="https://img.shields.io/badge/WebSite-steampp.net-brightgreen.svg?style=flat-square&color=61dafb" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/news/173192"><img alt="Steam++ v2.6.2" src="https://img.shields.io/badge/Steam++-v2.6.2-brightgreen.svg?style=flat-square&color=512bd4" referrerpolicy="no-referrer"></a></p> 
<p><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FBeyondDimension%2FSteamTools%2Fblob%2Fdevelop%2Fdownload-guide.md" target="_blank">不知道该下载哪个文件?</a></p> 
<p>详情查看：<a href="https://gitee.com/rmbgame/SteamTools/releases/2.6.2">https://gitee.com/rmbgame/SteamTools/releases/2.6.2</a></p>
                                        </div>
                                      
</div>
            