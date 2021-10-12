
---
title: 'Krita 5.0 公开测试第 2 版已经推出'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://krita.org/wp-content/uploads/2021/08/electrichearts_20201224A_kiki_c1_1080P-1024x512.png'
author: 开源中国
comments: false
date: Mon, 11 Oct 2021 20:52:00 GMT
thumbnail: 'https://krita.org/wp-content/uploads/2021/08/electrichearts_20201224A_kiki_c1_1080P-1024x512.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">2021年10月11日 Krita 5.0 的第二个公开测试版正式发布。此次发布比原计划的要晚，原因是因为一些开发人员在长达一年半的隔离解封后迫不及待地线下碰头，却不小心得了重感冒。</p> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">Krita 公开测试第 2 版与第 1 版一样存在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fzh%2Fitem%2Ffirst-beta-for-krita-5-0-released-zh%2F" target="_blank">一些需要旧版用户注意的事项</a>，请在充分了解情况后才进行使用。</p> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">公开测试第 2 版在第 1 版的基础上修复了超过 700 项程序缺陷。现在我们至少还需要解决<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fbuglist.cgi%3Fbug_severity%3Dcritical%26bug_severity%3Dgrave%26bug_severity%3Dmajor%26bug_severity%3Dcrash%26bug_severity%3Dnormal%26bug_severity%3Dminor%26bug_status%3DUNCONFIRMED%26bug_status%3DCONFIRMED%26bug_status%3DASSIGNED%26bug_status%3DREOPENED%26keywords%3Dregression%252C%2520release_blocker%252C%2520%26keywords_type%3Danywords%26list_id%3D1918546%26product%3Dkrita%26query_format%3Dadvanced" target="_blank">这些程序缺陷</a>后才能正式发布 Krita 5.0。此版软件还包含了重构的 GPU 加速画布程序，大幅改善了在 HiDPI 和 macOS 环境下的性能。</p> 
<div style="text-align:start">
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fwp-content%2Fuploads%2F2021%2F08%2Felectrichearts_20201224A_kiki_c1_1080P.png" target="_blank"><img alt height="512" src="https://krita.org/wp-content/uploads/2021/08/electrichearts_20201224A_kiki_c1_1080P-1024x512.png" width="1024" referrerpolicy="no-referrer"></a> 
 <p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:center">Tyson Tan (钛山) 绘制的新版启动图</p> 
</div> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">下面是自公开测试第 1 版以来的比较值得一提的更新：</p> 
<ul> 
 <li>Dmitry Kazakov 和 Ivan Yossi 实现了一套上传纹理到 GPU 的新方案，改善了画布性能，尤其是 macOS 下的性能。</li> 
 <li>Michał Chojnowski 修复了色域蒙版工具栏的一处崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441122" target="_blank">BUG:441122</a>)</li> 
 <li>Alvin Wong 大幅改善了 Krita 的可翻译性，并对繁体中文的翻译进行了大量改进。</li> 
 <li>Tyson Tan 也大幅改善了 Krita 的可翻译性，并对简体中文的翻译进行了大量改进。</li> 
 <li>Amyspark 修复了一个在使用 G’Mic-Qt 插件时会造成设置重置的程序缺陷。G’Mic 也已经更新到了最新版本。</li> 
 <li>Deif Lou 修复了滤镜笔刷引擎中存在的数个问题。</li> 
 <li>Amyspark 重构了图层元数据框架 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D410341" target="_blank">BUG:410341</a>)</li> 
 <li>Agata Cacko 修复了颜色历史按钮布局 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D434915" target="_blank">BUG:434915</a>)</li> 
 <li>Alan North 修复了笔刷编辑器中调整共享曲线时会发生的问题。</li> 
 <li>Agata Cacko 改进了 Adobe 样式库文件支持，现在可以加载唯一 ID 冲突的 ASL 文件。</li> 
 <li>Alvin Wong 修复了画布浮动缩放水平消息的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D429569" target="_blank">BUG:429569</a>)</li> 
 <li>Tom Tom Tom 修复了西文书法工具中的一处程序缺陷</li> 
 <li>Eoin O’Neill 修复了分镜头脚本面板中的一处崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441592" target="_blank">BUG:441592</a>)</li> 
 <li>Emmet O’Neill 改进了分镜头脚本面板的易用性 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441593" target="_blank">BUG:441593</a>)</li> 
 <li>Sharaf Zaman 修复了安卓/ChromeOS 版的欢迎页面。</li> 
 <li>Matthias Wein 修复了面板标题栏的数个问题。</li> 
 <li>Alvin Wong 修复了 Windows 版显示弹窗时的一些问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441935" target="_blank">BUG:441935</a>)</li> 
 <li>Alvin Wong 修复了触控平移手势在移动太快时会出错的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441706" target="_blank">BUG:441706</a>)</li> 
 <li>Wolthera van Hövell tot Westerflier 修复了使用 Lab 色彩空间定义的 KPL 色板的加载失败问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441139" target="_blank">BUG:441139</a>)</li> 
 <li>Alvin Wong 修复了导航器面板的一处性能问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D442075" target="_blank">BUG:442075</a>)</li> 
 <li>Wolthera van Hövell tot Westerflier 修复了通道面板的一处崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D442117" target="_blank">BUG:442117</a>)</li> 
 <li>Matthias Wein 修复了通道面板的一处性能问题</li> 
 <li>Alvin Wong 改进了 Krita 在多文档模式下的易用性 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441644" target="_blank">BUG:441644</a>)</li> 
 <li>Halla Rempt 修复了操作流程面板在执行已禁用操作时的崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441638" target="_blank">BUG:441638</a>)</li> 
 <li>Halla Rempt 修复了 Qt 字体数据库在字体名称中角括号中间存在空格时导致解析器出错的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D430220" target="_blank">BUG:430220</a>)</li> 
 <li>Agata Cacko 修复了多种辅助尺形状的预览问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441212" target="_blank">BUG:441212</a>)</li> 
 <li>Alvin Wong 修复了在使用 Windows Ink 或 Wintab 时某些驱动程序会重复发送数位板事件，从而激活一个鼠标事件的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441687" target="_blank">BUG:441687</a>)</li> 
 <li>Matthias Weind 修复了一个会导致新图像尺寸计算错误的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D442124" target="_blank">BUG:442124</a>)</li> 
 <li>Sharaf Zaman 修复了安卓版的增量备份保存功能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D427042" target="_blank">BUG:427042</a>)</li> 
 <li>Halla Rempt 修复了系统日志的滚动更新功能</li> 
 <li>Halla Rempt 将默认撤销次数从 30 改为 200</li> 
 <li>Agata Cacko 修复了渐变编辑后预览的更新问题</li> 
 <li>Amyspark 修复了LittleCMS 的 32 位浮点 RGB (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D442004" target="_blank">BUG:442004</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D439947" target="_blank">BUG:439947</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D437429" target="_blank">BUG:437429</a>)</li> 
 <li>Wolthera van Hövell tot Westerflier 修复了透明度通道分离到单独图层功能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D434288" target="_blank">BUG:434288</a>)</li> 
 <li>Halla Rempt 为创建矢量图层新增了一个默认快捷键：CTRL+Insert (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D442585" target="_blank">BUG:442585</a>)</li> 
 <li>Wolthera van Hövell tot Westerflier 实现了在作为 Krita 图像编辑笔刷时加载 GIMP 笔刷或 GIMP 图像水管笔刷作为彩色图像，并修复了这类笔刷的保存问题  (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D442316" target="_blank">BUG:442316</a>)</li> 
 <li>Wolthera van Hövell tot Westerflier 为自动笔刷空间增加了一个重置选项 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D437006" target="_blank">BUG:437006</a>)</li> 
 <li>Halla Rempt 修复了快捷键定义文件遗失，造成菜单项显示为空白的程序缺陷 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D428453" target="_blank">BUG:428453</a>)</li> 
 <li>Eoin O’Neill 为分镜头脚本面板编写了全新的导出界面。</li> 
 <li>Eoin O’Neill 修复了在动画蒙版上使用移动工具时的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441974" target="_blank">BUG:441974</a>)</li> 
 <li>Eoin O’Neill 修复了裁剪工具在克隆的动画帧中不正常工作的程序缺陷 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441369" target="_blank">BUG:441369</a>)</li> 
 <li>Wolthera van Hövell tot Westerflier 改进了时间轴面板，现在可以对蒙版分配色标并固定到时间轴面板 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D438124" target="_blank">BUG:438124</a>)</li> 
 <li>Wolthera van Hövell tot Westerflier 修复了操作流程面板的外观问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D442185" target="_blank">BUG:442185</a>)</li> 
 <li>Alvin Wong 修复了非正数倍显示缩放倍率的一系列问题</li> 
 <li>Sharaf Zaman 修复了安卓版更改光标图标时的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D431859" target="_blank">BUG:431859</a>)</li> 
 <li>Reinold Rojas 为拾色器工具启用了颜色采样预览功能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D396490" target="_blank">BUG:396490</a>)</li> 
 <li>Reinold Rojas 修复了隐藏面板模式的全屏状态问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D437932" target="_blank">BUG:437932</a>)</li> 
 <li>Halla Rempt 为变形工具新增了一个工具预览选项，方便用户在快速预览和图层混合模式之间切换。</li> 
 <li>Black Cat 修复了在文字工具中应用字体风格的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D392343" target="_blank">BUG:392343</a>)</li> 
 <li>Agata Cacko 修复了局部辅助尺的预览问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D442619" target="_blank">BUG:442619</a>)</li> 
 <li>Wolthera van Hövell tot Westerflier 修复了裁剪工具的一系列文问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D442827" target="_blank">BUG:442827</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D442959" target="_blank">BUG:442959</a>)</li> 
 <li>Wolthera van Hövell tot Westerflier 修复了合并克隆阵列的问题，现在合并后的图层能处在正确的位置 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D437431" target="_blank">BUG:437431</a>)</li> 
 <li>Wolthera van Hövell tot Westerflier 修复了颜色调整滤镜蒙版的一处可能的崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D428349" target="_blank">BUG:428349</a>)</li> 
 <li>Agata Cacko 修复了创建资源包时的渐变预览图</li> 
 <li>Agata Cacko 修复了资源标签系统中的一系列问题</li> 
 <li>Dmitry Kazakov 改进了蒙版笔刷的性能</li> 
 <li>Halla Rempt 实现了用户定义标签的保存功能</li> 
 <li>Dmitry Kazakov 改进了当前笔尖非常大时起笔时的性能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D436731" target="_blank">BUG:436731</a>)</li> 
 <li>Sharaf Zaman 改进了安卓或 ChromeOS 下文字工具的易用性。</li> 
 <li>Dmitry Kazakov 修复了属于一个已变形图层组中的形状更新 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D443161" target="_blank">BUG:443161</a>)</li> 
 <li>Dmitry Kazakov 修复了四方连续模式下的画布更新 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D442796" target="_blank">BUG:442796</a>)</li> 
 <li>Dmitry Kazakov 修复了颜色涂抹笔刷引擎的色相感应程序造成的杂色 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D441755" target="_blank">BUG:441755</a>)</li> 
 <li>Matthias Wein 修复了创建新图像对话框的一处内存泄漏问题</li> 
 <li>Halla Rempt 修复了通知程序脚本类的一个初始化问题</li> 
 <li>Agata Cacko 改进了透视辅助尺的性能</li> 
</ul> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">我们将继续修复在公开测试版和每日构建版中发现的问题，以确保在发布 Krita 5.0 正式版时程序的可靠性。</p> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">如果条件允许，请考虑通过<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffund.krita.org%2F" target="_blank">Krita 开发基金</a>支持我们的工作：</p> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffund.krita.org%2F" target="_blank"><img alt height="346" src="https://krita.org/wp-content/uploads/2021/08/devfund-1024x346.png" width="1024" referrerpolicy="no-referrer"></a></p> 
<h2 style="text-align:start">下载</h2> 
<h3 style="text-align:start">中文版信息</h3> 
<ul> 
 <li>中文支持：Krita 的所有软件包均内建中文支持，首次安装时会自动设置为操作系统的语言。</li> 
 <li>手动设置：菜单栏 –> Settings –> Switch Application Language (倒数第二项) –> 下拉选单 –> 中文 (底部)，重启程序生效。</li> 
 <li>插件翻译：G’MIC 插件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FSBopNjOn" target="_blank">需要下载翻译包</a></li> 
 <li>网盘下载：请在官网下载困难时使用，更新时间可能滞后。</li> 
</ul> 
<h3 style="text-align:start">Windows 版本</h3> 
<ul> 
 <li><strong>64 位 Windows 安装程序</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fkrita-x64-5.0.0-beta2-setup.exe" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F60HLzj6I" target="_blank">网盘下载</a></li> 
 <li><strong>64 位 Windows 免安装包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fkrita-x64-5.0.0-beta2.zip" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F60HLzj6I" target="_blank">网盘下载</a></li> 
 <li><strong>64 位程序崩溃调试包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fkrita-x64-5.0.0-beta2-dbg.zip" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F60HLzj6I" target="_blank">网盘下载</a></li> 
</ul> 
<ul> 
 <li><strong>配套网盘资源 (中文社区维护)</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FDea2uj0M" target="_blank">中文离线文档</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F6tH13bVC" target="_blank">FFmpeg 软件包</a> |<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FSBopNjOn" target="_blank">G’Mic 滤镜汉化</a><span> </span>|</li> 
</ul> 
<ul> 
 <li>32 位支持：最后一版支持 32 位 Windows 的 Krita 为 4.4.3，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Fstable%2Fkrita%2F4.4.3%2Fkrita-x86-4.4.3-setup.exe" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FwdMnx1WB" target="_blank">网盘下载</a>。</li> 
 <li>免安装包：解压到任意位置，运行目录中的 Krita 快捷方式。不带文件管理器缩略图插件，与已安装版本共用配置文件和资源，但程序本身相互独立。</li> 
 <li>程序崩溃调试包：解压到 Krita 的安装目录，在报告程序崩溃问题时用于获取回溯追踪数据。日常使用无需下载此包。</li> 
</ul> 
<h3 style="text-align:start">Linux 版本</h3> 
<ul> 
 <li><strong>64 位 Linux AppImage 程序包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fkrita-5.0.0-beta2-x86_64.appimage" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FC0gZ6joR" target="_blank">网盘下载</a></li> 
 <li>从此版开始，G’Mic 插件已经整合到主程序包中</li> 
 <li>如果浏览器把链接作为文本打开，请右键点击链接另存为文件。</li> 
</ul> 
<h3 style="text-align:start">macOS 版本</h3> 
<ul> 
 <li><strong>macOS 程序映像</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fkrita-5.0.0-beta2.dmg" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FgVg0CI53" target="_blank">网盘下载</a></li> 
</ul> 
<ul> 
 <li>如果您还在使用 OSX Sierra 或者 High Sierra，请<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D3py0kgq95Hk" target="_blank">观看此视频</a>了解如何启动由开发人员签名的可执行软件包。</li> 
</ul> 
<h3 style="text-align:start">安卓版本</h3> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">安卓版本目前尚处于早期测试阶段，整体功能与桌面版本几乎完全相同。它仅为安卓平板和 ChromeBook 类设备进行了初步适配，大部分功能依然需要搭配键盘使用，还有不少功能无法正常工作。</p> 
<ul> 
 <li><strong>64 位 Intel CPU APK 安装包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fkrita-x86_64-5.0.0-beta2-release-signed.apk" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FAKSomiNJ" target="_blank">网盘下载</a></li> 
 <li><strong>32 位 Intel CPU APK 安装包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fkrita-x86-5.0.0-beta2-release-signed.apk" target="_blank">本站下载</a> |<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FAKSomiNJ" target="_blank">网盘下载</a></li> 
 <li><strong>64 位 ARM CPU APK 安装包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fkrita-arm64-v8a-5.0.0-beta2-release-signed.apk" target="_blank">本站下载</a> |<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FGCKrtN0F" target="_blank">网盘下载</a></li> 
 <li><strong>32 位 ARM CPU APK 安装包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fkrita-armeabi-v7a-5.0.0-beta2-release-signed.apk" target="_blank">本站下载</a> |<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FGCKrtN0F" target="_blank">网盘下载</a></li> 
</ul> 
<h3 style="text-align:start">源代码</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fkrita-5.0.0-beta2.tar.gz" target="_blank">TAR.GZ 格式源代码包</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fkrita-5.0.0-beta2.tar.xz" target="_blank">TAR.XZ 格式源代码包</a></li> 
</ul> 
<h3 style="text-align:start">md5sum 校验码</h3> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">适用于上述所有软件包，用于校验下载文件的完整性，不了解文件校验请忽略：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2Fmd5sum.txt" target="_blank">ms5sum 校验码文本文件</a></li> 
</ul> 
<h3 style="text-align:start">文件完整性验证密钥</h3> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">Linux 的 Appimage 可执行文件包和源代码的 .tar.gz 和 .tar.xz tarballs 压缩包已经经过数字签名。您可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffiles.kde.org%2Fkrita%2F4DA79EDA231C852B" target="_blank">在此下载公钥</a>，还可以在此下载<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta2%2F" target="_blank">数字签名的 SIG 文件</a>。</p> 
<h2 style="text-align:start">请支持 Krita</h2> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">Krita 是一个自由和开源的软件项目。如果条件允许，请考虑通过<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffund.krita.org%2F" target="_blank">捐款</a><span> </span>或者<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fen%2Fshop%2F" target="_blank">购买培训教程和画册</a><span> </span>等方式支持我们的存续和发展，这样我们才能支持开发人员为 Krita 全职工作。</p>
                                        </div>
                                      
</div>
            