
---
title: 'Linux Lab 发布 v0.8-rc3，正式支持 Rust, LLVM 和 openEuler'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic3.zhimg.com/80/v2-1a0d63ae7ea54b06219169153764ba52_720w.jpg'
author: 开源中国
comments: false
date: Tue, 05 Oct 2021 12:53:00 GMT
thumbnail: 'https://pic3.zhimg.com/80/v2-1a0d63ae7ea54b06219169153764ba52_720w.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0; margin-right:0; text-align:start">1. 简介</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#dddad5; color:#121212; margin-left:0px; margin-right:0px; text-align:start">自 2021 年 6 月 3 日发布 v0.7 正式版后，本次迎来了 v0.8-rc3，这将是 v0.8 正式版发布之前的最后一个候选版本。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#dddad5; color:#121212; margin-left:0px; margin-right:0px; text-align:start">除了某型 RISC-V 真实开发板支持，其他 v0.8 开发计划基本都有落地。RISC-V 真板适配的开发延迟主要有两方面原因，一方面是缺少来自开发板官方的有效支持，另外一方面是缺少来自社区的爱好者报名，这部分工作将继续延期到后续版本。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><strong>2. v0.8-rc3 重要变更</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新功能 
  <ul style="margin-left:0; margin-right:0"> 
   <li>新增 Rust for Kernel 开发支持，用法见文档使用“内核特性”部分的 4.1.3.3 节</li> 
   <li>新增 openEuler Kernel 开发支持，用法见<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F414642391" target="_blank">10分钟内快速开展国产 openEuler 内核开发</a></li> 
   <li>新增 llvm 编译支持，`make kernel LLVM=1` 即可切换为 llvm 编译（需较高版本内核）</li> 
   <li>新增 rust 环境安装脚本：tools/deps/rust.sh，默认下载在 tools/deps/rust 目录下，重启 Linux Lab 无需重新安装</li> 
  </ul> </li> 
 <li>功能完善或修复 
  <ul style="margin-left:0; margin-right:0"> 
   <li>清理 examples 下的案例，删除部分过期案例，修订所有汇编案例</li> 
   <li>新增 .mbx 格式的内核 patch 支持</li> 
   <li>新增 samples 目录到内核模块支持；修复诸如 rust_print<em><span> </span>这样带“_</em>”的模块名字</li> 
   <li>优化 feature 支持：强化 download 支持，主动触发 olddefconfig，在 download.sh 中可以下载 patchset 并安装缺失的环境</li> 
   <li>在 boot with nfs 过程中自动安装 src/system 中的文件，方便在 src/system 中预设需要的测试脚本和测试文件</li> 
   <li>修复 host gcc 对早期 x86 内核版本的自动切换功能</li> 
   <li>新增 _range 函数，方便设定某个内核版本范围内的 gcc 等环境要素</li> 
   <li>在 clone 目标中自动 clone patchset，方便快速复用就近的内核版本支持</li> 
  </ul> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">3. 同期进展</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#dddad5; color:#121212; margin-left:0px; margin-right:0px; text-align:start">在 v0.8-rc3 这一个月的开发周期内，随身 Linux Lab 实验盘与随身 Pocket Linux 系统盘同步新增了更多的主流发行版支持，目前已经涵盖：Ubuntu 18.04/20.04/21.04, Deepin 20.2, Fedora 34 和 Manjaro。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#dddad5; color:#121212; margin-left:0px; margin-right:0px; text-align:start">如果考虑省去安装 Linux Lab 的烦恼，可以考虑直接从某宝的社区开源小店选购一支随身 Linux Lab 实验盘，容量覆盖 16G-512G，有高速与固态主控，另外支持智能启动、透明倍容、零损编译和时区兼容。 <img src="https://pic3.zhimg.com/80/v2-1a0d63ae7ea54b06219169153764ba52_720w.jpg" width="1024" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">4. 后续计划</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#dddad5; color:#121212; margin-left:0px; margin-right:0px; text-align:start">将于一周后发布 v0.8 正式版。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#dddad5; color:#121212; margin-left:0px; margin-right:0px; text-align:start">社区后续将重点加强对更多实验材料的支持，加强视频内容的输出，方便大家更好地把 Linux Lab 开源项目使用起来。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#dddad5; color:#121212; margin-left:0px; margin-right:0px; text-align:start">欢迎在这里提需求哈：</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#dddad5; color:#121212; margin-left:0px; margin-right:0px; text-align:start"><a href="https://www.oschina.net/news/gitee.com/tinylab/linux-lab/issues/I49VV9" target="_blank">成功适配过 Linux Lab 的国内外图书、线上课程列表 · Issue #I49VV9 · 泰晓科技/Linux Lab - Gitee.com</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">5. 延伸阅读</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F415617020" target="_blank">如何在几分钟内快速获取并体验某项 Linux 内核新技术</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F414642391" target="_blank">10分钟内快速开展国产 openEuler 内核开发</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F413717850" target="_blank">仅用 3 条命令快速体验 Rust For Linux</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F404733757" target="_blank">Linux Lab 新增 RISC-V 操作系统课程 RVOS 实验支持</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F273550410%2Fanswer%2F2145562757" target="_blank">Linux内核代码一次性编译通过，可能吗？</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F456820006%2Fanswer%2F2143557430" target="_blank">如何评价 linux 内核开始支持使用 rust 进行开发?</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F488900079%2Fanswer%2F2143443583" target="_blank">如何评价 2021 年 9 月 25 日华为全新发布的 openEuler 欧拉操作系统？</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F482782438%2Fanswer%2F2134373947" target="_blank">需要用到 Linux/Unix，是买 MacBook Pro还是 Windows 装Linux vm？</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F451548622%2Fanswer%2F1830251840" target="_blank">想认真学习Linux内核，选哪个发行版为好？或者随意哪个发行版都可以？</a></li> 
</ul>
                                        </div>
                                      
</div>
            