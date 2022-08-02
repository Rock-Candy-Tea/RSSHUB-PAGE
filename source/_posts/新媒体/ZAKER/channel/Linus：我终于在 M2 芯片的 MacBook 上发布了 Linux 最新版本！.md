
---
title: 'Linus：我终于在 M2 芯片的 MacBook 上发布了 Linux 最新版本！'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62e8cca38e9f090c45720a31_1024.jpg'
author: ZAKER
comments: false
date: Tue, 02 Aug 2022 02:08:18 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62e8cca38e9f090c45720a31_1024.jpg'
---

<div>   
<p>整理 | 彭慧中 责编 | 屠敏</p><p>近日，Linus Torvalds（以下简称 "Linus"）宣布 Linux Kernel 5.19 正式版终于可以和大家见面了。这一版本意义重大，虽然它比原计划晚了一周发布，但其带来了更多新功能、硬件支持以及大量错误和安全修复。</p><p>不过，以上都不是最惊喜的，最让 Linus 津津乐道的是，他借助了<a href="http://iphone.myzaker.com/zaker/link.php?pk=62e8dd12b15ec06d063257c6&b=aHR0cDovL21wLndlaXhpbi5xcS5jb20vcz9fX2Jpej1Nak01TWpBd09ETTRNQT09Jm1pZD0yNjUwOTMwNjUxJmlkeD0xJnNuPTcyM2I1YmYyNjIzZTM4ZDdlNThjNjNkMmVhN2ZlNDFjJmNoa3NtPWJkNTk4YzA4OGEyZTA1MWU5MDU5MjI1MzVmZDFkMDNkYmI5MTU2YjdjOTZmZjhjMWQzNzBhMzkwM2MyYzI4YzM0MjA3OTcxYjZmNGEmc2NlbmU9MjEjd2VjaGF0X3JlZGlyZWN0&bcode=0e34a24b&target=_new" target="_blank">Asahi Linux 项目</a>，<strong>在配有 M2 芯片的 MacBook Air 上发布了<strong>Linux 内核新版本</strong></strong>。</p><p><strong>逐步实现 " 拥抱 ARM64"</strong></p><p>Linus 在邮件中表示：" 就个人而言，我认为最有趣的部分是我在 ARM64 笔记本电脑上发布 Linux Kernel 5.19 正式版，并且写下了这封邮件。这是我期待已久的事情，感谢 Asahi 团队，使这一切终于成为现实。尽管我们使用 ARM64 硬件来运行 Linux 已有一段时日，但直到现在它都没有真正用作开发平台。"</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202208/62e8cca38e9f090c45720a31_1024.jpg" data-height="1333" data-width="1829" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62e8cca38e9f090c45720a31_1024.jpg" referrerpolicy="no-referrer"></div></div>这已经是 Linus 第三次使用苹果硬件进行 Linux 开发了。在很早之前他曾在搭载 PPC970 处理器（IBM 开发）的麦金塔 G5 设备上为 PowerPC 进行过开发；第二次是十几年前的第一代 MacBook Air；而如今，Linus 又在搭载了 M2 芯片的 MacBook Air 这款超薄的笔记本上进行操作，可见他对于在苹果硬件上开发 Linux 有相当大的执念。<p></p><p>Linus 表示：" 现阶段我并没有将 MacBook Air 用于任何实际的工作，我只是将其用于版本测试、启动以及现在的版本发布。<strong>不过我会尝试将工作迁移到这款 MacBook 上，也许下次发布版本的时候我能够完全拥抱 ARM64。</strong>"</p><p>对大多数 Linux 用户来说，Linus 目前使用什么电脑并不重要，而且 Asahi Linux 仍然处于粗糙的早期状态。但<strong>使用现代版本的 ARM 指令集和 " 接近上游的内核 "，会产生连锁反应，使生态系统的其他部分受益</strong>。</p><p>更多的人使用 ARM 版本的 Linux，意味着更多的人修复与 ARM 有关的错误，这将使所有发行版受益。最终，在 ARM 硬件上使用 Linux 的经验将会对每个人都有所改善，尽管这些好处可能需要数年时间才能显现出来。</p><p><strong>Linux Kernel 5.19 其他重要变化</strong></p><p>随着 Linux 5.19 内核版本的发布，其也支持国产 CPU 龙芯自研指令集，Linus 也表示这是重要的一步。</p><p>除此之外，Linux 5.19 版内核的还有一些非常值得关注的重要变化：</p><p>支持英特尔的信任域扩展，将虚拟机与虚拟机管理程序 /hypervisor 和平台上的任何其他软件隔离开来，以增加传统虚拟化所能实现的隔离性。</p><p>支持 AMD 的 SEV-SNP，它可以保护虚拟机免受对管理程序的攻击。</p><p>对 Arm 的多平台支持已基本完成。</p><p>改进了对华硕主板的监控。</p><p>移除对瑞萨 H8/300 CPU 架构的支持，该架构有一个奇怪的特点，就是已经从内核中移除，然后又恢复了。</p><p>Linus 在邮件的最后表示，他打算把下一个版本的内核<strong>从原来按照版本号命名的 Linux 5.20 改为 Linux 6.0，因为他开始担心大家再次被 " 大数字 " 弄迷糊</strong>。这种做法与 4.x 系列略微不一致，之前 Linux 4.20 版本发布之后版本才来到了 Linux 5.0，如今的做法遵循了 3.x 系列使用的相同方案，该系列停在 3.19。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            