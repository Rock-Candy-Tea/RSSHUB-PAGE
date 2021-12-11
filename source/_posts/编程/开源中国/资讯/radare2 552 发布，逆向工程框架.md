
---
title: 'radare2 5.5.2 发布，逆向工程框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7340'
author: 开源中国
comments: false
date: Sat, 11 Dec 2021 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7340'
---

<div>   
<div class="content">
                                                                    
                                                        <p data-darkreader-inline-color style="--darkreader-inline-color:#d8d4cf; color:#e8e6e3; margin-left:0px; margin-right:0px; text-align:start">radare2 是 radare 的一个重写版本，是一个逆向工程框架和命令行工具集，可以用来简化逆向工程任务。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d8d4cf; color:#e8e6e3; margin-left:0px; margin-right:0px; text-align:start">radare2 5.5.2 正式发布，该版本更新内容包括：</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>ARM/THUMB</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>修复<span> </span></strong><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">arm64 上 adrp 的组装错误  </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19464" target="_blank">#19464</a> </li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">使用的 asm 插件不存在时使用 null 插件</span></li> 
 <li>为 ARM 二进制文件处理更多 ELF 重定位</li> 
 <li>修复 Thumb 指令<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">mov-pc 的仿真问题</span></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Binary parsing（二进制解析）</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">加入 Plan 9的符号解析</span></li> 
 <li>修复 PE 元数据头部名称解析（.net 相关）</li> 
 <li>添加<span> </span><code>bin_xtr.xtr_pemixed</code><span> </span>PE 用户插件</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">构建</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在 git pull 的安装脚本中使用远程 URL</li> 
 <li>在 CI（新的一流平台）中启用 mingw32/mingw64 构建</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>cons/ui</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>改善面板模式下的 snow 体验</li> 
 <li>加入<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">eco! 和 eco* ，和其他生态排序列表。</span></li> 
 <li>在 graph.few 中显示上一个节点</li> 
 <li>分析代码时，在 disasm 中改进光标上/下的可视性</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>crash</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">修正了</span><span> </span>dwarf 解析器<span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">无效的指针读取问题</span></li> 
 <li>Fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19455" target="_blank">#19455</a><span> </span>-<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">pyc 缓冲区中使用的负污染偏移导致 oobread</span></li> 
 <li>Fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19448" target="_blank">#19448</a><span> </span>-<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">修正了在 PE 段头文件中使用非 null 终止字符串的问题</span></li> 
 <li>Fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19446" target="_blank">#19446</a><span> </span>-<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">x509 解析器中的空解引用（</span><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">null </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">derefs）</span></li> 
 <li>Fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19443" target="_blank">#19443</a><span> </span>-  marshall 中的 UAF 是空对象的问题</li> 
 <li>Fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19442" target="_blank">#19442</a><span> </span>-<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">修正 pyc 编组中的堆下溢</span></li> 
 <li>Fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19444" target="_blank">#19444</a><span> </span>-<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">PE签名逻辑中的空解引用</span></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>其他</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19463" target="_blank">#19463</a><span> </span>- io 写入错误会报告回归</li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Fissues%2F19473" target="_blank">#19473</a><span> </span>-<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">支持 libc 文件名 w/o 版本的堆分析</span></li> 
 <li>修复 Dalvik 的 Esil 条件</li> 
 <li>对六边形 VLIW 的初步支持</li> 
 <li>修复 r_str_replace 中的无限循环</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>差异/签名</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在 radiff2 中实现符号名称列表差异</li> 
 <li>修复<code>zj</code>变量的输出</li> 
 <li>将二分搜索算法添加到 pvector</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>r2pipe</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 r2pipe.cmd("Z") 命令失败时不返回任何输出的问题</li> 
 <li>更新了对 Go 和 V 的 R2pipeSide 支持</li> 
</ul> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d8d4cf; color:#e8e6e3; margin-left:0px; margin-right:0px; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Freleases%2Ftag%2F5.5.2" target="_blank">https://github.com/radareorg/radare2/releases/tag/5.5.2</a></p>
                                        </div>
                                      
</div>
            