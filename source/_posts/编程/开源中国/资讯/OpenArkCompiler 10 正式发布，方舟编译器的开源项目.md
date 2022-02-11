
---
title: 'OpenArkCompiler 1.0 正式发布，方舟编译器的开源项目'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0211/072137_eZCQ_2720166.png'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 07:32:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0211/072137_eZCQ_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>OpenArkCompiler 1.0 版本已正式发布。</p> 
<p>OpenArkCompiler 是来自华为方舟编译器的开源项目，它具备的四个技术特点能够将不同语言代码编译成一套可执行文件，在运行环境中高效执行：</p> 
<ul> 
 <li>支持多语言联合优化、消除跨语言调用开销；</li> 
 <li>更轻量的语言运行时；</li> 
 <li>软硬协同充分发挥硬件能效；</li> 
 <li>支持多样化的终端设备平台</li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2022/0211/072137_eZCQ_2720166.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://gitee.com/openarkcompiler/OpenArkCompiler/releases/v1.0.0"><strong>1.0 发布说明</strong></a></p> 
<p>Maple 编译器基础设施提供 C 编译器、稳定的 aarch64 静态代码生成器以及大量优化套件。</p> 
<p><strong>前端</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#40485b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Hir2mpl 支持 .ast、.dex、.class 和 .jar 作为输入。目前，未启用 .dex、.class 和 .jar。它根据输入启用相应的编译过程。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#40485b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Hir2mpl 将 clang 生成的 .ast 文件作为输入，并将其转换为 mpl 文件。有关 mpl 文件和 MapleIR 的更多详细信息，查看 <a href="https://gitee.com/openarkcompiler/OpenArkCompiler/blob/master/doc/en/MapleIRDesign.md" target="_blank">MapleIRDesign</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><strong>中间层</strong></p> 
<ul> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Function inlining</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Constant folding</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Auto vectorization</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Loop unrolling</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">CFG simplification</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Value range propagation</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Dead store elimination</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Copy propagation</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Partial Redundancy Elimination</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Induction variable optimizations</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Code sinking</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Optimized basic block layout</li> 
</ul> 
<p><strong>后端</strong></p> 
<ul> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Copy propagation</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Target specific propagation</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Register coalescence</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Peephole optimization</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Dead code elimination</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">If conversion optimization</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Extended block optimization</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Instruction scheduling</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">Register allocation</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">CFG optimization</li> 
</ul> 
<p>最后，公告提到 <span><span><span><span><span style="color:#40485b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Maple 可以正常使用 SPEC CPU 2017，gcc.c-torture。他们使用 Clang 作为解析器和词法分析器，使用 aarch64-linux-gnu-gcc 作为汇编器和链接器。而他们</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span style="color:#40485b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>自己的解析器和词法分析器正在开发中。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><span><span><span><span><span style="color:#40485b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://gitee.com/openarkcompiler/OpenArkCompiler/releases/v1.0.0">详情查看 release note</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            