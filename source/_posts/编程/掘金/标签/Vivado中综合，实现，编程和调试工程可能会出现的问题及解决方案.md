
---
title: 'Vivado中综合，实现，编程和调试工程可能会出现的问题及解决方案'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c4667f1e836486ba3249c947188d25e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 17:12:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c4667f1e836486ba3249c947188d25e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Xilinx公司的IDE(集成开发环境) Vivado用处广泛，学会使用Vivado对FPGA的学习至关重要，这里以PRX100-D开发板为例，对Vivado的学习使用进行探讨。本文将会持续更新，列出一些常见的Vivado使用过程中出现的问题，供大家参考。</p>
<p>在Vivado使用过程中 出现的问题，主要会分为以下几类：</p>
<ol>
<li>与Vivado软件本身相关的问题</li>
<li>Vivado综合，仿真，实现过程中出现的问题</li>
<li>编程和调试PRX100-D开发板注意事项</li>
</ol>
<p> </p>
<h1 data-id="heading-0">1.与Vivado软件本身相关的问题</h1>
<ul>
<li><strong>Vivado在添加新的工程/HDL文件后会自动崩溃退出</strong></li>
</ul>
<p>这一问题出现在2018.2版本中。Xilinx官方网站上说明在2017.1版本后都出现过该问题。该问题的出现可能是与srcscanner.exe(用于刷新工程文件的hierarchy结构) 和低端的启动库有关。解决方法为先尝试重启系统，如果不能解决这个问题，可以尝试安装Xilinx提供windows操作系统下的boot可执行文件，文件在bootSharedDirFixApp.zip(附在文后)里面。直接解压缩和执行就能解决这个问题。</p>
<ul>
<li><strong>Vivado出现内部异常，如图1.1所示</strong></li>
</ul>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.icfedu.cn%2Fwp-content%2Fuploads%2F2021%2F03%2Fvivado_internal_e.jpg" target="_blank" rel="nofollow noopener noreferrer" title="http://www.icfedu.cn/wp-content/uploads/2021/03/vivado_internal_e.jpg" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c4667f1e836486ba3249c947188d25e~tplv-k3u1fbpfcp-zoom-1.image" alt="vivado_internal_e" title="%title插图%num" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>图1.1 Vivado出现内部异常</p>
<p>导致内部异常的原因有很多，但是可行的解决方法有非常直接的，经测试后可行的就是关闭Vivado窗口，再次重新打开。</p>
<p> </p>
<p> </p>
<h1 data-id="heading-1">2.Vivado综合，仿真，实现过程中 出现的问题</h1>
<ul>
<li><strong>在Vivado综合时，出现如图2.1所示错误</strong></li>
</ul>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.icfedu.cn%2Fwp-content%2Fuploads%2F2021%2F03%2Ferror.jpg" target="_blank" rel="nofollow noopener noreferrer" title="http://www.icfedu.cn/wp-content/uploads/2021/03/error.jpg" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43aafbb513044a739c88c548fa232473~tplv-k3u1fbpfcp-zoom-1.image" alt="error" title="%title插图%num" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>图2.1 Vivado综合错误</p>
<p>图2.1显示了<strong>没有错误信息，只有警告信息，但是工程综合失败</strong>。这种情况可能是由于<strong>工程的路径名上出现了中文</strong>导致的。所以可以将工程路径全改成由英文/数字/下划线组成。Vivado只支持由Ascii字符组成的名字，包括：A-Z，a-z，0-9和下划线。</p>
<p> </p>
<ul>
<li><strong>Vivado错误：Vivado [Common 17-180] Spawn failed: No error</strong></li>
</ul>
<p>这个错误出现的原因是工程的路径名太长，超过了80个字符。解决方法也很简单，缩短工程路径即可。</p>
<p> </p>
<ul>
<li><strong>Vivado在编写和genvar有关的代码时，出现的错误：[Synth 8-196] conditional expression could not be resolved to a constant</strong></li>
</ul>
<p>错误原因不明，也没有官方的解决方法，已知都是与genvar有关。尝试过有效的解决方式是将声明的genvar的名字更改的更特别，比如从genvar u换成genvar uu_var。</p>
<p> </p>
<ul>
<li><strong>Vivado综合时出现错误:[Synth 8-3352] multi-driven net…</strong></li>
</ul>
<p>在使用D flip-flop时，错误将输出Q端在不同的代码块内被赋值了两次。简易的D flip-flop如图2.2所示。解决办法是把两次不同的赋值集中到一个代码块，并且添加不同的条件限制，使其不是同时被执行。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.icfedu.cn%2Fwp-content%2Fuploads%2F2021%2F03%2Fdff.jpg" target="_blank" rel="nofollow noopener noreferrer" title="http://www.icfedu.cn/wp-content/uploads/2021/03/dff.jpg" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb5a6026fe6640d2a5c9b9f51a863eae~tplv-k3u1fbpfcp-zoom-1.image" alt="dff" title="%title插图%num" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>图2.2 D flip-flop简单示意图</p>
<p> </p>
<ul>
<li><strong>Vivado仿真出现错误：ERROR: [Simulator 45-7] No such file ‘C:/FII_RISCV_V2.01_2020_0724/FII_RISCV_V2.01.srcs/sources_1/new/cpu_sys/fii_rv32i_core.v’ in the design.</strong></li>
</ul>
<p>错误出现原因是将工程转移到了另外的文件路径下。解决方法有以下几种：</p>
<ul>
<li>
<ul>
<li>换一种文件途径名，避免出现不支持的字符，比如空格，中文等</li>
<li>挪回原来的文件夹</li>
<li>重启工程/仿真</li>
<li>删掉C:\FII_RISCV_V2.01_2020_0724\FII_RISCV_V2.01.sim\sim_1\behav\xsim（这里是示例文件途径，可针对性自己的文件途径修改）</li>
</ul>
</li>
</ul>
<p>经过测试，最后一种方法解决了这个问题。</p>
<p> </p>
<ul>
<li><strong>Vivado仿真出现错误：ERROR: [XSIM 43-3322] Static elaboration of top level Verilog design unit(s) in library work failed.</strong></li>
</ul>
<p>在网上查询得到的是Vivado软件的错误，但实际测试后发现，该错误出现的原因是仿真读取十六进制数据时(使用的是readmemh)，模块的路径错误。已知readmemh的用法如下：</p>
<pre><code class="copyable">reg [<memory_width>] <reg_name> [<memory_depth>];

initial
$readmemh ("<file_name>", <reg_name>, <start_address>, <end_address>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际用法如下所示，在将红体标记的路径改正后，可以正常进行仿真：</p>
<pre><code class="copyable">localparam FILE_NAME = "../../../f_seg.HEX";
integer file_handle = 0;
initial begin
file_handle = $fopen(FILE_NAME,"r");
if(!file_handle)
begin
$display("Could not open File \r");
$stop;
end
$readmemh (FILE_NAME, fii_cpu_sys_inst.fii_riscv_cpu_inst.fii_rv32i_core_inst.fii_instr_rib_inst.program_inst.inst.native_mem_module.blk_mem_gen_v8_4_1_inst.memory);

$fclose(file_handle); 
end
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p> </p>
<h1 data-id="heading-2">3.编程和调试PRX100-D开发板注意事项</h1>
<ul>
<li><strong>连接到JTAG后，在Vivado中找不到相应的硬件</strong></li>
</ul>
<p>可能原因有PRX100-D上JTAG的跳线位置不对，注意在图3.1所示的跳线中，应当连接<strong>内部</strong>JTAG，也就是<strong>2-3</strong>。并使用对应的线连接上PRX100-D和电脑。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.icfedu.cn%2Fwp-content%2Fuploads%2F2021%2F03%2Fjumper-e1616693441321.jpg" target="_blank" rel="nofollow noopener noreferrer" title="http://www.icfedu.cn/wp-content/uploads/2021/03/jumper-e1616693441321.jpg" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92f91576a02a43a7954e07cf53d2d111~tplv-k3u1fbpfcp-zoom-1.image" alt="jumper" title="%title插图%num" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>图3.1 JTAG跳线</p>
<p>还有一种可能是连接JTAG和电脑的线缆供电不足，这种情况可以通过用<strong>外部12V电源供电</strong>的方式，如图3.2所示，将电源线接到电源口，并且将电源跳线连接EXT-5V和PWR_5V(用连接JTAG和电脑的线供电时，需要将电源跳线跳到USB_5V和PWR_5V)，如图3.3所示，即可缓解单根JTAG到电脑线的供电不足问题。也可以尝试同时连接JATG端口，UART端口和电脑，用两根线缆同时供电。</p>
<p> </p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.icfedu.cn%2Fwp-content%2Fuploads%2F2021%2F03%2Fpower_supply.jpg" target="_blank" rel="nofollow noopener noreferrer" title="http://www.icfedu.cn/wp-content/uploads/2021/03/power_supply.jpg" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e30ecf7cd89b459288bc782a6983b0db~tplv-k3u1fbpfcp-zoom-1.image" alt="power_supply" title="%title插图%num" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>图3.2 电源接口</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.icfedu.cn%2Fwp-content%2Fuploads%2F2021%2F03%2Fpower_jumper.jpg" target="_blank" rel="nofollow noopener noreferrer" title="http://www.icfedu.cn/wp-content/uploads/2021/03/power_jumper.jpg" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13230d52001a4a50988ac0c70a76a361~tplv-k3u1fbpfcp-zoom-1.image" alt="power_jumper" title="%title插图%num" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>图3.3 电源选择跳线</p>
<p>最后，注意在连接好PRX100-D和电脑后，需要将开发板的电源按钮按下启动。电源启动按钮如图3.4所示。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.icfedu.cn%2Fwp-content%2Fuploads%2F2021%2F03%2Fpower_bnutton.png" target="_blank" rel="nofollow noopener noreferrer" title="http://www.icfedu.cn/wp-content/uploads/2021/03/power_bnutton.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e168abd65bd74fdf85354937caaba765~tplv-k3u1fbpfcp-zoom-1.image" alt="power_bnutton" title="%title插图%num" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>图3.4 电源启动按键</p>
<p> </p>
<ul>
<li><strong>连接到UART接线后，在windows下的设备管理器下没有出现相应的端口。</strong></li>
</ul>
<p>正确的设备管理器发现UART接线的情况，如图3.5所示。但可能有少数情况下，UART的硬件无法被windows系统发现，这时，则需要重新安装CP210x的驱动程序，可以从Silicon Lab上官方网站上下载(点击<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.icfedu.cn%2Fgo%3F_%3D209885c0d3aHR0cHM6Ly93d3cuc2lsYWJzLmNvbS9kZXZlbG9wZXJzL3VzYi10by11YXJ0LWJyaWRnZS12Y3AtZHJpdmVycw%253D%253D" target="_blank" rel="nofollow noopener noreferrer" title="http://www.icfedu.cn/go?_=209885c0d3aHR0cHM6Ly93d3cuc2lsYWJzLmNvbS9kZXZlbG9wZXJzL3VzYi10by11YXJ0LWJyaWRnZS12Y3AtZHJpdmVycw%3D%3D" ref="nofollow noopener noreferrer">这里</a>到相应的界面)对应的驱动。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.icfedu.cn%2Fwp-content%2Fuploads%2F2021%2F03%2FUART.jpg" target="_blank" rel="nofollow noopener noreferrer" title="http://www.icfedu.cn/wp-content/uploads/2021/03/UART.jpg" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c82bf8f87a92412ab6068e15e28430af~tplv-k3u1fbpfcp-zoom-1.image" alt="UART" title="%title插图%num" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>图3.5 设备管理器中出现正常的UART接线</p>
<p> </p>
<ul>
<li><strong>Vivado错误：ERROR: [Common 17-70] Application Exception: CORE_LOCATION mismatch</strong></li>
</ul>
<p>错误出现的步骤一般是在添加debug core后上板调试时，错误原因不明。Xilinx官方技术人员提供的解决方法都没有效果。实际有效的操作为关闭Vivado窗口，再次重新打开。</p>
<p> </p>
<p> </p>
<h1 data-id="heading-3">4.文章参考</h1>
<p>[1] Xilinx官方论坛：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.xilinx.com%2Fsupport.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.xilinx.com/support.html" ref="nofollow noopener noreferrer">www.xilinx.com/support.htm…</a></p></div>  
</div>
            