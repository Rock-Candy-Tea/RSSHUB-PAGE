
---
title: 'KDE Framework 5.92.0 发布，大量更新项'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7387'
author: 开源中国
comments: false
date: Wed, 16 Mar 2022 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7387'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">KDE Frameworks 5.92.0 已正式发布。KDE Frameworks 是 Qt 的 83 个附加库，它在成熟的、经过同行评审和测试的库中提供了各种常见的功能，并且具有友好的许可条款。</span></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">此版本中的新功能</h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">对多个框架的更改</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>删除损坏的 Python 绑定生成</li> 
 <li>使<span> </span><code>BUILD_DESIGNERPLUGIN</code><span> </span>选项依赖于不交叉编译</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">图标</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>为 TeXstudio 添加应用程序图标</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">额外的 CMake 模块</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[ECMQmlModule] 修复文档语法</li> 
 <li>ECMGeneratePriFile：支持多个包含安装目录</li> 
 <li>KDEInstallDirs6：用 qtpaths 替换 ECMQueryQMake 用法</li> 
 <li>将 Android 工具链文件和 FindGradle 适配到 Qt6</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">KActivityStats</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将 Boost 依赖项移至 BUILD_TESTING 块</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">KActivities</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在将可执行文件传递给 QProcess 之前，检查 PATH 中是否存在可执行文件</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">KAuth</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>标准化标题名称并包含符合 KF 标准的路径布局</li> 
 <li>准备 KF6 KAuthWidgets 库，带有 KF5 的接口库</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">KBookmarks</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在将可执行文件传递给 QProcess 之前，检查 PATH 中是否存在可执行文件</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">KCalendarCore</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在比较平等发生率时比较 timeSpecs</li> 
 <li>保留全天事件 dtEnd 的 timeSpec</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">KConfig</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加 KWindowStateSaver</li> 
 <li>从 kauthorized.h 中删除警告</li> 
 <li>KConfigCompiler：支持 ItemAccessors=true 与信号项</li> 
 <li>QMake pri 文件：修复缺少版本标头的新路径</li> 
 <li>支持没有 Qt 会话管理器的构建</li> 
 <li>添加 KConfig GUI 日志记录类别</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">KConfigWidgets</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>KHamburgerMenu：在显示菜单栏时避免空接收器警告</li> 
 <li>添加一个 KColorScheme::operator==</li> 
 <li>KHambugerMenu：修复从 KHamburgerMenu 显示窗口菜单栏时窗口崩溃的问题</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">KContacts</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将内部和外部 API 拆分为不同的文件</li> 
 <li>还要安装地址格式 API 头</li> 
 <li>通过每行 3 个以上的字段，改进不完整地址和格式的输出</li> 
 <li>重写地址格式化程序</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">KCore插件</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>弃用 KPluginMetaData::fromDesktopFile</li> 
 <li>KPluginMetaDataTest：显式调用专用构造函数</li> 
 <li>KPluginMetaData：针对已弃用的代码路径发出运行时弃用警告</li> 
 <li>KPluginMetaData：为构造函数的弃用代码路径添加注释</li> 
 <li>KPluginMetaData：使用 QFileInfo::completeBaseName 导出插件 id</li> 
 <li>将不匹配的主机工具版本降级为警告</li> 
 <li>添加一种方式来指示在完成时不显示通知</li> 
 <li>允许为没有嵌入 JSON 元数据的插件创建有效的 KPluginMetaData</li> 
 <li>将<span> </span><code>OUTPUT_FILE</code><span> </span>参数添加到<span> </span><code>kcoreaddons_desktop_to_json()</code></li> 
 <li>添加 KSignalHandler</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本还包含其他大量更新内容，详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkde.org%2Fannouncements%2Fframeworks%2F5%2F5.92.0%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            