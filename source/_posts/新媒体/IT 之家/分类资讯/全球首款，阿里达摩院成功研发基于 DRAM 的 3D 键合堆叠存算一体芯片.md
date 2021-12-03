
---
title: '全球首款，阿里达摩院成功研发基于 DRAM 的 3D 键合堆叠存算一体芯片'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/12/e06f96d8-1d4f-45bc-9178-7b92d1589c7d.jpg@s_2,w_820,h_548'
author: IT 之家
comments: false
date: Fri, 03 Dec 2021 05:50:36 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/12/e06f96d8-1d4f-45bc-9178-7b92d1589c7d.jpg@s_2,w_820,h_548'
---

<div>   
<p data-vmark="a310"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 12 月 3 日消息，据阿里云官方发布，阿里达摩院成功研发存算一体芯片。这是全球首款基于 DRAM 的 3D 键合堆叠存算一体芯片。它可突破冯・诺依曼架构的性能瓶颈，满足人工智能等场景对高带宽、高容量内存和极致算力的需求。在特定 AI 场景中，该芯片性能提升 10 倍以上，效能比提升高达 300 倍。</p><p data-vmark="fcc1"><img src="https://img.ithome.com/newsuploadfiles/2021/12/e06f96d8-1d4f-45bc-9178-7b92d1589c7d.jpg@s_2,w_820,h_548" w="1019" h="681" title="全球首款，阿里达摩院成功研发基于 DRAM 的 3D 键合堆叠存算一体芯片" srcset="https://img.ithome.com/newsuploadfiles/2021/12/e06f96d8-1d4f-45bc-9178-7b92d1589c7d.jpg 2x" width="1019" height="548" referrerpolicy="no-referrer"></p><h3 data-vmark="3990">为什么要研发存算一体芯片？</h3><p data-vmark="2893">随着人工智能应用场景的爆发，现有的计算机系统架构的短板逐渐显露，例如功耗墙、性能墙、内存墙等问题。</p><p data-vmark="3053">其主要症结在于：</p><p data-vmark="4395">一是数据搬运带来了巨大的能量消耗。在传统架构下，数据从内存单元传输到计算单元需要的功耗是计算本身的约 200 倍，因此真正用于计算的能耗和时间占比很低。</p><p data-vmark="ba03">二是内存的发展远远滞后于处理器的发展。目前，处理器的算力以每两年 3.1 倍的速度增长，而内存的性能每两年只有 1.4 倍的提升。后者的性能极大地影响了数据传输的速度，这也被认为是传统计算机的阿克琉斯之踵。</p><p data-vmark="bce2"><img src="https://img.ithome.com/newsuploadfiles/2021/12/71d6f24a-c70b-4980-a0ff-884bb8b31d2a.png" w="997" h="523" title="全球首款，阿里达摩院成功研发基于 DRAM 的 3D 键合堆叠存算一体芯片" width="997" height="430" referrerpolicy="no-referrer"></p><p data-vmark="66d9">存算一体芯片是目前解决以上问题的最佳途径 —— 它类似于人脑，将数据存储单元和计算单元融合为一体，大幅减少数据搬运，从而极大提高计算并行度和能效。</p><p data-vmark="1763">这一技术早在 90 年代就被提出，但受限于技术的复杂度、高昂的设计成本以及应用场景的匮乏，过去几十年业界对存算一体芯片的研究进展缓慢。如今，达摩院希望通过自研创新技术解决算力瓶颈这一业界难题。</p><p data-vmark="8b5d">此外，存算一体芯片在终端、边缘端以及云端都有广阔的应用前景。例如 VR/AR、无人驾驶、天文数据计算、遥感影像数据分析等场景中，存算一体芯片都可以发挥高带宽、低功耗的优势。</p><p data-vmark="15f0">从长远来看，存算一体技术还将成为类脑计算的关键技术。</p><h3 data-vmark="867e">实现存算一体的三种路线</h3><p data-vmark="0f70">实现存算一体有三种技术路线：</p><ul class=" list-paddingleft-2"><li><p data-vmark="b073">近存储计算（Processing Near Memory）：计算操作由位于存储芯片外部的独立计算芯片完成。</p></li><li><p data-vmark="0bbe">内存储计算（Processing In Memory）：计算操作由位于存储芯片内部的独立计算单元完成，存储单元和计算单元相互独立存在。</p></li><li><p data-vmark="43f6">内存执行计算（Processing With Memory）：存储芯片内部的存储单元完成计算操作，存储单元和计算单元完全融合，没有一个独立的计算单元。</p></li></ul><p data-vmark="ed34">其中，近存计算通过将计算资源和存储资源距离拉近，实现对能效和性能的大幅度提升，被认为是现阶段解决内存墙问题的最佳途径。达摩院本次也是沿着这一方向进行突破。</p><h3 data-vmark="d814">混合键合 3D 堆叠技术</h3><p data-vmark="87a6">为了拉近计算资源和存储资源的距离，达摩院计算技术实验室创新性采用混合键合 (Hybrid Bonding) 的 3D 堆叠技术进行芯片封装 —— 将计算芯片和存储芯片 face-to-face 地用特定金属材质和工艺进行互联。</p><p data-vmark="83ef">比起业内常见的封装方案 HBM，混合键合 3D 堆叠技术拥有高带宽、低成本等特点，被认为是低功耗近存计算的完美载体之一。</p><p data-vmark="8b9e"><img src="https://img.ithome.com/newsuploadfiles/2021/12/4db04782-4867-4fa2-80ce-3b0a070d125b.png" w="1080" h="617" title="全球首款，阿里达摩院成功研发基于 DRAM 的 3D 键合堆叠存算一体芯片" width="1080" height="468" referrerpolicy="no-referrer"></p><p data-vmark="350b">此外，内存单元采用异质集成嵌入式 DRAM ，拥有超大内存容量和超大带宽优势。</p><p data-vmark="a826">IT之家获悉，在计算芯片方面，达摩院研发设计了流式的定制化加速器架构，对推荐系统进行“端到端”加速，包括匹配、粗排序、神经网络计算、细排序等任务。</p><p data-vmark="2b29">这种近存架构有效解决了带宽受限的问题，最终内存、算法以及计算模块的完美融合，大幅提升带宽的同时还实现了超低功耗，展示了近存计算在数据中心场景的潜力。</p><p data-vmark="3a3c">达摩院表示，最终的测试芯片显示，这种存算技术和架构的优势明显：</p><blockquote><p data-vmark="94f6">能通过拉近存储单元与计算单元的距离增加带宽，降低数据搬运的代价，缓解由于数据搬运产生的瓶颈，而且与数据中心的推荐系统对于带宽/内存的需求完美匹配。</p></blockquote><p data-vmark="a982">该芯片的研究成果已被芯片领域顶级会议 ISSCC 2022 收录。未来，达摩院希望能进一步攻克存内计算技术，并逐步优化典型应用、生态系统等方面。</p>
          
</div>
            