
---
title: 'Qt 6.3 正式发布，添加 Qt 快速编译器、大量 Qt Quick 控件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-86400f3b3019098ba6ded72843cb86cf2dd.webp'
author: 开源中国
comments: false
date: Wed, 13 Apr 2022 07:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-86400f3b3019098ba6ded72843cb86cf2dd.webp'
---

<div>   
<div class="content">
                                                                                            <p>Qt 6.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-6.3-released" target="_blank">发布</a>了，<span style="color:#09102b">与往常一样，该版本包含许多新功能以及大量 Bug 修复：</span>自 Qt 6.2 发布以来修复了用户报告的总共 1750 个错误。下面摘录较为重要的新功能作介绍：</p> 
<h3>Qt Quick 编译器</h3> 
<p>新的 Qt 快速编译器是 Qt 6.3 中引入的重要新功能之一。 新的 QML 编译器由两个工具组成，QML 类型编译器 ( qmltc ) 和 QML 脚本编译器 ( qmlsc )。</p> 
<ul> 
 <li>QML 类型编译器将 QML 类型编译为 C++，显着加快了 QML 类型的实例化。</li> 
 <li>QML 脚本编译器在有意义的地方将函数和绑定编译到 C++，在 QML 中评估函数和绑定时能显著提高性能。</li> 
</ul> 
<p><img alt height="396" src="https://oscimg.oschina.net/oscnet/up-86400f3b3019098ba6ded72843cb86cf2dd.webp" width="700" referrerpolicy="no-referrer"></p> 
<p>Qt 快速编译器旨在<strong>尽可能</strong>将 QML 中的函数和绑定编译成 C++ 代码。由于 QML 是一种动态类型的语言，如果不能在编译时确定所有类型，那编译行为也将变得无意义。在这种情况下，编译器会退回到将方法编译成类似于旧的 qmlcachegen 的字节码。</p> 
<p>Qt 快速编译器对可以编译为本机代码的绑定和函数实现了显著的性能改进，绑定的评估速度比没有编译器的情况<strong>快 20% 到 35%</strong>。</p> 
<p><img alt height="700" src="https://oscimg.oschina.net/oscnet/up-08a32960a5a75934c18a58130b13defd495.webp" width="700" referrerpolicy="no-referrer"></p> 
<p>有关该 Qt Quick Compiler 的更多细节，可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fthe-new-qt-quick-compiler-is-coming-in-qt" target="_blank">这篇 Qt 博客中</a>细阅。</p> 
<h3>Qt Quick 和 Qt Quick 控件</h3> 
<p> Qt 6.3 添加了几个新的 Qt 快速控件，其中一些控件以前作为独立组件提供，比如控制树状视图的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.qt.io%2Fqt-6%2Fqml-qtquick-treeview.html" target="_blank">TreeView</a></p> 
<p><img alt height="552" src="https://oscimg.oschina.net/oscnet/up-9984430c6cd422d9b9de009b652bf5faee4.png" width="700" referrerpolicy="no-referrer"></p> 
<p>控制日历、日程表的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.qt.io%2Fqt-6%2Fqml-qtquick-controls2-calendarmodel.html" target="_blank">Calendar </a>：</p> 
<p><img alt height="552" src="https://oscimg.oschina.net/oscnet/up-ddd521465e73bd6366c117ae0615c19eadf.png" width="700" referrerpolicy="no-referrer"></p> 
<p>如今这些组件已被集成到 Qt 标准控件中。此外还添加了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.qt.io%2Fqt-6%2Fqml-qtquick-dialogs-folderdialog.html" target="_blank">FolderDialog</a> 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.qt.io%2Fqt-6%2Fqml-qtquick-dialogs-messagedialog.html" target="_blank">MessageDialog</a> 两个新对话框。 Qt Quick 中文本组件（Text、TextEdit、TextArea、TextInput）的性能也得到改进，以前，将非常大的文档传递给文本控件，可能会占用大量内存并导致绘图性能下降。该问题已在 Qt 6.3 中修复，确保后端只呈现可见的部分文本。</p> 
<h2>Qt Quick 3D</h2> 
<p>Qt Quick 3D 也又一些新特性，比如对反射的新支持。该反射使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.qt.io%2Fqt-6%2Fqml-qtquick3d-reflectionprobe.html" target="_blank">ReflectionProbe</a>  QML 元素实现，它的探针定位在场景中，捕捉周围环境并将其保存在立方体贴图中，然后其他元素可以使用该地图来显示反射。</p> 
<p><img alt height="403" src="https://oscimg.oschina.net/oscnet/up-836b9af29494df0825112e45e7fb2a36dc5.jpg" width="700" referrerpolicy="no-referrer"></p> 
<p>有关反射功能的更多详细信息，请查看介绍该功能的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqtquick3d-realtime-reflections%3FhsLang%3Den" target="_blank">博客文章。</a></p> 
<ul> 
 <li>此外，新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.qt.io%2Fqt-6%2Fqml-qtquick3d-resourceloader.html" target="_blank">ResourceLoader</a> 元素可以更好地控制 Qt Quick 3D 中的资源管理，允许预加载大型资源，例如网格或纹理。</li> 
 <li>粒子系统也获得了一些新功能，在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fnew-3d-particles-features-in-qt-6.3%3FhsLang%3Den" target="_blank">此处的博客文章</a>中了解更多信息。</li> 
</ul> 
<h2>Qt PDF</h2> 
<p>6.3 版本的 Qt PDF 也获得了一些性能改进，现在与 Qt 5.15 LTS 版本的性能一致。</p> 
<p><img alt height="637" src="https://oscimg.oschina.net/oscnet/up-f2c7a28529d3afc20e56a54e5b6831304c2.png" width="700" referrerpolicy="no-referrer"></p> 
<p>另外，官方透露 Qt 6.4 版本计划为 PDF 模块整一些新功能，但未对新内容作任何介绍。</p> 
<h2>其他改进</h2> 
<p>此外，该版本还有大量细小变化，包含支持 QLocale 中的 ISO639-2 语言标签、在 QDate、QTime 和 QLocale 中将时间转换为字符串时的 AM/PM 说明符，更容易在 JSON 和 CBOR 之间转换、新的 QtFuture::whenAll() 和 whenAny() 方法，以及许多其他较小的改进。</p> 
<p><span style="background-color:#ffffff; color:#09102b">对 Qt Widgets 进行了许多改进，重点是高分辨率显示、样式、样式表和项目视图的样式。</span></p> 
<p>在构建系统方面， Qt 6.3 对 CMake 的支持有了很多改进，值得注意的是新函数  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.qt.io%2Fqt-6%2Fqt-generate-deploy-app-script.html" target="_blank">qt-generate-deploy-app-script()</a>，它极大地简化了为不同平台上的应用程序生成部署脚本。</p> 
<h2>下一步计划</h2> 
<blockquote> 
 <p>Qt 6.3 是朝着下一个版本 Qt 6.4 和 Qt 6 系列的下一个 LTS 版本 Qt 6.5 迈出的一大步。</p> 
 <p>我们对这些版本有一些很棒的计划，其中包括对 WebAssembly 的全面支持、QHttpServer、gRPC 支持、基于 FFmpeg 的 Qt Multimedia 跨平台后端、Qt Speech、Qt Location，以及 Windows 11 上更好的原生 Look&Feel 和 iOS 支持</p> 
</blockquote> 
<p> </p> 
<p>可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.qt.io%2Fqt-6%2Fwhatsnew63.html" target="_blank">Qt 6.3 新功能</a>页面查看该版本所有新内容，在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-6.3-released" target="_blank">发行公告</a>中进一步了解该版本的所有变更。</p> 
<p> </p>
                                        </div>
                                      
</div>
            