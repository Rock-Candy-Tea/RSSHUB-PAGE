
---
title: 'Qt 6.3 首个 Beta 测试版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7759'
author: 开源中国
comments: false
date: Sat, 05 Feb 2022 08:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7759'
---

<div>   
<div class="content">
                                                                                            <p>Qt 6.3 首个 Beta 测试版<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-6.3-beta-released" target="_blank">已发布</a>，正式版计划在 3 月底或者 4 月初推出。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Qt 6.3 新增的 Modules：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Qt Language Server：实现了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmicrosoft.github.io%2Flanguage-server-protocol%2Fspecifications%2Fspecification-current%2F" target="_blank">Language Server Protocol Specification</a><span> </span>和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jsonrpc.org%2Fspecification" target="_blank">JsonRpc 2.0</a><span> </span>协议。此模块不包含公共 API</li> 
</ul> 
<p>Qt 6.3 的新 Qt Language Server module 实现了语言服务器协议 (LSP) 规范和 JsonRpc 2.0 协议，以便更好地与源代码编辑器/IDE 集成。新的 QML 类型编译器将 QML 对象结构编译为 C++ 类，而新的 QML 脚本编译器将函数和表达式编译为 C++ 代码。还有一个新的 QML Lint 用于发现新编译器可能无法很好地翻译的代码。Qt 公司预计，这种新的 QML 编译器工作将使启动和执行时间最多加快 30%。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Qt 6.3 恢复的 Modules（Qt 6.3 重新引入了以下 Qt 6.2 中没有的 Modules。所有列出的 Modules 都被移植到 Qt 6 和 CMake 构建系统中）</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqtpdf-index.html" target="_blank">Qt PDF</a>（现处于技术预览阶段）</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">每个 Modules 的详细变更点此查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fmodulechanges.html" target="_blank">https://doc-snapshots.qt.io/qt6-6.3/modulechanges.html</a></p> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Qt 6.3 的变化主要集中在 Qt Core Module（核心模块）上：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>添加了用于组合多个 future 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqtfuture.html%23whenAll" target="_blank">QtFuture::whenAll</a>() 和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqtfuture.html%23whenAny" target="_blank">QtFuture::whenAny</a>() 函数</li> 
 <li>添加了接受权限参数的 QDir::mdkir() 和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqfile.html%23open" target="_blank">QFile::open</a>() 重载</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqmetatype.html" target="_blank">QMetaType</a><span> </span>现支持将<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqfuture.html" target="_blank">QFuture</a><T> 转换为<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqfuture.html" target="_blank">QFuture</a><void></li> 
 <li>添加<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqdiriterator.html%23nextFileInfo" target="_blank">QDirIterator::nextFileInfo</a>() 来促进并获得完整的文件信息</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqregularexpressionmatch.html" target="_blank">QRegularExpressionMatch</a><span> </span>现支持使用 hasCaptured() 方法来测试给定的组是否被捕获</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqvarlengtharray.html" target="_blank">QVarLengthArray</a><span> 现已拥有</span> emplace() 和 emplace_back() 方法</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqcbormap.html%23fromJsonObject" target="_blank">QCborMap::fromJsonObject</a>() 和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqcborarray.html%23fromJsonArray" target="_blank">QCborArray::fromJsonArray</a>() 现已拥有 rvalue 重载</li> 
 <li>……</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fwhatsnew63.html" target="_blank">详情查看新特性介绍公告</a>。    </p>
                                        </div>
                                      
</div>
            