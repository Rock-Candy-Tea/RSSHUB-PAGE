
---
title: 'Rocky Linux 9.0 发布，CentOS 继承者'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0715/073239_IdbU_4937141.png'
author: 开源中国
comments: false
date: Fri, 15 Jul 2022 07:32:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0715/073239_IdbU_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Rocky Linux 是一个由 Rocky Enterprise Software Foundation 开发的 Linux 发行版，当红帽公司宣布他们将停止开发 CentOS 后，作为回应 CentOS 的原创始人 Gregory Kurtzer 宣布将启动一个项目来实现 CentOS 的最初目标。其名字是为了向 CentOS 早期的联合创始人 Rocky McGaugh 致敬。</p> 
<p><img alt height="394" src="https://static.oschina.net/uploads/space/2022/0715/073239_IdbU_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>Rocky Linux 9.0 于今天正式发布，该版本基于 Red Hat Enterprise Linux 9，值得关注的更新内容包括：</p> 
<h3>桌面环境</h3> 
<p>Rocky Linux 9 将 GNOME 40 作为默认的桌面环境。重新设计的核心应用程序、设置和用户界面使 Rocky Linux 作为一个桌面操作系统使用起来比以往更容易。Activities 现在在工作、启动应用程序等方面提供了更好的体验。</p> 
<p>其他针对桌面使用的显著改进包括：</p> 
<ul> 
 <li>通过右键单击并选择适当的选项，软件可以在独立显卡上运行</li> 
 <li>能够通过选择 "勿扰" 将通知静音，这将作为一个单独的按钮出现在通知中</li> 
 <li>每个屏幕可以使用不同的刷新率</li> 
 <li>Activities 程序允许你使用拖放的方法将应用程序图标分组到文件夹里</li> 
 <li>小数点显示比例</li> 
</ul> 
<h3>文件系统</h3> 
<p>XFS 现在支持 Direct Access（DAX）操作，允许直接访问可由字节寻址的持久性内存，帮助避免使用传统 block I/O 引发的延迟。NFS 引入了 "eager write" 挂载选项，以帮助减少延迟。</p> 
<h3>语言运行时和工具</h3> 
<p>Rocky Linux 9 拥有许多最新的运行时和编译器，包括 GCC 11.2.1、LLVM（13.0.1）、Rust（1.58.1）和 Go（1.17.1）。</p> 
<p>Rocky Linux 9 有更新的开发者工具链版本，包括 GCC（11.2.1）、glibc（2.34）和 binutils（2.35）。GCC 编译器的新功能帮助开发者通过改进的调试选项更好地跟踪代码，并编写优化的代码以有效使用硬件。</p> 
<p>Rocky Linux 9 扩展了 Rocky Linux 8 中的模块打包功能。Software Collections、Flatpaks 和 RPM 如今都被纳入了应用流，使开发者更容易使用他们喜欢的包。</p> 
<ul> 
 <li>Python 3.9 将在 Rocky Linux 9 的整个生命周期中得到支持，并带有许多新功能，包括新的字符串前缀和后缀方法、字典联合操作、高性能解析器、多进程改进。</li> 
 <li>Node.js 16 包括将 V8 引擎升级到 9.2 版本，新的 Timer Promises API、新的 Web streams API，以及对 npm 软件包管理器 7.20.3 版本的支持。Node.js 现在与 OpenSSL 3.0 兼容。</li> 
 <li>Ruby 3.0.3 提供了若干性能改进，以及错误和安全修复。重要的改进包括并发性、静态分析、带 case/in 表达式的模式匹配、重新设计的单行模式匹配和查找模式匹配。</li> 
 <li>Perl 5.32 提供了错误修复和改进，包括 Unicode 第 13 版、一个新的实验性 infix 操作符，以及更快的特征检查。</li> 
 <li>PHP 8.0 提供了错误修复和增强功能，包括使用结构化元数据语法，新命名的参数，以及提高了即时编译的性能。</li> 
</ul> 
<h3>安全性</h3> 
<p>默认情况下，通过 SSH 进行的 root 用户密码认证已被禁用。OpenSSH 的默认配置不允许 root 用户用密码登录，从而防止攻击者通过暴力密码攻击获得访问权。用户可以使用 SSH 密钥来登录远程系统，而不是使用 root 密码。</p> 
<p>OpenSSL 3.0 增加了一个 Provider 的概念、一个新的版本管理方案，以及改进的 HTTPS。OpenSSL 3.0 的新 FIPS 模块可以防止非 FIPS 算法的使用，同时 FIPS 标志可以在内核中设置，而无需将 OpenSSL 切换到 FIPS 模式。</p> 
<h3>系统监控</h3> 
<p>Cockpit Web 控制台有一个改进的性能指标页面，有助于识别 CPU、内存、磁盘和网络资源占用高的原因。</p> 
<h3>下载</h3> 
<p>用户可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frockylinux.org%2Fdownload%2F" target="_blank">下载页面</a>下载适用于 x86_64、aarch64、ppc64le 和 s390x 架构的 Rocky Linux 9.0。</p> 
<h3>支持</h3> 
<ul> 
 <li>Rocky Linux 9 将被支持到 2032 年 5 月 31 日</li> 
 <li>Rocky Linux 8 将继续被支持到 2029 年 5 月 31 日</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frockylinux.org%2Fnews%2Frocky-linux-9-0-ga-release%2F" target="_blank">https://rockylinux.org/news/rocky-linux-9-0-ga-release/</a></p>
                                        </div>
                                      
</div>
            