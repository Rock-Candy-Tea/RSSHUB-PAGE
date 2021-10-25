
---
title: '产品经理：一个商业云AIoT智能硬件产品的完整拆解'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/PirgfrpWItwdqqkmMedd.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 23 Apr 2020 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/PirgfrpWItwdqqkmMedd.jpg'
---

<div>   
<blockquote><p>本文作者根据自身项目经验，详细复盘了商业云AIoT智能硬件产品项目从0到1的全过程，总结了在项目执行过程中所遇到的问题，分享给大家用以参考学习。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-3753303 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/PirgfrpWItwdqqkmMedd.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">写在前面的话</h2>
<p>笔者从2013年开始进入智能家居领域，这些年磕磕碰碰掉了不少坑，一路走来几乎面对所有要解决的问题都找不到人可以指点，全凭自己交学费。</p>
<p>以前总寄希望能买到一些书籍或者网上资料可以对行业进行系统讲解以获取入行的门道，买了各种名目的书本，有道笔记上收藏的行业文章也达数百篇，到最后发现这些技能都是别人的 Knowhow，愿意真正把有用知识分享出来的并不多。</p>
<p>所以，一直在思考，互联网的精神是什么？不是开放、分享吗？我们现在取得的成绩都是基于前辈的努力成果，如果自己花了如此庞大的精力和金钱代价所解决的问题，又让后人重来一遍，那么这样的社会成本付出是无价值的，It doesn’t make any sense.</p>
<p>以前大学期间就经常帮老师写教学课件，在社团也经常负责学员授课的工作。把学到的知识分享给别人是一件快乐的事情，故而有此篇口水文章的撰写。</p>
<p>注意，<strong>这篇文章面对的读者对象并不是缺乏必要大学课本知识的中学生</strong>，笔者曾经也设想将行业知识进行彻底讲解，但是奈何篇幅实在不够，如果真的要细化知识点到科普水平，那内容厚度差不多要出本书了。</p>
<p><strong>此篇文章的目标是希望能对一个完整涉及到互联网产业上下游的产品进行覆盖性讲解，力争通过尽量少的文字讲明白一个互联网产品各领域所涉及到的知识点。</strong></p>
<p>笔者尽量在<strong>技术原理、行业知识、产品设计</strong>这三个方面之间做出权衡，不过分偏重技术但又避免表面知识，最基本的，会让读者明白未来准备涉及的相应领域要怎么入手。</p>
<p>本文并不携带商业信息，故而隐去了所有涉及公司的真实名称，限于笔者私人时间及内容篇幅，且文笔拙劣，文章不甚完美，错误之处欢迎批评指正。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/1ziM4p2HmJmCZspDA0gw.jpeg" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">一、项目立项</h2>
<h3>1.1 客户背景</h3>
<p>客户来自中国台湾，希望做一个智能语音机器人，并且带宝宝远程视频看护功能，对标大陆这边的智伴机器人和阿尔法蛋。</p>
<p>客户质量方面，其自身积累了大量人脉，与各种渠道商都建立有大量合作，同台湾的一些酒店连锁集团也建立有合作关系，而且在敬老院市场也有相关渠道入口，未来销量保底80K/Year……</p>
<p><strong>客户掏了开案费。</strong></p>
<h3>1.2 需求确认</h3>
<p>由于商务合作内容方面的关系，客户最终要求交 Turn-key 的形式，翻译过来就是：<strong>撒手不管但你最好按我脑子里想的要求去做。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/7l8dMUfny5y8Icki3V4s.jpeg" referrerpolicy="no-referrer"></p>
<p>经多番友好沟通之后，客户最终还是给了一份需求文档：<strong>“你猜猜我要啥&你看着设计呗.docx”</strong></p>
<h3>1.3 自身经验</h3>
<p>一般从零开始做一整套互联网硬件产品，预期时间大约为一年，但是这次客户的期望时间是6个月。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/TYvf395MbcuUUOkMM9qW.jpeg" referrerpolicy="no-referrer"></p>
<p>作为一个纯粹的物联网云服务提供商，此前完全没有硬件及嵌入式开发经验，突然被要求跑去给客户做完整套硬件产品的确是不小的挑战，<strong>况且由于公司内部项目的安排，只有三个程序猿可供我虐待。</strong></p>
<h3>1.4 Get the shit done</h3>
<p>虽然公司业务为云服务，但好在云端系统从一开始就要求为模块化设计，类似现在流行的中台，内部代号为 CloudMeet 。模块化的好处是可以选择组合出各种业务产品云端服务形态。</p>
<h3>1.5 关键性问题</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/DbsZZ7n2tSFyVwHfk49V.jpeg" referrerpolicy="no-referrer"><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/ADFa6hU5iCdOA1iOlGBE.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/iU6IcfsnznZ5B4H647LO.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">二、工业设计（ID）</h2>
<h3>2.1 形象定位</h3>
<p>产品定位为智能语音机器人，面对的是儿童教育市场，所以在产品形象上要考虑小朋友的喜好，无非几种：<strong>动物、卡通、人形机器人。</strong></p>
<p>卡通形象没钱买IP，人形机器人则太直男，<strong>最后选定动物形象：狗子。</strong></p>
<h3>2.2 产品需求确认</h3>
<p>设计方面，找了深圳设计公司A的老王，俗称<strong>王工</strong>；</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/fhextXkybogBzX3E0e0G.jpeg" referrerpolicy="no-referrer"></p>
<p>初步面谈沟通后，告知了设计师产品立项的背景和目标；然后再提供正式的设计需求文档给到王工，说明产品的<strong>设计定位、形象要求、外观设计要求等基本要素。</strong></p>
<h3>2.3 初步设计稿</h3>
<p>在确认需求后，王工开始进行设计，一般工期大概为一周。</p>
<p>常规的设计公司合作方式，<strong>一般是一份设计合同提供三份不同的原型设计</strong>，然后让客户从中挑选一个作为选定方案。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/HXr77UeV1xilZzU3BoWY.jpeg" referrerpolicy="no-referrer"></p>
<p>另外，<strong>比较贱的设计公司会让高水平的设计师设计一份稿件，再让公司实习生或者初级设计师做两份 Bullshit 凑数，</strong>从而让客户能产生一眼就相中的快感。</p>
<p><strong>总之，设计套路深，多看别当真~</strong></p>
<h3>2.4 初次手板</h3>
<p>选定了设计方案后，需要再跟王工进一步沟通细化调整，包括整体尺寸和颜色搭配调整，细节调整完成后，则开始安排制作手板。</p>
<p>手板的意思是验证模型，<strong>将产品的设计纯粹用塑料模型制作出来以便确认实际效果。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/ZoWFJouHWaJd9dq1ENjl.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">CNC雕刻加上喷油可以得出非常漂亮的质感</p>
<p>这部分进行处理的是手板厂的程工，王工给程工提供设计文件，手板类型选择了程工说的最漂亮的CNC雕刻。</p>
<h3>2.5 直男白+中国红</h3>
<p>手板出来后，<strong>跟同事一起左看右看，怎么看怎么好看。</strong></p>
<p>为体现该设计符合市场目标客户的需求，特意带着手板去请一个咖啡店的老板娘鉴赏，她有一个六岁的小朋友，典型的目标客户。</p>
<p>一开场我便激昂而款款地谈论产品的设计创意和市场目标，<strong>终于在口水多过咖啡的交流过程中得出一个结论：</strong><strong>直男设计。</strong></p>
<p>值得反思的是，<strong>毕竟连女孩子的手都没牵过，不能正确理解母婴市场的产品设计原则应该也是情有可原。</strong></p>
<p>于是再去做功课，研究了市场上儿童智能设备的外观设计比例、配色特点。人类视觉上对于“萌”的感觉有会一些关键特征。</p>
<p>比如<strong>：动漫的角色大都具有大眼睛大脑袋短身子</strong>，而人类的婴儿也是类似的特征。</p>
<p>估计不按这种图纸比例生出来的婴儿，在远古时期容易养着养着就被大人撒点孜然烤了，不利于物种繁衍。</p>
<h3>2.6 比例调整</h3>
<p>定出新的设计方向后，然后就是麻烦王工再通宵加班修改了。</p>
<p>首先是比例调整，这次没有再选CNC，而是选择了3D打印。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/szAipe0Kiq8iOeoeAd3u.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">3D打印</p>
<p>对于外观及颜色的初步验证来说，这已经足够，关键是制作周期要短很多（便宜）。</p>
<h3>2.7 颜色调整</h3>
<p>颜色部分遇到了一个问题，就是颜色的具体定义。我们重新选定了淡蓝色和淡粉色两个配色标准，但这两个描述对于设计师而言，<strong>就跟我描述女生的口红色号一样：</strong><strong>不是姨妈红就是牛屎绿。</strong></p>
<p>尝试在网上找色盘去选定色值参数，而王工进行上色设计后，怎么看都不对。反复折腾了王工之后终于还是办法比问题多：<strong>直接从网上买了一对杯子</strong>。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/1Ci9df9IiHuUeYTkUrnY.jpeg" referrerpolicy="no-referrer"></p>
<p>这两只杯子刚好一粉一蓝，而且颜色符合要求，王工直接对着杯子参考。</p>
<h3>2.8 关键性问题</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/tWNvs1C9q7ymXalk1sYV.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/UQGLGzKGrU7wwe4ZWgC4.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">三、结构设计（MD)</h2>
<h3>3.1 设计需求</h3>
<p>ID设计确认之后，下个阶段便是产品内部结构设计，这部分找的是深圳另一家设计公司B的<strong>刘工</strong>。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/09z78GwRgFSpyjjXhie5.jpeg" referrerpolicy="no-referrer"></p>
<p>常规来说一般ID和MD都会选择同一家公司设计，一方面合并费用低一些，另一方面减少沟通成本。</p>
<p>不过由于一些原因，我最终将ID和MD设计分开，所以这阶段会再次产生设计需求的确认工作。</p>
<p><strong>外观部分，ID工程师提供设计的渲染图及对应尺寸标注文件，并注明外观颜色要求；结构部分，电子工程师提供电子结构空间设计要求文档，告知所选用的关键电子元器件尺寸及散热、布局和避空要求。</strong></p>
<h3>3.2 首次结构设计</h3>
<p>因为整体结构比较大，发挥空间充足，<strong>所以首次结构并不需要考虑太多元器件冲突问题。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/7ur7ibsRoKYnZe172maB.jpeg" referrerpolicy="no-referrer"></p>
<p>在ID确定之后，修改MD部分的时候一般由于实际的空间摆放、器件避空等要求，外观都会有调整，这部分由于刘工也做过ID，就一并修改了。</p>
<p>结构设计工作完成就可以进行3D打印做手板，用以确认外观变动、结构实际状况。<strong>一般首次结构实物确认都是体现设计问题，比如螺丝柱遗漏、按键骨架脆弱等。</strong></p>
<h3>3.3 初版结构确认</h3>
<p>在调整结构设计问题之后，再进行3D打印的手板制作，经实物确认即可作为初版的结构定型。</p>
<p>下一步刘工会向电子工程师提供<strong>版框图</strong>，电子工程师根据结构调整原理图及元器件选用，进行后续的电路Layout，电路部分样品制作完成将与结构进行配合验证。</p>
<h3>3.4 0.618</h3>
<p>在第一次拿到电路板正式与外壳手板进行组装之后，总还是觉得外观有所欠缺。</p>
<p style="text-align: center;"><strong> 改 ！！！ </strong></p>
<p>首先是耳朵，感觉上有点偏大，然后按一个毫米的幅度反复调整了两三个版本，尾巴也为了卡哇伊缩短为柯基版本。而最麻烦的是身体比例，<strong>为了头部与身体的视觉协调，反复拜托刘工进行微调，以希望头身比例尽可能逼近黄金分割比。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/SlW2qZMOG6CHhuifV1X8.jpeg" referrerpolicy="no-referrer"></p>
<p>在刘工电脑旁站久了之后，竟然发现他的光头还挺可爱的，不知道他还有头发的时候会是什么样子~</p>
<h3>3.5 MIC位置确定</h3>
<p><strong>（1）单 MIC</strong></p>
<p>产品的麦克风主要作用的机器人唤醒（类似“喂，Siri”）、AI对讲和远程双向通话，物理上要考虑拾音、回声的问题。</p>
<p>一开始结构设计上考虑的是单MIC设计，这种情况下拾音效果最佳的位置是正对用户，<strong>在ID设计初期MIC开孔放在了机器人正面嘴巴的位置。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/QwFExbdrvRrlw3bPMPK9.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">单MIC位置</p>
<p><strong>（2）MIC 阵列</strong></p>
<p>ID阶段制作了手板发现不大美观，所以在MD设计时就放在了铃铛的位置。感觉美观问题总算是解决了客户又提了个小需求：<strong>预留双MIC阵列，提升拾音和回音消除效果。</strong></p>
<p>这个小需求怎么说呢，反正，客户是上帝。于是跑去咨询一个音频算法大牛，<strong>彭工</strong>。大牛表示<strong>要想实现双MIC阵列，在开孔的物理设计上有严格的要求，这会直接关系到拾音的能力、回音消除的效果。</strong></p>
<p>贿赂了两包黄鹤楼之后，刘工终于又修改了结构，<strong>两个MIC的位置最终被放置在了机器人顶部。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/O1WInZWbmRE1UZbvyhRA.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">MIC阵列位置</p>
<h3>3.6 声音系统</h3>
<p>放音喇叭的设计是一套比较系统的工程，牵涉的部分也比较多，关系到：<strong>共振、MIC输入干涉、放音品质、设备重心等一系列考量。</strong></p>
<p>正常来说，为避免SPK放出的声音影响到MIC的输入，<strong>喇叭在设计要尽量远离麦克风并且最好呈背对形式。</strong>比如360小水滴、萤石C2W两种智能摄像头的设计。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/E9ILxWvf8sMSNjYnFg1O.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（1）SPK位置</strong></p>
<p>单MIC正前方设计时，喇叭在机身后的位置影响不大，因为彼此是背对的。</p>
<p>但双MIC布局在脑袋顶部之后，就会发现喇叭和麦克风已经不能背对设计了，那么<strong>SPK就要考虑尽量远离MIC</strong>。</p>
<p>最开始考虑的是放在机身背部下方，刘工修改了之后看效果图还是觉得比较丑。再往上摆，处于脑袋正下方，但由于形状冲突（弧面过小），最终只能选择在脑袋正后方。</p>
<p><strong>（2）SPK选型</strong></p>
<p>在测试声音播放品质过程中，遇到了不少问题。</p>
<p>首先是喇叭的选型，外磁的喇叭价格比较便宜但是重量大，内磁的喇叭轻一些但是价格高。</p>
<p>由于喇叭位置在脑袋正后方，重心靠外，所以为尽量平衡产品的重心问题，选用了一个内磁喇叭，<strong>然而音质测试并不理想。</strong></p>
<p>在测试声音播放品质时，发现不管更换任何测试音频，都有一种声音被闷住无法输出的感觉。</p>
<p>在更换了三四个供应商提供的喇叭还是不满意之后，直接从阿里巴巴上找了十几家喇叭厂商，逐一购买了内磁、外磁的各型喇叭数十个。</p>
<p>在各种喇叭快装满一抽屉之后，<strong>想到了从喇叭开孔问题</strong>。因为不管换了多少种喇叭，声音都处于闷住状态，直接把喇叭开孔全部砸开就没问题，所以只能拜托刘工再从喇叭开孔入手。</p>
<p><strong>（3）开孔设计</strong></p>
<p>在物理上，喇叭的开孔并不是随意而为之，而是有既定的开孔公式进行换算。一开始我们打算单纯增加开孔数量，但是过多的开孔数量会导致孔径变小，这会影响后续的模具问题。</p>
<p>权衡之下，只能尝试在<strong>小量增加开孔数量的同时，更改开孔排列形状</strong>，然后把几个不同形状的喇叭开孔打了手板进行验证之后，但仍是差强人意。</p>
<p><strong>这要上升到玄学的范畴了。</strong></p>
<p>从结构设计师、喇叭供应商、电子工程师都已经无法理解到底是什么原因导致了声音无法出来。看着刘工怨念的眼神，我突然想到<strong>为何不能仿造别家产品的喇叭开孔？</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/r70OIF3h3BSagTMy2LYY.jpeg" referrerpolicy="no-referrer"></p>
<p>于是立即下单买了个小米的米兔，带着一包玉溪又拜托刘工比对米兔的开孔设计修改了一次——声音终于是肯出来了，最后为了音质，还是选定了一个外磁的喇叭。</p>
<p><strong>（4）后音腔</strong></p>
<p>声音能出来之后，虽然音质满意，但是洪量度不够，<strong>又双叒叕请刘工再调整设计，增加了后音腔。</strong></p>
<p>但手板打出来之后测试发现没啥帮助，加上客户考虑到增加的模具费用，最终并未使用后音腔设计，但预留了装配空间。</p>
<p><strong>（5）刘工疯了</strong></p>
<p>鲁迅有讲，“人类的悲欢并不相通” ，深以为然。</p>
<p>坦白来说，<strong>我的确不大知道在修改了26次结构设计之后，刘工心里在想着什么。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/FrjIDIDzLPwELtMpxU6M.jpeg" referrerpolicy="no-referrer"></p>
<p>在雕刻一件艺术品？正在打造一款东半球最棒的智能机器人？不过看起来当时他手里那把<strong>40米</strong>的大砍刀似乎是从瑞士买的。</p>
<h3>3.7 最终设计</h3>
<h3><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/R2eK58BV1S6wSBK7MvVS.jpeg" referrerpolicy="no-referrer">3.8 关键性问题</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/ZkoMcRbBR6d55kOvXgZB.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/14q8tmRN07TS9h2xZJ5a.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">四、模具设计</h2>
<h3>4.1 设计资料</h3>
<p>在结构部分确认之后，刘工将提供ID文件和MD文件给到模具厂的<strong>老陈</strong>，王工再将外观设计要求文档一并给到老陈。</p>
<p>老陈是模具厂的老板，工程出身。虽然是做技术的，<strong>但是实际上是个表面人畜无害，内心猥琐巴拉的老实人。</strong>一般模具报价、生产报价、工期都是老陈直接给出，</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/7I6eJx0krofrgNRWVnz0.jpeg" referrerpolicy="no-referrer"></p>
<p>这次项目由于是Turn-key所以模具报价方面需要代客户沟通。虽然其内心猥琐，但是要在报价上拗过老陈却不是件容易的事。</p>
<p><strong>羊毛不可能出在猪身上</strong></p>
<h3>4.2 砍价</h3>
<p>制造业这行做的多半是酒桌生意，但老陈一向不喜欢应酬，他觉得毕竟请客户吃饭最终也是羊毛出在羊身上，不实在。</p>
<p>我也不喜欢应酬吃喝，一方面毕业几年因为工作的缘故胖成了工伤，另一方面由于家族遗传缺乏乙醇分解酶，基本三瓶青岛就会倒。</p>
<p><strong>但这次老陈带了个业务妹子一起吃饭。</strong></p>
<p>一阵酒桌公式化寒暄客套之后，</p>
<p>我便掉入了陷阱——光顾着跟模具厂老板聊人生谈理想不知不觉就<strong>喝掉了12罐百威。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/IIwXpFdwKUqxFq4ZfZTI.jpeg" referrerpolicy="no-referrer"></p>
<p>推杯换盏之后老陈长什么样已不大记得，代驾回来在平峦山脚的社区医院门口地板直接就躺下了。</p>
<p><strong>睡不着，滚不动，光想着漂亮女鬼。</strong></p>
<p>直到一个多小时后，被Talan叉起了身子，镀着月光回去。</p>
<h3>4.3 开模</h3>
<p>三天后老陈的报价少了四万块，这边<strong>千恩万谢兄弟兄弟</strong>之后，便是付款开模。</p>
<p>一般开模时间取决于模具复杂度和大小，这次包括购买钢材和设计模具在内时间大约在45天。</p>
<p>这玩意大概长成下面这样：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/YOPHuGGpYgjEr3pRhKGC.jpeg" referrerpolicy="no-referrer"></p>
<h3>4.4 试模</h3>
<p>模具制作完成，<strong>模具厂会先购买原料通过注塑机（啤机）试产小数量成品进行验证，</strong>包括外观、结构、颜色相关问题。</p>
<p><strong>（1）触控键</strong></p>
<p>机器人头顶设计有一个触控按键，这个按键需要通过铜皮利用电容效应进行触发，为避免电路触发不够灵敏，所以在铜皮贴合位置的壳子部分进行了减胶做薄处理。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/CdFv0wDb6wkriqtYwxAe.jpeg" referrerpolicy="no-referrer"></p>
<p>由于在壳子上挖了个正方形的矩形坑，导致生产时带来了<strong>缩水的问题</strong>，最后解决的办法是将矩形坑做圆角处理，减轻注胶冷却时各区域收缩不一致问题。</p>
<p><strong>（2）电池仓</strong></p>
<p>机器人支持电池使用模式，为追求终端用户体验设计选用了两颗18650电池组，就是特斯拉上的那种。</p>
<p>这种类型锂电池有较好的稳定性，但是<strong>缺点是偏重</strong>。固定电池的电池仓一开始设计的是两条腿固定，但是实际组装后进行摔落测试发现很容易出现断腿事件，讨论之后只能增加腿的数量到四条，改结构。</p>
<p><strong>（3）耳朵硬度</strong></p>
<p>耳朵一开始为了小朋友摸起来舒服，将硬度设计得很低，这使得耳朵稍微使劲一拽就掉了。</p>
<p>让模厂调整材料，变成硬质形式，又导致机器人很不扛摔，多次修改尝试之后，<strong>最终选定了一个材料硬度系数在保证不被抠出来的同时又让耳朵尽量柔软。</strong></p>
<p><strong>（4）颜色校正</strong></p>
<p>外观颜色方面，虽然ID给了详细的数值，但是实际生产出来的效果仍然还是有细微差距，因为<strong>色粉的值</strong>并不是完全跟计算机图示效果一致，所以最终把王工手里的两个杯子给拿到了模厂进行比对配色。</p>
<h3>4.5 定型</h3>
<p><strong>（1）签样</strong></p>
<p>再多次试模之后，便最终确定模具的设计及生产要求，外壳部分模具厂生产工程师陈小姐，<strong>会出具一份纸质承认书及对应壳子样品，进行签字。</strong></p>
<p><strong>（2）验收标准</strong></p>
<p>而生产部分，我这边会根据讨论，出具一份成品验收标准书给到品质工程师李工，由模具厂、组装工厂、客户（PM）三方进行确认，<strong>其中关键的部分是外观检查标准卡。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/eMGpMp5GKOjZSFjjiPkY.jpeg" referrerpolicy="no-referrer"></p>
<p>因为外壳越大，产生色点和污染的概率越大，外观检查卡用以测定外观污点的尺寸，需要指定一个多方可接受的标准。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/tOpozLhWX3Sl2tjHMMGa.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/WNiNa1ip9CZOlPmwqOoF.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">五、硬件开发</h2>
<h3>5.1 规格确认</h3>
<p>电子部分由东莞一家OEM厂进行配合，电路设计交由该厂的<strong>张工</strong>负责。</p>
<p>张工是河南人，每次看到网上有井盖出现他都要义愤填膺一番，<strong>天天把戒烟戒酒挂在嘴边，但身体从来都很诚实。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/YxlDxHJkTUmc5k9oV34q.jpeg" referrerpolicy="no-referrer"></p>
<p>在张工开始设计之前，我需要先编写产品电子规格文档交给张工，除了产品的功能描述和市场定位，还包括<strong>摄像头参数、点阵参数、电池容量、耳朵颜色</strong>等。</p>
<h3>5.2 设计资料确认</h3>
<p>产品电子规格确认之后，需要组织CPU原厂、嵌入式工程师、电子设计工程师进行讨论，原厂的工程师会告知嵌入式系统的一些特性及电路设计上的要求。</p>
<p><strong>工程师之间的沟通往往比较质朴，闷头讲完画几个白板就是各自留邮箱和微信了，</strong>该阶段原厂这边会将电路设计用到的芯片资料和原理图资料发出来。</p>
<h3>5.3 EVT阶段</h3>
<p>Engineering Verification Test，<strong>该阶段设计纯粹验证电路原理设计及Layout的设计。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/dZH7nYYNsq1T0qTeZxpP.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（1）硬件设计</strong></p>
<p>张工拿到原厂给的资料首先会进行的是电路原理设计。</p>
<p><strong>该阶段硬件第一步目标首先要进行验证性研发</strong>，既完整产品涉及到的所有硬件功能节点都设计到一块电路板上，主要用于原理设计及元器件选型的可行性验证。</p>
<p>原理图设计完成张工会将设计文件发回给原厂，原厂的硬件工程师Evans会进行<strong>原理图的设计review</strong>，以保证张工的原理设计是符合芯片技术要求。</p>
<p>原理图修正并确认后，既可进行PCB Layout设计，将元器件布局到电路上。</p>
<p><strong>（2）洗板</strong></p>
<p>所有设计经过确认之后，便可以交由洗板厂进行PCB洗板，洗板所花费的时间会受到PCB层数的影响，比如从二层板、四层板、六层板所需要的洗板时间会以此增加，费用也会更贵，当然对于硬件性能来说也会更好些。</p>
<p><strong>（3）SMT</strong></p>
<p><strong>PCB洗板完成，物料备齐之后便是上机贴片（SMT）。</strong></p>
<p><strong>SMT是表面贴装技术Surface Mounted Technology的缩写</strong>，SMT贴片指的是在PCB基础上进行加工的系列工艺流程的简称。</p>
<p>电路板通过钢网刷上锡膏之后，由高速贴片机(SMT)将相应元器件贴合至电路板上，该步骤得出的结果便是<strong>PCBA。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/vvwHe4kIXESAzTxszjJG.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">这是机器的样子</p>
<p><strong>（4）组装</strong></p>
<p>将外围器件，比如MIC、SPK、电池等相关器件，通过相应电子连线串接至PCBA上，便可得到一个完整的硬件设备，由于处于EVT阶段，硬件设计与结构无相关性，所以这里组装并不涉及外壳。</p>
<p><strong>（5）测试</strong></p>
<p>该阶段硬件测试主要是电路的工作测试，比如上电之后CPU是否能正常点亮，各种模块的电流、电压是否正确等等。<strong>对于问题的修正，一般用飞线的形式进行操作验证。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/2TYJUHWTJ9HKvpFPQdxt.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">所有的元器件都集合到一个板子</p>
<h3>5.4 DVT阶段</h3>
<p><strong>Design Verification Test，</strong>该阶段修正EVT阶段的电路原理设计，并根据外壳结构进行Layout验证。</p>
<p><strong>（1）设计</strong></p>
<p>在EVT阶段验证通过之后，便可以进行下一阶段的DVT设计。</p>
<p>张工根据EVT的测试结果，重新修正原理图设计并发给原厂review，并根据从设计公司B的刘工那给出的结构版框图重新进行layout，将元器件按正式的外壳结构进行布局。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/Wqgcvkw5T3ppj9DQXk32.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（2）结构验证</strong></p>
<p>该阶段板子洗完并贴片后，即可与初版的外壳手板进行匹配验证。<strong>包括电路板与螺丝柱契合是否正确，结构与板型对于生产方面的简易程度、抗摔性等。</strong>外壳结构及电路布局设计都会进行微调以实现两者锲合度最佳化。</p>
<p><strong>（3）软硬件功能配合开发</strong></p>
<p>电路设计的经过EVT的验证，在DVT阶段修改了layout之后，则开始配合嵌入式、单片机程序进行验证。</p>
<p>单片机、嵌入式程度，对于电路硬件的验证会进行反复调整修正，以确定硬件设计是符合软件要求。同时OEM工厂会与天线工厂完成<strong>天线的位置测定。</strong></p>
<p><strong>这个阶段是整个项目开发的主要工作，基本会占到整个项目开发时间的65%，</strong>硬件、嵌入式、单片机会在这个阶段完成到可试产状态。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/YFAA9FSzcbIL62bAOiRs.jpeg" referrerpolicy="no-referrer"></p>
<h3>5.5 NCC认证</h3>
<p><strong>（1）目的</strong></p>
<p>类似于大陆市场的消费类电子产品需要做3C认证，台湾市场的监管要求电子产品需要做NCC认证。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/2TmyCEaG6Z3Yd3yHeC53.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>对于本产品的认证测试包括：</strong></p>
<p>A.大于1GHz高频的EMC测试，主要是WiFi模块。</p>
<p>B.低于1GHz低频的EMC测试，其他普通元器件。</p>
<p>C.传导发射（Conducted Emission）测试， 通常也会被称为骚扰电压测试，主要是测试连接适配器时对供电系统的影响。</p>
<p>D.静电测试</p>
<p><strong>（2）高频EMC</strong></p>
<p>这里的高频是指大于1GHz的电磁辐射测试，设备中主要是WiFi模块会涉及这个部分测试。</p>
<p><strong>A. WiFi定频</strong></p>
<p>在开始之前首先要对WiFi模块进行定频。这个部分是由WiFi模组厂进行协助处理，负责对接的是彭工。</p>
<p>我们将完整设备带到实验室，彭工首先进行<strong>WiFi功率测定，</strong>将模块的工作功率设定至合理水平，然后将WiFi工作频率和通道进行限定测试，通过之后会给出相应的操作指令文档。</p>
<p><strong>B.辐射测试</strong></p>
<p>这个部分我们找了深圳的一家测试实验室A，对方的测试工程师是个萌妹子，但她强烈要求我称她为<strong>温大侠</strong>。</p>
<p>设备的辐射测试需要将设备<strong>放到一个巨大的屏蔽房</strong>，然后将设备调整到正常运行状态，再测定各频率波段的辐射情况。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/Kt8xygTDu9KiFKBXZ7B4.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">屏蔽房</p>
<p>由于电路在设计之初就考虑到了过认证测试的情况，所以预留了相应设计用于进行屏蔽修改，对于需要增加屏蔽的部分焊上相应参数的磁珠即可。</p>
<p>过程不大顺利，虽然焊磁珠解决了部分问题，但是测试几次都仍然有不能通过的部分。而WiFi的定频测试比较顺利，设定几个频率接入测试设备后都通过了。</p>
<p><strong>（3）低频EMC</strong></p>
<p>在测试实验室A多次修改之后，低频部分都测试不过，需要进行详细的整改。考虑到每个小时高达700软妹币的整改费用，于是我们<strong>靠友谊的友谊的友谊</strong>找到了另一家测试<strong>实验室B</strong>。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/Hn2ZSjDY3LVF22pX5PXG.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">测试实验室B</p>
<p>靠脸皮的关系拜托了<strong>梁工</strong>加班整改，在尝试了调整摄像头驱动等级，给电路板增加磁珠，给连接线增加磁环等各种方式后，对辐射波形进行读点操作终于符合了认证要求。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/1mY7E7tbsiAS34C9l0jf.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（4）传导发射</strong></p>
<p>传导发射（Conducted Emission）测试，通常也会被称为骚扰电压测试，主要是测试连接适配器时对供电系统的影响。这部分也是在测试实验室A完成的，相对比较走运测试一次既通过了。</p>
<p><strong>（5）静电测试（ESD）</strong></p>
<p>Electro-Static discharge，在用户操作设备的过程中，有可能会因为自身的静电而击伤电路元器件，所以还<strong>需要对设备进行静电测试并作出整改以符合标准。</strong></p>
<p><strong>（6）领证</strong></p>
<p>在所有的测试都通过之后，实验室A、实验室B都会分别出具相应的<strong>整改报告</strong>给到OEM厂，由张工根据整改报告将设备进行整改之后，便可以将设备寄送至台湾NCC认证机构进行测试审核，通过之后便可颁发相应证书。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/oeo6XKZpwOXPHPJPVO7R.jpeg" referrerpolicy="no-referrer"></p>
<h3>5.6 PVT</h3>
<p>在DVT及NCC通过之后，便可以进行试产。</p>
<p>Process Verification Test，该阶段的目的：一方面是开始向客户交付测试样机检验功能及稳定性，一方面是开始为批量生产的流程确定标准。</p>
<p><strong>（1）签样</strong></p>
<p>在NCC整改确认之后，量产之前OEM厂首先会要求在生产之前进行<strong>电路板的签样</strong>，以确定原理设计、layout、BOM符合客户要求。</p>
<p>客户签字既锁定版本，OEM厂将以签样标准进行后续生产，如果由于市场原因需要更换物料，则要通知客户确认并重新进行测试签样。该部分签样由OEM厂的生产工程师李工负责对接。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/hKJqHhv4ntPaHWkdVFsM.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（2）最终设计</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/Z07u6P9BtJVz8WNSHR3M.jpeg" referrerpolicy="no-referrer"></p>
<h3>5.7 关键性问题</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/la24AV7JpatQBbtZh2TS.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/m79GncxpkzmeRqlIdtjH.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/nhHEmQ5HMx0if7Z5T7JV.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">六、嵌入式系统</h2>
<h3>6.1 需求确认</h3>
<p>在确认完硬件完整规格后，我这边还需要设计一份系统功能规格文档，用来给嵌入式开发的<strong>Danny</strong>和单片机开发的<strong>Talan</strong>，并且需要开个小会面谈功能以确认功能的理解。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/F5gxY71Fq60GFSvoC6w6.jpeg" referrerpolicy="no-referrer"></p>
<h3>6.2 原厂SDK验证</h3>
<p>从CPU原厂会拿到三样资料：<strong>SDK文件、开发资料文档、evb开发板。</strong></p>
<p>为确保后续开发不引入已知问题，Danny首先在开发板上进行SDK的功能验证，以确保原厂的SDK能正确工作。</p>
<h3>6.3 协议及规格定制</h3>
<p>在正式开发之前，与开发确认完系统功能规格后，为减轻开发的工作量，我还需要定制通信的报文协议及表情、提示音内容。</p>
<p><strong>（1）设备与APP交互指令</strong></p>
<p>该协议用于设备和APP之间进行交互控制，比如查看电量、控制静音等等。</p>
<p>CloudMeet平台本身支持为各种类型的设备提供服务，此前为方便各种厂商设备接入我已经定制了一个通用的协议表，而机器人由于是新增设备，所以还需要增加一些协议，比如儿童锁、睡眠之类的控制。</p>
<p>协议内容采用JSON格式，<strong>支持 HTTP 和 TCP 两种通信类型。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/Cx4LgF3ZcnX0XzGR1MrQ.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（2）单片机与SoC交互协议</strong></p>
<p>SoC处理的功能与单片机不同，所以两者之间也需要进行通信交互。</p>
<p>由于两者走的是 <strong>UART串口</strong>，所以需要自己定义协议。这里我们基于16进制定义了报文头和数据段及报文长度。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/5glW3d4gWs80SyXNNV6g.jpeg" referrerpolicy="no-referrer"><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/3wFNMnjZSaqrKmSyyVjj.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（3）表情规格书</strong></p>
<p>设备的表情由两组8×8 LED阵列进行控制，由 0/1 定义每颗LED灯的亮灭，再逐列进行点亮控制。</p>
<p>由于表情的IC连接在单片机的引脚上，所以表情的执行都通过单片机，我<strong>需要将表情的二进制数据设计出来并转化为单片机可执行的16进制数组。</strong></p>
<p>编号：ID 001 ；含义：笑脸；场景：功能规格书指定；方式：逐列扫描</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/Og1PWeUtQ9HBFQV1FLxR.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（4）提示音规格书</strong></p>
<p>机器人的各项操作都会伴随一些提示音，而这些提示音的编号及音频内容都要定义清楚，并由系统功能规格文档指定调用场景。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/TkJByGPFX1DK5SmJFiDj.jpeg" referrerpolicy="no-referrer"></p>
<h3>6.4 嵌入式开发</h3>
<p>嵌入式开发部分主要是基于Embedded Linux做开发，一些需求快速启动的产品则多半基于RTOS系统，前者是分时操作系统，后者是实时操作系统。</p>
<p>RTOS硬件资源占比小很多，但是开发上限制也很多。Embedded Linux资源占比较大，但是开发难度要低许多，该部分由Danny开发为主。</p>
<p>在正式开发之前Danny会先<strong>编写嵌入式功能设计技术文档，用以定义嵌入式的技术内容，以便未来其他人维护及开发，这会比代码写注释还要重要。</strong></p>
<p><strong>（1）联网模块</strong></p>
<p>该模块主要是解决设备的配网功能，首先通过APP将配网用的WiFi信息生成二维码，然后设备端调用摄像头采集图像并将二维码解码得出对应的WiFi信息。联网程序得到相关WiFi资料后执行联网操作，成功之后再将认证信息提交至CloudMeet系统。</p>
<p><strong>（2）回音消除</strong></p>
<p>回音消除功能(Acoustic Echo Cancellation,AEC)，作用是避免喇叭播放出来的声音又经过麦克风录制到系统，形成回声。该功能模块需要电路设计配合，即硬回采设计。</p>
<p>Codec模块将声音采集电路传入的音频提交到系统，系统再通过相应的AEC算法进行回声消除，从而得到单一的原始播放声音。这部分由SoC原厂的Kason配合算法部分开发。</p>
<p><strong>（3）唤醒模块</strong></p>
<p>唤醒，也叫做“热词”，类似iPhone“喂，Siri”。这个用以设备待机时唤醒设备或者设备执行其他动作时进行打断。</p>
<p>程序首选会进行VAD监测，发现有说话声音后再进入通过ASR进行热词识别，比如模型设定的是“啊猫啊猫”，你叫“啊狗啊狗”设备就不会鸟你。热词唤醒之后才会提交到云端AI进行处理。</p>
<p><strong>（4）NLP模块</strong></p>
<p>AI模块主要是自然语言处理，既NLP。在热词唤醒之后将用户输入音频提交至AI云端，进行语音识别，云端再回复相关内容至设备或执行相应动作。</p>
<p><strong>（5）点播模块</strong></p>
<p>点播模块的作用是用户从APP端H5页面点播内容时，经由CM IoT服务推送至设备端进行播放。</p>
<p><strong>（6）播放模块</strong></p>
<p>设备所有的声音、音频内容都是由播放模块进行处理。由于客户要求较高，需要设备直接播放YouTube连接内容，Danny这边直接用FFmpeg移植到设备端，并进行二次开发。</p>
<p><strong>（7）音视频模块</strong></p>
<p>视频通话这块，因为之前在PC和移动端做过Webrtc，所以一开始曾经考虑将Webrtc移植到嵌入式端。多番讨论后觉得移植成本过大，最终选择了使用P2P通信，走的是RTSP协议。</p>
<p><strong>（8）云存储模块</strong></p>
<p>产品的定位是儿童智能教育+家长看护，所以带有摄像头功能。而CloudMeet本身具有视频云存储服务，所以一开始我们根据需求给客户开发了视频云存储功能，走RTMP协议。</p>
<p>BUT，测试通过后客户想想不对劲，一个儿童故事机为啥需要云存储功能？最后还是取消了，对此<strong>Danny只是嘴角微微上扬了一下……</strong></p>
<p><strong>（9）智能控制</strong></p>
<p>用以控制IoT设备，比如用户唤醒设备后，说出指令：帮我打开窗帘。则机器人会自动发出指令让窗帘自动打开。</p>
<p><strong>（10）按键模块</strong></p>
<p>设备的按键部分由于涉及到电路的控制，由Talan进行处理，从驱动层捕获到按键事件后直接通知Danny的应用层进行处理。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/w9QYSXOFnEFJTjeVEmih.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（11）OTA模块</strong></p>
<p>OTA则是系统固件更新，这个要麻烦不少。根据我之前设定的交互指令，需要先App先从CloudMeet OTA服务处查询可用更新，再将更新信息和指令发送至设备端，设备端验证通过后再将固件下载到设备端，设备再重新系统进入内存模式进行更新系统。</p>
<h3>6.5 单片机(MCU)开发</h3>
<p>单片机相对SoC要低阶很多，但是好处是便宜还能待机，所以一些开关操作都会交给单片机进行处理。这个部分由Talan负责，同时开始之前会先编写一份单片机设计技术文档。</p>
<p><strong>（1）开关机控制</strong></p>
<p>为了美观，设备开关机按键没有使用早期设计的直接控制通断的分立元件，既拨动开关形式，而通过单片机监控。</p>
<p>也就是：<strong>关机模式时，用户长按Power键，触发单片机监测进入计时器，到达预定时长后控制电源模块给SoC上电，Linux系统进行启动，反之亦然。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/UgTLyop3wykdORxluIoD.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">机器人开关</p>
<p><strong>（2）电池管理</strong></p>
<p>电池的充放电管理由硬件控制，但是电流检测及充电状态则由单片机执行，再将结果通信给SoC。</p>
<p><strong>（3）表情模块</strong></p>
<p>根据系统功能规格书，具体到每个行为都会有对应的一个表情，这些表情都通过表情规格书进行编码。</p>
<h3>6.6 测试文档</h3>
<p>功能开发完成后，需要根据功能规格文档编写测试文档进行测试。测试方式是按照一般的操作流程写出预期的正确结果和错误结果，然后完成跑一遍文档的流程以验证测试结果是否符合功能设计预期。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/xJvrnMZrABWpYat0uzFH.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/ljYmL0KgtXA8n39m66VN.jpeg" referrerpolicy="no-referrer"></p>
<h3>6.7 关键性问题</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/e3bEVzD4b9iNV92oPz3V.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/JaQ3SrnBdY79QrscJfok.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/YKbDvZ3uYBhhFuq1SCuF.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/Kwe5FGw7iR5R4ZeUT8y0.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-8">七、云端系统</h2>
<h3>7.1 CloudMeet</h3>
<p>本云端系统在设计的定位上是一种模块化设计，类似现在流行的<strong>中台设计。</strong>该种设计的特点是：<strong>所有的模块都是解耦的，而选用不同功能模块则可以组成不同的云端服务能力。</strong></p>
<p>对于智能机器人产品而言，则是从CloudMeet的模块中挑选出需要的服务，部分欠缺的细节功能再补充开发即可。机器人新增的服务功能部分由Jack负责，流程依然是先提供需求文档然后开发，最后测试验收。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/KSD8RDBNrA2LGFR0RPWe.jpeg" referrerpolicy="no-referrer"></p>
<h3>7.2 AI系统</h3>
<p>一个完整的AI对话系统大致包含四大模块：ASR、STT、NLP、TTS。</p>
<p><strong>（1）ASR（Automatic Speech Recognition）</strong></p>
<p>语音识别，一般简称ASR，其作用是将声音转换为文字的过程。对于机器人而言，语音识别的主要应用方式是远场语音识别（Farfield Voice Recognition），这里我们选用了苏州的一家语音服务商，这部分由苏州的语音服务厂商刘工配合，该服务包含两个主要模块。</p>
<p>1）语音激活检测（VAD）</p>
<p>Voice Active Detection，主要作用是在麦克风持续工作并输入音频的过程中，检测何时才是发生有效的声音输入，识别并消除长时间的静音期。</p>
<p>2）语音唤醒（KWS）</p>
<p>Keyword Spotting，当输入的声音经过VAD处理后，进行语音识别。该识别会判断是否包含用户输入的语音中是否包含关键字，该关键字可认为是机器人设备的“名字”，例如iPhone的“Siri”、亚马逊Echo的“Alexa”等。如果检测语音中包含该关键字，则将设备唤醒。</p>
<p><strong>（2）STT( Speech to Text)</strong></p>
<p>语音识别的一种应用类型，将音频转换成文字。这部分我们仍然选用了苏州的服务商。</p>
<p><strong>（3）NLP(Natural Language Processing)</strong></p>
<p>自然语音处理，通俗的解释就是理解用户到底在说什么。</p>
<p><strong>用户输入的语音通过STT识别为文字时，系统是无法理解内容阐述的是什么，需要进行语义理解，分析出对话所要表达的内容，然后才能安排下一步的回应动作</strong>，比如问答形式回复用户，或者是指令相关控制性指令。</p>
<p>因为目标是台湾市场，所以我们选择了一家台湾的AI服务商，这部分由台湾的AI服务商<strong>Nick</strong>配合。</p>
<p><strong>（4）TTS（Text to Speech）</strong></p>
<p>在NLP系统理解了用户的对话后，需要作出对话回复，该回复一般是即时文字内容生成，对于设备端而言需要播放的是音频，所以需要预先将回复的内容转换为音频再进行进行播放。</p>
<p>一开始用的也是跟STT相同的苏州服务商，但是对方不具备台湾腔的语调。最后我们选用了KDXF的TTS服务，以实现台湾腔调的音频。</p>
<p><strong>（5）完整时序图</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/QtOD5vMW55tKfPVIKJ80.jpeg" referrerpolicy="no-referrer"></p>
<h3>7.3 AIoT系统</h3>
<p>客户的诉求之一是需要通过语音交互实现物联网设备的控制，由于我们之前就有IoT的服务，所以在系统设计上并无太多难度。</p>
<p>最终实现的场景为：<strong>用户通过语音给设备下指令，设备将语音提交至AI系统处理，解析出用户操作指令后调用CM的IoT服务，再由MQTT协议推送至物理设备端以实现交互控制。</strong></p>
<p>比如用户唤醒设备后，下达语音指令：帮我打开电视。机器人收到指令后将命令提交到云端，然后再通过云端控制打开电视机。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/oHAh2CX4citoSHyxF6Kr.jpeg" referrerpolicy="no-referrer"></p>
<h3>7.4 关键性问题</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/KrbbND6NJBKw9mpkGs6y.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/ZQe5GUo0tr2RfJsliIxC.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-9">八、APP客户端</h2>
<h3>8.1 UI设计需求</h3>
<p><strong>（1）功能需求文档</strong></p>
<p>与Jennifer的沟通界面首先要提供一个功能需求文档，并告知产品的市场定位、目标受众、同类型产品参考等。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/eVX1X1N8DYOOgYSvSCpp.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（2）原型设计</strong></p>
<p>根据设计师配合的形式各异，有些设计师仅处理UI部分，不做UX部分设计，这种情况需要PM提供原型设计，我一般会用<strong>Axure。</strong></p>
<p>由于项目工期紧张，为节约时间这里Jennifer会囊括UX的设计，所以这次我并不需要再提供原型。</p>
<h3>8.2 交互要求</h3>
<p>交互部分我一般会有两个基本的设计要求，分别是目标路径、目标成本。</p>
<p><strong>（1）目标路径</strong></p>
<p>所谓目标路径既用户到达其目标的路径。举个例子，对比微信在iOS和原生Android两个系统下启用微信“位置权限”的设定的典型操作。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/b0H8YwhNl5YQiEQaR2dH.jpeg" referrerpolicy="no-referrer"></p>
<p>工程师思维与用户交互思维往往会相左。<strong>工程师会希望保证工程（功能）的整洁性而倾向对功能模块进行收纳、归类、分组，但是这会导致用户操作的目标路径变深变长。</strong></p>
<p>而用户永远追求<strong>“一眼就看到”</strong>的使用需求，操作路径越短越好，但是这对交互设计而言又会使得功能模块过度扁平化形成层次逻辑混乱的焦虑。</p>
<p>但就交互设计的目标而言，永远都是尽可能缩短目标路径。</p>
<p><strong>（2）目标成本</strong></p>
<p>所谓目标成本，是指在用户在目标路径上操作时间成本的数学期望。</p>
<p><strong>做个假设：</strong>微信在未来除了提供普通群聊，还提供更高一级的高级群聊，则目标路径深度分别如下：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/hhRVSt6rrhMZfY8ZJzOb.jpeg" referrerpolicy="no-referrer"></p>
<p>我们假定微信所有的群创建类型都符合幂律分布，选取普通群:高级群=8:2，微信的每一步操作成本计量值为10，则得出目标成本计算公式：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/THaX8mTNTHgthzHU53tc.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>由此可见在不同的设计情况下，应用到用户实际场景中会带来不同的目标成本预期。</strong></p>
<p>所以在设计上，我们希望通过改变用户的交互形式来使得这个成本尽量变小。</p>
<h3>8.3 APP配色风格</h3>
<p><strong>（1）暖色调</strong></p>
<p>由于产品的目标人群是儿童，而APP的目标人群是父母，所以APP的配色风格一开始优先考虑的是暖色调。</p>
<p>我们参考MIUI的设计情景，为了追求暖色调而大量使用橙色、黄色、红色这些配色，<strong>用户初期视觉接触感很好，用久了之后却会形成视觉压力从而造成使用者的视觉疲劳。</strong></p>
<p><strong>（2）安全色</strong></p>
<p>如果花点时间去研究下，我们会发现Facebook、WhatsApp、支付宝、App Store、饿了么、Safari，这些巨型应用的ICON或界面主色调多为蓝色/淡蓝色。而根据调查数据显示，大多数人都喜欢蓝色。在全球范围内来讲，<strong>蓝色也是最安全的颜色。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/6x1h9QFLJX93nDLnUjxu.jpeg" referrerpolicy="no-referrer"></p>
<h3>8.4 视觉稿件</h3>
<p>在确认完设计的相关要求并沟通清楚功能需求后，Jennifer便可开始进行设计。</p>
<p>初版设计完成后会先输出视觉稿件，用以确认功能、配色、交互上是符合预期的。</p>
<h3>8.5 UI FLOW</h3>
<p>视觉稿件经多次修改确认后，在正式输出设计文件之前，先要输出UI FLOW，这是一个完整的交互流程图，除了部分细节弹窗提示，绝大部分的界面跳转都会体现出来。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/prnocCV8kuZ6EQsHjpzN.jpeg" referrerpolicy="no-referrer"></p>
<p>该设计的输出一方面方便设计师自我检查，也方便PM进行二次交互设计确认，最后也需要给到工程师以便于了解完整设计。</p>
<h3>8.6 UI文件输出</h3>
<p><strong>（1）标注文件</strong></p>
<p>在正式切图输出之前，需要对界面设计进行标注，包括元素的宽高、色值、字体等。</p>
<p><strong>（2）切图文件</strong></p>
<p>根据Android系统、iOS系统的规格要求，切图并输出对应分辨率要求的设计元素图片。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/ndI9IX35BttDP53sA0oN.jpeg" referrerpolicy="no-referrer"></p>
<h3>8.7 App功能需求确认</h3>
<p><strong>（1）需求可行性确认</strong></p>
<p>在功能需求文档设计完毕，首先会跟APP开发讨论，Jack和Talan会根据功能需求，告知功能是否可实现及实现的成本。</p>
<p>PM需要再进行功能取舍，一个被揍比较少的PM，都会尽量少提<strong>“APP主题颜色要跟随手机壳颜色变化”</strong>之类的需求。</p>
<p><strong>（2）设计可行性确认</strong></p>
<p>正所谓<strong>“UI动动手，RD跑断腿”，</strong>设计师很多时候会为了追求交互、视觉体验，设计各种酷炫的交互效果，而不顾开发成本。</p>
<p>PM就需要在UI和RD之间的诉求做权衡。所以在跟UI讨论设计方向的初期，就会把UI的设计设想反馈给RD进行可行性确认。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/mYo2bGDztF1JFygrBtOj.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（3）功能规格</strong></p>
<p>需求及设计可行性确认后，将功能需求细化为规格文档，定义出输入边界、操作粒度等细节。</p>
<h3>8.8 开发</h3>
<p>正式开发之前先由Jack编写APP功能设计技术文档，文档用以描述技术开发内容定义，用以iOS和Android进行规格统一。</p>
<p><strong>（1）账户系统</strong></p>
<p>用户用以注册登录账号的功能，一开始给客户提供了<strong>全球手机号+邮件地址的账号体系</strong>，不过后面客户去掉了邮件地址。</p>
<p><strong>（2）点播功能</strong></p>
<p>该功能具体是在APP嵌套一个H5页面，该页面由AI服务商提供，主要是媒体内容，故事、英语、儿歌之类。点击之后由AI服务商的内容服务端向CloudMeet服务端发起请求然后推送至设备进行播放。</p>
<p><strong>（3）看护功能</strong></p>
<p>该功能既是视频监控功能，叫做baby monitor。用户可在APP上远程查看设备的摄像头内容，并且支持双向音频对讲。</p>
<p><strong>（4）设备管理</strong></p>
<p>该功能包括设备配网、添加设备、设备分享、远程控制、OTA升级等功能。</p>
<p><strong>（5）群聊功能</strong></p>
<p>由于机器人具有家庭看护的功能，所以客户要求有一个设备与多个APP端群聊的功能，方便孩子与父母亲进行对话。这部分实际上是IM的功能，消息要支持音频和文字两种。</p>
<p>APP端发出的文字消息则需要经过TTS进行转换才发送至设备。因为以前开发设计过社交软件，这部分并未使用第三方IM服务商，直接由CloudMeet服务解决。</p>
<p><strong>（6）个人设置</strong></p>
<p>个人设置包括一些个人昵称、账号等相关信息。</p>
<p><strong>（7）拨打电话</strong></p>
<p>如果APP端的用户设置了昵称，比如“爸爸”，则机器人被语音呼叫“打电话给爸爸”时，APP端会响起来电，点击接听即可实现APP与设备视频端通话。</p>
<h3>8.9 测试</h3>
<p>APP开发完整需要编写APP测试文档，测试验证功能开发是否正确符合设计需求。在APP上架之前，Android通过APK包形式进行安装测试，iOS则通过<strong>TestFlight</strong>进行测试。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/VnJYHW7m2ys0ISYCaHhG.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/C0MIwpH3pQRwC2i5UYAx.jpeg" referrerpolicy="no-referrer"></p>
<h3>8.10 上架</h3>
<p>App Store的上架比较麻烦，提交上架时需要同时准备账号和设备，以便审核人员进行远程测试验证。Google Play 的上架则要容易一些。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/pzej2Xkd2Qab0MX2qd2u.jpeg" referrerpolicy="no-referrer"></p>
<p>而国内的Android市场则需要在上架时提交<strong>软件著作权登记证书</strong>，这需要提前40天左右准备好。</p>
<h3>8.11 关键性问题</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/kItezzrZ9nuRQhUoMbBK.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/edxRSlm9HUvc3lEgdyth.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-10">九、官网&控制台</h2>
<h3>9.1 官网</h3>
<p>客户的官网比较简单，一个WEB前端页面，包含大屏banner轮播、产品简介等基本内容，并无发布新闻、登录操作等相关后端开发。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/1xKzciP4NObaGc5AWC85.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（1）需求确认</strong></p>
<p>首先跟客户确认要展示的内容，希望的设计以及对应的文字内容及风格确认等。</p>
<p><strong>（2）UI设计</strong></p>
<p>将客户需求整理并告知Jennifer，然后进行设计切图。</p>
<p><strong>（3）开发</strong></p>
<p>由于页面简单，得到切图文件后，Jack使用Bootstrap框架简单为客户开发了一个官网。<strong>需要特别声明的是，logo和banner并不属于我的品位。</strong></p>
<h3>9.2 控制台</h3>
<p><strong>（1）SN号管理</strong></p>
<p>SN号为设备的唯一标示，作为云端服务器识别设备身份是否合法的关键信息，CloudMeet后台提供了该管理功能，包括新SN号导入、删除等。</p>
<p><strong>（2）设备追踪</strong></p>
<p>客户通过不同的渠道销售的设备都希望得到跟踪，所以需要一个设备激活、有效状态、渠道信息等的管理界面，这个也包含在CloudMeet的服务之中，所以客户直接使用即可。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/Hb11noMb1ynx9GpTCcOk.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（3）OTA升级</strong></p>
<p>设备端的固件升级需要经过OTA系统，由客户掌控升级的进度及版本管理，该功能也在CloudMeet服务中提供。</p>
<p><strong>（4）界面内容</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/wdriH02puOlWa20u8Bvr.jpeg" referrerpolicy="no-referrer"></p>
<h3>9.3 Line官方账号</h3>
<p>类似中国大陆的企业公众号和服务号，中国台湾地区主要使用的Line社交软件也具备类似的服务，叫做<strong>官方账号2.0</strong>。我们为客户设计了以下功能：</p>
<p><strong>（1）账户绑定</strong></p>
<p>通过关注Line官方账号，可绑定自身账户。</p>
<p><strong>（2）自动应答</strong></p>
<p>Line的官方账号有聊天机器人功能，在开发者后台预设相应的关键字及回复内容及可自动回复用户的信息，这主要是一些产品信息的基本问答。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/Uiy6sZGks3pIy2gF6vU0.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（3）消息推送</strong></p>
<p>在Line上叫做推播功能，当机器人端呼叫某一APP用户时，除了APP会弹出来电界面，Line官方账号也会提送相关消息给用户。</p>
<h3>9.4 关键性问题</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/4Q72TXI1jwm8JAdRyho5.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/KGJ5Cf29fnoajQyYCwWL.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-11">十、工厂生产</h2>
<h3>10.1 包装设计</h3>
<p><strong>（1）缓冲结构</strong></p>
<p>对于设备的内部缓冲结构，一开始考虑的是珍珠棉，这玩意对于偏大型产品的保护效果好，又比较美观，但是找了好几个厂商后发现价格过高。</p>
<p>又考虑过换成瓦楞盒，但是在样品测试摔落时表现不好，长得也比较廉价，再三考虑钱包问题，最后选用了吸塑。</p>
<p>首先要将完整设备提供给材料厂商李工，用以评估产品重量并进行进行抄数。</p>
<p><strong>抄数的意思是对设备整个外形的尺寸数据进行测量，</strong>然后根据该参数进行制作对应的吸塑模具。</p>
<p><strong>（2）彩盒</strong></p>
<p>外包装彩盒的设计比较简单，我这边先跟客户Mic讨论他的想法，然后Jennifer提供相应的设计图形。</p>
<p>最后整理资料，包括<strong>图形文件、颜色及四面排版要求</strong>，印刷厂的黄小姐即可将元素按照吸塑的外形重新排版设计。</p>
<p><strong>（3）说明书</strong></p>
<p>说明书稍麻烦点，印刷厂黄小姐明确表示，说明书如果找他们做只包印刷不包设计。所以这边找了一直兼职配合我做文案的<strong>Jensen</strong>，客户Mic先提供相关说明书内容，我这边准备App截图，然后请Jensen设计为PPT然后再交由黄小姐。</p>
<p><strong>（4）组装说明文档</strong></p>
<p>缓冲结构、彩盒、说明书都确认之后，我这边会出具一份外包装组装说明文档给到工厂，产线将按照该标准进行最后的组装。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/ERHzos5beCjslAEiZew8.jpeg" referrerpolicy="no-referrer"></p>
<h3>10.2 外壳</h3>
<p>生产订单下给模具厂，排期大约两周可以交付。由模厂的品质总监李工按照验收标准文档进行质量检查，符合标准之后运送至OEM厂。OEM厂这边由品质工程师何工进行验收，符合标准之后完成验收并安排给产线生产工程师李工。</p>
<h3>10.3 SMT</h3>
<p>Layout完成的电路设计会交由洗板工厂洗出印刷电路板（PCB），然后进行元器件贴片（SMT）得到PCBA，再将外围元器件（喇叭、电池等）与外壳进行组装后得到完整产品。</p>
<h3>10.4 PCBA产测</h3>
<p>PCB进行贴片后，由于是批量生产，除了工厂自身的通电测试，还需要进行PCBA的批量测试。</p>
<p>这个部分由于涉及到硬件端口的读写控制，所以由Talan与OEM厂的张工进行讨论后，编写相应测试程序并提供操作文档给到OEM厂的<strong>黄工</strong>，黄工的责任为生产测试。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/DcmA5Mbb6A18tzEXMth9.jpeg" referrerpolicy="no-referrer"></p>
<p>黄工会在PCBA组装好之后单纯将板子联通到一起，然后通过测试程序自动逐一测试对应功能，如果有测试不通过则给出错误提示。</p>
<h3>10.5 装配</h3>
<p>在PCBA完成测试之后，硬件交由组装产线进行<strong>PCBA+辅料+外壳</strong>的整体装配工序。</p>
<p>这阶段工厂会由生产工程师制作并<strong>打印装配指导手册</strong>，告知产线工人按照什么标准进行产品的组装。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/GlqGAYNaWrj9SaoSg5HP.jpeg" referrerpolicy="no-referrer"></p>
<h3>10.6 整机测试</h3>
<p>设备组装完毕，进入到整机批量测试工序。由Danny与OEM厂的张工进行讨论后，将系统应用功能做成一个自动化执行的程序，并提供相应的操作文档，由OEM厂的黄工安排工人按照自动测试流程对整机进行测试。</p>
<p>同时测试通过之后，进入设备信息烧录，Danny提供烧录程序让产线工人将设备的SN号自动烧录到设备中，完成生产工作。</p>
<h3>10.7 成品质检</h3>
<p>在成品按照相应标准组装完成之后，由OEM厂何工先安排工人先进行内部抽检，通过之后再交由客户（我）进行检查，PVT首次试产都要进行全检，后续生产则进行抽样检查，不良率一般可接受标准为 <3%。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/Rto7gAaiH5DxuRQcb2QC.jpeg" referrerpolicy="no-referrer"></p>
<h3>10.8 关键性问题</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/wBrDBDd1HJTEq2hzeGcB.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/1oZ0XdwRHaxXTey8LTpK.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-12">十一、项目成果</h2>
<h3>11.1 项目协调</h3>
<p>由于整个项目涉及第三方合作商非常多，并且分隔各地，各参与角色所负责的<strong>需求确认、各方之间的技术对接、资源协调、跨公司的项目排期</strong>等等都是些挺折腾的事情。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/81lpaTMZiad9anEAgBQw.jpeg" referrerpolicy="no-referrer"></p>
<h3>11.2 关于开发模式</h3>
<p><strong>（1）瀑布流式和敏捷式</strong></p>
<p>瀑布流式开发是传统的开发模式，强调文档和流程，相对缺少迭代与反馈，不适合客户需求不断变化的开发场景，但是好处是从一开始终点目标就清晰明确。</p>
<p>敏捷式开发强调“快”，要求快速迭代以获取频繁的反馈，适合应对市场和客户需求不断变化的互联网场景，缺点是很容易欠下技术债。</p>
<p>举个例子，假如要造一台汽车。瀑布流式开发会花上好几个月来确认每一个汽车零件，然后再动手；但是敏捷模式则会拆分阶段，每个阶段都会先做一个“可被测试”的东西。</p>
<p>如果这个不管用，那就再做一个，逐步逼近一台真正的车子。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/hFnl2Bg25wiNR6CGNWHr.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>（2）模式选择</strong></p>
<p>在APP应用类型的开发中非常适合敏捷式开发，因为市场的需求很多时候是未知的，<strong>产品经理拍脑袋想出来的great idea往往可能是个坑。</strong></p>
<p>而敏捷开发的好处是快速迭代，并且短时间内即可验证想法。否则一个功能模块的上新需要等待两个月之后才能知道市场反馈，整个团队的试错成本极高。</p>
<p><strong>但在智能硬件领域，我个人觉得还是比较适合瀑布流模式。</strong></p>
<p><strong>首先电路设计的更改成本极高，</strong>随便更换一个设计就要重新画原理图、ayout、洗板、贴片、测试，一个周期下来差不多一个月时间就过去了。</p>
<p><strong>其次产品系统模块之间的联动性极强，</strong>比如APP端如果要调整控制报文的发送模式，那就会导致云端要同步更改、测试，嵌入式端要同步更改、测试。</p>
<p><strong>再者是资源协调和工程排期问题，</strong>除非是大型的公司，否则小公司研发硬件多半需要各种不同的公司一起配合研发。而任何要变更一个需求，都需要重新协调对应的公司工程师资源及对方的排期安排。</p>
<p>这一系列的联动性都会使得项目在开发过程中不合适过多的调整变更设计。</p>
<h3>11.3 项目交付</h3>
<p>项目的工期卡得相当紧，客户期望是6个月可以出货，在现有的经验和资源下几乎是个 <strong>Impossible Mission。</strong></p>
<p>最后我们花了8个月时间实现 <strong>Case Close，</strong>虽然比客户设定的时间晚了两个月，但总算是顺利交付客户。</p>
<h2 id="toc-13">十二、标准作业程序(SOP)</h2>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/SMGjIJBXyQa55bG8PjkX.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/K9Yg58G7otvuxgxJKerd.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/ZulUk0Oo0And3ezoB1xI.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/X9UwOpthZVkeTjZDWLrY.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/m1b6oHxqDmWnKD00vjk5.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/1amJeqM2d3rJhfCBqsmb.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/yD5BtH8fwsdDzF92HsfI.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/Ov4peKBLTMPaMI6Pd8h1.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/4EEn9EY3OCGfXmYd0m8l.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/m4KUD856TVdjoKjWLvYT.jpeg" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/04/X6pb5ITVHcQvoOSlzSVk.jpeg" referrerpolicy="no-referrer"></p>
<p> </p>
<p>作者：Kesure，微信公众号：kesure225；长期扎根于AIoT智能硬件领域，撸过算法，写过应用，编过文案，干过推广，蹲过生产，拿过投资，专业并专注的产品背锅侠~</p>
<p>本文由 @Kesure 原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="3745718" data-author="1075800" data-avatar="http://image.woshipm.com/wp-files/2020/04/1jnmPlabWJ5PwPj6J4zA.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">2人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/WX_U_202008_20200803174056_6506.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/WX_U_202008_20200828154652_3943.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            