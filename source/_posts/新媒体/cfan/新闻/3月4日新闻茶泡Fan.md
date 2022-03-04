
---
title: '3月4日新闻茶泡Fan'
categories: 
 - 新媒体
 - cfan
 - 新闻
headimg: 'https://upload.cfan.com.cn/2022/0304/1646358947842.png'
author: cfan
comments: false
date: Fri, 04 Mar 2022 09:58:00 GMT
thumbnail: 'https://upload.cfan.com.cn/2022/0304/1646358947842.png'
---

<div>   
<p><strong>Intel i7-12650HX首次现身</strong></p>
<p>UserBenchmark里出现了一款尚未发布的12代酷睿移动版处理器，型号i7-12650HX，14核心20线程，也就是6个性能核心、8个能效核心，基准频率2.3GHz，平均睿频加速4.05GHz(不一定是最高值)，搭配的内存是DDR5 SO-DIMM。</p>
<p>Intel目前的产品线里有一款i7-12650H，不过只有10核心16线程(6大4小)。从目前迹象看，i7-12650HX属于尚未发布的H55系列，面向移动端，但采用特殊的S-BGA封装，功耗范围45-55W，可以视作把桌面端整合封装用于移动端。早前的路线图上就出现过H55系列，但配置只有8大8小、4大8小，看来是又增加了6大8小。除了i7-12650HX，该系列应该还会有更高端的i9-12980HX、i9-12900HX等等。</p>
<p>PS：AMD经常效仿Intel的产品命名方式，但这次的HX似乎是偷师自AMD，后者的HX系列就是最顶级移动版，功耗开放到45W+。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0304/1646358947842.png" border="0" alt="s_0dbb6d16e64040a38641ca97ef45bc23" referrerpolicy="no-referrer"></p>
<p><strong>PCIe 5.0显卡果然是超级电老虎</strong></p>
<p>有关下一代PCIe 5.0显卡将引入全新16针（或者说12+4针），已经讲了不少次，华硕、酷冷、微星也都陆续发布了配备新接口、新电源线（转接线）的电源产品。现在，PCIe 5.0显卡供电的官方标准规范，终于泄露了一部分出来。新标准的官方名为“12VHPWR”，非常拗口，也是导致产品命名混乱不规范的根源。</p>
<p>我们知道，PCIe x16插槽的供电能力是75W，从未变过，PCIe 6针、8针辅助供电最高分别是75W、150W。到了PCIe 5.0的时代，根据新标准，12VHPWR 16针的供电电压为12V，单个针脚电流最大9.2A，整体最大55A，最高稳定功率则有四个档次，从低到高分别是150W、300W、450W、600W，具体会在接头上明确标注，方便识别。</p>
<p>当然，16个针脚中只有12个是负责供电的，另外4个负责信号监视传输，属于可选，但没有它们就上不到600W，最多只能到450W。如果再加上PCIe ×16插槽本身的75W，PCIe 5.0显卡可以获得最高675W的供电支撑。</p>
<p>同时，标准还定义了两个边带信号(sideband signal)，分别叫Sense0、Sense1，全部接地的时候，才能达到600W的持续供电能力，系统启动时供电为375W。如果有任何一个非接地，持续和启动供电功率就会逐级下降，450W、300W、225W峰值分别对应225W、150W、100W起步。如果显卡不监控此边带信号，则必须以最低的100W来启动。</p>
<p>另外根据ATX 3.0电源标准，16针供电不兼容现在的6/8针，因为无论是接口尺寸还是电流电压，都不完全一样，必须使用转接。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0304/1646358955305.png" border="0" alt="s_5ac72f7309b94bbeb049135db2c13bd5" referrerpolicy="no-referrer"></p>
<p><strong>Intel 700系列芯片或仅支持DDR5内存</strong></p>
<p>据TechPowerUp的报告来看，Intel正在研发仅为13代Raptor Lake处理器提供支持的700系列芯片组主板，虽然DDR4+DDR5的内存控制器仍是主流，但Intel正在努力提升DDR5内存的市场比例。</p>
<p>从该报道来看，Intel正在研发的700系列芯片组主板将仅支持DDR5内存，而DDR4内存则主要保留在600系芯片组平台。不过需要注意的是，厂商往往并不会完全听从Intel指挥，只要市场需要700系主板支持DDR5内存的呼声够大，总会有厂商忍不住。</p>
<p>此外，13代Raptor Lake CPU提供了DDR5-5600的原生内存频率支持，与12代Alder Lake的DDR5-5200相比进一步提升。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0304/1646358963360.jpg" border="0" alt="s_1b24d5e66acb493a96b023940c1c456f" referrerpolicy="no-referrer"></p>
<p><strong>影驰推出DDR5-6200MHz内存</strong></p>
<p>今年早些时候影驰发布了GAMER DDR5系列内存4800MHz、5600MHz两个版本，如今GAMER RGB DDR5 6200MHz正式发布，首发规格16GB*2，价格2999元。</p>
<p>GAMER DDR5 6200MHz版与之前两个版本区别不大，依然是金属外壳搭配红蓝撞色设计，积木元素覆盖全身，内存顶部则预留了多个积木孔位，可以像积木那样自由组建。</p>
<p>据悉，GAMER DDR5 6200MHz版支持XMP 3.0超频技术，时序规格为CL32-38-38-76，在官方测试中，读取速度为96581MB/s，写入速度为86258MB/s。</p>
<p>影驰方面表示，GAMER DDR5系列内存采用原厂DRAM颗粒搭配8层黑色定制化PCB，为内存提供稳定电压，降低主板对内存性能的影响。需要注意的是，目前普通DDR5 4800MHz 16GB×2内存条的价格在2500元左右，也就说GAMER DDR5 6200MHz版还是蛮吸引人的。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0304/1646358974833.jpg" border="0" alt="S19367f3f-d54a-44fd-a509-55a6ac351573" referrerpolicy="no-referrer"></p>
<p><strong>三星LPDDR5X内存来了</strong></p>
<p>今天三星半导体官方微博宣布，三星首款基于14nm的LPDDR5X内存已在高通骁龙移动平台上验证使用。三星表示，三星与高通公司密切合作，7.5Gbps的LPDDR5X用于骁龙移动平台。</p>
<p>LPDDR5X的速度比目前高端智能手机上的LPDDR5（6.4Gbps）快约1.2倍，有望在下一代智能手机上提升超高分辨率视频录制性能和语音识别、图像识别、自然语言处理等人工智能功能。此外，三星LPDDR5X内存采用先进的电路设计和动态电压频率缩放，功耗可降低约20%。</p>
<p>三星半导体执行副总裁兼内存全球销售和营销负责人Jinman Han表示：LPDDR5X解决方案在高通技术公司骁龙移动平台上的成功验证，证明了我们在DRAM技术方面的先进地位。我们预计这种高性能、低功耗内存的应用将从智能手机扩展到数据中心、个人电脑和汽车，使越来越多的设备和系统得以更高的效率运行。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0304/1646358983696.jpg" border="0" alt="s_b1beab56ea7f4fb7a6dcbe000c40cdbd" referrerpolicy="no-referrer"></p>
<p><strong>1999元 realme V25发布</strong></p>
<p>昨天下午，realme V25正式发布，售价1999元（12GB+256GB），3月4日0点正式发售，有紫微星、启明星和苍穹黑等多彩配色可选。</p>
<p>该机看点之一是标配12GB内存，同时支持DRE动态运存拓展技术，最大可以扩展7GB，带来等同于19GB内存的使用体验，比肩高端旗舰。据悉，内存拓展技术是一项辅助功能，在手机使用过程当中，运行内存不够用时可以调用一部分存储空间临时当作运行内存来使用，让手机能够同时开启更多的应用并保证手机流畅运行，做到让手机配置物尽其用，最高效率运转。</p>
<p>除了拥有堪比19GB内存手机的体验，realme V25的续航也是一大看点，该机配备了5000mAh大电池，支持33W满血快充。官方数据显示，realme V25连续待机可以做到24天，连续通话可以达到49小时，连续音乐90小时，连续吃鸡9小时，连续抖音15.5小时，连续录像6.5小时。</p>
<p>核心配置上，realme V25采用6.6英寸全面屏，支持6档刷新率智能变速，屏幕亮度达到了600尼特，搭载高通骁龙695处理器，前置1600万像素，后置6400万AI三摄。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0304/1646358996441.jpg" border="0" alt="s_f4f4260675b74a73a411f9af742aa470" referrerpolicy="no-referrer"></p>
<p><strong>OPPO Find N获最具突破性创新产品奖</strong></p>
<p>3月3日消息，OPPO宣布OPPO首款折叠屏Find N获得了2022年全球移动大奖最具突破性创新产品奖。该机发布于2021年12月份，首发起售价为7699元，上市后一直供不应求，人气火爆。</p>
<p>不仅如此，OPPO Find N成为了中国市场销售速度最快的折叠屏，这一切源于OPPO Find N极具竞争力的价格和近乎无折痕的全新设计。</p>
<p>OPPO Find N搭载OPPO自研的精工拟椎式水滴形铰链，这种铰链可以最大程度减少折痕，并且使用寿命也更长，但结构设计也更复杂，成本更高，是其它铰链成本的三倍。在精工拟椎式铰链的加持下，OPPO Find N在展开状态下，没有明显的折痕，屏幕表面平整，这种效果已经超越市面上大部分折叠屏了，堪称“折叠屏标杆”。</p>
<p>规格方面，OPPO Find N搭载高通骁龙888处理器，最高配备12GB内存、512GB存储，前置3200万像素，电池为4500mAh，支持33W闪充。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0304/1646359047783.jpg" border="0" alt="s_94f1d3f762d4462289fc0cc60ca4efb0" referrerpolicy="no-referrer"></p>
<p><strong>新版Edge浏览器将引入性能检测功能</strong></p>
<p>根据Windows Latest透露的消息，Win10及Win11平台的Edge浏览器将引入一项新“性能检测器”功能，从而提升程序的运行速度。据悉，该功能是Edge浏览器目前效率模式的补充，能够自动检测目前存在的性能问题，并自动提出合理的解决方案。</p>
<p>此外，该功能将搭配现有的效率模式，通过优化网络性能、改善响应速度、减少CPU、内存使用等方式来提升浏览器的网页的运行速度，并通过休眠模式解决性能问题。同时，根据图片信息，该功能除了会针对浏览器的性能问题向用户提出推荐建议外，还将检测浏览器的扩展与其他功能的潜在问题，并提出建议。</p>
<p>除了该功能外，有消息称，微软正在为Edge测试新的全屏功能，这一功能相较目前的版本有更大的适用范围，并更为易用。值得一提的是，目前，Edge浏览器的版本已经来到了98.0.1108.63，这意味着，在Chrome跨过100大关后不久，Edge也将成为一款拥有三位数版本号的浏览器。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0304/1646359061539.jpg" border="0" alt="s_6bc2aa88e8954755bd5fbe0a9b61638b" referrerpolicy="no-referrer"></p>　  
</div>
            