
---
title: '为什么谷歌被骂上热搜一点也不冤，详解FLoC背后联邦计算'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210511/v2_bb9688ce13fd42d1b986569e563dbed0_img_000'
author: 36kr
comments: false
date: Tue, 11 May 2021 03:19:59 GMT
thumbnail: 'https://img.36krcdn.com/20210511/v2_bb9688ce13fd42d1b986569e563dbed0_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/C12rTTbJQ5FMQR02D7XGcQ">“CSDN”（ID:CSDNnews）</a>，36氪经授权发布。</p> 
<p>作者 | 马超</p> 
<p>责编 | 欧阳姝黎</p> 
<p>近几天<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>因为一项叫做FLoC的技术而被骂上了热搜，笔者看了一下这是一种基于联邦学习的“用户追踪”技术，可以在不暴露客户隐私的情况下进行用户画像及大数据营销，这项技术对于谷歌这种广告收入占总体营收9成的互联网公司来讲意义重大。</p> 
<p>其实FLoC相比于Cookie从某种程度上讲还是有一定进步的，通过Cookie网站能轻松追踪到用户的所有上网行为，而通过FLoC只能追踪到分类相同的用户组，从这个逻辑上讲今后如果读者突然发现APP突然疯狂向你推荐某些莫名其妙的商品，那很有可能是你所在的用户组中的其它人搜索这种商品的次数比较多。不过Cookie只能给单个网站提供相应服务，但是FLoC的联邦学习将有助于广告商掌握用户组全局的浏览行为。</p> 
<p>凭心而论谷歌这次被骂的并不冤，在没有进行任何说明的情况下谷歌就把上百万用户列为了小白鼠，并且这些试验用户只能在“旧追踪技术”也就是Cookie和“新追踪技术”FLoC之间选择，“不可追踪”的选项被谷歌删除了。而且谷歌遭反弹最强烈的操作是由于担心违反欧盟GDPR的隐私保护法规，这次试用计划并没有在欧盟开展。</p> 
<p>当然笔者更加关注FLoC背后的联邦学习技术，因为笔者突然发现这可是被ARM v9和<a class="project-link" data-id="3968654" data-name="英特尔" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968654" target="_blank">英特尔</a>联合Pick从芯片底层给予支持的黑科技。</p> 
<h2>安全联邦计算-为何被科技巨头Pick </h2> 
<p>之前笔者曾经写过一篇《ARM V9到底强在哪》的文章，其中对于ARM V9的新安全计算技术并没有特别看好。但是在两周前英特尔首任CTO帕特.基辛格重回老东家执掌帅位后推出的Ice Lake-SP也把安全计算的<a class="project-link" data-id="6632" data-name="指令集" data-logo="https://img.36krcdn.com/20210422/v2_eb69c924ba514dfd9d371fea3b2b45d2_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4854500224" target="_blank">指令集</a>SGX列入主推方向，这让我感觉安全计算背后必有看点。</p> 
<p>而且帕特.基辛格与谷歌的关系应该也比较微妙，谷歌母公司Alphabet现任董事长约翰·亨尼斯就是帕特.基辛格在斯坦福的硕士导师。帕特虽然出身寒门，与很多硅谷大佬一样，帕特.基辛格也是在十八九岁、年纪轻轻时就走上了工作岗位，不过与比尔盖茨不同的是，在英特尔的资助下帕特拿到了圣<a class="project-link" data-id="221696" data-name="克拉拉" data-logo="https://img.36krcdn.com/20201111/v2_d5ac2217f96841c780239d06bafa1f0c_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/221696" target="_blank">克拉拉</a>大学的电气工程学士学位和斯坦福大学计算机科学的硕士学位。在出任英特尔CTO后，帕特.基辛格转战Vmware出任CEO，并在上个月初正式回归英特尔。</p> 
<p>我们知道约翰·亨尼斯的另一个身份是RISC之父，因此帕特.基辛格回归之后开启的IDM2.0模式其中这个重要的改变就是可以代工RISC-V和ARM架构的RISC芯片了。</p> 
<p>说回SGX安全计算，其实这项技术的历史已经非常久远了，简单来讲安全计算可以百万富翁问题来表述，假如两个百万富翁街头邂逅，他们都想炫一下富，比比谁更有钱，但是出于隐私，都不想让对方知道自己到底拥有多少财富，如何在不借助第三方的情况下，让他们知道彼此之间到底谁更有钱？针对这个问题，在上世纪80年代，清华大学的姚期智院士提出了解决方案，并因此获取了<a class="project-link" data-id="577369" data-name="图灵" data-logo="https://img.36krcdn.com/20210422/v2_7af949d0a6034f87b8a2327a885c6450_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4781700122" target="_blank">图灵</a>奖，从理论层面证明了多方可信计算问题的可行性。</p> 
<p>但在实践层面多方安全计算依然困扰业界，即使像是<a class="project-link" data-id="24961" data-name="腾讯" data-logo="https://img.36krcdn.com/20201201/v2_016524a9a477434cb3584e1558f3257a_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/24961" target="_blank">腾讯</a>、脸书这样的流量巨头，所无法收集用户全部的行为数据，单靠他们一家社交数据训练不出特别好的模型，而想让亚马逊和阿里的电商数据也都共同都拿出来共享吧，又<a class="project-link" data-id="224203" data-name="有客" data-logo="https://img.36krcdn.com/20210422/v2_80fa382b5f17457a9686ba3f8e8960ec_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4802801031" target="_blank">有客</a>户隐私泄漏的风险。如何在不让其它参与者看到真实数据的情况下进行计算，把姚期智院士的解决方案落地，就成了一个难题。在这个经典问题之下，目前只有蓝象智联的GAIA CUBE等少数几个平台能够做到让数据在不泄露的情况下联合多方的数据进行联合计算并<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>明文计算结果，实现数据的所有权和数据使用权的分离，而且这还都是基于区块链软件技术机制保证安全可信。而谷歌的联邦学习产品FLOC甚至都没有基于区块链设计，FLOC从很大程度上是基于谷歌自身的平台信誉背书，这也难怪人们对FLOC产<a class="project-link" data-id="153854" data-name="生众" data-logo="https://img.36krcdn.com/20201105/v2_c3554ca77dac47e190816cdf7923bdc3_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/153854" target="_blank">生众</a>多质疑。</p> 
<p>而英特尔的SGX和ARM V9则力争从硬件安全角度用户打消顾虑，CPU安全计算实际是给计算机加了一个安全密室，即使拥有最高权限的特权管理员也不能进入安全密室，更无法在安全密室前布放监控。安全密室与外界的一切交互全部要经过加密并进行完整性校验。</p> 
<p>其实英特尔的SGX技术早在几年前就已经实现了，但当时SGX能创建的内存空间只有128M，而目前的AI机器学习模型动辙要上百M，大的甚至要几十上百个G，当时的SGX根本放不下这样的模型，无法在多方安全计算中使用。不过这次Ice Lake-SP最高可以支持1T的安全空间，这种程度的提升将全面拓展SGX的应用场景，比如腾讯就联合北京微芯边缘计算和区块链研究院，将区块链与SGX结合，保障数据安全性，做到最终数据可用不可见。不过话虽这么说，但是笔者还是对于联邦学习的安全性有所顾虑，因为现在的AI重建技术太过强大了。</p> 
<h2>缺陷数据的恢复也没那么难</h2> 
<p>其实回归到百万富翁问题，只要富翁A斗富的次数够多，那么他具体的财富数值就不再是什么秘密了，怎么把这种被损坏了的数据恢复回来，其实这个问题完全是GAN等生成模型的攻击范围。比如如何把打了马赛克的人脸数据恢复回来，目前比较优秀的开源模型是由<a class="project-link" data-id="3969182" data-name="英伟达" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969182" target="_blank">英伟达</a>提出的Partialconv（https://github.com/NVIDIA/partialconv）。</p> 
<p>即使图像丢失了大面积的像素，也能通过Partialconv模型将损失进行修复。之前红遍网络的一键去“马赛克“技术，其实背后都是Partialconv，其效果图如下：</p> 
<p class="image-wrapper"><img data-img-size-val="586,370" src="https://img.36krcdn.com/20210511/v2_bb9688ce13fd42d1b986569e563dbed0_img_000" referrerpolicy="no-referrer"></p> 
<p>其实联邦学习就是用户A与用户B联合进行数据挖掘，但是用户A只有计算结果和自身的数据，但是用户B的数据不可见，但是想推理出用户B的数据似乎也不是不可能，这项技术从本质上讲和A<a class="project-link" data-id="184135" data-name="i换" data-logo="https://img.36krcdn.com/20200729/v2_039c2dd27a7e4187aba90223280187e9_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/184135" target="_blank">i换</a>脸有点像，也就是说用户A有换脸后的结果和自身的面部数据，那么他应该也有机会推测出用户B的数据。值得注意的是目前AI甚至突破了之前的分辨率限制，比如去年年中使用自编码模型技术的AI换脸项目ALAE成功登顶了Github趋势榜（https://github.com/podgorskiy/ALAE），相比于之于的之前的Faceswap以及Deepfakes等换脸项目，ALAE可谓将AI换脸带到了一个新高度，这种最新的技术突破了之前的分辨率极限，可以生成高清的换脸图像，以下是效果图。</p> 
<p class="image-wrapper"><img data-img-size-val="554,282" src="https://img.36krcdn.com/20210511/v2_08ca9f44089e44d198171059997216e8_img_000" referrerpolicy="no-referrer"></p> 
<p>所以说即使是最终数据被打码不可见，可能也很难避免被恢复的最终结果。</p> 
<p>因此笔者最后推荐一下苹果的手机，在IOS中把追踪功能关掉就万事大吉了。而非苹果的用户可以考虑由Opea创始人开发的维瓦尔第（Vivaldi）浏览器。这款浏览器兼容chrome插件，最近颇为良心的还出了阻止你同意cookies的弹窗功能。</p> 
<h3>作者简介</h3> 
<p>马超，CSDN博客专家，<a class="project-link" data-id="8432" data-name="阿里云" data-logo="https://img.36krcdn.com/20200729/v2_8a0d7d1338ac4c8297f29bd457c5521a_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/8432" target="_blank">阿里云</a>MVP、<a class="project-link" data-id="25167" data-name="华为" data-logo="https://img.36krcdn.com/20200729/v2_7c7826d711824e758a8e1511c9d7eecc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25167" target="_blank">华为</a>云MVP，华为2020年技术社区开发者之星</p>  
</div>
            