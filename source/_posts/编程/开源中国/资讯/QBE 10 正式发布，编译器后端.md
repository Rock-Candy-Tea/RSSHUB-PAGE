
---
title: 'QBE 1.0 正式发布，编译器后端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0625/074444_ihYe_5430600.png'
author: 开源中国
comments: false
date: Sat, 25 Jun 2022 07:44:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0625/074444_ihYe_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">历经 8 年的开发，QBE 1.0 已正式</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fc9x.me%2Fcompile%2Freleases.html" target="_blank">发布</a><span style="background-color:#ffffff; color:#000000">。</span></p> 
<p><img alt height="459" src="https://static.oschina.net/uploads/space/2022/0625/074444_ihYe_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">QBE 是一个纯 C 实现的嵌入式编译器后端，<span style="color:#121212">作者将 QBE 与 LLVM 对比，强调 QBE 的优势是简单高效，声称以 LLVM 的 10% 代码量达到其 70% 的性能水平。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#121212"><strong>主要特性</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>完全支持 C ABI</li> 
 <li>支持 IEEE 32 位和 64 位浮点数</li> 
 <li>使用统一且简单的基于 SSA 的中间语言 (IL)</li> 
 <li>在所有编译阶段使用相同的 IL</li> 
 <li>Copy elimination</li> 
 <li>编译速度快（在<code>CFLAGS=-O2</code>的 Core 2 Duo 上为 2 秒）</li> 
 <li>……</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">QBE 目前已经在下列平台上编译和并通过测试：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Linux</li> 
 <li>FreeBSD</li> 
 <li>Mac OS X</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">编译 QBE 需要 GNU Make 和一个 C99 编译器。而 HTML 文档则使用一个 OCaml 程序根据正则文本文件来生成。</p>
                                        </div>
                                      
</div>
            