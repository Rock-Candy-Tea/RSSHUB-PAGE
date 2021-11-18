
---
title: 'Linux已做好部署x86 CPU_直线推测_漏洞缓解措施的准备'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1118/c48519bbe9d754d.png'
author: cnBeta
comments: false
date: Thu, 18 Nov 2021 11:03:18 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1118/c48519bbe9d754d.png'
---

<div>   
上月，Phoronix 报道了有关 x86_64 CPU“直线推测”（简称 SLS）漏洞的缓解措施，相关工作有些类似于去年的 ARM 补丁。<strong>最新消息是，x86（包括 x86_64）方面的 SLS 缓解工作已被合并到 GCC 12 Git，预计不久后就会推出内核补丁。</strong>作为最新的 CPU 安全防护特性，几周前的大部分讨论，都提到 ARM 平台已率先得到修复。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1118/c48519bbe9d754d.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：<a href="https://gcc.gnu.org/git/?p=gcc.git;a=commitdiff;h=53a643f8568067d7700a9f2facc8ba39974973d3" target="_self">GCC.GNU.ORG</a>）</p><p>随着 GCC 和 LLVM / Clang 将它们的缓解措施合并，目前的工作重心开始越来越多地向 x86_64 方面倾斜。于是周三的时候，我们终于迎来了 GNU Compiler Collection 的合并支持。</p><blockquote><p>可知除了为 x86_64 带来 -mharden-sls= 的选项，它还包含了 none、all、return 或 indirect-branch 这几个值。</p><p>该行为可减轻控制流无条件改变后，于内存中线性推测执行指令的相关推测（通过在函数返回和间接分支之后添加 INT3 指令来实现）。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/1118/1ce5d9f9d9b3718.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">静待 GCC12 更新（截图 via <a href="https://gcc.gnu.org/bugzilla/show_bug.cgi?id=102952#c25" target="_self">Bugzilla</a>）</p><p>现有的一个 Linux 内核补丁，提议在可用的情况下使用此编译器的 SLS 强化选项。</p><p>由早前的 GCC 报错留言页面可知，其预计很快就会发布一个新的补丁（GCC 现已合并），并提议为所有 RETPOLINE 内核构建启用该选项。</p><p>若补丁被接受，各大 Linux 发行版供应商也将很快跟进。至于这件事到底会多快到来，还得看近期行业开发者对它的兴趣到底有多浓厚。</p><p>一切顺利的话，带有“-mharden-sls=”选项的 GCC 编译器的 12.1 稳定版本，有望于 2022 年 4 月前后发布。</p>   
</div>
            