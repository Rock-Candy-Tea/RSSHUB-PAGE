
---
title: 'xmake v2.5.9 发布，改进 C++20 模块, 支持 Nim, Unity Build'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7806'
author: 开源中国
comments: false
date: Mon, 01 Nov 2021 09:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7806'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">xmake</a> 是一个基于 Lua 的轻量级跨平台构建工具，使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p>这个版本，我们增加了大量重量级的新特性，例如：Nim 语言项目的构建支持，Keil MDK，Circle 和 Wasi 工具链支持。</p> 
<p>另外，我们对 C++20 Modules 进行了大改进，不仅支持最新 gcc-11, clang 和 msvc 编译器，而且还得模块间依赖做了自动分析，实现最大程度的并行化编译支持。</p> 
<p>最后，还有一个比较有用的特性就是 Unity Build 支持，通过它我们可以对 C++ 代码的编译速度做到很大程度的提升。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2>新特性介绍</h2> 
<h3>Nimlang 项目构建</h3> 
<p>最近，我们新增了对 Nimlang 项目的构建支持，相关 issues 见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1756" target="_blank">#1756</a></p> 
<h4>创建空工程</h4> 
<p>我们可以使用 <code>xmake create</code> 命令创建空工程。</p> 
<pre><code class="language-console">xmake create -l nim -t console test
xmake create -l nim -t static test
xmake create -l nim -t shared test
</code></pre> 
<h4>控制台程序</h4> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

target("test")
    set_kind("binary")
    add_files("src/main.nim")
</code></pre> 
<pre><code class="language-console">$ xmake -v
[ 33%]: linking.release test
/usr/local/bin/nim c --opt:speed --nimcache:build/.gens/test/macosx/x86_64/release/nimcache -o:b
uild/macosx/x86_64/release/test src/main.nim
[100%]: build ok!
</code></pre> 
<h4>静态库程序</h4> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

target("foo")
    set_kind("static")
    add_files("src/foo.nim")

target("test")
    set_kind("binary")
    add_deps("foo")
    add_files("src/main.nim")
</code></pre> 
<pre><code class="language-console">$ xmake -v
[ 33%]: linking.release libfoo.a
/usr/local/bin/nim c --opt:speed --nimcache:build/.gens/foo/macosx/x86_64/release/nimcache --app
:staticlib --noMain --passC:-DNimMain=NimMain_B6D5BD02 --passC:-DNimMainInner=NimMainInner_B6D5B
D02 --passC:-DNimMainModule=NimMainModule_B6D5BD02 --passC:-DPreMain=PreMain_B6D5BD02 --passC:-D
PreMainInner=PreMainInner_B6D5BD02 -o:build/macosx/x86_64/release/libfoo.a src/foo.nim
[ 66%]: linking.release test
/usr/local/bin/nim c --opt:speed --nimcache:build/.gens/test/macosx/x86_64/release/nimcache --pa
ssL:-Lbuild/macosx/x86_64/release --passL:-lfoo -o:build/macosx/x86_64/release/test src/main.nim
[100%]: build ok!
</code></pre> 
<h4>动态库程序</h4> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

target("foo")
    set_kind("shared")
    add_files("src/foo.nim")

target("test")
    set_kind("binary")
    add_deps("foo")
    add_files("src/main.nim")
</code></pre> 
<pre><code class="language-console">$ xmake -rv
[ 33%]: linking.release libfoo.dylib
/usr/local/bin/nim c --opt:speed --nimcache:build/.gens/foo/macosx/x86_64/release/nimcache --app
:lib --noMain -o:build/macosx/x86_64/release/libfoo.dylib src/foo.nim
[ 66%]: linking.release test
/usr/local/bin/nim c --opt:speed --nimcache:build/.gens/test/macosx/x86_64/release/nimcache --pa
ssL:-Lbuild/macosx/x86_64/release --passL:-lfoo -o:build/macosx/x86_64/release/test src/main.nim
[100%]: build ok!
</code></pre> 
<h4>C 代码混合编译</h4> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

target("foo")
    set_kind("static")
    add_files("src/*.c")

target("test")
    set_kind("binary")
    add_deps("foo")
    add_files("src/main.nim")
</code></pre> 
<h4>Nimble 依赖包集成</h4> 
<p>完整例子见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fdev%2Ftests%2Fprojects%2Fnim%2Fnimble_package" target="_blank">Nimble Package Example</a></p> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

add_requires("nimble::zip >0.3")

target("test")
    set_kind("binary")
    add_files("src/main.nim")
    add_packages("nimble::zip")
</code></pre> 
<p>main.nim</p> 
<pre><code class="language-nim">import zip/zlib

echo zlibVersion()
</code></pre> 
<h4>Native 依赖包集成</h4> 
<p>完整例子见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fdev%2Ftests%2Fprojects%2Fnim%2Fnative_package" target="_blank">Native Package Example</a></p> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

add_requires("zlib")

target("test")
    set_kind("binary")
    add_files("src/main.nim")
    add_packages("zlib")
</code></pre> 
<p>main.nim</p> 
<pre><code class="language-nim">proc zlibVersion(): cstring &#123;.cdecl, importc&#125;

echo zlibVersion()
</code></pre> 
<h3>Unity Build 加速</h3> 
<p>我们知道，C++ 代码编译速度通常很慢，因为每个代码文件都需要解析引入的头文件。</p> 
<p>而通过 Unity Build，我们通过将多个 cpp 文件组合成一个来加速项目的编译，其主要好处是减少了解析和编译包含在多个源文件中的头文件内容的重复工作，头文件的内容通常占预处理后源文件中的大部分代码。</p> 
<p>Unity 构建还通过减少编译链创建和处理的目标文件的数量来减轻由于拥有大量小源文件而导致的开销，并允许跨形成统一构建任务的文件进行过程间分析和优化（类似于效果链接时优化）。</p> 
<p>它可以极大提升 C/C++ 代码的编译速度，通常会有 30% 的速度提升，不过根据项目的复杂程度不同，其带来的效益还是要根据自身项目情况而定。</p> 
<p>xmake 在 v2.5.9 版本中，也已经支持了这种构建模式。相关 issues 见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1019" target="_blank">#1019</a>。</p> 
<h4>如何启用？</h4> 
<p>我们提供了两个内置规则，分别处理对 C 和 C++ 代码的 Unity Build。</p> 
<pre><code class="language-lua">add_rules("c.unity_build")
add_rules("c++.unity_build")
</code></pre> 
<h4>Batch 模式</h4> 
<p>默认情况下，只要设置上述规则，就会启用 Batch 模式的 Unity Build，也就是 xmake 自动根据项目代码文件，自动组织合并。</p> 
<pre><code class="language-lua">target("test")
    set_kind("binary")
    add_includedirs("src")
    add_rules("c++.unity_build", &#123;batchsize = 2&#125;)
    add_files("src/*.c", "src/*.cpp")
</code></pre> 
<p>我们可以额外通过设置 <code>&#123;batchsize = 2&#125;</code> 参数到规则，来指定每个合并 Batch 的大小数量，这里也就是每两个 C++ 文件自动合并编译。</p> 
<p>编译效果大概如下：</p> 
<pre><code class="language-console">$ xmake -r
[ 11%]: ccache compiling.release build/.gens/test/unity_build/unity_642A245F.cpp
[ 11%]: ccache compiling.release build/.gens/test/unity_build/unity_bar.cpp
[ 11%]: ccache compiling.release build/.gens/test/unity_build/unity_73161A20.cpp
[ 11%]: ccache compiling.release build/.gens/test/unity_build/unity_F905F036.cpp
[ 11%]: ccache compiling.release build/.gens/test/unity_build/unity_foo.cpp
[ 11%]: ccache compiling.release build/.gens/test/unity_build/main.c
[ 77%]: linking.release test
[100%]: build ok
</code></pre> 
<p>由于我们仅仅启用了 C++ 的 Unity Build，所以 C 代码还是正常挨个编译。另外在 Unity Build 模式下，我们还是可以做到尽可能的并行编译加速，互不冲突。</p> 
<p>如果没有设置 <code>batchsize</code> 参数，那么默认会吧所有文件合并到一个文件中进行编译。</p> 
<h4>Group 模式</h4> 
<p>如果上面的 Batch 模式自动合并效果不理想，我们也可以使用自定义分组，来手动配置哪些文件合并到一起参与编译，这使得用户更加地灵活可控。</p> 
<pre><code class="language-lua">target("test")
    set_kind("binary")
    add_rules("c++.unity_build", &#123;batchsize = 0&#125;) -- disable batch mode
    add_files("src/*.c", "src/*.cpp")
    add_files("src/foo/*.c", &#123;unity_group = "foo"&#125;)
    add_files("src/bar/*.c", &#123;unity_group = "bar"&#125;)
</code></pre> 
<p>我们使用 <code>&#123;unity_group = "foo"&#125;</code> 来指定每个分组的名字，以及包含了哪些文件，每个分组的文件都会单独被合并到一个代码文件中去。</p> 
<p>另外，<code>batchsize = 0</code> 也强行禁用了 Batch 模式，也就是说，没有设置 unity_group 分组的代码文件，我们还是会单独编译它们，也不会自动开启自动合并。</p> 
<h4>Batch 和 Group 混合模式</h4> 
<p>我们只要把上面的 <code>batchsize = 0</code> 改成非 0 值，就可以让分组模式下，剩余的代码文件继续开启 Batch 模式自动合并编译。</p> 
<pre><code class="language-lua">target("test")
    set_kind("binary")
    add_includedirs("src")
    add_rules("c++.unity_build", &#123;batchsize = 2&#125;)
    add_files("src/*.c", "src/*.cpp")
    add_files("src/foo/*.c", &#123;unity_group = "foo"&#125;)
    add_files("src/bar/*.c", &#123;unity_group = "bar"&#125;)
</code></pre> 
<h4>忽略指定文件</h4> 
<p>如果是 Batch 模式下，由于是自动合并操作，所以默认会对所有文件执行合并，但如果有些代码文件我们不想让它参与合并，那么我们也可以通过 <code>&#123;unity_ignored = true&#125;</code> 去忽略它们。</p> 
<pre><code class="language-lua">target("test")
    set_kind("binary")
    add_includedirs("src")
    add_rules("c++.unity_build", &#123;batchsize = 2&#125;)
    add_files("src/*.c", "src/*.cpp")
    add_files("src/test/*.c", &#123;unity_ignored = true&#125;) -- ignore these files
</code></pre> 
<h4>Unique ID</h4> 
<p>尽管 Unity Build 带啦的收益不错，但是我们还是会遇到一些意外的情况，比如我们的两个代码文件里面，全局命名空间下，都存在相同名字的全局变量和函数。</p> 
<p>那么，合并编译就会带来编译冲突问题，编译器通常会报全局变量重定义错误。</p> 
<p>为了解决这个问题，我们需要用户代码上做一些修改，然后配合构建工具来解决。</p> 
<p>比如，我们的 foo.cpp 和 bar.cpp 都有全局变量 i。</p> 
<p>foo.cpp</p> 
<pre><code class="language-c">namespace &#123;
    int i = 42;
&#125;

int foo()
&#123;
    return i;
&#125;
</code></pre> 
<p>bar.cpp</p> 
<pre><code class="language-c">namespace &#123;
    int i = 42;
&#125;

int bar()
&#123;
    return i;
&#125;
</code></pre> 
<p>那么，我们合并编译就会冲突，我们可以引入一个 Unique ID 来隔离全局的匿名空间。</p> 
<p>foo.cpp</p> 
<pre><code class="language-c">namespace MY_UNITY_ID &#123;
    int i = 42;
&#125;

int foo()
&#123;
    return MY_UNITY_ID::i;
&#125;
</code></pre> 
<p>bar.cpp</p> 
<pre><code class="language-c">namespace MY_UNITY_ID &#123;
    int i = 42;
&#125;

int bar()
&#123;
    return MY_UNITY_ID::i;
&#125;
</code></pre> 
<p>接下来，我们还需要保证代码合并后， <code>MY_UNITY_ID</code> 在 foo 和 bar 中的定义完全不同，可以按文件名算一个唯一 ID 值出来，互不冲突，也就是实现下面的合并效果：</p> 
<pre><code class="language-c">#define MY_UNITY_ID <hash(foo.cpp)>
#include "foo.c"
#undef MY_UNITY_ID
#define MY_UNITY_ID <hash(bar.cpp)>
#include "bar.c"
#undef MY_UNITY_ID
</code></pre> 
<p>这看上去似乎很麻烦，但是用户不需要关心这些，xmake 会在合并时候自动处理它们，用户只需要指定这个 Unique ID 的名字就行了，例如下面这样：</p> 
<pre><code class="language-lua">target("test")
    set_kind("binary")
    add_includedirs("src")
    add_rules("c++.unity_build", &#123;batchsize = 2, uniqueid = "MY_UNITY_ID"&#125;)
    add_files("src/*.c", "src/*.cpp")
</code></pre> 
<p>处理全局变量，还有全局的重名宏定义，函数什么的，都可以采用这种方式来避免冲突。</p> 
<h3>C++20 Modules</h3> 
<p>xmake 采用 <code>.mpp</code> 作为默认的模块扩展名，但是也同时支持 <code>.ixx</code>, <code>.cppm</code>, <code>.mxx</code> 等扩展名。</p> 
<p>早期，xmake 试验性支持过 C++ Modules TS，但是那个时候，gcc 还不能很好的支持，并且模块间的依赖也不支持。</p> 
<p>最近，我们对 xmake 做了大量改进，已经完整支持 gcc-11/clang/msvc 的 C++20 Modules 构建支持，并且能够自动分析模块间的依赖关系，实现最大化并行编译。</p> 
<p>同时，对新版本的 clang/msvc 也做了更好地处理。</p> 
<pre><code class="language-lua">set_languages("c++20")
target("test")
    set_kind("binary")
    add_files("src/*.cpp", "src/*.mpp")
</code></pre> 
<p>更多例子见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fmaster%2Ftests%2Fprojects%2Fc%252B%252B%2Fmodules" target="_blank">C++ Modules</a></p> 
<h3>Lua5.4 运行时支持</h3> 
<p>上个版本，我们增加了对 Lua5.3 运行时支持，而在这个版本中，我们进一步升级 Lua 运行时到 5.4，相比 5.3，运行性能和内存利用率上都有很大的提升。</p> 
<p>不过，目前 xmake 的默认运行时还是 luajit，预计 2.6.1 版本（也就是下个版本），会正式切到 Lua5.4 作为默认的运行时。</p> 
<p>尽管切换了 Lua 运行时，但是对于用户端，完全是无感知的，并且完全兼容现有工程配置，因为 xmake 原本就对暴露的 api 提供了一层封装， 对于 lua 版本之间存在兼容性问题的接口，例如 setfenv, ffi 等都隐藏在内部，原本就没有暴露给用户使用。</p> 
<h3>Keil MDK 工具链支持</h3> 
<p>我们在这个版本中，还新增了 Keil/MDK 嵌入式编译工具链的支持，相关例子工程：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fdev%2Ftests%2Fprojects%2Fmdk%2Fhello" target="_blank">Example</a></p> 
<p>xmake 会自动探测 Keil/MDK 安装的编译器，相关 issues <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1753" target="_blank">#1753</a>。</p> 
<h4>使用 armcc 编译</h4> 
<pre><code class="language-console">$ xmake f -p cross -a cortex-m3 --toolchain=armcc -c
$ xmake
</code></pre> 
<h4>使用 armclang 编译</h4> 
<pre><code class="language-console">$ xmake f -p cross -a cortex-m3 --toolchain=armclang -c
$ xmake
</code></pre> 
<h4>控制台程序</h4> 
<pre><code class="language-lua">target("hello")
    add_deps("foo")
    add_rules("mdk.console")
    add_files("src/*.c", "src/*.s")
    add_defines("__EVAL", "__MICROLIB")
    add_includedirs("src/lib/cmsis")
</code></pre> 
<h4>静态库程序</h4> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

target("foo")
    add_rules("mdk.static")
    add_files("src/foo/*.c")
</code></pre> 
<h3>Wasi 工具链支持</h3> 
<p>之前我们支持了 wasm 平台的 emcc 工具链来构建 wasm 程序，而这里，我们新加了另外一个启用了 WASI 的 Wasm 工具链来替换 emcc。</p> 
<pre><code class="language-console">$ xmake f -p wasm --toolchain=wasi
$ xmake
</code></pre> 
<h3>Circle 工具链支持</h3> 
<p>我们还新增了 circle 编译器的支持，这是个新的 C++20 编译器，额外附带了一些有趣的编译期元编程特性，有兴趣的同学可以到官网查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.circle-lang.org%2F" target="_blank">https://www.circle-lang.org/</a></p> 
<pre><code class="language-console">$ xmake f --toolchain=circle
$ xmake
</code></pre> 
<h3>gcc-8/9/10/11 特定版本支持</h3> 
<p>如果用户额外安装了 gcc-11, gcc-10 等特定版本的 gcc 工具链，在本地的 gcc 程序命名可能是 <code>/usr/bin/gcc-11</code>。</p> 
<p>一种办法是通过 <code>xmake f --cc=gcc-11 --cxx=gcc-11 --ld=g++-11</code> 挨个指定配置来切换，但非常繁琐。</p> 
<p>所以，xmake 也提供了更加快捷的切换方式：</p> 
<pre><code class="language-console">$ xmake f --toolchain=gcc-11 -c
$ xmake
</code></pre> 
<p>只需要指定 <code>gcc-11</code> 对应的版本名，就可以快速切换整个 gcc 工具链。</p> 
<h3>C++17/20 编译器特性检测</h3> 
<p>xmake 提供了 check_features 辅助接口来检测编译器特性。</p> 
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
<p>而在 2.5.9 版本中，我们新增了 c++17 特性检测：</p> 
<table> 
 <thead> 
  <tr> 
   <th>特性名</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>cxx_aggregate_bases</td> 
  </tr> 
  <tr> 
   <td>cxx_aligned_new</td> 
  </tr> 
  <tr> 
   <td>cxx_capture_star_this</td> 
  </tr> 
  <tr> 
   <td>cxx_constexpr</td> 
  </tr> 
  <tr> 
   <td>cxx_deduction_guides</td> 
  </tr> 
  <tr> 
   <td>cxx_enumerator_attributes</td> 
  </tr> 
  <tr> 
   <td>cxx_fold_expressions</td> 
  </tr> 
  <tr> 
   <td>cxx_guaranteed_copy_elision</td> 
  </tr> 
  <tr> 
   <td>cxx_hex_float</td> 
  </tr> 
  <tr> 
   <td>cxx_if_constexpr</td> 
  </tr> 
  <tr> 
   <td>cxx_inheriting_constructors</td> 
  </tr> 
  <tr> 
   <td>cxx_inline_variables</td> 
  </tr> 
  <tr> 
   <td>cxx_namespace_attributes</td> 
  </tr> 
  <tr> 
   <td>cxx_noexcept_function_type</td> 
  </tr> 
  <tr> 
   <td>cxx_nontype_template_args</td> 
  </tr> 
  <tr> 
   <td>cxx_nontype_template_parameter_auto</td> 
  </tr> 
  <tr> 
   <td>cxx_range_based_for</td> 
  </tr> 
  <tr> 
   <td>cxx_static_assert</td> 
  </tr> 
  <tr> 
   <td>cxx_structured_bindings</td> 
  </tr> 
  <tr> 
   <td>cxx_template_template_args</td> 
  </tr> 
  <tr> 
   <td>cxx_variadic_using</td> 
  </tr> 
 </tbody> 
</table> 
<p>还新增了 c++20 特性检测：</p> 
<table> 
 <thead> 
  <tr> 
   <th>特性名</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>cxx_aggregate_paren_init</td> 
  </tr> 
  <tr> 
   <td>cxx_char8_t</td> 
  </tr> 
  <tr> 
   <td>cxx_concepts</td> 
  </tr> 
  <tr> 
   <td>cxx_conditional_explicit</td> 
  </tr> 
  <tr> 
   <td>cxx_consteval</td> 
  </tr> 
  <tr> 
   <td>cxx_constexpr</td> 
  </tr> 
  <tr> 
   <td>cxx_constexpr_dynamic_alloc</td> 
  </tr> 
  <tr> 
   <td>cxx_constexpr_in_decltype</td> 
  </tr> 
  <tr> 
   <td>cxx_constinit</td> 
  </tr> 
  <tr> 
   <td>cxx_deduction_guides</td> 
  </tr> 
  <tr> 
   <td>cxx_designated_initializers</td> 
  </tr> 
  <tr> 
   <td>cxx_generic_lambdas</td> 
  </tr> 
  <tr> 
   <td>cxx_impl_coroutine</td> 
  </tr> 
  <tr> 
   <td>cxx_impl_destroying_delete</td> 
  </tr> 
  <tr> 
   <td>cxx_impl_three_way_comparison</td> 
  </tr> 
  <tr> 
   <td>cxx_init_captures</td> 
  </tr> 
  <tr> 
   <td>cxx_modules</td> 
  </tr> 
  <tr> 
   <td>cxx_nontype_template_args</td> 
  </tr> 
  <tr> 
   <td>cxx_using_enum</td> 
  </tr> 
 </tbody> 
</table> 
<h3>Xrepo 包虚拟环境管理</h3> 
<h4>进入虚拟环境</h4> 
<p>xmake 自带的 xrepo 包管理工具，现在已经可以很好的支持包虚拟机环境管理，类似 nixos 的 nixpkgs。</p> 
<p>我们可以通过在当前目录下，添加 xmake.lua 文件，定制化一些包配置，然后进入特定的包虚拟环境。</p> 
<pre><code class="language-lua">add_requires("zlib 1.2.11")
add_requires("python 3.x", "luajit")
</code></pre> 
<pre><code class="language-console">$ xrepo env shell
> python --version
> luajit --version
</code></pre> 
<p>我们也可以在 xmake.lua 配置加载对应的工具链环境，比如加载 vs 的编译环境。</p> 
<pre><code class="language-lua">set_toolchains("msvc")
</code></pre> 
<h4>管理虚拟环境</h4> 
<p>我们可以使用下面的命令，把指定的虚拟环境配置全局注册到系统中，方便快速切换。</p> 
<pre><code class="language-console">$ xrepo env --add /tmp/base.lua
</code></pre> 
<p>这个时候，我们就保存了一个名叫 base 的全局虚拟环境，我们可以通过 list 命令去查看它。</p> 
<pre><code class="language-console">$ xrepo env --list
/Users/ruki/.xmake/envs:
  - base
envs(1) found!
</code></pre> 
<p>我们也可以删除它。</p> 
<pre><code class="language-console">$ xrepo env --remove base
</code></pre> 
<h4>切换全局虚拟环境</h4> 
<p>如果我们注册了多个虚拟环境，我们也可以快速切换它们。</p> 
<pre><code class="language-console">$ xrepo env -b base shell
> python --version
</code></pre> 
<p>或者直接加载指定虚拟环境运行特定命令</p> 
<pre><code class="language-console">$ xrepo env -b base python --version
</code></pre> 
<p><code>xrepo env -b/--bind</code> 就是绑定指定的虚拟环境，更多详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1762" target="_blank">#1762</a></p> 
<h3>Header Only 目标类型</h3> 
<p>对于 target，我们新增了 <code>headeronly</code> 目标类型，这个类型的目标程序，我们不会实际编译它们，因为它没有源文件需要被编译。</p> 
<p>但是它包含了头文件列表，这通常用于 headeronly 库项目的安装，IDE 工程的文件列表生成，以及安装阶段的 cmake/pkgconfig 导入文件的生成。</p> 
<p>例如：</p> 
<pre><code class="language-lua">add_rules("mode.release", "mode.debug")

target("foo")
    set_kind("headeronly")
    add_headerfiles("src/foo.h")
    add_rules("utils.install.cmake_importfiles")
    add_rules("utils.install.pkgconfig_importfiles")
</code></pre> 
<p>更多详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1747" target="_blank">#1747</a></p> 
<h3>从 CMake 中查找包</h3> 
<p>现在 cmake 已经是事实上的标准，所以 CMake 提供的 find_package 已经可以查找大量的库和模块，我们完全复用 cmake 的这部分生态来扩充 xmake 对包的集成。</p> 
<p>我们可以通过 <code>find_package("cmake::xxx")</code> 去借助 cmake 来找一些包，xmake 会自动生成一个 cmake 脚本来调用 cmake 的 find_package 去查找一些包，获取里面包信息。</p> 
<p>例如：</p> 
<pre><code class="language-console">$ xmake l find_package cmake::ZLIB
&#123;
  links = &#123;
    "z"
  &#125;,
  includedirs = &#123;
    "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.
15.sdk/usr/include"
  &#125;,
  linkdirs = &#123;
    "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.
15.sdk/usr/lib"
  &#125;
&#125;
$ xmake l find_package cmake::LibXml2
&#123;
  links = &#123;
    "xml2"
  &#125;,
  includedirs = &#123;
    "/Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include/libxml2"
  &#125;,
  linkdirs = &#123;
    "/usr/lib"
  &#125;
&#125;
</code></pre> 
<h4>指定版本</h4> 
<pre><code class="language-lua">find_package("cmake::OpenCV", &#123;required_version = "4.1.1"&#125;)
</code></pre> 
<h4>指定组件</h4> 
<pre><code class="language-lua">find_package("cmake::Boost", &#123;components = &#123;"regex", "system"&#125;&#125;)
</code></pre> 
<h4>预设开关</h4> 
<pre><code class="language-lua">find_package("cmake::Boost", &#123;components = &#123;"regex", "system"&#125;, presets = &#123;Boost_USE_STATIC_LIB = true&#125;&#125;)
set(Boost_USE_STATIC_LIB ON) -- will be used in FindBoost.cmake
find_package(Boost REQUIRED COMPONENTS regex system)
</code></pre> 
<h4>设置环境变量</h4> 
<pre><code class="language-lua">find_package("cmake::OpenCV", &#123;envs = &#123;CMAKE_PREFIX_PATH = "xxx"&#125;&#125;)
</code></pre> 
<h4>指定自定义 FindFoo.cmake 模块脚本目录</h4> 
<p>mydir/cmake_modules/FindFoo.cmake</p> 
<pre><code class="language-lua">find_package("cmake::Foo", &#123;moduledirs = "mydir/cmake_modules"&#125;)
</code></pre> 
<h4>包依赖集成</h4> 
<pre><code class="language-lua">package("xxx")
    on_fetch(function (package, opt)
         return package:find_package("cmake::xxx", opt)
    end)
package_end()

add_requires("xxx")
</code></pre> 
<h4>包依赖集成（可选组件）</h4> 
<pre><code class="language-lua">package("boost")
    add_configs("regex",   &#123; description = "Enable regex.", default = false, type = "boolean"&#125;)
    on_fetch(function (package, opt)
         opt.components = &#123;&#125;
         if package:config("regex") then
             table.insert(opt.components, "regex")
         end
         return package:find_package("cmake::Boost", opt)
    end)
package_end()

add_requires("boost", &#123;configs = &#123;regex = true&#125;&#125;)
</code></pre> 
<p>相关 issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1632" target="_blank">#1632</a></p> 
<h3>添加自定义命令到 CMakelists.txt</h3> 
<p>我们进一步改进了 cmake 生成器，现在可以将 rule 里面自定义的脚本序列化成命令列表，一起生成到 CMakelists.txt</p> 
<p>不过目前只能支持 batchcmds 系列脚本的序列化。</p> 
<pre><code class="language-lua">rule("foo")
    after_buildcmd(function (target, batchcmds, opt)
        batchcmds:show("hello xmake!")
        batchcmds:cp("xmake.lua", "/tmp/")
        -- batchcmds:execv("echo", &#123;"hello", "world!"&#125;)
        -- batchcmds:runv("echo", &#123;"hello", "world!"&#125;)
    end)

target("test")
    set_kind("binary")
    add_rules("foo")
    add_files("src/*.c")
</code></pre> 
<p>它将会生成类似如下的 CMakelists.txt</p> 
<pre><code># ...
add_custom_command(TARGET test
    POST_BUILD
    COMMAND echo hello xmake!
    VERBATIM
)
add_custom_command(TARGET test
    POST_BUILD
    COMMAND cp xmake.lua /tmp/
    VERBATIM
)
target_sources(test PRIVATE
    src/main.c
)
</code></pre> 
<p>不过 cmake 的 <code>ADD_CUSTOM_COMMAND</code> PRE_BUILD 实际效果在不同生成器上，差异比较大，无法满足我们的需求，因此我们做了很多处理来支持它。</p> 
<p>相关 issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1735" target="_blank">#1735</a></p> 
<h3>改进对 NixOS 的安装支持</h3> 
<p>我们还改进了 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fget.sh" target="_blank">get.sh</a> 安装脚本，来更好地支持 nixOS。</p> 
<h2>更新内容</h2> 
<h3>新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1736" target="_blank">#1736</a>: 支持 wasi-sdk 工具链</li> 
 <li>支持 Lua 5.4 运行时</li> 
 <li>添加 gcc-8, gcc-9, gcc-10, gcc-11 工具链</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1632" target="_blank">#1623</a>: 支持 find_package 从 cmake 查找包</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1747" target="_blank">#1747</a>: 添加 <code>set_kind("headeronly")</code> 更好的处理 headeronly 库的安装</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1019" target="_blank">#1019</a>: 支持 Unity build</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1438" target="_blank">#1438</a>: 增加 <code>xmake l cli.amalgamate</code> 命令支持代码合并</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1756" target="_blank">#1765</a>: 支持 nim 语言</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1762" target="_blank">#1762</a>: 为 <code>xrepo env</code> 管理和切换指定的环境配置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1767" target="_blank">#1767</a>: 支持 Circle 编译器</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1753" target="_blank">#1753</a>: 支持 Keil/MDK 的 armcc/armclang 工具链</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1774" target="_blank">#1774</a>: 添加 table.contains api</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1735" target="_blank">#1735</a>: 添加自定义命令到 cmake 生成器</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1781" target="_blank">#1781</a>: 改进 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fget.sh" target="_blank">get.sh</a> 安装脚本支持 nixos</li> 
</ul> 
<h3>改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1528" target="_blank">#1528</a>: 检测 c++17/20 特性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1729" target="_blank">#1729</a>: 改进 C++20 modules 对 clang/gcc/msvc 的支持，支持模块间依赖编译和并行优化</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1779" target="_blank">#1779</a>: 改进 ml.exe/x86，移除内置的 <code>-Gd</code> 选项</li> 
</ul>
                                        </div>
                                      
</div>
            