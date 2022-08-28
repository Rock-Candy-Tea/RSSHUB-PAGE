
---
title: 'Xmake v2.7.1 发布，更好的 C++ Modules 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://tboox.org/static/img/xmake/xmake-watch.gif'
author: 开源中国
comments: false
date: Sat, 27 Aug 2022 10:25:00 GMT
thumbnail: 'https://tboox.org/static/img/xmake/xmake-watch.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">Xmake</a><span> </span>是一个基于 Lua 的轻量级跨平台构建工具。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">它非常的轻量，没有任何依赖，因为它内置了 Lua 运行时。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">它使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们能够使用它像 Make/Ninja 那样可以直接编译项目，也可以像 CMake/Meson 那样生成工程文件，另外它还有内置的包管理系统来帮助用户解决 C/C++ 依赖库的集成使用问题。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">目前，Xmake 主要用于 C/C++ 项目的构建，但是同时也支持其他 native 语言的构建，可以实现跟 C/C++ 进行混合编译，同时编译速度也是非常的快，可以跟 Ninja 持平。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code>Xmake = Build backend + Project Generator + Package Manager + [Remote|Distributed] Build + Cache
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">尽管不是很准确，但我们还是可以把 Xmake 按下面的方式来理解：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code>Xmake ~= Make/Ninja + CMake/Meson + Vcpkg/Conan + distcc + ccache/sccache
</code></pre> 
</div> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">新特性介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这个版本我们对 C++20 Modules 的实现进行了重构和改进，改进了模块文件的依赖图解析，新增了对 STL 和 User HeaderUnits 的支持，同时让 CMakelists/compile_commands 生成器也支持了 C++ Modules。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，我们新增了一个<span> </span><code>xmake watch</code><span> </span>插件，可以实时监控当前工程文件更新，自动触发增量构建，或者运行一些自定义的命令。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img src="https://tboox.org/static/img/xmake/xmake-watch.gif" width="60%" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">C++ Modules 改进</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">Xmake 很早就已经支持 C++ Modules 的构建支持，并且能够自动分析模块间的依赖关系，实现最大化的并行编译。 另外，Xmake 采用<span> </span><code>.mpp</code><span> </span>作为默认的模块扩展名，但是也同时支持<span> </span><code>.ixx</code>,<span> </span><code>.cppm</code>,<span> </span><code>.mxx</code><span> </span>等扩展名。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">例如：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">set_languages</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"c++20"</span><strong style="color:#000000">)</strong>
<span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"class"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/*.cpp"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"src/*.mpp"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更多例子见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fmaster%2Ftests%2Fprojects%2Fc%252B%252B%2Fmodules" target="_blank">C++ Modules</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">但是之前的实现还存在很多不足之处：</p> 
<ol> 
 <li>不支持 HeaderUnits，因此也无法使用 stl 等模块</li> 
 <li>自己扫描源码实现模块依赖图解析，不支持编译器提供的依赖扫描，因此不完全可靠</li> 
 <li>不支持 CMakelists 生成</li> 
 <li>不支持 compile_commands.json 生成</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">而在新版中，我们对 C++20 模块的实现进行了重构和升级，上面提到的几点，我们都做了支持，新增了对 Headerunits 的支持，因此我们可以在模块中引入 STL 和 用户头文件模块。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">同时，由于 msvc 和 gcc 高版本 都已经内置对模块依赖图的扫描分析，Xmake 会优先借助编译器实现模块依赖图分析，如果编译器不支持（clang），那么 Xmake 也会退化到自己的源码扫描实现上去。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">相关的补丁见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2641" target="_blank">#2641</a>，非常感谢<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FArthapz" target="_blank">@Arthapz</a><span> </span>的贡献。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">下面是一个使用了 STL HeaderUnits 的模块例子，例如：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">stl_headerunit$ </span>xmake
<strong style="color:black">[</strong>  0%]: generating.cxx.module.deps src/main.cpp
<strong style="color:black">[</strong>  0%]: generating.cxx.module.deps src/hello.mpp
<strong style="color:black">[</strong> 20%]: generating.cxx.headerunit.bmi iostream
<strong style="color:black">[</strong> 60%]: generating.cxx.module.bmi hello
<strong style="color:black">[</strong> 70%]: cache compiling.release src/main.cpp
<strong style="color:black">[</strong> 80%]: linking.release stl_headerunit
<strong style="color:black">[</strong>100%]: build ok!
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">对于首次编译，我们会扫描模块代码之间的依赖关系，然后预编译 iostream 等 stl 库作为 headerunit。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">之后的重新编译，都会直接复用它们，实现编译加速。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">注：通常我们至少需要添加一个<span> </span><code>.mpp</code><span> </span>文件，才能开启 C++20 modules 编译，如果只有 cpp 文件，默认是不会开启模块编译的。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">但是，如果我们仅仅只是想在 cpp 文件中使用模块的 Headerunits 特性，比如引入一些 STL Headerunits 在 cpp 中使用， 那么我们也可以通过设置<span> </span><code>set_policy("build.c++.modules", true)</code><span> </span>来强行开启 C++ Modules 编译，例如：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_rules</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"mode.debug"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"mode.release"</span><strong style="color:#000000">)</strong>

<span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/*.cpp"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_languages</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"c++20"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_policy</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"build.c++.modules"</span><strong style="color:#000000">,</strong> <strong style="color:#800080">true</strong><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:start">工程文件监视和自动构建</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这个版本中，我们新增了<span> </span><code>xmake watch</code><span> </span>插件命令，可以自动监视项目文件更新，然后触发自动构建，或者运行一些自定义命令。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这通常用于个人开发时候，实现快速的实时增量编译，而不需要每次手动执行编译命令，提高开发效率。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">项目更新后自动构建</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">默认行为就是监视整个项目根目录，任何文件改动都会触发项目的增量编译。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake watch
watching /private/tmp/test/src/<span style="color:blue">**</span> ..
watching /private/tmp/test/<span style="color:blue">*</span> ..
/private/tmp/test/src/main.cpp modified
<strong style="color:black">[</strong> 25%]: ccache compiling.release src/main.cpp
<strong style="color:black">[</strong> 50%]: linking.release <span style="color:black">test</span>
<strong style="color:black">[</strong>100%]: build ok!
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">监视指定目录</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以监视指定的代码目录，缩小监视范围，提升监视性能。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake watch -d src
<span style="color:#8f5902">$ </span>xmake watch -d <span style="color:#ff00ff">"src;tests/*"</span>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">上面的命令，会去递归监视所有子目录，如果想要仅仅监视当前目录下的文件，不进行递归监视，可以使用下面的命令。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake watch -p src
<span style="color:#8f5902">$ </span>xmake watch -p <span style="color:#ff00ff">"src;tests/*"</span>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">监视并运行指定命令</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果想在自动构建后，还想自动运行构建的程序，我们可以使用自定义的命令集。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake watch -c <span style="color:#ff00ff">"xmake; xmake run"</span>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">上面的命令列表是作为字符串传递，这对于复杂命令参数，需要转义比较繁琐不够灵活，那么我们可以使用下面的方式进行任意命令的设置。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake watch -- <span style="color:black">echo </span>hello xmake!
<span style="color:#8f5902">$ </span>xmake watch -- xmake run --help
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">监视并运行目标程序</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">尽管我们可以通过自定义命令来实现目标程序的自动运行，但是我们也提供了更加方便的参数来实现这个行为。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake watch -r
<span style="color:#8f5902">$ </span>xmake watch --run
<strong style="color:black">[</strong>100%]: build ok!
hello world!
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img src="https://tboox.org/static/img/xmake/xmake-watch.gif" width="60%" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">监视并运行 lua 脚本</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们还可以监视文件更新后，运行指定的 lua 脚本，实现更加灵活复杂的命令定制。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake watch -s /tmp/test.lua
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们还可以再脚本中获取所有更新的文件路径列表和事件。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:blue">function</span> <span style="color:black">main</span><strong style="color:#000000">(</strong><span style="color:#000000">events</span><strong style="color:#000000">)</strong>
    <em>-- TODO handle events</em>
<span style="color:blue">end</span>
</code></pre> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:start">Mac Catalyst 支持</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">MAc Catalyst 是苹果后来新推的一项让 iPad App 带入 Mac 的方案，通过 Mac Catalyst 构建的 Mac App 与您的 iPad App 共享代码，而且您可以单独为 Mac 添加更多功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">新版本中，我们新增了 Mac Catalyst 目标的构建支持，在 macOS 平台上，我们只需要添加<span> </span><code>--appledev=catalyst</code><span> </span>配置选项，就可以支持编译现有的 iOS 代码，并让它在 macOS 上运行起来，而无需做任何改动。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake f --appledev<strong style="color:black">=</strong>catalyst
<span style="color:#8f5902">$ </span>xmake
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们可以在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fmaster%2Ftests%2Fprojects%2Fobjc%2Fiosapp_with_framework" target="_blank">iosapp_with_framework</a><span> </span>这个测试项目中体验 Mac Catalyst 程序的编译运行。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake
<strong style="color:black">[</strong> 36%]: processing.xcode.release src/framework/Info.plist
<strong style="color:black">[</strong> 40%]: cache compiling.release src/framework/test.m
<strong style="color:black">[</strong> 44%]: linking.release <span style="color:black">test</span>
<strong style="color:black">[</strong> 48%]: generating.xcode.release test.framework
<strong style="color:black">[</strong> 56%]: compiling.xcode.release src/app/Assets.xcassets
<strong style="color:black">[</strong> 56%]: processing.xcode.release src/app/Info.plist
<strong style="color:black">[</strong> 60%]: cache compiling.release src/app/ViewController.m
<strong style="color:black">[</strong> 60%]: cache compiling.release src/app/SceneDelegate.m
<strong style="color:black">[</strong> 60%]: cache compiling.release src/app/main.m
<strong style="color:black">[</strong> 60%]: cache compiling.release src/app/AppDelegate.m
<strong style="color:black">[</strong> 60%]: compiling.xcode.release src/app/Base.lproj/LaunchScreen.storyboard
<strong style="color:black">[</strong> 60%]: compiling.xcode.release src/app/Base.lproj/Main.storyboard
<strong style="color:black">[</strong> 88%]: linking.release demo
<strong style="color:black">[</strong> 92%]: generating.xcode.release demo.app
<strong style="color:black">[</strong>100%]: build ok!
<span style="color:#8f5902">$ </span>xmake run
2022-08-26 15:11:03.581 demo[86248:9087199] add<strong style="color:black">(</strong>1, 2<strong style="color:black">)</strong>: 3
2022-08-26 15:11:03.581 demo[86248:9087199] hello xmake!
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img src="https://tboox.org/static/img/xmake/mac-catalyst.png" width="60%" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">改进远程编译</h3> 
<h4 style="margin-left:0; margin-right:0; text-align:start">拉取远程构建文件</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">对于远程编译，我们新增加了一个拉取远程文件的命令，通常可用于远程编译完成后，下载远程的目标生成文件，库文件到本地。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake service --pull <span style="color:#ff00ff">'build/**'</span> outputdir
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们可以通过<span> </span><code>--pull 'build/**'</code><span> </span>模式匹配需要下载的文件，可以是构建文件，也可以是其他文件。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">注：文件是按项目隔离的，只能指定下载当前项目下的文件，并不会让用户下载服务器上其他目录下的文件，避免一些安全隐患。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">实时回显输出</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">先前的版本在使用远程编译的时候，客户端是无法实时输出服务端的编译信息的，由于缓存的存在，本地看到的编译进度信息都是一块一块刷新出来，体验不是很好。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">因此我们加上了行缓冲刷新支持，提高了输出回显的实时性，使得用户在远程编译时，更接近本地编译的体验。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">改进分布式编译调度算法</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们对 xmake 的分布式编译的服务器节点调度也做了进一步改进，加上了 cpu 负载和内存资源的权重，而不仅仅通过 cpu core 数量来分配任务。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">因此，如果某些节点负载过高，我们会优先将编译任务调度到相当比较空闲的节点上去，充分利用所有编译资源。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">更灵活的 cmake 包查找</h3> 
<h4 style="margin-left:0; margin-right:0; text-align:start">指定链接</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">对于 cmake 包，我们新增了<span> </span><code>link_libraries</code><span> </span>配置选项，让用户在查找使用 cmake 包的时候，可以自定义配置包依赖的链接库，甚至对 target 链接的支持。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cmake::xxx"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">link_libraries</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#ff00ff">"abc::lib1"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"abc::lib2"</span><strong style="color:#000000">&#125;&#125;&#125;)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">xmake 在查找 cmake 包的时候，会自动追加下面的配置，改进对 links 库的提取。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:black">target_link_libraries</span><strong style="color:#000000">(</strong>test PRIVATE ABC::lib1 ABC::lib2<strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">指定搜索模式</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，我们增加的搜索模式配置：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cmake::xxx"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">search_mode</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"config"</span><strong style="color:#000000">&#125;&#125;)</strong>
<span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cmake::xxx"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">search_mode</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"module"</span><strong style="color:#000000">&#125;&#125;)</strong>
<span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cmake::xxx"</span><strong style="color:#000000">)</strong> <em>-- both</em>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">比如指定 config 搜索模式，告诉 cmake 从<span> </span><code>XXXConfig.cmake</code><span> </span>中查找包。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">xmake 在查找 cmake 包的时候，内部会自动追加下面的配置。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:black">find_package</span><strong style="color:#000000">(</strong>ABC CONFIG REQUIRED<strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:start">armcc/armclang/rc 增量编译支持</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">在新版本中，我们对 keil 的 armcc/armclang 编译器也进行头文件依赖分析，来支持增量编译。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，msvc 的 rc.exe 资源编译器本身是无法提供头文件依赖分析的，但是 cl.exe 的预处理器却是可以处理资源文件的。 因此我们可以通过<span> </span><code>cl.exe /E test.rc</code><span> </span>去预处理资源文件，从中提取依赖信息，来实现资源文件的增量编译支持。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">目前测试下来，效果还不错，同时我们也对内部 ICON/BITMAP 的资源引用依赖也做了支持。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">其他问题修复</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们对构建缓存也做了很多修复，它将比之前的版本更加的稳定。另外我们也精简了 CMakelists 的生成。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更多细节改进见下面的更新日志：</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">更新内容</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start">新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2555" target="_blank">#2555</a>: 添加 fwatcher 模块和<span> </span><code>xmake watch</code><span> </span>插件命令</li> 
 <li>添加<span> </span><code>xmake service --pull 'build/**' outputdir</code><span> </span>命令去拉取远程构建服务器上的文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2641" target="_blank">#2641</a>: 改进 C++20 模块, 支持 headerunits 和 project 生成</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2679" target="_blank">#2679</a>: 支持 Mac Catalyst 构建</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2576" target="_blank">#2576</a>: 改进从 cmake 中查找包，提供更过灵活的可选配置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2577" target="_blank">#2577</a>: 改进 add_headerfiles()，增加<span> </span><code><span>&#123;</span><span>install</span><span><span> </span></span><span>=</span><span><span> </span></span><span>false</span><span>&#125;</span></code><span> </span>支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2603" target="_blank">#2603</a>: 为 ccache 默认禁用<span> </span><code>-fdirectives-only</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2580" target="_blank">#2580</a>: 设置 stdout 到 line 缓冲输出</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2571" target="_blank">#2571</a>: 改进分布式编译的调度算法，增加 cpu/memory 状态权重</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2410" target="_blank">#2410</a>: 改进 cmakelists 生成</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2690" target="_blank">#2690</a>: 改机传递 toolchains 到包</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2686" target="_blank">#2686</a>: 改进 armcc/armclang 支持增量编译</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2562" target="_blank">#2562</a>: 改进 rc.exe 对引用文件依赖的解析和增量编译支持</li> 
 <li>改进默认的并行构建任务数</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2614" target="_blank">#2614</a>: 为 msvc 修复构建 submodules2 测试工程</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2620" target="_blank">#2620</a>: 修复构建缓存导致的增量编译问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2177" target="_blank">#2177</a>: 修复 python.library 在 macOS 上段错误崩溃</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2708" target="_blank">#2708</a>: 修复 mode.coverage 规则的链接错误</li> 
 <li>修复 ios/macOS framework 和 application 的 rpath 加载路径</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            