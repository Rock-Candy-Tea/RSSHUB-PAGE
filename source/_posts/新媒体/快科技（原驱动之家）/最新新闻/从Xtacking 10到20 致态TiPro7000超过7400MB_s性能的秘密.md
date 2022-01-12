
---
title: '从Xtacking 1.0到2.0 致态TiPro7000超过7400MB_s性能的秘密'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220112/S7eae2cc8-590e-4bb7-9e17-6c9fa69ad60c.jpg'
author: 快科技（原驱动之家）
comments: false
date: Wed, 12 Jan 2022 08:37:33 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220112/S7eae2cc8-590e-4bb7-9e17-6c9fa69ad60c.jpg'
---

<div>   
<p>近段时间以来，致态TiPro7000的问世，再次引发了全行业关注，作为一家2016年堪堪成立，不到6年，却实现了从SATA到PCIe3.0，再到如今消费级固态硬盘巅峰PCIe4.0 SSD，全领域的产品布局，长江存储·致态背后的Xtacking?为何如此神奇？Xtacking技术究竟又有多少魔力？</p>
<p>根据官方解释，Xtacking?是长江存储核心专利和技术品牌，代表着长江存储在3D NAND存储技术领域的创新进取和卓越贡献，同时它也是长江存储面向企业客户、消费者推广3D NAND产品的关键所在，也是体现长江存储原创设计的代表品牌。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220112/7eae2cc8-590e-4bb7-9e17-6c9fa69ad60c.jpg" target="_blank"><img alt="从Xtacking 1.0到2.0 致态TiPro7000超过7400MB/s性能的秘密" h="450" src="https://img1.mydrivers.com/img/20220112/S7eae2cc8-590e-4bb7-9e17-6c9fa69ad60c.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
致态TiPro7000（1TB）</p>
<p>这个解释实质上有两重意思，一方面着重强调了Xtacking是一项核心的闪存制造技术，是长江存储近年来发展壮大的关键专利，另一方面则是揭示了Xtacking已然成为长江存储重要的品牌资产和代名词，有着非同凡响的象征意义。</p>
<p>今天，我们抛开品牌意义不聊，重点聊聊Xtacking?作为闪存制造技术，是如何推动致态TiPro7000的性能炸裂。</p>
<p><strong>01 主流NAND闪存制造逻辑</strong></p>
<p>在理解Xtacking?技术之前，我们需要先聊聊全球其他闪存厂是如何制造闪存的。</p>
<p style="text-align: center"><img alt="从Xtacking 1.0到2.0 致态TiPro7000超过7400MB/s性能的秘密" h="291" src="https://img1.mydrivers.com/img/20220112/c0ac3d26-3510-4af5-aa73-3b24dcc5214c.jpg" style="border: black 1px solid" w="599" referrerpolicy="no-referrer"><br>
图源于互联网</p>
<p>我们都知道现阶段全球NAND闪存玩家，主要有三星、铠侠/西数、Intel/Micron以及SK海力士等几家，其中铠侠和西数，intel和Micron，基于资本和市场共享机制，在这里可视为一家。</p>
<p>通过上图全球主流NAND闪存横截面可以看到，制造技术上，三星和铠侠/西数大体上保持一致，都是常规的并列式架构，这样的好处在于加工难度较低，但对于晶圆蚀刻设备与技术要求太高，尤其是三星采用的一次性加工、内存孔（Memory Hole）的HARC蚀刻技术，更是对于设备和操作经验要求极高；</p>
<p>铠侠/西数采用的则是相对轻松的两个48层堆叠而成，在技术难度上更具操作性，但也存在着内存孔的贴合匹配等问题。</p>
<p>Intel/Micron以及SK海力士，则采用了另一条制造路径，即CUA，CMOS under Array，顾名思义就是将能够控制数据读取、写入的CMOS线路放置在Array以下的一种加工方式，这样的架构同样存在制造工艺难度较高，优势则在于能够扩大单个芯片的存储密度。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220112/47a15051-1dd9-4402-b4cc-51ade08b6be9.jpg" target="_blank"><img alt="从Xtacking 1.0到2.0 致态TiPro7000超过7400MB/s性能的秘密" h="450" src="https://img1.mydrivers.com/img/20220112/S47a15051-1dd9-4402-b4cc-51ade08b6be9.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
Xtacking架构下的长存颗粒</p>
<p>至于YMTC即长江存储则是采用了Xtacking架构，该架构原理是将CMOS线路用一种不同于存储单元（Memory Cell）的晶圆制造而成，分别通过Bonding工艺进行贴合，更加朴素的解释便是等同于，在指甲盖大小的面积上通过数十亿根金属通道，将CMOS和Array进行连接，合二为一。</p>
<p><strong>02 Xtacking的先进性</strong></p>
<p>看到这里，大家应该能够脑补Xtacking?架构和传统上下并列，CUA等闪存结构的不同之处，那么耦合而成的Xtacking又有哪些特点呢？</p>
<p>从理论设计和实际经验来看，主要有更快的传输速度、更高的存储密度以及更灵活的开发周期。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220112/2643671f-acee-44ec-b208-ec0af7461fa1.jpg" target="_blank"><img alt="从Xtacking 1.0到2.0 致态TiPro7000超过7400MB/s性能的秘密" h="234" src="https://img1.mydrivers.com/img/20220112/S2643671f-acee-44ec-b208-ec0af7461fa1.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
Xtacking架构生产工艺</p>
<p>先说速度，Xtacking的制造原理是在两片独立的晶圆上，分别加工外围电路和存储单元，这样的话，可以在逻辑工艺上有着更多的自主选择性，从而让NAND获取更高的I/O接口速度及更多的操作功能，这也是致态TiPro7000能够取得超过7400MB/s的核心要义，从闪存制造的源头上，进行了性能优化，更多更高的I/O接口通道，为后续主控的性能调配奠定基础。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220112/4db5af91-e506-4344-a06c-3390c31f1cc8.jpg" target="_blank"><img alt="从Xtacking 1.0到2.0 致态TiPro7000超过7400MB/s性能的秘密" h="316" src="https://img1.mydrivers.com/img/20220112/S4db5af91-e506-4344-a06c-3390c31f1cc8.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
密度优化</p>
<p>再说密度，3D NAND颗粒最重要的发展方向便是密度的优化，在传统3D NAND架构中，外围电路约占芯片面积20~30%， Xtacking?技术创新的将外围电路置于存储单元之上，从而实现比传统3D NAND更高的存储密度，芯片面积可减少约25%，同等面积基础上，Xtacking?架构能够提供更多的存储单元。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220112/af8a8462-42e0-45e1-b206-17a90605c38f.jpg" target="_blank"><img alt="从Xtacking 1.0到2.0 致态TiPro7000超过7400MB/s性能的秘密" h="309" src="https://img1.mydrivers.com/img/20220112/Saf8a8462-42e0-45e1-b206-17a90605c38f.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
Xtacking工艺独立加工</p>
<p>最后再来看灵活的生产周期，实际上NAND颗粒的良品率和出货量，是目前市场竞争的重要一环，良品率方面，随着Xtacking 2.0技术的诞生，长江存储闪存颗粒的良品率已然实现大幅度跃升，能够满足现阶段长江存储客户的良品需求；</p>
<p>而出货量上，基于Xtacking工艺存储单元和外围电路的能够独立加工的特性，长江存储可以实现并行、模组化的灵活生产制造，根据推算Xtacking?工艺相较于传统结构，产品开发周期可缩短三个月，生产周期可缩短20%。</p>
<p><strong>03 不止于Xtacking? 致态TiPro7000强悍性能的秘密</strong></p>
<p>更快更高更灵活的Xtacking?架构，为致态TiPro7000奠定了旗舰级性能的基础，可我们都知道一款旗舰级固态硬盘，除开闪存颗粒，在主控的选配和硬件优化方面同样关键。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220112/35d91df9-ac4a-4ce2-9122-4b13316ad52e.jpg" target="_blank"><img alt="从Xtacking 1.0到2.0 致态TiPro7000超过7400MB/s性能的秘密" h="450" src="https://img1.mydrivers.com/img/20220112/S35d91df9-ac4a-4ce2-9122-4b13316ad52e.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
致态TiPro7000 SSD</p>
<p>致态TiPro7000内置了英韧科技IG5236主控，这是一款采用12nm FinFET CMOS制造工艺的PCIe4.0主控芯片，长江存储在该主控基础上，进行了固件的优化升级，历经长久的端到端的产品匹配，在充分挖掘该主控在GEN4协议上的潜能，并和Xtacking?2.0架构的长江存储高品质3D TLC颗粒进行校正和适配后，最终实现了性能的全部挖掘。</p>
<p style="text-align: center"><img alt="从Xtacking 1.0到2.0 致态TiPro7000超过7400MB/s性能的秘密" h="359" src="https://img1.mydrivers.com/img/20220112/a884c06c-c524-4a57-b815-85574d4ae8fd.jpg" style="border: black 1px solid" w="496" referrerpolicy="no-referrer"><br>
CrystalDiskMark测试</p>
<p>经过笔者实测，致态TiPro7000在最大顺序性能方面达到了GEN4行业的巅峰水准，最大连续读取7400MB/s，而最大连续写入也达到了5400MB/s，这一性能无论是对于游戏发烧友，还是存储负载较重的专业内容创作者，都能完全满足他们在硬盘带宽方面的性能需求。</p>
<p><strong>04 综述</strong></p>
<p>从Xtacking?技术的原理，我们可以发现，唯有打破常规，持续创新，才是推动产品革新，攀上巅峰的唯一要义。</p>
<p>作为一家年轻的存储公司，长江存储·致态是幸福，也是幸运的，不断迭代的Xtacking?技术，层出不穷的诸如致态TiPro7000优秀产品，都一一昭示着它们正在一条正确的道路上，前行着。</p>
<p>虽然正确的道路，往往是曲折的，泥泞的，甚至是充满危机的，但方向对了，其他不都是浮云了吗？</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/shancun.htm"><i>#</i>闪存</a><a href="https://news.mydrivers.com/tag/ssd.htm"><i>#</i>SSD</a><a href="https://news.mydrivers.com/tag/changjiangcunchu.htm"><i>#</i>长江存储</a></p>
<p class="url">
     <span>原文链接：<a href="https://diy.zol.com.cn/784/7845894.html">中关村在线</a></span>
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            