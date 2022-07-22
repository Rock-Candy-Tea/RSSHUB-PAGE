
---
title: '很多小功率设备只能A to C 不能C to C充电的原因：终于懂了'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220722/Sa1f6aa72-0e3e-4038-b2d7-a9a8280eb63a.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 22 Jul 2022 20:18:30 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220722/Sa1f6aa72-0e3e-4038-b2d7-a9a8280eb63a.jpg'
---

<div>   
<p><strong>前言</strong></p>
<p>之所以会有这篇内容主要是意外，充电头网办公地点在深圳，高温常伴，即使办公室开着空调但工位上依旧会有小风扇常备。而且小风扇几乎还是那种一直开着的状态，一段时间后小风扇的电池扛不住了，就想着找个充电器给它充电……</p>
<p><strong>都是USB-C充电</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220722/a1f6aa72-0e3e-4038-b2d7-a9a8280eb63a.jpg" target="_blank"><img alt="很多小功率设备只能A to C 不能C to C充电的原因：终于懂了" h="400" src="https://img1.mydrivers.com/img/20220722/Sa1f6aa72-0e3e-4038-b2d7-a9a8280eb63a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>笔者用的小风扇比较“先进”，配备了USB-C充电接口，支持物理盲插，所以就顺手抄起了身边的USB-C数据线给它充电，但换了线和换了方向插就不能充电，这是咋回事？小风扇坏了？不会呀，这是新买的呀，研究了半天才发现原因。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220722/4d9c4739-4b25-41c1-b251-1e77e0253322.jpg" target="_blank"><img alt="很多小功率设备只能A to C 不能C to C充电的原因：终于懂了" h="400" src="https://img1.mydrivers.com/img/20220722/S4d9c4739-4b25-41c1-b251-1e77e0253322.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>在充电头网上班，身边全是100W PD充电器，C2C快充线随处可见，当时就是取了一个C2C快充线搭配PD充电器为小风扇充电，试了好久都无法充电，最后换用了一根A2C的线材搭配USB-A接口的充电器才成功为小风扇充电。</p>
<p>此USB-C非彼USB-C？</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220722/61e7dcc9-833e-42f5-b180-ba6bc5bc6ae7.jpg" target="_blank"><img alt="很多小功率设备只能A to C 不能C to C充电的原因：终于懂了" h="400" src="https://img1.mydrivers.com/img/20220722/S61e7dcc9-833e-42f5-b180-ba6bc5bc6ae7.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>这种情况还是第一次遇见，小风扇不支持C2C的线充电，只支持A2C的线充电，但都是USB-C接口。不知道大家在日常使用时有没有遇到过这种情况，欢迎留言交流。</p>
<p>从目前来看，能解释这种情况的就只有一种可能了，小风扇不支持PD快充协议。</p>
<p><strong>USB PD 快充协议</strong></p>
<p>USB PD的快充电术可以给各种USB接口的设备进行充电，并提供了4种电压规格的能力，包含5V、9V、15V、20V。对于 5V、9V 和 15V 来说，最大的电流为 3A；但在20V 的配置中，普通线缆最大容许的输出是 20V3A 即 60W；假如使用了特别定制的含电子标签电缆，相应的输出功率可以输出到 20V5A 即 100W功率，就如日常给轻薄笔记本等设备充电。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220722/c9123bc6-026d-4e17-878c-73bbd66b1cca.png" target="_blank"><img alt="很多小功率设备只能A to C 不能C to C充电的原因：终于懂了" h="290" src="https://img1.mydrivers.com/img/20220722/Sc9123bc6-026d-4e17-878c-73bbd66b1cca.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
USB PD2.0电压电流等级</p>
<p>USB PD快充连接需要供电设备的是PD适配器，当需要哪一档供电时，会进行供电电压档的调整，而调整的过程是通过PD供电协议“协商”输出，而不是直接提供某种电压的功率。</p>
<p>就像是USB设备被接入通过PD供电规范告诉主机，需要的功率是多少电压电流，然后与电压档位进行握手，然后就提供需要的供电功率供电；并且通讯的过程在USB-C接口中是通过CC（channel configure）线实现，在USB2.0规范中是通过VBUS管脚实现。</p>
<p><strong>小设备的充电</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220722/6a26926c-85fb-403e-9c75-858724481a0a.jpg" target="_blank"><img alt="很多小功率设备只能A to C 不能C to C充电的原因：终于懂了" h="400" src="https://img1.mydrivers.com/img/20220722/S6a26926c-85fb-403e-9c75-858724481a0a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>像风扇、手环、手电等一些小型的用电设备大多都是使用microUSB接口进行充电，一方面是产品本身售价就相对便宜，对于厂商来说肯定要尽可能的削减成本，能省则省；</p>
<p>另一方面，虽然USB-C在目前来看已经大范围普及了，但microUSB接口的市场保有量依旧不可小觑，就连现在一些廉价手机的充电接口都是microUSB。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220722/e98a12b7-e8a0-4c6c-910d-399d4ac2ed3a.jpg" target="_blank"><img alt="很多小功率设备只能A to C 不能C to C充电的原因：终于懂了" h="400" src="https://img1.mydrivers.com/img/20220722/Se98a12b7-e8a0-4c6c-910d-399d4ac2ed3a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>目前USB-C接口已经出现在了各种各样的设备上，手机、平板电脑、笔记本电脑、电动工具，家用电器等等，而现在即使像小风扇、小手电这样价格较便宜的小东西也用上了USB-C充电接口，至少从接口的配置上还是值得称赞的，因为现在在办公室想找一根A to microUSB的数据线已经非常难了，遍地都是USB-C。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220722/16f454c6-5e95-4e8e-a7c3-1361c1d5fcac.jpg" target="_blank"><img alt="很多小功率设备只能A to C 不能C to C充电的原因：终于懂了" h="400" src="https://img1.mydrivers.com/img/20220722/S16f454c6-5e95-4e8e-a7c3-1361c1d5fcac.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>整体来看USB-C充电接口出现在了小设备上是一个好现象，至少不用再费很大的劲去找microUSB数据线了，只需要使用A2C线材就可以小设备充电。</p>
<p><strong>充电头网总结</strong></p>
<p>这次简单的聊了聊小型用电设备配备USB-C接口但却不支持PD快充协议的事情，相信大家或多或少的都遇到过。</p>
<p>小型用电设备搭载USB-C接口是好事，但USB-C端口内部，CC引脚对地并没做下拉电阻，因此无法识别是否接入设备，进而VBUS是没有输出的；猜测是可能受限于成本的原因才导致这一现象，有兴趣的用户可以去查阅之前的USB-C端口拆解文章。</p>
<p>所以如果家里有类似小型用电设备，并且是USB-C充电接口，如果使用PD充电器搭配C2C数据线无法充电的话，可以试试搭配USB-A接口的充电器和A2C数据线使用。</p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：万南</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/chongdian.htm">充电</a><a href="https://news.mydrivers.com/tag/usb_type-c.htm">USB Type-C</a><a href="https://news.mydrivers.com/tag/usb-c.htm">USB-C</a>  </p>
        
</div>
            