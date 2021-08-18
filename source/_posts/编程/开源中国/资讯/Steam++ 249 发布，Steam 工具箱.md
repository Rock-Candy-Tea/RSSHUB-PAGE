
---
title: 'Steam++ 2.4.9 发布，Steam 工具箱'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3108'
author: 开源中国
comments: false
date: Wed, 18 Aug 2021 12:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3108'
---

<div>   
<div class="content">
                                                                                            <p>Steam++ 2.4.9 已经发布，Steam 工具箱。</p> 
<p>此版本更新内容包括：</p> 
<h3>新增内容</h3> 
<ol> 
 <li>CLR 升级至 .NET 6 Preview 7</li> 
 <li>新增 库存游戏可浏览已安装的游戏文件夹</li> 
 <li>新增 创意工坊划词翻译脚本</li> 
 <li>新增 通用设置-使用硬件加速设置项，也可通过命令行参数禁用硬件加速启动 -clt devtools -disable_gpu</li> 
 <li>新增 账号切换内新增家庭库共享排序功能，该功能可调整当前设备的多个家庭共享账号库存的优先级顺序。</li> 
 <li>新增 QQ 快速登录渠道</li> 
 <li>新增 意大利语支持</li> 
 <li>新增 西班牙语支持</li> 
 <li>新增 通用设置内可支持访问程序的 AppData、Cache、Logs 文件夹和查看缓存及日志占用空间大小情况</li> 
 <li>新增 本地令牌可以查看令牌二维码导入到移动端</li> 
 <li>Android/macOS/Linux 版现已开启 Beta/Alpha 测试，可从 GitHub/Gitee 上下载</li> 
</ol> 
<h3>修复问题</h3> 
<ol> 
 <li>修复 开机自启动在 2.4.x 中不生效</li> 
 <li>改进 深色和浅色模式的视觉效果</li> 
 <li>改进 社区加速计时逻辑</li> 
 <li>更正 导出令牌窗口标题文本错误</li> 
 <li>改进 添加令牌弹窗可调整窗口大小</li> 
 <li>改进 本地令牌自定义修改名称操作</li> 
 <li>修复 我的面板中出现垂直滚动条</li> 
 <li>改进 解锁成就风险提示弹窗可以设置不再提示</li> 
 <li>修复 任务栏位于顶部时托盘菜单位置不正确</li> 
 <li>修复 挂时长运行中列表移除游戏时引发的闪退</li> 
 <li>改进 自动更新机制</li> 
 <li>改进 开机自启动现仅对当前用户生效</li> 
 <li>改进 第三方账号快速登录，现使用系统浏览器进行快速登录</li> 
 <li>改进 现已编译为 ReadyToRun (R2R) 格式，这将改进应用程序的启动时间和延迟（仅 Windows 版）</li> 
 <li>修复 库存游戏中部分游戏被错误屏蔽没有加载</li> 
 <li>改进 部分语言的翻译文本</li> 
 <li>改进 本地令牌上移下移功能顺序错乱问题</li> 
 <li>修复 程序在加载库存游戏时有概率闪退的问题</li> 
 <li>修复 打开托盘菜单有概率导致程序闪退的问题</li> 
 <li>修复 程序启动时界面不会加载任何内容无法正常使用的问题</li> 
 <li>改进 账号切换功能 UI</li> 
 <li>改进 移除了 CEF 模块，缩减程序体积和运行时内存占用</li> 
 <li>改进 库存游戏支持显示已安装游戏占用空间大小</li> 
 <li>改进 库存游戏封面大小调节可支持滚动调节</li> 
 <li>改进 hosts 文件编码在 Windows 上使用系统的活动代码页(ANSICodePage)，例如 GB2312/936，其他操作系统则使用 UTF-8，还原 V1 版本行为</li> 
 <li>改进 开始菜单磁贴背景由黑色更改为透明</li> 
 <li>修复 账号切换修改账号备注重启后被还原</li> 
</ol> 
<h3>已知问题</h3> 
<ul> 
 <li>macOS 
  <ul> 
   <li>尚未公证，这会影响 macOS Catalina（版本 10.15）以上</li> 
   <li>自动更新不可用</li> 
  </ul> </li> 
 <li>Linux 
  <ul> 
   <li>托盘不生效，这将影响程序不能正常退出</li> 
   <li>窗口弹出位置不正确</li> 
   <li>自动更新不可用</li> 
  </ul> </li> 
 <li>Android 
  <ul> 
   <li>扫码导入暂不可用</li> 
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
 </tbody> 
</table> 
<table> 
 <thead> 
  <tr> 
   <th>File</th> 
   <th>Checksum (SHA256)</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>Steam++_win_x64_v2.4.9.7z</td> 
   <td>D8620FF0F46BA3D10701309F13AE0FFF857E2E122FA9D1DB0D305D2CF76EAE44</td> 
  </tr> 
  <tr> 
   <td>Steam++_win_x64_v2.4.9.exe</td> 
   <td>05B032574F61B2E16E6A0EF74D7EC9BBE6880AE7B7496E8097DB88D2BEAB7B45</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_linux_x64_v2.4.9.7z</td> 
   <td>E056112C66E92D49A69DB3AD58B8B48822E6A5C72DA0A0F6D602C157C1605B4E</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.4.9.7z</td> 
   <td>608BCC6305A867EF3EFC3444E32E1A35CD523DD08C3ACFBED30F6E66A758EE4C</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.4.9.dmg</td> 
   <td>927F495DCBA6380475568428F650FBC69A7AE390F06E0CD9305B38E98C13E568</td> 
  </tr> 
  <tr> 
   <td>Steam++_macos_x64_v2.4.9.app.zip</td> 
   <td>B19009C763E5168CEC40D28CC93418F621D30C1F013609C0D7F6B4012B24C8AE</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Steam++_android_arm64_v8a_v2.4.9.apk</td> 
   <td>2EAE8803C14DB38E1E2C68B44647F7A35F8F0AFE45CF9727A3DAEBD5DD4630A2</td> 
  </tr> 
  <tr> 
   <td>Steam++_android_armeabi_v7a_v2.4.9.apk</td> 
   <td>26206AD0B904B45616C0E3263594AE6A846C222E9AEC71C2151A83E0DDC7F7E2</td> 
  </tr> 
 </tbody> 
</table> 
<p>详情查看：<a href="https://gitee.com/rmbgame/SteamTools/releases/2.4.9">https://gitee.com/rmbgame/SteamTools/releases/2.4.9</a></p>
                                        </div>
                                      
</div>
            