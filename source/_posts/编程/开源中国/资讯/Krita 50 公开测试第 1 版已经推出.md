
---
title: 'Krita 5.0 公开测试第 1 版已经推出'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://krita.org/wp-content/uploads/2021/08/electrichearts_20201224A_kiki_c1_1080P-1024x512.png'
author: 开源中国
comments: false
date: Thu, 19 Aug 2021 03:59:00 GMT
thumbnail: 'https://krita.org/wp-content/uploads/2021/08/electrichearts_20201224A_kiki_c1_1080P-1024x512.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">今天 Krita 开发团队为大家带来了 Krita 5.0 的公开测试第 1 版。Krita 5.0 是一次重大更新版本，它包含了大量新功能和程序功能的变更。</p> 
<div style="text-align:start">
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fwp-content%2Fuploads%2F2021%2F08%2Felectrichearts_20201224A_kiki_c1_1080P.png" target="_blank"><img alt src="https://krita.org/wp-content/uploads/2021/08/electrichearts_20201224A_kiki_c1_1080P-1024x512.png" referrerpolicy="no-referrer"></a> 
 <p style="text-align:center">Krita 5.0 新版启动图，由 Tyson Tan (钛山) 绘制</p> 
</div> 
<h3 style="text-align:start">Krita 5.0 使用前注意事项</h3> 
<ul> 
 <li>Krita 5 完全重写了资源管理系统。Krita 不再需要在每次启动时扫描并加载全部笔刷、图案、渐变和其他资源，而是在首次启动时扫描资源，然后将资源信息写入一个缓存数据库中以便日后直接调用。这意味着 Krita 会在首次启动时耗费较长时间，但日后的启动将明显变快。</li> 
 <li>Krita 5 会为用户编辑的资源保存一组版本历史数据，此功能与 Krita 4 不兼容。如果您升级到了 Krita 5，之后又降级回 Krita 4，将可能造成 Krita 4 显示重复的资源。</li> 
 <li>Krita 5 不再支持加载 Krita 3 和更早版本的矢量图层。</li> 
 <li>Krita 5 创建的 Krita 图像文件 (.kra) 和 Krita 笔刷预设文件 (.kpp) 不能保证与 Krita 4 兼容。</li> 
 <li>Krita 5 修复了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fen%2Fkrita-5-0-release-notes%2F%23text_size_dpi_issue_fix" target="_blank">一个与图像内嵌文字大小有关的程序缺陷</a>，但是打开旧版 Krita 创建的图像时可能需要<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.krita.org%2Fen%2Freference_manual%2Fpreferences%2Fgeneral_settings.html%23miscellaneous" target="_blank">手动更改一处设置</a>才能显示文字的原先大小。</li> 
 <li>Krita 5 的 G’Mic 插件存在一处程序缺陷，执行 G’Mic 滤镜将造成 Krita 设置暂时重置为默认值。此时重新启动 Krita 即可恢复之前设置状态。</li> 
 <li>如果您在使用色彩管理功能并使用了显示器的特性文件，多功能拾色器的三角形区域可能会无法显示。请在菜单栏-设置-色彩管理页面关闭“允许 LittleCMS 优化”，或者在拾色器设置页面改用四方形拾色器形状。</li> 
</ul> 
<h3 style="text-align:start">Krita 5.0 的新功能</h3> 
<p style="text-align:start">Krita 5.0 带来了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fen%2Fkrita-5-0-release-notes%2F" target="_blank">众多新功能</a>，详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fen%2Fkrita-5-0-release-notes%2F" target="_blank">完整发行日志</a> (将在 Krita 5.0 正式版发布时翻译为中文)。下面仅介绍一些比较重要的方面：</p> 
<ul> 
 <li>开发历时 5 年的全新资源管理系统</li> 
 <li>渐变抖动和宽色域渐变</li> 
 <li>通过 LittleCMS fastfloat 插件提高了程序性能</li> 
 <li>新增 MyPaint 笔刷引擎</li> 
 <li>颜色涂抹笔刷引擎完全重写</li> 
 <li>动画时间线面板重新设计</li> 
 <li>动画克隆帧功能</li> 
 <li>动画曲线面板更新</li> 
 <li>动画可使用变形蒙版</li> 
 <li>全新分镜头面板</li> 
 <li>图标设计更新和界面打磨</li> 
 <li>支持 HEIF、AVIF、WebP 图像文件格式</li> 
 <li>TIFF 图像支持改进</li> 
 <li>全新的绘画过程录像工具</li> 
 <li>全新的两点透视辅助尺，以及辅助尺的限制工作区域功能</li> 
 <li>变形工具预览可以按照图层组混合后的效果显示</li> 
 <li>粘贴到当前图层而不是粘贴为新图层功能</li> 
 <li>G’Mic 插件现已支持 macOS</li> 
</ul> 
<p style="text-align:start">对中文用户而言，Krita 5.0 全面改进了中文支持：</p> 
<ul> 
 <li>支持中文标签</li> 
 <li>支持中文资源名称</li> 
 <li>鼠标悬停于资源时显示资源的中文译名</li> 
 <li>所有输入框均可输入中文</li> 
 <li>调整了默认字体，改善可读性</li> 
 <li>之前不显示中文翻译的少数按钮现已全部正常显示中文</li> 
 <li>欢迎画面的新闻板块可以选择显示中文文章</li> 
 <li>帮助菜单的使用手册链接可以自动跳转到中文文档</li> 
 <li>中文文档网站的搜索框可以有限搜索中文关键词</li> 
</ul> 
<p style="text-align:start">除此之外，Krita 5.0 还包括了许多功能和性能方面的小幅改进。在此不再赘述。</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fwp-content%2Fuploads%2F2021%2F08%2Fkrita-style-change.png" target="_blank"><img alt="Krita in the old oxygen style" height="533" src="https://krita.org/wp-content/uploads/2021/08/krita-style-change-1024x533.png" width="1024" referrerpolicy="no-referrer"></a></p> 
<p style="text-align:start">我们希望能在今年 9 月份发布 Krita 5.0 的正式版本，但我们无法确保能按时发布。我们接下来将要继续修复在测试版中发现的问题，尽可能保证 Krita 5.0 正式发布时的可靠性。为了支持 Krita 的开发工作，请在条件允许时考虑向 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffund.krita.org%2F" target="_blank">Krita 发展基金</a>捐款：</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffund.krita.org%2F" target="_blank"><img alt height="346" src="https://krita.org/wp-content/uploads/2021/08/devfund-1024x346.png" width="1024" referrerpolicy="no-referrer"></a></p> 
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
 <li><strong>64 位 Windows 安装程序</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fkrita-x64-5.0.0-beta1-setup.exe" target="_blank">本站下载</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F60HLzj6I" target="_blank">网盘下载</a></li> 
 <li><strong>64 位 Windows 免安装包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fkrita-x64-5.0.0-beta1.zip" target="_blank">本站下载</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F60HLzj6I" target="_blank">网盘下载</a></li> 
 <li><strong>64 位程序崩溃调试包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fkrita-x64-5.0.0-beta1-dbg.zip" target="_blank">本站下载</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F60HLzj6I" target="_blank">网盘下载</a></li> 
</ul> 
<ul> 
 <li><strong>配套网盘资源 (中文社区维护)</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FDea2uj0M" target="_blank">中文离线文档</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F6tH13bVC" target="_blank">FFmpeg 软件包</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FSBopNjOn" target="_blank">G’Mic 滤镜汉化</a> |</li> 
</ul> 
<ul> 
 <li>32 位支持：最后一版支持 32 位 Windows 的 Krita 为 4.4.3，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Fstable%2Fkrita%2F4.4.3%2Fkrita-x86-4.4.3-setup.exe" target="_blank">本站下载</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FwdMnx1WB" target="_blank">网盘下载</a>。</li> 
 <li>免安装包：解压到任意位置，运行目录中的 Krita 快捷方式。不带文件管理器缩略图插件，与已安装版本共用配置文件和资源，但程序本身相互独立。</li> 
 <li>程序崩溃调试包：解压到 Krita 的安装目录，在报告程序崩溃问题时用于获取回溯追踪数据。日常使用无需下载此包。</li> 
</ul> 
<h3 style="text-align:start">Linux 版本</h3> 
<ul> 
 <li><strong>64 位 Linux AppImage 程序包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fkrita-5.0.0-beta1-x86_64.appimage" target="_blank">本站下载</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FC0gZ6joR" target="_blank">网盘下载</a></li> 
 <li>从此版开始，G’Mic 插件已经整合到主程序包中</li> 
 <li>如果浏览器把链接作为文本打开，请右键点击链接另存为文件。</li> 
</ul> 
<h3 style="text-align:start">macOS 版本</h3> 
<ul> 
 <li><strong>macOS 程序映像</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fkrita-5.0.0-beta1.dmg" target="_blank">本站下载</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FgVg0CI53" target="_blank">网盘下载</a></li> 
</ul> 
<ul> 
 <li>如果您还在使用 OSX Sierra 或者 High Sierra，请<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D3py0kgq95Hk" target="_blank">观看此视频</a>了解如何启动由开发人员签名的可执行软件包。</li> 
</ul> 
<h3 style="text-align:start">安卓版本</h3> 
<p style="text-align:start">安卓版本目前尚处于早期测试阶段，整体功能与桌面版本几乎完全相同。它仅为安卓平板和 ChromeBook 类设备进行了初步适配，大部分功能依然需要搭配键盘使用，还有不少功能无法正常工作。</p> 
<ul> 
 <li><strong>64 位 Intel CPU APK 安装包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fkrita-x86_64-5.0.0-beta1-release-signed.apk" target="_blank">本站下载</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FtEkbnO1K" target="_blank">网盘下载</a></li> 
 <li><strong>32 位 Intel CPU APK 安装包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fkrita-x86-5.0.0-beta1-release-signed.apk" target="_blank">本站下载</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FtEkbnO1K" target="_blank">网盘下载</a></li> 
 <li><strong>64 位 ARM CPU APK 安装包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fkrita-arm64-v8a-5.0.0-beta1-release-signed.apk" target="_blank">本站下载</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FtEkbnO1K" target="_blank">网盘下载</a></li> 
 <li><strong>32 位 ARM CPU APK 安装包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fkrita-armeabi-v7a-5.0.0-beta1-release-signed.apk" target="_blank">本站下载</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FtEkbnO1K" target="_blank">网盘下载</a></li> 
</ul> 
<h3 style="text-align:start">源代码</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fkrita-5.0.0-beta1.tar.gz" target="_blank">TAR.GZ 格式源代码包</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fkrita-5.0.0-beta1.tar.xz" target="_blank">TAR.XZ 格式源代码包</a></li> 
</ul> 
<h3 style="text-align:start">md5sum 校验码</h3> 
<p style="text-align:start">适用于上述所有软件包，用于校验下载文件的完整性，不了解文件校验请忽略：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2Fmd5sum.txt" target="_blank">ms5sum 校验码文本文件</a></li> 
</ul> 
<h3 style="text-align:start">文件完整性验证密钥</h3> 
<p style="text-align:start">Linux 的 Appimage 可执行文件包和源代码的 .tar.gz 和 .tar.xz tarballs 压缩包已经经过数字签名。您可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffiles.kde.org%2Fkrita%2F4DA79EDA231C852B" target="_blank">在此下载公钥</a>，还可以在此下载<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.0.0-beta1%2F" target="_blank">数字签名的 SIG 文件</a>。</p> 
<h2 style="text-align:start">请支持 Krita</h2> 
<p style="text-align:start">Krita 是一个自由和开源的软件项目。如果条件允许，请考虑通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffund.krita.org%2F" target="_blank">捐款</a> 或者 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fen%2Fshop%2F" target="_blank">购买培训教程和画册</a> 等方式支持我们的存续和发展，这样我们才能支持开发人员为 Krita 全职工作。</p>
                                        </div>
                                      
</div>
            