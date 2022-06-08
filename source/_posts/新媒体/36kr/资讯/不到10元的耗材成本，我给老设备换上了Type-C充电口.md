
---
title: '不到10元的耗材成本，我给老设备换上了Type-C充电口'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220608/v2_7bdaf829e1d04f9486580a470012ecc1_img_000'
author: 36kr
comments: false
date: Wed, 08 Jun 2022 05:09:26 GMT
thumbnail: 'https://img.36krcdn.com/20220608/v2_7bdaf829e1d04f9486580a470012ecc1_img_000'
---

<div>   
<p><strong>安全提示</strong>：本文涉及电子产品的充电接口及电路改装，有可能产生安全隐患，改造过程仅供参考。</p> 
<h2><strong>背景</strong></h2> 
<p><a class="project-link" data-id="1735563305144195" data-name="我家" data-logo="https://img.36krcdn.com/20200426/v2_c2e6eae068ea4ed8b1e7ac191b7b02a4_img_jpeg" data-refer-type="1" href="https://36kr.com/project/1735563305144195" target="_blank">我家</a>里的许多旧设备，都是 Micro-USB 充电口，即便现在去买一些电子产品（如充电台灯），许多设备依旧脱离时代的步伐，还在使用 Micro-USB 充电口，这让我相当反感，但又不得买。</p> 
<p>作为一个强迫症，我恨不得将所有的 Micro-USB 都改为 Type-C 充电口。在查找了许多资料后，我发现许多人都尝试过，但多数改得不太理想，不够完美、通用。</p> 
<p>在经过更多的资料查找、多次实践、改进后，我总结出了一个比较通用、简单的改装方案，可以将大部分设备的 Micro-USB 充电口改为 Type-C 接口，这样，以后买电子设备时就不会因为它的充电接口太老旧而烦恼了。</p> 
<p>我知道，有不少人非常希望把手上的旧设备都更新成 Type-C 充电口，所以我写下这篇文章，详细记录一次改装过程，希望对读者有帮助。</p> 
<blockquote> 
 <p>需要提前说明，这一改造方案只适用于改造充电口，如「蓝牙耳机、音响、手柄、无线键盘、无线鼠标、充电台灯、老人手机……」的充电口，但不适用于需要传输数据的设备（如旧安卓手机）</p> 
</blockquote> 
<p>此次改装的是我三年前买的的 QCY T1 蓝牙耳机，它的充电口没有传输数据的作用，非常适合改装。</p> 
<h2><strong>实践</strong></h2> 
<p>准备工具：</p> 
<ul> 
 <li>万用电表</li> 
 <li>电烙铁、含铅焊锡、金鸡牌助焊剂、吸锡线、酒精、纸巾</li> 
 <li>AB 胶（改性聚丙烯酸酯胶，哥俩好）</li> 
 <li>尖镊子、小螺丝刀、双面胶、手工刀</li> 
</ul> 
<p>准备耗材：</p> 
<ul> 
 <li>Type-C 母座（沉板式，6Pin），淘宝大约 3 毛一个，运费 3 块</li> 
 <li>0603 贴片电阻 5.1KΩ，拼多多 4 块钱 100 个包邮（0603 表示长 0.6 英寸、宽 0.3 英寸，换算下来就是 1.6mm×0.8mm）</li> 
 <li>细导线</li> 
</ul> 
<p>先处理下 Type-C 母座，取一个 Type-C 沉板式 6Pin 母座，以及两个 0603 规格的 5.1kΩ 贴片电阻：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_7bdaf829e1d04f9486580a470012ecc1_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">左母座，右电阻</p> 
<p>在动手之前，要先搞清楚母座的 6 个 Pin 的定义，在购物界面会有图纸描述，这里我作了张图，更容易理解：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_b793210b80ae4c358f05c913f435fc59_img_000" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>这种 6Pin 的 Type-C 有六个引脚，两个地极（GND）、两个正极（VBUS）、两个 CC，金属外壳与地极是相通的 ，它不能传数据。</p> 
 <p>CC 引脚是 Type-C 用于区分正反面、进行 PD 握手的。如果两个 CC 引脚没有接 5.1kΩ 电阻（下拉电阻）接地，PD 充电器就会拒绝供电（C to C 充电线就用不了）。</p> 
 <p>所以在这一次改装中，需要手动焊接两只贴片电阻。焊接贴片电阻是个精细活，需要练习才能做好，练习 2 小时就够了，要记得勤用助焊剂，含铅焊锡更好操作，电烙铁温度 330 到 350 度就可以。</p> 
 <p>如果焊这两片电阻太难了，也可以省略接电阻这一步。普通的 A-to-C 数据线可以正常供电。</p> 
</blockquote> 
<p>将母座中间的两个 cc 引脚掰起来，再把边上两个 GND 引脚掰下去，方便之后接线：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_560d0dcaa01840b89447796595b95ca5_img_000" referrerpolicy="no-referrer"></p> 
<p>依次将两个 cc 引脚通过贴片电阻接地：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_dc401225ad944ba78eb63cce671c9ab6_img_000" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>在上方引脚定义的地方有讲到，金属外壳与 GND 极是相通的，所以只要用电阻将 CC 引脚与金属外壳连接起来即可完成下拉接地。</p> 
</blockquote> 
<p>接上 PD 充电器的 c to c 数据线，用万用电表测试正极与地极间的电压：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_3b8db77909374ac0990734846a152df1_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">电压正常 5V，说明 CC 下拉电阻焊接完美</p> 
<p>再来处理充电仓。充电仓是卡扣固定的，所以可以用小刀撬，<a class="project-link" data-id="1713078839699968" data-name="拆开" data-logo="https://img.36krcdn.com/20210424/v2_02ad9198b613472b910b038d2f8e6964_img_jpg" data-refer-type="1" href="https://36kr.com/project/1713078839699968" target="_blank">拆开</a>后露出电路板。最好对电路板拍个照，避免最后忘记接线：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_45eb112f037847e2a4b74953bcc18eac_img_000" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>贵重的设备最好及时断开电池，再进行后续操作，以避免意外短路损坏电路。</p> 
 <p>这里我没有将电池断开，是因为已操作熟练，可以确保不会出现短路。（东西便宜，懒得费工夫断电池再接电池了）</p> 
</blockquote> 
<p>要换充电口母座，自然要将旧的母座取下，最好的工具是「风枪」，但由于风枪太大，用的不多，放箱子里占地方，我懒得买它，所以使用「堆锡法」，就是在旧底座上堆一大坨焊锡，利用融化的焊锡，将热量从电烙铁传递到整个母座，取下母座。</p> 
<p>给电烙铁换上 K 刀头，用双面胶将耳机盒外壳固定在桌面上（没有台虎钳也可以稳固操作），在旧母座涂上助焊剂，堆锡，取下 Micro-USB 母座：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_033595d1dcf840d3a396168f23eb310b_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">K 刀头堆锡取 Micro-USB 母座</p> 
<p>用吸锡线清理多余的锡：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_73d07edcdde046eaaa3e74f4b1318861_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">清理焊锡</p> 
<p>Micro-USB 的母座有五个引脚，最右边和最左边那个触点分别是 GND 和 VBus，即负极和正极。仔细观察下，GND 触点是和电路板上的「覆铜层」连着的，它也和固定母座金属外壳的焊点相通，用万用电表的通路检测，可以很容易地判断出正负触点。</p> 
<p>在地线和正极接上飞线（细导线）：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_377bae3e82b947709d8327e1f4b24d05_img_000" referrerpolicy="no-referrer"></p> 
<p>之后，我们要将 Type-C 母座固定到原来 Micro-USB 母座的位置。由于母座的外壳是金属，所以需要在母座和下方的引脚之间做一个绝缘层，以避免下方的引脚处短路。先用酒精和纸巾清理残余的助焊剂，再在引脚处涂上一层 AB 胶，等待五分钟完成固化，就完成了绝缘处理（用酒精将助焊剂清洗掉，就是为了涂上 AB 胶后固定得更牢）：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_3e9f896e86654a8f8411d1aca49f1c2a_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">AB 胶绝缘处理</p> 
<p>下一步，在绝缘层上再涂一层厚厚的 AB 胶 ，将母座固定（固化五分钟），剪短飞线，剥出末端铜丝：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_16f3eaa5e52b4d6e903bfced62b1f1da_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">固定母座，调整飞线</p> 
<p>将正极飞线连接到正极引脚，负极飞线可以直接连接到母座外壳，焊好后插入 PD 数据线，测试通电：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_b357af53488942d688eccdabd78e72c6_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">连线，测试</p> 
<p>之后就是要装壳了，但 Type-C 母座要比 Micro-USB 母座大一些，因此要打磨一下外壳的充电口：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_dc50a00d57c44dcd8428dd9d13f5c82b_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">手劲没控好，磨丑了😥</p> 
<p>最后，装回，测试：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_7c9ae09914f34c97b0549bb989791755_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">测试成功！</p> 
<h2><strong>总结</strong></h2> 
<p>对于简单的 Micro-USB 供电设备，都可以用这种方式改为 Type-C 供电，对外观不会有太大的影响。如果对 C to C 线供电有需要，那就必须要在两个 CC 引脚焊接上 5.1kΩ 电阻接地。这个实践也解释了为什么有些设备无法用 PD 充电器充电，其实就是厂家画电路时忘了设计下拉电阻的电路。</p> 
<p>在这次的改装中，我使用了 AB 胶「哥俩好」，它一方面是优良的绝缘层，另一方面可以如同焊接一样牢固地将母座固定在电路板上。我丝毫不担心它的强度，因为它实在太结实了，老化速度很慢，足够走到这个电子产品寿命的终结。</p> 
<p><strong>⚠ 特别提示</strong>：千万不要用热熔胶、502 固定这种长期有插拔的接口！</p> 
<p>这种改装方式能提供最大 5V 2A 的充电功率，更高功率的快充需要，需要数据功能的支持。而这种改装的不足就是，无法传输数据。</p> 
<p>其实淘宝上有卖能传输数据的 Type-C 母座，它长这样：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220608/v2_413990d724ab43d4ab3fe7babfbac591_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">带传数据功能的 Type-C 母座</p> 
<p>如你所见，这种母座后方带了一小块电路板，后方有「GND、Data+、Data-、VBus」四个触点，背面有 CC 下拉电阻的焊盘。但这种母座体积太大了，如果想改旧安卓手机的充电口，这个母座显然是塞不进去的。</p> 
<p>至此，有了这样一个改装方案，以后再买电子设备，我基本不用纠结它的充电口太旧了。</p> 
<p>在这一次改装记录的过程中，另一个很深的感触就是：人造光和自然光差距真大。这一次的记录中，在室内拍摄电路板时，我已经使用了高显色指数的台灯，但室内与室外的拍摄对比，在色彩、细节上的差距真是好大，远不是调色能弥补的。</p> 
<h3>原文链接：</h3> 
<p>https://sspai.com/post/73056?utm_source=wechat&utm_medium=social</p> 
<p>本文来自微信公众号<a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247536221&idx=2&sn=9b49b4c6fea3bcf53b8ac8a8ce917365&chksm=fdb3bb37cac43221835f7cb1bb058bbe475e5f1c491bc5d4b48b104079a4c2f7bf7912ea8143#rd">“少数派”（ID：sspaime）</a>，作者：淳帅二代，责编：张奕源Nick ，36氪经授权发布。</p>  
</div>
            