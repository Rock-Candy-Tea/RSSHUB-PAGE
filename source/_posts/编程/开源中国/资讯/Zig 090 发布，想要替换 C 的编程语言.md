
---
title: 'Zig 0.9.0 发布，想要替换 C 的编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1223/073112_LnCS_2720166.png'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 07:31:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1223/073112_LnCS_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html" target="_blank">Zig 0.9.0 已发布</a>，Zig 是一种通用的编程语言和工具链，用于维护健壮、最优和可重用的软件。</p> 
<p>此版本代表了团队近 6 个月以来的开发工作，共有 177 名不同的贡献者参与了进来，包含总计 2023 个 commit。</p> 
<p>团队用一句话总结了 0.9.0 的主要变化：“<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Toolchain" target="_blank">工具链</a>支持在更多场景中正常使用；<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Bug-Fixes" target="_blank">修复了许多错误</a>；<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Self-Hosted-Compiler" target="_blank">自托管编译器</a>完成了 44%；扩展了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Support-Table" target="_blank"> Support Table</a>；少量的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Language-Changes" target="_blank">语言特性变化</a>；开始进行<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Performance-Tracking" target="_blank">性能跟踪</a>；<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Standard-Library" target="_blank">标准库</a>虽然尚未稳定，但变得更有用。”</p> 
<p>根据 Roadmap，<span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>0.9.0 发布周期的主要目标是实现<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Self-Hosted-Compiler" target="_blank">自托管编译器</a>。现在，44% 的行为测试通过，并且该百分比正在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftwitter.com%2Fandy_kelley%2Fstatus%2F1467652028159561728" target="_blank">迅速上升</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span>0.10.0 发布周期的主要目标则是<strong>稳定语言特性</strong>、<strong>创建语言规范的初稿</strong>和<strong>自托管编译器</strong>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>下一个发布周期中部分即将到来的里程碑：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Self-Hosted-Compiler" target="_blank">自托管编译器</a>可以使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23LLVM-Backend" target="_blank">LLVM 后端</a>构建自身</li> 
 <li>所有行为测试和其他测试都通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23LLVM-Backend" target="_blank">LLVM 后端</a>。此时可以发布<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Self-Hosted-Compiler" target="_blank">自托管编译器</a>而不是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Bootstrap-Compiler" target="_blank">Bootstrap 编译器</a>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Self-Hosted-Compiler" target="_blank">自托管编译器</a>可以使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23C-Backend" target="_blank">C 后端</a>构建自身</li> 
 <li>对 ELF 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Self-Hosted-Linker" target="_blank">自托管链接器</a>支持</li> 
 <li>对 PE/COFF 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Self-Hosted-Linker" target="_blank">自托管链接器</a>支持</li> 
 <li>通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23x86-Backend" target="_blank">x86 后端</a>或 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23aarch64-Backend" target="_blank">aarch64 后端的</a>行为测试，在针对相应架构时释放完整编译速度</li> 
</ul> 
<p style="text-align:start"><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>以下是 Zig 达到 1.0 的步骤：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ol> 
 <li>完成<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Self-Hosted-Compiler" target="_blank">自托管编译器</a>。</li> 
 <li>稳定语言特性，不再有<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Language-Changes" target="_blank">语言特性变更</a></li> 
 <li>完成语言规范初稿</li> 
 <li>实现官方包管理器</li> 
 <li>提供稳定<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fziglang.org%2Fdownload%2F0.9.0%2Frelease-notes.html%23Standard-Library" target="_blank">标准库</a></li> 
 <li>在没有任何重大更改的情况下进行一个完整的发布周期</li> 
 <li>最后标记 1.0。</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Zig 是一门通用编程语言，专为稳定性、可维护性和性能而设计，追求替代 C 语言在系统编程上的最佳地位。Zig 具有以下值得关注的特性：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>手动管理内存</li> 
 <li>与 C 语言竞争而非依赖它，Zig 标准库不依赖于 libc</li> 
 <li>轻量而简单，专注于调试应用而不是调试编程语言的知识</li> 
 <li>新的错误处理方法，与编写良好的 C 语言错误处理类似，但减少了很多冗余</li> 
 <li>调试模式下优化了快速编译时间，并在不确定行为发生时使用堆栈跟踪崩溃</li> 
 <li>ReleaseFast 模式和 ReleaseSafe 模式</li> 
 <li>泛型数据结构和函数</li> 
 <li>通过协程实现并发</li> 
 <li>导入 .h 头文件并直接使用 C 语言的类型、变量和函数</li> 
 <li>导出要依赖 C 语言代码的函数，变量和类型，自动生成 .h 头文件</li> 
 <li>可选类型而非空指针</li> 
 <li>交叉编译是主要用例</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2021/1223/073112_LnCS_2720166.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            