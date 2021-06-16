
---
title: '深入了解iOS中的Bitcode功能'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9516ece6ffb442fb5ca75d24ea762c7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 30 May 2021 18:17:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9516ece6ffb442fb5ca75d24ea762c7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>苹果在WWDC 2015大会上引入了bitcode，随后在Xcode7中添加了在二进制中嵌入bitcode(Enable Bitcode)的功能，并且默认设置为开启状态。很多人在引入第三方SDK时都遇到过bitcode报错，搜索一番后发现只要关闭bitcode功能就好，其实大部分开发者都不了解bitcode到底是何物。这篇文章我们就来深入分析下Bitcode。</p>
<h2 data-id="heading-1">什么是Bitcode</h2>
<p>LLVM是目前苹果采用的编译器工具链，Bitcode是LLVM编译器的中间代码的一种编码，这种中间编码能根据不同目标机器芯片平台转换为相应的汇编指令以及翻译为机器码。虽然Bitcode仅仅只是一个中间码不能在任何平台上运行，但是它可以转化为任何被支持的CPU架构，包括现在还没被发明的CPU架构。那么Bitcode是在LLVM工作的哪个阶段被生成的呢？要解答这个问题，我们需要对LLVM的工作流程有个简单的了解。</p>
<blockquote>
<p>LLVM是构架编译器(compiler)的框架系统，以C++编写而成，用于优化以任意程序语言编写的程序的编译时间(compile-time)、链接时间(link-time)、运行时间(run-time)以及空闲时间(idle-time)，对开发者保持开放，并兼容已有脚本。</p>
</blockquote>
<p>LLVM计划启动于2000年，最初由美国UIUC大学的Chris Lattner博士主持开展。2006年Chris Lattner加盟Apple Inc.并致力于LLVM在Apple开发体系中的应用。Apple也是LLVM计划的主要资助者。
目前LLVM已经被Apple、Microsoft、Google、Facebook等各大公司采用。(本段摘自百度百科)</p>
<p>想要对LLVM有个比较清楚的了解看<a href="https://zhuanlan.zhihu.com/p/140462815" target="_blank" rel="nofollow noopener noreferrer">这个</a>。</p>
<p>因为LLVM只是一个编译器框架，所以还需要一个前端来支撑整个系统，所以Apple又拨款拨人一起研发了Clang，作为整个编译器的前端，Clang用来编译C、C++和Objective-C。你可以将clang和lld都看做是LLVM的组成部分，框架的意思是，你可以基于LLVM提供的功能开发自己的模块，并集成在LLVM系统上，增加它的功能，或者就单纯自己开发软件工具，而利用LLVM来支撑底层实现。LLVM由一些库和工具组成，正因为它的这种设计思想，使它可以很容易和IDE集成（因为IDE软件可以直接调用库来实现一些如静态检查这些功能），也很容易构建生成各种功能的工具（因为新的工具只需要调用需要的库就行）。</p>
<p>下图是Clang/LLVM的简单架构。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9516ece6ffb442fb5ca75d24ea762c7~tplv-k3u1fbpfcp-zoom-1.image" alt="LLVM架构图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>LLVM编译一个源文件的过程：预处理 -> 词法分析 -> Token -> 语法分析 -> AST -> （中间）代码生成 -> LLVM IR -> 优化 -> 生成汇编代码 -> Link -> 目标文件</p>
<p>LLVM前端可以使用不同的编译工具对代码文件做词法分析以形成抽象语法树AST，然后将分析好的代码转换成LLVM的中间表示IR（intermediate representation）；中间部分的优化器只对中间表示IR操作，通过一系列的pass对IR做优化；后端负责将优化好的IR解释成对应平台的机器码。</p>
<p>LLVM IR是LLVM的中间表示，这是LLVM中很重要的一个东西。IR有三种表示，一种是可读的IR，类似于汇编代码，但其实它介于高等语言和汇编之间，这种表示就是给人看的，磁盘文件后缀为.ll；第二种是不可读的二进制IR，被称作位码（bitcode），磁盘文件后缀为.bc；第三种表示是一种内存格式，只保存在内存中，所以谈不上文件格式和文件后缀，这种格式是LLVM之所以编译快的一个原因，它不像gcc，每个阶段结束会生成一些中间过程文件，它编译的中间数据都是这第三种表示的IR。三种格式是完全等价的，我们可以在Clang/LLVM工具的参数中指定生成这些文件，可以通过llvm-as和llvm-dis来在前两种文件之间做转换。</p>
<p>LLVM backend就是LLVM真正的后端，也被称为LLVM核心，包括编译、汇编、链接这一套，最后生成汇编文件或者目标码。</p>
<p>看了上面有关LLVM的介绍，我们知道，Bitcode是在前端Clang处理源代码文件时生成的一个二进制表示的文件<code>.bc</code>。并且它还有另外两种表示形式，可读的介于汇编和高等语言<code>.ll</code>，以及存在内存中的IR。</p>
<h2 data-id="heading-2">Bitcode初识</h2>
<p>既然Bitcode是代码的另一种表现形式，那么他必定有自己相应的语法。我们可以通过创建简单的demo来一探究竟。</p>
<p>先创建一个最简单的c文件，保存为bc.c。代码如下：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><stdio.h></span></span>

<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-built_in">printf</span>(<span class="hljs-string">"hello world!"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后通过以下命令可以把源代码文件转换成目标文件。</p>
<pre><code class="copyable">clang -c bc.c -o bc_o.o
file bc_c.o //file命令用于辨识文件类型。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：</p>
<blockquote>
<p>bc_o.o: Mach-O 64-bit object x86_64</p>
</blockquote>
<p><code>clang -c</code> 作用是：<strong>只运行预处理,编译和汇编步骤</strong></p>
<p><code>clang -o <file></code> 作用是：<strong>输出到目标文件file</strong></p>
<p>而我们要探究的bitcode正好在<code>clang -c</code>过程中，LLVM为我们提供了输出bitcode的命令。</p>
<pre><code class="copyable">clang -emit-llvm -c bc.c -o bc.bc // 或者clang -c -emit-llvm bc.c
file bc.bc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：</p>
<blockquote>
<p>c.bc: LLVM bitcode, wrapper x86_64</p>
</blockquote>
<pre><code class="copyable">clang -c bc.bc -o bc.bc.o
file bc.bc.o
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：</p>
<blockquote>
<p>bc.bc.o: Mach-O 64-bit object x86_64</p>
</blockquote>
<p>比较下两个.o文件的区别：</p>
<pre><code class="copyable">xxd bc.bc.o > bc.bc.hex //转换为可读格式（hex文件，实际上就是用printf("%02x")将二进制文件按字节打印为可读数据）
xxd bc.o > bc.hex
diff bc.bc.hex bc.hex
// 输出为空
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由此可以确定，将bitcode文件作为clang的输入，编出的object文件跟直接编源代码是相同的。</p>
<p>接下来我们尝试着解读<code>.bc</code>这个文件，输出ASCII字符看看：</p>
<pre><code class="copyable"> hexdump -c bc.bc
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9901213ad994960a79941e4254425de~tplv-k3u1fbpfcp-zoom-1.image" alt="全是乱码" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到全是乱码，好在可以通过<code>-emit-llvm -S</code> 将源代码编译为文本格式的bitcode，叫做LLVM Assembly Language，一般后缀名使用.ll。</p>
<pre><code class="copyable">clang -emit-llvm -S bc.c -o bc.ll
file bc.ll
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：</p>
<blockquote>
<p>bc.ll: ASCII text, with very long lines</p>
</blockquote>
<p>完整的文件内容如下：</p>
<pre><code class="copyable">; ModuleID = 'bc.c'
source_filename = "bc.c"
target datalayout = "e-m:o-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-apple-macosx11.0.0"

@.str = private unnamed_addr constant [13 x i8] c"hello world!\00", align 1
; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() #0 &#123;
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([13 x i8], [13 x i8]* @.str, i64 0, i64 0))
  ret i32 0
&#125;
declare i32 @printf(i8*, ...) #1

attributes #0 = &#123; noinline nounwind optnone ssp uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "darwin-stkchk-strong-link" "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "probe-stack"="___chkstk_darwin" "stack-protector-buffer-size"="8" "target-cpu"="penryn" "target-features"="+cx16,+cx8,+fxsr,+mmx,+sahf,+sse,+sse2,+sse3,+sse4.1,+ssse3,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" &#125;
attributes #1 = &#123; "correctly-rounded-divide-sqrt-fp-math"="false" "darwin-stkchk-strong-link" "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "probe-stack"="___chkstk_darwin" "stack-protector-buffer-size"="8" "target-cpu"="penryn" "target-features"="+cx16,+cx8,+fxsr,+mmx,+sahf,+sse,+sse2,+sse3,+sse4.1,+ssse3,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" &#125;

!llvm.module.flags = !&#123;!0, !1, !2&#125;
!llvm.ident = !&#123;!3&#125;

!0 = !&#123;i32 2, !"SDK Version", [2 x i32] [i32 11, i32 0]&#125;
!1 = !&#123;i32 1, !"wchar_size", i32 4&#125;
!2 = !&#123;i32 7, !"PIC Level", i32 2&#125;
!3 = !&#123;!"Apple clang version 12.0.0 (clang-1200.0.32.27)"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有关bicode.ll文本的语法可以参考<a href="https://llvm.org/docs/LangRef.html" target="_blank" rel="nofollow noopener noreferrer">文档</a>。</p>
<h2 data-id="heading-3">Xcode的Enable Bitcode</h2>
<p>Apple对此有这么一段<a href="https://help.apple.com/xcode/mac/10.1/index.html?localePath=en.lproj#/itcaec37c2a6" target="_blank" rel="nofollow noopener noreferrer">描述</a>:</p>
<blockquote>
<p>Enable Bitcode (ENABLE_BITCODE)</p>
</blockquote>
<p>Activating this setting indicates that the target or project should generate bitcode during compilation for platforms and architectures that support it. For Archive builds, bitcode will be generated in the linked binary for submission to the App Store. For other builds, the compiler and linker will check whether the code complies with the requirements for bitcode generation, but will not generate actual bitcode.</p>
<p>翻译一下就是：</p>
<ul>
<li>激活此设置意味着目标或项目应该在编译支持它的平台和体系结构时生成位码。</li>
<li>对于Archive构建，bitcode将在链接二进制中生成，以便提交到App Store。</li>
<li>对于其他版本，编译器和链接器会检查代码是否符合生成位码的要求，但不会生成实际的位码。</li>
</ul>
<p>也就是说，当我们开启Bicode功能，将会在支持的平台和架构中生成bitcode，像现在主流的armv7，arm64。但用模拟器debug时是不会生成的，这个是Xcode做的限制，我们用命令行还是能自己生成bitcode的。</p>
<p>而生成的bitcode会被嵌入到最终Archive的二进制文件中，并随着版本发布一起提交到AppStrore。关闭这一功能则不会生成这个bitcode文件，也就不会包含在构建包时的二进制文件中。这也是一旦开启这一功能，就会发现提交的包变大了的原因。</p>
<p>当进行非Archive的build时，Enable Bitcode 将会增加编译参数 -fembed-bitcode-marker， 只是在object文件中做了标记，表明我可以有bitcode，但是现在暂时没有带上它。因为本地编译调试时并不需要bitcode，只有AppStore需要这玩意儿，去掉这个不必要的步骤，会加快编译速度。</p>
<p>当然，你可以将 Enable Bitcode 设置为NO， 然后在 <strong>Other Compiler Flags</strong> 和 <strong>Other Linker Flags</strong> 中手动为真机架构添加<code>-fembed-bitcode</code> 参数，这样任何类型的Build都会带上bitcode。</p>
<blockquote>
<p><code>-fembed-bitcode-maker</code>:只是简单的标记一下在archive出来的二进制中bitcdoe所在的位置。<br></p>
</blockquote>
<p><code>-fembed-bitcode</code>: 真的会生成bitcode指令，并且嵌入到二进制中，这个设置不止要在app中设置，同样你也必须在编译静态链接库的时候使用。而且需要主题的是该参数系统只默认在archive模式下会添加</p>
<p>clang命令的<a href="https://gist.github.com/masuidrive/5231110" target="_blank" rel="nofollow noopener noreferrer">-optional</a></p>
<hr>
<p>我们来看下开启 Enable Bitcode 后的文件变异出来是怎样的。</p>
<pre><code class="copyable">clang -fembed-bitcode -c bc.c -o bc_bitcode.o
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过otool工具可以查看Object文件的结构：<a href="https://www.cnblogs.com/sonofelice/p/5571416.html" target="_blank" rel="nofollow noopener noreferrer">otool介绍</a></p>
<pre><code class="copyable">otool -l bc_bitcode.o
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出:</p>
<pre><code class="copyable">bc_bitcode.o:
Mach header
      magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
 0xfeedfacf 16777223          3  0x00           1     4        680 0x00002000
Load command 0
      cmd LC_SEGMENT_64
  cmdsize 552
  segname
   vmaddr 0x0000000000000000
   vmsize 0x0000000000000d60
  fileoff 712
 filesize 3424
  maxprot 0x00000007
 initprot 0x00000007
   nsects 6
    flags 0x0
Section
  sectname __text
   segname __TEXT
      addr 0x0000000000000000
      size 0x000000000000002a
    offset 712
     align 2^4 (16)
    reloff 4136
    nreloc 2
     flags 0x80000400
 reserved1 0
 reserved2 0
Section
  sectname __cstring
   segname __TEXT
      addr 0x000000000000002a
      size 0x000000000000000d
    offset 754
     align 2^0 (1)
    reloff 0
    nreloc 0
     flags 0x00000002
 reserved1 0
 reserved2 0
Section
  sectname __bitcode
   segname __LLVM
      addr 0x0000000000000040
      size 0x0000000000000c60
    offset 776
     align 2^4 (16)
    reloff 0
    nreloc 0
     flags 0x00000000
 reserved1 0
 reserved2 0
Section
  sectname __cmdline
   segname __LLVM
      addr 0x0000000000000ca0
      size 0x000000000000005a
    offset 3944
     align 2^4 (16)
    reloff 0
    nreloc 0
     flags 0x00000000
 reserved1 0
 reserved2 0
// 太长了，我删掉一点...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和bc.o目标文件比较会发现开启Enable Bitcode的文件多了两个Section，<code>__LLVM,__bitcode</code> 和 <code>__LLVM,__cmdline</code>。</p>
<p>Xcode 提供的 <code>segedit</code> 命令可以直接将指定的Section导出，只需要给定Section的名字接口。</p>
<pre><code class="copyable">segedit -extract __LLVM __bitcode bc_bitcode.o.bc -extract __LLVM __cmdline bc_bitcode.o.comdline bc_bitcode.o
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成<code>bc_bitcode.o.bc</code>和<code>bc_bitcode.o.comdline</code>两个文件。这个时候，我们应该有如下这些文件了(上文没提到的无需要理会)。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c16425b986e4e49a099a3e0ef12a763~tplv-k3u1fbpfcp-zoom-1.image" alt="文件列表" loading="lazy" referrerpolicy="no-referrer">
（图片背景有问题，换了一张，大家将就着看吧~）</p>
<p>注意到我们一开始导出的<code>bc.bc</code>，大小和<code>bc_bitcode.o.bc</code>一致。有点可疑，比较下两文件。</p>
<pre><code class="copyable">md5 bc.bc bc_bitcode.o.bc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出:</p>
<blockquote>
<p>MD5 (bc.bc) = 020389ec450aa7451bc105d7b010418c</p>
</blockquote>
<p>MD5 (bc_bitcode.o.bc) = c0f0a511804418e167c3a74e1d816c21</p>
<p>咦，从目标文件内导出的bitcode文件和直接编译的bitcode不一样？</p>
<p>我们试着转换下格式使<code>bc_bitcode.o.bc</code>文件变得可读。</p>
<pre><code class="copyable">clang -emit-llvm -S bc_bitcode.o.bc -o bc_bitcode.o.ll
<span class="copy-code-btn">复制代码</span></code></pre>
<p>bc_bitcode.o.ll文件内容如下：</p>
<pre><code class="copyable">; ModuleID = 'bc_bitcode.o.bc'
source_filename = "bc.c"
target datalayout = "e-m:o-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-apple-macosx11.0.0"

@.str = private unnamed_addr constant [13 x i8] c"hello world!\00", align 1
; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() #0 &#123;
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([13 x i8], [13 x i8]* @.str, i64 0, i64 0))
  ret i32 0
&#125;
declare i32 @printf(i8*, ...) #1

attributes #0 = &#123; noinline nounwind optnone ssp uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "darwin-stkchk-strong-link" "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "probe-stack"="___chkstk_darwin" "stack-protector-buffer-size"="8" "target-cpu"="penryn" "target-features"="+cx16,+cx8,+fxsr,+mmx,+sahf,+sse,+sse2,+sse3,+sse4.1,+ssse3,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" &#125;
attributes #1 = &#123; "correctly-rounded-divide-sqrt-fp-math"="false" "darwin-stkchk-strong-link" "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "probe-stack"="___chkstk_darwin" "stack-protector-buffer-size"="8" "target-cpu"="penryn" "target-features"="+cx16,+cx8,+fxsr,+mmx,+sahf,+sse,+sse2,+sse3,+sse4.1,+ssse3,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" &#125;

!llvm.module.flags = !&#123;!0, !1, !2&#125;
!llvm.ident = !&#123;!3&#125;

!0 = !&#123;i32 2, !"SDK Version", [2 x i32] [i32 11, i32 0]&#125;
!1 = !&#123;i32 1, !"wchar_size", i32 4&#125;
!2 = !&#123;i32 7, !"PIC Level", i32 2&#125;
!3 = !&#123;!"Apple clang version 12.0.0 (clang-1200.0.32.27)"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>diff bc.ll bc_bitcode.o.ll</code>比较发现，除了<code>ModuleID</code>和<code>source_filename</code>不一样外，其他内容完全一样。可见是因为这个文件还保存了和实际代码无关的文件信息，所以才会导致文件不一致，其实两文件都表示同一份代码。</p>
<p>再来回顾下，非Archive类型的build，比如直接 <code>⌘ + B</code>，即使开启了bitcode，也不会编出bitcode，那么会产生什么样的文件呢？</p>
<pre><code class="copyable">clang -fembed-bitcode-marker -c bc.c -o bc_mark.o
otool -l bc_mark.o
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：</p>
<pre><code class="copyable">bc_mark.o:
Mach header
      magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
 0xfeedfacf 16777223          3  0x00           1     4        680 0x00002000
Load command 0
      cmd LC_SEGMENT_64
  cmdsize 552
  segname
   vmaddr 0x0000000000000000
   vmsize 0x00000000000000a0
  fileoff 712
 filesize 160
  maxprot 0x00000007
 initprot 0x00000007
   nsects 6
    flags 0x0
Section
  sectname __text
   segname __TEXT
      addr 0x0000000000000000
      size 0x000000000000002a
    offset 712
     align 2^4 (16)
    reloff 872
    nreloc 2
     flags 0x80000400
 reserved1 0
 reserved2 0
Section
  sectname __cstring
   segname __TEXT
      addr 0x000000000000002a
      size 0x000000000000000d
    offset 754
     align 2^0 (1)
    reloff 0
    nreloc 0
     flags 0x00000002
 reserved1 0
 reserved2 0
Section
  sectname __bitcode
   segname __LLVM
      addr 0x0000000000000037
      size 0x0000000000000001
    offset 767
     align 2^0 (1)
    reloff 0
    nreloc 0
     flags 0x00000000
 reserved1 0
 reserved2 0
Section
  sectname __cmdline
   segname __LLVM
      addr 0x0000000000000038
      size 0x0000000000000001
    offset 768
     align 2^0 (1)
    reloff 0
    nreloc 0
     flags 0x00000000
 reserved1 0
 reserved2 0
// 还是删掉一部分...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的方式编译出的文件结构与<code>-fembed-bitcode</code> 的结果是一样的，唯一的区别就是 <code>(__LLVM,__bitcode)</code> 和 <code>(__LLVM,__cmdline)</code> 的内容并没有将实际的bitcode文件和编译参数嵌入进来，仔细看看<code>(__LLVM,__bitcode)</code>段和<code>(__LLVM,__cmdline)</code>段，发现他们的size只有1个字节(<code>0x0000000000000001</code>)。</p>
<p>这一个字节存了什么东西，我们尝试剥离这个Section段来看看：</p>
<pre><code class="copyable">segedit -extract __LLVM __bitcode bc_mark.o.bc bc_mark.o
clang -emit-llvm -S bc_mark.o.bc -o bc_mark.o.ll
cat bc_mark.o.ll
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：</p>
<pre><code class="copyable">; ModuleID = 'bc_mark.o.bc'
source_filename = "bc_mark.o.bc"
target datalayout = "e-m:o-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-apple-macosx11.0.0"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到只生成了文件名，target信息以及支持的cpu架构信息，没有任何代码相关信息。</p>
<h4 data-id="heading-4">通过bitcode编译出Object文件</h4>
<p>通过上文分析，bitcode是源代码的一种中间形式。那么，我们是否可以通过bitcode来编译出Object文件呢？理论上应该是可以的，我们动手尝试下。</p>
<p>准备好之前导出的 <strong>bc_bitcode.o.bc</strong> 和 <strong>bc_bitcode.o.comdline</strong> 。其中<strong>bc_bitcode.o.comdline</strong> 是编译bitcode到Object的必要参数。</p>
<p>先列出我们上诉所说的文件：</p>
<pre><code class="copyable">l bc_bitcode.o bc_bitcode.o.bc bc_bitcode.o.comdline
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：</p>
<blockquote>
<p>-rw-r--r--  1 zl  staff   4.2K  5 26 16:42 bc_bitcode.o</p>
</blockquote>
<p>-rw-r--r--  1 zl  staff   3.1K  5 26 17:15 bc_bitcode.o.bc<br>
-rw-r--r--  1 zl  staff    90B  5 26 17:15 bc_bitcode.o.comdline</p>
<p>这里网上都说使用<code>clang -cc1 -triple x86_64-apple-macosx10.14.0 -emit-obj -disable-llvm-passes bc_bitcode.o.bc -o bc_rebuild.o</code>命令可以编译生成Object文件，但这里有个疑点，<code>bc_bitcode.o.comdline</code>文件没用上。并且终端还会出warning！</p>
<blockquote>
<p>warning: overriding the module target triple with x86_64-apple-macosx11.0.1</p>
</blockquote>
<p>1 warning generated.</p>
<p>最终生成的bc_rebuild.o也和开启bitcode后生成的Object文件不一致。查看下部分文件。<code>l bc.o bc_bitcode.o bc_rebuild.o</code>
输出：</p>
<pre><code class="copyable">-rw-r--r--  1 zl  staff   776B  5 26 15:27 bc.o
-rw-r--r--  1 zl  staff   4.2K  5 26 16:42 bc_bitcode.o
-rw-r--r--  1 zl  staff   776B  5 28 15:21 bc_rebuild.o
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看下bc_rebuild.o，<code>otool -l bc_rebuild.o</code>，我们会发现有关bitcode的信息都被删除了，因此最终的Object文件和开启bitcode编译处的bc_bitcode.o文件大小相差这么多。</p>
<p>附：贴一下开启 Enable Bitcode 时的build和archive的编译日志对比。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/905429114b4b4c5f8a307221ed819a93~tplv-k3u1fbpfcp-zoom-1.image" alt="对比图" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">写在最后</h2>
<h4 data-id="heading-6">开启bitcode的优点:</h4>
<p>减少二进制包的大小；</p>
<blockquote>
<p>简单说，以前是把所有的arm7、arm64平台的源码编译好，然后打成一个App；而开启Bitcode之后，可以使得开发者上传App时只需上传Intermediate Representation(中间件)，而非最终的可执行二进制文件。 在用户下载App之前，AppStore会自动编译中间件，产生设备所需的执行文件供用户下载安装。以后新设计了新指令集的新CPU，可以继续从这份bitcode开始编译出新CPU上执行的可执行文件，以供用户下载安装；</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78ff0d7fb3ad400e9e39983ddca4bd3c~tplv-k3u1fbpfcp-zoom-1.image" alt="原理" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-7">参考文档</h2>
<p><a href="https://clang.llvm.org/docs/UsersManual.html" target="_blank" rel="nofollow noopener noreferrer">clang用户手册</a><br>
<a href="http://xelz.info/blog/2018/11/24/all-you-need-to-know-about-bitcode/" target="_blank" rel="nofollow noopener noreferrer">关于bitcode，知道这篇就够了</a><br>
<a href="http://www.cocoachina.com/articles/14432" target="_blank" rel="nofollow noopener noreferrer">bitcode适配指南</a><br>
<a href="https://zhuanlan.zhihu.com/p/140462815" target="_blank" rel="nofollow noopener noreferrer">LLVM基本概念入门</a></p></div>  
</div>
            