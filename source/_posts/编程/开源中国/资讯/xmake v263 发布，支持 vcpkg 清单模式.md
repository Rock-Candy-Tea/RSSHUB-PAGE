
---
title: 'xmake v2.6.3 发布，支持 vcpkg 清单模式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2430'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 09:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2430'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">Xmake</a><span> </span>是一个基于 Lua 的轻量级跨平台构建工具。</p> 
<p style="margin-left:0; margin-right:0">它非常的轻量，没有任何依赖，因为它内置了 Lua 运行时。</p> 
<p style="margin-left:0; margin-right:0">它使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p style="margin-left:0; margin-right:0">我们能够使用它像 Make/Ninja 那样可以直接编译项目，也可以像 CMake/Meson 那样生成工程文件，另外它还有内置的包管理系统来帮助用户解决 C/C++ 依赖库的集成使用问题。</p> 
<p style="margin-left:0; margin-right:0">目前，Xmake 主要用于 C/C++ 项目的构建，但是同时也支持其他 native 语言的构建，可以实现跟 C/C++ 进行混合编译，同时编译速度也是非常的快，可以跟 Ninja 持平。</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code>Xmake = Build backend + Project Generator + Package Manager
</code></pre> 
</div> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0">新版本改动</h2> 
<p style="margin-left:0; margin-right:0">这个版本主要新增下面几个特性：</p> 
<ol> 
 <li>通过 vcpkg 的清单模式实现 vcpkg 包的版本选择</li> 
 <li>python 模块构建支持</li> 
 <li>支持在 CMakeLists.txt 中集成 Xrepo/Xmake 包管理</li> 
</ol> 
<p style="margin-left:0; margin-right:0">剩下的主要是一些零散的功能改进和 Bugs 修复，可以看下文末的更新内容明细，一些比较大的改动，下面也会逐一说明。</p> 
<h2 style="margin-left:0; margin-right:0">新特性介绍</h2> 
<h3 style="margin-left:0; margin-right:0">支持 Vcpkg 清单模式</h3> 
<p style="margin-left:0; margin-right:0">新版本中，Xmake 新增了 vcpkg 清单模式支持，通过它，我们就能支持 vcpkg 包的版本选择，例如：</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"vcpkg::zlib 1.2.11+10"</span><strong style="color:#000000">)</strong>
<span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"vcpkg::fmt >=8.0.1"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">baseline</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"50fd3d9957195575849a49fa591e645f1d8e7156"</span><strong style="color:#000000">&#125;&#125;)</strong>
<span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"vcpkg::libpng"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">features</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#ff00ff">"apng"</span><strong style="color:#000000">&#125;&#125;&#125;)</strong>

<span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/*.cpp"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_packages</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"vcpkg::zlib"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"vcpkg::fmt"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"vcpkg::libpng"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="margin-left:0; margin-right:0">但是，vcpkg 的版本选择限制还是不少，必须要硬编码指定 baseline，而且还不支持<span> </span><code><=1.0</code>,<span> </span><code>1.x</code><span> </span>等版本语义选择，不过总比之前不能选择版本好了不少。</p> 
<h3 style="margin-left:0; margin-right:0">在 CMake 中使用 Xrepo 的依赖包管理</h3> 
<p style="margin-left:0; margin-right:0">我们新增了一个独立项目<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxrepo-cmake" target="_blank">xrepo-cmake</a>。</p> 
<p style="margin-left:0; margin-right:0">它是一个基于 Xrepo/Xmake 的 C/C++ 包管理器的 CMake 包装器。</p> 
<p style="margin-left:0; margin-right:0">这允许使用 CMake 来构建您的项目，同时使用 Xrepo 来管理依赖包。这个项目的部分灵感来自<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fconan-io%2Fcmake-conan" target="_blank">cmake-conan</a>。</p> 
<p style="margin-left:0; margin-right:0">此项目的示例用例：</p> 
<ul> 
 <li>想要使用 Xrepo 管理包的现有 CMake 项目。</li> 
 <li>必须使用 CMake，但想使用 Xrepo 管理的新项目包。</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0">使用来自官方存储库的包</h4> 
<p style="margin-left:0; margin-right:0">Xrepo 官方仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake-repo" target="_blank">xmake-repo</a></p> 
<p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxrepo-cmake%2Fblob%2Fmain%2Fxrepo.cmake" target="_blank">xrepo.cmake</a><span> </span>提供<code>xrepo_package</code>函数来管理包。</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:black">xrepo_package</span><strong style="color:#000000">(</strong>
    <span style="color:#ff00ff">"foo 1.2.3"</span>
    [CONFIGS feature1=true,feature2=false]
    [MODE debug|release]
    [OUTPUT verbose|diagnosis|quiet]
    [DIRECTORY_SCOPE]
<strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="margin-left:0; margin-right:0">一些函数参数直接对应于 Xrepo 命令选项。</p> 
<p style="margin-left:0; margin-right:0">调用<span> </span><code>xrepo_package(foo)</code><span> </span>后，有两种使用<span> </span><code>foo</code><span> </span>包的方法：</p> 
<ul> 
 <li>如果包提供 cmake 模块来查找它，则调用<span> </span><code>find_package(foo)</code>, 参考 CMake<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcmake.org%2Fcmake%2Fhelp%2Flatest%2Fcommand%2Ffind_package.html" target="_blank"><code>find_package</code></a><span> </span>文档了解更多详情</li> 
 <li>如果包不提供 cmake 模块，<code>foo_INCLUDE_DIR</code><span> </span>和<span> </span><code>foo_LINK_DIR</code><span> </span>变量将设置为包包含和库路径。使用这些变量在 CMake 代码中设置包含和库路径。</li> 
 <li>如果指定了<span> </span><code>DIRECTORY_SCOPE</code>，则<span> </span><code>xrepo_package</code><span> </span>将运行以下代码（这样用户只需要在<span> </span><code>target_link_libraries</code><span> </span>中指定库名称）</li> 
</ul> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:black">include_directories</span><strong style="color:#000000">(</strong>foo_INCLUDE_DIR<strong style="color:#000000">)</strong>
<span style="color:black">link_directories</span><strong style="color:#000000">(</strong>foo_LINK_DIR<strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="margin-left:0; margin-right:0">这是一个使用<span> </span><code>gflags</code><span> </span>包版本 2.2.2 的示例<span> </span><code>CMakeLists.txt</code><span> </span>由 Xrepo 管理。</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:black">cmake_minimum_required</span><strong style="color:#000000">(</strong>VERSION 3.13.0<strong style="color:#000000">)</strong>

<span style="color:black">project</span><strong style="color:#000000">(</strong>foo<strong style="color:#000000">)</strong>

<em># Download xrepo.cmake if not exists in build directory.</em>
<span style="color:black">if</span><strong style="color:#000000">(</strong>NOT EXISTS <span style="color:#ff00ff">"</span><span style="color:#ff00ff">$&#123;</span><span style="color:black">CMAKE_BINARY_DIR</span><span style="color:#ff00ff">&#125;</span><span style="color:#ff00ff">/xrepo.cmake"</span><strong style="color:#000000">)</strong>
    <span style="color:black">message</span><strong style="color:#000000">(</strong>STATUS <span style="color:#ff00ff">"Downloading xrepo.cmake from https://github.com/xmake-io/xrepo-cmake/"</span><strong style="color:#000000">)</strong>
    <em># mirror https://cdn.jsdelivr.net/gh/xmake-io/xrepo-cmake@main/xrepo.cmake</em>
    <span style="color:black">file</span><strong style="color:#000000">(</strong>DOWNLOAD <span style="color:#ff00ff">"https://raw.githubusercontent.com/xmake-io/xrepo-cmake/main/xrepo.cmake"</span>
                  <span style="color:#ff00ff">"</span><span style="color:#ff00ff">$&#123;</span><span style="color:black">CMAKE_BINARY_DIR</span><span style="color:#ff00ff">&#125;</span><span style="color:#ff00ff">/xrepo.cmake"</span>
                  TLS_VERIFY ON<strong style="color:#000000">)</strong>
<span style="color:black">endif</span><strong style="color:#000000">()</strong>

<em># Include xrepo.cmake so we can use xrepo_package function.</em>
<span style="color:black">include</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">$&#123;</span><span style="color:black">CMAKE_BINARY_DIR</span><span style="color:#ff00ff">&#125;</span>/xrepo.cmake<strong style="color:#000000">)</strong>

<em># Call `xrepo_package` function to use gflags 2.2.2 with specific configs.</em>
<span style="color:black">xrepo_package</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"gflags 2.2.2"</span> CONFIGS <span style="color:#ff00ff">"shared=true,mt=true"</span><strong style="color:#000000">)</strong>

<em># `xrepo_package` sets `gflags_DIR` variable in parent scope because gflags</em>
<em># provides cmake modules. So we can now call `find_package` to find gflags</em>
<em># package.</em>
<span style="color:black">find_package</span><strong style="color:#000000">(</strong>gflags CONFIG COMPONENTS shared<strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0">使用来自第三个存储库的包</h4> 
<p style="margin-left:0; margin-right:0">除了从官方维护的存储库安装软件包之外，Xrepo 还可以安装来自第三方包管理器的包，例如 vcpkg/conan/conda/pacman/homebrew/apt/dub/cargo。</p> 
<p style="margin-left:0; margin-right:0">关于命令行的使用，我们可以参考文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxrepo.xmake.io%2F%23%2Fgetting_started%3Fid%3Dinstall-packages-from-third-party-package-manager" target="_blank">Xrepo命令用法</a></p> 
<p style="margin-left:0; margin-right:0">我们也可以直接在 cmake 中使用它来安装来自第三方仓库的包，只需将仓库名称添加为命名空间即可。例如：<code>vcpkg::zlib</code>,<span> </span><code>conan::pcre2</code></p> 
<p>Conan</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:black">xrepo_package</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"conan::gflags/2.2.2"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p>Conda</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:black">xrepo_package</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"conda::gflags 2.2.2"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p>Vcpkg</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:black">xrepo_package</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"vcpkg::gflags"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p>Homebrew</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:black">xrepo_package</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"brew::gflags"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<h3 style="margin-left:0; margin-right:0">Python 模块构建支持</h3> 
<p style="margin-left:0; margin-right:0">我们可以用这个规则，配合 pybind11 生成 python 库模块，它会调整 python 库的模块名。</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_rules</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"mode.release"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"mode.debug"</span><strong style="color:#000000">)</strong>
<span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"pybind11"</span><strong style="color:#000000">)</strong>

<span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"example"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_rules</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"python.library"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/*.cpp"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_packages</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"pybind11"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_languages</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"c++11"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="margin-left:0; margin-right:0">带有 soabi：</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_rules</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"mode.release"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"mode.debug"</span><strong style="color:#000000">)</strong>
<span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"pybind11"</span><strong style="color:#000000">)</strong>

<span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"example"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_rules</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"python.library"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">soabi</span> <strong style="color:black">=</strong> <strong style="color:#800080">true</strong><strong style="color:#000000">&#125;)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/*.cpp"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_packages</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"pybind11"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_languages</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"c++11"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<h3 style="margin-left:0; margin-right:0">新增删除头文件列表接口</h3> 
<p style="margin-left:0; margin-right:0">通过此接口，可以从<span> </span><code>add_headerfiles</code><span> </span>接口添加的头文件列表中，删除指定的文件，例如：</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_headerfiles</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/*.h"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">remove_headerfiles</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/test.h"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="margin-left:0; margin-right:0">上面的例子，可以从<code>src</code>目录下添加除<code>test.h</code>以外的所有头文件，当然这个也可以通过<span> </span><code>add_headerfiles("src/*.h|test.h")</code><span> </span>来达到相同的目的，但是这种方式更加灵活。</p> 
<h3 style="margin-left:0; margin-right:0">新增 on_config 配置脚本</h3> 
<p style="margin-left:0; margin-right:0">在<span> </span><code>xmake config</code><span> </span>执行完成后，Build 之前会执行此脚本，通常用于编译前的配置工作。它与 on_load 不同的是，on_load 只要 target 被加载就会执行，执行时机更早。</p> 
<p style="margin-left:0; margin-right:0">如果一些配置，无法在 on_load 中过早配置，那么都可以在 on_config 中去配置它。</p> 
<p style="margin-left:0; margin-right:0">另外，它的执行时机比 before_build 还要早，大概的执行流程如下：</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code>on_load -> after_load -> on_config -> before_build -> on_build -> after_build
</code></pre> 
</div> 
<h3 style="margin-left:0; margin-right:0">内置 Github 代理镜像配置</h3> 
<p style="margin-left:0; margin-right:0">Xmake 提供了一些内置的镜像配置可以直接使用，例如 github 的镜像加速：</p> 
<div style="margin-left:0; margin-right:0"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> g --proxy_pac=github_mirror.lua
</span></code></pre> 
</div> 
<p style="margin-left:0; margin-right:0">我们不用自己编写 pac.lua，就可以直接使用它来加速 github 源的下载。</p> 
<h2 style="margin-left:0; margin-right:0">更新内容</h2> 
<h3 style="margin-left:0; margin-right:0">新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1928" target="_blank">#1298</a>: 支持 vcpkg 清单模式安装包，实现安装包的版本选择</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1896" target="_blank">#1896</a>: 添加<span> </span><code>python.library</code><span> </span>规则去构建 pybind 模块，并且支持 soabi</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1939" target="_blank">#1939</a>: 添加<span> </span><code>remove_files</code>,<span> </span><code>remove_headerfiles</code><span> </span>并且标记<span> </span><code>del_files</code><span> </span>作为废弃接口</li> 
 <li>将 on_config 作为正式的公开接口，用于 target 和 rule</li> 
 <li>添加 riscv32/64 支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1970" target="_blank">#1970</a>: 添加 CMake wrapper 支持在 CMakelists 中去调用 xrepo 集成 C/C++ 包</li> 
 <li>添加内置的 github 镜像加速 pac 代理文件,<span> </span><code>xmake g --proxy_pac=github_mirror.lua</code></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0">改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1923" target="_blank">#1923</a>: 改进构建 linux 驱动，支持设置自定义 linux-headers 路径</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1962" target="_blank">#1962</a>: 改进 armclang 工具链去支持构建 asm</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F1959" target="_blank">#1959</a>: 改进 vstudio 工程生成器</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1969" target="_blank">#1969</a>: 添加默认的 option 描述</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0">Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1875" target="_blank">#1875</a>: 修复部署生成 Android Qt 程序包失败问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1973" target="_blank">#1973</a>: 修复合并静态库</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F1982" target="_blank">#1982</a>: 修复 clang 下对 c++20 子模块的依赖构建</li> 
</ul>
                                        </div>
                                      
</div>
            