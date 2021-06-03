
---
title: 'B站产品需求文档（PRD）与思考'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/NcGKsO1UpW0khjESzzng.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 03 Jun 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/NcGKsO1UpW0khjESzzng.jpg'
---

<div>   
<blockquote><p>编辑导语：B站以视频社区为核心，吸引了大量年轻人使用，并形成了它的独特圈层与文化氛围。在这样的背景下，B站未来如何发展或破圈，都将受到更多人的瞩目。本篇文章里，作者结合其体验，总结了一份B站产品需求文档，且对B站未来如何发展做了一定思考，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4645158 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/NcGKsO1UpW0khjESzzng.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、文档综述</h2>
<h3>1. 版本修订记录</h3>
<p><strong><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/hFsSoAoF5hxCF6UdUqpA.png" alt width="420" height="67" referrerpolicy="no-referrer"></strong></p>
<h3>2. PRD输出环境</h3>
<p><strong><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/jXTs0x642rWwEm6HRFk5.png" alt width="423" height="198" referrerpolicy="no-referrer"></strong></p>
<h3>3. 产品介绍</h3>
<p>哔哩哔哩（bilibili，简称B站）成立于2009年6月26日，是以泛二次元文化为核心，覆盖动画、舞蹈、游戏、音乐、鬼畜、科技等多个内容板块的文化社区和视频弹幕平台。</p>
<h2 id="toc-2">二、需求整理</h2>
<h3>1. 市场需求</h3>
<p>在早期，B站的主要用户是喜欢二次元亚文化的人群，二次元文化包含了动画、漫画、游戏和轻小说四个领域，在后期，B站扩展了用户范围，其产品涵盖了更加多元化的“泛二次元”业务。</p>
<p>随着互联网的发展，国民对二次元文化的接受度逐渐提高，且由二次元而展开的“泛二次元”文化包含了更多的内容，如影视、鬼畜、舞蹈、音乐等，受众面更广。“泛二次元”的用户规模到2020年已经增长至4.1亿人，增长的群体促进了对于泛二次元视频社区的需求，人们需要强有力的平台进行内容的创作、消费与讨论。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/QXOrGQRxzE1QBc2FoUcf.png" alt width="587" height="351" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（数据：艾瑞咨询）</p>
<p>B站作为国内泛二次元视频和社区平台的领头羊，随着泛二次元的发展，近几年的活跃用户得到了显著提高。</p>
<p>根据公司的财报数据，截止2020年四季度末，<strong>B站的日均活跃人数已达到了5400万人，月均活跃人数突破了2亿。</strong>而随着泛二次元文化的扩张趋势和B站近几年在其它领域（如影视、在线课堂、电商等）的发展，预计未来B站的用户规模仍有较大增长空间。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ZLGneDuvxrIqsxY4myT3.png" alt width="588" height="355" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（数据来源：BILIBILI财报）</p>
<h3>2. 用户画像</h3>
<p>根据火烧云2020年Q1监测到的数据，B站用户男女比例为57：43，近八成的用户年龄层为18-35岁，在地域分布上，华东（34%）和华南（21%）的用户最多，西南的用户（13%）最少。</p>
<p>此外，在用户城市类型分布上，B站的用户分布较为均匀，呈现纺锤结构，50%的新用户来自三线及三线以下城市。在受教育程度上，B站的用户受教育程度较高，在本科及以上学历的比例高出全网10%。</p>
<p>把B站的视频按视频总数、播放总量、全部评论量、全部弹幕量取频率最高的Top100词汇，绘制出词云，可以看出<strong>用户对于VLOG、搞笑、科普、测评、生活、学习类原创视频比较感兴趣</strong>，此外“中国”“日本”词条的热度也较高，可以看出用户对于时事政治也较为关注。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/nTW3GzhP20SG07zx2nkH.png" alt width="582" height="291" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（图片来源：街机时代）</p>
<p>而根据B站2020年的年报数据来看，B站的用户倾向于在<strong>手游业务（40%）、增值服务业务（32%）模块</strong>进行消费。且近三年，B站用户在<strong>增值服务和广告业务</strong>的付费意愿显著提高。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/4GYKr2zaD6dsJLalXaG6.png" alt width="583" height="356" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（数据来源：B站年报）</p>
<p>而从增值业务的细分业务收入占比来看，“漫画和其它付费内容”的增值服务收入占比从2018年的3%上升至2020年的23%，这说明随着B站的业务扩展，<strong>用户对更多形式的内容（如课程、小说等）的支付意愿提升。</strong></p>
<p>与之相比，直播业务收入在增值服务收入的占比减小，从2018年的55%下滑至2020年的34%，<strong>B站的直播业务发展受阻</strong>，不能与其它的增值服务保持同样的速度增长，消费者对于直播业务的支付意愿增长较为缓慢。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/fCdlbDHHu3RQTC3IlbEC.png" alt width="585" height="360" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（数据来源：B站年报）</p>
<p>受益于增值业务营收的增长，虽然直播业务收入在增值业务的占比减小，但总体也呈现增长状态。2020年，其在净收入的占比达到了10.9%，这说明在B站的用户中，虽然对于直播的支付意愿增长较缓，但总体也呈现增长趋势，<strong>直播业务还有一定的发展空间；</strong>而占一成的净收入的比例也说明了愿意<strong>消费直播内容的用户具有一定规模</strong>。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/kchUL64zmZE204lbYn6H.png" alt width="587" height="365" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（数据来源：B站年报）</p>
<p>综上，可以得出如下B站用户画像：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/JsZGx6dHKRCII8Rvdesf.png" alt width="590" height="254" referrerpolicy="no-referrer"></p>
<h3>3. 用户需求</h3>
<p>按照维度划分，B站的用户主要分为如下几种类型：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/gV0czvhqoDfGUdAOp4cE.png" alt width="587" height="316" referrerpolicy="no-referrer"></p>
<p>根据不同类型的用户需求，B站主要需要具有如下功能：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/xMGNdLlj1h4GmjBFZ2Lv.png" alt width="588" height="435" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、产品结构</h2>
<p>B站的一级功能页面为“首页”“频道”“动态”“会员购” “我的”“游戏中心”和“消息”。</p>
<p>其通过一系列的创作引导（如话题、创作中心的数据分析、自行开发剪辑APP等），激励用户持续地生产内容，通过视频推荐、热搜、排行榜等形式，采用去中心化的内容分发方法，把用户的创作内容呈现在大众视野，通过点赞、投币、收藏、转发、弹幕、评论等一系列反馈/互动功能增加社区活跃度和用户粘性。</p>
<p>其主要结构是围绕视频展开的社区APP，视频包括了原创/剪辑中短视频、番剧、影视三种主要类型，并增加了直播、电商、游戏中心、专栏等功能。</p>
<p>以下为B站具体的产品功能结构图、产品信息图和产品结构图。</p>
<h3>1. 产品功能结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/tUSvSYMKM94H5lpLjiKe.jpg" alt width="894" height="2375" referrerpolicy="no-referrer"></p>
<h3>2. 产品信息图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/s0FK7cafMguqwsoEfYEy.jpg" alt width="898" height="2278" referrerpolicy="no-referrer"></p>
<h3>3. B站产品结构图</h3>
<p>综上，B站主要分为“首页”“频道”“动态”“会员购”“我的”“消息”“游戏中心”“广告”八大大结构，首页、频道、动态模块是主要的视频/内容模块，“会员购”“游戏中心”则是除视频模块外扩展的模块，“消息”对应的是互动模块，而“我的”则是个人中心模块。</p>
<p>首页涵盖了直播、番剧、影视、推荐、热门、建档百年六个二级结构，与“频道”模块有所重合，把部分频道的视频内容按照用户喜好和二级分类呈现在用户眼前。</p>
<p>根据B站2020年的财报，直播收入占比已从2018年的7.8%上升至2020年的10.9%，直播付费用户已达到110万人，月均消费105元。</p>
<p>考虑到B站的破次元战略和在电竞、游戏的布局，以及近几年直播总体行业的发展，虽然B站的直播业务有疲软之势，笔者认为或许可以把直播上升至一级产品结构，并优化直播业务，促进消费需求。</p>
<p>下图为B站的产品结构图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/DVWnxaRhlqxU2CGTc323.png" alt width="898" height="916" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、全局说明</h2>
<h3>1. 功能权限</h3>
<p>权限功能分为未登录状态和登录状态，未登录状态。</p>
<ul>
<li>对于未登录状态，除了可以观看视频、点赞视频、分享视频外，不可以进行其它的视频互动、反馈操作，也不可以进行购买任何虚拟/实体商品的行为。</li>
<li>对于登录状态，B站将用户分为了普通会员和月度会员、年度会员三个群体。</li>
</ul>
<p>对于普通会员，根据用户的等级，权限管理如下所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/79PU4vzGo3kiqit2fXrO.png" alt width="594" height="286" referrerpolicy="no-referrer"></p>
<p>月度会员和年度会员除了可以享受普通会员的权益外，还享受如下特权：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/c0eWHBzKFXxzT93FqUd2.png" alt width="328" height="233" referrerpolicy="no-referrer"></p>
<p><strong>思考</strong></p>
<p>不同于其它的社区APP，B站对于不同等级用户可享受的<strong>权限划分得比较鲜明</strong>，除了付费大会员可以享受更多特权外，普通会员也会因为不同的等级而享受不同的权力，这给了用户升级的动力。升级所需的积分需要通过点赞、转发、评论、投币、发送弹幕、发布视频/专栏、发布动态等形式获得，促进了内容的创作以及内容的反馈/互动。</p>
<p>此外，<strong>鲜明的等级权限划分也在一定程度上保证了社区内容的质量。</strong>而用户在等级成长体系中，也会潜移默化地被社区文化所感染，成长为潜在的高质量内容创作者，从而继续社区文化的传播与发展。</p>
<p>当然，等级划分也使新用户不能拥有很多权益，不能参与很多互动，可能会带来不好的用户体验。</p>
<p>因此在做社区APP时也需注意等级权限的区分度和使用体验，<strong>在不影响低等级用户参与社区互动/反馈的同时，让高等级用户享受更多的权限，</strong>增加用户升级的动力和等级荣誉感，并用等级制度作为保证高质量内容输出的第一道门槛。</p>
<h3>2. 键盘说明</h3>
<p>点击手机号输入框和验证码输入框，弹出数字键盘。</p>
<p>点击手机或邮箱输入框、账号密码输入框、搜索框、评论框、弹幕框、发布动态框、发布主题框、聊天框、个人信息填写框，弹出字母键盘。</p>
<p>在用第三方支付时，点击输入密码框，弹出数字键盘。</p>
<h3>3. 页面内交互</h3>
<p><strong>1）提示信息</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/QEAG29cvuagggQc5JeLu.png" alt width="594" height="530" referrerpolicy="no-referrer"></p>
<p><strong>2）弹窗</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/bVPE9WpfFcit1yfoie6Y.png" alt width="583" height="428" referrerpolicy="no-referrer"></p>
<p><strong>3）更新信息</strong></p>
<p><strong><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/rXfb4H3B9UX0g2CQVudj.png" alt width="581" height="548" referrerpolicy="no-referrer"></strong></p>
<p><strong>4）页面交互</strong></p>
<p><strong>① 切换页面</strong></p>
<p>用户可以选择点击相应的页面按钮切换页面，或是左右滑动切换页面。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/NmeLU6ANvkOcf0UTfruz.png" alt width="578" height="552" referrerpolicy="no-referrer"></p>
<p><strong>② 刷新页面</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/vIXs6Nbb2ZvjqoNZtSoE.png" alt width="284" height="528" referrerpolicy="no-referrer"></p>
<p><strong>5）页面异常</strong></p>
<p>没有网络和未连接WiFi。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/yfZVd80q90dsuo6h07u9.png" alt width="680" height="650" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、部分业务流程</h2>
<h3>1. 用户登录/注册流程</h3>
<p>B站的登录方式分为“手机号码+验证码”登录和密码登录两种，密码登录可选择输入注册手机号码或者绑定邮箱账号，再输入密码进行登录，不支持第三方账号登录。</p>
<p>当点击“登录”时，默认跳转到“手机号登录注册“页面，如需密码登录，用户需要点击”密码登录“按钮进行页面跳转。</p>
<p>对于新用户，<strong>只有用手机号注册这一项选择</strong>，而其它社区或视频平台，如小红书、知乎、优酷、爱奇艺等，均可以使用第三方进行登录，只是有的需要辅以手机验证码确认。</p>
<p>单一的注册登录方式的好处是B站可以不依赖于第三方平台，实现自己私域流量的管理，便于沉淀用户，打造自己的社区文化；但也增多了用户登录的步骤，变相提高了平台的准入门槛。</p>
<p><strong>较高的注册门槛，不借助第三方登录，也有利于进行社区文化的管理，</strong>使社区氛围不变质，形成用户管理闭环。而且多数网站在进行第三方登录后，还需要进一步的手机号验证，这样对比起来，B站的注册注册方式少了一步，更加简洁。</p>
<p>此外，为了维持社区内容（如评论、弹幕、论坛等）的质量，第一次注册B站的用户需要进行答题后，才能转正成为正式会员，享受视频互动/反馈功能。</p>
<p>下图为详细的B站用户登录注册逻辑：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/iJMNxZhriNTKHksENCKP.png" alt width="653" height="729" referrerpolicy="no-referrer"></p>
<h3>2. 用户观看视频逻辑</h3>
<p>用户可以通过首页的各页面、频道页面、动态页面、离线缓存页面或者通过搜索框搜索想看的视频，来选择自己想看的视频进行观看。</p>
<p>判断用户是否可以观看该视频分为四个个维度，其一是用户的所在区域是否可以观看该视频、其二是视频是否为付费视频、其三是视频是否为大会员专享视频、其四是非WIFI用户是否选择用流量观看。</p>
<p>下图显示了详细的用户观看视频逻辑：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/RyBaYCEmv6X3kMxspTCy.png" alt width="652" height="1001" referrerpolicy="no-referrer"></p>
<p>在用户成功打开视频后，可以进行观看视频操作，如互动、分享、举报、缓存以及播放设置等。</p>
<p>在相应的操作中，对于已登录用户，B站按照用户等级和是否是大会员对用户进行了分组，不同的用户有不同的权限。</p>
<p>低等级用户不可以进行视频举报、评论、发送弹幕等操作，这样有利于维护“亚二次元“群体的社区文化，提高社区内容的质量，使能发表视频反馈/互动的人都是使用APP一段时间、对于B站有所了解的用户；而B站也在无形中塑造了这些用户的使用APP习惯，使他们更加认同B站，从而使社区更有凝聚力。</p>
<p>但是就如前文所言，分明的等级制度的权限管理也使初入B站的新用户难以参与视频和社区的讨论，从而降低了APP的使用体验感和社区的参与感，导致部分用户无法转化为活跃用户。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/P8Xi0NLKVRADH0bNXdXD.png" alt width="652" height="848" referrerpolicy="no-referrer"></p>
<h3>3. 用户观看直播逻辑</h3>
<p>直播页面是B站的二级页面，位于首页的子页面下。</p>
<p>B站的用户可以从“直播——推荐页”“直播——分类页”以及“动态页”进入直播间。</p>
<p>“直播——推荐页”对应想要看直播、但没有明确需求的用户，平台根据用户的喜好和直播间的质量向用户推荐优质的直播间。此外，如果有关注的主播正在直播，也会在此页显示。</p>
<p>“直播——分类标签页”选项对应有明确的观看直播类型喜好的用户，用户通过标签筛选可以查看相关类型的直播间，选择喜欢的进入。</p>
<p>在“动态页”中，上侧的“最常访问UP主”栏会显示关注的正在直播的UP主，用户点击正在直播的UP主头像，可以进入其直播间。这对应的是用户对于自己小社圈的内容消费需求，用户可以实时获得自己关注的UP主的直播信息，并进行查看。</p>
<p>下图为用户观看直播的逻辑：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/IL4Gkhhd6QNXZ2MPcKdi.png" alt width="639" height="783" referrerpolicy="no-referrer"></p>
<p>此外，打开B站APP默认页面是“首页——推荐”页面，如果有关注的UP主在直播，不会反应到此页，这增加了用户获取关注的人的直播信息的时间成本。B站可以考虑在“首页——推荐”页中，在推荐的视频区域中设置一个位置，当关注的UP主正在直播时、当用户刷新页面时显示相应的直播间信息，并提示用户是自己关注的UP主在直播。</p>
<p>其次，在直播页面，由于是二级子页面，没有单独的直播搜索框，用户只可以根据直播间的分类一步步来筛选喜好的直播间。这增大了用户查找的时间成本，可以考虑后期增设一个直播间搜索功能。</p>
<h3>4. 用户购买商品逻辑</h3>
<p>用户可以在“会员购”页面进行商品的购买，有三种方式可以选择心仪的商品，对于有明确商品需求的用户，可以在搜索框内输入想要的商品，进行查找和购买；对于有明确商品种类需求的用户，可以通过分类筛选商品，进行对应类别的商品的查找和购买；对于无明确购物需求的用户，B站可以在会员购首页面根据用户喜好，推荐相应的商品。</p>
<p>购买方式分为两种，“直接购买”和“加入购物车”进行购买，支付方式有“支付宝”“微信”“银联云闪付”“花呗”“一网通支付”“QQ支付”六种，都是借助第三方平台，<strong>暂无专属B站的支付方式。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/PgAUjXqOwczQQu6gtRY9.png" alt width="648" height="825" referrerpolicy="no-referrer"></p>
<p>B站的会员购主要还是专注于二次元商品的售卖，由于二次元商品的特殊性质，预售商品比较多，从支付定金到商品最终送达用户手中的购买周期较长，且因为预售商品的特殊性质，很多预售商品/定金不可退。</p>
<p>因此，在这个期间<strong>如何通过良好的服务来减少用户因为等待而降低的购物体验是重点</strong>，这需要提高客服服务水平，完善商品进度查询功能和商品退货流程。</p>
<p>此外，目前B站暂无自己的支付体系，都是借助第三方平台进行支付。这样一是增加了用户支付的操作流程，二是平台也需要支付较多的第三方平台支付服务费。</p>
<p>据了解，B站目前也在开发自己的支付体系，若此体系搭建成功，更容易形成用户消费的闭环，而且付费流程也会更为简便。</p>
<h3>5. 用户下载游戏逻辑</h3>
<p>B站有两个地方可以进入“游戏中心”，其一是“首页”页面的右上方的游戏图标，其二是“我的”页面的“游戏中心”按钮。</p>
<p>对于有明确游戏下载需求的用户，可以通过发现页的分类/排行榜页面进行游戏的筛选与下载，对于无明确下载需求的用户，可以通过发现页的发现页面、我的-猜你喜好页面、精选页浏览游戏，选择喜欢的游戏进行下载。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/DY0yE5BXK5IxYVr0g9ml.png" alt width="592" height="717" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、部分产品详细功能说明</h2>
<h3>1. 播放页面</h3>
<p><strong>1）页面名称：</strong>播放页面</p>
<p><strong>2）页面入口：</strong>点击任一视频，打开竖屏视频播放页面。</p>
<p><strong>3）页面结构</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/1ORh6vrtuJ5Zejp3Rvu6.png" alt width="635" height="586" referrerpolicy="no-referrer"></p>
<p>播放页面分为横屏和竖屏两种，其页面结构如上图所示。</p>
<p>对于<strong>横屏播放页面</strong>，按照从上到下、从左到右的顺序，其页面由返回按钮、视频基本信息区、视频反馈区、播放设置按钮、视频互动弹窗、截图按钮、锁频按钮、视频进度操作区、播放控制按钮、弹幕操作区和常用播放设置按钮组成。</p>
<p>对于<strong>竖屏屏播放页面</strong>，除了把视频基本信息区、弹幕操作区、视频反馈区下移至非视频区域外，在视频区域，还增加了最大化视频按钮，减去了常用播放设置按钮、锁频按钮和截图按钮。</p>
<p>此外，竖屏播放页面在非视频区域，增加了广告区以及相似视频推荐区，均以<strong>单列、纵向的方式展示相关广告和视频。</strong></p>
<p>对比腾讯视频、优酷视频等相似视频推荐区均以横向滑动的方式呈现相关内容的模式，B站纵向的设计利于用户查看视频，<strong>提高推荐视频的点击率</strong>，虽然不如横向滑动一样可以呈现更多的内容和占用更少的空间， 但是<strong>有更好的内容分发效果</strong>。</p>
<p><strong>4）页面逻辑</strong></p>
<p><strong>对于横屏播放页面，其页面逻辑如下。</strong></p>
<p><strong>返回按钮</strong>：点击可以切换到视频竖屏播放页面。</p>
<p><strong>视频基本信息区</strong>：点击UP主头像，跳转到UP的个人空间；点击视频参与的活动标签，右侧弹出相应活动的介绍、双列展示优秀稿件，点击弹窗外区域，弹窗消失。</p>
<p><strong>视频反馈区</strong>：点击点赞、不喜欢图标可以进行点赞、不喜欢操作，并在进行操作后标红相应图标；点击投币，右侧弹出弹窗，弹窗外区域，弹窗消失；或者在弹窗中选择投币的数额，投币后弹窗消失，中间出现提示消息框——“投币成功”，悬浮三秒后消失；点击转发，下侧弹出弹窗，转发成功后或点击弹窗外的区域后，弹窗消失。</p>
<p><strong>播放设置按钮</strong>：点击后右侧弹出播放设置弹窗弹窗，点击弹窗外的区域，弹窗消失。</p>
<p><strong>视频互动弹窗</strong>：在视频播放到一定时间时弹出，用户点击弹窗内的选项按钮后消失，当用户没有任何操作时，悬浮5秒后消失。弹窗主要用于UP主发起某个互动话题，或是用于激励用户进行视频反馈（投币、收藏、点赞和关注UP主）的操作。</p>
<p><strong>视频进度操作区</strong>：显示当前播放视频进度，用户调整进度后，视频播放跳转到相应进度处进行播放。</p>
<p><strong>截图按钮</strong>：点击截图按钮，截图当前视频区域页面，图片自动保存在相册，并在视频中部显示“截图保存相册成功”消息提示框，悬浮三秒后消失。</p>
<p><strong>锁频按钮</strong>：点击锁频按钮，播放页面的其它操作按钮、信息栏消失，视频转换为锁频模式，按钮由“解锁”图标变为“上锁”图标，再次点击图标后，视频转换为非锁频模式。</p>
<p><strong>播放控制按钮</strong>：点击后视频进行播放/暂停操作，按钮切换成“暂停”/“播放”图标。</p>
<p><strong>视频剧集切换按钮</strong>：位于播放控制按钮的右侧，当视频有续集时，有此按钮。点击按钮，切换到下一集。</p>
<p><strong>弹幕操作区</strong>：点击弹幕关闭/开启按钮，视频关闭/开启弹幕，按钮切换为弹幕关闭/开启图标。点击弹幕设置按钮，右侧弹出弹幕设置弹窗，点击弹窗外的区域，弹窗消失。点击弹幕输入框，视频暂停，弹出弹幕输入键盘框，点击发送弹幕或是弹幕键盘输入框外的区域，键盘框消失，视频继续播放。</p>
<p><strong>常用键盘播放设置按钮</strong>：从左到右由选集按钮（如无选集，则无此按钮）、倍速按钮、清晰度调整按钮组成；点击按钮，右侧弹出相应弹窗，用户进行操作后，弹窗消失，左侧显示消息提示框，提示用户操作成功，消息框悬浮三秒；或当用户点击弹窗外的区域后，弹窗消失。</p>
<p><strong>竖屏播放的页面逻辑与横屏基本相同，对于多增的元素，其页面逻辑如下：</strong></p>
<p><strong>最大化视频按钮</strong>：点击可以最大化视频，切换到视频横屏播放模式。</p>
<p><strong>视频简介/评论页面切换栏</strong>：下划线标红正在浏览的页面按钮，当用户点击相应页面的按钮时，非视频区域切换到对应页面。</p>
<p><strong>广告区域</strong>：广告分为紧贴视频下方的广告和位于推荐视频区域的广告；点击广告，跳转到相应广告页面，点击广告右侧的“扩展”图标，下侧弹出广告反馈弹窗，用户在弹窗内进行相关操作或点击弹窗外的区域后，弹窗消失。</p>
<p><strong>视频标签分类区</strong>：用户点击相关的分类标签后，跳转到对应的视频标签分类页面。</p>
<p><strong>相似视频推荐区</strong>：以单列的形式给用户推荐与观看视频相关的视频，点击跳转到对应视频的播放页面，用户点击该区域视频右下角的“扩展”按钮，这个视频所占区域的右下角弹出“添加至稍后再看”选项，点击该选项或是点击弹窗外的区域，弹窗消失。</p>
<p>其评论、发送弹幕、广告反馈操作逻辑如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/tHcPYSmK4E7d3Mt2TYOB.png" alt width="640" height="937" referrerpolicy="no-referrer"></p>
<p><strong>5）思考</strong></p>
<p>对比其它视频APP，B站的横屏播放页面<strong>突出了视频上传者、视频参与话题活动的信息；</strong>在左上角的视频基本信息区域设置了UP主的头像框、视频参加的话题，这样一是<strong>帮助UP主获取更多的关注</strong>，从而激励他们进行创作，二是用话题的形式，<strong>增加社区不同类型内容的讨论度</strong>，也引导了用户产出高质量的内容。</p>
<p>其次，B站在视频播放区加入了互动弹窗，想要增加视频的互动/反馈度，激励用户进行点赞/投币/收藏/转发/互动等操作。</p>
<p>但总体而言，相比其它视频APP，B站播放视频的区域元素太多，结构过于复杂，容易遮挡视频内容，影响观看体验。</p>
<p>互动弹窗占据视频播放区太多位置，且不可以选择关闭，影响观看原视频。可以在播放设置中添加关闭互动弹窗功能，让用户自行选择是否要开启互动弹窗，或者可以设置当点击互动弹窗外的区域，关闭弹窗，而不是悬浮五秒后弹窗才消失。</p>
<p>此外，评论页面可按照热度和时间顺序显示评论，但当用户评论了视频后，不可以快速看到自己的评论内容。建议在“按热度”“按时间”评论选项栏下加一个“我的评论”选项，便于用户查看以前观看视频时的心情和想法，记录用户的成长。</p>
<p>其次，目前比较难以在竖屏播放页面中找到“缓存”按钮，如果想要下载视频，需要在竖屏播放页面中，点击右上角的“展开”按钮，才可以选择视频缓存，操作十分不便捷；而且“缓存”图标的设置也不醒目，对于新用户而言，难以找到下载视频的按钮，建议在视频反馈区右侧添加“离线缓存”按钮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/4cZK9pihzIflfU2aRgE7.png" alt width="647" height="409" referrerpolicy="no-referrer"></p>
<h3>2. 首页</h3>
<p><strong>1）页面名称：</strong>首页</p>
<p><strong>2）页面入口：</strong>打开APP后的默认页面，或者单机底部导航栏的“首页”，即可跳转到首页页面。</p>
<p><strong>3）页面结构</strong></p>
<p>按照从上到下，从左到右的顺序分为：用户头像栏、搜索栏、游戏中心按钮、消息按钮、子页面切换栏、动态广告/活动/热门视频展示栏、双列视频/其它内容展示栏、底部导航栏。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/mfUFcOCfEMlS4gs5wEMq.png" alt width="654" height="478" referrerpolicy="no-referrer"></p>
<p><strong>4）页面逻辑</strong></p>
<p><strong>用户头像栏</strong>：点击进入“我的”页面。</p>
<p><strong>搜索栏</strong>：点击进入搜索页面，用户可以在此页面查看热搜、搜索历史、搜索发现词条。</p>
<p><strong>游戏中心按钮</strong>：点击可以跳转到游戏中心页面。</p>
<p><strong>消息按钮</strong>：点击可以跳转到消息中心页面。</p>
<p><strong>子页面切换栏</strong>：下划线标红当前页面的按钮，点击想要切换的页面按钮，可以在首页分类下的“直播”“推荐”“热门”“追番”“影视”“建档百年”页面之间切换。</p>
<p><strong>动态广告/活动/热门视频展示栏</strong>：单列大屏展示相应的内容，点击跳转到对应页面。</p>
<p><strong>双列视频/其它内容展示栏</strong>：点击对应视频/内容区域，跳转到视频播放/内容页面；每个视频区域的右下角有“展开“按钮，点击，下侧弹出视频反馈弹窗，用户可以在这里选择对此类视频推荐的反馈，反馈完成后，弹窗消失，上方显示”将减少类似视频推荐“信息提示，悬浮三秒消失，或是点击弹窗外区域，弹窗消失。</p>
<p><strong>底部导航栏</strong>：标红当前页面按钮，点击相应页面的按钮，跳转到对应页面。</p>
<p>其简要的页面交互逻辑如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Wgj1Iy5hFW6ybU3D5nmC.png" alt width="659" height="822" referrerpolicy="no-referrer"></p>
<p><strong>5）思考</strong></p>
<p>与其它视频播放APP的首页相比，B站的<strong>首页元素较为简洁</strong>，以“导航栏”+“广告/活动/热门视频栏”+“双列视频/内容展示栏”三个要素组成。</p>
<p>双列视频/内容推荐栏多为用户感兴趣的剪辑/原创视频，少量穿插直播间、专栏、游戏和广告内容，非视频内容会在内容标题下面打上所属类型的标签（如“广告”“游戏”“直播”等），均采用一样的排版呈现在用户眼前。比起其它视频APP的复杂结构，排版和交互更为简洁，且每个视频标题下方都会显示视频的频道和分区，便于用户快速知道这个视频的主内容是什么。</p>
<p>这与B站主推原创中等长度视频以及主打社区文化有关；<strong>交互越简洁，排版越简单，信息呈现越直白，越便于用户进行内容的粗略查看，快速找到自己喜欢的高质量视频，减少用户决策时间。同时，双列的视频/内容展示的设计，也给了用户更多选择的空间、增加了视频的曝光度。</strong></p>
<h3>3. 频道页</h3>
<p><strong>1）页面名称：</strong>频道页</p>
<p><strong>2）页面入口：</strong>点击最下方页面切换栏的“频道”，即可跳转到频道页面。</p>
<p><strong>3）页面结构</strong></p>
<p>按照从上到下的顺序分为：子页面切换栏、搜索栏、订阅频道展示栏、最近看过的频道展示栏、我订阅的频道展示栏、热门频道展示栏、其它频道详细展示栏和底部导航栏。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/oVw5cARSsBeciZc9RGTE.png" alt width="654" height="958" referrerpolicy="no-referrer"></p>
<p><strong>4）页面逻辑</strong></p>
<p><strong>① 频道——频道页</strong></p>
<p><strong>子页面切换栏</strong>：下划线标红当前页面的按钮，点击想要切换的子页面按钮，可以在频道页面下的“频道”“分区”页面之间切换。</p>
<p><strong>搜索栏</strong>：点击进入搜索页面，用户可以在此页面查看搜索历史词条。</p>
<p><strong>订阅频道展示栏</strong>：横向展示用户订阅的频道的图标，点击图标，跳转到对应的频道页面。</p>
<p><strong>看过的频道展示栏</strong>：按看频道的时间的顺序，由近及远地横向展示用户看过的频道和日期，向右滑动显示更早期的时间看过的频道，点击其中一个频道，跳转到对应的频道页面。</p>
<p><strong>我订阅的频道展示栏</strong>：双列展示订阅频道的精选视频，点击视频，跳转到相应视频的播放页面，若无订阅频道，则不展示此栏。</p>
<p><strong>热门频道展示栏</strong>：横向展示热门频道的图标，点击一个频道的图标，跳转到对应的频道页面；点击栏目右上角的“换一换“按钮，更新此栏推荐的热门频道，并更新下方“热门频道详细展示栏”展示的频道。</p>
<p><strong>热门频道详细展示栏</strong>：按照“热门频道展示栏”的推荐频道的顺序，双列展示对应频道的精选视频，点击视频，跳转到相应视频播放页面；点击展示栏右上角的“订阅”按钮，按钮变灰，并显示“已订阅”，用户成功订阅此频道。</p>
<p><strong>底部导航栏</strong>：标红当前显示页面的按钮，点击其它页面的按钮，跳转到对应页面。</p>
<p><strong>② 频道——分区页</strong></p>
<p><strong>子页面切换栏</strong>：下划线标红当前页面的按钮，点击想要切换的子页面按钮，可以在频道页面下的“频道”“分区”页面之间切换。</p>
<p><strong>详细分区展示栏</strong>：点击相应的分区图标，跳转到对应的分区页面。</p>
<p><strong>底部导航栏</strong>：标红当前显示页面的按钮，点击其它页面的按钮，跳转到对应页面。</p>
<p>简要页面交互逻辑如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/s9glu7DWDrIp9glxGzji.png" alt width="652" height="676" referrerpolicy="no-referrer"></p>
<p><strong>5）思考</strong></p>
<p>频道页属于B站的5大核心功能页，有利于用户选择喜欢的分区和频道进行视频的观看，<strong>且频道页细化了顾客需求，</strong>针对不同喜好的客户推出不同的内容，以分区为一级分类，频道为二级分类的模式，为顾客提供更加细致化的服务。</p>
<p>由于B站是以个强调社区的APP，频道的细化也有利于喜好不同的用户在不同的圈子进行社区内容的创作、浏览和讨论，让用户快速加入自己的兴趣圈子，<strong>提升社区认同感</strong>，提高每个小社区的人的互动频率，鼓励用户创作更多的内容。</p>
<p>在“频道——频道”页面，B站展示频道的顺序是用户关注的频道、用户看过的频道、用户关注的频道的精选视频展示、热门频道、热门频道的精选视频展示，<strong>权重是关注大于浏览记录大于热门，比较清晰地显示了以用户的兴趣为主展开的频道内容展示。</strong></p>
<p>笔者认为或许可以再添加一个维度，推荐的频道，用户多次刷关注的频道，容易因为内容同质化而厌倦视频，在用户关注的频道下面加一个“猜你喜欢”频道推荐，有利于扩展用户参与讨论的社圈，增加刷B站乐趣的多样性，从而有更高的用户粘性。</p>
<p>此外，当点击“频道——频道”页的搜索框时，只能展示历史搜索记录，无推荐频道、热门频道的展示，虽然在“频道——频道”页有详细的热门频道展示，但笔者认为，在搜索页面展现相应的词条，会更有利于用户发现自己感兴趣的社区内容。</p>
<h3>4. 动态页</h3>
<p><strong>1）页面名称：</strong>动态页。</p>
<p><strong>2）页面入口：</strong>点击最下方底部导航栏的“动态”按钮，即可跳转到动态页面。</p>
<p><strong>3）页面结构</strong></p>
<p>按照从上到下的顺序分为：频道——子页面切换栏、发布动态栏、搜索栏、最常访问关注UP主展示栏、“频道与话题”展示栏、关注的用户动态更新展示区和页面切换栏。</p>
<p><strong><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/3P7vy0dTzIkVnq11QMNy.png" alt width="647" height="405" referrerpolicy="no-referrer"></strong></p>
<p><strong>4）页面逻辑</strong></p>
<p><strong>子页面切换栏</strong>：下划线标红当前显示页面按钮，点击想要跳转页面按钮，可以在动态页面下的“视频”“综合“页面之间切换。</p>
<p><strong>发布动态栏</strong>：点击跳转到发布动态页面。</p>
<p><strong>搜索栏</strong>：下拉页面，可以显示搜索栏，点击搜索栏，进入搜索页面，用户可以在此页面查看大家都在搜、搜索历史的话题词条。</p>
<p><strong>最常访问关注UP主展示栏</strong>：横向展示关注UP主的头像和用户名，对于更新了动态的UP主，头像框右下角标红点显示，向右滑动可以查看更多的UP主信息。</p>
<p>UP主的排序规则为，首先按照关注的UP主是否进行了动态更新进行排序，更新了的UP主排在未更新的UP主前；其次按照该用户对关注UP主的访问量进行排序，用户访问次数越多的UP主排在越前面。当用户点击相应UP主的头像时，按时间的顺序，在“关注用户动态更新展示区“下由近及远地展示该UP主的动态。</p>
<p>对于正在直播的关注UP主，其头像放在该栏的最前面，并在头像最下方标注“正在直播”，用户点击其头像可以进入相应的直播间。</p>
<p><strong>频道与话题展示栏</strong>：点击对应话题或频道，跳转到相应话题或频道页面，点击“查看更多”，跳转到“话题”页面。</p>
<p><strong>关注用户动态更新展示区</strong>：以时间顺序，由近及远地展示关注用户的动态，下滑展现用户更多的动态内容。若动态是视频，点击动态跳转到视频播放页面，若是其它内容，则点击后可查看详情。</p>
<p><strong>底部导航栏</strong>：标红当前显示页面的按钮，点击相应页面的按钮，跳转到对应页面。</p>
<p>简略的页面逻辑如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/hQ1C2vtU8TU1Y3QlUICG.png" alt width="648" height="895" referrerpolicy="no-referrer"></p>
<p><strong>5）思考</strong></p>
<p>动态页的的内容部分主要由三个部分组成，最常访问的UP主头像、“频道与话题“以及关注用户更新的动态内容。</p>
<p>“频道——频道”页和“动态”页的功能有所类似，都是围绕用户展开的一个社区，只是一个对应的是用户关注的频道的社区视频内容，一个对应的是用户关注的人的动态内容，<strong>后者更加强调的是用户的个人社交圈。</strong>在展示上，不同于频道页的双列式展示，动态页采取了单列式内容展示，且每个动态都采用大图进行展示。</p>
<p>频道页的双列展示有利于提供更多的创作视频曝光机会，激励创作者进行创作，也给与了用户更多选择自己喜欢内容机会。而动态页对接的是已关注的UP主的动态，其动态内容一般是用户感兴趣的，一般都会进行浏览，<strong>不用太多的选择权，单列展示更利于用户进行内容的查看，减少操作。</strong></p>
<p>此外，虽然在动态页，关注的UP主动态更新了会在头像右下角标红显示，但当点开动态内容时，无法跳转到上次查看这个UP主的动态的地方，新增一个“从上次浏览的地方开始浏览”功能，可以减少用户下滑查找上次看到动态的地方的时间，使用户操作更加便捷。</p>
<h3>5. 会员购</h3>
<p><strong>1）页面名称：</strong>“会员购”页。</p>
<p><strong>2）页面入口：</strong>点击底部导航栏的“会员购”按钮，即可跳转到会员购页面。</p>
<p><strong>3）页面结构</strong></p>
<p>按照从上到下的顺序分为：魔力仓库按钮、购物车按钮、会员购中心按钮、搜索栏、商品分类栏、商品活动展示栏、魔力赏商品展示栏、商品上新按钮、抢先看按钮、人气排行按钮、用户签到按钮、商品展示栏、底部导航栏。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/a8fk35Il2AabMpL5LJQs.png" alt width="646" height="504" referrerpolicy="no-referrer"></p>
<p><strong>4）页面逻辑</strong></p>
<p><strong>魔力仓库按钮</strong>：点击按钮，跳转到魔力仓库页面。</p>
<p><strong>购物车按钮</strong>：点击按钮，跳转到购物车页面。</p>
<p><strong>会员购中心按钮</strong>：点击按钮，跳转到会员购中心页面</p>
<p><strong>搜索栏</strong>：点击搜索栏，跳转到搜索页面，可以查看搜索历史和搜索发现。</p>
<p><strong>商品分类栏</strong>：点击相应的分类图标，按照类别跳转到对应的商品展示页面，点击“全部分类”，跳转到商品分类页面。</p>
<p><strong>商品上新按钮</strong>：点击按钮，跳转到商品上新页面。</p>
<p><strong>抢先看按钮</strong>：点击按钮，跳转到抢先看页面。</p>
<p><strong>商品排行按钮</strong>：点击按钮，跳转到商品排行页面。</p>
<p><strong>用户签到按钮</strong>：点击按钮，跳转到用户签到页面。</p>
<p><strong>商品展示栏</strong>：展示商品的图片、标题、价格和有多少人想要，用标签标注商品的重要信息（如榜单排行、是否是新品等）。点击对应商品，跳转到商品详情页。</p>
<p><strong>底部导航栏</strong>：标红当前显示页面的按钮，点击相应页面的按钮，跳转到对应页面。</p>
<p>简要逻辑如下所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ZC0IUphkthiwEJcgPPKQ.png" alt width="649" height="842" referrerpolicy="no-referrer"></p>
<p><strong>5）思考</strong></p>
<p>B站的会员购页面设置较为简洁，顶部是搜索框和商品分类，中部是活动商品展示窗口，中下部以双列形式展示商品，便于用户查看更多的商品后再进行决策。</p>
<p>对于喜欢的IP，用户可以选择订阅，但是会员购页面并无“我的订阅“IP商品的推荐窗口，由于B站售卖的商品多是二次元商品，比起普通商品，用户对于个人感兴趣的IP商品关注度会更高。笔者认为在会员购页面需要添加一个”我的订阅“商品展示栏，便于用户即使了解自己关注IP的商品上新情况，增加用户的购买欲。</p>
<p>此外，在商品搜索页面，只有“搜索历史”和“搜索发现”，笔者认为添加一个“热搜”展示会更好。虽然会员购页面已有人气排行功能，但此功能按钮并不是很醒目，而且当用户进行商品搜索决策时，热搜有利于让用户了解大家感兴趣的商品是什么，有潜在的激发用户购买决策的潜力。</p>
<h3>6. 我的页面</h3>
<p><strong>1）页面名称：</strong>“我的”页。</p>
<p><strong>2）页面入口：</strong>点击底部导航栏的“我的”按钮，或是在首页点击用户自己的头像框，即可跳转到“我的”页面。</p>
<p><strong>3）页面结构</strong></p>
<p>按照从上到下、从左到右的顺序分为：二维码扫描按钮、主题设置按钮、日用或夜用设置按钮、个人信息展示栏、开通大会员栏、离线缓存按钮、历史记录按钮、我的收藏按钮、稍后再看按钮、发布视频栏、个人服务展示栏、底部导航栏。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Bx7aQl2k6nSyME5H6NET.png" alt width="644" height="446" referrerpolicy="no-referrer"></p>
<p><strong>4）页面逻辑</strong></p>
<p><strong>二维码扫描按钮</strong>：点击按钮，跳转到二维码扫描页面。</p>
<p><strong>主题设置按钮</strong>：点击按钮，跳转到主题设置页面。</p>
<p><strong>日用或夜用设置按钮</strong>：点击按钮，切换日用/夜用模式，按钮变为“切换夜用/切换日用”图标形状。</p>
<p><strong>个人信息展示栏</strong>：点击此栏，跳转到用户个人空间。</p>
<p><strong>开通大会员栏</strong>：点击此栏，跳转到大会员支付页面。</p>
<p><strong>离线缓存按钮</strong>：点击按钮，跳转到离线缓存视频页面。</p>
<p><strong>历史记录按钮</strong>：点击按钮，跳转到视频播放历史记录页面。</p>
<p><strong>我的收藏按钮</strong>：点击按钮，跳转到用户收藏视频页面。</p>
<p><strong>稍后再看按钮</strong>：点击按钮，跳转到用户个人的稍后再看视频页面。</p>
<p><strong>发布视频栏</strong>：点击“有奖发布”，弹出“内容上传”弹窗，点击弹窗内的选项，跳转到对应页面，点击弹窗外区域，弹窗消失。</p>
<p><strong>个人服务展示栏</strong>：点击此栏内的服务按钮，跳转到对应的服务页。</p>
<p><strong>底部导航栏</strong>：标红当前显示页面的按钮，点击相应页面的按钮，跳转到对应页面。</p>
<p>简要交互逻辑如下所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/7Yg2ovIoM5m5erJukJP7.png" alt width="651" height="855" referrerpolicy="no-referrer"></p>
<p><strong>5）思考</strong></p>
<p>由于比起其它视频APP，B站更加注重社区内容创作，因此在个人页面中，<strong>发布视频栏位于中部较为显眼的位置，便于激励用户进行视频的创作与上传。</strong></p>
<p>在视频离线缓存按钮、历史记录按钮等一栏中，并无用户点赞视频/投币视频按钮，笔者认为可能因为此功能与“我的收藏“有所重复。而且点赞/投币的视频对用户的重要程度不如收藏那么高，用户再次查看这些视频的概率较小，因此没有查询点赞/投币视频按钮。</p>
<p>此外，B站在此页设置了创作中心、直播中心服务按钮，有利于指导内容创作者进行创作，保证更多高质量内容的产出。</p>
<h3>7. 追番页面</h3>
<p><strong>1）页面名称：</strong>“追番”页。</p>
<p><strong>2）页面入口：</strong>点击首页的顶部导航栏的“追番”按钮，即可跳转到“追番”页面。</p>
<p><strong>3）页面结构</strong></p>
<p>按照从上到下的顺序分为：顶部导航栏、番剧轮播栏、看番工具栏、“猜你想追”番剧展示栏、“番剧推荐”栏、底部导航栏。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/bU7zgzopEBpKiPzCAXbV.png" alt width="652" height="535" referrerpolicy="no-referrer"></p>
<p><strong>4）页面逻辑</strong></p>
<p><strong>顶部导航栏</strong>：由用户头像、搜索框、游戏中心按钮、消息按钮、子页面切换栏组成，点击用户头像，跳转到“我的”页面，点击搜索框，跳转到“搜索页面，点击“游戏中心”按钮，跳转到“游戏中心”页面，点击“消息”按钮，跳转到“消息”页面，点击子页面切换栏的子页面按钮，跳转到对应子页面，且对应子页面的按钮标红和底部以红色边框标注。</p>
<p><strong>番剧轮播栏</strong>：轮播六部番剧/活动的推荐图，三秒切换一张展示图，点击图片，跳转到对应的视频播放/活动页面。</p>
<p><strong>看番工具栏</strong>：横向展示看番的工具按钮，右滑展示更多的看番工具，点击任一工具按钮，跳转到对应页面。</p>
<p><strong>“猜你想追”番剧展示栏</strong>：横向展示用户可能感兴趣的番剧，右滑展示更多的番剧推荐，点击“查看全部”，跳转到“猜你想追”页面，点击任一番剧，跳转到播放页面。</p>
<p><strong>“番剧推荐”栏</strong>：纵向双列展示推荐的番剧，点击番剧，跳转到播放页面，点击“查看更多”，跳转到“番剧推荐”页。</p>
<p><strong>底部导航栏</strong>：标红当前显示页面的按钮，点击相应页面的按钮，跳转到对应页面。</p>
<p>简要交互逻辑如下所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/zk2kkMVw8ZyhlwckEYeU.png" alt width="654" height="714" referrerpolicy="no-referrer"></p>
<h3>8. 影视页面</h3>
<p><strong>1）页面名称：</strong>“影视”页。</p>
<p><strong>2）页面入口：</strong>点击首页的顶部导航栏的“影视”按钮，即可跳转到“影视”页面。</p>
<p><strong>3）页面结构</strong></p>
<p>按照从上到下的顺序分为：顶部导航栏、影视轮播栏、影视工具栏、“正在热播”影视展示栏、底部导航栏。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/i4LzXsbBSrJfNSo54bFt.png" alt width="653" height="511" referrerpolicy="no-referrer"></p>
<p><strong>4）页面逻辑</strong></p>
<p><strong>顶部导航栏</strong>：由用户头像、搜索框、游戏中心按钮、消息按钮、子页面切换栏组成。点击用户头像，跳转到“我的”页面；点击搜索框，跳转到“搜索页面；点击“游戏中心”按钮，跳转到“游戏中心”页面；点击“消息”按钮，跳转到“消息”页面；点击子页面切换栏的子页面按钮，跳转到对应子页面，且对应子页面的按钮标红和底部以红色边框标注。</p>
<p><strong>影视轮播栏</strong>：轮播六部影视/活动的推荐图，三秒切换一张展示图，点击图片，跳转到对应的视频播放/活动页面。</p>
<p><strong>影视工具栏</strong>：横向展示影视的工具按钮，右滑展示更多的影视工具，点击任一工具按钮，跳转到对应页面。</p>
<p><strong>“正在热播”影视展示栏</strong>：纵向双列展示展示正在热播的影视作品，点击任一影视作品，跳转到播放页面。</p>
<p><strong>底部导航栏</strong>：标红当前显示页面的按钮，点击相应页面的按钮，跳转到对应页面。</p>
<p>简要交互逻辑如下所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/g6T50n5Utn30WyThKFCh.png" alt width="639" height="754" referrerpolicy="no-referrer"></p>
<p><strong>5）思考</strong></p>
<p>“影视”页面的布局比“看番”页面更为简单，少了“猜你想追”页面，且与其它视频播放APP相比，在视频展示区，其没有把“新剧推荐”放在最前面的位置，也没有此展示栏。这可能与B站在影视方面的资源比较少有关，没有太多的上新资源，因此减少了新剧推荐功能。</p>
<p>笔者认为<strong>需要增加“猜你想追”功能；</strong>虽然影视业务不是B站的主业务，但是只有更加定制化、以用户为中心的服务才能提升用户体验，从而增加用户粘性。</p>
<h3>9. 游戏中心页面</h3>
<p><strong>1）页面名称：</strong>“游戏中心”页。</p>
<p><strong>2）页面入口：</strong>在首页，点击顶部导航栏的“游戏中心”按钮，即可跳转到“游戏中心”页面；或是在“我的”页面，点击服务栏的“游戏中心”按钮，可以跳转到“游戏中心”页面。</p>
<p><strong>3）页面结构</strong></p>
<p>按照从上到下、从左到右的顺序分为：返回按钮、搜索框、下载管理按钮、消息按钮、单列推荐游戏展示栏、双列推荐游戏展示栏、添加游戏中心至桌面弹窗、底部导航栏。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/bcjJE0p87qIP1pnLd0TZ.png" alt width="651" height="579" referrerpolicy="no-referrer"></p>
<p><strong>4）页面逻辑</strong></p>
<p><strong>返回按钮</strong>：点击退出“游戏中心”页面，返回前页面。</p>
<p><strong>搜索框</strong>：点击此框，跳转至搜索页面，显示历史搜索、热搜游戏、热门游戏词条。</p>
<p><strong>首要推荐游戏展示栏</strong>：半屏展示APP最近推荐的游戏，点击跳转到对应游戏页面。</p>
<p><strong>单列游戏展示栏</strong>：纵向单列展示推荐的游戏，点击任一游戏，跳转到对应的游戏介绍页面，点击右上角的“更多”按钮，跳转到“游戏推荐”页面。</p>
<p><strong>底部导航栏</strong>：标蓝当前显示页面的按钮，点击相应页面的按钮，跳转到对应页面。</p>
<p>简要交互逻辑如下所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/rtYsRUmUyc8FXY8f13hX.png" alt width="657" height="1282" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">七、总结与思考</h2>
<p>B站是以视频社区为核心，围绕泛二次元内容展开的APP，其在产品结构上结合了视频APP和社区APP的特点。</p>
<p>在内容生产上，通过<strong>话题/活动引导、MCN合作、数据分析中心、视频/内容创作母版模板等形式，引导UP主进行视频的创作，</strong>保证了原创视频的持续产出。</p>
<p>在内容分发上，<strong>采用去中心化的分发规则</strong>，让更多的视频被用户看到，同时，采用排行榜、热搜、推荐的形式，提高高质量的视频的观看量、互动量，从而保证社区内容的质量。</p>
<p>而在内容互动和反馈上，采用了点赞、投币、收藏、不喜欢、转发、评论、弹幕等<strong>多样化的形式，鼓励用户互动</strong>，增加社区活跃度，而反馈量的增多也给了创作者更多的创作动力，从而形成正向循环。</p>
<p>从内容的排版和交互来看，因为B站多数原创视频是中等长度的视频，视频承载的有价值信息更多，不能完全归类为KILL TIME的无脑娱乐视频 ，所以视频的<strong>陈列方式主要以纵向双列为主</strong>，不似短视频APP的单列沉浸式模式，给了用户<strong>更多的选择空间。</strong></p>
<p>此外，B站排版也不似长视频APP的横向滑动排版，这减少了交互的复杂程度，也<strong>保证了更多的内容能被用户看到</strong>。</p>
<p>而从内容推荐的优先级上看，B站推荐的优先顺序是<strong>用户感兴趣内容≥历史观看内容＝热门内容</strong>，打造一个以“我”为核心的社区内容推荐，保证了用户能快速找到喜欢的内容，从而参与社区讨论，增加用户的社区认同感。</p>
<p>随着B站的发展，其也在破圈，努力提高APP的受众范围，致力于发展多样模式的营收体系，通过不同的产品功能，引导用户进行消费，摆脱对于游戏业务收入的过度依赖。分别在直播、影视、知识教育、图文专栏等布局，使产品内容更加多元化。</p>
<p>但目前这些功能都不是B站的一级功能，还在试验和发展阶段，后期可以随着市场需求和营收占比的变化，适当提升几个业务的重要性，把它们做成一级功能或放在更加显眼的位置。</p>
<p>但是破圈的同时也需要把握好节奏，考虑老用户的感受，让社区氛围不变质，把控好原有的细分社区圈子的内容质量，不让老用户因为“扩圈”导致的氛围变化而离开平台。这<strong>需要做好新用户的成长体系指引，引导新用户认识、接受、融入B站的社区文化， 从而为B站的持续发展献一份力。</strong></p>
<p>此外，就B站目前的结构而言，还未实现闭环。虽然在流量方面摆脱了对第三方平台的依赖，但在支付体系上还依赖其它平台，B站在2021年初已开始布局支付体系，期待以后的表现。</p>
<p><strong>参考文献</strong></p>
<p>街机时代. (2020年12月15日). b站用户画像2020_B站用户行为分析非官方报告. 检索来源: CSDN: https://blog.csdn.net/weixin_30979229/article/details/112125176</p>
<p>木子. (2020年7月1日). 社交产品系列：社区类产品迭代设计. 检索来源: 人人都是产品经理: http://www.woshipm.com/pd/4049306.html</p>
<p> </p>
<p>本文由 @Conlin  原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4640553" data-author="1260223" data-avatar="http://image.woshipm.com/wp-files/2021/04/gwBSRqnCbkU8PnCF1k10.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            