
---
title: 'Qt 6.2 Beta 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5652'
author: 开源中国
comments: false
date: Wed, 07 Jul 2021 06:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5652'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Qt 6.2 Beta 现已发布，这是其 6.2 系列的第一个 Beta 版本。Qt 6.2 包括所有广泛使用的 Qt 附加模块，也是 Qt 6 系列中第一个为商业授权者提供长期支持的版本，并提供了 3D 粒子等多项新功能。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>新特性 
  <ul> 
   <li>QtCore 
    <ul> 
     <li>许多属性现在都是可绑定的</li> 
     <li>Windows上的 UNC 路径和网络共享现在得到一致处理</li> 
     <li>QCalendar 现在支持从自定义后端 ID 构建</li> 
     <li>QCoreApplication 的 exit() 现在和 quit() 一样，对于 QEventLoop 和 QThread 也是如此</li> 
     <li>QDateTime 现在考虑到了整个 time_t 范围内的时区（只要平台提供了这样的信息），而不是人为地将范围限制在 1970-2037</li> 
     <li>QList（因此也包括 QVector）现在在为 C++20 构建时是一个满足 contiguous_range 的 contiguous_iterator</li> 
     <li>QLocalSocket::waitFor*() 现在在 Windows 上支持双工操作</li> 
     <li>QLockFile 的方法现在有了 std::Chrono 的重载</li> 
     <li>QString 现在可以从 char8_t 构建</li> 
     <li>QThreadPool 的线程优先级现在是可配置的</li> 
    </ul> </li> 
   <li>QtGui 
    <ul> 
     <li>QImage 中增加了 16 位和 32 位浮点图像格式</li> 
     <li>将 RGB 图像转换为灰度图像，或将RGB颜色绘制到灰度图像上，现在已经进行了伽马校正，并以输入颜色空间的亮度值产生</li> 
    </ul> </li> 
   <li>QtQuick 
    <ul> 
     <li>通过为其分配 ItemSelectionModel 添加了对在 TableView 中选择单元格的支持</li> 
    </ul> </li> 
   <li>QtQuickControls 
    <ul> 
     <li>增加了新的控件 SelectionRectangle，该个控件可以通过使用一个有样式的选择矩形来选择 TableView 中的单元格</li> 
    </ul> </li> 
   <li>QtQuick3D 
    <ul> 
     <li>支持实例渲染（Instanced Rendering），这是一种优化的方法，可以用不同的变换来绘制同一个物体的多个实例。</li> 
     <li>3D Particles，一个用于向 3D 场景添加粒子效果的 API</li> 
     <li>支持 Qt 快速输入事件，用于 3D 中的 2D 项目（在场景和纹理中）</li> 
     <li>使得在运行时加载 glTF2 文件成为可能</li> 
     <li>视差遮蔽映射。使得高度贴图的使用不需要增加几何体的成本</li> 
     <li>材质上的深度绘制模式。能够精细控制是否以及何时对一个材质进行深度渲染</li> 
    </ul> </li> 
  </ul> </li> 
 <li>平台相关 
  <ul> 
   <li>Android 
    <ul> 
     <li>之前在 QtAndroidExtras 下的 QtAndroid 命名空间下的一些调用现在在 QNativeInterface::QAndroidApplication 中</li> 
     <li>删除了 Ministro 代码，因为它不受 Android 支持</li> 
     <li>简化 AndroidManifest.xml 文件，只包含用户相关的标签</li> 
     <li>将 Android Gradle 插件更新到 4.1.3（补丁链接）</li> 
    </ul> </li> 
  </ul> </li> 
 <li>提供了一系列新的和恢复的模块，包括： 
  <ul> 
   <li>Qt Quick</li> 
   <li>Qt Bluetooth</li> 
   <li>Qt Multimedia</li> 
   <li>Qt NFC</li> 
   <li>Qt Positionin</li> 
   <li>Qt RemoteObjects</li> 
   <li>Qt Sensors</li> 
   <li>Qt SerialBus</li> 
   <li>Qt Serialport</li> 
   <li>Qt WebChannel</li> 
   <li>Qt WebEngine</li> 
   <li>Qt WebSockets</li> 
   <li>Qt WebView</li> 
  </ul> </li> 
</ul> 
<p>更多详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-6.2-beta-released" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            