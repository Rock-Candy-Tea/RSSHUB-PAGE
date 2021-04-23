
---
title: 'radare2 5.2.1 发布，逆向工程平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7442'
author: 开源中国
comments: false
date: Fri, 23 Apr 2021 07:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7442'
---

<div>   
<div class="content">
                                                                    
                                                        <p>radare2 5.2.1 发布了。radare2 是一款开放源代码的逆向工程平台，它可以反汇编、调试、分析和操作二进制文件。</p> 
<p>主要更新内容：</p> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>修复 coverity 带来的所有 high impact 问题（主要是 non null terminated strings、oobreads、ub 和 uaf）</li> 
 <li>修复从 nested elfs 中加载符号的问题</li> 
 <li>修复在不同环境下的 i*j 输出</li> 
 <li>改进的绑定和签名匹配结果</li> 
 <li>修复了空的 R2_GITTAP 版本字符串问题</li> 
 <li>pdcj（内部反编译器的 json 输出）现在可以使用了</li> 
 <li>修复 build --with-openssl</li> 
 <li>修复正则表达式搜索问题</li> 
</ul> 
<p><strong>Performance</strong></p> 
<ul> 
 <li>优化 RCodeMeta API（在 iaito 中反编译速度快约 10 倍）</li> 
 <li>现在，Linux 调试器的速度提高了 35 倍（<code>aaaa</code>现在只需 6 秒而不是 4 分钟）</li> 
 <li>在 cfg.debug 上设置 anal.in = dbg.map，加速分析</li> 
</ul> 
<p><strong>Improvements</strong></p> 
<ul> 
 <li>在生成 ih json 输出之前加载 binary header structs</li> 
 <li>扩展的 ESIL 支持以获取更多 MMX 指令</li> 
 <li>Rafind2 输出默认类似于 grep，更适合脚本编写</li> 
 <li>命名为<code>bluy</code>的新颜色主题</li> 
 <li>更新到最后一个 GNU 反汇编程序，并支持所有最新的 MIPS asm.cpu</li> 
 <li>oss-fuzz 已被修复，radare2-fuzz 项目已创建</li> 
</ul> 
<p><strong>Linux 上的调试器改进</strong></p> 
<ul> 
 <li>修复了 ubuntu-arm64 上的调试器步骤</li> 
 <li>修复 Linux 调试器上的 REGREAD 错误（并非所有内核都支持）</li> 
 <li>修复Alpine Linux调试器附加问题</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Freleases%2Ftag%2F5.2.1" target="_blank">https://github.com/radareorg/radare2/releases/tag/5.2.1</a></p>
                                        </div>
                                      
</div>
            