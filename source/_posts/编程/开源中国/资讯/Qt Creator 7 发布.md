
---
title: 'Qt Creator 7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5842'
author: 开源中国
comments: false
date: Fri, 25 Mar 2022 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5842'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Qt Creator 是一个跨平台的 C++、JavaScript 和 QML 集成开发环境，它简化了 GUI 应用的开发。它是 Qt GUI 应用开发框架的 SDK 的一部分。该编辑器具有语法高亮和自动补全等功能。</p> 
<p>Qt Creator 7 正式发布，更新内容如下：</p> 
<h3>常规</h3> 
<ul> 
 <li>给予 <code>Welcome</code> 一个新的外观</li> 
 <li>将 <code>New File or Project</code> 分为 <code>New File</code> 和 <code>New Project</code></li> 
 <li>增加了在线安装程序中可供选择的 Qt 新版本通知</li> 
 <li>在更多的上下文菜单中增加了 <code>Show in File System View</code></li> 
 <li>增加了 <code>Tools > Debug Qt Creator > Show Logs</code>，用于查看 Qt Creator 调试日志</li> 
 <li>将 C++ 代码模型和语言客户端检查器移至 <code>Tools > Debug Qt Creator</code></li> 
</ul> 
<h3>编辑</h3> 
<ul> 
 <li>增加了选择文档中所有搜索结果的操作</li> 
 <li>增加了对选择外部编辑器作为默认编辑器的支持</li> 
 <li>修正了文本编辑宏中的复制动作</li> 
 <li>修正了退格后的光标位置，以及向上或向下移动的问题</li> 
</ul> 
<h3>C++</h3> 
<ul> 
 <li>在二进制包中切换到 LLVM 14</li> 
 <li>默认切换到 Clangd</li> 
 <li>修正了编译错误出现在 Issues 面板的代码模型错误下面的问题。</li> 
 <li>修正了全局索引器的性能问题</li> 
 <li>修正了 HiDPI 屏幕上的重构图标</li> 
 <li>修正了带有额外字符的点到箭头的转换</li> 
 <li>clang-format 
  <ul> 
   <li>将设置移到了 <code>Code Style</code> 编辑器中</li> 
   <li>增加了 <code>clang-format</code> 设置和自定义代码样式之间的同步</li> 
  </ul> </li> 
</ul> 
<h3>QML</h3> 
<ul> 
 <li>更新了解析器至最新的 Qt 版本</li> 
 <li>修正了应用程序目录没有搜索到 QML 模块的问题</li> 
</ul> 
<h3>Python</h3> 
<ul> 
 <li>添加了 Python 特定的语言服务器设置</li> 
</ul> 
<h3>语言服务器协议</h3> 
<ul> 
 <li>删除了对过时的语义高亮协议提案的支持</li> 
 <li>修正了过时的诊断可能被显示的问题</li> 
 <li>修正了重新高亮的问题</li> 
 <li>修正了快速关闭文档时的崩溃</li> 
</ul> 
<h3>FakeVim</h3> 
<ul> 
 <li>增加了对替代命令中反斜线的支持</li> 
</ul> 
<h3>Git</h3> 
<ul> 
 <li>添加了按作者过滤日志的支持</li> 
 <li>在 Windows 上添加了对 <code>HOMEDRIVE</code> 和 <code>HOMEPATH</code> 的处理</li> 
 <li>修复无法解决与已删除文件冲突的问题</li> 
</ul> 
<h3>Windows</h3> 
<ul> 
 <li>修复了 MinGW 编译器的自动检测</li> 
 <li>修复了 MSVC 缺少的编译 <code>Issues</code></li> 
 <li>修复了使用 <code>client</code> 时错误的路径分隔符</li> 
</ul> 
<h3>Linux</h3> 
<ul> 
 <li>添加 Wayland 后端</li> 
</ul> 
<h3>macOS</h3> 
<ul> 
 <li>修复了 macOS 深色模式不适用于深色主题</li> 
 <li>修复了用户应用程序从 Qt Creator 继承访问权限的问题</li> 
 <li>修复了键重复</li> 
 <li>修复了使用 <code>zsh</code> 打开 <code>Terminal</code> 时的环境</li> 
</ul> 
<h3>Android</h3> 
<ul> 
 <li>添加了默认 NDK 的选项</li> 
 <li>修复了 <code>Include prebuilt OpenSSL library</code> 可能会添加错误的 <code>.pro</code> 文件的问题</li> 
 <li>修复了使用 LLDB 调试带有大写标识符的设备</li> 
 <li>修复了对最近 NDK 的可用 NDK 平台的检测</li> 
 <li>修复了同时通过 USB 和 WiFi 连接的设备的命名</li> 
</ul> 
<h3>WebAssembly</h3> 
<ul> 
 <li>改进的浏览器选择</li> 
 <li>修复了使用 Qt 6.2 运行基于 CMake 的 Qt Quick 应用程序</li> 
</ul> 
<h3>Docker</h3> 
<ul> 
 <li>添加了对 macOS 主机的实验性支持</li> 
</ul> 
<p>……</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-creator-7-released" target="_blank">https://www.qt.io/blog/qt-creator-7-released</a></p>
                                        </div>
                                      
</div>
            