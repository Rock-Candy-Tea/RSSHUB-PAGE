
---
title: 'xmake v2.5.7 发布，包依赖锁定和 Vala_Metal 语言编译支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://tboox.org/static/img/xmake/xmake-metal.png'
author: 开源中国
comments: false
date: Mon, 30 Aug 2021 09:28:00 GMT
thumbnail: 'https://tboox.org/static/img/xmake/xmake-metal.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">xmake</a> 是一个基于 Lua 的轻量级跨平台构建工具，使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p style="text-align:start">这个版本，我们新增了很多新特性，不仅增加了对 Vala 和 Metal 语言的编译支持，另外我们还改进了包依赖管理，能够像 npm/package.lock 那样支持对依赖包的锁定和更新，使得用户的项目不会受到上游包仓库的更新变动影响。</p> 
<p style="text-align:start">此外，我们还提供了一些比较实用的规则， 比如 <code>utils.bin2c</code> 可以让用户方便快速的内嵌一些二进制资源文件到代码中去，以头文件的方式获取相关数据。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2 style="text-align:start">新特性介绍</h2> 
<h3 style="text-align:start">新增 Vala 语言支持</h3> 
<p style="text-align:start">这个版本，我们已经可以初步支持构建 Vala 程序，只需要应用 <code>add_rules("vala")</code> 规则。</p> 
<p style="text-align:start">同时，我们需要添加一些依赖包，其中 glib 包是必须的，因为 vala 自身也会用到它。</p> 
<p style="text-align:start"><code>add_values("vala.packages")</code> 用于告诉 valac，项目需要哪些包，它会引入相关包的 vala api，但是包的依赖集成，还是需要通过 <code>add_requires("lua")</code> 下载集成。</p> 
<p style="text-align:start">例如：</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_rules</span><strong>(</strong><span style="color:#ff00ff">"mode.release"</span><strong>,</strong> <span style="color:#ff00ff">"mode.debug"</span><strong>)</strong>

<span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"lua"</span><strong>,</strong> <span style="color:#ff00ff">"glib"</span><strong>)</strong>

<span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_rules</span><strong>(</strong><span style="color:#ff00ff">"vala"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.vala"</span><strong>)</strong>
    <span style="color:#000000">add_packages</span><strong>(</strong><span style="color:#ff00ff">"lua"</span><strong>,</strong> <span style="color:#ff00ff">"glib"</span><strong>)</strong>
    <span style="color:#000000">add_values</span><strong>(</strong><span style="color:#ff00ff">"vala.packages"</span><strong>,</strong> <span style="color:#ff00ff">"lua"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">更多例子：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fmaster%2Ftests%2Fprojects%2Fvala" target="_blank">Vala examples</a></p> 
<h3 style="text-align:start">新增包依赖锁定支持</h3> 
<p style="text-align:start">这个特性类似 npm 的 package.lock, cargo 的 cargo.lock。</p> 
<p style="text-align:start">比如，我们引用一些包，默认情况下，如果不指定版本，那么 xmake 每次都会自动拉取最新版本的包来集成使用，例如：</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"zlib"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">但如果上游的包仓库更新改动，比如 zlib 新增了一个 1.2.11 版本，或者安装脚本有了变动，都会导致用户的依赖包发生改变。</p> 
<p style="text-align:start">这容易导致原本编译通过的一些项目，由于依赖包的变动出现一些不稳定因素，有可能编译失败等等。</p> 
<p style="text-align:start">为了确保用户的项目每次使用的包都是固定的，我们可以通过下面的配置去启用包依赖锁定。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">set_policy</span><strong>(</strong><span style="color:#ff00ff">"package.requires_lock"</span><strong>,</strong> <strong>true</strong><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">这是一个全局设置，必须设置到全局根作用域，如果启用后，xmake 执行完包拉取，就会自动生成一个 <code>xmake-requires.lock</code> 的配置文件。</p> 
<p style="text-align:start">它包含了项目依赖的所有包，以及当前包的版本等信息。</p> 
<div style="text-align:start"> 
 <pre><code><strong>&#123;</strong>
    <span style="color:#000000">__meta__</span> <strong>=</strong> <strong>&#123;</strong>
        <span style="color:#000000">version</span> <strong>=</strong> <span style="color:#ff00ff">"1.0"</span>
    <strong>&#125;,</strong>
    <strong>[</strong><span style="color:#ff00ff">"macosx|x86_64"</span><strong>]</strong> <strong>=</strong> <strong>&#123;</strong>
        <strong>[</strong><span style="color:#ff00ff">"cmake#31fecfc4"</span><strong>]</strong> <strong>=</strong> <strong>&#123;</strong>
            <span style="color:#000000">repo</span> <strong>=</strong> <strong>&#123;</strong>
                <span style="color:#000000">branch</span> <strong>=</strong> <span style="color:#ff00ff">"master"</span><strong>,</strong>
                <span style="color:#000000">commit</span> <strong>=</strong> <span style="color:#ff00ff">"4498f11267de5112199152ab030ed139c985ad5a"</span><strong>,</strong>
                <span style="color:#000000">url</span> <strong>=</strong> <span style="color:#ff00ff">"https://github.com/xmake-io/xmake-repo.git"</span>
            <strong>&#125;,</strong>
            <span style="color:#000000">version</span> <strong>=</strong> <span style="color:#ff00ff">"3.21.0"</span>
        <strong>&#125;,</strong>
        <strong>[</strong><span style="color:#ff00ff">"glfw#31fecfc4"</span><strong>]</strong> <strong>=</strong> <strong>&#123;</strong>
            <span style="color:#000000">repo</span> <strong>=</strong> <strong>&#123;</strong>
                <span style="color:#000000">branch</span> <strong>=</strong> <span style="color:#ff00ff">"master"</span><strong>,</strong>
                <span style="color:#000000">commit</span> <strong>=</strong> <span style="color:#ff00ff">"eda7adee81bac151f87c507030cc0dd8ab299462"</span><strong>,</strong>
                <span style="color:#000000">url</span> <strong>=</strong> <span style="color:#ff00ff">"https://github.com/xmake-io/xmake-repo.git"</span>
            <strong>&#125;,</strong>
            <span style="color:#000000">version</span> <strong>=</strong> <span style="color:#ff00ff">"3.3.4"</span>
        <strong>&#125;,</strong>
        <strong>[</strong><span style="color:#ff00ff">"opengl#31fecfc4"</span><strong>]</strong> <strong>=</strong> <strong>&#123;</strong>
            <span style="color:#000000">repo</span> <strong>=</strong> <strong>&#123;</strong>
                <span style="color:#000000">branch</span> <strong>=</strong> <span style="color:#ff00ff">"master"</span><strong>,</strong>
                <span style="color:#000000">commit</span> <strong>=</strong> <span style="color:#ff00ff">"94d2eee1f466092e04c5cf1e4ecc8c8883c1d0eb"</span><strong>,</strong>
                <span style="color:#000000">url</span> <strong>=</strong> <span style="color:#ff00ff">"https://github.com/xmake-io/xmake-repo.git"</span>
            <strong>&#125;</strong>
        <strong>&#125;</strong>
    <strong>&#125;</strong>
<strong>&#125;</strong>
</code></pre> 
</div> 
<p style="text-align:start">当然，我们也可以执行下面的命令，强制升级包到最新版本。</p> 
<div style="text-align:start"> 
 <pre><code><u>$ </u><span style="color:black">xmake</span> require --upgrade
upgrading packages ..
  zlib: 1.2.10 -> 1.2.11
1 package is upgraded!
</code></pre> 
</div> 
<h3 style="text-align:start">option 支持代码片段的运行时检测</h3> 
<p style="text-align:start">option 本身有提供 <code>add_csnippets/add_cxxsnippets</code> 两个接口，用于快速检测特定一段 c/c++ 代码是否通过编译，如果编译通过就会启用对应 option 选项。</p> 
<p style="text-align:start">但之前的版本仅仅只能提供编译期检测，而新版本中，我们还新增了运行时检测支持。</p> 
<p style="text-align:start">我们可以通过设置 <code>&#123;tryrun = true&#125;</code> 和 <code>&#123;output = true&#125;</code> 两个参数，用于尝试运行检测和捕获输出。</p> 
<h4 style="text-align:start">尝试运行检测</h4> 
<p style="text-align:start">设置 tryrun 可以尝试运行来检测</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">option</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">add_cxxsnippets</span><strong>(</strong><span style="color:#ff00ff">"HAS_INT_4"</span><strong>,</strong> <span style="color:#ff00ff">"return (sizeof(int) == 4)? 0 : -1;"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">tryrun</span> <strong>=</strong> <strong>true</strong><strong>&#125;)</strong>
</code></pre> 
</div> 
<p style="text-align:start">如果编译运行通过，test 选项就会被启用。</p> 
<h4 style="text-align:start">运行时检测并捕获输出</h4> 
<p style="text-align:start">设置 output 也会尝试去检测，并且额外捕获运行的输出内容。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">option</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">add_cxxsnippets</span><strong>(</strong><span style="color:#ff00ff">"INT_SIZE"</span><strong>,</strong> <span style="color:#ff00ff">'printf("%d", sizeof(int)); return 0;'</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">output</span> <strong>=</strong> <strong>true</strong><strong>,</strong> <span style="color:#000000">number</span> <strong>=</strong> <strong>true</strong><strong>&#125;)</strong>
</code></pre> 
</div> 
<p style="text-align:start">如果编译运行通过，test 选项就会被启用，同时能获取到对应的输出内容作为 option 的值。</p> 
<p style="text-align:start">注：设置为捕获输出，当前 option 不能再设置其他 snippets</p> 
<p style="text-align:start">我们也可以通过 <code>is_config</code> 获取绑定到option的输出。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:blue">if</span> <span style="color:#000000">is_config</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>,</strong> <span style="color:#ff00ff">"8"</span><strong>)</strong> <span style="color:#000000">tben</span>
    <em>-- xxx</em>
<span style="color:blue">end</span>
</code></pre> 
</div> 
<p style="text-align:start">另外，我们也对 <code>includes("check_csnippets")</code> 的辅助检测接口，也做了改进来支持运行时检测。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">includes</span><strong>(</strong><span style="color:#ff00ff">"check_csnippets.lua"</span><strong>)</strong>

<span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"*.c"</span><strong>)</strong>
    <span style="color:#000000">add_configfiles</span><strong>(</strong><span style="color:#ff00ff">"config.h.in"</span><strong>)</strong>

    <span style="color:#000000">check_csnippets</span><strong>(</strong><span style="color:#ff00ff">"HAS_INT_4"</span><strong>,</strong> <span style="color:#ff00ff">"return (sizeof(int) == 4)? 0 : -1;"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">tryrun</span> <strong>=</strong> <strong>true</strong><strong>&#125;)</strong>
    <span style="color:#000000">check_csnippets</span><strong>(</strong><span style="color:#ff00ff">"INT_SIZE"</span><strong>,</strong> <span style="color:#ff00ff">'printf("%d", sizeof(int)); return 0;'</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">output</span> <strong>=</strong> <strong>true</strong><strong>,</strong> <span style="color:#000000">number</span> <strong>=</strong> <strong>true</strong><strong>&#125;)</strong>
    <span style="color:#000000">configvar_check_csnippets</span><strong>(</strong><span style="color:#ff00ff">"HAS_LONG_8"</span><strong>,</strong> <span style="color:#ff00ff">"return (sizeof(long) == 8)? 0 : -1;"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">tryrun</span> <strong>=</strong> <strong>true</strong><strong>&#125;)</strong>
    <span style="color:#000000">configvar_check_csnippets</span><strong>(</strong><span style="color:#ff00ff">"PTR_SIZE"</span><strong>,</strong> <span style="color:#ff00ff">'printf("%d", sizeof(void*)); return 0;'</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">output</span> <strong>=</strong> <strong>true</strong><strong>,</strong> <span style="color:#000000">number</span> <strong>=</strong> <strong>true</strong><strong>&#125;)</strong>
</code></pre> 
</div> 
<p style="text-align:start">如果启用捕获输出，<code>config.h.in</code> 的 <code>$&#123;define PTR_SIZE&#125;</code> 会自动生成 <code>#define PTR_SIZE 4</code>。</p> 
<p style="text-align:start">其中，<code>number = true</code> 设置，可以强制作为 number 而不是字符串值，否则默认会定义为 <code>#define PTR_SIZE "4"</code></p> 
<h3 style="text-align:start">快速内嵌二进制资源文件到代码</h3> 
<p style="text-align:start">我们可以通过 <code>utils.bin2c</code> 规则，在项目中引入一些二进制文件，并见他们作为 c/c++ 头文件的方式提供开发者使用，获取这些文件的数据。</p> 
<p style="text-align:start">比如，我们可以在项目中，内嵌一些 png/jpg 资源文件到代码中。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"console"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binart"</span><strong>)</strong>
    <span style="color:#000000">add_rules</span><strong>(</strong><span style="color:#ff00ff">"utils.bin2c"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">extensions</span> <strong>=</strong> <strong>&#123;</strong><span style="color:#ff00ff">".png"</span><strong>,</strong> <span style="color:#ff00ff">".jpg"</span><strong>&#125;&#125;)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.c"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"res/*.png"</span><strong>,</strong> <span style="color:#ff00ff">"res/*.jpg"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">注：extensions 的设置是可选的，默认后缀名是 .bin</p> 
<p style="text-align:start">然后，我们就可以通过 <code>#include "filename.png.h"</code> 的方式引入进来使用，xmake 会自动帮你生成对应的头文件，并且添加对应的搜索目录。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:blue">static</span> <span style="color:blue">unsigned</span> <span style="color:blue">char</span> <span style="color:#000000">g_png_data</span><strong>[]</strong> <strong>=</strong> <strong>&#123;</strong>
    <em>#include "image.png.h"
</em><strong>&#125;;</strong>

<span style="color:blue">int</span> <span style="color:black">main</span><strong>(</strong><span style="color:blue">int</span> <span style="color:#000000">argc</span><strong>,</strong> <span style="color:blue">char</span><strong>**</strong> <span style="color:#000000">argv</span><strong>)</strong>
<strong>&#123;</strong>
    <span style="color:#000000">printf</span><strong>(</strong><span style="color:#ff00ff">"image.png: %s, size: %d</span><span style="color:#ff00ff">\n</span><span style="color:#ff00ff">"</span><strong>,</strong> <span style="color:#000000">g_png_data</span><strong>,</strong> <span style="color:blue">sizeof</span><strong>(</strong><span style="color:#000000">g_png_data</span><strong>));</strong>
    <span style="color:blue">return</span> <strong>0</strong><strong>;</strong>
<strong>&#125;</strong>
</code></pre> 
</div> 
<p style="text-align:start">生成头文件内容类似：</p> 
<div style="text-align:start"> 
 <pre><code>cat build/.gens/test/macosx/x86_64/release/rules/c++/bin2c/image.png.h
  0x68, 0x65, 0x6C, 0x6C, 0x6F, 0x20, 0x78, 0x6D, 0x61, 0x6B, 0x65, 0x21, 0x0A, 0x00
</code></pre> 
</div> 
<h3 style="text-align:start">新增 iOS/macOS 应用 Metal 编译支持</h3> 
<p style="text-align:start">我们知道 <code>xcode.application</code> 规则可以编译 iOS/macOS 应用程序，生成 .app/.ipa 程序包，并同时完成签名操作。</p> 
<p style="text-align:start">不过之前它不支持对带有 .metal 代码的编译，而新版本中，我们新增了 <code>xcode.metal</code> 规则，并默认关联到 <code>xcode.application</code> 规则中去来默认支持 metal 编译。</p> 
<p style="text-align:start">xmake 会自动编译 .metal 然后打包生成 default.metallib 文件，并且自动内置到 .app/.ipa 里面。</p> 
<p style="text-align:start">如果用户的 metal 是通过 <code>[_device newDefaultLibrary]</code> 来访问的，那么就能自动支持，就跟使用 xcode 编译一样。</p> 
<p style="text-align:start">这里是我们提供的一个完整的：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fblob%2Fmaster%2Ftests%2Fprojects%2Fobjc%2Fmetal_app%2Fxmake.lua" target="_blank">项目例子</a>。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_rules</span><strong>(</strong><span style="color:#ff00ff">"mode.debug"</span><strong>,</strong> <span style="color:#ff00ff">"mode.release"</span><strong>)</strong>

<span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"HelloTriangle"</span><strong>)</strong>
    <span style="color:#000000">add_rules</span><strong>(</strong><span style="color:#ff00ff">"xcode.application"</span><strong>)</strong>
    <span style="color:#000000">add_includedirs</span><strong>(</strong><span style="color:#ff00ff">"Renderer"</span><strong>)</strong>
    <span style="color:#000000">add_frameworks</span><strong>(</strong><span style="color:#ff00ff">"MetalKit"</span><strong>)</strong>
    <span style="color:#000000">add_mflags</span><strong>(</strong><span style="color:#ff00ff">"-fmodules"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"Renderer/*.m"</span><strong>,</strong> <span style="color:#ff00ff">"Renderer/*.metal"</span><strong>)</strong> <em>------- 添加 metal 文件</em>
    <span style="color:blue">if</span> <span style="color:#000000">is_plat</span><strong>(</strong><span style="color:#ff00ff">"macosx"</span><strong>)</strong> <span style="color:blue">then</span>
        <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"Application/main.m"</span><strong>)</strong>
        <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"Application/AAPLViewController.m"</span><strong>)</strong>
        <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"Application/macOS/Info.plist"</span><strong>)</strong>
        <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"Application/macOS/Base.lproj/*.storyboard"</span><strong>)</strong>
        <span style="color:#000000">add_defines</span><strong>(</strong><span style="color:#ff00ff">"TARGET_MACOS"</span><strong>)</strong>
        <span style="color:#000000">add_frameworks</span><strong>(</strong><span style="color:#ff00ff">"AppKit"</span><strong>)</strong>
    <span style="color:blue">elseif</span> <span style="color:#000000">is_plat</span><strong>(</strong><span style="color:#ff00ff">"iphoneos"</span><strong>)</strong> <span style="color:blue">then</span>
        <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"Application/*.m"</span><strong>)</strong>
        <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"Application/iOS/Info.plist"</span><strong>)</strong>
        <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"Application/iOS/Base.lproj/*.storyboard"</span><strong>)</strong>
        <span style="color:#000000">add_frameworks</span><strong>(</strong><span style="color:#ff00ff">"UIKit"</span><strong>)</strong>
        <span style="color:#000000">add_defines</span><strong>(</strong><span style="color:#ff00ff">"TARGET_IOS"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">比如，在 macOS 上，编译运行后，就会通过 metal 渲染出需要的效果。</p> 
<p style="text-align:start"><img alt src="https://tboox.org/static/img/xmake/xmake-metal.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">如果，我们的项目没有使用默认的 metal library，我们也可以通过上面提到的 <code>utils.bin2c</code> 规则，作为源文件的方式内嵌到代码库中，例如：</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_rules</span><strong>(</strong><span style="color:#ff00ff">"utils.bin2c"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">extensions</span> <strong>=</strong> <span style="color:#ff00ff">".metal"</span><strong>&#125;)</strong>
<span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"Renderer/*.metal"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">然后代码中，我们就能访问了：</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:blue">static</span> <span style="color:blue">unsigned</span> <span style="color:blue">char</span> <span style="color:#000000">g_metal_data</span><strong>[]</strong> <strong>=</strong> <strong>&#123;</strong>
    <em>#include "xxx.metal.h"
</em><strong>&#125;;</strong>

<span style="color:#000000">id</span><strong><</strong><span style="color:#000000">MTLLibrary</span><strong>></strong> <span style="color:#000000">library</span> <strong>=</strong> <strong>[</strong><span style="color:#000000">_device</span> <span style="color:#000000">newLibraryWithSource</span><strong>:</strong><strong>[[</strong><span style="color:#000000">NSString</span> <span style="color:#000000">stringWithUTF8String</span><strong>:</strong><span style="color:#000000">g_metal_data</span><strong>]]</strong> <span style="color:#000000">options</span><strong>:</strong><span style="color:#000000">nil</span> <span style="color:#000000">error</span><strong>:&</strong><span style="color:#000000">error</span><strong>];</strong>
</code></pre> 
</div> 
<h3 style="text-align:start">改进 add_repositories</h3> 
<p style="text-align:start">如果我们通过内置在项目中的本地仓库，我们之前是通过 <code>add_repositories("myrepo repodir")</code> 的方式来引入。</p> 
<p style="text-align:start">但是，它并不像 <code>add_files()</code> 那样是基于当前 xmake.lua 文件目录的相对目录，也没有路径的自动转换，因此容易遇到找不到 repo 的问题。</p> 
<p style="text-align:start">因此，我么你改进了下它，可以通过额外的 rootdir 参数指定对应的根目录位置，比如相对当前 xmake.lua 的脚本目录。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_repositories</span><strong>(</strong><span style="color:#ff00ff">"myrepo repodir"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">rootdir</span> <strong>=</strong> <span style="color:#000000">os</span><strong>.</strong><span style="color:#000000">scriptdir</span><strong>()&#125;)</strong>
</code></pre> 
</div> 
<h3 style="text-align:start">os.cp 支持符号链接</h3> 
<p style="text-align:start">之前的版本，<code>os.cp</code> 接口不能很好的处理符号链接的复制，他会自动展开链接，复制实际的文件内容，只会导致复制后，符号链接丢失。</p> 
<p style="text-align:start">如果想要复制后，原样保留符号链接，只需要设置下参数：<code>&#123;symlink = true&#125;</code></p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">os</span><strong>.</strong><span style="color:#000000">cp</span><strong>(</strong><span style="color:#ff00ff">"/xxx/symlink"</span><strong>,</strong> <span style="color:#ff00ff">"/xxx/dstlink"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">symlink</span> <strong>=</strong> <strong>true</strong><strong>&#125;)</strong>
</code></pre> 
</div> 
<h3 style="text-align:start">更方便地编译自动生成的代码</h3> 
<p style="text-align:start">有时候，我们会有这样一个需求，在编译前，自动生成一些源文件参与后期的代码编译。但是由于 <code>add_files</code> 添加的文件在执行编译时候，就已经确定，无法在编译过程中动态添加它们（因为需要并行编译）。</p> 
<p style="text-align:start">因此，要实现这个需求，我们通常需要自定义一个 rule，然后里面主动调用编译器模块去处理生成代码的编译，对象文件的注入，依赖更新等一系列问题。</p> 
<p style="text-align:start">这对于 xmake 开发者本身没什么大问题，但是对于用户来说，这还是比较繁琐了，不好上手。</p> 
<p style="text-align:start">新版本中，我们改进了对 <code>add_files</code> 的支持，并添加了 <code>&#123;always_added = true&#125;</code> 配置来告诉 xmake 我们始终需要添加指定的源文件，即使它还不存在。</p> 
<p style="text-align:start">这样我们就可以依靠xmake的默认编译过程来编译自动生成的代码了，像这样：</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_rules</span><strong>(</strong><span style="color:#ff00ff">"mode.debug"</span><strong>,</strong> <span style="color:#ff00ff">"mode.release"</span><strong>)</strong>

<span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"autogen_code"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"$(buildir)/autogen.cpp"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">always_added</span> <strong>=</strong> <strong>true</strong><strong>&#125;)</strong>
    <span style="color:#000000">before_build</span><strong>(</strong><span style="color:blue">function</span> <strong>(</strong><span style="color:#000000">target</span><strong>)</strong>
        <span style="color:#000000">io</span><strong>.</strong><span style="color:#000000">writefile</span><strong>(</strong><span style="color:#ff00ff">"$(buildir)/autogen.cpp"</span><strong>,</strong> <span style="color:#ff00ff">[[
#include <iostream>

using namespace std;

int main(int argc, char** argv)
&#123;
    cout << "hello world!" << endl;
    return 0;
&#125;
        ]]</span><strong>)</strong>
    <span style="color:blue">end</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">都不需要额外的 rule 定义，只需要保证编译顺序，在正确的阶段生成代码文件就可以了。</p> 
<p style="text-align:start">但是，我们也需要注意，由于当前自动生成的源文件可能还不存在，我们不能在 <code>add_files</code> 里面使用模式匹配，只能显式添加每个源文件路径。</p> 
<h2 style="text-align:start">更新内容</h2> 
<h3 style="text-align:start">新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1534" target="_blank">#1534</a>: 新增对 Vala 语言的支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1544" target="_blank">#1544</a>: 添加 utils.bin2c 规则去自动从二进制资源文件产生 .h 头文件并引入到 C/C++ 代码中</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1547" target="_blank">#1547</a>: option/snippets 支持运行检测模式，并且可以获取输出</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1567" target="_blank">#1567</a>: 新增 xmake-requires.lock 包依赖锁定支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1597" target="_blank">#1597</a>: 支持编译 metal 文件到 metallib，并改进 xcode.application 规则去生成内置的 default.metallib 到 app</li> 
</ul> 
<h3 style="text-align:start">改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1540" target="_blank">#1540</a>: 更好更方便地编译自动生成的代码</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1578" target="_blank">#1578</a>: 改进 add_repositories 去更好地支持相对路径</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1582" target="_blank">#1582</a>: 改进安装和 os.cp 支持符号链接</li> 
</ul> 
<h3 style="text-align:start">Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1531" target="_blank">#1531</a>: 修复 targets 加载失败的错误信息提示错误</li> 
</ul>
                                        </div>
                                      
</div>
            