
---
title: 'xmake v2.6.1 发布，使用 Lua5.4 运行时， Rust 和 C++ 混合编译支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=57'
author: 开源中国
comments: false
date: Sat, 04 Dec 2021 10:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=57'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">xmake</a> 是一个基于 Lua 的轻量级跨平台构建工具，使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p>这个版本，我们正式将默认的 Luajit 运行时切换到 Lua5.4 运行时，并且新增了 Rust 和 C++ 的混合编译支持，我们也集成了 Cargo 的包管理支持。</p> 
<p>另外，我们新增了一个实用的 <code>utils.glsl2spv</code> 规则，用于实现对 glsl shader 的编译支持，并自动生成对应的 C 代码头文件，方便快速内嵌编译后的 .spv 文件数据到代码中。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2>新特性介绍</h2> 
<h3>默认切换到 Lua5.4 运行时</h3> 
<p>历经几个版本的迭代测试，我们在 2.6.1 版本，正式切换到 Lua5.4 运行时。</p> 
<p>不过，这对于用户来说是完全无感知的，基本上没有任何兼容性问题，因为 xmake 对大部分接口都是封装过的，完全消除了 Lua 版本间的兼容性问题。</p> 
<p>对于构建性能方面，由于构建的性能瓶颈主要来自编译器，Lua 自身的性能损耗完全可以忽略，而且 xmake 用 c 重写了 lua 原生的所有 io 接口，并且对耗时的接口都用 c 实现了优化。</p> 
<p>因此，通过对比测试，不管是使用 Lua 还是 Luajit，构建项目的耗时基本一致，没有明显差异。</p> 
<h4>为什么要切换？</h4> 
<p>因为 Luajit 对一些新架构基本不支持，例如：riscv, lonngarch，而且 luajit 作者基本已经不怎么维护它了，一些新架构支持和稳定性修复进展属于停滞状态。</p> 
<p>为了能够更好的支持更多的平台，已经获取更快的迭代维护，我们选择使用 Lua 会带来非常多的好处。</p> 
<h3>添加 Cargo 包依赖</h3> 
<p>我们在这个版本中，新增了 Cargo 包依赖管理器的支持，不过目前主要用于 Rust 项目。</p> 
<p>例子: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fdev%2Ftests%2Fprojects%2Frust%2Fcargo_deps" target="_blank">https://github.com/xmake-io/xmake/tree/dev/tests/projects/rust/cargo_deps</a></p> 
<pre><code class="language-lua">add_rules("mode.release", "mode.debug")
add_requires("cargo::base64 0.13.0")
add_requires("cargo::flate2 1.0.17", &#123;configs = &#123;features = "zlib"&#125;&#125;)

target("test")
    set_kind("binary")
    add_files("src/main.rs")
    add_packages("cargo::base64", "cargo::flate2")
</code></pre> 
<h3>Rust 和 C++ 混合编译</h3> 
<h4>使用 cxxbridge 在 c++ 中调用 rust</h4> 
<p>例子: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fdev%2Ftests%2Fprojects%2Frust%2Fcxx_call_rust_library" target="_blank">cxx_call_rust_library</a></p> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

add_requires("cargo::cxx 1.0")

target("foo")
    set_kind("static")
    add_files("src/foo.rs")
    set_values("rust.cratetype", "staticlib")
    add_packages("cargo::cxx")

target("test")
    set_kind("binary")
    add_rules("rust.cxxbridge")
    add_deps("foo")
    add_files("src/main.cc")
    add_files("src/bridge.rsx")
</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ffoo.rs" target="_blank">foo.rs</a></p> 
<pre><code class="language-rust">#[cxx::bridge]
mod foo &#123;
    extern "Rust" &#123;
        fn add(a: i32, b: i32) -> i32;
    &#125;
&#125;

pub fn add(a: i32, b: i32) -> i32 &#123;
    return a + b;
&#125;
</code></pre> 
<p>我们还需要在 c++ 项目中添加桥接文件 bridge.rsx</p> 
<pre><code class="language-rust">#[cxx::bridge]
mod foo &#123;
    extern "Rust" &#123;
        fn add(a: i32, b: i32) -> i32;
    &#125;
&#125;
</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmain.cc" target="_blank">main.cc</a></p> 
<pre><code class="language-c++">#include <stdio.h>
#include "bridge.rs.h"

int main(int argc, char** argv) &#123;
    printf("add(1, 2) == %d\\n", add(1, 2));
    return 0;
&#125;
</code></pre> 
<h4>在 Rust 中调用 C++</h4> 
<p>例子: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fdev%2Ftests%2Fprojects%2Frust%2Frust_call_cxx_library" target="_blank">rust_call_cxx_library</a></p> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

target("foo")
    set_kind("static")
    add_files("src/foo.cc")

target("test")
    set_kind("binary")
    add_deps("foo")
    add_files("src/main.rs")
</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmain.rs" target="_blank">main.rs</a></p> 
<pre><code class="language-rust">extern "C" &#123;
    fn add(a: i32, b: i32) -> i32;
&#125;

fn main() &#123;
    unsafe &#123;
        println!("add(1, 2) = &#123;&#125;", add(1, 2));
    &#125;
&#125;
</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ffoo.cc" target="_blank">foo.cc</a></p> 
<pre><code class="language-c++">extern "C" int add(int a, int b) &#123;
    return a + b;
&#125;
</code></pre> 
<h3>新增 glsl shader 编译规则</h3> 
<p>我们新增了一个 <code>utils.glsl2spv</code> 编译规则，可以在项目中引入 <code>*.vert/*.frag</code> 等 glsl shader 文件，然后实现自动编译生成 <code>*.spv</code> 文件。</p> 
<p>另外，我们还支持以 C/C++ 头文件的方式，二进制内嵌 spv 文件数据，方便程序使用。</p> 
<h4>编译生成 spv 文件</h4> 
<p>xmake 会自动调用 glslangValidator 或者 glslc 去编译 shaders 生成 .spv 文件，然后输出到指定的 <code>&#123;outputdir = "build"&#125;</code> 目录下。</p> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

add_requires("glslang", &#123;configs = &#123;binaryonly = true&#125;&#125;)

target("test")
    set_kind("binary")
    add_rules("utils.glsl2spv", &#123;outputdir = "build"&#125;)
    add_files("src/*.c")
    add_files("src/*.vert", "src/*.frag")
    add_packages("glslang")
</code></pre> 
<p>注，这里的 <code>add_packages("glslang")</code> 主要用于引入和绑定 glslang 包中的 glslangValidator，确保 xmake 总归能够使用它。</p> 
<p>当然，如果用户自己系统上已经安装了它，也可以不用额外绑定这个包，不过我还是建议添加一下。</p> 
<h4>编译生成 c/c++ 头文件</h4> 
<p>我们也可以内部借助 bin2c 模块，将编译后的 spv 文件生成对应的二进制头文件，方便用户代码中直接引入，我们只需要启用 <code>&#123;bin2c = true&#125;</code>。:w</p> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

add_requires("glslang", &#123;configs = &#123;binaryonly = true&#125;&#125;)

target("test")
    set_kind("binary")
    add_rules("utils.glsl2spv", &#123;bin2c = true&#125;)
    add_files("src/*.c")
    add_files("src/*.vert", "src/*.frag")
    add_packages("glslang")
</code></pre> 
<p>然后我们可以在代码这么引入：</p> 
<pre><code class="language-c">static unsigned char g_test_vert_spv_data[] = &#123;
    #include "test.vert.spv.h"
&#125;;

static unsigned char g_test_frag_spv_data[] = &#123;
    #include "test.frag.spv.h"
&#125;;
</code></pre> 
<p>跟 bin2c 规则的使用方式类似，完整例子见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Ftree%2Fmaster%2Ftests%2Fprojects%2Fother%2Fglsl2spv" target="_blank">glsl2spv example</a></p> 
<h3>改进 C++ Modules 构建</h3> 
<p>上个版本，我们重构了 C++20 Modules 构建支持，而在这个版本中，我们继续对它做了改进。</p> 
<p>对于 msvc 编译器，我们已经能够在模块中导入 std 标准库模块，另外，我们修复了多个 target 之间存在依赖时，模块导入编译失败的问题。</p> 
<h3>改进 MDK 程序构建配置</h3> 
<p>上个版本，我们新增了 MDK 程序的构建支持，需要注意的是，目前一些 mdk 程序都使用了 microlib 库运行时，它需要编译器加上 <code>__MICROLIB</code> 宏定义，链接器加上 <code>--library_type=microlib</code> 等各种配置。</p> 
<p>而在这个版本中，我们可以通过 <code>set_runtimes("microlib")</code> 直接设置到 microlib 运行时库，可以自动设置上所有相关选项。</p> 
<h4>控制台程序</h4> 
<pre><code class="language-lua">target("hello")
    add_deps("foo")
    add_rules("mdk.console")
    add_files("src/*.c", "src/*.s")
    add_includedirs("src/lib/cmsis")
    set_runtimes("microlib")
</code></pre> 
<h4>静态库程序</h4> 
<pre><code class="language-lua">add_rules("mode.debug", "mode.release")

target("foo")
    add_rules("mdk.static")
    add_files("src/foo/*.c")
    set_runtimes("microlib")
</code></pre> 
<h3>改进 OpenMP 项目配置</h3> 
<p>我们也改进了 openmp 项目的配置，更加简化和统一，我们不再需要额外配置 rules，仅仅通过一个通用的 openmp 包就可以实现相同的效果。</p> 
<pre><code class="language-lua">add_requires("openmp")
target("loop")
    set_kind("binary")
    add_files("src/*.cpp")
    add_packages("openmp")
</code></pre> 
<p>在之前的版本，我们需要这么配置，对比一下，就能看出新的配置更加的简洁。</p> 
<pre><code class="language-lua">add_requires("libomp", &#123;optional = true&#125;)
target("loop")
    set_kind("binary")
    add_files("src/*.cpp")
    add_rules("c++.openmp")
    add_packages("libomp")
</code></pre> 
<h2>更新内容</h2> 
<h3>新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1799" target="_blank">#1799</a>: 支持混合 Rust 和 C++ 程序，以及集成 Cargo 依赖库</li> 
 <li>添加 <code>utils.glsl2spv</code> 规则去编译 <em>.vert/</em>.frag shader 文件生成 spirv 文件和二进制 C 头文件</li> 
</ul> 
<h3>改进</h3> 
<ul> 
 <li>默认切换到 Lua5.4 运行时</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1776" target="_blank">#1776</a>: 改进 system::find_package，支持从环境变量中查找系统库</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1786" target="_blank">#1786</a>: 改进 apt:find_package，支持查找 alias 包</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1819" target="_blank">#1819</a>: 添加预编译头到 cmake 生成器</li> 
 <li>改进 C++20 Modules 为 msvc 支持 std 标准库</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1792" target="_blank">#1792</a>: 添加自定义命令到 vs 工程生成器</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1835" target="_blank">#1835</a>: 改进 MDK 程序构建支持，增加 <code>set_runtimes("microlib")</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1858" target="_blank">#1858</a>: 改进构建 c++20 modules，修复跨 target 构建问题</li> 
 <li>添加 $XMAKE_BINARY_REPO 和 $XMAKE_MAIN_REPO 仓库设置环境变量</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1865" target="_blank">#1865</a>: 改进 openmp 工程</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1845" target="_blank">#1845</a>: 为静态库安装 pdb 文件</li> 
</ul> 
<h3>Bugs 修复</h3> 
<ul> 
 <li>修复语义版本中解析带有 0 前缀的 build 字符串问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibbpf%2Flibbpf-bootstrap%2Fissues%2F50" target="_blank">#50</a>: 修复 rule 和构建 bpf 程序 bug</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1610" target="_blank">#1610</a>: 修复 <code>xmake f --menu</code> 在 vscode 终端下按键无响应，并且支持 ConPTY 终端虚拟按键</li> 
</ul>
                                        </div>
                                      
</div>
            