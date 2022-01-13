
---
title: 'Ubuntu Desktop硬件门槛降低 支持2GB树莓派4上运行'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0113/ca3cc9dc4914a02.webp'
author: cnBeta
comments: false
date: Thu, 13 Jan 2022 07:32:37 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0113/ca3cc9dc4914a02.webp'
---

<div>   
<strong>今天，Canonical 宣布进一步降低 Ubuntu Desktop 的硬件门槛，支持在 2GB 内存的树莓派 4 上运行。</strong>完整的 Ubuntu 桌面环境对于树莓派来说是相当大的负担，因此 Canonical 推荐用户使用 4GB/8GB 内存的型号，以确保其性能良好。而即将发布的 Ubuntu 22.04 LTS，目标之一是降低入门门槛。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0113/ca3cc9dc4914a02.webp" alt="njj2qbk4.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">这意味着要在 Raspberry Pi 4 2GB 机型上实现可行的桌面体验。而之所以能够在 2GB 内存的树莓派 4 上运行 Ubuntu，最大的秘诀就是叫做 zswap 的功能，并表示该功能会成为 Ubuntu 22.04 的标准功能。</p><p style="text-align: left;"><strong>什么是 zswap？</strong></p><p style="text-align: left;">为了回答这个问题，我们需要讨论一下常规的 swap 文件。</p><p style="text-align: left;">如果你正在运行任何类型的 Linux 系统，你很有可能（并且建议）在你的硬盘或 SD 卡上分配一个交换文件。交换文件作为你的内存的一种延伸，缓存那些很少使用的页面，为更多的活动进程释放内存。这使你能够继续工作，即使你的系统正在使用几乎所有的内存。 然而，swap 的性能不如 RAM，因为访问硬盘（或SD卡）的速度较慢。</p><p style="text-align: left;">好吧，那么 zswap 是怎么来的呢？</p><p style="text-align: left;">zswap 本质上是一个压缩工具。当一个进程要被转移到交换文件时，zswap 会对它进行压缩，并检查新的、更小的大小是否还需要被转移，或者它是否可以留在你的RAM中。解压缩"zswapped"页面要比访问交换文件快得多，所以这是一个从内存较小的系统中获得更多收益的好方法。</p><p style="text-align: left;"><strong>听起来不错，我如何启用它呢？</strong></p><p style="text-align: left;">由于zswap是默认支持的，你可以用一个简单的命令来启用它。</p><p style="text-align: left;">在你的终端输入以下内容。</p><pre>$ sudo sed -i -e 's/$/ zswap.enabled=1/' /boot/firmware/cmdline.txt</pre><p style="text-align: left;">这条命令基本上是编辑启动文件夹中cmdline.txt文件的一个快捷方式，并将zswap.enabled参数设置为"True"（1）。一旦你这样做了，你就可以重新启动你的设备，并受益于性能的提升。</p><p style="text-align: left;"><strong>进一步优化</strong></p><p style="text-align: left;">如果你不愿太折腾，那么你可以到此为止。上述命令应该可以提高现有的 4GB/8GB 树莓派 4 的性能，但是性能提升不如 2GB 的树莓派 4 这么明显。对于更高级的用户，在 Canonical 领导 Ubuntu Raspberry Pi 工作的 Dave Jones 有一些额外的改进要分享。 他在他的个人博客上写了一篇更详细的关于如何配置的博文，但我们将在下面转述这些内容。</p><p style="text-align: left;"><strong>● 切换到 z3fold 和 lz4</strong></p><p style="text-align: left;">→ 增加被压缩对象的数量，使用一个叫做z3fold的分配器。</p><p style="text-align: left;">→ 使用一种叫做 lz4 的不同的压缩算法，该算法在速度和压缩方面提供了更好的平衡。</p><p style="text-align: left;">在你的终端输入以下命令:</p><pre>$ Sudo -i</pre><p style="text-align: left;">这将提示你输入密码，并使你进入root模式，你可以输入以下命令。</p><pre># echo lz4 >> /etc/initramfs-tools/modules
# echo z3fold >> /etc/initramfs-tools/modules
# update-initramfs -u</pre><p style="text-align: left;">这将把lz4和z3fold模块添加到initramfs中，这样它们就可以在初始化时被访问。等待update-initramfs进程完成，然后输入。最后，需要在你的 cmdline.txt 文件中添加以下命令，与之前类似。</p><pre>$ sudo sed -i -e 's/$/ zswap.compressor=lz4/' /boot/firmware/cmdline.txt
$ sudo sed -i -e"s/$/ zswap.zpool=z3fold/ /boot/firmware/cmdline.txt</pre><p style="text-align: left;">然后重新启动（你可以直接在终端输入 reboot）。</p><p style="text-align: left;">你可以通过使用grep搜索参数来检查这些变化是否正确。</p><pre>$ grep -R . /sys/module/zswap/parameters</pre><p style="text-align: left;">如果你的配置正确，那么输出应该是这样的。</p><pre>/sys/module/zswap/parameters/same_filled_pages_enabled:Y
/sys/module/zswap/parameters/enabled:Y
/sys/module/zswap/parameters/max_pool_percent:20
/sys/module/zswap/parameters/compressor:lz4
/sys/module/zswap/parameters/zpool:z3fold
/sys/module/zswap/parameters/accept_threshold_percent:90</pre><p style="text-align: left;">为Raspberry Pi上的Ubuntu桌面提升速度!</p><p style="text-align: left;">如果上面的<a data-link="1" href="https://c.duomai.com/track.php?k=iRyUSQzUycwRHdo1Ddm0DZpVXZmkDN2ITPklWYmYDO5IDNy0DZp9VZ0l2cmUmchdHdm92cGJTJjZkMl42Yu02bj5SZy9GdzRnZvN3byNWat5yd3dnRyU" target="_blank">教程</a>看起来有点复杂，不要担心。当Ubuntu 22.04在4月发布时，这些优化将被默认包含在所有Raspberry Pi 4设备中，包括400！但是，如果你真的做了这些改变，那么你就会发现，Ubuntu桌面的速度会变得更快。</p><p style="text-align: left;">不过，如果你真的做了这些改变，并在2GB的Raspberry Pi 4上进行了尝试，我们很想听听你的性能有多大提高。让我们知道你是否觉得它为2GB用户提供了高质量的Ubuntu桌面体验。</p>   
</div>
            