
---
title: 'Intel 12代酷睿超频详解：DDR5还能这么玩！'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211028/s_25d07cefc136430687aea6c8a2e990d6.png'
author: 快科技（原驱动之家）
comments: false
date: Thu, 28 Oct 2021 22:31:03 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211028/s_25d07cefc136430687aea6c8a2e990d6.png'
---

<div>   
<p>超频，DIYer永恒的话题。</p>
<p>虽然赛扬300A那样的奇迹不可能再重演，如今的超频也存在诸多限制，但仍有诸多玩家乐此不疲，厂商也乐意提供一个尽可能开放的平台。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211028/25d07cefc136430687aea6c8a2e990d6.png" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_25d07cefc136430687aea6c8a2e990d6.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211028/766986eac6814cf3a0f673de74ae113a.png" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_766986eac6814cf3a0f673de74ae113a.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><a class="f14_link" href="https://news.mydrivers.com/1/792/792044.htm" target="_blank">Intel最新发布的Alder Lake 12代酷睿处理器</a>，首发六款K/KF系列型号，搭配Z690主板，全都解锁超频技能，并加入了不少新玩法，尤其是首发的DDR5内存，更是值得深深挖掘。</p>
<p>12代酷睿采用了混合架构设计，这次不但高性能的P核可以超频，高能效的E核同样支持，还能控制内部BCLK基准外频。</p>
<p>同时，DDR5的超频更丰富，不但支持XMP 3.0一键超频，更是有<strong>动态内存加速(Dynamic Memory Boost)</strong>等新技能。</p>
<p>软件方面，Intel XTU超频软件也顺应升级到了7.5版本，当然你也可以在主板BIOS里深入挖掘。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211028/e65edcbf37ec42ab9312a47cf68b35dd.png" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_e65edcbf37ec42ab9312a47cf68b35dd.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>12代酷睿平台的超频架构图，<strong>P核倍频(xP)、E核倍频(xE)、环形总线与缓存频率(xR)、核显频率(xG)、内存频率(xM)、基准时钟频率/外频(BCLK)</strong>，都是可以调的。</p>
<p>当然了，“外频”的可调空间一直非常小，基本不用去考虑，除非是冲击极限记录。</p>
<p>跟具体来说，在超频选项上，既有传统的AVX偏移/关闭、每核心超线程开关、每核心倍频、实时内存频率、电压控制等选项，也支持<strong>PLL控制、外频适应性电压、PEG/DMI总线超频、TjMax温度阈值偏移、每核心开关</strong>等等新的玩法，Intel一共开放了超过20种设置。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211028/270b98c59e2046f6bca8cc611f8c77f2.png" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_270b98c59e2046f6bca8cc611f8c77f2.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211028/5316dc61c40845debae209748545e44d.png" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_5316dc61c40845debae209748545e44d.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211028/3dd45a6118df4f94a265c1037203b243.png" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_3dd45a6118df4f94a265c1037203b243.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>Intel XTU 7.5软件的功能也越发强大，大部分时候都可以不用再去BIOS里修改了，<strong>这次针对12代酷睿专门加入了E核、DDR5的超频控制</strong>，还集成XTU Benchmark 2.0，方便检验超频稳定性。</p>
<p>如果你不喜欢复杂的超频，或者不懂，Intel也提供了<strong>基于ISO技术的一键超频，它会自动检测P核、E核的频率、电压等参数，设置最合适的超频频率</strong>，当然幅度会保守一些。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211028/aefb01b41af44595a923a42d5d7db5fb.png" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_aefb01b41af44595a923a42d5d7db5fb.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211028/2471453f8ee24cb39af41b27b36a2f8e.png" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_2471453f8ee24cb39af41b27b36a2f8e.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211028/b17e5b8ed98d41d994d789d4a1faeb04.png" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_b17e5b8ed98d41d994d789d4a1faeb04.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211028/fbdc54ffe97847a0b8b239d4a9ff5c65.png" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_fbdc54ffe97847a0b8b239d4a9ff5c65.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>接下来说说XMP。</p>
<p>这是Intel制定的内存建议超频方式，2007年诞生，最初服务于DDR3，目前使用最广泛的XMP 2.0版对应DDR4，现在升级到XMP 3.0来支持DDR5。</p>
<p><span style="color:#ff0000;"><strong>XMP 1.x/2.0都只支持两组配置档(Profile)，XMP 3.0则增加到了五组，其中三组出厂预设不能变更，另外两组允许玩家读写修改，为了防止乱改还支持CRC错误校验。</strong></span></p>
<p>同时，配置档的文件名也开放到了<strong>最多16个字符</strong>，存储空间从102个字节扩大到<strong>384个字节</strong>。</p>
<p>更值得一提的是，DDR5内存由于集成了PMIC电源管理电路，因此<strong><span style="color:#ff0000;">可以更开放地单独调整电压，主要是VDD、VDDQ、VPP</span></strong>，而且它们都是JEDEC、Intel共同规范的，在不同主板上保持一致。</p>
<p>目前，<strong>海盗船、芝奇、美光英睿达、金士顿Fury、博帝、十铨TForce</strong>等六家内存厂商已经完整支持XMP 3.0，像海盗船还提供了专门的软件IQsoftware，使用更加方便。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211028/0b692c3159e84e3bbd38fab52959afb1.png" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_0b692c3159e84e3bbd38fab52959afb1.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>最后说说动态内存频率调整，一种更智能的内存超频方式，有点类似睿频。</p>
<p><strong>它仅限12代酷睿，但同时支持DDR4、DDR5</strong>，唯一要求就是XMP得到了Intel官方认证。</p>
<p><span style="color:#ff0000;"><strong>在BIOS里开启此功能后，如果系统负载较高，它就会自动切换到XMP高频配置，轻负载的时候则回到內建的JEDEC低负载。</strong></span></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211028/7b63665da77746ffb379e13edc13ebcc.png" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿超频详解：DDR5还能这么玩！" h="338" src="https://img1.mydrivers.com/img/20211028/s_7b63665da77746ffb379e13edc13ebcc.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/intel.htm"><i>#</i>Intel</a><a href="https://news.mydrivers.com/tag/cpuchuliqi.htm"><i>#</i>CPU处理器</a><a href="https://news.mydrivers.com/tag/chaopin.htm"><i>#</i>超频</a><a href="https://news.mydrivers.com/tag/ddr5.htm"><i>#</i>DDR5</a><a href="https://news.mydrivers.com/tag/alder_lake.htm"><i>#</i>Alder Lake</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            