
---
title: '运行个 Hello World 也能出 Bug？Python、Java、C++ 等 16 种语言中枪，最严重可导致文件丢失'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/3/5f45062e-2936-48ec-b0fc-4caecd46ded1.png'
author: IT 之家
comments: false
date: Mon, 21 Mar 2022 07:34:16 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/3/5f45062e-2936-48ec-b0fc-4caecd46ded1.png'
---

<div>   
<p data-vmark="f74b">一句最简单的 Hello World，居然也会出 Bug？</p><p data-vmark="a5e9">倒不是这句代码还能写错，而是运行时找到了许多操作系统对异常处理的漏洞。</p><p data-vmark="30c1">在向 <span class="accentTextColor">/dev/full</span> 输出结果，也就是设备空间不足、任何写入都应失败的情况下，C 语言依然返回了 0，成功退出：</p><pre>$ gcc hello.c -o hello
$ ./hello > /dev/full
$ echo $?
0</pre><p data-vmark="ef01">Bug 的最初发现者表示：这可不是一个小错误，本质上是“打印到标准输出”的任务。</p><p data-vmark="2510"><span class="accentTextColor">发生了错误但不抛出异常</span>，意味着即使出现数据丢失，进程依然会继续运行。</p><p data-vmark="9b72">于是他一不做二不休，又测试了 C++、Python、Java 等热门语言，发了篇博客，很快就在论坛盖起了高楼，讨论度直接爆了：</p><p data-vmark="ffa1" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/5f45062e-2936-48ec-b0fc-4caecd46ded1.png" w="1080" h="352" title="运行个 Hello World 也能出 Bug？Python、Java、C++ 等 16 种语言中枪，最严重可导致文件丢失" width="1080" height="267" referrerpolicy="no-referrer"></p><p data-vmark="d2c0">而评论区网友一通 Debug，综合整理下来，踩中这一 Bug 的语言，竟足足有 <span class="accentTextColor">16 种</span>之多！</p><p data-vmark="d39d" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/c48f6756-be03-494c-80a0-ee662aa74702.png" w="1080" h="911" title="运行个 Hello World 也能出 Bug？Python、Java、C++ 等 16 种语言中枪，最严重可导致文件丢失" width="1080" height="692" referrerpolicy="no-referrer"></p><h2 data-vmark="d3cb">Hello World 的 DeBug 过程</h2><p data-vmark="1ffc">最初的发现者是一名名叫 sunfishcode 的技术博主，他在博客里展示了 C 和 Python 两种语言的详细的 deBug 过程。</p><p data-vmark="0011">主要使用的是 Linux 系统下的一个经典的设备文件，/dev/ full。</p><p data-vmark="2492">/dev/ full 总是在写入时返回设备无剩余空间（错误码为 ENOSPC），常常用于测试程序能否正确处理 I / O 错误。</p><p data-vmark="15c5">如果程序正常，那么就会返回错误报告：</p><pre>$ echo "Hello World!" > /dev/full
bash: echo: write error: No space left on device
$ echo $?
1</pre><p data-vmark="0e1a">而正如我们开头所示的代码，在用 C 语言进行输出时，hello 程序却报告成功，返回了 0。</p><p data-vmark="387f">用 strace 命令跟踪这一进程产生的系统调用可以发现，程序确实出现了故障：</p><pre>$ strace -etrace=write ./hello > /dev/full
write(1, "Hello World!\n", 13)          = -1 ENOSPC (No space left on device)
+++ exited with 0 +++</pre><p data-vmark="1501">而以“错误不该被悄悄传递”为口号的 Python 也着了道。</p><p data-vmark="c008">程序向 stderr 打印了一条消息，丢失了信息，但最后也返回了 0：</p><pre>$ python2 hello.py > /dev/full
close failed in file object destructor:
sys.excepthook is missing
lost sys.stderr
$ echo $?
0</pre><p data-vmark="ac6c">这个 Bug 严重吗？现实世界任何一个程序都不会拿 Hello World 当作关键性安全问题，但“打印到标准输出”却是现实中确实会有的程序任务。</p><p data-vmark="b4cc">而这也正是 Hello World 这个最简单的程序的本质。</p><p data-vmark="7775">博主 sunfishcode 这样说：</p><blockquote><p data-vmark="8143">标准输出可能意味着一个具体文件，那么如果这个文件刚好耗尽了空间，程序又因为 Bug 没有检测到这一错误呢？</p><p data-vmark="a442">父进程不会知道子进程失败了，只会继续运行。但期望生成的输出实际上已经丢失了数据。</p></blockquote><p data-vmark="b716">当然，博主在最后也给出了没有踩雷的语言列表：</p><p data-vmark="5a82" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/decbeb15-d332-4190-bf5c-532aa7e9ec07.png" w="1080" h="862" title="运行个 Hello World 也能出 Bug？Python、Java、C++ 等 16 种语言中枪，最严重可导致文件丢失" width="1080" height="654" referrerpolicy="no-referrer"></p><h2 data-vmark="3ed5">网友热议：这到底算不算 Bug？</h2><p data-vmark="9d88">目前，博主已经针对这一 Bug 给出了一些解决方案，比如在 C 语言环境中可以采用这样的方法：</p><pre>#include <stdio.h>
#include <stdlib.h>

int main(void) &#123;
    printf("Hello, World!\n");

    if (fflush(stdout) != 0 || ferror(stdout) != 0) &#123;
        return EXIT_FAILURE;
    &#125;

    return EXIT_SUCCESS;
&#125;</pre><p data-vmark="003e">而评论区也贡献了 Java 环境中的解决方案，即添加一个方法来获得底层的、未包装的 OutputStream：</p><pre>System.out.println("Hello World!");
    if (System.out.checkError()) throw new IOException();</pre><p data-vmark="91f2">下方还有人补充到，Java 已经引入的 RuntimeIOException 就可以用于 I / O 异常出现意外的情况：</p><blockquote><p data-vmark="0d00">因此我们可以引入一个新的类，比如 ErrorCheckingPrintStream，并将“ErrorCheckingPrintStream withErrorChecks ()”方法添加到 PrintStream 中。</p></blockquote><p data-vmark="5dbe" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/17008d87-fc41-4c98-90ed-19d2da3267f5.jpg@s_2,w_820,h_607" w="1080" h="799" title="运行个 Hello World 也能出 Bug？Python、Java、C++ 等 16 种语言中枪，最严重可导致文件丢失" srcset="https://img.ithome.com/newsuploadfiles/2022/3/17008d87-fc41-4c98-90ed-19d2da3267f5.jpg 2x" width="1080" height="607" referrerpolicy="no-referrer"></p><p data-vmark="81bf">而除此之外，评论区热议的一个话题就是：</p><p data-vmark="42da">这位博主所公布的问题到底算不算是一个 Bug？</p><p data-vmark="2f7e">反对者直言作者是在标题党，还以为是发现了什么 C 语言标准库里的 Bug，但实际上只是处理所有可能的系统调用的失败情况：</p><blockquote><p data-vmark="c3bf">Hello World 只是简单地将 API 调用到文本界面，对一个简单的接口进行调用，我在那里没有发现过任何 Bug。</p></blockquote><p data-vmark="37e9" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/3a7c44e5-37d5-4ffd-8b62-30cab72eed7d.png" w="1080" h="699" title="运行个 Hello World 也能出 Bug？Python、Java、C++ 等 16 种语言中枪，最严重可导致文件丢失" width="1080" height="531" referrerpolicy="no-referrer"></p><p data-vmark="506e">有赞同的评论在下方做了进一步的补充，他认为 C 语言的编写方式里本来就写明：程序不关心任何形式的错误条件。</p><p data-vmark="25e3">包括 printf 的返回值被忽略、输出不被刷新、刷新的返回不被检查、不关心 errno 值等等。</p><p data-vmark="9f9b">所以，用户本就不应该期望给定的系统调用返回额外的 errno 值，而是应该用特殊方法处理特殊情况。</p><p data-vmark="9de1">甚至有人表示：程序的失败不是由程序控制结构定义，而是由需求定义，Hello World 程序的需求难道包括主机系统的所有错误边界吗？</p><p data-vmark="b05c">也有人更赞同作者，认为 Hello World 不只是接口调用，实际是在要求操作系统在某处写入数据，而这正是简单的程序与现实世界相关联的地方：</p><p data-vmark="ae3d">这是一个严重的问题，而似乎在大多数时候，这种看似简单的功能中存在的大量复杂性都被忽略了。</p><p data-vmark="809d" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/d65607de-133b-49f7-bf85-c4147324fa51.jpg@s_2,w_820,h_358" w="1080" h="471" title="运行个 Hello World 也能出 Bug？Python、Java、C++ 等 16 种语言中枪，最严重可导致文件丢失" srcset="https://img.ithome.com/newsuploadfiles/2022/3/d65607de-133b-49f7-bf85-c4147324fa51.jpg 2x" width="1080" height="358" referrerpolicy="no-referrer"></p><p data-vmark="3aa0">还有另辟蹊径，从教育的角度来看的评论：</p><p data-vmark="7dba">毕竟 C 语言时很多程序员的入门语言，hello.c 又是其中的第一个程序，要让初学者更好地理解控制结构，块，返回值，缓冲流的，printf 格式化语言等概念，所以还是把它当成一个 Bug 吧。</p><p data-vmark="e1b6">那么你又怎么看？</p><p data-vmark="2f11"><strong>参考链接：</strong></p><p data-vmark="8f27">[1]<span class="link-text-start-with-http">https://blog.sunfishcode.online/Bugs-in-hello-world/</span></p><p data-vmark="e116">[2]<span class="link-text-start-with-http">https://news.ycombinator.com/item?id=30611367</span></p><p data-vmark="46fe">[3]<span class="link-text-start-with-http">https://github.com/sunfishcode/hello-world-vs-io-errors</span></p>
          
</div>
            