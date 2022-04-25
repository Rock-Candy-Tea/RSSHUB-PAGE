
---
title: 'xmake v2.6.5 发布，远程编译支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://xmake.io/assets/img/manual/filegroup1.png'
author: 开源中国
comments: false
date: Mon, 25 Apr 2022 14:56:00 GMT
thumbnail: 'https://xmake.io/assets/img/manual/filegroup1.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">Xmake</a><span> </span>是一个基于 Lua 的轻量级跨平台构建工具。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">它非常的轻量，没有任何依赖，因为它内置了 Lua 运行时。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">它使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们能够使用它像 Make/Ninja 那样可以直接编译项目，也可以像 CMake/Meson 那样生成工程文件，另外它还有内置的包管理系统来帮助用户解决 C/C++ 依赖库的集成使用问题。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">目前，Xmake 主要用于 C/C++ 项目的构建，但是同时也支持其他 native 语言的构建，可以实现跟 C/C++ 进行混合编译，同时编译速度也是非常的快，可以跟 Ninja 持平。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code>Xmake = Build backend + Project Generator + Package Manager
</code></pre> 
</div> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">新特性介绍</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start">远程编译支持</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">新版本提供了远程编译支持，我们可以通过它可以远程服务器上编译代码，远程运行和调试。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">服务器可以部署在 Linux/MacOS/Windows 上，实现跨平台编译，例如：在 Linux 上编译运行 Windows 程序，在 Windows 上编译运行 macOS/Linux 程序。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">相比 ssh 远程登入编译，它更加的稳定，使用更加流畅，不会因为网络不稳定导致 ssh 终端输入卡顿，也可以实现本地快速编辑代码文件。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">甚至我们可以在 vs/sublime/vscode/idea 等编辑器和IDE 中无缝实现远程编译，而不需要依赖 IDE 本身对远程编译的支持力度。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">开启服务</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service
</span><remote_build_server>: listening 0.0.0.0:90091 ..
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以开启服务的同时，回显详细日志信息。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service -vD
</span><remote_build_server>: listening 0.0.0.0:90091 ..
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">以 Daemon 模式开启服务</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service --start
</span><u>$ </u><span style="color:black">xmake</span><span> service --restart
</span><u>$ </u><span style="color:black">xmake</span><span> service --stop
</span></code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">配置服务端</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们首先，运行<span> </span><code>xmake service</code><span> </span>命令，它会自动生成一个默认的<span> </span><code>service.conf</code><span> </span>配置文件，存储到<span> </span><code>~/.xmake/service.conf</code>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">然后，我们编辑它，修复服务器的监听端口（可选）。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><strong style="color:#000000">&#123;</strong>
    <span style="color:#000000">logfile</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/logs.txt"</span><strong style="color:#000000">,</strong>
    <span style="color:#000000">remote_build</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong>
        <span style="color:#000000">server</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong>
            <span style="color:#000000">listen</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"0.0.0.0:90091"</span>
        <strong style="color:#000000">&#125;</strong>
    <strong style="color:#000000">&#125;</strong>
<strong style="color:#000000">&#125;</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">配置客户端</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们还是编辑这个文件<span> </span><code>~/.xmake/service.conf</code>，配置客户端需要连接的服务器地址。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><strong style="color:#000000">&#123;</strong>
    <span style="color:#000000">logfile</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/logs.txt"</span><strong style="color:#000000">,</strong>
    <span style="color:#000000">remote_build</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong>
        <span style="color:#000000">client</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong>
            <span style="color:#000000">connect</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"192.168.56.101:90091"</span><strong style="color:#000000">,</strong>
        <strong style="color:#000000">&#125;</strong>
    <strong style="color:#000000">&#125;</strong>
<strong style="color:#000000">&#125;</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">导入给定的配置文件</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以通过下面的命令，导入指定的配置文件。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service --config=/tmp/service.conf
</span></code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">连接远程的服务器</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">接下来，我们只需要进入需要远程编译的工程根目录，执行<span> </span><code>xmake service --connect</code><span> </span>命令，进行连接。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> create test
</span><u>$ </u><span style="color:black">cd</span><span> test
</span><u>$ </u><span style="color:black">xmake</span><span> service --connect 
</span><remote_build_client>: connect 192.168.56.110:90091 ..
<remote_build_client>: connected!
<remote_build_client>: sync files in 192.168.56.110:90091 ..
Scanning files ..
Comparing 3 files ..
    [+]: src/main.cpp
    [+]: .gitignore
    [+]: xmake.lua
3 files has been changed!
Archiving files ..
Uploading files with 1372 bytes ..
<remote_build_client>: sync files ok!
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">远程构建工程</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">连接成功后，我们就可以像正常本地编译一样，进行远程编译。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span>
</span><remote_build_client>: run xmake in 192.168.56.110:90091 ..
checking for platform ... macosx
checking for architecture ... x86_64
checking for Xcode directory ... /Applications/Xcode.app
checking for Codesign Identity of Xcode ... Apple Development: waruqi@gmail.com (T3NA4MRVPU)
checking for SDK version of Xcode for macosx (x86_64) ... 11.3
checking for Minimal target version of Xcode for macosx (x86_64) ... 11.4
[ 25%]: ccache compiling.release src/main.cpp
[ 50%]: linking.release test
[100%]: build ok!
<remote_build_client>: run command ok!
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">远程运行目标程序</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以像本地运行调试那样，远程运行调试编译的目标程序。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> run
</span><remote_build_client>: run xmake run in 192.168.56.110:90091 ..
hello world!
<remote_build_client>: run command ok!
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">远程重建工程</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> -rv
</span><remote_build_client>: run xmake -rv in 192.168.56.110:90091 ..
[ 25%]: ccache compiling.release src/main.cpp
/usr/local/bin/ccache /usr/bin/xcrun -sdk macosx clang -c -Qunused-arguments -arch x86_64 -mmacosx-version-min=11.4 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.3.sdk -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG -o build/.objs/test/macosx/x86_64/release/src/main.cpp.o src/main.cpp
[ 50%]: linking.release test
"/usr/bin/xcrun -sdk macosx clang++" -o build/macosx/x86_64/release/test build/.objs/test/macosx/x86_64/release/src/main.cpp.o -arch x86_64 -mmacosx-version-min=11.4 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.3.sdk -stdlib=libc++ -Wl,-x -lz
[100%]: build ok!
<remote_build_client>: run command ok!
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">远程配置编译参数</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> f --xxx --yy
</span></code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">手动同步工程文件</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">连接的时候，会自动同步一次代码，后期代码改动，可以执行此命令来手动同步改动的文件。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service --sync
</span><remote_build_client>: sync files in 192.168.56.110:90091 ..
Scanning files ..
Comparing 3 files ..
    [+]: src/main.cpp
    [+]: .gitignore
    [+]: xmake.lua
3 files has been changed!
Archiving files ..
Uploading files with 1372 bytes ..
<remote_build_client>: sync files ok!
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">断开远程连接</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">针对当前工程，断开连接，这仅仅影响当前工程，其他项目还是可以同时连接和编译。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service --disconnect
</span><remote_build_client>: disconnect 192.168.56.110:90091 ..
<remote_build_client>: disconnected!
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">查看服务器日志</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service --logs
</span></code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">清理远程服务缓存和构建文件</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以手动清理远程的任何缓存和构建生成的文件。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">cd</span><span> projectdir
</span><u>$ </u><span style="color:black">xmake</span><span> service --clean
</span></code></pre> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:start">改进 Cargo 包依赖</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">在之前的版本中，我们已经可以通过<span> </span><code>add_requires("cargo::base64")</code><span> </span>去单独集成每个 cargo 包，用于编译 rust 项目，以及与 C/C++ 的混合编译，例如：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_rules</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"mode.release"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"mode.debug"</span><strong style="color:#000000">)</strong>
<span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cargo::base64 0.13.0"</span><strong style="color:#000000">)</strong>
<span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cargo::flate2 1.0.17"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">features</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"zlib"</span><strong style="color:#000000">&#125;&#125;)</strong>

<span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/main.rs"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_packages</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cargo::base64"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"cargo::flate2"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">但是上面的方式会有一个问题：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果依赖很多，并且有几个依赖都共同依赖了相同的子依赖，那么会出现重定义问题，因此如果我们使用完整的 Cargo.toml 去管理依赖就不会存在这个问题。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">例如：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_rules</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"mode.release"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"mode.debug"</span><strong style="color:#000000">)</strong>
<span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cargo::test"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">cargo_toml</span> <strong style="color:black">=</strong> <span style="color:#000000">path</span><strong style="color:#000000">.</strong><span style="color:#000000">join</span><strong style="color:#000000">(</strong><span style="color:#000000">os</span><strong style="color:#000000">.</strong><span style="color:#000000">projectdir</span><strong style="color:#000000">(),</strong> <span style="color:#ff00ff">"Cargo.toml"</span><strong style="color:#000000">)&#125;&#125;)</strong>

<span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/main.rs"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_packages</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cargo::test"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">然后，我们就可以在 Cargo.toml 中集成所有需要的依赖，让 Rust 自己去分析依赖关系，避免重复的子依赖冲突。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">完整例子见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fblob%2Fdev%2Ftests%2Fprojects%2Frust%2Fcargo_deps_with_toml%2Fxmake.lua" target="_blank">cargo_deps_with_toml</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">当然，如果用户的依赖比较单一，那么之前的集成方式还是完全可用。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">为什么使用 Xmake 编译 Rust?</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这个时候，肯定会有人问，既然都用了 Cargo.toml 和 Cargo 了，为什么还要在 xmake.lua 中去配置呢，直接 Cargo 编译不就好了么。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果我们是在用 Xmake 开发 C/C++ 项目，但是需要引入一些 Rust 子模块给 C/C++ 项目使用，那么就可以借助这种方式，快速方便地在 C/C++ 中调用 Rust 库和代码。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更多关于 C/C++ 中调用 Rust 代码库的说明，见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fguide%2Fproject_examples%3Fid%3D%25e4%25bd%25bf%25e7%2594%25a8-cxxbridge-%25e5%259c%25a8-c-%25e4%25b8%25ad%25e8%25b0%2583%25e7%2594%25a8-rust" target="_blank">使用 cxxbridge 在 C/C++ 中调用 Rust</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">支持源文件分组</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">新版本，我们提供了一个新接口<span> </span><code>add_filegroups</code>，用于对 vs/vsxmake/cmakelists generator 生成的工程文件进行源文件分组展示。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果不设置分组展示，Xmake 也会默认按照树状模式展示，但是有些极端情况下，目录层级显示不是很好，例如：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"../../../../src/**.cpp"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt src="https://xmake.io/assets/img/manual/filegroup1.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">目前主要支持两种展示模式：</p> 
<ul> 
 <li>plain: 平坦模式</li> 
 <li>tree: 树形展示，这也是默认模式</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，它也支持对<span> </span><code>add_headerfiles</code><span> </span>添加的文件进行分组。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">设置分组并指定根目录</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"../../../../src/**.cpp"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_filegroups</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"group1/group2"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">rootdir</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"../../../../"</span><strong style="color:#000000">&#125;)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt src="https://xmake.io/assets/img/manual/filegroup2.png" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">设置分组并指定文件匹配模式</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"../../../../src/**.cpp"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_filegroups</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"group1/group2"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">rootdir</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"../../../../"</span><strong style="color:#000000">,</strong> <span style="color:#000000">files</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#ff00ff">"src/**.cpp"</span><strong style="color:#000000">&#125;&#125;)</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">作为平坦模式展示</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这种模式下，所有源文件忽略嵌套的目录层级，在分组下同一层级展示。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"../../../../src/**.cpp"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_filegroups</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"group1/group2"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">rootdir</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"../../../../"</span><strong style="color:#000000">,</strong> <span style="color:#000000">mode</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"plain"</span><strong style="color:#000000">&#125;)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt src="https://xmake.io/assets/img/manual/filegroup3.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">包版本选择支持 Git Commit</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">Xmake 的包依赖管理接口<span> </span><code>add_requires</code><span> </span>支持版本语义选择，分支选择，例如：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"tbox 1.6.1"</span><strong style="color:#000000">)</strong>
<span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"tbox >=1.6.1"</span><strong style="color:#000000">)</strong>
<span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"tbox master"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">但是，之前的版本，我们还不支持从 Git Commit 中选择版本，而现在我们也支持上了。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"tbox e807230557aac69e4d583c75626e3a7ebdb922f8"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">只要，这个包的配置中带有 Git url，就能从 Commit 中选择版本。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">更好地支持 iOS 模拟器编译</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果要编译 iOS 平台目标程序，之前可以使用如下配置，仅仅通过切换 arch，就能分别编译真机，模拟器版本程序。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake f -p iphoneos <strong style="color:black">[</strong>-a armv7|armv7s|arm64|i386|x86_64]
<span style="color:#8f5902">$ </span>xmake
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">但是由于 M1 设备上模拟器也支持 arm64 架构，因此之前单纯从 arch 去区分是否为模拟器，已无法满足需求。 因此，在新版本中，我们新增了一个参数配置去区分是否为模拟器目标。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake f -p iphoneos --appledev<strong style="color:black">=</strong>simulator
<span style="color:#8f5902">$ </span>xmake f -p watchos --appledev<strong style="color:black">=</strong>simulator
<span style="color:#8f5902">$ </span>xmake f -p appletvos --appledev<strong style="color:black">=</strong>simulator
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">而如果没有指定<span> </span><code>--appledev=</code><span> </span>参数，默认就是编译真机程序，当然，之前的模式也是完全兼容的。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">更新内容</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start">新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2138" target="_blank">#2138</a>: 支持模板包</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2185" target="_blank">#2185</a>: 添加<span> </span><code>--appledev=simulator</code><span> </span>去改进 Apple 模拟器目标编译支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2227" target="_blank">#2227</a>: 改进 cargo 包，支持指定 Cargo.toml 文件</li> 
 <li>改进<span> </span><code>add_requires</code><span> </span>支持 git command 作为版本</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F622" target="_blank">#622</a>: 支持远程编译</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2282" target="_blank">#2282</a>: 添加<span> </span><code>add_filegroups</code><span> </span>接口为 vs/vsxmake/cmake generator 增加文件组支持</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2137" target="_blank">#2137</a>: 改进 path 模块</li> 
 <li>macOS 下，减少 50% 的 Xmake 二进制文件大小</li> 
 <li>改进 tools/autoconf,cmake 去更好地支持工具链切换</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2221" target="_blank">#2221</a>: 改进注册表 api 去支持 unicode</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2225" target="_blank">#2225</a>: 增加对 protobuf 的依赖分析和构建支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2265" target="_blank">#2265</a>: 排序 CMakeLists.txt</li> 
 <li>改进 os.files 的文件遍历速度</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2233" target="_blank">#2233</a>: 修复 c++ modules 依赖</li> 
</ul>
                                        </div>
                                      
</div>
            