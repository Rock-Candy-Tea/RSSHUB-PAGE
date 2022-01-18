
---
title: 'Qt 6.3 Alpha 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8701'
author: 开源中国
comments: false
date: Tue, 18 Jan 2022 07:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8701'
---

<div>   
<div class="content">
                                                                                            <p>Qt 6.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-6.3-alpha-released" target="_blank">发布</a>了首个 Alpha 版本。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdownload.qt.io%2Fdevelopment_releases%2Fqt%2F6.3%2F" target="_blank">http://download.qt.io/development_releases/qt/6.3/</a></p> 
<p>Qt 6.3 新增的 Modules：</p> 
<ul> 
 <li>Qt Language Server：实现了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmicrosoft.github.io%2Flanguage-server-protocol%2Fspecifications%2Fspecification-current%2F" target="_blank">Language Server Protocol Specification</a><span> </span>和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jsonrpc.org%2Fspecification" target="_blank">JsonRpc 2.0</a><span> </span>协议。此模块不包含公共 API</li> 
</ul> 
<p>Qt 6.3 恢复的 Modules（Qt 6.3 重新引入了以下 Qt 6.2 中没有的 Modules。所有列出的 Modules 都被移植到 Qt 6 和 CMake 构建系统中）</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqtpdf-index.html" target="_blank">Qt PDF</a>（现处于技术预览阶段）</li> 
</ul> 
<p>每个 Modules 的详细变更点此查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fmodulechanges.html" target="_blank">https://doc-snapshots.qt.io/qt6-6.3/modulechanges.html</a></p> 
<hr> 
<p>Qt 6.3 的变化主要集中在 Qt Core Module（核心模块）上：</p> 
<ul> 
 <li>添加了用于组合多个 future 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqtfuture.html%23whenAll" target="_blank">QtFuture::whenAll</a>() 和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqtfuture.html%23whenAny" target="_blank">QtFuture::whenAny</a>() 函数</li> 
 <li>添加了接受权限参数的 QDir::mdkir() 和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqfile.html%23open" target="_blank">QFile::open</a>() 重载</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqmetatype.html" target="_blank">QMetaType</a><span> </span>现支持将<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqfuture.html" target="_blank">QFuture</a><T> 转换为<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqfuture.html" target="_blank">QFuture</a><void></li> 
 <li>添加<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqdiriterator.html%23nextFileInfo" target="_blank">QDirIterator::nextFileInfo</a>() 来促进并获得完整的文件信息</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqregularexpressionmatch.html" target="_blank">QRegularExpressionMatch</a><span> </span>现支持使用 hasCaptured() 方法来测试给定的组是否被捕获</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqvarlengtharray.html" target="_blank">QVarLengthArray</a><span> 现已拥有</span> emplace() 和 emplace_back() 方法</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqcbormap.html%23fromJsonObject" target="_blank">QCborMap::fromJsonObject</a>() 和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fqcborarray.html%23fromJsonArray" target="_blank">QCborArray::fromJsonArray</a>() 现已拥有 rvalue 重载</li> 
 <li>……</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.3%2Fwhatsnew63.html" target="_blank">详情查看新特性介绍公告</a>。</p>
                                        </div>
                                      
</div>
            