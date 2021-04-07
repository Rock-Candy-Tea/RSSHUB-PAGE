
---
title: 'C 和 C++ 不安全？Android 支持 Rust 开发操作系统'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210407/v2_364fed9b63f54a08bff17aad26f46a20_img_000'
author: 36kr
comments: false
date: Wed, 07 Apr 2021 12:07:18 GMT
thumbnail: 'https://img.36krcdn.com/20210407/v2_364fed9b63f54a08bff17aad26f46a20_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/HzYfLR8wCSrbhYSy9puZqw">“CSDN”（ID:CSDNnews）</a>，作者：Carol，36氪经授权发布。</p> 
<p>Rust这两年实火了。</p> 
<p>近年来，Rust凭借着出色的内存效率、速度与安全性，深受亚马逊、微软、<a class="project-link" data-id="25167" data-name="华为" data-logo="https://img.36krcdn.com/20200729/v2_7c7826d711824e758a8e1511c9d7eecc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25167" target="_blank">华为</a>、Facebook等科技巨头的青睐。Rust从根本上考虑安全性，提出了“没有数据竞争的并发性”、“没有垃圾收集的内存安全”及最终的“无恐惧的黑客“等概念，反映了Rust独特的学术研究和工业实用性结合价值。除了企业使用Rust语言的场景逐步扩大，操作系统也不例外。</p> 
<p>而作为一个完善的移动操作系统，Android系统涉及到很多组件，可以广义地概括为两部分：生态系统及操作系统本身。</p> 
<p>作为开发者来说，你开发Android的哪个部分决定了你所选择的编程语言；对于应用开发者来说，Java和Kotlin是比较流行的选择；而对于操作系统及其内部底层的开发者来说，C语言和C++语言是目前更受欢迎的选项。</p> 
<p>如今，谷歌为操作系统开发者增加了第3个选择：Rust。因为Android Open Source Project现在支持Rust语言来开发操作系统了。</p> 
<p><img src="https://img.36krcdn.com/20210407/v2_364fed9b63f54a08bff17aad26f46a20_img_000" data-img-size-val="724,1024" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题">C和C++有哪些限制？</h2> 
<p>Android系统的底层需要C和C++这样的系统编程语言，因为这类语言可以为开发者提供控制和可预测性，这在访问底层系统资源和硬件时非常重要。</p> 
<p>但问题是，C和C++并不能提供内存安全保证。这样一来使它们很容易出现错误和安全漏洞，开发者需要在复杂和多线程的代码库中管理这些语言的内存寿命，并非一件易事。</p> 
<p>C和C++构成了Android平台上数千万行代码，这使得一旦发生内存安全漏洞，就形成最难以解决的代码错误来源，占Android高严重度安全漏洞的70%左右。所以与其事后再解决这些Bug，不如从一开始就预防。</p> 
<p>因为缺乏内存安全保障，迫使开发者在严格约束和无权限沙盒内运行Android进程。但使用沙盒是成本很高的，不仅会消耗额外的开销还会引起延迟，并且不能完全消除代码的漏洞，而且由于Bug密度高，沙盒的有效性降低了，这样的情况让攻击者可以将多个漏洞连接起来。</p> 
<p>缺乏内存安全保障迫使开发者在严格受限和无特权的沙箱中运行Android进程。但是沙箱在资源上是昂贵的，消耗额外的开销并引入延迟。沙箱也没有完全消除代码的漏洞，而且由于漏洞密度高，沙箱的有效性降低了，进一步允许攻击者将多个漏洞链接起来。</p> 
<p>另一方面的限制是，为了检测到错误状态，必须在工具化的代码中实际触发才能被检测到。因此即使你的代码经过了严密的测试，也可能发现不了隐藏的Bug。而等到发现Bug的时候，修复他们又是一个漫长而高成本的过程了，而且还不一定能<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>最准确的修复。</p> 
<p>这导致Bug的检测变得很不可靠，鉴于这些限制，事前预防Bug是最好的方法。针对这些问题，Rust这样的语言就到了发挥的时候了。</p> 
<h2 label="一级标题">从C和C++转向Rust，对Android意味着什么?</h2> 
<p>为Android系统增加一种新语言，实际上是一项很艰巨的任务，包括工具链和依赖项需要维护、测试基础设施和工具必须更新、开发人员需要接受培训等。不过在谷歌方面，最近一年多时间里已经一直在大力推广Rust了。</p> 
<p>在谷歌看来，想要预防非安全语言编写软件的Bug，现在是内存安全编程语言切入的好时机。因为谷歌已经在其免费OSS-Fuzz服务的375个开源项目里发现了由内存安全错误引起的5500多个漏洞；还发布了Syzkaller来监测操作系统内核中的Bug，并通过gVisor等沙盒来减少Bug检测期间造成的实际影响。</p> 
<p>在使用Rust方面，谷歌用Rust将Android中的操作系统模块进行了优化，包括蓝牙和Keystore2.0，Keystore 2.0模块就是用Rust编写的；在底层的项目中使用Rust，如ChromeOS中的crosvm虚拟机监视器和驱动程序；包括curl的HTTP和TLS后端、以及Apache httpd新的TLS库，这些代码库位于Internet的网关，需要保护全球数百万用户的数据，它们的安全性极其重要。所以这些作为相关工作重要起点的代码库，均已开始接受Rust语言改造。</p> 
<p>虽然目标已经定下了，但谷歌方面也很明确，真正将Rust扩展到更多的操作系统，需要很多年的时间。</p> 
<p>而对于应用开发者来说，这样的切换不会改变其编写应用的方式，也不会改变框架API的工作方式，只是会影响操作系统的编写方式。根据Android开发者团队透露，谷歌目前也没有发布Rust NDK的计划，支持应用程序开发的语言还继续是Kotlin、Java、C和C++。</p> 
<h2></h2>  
</div>
            