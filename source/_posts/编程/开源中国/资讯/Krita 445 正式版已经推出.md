
---
title: 'Krita 4.4.5 正式版已经推出'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8736'
author: 开源中国
comments: false
date: Sun, 01 Aug 2021 19:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8736'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start"><em>本文发表时间：   2021 年 06 月 09 日</em></p> 
<p style="text-align:start">今天 Krita 团队推出了 Krita 4.4.5，它是 5.0 发布前的最后一个程序缺陷修复版本。我们发布此版的最主要原因是要修复一个 macOS 版的严重缺陷，但我们也顺便把大量其他修复也合并到此版中，希望能提升使用体验。</p> 
<p style="text-align:start">注意：Krita 4.4.4 只在 Epic 游戏商城发布过，并未在本站发布。</p> 
<ul> 
 <li>为在 mdiarea 中的标签页设置 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D433640" target="_blank">Bug 433640</a>)</li> 
 <li>如果图像加载频繁失败，则停止重试 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D433652" target="_blank">Bug 433652</a>)</li> 
 <li>使用 QVersionNumber 来比较版本</li> 
 <li>修复油画滤镜的图块显示错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkrita.org%2Fzh%2Fitem%2Fkrita-arrives-in-the-epic-store-zh%2F" target="_blank">相关代码提交</a></li> 
 <li>仅在使用 Krita alpha 或 beta 版时打开程序缺陷报告对话框</li> 
 <li>修复在右键面板显示比例为 125% 时的崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D431944" target="_blank">Bug 431944</a>)</li> 
 <li>修复 GCC11 的编译，感谢 Jonathan Wakely 提供建议线索 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D434150" target="_blank">Bug 434150</a>)</li> 
 <li>在 Arm Linux 下使用 OpenGL ES (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D421136" target="_blank">Bug 421136</a>)</li> 
 <li>修复导入损坏的 ICC 色彩特性文件时的崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D434273" target="_blank">Bug 434273</a>)</li> 
 <li>移除 hello world 演示插件 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D422380" target="_blank">Bug 422380</a>)</li> 
 <li>修复缺陷：裁剪工具崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D433770" target="_blank">Bug 433770</a>)</li> 
 <li>修复缺陷：变形 (斜切) 的参照点无效 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D427462" target="_blank">Bug 427462</a>)</li> 
 <li>修复状态栏和导航器中的角度选择器范围 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D434993" target="_blank">Bug 434993</a>)</li> 
 <li>在曲线网格变形中实现“按比例缩放手柄”</li> 
 <li>修复缺陷：裁剪工具不响应某些事件 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D435201" target="_blank">Bug 435201</a>)</li> 
 <li>从剪贴板支持图像格式列表中移除 JPG (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D431310" target="_blank">Bug 431310</a>)</li> 
 <li>如果操作为空，则不设置菜单文字 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D437036" target="_blank">Bug 437036</a>)</li> 
 <li>为 libkis 提供节点的唯一 ID <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2F57f0af27d358e21ffdaf8af5a38a196df1565dcf" target="_blank">commit</a></li> 
 <li>修复 quicklook 生成器 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D436224" target="_blank">Bug 436224</a>)</li> 
 <li>修复 macOS 下的随机崩溃并修复光标在使用 cmb+tab 切换到其他应用程序并使用鼠标返回 Krita 时的卡死现象 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D434646" target="_blank">Bug 434646</a>)</li> 
 <li>修复当裁剪操作活动时按下 Ctrl+Z 会造成数据损坏的问题 (CC<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D433770" target="_blank">Bug 433770</a>)</li> 
 <li>修复智能填色工具色板的缩放 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D410997" target="_blank">Bug 410997</a>)</li> 
 <li>修复按下 Shift 修饰键时手绘轮廓选区工具的精确度问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D437048" target="_blank">Bug 437048</a>)</li> 
 <li>修复在某些笔画还在渲染途中时过早关闭 Krita 造成的崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D419021" target="_blank">Bug 419021</a>)</li> 
 <li>修复 KisCanvas2::setProofingOptions() 的不正确内存访问</li> 
 <li>修复自发任务开始时的 race 状态 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D434648" target="_blank">Bug 434648</a>)</li> 
 <li>修复导航器的色彩管理显示 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D428605" target="_blank">Bug 428605</a>)</li> 
 <li>修复透视变形模式的最近邻插值过滤器 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D420811" target="_blank">Bug 420811</a>)</li> 
 <li>修复变形后的图像会在移动鼠标过快时造成漂移 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D416899" target="_blank">Bug 416899</a>)</li> 
 <li>修复自由变形模式的平滑度 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D416899" target="_blank">Bug 416899</a>)</li> 
 <li>修复 (不限于) 中文输入法无法在某些弹出部件中使用的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D395598" target="_blank">Bug 395598</a>)</li> 
 <li>修复在命令行模式下 Krita 的导出功能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2F38b9dfa668494c03a9d11b16e3f619ff3c4f27a8" target="_blank">相关代码提交</a></li> 
 <li>修复 OpenColorIO 的 include 目录检测 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2F1c55fefecb85366feee7d101a343f31d3cfb8e5d" target="_blank">相关代码提交</a></li> 
 <li>修复 OverviewThumbnailStrokeStrategy 中的参数顺序 (CID 310957)</li> 
 <li>不要在 psd_image_data 中依赖字节顺序 (CID 35080)</li> 
 <li>在进行计算之前拓宽变量 (CID 248925)</li> 
 <li>用默认值覆盖数值为 0 的 patchWidth 和 patchHeight (CID 248441, CID 248622)</li> 
 <li>在 ConvertColorSpacePr.Vis 中进行动态投射后检查数值 (CID 304985)</li> 
 <li>在转换时正确绑定数值 (CID 248629, CID 248458)</li> 
 <li>在 KisMetaData::TypeInfo::Private 中初始化 propertyType (CID 35498)</li> 
 <li>初始化 KoRuler and KisFullRefreshWalker 中的变量 (CID 35523, CID 35612)</li> 
 <li>初始化 KisImagePyramid 中的成员 (CID 36041)</li> 
 <li>初始化 DlgOffsetImage and DeformBrush 中初始化成员 (CID 36144, CID 36265)</li> 
 <li>初始化 KCanvasPreview 中的成员 (CID 36395)</li> 
 <li>初始化 DlgClonesArray 中的成员 (CID 248509)</li> 
 <li>初始化 KisShadeSelectorLine 中的成员 (CID 36338)</li> 
 <li>初始化 assistant 类 的成员 (CID 248502, CID 248916)</li> 
 <li>初始化数值框相关类的成员 (CID 248555, CID 248871)</li> 
 <li>修复 xyYtoXYZ 色彩转换方程</li> 
 <li>简化三角形拾色器代码 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2F789edc1cf4fe7c2c885368337788c9db7e22d1c6" target="_blank">相关代码提交</a></li> 
 <li>修复颜色通道面板显示更新 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2Fcb81820599f35ffae4c4e41ce8039829ffec37d7" target="_blank">相关代码提交</a></li> 
 <li>修复直方图面板显示更新 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2F6ddf4a12db10510715b177e71768ea176b6327a2" target="_blank">相关代码提交</a></li> 
 <li>修复直方图部件的多线程处理 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2F04d8cf6c586877e76c174aff445fb726962a4984" target="_blank">相关代码提交</a></li> 
 <li>在 HistogramDockerWidget 中更改 typedef 为 using <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2F4cfcf5e967a195af07c4f4c238183a147d513899" target="_blank">相关代码提交</a></li> 
 <li>修复 SvgStyleWriter 中参照空值 (CID 329512)</li> 
 <li>修复在 HistogramDockerWidget 中的未初始化数值 (CID 329509)</li> 
 <li>修复撤销历史记录面板的高分辨率支持模式画布预览 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2F7bfca14742ba2b99c42c33ef3978be1fb7fb868f" target="_blank">相关代码提交</a></li> 
 <li>修复在保存巨大图像为 .kra 时崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D432182" target="_blank">Bug 432182</a>)</li> 
 <li>确保变形工作器不尝试缩放为 0 倍 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D432182" target="_blank">Bug 432182</a>)</li> 
 <li>修复 KoQuaZipStore 的错误检测 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2F80f43d1ce4bb1305731cffc192c4e9907a88b986" target="_blank">相关代码提交</a></li> 
 <li>在语言列表中显示国家/地区以便区分 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D437994" target="_blank">Bug 437994</a>)</li> 
 <li>修复在使用变形工具处理矢量图层时的更新失败 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D437886" target="_blank">Bug 437886</a>)</li> 
 <li>不为 zh_CN 和 zh_TW 区域设置附加国家/地区标识 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D437994" target="_blank">Bug 437994</a>)</li> 
 <li>回退“修复 OpenColorIO 的 include 目录检测”</li> 
 <li>保存为 kra 文件时添加更多检测 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2Fd47163e4f7e99d790be7905b79b2ca94ef8ef675" target="_blank">相关代码提交</a></li> 
 <li>为浮点数值修复非浮点数值结果 (CID 329390, CID 329448, CID 329482)</li> 
 <li>修复多个类中的未初始化数值 (CID 329508, CID 329504, CID 329503, CID 329502, CID 329501)</li> 
 <li>不对 0 字节色板进行 assert <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2F876d61fc8d2b0a3f76277a814ccc9f595f063c7d" target="_blank">相关代码提交</a></li> 
 <li>初始化 SVG 符号类成员 (CID 304987)</li> 
 <li>初始化 KisColorSelector 类成员 (CID 36349, CID 248848, CID 248452, CID 248707)</li> 
 <li>安卓版本：让退出时保存的操作更加可靠 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2Ff248c032199be64e9ac4e172155434d793fdd212" target="_blank">相关代码提交</a></li> 
 <li>缺陷修复：在存在不止一个辅助尺时发生显示错误 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D401940" target="_blank">Bug 401940</a>)</li> 
 <li>安卓版本：发生 TouchCancel 事件时的 SAFE_ASSERT <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkrita%2F-%2Fcommit%2Fadebed6735b94bbcd7945aeace304975f43e5667" target="_blank">相关代码提交</a></li> 
 <li>安卓版本：图像属性文字框不响应键盘事件</li> 
 <li>安卓版本：修复旋转时窗口管理器的位置</li> 
 <li>缺陷修复：描边填充和形状填充效果不一致 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D399127" target="_blank">Bug 399127</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D422204" target="_blank">Bug 422204</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D434828" target="_blank">Bug 434828</a>)</li> 
</ul>
                                        </div>
                                      
</div>
            