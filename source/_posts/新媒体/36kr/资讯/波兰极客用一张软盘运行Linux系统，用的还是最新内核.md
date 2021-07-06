
---
title: '波兰极客用一张软盘运行Linux系统，用的还是最新内核'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210706/v2_763943d31d644bc9a8ae500ce3084af8_img_000'
author: 36kr
comments: false
date: Tue, 06 Jul 2021 07:16:52 GMT
thumbnail: 'https://img.36krcdn.com/20210706/v2_763943d31d644bc9a8ae500ce3084af8_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/-8L5MFZrgmyatGgYaR1AEA">“量子位”（ID:QbitAI）</a>，作者：丰色，36氪经授权发布。</p> 
<p>用软盘启动Linux系统曾经很“家常便饭”，当然那都是90-00年代的事了。</p> 
<p>有年纪（bushi）的同学可能熟悉。</p> 
<p>但现在，即使你还有一张能用的3.5英寸软盘，可1.44MB的容量远远装不下一个现代linux内核，更不用说还得加上所有支持软件了。</p> 
<p>但奇人有招，波兰一位游戏开发小哥只用一张软盘就把现代Linux操作系统嵌进去了！</p> 
<p>盘上还有几百KiB的剩余空间！而且用的都是最新“组件”，包括今年5.16号才发布的5.13.0-rc2版本的Linux内核。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_763943d31d644bc9a8ae500ce3084af8_img_000" data-img-size-val="1080,810" referrerpolicy="no-referrer"></p> 
<h2>一张软盘装下现代Linux系统</h2> 
<p>小哥把这个系统命名为Floppinux，在它的官网上带大家走了整个过程，包括从下拉（pull down）、编译源代码到创建最终的磁盘映像的所有命令。</p> 
<p>而之所以做这么一件事情，是因为小哥觉得自己用了好多年Linux，也用过很多Live-CD（能够在不安装到硬盘的前提下，体验Linux操作系统的东西）。</p> 
<p>但他对其背后的基本原理知之甚少，所以决定动手研究一下。</p> 
<p>小哥的第一个目标是运行Nomad Diskmag程序。</p> 
<p>Diskmag这个远古东西不知道有人了解吗？</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_afe66f30f98749f980c2711061c3abf4_img_000" data-img-size-val="776,944" referrerpolicy="no-referrer"></p> 
<p>它的全称叫disk magazine，也就是磁盘杂志，是一种在上世纪80-90年代，以软盘形式发行的电子杂志。90年代后就被在线出版物所取代了。</p> 
<p>小哥已经用bash脚本搞定了前端界面，就差封面、目录和cat每个文件的正文了。</p> 
<p>为了运行他写的脚本，需要一个可用的Linux 发行版，也就是一个可以在软盘上运行的系统。</p> 
<p>动手！</p> 
<p>因为在64位系统上编译32位代码有点棘手。为了更简单，小哥用他的32位CPU的旧笔记本来做这一切。</p> 
<p>可以使用32位系统的VirtualBox，如果要用64位，添加命令“ARCH=x86”，例如：make ARCH=x86 tinyconfig。</p> 
<p>下面就是把现代Linux操作系统装进一张1.44MB软盘的大概过程：</p> 
<p><strong>1、创建并进入你想要保存文件的目录</strong></p> 
<p><strong>2、配置和构建定制内核</strong></p> 
<p>使用最新Linux内核（版本5.13.0-rc2）：</p> 
<p>git clone --depth=1 https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git</p> 
<p>进行最小配置：make tinyconfig</p> 
<p>添加额外配置：make menuconfig</p> 
<p>从菜单中选择以下选项：</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_43489e2206a94cb7ad259b6605dddca4_img_000" data-img-size-val="1080,442" referrerpolicy="no-referrer"></p> 
<p>将设置保存并退出，等待编译完成，最后内核将在arch/x86/boot/bzImage中构建，把它移到主目录。</p> 
<p><strong>3、 添加工具</strong></p> 
<p>如果没有工具，内核只会启动，无法执行任何操作。小哥使用BusyBox（最流行的轻量级工具之一），下载并解压：</p> 
<p>wget https://busybox.net/downloads/busybox-1.33.1.tar.bz2</p> 
<p>进入目录，进行启动配置：make allnoconfig</p> 
<p>然后选择你想要的工具：make menuconfig</p> 
<p>每个菜单项都显示各工具需占用多少KB，合理选择哦。</p> 
<p>小哥的选择：</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_4435212918ec4a3bb9d540abc7310895_img_000" data-img-size-val="1080,543" referrerpolicy="no-referrer"></p> 
<p>保存配置并退出，编译完成后_install目录下会创建一个包含所有文件的文件系统，把它移到主目录。</p> 
<p><strong>4、添加目录结构</strong></p> 
<p>有了内核和基本工具，仍然需要一些额外的目录结构：</p> 
<p>cd ../filesystemmkdir -pv &#123;dev,proc,etc/init.d,sys,tmp&#125;sudo mknod dev/console c 5 1sudo mknod dev/null c 1 3</p> 
<p>接下来创建几个配置文件，启动后显示欢迎消息：</p> 
<p>cat >> welcome << EOFSome welcome text...EOF</p> 
<p>然后配置处理启动、退出和重启的Inittab文件&实际的初始化脚本，并使初始化脚本可执行，并将所有文件的所有者设置为root。（限于篇幅命令已省略，具体可查看文末链接[1]）</p> 
<p>最后，将此目录压缩为一个文件。</p> 
<p>可通过从主目录运行QEMU（在GNU/Linux 平台上广泛使用的模拟处理器）对以上所有内容进行测试。</p> 
<p><strong>5、下面就是把这一切放进软盘了</strong></p> 
<p>创建指向内核和文件系统的Syslinux引导文件（boot file）：</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_dff684dcb37948ec8daa10332670b77a_img_png" data-img-size-val="839,210" referrerpolicy="no-referrer"></p> 
<p>创建空软盘映像：</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_253ddc676a254e96897d1a90a751934d_img_png" data-img-size-val="833,78" referrerpolicy="no-referrer"></p> 
<p>Mount it !并将syslinux、内核和文件系统复制到软盘映像：</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_961a15ba5c5644e6a20e2e90953b186f_img_png" data-img-size-val="832,118" referrerpolicy="no-referrer"></p> 
<p>完成！</p> 
<p>现在你就有了自己的发行版映像floppinux.img，你可以烧录到软盘，然后在真正的硬件上启动它了！</p> 
<h2>启动耗时1分多</h2> 
<p>小哥花了不到3分钟烧录成功，然后开始了首次启动：</p> 
<p>成功！大概只花了1分多钟。</p> 
<p>小哥（老哥）表示，在这种裸机的现代硬件上，唯一能阻止启动速度的就是软驱的实际速度。它们最大原始速度为125KB/s。实际上可能会更慢。</p> 
<p>下面是软盘占有空间总结，可以看到还剩272KiB。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_356fda4cd78b472ba8ec3a8348e2e0ee_img_000" data-img-size-val="1080,209" referrerpolicy="no-referrer"></p> 
<h2>网友热议：“92年的时候我可是需要两张5.25”的软盘”</h2> 
<p>硬件<a class="project-link" data-id="4262185" data-name="开源项目" data-logo="https://img.36krcdn.com/20210603/v2_43fe3145b6494227bd8db07dcdc0147b_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/4262185" target="_blank">开源项目</a>网站 Hackaday对小哥的创造进行了报道，<a class="project-link" data-id="395913" data-name="并点" data-logo="https://img.36krcdn.com/20201105/v2_3e58b018e0db433d84d2d8b155d99ced_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/395913" target="_blank">并点</a>评道：</p> 
<blockquote> 
 <p>当然，为了将最新的Linux内核和BusyBox构建到大约1MB的空间，必须做出一些让步，所以Floppinux肯定不是任何人所说的日常驱动程序。一旦系统启动，除了编写一些shell脚本之外，就没有什么可做的了。</p> 
 <p>即使你没有软盘，也值得跟着他的教程，在QEMU中启动映像，看看如何从零开始正式构建一个Linux系统。这事不仅可以用来吹牛，这样一个最小安装的所有组件如何组合在一起的知识，对学习嵌入式Linux设备也很有用。</p> 
</blockquote> 
<p>而在Hacker News 论坛上很多人纷纷对小哥竖起大拇指，有人表示最令他惊讶的就是用的最新版的Linux内核和BusyBox。而且这对其他嵌入式系统也很有用。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_8352c8f0566a4059a6f274a51a90e8fb_img_000" data-img-size-val="1080,242" referrerpolicy="no-referrer"></p> 
<p>有人说，92年的时候我可是需要两张5.25英寸的软盘来运行Linux！</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_dd82e7429896441ebcbe6f64aecd0227_img_000" data-img-size-val="1080,82" referrerpolicy="no-referrer"></p> 
<h2>开发者介绍</h2> 
<p><img src="https://img.36krcdn.com/20210706/v2_87b45c955c5c42d49b60e9d7452a86d9_img_000" data-img-size-val="512,740" referrerpolicy="no-referrer"></p> 
<p>文中的主角“小哥”叫Krzysztof Jankowski，来自波兰，85后，是一名专业的游戏开发者和数字艺术家。</p> 
<p>25年前就开始用QBASIC编程，喜欢FOSS、像素画（pixel art）、树莓派,、游戏引擎等。</p> 
<p>去年，他创办了自己的公司Cyfrowy Nomada，与beffio签订了高级游戏引擎开发合同。他成为一名专业的游戏开发商的梦想成为现实。</p> 
<p>他和他的伙伴们开发的游戏“自由坦克”（Tanks of Freedom）不知道有人玩过没？</p> 
<p>GitHub传送门：https://github.com/w84death/floppinux</p> 
<p>参考链接：</p> 
<p>[1]https://bits.p1x.in/floppinux-an-embedded-linux-on-a-single-floppy/</p> 
<p>[2]https://hackaday.com/2021/05/24/running-modern-linux-from-a-single-floppy-disk/</p> 
<p>[3]https://news.ycombinator.com/item?id=27247612</p> 
<p>[4]https://krzysztofjankowski.com/</p>  
</div>
            