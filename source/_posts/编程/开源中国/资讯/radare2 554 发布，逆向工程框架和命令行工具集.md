
---
title: 'radare2 5.5.4 发布，逆向工程框架和命令行工具集'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5378'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 07:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5378'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">radare2 是 radare 的一个重写版本，是一个逆向工程框架和命令行工具集，可以用来简化逆向工程任务。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">radare2 5.5.4 正式发布，该版本更新内容包括：</p> 
<h2><strong>架构支持</strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">与拆解、组装和分析相关的变化：</p> 
<ul> 
 <li>在 anal.x86.cs 中使用 cs_disasm_iter ：可以使用更少的堆（<span style="color:#24292f">heap</span>）加速分析和反汇编</li> 
 <li>禁用 8051 的 asm 插件中的反汇编逻辑</li> 
 <li>在 8051 汇编程序中处理 jbc [reg]</li> 
 <li>在 8051 上推送时处理寄存器</li> 
 <li>改进 pD 循环读取太多字节问题</li> 
 <li>来自 asm 模块的更好的分析插件处理</li> 
</ul> 
<h2><strong>二进制解析</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>不再依赖区分大小写的 FS 来加载 DLL sdbs</li> 
 <li>支持 Mach-O DYLD_CHAINED_PTR_64_OFFSET 格式</li> 
</ul> 
<h2><strong>构建/ CI</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在安装脚本中检查现有的上游远程</li> 
 <li>修复 libr_lang 链接问题（在 5.5.2 中引入的新功能）</li> 
 <li>不要使用 d/ 重新制作模块（更快的“制作”构建）</li> 
</ul> 
<h2><strong>搜索</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>清理公共 API</li> 
 <li>将 JSON 输出添加到 zb 命令</li> 
</ul> 
<h2><strong>安全</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19476" target="_blank">#19476</a><span> </span>-<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19476" target="_blank">aao 中的</a>堆溢出</li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19478" target="_blank">#19478</a><span> </span>- 符号文件中的空 deref</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Freleases%2Ftag%2F5.5.4" target="_blank">https://github.com/radareorg/radare2/releases/tag/5.5.4</a></p>
                                        </div>
                                      
</div>
            