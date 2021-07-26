
---
title: 'Ghidra 10.0 发布，NSA 的软件逆向工程框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1823'
author: 开源中国
comments: false
date: Mon, 26 Jul 2021 07:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1823'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ghidra 是由美国国家安全局 (NSA, National Security Agency) 的研究理事会为 NSA 的网络安全任务开发的软件逆向工程 (SRE) 框架，此框架包括一套功能齐全的高级软件分析工具，使用户能够在包括 Windows、MacOS 和 Linux 在内的各种平台上分析编译后的代码，功能包括反汇编、汇编、反编译、绘图和脚本编写，以及数百种其他功能。</p> 
<p>Ghidra 支持多种处理器指令集和可执行格式，并且可以在用户交互和自动化模式下运行。用户还可以使用公开的 API 开发自己的 Ghidra 插件组件（或脚本）。它有助于分析恶意代码和病毒等恶意软件，并可以让网络安全专业人员更好地了解其网络和系统中的潜在漏洞。</p> 
<p>Ghidra 10.0 的 release note<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhtmlpreview.github.io%2F%3Fhttps%3A%2F%2Fgithub.com%2FNationalSecurityAgency%2Fghidra%2Fblob%2FGhidra_10.0_build%2FGhidra%2FConfigurations%2FPublic_Release%2Fsrc%2Fglobal%2Fdocs%2FWhatsNew.html" target="_blank"> 写道</a>，此版本完全向后兼容以前版本的项目数据。但在 10.0 中创建或修改的程序和数据类型存档将无法用于较早的 Ghidra 版本。另外，Ghidra 10.0 带来了许多新特性和功能、性能改进，以及 Bugfix 等。</p> 
<h3>Ghidra 10.0 主要变化</h3> 
<h4>正式推出新调试器</h4> 
<p>其主要用于 Linux 和 Windows 上的用户模式应用程序调试，调试器新功能：</p> 
<ul> 
 <li>提供跟踪数据的 API</li> 
 <li>提供平台调试器模型 API</li> 
 <li>提供执行 SLEIGH / p-code 的 API</li> 
 <li>平台调试器支持其他模式，包括内核模式和远程调试</li> 
 <li>支持在 Windows 上连接到 WinDbg 预览版</li> 
 <li>支持通过 GDB 跟踪以下架构：arm、m68k、mips、powerpc</li> 
 <li>支持通过 JDI 跟踪以下架构：Java、Dalvik</li> 
</ul> 
<h4><span style="color:null"><span style="background-color:null">用户定义的编译器规范扩展</span></span></h4> 
<p>Ghidra 10.0 为分配给特定程序的<strong>编译器规范</strong>添加了对用户定义扩展的支持。特别是，用户现在可以定义自己的：</p> 
<ul> 
 <li><strong>调用约定</strong>- 告知分析和反编译参数如何在函数之间传递</li> 
 <li><strong>Call-Fixups</strong> - 在分析生成它们的函数时用行为代替特定的 CALL</li> 
 <li><strong>Callother-Fixups</strong> - 在分析包含它们的函数时用行为代替某些指令</li> 
</ul> 
<h3>从 RTTI 恢复原型类</h3> 
<p>管理和应用 PDB 文件具有重大改进的 GUI，包括对多个符号服务器位置的支持。</p> 
<h3>可保存的分析选项配置</h3> 
<p>分析选项配置可以按名称保存，并使用分析配置菜单中的新功能进行快速更改。即使在退出 Ghidra 之后，下次分析程序时，最后使用的命名配置也将用作默认选项。如果分析器提供的结果不佳，或者将使用的二进制类型不需要分析，这对于禁用一个或多个选项（例如堆栈分析）很有用。例如，默认情况下，应在第一次通过时为所有可疑恶意软件二进制文件关闭某些分析选项，以避免某些类型的混淆问题。</p> 
<h3>Bugfix 和功能增强</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhtmlpreview.github.io%2F%3Fhttps%3A%2F%2Fraw.githubusercontent.com%2FNationalSecurityAgency%2Fghidra%2FGhidra_10.0_build%2FGhidra%2FConfigurations%2FPublic_Release%2Fsrc%2Fglobal%2Fdocs%2FChangeHistory.html" target="_blank">ChangeHistory</a> 文件完整列出了许多其他错误修复和改进。</p> 
<p>更多内容查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhtmlpreview.github.io%2F%3Fhttps%3A%2F%2Fgithub.com%2FNationalSecurityAgency%2Fghidra%2Fblob%2FGhidra_10.0_build%2FGhidra%2FConfigurations%2FPublic_Release%2Fsrc%2Fglobal%2Fdocs%2FWhatsNew.html" target="_blank"> release note</a>。</p>
                                        </div>
                                      
</div>
            