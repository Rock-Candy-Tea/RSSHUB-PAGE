
---
title: '谷歌讲述从Goobuntu转向gLinux内部桌面发行版的心路历程'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0730/89bcac69c71a10b.jpg'
author: cnBeta
comments: false
date: Sat, 30 Jul 2022 08:18:21 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0730/89bcac69c71a10b.jpg'
---

<div>   
位于加州山景城的 Google 总部办公室，遍布着 Windows、Chromebook、Mac 等设备。<strong>但除了依靠 Linux 服务器之外，这家科技巨头其实还拥有自己的 Linux 桌面发行版。</strong>尽管外界知之甚少，但 Google 一直在积极酝酿。而首个版本，就是基于 Ubuntu 改造出来的 Goobuntu 。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0730/89bcac69c71a10b.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：Google Cloud <a href="https://cloud.google.com/blog/topics/developers-practitioners/how-google-got-to-rolling-linux-releases-for-desktops" target="_self">Blog</a>）</p><p>2018 年，Google 又将其内部 Linux 桌面，从 Goobuntu 迁移到了基于 Debian 的 gLinux 发行版。</p><p>该公司解释称：</p><blockquote><p>Ubuntu LTS 的两年期限，意味着我们必须在操作系统支持周期结束前，对超过 10 万+的设备进行升级。</p><p>而 Goobuntu 舰队的完整升级工作，需要耗费一年中的大部分时间，意味着窗口期只剩下一年。</p><p>再加上对工程 PC 的完全定制所需的耗时，这么做实在过于昂贵和痛苦。更难受的是，在下一个 LTS 轮回中，Goobuntu 团队还得重新再过一遍。</p><p>整个过程对我们来说是一个巨大的压力因素，除了要搞定成百上千的问题，还得努力帮助解决各种极端状况。</p></blockquote><p>在受够了这一切之后，我们也不难理解为何 Google 要从 Ubuntu 转向 Debian Linux 了。</p><p>需要指出的是，该公司打造了一个特殊的 Debian 滚动发行版 —— 它就是 GLinux Rolling Debian Testing（Rodete）。</p><blockquote><p>其设想是为用户和开发者带来最佳体验，在创建并认为已准备好投入生产环境时尽快为他们提供最新的补丁和更新。</p><p>同属此类的发行版，还包括了 Arch Linux、Debian Testing 和 openSUSE Tumbleweed 。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0730/6b48b7e141b5141.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>不过对于 Google 来说，此时最迫切的目标是摆脱两年的升级周期限制。</p><blockquote><p>正如向持续集成 / 部署（<a href="https://practical-tech.com/2018/07/10/continuous-integration-and-delivery-tool-basics/" target="_self">CI / CD</a>）转变所表明的那样，这些增量更改运行很是良好。即便遇到问题，也能够更加轻松地控制和回滚。</p><p>为了让所有这些工作不耗费大量时间和精力，Google 甚至打造了一套全新的 Sieve 工作流系统。</p><p>每当发现一个新版 Debian 软件包时，它就会开始一个新的构建。此外考虑到通常单独的包必须一起升级，这些包也被成组放置。</p><p>接下来便是使用完整的系统安装、引导和本地测试套件，分别对每组包进行测试 —— 包构建可在几分钟内完成，但测试可能需耗费一小时。</p></blockquote><p>完成后，所有新软件包都将与最新的 gLinux 软件包池合并。然后当 Google 决定将其发布到生产环境时，团队就会启用该池的快照。</p><p>最后才是向整个舰队推送新版本，但不仅仅是将其转储给用户，而是基于站点可靠性工程（SRE）原则来逐步推进（比如 incremental Canarying 增量尝鲜），以避免遭遇重大失误。</p><blockquote><p>多年来，Google 在这方面一直做得很好。且得益于 Sieve，今天整个 gLinux 开发团队，都由一个在成员之间轮值的发布工程师来担当。</p><p>即使想要对所有机器进行升级，也无需使出多大的力气去推动 —— 因为它砍去了从 alpha、beta 到通用发布（GA）的多个阶段。</p><p>更棒的是，由于采用了滚动发布计划，Google 可以快速修补整个舰队的安全漏洞、而不至于影响整体的稳定性。</p><p>而在此之前，安全工程师们必须仔细检查每个 Debian 安全公告（<a href="https://www.debian.org/security/index.en.html" target="_self">DSA</a>），以确保所有修复都已囊括其中。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0730/08aceb95a780fcc.png" alt="3.png" referrerpolicy="no-referrer"></p><p>此外 Google 改进了测试套件和运行关键开发人员系统的关键集成测试，合作伙伴团队会评估其最新 Linux 内核 / 发行版所提供的稳定体验。</p><blockquote><p>我们对自动化管道中的一切强烈渴望，已经显著减少了团队的工作量和压力。</p><p>现在还可上报错误、以及与其它库版本的不兼容性，同时确保 Google 工具在 Linux 生态系统中更好地工作。</p></blockquote><p>展望未来，Google 团队还将通过与上游 Debian 展开更紧密的合作、贡献更多的内部补丁，来帮助维护 Debian 软件包的生态系统。</p><p>这一切听起来都很棒，但 <a href="https://www.computerworld.com/article/3668548/the-story-behind-google-s-in-house-desktop-linux.html" target="_self">Computer World</a> 还是有两点要指出：</p><blockquote><p>首先，对于某些组织来说，LTS 长期支持版本仍有其存在的意义。如果你所在的企业并不需要最新、最闪耀的程序，Ubuntu 或 Red Hat LTS Linux 仍是个不错的选择。</p><p>其次，CW 并不认为 Google 已经发展到了能够让整条滚动发行版的自动化生产管道，精进到只需一名工程师便可维护超过 10 万用户的 Linux 桌面。</p><p>更重要的是，如果 Google 有足够的自信，那不妨直接将 Sieve 代码分享出来，以便大家都可轻松上手滚动更新的 Linux 桌面发行版。</p></blockquote>   
</div>
            