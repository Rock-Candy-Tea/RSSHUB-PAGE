
---
title: 'KDE Frameworks 5.93 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5489'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5489'
---

<div>   
<div class="content">
                                                                    
                                                        <p>KDE Frameworks 是一个库和软件框架的集合，可供任何基于 Qt 的软件堆栈或多个操作系统上的应用程序使用。具有经常需要的功能解决方案，如硬件集成、文件格式支持、额外的图形控制元素、绘图功能和拼写检查，该集合作为 KDE Plasma 和 KDE Gear 的技术基础，以 LGPL 发布。</p> 
<p>KDE 近日正式发布 KDE Frameworks 5.93，部分更新内容如下：</p> 
<h3>Breeze 图标</h3> 
<ul> 
 <li>为缩放图标添加更多符号链接</li> 
 <li>添加 input-tvremote</li> 
</ul> 
<h3>额外的 CMake 模块</h3> 
<ul> 
 <li>修复查找 qmake</li> 
 <li>ECMQueryQt：添加回退</li> 
 <li>ECMAddQch：使其也可以与 Qt6::qhelpgenerator 一起使用</li> 
 <li>弃用 ECMQueryQmake，由 ECMQueryQt 取代</li> 
 <li>KDEInstallDirs6：从自定义逻辑移植到 ecm_query_qt</li> 
 <li>从 ECMQueryQmake 移植到 ECMQueryQt</li> 
 <li>Android：使用当前的 cmake 可执行文件</li> 
 <li>添加 ECMQueryQt 模块，该模块包含 Qt5 Qmake 和 Qt6 qtpaths</li> 
 <li>……</li> 
</ul> 
<h3>KDE Doxygen 工具</h3> 
<ul> 
 <li>为标准化构建添加 cmake 文件</li> 
</ul> 
<h3>KBookmarks</h3> 
<ul> 
 <li>在 repo 元数据中将 Android 添加到支持的平台</li> 
</ul> 
<h3>KCalendarCore</h3> 
<ul> 
 <li>Note 使用低级 libical 函数</li> 
 <li>在加载 vCalendars 时打印有关错误的更多信息</li> 
 <li>解析 iCal 数据时实现笔记本关联</li> 
 <li>比较 QDateTime 时间、时间规范和时区</li> 
 <li>……</li> 
</ul> 
<h3>KCMUtils</h3> 
<ul> 
 <li>修复 KPluginSelector KCM 在插件加载时丢失其元数据</li> 
 <li>将 Windows 和 macOS 标记为受支持</li> 
</ul> 
<h3>KConfig</h3> 
<ul> 
 <li>默认情况下在 Windows 上禁用 DBus 支持</li> 
 <li>公开 KConfig::mainConfigName()</li> 
 <li>kconf_update：修复检查更新文件的更改</li> 
</ul> 
<p>……</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkde.org%2Fannouncements%2Fframeworks%2F5%2F5.93.0%2F" target="_blank">https://kde.org/announcements/frameworks/5/5.93.0/</a></p>
                                        </div>
                                      
</div>
            