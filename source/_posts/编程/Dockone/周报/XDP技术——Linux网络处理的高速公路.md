
---
title: 'XDP技术——Linux网络处理的高速公路'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211206/621a7bd575d4b39d8bd4f765b140f734.jpg'
author: Dockone
comments: false
date: 2021-12-08 04:10:34
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211206/621a7bd575d4b39d8bd4f765b140f734.jpg'
---

<div>   
<br><h3>XDP及相关技术简介</h3>传统的Linux内核网络协议栈由于更加注重通用性，其网络处理存在着固有的性能瓶颈，随着10G、25G、40G、100G甚至更高速率的网卡出现，这种性能瓶颈变得更加突出，传统内核网络协议栈已经难以满足高性能网络处理的要求。<br>
<br>在人们想办法提升处理性能的同时，一批人抱着它不行就绕开它的思路，在2010年，开发出了DPDK内核旁路（Kernel Bypass）技术，并逐渐成为网络处理加速的一种成熟方案。然而这种方案也有自己的一些固有缺陷，且始终是独立于linux内核的，在2016年的Linux Netdev会议上，David S. Miller更是带领听众一起高呼“DPDK is not Linux”。同年，伴随着eBPF技术的成熟，Linux也终于合入了属于自己的网络处理高速公路——XDP。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211206/621a7bd575d4b39d8bd4f765b140f734.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211206/621a7bd575d4b39d8bd4f765b140f734.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
XDP全称eXpress Data Path，即快速数据路径，XDP是Linux网络处理流程中的一个eBPF钩子，能够挂载eBPF程序，它能够在网络数据包到达网卡驱动层时对其进行处理，具有非常优秀的数据面处理性能，打通了Linux网络处理的高速公路。<br>
<br>运行的XDP程序可以通过XDP动作码来指定驱动对网络数据包的后续动作：<br>
<ul><li>XDP_ABORTED意味着程序错误，会将数据包丢掉，与XDP_DROP不同之处在于XDP_ABORTED会用trace_xdp_exception记录错误行为。</li><li>XDP_DROP会在网卡驱动层直接将该数据包丢掉，无需再进一步处理，也就是无需再耗费任何额外的资源。在收到DDoS攻击时，这种特性可以瓦解DDoS的根本目标——占满被攻击主机的CPU资源使得其他正常流量无法被处理，因为XDP丢包不会再动用额外的CPU资源。</li><li>XDP_PASS会将该数据包继续送往内核的网络协议栈，和传统的处理方式一致。这也使得XDP可以在有需要的时候方便地使用传统的内核协议栈进行处理。</li><li>XDP_TX会将该数据包从同一块网卡返回。</li><li>XDP_REDIRECT则是将数据包重定向到其他的网卡或CPU，结合AF_XDP可以将数据包直接送往用户空间。</li></ul><br>
<br>以上几种XDP动作码的组合，带来了多种应用可能。<br>
<br>XDP具有三种运行模式：<br>
<ul><li>原生模式：即驱动模式，在该模式下的XDP程序运行在网络驱动程序的早期路径，需要网卡驱动程序的支持，而10G及以上速率的大多数网卡基本都是支持的。</li><li>卸载模式：，该模式会直接将XDP程序卸载到网卡上，从而彻底释放主机CPU资源，相较于原生模式，具有更高的性能。目前支持的网卡似乎只有Netronome智能网卡。</li><li>通用模式：该模式下的XDP程序运行于驱动之后的位置，无需驱动支持，但性能较差，一般用于测试。</li></ul><br>
<br>上述提到的eBPF则是起源更早的一种技术：<br>
<br>1992年，BPF第一次在Berkeley实验室被提出，从名字可以看出来，最初BPF的功能就是用于包过滤的，我们平时所用的tcpdump就是基于eBPF实现的。2013年，BPF被加强，得到了eBPF，并在2014年正式并入Linux内核。通俗的来讲，eBPF提供了一种在各种内核和应用事件发生时运行一小段程序的机制。除去在XDP、TC等网络方面的应用，eBPF也用于性能监控、跟踪等多种场景。<br>
<br>到了2018年，Linux在4.18版本中也开通了属于自己的直达用户空间的高速公路——AF_XDP，合入了Linux内核，后续将持续对这条高速公路进行支持。AF_XDP是一种协议族(Address family)，指定socket通讯类型。通过XDP程序的redirect，我们可以将报文重定向到一块指定的用户态可读写的内存队列(UMEM)中，用户态的应用程序可以直接使用AF_XDP socket即XSK去接收数据，直接访问这块内存的数据包。<br>
<br>使用XDP技术进行快速的包处理具有如下优势：<br>
<ul><li>是Linux内核的一部分。这是一个长期的解决架构方案，由Linux内核社区维护，如同内核的其他部分，具有稳定的API，无需修改内核，无需增加额外的软件框架。</li><li>使用与内核协同，而非完全内核旁路的方式。XDP可重用所有Linux上游的网络工具和驱动，能够复用内核访问硬件的安全模型。而DPDK等技术则需要使用其专属的网络和安全工具。</li><li>安全性。由于eBPF验证器(verifier)的存在，一些不安全的指令会被内核拒绝加载。</li><li>无需独占CPU资源。即便是在空负载的情况下，DPDK也需要使用忙轮询来进行收包检查，分配的CPU核永远是打满的。而XDP可以始终运行，只有在负载升高时才会开始占用CPU。同时XDP程序也是可以运行在多个CPU之上的，这进一步提高了其性能。</li><li>动态注入。eBPF程序可以随时重新挂载和更新。</li><li>无需分配巨页。</li><li>适用性强。高于4.8版本的内核和绝大多数高速网卡都是支持XDP的，无需专有硬件的支持。</li><li>……</li></ul><br>
<br><h3>XDP技术的使用</h3>当前，XDP技术被OVS、Cilium、Polycube等用于网络快速路径的新选择，DPDK也做了AF_XDP PMD。<br>
<br>XDP程序在CPU可用来处理的最早时间点被执行，尤其适合DDoS防御、防火墙。<br>
<br>Cloudflare在他们的DDoS防御L4Drop中便利用了XDP，丢包规则将被转化为eBPF程序，并挂载到XDP钩子上，相比其他方案，无需用轮询独占CPU核，使用更低CPU资源的同时也能提供更加优秀的丢包性能，在云环境下，这种节省宝贵CPU资源的特性是非常吸引人的。<br>
<br>这种Linux的原生技术还在不断为网络处理带来新的思路。2019年，Sebastiano Miano等人使用XDP和TC钩子挂载eBPF程序实现了Linux的防火墙iptable，在规则数量提高的情况下提供相比原始iptable高数倍甚至数十倍的性能。2021年，Yoann Ghigoff等人更是基于eBPF和XDP、TC在内核中实现了一层Memcached的缓存，达到了比DPDK内核旁路方案还要高的性能。智能网卡也开始对eBPF卸载进行了支持，将包处理进一步从网卡驱动层卸载到了网卡，释放了更多的主机CPU资源，实现更高的性能。我们常用的虚拟交换机OVS的团队也在2.12.0版本就开始对AF_XDP进行探索，在2021年SIGCOMM会议上，发表了这些年他们对于数据面的探索，将AF_XDP选型用于其数据面，解决了很多DPDK解决不了的问题。其他的应用场景如负载均衡、流采样和监控……更多的可能正在被学术和工业界探索。<br>
<h3>结语</h3>作为另一个操作系统巨头，微软从原先“开源公敌”变为拥抱开源、拥抱linux，也在开始拥抱eBPF，ebpf-for-windows是微软的开源项目，用于在Windows 10和Windows Server 2016及以后的版本上运行eBPF，使得开发者可以用熟悉的eBPF工具链和API进行开发。可能不久的将来，Windows也会对eBPF、XDP技术作出更多支持。<br>
<br>XDP技术的发展只过了几年，AF_XDP正式合入内核更是不过三年的时间，但它是Linux内核社区长期维护的技术，具有足以媲美DPDK的性能，具备多种独有的优势。待未来更多优化被合入以后，必然是一种网络处理加速的重要技术。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/Bw1zV82-atVnA1Vz0noEyQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/Bw1zV82-atVnA1Vz0noEyQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            