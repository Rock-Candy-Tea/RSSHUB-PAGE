
---
title: 'xmake v2.6.2 发布，新增 Linux 内核驱动模块构建支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://tboox.org/static/img/xmake/xmake-cmake.jpeg'
author: 开源中国
comments: false
date: Sat, 18 Dec 2021 11:53:00 GMT
thumbnail: 'https://tboox.org/static/img/xmake/xmake-cmake.jpeg'
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
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img src="https://tboox.org/static/img/xmake/xmake-cmake.jpeg" width="30%" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">新版本改动</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这个版本主要新增两大特性：</p> 
<ol> 
 <li>Linux 内核驱动模块的构建支持</li> 
 <li>分组构建和批量运行支持，可用于实现<span> </span><code>Run all tests</code><span> </span>功能</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">剩下的主要是一些零散的功能改进和 Bugs 修复，可以看下文末的更新内容明细，一些比较大的改动，下面也会逐一说明。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">新特性介绍</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start">构建 Linux 内核驱动模块</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">Xmake 也许是首个提供 Linux 内核驱动开发 内置支持的第三方构建工具了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">尽管网上也有介绍 CMake 如何去配置构建 linux 驱动，但是大都是通过<span> </span><code>add_custom_command</code><span> </span>方式自定义各种命令，然后执行<span> </span><code>echo</code><span> </span>去自己拼接生成 Linux 的 Makefile 文件。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">也就是说，其实还是依赖 Linux 内核源码的 Makefile 来执行的构建，因此如果想自己追加一些编译配置和宏定义都会非常麻烦。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">而使用 Xmake，我们可以提供更加灵活的可配置性，更加简单的配置文件，以及一键编译、自动依赖拉取集成、Linux kernel 源码自动下载集成，内核驱动交叉编译等特性。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">Hello World</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们通过一个最简单的字符驱动来直观感受下。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">首先，我们准备一个 Hello World 驱动代码，例如：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"linux-headers"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">driver_modules</span> <strong style="color:black">=</strong> <strong style="color:#800080">true</strong><strong style="color:#000000">&#125;&#125;)</strong>

<span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"hello"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_rules</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"platform.linux.driver"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/*.c"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_packages</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"linux-headers"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_license</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"GPL-2.0"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">它的配置非常简单，只需要配置上支持模块的 linux-headers 包，然后应用<span> </span><code>platform.linux.driver</code><span> </span>构建规则就行了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">然后直接执行 xmake 命令，一键编译，生成内核驱动模块 hello.ko。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span>
</span>[ 20%]: ccache compiling.release src/add.c
[ 20%]: ccache compiling.release src/hello.c
[ 60%]: linking.release build/linux/x86_64/release/hello.ko
[100%]: build ok!
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">简单么，也许你会说，这跟直接用 Makefile 配置，然后 make 编译也没啥太大区别么。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">那么重点来了，Xmake 是会自动帮你拉取指定版本依赖内核源码，make 不会，CMake 也不会，用户必须通过<span> </span><code>sudo apt install linux-headers-generic</code><span> </span>自己安装它们。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">但是 Xmake 不需要，上面的一键编译，我其实省略了部分输出，实际上是这样的。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span>
</span>note: install or modify (m) these packages (pass -y to skip confirm)?
in xmake-repo:
  -> m4 1.4.19 [from:linux-headers,bison,flex,elfutils]
  -> flex 2.6.4 [from:bc,linux-headers]
  -> bison 3.8.2 [from:bc,linux-headers]
  -> ed 1.17 [from:bc,linux-headers]
  -> texinfo 6.7 [from:bc,linux-headers]
  -> bc 1.07.1 [from:linux-headers]
  -> pkg-config 0.29.2 [from:linux-headers]
  -> openssl 1.1.1l [private, from:linux-headers]
  -> elfutils 0.183 [private, from:linux-headers]
  -> linux-headers 5.10.46 [driver_modules:y]
please input: y (y/n/m)

  => download https://github.com/xmake-mirror/ed/archive/refs/tags/1.17.tar.gz .. ok
  => install ed 1.17 .. ok
  => download https://ftp.gnu.org/gnu/m4/m4-1.4.19.tar.xz .. ok
  => download https://ftp.gnu.org/gnu/texinfo/texinfo-6.7.tar.xz .. ok
  => download https://pkgconfig.freedesktop.org/releases/pkg-config-0.29.2.tar.gz .. ok
  => download https://github.com/openssl/openssl/archive/OpenSSL_1_1_1l.zip .. ok
  => install m4 1.4.19 .. ok
  => download https://github.com/westes/flex/releases/download/v2.6.4/flex-2.6.4.tar.gz .. ok
  => install texinfo 6.7 .. ok
  => install pkg-config 0.29.2 .. ok
  => download http://ftp.gnu.org/gnu/bison/bison-3.8.2.tar.gz .. ok
  => install flex 2.6.4 .. ok
  => download https://sourceware.org/elfutils/ftp/0.183/elfutils-0.183.tar.bz2 .. ok
  => install elfutils 0.183 .. ok
  => install bison 3.8.2 .. ok
  => download https://ftp.gnu.org/gnu/bc/bc-1.07.1.tar.gz .. ok
  => install bc 1.07.1 .. ok
  => install openssl 1.1.1l .. ok
  => download https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.10.46.tar.xz .. ok
  => install linux-headers 5.10.46 .. ok
[ 16%]: ccache compiling.release src/add.c
[ 16%]: ccache compiling.release src/hello.c
[ 16%]: ccache compiling.release src/hello.mod.c
[ 66%]: linking.release build/linux/x86_64/release/hello.ko
[100%]: build ok!
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">首次编译，Xmake 会拉取所有依赖，如果用户自己已经通过 apt 等第三方包管理安装了它们，Xmake 也会优先用系统已经安装的版本，省去下载安装过程。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">也就是说，不管在哪个环境，用户都不需要关心如何去搭建内核驱动开发环境，仅仅只需要一个<span> </span><code>xmake</code><span> </span>命令，就能搞定一切。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">而这些依赖拉取，都是通过<span> </span><code>add_requires("linux-headers", &#123;configs = &#123;driver_modules = true&#125;&#125;)</code><span> </span>配置包来实现的。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，我们也可以看完整构建命令参数。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> -v
</span>[ 20%]: ccache compiling.release src/add.c
/usr/bin/ccache /usr/bin/gcc -c -m64 -O2 -std=gnu89 -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include/generated -I/usr/src/linux-headers-5.11.0-41-generic/include -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include/uapi -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include/generated/uapi -I/usr/src/linux-headers-5.11.0-41-generic/include/uapi -I/usr/src/linux-headers-5.11.0-41-generic/include/generated/uapi -D__KERNEL__ -DMODULE -DKBUILD_MODNAME=\"hello\" -DCONFIG_X86_X32_ABI -isystem /usr/lib/gcc/x86_64-linux-gnu/10/include -include /usr/src/linux-headers-5.11.0-41-generic/include/linux/kconfig.h -include /usr/src/linux-headers-5.11.0-41-generic/include/linux/compiler_types.h -nostdinc -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-80387 -mno-fp-ret-in-387 -mpreferred-stack-boundary=3 -mskip-rax-setup -mtune=generic -mno-red-zone -mcmodel=kernel -mindirect-branch=thunk-extern -mindirect-branch-register -mrecord-mcount -fmacro-prefix-map=./= -fno-strict-aliasing -fno-common -fshort-wchar -fno-PIE -fcf-protection=none -falign-jumps=1 -falign-loops=1 -fno-asynchronous-unwind-tables -fno-jump-tables -fno-delete-null-pointer-checks -fno-allow-store-data-races -fno-reorder-blocks -fno-ipa-cp-clone -fno-partial-inlining -fstack-protector-strong -fno-inline-functions-called-once -falign-functions=32 -fno-strict-overflow -fno-stack-check -fconserve-stack -DKBUILD_BASENAME=\"add\" -o build/.objs/hello/linux/x86_64/release/src/add.c.o src/add.c
[ 20%]: ccache compiling.release src/hello.c
/usr/bin/ccache /usr/bin/gcc -c -m64 -O2 -std=gnu89 -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include/generated -I/usr/src/linux-headers-5.11.0-41-generic/include -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include/uapi -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include/generated/uapi -I/usr/src/linux-headers-5.11.0-41-generic/include/uapi -I/usr/src/linux-headers-5.11.0-41-generic/include/generated/uapi -D__KERNEL__ -DMODULE -DKBUILD_MODNAME=\"hello\" -DCONFIG_X86_X32_ABI -isystem /usr/lib/gcc/x86_64-linux-gnu/10/include -include /usr/src/linux-headers-5.11.0-41-generic/include/linux/kconfig.h -include /usr/src/linux-headers-5.11.0-41-generic/include/linux/compiler_types.h -nostdinc -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-80387 -mno-fp-ret-in-387 -mpreferred-stack-boundary=3 -mskip-rax-setup -mtune=generic -mno-red-zone -mcmodel=kernel -mindirect-branch=thunk-extern -mindirect-branch-register -mrecord-mcount -fmacro-prefix-map=./= -fno-strict-aliasing -fno-common -fshort-wchar -fno-PIE -fcf-protection=none -falign-jumps=1 -falign-loops=1 -fno-asynchronous-unwind-tables -fno-jump-tables -fno-delete-null-pointer-checks -fno-allow-store-data-races -fno-reorder-blocks -fno-ipa-cp-clone -fno-partial-inlining -fstack-protector-strong -fno-inline-functions-called-once -falign-functions=32 -fno-strict-overflow -fno-stack-check -fconserve-stack -DKBUILD_BASENAME=\"hello\" -o build/.objs/hello/linux/x86_64/release/src/hello.c.o src/hello.c
[ 60%]: linking.release build/linux/x86_64/release/hello.ko
/usr/bin/ld -m elf_x86_64 -r -o build/.objs/hello/linux/x86_64/release/build/linux/x86_64/release/hello.ko.o build/.objs/hello/linux/x86_64/release/src/add.c.o build/.objs/hello/linux/x86_64/release/src/hello.c.o
/usr/src/linux-headers-5.11.0-41-generic/scripts/mod/modpost -m -a -o build/.objs/hello/linux/x86_64/release/build/linux/x86_64/release/Module.symvers -e -N -T -
WARNING: modpost: Symbol info of vmlinux is missing. Unresolved symbol check will be entirely skipped.
/usr/bin/ccache /usr/bin/gcc -c -m64 -O2 -std=gnu89 -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include/generated -I/usr/src/linux-headers-5.11.0-41-generic/include -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include/uapi -I/usr/src/linux-headers-5.11.0-41-generic/arch/x86/include/generated/uapi -I/usr/src/linux-headers-5.11.0-41-generic/include/uapi -I/usr/src/linux-headers-5.11.0-41-generic/include/generated/uapi -D__KERNEL__ -DMODULE -DKBUILD_MODNAME=\"hello\" -DCONFIG_X86_X32_ABI -isystem /usr/lib/gcc/x86_64-linux-gnu/10/include -include /usr/src/linux-headers-5.11.0-41-generic/include/linux/kconfig.h -include /usr/src/linux-headers-5.11.0-41-generic/include/linux/compiler_types.h -nostdinc -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-80387 -mno-fp-ret-in-387 -mpreferred-stack-boundary=3 -mskip-rax-setup -mtune=generic -mno-red-zone -mcmodel=kernel -mindirect-branch=thunk-extern -mindirect-branch-register -mrecord-mcount -fmacro-prefix-map=./= -fno-strict-aliasing -fno-common -fshort-wchar -fno-PIE -fcf-protection=none -falign-jumps=1 -falign-loops=1 -fno-asynchronous-unwind-tables -fno-jump-tables -fno-delete-null-pointer-checks -fno-allow-store-data-races -fno-reorder-blocks -fno-ipa-cp-clone -fno-partial-inlining -fstack-protector-strong -fno-inline-functions-called-once -falign-functions=32 -fno-strict-overflow -fno-stack-check -fconserve-stack -o build/.objs/hello/linux/x86_64/release/build/linux/x86_64/release/hello.ko.mod.o build/.objs/hello/linux/x86_64/release/build/linux/x86_64/release/hello.ko.mod.c
/usr/bin/ld -m elf_x86_64 -r --build-id=sha1 -T /usr/src/linux-headers-5.11.0-41-generic/scripts/module.lds -o build/linux/x86_64/release/hello.ko build/.objs/hello/linux/x86_64/release/build/linux/x86_64/release/hello.ko.o build/.objs/hello/linux/x86_64/release/build/linux/x86_64/release/hello.ko.mod.o
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">使用特定版本的内核源码</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以指定版本语义规则，选取自己需要的内核源码作为构建源。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"linux-headers 5.9.x"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">driver_modules</span> <strong style="color:black">=</strong> <strong style="color:#800080">true</strong><strong style="color:#000000">&#125;&#125;)</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">交叉编译</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也支持内核驱动模块的交叉编译，比如在 Linux x86_64 上使用交叉编译工具链来构建 Linux Arm/Arm64 的驱动模块。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们只需要准备好自己的交叉编译工具链，通过<span> </span><code>--sdk=</code><span> </span>指定它的根目录，然后配置切换到<span> </span><code>-p cross</code><span> </span>平台， 最后指定需要构建的架构 arm/arm64 即可。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">同样的，我们不用关心如何准备 linux-headers 去支持交叉编译，Xmake 的依赖包管理会帮你准本好一切，拉取构建支持对应架构的内核源码。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这里用到的交叉工具链，可以从这里下载:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freleases.linaro.org%2Fcomponents%2Ftoolchain%2Fbinaries%2Flatest-7%2Faarch64-linux-gnu%2F" target="_blank">Download toolchains</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更多，交叉编译配置文档，见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fguide%2Fconfiguration%3Fid%3Dcommon-cross-compilation-configuration" target="_blank">配置交叉编译</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">注：目前仅仅支持 arm/arm64 交叉编译架构，后续会支持更多的平台架构。</p> 
<p>构建 Arm 驱动模块</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> f -p cross -a arm --sdk=/mnt/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf -c
</span><u>$ </u><span style="color:black">xmake</span><span>
</span>[ 20%]: ccache compiling.release src/add.c
[ 20%]: ccache compiling.release src/hello.c
[ 60%]: linking.release build/cross/arm/release/hello.ko
[100%]: build ok!

</code></pre> 
</div> 
<p>构建 Arm64 驱动模块</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> f -p cross -a arm64 --sdk=/mnt/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu -c
</span><u>$ </u><span style="color:black">xmake</span><span>
</span>[ 20%]: ccache compiling.release src/add.c
[ 20%]: ccache compiling.release src/hello.c
[ 60%]: linking.release build/cross/arm64/release/hello.ko
[100%]: build ok!
</code></pre> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:start">分组批量构建和运行支持</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">早期，我们已经支持了通过<span> </span><code>set_group</code><span> </span>设置目标分组，实现 vs/vsxmake 工程在 vs 下的源文件分组管理展示。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">但是，这个分组仅限于这个特性，没有用于其他地方，而新版本中，我们继续改进利用分组特性，实现指定构建一批目标程序，以及批量运行一批目标程序。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这通常有什么用呢，比如可以用来提供<span> </span><code>Run all tests</code><span> </span>和<span> </span><code>Run all benchmarks</code><span> </span>等功能。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">编译指定一批目标程序</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们可以使用<span> </span><code>set_group()</code><span> </span>将给定的目标标记为<span> </span><code>test/benchmark/...</code><span> </span>并使用<span> </span><code>set_default(false)</code><span> </span>禁用来默认构建它。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这样，默认情况下 Xmake 不会去构建它们，但是我们可以通过<span> </span><code>xmake -g xxx</code><span> </span>命令就能指定构建一批目标程序了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">比如，我们可以使用此功能来构建所有测试。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test1"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_default</span><strong style="color:#000000">(</strong><strong style="color:#800080">false</strong><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_group</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/*.cpp"</span><strong style="color:#000000">)</strong>

<span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test2"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_default</span><strong style="color:#000000">(</strong><strong style="color:#800080">false</strong><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_group</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/*.cpp"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> -g test
</span><u>$ </u><span style="color:black">xmake</span><span> --group=test
</span></code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">运行指定一批目标程序</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以通过设置分组，来指定运行所有带有<span> </span><code>test</code><span> </span>分组的测试程序。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这通常非常有用，在此之前想要实现<span> </span><code>Run all tests</code><span> </span>功能，我们只能通过定义一个<span> </span><code>task("tests")</code><span> </span>在里面调用<span> </span><code>os.exec</code><span> </span>去挨个执行测试目标，配置比较繁琐，对用户要求比较高。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">而现在，我们只需要对需要执行的测试目标程序标记为<span> </span><code>set_group("test")</code>，然后就可以批量运行它们了。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> run -g test
</span><u>$ </u><span style="color:black">xmake</span><span> run --group=test
</span></code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">支持分组模式匹配</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，我们还可以支持分组的模式匹配，非常的灵活：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code>$ xmake build -g test_*
$ xmake run -g test/foo_*
$ xmake build -g bench*
$ xmake run -g bench*
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更多信息见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1913" target="_blank">#1913</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">改进 CMake 包源的查找和集成</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">之前的版本中，我们提供了<span> </span><code>find_package("cmake::xxx")</code><span> </span>来查找 cmake 内部的包，但是这种方式对于用户集成使用还是很繁琐。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">因此，新版本中，我们进一步改进它，通过<span> </span><code>add_requires</code><span> </span>来实现统一快速的 cmake 包集成。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cmake::ZLIB"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">alias</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"zlib"</span><strong style="color:#000000">,</strong> <span style="color:#000000">system</span> <strong style="color:black">=</strong> <strong style="color:#800080">true</strong><strong style="color:#000000">&#125;)</strong>
<span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"test"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_kind</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/*.c"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_packages</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"zlib"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们指定<span> </span><code>system = true</code><span> </span>告诉 xmake 强制从系统中调用 cmake 查找包，如果找不到，不再走安装逻辑，因为 cmake 没有提供类似 vcpkg/conan 等包管理器的安装功能， 只提供了包查找特性。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">指定版本</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cmake::OpenCV 4.1.1"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">system</span> <strong style="color:black">=</strong> <strong style="color:#800080">true</strong><strong style="color:#000000">&#125;)</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">指定组件</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cmake::Boost"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">system</span> <strong style="color:black">=</strong> <strong style="color:#800080">true</strong><strong style="color:#000000">,</strong> <span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">components</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#ff00ff">"regex"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"system"</span><strong style="color:#000000">&#125;&#125;)&#125;</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">预设开关</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cmake::Boost"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">system</span> <strong style="color:black">=</strong> <strong style="color:#800080">true</strong><strong style="color:#000000">,</strong> <span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">components</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#ff00ff">"regex"</span><strong style="color:#000000">,</strong> <span style="color:#ff00ff">"system"</span><strong style="color:#000000">&#125;,</strong>
                                             <span style="color:#000000">presets</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">Boost_USE_STATIC_LIB</span> <strong style="color:black">=</strong> <strong style="color:#800080">true</strong><strong style="color:#000000">&#125;&#125;&#125;)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">相当于内部调用 find_package 查找包之前，在 CMakeLists.txt 中预定义一些配置，控制 find_package 的查找策略和状态。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code>set(Boost_USE_STATIC_LIB ON) -- will be used in FindBoost.cmake
find_package(Boost REQUIRED COMPONENTS regex system)
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">设置环境变量</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cmake::OpenCV"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">system</span> <strong style="color:black">=</strong> <strong style="color:#800080">true</strong><strong style="color:#000000">,</strong> <span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">envs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">CMAKE_PREFIX_PATH</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"xxx"</span><strong style="color:#000000">&#125;&#125;&#125;)</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">指定自定义 FindFoo.cmake 模块脚本目录</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">mydir/cmake_modules/FindFoo.cmake</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">add_requires</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"cmake::Foo"</span><strong style="color:#000000">,</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">system</span> <strong style="color:black">=</strong> <strong style="color:#800080">true</strong><strong style="color:#000000">,</strong> <span style="color:#000000">configs</span> <strong style="color:black">=</strong> <strong style="color:#000000">&#123;</strong><span style="color:#000000">moduledirs</span> <strong style="color:black">=</strong> <span style="color:#ff00ff">"mydir/cmake_modules"</span><strong style="color:#000000">&#125;&#125;)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">相关 issues:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1632" target="_blank">#1632</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">xmake-idea 插件更新</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake-idea" target="_blank">xmake-idea</a><span> </span>这个插件由于个人时间和精力的关系，一直没有花时间去维护更新，而 IDEA 插件的兼容性问题有非常多，只要一段时间不用，就无法在新的 Idea/Clion 上正常使用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">最近，我花了点时间，修复了一些兼容性问题，比如 Windows 上创建工程会卡死的问题，新版本 Clion 无法安装等问题。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">目前，最新版本应该可以在全平台正常使用了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img src="https://tboox.org/static/img/xmake/xmake-idea-output_panel.png" width="50%" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">另外一些值得提起的事情</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start">年终总结</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这是 2021 年我发布的最后一个版本，这一年下来，经历了很多，Xmake 也在逐渐成长为一个更加强大的构建工具。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">到今年年底，Xmake 总共收获了 4.2k stars，处理了 1.9k 的 issues/pr，超过 8k 多次 commits。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img src="https://tboox.org/static/img/xmake/xmake-star-history.png" width="50%" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">而官方的包管理仓库<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake-repo" target="_blank">xmake-repo</a><span> </span>也已经收录了近 500+ 的常用依赖包。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">感谢</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">感谢各位贡献者对 xmake-repo 仓库 和 Xmake 的贡献，完整贡献者列表见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fgraphs%2Fcontributors" target="_blank">Contributors</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">也非常感谢大家对 Xmake 的赞助的支持，使得我能够有足够的动力去持续维护，完整捐助列表见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fsponsor" target="_blank">Sponsors</a>。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">更新内容</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start">新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1902" target="_blank">#1902</a>: 支持构建 linux 内核驱动模块</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1913" target="_blank">#1913</a>: 通过 group 模式匹配，指定构建和运行一批目标程序</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1872" target="_blank">#1872</a>: 支持转义 set_configvar 中字符串值</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1888" target="_blank">#1888</a>: 改进 windows 安装器，避免错误删除其他安装目录下的文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1895" target="_blank">#1895</a>: 改进<span> </span><code>plugin.vsxmake.autoupdate</code><span> </span>规则</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1893" target="_blank">#1893</a>: 改进探测 icc 和 ifort 工具链</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F1905" target="_blank">#1905</a>: 改进 msvc 对 external 头文件搜索探测支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F1904" target="_blank">#1904</a>: 改进 vs201x 工程生成器</li> 
 <li>添加<span> </span><code>XMAKE_THEME</code><span> </span>环境变量去切换主题配置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1907" target="_blank">#1907</a>: 添加<span> </span><code>-f/--force</code><span> </span>参数使得<span> </span><code>xmake create</code><span> </span>可以在费控目录被强制创建</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F1917" target="_blank">#1917</a>: 改进 find_package 和配置</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1885" target="_blank">#1885</a>: 修复 package:fetch_linkdeps 链接顺序问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1903" target="_blank">#1903</a>: 修复包链接顺序</li> 
</ul>
                                        </div>
                                      
</div>
            