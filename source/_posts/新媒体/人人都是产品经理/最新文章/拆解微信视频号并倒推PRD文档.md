
---
title: '拆解微信视频号并倒推PRD文档'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2021/11/6Y61ig3yCNjrTUtaKRTw.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 08 Nov 2021 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2021/11/6Y61ig3yCNjrTUtaKRTw.jpg'
---

<div>   
<blockquote><p>编辑导语：目前，短视频市场仍然在稳健增长。继主要产出图文的公众号后，微信推出了视频号，补足了基于现实好友的短视频社区的空缺，促进了公域流量和私域流量的互相转换。这篇文章从产品说明、产品定位、需求分析、产品结构等方面入手，分析了微信视频号的“视频观看”和“视频创作”两大核心功能。一起来看看吧！</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-711251" src="https://image.yunyingpai.com/wp/2021/11/6Y61ig3yCNjrTUtaKRTw.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>该PRD文档是以人人都是产品经理网站上已有的其他应用PRD文档为参考，以微信视频号为主题撰写而成。由于作者人在国外，无法正常使用直播功能，且直播属于后续迭代添加功能，因此本PRD文档主要关注的是“<strong>视频观看</strong>”和“<strong>视频创作</strong>”两大核心功能。作者本身初入产品行业，本文内如有不当或错误之处，请大家海涵，也请大家斧正。</p>
<h2 id="toc-1">一、文档综述</h2>
<h3>1. 版本修订记录</h3>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/P6uzJhAGaESEnlAP0v1l.png" alt width="602" height="85" referrerpolicy="no-referrer"></p>
<h3>2. PRD 输出环境</h3>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/diYYvyt5ce1bZ6oF0pFL.png" alt width="598" height="202" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、产品说明</h2>
<h3>1. 产品简介与背景介绍</h3>
<p>微信是腾讯于2011年1月21日推出的一款即时通讯软件，提供语音对话，朋友圈，支付，公众号，小程序，视频通讯等功能。</p>
<p>通过十年发展，微信不仅成功将发短信写入历史，更将其变成了一种生活方式，一款具有11亿日活的国民级产品。2020年底，每天有10.9亿用户打开微信，3.3亿人进行视频通话，7.8亿人进入朋友圈，1.2亿人发朋友圈，朋友圈每天有1亿条视频内容。每天有3.6亿人进入公众号，4亿用户使用小程序。</p>
<p>在目前的微信生态体系中，公众号对内容产出具有较高的要求，只适合少部分人使用。而朋友圈主要以图片和简短文字为主。同时，随着短视频和4/5G网络的快速发展，视频化表达已经被越来越多用户接纳并采用，公域流量饱和而私域流量逐渐发力，在微信生态体系中应该出现一个视频内容平台。</p>
<p>因此我们计划推出“视频号”功能，我们将视频号定义为一个人人都可创作的短内容平台。一方面，我们希望通过视频号能够满足C端用户“视频化表达”的核心诉求，在另一方面，我们更期待将微信服务号、公众号、视频号与直播的功能相互打通，从而实现B端官网“微信化”，公域流量与私域流量互相转换的进程。</p>
<h3>2. 行业概述</h3>
<p><strong>短视频市场在几年前的快速爆发后，已经进入了稳健增长的时期。</strong>CNNIC数据显示，2020年6月，我国短视频用户规模已经达到81786万人，使用率高达87%。短视频在网民人均app每日使用时长中名列前茅，占29.6%。短视频月活用户规模增速虽然有所放缓，但在2020年整体规模已达8亿。</p>
<p>在行业平稳发展的同时，业内各大平台也在不断探索多元化和商业化的模式，如抖音开设了商品橱窗，引入更多KOL直播带货等。2020年我国短视频行业市场规模已经突破2000亿元。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/KyVA4GPva1vQCMNAgGLY.png" alt width="599" height="210" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、 产品定位</h2>
<h3>1. 竞品分析</h3>
<p>明确视频号的产品定位离不开对当前市场上主要竞品的分析，而短视频领域无非抖快二家。</p>
<p><strong>（1）抖音</strong></p>
<p>抖音的定位为<strong>“优质爆款”，内核是高质量的娱乐视频</strong>，重算法重消费，轻关系轻生产。</p>
<p><strong>价值观：</strong>抖音的slogan为“记录美好生活”，强调帮助用户消费“美好”的视频内容</p>
<p><strong>算法上：</strong>“<strong>中心化</strong>”，强调优质内容得到足够的流量和分发，实现优质内容精准匹配用户。</p>
<p><strong>交互上：</strong>采用<strong>单列视频流</strong>的方式，在精准推荐算法的支持下强化用户的沉浸式观感体验。</p>
<p><strong>运营上：</strong>通过邀请优质视频创作者入驻，用户成长体系，流量倾斜，补贴等方式鼓励优质内容产出。在出现“爆款”视频后通过原声做同款，视频模板，以及如今的剪辑工具剪映等功能来便利创作端，降低创作门槛，帮助更多创作者复现爆款视频。另一方面，通过明星联动，春节红包等等大型宣传活动吸引消费端，提高品牌知名度。</p>
<p><strong>效果：</strong>这样的产品策略保证了抖音强大的信息流和激增的用户数量，也使信息流广告得到了巨大成功。但另一方面，由于只有优质视频得到大量分发，使得用户和用户之间，用户和视频制作者之间的关系较为薄弱，缺乏紧密关系，公域流量为主，私域流量薄弱。</p>
<p><strong>（2）快手</strong></p>
<p>快手的定位为<strong>“内容/社交社区”，内核是以直播和短视频为表现形式的社区</strong>，重关系重生产，轻算法轻消费。</p>
<p><strong>价值观：</strong>快手秉持“<strong>公平，普惠”</strong>的价值观，强调短视频只是一个载体，更重要的是通过视频内容形成社区生态，实现人与人之间的链接。</p>
<p><strong>算法上：“去中心化”，强调中长尾视频也能得到分发。</strong>快手号称将70%的主要流量分发给了普通用户/素人制作者，并且引入“基尼系数”，确保头部PGC视频不会过多挤占用户时长。</p>
<p><strong>交互上：</strong>（8.0版本前）采用双列视频流的方式给予用户主动选择的方式，也提供更多的视频曝光量，让用户可以选择感兴趣的主播/视频。在8.0版本后，快手逐步强调内容，强调算法推荐视频，新增以优质视频为主的精选tab，采用和抖音一致的单列视频流形式。</p>
<p><strong>运营上：</strong>早期的快手由于缺乏竞争对手，一直采取轻运营的策略。自2018,19年以来开始开始发力，类似抖音一方面推出“光合计划”等运营方案通过流量，补贴等方式扶持中小视频制作者和MCN机构，并推出创作者激励计划鼓励创作。另一方面开始邀请明星，如周杰伦入驻快手，以吸引更多的内容消费者。</p>
<p><strong>效果：</strong>快手的产品定位和策略决定其对内容生产者较为友好，质量稍差的内容创作者也能得到足量分发，从而提升创作动力。同时，粉丝和创作者之间的关系更加紧密，用户相信创作者并愿意为其买单。这也使得直播成为快手最为重要的经济支柱。</p>
<p>可以说目前在泛娱乐内容的短视频市场已经相对饱和，市场增幅放缓，进入存量市场。抖快两家用户重叠度不断上升，都在做用户下沉和渗透。因此在当前竞争格局下，仍然选择以“泛娱乐”作为主要内容是不明智的。</p>
<p>另一方面，抖音和快手仍属于陌生人社交/半熟人社交，其关注账号，好友大多不是现实生活中的好友（当然抖音目前正在做关系网络的强化），而基于现实好友的短视频社交社区目前仍然是一个空缺，且目前看来也只有腾讯有能力做。</p>
<h3><span style="font-family: 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', STHeiti, 'WenQuanYi Micro Hei', Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal;">2. </span>产品定位</h3>
<p>笔者认为微信视频号的主要定位在于<strong>“个人品牌展示”。</strong></p>
<p>微信作为一款即时通讯软件，其所具有的核心功能，或者从某种程度上说唯一的功能，便是信息的传递（发出和接收）。而微信目前所承载了多数用户的社交关系网络，决定了用户在微信中发出的每一段公开信息（公域），都将影响他的社会形象，甚至于社会自我。换言之，<strong>微信账号在公域中发出的每段流量都将塑造他的品牌。</strong></p>
<p>该观点可以由公众号为之作证。公众号的slogan为：再小的个体，也有自己的品牌。事实上，公众号同样承担着“个人品牌展示”的使命诞生。但是由于微信在迭代历程中对创作平台以及创作内容，形式（长文章）的限制（参见2020微信公开课pro），导致公众号的创作门槛不断提升，导致只有“大个体”，PGC才能拥有自己的品牌。</p>
<p><strong>视频、直播，是对普通人创作门槛更低的一种创作形式。</strong>视频创作端具有大量的模板，配乐，滤镜，用户甚至只需要拍摄一张图片便可轻松编辑出（短）视频。而直播更是一种无需过多准备的创作形式，在理想的状态下，用户拿起手机便可以直播，直播的内容仅仅为他看到的，在做的事情。</p>
<p>视频号承载着公众号未能完成的使命，让所有的用户通过浏览行为与视频创作，打造自己的品牌。而进一步发展，B端账号也属于视频号的个体用户，公司同样可以通过视频号的平台来塑造自己的品牌形象，在未来视频号可能会成为公司市场营销的一块主阵地。</p>
<p>此外，该定位与公众号具有两个身份的账号体系并不冲突，允许用户操作不被好友察觉，进行私密点赞必然是一个较大较强烈的需求。只是笔者认为视频号更大的价值在于用户账号形象的塑造，而非内容的消费。</p>
<h3>3. 内容调性与算法</h3>
<p>在内容调性上，一方面由于抖快的竞争，另一方面由于用户个人账号塑造的诉求，视频号的视频内容调性必然不可能类似抖音以幽默，搞笑视频为主，而可能更多以<strong>生活类，情感类甚至时政类</strong>为主。</p>
<p>因为这类内容更可能帮助用户打造个人形象。</p>
<ul>
<li>例1，相比于点赞/创作王者荣耀的操作记录，创作一个出游的精致生活vlog更能帮助用户打造热爱生活，心灵手巧的正面形象。</li>
<li>例2，点赞中国某项政策成效视频，更容易帮助男生打造阳光正面，热爱国家的形象。</li>
</ul>
<p>这一推测也得到了数据的验证，根据东方证券数据，情感/生活/影视/时政是视频的主要热门内容。</p>
<p>在视频算法上，视频号必然是以“<strong>去中心化</strong>”为主的。利好中长尾创作者算法，因为视频号的核心不在于向用户推荐优质的视频内容，让用户沉浸不断刷视频，而在于帮助“再小的个体”传递视频信息，打造个人形象。而采用中心化为主的算法方式将极大削弱UGC的创作热情，并且导致PGC，MCN的大量流入。</p>
<h2 id="toc-4">三、需求分析</h2>
<h3>1. 用户分类</h3>
<p>微信目前已有约12亿日活用户，属于国民级产品，用户基本覆盖全年龄段。</p>
<p>《2020 短视频用户价值研究报告》数据显示，短视频用户逐渐呈现出全民化、大众化的趋势。总体用户数量已经超过8亿，观看短视频的网民占比数达92%，同时40岁以上的用户数量逐渐增多。</p>
<p>同时，根据用户的行为及偏好，报告将个人内容消费者分为6大类：</p>
<ul>
<li>活跃自我派：重度用户，年龄分布平均，女性占比略高，通过短视频追寻情感寄托，最喜爱情感类短视频；</li>
<li>现实开放派：中度用户，40岁以上用户较高，学历收入较高，注重短视频的社交和陪伴属性，倾向泛生活类短视频；</li>
<li>实用求知派：重度用户，喜欢现实交友，以学习/工作提升为主要目的，最喜欢历史，人文等知识类视频，内容付费意愿最低。</li>
<li>自由随性派：轻度用户，男性占比略高，观看短视频动机分散，依赖平台的内容推荐。</li>
<li>休闲娱乐派：轻度用户，理性消费，通过短视频休闲解压，内容偏好多远，主要以泛娱乐内容为主，同时创作短视频积极性高。</li>
</ul>
<h3>2. 需求场景</h3>
<p>在核心需求上，视频号和抖快都满足用户<strong>休闲娱乐</strong>以及<strong>表达自我</strong>的需求，只是视频号更重后者。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/XNCs7QUrwruXpmS8lXJF.png" alt width="500" height="319" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/PP4OEFgSYhHe7Hwi6Vel.png" alt width="500" height="550" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">四、产品结构</h2>
<h3>1. 视频号功能结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/WfLUvHA0hIb5ousLtUZO.png" alt width="600" height="494" referrerpolicy="no-referrer"></p>
<h3>2. 视频号信息结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/TZH7TRz3LFMeYoHm9xKW.png" alt width="600" height="592" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">五、全局说明</h2>
<h3>1. 账号设置</h3>
<ul>
<li>账号分为Wechat身份，视频号身份和一个新建身份；</li>
<li>初始登录与浏览视频使用自动采用Wechat身份；</li>
<li>当用户进行视频制作/直播操作时，要求用户注册视频号身份后才可继续操作；</li>
</ul>
<h3>2. 键盘交互</h3>
<ul>
<li>点击搜索框、评论框、编辑框时页面底部弹出键盘。</li>
<li>进行账号创建时，点击文字框时页面底部弹出键盘。</li>
</ul>
<h3>3. 网络异常</h3>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/q6wIsjYZbk3zACxDKunO.png" alt width="267" height="333" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/laJLPMCw77Gc19qgFEyd.png" alt width="264" height="331" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/nYyd1oDfVxjT0n9CPwo7.png" alt width="266" height="314" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">六、业务流程图</h2>
<h3>1. 观看视频/直播流程</h3>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/cwbEuDm5WCO6emjTgsoM.png" alt width="400" height="611" referrerpolicy="no-referrer"></p>
<h3>2. 发布视频流程</h3>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/joYePL5F45mL8XheLg6R.png" alt width="600" height="362" referrerpolicy="no-referrer"></p>
<p>视频号的视频发布有直接拍摄，相簿选取和使用秒剪制作三种模式。</p>
<p>在个人主页进入视频发布流程的用户，在发布视频后仍返回个人主页；通过首页个人设置进入视频发布流程的用户，在发布视频后返回首页，同时显示刚发布的视频。</p>
<h2 id="toc-8">七、页面逻辑图</h2>
<h3>1. 首页逻辑图</h3>
<p>在该页面包括了切换tab、点赞、评论、进入个人设置及主页等操作。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/T2TB8UrDvYUsZUZYuqpW.png" alt width="600" height="625" referrerpolicy="no-referrer"></p>
<h3>2. 发布视频页面逻辑图</h3>
<p>该逻辑图主要包括了从个人设置页面发布视频的流程。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/emioMZJqK4l8BAxP8fxJ.png" alt width="598" height="440" referrerpolicy="no-referrer"></p>
<h2 id="toc-9">八、核心功能详细说明</h2>
<h3>1. 首页功能详细说明</h3>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/fGkyIY4bXUO0gtEAHqwS.png" alt width="600" height="636" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/FUZ2H0d5LisLlGfjDT3i.png" alt width="600" height="642" referrerpolicy="no-referrer"></p>
<h3>2. 视频发布功能详细说明</h3>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/qc367olOiZaz0HK5SyWL.png" alt width="599" height="458" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/9tLZlisnrAotmcKJToEs.png" alt width="600" height="874" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/11/AjEKtKl8q2sMoSLx3b6k.png" alt width="601" height="126" referrerpolicy="no-referrer"></p>
<h2 id="toc-10">九、小结</h2>
<p>微信视频号自2020年1月内测、9月公测以来，保持着极高频率的更新和快速的发展速度，目前视频号的DAU已经超过三亿，超越快手成为仅此抖音的第二大短视频产品。</p>
<p>同时，视频号独有的社交推荐功能，具备的巨大流量潜力和曝光量，在微信生态体系中承担的公私流量转化核心地位，甚至于其源自微信“小而美”的产品设计理念，都让作者对这款产品的未来持有很高的期望。</p>
<p>参考：东方证券传媒行业短视频系列报告；2020，2021年微信公开课。</p>
<p> </p>
<p>本文由 @cky 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5199302" data-author="1318268" data-avatar="https://static.qidianla.com/woshipm_def_head_1.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            