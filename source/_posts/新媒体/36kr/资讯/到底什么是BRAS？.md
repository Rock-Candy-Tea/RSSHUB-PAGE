
---
title: '到底什么是BRAS？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220317/v2_badde6bd563f4bfbb2ee2bdc5ac9cbc9_img_000'
author: 36kr
comments: false
date: Fri, 18 Mar 2022 00:18:07 GMT
thumbnail: 'https://img.36krcdn.com/20220317/v2_badde6bd563f4bfbb2ee2bdc5ac9cbc9_img_000'
---

<div>   
<p>大家好，我们今天聊聊BRAS。</p> 
<p>英文好的同学估计会有点懵。因为“BRAS”这个词，在英文里，是“胸罩”的意思。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220317/v2_badde6bd563f4bfbb2ee2bdc5ac9cbc9_img_000" referrerpolicy="no-referrer"></p> 
<p>我们作为通信专业科普公众号，肯定不会研究内衣。今天文章所说的BRAS，是另一个BRAS，全名叫做Broadband Remote Access Server，也就是宽带接入服务器。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220317/v2_d38b2159929848b8a48237aba83ac625_img_000" referrerpolicy="no-referrer"></p> 
<p>顾名思义，BRAS和我们的宽带上网业务有关。事实上，它对每个人都非常重要。如果没有它，我们家里的宽带就无法正常工作，我们也就无法畅游网络世界。</p> 
<h2 label="一级标题" style><strong>什么是BRAS</strong></h2> 
<p>在详细介绍BRAS之前，我们先做<a class="project-link" data-id="428988" data-name="一点知" data-logo="https://img.36krcdn.com/20210812/v2_a8fb2da30d5a41dfa33e8826168edc17_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/428988" target="_blank">一点知</a>识铺垫。</p> 
<p>在以往的文章中，我多次给大家介绍过<strong>传输网</strong>。</p> 
<p>传输网是我们整<a class="project-link" data-id="66837" data-name="个通" data-logo="https://img.36krcdn.com/20210807/v2_4d28d6d2fcf040daba9b7450378c0201_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/66837" target="_blank">个通</a>信网络的底座，负责把各地的家庭用户、政企用户和数据中心连接起来。它也是互联网的主干。</p> 
<p>我们整个传输网，分别是骨干网和城域网。</p> 
<p>骨干网，又分为国家骨干网（一干）和省级骨干网（二干）。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220317/v2_87d294fe6cb0431f820c9ea4bf578fce_img_000" referrerpolicy="no-referrer"></p> 
<p>城域网呢，顾名思义，就是单个城市范围内的通信网络（简称MAN，Metropolitan Area Network）。</p> 
<p>城域网也有进一步细分，分为三层：核心层、汇聚层、接入层。</p> 
<p>我们现在都是光纤上网，每家每户都有“光猫”。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220317/v2_66d4ae7990464417b74640f4771f61e4_img_000" referrerpolicy="no-referrer"></p> 
<p>我之前和大家介绍过，“光猫”学名叫做ONT，属于PON（Passive Optical Network，无源光网络）系统。而PON系统，属于城域网的接入层。（关于PON，详细看这里：链接）</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220317/v2_95987c01c3db4adabf53e1c8bebaad02_img_000" referrerpolicy="no-referrer"></p> 
<p>PON，说白了，就是把一根光纤变成N根光纤，实现千家<a class="project-link" data-id="4262191" data-name="万户" data-logo="https://img.36krcdn.com/20220120/v2_ffbbd669626a4da79275bc62b3e737bc_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4265801011?mp=zzquote" target="_blank">万户</a>的“光连接”。</p> 
<p>大家可能会想到路由器。路由器也是分发和聚合的作用，一根网线变成N根网线。</p> 
<p>那么，PON是不是一个“光纤版”的路由器呢？</p> 
<p>准确来说，不是。</p> 
<p>PON是底层的系统，它只管光，只负责把光送到你家。换句话说，它只是把水管接到你家里，但是，水管里并没有水。</p> 
<p>想要有水，你必须先去自来水公司开户。</p> 
<p>于是，我们就需要<strong>BRAS</strong>。</p> 
<p>大家如果捣鼓过无线路由器或光猫，那么一定对这个界面很眼熟：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220317/v2_055727778a7648379c1a6b83127b74b7_img_000" referrerpolicy="no-referrer"></p> 
<p>是的，PPPOE拨号的界面。</p> 
<p>输出用户名密码之后，点拨号，成功了，就能上网了。如果不拨号，仅仅是网口亮了灯，你还是无法上网的。</p> 
<p>这个PPPOE拨号，相当于就是你告诉运营商你的宽带账户信息，然后让运营商给你拧开水管，送水上门。</p> 
<p>这就是一个典型的认证鉴权过程。BRAS最主要的作用之一，就是认证鉴权。</p> 
<p>说白了，如果没有BRAS，运营商就不能对用户进行身份识别，也不能判断用户的权限，更不能对用户进行计费。</p> 
<p>说了半天，BRAS到底在哪呢？</p> 
<p>如下图所示，BRAS一般部署在城域网的核心层。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220317/v2_2943609a521945a3a43a64b714581fc5_img_000" referrerpolicy="no-referrer"></p> 
<p>现在比较流行的分层叫法，也会把BRAS所在的这层，叫做业务控制层。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220317/v2_2bf7e072fcec42fa9ac828f67e552d22_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>CR：Core Router，核心路由器</p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>SR：Service Router，业务路由器</p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>SW：Switch，交换机</p> 
<p>从组网图也可以看出，BRAS是接入网和骨干网之间的桥梁。它是一个网关，牢牢控制着用户的数据进出骨干网。换句话说，它就像一个高速公路的收费站，对用户进行管理和计费。</p> 
<p>它再往上，就是骨干网的核心路由器CR，是整个城域网流量的出入口。</p> 
<p>用户如果想要上网，首先要确保PON的光通路是OK的。然后，光猫（也可以是无线路由器）和BRAS之间，建立一个<strong>PPP会话</strong>。</p> 
<p>PPP，Point to Point Protocol（点对点协议），是一种数据链路层协议。建立PPP会话后，用户就可以访问互联网（接入骨干网）。</p> 
<p>前面我们说的PPPOE，就是PPP over Ethernet（以前还有PPPOA，也就是PPP over ATM）。</p> 
<p>PPP会话的建立过程如下图所示，都是协议流程，我就不详细介绍了，大家可以查询相关资料。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220317/v2_a86ae33e9f2145f7903decc31950f091_img_000" referrerpolicy="no-referrer"></p> 
<p>BRAS通过与认证系统和计费系统的配合，完成认证和计费功能。</p> 
<p>值得一提的是，为了完成认证，还有一个重要的网元，那就是RADIUS服务器（Remote Authentication Dial In User Service，远程用户拨号认证系统）。上面图中，BRAS收到终端侧过来的用户名密码，就要去找RADIUS认证。</p> 
<p>除了认证、鉴权和计费之外，BRAS还可以用于QoS、安全管理、组播和VPN等。</p> 
<p>它作为宽带网络的控制中心，其实就是<strong>宽带网络的核心网</strong>。它与运营商的运营支撑平台相结合，还能开展很多充满想象力的增值业务，是名副其实的“大管家”。</p> 
<h2 label="一级标题" style><strong>BRAS的发展演进</strong></h2> 
<p>BRAS在ADSL时代就已经诞生了。当时宽带用户数量激增，BRAS有效地简化了网络架构，实现了集中化的管理功能，为宽带业务大爆发奠定了基础。</p> 
<p>后来，它不仅支持了xDSL，还支持Cable Modem、以太网接入（LAN）、无线宽带数据接入（WLAN）、FTTx（也就是刚才我们说的光纤入楼、入户）等多种方式网络类型，支撑了宽带IP网络和ATM网络的数据接入，成为运营商和政企客户的最爱。</p> 
<p>2017年左右，BRAS开始了新的演进变化。</p> 
<p>前面我提到，BRAS其实就像移动网里的核心网。核心网在10多年前，有一个明显的演进，就是控制和转发分离。也就是说，设备进行解耦，控制面和数据转发面分开，各走各的通路。（参考：从2G到5G，核心网，你到底经历了什么？）</p> 
<p>这一趋势，也发生在BRAS的身上。</p> 
<p>传统BRAS，作为网关，既要负责用户管理，也要负责数据流的转发，负担很重，性能很难提升上来。</p> 
<p>而且，BRAS设备的数量很多，随着网络规模持续扩大，还有一些新业务上线，BRAS的维护工作量越来越大。部署新业务的速度，也非常慢，影响网络的长期发展。</p> 
<p>于是，BRAS开始解耦，把将多台BRAS设备上的用户管理功能抽取出来并且集中，形成控制面（Control Plane，简称CP）。BRAS设备上，保留路由器的控制面以及BRAS的转发面，形成转发面（User Plane，简称UP）。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220317/v2_e5150b58f1f54b658d59ed7f36412ad5_img_000" referrerpolicy="no-referrer"></p> 
<p>和移动核心网一样，除了把控制面集中起来之外，还引入了虚拟化（云化），形成了vBRAS。好处和云核心网是一样的，可以灵活进行弹性扩容、缩容，简化运维，统一标准接口，提升设备性能。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220317/v2_d15483600eb349629865c782183fcb6b_img_000" referrerpolicy="no-referrer"></p> 
<p>采用vBRAS之外，转发面也变得灵活。</p> 
<p>对于大流量业务，可采用高性能硬件，分布式部署，满足转发性能需求。对于大session小流量业务，可采用x86云化设备，集中式部署，节约成本。</p> 
<p>vBRAS的出现，体现了城域网云化的趋势。它的底层演进逻辑，和4G/5G移动通信网是一样的。</p> 
<p>值得一提的是，除了形态变化之外，BRAS的定位也有些变化。</p> 
<p>随着设备性能的提升，前面我们看到的在<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>的BRAS和SR（业务路由器），设备功能逐渐融合为MSE（Multi-Service Edge，多业务边缘路由器）或BNG（Broadband Network Gateway，宽带网络网关）。这也是某种形式的合体。</p> 
<p>好了，以上就是关于BRAS的全部内容。感谢大家的耐心观看。</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号 <a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MzI1NTA0MDUyMA==&mid=2456681860&idx=1&sn=ba8dfd1457248d1718863a58f77ff57b&chksm=fda550e3cad2d9f5b3e870309cbf1ae3f7f6b3cec8ccd3b52cbb650e79541edd38da63fddd31#rd">“鲜枣课堂”（ID：xzclasscom）</a>，作者：小枣君，36氪经授权发布。</p>  
</div>
            