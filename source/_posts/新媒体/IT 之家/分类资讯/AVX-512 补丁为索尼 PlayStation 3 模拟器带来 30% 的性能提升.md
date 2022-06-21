
---
title: 'AVX-512 补丁为索尼 PlayStation 3 模拟器带来 30% 的性能提升'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/6/85ffbe21-dd37-41e0-b462-12b99214ca57.jpg'
author: IT 之家
comments: false
date: Mon, 20 Jun 2022 15:12:19 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/6/85ffbe21-dd37-41e0-b462-12b99214ca57.jpg'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D2056699" rel="nofollow">OC_Formula</a> 的线索投递！</div>
            <p data-vmark="1861"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 6 月 20 日消息，开源的多平台 PS3 模拟器 RPCS3 开发商 Whatcookie 发布了一个补丁，加入了 AVX-512 指令，使模拟器的性能提高了 30%。</p><p data-vmark="000d">众所周知，目前 AVX-512 指令对游戏还没有太大意义，但是对于模拟器来说很有意义，支持 AVX -512 硬件的大型寄存器文件、数据级并行性和 LLVM 编译器甚至可以创造奇迹。</p><p data-vmark="9ce9">Whatcookie 在他的博客文章中详细解释了 AVX-512 指令对 RPCS3 的意义。</p><p data-vmark="5863">“AVX-512 还增加了新的掩码寄存器，可以与 EVEX 编码指令一起使用，”Whatcookie 写道。</p><p data-vmark="6c2b">不管怎么说，30% 的性能提升是非常明显的，它对现有低功耗或旧平台的机器意义重大，而且 AMD 即将推出的 Ryzen 7000 处理器也将支持 AVX-512 指令集。</p><p data-vmark="82b7"><img src="https://img.ithome.com/newsuploadfiles/2022/6/85ffbe21-dd37-41e0-b462-12b99214ca57.jpg" w="320" h="180" alt="Sony and Microsoft Gaming Consoles" title="AVX-512 补丁为索尼 PlayStation 3 模拟器带来 30% 的性能提升" width="320" height="180" referrerpolicy="no-referrer"></p><p data-vmark="7cea">索尼 PS3 基于 Cell CPU，该 CPU 具有一个通用的 Power 核心和八个协同处理器 (SPEs)，但游戏行业对此并没有特别深的印象，毕竟 Cell 与 2006 年的传统处理器也是有着很大差异的。</p><p data-vmark="eca5">后来，英特尔 2013 年在 Xeon Phi 'Knights Landing' 超级计算机加速器中引入的 AVX-512 指令被添加到 Skylake-X 桌面处理器中 (以及相应的一代 Xeon Scalable)，为生产力平台带去一定的提升。</p><p data-vmark="5443">据悉，线程级和数据级并行 (SIMD) 非常适合高性能计算 (HPC)、数据中心、编码和加密工作负载，但游戏却很难利用它们，这也是为什么微软和索尼都是基于 x86 平台 (只有 AVX2，没有 AVX-512) 并采用传统的 Radeon GPU 架构的原因之一。</p>
          
</div>
            