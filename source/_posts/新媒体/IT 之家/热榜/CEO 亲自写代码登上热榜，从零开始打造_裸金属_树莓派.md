
---
title: 'CEO 亲自写代码登上热榜，从零开始打造_裸金属_树莓派'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/10/a605415c-326a-4133-bf29-ed4f3606941b.png'
author: IT 之家
comments: false
date: Sun, 10 Oct 2021 04:52:13 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/10/a605415c-326a-4133-bf29-ed4f3606941b.png'
---

<div>   
<p data-vmark="9370">10 月 10 日消息 CEO 亲自写的代码是啥样？来自 RealVNC 公司的 CEO 说，自己常年当管理者，代码生疏了，所以决定重拾一下程序员工作，写一点树莓派的代码。</p><p data-vmark="07c8">结果，一不小心就上了技术论坛 Hacker News 热门。</p><p data-vmark="7090"><img src="https://img.ithome.com/newsuploadfiles/2021/10/a605415c-326a-4133-bf29-ed4f3606941b.png" w="1080" h="414" title="CEO 亲自写代码登上热榜，从零开始打造“裸金属”树莓派" width="1080" height="314" referrerpolicy="no-referrer"></p><p data-vmark="5b82">这串代码究竟是什么？打开这位 CEO 的 Twitter 一看，是一段小游戏。</p><p data-vmark="ca30"><img src="https://img.ithome.com/newsuploadfiles/2021/10/4b0d8f35-3bfa-4950-b045-8afe9c11ecf9.gif" w="640" h="376" title="CEO 亲自写代码登上热榜，从零开始打造“裸金属”树莓派" width="640" height="376" referrerpolicy="no-referrer"></p><h2 data-vmark="af10">花了一年时间就写了个这？当然不是，<span class="accentTextColor">这位 CEO 可是从零开始打造的这款游戏，连系统启动文件都是自己写的</span>。</h2><p data-vmark="d89f">通常我们使用树莓派都会在 SD 卡上刷写好操作系统，其实树莓派还能从零开始打造成一款“裸金属”（Bare Metal）计算机。</p><p data-vmark="594a"><img src="https://img.ithome.com/newsuploadfiles/2021/10/4abad0fc-a598-4907-9145-b69a7080661f.png" w="640" h="480" title="CEO 亲自写代码登上热榜，从零开始打造“裸金属”树莓派" width="640" height="480" referrerpolicy="no-referrer"></p><p data-vmark="aa64">所谓“裸金属”就是没有操作系统的计算机，直接在逻辑硬件上执行指令。这位 CEO 说，打造一个裸金属系统是他儿时的志向。</p><p data-vmark="276a">所以就有了这串，从零开始到成功运行 Hello World，再到运行小游戏的程序。</p><h2 data-vmark="94a8">从启动硬件到 Hello World</h2><p data-vmark="ff0d">目前，该项目已经完成了 12 章，<span class="accentTextColor">仍在 GitHub 上继续更新中</span>，截至今天已经收获了 1.6k 星。</p><p data-vmark="1e41"><img src="https://img.ithome.com/newsuploadfiles/2021/10/f16627b0-cd59-4532-af3d-b7ff7d7c679f.png" w="948" h="350" title="CEO 亲自写代码登上热榜，从零开始打造“裸金属”树莓派" width="948" height="303" referrerpolicy="no-referrer"></p><p data-vmark="0786">项目内容有：启动、构建基本代码、运行 HelloWorld、调用蓝牙声音硬件等。</p><p data-vmark="90e4">在编写代码之前先要准备树莓派 4 的周边硬件：HDMI 线、micro-SD 卡以及 USB 转 TTL 线。</p><p data-vmark="4982">由于编译过程是在电脑上进行，而程序是在树莓派上运行，因此还要在电脑上安装<span class="accentTextColor">交叉编译器</span>。</p><p data-vmark="a582">接下来开始引导树莓派启动：</p><p data-vmark="8335">树莓派 4 运行的第一个代码需要用汇编语言编写，之后由 C 语言来编写内核。</p><p data-vmark="f7be">写好启动代码后，再制作 makefile 文件进行交叉编译。</p><pre class="brush:javascript;toolbar:false">CFILES = $(wildcard *.c)
FILES = $(CFILES:.c=.o)
GCCFLAGS = -Wall -O2 -ffreestanding -nostdinc -nostdlib -nostartfiles
GCCPATH = ../../gcc-arm-10.3-2021.07-x86_64-aarch64-none-elf/bin
all: clean kernel8.img
boot.o: boot.S
$(GCCPATH)/aarch64-none-elf-gcc $(GCCFLAGS) -c boot.S -o boot.o
%.o: %.c
$(GCCPATH)/aarch64-none-elf-gcc $(GCCFLAGS) -c $< -o <a href="https://www.ithome.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="3b1f7b">[email protected]</a>
kernel8.img: boot.o $(OFILES)
$(GCCPATH)/aarch64-none-elf-ld -nostdlib boot.o $(OFILES) -T link.ld -o kernel8.elf
$(GCCPATH)/aarch64-none-elf-objcopy -O binary kernel8.elf kernel8.img
clean:
/bin/rm kernel8.elf .o .img > /dev/null 2> /dev/null || true</pre><p data-vmark="49a7">运行 make 后构建内核映像 kernel8.img，将镜像文件复制到 SD 卡中，这样就可以启动树莓派了。</p><p data-vmark="fdb6">不过树莓派在这一通操作后只能运行启动画面，之后只剩下一个空的黑屏。</p><p data-vmark="89ac">然后就是让树莓派程序员熟悉的“Hello World”程序，但是在一台黑屏的机器上如何运行呢？这就需要用到 UART 串行通信。</p><p data-vmark="35bf">刚刚准备的 USB 转 TTL 线这时候就派上了用场。</p><p data-vmark="509c">将 TTL 的 RX 引线（白色）链接到 GPIO 的 TXD 引脚上，TX 引线（绿色）链接到 GPIO 的 RXD 引脚上，地线（黑线）连接到 Ground 引脚上。</p><p data-vmark="fdf4"><img src="https://img.ithome.com/newsuploadfiles/2021/10/52e1e166-05ba-42bf-a6d4-e75ed85836e7.png" w="1080" h="620" title="CEO 亲自写代码登上热榜，从零开始打造“裸金属”树莓派" width="1080" height="471" referrerpolicy="no-referrer"></p><p data-vmark="ca92">电脑上还要安装 PuTTY，将链接方式选择为“Serial”，Speed 设置为 115200</p><p data-vmark="05f9"><img src="https://img.ithome.com/newsuploadfiles/2021/10/df6d4e7f-ffd2-4a4f-afd7-6e8e7bf9dc97.png" w="456" h="435" title="CEO 亲自写代码登上热榜，从零开始打造“裸金属”树莓派" width="456" height="435" referrerpolicy="no-referrer"></p><pre class="brush:javascript;toolbar:false ai-word-checked">#include“io.h”
void main()
&#123;
uart_init();
uart_writeText(“Hello world!\n”);
while (1);
&#125;</pre><p data-vmark="275d">这里的头文件 io.h 也不存在，需要自己定义。</p><p data-vmark="4da9">但是此时的树莓派还有没字体文件，也就是屏幕无法正常显示英文字母，也需要自定义。经过一系列操作后，这位 CEO 终于在屏幕上成功显示了“Hello world！”和几个几何图形。</p><p data-vmark="760f"><img src="https://img.ithome.com/newsuploadfiles/2021/10/0777f455-ac8d-4fee-ae6e-a0f4417ee5f1.png" w="1080" h="810" title="CEO 亲自写代码登上热榜，从零开始打造“裸金属”树莓派" width="1080" height="615" referrerpolicy="no-referrer"></p><p data-vmark="8193">编程并没有到此截止，这位 CEO 后面又实现了<span class="accentTextColor">蓝牙互传信息、播放音频文件等操作</span>。他还表示，项目还在持续更新中。</p><h2 data-vmark="f8a3">关于作者</h2><p data-vmark="006c">“裸金属”树莓派的作者 Adam Greenwood-Byrne 毕业于牛津大学，2009 年加入 RealVNC 担任销售经理，2018 年成为这家公司 CEO。</p><p data-vmark="420d"><img src="https://img.ithome.com/newsuploadfiles/2021/10/d71d81cc-0023-417e-a639-c36c282ab1d5.png" w="1080" h="439" title="CEO 亲自写代码登上热榜，从零开始打造“裸金属”树莓派" width="1080" height="333" referrerpolicy="no-referrer"></p><p data-vmark="d289">他的 GitHub 主页上目前只有一个项目，第一章内容是他在疫情隔离期间完成的，之后项目就处于休眠状态。</p><p data-vmark="c501"><img src="https://img.ithome.com/newsuploadfiles/2021/10/3eedd546-be4e-49a9-92e2-b45acbaef7a7.png" w="1080" h="279" title="CEO 亲自写代码登上热榜，从零开始打造“裸金属”树莓派" width="1080" height="212" referrerpolicy="no-referrer"></p><p data-vmark="5c6b">不过从今年的活跃度来看，他从今年开始又重拾了该项目，开始认真写代码了。</p><p data-vmark="520d">项目 GitHub 链接：<a href="https://github.com/isometimes/rpi4-osdev" target="_blank">点击打开</a></p>
          
</div>
            