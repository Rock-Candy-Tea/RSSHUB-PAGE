
---
title: 'Steam++ 2.6.0 已经发布，Steam 工具箱'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6079'
author: 开源中国
comments: false
date: Wed, 24 Nov 2021 15:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6079'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Steam++ 2.6.0 已经发布，Steam 工具箱</p> 
<p>此版本更新内容包括：</p> 
<h3>新增内容</h3> 
<ol> 
 <li>CLR 更新至 6.0 RTM</li> 
 <li>新增 捐助功能，在关于中可使用 <strong>爱发电</strong>、<strong>Ko-fi</strong>、<strong>Patreon</strong> 平台捐助</li> 
 <li>新增 ASF 本地挂卡功能 (Beta)</li> 
 <li>新增 本地令牌搜索功能</li> 
 <li>新增 库存游戏右键菜单导航到 Steam 客户端</li> 
 <li>新增 Windows 11 上可设置材质 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fwindows%2Fapps%2Fdesign%2Fstyle%2Fmica" target="_blank">云母(Mica)</a></li> 
 <li>新增 搜索框支持拼音搜索</li> 
 <li>新增 框架依赖部署模式(FDE)，可通过共享运行库减少磁盘占用空间，仅支持 Windows 与 Linux</li> 
 <li>新增 Windows 上可将动态壁纸设置为程序背景</li> 
 <li>新增 桌面端 背景材质设置，并修复之前AcrylicBlur透明效果异常问题</li> 
 <li>改进 桌面端 UI 适配 Windows 11 风格</li> 
 <li>改进 Hosts 文件在 Windows 上默认使用 UTF8WithBOM 编码</li> 
 <li>改进 账号注销现需要通过手机号或昵称验证</li> 
 <li>改进 令牌账号加密、导出的界面UI和导入过程中的提示</li> 
 <li>改进 Steam 账号切换支持头像框、等级和游戏中信息的显示</li> 
 <li>改进 文本框窗口弹出时将自动设置焦点</li> 
 <li>改进 Windows 上端口占用提示文本显示占用该端口的进程名</li> 
 <li>改进 Linux 上存储数据遵循 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspecifications.freedesktop.org%2Fbasedir-spec%2Fbasedir-spec-latest.html" target="_blank">XDG Base Directory Specification</a></li> 
 <li>改进 主题切换现在不在需要重启程序，提升主题切换速度</li> 
 <li>改进 本地令牌账号导入过程中的说明提示</li> 
 <li>改进 Windows 上账号切换启动 Steam 时，默认不在以管理员身份启动</li> 
 <li>改进 macOS 上修改 hosts 文件可以不用每次输入密码</li> 
</ol> 
<h3>修复问题</h3> 
<ol> 
 <li>修复 本地令牌 中确认交易时 Http 302 重定向错误</li> 
 <li>修复 Linux 与 macOS 上代理错误</li> 
 <li>修复 库存游戏无限加载</li> 
 <li>修复 脚本未启用时保存状态会全部未启用</li> 
 <li>修复 桌面端 上主题运行时切换与跟随系统</li> 
 <li>修复 Windows 上窗口边缘滚动条难以拖拽</li> 
 <li>修复 本地令牌 确认交易登录时会错误的提示没有开启加速</li> 
 <li>修复 本地令牌 确认交易有时会卡在提示登录中的问题</li> 
 <li>修复 Windows 上资源管理器重启后托盘消失，以及尝试修复开机自启时有时不显示托盘</li> 
 <li>修复 桌面端 上导航栏的弹出菜单失去焦点时不会自动隐藏的问题</li> 
</ol> 
<h3>已知问题</h3> 
<ul> 
 <li>Desktop 
  <ul> 
   <li>macOS 
    <ul> 
     <li>尚未公证，这会影响 macOS Catalina（版本 10.15）以上</li> 
     <li>自动更新不可用</li> 
    </ul> </li> 
   <li>Linux 
    <ul> 
     <li>在 Deepin 中托盘不生效，可通过 <code>Exit.sh</code> 退出程序</li> 
     <li>窗口弹出位置不正确</li> 
     <li>自动更新不可用</li> 
     <li>鼠标指针浮动样式不正确</li> 
    </ul> </li> 
   <li>Windows 
    <ul> 
     <li>在 CPU 不受支持的 Win11 上无法启动，Windows 日志中显示 <code>Failed to create CoreCLR, HRESULT: 0x80004005</code> 
      <ul> 
       <li>仅 .NET 6.0 受此影响，在几周后的 Insider 中会修复，见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Fissues%2F6733" target="_blank">issue</a></li> 
       <li><strong>解决方案：</strong> 可尝试使用早期版本，例如 v2.3.0</li> 
      </ul> </li> 
    </ul> </li> 
   <li>Shared 
    <ul> 
     <li>拼音搜索不能正确的识别多音字</li> 
    </ul> </li> 
  </ul> </li> 
 <li>Mobile 
  <ul> 
   <li>Android 
    <ul> 
     <li>确认交易列表刷新后数据有时会显示不正确</li> 
     <li>自动更新暂不可用</li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h2><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSteamTools-Team%2FSteamTools%2Fblob%2Fdevelop%2Fdownload-guide.md" target="_blank">下载指南</a></h2> 
<table> 
 <thead> 
  <tr> 
   <th>File</th> 
   <th>Checksum (SHA256)</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>Steam++_win_x64_v2.6.0.7z</td> 
   <td>c88b2b6a8ecfcc244685d57207bc7f20458172f4b48652cc9ffac4f09e6dd427</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.6.0.7z</td> 
   <td>b716b20b99bcddc96efbdb6bbdfc1e9f1da61c6cf96969846947f2ec95442fd4</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_v2.6.0.exe</td> 
   <td>21456a847e0d74c78d3ca03ad668f24521f891fcf3aec66536e66ce810c5d002</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_fde_v2.6.0.exe</td> 
   <td>479d9f24f8b1a033b2cc954c8a05301fceecbff24ff19abf040d75932b862771</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.6.0.7z</td> 
   <td>a9a5a92c9629a49caea457aea0ae5d9c68c0d13397cfccca24d8c51549be219c</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.6.0.7z</td> 
   <td>adc21ad1574af783aeeeeee8c3c8ffa134d8fc580b5407caf0a934ea5f362948</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm_v2.6.0.7z</td> 
   <td>e6ecae858c9fcd73770cc6a492f17cdc3caa5317064222fdcf3fc7bdff1a4f8b</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_fde_v2.6.0.7z</td> 
   <td>b3b1af30d31b85716ed5496a7dbc78a4b5407f24e7711e9ff3a028748b928fb5</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_fde_v2.6.0.7z</td> 
   <td>828f998b431ba7949adc3ec9fdbd4ef35c3baff18a5b17271cf5f63dd9e14629</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm_fde_v2.6.0.7z</td> 
   <td>a7c97b91dacb7ed7959b7be6c9e48b86e20974f96b0571a1835381cab8fe68bf</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.6.0.deb</td> 
   <td>43cc3440d08a0fc67867b17c1af48e84f878cc0c4021a14e5c7f6f1d52733681</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.6.0.deb</td> 
   <td>a62b4d8ad3606d41c239523db92b5ca0376fa5ef988a2180e186426b0480084c</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm_v2.6.0.deb</td> 
   <td>20edc52411217d097e3a725cb30d0621f7518e4b4a2395909cc063e15f456d65</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_fde_v2.6.0.deb</td> 
   <td>3154415944314c6c8c20f72c1364d0aa89b030548f396a50430841f5404920e0</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_fde_v2.6.0.deb</td> 
   <td>0d31ea4232343769c0afadf0930aa6df59aa021e4764fbc9a97298637012ea86</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm_fde_v2.6.0.deb</td> 
   <td>deb78353606819ea2d3349a36dfebed149da9b0d3e94f441652dcd23d331f41f</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.6.0.rpm</td> 
   <td>8070a1be891bc9af46cf5e569dfdaab724d8185e835260800695e4735e6b3b18</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_v2.6.0.rpm</td> 
   <td>759afb42bdae7149671d0f70a2b065d33a7e452cd8539d675784c16f3036caac</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm_v2.6.0.rpm</td> 
   <td>e04d499838684fa1c88f752c0343ff721b437432bffa14d3900c1e5d7f34e406</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_fde_v2.6.0.rpm</td> 
   <td>fb1f60171b70c5d937420b14d3ca3eda9e17e904af9a67f02d8ca5d2d6e1c9c4</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm64_fde_v2.6.0.rpm</td> 
   <td>184e4f1a92d633eb6530bab0b4b9d7e8183f32ef77d9581b3c28e0d86319d8ae</td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_arm_fde_v2.6.0.rpm</td> 
   <td>4a9e6536e57c0f4a585c2834488b36aaa348a79e4c642825bf9d831d74e87cd4</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.6.0.dmg</td> 
   <td>3a8453393e79eb90953482b359758f366d32432a0c83aa9aeb1f979962050a1a</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_arm64_v2.6.0.dmg</td> 
   <td>59aeab8d5b57234ecdc651004b2fcffa220a8b21825bd5f8fa102b0fcd567caf</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.6.0.7z</td> 
   <td>683adf6269175b24a3d29f087b98488dd44b3f06a1ae3770345c3d70f5a3d442</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_arm64_v2.6.0.7z</td> 
   <td>29a4ad9bf29452157aa141d97e8cb7859bdb1fc16f40ba0f4091dcb4753a862b</td> 
  </tr> 
 </tbody> 
</table> 
<p>详情查看：<a href="https://gitee.com/rmbgame/SteamTools/releases/2.6.0">https://gitee.com/rmbgame/SteamTools/releases/2.6.0</a></p>
                                        </div>
                                      
</div>
            