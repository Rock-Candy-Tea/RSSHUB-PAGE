
---
title: 'xmake v2.5.6 发布，改进预编译二进制镜像包兼容性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2162'
author: 开源中国
comments: false
date: Fri, 30 Jul 2021 10:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2162'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">xmake</a> 是一个基于 Lua 的轻量级跨平台构建工具，使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p style="text-align:start">这是一个稳定性修复版本，主要修复和改进了一些跟预编译二进制包相关的兼容性问题。另外新增了一些实用的接口来设置默认的编译平台、架构和模式，以及允许的编译平台、架构列表等等。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2 style="text-align:start">新特性介绍</h2> 
<h3 style="text-align:start">windows 预编译包的兼容性修复</h3> 
<p style="text-align:start">上个版本对 Windows 下的 预编译包安装做了初步的支持，但是由于没有考虑 toolset 版本的兼容性问题，因此如果用户的 vs 版本过低，就会在集成包时候出现链接问题。</p> 
<p style="text-align:start">根据 ms 的官方描述，其实 msvc 的二进制库对于 toolset 的版本是向下兼容的。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fcpp%2Fporting%2Fbinary-compat-2015-2017%3Fview%3Dmsvc-160" target="_blank">https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160</a></p> 
<blockquote> 
 <p>You can mix binaries built by different versions of the v140, v141, and v142 toolsets. However, you must link by using a toolset at least as recent as the most recent binary in your app. Here’s an example: you can link an app compiled using any 2017 toolset (v141, versions 15.0 through 15.9) to a static library compiled using, say, Visual Studio 2019 version 16.2 (v142), if they’re linked using a version 16.2 or later toolset. You can link a version 16.2 library to a version 16.4 app as long as you use a 16.4 or later toolset.</p> 
</blockquote> 
<p style="text-align:start">也就是说，云端采用 v141 编译的库，用户的 msvc toolset 只要是 >=141 就可以兼容支持。</p> 
<p style="text-align:start">因此，我们改进了云端的预编译逻辑，针对 vs2015/14.16 和 vs2019/14.29 两个工具集分别进行预编译，然后 xmake 会根据用户 msvc 的 toolset 版本，优先选取最优的兼容版本库下载集成。</p> 
<h3 style="text-align:start">set_defaultplat</h3> 
<h4 style="text-align:start">设置默认的编译平台</h4> 
<p style="text-align:start">v2.5.6 以上版本才支持，用于设置工程默认的编译平台，如果没有设置，默认平台跟随当前系统平台，也就是 os.host()。</p> 
<p style="text-align:start">比如，在 macOS 上默认编译平台是 macosx，如果当前项目是 ios 项目，那么可以设置默认编译平台为 iphoneos。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">set_defaultplat</span><strong>(</strong><span style="color:#ff00ff">"iphoneos"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">它等价于，<code>xmake f -p iphoneos</code>。</p> 
<h3 style="text-align:start">set_defaultarch</h3> 
<h4 style="text-align:start">设置默认的编译架构</h4> 
<p style="text-align:start">v2.5.6 以上版本才支持，用于设置工程默认的编译架构，如果没有设置，默认平台跟随当前系统架构，也就是 os.arch()。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">set_defaultplat</span><strong>(</strong><span style="color:#ff00ff">"iphoneos"</span><strong>)</strong>
<span style="color:#000000">set_defaultarch</span><strong>(</strong><span style="color:#ff00ff">"arm64"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">它等价于，<code>xmake f -p iphoneos -a arm64</code>。</p> 
<p style="text-align:start">我们也可以设置多个平台下的默认架构。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">set_defaultarch</span><strong>(</strong><span style="color:#ff00ff">"iphoneos|arm64"</span><strong>,</strong> <span style="color:#ff00ff">"windows|x64"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">在 iphoneos 上默认编译 arm64 架构，在 windows 上默认编译 x64 架构。</p> 
<h3 style="text-align:start">set_defaultmode</h3> 
<h4 style="text-align:start">设置默认的编译模式</h4> 
<p style="text-align:start">v2.5.6 以上版本才支持，用于设置工程默认的编译模式，如果没有设置，默认是 release 模式编译。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">set_defaultmode</span><strong>(</strong><span style="color:#ff00ff">"releasedbg"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">它等价于，<code>xmake f -m releasedbg</code>。</p> 
<h3 style="text-align:start">set_allowedplats</h3> 
<h4 style="text-align:start">设置允许编译的平台列表</h4> 
<p style="text-align:start">v2.5.6 以上版本才支持，用于设置工程支持的编译平台列表，如果用户指定了其他平台，会提示错误，这通常用于限制用户指定错误的无效平台。</p> 
<p style="text-align:start">如果没有设置，那么没有任何平台限制。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">set_allowedplats</span><strong>(</strong><span style="color:#ff00ff">"windows"</span><strong>,</strong> <span style="color:#ff00ff">"mingw"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">设置当前项目仅仅支持 windows 和 mingw 平台。</p> 
<h3 style="text-align:start">set_allowedarchs</h3> 
<h4 style="text-align:start">设置允许编译的平台架构</h4> 
<p style="text-align:start">v2.5.6 以上版本才支持，用于设置工程支持的编译架构列表，如果用户指定了其他架构，会提示错误，这通常用于限制用户指定错误的无效架构。</p> 
<p style="text-align:start">如果没有设置，那么没有任何架构限制。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">set_allowedarchs</span><strong>(</strong><span style="color:#ff00ff">"x64"</span><strong>,</strong> <span style="color:#ff00ff">"x86"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">当前项目，仅仅支持 x64/x86 平台。</p> 
<p style="text-align:start">我们也可以同时指定多个平台下允许的架构列表。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">set_allowedarchs</span><strong>(</strong><span style="color:#ff00ff">"windows|x64"</span><strong>,</strong> <span style="color:#ff00ff">"iphoneos|arm64"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">设置当前项目在 windows 上仅仅支持 x64 架构，并且在 iphoneos 上仅仅支持 arm64 架构。</p> 
<h3 style="text-align:start">set_allowedmodes</h3> 
<h4 style="text-align:start">设置允许的编译模式列表</h4> 
<p style="text-align:start">v2.5.6 以上版本才支持，用于设置工程支持的编译模式列表，如果用户指定了其他模式，会提示错误，这通常用于限制用户指定错误的无效模式。</p> 
<p style="text-align:start">如果没有设置，那么没有任何模式限制。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">set_allowedmodes</span><strong>(</strong><span style="color:#ff00ff">"release"</span><strong>,</strong> <span style="color:#ff00ff">"releasedbg"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">设置当前项目仅仅支持 release/releasedbg 两个编译模式。</p> 
<h2 style="text-align:start">更新内容</h2> 
<h3 style="text-align:start">新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1483" target="_blank">#1483</a>: 添加 <code>os.joinenvs()</code> 和改进包工具环境</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1523" target="_blank">#1523</a>: 添加 <code>set_allowedmodes</code>, <code>set_allowedplats</code> 和 <code>set_allowedarchs</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1523" target="_blank">#1523</a>: 添加 <code>set_defaultmode</code>, <code>set_defaultplat</code> 和 <code>set_defaultarch</code></li> 
</ul> 
<h3 style="text-align:start">改进</h3> 
<ul> 
 <li>改进 vs/vsxmake 工程插件支持 vs2022</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1513" target="_blank">#1513</a>: 改进 windows 预编译包的兼容性问题</li> 
 <li>改进 vcpkg 包在 windows 上的查找</li> 
 <li>改进对 Qt6 的支持</li> 
</ul> 
<h3 style="text-align:start">Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake-repo%2Fpull%2F489" target="_blank">#489</a>: 修复 run os.execv 带有过长环境变量值出现的一些问题</li> 
</ul>
                                        </div>
                                      
</div>
            