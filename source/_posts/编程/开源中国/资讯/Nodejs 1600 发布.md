
---
title: 'Node.js 16.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2393'
author: 开源中国
comments: false
date: Wed, 21 Apr 2021 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2393'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Node.js 是能够在服务器端运行 JavaScript 的开放源代码、跨平台 JavaScript 运行环境。Node.js 由Node.js Foundation（已与JS Foundation合并为OpenJS Foundation）持有和维护，亦为 Linux 基金会的项目。Node.js采用Google开发的V8运行代码，使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E4%25BA%258B%25E4%25BB%25B6%25E9%25A9%2585%25E5%258B%2595">事件驱动</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzh.wikipedia.org%2Fw%2Findex.php%3Ftitle%3D%25E9%259D%259E%25E9%2598%25BB%25E5%25A1%259E%26action%3Dedit%26redlink%3D1">非阻塞</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%25BC%2582%25E6%25AD%25A5IO">异步输入输出</a>模型等技术来提高性能，可优化应用程序的传输量和规模。这些技术通常用于资料密集的即时应用程序。</p> 
<p>Node.js 16.0.0 正式发布，本次更新内容如下：</p> 
<h3><strong>稳定 Timers Promises API：</strong></h3> 
<p>Timers Promises API 提供了一组替代的定时器函数，这些函数返回 Promise 对象。在Node.js v15.0.0 中添加，在此版本中，它们从实验状态升级为稳定状态。</p> 
<h3>Toolchain <strong>和编译器升级：</strong></h3> 
<p>Node.js v16.0.0 将是发布用于 Apple Silicon 的预构建二进制文件的第一个版本。虽然我们将为 Intel（<code>darwin-x64</code>）和 ARM（<code>darwin-arm64</code>）架构提供单独的压缩文件，但 macOS 安装程序（<code>.pkg</code>）将作为多架构二进制文件提供。</p> 
<ul> 
 <li><strong>(SEMVER-MAJOR)</strong> build：移除对 Python 2 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F36691" target="_blank">#36691</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> build：将 Makefile 中的 Python 默认为 Python3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37764" target="_blank">#37764</a></li> 
 <li>build：更新 Makefile 以支持 fat 二进制 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37861" target="_blank">#37861</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> build：在 macOS 上启用 ASLR (PIE)  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F35704" target="_blank">#35704</a></li> 
 <li>build：对早于 8.3.0 的 gcc 版本发出警告 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37935" target="_blank">#37935</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> doc：将最低支持的 Xcode 更新到 11 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37872" target="_blank">#37872</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> doc：将最低支持的 GCC 更新到 8.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37871" target="_blank">#37871</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> doc：将 AIX 的 16.x 版本更新为 GCC 8 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37677" target="_blank">#37677</a></li> 
 <li>工具：在 Distribution.xml 中设置 arch <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F38261" target="_blank">#38261</a></li> 
</ul> 
<h3>V8 9.0：</h3> 
<p>V8 JavaScript 引擎已更新至 9.0，其中包括性能调整和改进。</p> 
<p>这次更新还带来了 ECMAScript RegExp Match Indices，它提供了捕获字符串的开始和结束索引。当正则表达式有 <code>/d</code> 标志时，索引数组可以通过匹配对象上的 <code>.indices</code> 属性获得。</p> 
<h3><strong>弃用和移除：</strong></h3> 
<ul> 
 <li><strong>(SEMVER-MAJOR)</strong> fs：删除允许的 rmdir 递归 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37216" target="_blank">#37216</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> fs：运行时弃用rmdir递归选项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37302" target="_blank">#37302</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> lib：运行时弃用访问 process.binding（'http_parser'） <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37813" target="_blank">#37813</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> lib：运行时弃用访问 process.binding（'url'）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37799" target="_blank">#37799</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> lib：使 process.binding（'util'）仅返回类型检查器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37819" target="_blank">#37819</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> lib：运行时弃用访问 process.binding（'crypto'） <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37790" target="_blank">#37790</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> 模块：删除 module.createRequireFromPath <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37201" target="_blank">#37201</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> 模块：运行时弃用子路径文件夹映射 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37215" target="_blank">#37215</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> 模块：运行时弃用“主”索引和扩展查找 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37206" target="_blank">#37206</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> 模块：运行时弃用无效的 package.json 主要条目 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37204" target="_blank">#37204</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> 进程：运行时弃用更改 process.config <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F36902" target="_blank">#36902</a></li> 
</ul> 
<h3>其他值得注意的变化</h3> 
<ul> 
 <li><strong>(SEMVER-MAJOR)</strong> 缓冲区：将 btoa 和 atob 暴露为全局变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37786" target="_blank">#37786</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> <strong>deps</strong>: 将最低 ICU 版本提升到 68 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37330" target="_blank">#37330</a></li> 
 <li><strong>deps</strong>: 更新 ICU 至 69.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F38178" target="_blank">#38178</a></li> 
 <li><strong>deps</strong>: 将 llhttp 升级到 6.0.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F38277" target="_blank">#38277</a></li> 
 <li><strong>deps</strong>: 将 npm 升级到 7.10.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F38254" target="_blank">#38254</a></li> 
 <li><strong>(SEMVER-MINOR)</strong> <strong>http</strong>: 添加 http.ClientRequest.getRawHeaderNames()  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37660" target="_blank">#37660</a></li> 
 <li><strong>(SEMVER-MAJOR)</strong> <strong>lib,src</strong>: 更新群集以使用 Parent <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F36478" target="_blank">#36478</a></li> 
 <li><strong>(SEMVER-MINOR)</strong> 模块：添加对有 <code>require(…)</code> 前缀的 <code>node:</code> 调用的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37246" target="_blank">#37246</a></li> 
 <li><strong>(SEMVER-MINOR)</strong> <strong>perf_hooks</strong>: 添加直方图选项以定时 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37475" target="_blank">#37475</a></li> 
 <li><strong>(SEMVER-MINOR)</strong> 为有 <code>require(…)</code> 前缀的 <code>node:</code> 调用添加自动完成功能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F37246" target="_blank">#37246</a></li> 
 <li><strong>(SEMVER-MINOR)</strong> <strong>util</strong>: 添加 getSystemErrorMap() impl <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F38101" target="_blank">#38101</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fblob%2Fmaster%2Fdoc%2Fchangelogs%2FCHANGELOG_V16.md%2316.0.0" target="_blank">https://github.com/nodejs/node/blob/master/doc/changelogs/CHANGELOG_V16.md#16.0.0</a></p>
                                        </div>
                                      
</div>
            