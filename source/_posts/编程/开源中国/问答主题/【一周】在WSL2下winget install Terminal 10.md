
---
title: '【一周】在WSL2下winget install Terminal 1.0'
categories: 
 - 编程
 - 开源中国
 - 问答主题
headimg: 'https://oscimg.oschina.net/oscnet/up-938c6c67d2acc2a785521eaef0293664753.png'
author: 开源中国
comments: false
date: Sat, 23 May 2020 21:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-938c6c67d2acc2a785521eaef0293664753.png'
---

<div>   
<p><strong><a href="https://www.oschina.net/question/topic/weekly-news?show=time" rel="nofollow">回顾一周社区热门资讯</a></strong></p> 
<p>第【七十四】期：20200516-20200522</p> 
<p><img height="807" src="https://oscimg.oschina.net/oscnet/up-938c6c67d2acc2a785521eaef0293664753.png" width="1222" referrerpolicy="no-referrer"></p> 
<p><span style="color:#d35400"><strong>点击相应标题，跳转阅读全文</strong></span></p> 
<h4><strong><a href="https://www.oschina.net/news/115696/linux-upstream-against-o3-optimize-kernal" target="news" rel="nofollow">上游 Linux 开发者反对"-O3"级别的内核优化</a></strong></h4> 
<p>将内核默认编译优化级别设置为 -O3 的提案遭到了广泛的反对，因为这不一定会让内核变得更快，反而有可能会引入因优化而导致出现的特殊特性，甚至会产生让代码变得更慢的地方。Linus Torvalds 也进行了表态，他不认为这是一个明智的想法，尤其是 GCC -O3 级别的优化有时会导致出现问题。</p> 
<h4><strong><a href="https://www.oschina.net/news/115697/linux-5-8-inline-encryption-blk-mq" target="news" rel="nofollow">Linux Kernel 5.8 将为 blk-mq 引入内联加密支持</a></strong></h4> 
<p><span style="background-color:#ffffff; color:#24292e"><span style="background-color:#ffffff">blk-mq 是 Linux 的</span></span><span style="background-color:#fcfcfc; color:#333333">块设备层多队列机制，它将 Linux 内核存储栈中请求层的单队列改成多队列，理论上提升性能。</span></p> 
<h4><strong><a href="https://www.oschina.net/news/115701/spring-boot-2-3-0-released" target="news" rel="nofollow">Spring Boot 2.3.0 发布</a></strong></h4> 
<p><span style="color:#333333">带来大量新特性与改进。</span></p> 
<h4><strong><a href="https://my.oschina.net/editorial-story/blog/4280022" target="news" rel="nofollow">开源让软件更加安全了吗？</a></strong></h4> 
<p><span style="background-color:#ffffff; color:#494949">开源开发往往被认为是“常发布”（</span><span style="background-color:#ffffff; color:#494949">Release often）</span><span style="background-color:#ffffff; color:#494949">以及“更少漏洞”的，但近期的几份报告将目光放到更广泛的开源应用中去，得出相反的结论——使用者往往不能及时更新软件，这可能造成安全风险。</span></p> 
<h4><strong><a href="https://www.oschina.net/news/115721/evm-1-0-released" target="news" rel="nofollow">EVM 超轻量物联网虚拟机 1.0 正式版发布</a></strong></h4> 
<p>EVM 全称 Embedded Virtural Machine<span style="background-color:#ffffff; color:#333333">，本质上是一款通用、精简的嵌入式虚拟机，由语法解析前端框架和字节码运行后端构成，可运行在资源受限制的单片机上。</span></p> 
<h4><strong><a href="https://www.oschina.net/news/115770/drop-flash-support-in-firefox-84" target="news" rel="nofollow">Firefox 84 将完全停止对 Flash 的支持</a></strong></h4> 
<p><img src="https://static.oschina.net/uploads/space/2020/0519/081346_mvfY_4105562.png" referrerpolicy="no-referrer"></p> 
<h4><strong><a href="https://www.oschina.net/news/115772/mit-openag-project-failed" target="news" rel="nofollow">MIT “AI 种菜”项目失败，还因环保问题被罚 25125 美元</a></strong></h4> 
<p><span style="background-color:#ffffff; color:#333333">虽然 OpenAg 被认为是在割投资人韭菜，PFC 的产品设计不切实际，但不可否认，AI+农业的项目和实践已经越来越多。实际上，单就 AI “种菜”的场景来说，已经成为一道通用的科技考题：去年，世界顶级农业大学荷兰瓦赫宁根大学举办了一场人工智能温室种植大赛，微软、英特尔、腾讯等企业参加比赛，专门研究如何用农业AI培育出高产、高性价比的黄瓜？</span></p> 
<h4><strong><a href="https://www.oschina.net/news/115771/five-years-of-rust" target="news" rel="nofollow">Rust 发行 5 周年</a></strong></h4> 
<p><img src="https://static.oschina.net/uploads/space/2020/0519/081533_JGIF_4105562.png" referrerpolicy="no-referrer"></p> 
<h4><strong><a href="https://www.oschina.net/news/115774/gcc11-flips-on-cpp20-coroutine" target="news" rel="nofollow">GCC 11 在 C++20 模式下将启用协程支持</a></strong></h4> 
<p><span style="background-color:#ffffff; color:#333333">C++20 标准在今年年初确定了技术规范后，将于近期正式发布。GCC 10 已经配备了 C++20 的大部分内容，而对于 GCC 11 来说，其余的项目很有可能将会被解决，包括像上周看到的</span>为 std=c++20 启用协程的<span style="background-color:#ffffff; color:#333333">更改。</span></p> 
<h4><strong><a href="https://www.oschina.net/news/115795/grafana-7-0-released" target="news" rel="nofollow">Grafana 7.0 发布：改进的界面、新的插件平台和可视化等</a></strong></h4> 
<p><img src="https://static.oschina.net/uploads/space/2020/0520/073218_uqLS_4105562.png" referrerpolicy="no-referrer"></p> 
<h4><strong><a href="https://my.oschina.net/editorial-story/blog/4282610" target="news" rel="nofollow">那些想要替代 C 与 Java 们的后浪，如今混得怎么样？</a></strong></h4> 
<p><span style="background-color:#ffffff; color:#494949">有的乘着新技术的东风在某一新兴领域成为了行业标杆；有的在与“前浪”的和谐共生中猥琐发育，静待日后的逆袭；当然，</span><span style="background-color:#ffffff; color:#494949">更多的是消逝在了历史的长河里</span><span style="background-color:#ffffff; color:#494949">，甚至没有泛起一丝涟漪……</span></p> 
<h4><strong><a href="https://www.oschina.net/news/115801/use-ai-to-recover-images" target="news" rel="nofollow">AI 复原 100 年前的京城老视频，靠这三个开源工具</a></strong></h4> 
<p><img src="https://static.oschina.net/uploads/space/2020/0520/103730_YDU5_4487475.jpeg" referrerpolicy="no-referrer"></p> 
<h4><strong><a href="https://www.oschina.net/news/115715/munich-shift-back-to-opensource-again" target="news" rel="nofollow">又一次抛弃 Windows，德国慕尼黑再次拥抱开源</a></strong></h4> 
<p><span style="background-color:#ffffff; color:#333333">只要不涉及任何机密或个人数据，市政府相关软件都将开源，微软 Windows 与 Office 等软件再次被抛弃。</span></p> 
<h4><strong><a href="https://www.oschina.net/news/115815/windows-terminal-1-0-released" target="news" rel="nofollow">Windows Terminal 1.0 正式发布</a></strong></h4> 
<p><img src="https://oscimg.oschina.net/oscnet/up-fe733d74dc2dcf738815246a69d8b860746.png" referrerpolicy="no-referrer"></p> 
<h4><strong><a href="https://www.oschina.net/news/115865/opensource-to-c-to-b" target="news" rel="nofollow">开源，用 To C 时代网络效应的打法做 To B 基础软件</a></strong></h4> 
<p><span style="background-color:#ffffff; color:#333333">开源在大数据时代的繁荣在美国，而AI、5G、IoT时代，中国有机会成为孕育伟大开源企业的最佳土壤。Open Source is Eating the World, but 饕餮 is in China.</span></p> 
<h4><strong><a href="https://www.oschina.net/news/115817/microsoft-release-winget" target="news" rel="nofollow">微软开源 Windows 软件包管理器 winget，一行命令安装软件</a></strong></h4> 
<p><img src="https://static.oschina.net/uploads/space/2020/0520/150235_IOjL_3820517.png" referrerpolicy="no-referrer"></p> 
<h4><strong><a href="https://www.oschina.net/news/115819/wsl-whats-new-in-build-2020" target="news" rel="nofollow">微软 Build 2020 WSL 一览：WSL2 即将到来，对 GPU 和 Linux GUI 的支持也不远了</a></strong></h4> 
<p><img src="https://static.oschina.net/uploads/space/2020/0520/172703_UaPR_4105562.png" referrerpolicy="no-referrer"></p> 
<h4><strong><a href="https://www.oschina.net/news/115858/xbox-source-code-leak-original-console-windows-3-5" target="news" rel="nofollow">初代 Xbox 主机操作系统和 Windows NT 3.5 源码泄露</a></strong></h4> 
<p>Xbox 主机操作系统被泄露的代码大概率会被用于开发 Xbox 模拟器，毕竟长期以来都有非官方的模拟器在复制此内核，但最终的成果仅支持少量游戏。微软有 Xbox 和 Xbox 360 的专用模拟器，不过只在 Xbox One 游戏主机上提供，不支持 Windows PC。民间开发的 Xbox 模拟器正好满足部分用户的需求。</p> 
<h4><strong><a href="https://www.oschina.net/news/115834/chrome-83-released" target="news" rel="nofollow">Chrome 83 发布：新的跨域政策、表单控件，和改进的 Web 体验</a></strong></h4> 
<p><img src="https://static.oschina.net/uploads/space/2020/0521/081747_ZWcq_4105562.gif" referrerpolicy="no-referrer"></p> 
<h4><strong><a href="https://www.oschina.net/question/2918182_2316593" target="news" rel="nofollow">云计算时代，容器底层 cgroup 的代码实现分析</a></strong></h4> 
<p>Linux 内核，从入门到出家。</p> 
<h4><strong><a href="https://www.oschina.net/news/115857/ubuntu-20-10-zfs-auto-trim" target="news" rel="nofollow">使用 ZFS 的 Ubuntu 20.10 安装工具默认启用 TRIM</a></strong></h4> 
<p><span style="background-color:#ffffff; color:#333333">OpenZFS/ZFSOnLinux 在去年正式支持 TRIM，此功能可帮助提升固态硬盘的性能。支持 TRIM 可以减少写入，从而延长硬盘寿命。</span></p> 
<p><strong><span style="color:#d35400">上期：</span><a href="https://www.oschina.net/question/3820517_2316536" rel="nofollow">开源的谎言 | Deno 1.0 | 开源仓库被要求下架 | LLVM影响Rust性能</a></strong></p> 
<p><strong><span style="color:#d35400">往期：</span><a href="https://www.oschina.net/question/topic/weekly-news?show=time" rel="nofollow">一周热点</a></strong></p>
                  
</div>
            