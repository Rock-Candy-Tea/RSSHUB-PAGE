
---
title: 'Arm最强芯片公布，这一刻我等了10年'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210528/v2_8674e0585cba4604856b32810a94a0ae_img_000'
author: 36kr
comments: false
date: Fri, 28 May 2021 00:02:56 GMT
thumbnail: 'https://img.36krcdn.com/20210528/v2_8674e0585cba4604856b32810a94a0ae_img_000'
---

<div>   
<p>编者按：本文来自微信公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s?__biz=MjM5MTg5NTU0MQ==&mid=2653886015&idx=2&sn=4f093b27cecbb6fc460ddd29312d5d10&chksm=bd752ca58a02a5b3ff4690a28a003bc23eaa6d670aacee6d2f5dd8ad10548639eccac1a873e0&mpshare=1&scene=1&srcid=0527SfnPeQfk8Tc1DbX78rSJ&sharer_sharetime=1622122756337&sharer_shareid=34e6e6992f92e1db4af35baa9f00f10f#rd">“雷科技”（ID:leitech）</a>，作者：TSknight ，36氪经授权发布。</p> 
<p>北京时间5月25日晚，Arm正式推出了新一代的CPU和GPU核心，包括全新的Cortex-X2、Cortex-A710、Cortex 510等三款CPU核心以及Mali-G710 GPU，在5月26日晚则是又更新了Mali-G610、Mali-G510、Mali-G310三款GPU核心。 </p> 
<p class="image-wrapper"><img data-img-size-val="600,337" src="https://img.36krcdn.com/20210528/v2_8674e0585cba4604856b32810a94a0ae_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val="600,337" src="https://img.36krcdn.com/20210528/v2_7d61c420605e4e2baf509a17c093db7a_img_000" referrerpolicy="no-referrer"></p> 
<p>本次所有的新核心都基于新的架构所设计，在性能、安全及AI性能方面对比上一代都有着明显的提升。 </p> 
<p>大家期待已久的新核心终于来了，但是采用新核心设计的处理器最快可能也要等到今年年末或是明年才会推出，所以短时间内大家也就只能先看看PPT解解馋了。 </p> 
<h2><strong>新架构的首秀</strong></h2> 
<p>本次Arm更新的三个CPU核心均基于今年4月份发布的Armv9<a class="project-link" data-id="6632" data-name="指令集" data-logo="https://img.36krcdn.com/20210518/v2_acc266b7f4d844478a729339a7dc7e40_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4854500224" target="_blank">指令集</a>设计，当然，你也可以称其为Armv9架构。 <strong>Armv9架构是Arm自2011年发布Armv8架构后的首次大规模架构更新</strong> ，不再是如同往年那样东一榔头西一棒子地改造Armv8，就连Arm高层都将其称为10年来最大的变革。 </p> 
<p class="image-wrapper"><img data-img-size-val="600,294" src="https://img.36krcdn.com/20210528/v2_242bda10c84240f482e363b1f78df915_img_000" referrerpolicy="no-referrer"></p> 
<p>关于Armv9，小雷在今年4月份写的一篇 文章 中详细的解析过它的优势，感兴趣的读者朋友可以去看看，赶时间的话小雷就用一句话给你们概括一下：性能UP、安全性UP、AI性能UP，在内存速度、信号处理、5G、虚拟/增强现实、机器学习等多个方面的性能都会有着明显提升，是未来数千亿芯片的基础。 </p> 
<p class="image-wrapper"><img data-img-size-val="600,337" src="https://img.36krcdn.com/20210528/v2_3f6a672c193b47f8b9fbc58615f713b8_img_000" referrerpolicy="no-referrer"></p> 
<p>所以，相比起往年的核心更新，这一次的Cortex-X2、Cortex-A710、Cortex 510和Mali-G710才会更加让人关心，毕竟Armv9架构的提升是否真如Arm所说的那么巨大，看看这次的核心提升就清楚了。 </p> 
<h2><strong>新大核Cortex-X2</strong></h2> 
<p>Cortex-X2作为新一代的大核，从Arm给出的数据来看，整数性能对比上一代的Cortex-X1提升了16%，浮点运算性能更是直接翻倍，也算是颇为可观。其中浮点性能的提升，意味着Cortex-X2将在图像处理、语音识别、视频编解码等方面表现出远超Cortex-X1的性能，对于智能拍摄、图像识别、智能语音助手等功能的提升较大。 </p> 
<p class="image-wrapper"><img data-img-size-val="967,471" src="https://img.36krcdn.com/20210528/v2_e72c36a2a1f6478daf0ab98c9aab368f_img_000" referrerpolicy="no-referrer"></p> 
<p>不过，小雷仔细看了看，发现Arm果然还是玩了一手经典套路， <strong>用来与Cortex-X2对比的Cortex-X1选择的是残废版，8MB的L3缓存被砍了一半，而Cortex-X2则是满血版8MB的L3缓存，</strong> 以此突出Cortex-X2的性能，实际的提升应该是达不到2倍。虽然，Arm故意拉大新旧品的差距也算是传统艺能，但是每次看到都让人有点欲言又止（大家懂的）。 </p> 
<p>而且，即使在发布会中公布了Cortex-X2将配备8MB的L3缓存，实际使用中估计也会依照成本和定位来下刀，最终到消费者手里的Cortex-X2性能到底如何，还需要看后续各芯片厂商的设计。 </p> 
<p>之后Arm还给出了关于分支预测、ROB性能等方面的提升，简单总结就是提升巨大。重点还是与上一代大核Cortex-X1的性能功耗对比图，在图中可以看到低功耗的情况下，Cortex-X2与Cortex-X1的性能十分接近，但是在达到一定功耗后Cortex-X2将拥有更出色的功耗比。 </p> 
<p class="image-wrapper"><img data-img-size-val="969,485" src="https://img.36krcdn.com/20210528/v2_f926ef534e69442a96614ef5631c0cc9_img_000" referrerpolicy="no-referrer"></p> 
<p>而且在功耗上限和性能上限方面都有着不少的提升，不过具体提升幅度不好预测，因为Arm没有标出任何的数字，只能靠脑补，反正具体的提升还是需要等待厂商的调教，Arm的对比图往往只是一个参考。 </p> 
<h2><strong>自由的Arm，中核A710来了</strong></h2> 
<p>大核之后我们来看看中核A710，让人无语的是，自由的高通突然又用回了以前的三位数命名方式，而不是大家所预测的A79，虽然没啥影响，但是也让人感叹Arm的命名方式还真是无法揣摩（骁龙888：你说的对）。 </p> 
<p class="image-wrapper"><img data-img-size-val="600,337" src="https://img.36krcdn.com/20210528/v2_927b81927066445f98aa2b65d23481be_img_000" referrerpolicy="no-referrer"></p> 
<p>说回A710，自从Arm更新了Cortex-X1后，原本的A系大核就沦为了新架构里的中核，而且从原本的主要负责性能提升转为主打功耗比，相比起Cortex-X2更看重在一定功耗下提供不错的性能体验，也是我们日常使用中最常用到的核心。 </p> 
<p>A710的主要提升项与Cortex-X2基本相同，不过有一点不同的是在某个地方还自刀了一下，削弱了些许解码性能从而实现更高的能耗比，对于日常使用基本没有影响。 </p> 
<p>在Arm给出的对比图中这次倒是标出了实际的差距， <strong>根据Arm的测算，以上代A78功耗为100来计算，A710在70功耗下可以达到A78相同的性能，而在100功耗下A710则能够提供A78的110%性能，同时还有着更高的功耗和性能上限。</strong></p> 
<p class="image-wrapper"><img data-img-size-val="600,337" src="https://img.36krcdn.com/20210528/v2_43952759bec248ec8ed4257900b7ff71_img_000" referrerpolicy="no-referrer"></p> 
<p>不过，与Cortex-X2不同，Arm并没有给出更直观的IPC性能对比数据，小雷猜测可能实际提升并不大，只不过是更省电了。 </p> 
<h2><strong>时隔四年终于更新，小核A510提升巨大</strong></h2> 
<p>最后我们来看看时隔四年终于迎来更新的小核——A510，也是本次的三个CPU核心中提升最大的（毕竟A55是四年前的老核心）。小核的更新主要效果就是拉升整个芯片组在低功耗下的性能，接下来的中低端芯片也许会迎来一次性能提升幅度不小的更新。 </p> 
<p class="image-wrapper"><img data-img-size-val="600,337" src="https://img.36krcdn.com/20210528/v2_21d6d47cc824460d819fb545f2e081f6_img_000" referrerpolicy="no-referrer"></p> 
<p>从Arm给出的数据来看，A510对比A55的提升幅度在35%-62%之间，勉强超过了曾经的大核A57，与之前媒体爆料称A510性能媲美A73不太符合，两者的性能还是有着一定的差距，不过整体来说提升已经算是相当的可观。 </p> 
<p class="image-wrapper"><img data-img-size-val="600,337" src="https://img.36krcdn.com/20210528/v2_2f04c0613d434ae7a920d5f26ed508d1_img_000" referrerpolicy="no-referrer"></p> 
<p>当然，大家也不用指望A510能够给整体性能带来多大的提升，小核的主要意义还是在提升续航上。不过，对比A55已经算是有了不少进步，只希望Arm不要像A55那样把A510用上几年就好。 </p> 
<h2><strong>新GPU扎堆发布，首次完整覆盖高中低端</strong></h2> 
<p>在Arm的第一天报告中，他们就已经为我们带来了三个新的CPU核心和一个Mali-G710 GPU核心，但是令人意外的是，在第二天的报告中，Arm又继续放出了三款新的GPU核心， <strong>本次发布的核心数量达到7个，而且完整覆盖高中低端的不同需求。</strong></p> 
<p class="image-wrapper"><img data-img-size-val="600,333" src="https://img.36krcdn.com/20210528/v2_75047bf6417542b59e0f4266713cf1ee_img_000" referrerpolicy="no-referrer"></p> 
<p>公布的四款GPU分别是： <strong>Mali-G710、Mali-G610、Mali-G510、Mali-G310</strong> ，其中25日发布的G710主打高端市场，G510和G310则分别针对中端和低端市场，还有个G610则是G710的性能阉割版，只是为了更好的区分所以这次给了一个独立的命名。 </p> 
<p class="image-wrapper"><img data-img-size-val="600,337" src="https://img.36krcdn.com/20210528/v2_239d06ca8f51423ea88909604a6a3452_img_000" referrerpolicy="no-referrer"></p> 
<p>对比上一代核心，定位高端的G710提升最低，综合性能提升仅20%，值得庆幸的是功耗比也提升了20%，至少续航提升颇为亮眼。至于性能方面，目前的GPU已经是足够大多数满足游戏需求（唯一的例外也就原神），所以对于大多数用户来说20%的性能提升也算不错了。 </p> 
<p class="image-wrapper"><img data-img-size-val="600,340" src="https://img.36krcdn.com/20210528/v2_8a0da0eeb04d40518e6a4a157fd6a53a_img_000" referrerpolicy="no-referrer"></p> 
<p>另一边的中端G510则相对提升更加明显，相比上一代综合性能提升高达100%，功耗比提升则是22%，如此亮眼的提升可以说并不多见。不过，主要原因是因为上一代的中端GPU核心G57性能较弱，所以G510的提升才会显得如此巨大。 </p> 
<p>最后则是G310，从Arm的描述来看， <strong>G310是对比上一代变化最大的，其中纹理性能提升多达6倍、Vulkan性能提升4.5倍、安卓UI内容性能提升2倍，是本次提升最大的GPU核心。</strong> 因为定位低端，所以对于追求极致性能的用户来说意义不大，主要是提升了低端处理器在游戏方面的性能。 </p> 
<h2><strong>总结</strong></h2> 
<p>简单总结一下，Armv9很给力，下一代旗舰处理器也会很给力，而且将会迎来一次全方位的性能升级。 <strong>所以，如果大家手上的手机性能还够用，不妨等等今年年底（也有可能是2022年）采用新核心的处理器上线后再换手机。</strong></p> 
<p>最后，Arm还在报告中特别指出应中国客户的要求， <strong>对A710采用了特殊的设计，让A710仍然可以支持OL0 AArch32，不过X2和A510将不再支持和兼容32位，仅支持64位指令集。</strong> 这个设计主要是考虑到国内大多数应用还停留在32位上，只有少部分采用了64位，如果核心不支持，届时所带来的问题将会是灾难性的。 </p> 
<p>这点倒是让小雷颇为震惊，有一种：软件厂商你们赚的钱都去哪里了.jpg 的感觉，2021年了居然还在用过时的32位指令集，确实有点说不过去，还是希望国内软件厂商可以逐步把软件切换到64位吧，毕竟64位对比32位的优势还是相当明显的。 </p> 
<p>至于有人关心的<a class="project-link" data-id="25167" data-name="华为" data-logo="https://img.36krcdn.com/20200729/v2_7c7826d711824e758a8e1511c9d7eecc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25167" target="_blank">华为</a>能不能用新核心的问题，从Arm公司给出的文件来看，暂时没有涉及关于禁止授权华为的消息，也就是说 <strong>华为依然有机会从Arm那里获得最新的核心授权，用来开发下一代处理器。</strong> 不过华为现在主要面对的问题是无法制造，而非无法开发，所以期待华为新旗舰处理器的朋友们可能要失望了。 </p>  
</div>
            