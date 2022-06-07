
---
title: '产品拆解丨月营收3个亿的斑马APP原来这样设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/VElCCu8yUodxIbRpeAQh.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 07 Jun 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/VElCCu8yUodxIbRpeAQh.jpg'
---

<div>   
<blockquote><p>编辑导语：作为一款在线英语教育启蒙APP，斑马APP是如何在产品功能、产品运营等层面吸引用户留存与转化的？在内容服务上，斑马APP又有哪些特点？本篇文章里，作者就斑马APP进行了产品设计拆解，一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5475048 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/VElCCu8yUodxIbRpeAQh.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>发展不到5年，平均月活跃用户人数87.65万，每日人均使用时长4.87小时，两年前就有业内人士透露月营收超过3亿，猿辅导旗下针对在线英语启蒙教育的小斑马，从出生就仿佛蕴藏着巨大的魅力。</p>
<p>这样的产品，到底是如何设计的，有什么值得我们学习的地方，本期「设计大侦探」全面拆解斑马，为大家一探究竟。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/W78jWYs85jAIb16hB2gI.png" alt width="711" height="529" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、产品画像</h2>
<h3>1. 产品介绍</h3>
<p>「斑马APP」前身为「斑马AI课」，是猿辅导旗下一款针对2-8岁儿童启蒙教育的产品，内容体系由国内外名校毕业的硕博领衔独立研发，通过完善的分龄体系和专业有趣的数字内容，培养全方位能力，专注实现全面发展，课程体系包含了英语、阅读、思维、音乐和写字等课程，目前产品已经迭代到V5.16.1版本。</p>
<p><img data-action="zoom" class=" wp-image-5474978 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/BoXgE5RF90AJzDxsNwqx.png" alt width="764" height="382" referrerpolicy="no-referrer"></p>
<h3>2. 产品生命周期</h3>
<p>斑马APP诞生于2017年，至今已发展5年，目前已经慢慢进入成熟期。斑马的盈利能力很强，月营收在2020年就已经突破3亿，当下的业务焦点除了用户活跃度和商业变现，还在探索更多的业务模式。从2022年3月份产品运营数据（数据来自易观千帆），斑马月活跃人数为87.65万，人均使用时长4.78小时。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/WdBedXeH7DIT4DFIqY5s.png" alt width="751" height="426" referrerpolicy="no-referrer"></p>
<h3>3. 商业模式</h3>
<p>斑马是一个主要针对2-8岁的儿童的综合学科学习平台，课程内容丰富，包含英语、阅读和思维等，目标用户群是以24-35岁的年轻妈妈，消费力水平较高，主要分布在新一线及二三线城市。斑马主要依靠系统课程盈利，其次还有绘本、周边等变现业务。斑马的课程模式以小班制为主，40-60人为一个小班，呈阶梯式学习，有效拉长用户生命周期，增加用户终身消费价值。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/Jp5ZsDgSWQmaTTO2Jrs8.png" alt width="777" height="402" referrerpolicy="no-referrer"></p>
<h3>4. 用户画像</h3>
<p>斑马的核心用户人群以女性为主，年龄在24-35岁之间，消费能力非常强，文化水平较高，主要分布在新一线城市、二线城市和三线城市，其中广东、山东、浙江、江苏和四川用户数最多。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/KmzGQsMeWYSzylGUTZlX.png" alt width="769" height="436" referrerpolicy="no-referrer"></p>
<h3>5. 功能架构</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/c8ugSo62V0VdGN8JWR5N.png" alt width="790" height="567" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、设计拆解</h2>
<p>根据增长模型，我把斑马的功能分为三大类，分别是学习服务，主要实现商业变现，内容服务，主要实现用户留存，营销服务，主要帮助产品传播拉新。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/XcqNdox9ununthxoBdAX.png" alt width="781" height="399" referrerpolicy="no-referrer"></p>
<h3>1. 学习服务</h3>
<p><strong>1）课程</strong></p>
<p><strong>① 功能价值</strong></p>
<p>斑马是一个综合学科学习平台，不仅有英语，还有思维、阅读、美术、写字和音乐等，其中科学和编程分别引流至猿辅导旗下其他教学产品。其次根据儿童年龄划分为S1-S5个级别，呈阶梯式学习，拉长用户终身消费价值。</p>
<p>课程划分为体验版和系统版，体验版主要用于新用户激活，用户购买后才能正式开始系统版的学习。而系统版是斑马的正式课程，斑马的正式课程以班为单位，一般为40-60人，需要达到一定的报名人数以后才会正式开课。每个班有班主任，开学前还有开学仪式，家长会等，体系非常完善。课程是面向用户销售的产品，是斑马商业变现的主要来源。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/M0eyPHhSbg1lTDX8yYA2.png" alt width="771" height="516" referrerpolicy="no-referrer"></p>
<p><strong>② 策略推导</strong></p>
<p><strong>a. 首页</strong></p>
<p>新用户进入APP后，斑马主要通过信任状和互惠来激活用户。金刚区展示了斑马的品牌介绍，瓷片区通过直播为新用户赠送福利，吸引用户快速激活。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/0IvFLLtDlsLQ3BQfndBG.png" alt width="792" height="474" referrerpolicy="no-referrer"></p>
<p>付费用户进入APP后，金刚区加入了推荐有礼和组队领礼两个营销活动，主要通过礼品激发用户拉新引流；瓷片区的内容为动态更新，目的是可以推送不同主题的内容，比如周周分享，课程直播，礼物兑换等，有效提升产品运营的灵活度。</p>
<p><img data-action="zoom" class=" wp-image-5474976 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/zS0z7kq4VPHj0EGb9LDA.png" alt width="772" height="462" referrerpolicy="no-referrer"></p>
<p>首页内容设计简单直接，主要分为体验版和系统版课程内容，体验版单价低，主要用于新用户、新课程的激活，而系统版是斑马的正式课程，以班为单位，需要达到一定的报名人数以后才会正式开课。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/lDt6gj52g7G419a488Gd.png" alt width="778" height="466" referrerpolicy="no-referrer"></p>
<p><strong>b. 体验版详情页</strong></p>
<p>体验课程有时间限制，通过赠送英语启蒙礼盒礼品，吸引用户，其次利用限购，增加稀缺性，有效提升用户购买率。用户评价可有效通过口碑效应打消用户顾虑，建立用户信任感。</p>
<p>学习详情是对体验课程的介绍，对斑马的课程模式、课程优势、课程内容、管理模式进行了全面的讲解，让用户对斑马有全面的了解。详情页底部展示赠品和品牌介绍，互惠营销首尾呼应，从而让用户快速下单。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/fMrm3vFflvfMxIzTrvLB.png" alt width="772" height="462" referrerpolicy="no-referrer"><br>
<strong>c. 系统版详情页</strong></p>
<p>系统版的赠品不仅颜值高，而且礼品丰富，提供了学习机、汉语拼音认读机、智能学习礼包、绘画盒子、保温杯等多项选择，对孩子妈妈的吸引力非常大。</p>
<p>向用户介绍斑马课程的学习体系，根据年龄划分为S1-S5个级别，呈阶梯式学习，这和传统启蒙教育模式相比，不仅提升了用户终身消费价值，还拉长了用户生命周期，这让平台可以利用用户基数探索更多的商业模式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/zKK2lvfqVkhPFfin5dyn.png" alt width="784" height="469" referrerpolicy="no-referrer"></p>
<p><strong>2）学习</strong></p>
<p><strong>① 功能价值</strong></p>
<p>用户购买系统版课程以后，需要等待课程的开班时间，开班后会有非常正式的开班仪式。课程的学习和上学一样，每周一个主题，周一到周五每天更新，以情景互动、游戏化的教学动画形式吸引小朋友，每一节课程会拆分为几个阶段，降低小朋友学习的行动成本。当小朋友学习完以后，会自动生成学习报告，鼓励用户分享传播，为产品拉新引流。</p>
<p>学习的内容决定了新用户是否会购买系统版课程，以及老用户的课程续费率，而学习的体验设计决定了小朋友能否简单、轻松、愉快的使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/ZpzKHaCYKbgHGFbsfqEN.png" alt width="725" height="487" referrerpolicy="no-referrer"></p>
<p><strong>② 策略推导</strong></p>
<p><strong>a. 引导页</strong></p>
<p>头部可切换用户购买的课程，方便查找；目录是所有系统课程的汇总，比如S2级别的用户需要去查找S1的课程，这里就是课程的入口。右上角可以进入作品墙和专题，这两个内容主要是提高用户活跃度。课程根据时间以列表Feed流展示，方便用户查找。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/zUirVp1gY0AMUFMbbvgK.png" alt width="787" height="320" referrerpolicy="no-referrer"></p>
<p><strong>b. 上课</strong></p>
<p><strong>目录页：</strong></p>
<p>课程划分为不同的小节，这可以把学习时间分割，降低行动成本，让小朋友可以轻松开始学习。以阅读课程为例，先从一个趣味性的故事开始，激发小朋友的兴趣，再通过听、说、读、练的步骤，让小朋友加深对课程的理解，最后生成学习报告。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/9yLDn4D9pUKZQgQF5eSH.png" alt width="783" height="469" referrerpolicy="no-referrer"></p>
<p><strong>学习页：</strong></p>
<p>学习页以游戏化的教学动画展现，斑马为每个课程设计了不同的卡通人物IP，这可以有效拉近和小朋友的距离，培养和小朋友的感情，如八斗、百夫子、Zara等卡通人物。</p>
<p><img data-action="zoom" class=" wp-image-5474966 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/QXrcAjc8urFiclZHug4k.png" alt width="784" height="438" referrerpolicy="no-referrer"></p>
<p>通过设置斑马币（可兑换礼品）的酬赏，有效激发小朋友认真学习，只有完全回答正确才能获得3颗星，而单节课累计的积分决定了本节课程的学习评分，形成了一个可量化的指标，帮助家长可对小朋友单次课程的学习做出评估。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/RX6HAHZHjXaR1JmUvmjX.png" alt width="788" height="440" referrerpolicy="no-referrer"></p>
<p><strong>结束页：</strong></p>
<p>当小朋友学习完以后，系统会自动生成一个学习报告。头部为课程的评分，满分为3颗星。当小朋友学完后，系统会对作业进行点评（有人工和班主任），和用户建立高频的互动，提供有温度的服务。</p>
<p>报告页的底部数据看板设计得很巧妙，展示了小朋友累计学习的课程、练习，这可以极大提高家长分享的欲望，从而拉新引流。其次作品也可以发布到社区作品墙，小朋友们可以相互观看其他同学的作品，提高用户活跃度，激发学习和传播欲望。</p>
<p><img data-action="zoom" class=" wp-image-5474964 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/rEley6TtYyoi0pH326fm.png" alt width="783" height="469" referrerpolicy="no-referrer"></p>
<p><strong>c. 课后</strong></p>
<p><strong>作品墙：</strong></p>
<p>当小朋友学习完以后，可以发布作品到社区的「作品墙」，这有效提升用户的课后活跃度。其次作品墙还有丰富多变的老师打卡学习挑战，对小朋友来说，这极大丰富了学习的乐趣，培养用户忠诚度。</p>
<p><img data-action="zoom" class=" wp-image-5474963 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/pwUFZGGaOy4j59NCoZgO.png" alt width="797" height="477" referrerpolicy="no-referrer"></p>
<p><strong>奖状墙：</strong></p>
<p>用户每学习3个单元，斑马都会给小朋友颁发一个荣誉证书，系统课程学完以后，还会颁发毕业证书，家长还可以填写实物信息，领取实物奖状，这增加了品牌的温度，极大提高了用户口碑。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/XlMBklLosRidLjdXeeAb.png" alt width="807" height="328" referrerpolicy="no-referrer"></p>
<p><strong>学习周报：</strong></p>
<p>「学习周报」把小朋友每周的学习成果通过数据化展示，不仅可以一目了然查看本周的学习成果，而且能提升用户的传播欲望，其次对家长来说，这就像一个孩子当周的学习数据看板，对孩子的学习有清晰直观的了解。</p>
<p><img data-action="zoom" class=" wp-image-5474962 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/x8Vv5HJ7iJdP5LXrfL5e.png" alt width="773" height="463" referrerpolicy="no-referrer"></p>
<p><strong>周末游乐场：</strong></p>
<p>「周末游乐场」就是娱乐小游戏，在每周末会以课程的形式的发布，儿童可以通过精美的小游戏一边学习一边娱乐，不仅可以劳逸结合，还可以提升用户活跃度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/J2gD4bVOA8nI34R6tyXm.png" alt width="765" height="311" referrerpolicy="no-referrer"></p>
<p><strong>d. 专题</strong></p>
<p>「专题」的设计，就像是为课程增加了无限多变的属性，目前斑马会根据不同的节假日推出专题（3-5节课，有免费和付费两种模式），小朋友可进行系统的学习，目标性强，也能让小朋友学以致用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/3F1CbGK9E6jVmGRhKRtO.png" alt width="768" height="460" referrerpolicy="no-referrer"></p>
<h3>2. 内容服务</h3>
<p><strong>1）绘本</strong></p>
<p>斑马的绘本出品质量非常高，不仅和多家全球领先的儿童书籍出版公司合作，而且结合当下的时事热点进行全新的创作，比如以冬奥主题的相关系列绘本。「绘本」不仅可以提高用户活跃度，培养用户对产品的忠诚度，其次也是斑马对商业变现的新探索，目前绘本已经分为免费和VIP付费两种模式。</p>
<p>绘本的设计，主要根据不同的主题进行划分，不仅可以让孩子找到自己感兴趣的主题内容，还可以增加功能属性。儿童阅读过的绘本会有系统记录，方便儿童查找，体验非常友好。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/CqbrEk84jPlQJQ2bOMEu.png" alt width="790" height="321" referrerpolicy="no-referrer"></p>
<p><strong>2）视频</strong></p>
<p><strong>① 看世界</strong></p>
<p>「看世界」是斑马的原创栏目，内容题材丰富，有美食、旅游、科学、运动等，核心的卖点是通过英语课程的几位国外老师以英语视频讲解的形式带着小朋友边看边学，既能增强英语语感，也能增长小朋友的见识。</p>
<p>其次视频的策划、出品都非常优质，这不仅可以提高用户留存率，还能引流传播，在腾讯视频等视频网站都能查看部分视频，极大提高了斑马AI的知名度和曝光度。</p>
<p><img data-action="zoom" class=" wp-image-5474961 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/0EPPIipECHgmBZcgpfrU.png" alt width="776" height="464" referrerpolicy="no-referrer"></p>
<p><strong>② 3D儿歌</strong></p>
<p>「3D儿歌」目前制作了33首，数量相对较少，但视频的出品非常优质，由国内外知名音乐学院顶尖制作人员参与制作，以斑马品牌形象Zara为主，对世界经典儿歌进行重新创作，目前在腾讯视频等视频网站都能查看，极大提高了斑马AI的知名度，还能为产品拉新引流。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/t0PBRt1pVpLuY3RlN9LS.png" alt width="805" height="481" referrerpolicy="no-referrer"></p>
<p><strong>3）娱乐</strong></p>
<p><strong>① 斑马拍</strong></p>
<p><strong>a. 功能价值</strong></p>
<p>「斑马拍」非常有趣，就像抖音一样，以短视频为主，官方会发布一些儿歌、活动挑战的模板，小朋友和父母还可以一起录制，极大增加了学习的趣味性，提高用户活跃度。未来斑马拍的发展空间非常大，也许会慢慢形成一个儿童学习+娱乐的UGC视频社区。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/kDkbU4Use8bPqb9yV3Zc.png" alt width="772" height="516" referrerpolicy="no-referrer"></p>
<p><strong>b. 策略推导</strong></p>
<p>右上角的挑战图标醒目，吸引用户可快速进入官方的用户挑战活动，点击头像则进入自己的主页。右边的头像暂不支持访问其他用户主页，但可访问官方栏目主页，比如八斗的宝藏世界、斑马百宝箱等。用户可把视频分享给微信好友和朋友圈，为产品分享传播。</p>
<p><img data-action="zoom" class=" wp-image-5474957 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/HaXnv7wJtQmBMcJPHYo0.png" alt width="793" height="474" referrerpolicy="no-referrer"></p>
<p>左下角为该视频所关联的课程，点击后可查看当节课程所有小朋友录制的课程，这可以利用从众效应引导小朋友录制视频，提高用户活跃度和学习的趣味性。右下角点击拍同款以后，小朋友就可以开始跟着视频的模板进行录制，让一款学习产品充满了娱乐性，多变又好玩。</p>
<p><img data-action="zoom" class=" wp-image-5474954 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/BqdVIW3Tztq2Lzfxt2bD.png" alt width="789" height="472" referrerpolicy="no-referrer"></p>
<p><strong>② 斑马速算</strong></p>
<p>「斑马速算」是一个思维课程练习的小游戏，小朋友以游戏闯关的形式学习算法，目前板块还比较单薄，没有太多内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/NMsOBKONZOCnBDjzJr6J.png" alt width="778" height="465" referrerpolicy="no-referrer"></p>
<p><strong>③ 斑马背古诗</strong></p>
<p>「斑马背古诗」的设计目前比较简单，玩法也比较单一，小朋友可以跟读，可以背诵，练习结束后可以分享作品。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/Yys0lZ5JJMS9hGvgihdZ.png" alt width="794" height="475" referrerpolicy="no-referrer"></p>
<p><strong>4）音频</strong></p>
<p><strong>① 有声故事</strong></p>
<p>「有声故事」属于会员VIP权益之一，主要以中文为主，结合国内经典名著及童话故事进行二次创作和改编，家长可以利用有声故事哄孩子睡觉，或降低孩子使用屏幕时间，保护眼睛。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/PCpvfR54W3D5V0zrR65Q.png" alt width="754" height="451" referrerpolicy="no-referrer"></p>
<p><strong>② FM</strong></p>
<p>「FM广播」分为英文和中文两大类，内容主要取材自系统课程，小朋友可根据课程搜索对应的音频。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/e8ZT31dlzpufe8Uo79zQ.png" alt width="763" height="456" referrerpolicy="no-referrer"></p>
<p><strong>5）直播</strong></p>
<p>随着用户习惯的改变，「直播」将会成为斑马在产品运营的重要方式。目前斑马的直播内容已经从新用户激活、老用户复购扩展到「斑马大讲堂」、「斑马育儿说」这样的特色栏目，主要以邀请业界的教育专家作为嘉宾，对用户做主题内容直播，不仅可以提高用户留存率，新用户激活变现，还可以帮助产品分享传播。</p>
<p><img data-action="zoom" class=" wp-image-5474950 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/fDtq2RYx44fJ1LWtXHvB.png" alt width="788" height="471" referrerpolicy="no-referrer"></p>
<h3>3. 营销服务</h3>
<p><strong>1）推荐有礼</strong></p>
<p>「推荐有礼」玩法非常简单，用户可直接分享给好友或分享朋友圈海报，好友扫码或购买课程后，用户均可获得平台的奖励。假如好友购买了系统课程，直接返现200元。推荐有礼充分了利用口碑营销，引导用户邀请好友获取砖石，在页面底部，通过精美的兑换礼品展示，进一步引导用户分享。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/2RXLX8oypKR4FtfGCzOe.png" alt width="797" height="324" referrerpolicy="no-referrer"></p>
<p><strong>2）周周分享</strong></p>
<p>「周周分享」每周一期，用户通过分享海报到朋友圈，保留2小时以后，凭截图在APP上传，审核通过后可获得500斑马币，如果好友最终报名课程，则会获得更丰厚的福利。</p>
<p><img data-action="zoom" class=" wp-image-5474948 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/f43Ay1nssBfuBtLXFwCr.png" alt width="788" height="472" referrerpolicy="no-referrer"></p>
<p><strong>3）组队领礼</strong></p>
<p>「组队领礼』是一个新用户拉新的活动，门槛低，只需邀满2人，但是好友必须是斑马非注册用户，组队成功后，队伍的三个用户均能领取斑马的随机礼品。这个活动充分利用互惠原则，通过赠送免费的小礼品引导老用户拉新，新用户激活。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/RKAcamSmg4VkAwSVS7ap.png" alt width="797" height="477" referrerpolicy="no-referrer"></p>
<p><strong>4）斑马商城</strong></p>
<p>「班玛商城」就是积分商城，小朋友通过每天课程的学习，积累的斑马币，可以在商城进行礼品兑换。斑马的周边产品颜值非常高，对小朋友和年轻妈妈都非常有吸引力，通过这样的酬赏，又能倒逼小朋友坚持认真学习。另外斑马也提供了更多的周边产品在官方淘宝店直接销售，如教具、玩具、文具等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/ITdoIOaLwcEyB6oQsUdL.png" alt width="775" height="315" referrerpolicy="no-referrer"></p>
<p><strong>5）礼品卡</strong></p>
<p>当用户报名了课程的体验版或系统版以后，平台会向用户赠送礼品卡，礼品卡又可以赠送给好友，从而引导用户进行传播分享，获取更多的新用户。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/q8vqWWwnikJqxSrv3YoT.png" alt width="762" height="456" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、总结</h2>
<p>结合《在线英语启蒙教育产品设计竞品分析模型工具》，我从三个维度对斑马产品设计进行总结。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/oPCt6GzM8LL9LEeCSBpX.png" alt width="812" height="612" referrerpolicy="no-referrer"></p>
<h3>1. 课程内容</h3>
<p>斑马作为一个多学科学习平台，其实已经从英语拓展到阅读、思维、美术等系统课程。课程内容以趣味互动为核心理念，由国内外名校拥有丰富教学经验和科研成果的的硕博领衔独立研发。其次根据儿童年龄划分为S1-S5个级别，呈阶梯式学习，有效拉长用户终身消费价值。斑</p>
<p>马的上课模式以小班制、学期制为主，开班前有开学典礼，开始上课后，班主任全程跟踪孩子情况，监测效果，定期电话回访，为用户提供精细化的运营。</p>
<p>其次通过对上课流程的拆解，斑马的学习流程用户体验也非常友好，不仅把课程划分为不同的小任务，利用趣味化的沉浸式动画教学，还充分考虑了家长、小朋友的学习用户习惯，从激活、留存、变现到传播，都设计了非常丰富的功能。</p>
<h3>2. 内容服务</h3>
<p>斑马不仅为每套课程创作了个性鲜明的IP角色，其次围绕这些IP角色打造了精彩丰富的内容。绘本、看世界、3D儿歌、有声故事、斑马拍等栏目内容，都主要以Zara、八斗等IP角色进行创作。这不仅可以让用户牢牢记住这些IP角色，提高用户忠诚度，其次更能培养用户的情景触发，产生条件反射。</p>
<p>其次斑马的内容服务丰富多变，传播形式丰富多样，不仅打造了斑马看世界、3D儿歌这样的高品质内容栏目，还通过斑马拍这样有趣好玩的短视频来链接用户，不仅仅是提高用户活跃度，而是让小朋友和家长都参与进来，未来斑马的产品定位不会只局限于一款学习产品，而会探索更多的可能性。</p>
<p>另外斑马已经开始通过直播创办很多特色栏目，这将会成为斑马在未来最重要的运营和营销方式，而且将会有更大的商业想象空间。</p>
<h3>3. 营销服务</h3>
<p>斑马的营销服务设计得非常丰富，从用户购买前后的所有环节，都把口碑推荐的模式设计到里面。体验课作为引流产品，让用户免费尝鲜，精美的周边礼品又能快速俘获年轻妈妈的心。当用户购买后，可以领取礼品卡送给好友，还能邀请好友组队领礼。</p>
<p>其次斑马的周边设计模式，非常值得借鉴。这些周边产品，颜值极高，制作精良，牢牢抓住了年轻妈妈的心，这不仅让这个群体产生了强烈的购买欲望，其次通过实物产品的传播和推荐，更能赢取新用户的信任，大大降低拓客成本，实现新用户增长。</p>
<p><strong>参考文献</strong></p>
<ul>
<li>易观千帆 – 斑马APP数据分析</li>
<li>斑马AI：启蒙英语APP竞品分析（偏运营）：http://www.woshipm.com/evaluating/4291310.html</li>
<li>案例分析：『斑马AI课』app的增长之路：http://www.woshipm.com/operate/3701123.html</li>
</ul>
<p> </p>
<p>本文由 @廖尔摩斯丨设计大侦探 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5473069" data-author="829489" data-avatar="https://static.woshipm.com/APP_U_202205_20220512164856_7431.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            