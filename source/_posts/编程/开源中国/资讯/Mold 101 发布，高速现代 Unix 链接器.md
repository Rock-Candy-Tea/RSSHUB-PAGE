
---
title: 'Mold 1.0.1 发布，高速现代 Unix 链接器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9167'
author: 开源中国
comments: false
date: Sat, 01 Jan 2022 07:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9167'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Mold 是现有 Unix 链接器的快速替代品，它比 LLVM lld 链接器快几倍。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前 Mold 发布了最新版本 1.0.1 ，此版本带来以下<span style="color:#24292f">新功能和各种错误修复：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新功能</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>make install</code>现在创建<code>/usr/local/libexec/mold/ld</code>，作为<code>mold</code>可执行文件的符号链接。现在也为 GCC 执行此操作，通过传递<code>-B/usr/local/libexec/mold</code>，可以告诉 GCC<code>ld</code>在该目录中使用，而不是<code>/usr/bin/ld</code>. (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2Fe8dcecfff0391af8d04d00845c36070a628e8c02" target="_blank">e8dcecf</a><span> </span>)</li> 
 <li>xxHash 库现在作为子树包含在模具的源树中，以便于构建。如果要链接到系统库目录中的 libxxhash，请传递<code>SYSTEM_XXHASH=1</code>到<code>make</code>. (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F665bffa52f3fc979c608c72f3fdf2f8280eeb13b" target="_blank">665bffa</a><span> </span>)</li> 
 <li><code>extern "C++"</code>指令现在在动态列表中受支持。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F7aa5c393e4bc1d35509f9ee7cc2980314359f89c" target="_blank">7aa5c39</a><span> </span>)</li> 
 <li>过去在 Mold 中受忽略的标志<span> </span><code>--color-diagnostics</code>，现已得到支持。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F6e290aab3e2bf445df46d117832579bf6ab2aa1c" target="_blank">6e290aa</a><span> </span>)</li> 
 <li>除了<span> </span><code>*</code><span> </span>，现在<span> </span><code>?</code><span> </span>也被视为版本脚本（<span style="color:#24292f">version script</span>）通配符模式中的特殊字符。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F31b0248b05e433c0589fe2736e61852515427d9a" target="_blank">31b0248</a><span> </span>)</li> 
 <li><code>--threads=N</code><span> </span>选项已添加为<span> </span><code>--thread-count=N</code>. (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2Ff9ff04866e9926b343d71d45facdb693ef37928d" target="_blank">f9ff048</a><span> </span>)</li> 
 <li>已添加下列选项：<code>--defsym</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2Ff6e800655b3ed6a5118017d4cdfddbba3b4fbf40" target="_blank">f6e8006</a>），<span> </span><code>-z nodefaultlib</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F8c86c2849697dd2a5747b075fa818ebead6b09e1" target="_blank">8c86c28</a>）<code>-z separate-code</code>，<code>-z noseparate-code</code>和<code>-z separate-lodable-segments</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F5601cf42366a20e04b080923fe535ab502929732" target="_blank">5601cf4</a>），<span> </span><code>-z max-page-size</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2Ff3766cda81f395adc84f79f2ab057a747172a1ef" target="_blank">f3766cd</a>）</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#24292f">bug 修复</span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>现在对未知<span> </span><code>-z</code><span> </span>选项发出警告而不是错误。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F8bc57363c8ea90c8bdc99274a03da1e347030255" target="_blank">8bc5736</a><span> </span>)</li> 
 <li>之前为非 SHF_ALLOC 注释段创建了一个 PT_NOTE 段。这是一个错误的行为，应该只为内存分配的部分创建段。这个问题已经解决。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F76407a66468802f42889fd161f1aa5a6c301dc9f" target="_blank">76407a6</a><span> </span>)</li> 
 <li>之前当未定义符号升级为动态符号时，版本脚本会影响它们的符号可见性，这是语义上不正确的行为，且会导致 libQt 构建失败（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fissues%2F151" target="_blank">#151</a>）。目前问题已修复。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F36633895e58c9cbb089ad80c64d9208a06e2baba" target="_blank">3663389</a><span> </span>)</li> 
 <li>从 1.0.1 开始， Mold 的行为与 GNU ld 相同。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F04ccd4dbdd77f6bc10508b19ab12e46cc9c32731" target="_blank"><u>04ccd4d</u></a><span> </span>)</li> 
 <li>以前，模具针对 Initial-Exec 线程局部变量应用了错误的重定位值。这导致 Mesa 3D 图形库 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fissues%2F197" target="_blank">#197</a><span> </span>)的链接失败。问题已解决。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2Fd1161137d9de64892e193cecda16fdf2f585351f" target="_blank">d116113</a><span> </span>)</li> 
 <li>GCC 7 有一个错误，它在特定条件下针对线程局部变量发出不正确的重定位，为了与 GCC 7 的错误兼容性，mold 不会将其报告为错误。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2Fd9606d65b5da7e7af4c1858a121264e80e58ef49" target="_blank">d9606d6</a><span> </span>)</li> 
 <li>如果输出文件包含多个线程局部 BSS 部分，则它们的布局会相互重叠。此错误导致使用 DMD 编译的程序出现运行时错误，DMD 是 D 语言的编译器 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fissues%2F126" target="_blank">#126</a><span> </span>)。此布局问题已解决。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2Fb151de6684a9b48381cc6340fa10b6e1cfc1a8c5" target="_blank">b151de6</a><span> </span>)</li> 
 <li>以前，在某些情况下的<span> </span><code>--sysroot</code> 中，mold 无法查找正确的文件。这导致<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FClickHouse%2FClickHouse" target="_blank">ClickHouse</a><span> </span>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fissues%2F150" target="_blank">#150</a><span> </span>)的链接失败。这个错误已被修复。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F135f17c5aa930fdd2441080a086f0a6379774c57" target="_blank">135f17c</a><span> </span>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Freleases%2Ftag%2Fv1.0.1" target="_blank">https://github.com/rui314/mold/releases/tag/v1.0.1</a></p>
                                        </div>
                                      
</div>
            