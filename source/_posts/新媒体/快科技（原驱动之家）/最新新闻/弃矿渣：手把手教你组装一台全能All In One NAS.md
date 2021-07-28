
---
title: '弃矿渣：手把手教你组装一台全能All In One NAS'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210728/S68fb2cfe-2018-45f3-b814-ac8c13a4c547.png'
author: 快科技（原驱动之家）
comments: false
date: Wed, 28 Jul 2021 19:18:20 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210728/S68fb2cfe-2018-45f3-b814-ac8c13a4c547.png'
---

<div>   
<p><strong>前言</strong></p>
<p>和一些数码大佬相比，我也算是新入NAS坑：18年新家买了群辉218play，后来赶上矿潮，花了群辉218play一半的钱换了一台暴风播酷云二期，刷了黑群918+，稳定用了两年，连媳妇都习惯了不定期同步手机相册到NAS，换新手机也没买大容量，家有NAS着实方便又省钱。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/68fb2cfe-2018-45f3-b814-ac8c13a4c547.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="96" src="https://img1.mydrivers.com/img/20210728/S68fb2cfe-2018-45f3-b814-ac8c13a4c547.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>对于普通家庭用户来说，J3455完全够用了。但对于我这个业余生活家来说，习惯手机里的素材自动同步到黑群辉，写文的时候从电脑资源管理器直接访问黑群相册文件夹，但是照片缩略图半天出不来着实很着急，于是半年前就有了升级J3455的念头。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/9bf317db-698b-43a6-bf98-47e4b8436adf.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="360" src="https://img1.mydrivers.com/img/20210728/S9bf317db-698b-43a6-bf98-47e4b8436adf.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>还有就是NAS升级万兆网络，考虑到内网暂时没有全部升级万兆的必要，不过NAS和主机之间可以局部升级到万兆。</p>
<p>之前暴风播酷云一直和主路由一起放在柜子里，到书房只有一根六类网线，书房还要接无线AP，导致一个万兆交换机也解决不了这个问题，加上最近气温高放在吧台柜里的黑群经常提示硬盘温度过高，所以这次升级直接把NAS放到书房书桌下面，NAS和主机直接万兆直连，散热，NAS机箱大小都不存在问题了。</p>
<p><strong>硬件选择</strong></p>
<p>硬件选择思路和配置，基本是照着大佬@阿文菌 来的，这也是标题“学大佬”的由来。Intel 10代酷睿性能优异，去年底到今年初那段时间价格也很厚道，我的大部分硬件也是当时看着合适就买好了。</p>
<p>不过虽然二季度疯狂涨价，近期价格回落了不少。</p>
<p><strong>1、主板</strong></p>
<p>升级主机空闲出来的七彩虹B460i主板，4月份闲鱼488淘的，支持个人送修，1年换新外加3年保修。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/5a2f8614-c567-462f-9b43-ecd37a06317d.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="521" src="https://img1.mydrivers.com/img/20210728/S5a2f8614-c567-462f-9b43-ecd37a06317d.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>接口配置一个M.2插槽，四个SATA接口，一个PCIe x 16插槽，够我使用了。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/ef453988-a0b1-4cb3-9214-7612253b81a2.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="480" src="https://img1.mydrivers.com/img/20210728/Sef453988-a0b1-4cb3-9214-7612253b81a2.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>不过需要多盘位，需要做软路由的还是建议M-ATX板型，SATA接口更多，两个PCIe插槽，可以扩展多个网卡。</p>
<p><strong>2、CPU</strong></p>
<p>处理器是4月份600元入手的，代号QSRL的10代i5-10400T ES处理器，选择这款处理器的原因主要还是性价比，毕竟双核的i3-7100T现在都要600多。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/6fdb6bbd-abca-46f0-a282-2971bd63d80f.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="394" src="https://img1.mydrivers.com/img/20210728/S6fdb6bbd-abca-46f0-a282-2971bd63d80f.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>QSRL，6核12线程，默频2.0GHz，TDP 35W，UHD630核显，用来做All In One NAS的处理器非常合适。</p>
<p>现在QSRL缺货&涨价，显然价格已经不是很合适了。不过眼睛君找了一下，发现另外一颗代号为QTW3的QS版处理器，也就是i3-10100T的正显版，功能正常的只要480，单通道的只要400，也非常适合用来做NAS处理器。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/e9d99999-a622-4f0c-8398-8a165ee8e015.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="500" src="https://img1.mydrivers.com/img/20210728/Se9d99999-a622-4f0c-8398-8a165ee8e015.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>3、内存</strong></p>
<p>内存是我闲置的，去年低价时候219入手的玖合16G。</p>
<p>玖合(JUHOR) 16GB 2666 DDR4 台式机内存 散热马甲条 星辰系列京东：￥409去看看</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/6d086d42-5e7c-401f-94dd-f4bc4331ad82.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="448" src="https://img1.mydrivers.com/img/20210728/S6d086d42-5e7c-401f-94dd-f4bc4331ad82.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>当时也是想着买两条8G不如买单条16G，其实对于NAS来说，8G就足够用了，就算需要16G内存，买8G*2组双通道也会好一些。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/a156a46f-f07d-4a75-8215-cf6d6d08ae75.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="250" src="https://img1.mydrivers.com/img/20210728/Sa156a46f-f07d-4a75-8215-cf6d6d08ae75.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>对于10代B460芯片组+i5处理器来说，内存频率最高支持到2666，所以购买内存的时候也不用追求高频率，而且2400、2666频率价格也便宜。</p>
<p><strong>4、机箱</strong></p>
<p>因为储存需求不是很大，所以四盘位的NAS机箱就够我用了。蜗牛矿渣以及小厂的做工用料看不上，大厂可选的也不多。</p>
<p>万由的四盘位NAS机箱，万由是专门做NAS产品的，在用的暴风播酷云机箱就是万由代工的。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/5e0aec34-9dee-4821-b717-9f02c428a938.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="266" src="https://img1.mydrivers.com/img/20210728/S5e0aec34-9dee-4821-b717-9f02c428a938.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>还有就是迎广MS04机箱，也是四盘位，支持热插拔。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/39d9379d-13cb-43ce-83f5-6486114b9c40.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="267" src="https://img1.mydrivers.com/img/20210728/S39d9379d-13cb-43ce-83f5-6486114b9c40.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>直到前几天看到了乔思伯N1发布的信息推送，熟悉的外观设计和用料，尺寸170*354*217mm也很小巧。N1这个外形设计，基本算是V8 mini，抽拉式设计，装机友好度高。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/27507c68-d70f-4287-bfb2-0a2f7076dc2c.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="118" src="https://img1.mydrivers.com/img/20210728/S27507c68-d70f-4287-bfb2-0a2f7076dc2c.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>看看这个热度，就知道NAS机箱是有多么的稀缺，乔思伯第一款NAS机箱，爆料推送就上了全站热门。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/8c254933-6e5f-4959-ba03-9d86da6fbad2.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="263" src="https://img1.mydrivers.com/img/20210728/S8c254933-6e5f-4959-ba03-9d86da6fbad2.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>反正我下手了，京东首发649。</p>
<p>乔思伯N1跟之前装机用过的V8设计如出一辙，不过尺寸上小了很多。</p>
<p>乔思伯JONSBO N1小型机箱 电脑台式机 NAS存储多合一 5硬盘6硬盘热插拔服务器机箱 银色京东：￥679去看看</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/263c97ca-d7c3-4b81-9d82-87b673aba515.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="455" src="https://img1.mydrivers.com/img/20210728/S263c97ca-d7c3-4b81-9d82-87b673aba515.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>跟双盘位的暴风播酷云放一起，正面差稍微高了一些，整体长了一些，体积算不上大。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/5a1ad558-a83b-4d9f-bc89-600110830972.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="403" src="https://img1.mydrivers.com/img/20210728/S5a1ad558-a83b-4d9f-bc89-600110830972.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>前IO预留了一个USB3.0 Type-A接口和一个USB3.2 Type-C接口，居然保留了3.5mm音频。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/516bed1b-934f-496e-bef3-9f68102e9e9c.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="427" src="https://img1.mydrivers.com/img/20210728/S516bed1b-934f-496e-bef3-9f68102e9e9c.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>背面，最下是半高PCIe挡板，装个半高显卡，这个小机箱用来做ITX主机机箱也是完全可以。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/935c6fb4-063c-4483-9009-e77fce355a6a.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="414" src="https://img1.mydrivers.com/img/20210728/S935c6fb4-063c-4483-9009-e77fce355a6a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>抽拉式设计，装机比较简单。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/8a229677-7803-4604-8837-f0a86356390e.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="346" src="https://img1.mydrivers.com/img/20210728/S8a229677-7803-4604-8837-f0a86356390e.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>内部安装框架，主要三个分区，前面是5个3.5英寸硬盘位，后面是主板和电源安装位置。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/e1a23a75-3f8b-472c-8ef9-266fe1abb443.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="373" src="https://img1.mydrivers.com/img/20210728/Se1a23a75-3f8b-472c-8ef9-266fe1abb443.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>机箱标配一个14cm大风量风扇，直接给硬盘散热，加上机箱两侧大面积的散热孔，整机散热效果应该可以。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/2aed74a5-0aa9-42e5-9a0b-0e867a1bfa0a.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="386" src="https://img1.mydrivers.com/img/20210728/S2aed74a5-0aa9-42e5-9a0b-0e867a1bfa0a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>硬盘笼有热插拔电源背板，有电阻电容稳压电路，数据接口采用的是SATA直连方式，供电为双D型插头。做工用料号称服务器级别，毕竟数据无价，供电稳定，能够保障硬盘寿命。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/f5ae0eca-d06b-4dcf-a967-0bafa07d7b27.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="491" src="https://img1.mydrivers.com/img/20210728/Sf5ae0eca-d06b-4dcf-a967-0bafa07d7b27.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/75f1b4c1-a0e8-4e8f-949b-ed93368de1ce.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="411" src="https://img1.mydrivers.com/img/20210728/S75f1b4c1-a0e8-4e8f-949b-ed93368de1ce.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>总的来说，649的首发价格，铝制箱体，抽拉式设计，做工用料都要比万由和迎广MS04要强很多。具体使用等后面装机再分享。</p>
<p><strong>5、电源</strong></p>
<p>很多NAS机箱都是1U或者FLEX电源，消费市场根本没有正规产品卖，大部分都是服务器拆机，噪音大质量没保障。乔思伯N1支持SFX电源，由于SFX电源可选性就比较大，这点好评。另外NAS整机功率并不大，300W以内就足够使用。不过还是建议买带80PLUS认证的，能效转换率高，NAS长期待机更省电。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/3c6a50c4-b61e-4e9b-9ea2-0cff9c658758.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="413" src="https://img1.mydrivers.com/img/20210728/S3c6a50c4-b61e-4e9b-9ea2-0cff9c658758.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>手里为主机准备的酷冷至尊V750 GOLD SFX电源还在闲置，所以这次就没有买新的SFX电源，先装到NAS上用。</p>
<p>酷冷至尊(CoolerMaster)额定750W V750GOLD SFX电源(金牌/全模组/全日系电容/加强显卡线缆/质保十年)京东：￥999去看看</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/d13d8eee-1db2-462f-8368-64e33f6d4b04.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="389" src="https://img1.mydrivers.com/img/20210728/Sd13d8eee-1db2-462f-8368-64e33f6d4b04.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>酷冷至尊V750采用工业级全日系电容，全模组电源线，80PLUS金牌认证，10年质保3年免费换新等，如果组装小钢炮主机，这款电源算是比较推荐的一款SFX电源。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/926d14eb-10c8-4ab3-a659-2ee3cda71ca1.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="437" src="https://img1.mydrivers.com/img/20210728/S926d14eb-10c8-4ab3-a659-2ee3cda71ca1.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>SFX电源体积真的是小。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/073a21c7-4e09-4684-8786-204685db70c9.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="398" src="https://img1.mydrivers.com/img/20210728/S073a21c7-4e09-4684-8786-204685db70c9.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>风扇带自动启停，低温状态下，风扇不工作，整机噪音更低。</p>
<p><strong>6、散热</strong></p>
<p>乔思伯N1机箱最大支持70mm散热，市面上常见的下压式散热基本都能使用。这次使用的是上次立人H88 pro装机使用过的利民AXP90纯铜版。</p>
<p>利民（Thermalright）AXP-90I纯铜版 支持 115x 4热管下压式散热器 全电镀 回流焊 铜底 47高度9cm 风扇京东：￥299去看看</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/84dbdbd8-5d75-43c0-8110-f558d8d78621.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="478" src="https://img1.mydrivers.com/img/20210728/S84dbdbd8-5d75-43c0-8110-f558d8d78621.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>这款散热也算是今年比较热门的下压式散热，不过扣具设计上有些bug，安装后肉眼明显可见的主板弯曲，听说后面版本扣具有改进，能够避免主板PCB弯曲的情况。</p>
<p><strong>7、万兆网卡及跳线</strong></p>
<p>网卡看了一圈，感慨一番万兆普及还要时日。开始看的双电口万兆网卡，价格便宜一些的，要么是HP561FLR-T拆机卡，通过转接卡使用。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/d5dc3935-08d2-42b9-910d-7bfb78a4985e.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="270" src="https://img1.mydrivers.com/img/20210728/Sd5dc3935-08d2-42b9-910d-7bfb78a4985e.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>要么是浪潮服务器拆机卡，接口是PCIe×8+PCIe×1，通过屏蔽后面的PCIe×1金手指，可以直接在普通电脑主板上的PCIe×16插槽上使用。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/ddfc5410-2193-4bc4-857a-3c3679e45bd5.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="440" src="https://img1.mydrivers.com/img/20210728/Sddfc5410-2193-4bc4-857a-3c3679e45bd5.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>两种卡都是intel X540-T2芯片，优点是电口，可以直接使用普通的网线跳线，缺点是都要做魔改，而且普遍评论电口在使用过程中发热量大。</p>
<p>最终还是老老实实地用去年比较热门的洋垃圾广达CX341OCP网卡。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/73540f28-0bfd-4949-ab3e-593c4d2a9323.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="461" src="https://img1.mydrivers.com/img/20210728/S73540f28-0bfd-4949-ab3e-593c4d2a9323.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>两张网卡70包邮，豪华带风扇转接板两套130包邮。总共花费200元两张单光口万兆网卡。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/be481084-39eb-4dce-a358-ea23d98b3239.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="224" src="https://img1.mydrivers.com/img/20210728/Sbe481084-39eb-4dce-a358-ea23d98b3239.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>乔思伯N1的PCIe是半高挡板，而电脑主机是全高挡板，所以买转接卡的时候要注意，让卖家发一高一低各一个。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/00a36486-52a6-437d-9caf-35e63b18752f.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="438" src="https://img1.mydrivers.com/img/20210728/S00a36486-52a6-437d-9caf-35e63b18752f.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>组装好之后是这样的。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/b916424a-531c-4bc8-8611-226a2a053852.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="458" src="https://img1.mydrivers.com/img/20210728/Sb916424a-531c-4bc8-8611-226a2a053852.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>不过这个半高挡板合体后，网卡PCB高出挡板一截，直觉告诉我可能会翻车，后面装机的时候再详说。</p>
<p>跳线淘宝随便买了一条SFP+ DAC直连电缆，1.5m淘宝券后32元包邮。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/b832dc04-36f1-423c-985c-485ecd83a067.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="267" src="https://img1.mydrivers.com/img/20210728/Sb832dc04-36f1-423c-985c-485ecd83a067.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>

<p><strong>配置清单</strong></p>
<p>最终的配置清单如下：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/11166b6e-bd5e-40e9-b30a-ca089caaaf16.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="424" src="https://img1.mydrivers.com/img/20210728/S11166b6e-bd5e-40e9-b30a-ca089caaaf16.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>我这个总价里，机箱和电源就占了一大半，换大部分人都不会这么做，尤其是电源。如果选择非模组低功率的SFX电源，内存和散热上再缩减一下预算，CPU换成代号QTW3的i3-10100T QS处理器（4核8线程，基频3.0GHz，QS正显）。整套配置可以做到2300元。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/95df2776-10cf-4775-867e-87fb72b384b0.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="407" src="https://img1.mydrivers.com/img/20210728/S95df2776-10cf-4775-867e-87fb72b384b0.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>如果不是和我一样执着ITX主板和乔思伯N1这款机箱，选择B460芯片组的MATX主板+普通MATX机箱，CPU换成QTW3单通道版，预算还能再砍700，整套配置只要1500，性能跟我的配置基本无差异。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210728/f5b076dd-14f6-415b-bd6d-cd6669b3acf9.png" target="_blank"><img alt="弃矿渣：手把手教你组装一台全能All In One NAS" h="409" src="https://img1.mydrivers.com/img/20210728/Sf5b076dd-14f6-415b-bd6d-cd6669b3acf9.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>这个价位虽然比不过矿渣，但是硬件性能还是要秒成品NAS，毕竟J4125核心的群辉920+，售价要3000多。</p>
<p><strong>总结</strong></p>
<p>关于价格，自己攒一台家用NAS，不光是追求性价比，有时候也是享受折腾的乐趣，如果你没有组装过电脑，这里其实是不推荐你折腾的，成品的NAS虽然价格高，但是系统配套成熟稳定不用折腾。</p>
<p>关于功耗，很多人会在意这套配置整机的功耗问题！计划下篇装机完成后，会详细测试这套配置的待机功耗。</p>
<p>目前计划是使用两块3.5英寸硬盘，实际功耗要是超过50W，就不考虑24小时待机使用了。当前规划的位置及硬件，并没有计划软路由功能，所以从节能来说，也不用24小时开机。</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/diy.htm"><i>#</i>DIY</a><a href="https://news.mydrivers.com/tag/nas.htm"><i>#</i>NAS</a></p>
<p class="url">
     <span>原文链接：<a href="https://best.pconline.com.cn/yuanchuang/10949679.html#ad=8387">太平洋电脑网</a></span>
<span>责任编辑：万南</span>
</p>
        
</div>
            