
---
title: 'xmake v2.5.8 发布，新增 Pascal_Swig 程序和 Lua53 运行时支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6016'
author: 开源中国
comments: false
date: Sat, 09 Oct 2021 07:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6016'
---

<div>   
<div class="content">
                                                                    
                                                        <hr> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">xmake</a> 是一个基于 Lua 的轻量级跨平台构建工具，使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p>这个版本，我们主要增加了对 Pascal 语言项目和 Swig 模块的构建支持，而对于上个版本新增的 Vala 语言支持，我们也做了进一步改进，增加了对动态库和静态库的构建支持。</p> 
<p>除此之外，xmake 现在也已经支持了可选的 Lua5.3 运行时，提供更好的跨平台支持能力，目前 xmake 已经能够在 LoongArch 架构上正常运行。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2>新特性介绍</h2> 
<h3>Pascal 语言支持</h3> 
<p>目前，我们可以使用跨平台的 Free pascal 工具链 fpc 去编译构建 Pascal 程序，例如：</p> 
<h4>控制台程序</h4> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")
target("test")
    set_kind("binary")
    add_files("src/*.pas")
</code></pre> 
<h4>动态库程序</h4> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")
target("foo")
    set_kind("shared")
    add_files("src/foo.pas")

target("test")
    set_kind("binary")
    add_deps("foo")
    add_files("src/main.pas")
</code></pre> 
<p>我们也可以通过 <code>add_fcflags()</code> 接口添加 Pascal 代码相关的编译选项。</p> 
<p>更多例子见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fmaster%2Ftests%2Fprojects%2Fpascal" target="_blank">Pascal examples</a></p> 
<h3>Vala 库编译支持</h3> 
<p>上个版本，我们新增了对 Vala 语言的支持，但是之前只能支持控制台程序的编译，无法生成库文件。而这个版本中，我们额外增加了对静态库和动态库的编译支持。</p> 
<h4>静态库程序</h4> 
<p>我们能够通过 <code>add_values("vala.header", "mymath.h")</code> 设置导出的接口头文件名，通过 <code>add_values("vala.vapi", "mymath-1.0.vapi")</code> 设置导出的 vapi 文件名。</p> 
<pre><code class="language-lua">add_rules("mode.release", "mode.debug")

add_requires("glib")

target("mymath")
    set_kind("static")
    add_rules("vala")
    add_files("src/mymath.vala")
    add_values("vala.header", "mymath.h")
    add_values("vala.vapi", "mymath-1.0.vapi")
    add_packages("glib")

target("test")
    set_kind("binary")
    add_deps("mymath")
    add_rules("vala")
    add_files("src/main.vala")
    add_packages("glib")
</code></pre> 
<h4>动态库程序</h4> 
<pre><code class="language-lua">add_rules("mode.release", "mode.debug")

add_requires("glib")

target("mymath")
    set_kind("shared")
    add_rules("vala")
    add_files("src/mymath.vala")
    add_values("vala.header", "mymath.h")
    add_values("vala.vapi", "mymath-1.0.vapi")
    add_packages("glib")

target("test")
    set_kind("binary")
    add_deps("mymath")
    add_rules("vala")
    add_files("src/main.vala")
    add_packages("glib")
</code></pre> 
<p>更多例子见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fmaster%2Ftests%2Fprojects%2Fvala" target="_blank">Vala examples</a></p> 
<h3>Swig 模块支持</h3> 
<p>我们提供了 <code>swig.c</code> 和 <code>swig.cpp</code> 规则，可以对指定的脚本语言，调用 swig 程序生成 c/c++ 模块接口代码，然后配合 xmake 的包管理系统实现完全自动化的模块和依赖包整合。</p> 
<p>相关 issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1622" target="_blank">#1622</a></p> 
<h4>Lua/C 模块</h4> 
<pre><code class="language-lua">add_rules("mode.release", "mode.debug")
add_requires("lua")

target("example")
    add_rules("swig.c", &#123;moduletype = "lua"&#125;)
    add_files("src/example.i", &#123;swigflags = "-no-old-metatable-bindings"&#125;)
    add_files("src/example.c")
    add_packages("lua")
</code></pre> 
<p>其中，swigflags 可以设置传递一些 swig 特有的 flags 选项。</p> 
<h4>Python/C 模块</h4> 
<pre><code class="language-lua">add_rules("mode.release", "mode.debug")
add_requires("python 3.x")

target("example")
    add_rules("swig.c", &#123;moduletype = "python"&#125;)
    add_files("src/example.i", &#123;scriptdir = "share"&#125;)
    add_files("src/example.c")
    add_packages("python")
</code></pre> 
<p>如果设置了 scriptdir，那么我们执行安装的时候，会将对应模块的 python wrap 脚本安装到指定目录。</p> 
<h4>Python/C++ 模块</h4> 
<pre><code class="language-lua">add_rules("mode.release", "mode.debug")
add_requires("python 3.x")

target("example")
    add_rules("swig.cpp", &#123;moduletype = "python"&#125;)
    add_files("src/example.i", &#123;scriptdir = "share"&#125;)
    add_files("src/example.cpp")
    add_packages("python")
</code></pre> 
<h3>Lua5.3 运行时支持</h3> 
<p>xmake 之前一直使用的 Luajit 作为默认的运行时，因为当初考虑到 Luajit 相对更加快速，并且固定的 lua 5.1 语法更加适合 xmake 内部实现的需要。</p> 
<p>但是考虑到 Luajit 的更新不给力，作者维护不是很积极，并且它的跨平台性比较差，对于一些新出的架构，比如：Loongarch，riscv 等支持不及时，这多少限制了 xmake 的平台支持力度。</p> 
<p>为此，新版本中，我们也将 Lua5.3 作为可选的运行时内置了进来，我们只需要通过下面的命令编译安装 xmake，就可以从 Luajit 切换到 Lua5.3 运行时：</p> 
<h4>Linux/macOS</h4> 
<pre><code class="language-bash">$ make RUNTIME=lua
</code></pre> 
<h4>Windows</h4> 
<pre><code class="language-bash">$ cd core
$ xmake f --runtime=lua
$ xmake
</code></pre> 
<p>目前，当前版本还是默认采用的 luajit 运行时，用户可以根据自己的需求切换到 Lua5.3 运行时，但这对于用户的项目 xmake.lua 配置脚本几乎没有任何兼容性影响。</p> 
<p>因为 xmake 的配置接口都已经做了一层的抽象封装，一些 Luajit/Lua5.3 存在兼容性差异的原生接口是不会开放给用户使用的，所以对项目构建来说，是完全无感知的。</p> 
<p>唯一的区别就是，带有 Lua5.3 的 xmake 支持更多的平台和架构。</p> 
<h4>性能对比</h4> 
<p>我做过一些基础构建测试，不管是启动时间，构建性能还是内存占用，Lua5.3 和 Luajit 的 xmake 都几乎没有任何差别。因为对于构建系统，主要的性能瓶颈是在编译器上，自身脚本的损耗占比是非常小的。</p> 
<p>而且 xmake 内部的一些底层 Lua 模块，比如 io，字符编码，字符串操作等，都自己用 c 代码全部重写过的，完全不依赖特定的 Lua 运行时引擎。</p> 
<h4>是否会考虑默认切换到 Lua?</h4> 
<p>由于我们刚刚支持 Lua5.3，尽管目前测试下来已经比较稳定，但是为了确保用户环境不受到任何影响，我们还需要再观察一段时间，短期还是默认使用 Luajit。</p> 
<p>等到 2.6.1 版本开始，我们会全面开始切换到 Lua5.3 作为默认的运行时环境，大家有兴趣的话，也可以线帮忙测试下，如果遇到问题，欢迎到 issues 上反馈。</p> 
<h4>LoongArch 架构支持</h4> 
<p>由于我们增加了 Lua5.3 运行时支持，所以现在我们已经可以支持再 LoongArch 架构上运行 xmake，并且所有测试例子都已经测试通过。</p> 
<h4>Lua 5.4</h4> 
<p>目前，我们对 Lua 5.4 还保持观望状态，如果后面等 lua5.4 稳定了，我们也会尝试考虑继续升级到 Lua5.4。</p> 
<h3>第三方源码混合编译支持</h3> 
<h4>集成 CMake 代码库</h4> 
<p>新版本中，我们已经能够通过 xmake 的包模式直接集成自己项目中带有 CMakeLists.txt 的代码库，而不是通过远程下载安装。</p> 
<p>相关 issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1714" target="_blank">#1714</a></p> 
<p>例如，我们有如下项目结构：</p> 
<pre><code>├── foo
│   ├── CMakeLists.txt
│   └── src
│       ├── foo.c
│       └── foo.h
├── src
│   └── main.c
├── test.lua
└── xmake.lua
</code></pre> 
<p>foo 目录下是一个使用 cmake 维护的静态库，而根目录下使用了 xmake 来维护，我们可以在 xmake.lua 中通过定义 <code>package("foo")</code> 包来描述如何构建 foo 代码库。</p> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

package("foo")
    add_deps("cmake")
    set_sourcedir(path.join(os.scriptdir(), "foo"))
    on_install(function (package)
        local configs = &#123;&#125;
        table.insert(configs, "-DCMAKE_BUILD_TYPE=" .. (package:debug() and "Debug" or "Release"))
        table.insert(configs, "-DBUILD_SHARED_LIBS=" .. (package:config("shared") and "ON" or "OFF"))
        import("package.tools.cmake").install(package, configs)
    end)
    on_test(function (package)
        assert(package:has_cfuncs("add", &#123;includes = "foo.h"&#125;))
    end)
package_end()

add_requires("foo")

target("demo")
    set_kind("binary")
    add_files("src/main.c")
    add_packages("foo")
</code></pre> 
<p>其中，我们通过 <code>set_sourcedir()</code> 来设置 foo 包的代码目录位置，然后通过 import 导入 <code>package.tools.cmake</code> 辅助模块来调用 cmake 构建代码，xmake 会自动获取生成的 libfoo.a 和对应的头文件。</p> 
<p>!> 如果仅仅本地源码集成，我们不需要额外设置 <code>add_urls</code> 和 <code>add_versions</code>。</p> 
<p>关于包的配置描述，详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fpackage%2Fremote_package%3Fid%3D%25e5%258c%2585%25e6%258f%258f%25e8%25bf%25b0%25e8%25af%25b4%25e6%2598%258e" target="_blank">包描述说明</a></p> 
<p>定义完包后，我们就可以通过 <code>add_requires("foo")</code> 和 <code>add_packages("foo")</code> 来集成使用它了，就跟集成远程包一样的使用方式。</p> 
<p>另外，<code>on_test</code> 是可选的，如果想要严格检测包的编译安装是否成功，可以在里面做一些测试。</p> 
<p>完整例子见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fmaster%2Ftests%2Fprojects%2Fc%2Flibrary_with_cmakelists" target="_blank">Library with CMakeLists</a></p> 
<h4>集成 autoconf 代码库</h4> 
<p>我们也可以使用 <code>package.tools.autoconf</code> 来本地集成带有 autoconf 维护的第三方代码库。</p> 
<pre><code class="language-lua">package("pcre2")

    set_sourcedir(path.join(os.scriptdir(), "3rd/pcre2"))

    add_configs("jit", &#123;description = "Enable jit.", default = true, type = "boolean"&#125;)
    add_configs("bitwidth", &#123;description = "Set the code unit width.", default = "8", values = &#123;"8", "16", "32"&#125;&#125;)

    on_load(function (package)
        local bitwidth = package:config("bitwidth") or "8"
        package:add("links", "pcre2-" .. bitwidth)
        package:add("defines", "PCRE2_CODE_UNIT_WIDTH=" .. bitwidth)
        if not package:config("shared") then
            package:add("defines", "PCRE2_STATIC")
        end
    end)

    on_install("macosx", "linux", "mingw", function (package)
        local configs = &#123;&#125;
        table.insert(configs, "--enable-shared=" .. (package:config("shared") and "yes" or "no"))
        table.insert(configs, "--enable-static=" .. (package:config("shared") and "no" or "yes"))
        if package:debug() then
            table.insert(configs, "--enable-debug")
        end
        if package:config("pic") ~= false then
            table.insert(configs, "--with-pic")
        end
        if package:config("jit") then
            table.insert(configs, "--enable-jit")
        end
        local bitwidth = package:config("bitwidth") or "8"
        if bitwidth ~= "8" then
            table.insert(configs, "--disable-pcre2-8")
            table.insert(configs, "--enable-pcre2-" .. bitwidth)
        end
        import("package.tools.autoconf").install(package, configs)
    end)

    on_test(function (package)
        assert(package:has_cfuncs("pcre2_compile", &#123;includes = "pcre2.h"&#125;))
    end)
</code></pre> 
<p><code>package.tools.autoconf</code> 和 <code>package.tools.cmake</code> 模块都是可以支持 mingw/cross/iphoneos/android 等交叉编译平台和工具链的，xmake 会自动传递对应的工具链进去，用户不需要做任何其他事情。</p> 
<h4>集成其他构建系统</h4> 
<p>我们还支持集成 Meson/Scons/Make 等其他构建系统维护的代码库，仅仅只需要导入对应的构建辅助模块，这里就不一一细讲了，我们可以进一步查阅文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fpackage%2Flocal_3rd_source_library" target="_blank">集成本地第三方源码库</a></p> 
<h3>改进编译器特性检测</h3> 
<p>在之前的版本中，我们可以通过 <code>check_features</code> 辅助接口来检测指定的编译器特性，比如：</p> 
<pre><code class="language-lua">includes("check_features.lua")

target("test")
    set_kind("binary")
    add_files("*.c")
    add_configfiles("config.h.in")
    configvar_check_features("HAS_CONSTEXPR", "cxx_constexpr")
    configvar_check_features("HAS_CONSEXPR_AND_STATIC_ASSERT", &#123;"cxx_constexpr", "c_static_assert"&#125;, &#123;languages = "c++11"&#125;)
</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fconfig.h.in" target="_blank">config.h.in</a></p> 
<pre><code class="language-c">$&#123;define HAS_CONSTEXPR&#125;
$&#123;define HAS_CONSEXPR_AND_STATIC_ASSERT&#125;
</code></pre> 
<p>config.h</p> 
<pre><code class="language-c">/* #undef HAS_CONSTEXPR */
#define HAS_CONSEXPR_AND_STATIC_ASSERT 1
</code></pre> 
<p>如果当前 cxx_constexpr 特性支持，就会在 config.h 中启用 HAS_CONSTEXPR 宏。</p> 
<h4>新增 C/C++ 标准支持检测</h4> 
<p>2.5.8 之后，我们继续新增了对 cstd 和 c++ std 版本检测支持，相关 issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1715" target="_blank">#1715</a></p> 
<p>例如：</p> 
<pre><code class="language-lua">configvar_check_features("HAS_CXX_STD_98", "cxx_std_98")
configvar_check_features("HAS_CXX_STD_11", "cxx_std_11", &#123;languages = "c++11"&#125;)
configvar_check_features("HAS_CXX_STD_14", "cxx_std_14", &#123;languages = "c++14"&#125;)
configvar_check_features("HAS_CXX_STD_17", "cxx_std_17", &#123;languages = "c++17"&#125;)
configvar_check_features("HAS_CXX_STD_20", "cxx_std_20", &#123;languages = "c++20"&#125;)
configvar_check_features("HAS_C_STD_89", "c_std_89")
configvar_check_features("HAS_C_STD_99", "c_std_99")
configvar_check_features("HAS_C_STD_11", "c_std_11", &#123;languages = "c11"&#125;)
configvar_check_features("HAS_C_STD_17", "c_std_17", &#123;languages = "c17"&#125;)
</code></pre> 
<h4>新增编译器内置宏检测</h4> 
<p>我们还能检测编译器存在一些内置的宏定义，比如：<code>__GNUC__</code> 等，我们可以通过 <code>check_macros</code> 和 <code>configvar_check_macros</code> 辅助脚本来检测它们是否存在。</p> 
<p>相关 issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1715" target="_blank">#1715</a></p> 
<pre><code class="language-lua">-- 检测宏是否定义
configvar_check_macros("HAS_GCC", "__GNUC__")
-- 检测宏没有被定义
configvar_check_macros("NO_GCC", "__GNUC__", &#123;defined = false&#125;)
-- 检测宏条件
configvar_check_macros("HAS_CXX20", "__cplusplus >= 202002L", &#123;languages = "c++20"&#125;)
</code></pre> 
<h3>增加对 Qt 4.x 的支持</h3> 
<p>除了 Qt 5.x 和 6.x，我们对于一些基于 Qt 4.x 的老项目，xmake 也增加了支持。</p> 
<h3>增加对 Android NDK r23 的支持</h3> 
<p>由于 google 对 Android NDK 的一些结构改动，导致 r23 影响了 xmake 对 android 项目部分编译特性的支持，在这个版本中，我们也做了修复。</p> 
<h3>修复 vsxmake 插件 Unicode 编码问题</h3> 
<p>另外，如果基于 Unicode 作为项目目录，那么生成的 vsxmake 项目会收到影响，导致 vs 项目编译和访问上存在很多问题，我们也在新版本中做了修复。</p> 
<h2>更新内容</h2> 
<h3>新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F388" target="_blank">#388</a>: Pascal 语言支持，可以使用 fpc 来编译 free pascal</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1682" target="_blank">#1682</a>: 添加可选的额lua5.3 运行时替代 luajit，提供更好的平台兼容性。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1622" target="_blank">#1622</a>: 支持 Swig</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1714" target="_blank">#1714</a>: 支持内置 cmake 等第三方项目的混合编译</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1715" target="_blank">#1715</a>: 支持探测编译器语言标准特性，并且新增 <code>check_macros</code> 检测接口</li> 
 <li>xmake 支持在 Loongarch 架构上运行</li> 
</ul> 
<h3>改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1618" target="_blank">#1618</a>: 改进 vala 支持构建动态库和静态库程序</li> 
 <li>改进 Qt 规则去支持 Qt 4.x</li> 
 <li>改进 <code>set_symbols("debug")</code> 支持 clang/windows 生成 pdb 文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1638" target="_blank">#1638</a>: 改进合并静态库</li> 
 <li>改进 on_load/after_load 去支持动态的添加 target deps</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F1675" target="_blank">#1675</a>: 针对 mingw 平台，重命名动态库和导入库文件名后缀</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1694" target="_blank">#1694</a>: 支持在 set_configvar 中定义一个不带引号的字符串变量</li> 
 <li>改进对 Android NDK r23 的支持</li> 
 <li>为 <code>set_languages</code> 新增 <code>c++latest</code> 和 <code>clatest</code> 配置值</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1720" target="_blank">#1720</a>: 添加 <code>save_scope</code> 和 <code>restore_scope</code> 去修复 <code>check_xxx</code> 相关接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1726" target="_blank">#1726</a>: 改进 compile_commands 生成器去支持 nvcc</li> 
</ul> 
<h3>Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1671" target="_blank">#1671</a>: 修复安装预编译包后，*.cmake 里面的一些不正确的绝对路径</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1689" target="_blank">#1689</a>: 修复 vsxmake 插件的 unicode 字符显示和加载问题</li> 
</ul>
                                        </div>
                                      
</div>
            