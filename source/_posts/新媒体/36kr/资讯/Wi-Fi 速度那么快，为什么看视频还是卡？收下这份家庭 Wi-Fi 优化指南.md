
---
title: 'Wi-Fi 速度那么快，为什么看视频还是卡？收下这份家庭 Wi-Fi 优化指南'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220318/v2_9de5110768b842169268cae57189dac8_img_000'
author: 36kr
comments: false
date: Fri, 18 Mar 2022 05:47:00 GMT
thumbnail: 'https://img.36krcdn.com/20220318/v2_9de5110768b842169268cae57189dac8_img_000'
---

<div>   
<p>相信很多朋友在挑选无线路由器时，都会对无线路由器下面褒贬不一的评论感到困惑，下面总有会人说：「这个路由器信号不好，经常断流」，也有另外一部分的人说：「覆盖很广，速度很快」。明明就是同一款产品为什么会产生这样的两级分化呢？笔者认为有两方面原因，一方面是无线路由器中有大量普通用户难以理解的术语，普通消费者根本不知道这个选项是干什么的；另一方面则是现在家用无线路由器的默认设置不够智能，反而劣化了网络。 </p> 
<p>想要知道无线路由器中每个参数是什么以及我们应该如何优化无线网络且看下文。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_9de5110768b842169268cae57189dac8_img_000" referrerpolicy="no-referrer"></p> 
<p>同一个产品两极分化的评论 </p> 
<p><strong>▍Wi-Fi 信号到底怎么才能算得上优秀？</strong></p> 
<p>无线信号其实是一个很复杂的问题，由于缺乏良好的科普再加上厂商的营销误导，导致很多消费者单一地认为较高的测速速率代表了较好的 Wi-Fi 信号强度。 </p> 
<p>在这一篇文章中我们已经分析过了理想状态下 Wi-Fi 速度的问题。但是较高的 Wi-Fi 传输速度仅能代表某一方面，并不代表这个 Wi-Fi 信号优化到位。「游戏时延迟突然暴增」也就是 Wi-Fi 设备丢包、「看视频频繁遇到缓冲」也就是 Wi-Fi 断流都代表了这个 Wi-Fi 并不优秀。如果你是 Mac，按住 Option 点击 Wi-Fi 图标，就可以看到如下参数： </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_8b96088f899849128361a89f80e6e0ad_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>一组 Wi-Fi 参数 </p> 
<p>而优化 Wi-Fi 信号就是需要我们优化<strong>信道</strong>、<strong>频宽</strong>、<strong>信号强度（RSSI）</strong>、<strong>噪声</strong>和<strong>信噪比 SNR</strong>。 </p> 
<p>而上图参数就能算是一个优秀的 Wi-Fi 信号了：</p> 
<p>信道：149</p> 
<p>频宽：40 MHz</p> 
<p>信号强度：-30 dBm</p> 
<p>噪声：-93 dBm</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>信噪比：63 dB</p></li> 
</ul> 
<h3><strong>信道与频宽</strong></h3> 
<p>在上一篇文章中，我们讲到了频宽和速度的关系，可以简单的把频宽想象成高速公路的车道数量，车道数量越多，单位时间可以行驶的流量也就越大。 </p> 
<p>而你所使用的 Wi-Fi 在所有的频段中有一个容纳其的位置，这就是<strong>信道</strong>，信道就是对于频段进行细分。国内划分给 2.4GHz 的信道划分了一共 13个信道，并依次标记为 1-13 ，每个信道之间相差 5Mhz，通过下图可以看到临近的频段是相互重叠的，也就是互相之间会产生干扰。因此在 2.4GHz 下最多可以容纳三个互不干扰的 20Mhz 频宽或者一个 40Mhz 频宽的的Wi-Fi 信号。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_8ac94733cbee40d4b3f9a068abae6e5d_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>2.4GHz信道的分布和重叠情况 </p> 
<p>而 5GHz Wi-Fi 下，5.2GHz 的可用信道为 36-64 ，5.8GHz 是 149-161。如下图： </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_694d97c89ef44a20832a7ae0ef80a594_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>5GHz 下 信道的分布和重叠情况 </p> 
<p>需要注意的是 UNII-2-Extended 在国内是无法使用的，因此 5GHz 上最多可以容纳 3 个互不干扰的 80Mhz 或者 1 个 160Mhz频段的信号。信号可以调整其通道编号来减少重叠进而避免干扰，2.4GHz 下以单个信道为单位，而 5GHz 下以 4 个信道为单位。 </p> 
<p><strong>噪声</strong></p> 
<p>噪声是影响 Wi-Fi 信号的一个重要指标，噪声可能来源于其他邻居家的 Wi-Fi 信号，也会来自其他同频无线电信号，比如 2.4GHz 下的蓝牙和 Zigbee 信号，甚至是<strong>微波炉</strong>和<strong>荧光灯</strong>的射频泄漏也会影响到 2.4GHz 频段的 Wi-Fi 信号。如果噪音水平过高，可能会导致无线信号强度的强度和性能下降。噪音和信号强度一样，也使用 dBm 作为单位，一般来说噪声强度在 -90dBm 以下的噪声对正常使用 Wi-Fi 没有干扰。</p> 
<h3><strong>信噪比</strong></h3> 
<p>信噪比（SNR）是信强和噪声水平之间的功率比。信噪比的单位是 dB，是一个<a class="project-link" data-id="245681" data-name="绝对值" data-logo="https://img.36krcdn.com/20210809/v2_bbf3faec15ec4e5a8f786e6aa053774d_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/245681" target="_blank">绝对值</a>，计算方法为： </p> 
<p><strong>SNR (dB) = RSSI (dBm) - 噪声 (dBM)</strong></p> 
<p>一般来说，30dB 以上的信噪比是一个较好的环境，SNR 低于 30dB 的情况下无线上网体验会受到比较严重的影响。一般家庭无线网络使用环境的噪声在 -90 - -95 dBm 左右，优质信号需要在 -65 dBm 以上。</p> 
<h2><strong>▍我如何优化信道和频宽？</strong></h2> 
<p>虽然，很多家用无线路由器中都有诸如「自动优化信道」的功能，但是笔者体验下来实际效果并不好，无线路由器并不能选择一个噪声和干扰都最小的信道，一些支持 160MHz 的无线路由器也不会因为环境噪声过大而降低频宽。接下来以笔者寝室的实际例子，我们讲讲如何手动优化 Wi-Fi。 </p> 
<p>首先找一个功能较为完整的 Wi-Fi 分析软件，笔者使用的是 Mac 上的Wi-Fi Explorer，这款软件包含在 Setapp 中；如果你手中有安卓移动设备，也可以选用 UBNT 开发的Wifiman进行检测；Windows 用户可以考虑使用inSSIDer分析 Wi-Fi： </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_d3eb18839c5d408fa8e2f822e60702f8_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Wi-Fi Explorer </p> 
<p>进入后我们可以看到这样的界面，详细展示了 Mac 目前所能接受到来自不同 AP 的所有 Wi-Fi 信号。界面下方也展示了当前选择网络的详细信息，比如信号强度，信道，频宽，SNR 等。 </p> 
<p>我们点击页面下方的 「Spectrum 2.4 / 5 GHz」 选项，还可以看到当前环境下的全部信道占用情况。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_1d663bd24ba74de09dc93a1930288e40_img_000" referrerpolicy="no-referrer"></p> 
<p>我们以 5GHz 为例：上文也介绍过 5.2GHz 频段可以容纳完整的两个 80Mhz 频宽或者一个 160Mhz 频宽，而 5.8GHz 下则只能使用一个完整的 80 MHz 频宽。但很多高端路由器出厂时会默认设定频宽为 160MHz，所以我们可以把 AP 设置成 160Mhz 以后来仔细观察此时的无线环境： </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_c4c25ec82e42425eb6b5dcbd4463877d_img_000" referrerpolicy="no-referrer"></p> 
<p>虽然这时协商速率最大可达 4.8Gbps，但是 5GHz Wi-Fi 到噪声比例高达 48%，即使是在 AP 附近，SNR 也仅有 46 dB。更低的信号噪比意味着，每一次传输有效的数据量也更少，反应到实际使用情况中比如使用 AirPlay 等无线传输协议时，就是经常出现断流等现象，体验极差。 </p> 
<p>由于宿舍楼无线环境复杂，每个房间都至少有一个无线路由器，还有大量学校布置的 AP，所以笔者这里将频宽设定成 80Mhz 时也会受到干扰，只能退而求其次信道频宽定为 40 MHz 149 信道。此时的噪声比例仅为 3%， SNR 也提高到了 61 dB，此时握手带宽依然有 600Mbps，完全能满足绝大多数的无线网络使用场景。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_163b6b79d7d0430fa7bf6df8175aa686_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_bce345b0c06640049f488a18384eb23c_img_000" referrerpolicy="no-referrer"></p> 
<p>所以我们<strong>完全可以牺牲 Wi-Fi 的协商速度获得更加稳定的 Wi-Fi 体验</strong>，经过优化后使得 AirPlay 等基于本地局域网工作的协议在体验上也获得了极大的改善。 </p> 
<p>当然我所在的环境算是非常复杂的网络环境了，各位在自己优化的时候切不能按图索骥，还需要结合自己的实际情况来。一般而言： </p> 
<p>正常户型家庭环境 5Ghz 频宽使用 80 MHz 选对信道一般没有问题。而 160 MHz 会和任何存在于 5.2GHz 的 Wi-Fi 互相干扰，所以不是非常纯<a class="project-link" data-id="186586" data-name="净的" data-logo="https://img.36krcdn.com/20210809/v2_efedefef3f9d405ea92899564441aa2a_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/186586" target="_blank">净的</a>环境一般并不推荐开启。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_a33496c3b3d042c5b59258996edf9a0c_img_000" referrerpolicy="no-referrer"></p> 
<p>而如果你和笔者一样在无线环境较为复杂的宿舍亦或者是出租屋中，那么建议选用 40MHz/80MHz 获得更高的连接稳定性。5GHz 下，如果选用 80 MHz，推荐使用 36，64，149，165信道，如果选用 40MHz，则选择更多一些。 </p> 
<p>2.4 GHz 网络则建议使用最小的 20Mhz 频段，以及 1，6 ，11/13 信道。但即使是这样优化体验也未必会很好，会干扰 2.4G Wi-Fi 的东西实在是太多了，所以目前的无线环境笔者极其不推荐使用 2.4GHz 作为家庭主干网络使用。 </p> 
<p><strong>▍多个无线路由器应该怎么设置</strong></p> 
<p>2.4GHz 干扰严重，所以现在主流移动设备都会支持 5GHz Wi-Fi 实现高速无线互联网连接。但 5GHz 的覆盖范围又远小于 2.4GHz，而且一般家庭的弱电箱都位于刚进门的位置，所以家中免不了会存在 5GHz Wi-Fi 信号死角。 </p> 
<p>因此为了让家中有不错的无线环境，较大户型、承重墙比较多或是有信号死角需要改善的情况下，均需要多台 AP 来改善主要活动区域的信号覆盖。但针对多 AP 的环境下优化无线环境是一个更为复杂的事情。</p> 
<h3><strong>信道调节</strong></h3> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_7f0546c5ccd94f9093f96e4835708570_img_000" referrerpolicy="no-referrer"></p> 
<p>当你有多台 AP 时，信号的强度热力图如上图所示，但千万不要被迷惑了，不论是 Mesh 组网还是 AC+AP 的模式，每个 AP 发射的无线信号都是独立且会相互干扰的。 </p> 
<p>所以中间交汇的区域不仅不是信号最强，而相反恰恰的是这部分是干扰最严重的区域。你的另一台 AP 发射的无线信号就如同你邻居家的无线信号一样，会干扰你现在正在上网的设备。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_f006dadcee8f4d2d91b9dd067156b8cf_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>可以看到使用 160MHz 信道干扰严重 </p> 
<p>虽然 Wi-Fi 6 技术引入了 BSS Coloring 这样的技术，但在实际环境中没有足够的证据证实 BSS Coloring 有明显的效果增益。所以我们能做的最直接优化就是：错开不同 AP 之间的<strong>频段</strong>或是让 AP 之间产生的信号无法互相干扰。 </p> 
<p>简单举例而言：如果你选用 40/80MHz 的频宽，可以在 5GHz 三个独立的 80MHz 频段，或者是 6 个独立的 40MHz 上分别分配给不同 AP。 </p> 
<p>如果选用 160MHz 频宽，由于 160MHz 只能使用在 5.2GHz 上，多台 AP 的信号必定会互相干扰，但我们可以使用下文中的「漫游和功率调节」提到的办法进行优化。 </p> 
<p>选择低频宽的信号会让你有较为自由且干扰较小的选择，而 160MHz 虽然会让你获得更高的连接速度，但是对于信号强度和干扰也更为敏感。因此对于一般家用笔者建议在没有高速移动需求的情况下，尽量选择 80MHz 或者一个折中的速度和较为自由的信道选择空间。 </p> 
<p>此外，需要注意的还有这些：</p> 
<p>52-64 信道也就是 DFS 信道也会被一些商业 / 军用高功率设备设备占用，如果你家附近有类似设备，可能会对其造成一定的干扰。</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>5.8GHz 相对「干净」，但是覆盖面积相较于 5.2GHz 略有下降。</p></li> 
</ul> 
<p>当然以上信道优化仅限于支持自由选择信道的 AP 成立，在笔者使用过的家用无线路由器中，Linksys 支持所有信道的自由调节，而<a class="project-link" data-id="121888" data-name="小米" data-logo="https://img.36krcdn.com/20200729/v2_7ad3d765f1d844018b8f4e75c4c8050d_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/121888" target="_blank">小米</a>则在组 Mesh 网络之后封锁了除了 36-48 信道以外所有的信道。另外就是笔者使用过的所有家用无线路由器均不支持在 Mesh 组网之后对于子节点进行细致的调节，有要对子节点进行细致调节的朋友可能需要购买 AP。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_e2472679ed834c4d8bdc196bf70fff0a_img_000" referrerpolicy="no-referrer"></p> 
<h3><strong>功率调节</strong></h3> 
<p>如果不支持信道调节，那怎么排除 AP 之间的信号干扰呢，答案也非常简单：我们只需要让我们常用区域位置上，仅能接收到一台 AP 的信号，就可以保证在这个位置上没有另一台 AP 的干扰，进而拥有一个不错的上网体验。 </p> 
<p>想要做到这一点我们可以：</p> 
<p>优化 AP 之间的放置位置。</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>优化 AP 的发射功率。</p></li> 
</ul> 
<p>放置位置不难理解，无线信号经过空气和各种障碍物均会产生不同的衰减，通过合理布放 AP 的位置，可以让常用活动区域内的信号不打架。 </p> 
<p>而在位置选择不多的情况下，或者使用无线 Mesh 不得不放在主 AP 信号附近的时候，我们可以通过适当调低 AP 的发射功率：比如在小米路由器的设置中，我们可以从「穿墙」改为「节能」以降低 AP 的发射功率，来让强信号只保留在其应该存在的房间中。如此调节，不仅可以优化上网体验，也可以让 AP 之间漫游效率更高。</p> 
<h3><strong>漫游设置</strong></h3> 
<p>当你的移动设备在两个 AP 之间移动时，终端会根据信号强弱在多个 AP 之间快速切换，让终端始终拥有一个好的上网的上网体验，这就是漫游。漫游在切换连接的 AP 时也需要一定的时间，而如果没有无缝漫游的情况下，则需要手动断开与 AP 的连接才能连接下一个 AP。一般而言，实现漫游的主要手段就是通过 802.11k/v/r 协议。 </p> 
<p>802.11k 协议的主要功能是 Radio Resource Measurment。简单来说就是如果当前 AP 型号强度变弱，那么 802.11k 就可以给终端（手机等设备）提供附近的可漫游的 AP 信息。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_2cccfbab57d74f28be64a20c21e58648_img_000" referrerpolicy="no-referrer"></p> 
<p>如果你的 Wi-Fi 支持 Country、Power Constraint、Radio Management (RM) Enable Capabilities 这三个字段则表示它支持 802.11k 协议 </p> 
<p>802.11v 协议的主要功能是允许终端设备交换网络拓扑的信息以及射频环境。简单来说就是，设备会根据当前 AP 的负载状况「考虑」切换到其他 AP 上；AP 也会根据实际情况断开与设备的连接，从而延长电池使用时间。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_537dd642b2f04a819ee4400772628f91_img_000" referrerpolicy="no-referrer"></p> 
<p>如果你的 Wi-Fi 支持 WNM Sleep Mode、BSS Transition 这两个字段则表示它支持 802.11v 协议 </p> 
<p>而 802.11k 和 802.11v 配合使用时能够加快搜索最佳目标 AP 的速度，也是绝大部分 Mesh 路由器普遍支持的两项协议。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_484a95b9660c47f3949961e8a4273069_img_000" referrerpolicy="no-referrer"></p> 
<p>如果你的 Wi-Fi 支持 Mobility Domain 这个字段则表示它支持 802.11r 协议 </p> 
<p>802.11r 的主要功能就是<strong>快速 BBS 切换</strong>（FT，Fast Basic Service Set Transition），简单来说就是简化了终端和 AP 之间连接的过程，让漫游更加迅速。一般而言只有高端的路由器和 AP 才会支持 802.11r 协议，体现在实际使用中就是切换 AP 时丢包丢得更少。 </p> 
<p>需要注意的是，802.11k/r/v 也并不是一个完<a class="project-link" data-id="131482" data-name="美的" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/131482" target="_blank">美的</a>解决方案，当 AP 过于密集的时候，终端会因为信号强度过高而拒绝漫游，因为漫游也会耗费时间，频繁漫游对于终端来说并不划算。通常来说大部分终端在两个 AP 中间的信号强度低于 -65 到 -75dBm 就会自动漫游，所以我们可以用提到的「位置调整」和「功率调节」两个办法让 AP 在适当的位置型号变差，这样漫游也会变得更为顺利。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220318/v2_578b986001384beda3e9eb2730f12e51_img_000" referrerpolicy="no-referrer"></p> 
<p>调整之后发射信号如图所示会<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20210807/v2_966db147ab4646ef82349f069ce61219_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>一个不错的无线环境和漫游体验 </p> 
<p><strong>▍总结</strong></p> 
<p>无线网络是一个非常复杂的问题，本篇内容也仅在信道，频宽，发射功率做一些初级优化。大多数用户的网络环境也不尽相同：对于单 AP 的家庭网络环境，只需要对信道和频宽进行一定调整；多 AP 用户则需要根据周围干扰，使用区域，信号强度，漫游速度等对各个 AP 调整信道频宽以及发射功率。在优化无线网络的时候还是要具体问题具体分析。 </p> 
<p>写到这里可能还是会有很多朋友会有疑问：我应该怎么选择一台家用无线路由器？关于家用 Mesh 无线路由器和 AC + AP 的讨论也一直没有停止过。笔者就从自己使用过的一些 AP 来简单罗列个中优劣： </p> 
<p><strong>家用 Mesh 无线路由器的优点</strong>：</p> 
<p>价格便宜，Mesh 路由器一般包含了路由器，AP，交换机功能，相比于 AC+AP 的方案会显得碗大量多，通常同样 AP 方案的家用无线路由器价格会低于商用 AP。</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>即插即用，通常家用 Mesh 无线路由器会配备手机 APP，入网方面配置起来相对轻松适合一般消费者。</p></li> 
</ul> 
<p><strong>家用 Mesh 无线路由器的缺点</strong>：</p> 
<p>组网过程较为繁琐：一般 Mesh 路由器不能直接组成有线回程，需要先用无线回程组网，这个步骤稳定性和简洁度相较于 AC+AP 较差。</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>功能缺失较多：一般 Mesh 路由器会缺失很多比较重要的功能，比如上文提到的信道选择和功率调节以及 802.11r，还有同频下多 SSID 以及基于 SSID 的 VLAN 功能。</p></li> 
</ul> 
<p><strong>AC + AP 方案的优点</strong>：</p> 
<p>功能齐全：对于每个 AP 都可以细致调节发射功率/信号频宽与频段，可以发射多个 SSID 以及划分 VLAN，完全支持 802.11k/v/r 协议。</p> 
<p>管理方便：通过 AC 控制器可以集中管理所有的 AP。</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>组网过程简单：通常情况下 AC+AP 只需要 AP 插上网线并且在 AC 中接管就可以完成组网。</p></li> 
</ul> 
<p><strong>AC + AP 方案的缺点</strong>：</p> 
<p>价格偏高，单个 AP 的价格也要高于家用 Mesh 路由器，还需要配套 PoE 交换机，AC 控制器（现在存在软 AC/云 AC 可以稍微降低成本），总体组网价格高。</p> 
<p>界面不友好，企业级无线方案由于增加了很多功能，UI 对于普通消费者来说并不友好，需要较长的学习过程。</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>对于前期布线要求较高，不过也有一些使用无线 Mesh 技术的 AP 出现，但是选择性和自由度相较于家用 Mesh 路由器较低。</p></li> 
</ul> 
<p>当然如果你觉得你家中网络环境优秀，那么我建议你不需要做任何调整。而如果你经常出现断流，丢包等等糟糕的体验，那么可以尝试跟着本文的步骤一步一步优化你家庭的无线网络。如果你周围的无线环境过于复杂，那么我还是建议你回归有线网络，不管是速度还是稳定性上，有线网络都远胜于无线网络。希望本篇文章可以帮助到苦恼于劣质无线网络环境的朋友。 </p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号 <a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247532120&idx=1&sn=aae385a4642cc2de5b36699ea67c5aa7&chksm=fdb38b32cac402249ead55ff198415cedbfc624067850f19e63e93bfbe866565bc07b55fff8c#rd">“少数派”（ID：sspaime）</a>，作者：EstrellaXD，36氪经授权发布。</p>  
</div>
            