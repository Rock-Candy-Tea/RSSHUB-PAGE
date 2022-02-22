
---
title: 'Swift团队把Swift之父气跑了，网友：Python之父的仁慈独裁者模式才是王道'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220222/v2_9d2c52c4d9f54d4ab205ee25af3852fe_img_000'
author: 36kr
comments: false
date: Tue, 22 Feb 2022 09:13:53 GMT
thumbnail: 'https://img.36krcdn.com/20220222/v2_9d2c52c4d9f54d4ab205ee25af3852fe_img_000'
---

<div>   
<p>苹果Swift语言、LLVM编译器之父<strong>Chris Lattner</strong>的<strong>新动向</strong>，引起程序员圈关注。</p> 
<p>这位编译器大神现在与Swift核心团队分道扬镳、彻底退出管理事务的消息引发了大量讨论。</p> 
<p class="image-wrapper"><img data-img-size-val="1012,108" src="https://img.36krcdn.com/20220222/v2_9d2c52c4d9f54d4ab205ee25af3852fe_img_000" referrerpolicy="no-referrer"></p> 
<p>Lattner在Swift官方论坛自曝，离开的原因是团队文化“有毒”。</p> 
<p>其中特别点出，去年夏天<a class="project-link" data-id="478389" data-name="一次视频" data-logo="https://img.36krcdn.com/20210812/v2_ee387ee939074ef4afefceb43a13f8c9_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/478389" target="_blank">一次视频</a>会议上他<strong>被人侮辱</strong>和大喊大叫，而且这已经不是第一次了。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,137" src="https://img.36krcdn.com/20220222/v2_7d6fa189613542cd9f101f3bba4f6210_img_000" referrerpolicy="no-referrer"></p> 
<p>此次冲突后，Lattner渐渐退出了Swift的管理和开发。</p> 
<p>反正他本人还有很多兴趣和事业可忙，不如向前看，眼不见为净。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,99" src="https://img.36krcdn.com/20220222/v2_183a70f94fba4bb6b581684f6072de08_img_000" referrerpolicy="no-referrer"></p> 
<p>现在他正忙着筹备新公司<strong>Modular.ai</strong>，致力于开发AI编译器、运行时等基础设施。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1218" src="https://img.36krcdn.com/20220222/v2_0df02b0a95354aea8a68c8b47e05f1d1_img_000" referrerpolicy="no-referrer"></p> 
<p>啊这，Swift团队具体出了什么问题，竟能把大神给气走了？</p> 
<h2><strong>“语法糖”惹的祸</strong></h2> 
<p>Lattner五年前就已不再是苹果正式员工，先后做过<a class="project-link" data-id="132410" data-name="特斯拉" data-logo="https://img.36krcdn.com/20200729/v2_e76e3d3d44c440138f072b13bc84a6dc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/132410" target="_blank">特斯拉</a>自动驾驶软件VP、<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>Tensorflow基础设施主管、SiFive工程总裁。</p> 
<p>不过Swift这门亲手研发的编程语言他心里一直放不下，坚持每周参加例会、参与社区讨论，也亲自编写和迭代了许多代码。</p> 
<p class="image-wrapper"><img data-img-size-val="800,800" src="https://img.36krcdn.com/20220222/v2_5570378c8044454baecccd3262b21f78_img_000" referrerpolicy="no-referrer"></p> 
<p>Swift语言逐渐发展壮大，接替老的Objective-C成为许多公司开发新iOS应用的首选语言。</p> 
<p>但这门语言发展的方向渐渐与Lattner的理想出现分歧，比如他的设计理念“简单事物的有效组合”（simple things that compose）就不再流行。</p> 
<p>有这种感觉的不止他一人，一些Swift忠实用户也感到很失望。</p> 
<blockquote> 
 <p>我在Swift上投入了很多，2015-2019年都是社区的活跃成员，看到现在这门语言的发展方向，我有点难过。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="1080,75" src="https://img.36krcdn.com/20220222/v2_b922b62ff189493fb6ed270ce34105ea_img_000" referrerpolicy="no-referrer"></p> 
<p>这位老哥主要不爽的是一些语言特性的添加太过随意和仓促，让编译过程不再透明。</p> 
<p>实际上，引发Lattner自曝退出原因的帖子，也是在讨论是否添加一个<strong>语法糖</strong>。</p> 
<p>一位开发者认为，随意添加语法糖对语言维护者来说不算什么，但带来的混乱会对语言使用者影响很大。</p> 
<blockquote> 
 <p>我不是说这个特性毫无价值，但我不想它被引入成语法糖，这会“折断语言使用者的脖子”。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="1080,156" src="https://img.36krcdn.com/20220222/v2_55b5d58c6cb04c0c9c13536973cf5972_img_000" referrerpolicy="no-referrer"></p> 
<p>随后，他引用了Lattner本人很早以前就发表的一段关于语法糖的思考。</p> 
<p>Lattner认为一门编程语言的主要功能相当于盖房子时的“<strong>砖</strong>”，语法糖相当于填砖缝的“<strong>灰浆</strong>”。</p> 
<p>如果房子主体都盖好了去填缝没啥问题。</p> 
<p>如果砖还没摆全就先抹了大量的浆，那整个房子成了用浆盖起来的，结构不会牢固，以后再想摆砖头也找不到合适的地放了。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,292" src="https://img.36krcdn.com/20220222/v2_9479ea9e316449bdb7745f5111e71e29_img_000" referrerpolicy="no-referrer"></p> 
<p>看来这种分歧在Swift社区由来已久，直到去年夏天那场视频会议，冲突集中爆发。</p> 
<p>Lattner会议上被人骂了以后休息了一段时间，后来找到团队管理层谈话。</p> 
<p>他认为管理层逃避问题、找借口，并明确表示不打算对此采取任何措施。</p> 
<p>后来大神决定暂时离开每周会议，只参与论坛讨论，反正还有很多别的事业可忙。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,138" src="https://img.36krcdn.com/20220222/v2_80b279b588a14206addcd8a242870962_img_000" referrerpolicy="no-referrer"></p> 
<p>不过他发表的意见越来越被核心团队忽视，觉得再这样下去就是浪费时间了，最终彻底离开。</p> 
<p>现在，Swift管理团队正在尝试推出新的社区治理机制来解决问题。</p> 
<p>他们打算参考其他编程语言和<a class="project-link" data-id="4262185" data-name="开源项目" data-logo="https://img.36krcdn.com/20210603/v2_43fe3145b6494227bd8db07dcdc0147b_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/4262185" target="_blank">开源项目</a>的成功经验，重新成立一个专注于语言本身演进迭代的大型工作组，并让更多社区成员能参与决策。</p> 
<p>对于编程语言社区究竟应该如何治理，也有网友发表了自己的观点。</p> 
<p>有人觉得<strong>Python之父</strong>这种“<strong>仁慈的终生独裁者</strong>”模式(BDFL, Benevolent Dictator For Life)才是王道。</p> 
<p>Python之父会听取社区意见，但是最终自己拍板决定。</p> 
<p>这位老哥认为所有不采用BDFL模式的编程语言都会因特性太多变得冗杂。</p> 
<p>因为开发团队每个成员都想把自己的想要的特性添加进去，特性之间的交互带来平方级的复杂度，这样用户就难受了。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,165" src="https://img.36krcdn.com/20220222/v2_6f970e8912b64290b8280355c71b39a8_img_000" referrerpolicy="no-referrer"></p> 
<p>其他网友觉得也有一个例外，<strong>Go语言</strong>不是由仁慈的独裁者管理，但团队始终坚持简洁的设计理念。</p> 
<blockquote> 
 <p>Go语言每个新功能提案都会被仔细权衡和讨论，有些用户觉得更新速度慢的像冰川移动，但我个人挺欣赏这点。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="1080,109" src="https://img.36krcdn.com/20220222/v2_08c230375f1645b78415834d9827a8c0_img_000" referrerpolicy="no-referrer"></p> 
<p>Lattner本人则在Swift官方论坛对此留下了最后一段建议和祝福。</p> 
<blockquote> 
 <p>我认为Swift是一种现象级的语言，有成功和长久的前景，但它肯定不应该是一种社区共同设计的语言，这在立项之初就写进了章程。</p> 
 <p>新的机制听起来有些希望……一个健康和包容的社区有益于Swift的设计和发展。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="1080,175" src="https://img.36krcdn.com/20220222/v2_848dab68917640cbafd9dd0f9c63004c_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>现在创业AI基础设施</strong></h2> 
<p>最后再来介绍一下Lattner现在去忙的新事业。</p> 
<p>Modular.ai，致力于为全世界重构AI基础设施。</p> 
<p>包括编译器、运行时环境，为异构计算设计、边缘和数据中心并重，并专注于可用性。</p> 
<p>最终构建出模块化、可组合和分层架构的人工智能。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,484" src="https://img.36krcdn.com/20220222/v2_6a4c4ab2eb7c4f77883a375ea2e62304_img_000" referrerpolicy="no-referrer"></p> 
<p>公司的共同创始人及首席产品官<strong>Tim Davis</strong>，此前在谷歌团队参与了TF Lite、 Android ML、NNAPI等项目的编译器开发。</p> 
<p class="image-wrapper"><img data-img-size-val="936,792" src="https://img.36krcdn.com/20220222/v2_10ddc92136b6448fb749226e711870d5_img_000" referrerpolicy="no-referrer"></p> 
<p>新公司正在全球范围内招聘大量编译器、运行时、ML Ops和框架方向的开发者，以及产品经理和云计算工程师。</p> 
<h3>参考链接：</h3> 
<p>[1]https://forums.swift.org/t/core-team-to-form-language-workgroup/55455/6</p> 
<p>[2]https://news.ycombinator.com/item?id=30416070</p> 
<p>[3]https://forums.swift.org/t/pitch-2-light-weight-same-type-requirement-syntax/55081/126</p> 
<p>[4]https://www.modular.ai/careers</p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/Mjewm3x7NBi58ST54ii2YA">“量子位”（ID:QbitAI）</a>，作者：梦晨，36氪经授权发布。</p>  
</div>
            