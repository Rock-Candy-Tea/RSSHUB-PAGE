
---
title: 'Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220701/S99f608ef-9d7d-4e17-96dc-f28b52d72a19.png'
author: 快科技（原驱动之家）
comments: false
date: Fri, 01 Jul 2022 19:59:50 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220701/S99f608ef-9d7d-4e17-96dc-f28b52d72a19.png'
---

<div>   
<p>作为移动芯片领域的王者，Arm每年都会带来新的CPU、GPU、互连技术方案，近日就奉上了全新的Arm TCS22，也就是2022年全面计算解决方案，包括一系列IP组合。</p>
<p>CPU方面是<strong>全新旗舰超大核心Cortex-X3、大核心Cortex-A715，以及升级版小核心Cortex-A510(名字没变)。</strong></p>
<p>GPU方面是<strong>首次支持硬件光线追踪的旗舰级Immotalis-G715、高端的Mali-G715、高端的Mali-G615。</strong></p>
<p>互连方面则是升级版的DSU-110。</p>
<p>接下来，我们就分别看看都有哪些变化。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/99f608ef-9d7d-4e17-96dc-f28b52d72a19.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="314" src="https://img1.mydrivers.com/img/20220701/S99f608ef-9d7d-4e17-96dc-f28b52d72a19.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>【CPU：超大核性能提升25％、三种核心组合更灵活】</strong></p>
<p>2021年3月底，Arm正式发布了全新的Armv9指令集，号称10年最重要的创新、面向未来10年移动计算的基石。</p>
<p>Armv9重点增强矢量计算(SEV2指令集)、机器学习、数字信号处理，强化安全性，并继续提升性能，号称IPC性能未来两代提升会超过30％。</p>
<p>当然，它完全向下兼容Armv8。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/743510f1-3fb7-45d2-a697-30d537c4aa7e.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="294" src="https://img1.mydrivers.com/img/20220701/S743510f1-3fb7-45d2-a697-30d537c4aa7e.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>Armv9指令集的Cortex-X2超大核心已经在骁龙8/骁龙8+、天玑9000/天玑9000+等旗舰移动处理器中得到应用，这次发布的是新一代Cortex-X3。</p>
<p>Cortex-X3在架构设计上的变化相当深入、广泛，比如解码器每周期指令从5个增加到6个，乱序执行窗口从288个增加到320个， ALU整数算数单元从4个增加到6个，二级缓存容量从512KB翻番到1MB，并且不再支持32位指令集。</p>
<p><span style="color:#000000;">性能方面，</span><span style="color:#ff0000;"><strong>3.3GHz频率、1MB二级缓存、8MB三级缓存的配置下，与基于Cortex-X2的安卓旗舰处理器对比，提升最多25％。</strong></span></p>
<p><span style="color:#ff0000;"><strong>3.6GHz频率、1MB二级缓存、16MB三级缓存的配置下，与主流笔记本处理器(Intel i7-1260p)相比，单核性能高出最多34％。</strong></span></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/e7687627-84c0-4204-839e-b9c6f0534a76.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="337" src="https://img1.mydrivers.com/img/20220701/Se7687627-84c0-4204-839e-b9c6f0534a76.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>Cortex-A715注重性能与能效的平衡，对比去年的Cortex-A710，在同等性能下能效提升最多20％，而在同等功耗下性能提升最多5％。</strong></p>
<p>同时，<strong>它已经达到了上上代超大核Cortex-X1的性能水准。</strong></p>
<p>对了，A710也仅支持64位指令集。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/0bd87948-8623-495c-990c-db7f27585558.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="333" src="https://img1.mydrivers.com/img/20220701/S0bd87948-8623-495c-990c-db7f27585558.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>Cortex-A510名字没变，性能也没变，不过能效提升了5％</strong>，应该是与更新制造工艺结合的效果。</p>
<p>同时，<strong>它也是唯一保留32位指令集支持的核心。</strong>如果一款App还没有升级到64位，今后只能依赖小核心执行，效率必然大打折扣。</p>
<p>Arm也是意在通过此举推动行业向64位加速转型。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/09a7d03a-9124-47c4-a75e-d4da958aa291.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="334" src="https://img1.mydrivers.com/img/20220701/S09a7d03a-9124-47c4-a75e-d4da958aa291.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>另外，<strong>DSU-110互连单元也更加强大灵活，支持核心数量增加50％，比如Cortex-X3可以最多12核心、16MB三级缓存，还支持更多指令集。</strong></p>
<p>big.LITTLE大小核的组合也更加灵活、丰富，同样1+3+4，X3+A715+A510的组合比去年的X2+A710+A510性能可提升12％。</p>
<p>1+4+4则可比1+3+4性能提升最多21％，2+2+4可提升最多23％，<span style="color:#ff0000;"><strong>还首次加入了8+4+0这样的组合，面向中高端笔记本，性能高出足足120％。</strong></span></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/284155a8-4358-4d30-be85-d4042bf0aa22.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="334" src="https://img1.mydrivers.com/img/20220701/S284155a8-4358-4d30-be85-d4042bf0aa22.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>总体而言，Cortex CPU今年的升级比较中规中矩。X3、A715都是预料之中的对位升级，A510本身几乎毫无变化。</p>
<p>但是，<strong>结合新的DSU-10互连单元，三种核心的配置更加灵活多变，可满足不同设备、应用场景的不同需求，包括在笔记本领域继续竞争Intel、AMD x86双雄。</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/4f7a71a3-eb44-408c-bac4-f9a18c31adcc.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="316" src="https://img1.mydrivers.com/img/20220701/S4f7a71a3-eb44-408c-bac4-f9a18c31adcc.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/9807cbe1-a5c2-4298-a691-48167a5b9a06.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="335" src="https://img1.mydrivers.com/img/20220701/S9807cbe1-a5c2-4298-a691-48167a5b9a06.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>【GPU：首次迎来硬件光追 名字都变了】</strong></p>
<p>Arm Mali GPU凭借与Cortex CPU的整合优化、持续不断的迭代升级，已经成为移动行业的绝对主流，出货量全球领先，累计已超80亿。</p>
<p><span style="color:#ff0000;"><strong>这一次，Arm GPU迎来了一次超级变脸，旗舰型号放弃了Mali的传统名字，改成了全新的“Immortalis”，首款型号“Immortalis-G715”。</strong></span></p>
<p>之所以改名，首要原因就是<strong>第一次支持基于硬件的光线追踪</strong>，和NVIDIA、AMD、Intel的高性能显卡一样进入了光追时代。</p>
<p>当然，Arm GPU不是第一个支持光追的移动端产品，Imagination此前已经做到，但是两家的影响力不可同日而语，Imagination的光追方案时至今日仍然没有落地。</p>
<p>其实，<strong>去年的Mali-G710已经支持软件光追</strong>，联发科天玑9000就开启了这一功能，并用在了OPPO Find X5 Pro天玑版手机中，今年则升级为硬件光追。</p>
<p>当然，光线追踪非常消耗硬件和软件资源，一般也会大大增加功耗，不过Arm宣称，<span style="color:#ff0000;"><strong>Immortalis-G715的光追单元只占用了大约4％的着色器核心面积，而且功耗非常低，就带来了超过3倍的性能提升(对比软件光追)。</strong></span></p>
<p>以下是Arm官方给出的光追效果对比图，右半部分为开启光追，可以看到丰富、清晰的反射、阴影，与非光追不可同日而语。</p>
<p>当然，无论是性能、功耗、效果，都还有待实际考验。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/18fc1944-38b7-4517-ab47-e35f5c91c2bb.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="299" src="https://img1.mydrivers.com/img/20220701/S18fc1944-38b7-4517-ab47-e35f5c91c2bb.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/8e58d910-573a-4ef5-9214-89654fbd35db.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="297" src="https://img1.mydrivers.com/img/20220701/S8e58d910-573a-4ef5-9214-89654fbd35db.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>VRS可变刷新率也成了标配</strong>，同样追上了NVIDIA、AMD、Intel的脚步。</p>
<p>该技术隶属于DX12范畴，简单地说可在单个帧画面内改变着色速率，选择性地降低画面部分区域的细节水平(被遮挡/画面边缘等)，从而在几乎不影响画质的情况下，提升图形性能。</p>
<p>Arm展示了VRS在腾讯《王者荣耀》中的效果，<strong>原画面和VRS画面几乎看不出任何区别，而在性能上，官方号称可将帧率提升最多达40％。</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/33d61051-badb-4a13-a8cb-0178c2584ba8.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="613" src="https://img1.mydrivers.com/img/20220701/S33d61051-badb-4a13-a8cb-0178c2584ba8.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>回到常规层面，Immotalis-G715的提升也非常可观，官方号称<strong>对比上代Mali-G710同等功耗下性能提升最多15％，机器学习性能直接翻番，而在同等性能下能效可提升最多15％。</strong></p>
<p>它可以配置<strong>10-16个核心。</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/202dbc85-023b-42e9-8e01-d7d97946f1cb.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="310" src="https://img1.mydrivers.com/img/20220701/S202dbc85-023b-42e9-8e01-d7d97946f1cb.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>另外，Arm对执行引擎也做了全方位增强，主要有三个方面：</p>
<p>一是重新设计转换模块，大大缩小占用面积。</p>
<p>二是升级乘积累加运算(FMA)，模块数量翻番，进一步提升性能和能效。</p>
<p>三是支持矩阵乘法指令(Matrix Multiply)，可提升计算摄影、图像增强的效率，这也是机器学习性能翻倍的主要来源。</p>
<p>其他方面，指令流前端(Command Stream Frontend)、层次细节(LOD)、固定率压缩(AFRC)等技术都得到了升级。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/d82efabe-6312-4c5b-938c-32cfbf029a40.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="310" src="https://img1.mydrivers.com/img/20220701/Sd82efabe-6312-4c5b-938c-32cfbf029a40.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>同时，Arm 也发布了<strong>高端的Mali-G715 GPU(是的编号一样)，没有光追，能效提升15％，可配置7-9个核心。</strong></p>
<p>还有<strong>高端的Mali-G615，可配置最多6个核心。</strong></p>
<p>它们俩也都支持VRS可变刷新率，这已经是Arm GPU的标配，同时也升级了执行引擎。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/87b48593-d5bc-47cc-9e25-6588a65bc9a7.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="292" src="https://img1.mydrivers.com/img/20220701/S87b48593-d5bc-47cc-9e25-6588a65bc9a7.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>总体而言，Arm GPU今年的变化比较极端，新引入的顶级核心Immortalis-G715整体焕然一新，性能提升明显，尤其是将开启手游的光追新时代。</p>
<p>Mali-G715、G615的亮点则在于普及了VRS。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/10065d31-2eb2-4987-996d-195c33970d5f.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="314" src="https://img1.mydrivers.com/img/20220701/S10065d31-2eb2-4987-996d-195c33970d5f.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/5b5ccdd5-12ba-47a8-93dd-e7fec7bd5145.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="296" src="https://img1.mydrivers.com/img/20220701/S5b5ccdd5-12ba-47a8-93dd-e7fec7bd5145.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>【未来：一年一变 每年提升两位数性能】</strong></p>
<p>有趣的是，Arm这次很大方地公布了未来两年的路线图。</p>
<p>明年的TCS23，超大核CPU升级为CXC23(预计命名Cortex-X4)，大核、小核分别升级为Hunter、Hayes，DSU互联单元升级为Hayden，旗舰GPU则升级为Titan。</p>
<p>后年的TCS24，超大核CPU再次升级为CXC24(预计命名Cortex-X5)，大核升级为Chaberton，小核则维持不变还是Hayes，旗舰GPU则继续升级为Krake。</p>
<p>另外，沿用多代的CoreLink CI-700一致性互连技术、CoreLink NI-700片上网络互连技术，也终将迎来更新，代号Tower。</p>
<p><strong>希望Arm未来能在能效、扩展性、平台安全性方面齐头并进。</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220701/ebf597f5-6dc1-42f0-a796-986073fad230.png" target="_blank"><img alt="Arm全面进化：CPU超越酷睿i7、GPU光追性能猛增3倍" h="313" src="https://img1.mydrivers.com/img/20220701/Sebf597f5-6dc1-42f0-a796-986073fad230.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：上方文Q</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/arm.htm">Arm</a><a href="https://news.mydrivers.com/tag/cortex-x3.htm">Cortex-X3</a><a href="https://news.mydrivers.com/tag/immotalis-g715.htm">Immotalis-G715</a><a href="https://news.mydrivers.com/tag/guangxianzhuizong.htm">光线追踪</a>  </p>
        
</div>
            