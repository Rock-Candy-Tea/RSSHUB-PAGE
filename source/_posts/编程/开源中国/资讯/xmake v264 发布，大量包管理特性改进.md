
---
title: 'xmake v2.6.4 发布，大量包管理特性改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5095'
author: 开源中国
comments: false
date: Mon, 07 Mar 2022 14:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5095'
---

<div>   
<div class="content">
                                                                                            <hr> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">Xmake</a> 是一个基于 Lua 的轻量级跨平台构建工具。</p> 
<p>它非常的轻量，没有任何依赖，因为它内置了 Lua 运行时。</p> 
<p>它使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p>我们能够使用它像 Make/Ninja 那样可以直接编译项目，也可以像 CMake/Meson 那样生成工程文件，另外它还有内置的包管理系统来帮助用户解决 C/C++ 依赖库的集成使用问题。</p> 
<p>目前，Xmake 主要用于 C/C++ 项目的构建，但是同时也支持其他 native 语言的构建，可以实现跟 C/C++ 进行混合编译，同时编译速度也是非常的快，可以跟 Ninja 持平。</p> 
<pre><code>Xmake = Build backend + Project Generator + Package Manager
</code></pre> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2>新特性介绍</h2> 
<h3>更灵活的包扩展</h3> 
<p>现在，我们可以通过 <code>set_base</code> 接口去继承一个已有的包的全部配置，然后在此基础上重写部分配置。</p> 
<p>这通常在用户自己的项目中，修改 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake-repo" target="_blank">xmake-repo</a> 官方仓库的内置包比较有用，比如：修复改 urls，修改版本列表，安装逻辑等等。</p> 
<p>例如，修改内置 zlib 包的 url，切到自己的 zlib 源码地址。</p> 
<pre><code class="language-lua">package("myzlib")
    set_base("zlib")
    set_urls("https://github.com/madler/zlib.git")
package_end()

add_requires("myzlib", &#123;system = false, alias = "zlib"&#125;)

target("test")
    set_kind("binary")
    add_files("src/*.c")
    add_packages("zlib")
</code></pre> 
<p>我们也可以用来单纯添加一个别名包。</p> 
<pre><code class="language-lua">package("onetbb")
    set_base("tbb")
</code></pre> 
<p>我们可以通过 <code>add_requires("onetbb")</code> 集成安装 tbb 包，只是包名不同而已。</p> 
<h3>包管理支持工具链切换</h3> 
<p>之前，我们限制了只能在 cross 平台下切换包安装的工具链，新版本中，我们可以支持更多平台下，对工具链的切换。</p> 
<p>例如：</p> 
<pre><code class="language-bash">$ xrepo install --toolchains=clang zlib
</code></pre> 
<p>我们可以在 linux 等平台上，快速切换到 clang 工具链编译安装 zlib 库。</p> 
<p>我们也可以在 xmake.lua 的配置文件中去切换他们。</p> 
<pre><code class="language-lua">add_requires("zlib", &#123;configs = &#123;toolchains = "gcc-11"&#125;&#125;)
</code></pre> 
<p>不同的工具链安装的 zlib 包，会被分别存储在不同目录，互不干扰，不会存在编译器差异导致的链接兼容问题。</p> 
<h3>内置的包虚拟环境</h3> 
<p>Xrepo 命令之前已经很好的支持了包虚拟环境管理，<code>xrepo env shell</code>，但是对于复杂的包环境，还是需要用户自己配置一个 xmake.lua 文件，用于管理自己的包环境。</p> 
<p>例如，我们需要一个常用的开发环境 shell，默认带有 cmake, python 和 vs/autoconf 等常用的开发工具链，我们需要自己起一个配置文件 devel.lua。</p> 
<pre><code class="language-lua">add_requires("cmake")
add_requires("python")
if is_host("linux", "bsd", "macosx") then
    add_requires("pkg-config", "autoconf", "automake", "libtool")
elseif is_host("windows") then
    set_toolchains("msvc")
end
</code></pre> 
<p>然后，执行下面的命令去导入到全局配置。</p> 
<pre><code class="language-bash">$ xrepo env --add devel.lua
</code></pre> 
<p>这样，我们可以通过下面的命令，去加载 shell 绑定这个环境：</p> 
<pre><code class="language-bash">$ xrepo env -b devel shell
> cmake --version
cmake version 3.19.3
</code></pre> 
<p>而在新版本中，我们内置了一些常用的环境，可以通过 <code>xrepo env -l</code> 查看：</p> 
<pre><code class="language-bash">$ xrepo env -l
  - msvc
  - llvm-mingw
  - llvm
  - mingw-w64
  - devel
  - python3
  - depot_tools
  - python2
</code></pre> 
<p>其中 devel 也在里面，所以，我们只需要执行 <code>xrepo env -b devel shell</code> 就可以带起一个 devel 开发环境，而不需要自己配置它们。</p> 
<p>像 python, msvc 等也都是一些比较常用的环境，都可以直接使用。</p> 
<p>当然，我们也支持临时在本地创建一个 xmake.lua 来配置加载包环境，而不放置到全局配置中去。</p> 
<h3>自定义安装包下载</h3> 
<p>我们可以通过新增的 <code>on_download</code> 接口，自定义包的下载逻辑，通常用不到，使用 Xmake 的内置下载就足够了。</p> 
<p>如果用户自建私有仓库，对包的下载有更复杂的鉴权机制，特殊处理逻辑，那么可以重写内部的下载逻辑来实现。</p> 
<pre><code class="language-lua">on_download(function (package, opt)
    -- download packages:urls() to opt.sourcedir
end)
</code></pre> 
<p>opt 参数里面，可以获取到下载包的目的源码目录 <code>opt.sourcedir</code>，我们只需要从 <code>package:urls()</code> 获取到包地址，下载下来就可以了。</p> 
<p>然后，根据需要，添加一些自定义的处理逻辑。另外，自己可以添加下载缓存处理等等。</p> 
<h3>ASN.1 程序构建支持</h3> 
<p>ASN.1 程序，需要借助 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvlm%2Fasn1c" target="_blank">ASN.1 Compiler</a> 去生成相关的 .c 文件参与项目编译。</p> 
<p>而 Xmake 内置提供了 <code>add_rules("asn1c")</code> 规则去处理 <code>.c</code> 文件生成，<code>add_requires("asn1c")</code> 自动拉取集成 ASN.1 编译器工具。</p> 
<p>下面是一个基础的配置例子：</p> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")
add_requires("asn1c")

target("test")
    set_kind("binary")
    add_files("src/*.c")
    add_files("src/*.asn1")
    add_rules("asn1c")
    add_packages("asn1c")
</code></pre> 
<p>具体见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fmaster%2Ftests%2Fprojects%2Fc%2Fasn1c" target="_blank">完整例子工程</a>。</p> 
<h3>支持全平台构建 Swift 程序</h3> 
<p>之前，Xmake 仅支持 macOS 下借助 Xcode 工具链实现对 Swift 程序的构建，新版本中，我们也进行了改进，可以独立使用 swift 工具链，支持在 linux/windows 上构架 swift 程序，用法跟之前相同。</p> 
<h3>支持指定符号列表导出</h3> 
<p>在之前的版本中，我们提供了 <code>utils.symbols.export_all</code> 对 windows 的 dll 库实现自动的完整符号导出。</p> 
<p>这尽管很方便，但只能支持 windows 程序，并且全量导出对生成的 dll 大小不好控制，有可能会存在不少根本不需要的内部符号被导出。</p> 
<p>而，我们新版本提供的 <code>utils.symbols.export_list</code> 规则，可以在 xmake.lua 里面直接定义导出的符号列表，例如：</p> 
<pre><code class="language-lua">target("foo")
    set_kind("shared")
    add_files("src/foo.c")
    add_rules("utils.symbols.export_list", &#123;symbols = &#123;
        "add",
        "sub"&#125;&#125;)
</code></pre> 
<p>或者，在 <code>*.export.txt</code> 文件中添加导出的符号列表。</p> 
<pre><code class="language-lua">target("foo2")
    set_kind("shared")
    add_files("src/foo.c")
    add_files("src/foo.export.txt")
    add_rules("utils.symbols.export_list")
</code></pre> 
<p>完整的工程例子见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fdev%2Ftests%2Fprojects%2Fc%2Fshared_library_export_list" target="_blank">导出符号例子</a></p> 
<p>通过指定符号导出，我们可以使得生成的动态库尽可能的小，无关的内部符号完全不去导出它们，另外这个规则支持 linux, macOS 和 windows，更加的通用。</p> 
<p>它内部会自动使用 .def, version scripts 和 <code>--exported_symbols_list</code> 去处理符号导出。</p> 
<h3>内置支持 linker scripts</h3> 
<p>新版中，我们也内置了 对 linker scripts 和 version scripts 文件的支持，我们可以使用 <code>add_files</code> 直接添加它们，而不需要配置 <code>add_ldflags("-Txxx.lds")</code>。</p> 
<p>当前支持 <code>.ld</code> 和 <code>.lds</code> 作为 linker scripts 配置文件来添加：</p> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

target("test")
    add_deps("foo")
    set_kind("binary")
    add_files("src/main.c")
    add_files("src/main.lds")
</code></pre> 
<p>我们也支持 <code>.ver</code>, <code>.map</code> 后缀文件作为 version script 来添加。</p> 
<pre><code class="language-lua">target("foo")
    set_kind("shared")
    add_files("src/foo.c")
    add_files("src/foo.map")
</code></pre> 
<p>foo.map 文件内容如下：</p> 
<pre><code>&#123;
    global:
        foo;

    local:
        *;
&#125;;
</code></pre> 
<h2>更新内容</h2> 
<h3>新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2011" target="_blank">#2011</a>: 支持继承和局部修改官方包，例如对现有的包更换 urls 和 versions</li> 
 <li>支持在 sparc, alpha, powerpc, s390x 和 sh4 上编译运行 xmake</li> 
 <li>为 package() 添加 on_download 自定义下载</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2021" target="_blank">#2021</a>: 支持 Linux/Windows 下构建 Swift 程序</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2024" target="_blank">#2024</a>: 添加 asn1c 支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2031" target="_blank">#2031</a>: 为 add_files 增加 linker scripts 和 version scripts 支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2033" target="_blank">#2033</a>: 捕获 ctrl-c 去打印当前运行栈，用于调试分析卡死问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2059" target="_blank">#2059</a>: 添加 <code>xmake update --integrate</code> 命令去整合 shell</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2070" target="_blank">#2070</a>: 添加一些内置的 xrepo env 环境配置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2117" target="_blank">#2117</a>: 支持为任意平台传递工具链到包</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2121" target="_blank">#2121</a>: 支持导出指定的符号列表，可用于减少动态库的大小</li> 
</ul> 
<h3>改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2036" target="_blank">#2036</a>: 改进 xrepo 支持从配置文件批量安装包，例如：<code>xrepo install xxx.lua</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2039" target="_blank">#2039</a>: 改进 vs generator 的 filter 目录展示</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2025" target="_blank">#2025</a>: 支持为 phony 和 headeronly 目标生成 vs 工程</li> 
 <li>优化 vs 和 codesign 的探测速度</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2077" target="_blank">#2077</a>: 改进 vs 工程生成器去支持 cuda</li> 
</ul> 
<h3>Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2005" target="_blank">#2005</a>: 修复 path.extension</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2008" target="_blank">#2008</a>: 修复 windows manifest 文件编译</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2016" target="_blank">#2016</a>: 修复 vs project generator 里，对象文件名冲突导致的编译失败</li> 
</ul>
                                        </div>
                                      
</div>
            