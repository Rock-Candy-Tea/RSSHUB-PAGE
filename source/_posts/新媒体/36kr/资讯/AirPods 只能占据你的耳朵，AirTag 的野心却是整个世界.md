
---
title: 'AirPods 只能占据你的耳朵，AirTag 的野心却是整个世界'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210511/v2_f3643f6e741e43f3bba385ab03d18dc8_img_000'
author: 36kr
comments: false
date: Tue, 11 May 2021 07:29:06 GMT
thumbnail: 'https://img.36krcdn.com/20210511/v2_f3643f6e741e43f3bba385ab03d18dc8_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/UPuba-uorkYuDhJalgJjaw">“极客公园”（ID:geekpark）</a>，作者：Jesse，36氪经授权发布。</p> 
<blockquote> 
 <p>UWB 落地在小的功能场景上，它有可能实现更大的梦想吗？</p> 
</blockquote> 
<p>如果你买了 AirTag，可能会发现一件事：发布会上苹果着重介绍的「精准查找」功能，在 AirTag 的使用过程中其实不太重要，至少没有苹果展示的那么重要。</p> 
<p>通过 UWB 技术，iPhone 能精准地定向查找 AirTag，定位距离和方向。听起来很棒，但 UWB 连接的有效范围并不远，实际使用中，这个距离最多只有 10 米左右。超出信号范围，你还是要通过蓝牙连接，控制 AirTag 发出声音，找到它的位置。</p> 
<p>而且只有配备了 U1 芯片的 iPhone 11、12 系列，能够与 AirTag 建立 UWB 连接，更早的 iPhone 也只能通过蓝牙信号查找。</p> 
<p class="image-wrapper"><img data-img-size-val="653,933" src="https://img.36krcdn.com/20210511/v2_f3643f6e741e43f3bba385ab03d18dc8_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">AirTag 基于 UWB 的定向追踪功能，只有 iPhone 11、12 系列能用｜Apple</p> 
<p>作为一种无线连接技术，UWB 并不能取代蓝牙。但苹果显然在往更深处布局 UWB，去年发布的 Apple Watch Series 6 上也配备了 U1 芯片，直到目前，它都没有任何跟 UWB 相关的功能，不能用来查找 AirTag。</p> 
<p>这个做法很不「苹果」，苹果很少往产品里加入「可有可无」的功能，更不会往里面塞用不到的技术。如此看重 UWB 的苹果，卖的到底是什么药？</p> 
<h2>什么是 UWB？</h2> 
<p>UWB 是 Ultra-Wide Band（超宽带）的缩写。</p> 
<p>它本质上和蓝牙、Wi-Fi 一样，也是一种通讯协议。不同点在于，UWB 覆盖的频段很宽，最低 3.1GHz，最高可以达到 10.6GHz，所以被称为超宽频。相比之下，蓝牙的覆盖频段只有 2.402 - 2.480 GHz。Wi-Fi 也是，在 2.4GHz 和 5GHz 下分别有一些很窄的频道。</p> 
<p>当然，实现超宽频覆盖也有代价。UWB 在特定频率下的发射功率相对蓝牙、Wi-Fi 要小很多，只能发射比较短的「脉冲信号」，而不是正弦波，能搭载的信息更少。</p> 
<p>任何一种通讯协议，都是取舍后的结果。UWB 也一样，它牺牲了一定的码率、传输距离，换来了更好的抗干扰性、更快的连接速度、更低的功耗。</p> 
<p>早在 2002 年，UWB 就被美国联邦通讯委员会批准民用。更早的时候，有人认为 UWB 能成为下一代数据传输的标准协议，但在传输距离、速度、功耗、成本上的难以平衡，让它输给了 Wi-Fi。</p> 
<p class="image-wrapper"><img data-img-size-val="900,525" src="https://img.36krcdn.com/20210511/v2_2bafdb8ac24a41528e8cc15d60b15ae9_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">UWB 覆盖的频段比 GPS、蓝牙、Wi-Fi 都宽，但发射功率更低｜ELIKO</p> 
<p>UWB 的发射的是「脉冲信号」，这使它具备了两个独特的功能优势——精准定位和极高的安全性。这两个特性，让 UWB 在沉寂 20 年后，突然有了焕发新生的可能性。</p> 
<p>UWB 发出的是极短的脉冲信号，这意味着 A 设备可以发出的信号里包含一个「时间戳」，B 设备处理信号并回传后，A 设备就能算出信号在空中跑了多久，用时间乘以光速，就等于两设备间的距离。这和雷达测距的原理类似。</p> 
<p>同时，因为 UWB 测得的距离极为精准，如果在设备里放上多根天线，就可以通过不同天线收到信号、测出距离的差值，算出信号在空间上的方向。测距 + 定向，就能实现精准的相对定位。</p> 
<p>除此之外，UWB 的脉冲信号因为在时域上极为精确，所以几乎不可能被拦截、篡改。这让它拥有更高的安全性，可以用来进行高安全级别的连接授权。</p> 
<h2>UWB 有什么用？</h2> 
<p>2019 年秋天，苹果首次在 iPhone 11 上搭载了专门用于 UWB 通讯的 U1 芯片。</p> 
<p>基于 U1 芯片，苹果首先提供了一个应用场景：AirDrop 定向传送。配备 U1 芯片的 iPhone 在 AirDrop 的时候，会尝试建立 UWB 连接，实现「用户指向哪个设备，就将这个设备置顶推荐」，方便用户选择传输文件的对象。当然，这个功能只能在配备 U1 的 iPhone 11 和 12 之间实现，跟 iPad、Mac 无关。</p> 
<p>包括 AirTag 在内，目前 UWB 的应用场景还比较窄，UWB 在 AirDrop、AirTag 产品体验中只占很小一部分。</p> 
<p>AirTag 发售后，有用户发现其实它的说明书上法律声明的年份是 2019，侧面说明 AirTag 可能早就完成了开发，最初是准备和 iPhone 11 <a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210422/v2_9d94d5f89e394f8082c3b500e50c340d_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>发售的。苹果考虑到要让支持 UWB 的 iPhone 更普及一些，才推迟至今发售。</p> 
<p>2020 年 WWDC 上，苹果还将基于 UWB 的「<a class="project-link" data-id="327178" data-name="近场" data-logo="https://img.36krcdn.com/20201114/v2_a2abc862e65742bab3066d407aa41e3e_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/327178" target="_blank">近场</a>交互」功能开放给了第三方开发者。开发者可以利用这个接口实现 iPhone 之间的实时测距、测向。在官方介绍中，苹果提出可以基于这个功能开发一些小游戏，并演示了一个体感「弹球游戏」。</p> 
<p class="image-wrapper"><img data-img-size-val="720,1383" src="https://img.36krcdn.com/20210511/v2_6af94ad2c5e544b7a1fe01e4e6f7991b_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">AirDrop 如果检测到了 iPhone 指向另一台 iPhone，就会将这个人的头像置顶显示｜Apple</p> 
<p>不只是苹果，其他厂商也都在尝试布局 UWB。<a class="project-link" data-id="121888" data-name="小米" data-logo="https://img.36krcdn.com/20200729/v2_7ad3d765f1d844018b8f4e75c4c8050d_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/121888" target="_blank">小米</a>在去年 10 月就提出了基于 UWB 的「一指连」功能。通过在手机和智能家居中植入 UWB 芯片，实现手机指向智能家居设备的同时自动探测，弹出设备的控制菜单，将手机变成一个「智能遥控器」。</p> 
<p>因为 UWB 连接具有较高安全性，它还可以被用来进行各种「解锁」的授权，比如智能门锁和车锁。2019 年 CES 上，三星就发布过一款智能门锁，通过 UWB 功能，实现家庭成员走到门口一米以内时，自动开锁。</p> 
<p>苹果则早已申请了与 UWB 车钥匙相关的专利。2020 年 WWDC 上，苹果推出 iPhone 车钥匙功能，目前是基于 NFC 对汽车进行解锁，需要将手机贴在车的门把手上。如果未来这项功能拓展到 UWB，用户就可以实现不掏手机，靠近汽车自动开锁。相<a class="project-link" data-id="81186" data-name="比目" data-logo="https://img.36krcdn.com/20200729/v2_2de30d2f5ca04d2e88544916251d2bc1_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/81186" target="_blank">比目</a>前主流的无钥匙进入方案，安全性会大大提升。</p> 
<h2>UWB 能成为一种基础设施吗？</h2> 
<p>对苹果来说，拥抱 UWB 技术首先是为了解决 AirDrop、AirTag 这些很「具体」的问题。但这个行业也有着更大的梦想。</p> 
<p>此前 UWB 领域主要的使用场景都是 toB 的，主要为仓库、厂房等场景提供高精度室内定位。这种定位方案需要在室内预先铺设「定位基站」，然后给需要定位的物品、人贴上类似 AirTag 的 UWB 标签，就可以实现客观位置的精确定位。</p> 
<p>耕耘这一领域多年的<a class="project-link" data-id="235767" data-name="全迹科技" data-logo="https://img.36krcdn.com/20210422/v2_ef0c7bbbcdf1472686927d5dac95a521_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4390601013" target="_blank">全迹科技</a> CEO 都延星，在接受<a class="project-link" data-id="28246" data-name="极客公园" data-logo="https://img.36krcdn.com/20210422/v2_893855a90fbc41d29837099321686b63_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4810801131" target="_blank">极客公园</a>采访时表示，如果在苹果的带领下，未来的智能手机都开始标配 UWB 芯片，这种室内定位解决方案将有可能走出 toB 场景，开始进入 toC 领域。很多公共场所，比如大型商场，可以通过铺设 UWB 定位基站，为顾客提供精确的室内导航服务。</p> 
<p>听起来似乎有点遥远，但这其实也曾是苹果探索过的方向。2013 年，苹果推出了基于低功耗蓝牙协议的 iBeacon 室内定位方案，和 UWB 室内定位原理类似，只是通讯协议不同。通过 iBeacon，零售商可以为用户提供室内定位导航服务，也可以触发 iPhone 上的一些动作，比如自动推荐打开 App、接收一些附近售卖的商品信息。</p> 
<p>iBeacon 最终失败了。一方面的原因在于蓝牙用于定位的精度还是不够，在公共场所的抗干扰能力也不够好；另一方面也在于这个使用场景还是相对薄弱了一点，并不是特别硬的需求。</p> 
<p>很难说苹果会不会通过 UWB 复活 iBeacon。但 UWB 已经是苹果技术储备的一个重要部分，隶属于「位置技术」（Location Technologies）团队。在苹果的硬件架构里，UWB 可以被用来确定位置、建立连接、实现功能，它也需要与蓝牙、Wi-Fi、GPS、NFC 等多项技术配合工作。</p> 
<p class="image-wrapper"><img data-img-size-val="770,577" src="https://img.36krcdn.com/20210511/v2_d36ce2af702741e693585876c6fbb782_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">很难说当年 iBeacon 的失败到底是技术不行，还是场景本身难以立足，这个问题的答案决定了苹果是否要用 UWB 复活 iBeacon｜Apple</p> 
<p>有人可能会感到担心。苹果从来都是一个崇尚「简洁」的公司，有着严格的「技术审美」，只有认定了一项技术能够服务于功能，才会加到硬件里来。像提前布局 UWB 这样的做法，会不会让产品变得越来越臃肿，甚至失去对需求的把握？</p> 
<p>问题的答案可能不在于技术。就像 AirDrop 和 AirTag，它们背后有着复杂的技术逻辑，但从用户视角去看，它们用起来都是极为直观、简洁的。今天的智能手机已经不像十年前，技术和功能之间有明确的对应，光线感应器就是用来调屏幕亮度，重力感应器就是用来调整屏幕方向。</p> 
<p>今天智能手机的很多功能和技术都没有明确的对应关系。比如苹果会综合 Wi-Fi、蓝牙等无线信号的强弱变化、感应加速度，来判断用户是不是在开车，开启驾驶模式。回到 UWB 上，苹果保持了产品上的克制，并没有为 AirTag 乱加功能。但毫无疑问，苹果也在持续思考，如何将 UWB 这项技术用得更好。</p> 
<p>这才是最值得期待的部分。</p>  
</div>
            