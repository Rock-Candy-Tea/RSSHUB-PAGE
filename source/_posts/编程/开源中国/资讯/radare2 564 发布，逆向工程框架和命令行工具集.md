
---
title: 'radare2 5.6.4 发布，逆向工程框架和命令行工具集'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1882'
author: 开源中国
comments: false
date: Wed, 02 Mar 2022 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1882'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">radare2 是 radare 的一个重写版本，是一个逆向工程框架和命令行工具集，可以用来简化逆向工程任务。</p> 
<p style="margin-left:0px">radare2 5.6.4 现已发布，该版本代码名称为"do bisa vijnu"，主要更新内容包括：</p> 
<h3 style="margin-left:0px"><strong>anal</strong></h3> 
<ul> 
 <li>在 agfm 中处理跳转表</li> 
 <li>添加 agfma 以在美人鱼（<span style="color:#24292f">mermaid</span>）图中进行组装</li> 
 <li>添加 agfm 命令以使用美人鱼语法打印 cfg 图</li> 
</ul> 
<h3><strong>bin</strong></h3> 
<ul> 
 <li>使用 izz 在 maddr'd 二进制文件中查找字符串</li> 
 <li>修复导致错过 ascii 字符串的 Wide32 字符串检测</li> 
 <li>修复 <span style="color:#24292f">macho </span>解析器中过长的加载时间</li> 
 <li>修复小 ELF 样本的缓慢加载时间</li> 
</ul> 
<h3><strong>build</strong></h3> 
<ul> 
 <li>修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19726" target="_blank">#19726</a> - 修复使用 syslz4 时的 <span style="color:#24292f">meson </span>定义顺序问题</li> 
 <li>添加 rasm2 和 rax2 wasi/wapm 包</li> 
 <li>为 wasi/wapm/wasm 构建修复，并更新 sdb</li> 
</ul> 
<h3>charset</h3> 
<ul> 
 <li>添加对片假名的初始支持</li> 
</ul> 
<h3><strong>crash</strong></h3> 
<ul> 
 <li>修复 clusterfuzz 报告的小类分析超时</li> 
 <li>修复 PE/QNX/DYLDCACHE/PSX 解析器中的 DoS</li> 
 <li>修复 kernelcache bin 解析器中的 DoS</li> 
 <li>修复 <span style="color:#24292f">macho </span>核心符号中的 oobread</li> 
 <li>修复 bin.symbols 中的 null deref</li> 
 <li>修复 minidump 解析器中的 DoS</li> 
 <li>修复 <span style="color:#24292f">macho</span> 解析器上的 DoS</li> 
 <li>修复 dyldcache 解析器中的堆缓冲区溢出</li> 
</ul> 
<h3><strong>调试</strong></h3> 
<ul> 
 <li><strong>在 FreeBSD 上添加对 powerpc、powerpc64、powerpc64le 和 riscv64 的支持</strong></li> 
</ul> 
<h3><strong>print</strong></h3> 
<ul> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19729" target="_blank">#19729</a> - 使 pswj 与 psw 输出一致</li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19739" target="_blank">#19739</a> - 修复 pv* 中的 oobread 并修复 pvj 中的错误</li> 
</ul> 
<h3><strong>shell</strong></h3> 
<ul> 
 <li>添加<code>aot</code>命令以显示指令类型（如 /atl）</li> 
</ul> 
<h3><strong>visual</strong></h3> 
<ul> 
 <li>在 V 中恢复和恢复块大小：</li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19737" target="_blank">#19737</a> - 处理 ascii 十六进制列中的 ESC 和空格</li> 
</ul> 
<p> </p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Freleases%2Ftag%2F5.6.4" target="_blank">https://github.com/radareorg/radare2/releases/tag/5.6.4</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            