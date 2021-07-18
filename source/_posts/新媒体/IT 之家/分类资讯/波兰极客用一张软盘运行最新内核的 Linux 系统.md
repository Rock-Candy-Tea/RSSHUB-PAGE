
---
title: '波兰极客用一张软盘运行最新内核的 Linux 系统'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/7/9549d19b-e1f8-475f-9fcb-fffb6e7eee29.jpg@s_2,w_820,h_615'
author: IT 之家
comments: false
date: Sun, 18 Jul 2021 07:59:51 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/7/9549d19b-e1f8-475f-9fcb-fffb6e7eee29.jpg@s_2,w_820,h_615'
---

<div>   
<p>7 月 18 日消息，用软盘启动 Linux 系统曾经很“家常便饭”，当然那都是 90-00 年代的事了。</p><p>但现在，即使你还有一张能用的 3.5 英寸软盘，<span class="accentTextColor">可 1.44MB 的容量远远装不下一个现代 linux 内核</span>，更不用说还得加上所有支持软件了。</p><p>但奇人有招，<span class="accentTextColor">波兰一位游戏开发小哥只用一张软盘就把现代 Linux 操作系统嵌进去了</span>。</p><p>盘上还有几百 KiB 的剩余空间，而且用的都是最新“组件”，包括今年 5.16 号才发布的 5.13.0-rc2 版本的 Linux 内核。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/9549d19b-e1f8-475f-9fcb-fffb6e7eee29.jpg@s_2,w_820,h_615" w="1080" h="810" title="波兰极客用一张软盘运行最新内核的 Linux 系统" srcset="https://img.ithome.com/newsuploadfiles/2021/7/9549d19b-e1f8-475f-9fcb-fffb6e7eee29.jpg 2x" width="1080" height="615" referrerpolicy="no-referrer"></p><h2>一张软盘装下现代 Linux 系统</h2><p>小哥把这个系统命名为 Floppinux，在它的官网上带大家走了整个过程，<span class="accentTextColor">包括从拉取（pull down）、编译源代码到创建最终的磁盘映像的所有命令</span>。</p><p>而之所以做这么一件事情，是因为小哥觉得自己用了好多年 Linux，也用过很多 Live-CD（能够在不安装到硬盘的前提下，体验 Linux 操作系统的东西）。</p><p>但他对其背后的基本原理知之甚少，所以决定动手研究一下。</p><p><span class="accentTextColor">小哥的第一个目标是运行 Nomad Diskmag 程序</span>。</p><p>Diskmag 这个远古东西不知道有人了解吗？</p><p>它的全称叫 disk magazine，也就是磁盘杂志，是一种在上世纪 80-90 年代，以软盘形式发行的电子杂志。90 年代后就被在线出版物所取代了。</p><p>小哥已经用 bash 脚本搞定了前端界面，就差封面、目录和 cat 每个文件的正文了。</p><p>为了运行他写的脚本，需要一个可用的 Linux 发行版，也就是一个可以在软盘上运行的系统。</p><p>因为在 64 位系统上编译 32 位代码有点棘手。为了更简单，小哥用他的 32 位 CPU 的旧笔记本来做这一切。</p><blockquote><p>可以使用 32 位系统的 VirtualBox，如果要用 64 位，添加命令“ARCH=x86”，例如：make ARCH=x86 tinyconfig。</p></blockquote><p>下面就是把现代 Linux 操作系统装进一张 1.44MB 软盘的大概过程：</p><p><strong>1、创建并进入你想要保存文件的目录</strong></p><p><strong>2、配置和构建定制内核</strong></p><p>使用最新 Linux 内核（版本 5.13.0-rc2）：</p><pre class="brush:javascript;toolbar:false">git clone --depth=1 https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git</pre><p>进行最小配置：</p><pre class="brush:javascript;toolbar:false ai-word-checked">make tinyconfig</pre><p>添加额外配置：</p><pre class="brush:javascript;toolbar:false">make menuconfig</pre><p>从菜单中选择以下选项：</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/6b26ff02-9e61-4060-8eeb-414b8d2b05e7.png" w="1080" h="442" title="波兰极客用一张软盘运行最新内核的 Linux 系统" width="1080" height="336" referrerpolicy="no-referrer"></p><p>将设置保存并退出，等待编译完成，最后内核将在 arch/x86/boot/bzImage 中构建，把它移到主目录。</p><p><strong>3、 添加工具</strong></p><p>如果没有工具，内核只会启动，无法执行任何操作。小哥使用 BusyBox（最流行的轻量级工具之一），下载并解压：</p><pre class="brush:javascript;toolbar:false ai-word-checked">wget https://busybox.net/downloads/busybox-1.33.1.tar.bz2</pre><p>进入目录，进行启动配置：</p><pre class="brush:javascript;toolbar:false">make allnoconfig</pre><p>然后选择你想要的工具：</p><pre class="brush:javascript;toolbar:false ai-word-checked">make menuconfig</pre><p>每个菜单项都显示各工具需占用多少 KB，合理选择哦。</p><p>小哥的选择：</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/614f7024-efdc-451f-859c-e22c7f90602c.png" w="1080" h="543" title="波兰极客用一张软盘运行最新内核的 Linux 系统" width="1080" height="412" referrerpolicy="no-referrer"></p><p>保存配置并退出，编译完成后_install 目录下会创建一个包含所有文件的文件系统，把它移到主目录。</p><p><strong>4、添加目录结构</strong></p><p>有了内核和基本工具，仍然需要一些额外的目录结构：</p><pre class="brush:javascript;toolbar:false">cd ../filesystem
mkdir -pv &#123;dev,proc,etc/init.d,sys,tmp&#125;
sudo mknod dev/console c 5 1
sudo mknod dev/null c 1 3</pre><p>接下来创建几个配置文件，启动后显示欢迎消息：</p><pre class="brush:javascript;toolbar:false ai-word-checked">cat >> welcome << EOF
Some welcome text...
EOF</pre><p>然后配置处理启动、退出和重启的 Inittab 文件 & 实际的初始化脚本，并使初始化脚本可执行，并将所有文件的所有者设置为 root。（限于篇幅命令已省略，具体可查看<a href="https://bits.p1x.in/floppinux-an-embedded-linux-on-a-single-floppy/" target="_blank">此链接</a>）</p><p>最后，将此目录压缩为一个文件。</p><p>可通过从主目录运行 QEMU（在 GNU/Linux 平台上广泛使用的模拟处理器）对以上所有内容进行测试。</p><p><strong>5、下面就是把这一切放进软盘了</strong></p><p>创建指向内核和文件系统的 Syslinux 引导文件（boot file）：</p><pre class="brush:javascript;toolbar:false">cat >> syslinux.cfg << EOF
DEFAULT linux
LABEL linux
SAY [ BOOTING FLOPPINUX VERSION 0.1.0 ]
KERNEL bzImage
END initrd=rootfs.cpio.gz
EOF
chmod +x syslinux.cfg</pre><p>创建空软盘映像：</p><pre class="brush:javascript;toolbar:false ai-word-checked">dd if=/dev/zero of=floppinux.img bs=1k count=1440
mkdosfs floppinux.img
syslinux --install floppinux.img</pre><p>Mount it ! 并将 syslinux、内核和文件系统复制到软盘映像：</p><pre class="brush:javascript;toolbar:false">sudo mount -o loop floppinux.img /mnt
sudo cp bzImage /mnt
sudo cp rootfs.cpio.gz /mnt
sudo cp syslinux.cfg /mnt
sudo umount /mnt</pre><p>完成！</p><p>现在你就有了自己的发行版映像 floppinux.img，你可以烧录到软盘，然后在真正的硬件上启动它了！</p><h2>启动耗时 1 分多</h2><p>小哥花了不到 3 分钟烧录成功，然后开始了首次启动，成功，大概只花了 1 分多钟。</p><p>小哥（老哥）表示，在这种裸机的现代硬件上，唯一能阻止启动速度的就是软驱的实际速度。它们最大原始速度为 125KB/s。实际上可能会更慢。</p><p>下面是软盘占有空间总结，可以看到还剩 272KiB。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/887447c6-1957-46da-a15a-690601aa2467.png" w="1080" h="209" title="波兰极客用一张软盘运行最新内核的 Linux 系统" width="1080" height="159" referrerpolicy="no-referrer"></p><h2>网友热议：“92 年的时候我可是需要两张 5.25”的软盘”</h2><p>硬件开源项目网站 Hackaday 对小哥的创造进行了报道，并点评道：</p><blockquote><p>当然，为了将最新的 Linux 内核和 BusyBox 构建到大约 1MB 的空间，必须做出一些让步，所以 Floppinux 肯定不是任何人所说的日常驱动程序。一旦系统启动，除了编写一些 shell 脚本之外，就没有什么可做的了。</p><p>即使你没有软盘，也值得跟着他的教程，在 QEMU 中启动映像，看看如何从零开始正式构建一个 Linux 系统。这事不仅可以用来吹牛，这样一个最小安装的所有组件如何组合在一起的知识，对学习嵌入式 Linux 设备也很有用。</p></blockquote><p>而在 Hacker News 论坛上很多人纷纷对小哥竖起大拇指，有人表示最令他惊讶的就是用的最新版的 Linux 内核和 BusyBox。而且这对其他嵌入式系统也很有用。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/91254de0-b0b6-4f5f-8e62-977651901740.png" w="1080" h="242" title="波兰极客用一张软盘运行最新内核的 Linux 系统" width="1080" height="184" referrerpolicy="no-referrer"></p><p>有人说，92 年的时候我可是需要两张 5.25 英寸的软盘来运行 Linux！</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/21d2fb68-a9fd-4fb8-980c-418e114692f9.png" w="1080" h="82" title="波兰极客用一张软盘运行最新内核的 Linux 系统" width="1080" height="62" referrerpolicy="no-referrer"></p><h2>开发者介绍</h2><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/348318b9-42ff-4172-be8e-1279f310753c.png" w="512" h="740" title="波兰极客用一张软盘运行最新内核的 Linux 系统" width="512" height="740" referrerpolicy="no-referrer"></p><p>文中的主角“小哥”叫 Krzysztof Jankowski，来自波兰，85 后，是一名专业的游戏开发者和数字艺术家。</p><p>25 年前就开始用 QBASIC 编程，喜欢 FOSS、像素画（pixel art）、树莓派，、游戏引擎等。</p><p>去年，他创办了自己的公司 Cyfrowy Nomada，与 beffio 签订了高级游戏引擎开发合同。他成为一名专业的游戏开发商的梦想成为现实。</p><p>他和他的伙伴们开发的游戏“自由坦克”（Tanks of Freedom）不知道有人玩过没？</p><p>GitHub 传送门：<a href="https://github.com/w84death/floppinux" target="_blank">点此直达</a></p>
          
</div>
            