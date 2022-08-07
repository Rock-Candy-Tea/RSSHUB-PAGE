
---
title: 'Krita 5.1.0 发布候补第 1 版已经推出'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7310'
author: 开源中国
comments: false
date: Sat, 06 Aug 2022 23:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7310'
---

<div>   
<div class="content">
                                                                                            <p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">8月4日krita开发团队为大家带来了 Krita 5.1.0 的第一个发布候补版。</p> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">完整的更新内容请见 Krita 5.1 系列版本说明 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fzh%2Fkrita-5-1-release-notes-zh%2F" target="_blank">中文</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fen%2Fkrita-5-1-release-notes%2F" target="_blank">英文</a>) (尚在编写中)。</p> 
<h2 style="text-align:start">已知问题</h2> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">请注意：先前发布的 Krita 5.1 的公开测试第 1 版存在一个程序缺陷，它会造成笔刷预设的保存异常。其他版本的 Krita 在加载受影响的笔刷预设时将会崩溃。如果您遇到了此问题，请使用此<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Ftymond%2Fbrushes-metadata-fixer" target="_blank">Python 脚本</a>来修复有问题的笔刷预设。</p> 
<h2 style="text-align:start">新增程序缺陷修复</h2> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">Krita 5.1 发布候补第 1 版在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fzh%2Fitem%2Fkrita-5-1-beta-2-zh%2F" target="_blank">公开测试第 2 版</a>的基础上又修复了以下程序缺陷：</p> 
<ul> 
 <li>修复了重命名资源的已有标签和系统标签时的一些问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D453831" target="_blank">BUG:453831</a></li> 
 <li>Python 脚本编程：现在程序能够获取所有图案资源了。</li> 
 <li>修复了在笔刷预设编辑器中将动态传感器绑定到旋转选项时的拖慢现象。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D456668" target="_blank">BUG:456668</a></li> 
 <li>修复了显示器缩放情景下的色彩空间浏览器的界面缩放。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D456929" target="_blank">BUG:456929</a></li> 
 <li>修复了分镜头脚本面板的一处内存泄漏。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D456998" target="_blank">BUG:456998</a></li> 
 <li>修复了图块引擎中的一处内存泄漏。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D457998" target="_blank">BUG:456998</a></li> 
 <li>将半调滤镜的默认图案生成器设为透明度模式。</li> 
 <li>改进了动画在仅导出帧或者仅导出视频之间切换时的处理方式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D443105" target="_blank">BUG:443105</a></li> 
 <li>在导出动画到帧被取消后清除生成的文件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D443105" target="_blank">BUG:443105</a></li> 
 <li>修复了 SVG 矢量图形功能中将椭圆转换为贝塞尔曲线时会造成 Krita 耗尽内存的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D456922" target="_blank">BUG:456922</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D439145" target="_blank">BUG:439145</a></li> 
 <li>修复了处理矢量对象的渐变填充时的处理问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D456807" target="_blank">BUG:456807</a></li> 
 <li>确保 MIME 类型选择器的确定和取消按钮能被正确翻译。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D448343" target="_blank">BUG:448343</a></li> 
 <li>修复了在通过 Python 脚本编程 API 进行图像克隆时的崩溃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D457080" target="_blank">BUG:457080</a></li> 
 <li>当创建已有图像的副本时重置文件路径。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D457081" target="_blank">BUG:457081</a></li> 
 <li>修复了复制粘贴一个带有矢量图层的图层组时的崩溃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D457154" target="_blank">BUG:457154</a></li> 
 <li>修复了带有文字对象的图像为 PSD。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D455988" target="_blank">BUG:455988</a></li> 
 <li>修复了在撤销创建文字形状时的崩溃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D457125" target="_blank">BUG:457125</a></li> 
 <li>修复了在为带有内嵌资源的 PSD 文件加载缩略图时的崩溃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D456123" target="_blank">BUG:457123</a></li> 
 <li>改进了最近图像列表在从 PSD 文件创建缩略图时的性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D456907" target="_blank">BUG:456907</a></li> 
 <li>修复了加载带有内嵌图案的 PSD 文件。</li> 
 <li>修复了撤销删除标签的功能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D440337" target="_blank">BUG:440337</a></li> 
 <li>支持打开某些无效的 PSD 文件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D444844" target="_blank">BUG:444844</a></li> 
 <li>修复了在从 G’Mic 插件返回时的图层位置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D456950" target="_blank">BUG:456950</a></li> 
 <li>修复了加载由 Substance Designer 创建的 JPEG-XL文件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D456738" target="_blank">BUG:456738</a></li> 
 <li>修复了拾色器工具的工具选项中的透明度通道的显示。</li> 
 <li>修复了剪贴板中图像损坏时的崩溃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D456778" target="_blank">BUG:456778</a></li> 
 <li>修复了粘贴多张参考图像时的位置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D456382" target="_blank">BUG:456382</a></li> 
 <li>修复了在使用相连选区工具时对双击过快的处理。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D450577" target="_blank">BUG:450577</a></li> 
 <li>修复了在使用拾色器拾取颜色时对当前色板的更新。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D455203" target="_blank">BUG:455203</a></li> 
 <li>改进了笔刷速度传感器的计算。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D453401" target="_blank">BUG:453401</a></li> 
</ul> 
<h2 style="text-align:start">下载</h2> 
<h3 style="text-align:start">中文版信息</h3> 
<ul> 
 <li>中文支持：Krita 的所有软件包均内建中文支持，首次安装时会自动设置为操作系统的语言。</li> 
 <li>手动设置：菜单栏 –> Settings –> Switch Application Language (倒数第二项) –> 下拉选单 –> 中文 (底部)，重启程序生效。</li> 
 <li>插件翻译：G’MIC 插件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FSBopNjOn" target="_blank">需要下载翻译包</a></li> 
 <li>网盘下载：请在官网下载困难时使用，更新时间可能会略有滞后。</li> 
</ul> 
<h3 style="text-align:start">Windows 版本</h3> 
<ul> 
 <li><strong>64 位 Windows 安装程序</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.1.0-RC1%2Fkrita-x64-5.1.0-RC1-setup.exe" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F60HLzj6I" target="_blank">网盘下载</a></li> 
 <li><strong>64 位 Windows 免安装包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.1.0-RC1%2Fkrita-x64-5.1.0-RC1.zip" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F60HLzj6I" target="_blank">网盘下载</a></li> 
 <li><strong>64 位程序崩溃调试包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.1.0-RC1%2Fkrita-x64-5.1.0-RC1-dbg.zip" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F60HLzj6I" target="_blank">网盘下载</a></li> 
 <li><strong>配套网盘资源 (中文社区维护)</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FDea2uj0M" target="_blank">中文离线文档</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2F6tH13bVC" target="_blank">FFmpeg 软件包</a> |<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FSBopNjOn" target="_blank">G’Mic 滤镜汉化</a><span> </span>|</li> 
</ul> 
<ul> 
 <li>32 位支持：最后一版支持 32 位 Windows 的 Krita 为 4.4.3，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Fstable%2Fkrita%2F4.4.3%2Fkrita-x86-4.4.3-setup.exe" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FwdMnx1WB" target="_blank">网盘下载</a>。</li> 
 <li>免安装包：解压到任意位置，运行目录中的 Krita 快捷方式。不带文件管理器缩略图插件，与已安装版本共用配置文件和资源，但程序本身相互独立。</li> 
 <li>程序崩溃调试包：解压到 Krita 的安装目录，在报告程序崩溃问题时用于获取回溯追踪数据。日常使用无需下载此包。</li> 
</ul> 
<h3 style="text-align:start">Linux 版本</h3> 
<ul> 
 <li><strong>64 位 Linux AppImage 程序包</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.1.0-RC1%2Fkrita-5.1.0-RC1-x86_64.appimage" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FC0gZ6joR" target="_blank">网盘下载</a></li> 
 <li>G’Mic 插件已经整合到主程序包中</li> 
 <li>如果浏览器把链接作为文本打开，请右键点击链接另存为文件。</li> 
</ul> 
<h3 style="text-align:start">macOS 版本</h3> 
<ul> 
 <li><strong>macOS 程序映像</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.1.0-RC1%2Fkrita-5.1.0-RC1.dmg" target="_blank">本站下载</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshare.weiyun.com%2FgVg0CI53" target="_blank">网盘下载</a></li> 
</ul> 
<ul> 
 <li>如果您还在使用 OSX Sierra 或者 High Sierra，请<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D3py0kgq95Hk" target="_blank">观看此视频</a>了解如何启动由开发人员签名的可执行软件包。</li> 
</ul> 
<h3 style="text-align:start">安卓版本</h3> 
<p style="color:#4c4c4c; margin-left:0; margin-right:0; text-align:start">注意：由于 Google 近期更改了安卓 SDK 的需求条件，我们这次来不及构建 Krita 5.1.0 RC1 的软件包。我们会在正式版发布时构建它们，目前请暂时继续使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fzh%2Fitem%2Fkrita-5-1-beta-2-zh%2F" target="_blank">公开测试第 2 版</a>。</p> 
<h3 style="text-align:start">源代码</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.1.0-RC1%2Fkrita-5.1.0-RC1.tar.gz" target="_blank">TAR.GZ 格式源代码包</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.kde.org%2Funstable%2Fkrita%2F5.1.0-RC1%2Fkrita-5.1.0-RC1.tar.xz" target="_blank">TAR.XZ 格式源代码包</a></li> 
</ul> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            