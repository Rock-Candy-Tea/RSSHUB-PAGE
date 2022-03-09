
---
title: '如何审核UGC社区内容'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/03/uIlgyY5lv7GzMofclXEO.png'
author: 人人都是产品经理
comments: false
date: Wed, 09 Mar 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/03/uIlgyY5lv7GzMofclXEO.png'
---

<div>   
<blockquote><p>编辑导语：短视频风行的时代，我们每天都在接收各种各样的信息。一直以来，碎片信息的参差不齐是一个值得重视的问题，UGC社区的审核也就显得非常重要。本文围绕如何审核UGC社区内容，为审核者提供了一些新思路。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-766638 aligncenter" src="https://image.yunyingpai.com/wp/2022/03/uIlgyY5lv7GzMofclXEO.png" alt referrerpolicy="no-referrer"></p>
<p>UGC 社区，是以用户生产原创内容为主的线上社区，但由于用户创作水平的不同，生产的内容自然有优劣之分，同时，有人聚集的地方就会有商机，自然有别有用心的人发广告。所以，对用户原创内容的审核，无论是为了良好的用户体验还是来自政府监管的压力，都是社区必须要做的事情。</p>
<p>从内容流程「生产 — 审核 — 加工 — 消费」来看，当内容生产后，运营人员在后台审核通过后，再做纠正错别字等加工，内容才会呈现在榜单、推荐 Feed 流 等前端展示位。</p>
<p>在审核过程中，运营人员充当「清洁工」和「淘宝客」，前者是做合规性审核，针对的是黄赌毒暴政恐，以及不符合社区业务的内容；后者是做质量审核，针对的是符合社区业务的内容，做出三六九等的质量评级，然后给予对应的曝光流量。</p>
<p>针对这两种内容性质的审核，一般都是以分值进行评判，比如针对不符合规性的内容，分值是 0 – 50 分，一般是不给予流量（冷处理）或直接删除；而针对质量等级的内容，分值是 60 – 100 分，且分数越高，说明内容质量越好，那么在前端就可以获得多一点流量。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/LKsFZyKE3iiJ2StagqrK.jpeg" alt="如何审核UGC社区内容" width="693" height="62" referrerpolicy="no-referrer"></p>
<p>为了加快内容审核，大公司都会开发出反广告的 antispam 系统，特点是「机器为主，人工为辅」，运营人员提供违禁词、敏感词，然后系统在用户发布内容后，直接删除触及到违禁词的内容，将触及敏感词的内容放置在待审核区，交给运营人员审核。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/HpVwrMFhclLU0h2Ny7wV.jpeg" alt="如何审核UGC社区内容" width="587" height="356" referrerpolicy="no-referrer"></p>
<p>但由于我之前所在的 UGC 社区处于探索期，后台审核只支持内容分类打标、设置内容等级的分值、下架删除内容等基础功能，再加上内容量在 5000 条左右（帖子 500 条，评论量 4500 条），相对那些上百万级发布量的社区而言，这一点的内容量还是比较少，于是我雇用几名兼职，采用人工方式搭建审核体系。</p>
<p>PS：文末有这篇文章目录的思维导图，可以保存下来，然后再阅读~</p>
<h2 id="toc-1">一、合规性审核</h2>
<p>我将不符合规性审核的内容，都称为广告，一共有 7 条，比如：</p>
<p>1）黄赌毒暴政恐等违法乱纪内容，特别是黑丝露腿截图</p>
<p>2）个人收卖，比如卖鞋、卖房、收游戏账号</p>
<p>3）有损自家平台的话语，比如辱骂、诋毁</p>
<p>在这些定义中，最好是附上例子，让兼职和其他同事可以快速明白，以便达成共识。</p>
<p><img data-action="zoom" class="size-full wp-image-766687 aligncenter" src="https://image.yunyingpai.com/wp/2022/03/L1OUlt2bFjVW8Ik62u6I.jpg" alt referrerpolicy="no-referrer"></p>
<p>当广告的定义设定之后，就需要给兼职分配工作。由于在我之前负责的社区中，内容主要有两部分，一部分是帖子，即用户发的动态，内容的载体有图文或视频，但没有直播形式；另一部分是评论，即用户在帖子下的评论。在后台系统中，帖子、帖子下的评论都是独立显示，也就是一个页面显示帖子列表，另外一个页面显示评论列表。如果要把两者关联起来，那么必须要人工通过帖子 ID 进行查询。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/O7B3q72zbIHms12L591f.jpeg" alt="如何审核UGC社区内容" width="816" height="374" referrerpolicy="no-referrer"></p>
<p>基于此，我把兼职分为两批，一批用来搭建帖子广告处理体系，另外一批用来搭建评论广告举报体系，如下：</p>
<h3>1. 帖子广告</h3>
<p>对于帖子广告，只需要一个人一天总共花 80 分钟，即可在后台系统查完，所以我安排了一名兼职在后台检查，发现广告的帖子，进行如下操作：</p>
<p>1）一般情况下，兼职打上广告标签进行标识，然后运营人员每天下班前审查广告标签的帖子，确定是广告的帖子，就进行冷处理（此时帖子会在前端隐藏），或直接删除。</p>
<p>2）遇到严重的情况，特别是黄赌毒，或反复发帖辱骂平台，兼职需要即时私信运营人员，一般都是直接删除。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/yOLeUovXKb1x4bqHAZoA.jpeg" alt="如何审核UGC社区内容" width="553" height="764" referrerpolicy="no-referrer"></p>
<h3 id="h_477752384_2">2. 评论广告</h3>
<p>由于评论数量多，再加上不少人直接发广告图片，以至于运营人员在后台查看时，即使花白天的时间，也仅仅找到几条。</p>
<p>所以，我换了一种思路，招募了 10 名兼职，专门在 APP 前端查看帖子，并且用马甲号进行评论，一旦遇到带有广告的评论，直接截图并且圈出来，分享到微信群，然后有额外一名兼职在后台系统处理，即时反馈每个兼职的当月累计举报次数。一个月下来，广告的举报总数可以高达 2000 条。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/hk9prYHwMVTzTWHeXhUF.jpeg" alt="如何审核UGC社区内容" width="546" height="1177" referrerpolicy="no-referrer"></p>
<p>此外，还可以收集一些频繁出现的广告关键字，比如要的联系、当面交易，那么可以每天在后台进行搜索。以后做反广告的 antispam 系统时，这些广告关键字可以直接派上用场。</p>
<p>多嘴一句，在发布量或评论量比较少的社区，特别是处于探索期时，不建议做 antispam 系统，除了耗人力之外，还有一个重要原因就是，太多限制的关键字会导致社区的忠实用户流失，比如大多数平台将「微信」及其衍生词「vx」等作为限制关键词，只要用户发表的言论带有这些词语，轻则直接删除，重则禁止用户发言，这极大地打击了用户的热情。</p>
<h2 id="h_477752384_3">二、质量审核</h2>
<p>在质量审核中，也会分为帖子和评论，主要是为了筛选出优质内容，防止出现劣币驱除良币的不良现象。需要注意的是，由于兼职不了解业务、内容网感差等因素，由运营人员全程参与，哪怕一天只能评级 20 条，那么也不会引入兼职做质量审核。</p>
<h3 id="h_477752384_4">1. 帖子质量</h3>
<p>考虑到我招募的 KOL 达人多半是职高学生，创作水平一般，我当时将帖子质量分为 A、B、C 三级，C 要求为语句通畅、表达清晰，而 A、B 则要求懂得结构化表达，即总分总结构。</p>
<p>在审核过程中，评为 A、B 两级的帖子，分值设为 80 – 100 分，优先在推荐页第一屏幕显示，而 C 级文章，分值在 60 分左右，将会在推荐页第二屏幕显示。</p>
<p>为了防止运营人员的强干预对内容造成误判，那么也会对每篇内容做独立的数据统计，比如知乎会将知乎答主的每篇回答的阅读量、互动数进行记录，并且做成看板提供给创作者。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/0fdFoCbcrorIhxmhs6wz.jpeg" alt="如何审核UGC社区内容" width="800" height="230" referrerpolicy="no-referrer"></p>
<p>此外，并且我公司系统将 24 小时内达到「阅读率 10%，点赞人数 8」（阅读率 = 阅读人数 / 曝光人数）的帖子设置为优质帖子，自动给予更多的流量。</p>
<p>对于优质帖子，运营人员还可以做以下的操作：</p>
<p><strong>1）置顶</strong></p>
<p>当某篇帖子被运营人员设为置顶后，在 APP 前端会有置顶标识，和其他普通帖子做出一定的区分，并且用户做下拉刷新不会改变其位置，比如今日头条 APP 经常会把官方的时政新闻置顶在推荐页顶部。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/uENHiVsyHxzHAMWfPtXk.jpeg" alt="如何审核UGC社区内容" width="583" height="1374" referrerpolicy="no-referrer"></p>
<p><strong>2）设置精选内容区</strong></p>
<p>可以设立榜单、编辑精选区等产品功能，将优质的帖子放进去。比如酷安每天都会将热门的图文、问答等类型的内容放入编辑精选区。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/MCBg1zaZjgukhtDQT56g.jpeg" alt="如何审核UGC社区内容" width="477" height="1517" referrerpolicy="no-referrer"></p>
<p><strong>3）制作《社区创作者指南》</strong></p>
<p>对于优质的内容，运营人员根据数据做简要分析，比如对于阅读率高于 4% 的帖子，原因可能是标题善于用「你」，让读者感到作者是和他对话，更为贴近人心，那么可以将这些心得整理到《社区创作者指南》，以指导社区的其他创作者。</p>
<p>这样做可以极大激励社区创作者的热情，就好像上小学时，老师会把学习成绩优秀的学生名字写在黑板上，鼓励其他学生的向他看齐。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/wbh35lv49dUY0d54FKev.jpeg" alt="如何审核UGC社区内容" width="762" height="185" referrerpolicy="no-referrer"></p>
<h3 id="h_477752384_5">2. 评论质量</h3>
<p>对于评论，一般是按照点赞、时间等维度进行算法排序，不需要运营太过于操心。</p>
<p>不过对于较为优质的评论，特别是神评论，一般是运营安排兼职用马甲号进行评论，俗称埋雷，在后台将该评论设置「加热」，该评论将会在 APP 前端显示在帖子的外面。此外，一般也可以使用程序算法进行自动设置，比如对每一条帖子，第一个评论超过 10 个点赞数，则自动设置为神评论。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/JRr8BzbIpvTPvAPtCEk1.jpeg" alt="如何审核UGC社区内容" width="464" height="1334" referrerpolicy="no-referrer"></p>
<p>但在埋雷时，一定要记得换号，防止出现「黄婆卖瓜，自卖自夸」的翻车现象，比如抖音不时有博主为了引发内容消费者多评论，故意在评论下夸自己的作品很好，但评论时却忘记了切换到小号。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/fNTOueBBItJourzDLcsq.jpeg" alt="如何审核UGC社区内容" width="466" height="1272" referrerpolicy="no-referrer"></p>
<h2 id="h_477752384_6">三、对违规用户的处理</h2>
<p>审核内容不仅仅是审核内容，还需要审核发内容的人，毕竟内容是由人发出来的。</p>
<p>我将用户分为普通用户、KOL、高危用户。其中 KOL 是可以创作出高质量帖子的用户，高危用户是时常违规的用户，比如经常广告，而其余的都是普通用户。</p>
<p>对于 KOL，一般都会爱惜自己的羽毛，不会轻易出现发广告、辱骂他人等违纪行为，所以对于他的帖子或评论，审核时都会直接通过，并且还会对他的帖子分配多一点流量。而对于他出现违规问题，那么运营人员可以私信他，对他进行警告提醒，如果情节严重或多次违反，那么可以对他进行禁言，短则七天，长则几个月</p>
<p>但对于高危用户，一般是注册才几天的新用户居多，注册后就会立即发广告的帖子或评论。而这些用户，一般是屡教不改，运营人员会把他拉进黑名单，禁止他发帖子或评论，并且对他所有的帖子以及评论进行删除，封禁时间一般为几个月。如果违规次数超过 3 次，那么会对其进行永久封号。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/enkGvJwFCf7AWUR09h0F.jpeg" alt="如何审核UGC社区内容" width="660" height="360" referrerpolicy="no-referrer"></p>
<p>在社区中，由于观点各异，在评论区经常会出现骂战，最后都会上升到人身攻击。当运营人员发现后，应该封禁双方当事人的账号，即时删除不好的评论，并且在在前端留下解禁的微信联系方式，当被封禁的用户再次进行发帖或评论，解禁的联系方式就会被弹出来，那么他可以添加微信，然后进行申述。</p>
<p>此外，由于审核会出现疏忽，那么可以发挥群众的力量。方式主要有两种，如下：</p>
<p><strong>1）产品实现举报功能</strong></p>
<p>比如知乎用户可以举报知乎回答或评论，然后知乎会在给出举报的处理结果：已处置 or 未发现违规。</p>
<p>但这种方式是非常耗人力，比如在产品端实现流程化之后，还需要用客服或运营人员进行核实。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/Lpz9nWY6IpSWwI6e2N3H.jpeg" alt="如何审核UGC社区内容" width="759" height="1227" referrerpolicy="no-referrer"></p>
<p><strong>2）私信官方号</strong></p>
<p>一般存在私信功能的社区，都会设置官方号，用户可以将要举报的用户或内容，截图或发链接给官方号，写上举报理由，然后交由官方号进行处理。这种方式比较省人力，并且运营人员可以即时跟举报者进行实时沟通。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/wJvWqulsNTheze3rcUyC.jpeg" alt="如何审核UGC社区内容" width="597" height="1181" referrerpolicy="no-referrer"></p>
<p>对于大公司如何审核内容，感兴趣的可以查看知乎 Alita 郑瑜的文章：<a href="https://zhuanlan.zhihu.com/p/26939457">《UGC社区的内容如何进行审核和过滤？》</a></p>
<p>最后，这篇文章比较长，特意为你准备了一张思维导图，方便你阅读。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="如何审核UGC社区内容" src="https://image.yunyingpai.com/wp/2022/03/GDJZkcs6SiJVjLcb5zpO.jpeg" alt="如何审核UGC社区内容" width="732" height="513" referrerpolicy="no-referrer"></p>
<p> </p>
<p>作者：猫晓豆豆，社区运营，会一点知识管理。微信公众号：猫晓豆豆。</p>
<p>本文由 @猫晓豆豆 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5346640" data-author="822052" data-avatar="https://static.woshipm.com/WX_U_201901_20190108001249_9875.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            