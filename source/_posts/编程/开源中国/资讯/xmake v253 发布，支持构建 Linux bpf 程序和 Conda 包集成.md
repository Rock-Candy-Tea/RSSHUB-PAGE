
---
title: 'xmake v2.5.3 发布，支持构建 Linux bpf 程序和 Conda 包集成'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1304'
author: 开源中国
comments: false
date: Thu, 08 Apr 2021 09:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1304'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">xmake</a> 是一个基于 Lua 的轻量级跨平台构建工具，使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p style="text-align:start">在 2.5.3 版本，我们新增了对 linux bpf 程序的构建支持，并且同时支持 android bpf 程序的构建。</p> 
<p style="text-align:start">尽管 bpf 对 编译工具链有一定的要求，比如需要较新的 llvm/clang 和 android ndk 工具链，但是 xmake 能够自动拉取特定版本的 llvm/ndk 来用于编译，并且还能自动拉取 libbpf 等依赖库，完全省去了用户折腾编译环境和 libbpf 库集成的问题。</p> 
<p style="text-align:start">另外，在新版本中我们还新增了对 Conda 包仓库的集成支持，现在除了能够从 Conan/Vcpkg/brew/pacman/clib/dub 等包仓库集成使用包，还能从 Conda 包仓库中集成各种二进制 C/C++ 包。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2 style="text-align:start">新特性介绍</h2> 
<h3 style="text-align:start">构建 Linux Bpf 程序</h3> 
<p style="text-align:start">新版本，我们开始支持 bpf 程序构建，同时支持 linux 以及 android 平台，能够自动拉取 llvm 和 android ndk 工具链。</p> 
<p style="text-align:start">更多详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1274" target="_blank">#1274</a></p> 
<p style="text-align:start">支持 linux 和 android 两端构建的配置大概如下，如果我们不需要构建 android 版本，可以做一些删减，配置会更加精简：</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_rules</span><strong>(</strong><span style="color:#ff00ff">"mode.release"</span><strong>,</strong> <span style="color:#ff00ff">"mode.debug"</span><strong>)</strong>
<span style="color:#000000">add_rules</span><strong>(</strong><span style="color:#ff00ff">"platform.linux.bpf"</span><strong>)</strong>

<span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"linux-tools"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">configs</span> <strong>=</strong> <strong>&#123;</strong><span style="color:#000000">bpftool</span> <strong>=</strong> <strong>true</strong><strong>&#125;&#125;)</strong>
<span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"libbpf"</span><strong>)</strong>
<span style="color:blue">if</span> <span style="color:#000000">is_plat</span><strong>(</strong><span style="color:#ff00ff">"android"</span><strong>)</strong> <span style="color:blue">then</span>
    <span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"ndk >=22.x"</span><strong>)</strong>
    <span style="color:#000000">set_toolchains</span><strong>(</strong><span style="color:#ff00ff">"@ndk"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">sdkver</span> <strong>=</strong> <span style="color:#ff00ff">"23"</span><strong>&#125;)</strong>
<span style="color:blue">else</span>
    <span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"llvm >=10.x"</span><strong>)</strong>
    <span style="color:#000000">set_toolchains</span><strong>(</strong><span style="color:#ff00ff">"@llvm"</span><strong>)</strong>
    <span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"linux-headers"</span><strong>)</strong>
<span style="color:blue">end</span>

<span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"minimal"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.c"</span><strong>)</strong>
    <span style="color:#000000">add_packages</span><strong>(</strong><span style="color:#ff00ff">"linux-tools"</span><strong>,</strong> <span style="color:#ff00ff">"linux-headers"</span><strong>,</strong> <span style="color:#ff00ff">"libbpf"</span><strong>)</strong>
    <span style="color:#000000">set_license</span><strong>(</strong><span style="color:#ff00ff">"GPL-2.0"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">通过上面的配置，大概可以看出，我们集成配置了特定版本的 llvm 和 NDK 工具链，以及 libbpf, linux-headers, linux-tools 等包，xmake 都会去自动拉取它们，然后使用对应的工具链集成编译这些依赖包，最后生成 bpf 程序。</p> 
<p style="text-align:start">其中 linux-tools 包主要使用了里面的 libtool 程序，用于生成 bpf skeleton 头文件，xmake 也会自动调用这个工具去生成它。</p> 
<h4 style="text-align:start">编译 linux bpf 程序</h4> 
<p style="text-align:start">我们只需要执行 xmake 命令即可完成编译，即使你还没安装 llvm/clang，当然，如果你已经安装了它们，如果版本匹配，xmake 也会去优先使用。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#8f5902">$ </span>xmake
</code></pre> 
</div> 
<p style="text-align:start">我们也可以通过 <code>xmake -v</code> 来编译并且查看完整详细的编译命令：</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#8f5902">$ </span>xmake -v
<strong>[</strong> 20%]: compiling.bpf src/minimal.bpf.c
/usr/bin/ccache /usr/bin/clang -c -Qunused-arguments -m64 -fvisibility<strong>=</strong>hidden -O3 -Ibuild/.gens/minimal/linux/x86_64/release/rules/bpf -isystem /home/ruki/.xmake/packages/l/linux-tools/5.9.16/0c52e491268946fe9a4bc91d4906d66b/include -isystem /home/ruki/.xmake/packages/z/zlib/1.2.11/3a7e4427eda94fc69fad0009a1629fd8/include -isystem /home/ruki/.xmake/packages/l/libelf/0.8.13/ced4fdd8151a475dafc5f51e2a031997/include -isystem /home/ruki/.xmake/packages/l/libelf/0.8.13/ced4fdd8151a475dafc5f51e2a031997/include/libelf -isystem /home/ruki/.xmake/packages/l/libcap/2.27/c55b28aa3b3745489b93895d0d606ed1/include -isystem /home/ruki/.xmake/packages/l/linux-headers/5.9.16/8e3a440cbe1f42249aef3d89f1528ecb/include -DNDEBUG -target bpf -g -o build/.gens/minimal/linux/x86_64/release/rules/bpf/minimal.bpf.o src/minimal.bpf.c
llvm-strip -g build/.gens/minimal/linux/x86_64/release/rules/bpf/minimal.bpf.o
bpftool gen skeleton build/.gens/minimal/linux/x86_64/release/rules/bpf/minimal.bpf.o
<strong>[</strong> 40%]: ccache compiling.release src/minimal.c
/usr/bin/ccache /usr/bin/clang -c -Qunused-arguments -m64 -fvisibility<strong>=</strong>hidden -O3 -Ibuild/.gens/minimal/linux/x86_64/release/rules/bpf -isystem /home/ruki/.xmake/packages/l/linux-tools/5.9.16/0c52e491268946fe9a4bc91d4906d66b/include -isystem /home/ruki/.xmake/packages/z/zlib/1.2.11/3a7e4427eda94fc69fad0009a1629fd8/include -isystem /home/ruki/.xmake/packages/l/libelf/0.8.13/ced4fdd8151a475dafc5f51e2a031997/include -isystem /home/ruki/.xmake/packages/l/libelf/0.8.13/ced4fdd8151a475dafc5f51e2a031997/include/libelf -isystem /home/ruki/.xmake/packages/l/libcap/2.27/c55b28aa3b3745489b93895d0d606ed1/include -isystem /home/ruki/.xmake/packages/l/linux-headers/5.9.16/8e3a440cbe1f42249aef3d89f1528ecb/include -DNDEBUG -o build/.objs/minimal/linux/x86_64/release/src/minimal.c.o src/minimal.c
<strong>[</strong> 60%]: linking.release minimal
/usr/bin/clang++ -o build/linux/x86_64/release/minimal build/.objs/minimal/linux/x86_64/release/src/minimal.c.o -m64 -L/home/ruki/.xmake/packages/l/linux-tools/5.9.16/0c52e491268946fe9a4bc91d4906d66b/lib64 -L/home/ruki/.xmake/packages/z/zlib/1.2.11/3a7e4427eda94fc69fad0009a1629fd8/lib -L/home/ruki/.xmake/packages/l/libelf/0.8.13/ced4fdd8151a475dafc5f51e2a031997/lib -L/home/ruki/.xmake/packages/l/libcap/2.27/c55b28aa3b3745489b93895d0d606ed1/lib -s -lbpf -lz -lelf -lcap
<strong>[</strong>100%]: build ok!
</code></pre> 
</div> 
<h4 style="text-align:start">编译 Android bpf 程序</h4> 
<p style="text-align:start">如果编译 Android 版本，我们也只需要切换到 android 平台即可，一样很方便</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#8f5902">$ </span>xmake f -p android
<span style="color:#8f5902">$ </span>xmake
</code></pre> 
</div> 
<p style="text-align:start">xmake 会去自动下来 ndk 工具链和对应 android 版本 libbpf 等库来使用。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#8f5902">$ </span>xmake f -p android -c
checking <span style="color:blue">for </span>architecture ... armeabi-v7a
checking <span style="color:blue">for </span>Android SDK directory ... no
checking <span style="color:blue">for </span>NDK directory ... no
note: try installing these packages <strong>(</strong>pass -y to skip confirm<strong>)</strong>?
<span style="color:blue">in </span><span style="color:black">local</span>-repo:
  -> libcap 2.27 <strong>[</strong>linux, x86_64, from:linux-tools]
  -> libelf 0.8.13 <strong>[</strong>linux, x86_64, from:linux-tools]
  -> zlib 1.2.11 <strong>[</strong>linux, x86_64, from:linux-tools]
  -> linux-tools 5.9.16 <strong>[</strong>bpftool:y]
  -> ndk 22.0
  -> libelf#1 0.8.13 <strong>[</strong>toolchains:@ndk, from:libbpf]
  -> zlib#1 1.2.11 <strong>[</strong>toolchains:@ndk, from:libbpf]
  -> libbpf v0.3 <strong>[</strong>toolchains:@ndk]
please input: y <strong>(</strong>y/n<strong>)</strong>

  <strong>=</strong>> install libcap 2.27 .. ok
  <strong>=</strong>> install zlib 1.2.11 .. ok
  <strong>=</strong>> install libelf 0.8.13 .. ok
  <strong>=</strong>> install ndk 22.0 .. ok
  <strong>=</strong>> install linux-tools 5.9.16 .. ok
  <strong>=</strong>> install libelf#1 0.8.13 .. ok
  <strong>=</strong>> install zlib#1 1.2.11 .. ok
  <strong>=</strong>> install libbpf v0.3 .. ok
<span style="color:#8f5902">ruki@010689392c4d:/mnt/bpf_minimal$ </span>xmake
<strong>[</strong> 20%]: compiling.bpf src/minimal.bpf.c
<strong>[</strong> 40%]: ccache compiling.release src/minimal.c
<strong>[</strong> 60%]: linking.release minimal
<strong>[</strong>100%]: build ok!
</code></pre> 
</div> 
<p style="text-align:start">当然，如果你已经手动下载了对应版本的 ndk 工具链，我们也可以指定使用，不再走自动拉取。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#8f5902">$ </span>xmake f -p android --ndk<strong>=</strong>/xxx/android-ndk-r22
<span style="color:#8f5902">$ </span>xmake
</code></pre> 
</div> 
<p style="text-align:start">不过，如果自己下载的话，记得至少要下载 ndk r22 以上版本的，因为低版本 ndk 里面的 clang 不支持编译生成 bpf 程序。</p> 
<p style="text-align:start">最后，这里有个完整的基于 xmake 的 bpf 脚手架工程，大家可以参考下：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhack0z%2Flibbpf-bootstrap" target="_blank">https://github.com/hack0z/libbpf-bootstrap</a></p> 
<p style="text-align:start">另外这里也有个最小 bpf 例子程序：https://github.com/xmake-io/xmake/tree/master/tests/projects/bpf/minimal</p> 
<h3 style="text-align:start">集成使用 Conda 包</h3> 
<p style="text-align:start">Conda 是一个很强大的第三方包管理器，支持各种语言的二进制包拉取，这里我们仅仅使用里面的 C/C++ 包。</p> 
<p style="text-align:start">它的集成使用方式跟 conan/vcpkg 类似，仅仅只是包命名空间改成了 <code>conda::</code></p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"conda::libpng 1.6.37"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">alias</span> <strong>=</strong> <span style="color:#ff00ff">"libpng"</span><strong>&#125;)</strong>
<span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"conda::openssl"</span><strong>)</strong>
<span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"testco"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.cpp"</span><strong>)</strong>
    <span style="color:#000000">add_packages</span><strong>(</strong><span style="color:#ff00ff">"libpng"</span><strong>,</strong> <span style="color:#ff00ff">"conda::openssl"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">注：虽然我们支持很多的第三方包管理器，比如 conan/conda/vcpkg/brew 等等，但是 xmake 也有自建的包仓库管理，目前已有将近 300 个常用包，支持不同的平台，其中部分包还支持 android/ios/mingw 甚至交叉编译环境。</p> 
<p style="text-align:start">因此，如果官方 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake-repo" target="_blank">xmake-repo</a> 仓库已经提供了需要的包，可以直接使用，不需要指定包命名空间。xmake 对第三方包管理的支持仅仅是作为补充，尽可能复用已有 c/c++ 生态，避免生态碎片化。</p> 
<h3 style="text-align:start">获取主机 cpu 信息</h3> 
<p style="text-align:start">当前版本，我们新增了一个 <code>core.base.cpu</code> 模块和 <code>os.cpuinfo</code> 接口，用于获取 cpu 的各种信息，比如：cpu family/model, microarchitecture，core number, features 等信息。</p> 
<p style="text-align:start">这通常在追求性能的项目中非常有用，这些项目通常需要根据CPU的内存模型和扩展指令集来优化，同时想要跨平台的话，就需要根据当前cpu信息指定对应的代码，（例如intel haswell之后一套，amd zen之后一套，更老的默认到没有优化）。很多高性能计算库里面也会用到这些信息。</p> 
<p style="text-align:start">因此，通过这个模块接口就可以在编译配置的时候获取当前主机 cpu 的信息和特性支持力度，来针对性开启相关优化编译。</p> 
<p style="text-align:start">我们可以通过 <code>os.cpuinfo()</code> 快速获取所有信息，也可以指定 <code>os.cpuinfo("march")</code> 获取特定信息，比如 march，也就是 microarchitecture</p> 
<p style="text-align:start">我们也可以通过 <code>xmake l</code> 命令来快速查看获取结果。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#8f5902">$ </span>xmake l os.cpuinfo
<strong>&#123;</strong>
  features <strong>=</strong> <span style="color:#ff00ff">"fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clfsh ds acpi mmx fxsr sse sse2 ss htt tm pbe sse3 pclmulqdq dtes64 mon dscpl vmx est tm2 ssse3 fma cx16 tpr pdcm
sse4_1 sse4_2 x2apic movbe popcnt aes pcid xsave osxsave seglim64 tsctmr avx1_0 rdrand f16c"</span>,
  vendor <strong>=</strong> <span style="color:#ff00ff">"GenuineIntel"</span>,
  model_name <strong>=</strong> <span style="color:#ff00ff">"Intel(R) Core(TM) i7-8569U CPU @ 2.80GHz"</span>,
  family <strong>=</strong> 6,
  march <strong>=</strong> <span style="color:#ff00ff">"Kaby Lake"</span>,
  model <strong>=</strong> 142,
  ncpu <strong>=</strong> 8
<strong>&#125;</strong>

<span style="color:#8f5902">$ </span>xmake l os.cpuinfo march
<span style="color:#ff00ff">"Kaby Lake"</span>

<span style="color:#8f5902">$ </span>xmake l os.cpuinfo ncpu
8
</code></pre> 
</div> 
<p style="text-align:start">如果要判断 sse 等扩展特性支持，就得需要 import 导入 <code>core.base.cpu</code> 模块来获取了。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.c"</span><strong>)</strong>
    <span style="color:#000000">on_load</span><strong>(</strong><span style="color:blue">function</span> <strong>(</strong><span style="color:#000000">target</span><strong>)</strong>
        <span style="color:#000000">import</span><strong>(</strong><span style="color:#ff00ff">"core.base.cpu"</span><strong>)</strong>
        <span style="color:blue">local</span> <span style="color:#000000">ncpu</span> <strong>=</strong> <span style="color:#000000">os</span><strong>.</strong><span style="color:#000000">cpuinfo</span><strong>(</strong><span style="color:#ff00ff">"ncpu"</span><strong>)</strong>
        <em>-- local ncpu = cpu.number()</em>
        <span style="color:blue">if</span> <span style="color:#000000">cpu</span><strong>.</strong><span style="color:#000000">has_feature</span><strong>(</strong><span style="color:#ff00ff">"sse"</span><strong>)</strong> <span style="color:blue">then</span>
            <span style="color:#000000">target</span><strong>:</strong><span style="color:#000000">add</span><strong>(</strong><span style="color:#ff00ff">"defines"</span><strong>,</strong> <span style="color:#ff00ff">"HAS_SSE"</span><strong>)</strong>
        <span style="color:blue">end</span>
    <span style="color:blue">end</span><strong>)</strong>
</code></pre> 
</div> 
<h3 style="text-align:start">新增 cmake 导入文件规则</h3> 
<p style="text-align:start">如果，我们开发的是库程序，在执行 <code>xmake install</code> 安装到系统后，仅仅只安装了库文件，没有 .cmake/.pc 等导入文件信息，因此 cmake 工程想通过 find_package 集成使用，通常是找不到我们的库。</p> 
<p style="text-align:start">为了能够让第三方 cmake 工程正常找到它并使用集成，那么我们可以使用 <code>utils.install.cmake_importfiles</code> 规则在安装 target 目标库文件的时候，导出 .cmake 文件，用于其他 cmake 项目的库导入和查找。</p> 
<p style="text-align:start">我们只需要通过 add_rules 接口应用此规则到指定的 target 库目标即可。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.c"</span><strong>)</strong>
    <span style="color:#000000">add_rules</span><strong>(</strong><span style="color:#ff00ff">"utils.install.cmake_importfiles"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">配置之后，<code>xmake install</code> 安装命令就能够自动导出 .cmake 导入文件。</p> 
<h3 style="text-align:start">新增 pkgconfig 导入文件规则</h3> 
<p style="text-align:start">跟上面的 cmake 导入类似，只不过我们这也可以通过 <code>utils.install.pkgconfig_importfiles</code> 规则安装 pkgconfig/.pc 导入文件，这对 autotools 等工具的库探测非常有用。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.c"</span><strong>)</strong>
    <span style="color:#000000">add_rules</span><strong>(</strong><span style="color:#ff00ff">"utils.install.pkgconfig_importfiles"</span><strong>)</strong>
</code></pre> 
</div> 
<h3 style="text-align:start">新增 Git 相关内置配置变量</h3> 
<p style="text-align:start">xmake 一直有提供 config.h 的自动生成特性，可以通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fmanual%2Fproject_target%3Fid%3Dtargetadd_configfiles" target="_blank">add_configfiles</a> 接口来配置，并且它还支持模板变量的替换，用户可以自己定义一些变量。</p> 
<p style="text-align:start">不过，xmake 也提供了一些常用的内置变量替换，比如 版本信息，平台架构等。具体详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fmanual%2Fproject_target%3Fid%3Dtargetadd_configfiles" target="_blank">https://xmake.io/#/manual/project_target?id=targetadd_configfiles</a></p> 
<p style="text-align:start">模板配置使用方式很简单，只需要：</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.c"</span><strong>)</strong>
    <span style="color:#000000">add_configfiles</span><strong>(</strong><span style="color:#ff00ff">"src/config.h.in"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">就能根据 config.h.in 自动生成 config.h 文件。</p> 
<p style="text-align:start">不过我们这里要讲的新特性是最近新提供的 Git 相关内置变量，来让用户在项目编译时候，快速方便的或者当前 git 项目最近的 tag/branch/commit 信息。</p> 
<p style="text-align:start">这对于后期排查定位问题非常有用，我们可以通过 commit 精确定位问题库是基于哪次 commit 提交导致的，这样，我们就能 checkout 但对应版本来排查问题。</p> 
<p style="text-align:start">我们只需要在 config.h.in 中配置定义以下变量。</p> 
<div style="text-align:start"> 
 <pre><code><em>#define GIT_COMMIT      "$&#123;GIT_COMMIT&#125;"
#define GIT_COMMIT_LONG "$&#123;GIT_COMMIT_LONG&#125;"
#define GIT_COMMIT_DATE "$&#123;GIT_COMMIT_DATE&#125;"
#define GIT_BRANCH      "$&#123;GIT_BRANCH&#125;"
#define GIT_TAG         "$&#123;GIT_TAG&#125;"
#define GIT_TAG_LONG    "$&#123;GIT_TAG_LONG&#125;"
#define GIT_CUSTOM      "$&#123;GIT_TAG&#125;-$&#123;GIT_COMMIT&#125;"
</em></code></pre> 
</div> 
<p style="text-align:start">执行 xmake 编译，就会自动生成如下 config.h 文件。</p> 
<div style="text-align:start"> 
 <pre><code><em>#define GIT_COMMIT      "8c42b2c2"
#define GIT_COMMIT_LONG "8c42b2c251793861eb85ffdf7e7c2307b129c7ae"
#define GIT_COMMIT_DATE "20210121225744"
#define GIT_BRANCH      "dev"
#define GIT_TAG         "v1.6.6"
#define GIT_TAG_LONG    "v1.6.6-0-g8c42b2c2"
#define GIT_CUSTOM      "v1.6.6-8c42b2c2"
</em></code></pre> 
</div> 
<p style="text-align:start">我们就可以在程序用通过宏定义的方式使用它们。</p> 
<h3 style="text-align:start">Android NDK r22 支持和远程拉取</h3> 
<p style="text-align:start">Android NDK 从 r22 之后，结构上做了非常大的改动，移除了一些被废弃的目录，比如 顶层的 sysroot 目录 和 platforms 目录，导致 xmake 之前的探测方式失效。</p> 
<p style="text-align:start">因此在新版本中，我们对 xmake 做了改进来更好的支持全版本 NDK 工具链，包括 r22 以上的新版本。</p> 
<p style="text-align:start">同时 xmae-repo 官方仓库也增加了对 ndk 包的收录，使得 xmake 能够远程拉取 ndk 工具链来使用。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"ndk >=22.x"</span><strong>)</strong>
<span style="color:#000000">set_toolchains</span><strong>(</strong><span style="color:#ff00ff">"@ndk"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">sdkver</span> <strong>=</strong> <span style="color:#ff00ff">"23"</span><strong>&#125;)</strong>
<span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.c"</span><strong>)</strong>
</code></pre> 
</div> 
<h2 style="text-align:start">更新内容</h2> 
<h3 style="text-align:start">新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1259" target="_blank">#1259</a>: 支持 <code>add_files("*.def")</code> 添加 def 文件去导出 windows/dll 符号</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1267" target="_blank">#1267</a>: 添加 <code>find_package("nvtx")</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1274" target="_blank">#1274</a>: 添加 <code>platform.linux.bpf</code> 规则去构建 linux/bpf 程序</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1280" target="_blank">#1280</a>: 支持 fetchonly 包去扩展改进 find_package</li> 
 <li>支持自动拉取远程 ndk 工具链包和集成</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1268" target="_blank">#1268</a>: 添加 <code>utils.install.pkgconfig_importfiles</code> 规则去安装 <code>*.pc</code> 文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1268" target="_blank">#1268</a>: 添加 <code>utils.install.cmake_importfiles</code> 规则去安装 <code>*.cmake</code> 导入文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake-repo%2Fpull%2F348" target="_blank">#348</a>: 添加 <code>platform.longpaths</code> 策略去支持 git longpaths</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1314" target="_blank">#1314</a>: 支持安装使用 conda 包</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1120" target="_blank">#1120</a>: 添加 <code>core.base.cpu</code> 模块并且改进 <code>os.cpuinfo()</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1325" target="_blank">#1325</a>: 为 <code>add_configfiles</code> 添加内建的 git 变量</li> 
</ul> 
<h3 style="text-align:start">改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1275" target="_blank">#1275</a>: 改进 vsxmake 生成器，支持条件化编译 targets</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F1290" target="_blank">#1290</a>: 增加对 Android ndk r22 以上版本支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1311" target="_blank">#1311</a>: 为 vsxmake 工程添加包 dll 路径，确保调试运行加载正常</li> 
</ul> 
<h3 style="text-align:start">Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1266" target="_blank">#1266</a>: 修复在 <code>add_repositories</code> 中的 repo 相对路径</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1288" target="_blank">#1288</a>: 修复 vsxmake 插件处理 option 配置问题</li> 
</ul>
                                        </div>
                                      
</div>
            