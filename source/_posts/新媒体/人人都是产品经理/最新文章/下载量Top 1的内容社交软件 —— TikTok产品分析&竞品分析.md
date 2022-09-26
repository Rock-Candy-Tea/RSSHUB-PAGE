
---
title: '下载量Top 1的内容社交软件 —— TikTok产品分析&竞品分析'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/09/H5E5cmS11CrmLuuhu4Rl.png'
author: 人人都是产品经理
comments: false
date: Mon, 26 Sep 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/09/H5E5cmS11CrmLuuhu4Rl.png'
---

<div>   
<blockquote><p>互联网产品出海中的佼佼者，当属TikTok。本篇文章中作者结合实际经验对TikTok的产品与初步竞品进行了一系列详细的分析，感兴趣的小伙伴们快来一起看看吧。</p>
</blockquote><p><img data-action="zoom" class="size-full wp-image-862826 aligncenter" src="https://image.yunyingpai.com/wp/2022/09/H5E5cmS11CrmLuuhu4Rl.png" alt referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、简单背景</h2>
<p>TikTok自2018年额全球下载量超过Instagram和Facebook成为下载量第一的内容社交软件。</p>
<p>应用市场短视频（Short-form video）分类中总榜第一，远超Likee和Lasso（总榜分别63和598），热度仅次Instagram，Facebook和YouTube。</p>
<p>2022年月活用户超过十亿，月人均使用时长在24小时,收入（主要为广告）接近40亿美元。</p>
<p>TikTok信息流内容加上其嵌入的推荐算法使‘刷’短视频成为了很多年轻人的生活方式。</p>
<h2 id="toc-2">二、TikTok的底层逻辑</h2>
<p>TikTok如此受欢迎和活跃用户增长速度如此快离不开其对人性的洞悉；实现这一目的其底层逻辑是TikTok的推荐算法。</p>
<p>从结果倒推：</p>
<ul>
<li>用户不需要注册账户，或只需要一键绑定任何一个社交账号就可以全屏观看视频内容；</li>
<li>内容上，最长三分钟，平均9-15秒的视频省略了不必要的铺垫和结尾，省略了开始的铺垫直接把最精华和高潮的部分展示给用户，在观看者注意力和兴趣达到峰值的时候也是内容最精彩的部分–带来的是即时满足感和沉浸感；</li>
<li>在延时和即时满足之间，人们倾向选择即时满足带来的快感，在主动学习和被动接受信息之间，惰性使得大多时候人会选择后者；</li>
<li>不需要思考的满足感和刺激是娱乐短视频内容成功的核心；</li>
<li>然后就是下划到下一个视频，无法预知下一个视频内容的刺激和意外感也是对人性的迎合。</li>
</ul>
<p>通过这种设计加上算法的嵌入带来的是爽感和刺激感的循环，用户每看一个视频，他的信息矩阵会不断更新，反哺算法强化用户的喜好；即刷得越多也就更能触达好的内容：虽然我不知道下一个视频是什么，但推荐算法大概率会推荐我感兴趣的内容，我才会更想往下刷。</p>
<p>这个基础上，算法和流量相互成就，带来的是流量价值和变现方式。（最直接的，广告）</p>
<h2 id="toc-3">三、有关产品</h2>
<h3>1. TikTok 推荐算法</h3>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/sKs45s4nfIq6WXqZ9e1S.png" alt width="552" height="485" referrerpolicy="no-referrer"></p>
<p>TikTok的推送逻辑为中心划的漏斗算法，发布在平在上的大多视频会从底层流量池获得100-1000的基础播放量，并根据用户反馈的数据判断视频质量（完播率/点赞 etc.），如果判断为高质量视频就会进入下一个流量进行叠加推送给目标用户；YouTube则是从通过DNN推荐模型（TikTok也是），从百万量级的视频库中根据用户特征，观看历史和场景筛选出少量视频，通过排序最终呈现给用户。</p>
<p>TikTok的流量池机制一定程度上鼓励了UGC，但对偏专业和深度内容的推荐，YouTube的中心化推荐机制一定程度上更能输出高质量的视频。</p>
<p>好处是更大程度契合用户偏好，即上述的底层逻辑。而坏处则是会产生信息蚕房，导致审美疲劳和内容相对单一化。</p>
<p>适当进行一定比例的跨域推荐可以有效打破信息蚕房：通过隐形特征挖掘共有属性进行跨域推荐。</p>
<p>比如在属（Attribute）层面上的相似属性：给喜欢看NBA相关视频的用户推荐CBA和国内街球篮球比赛(综艺)视频；如果跨域幅度更大可以推荐篮球教学，球鞋评测等作品；在品类（type）层面的相似属性：篮球和电子竞技都属于团队竞技体育，偏好用户重叠度较高；给偏好篮球分类的用户推荐电子竞技分类的作品；跨域推荐不同大品类的作品：比如用户在众多篮球解说视频中偏好美娜和小七等美女主播的解说，那么可以给用户推荐其他任意的美女视频。</p>
<h3>2. 交互设计</h3>
<p><strong>（1）鼓励互动和社交</strong></p>
<p>TikTok美国用户中，10到19岁占37.2%，20到 29岁占26.3%，30到39岁占16.7%。63.5%的用户都在30岁以下，（statista）该年龄段的用户对于社交媒体显然更熟悉，使用频率更高，需求更大。</p>
<p>而根据AppAnnie和Hootsuite的数据，使用安卓手机的TikTok用户每月在TikTok上花费大约13个小时，超过了Instagram。</p>
<p>而Instagram作为图片社交软件，又添加了Reel的短视频功能，和Tiktok相似，都采用了UCG+PCG的内容生产方式。</p>
<p>那对于部分使用TikTok替代Instagram的用户来说，满足社交和互动需求则显得尤为重要。</p>
<p>TikTok中，用户首页，快捷关注，赞，评论，分享，旋转音乐光盘等按钮垂直排列在视频播放主页右侧。</p>
<p>按钮较大，占据位置明显，鼓励用于进行社交操作，也与短视频适合分享，快速传播的特点契合。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/yCYMXTpmxY2oPMFE7EJG.png" alt width="576" height="916" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">HomePage-首页</p>
<p>TikTok采用进入应用后默认启动播放的交互形式，让用户立即进入到接受碎片化信息的环境。首页的播放主页顶端有推荐，关注两个Tab。</p>
<p>交互方式上，上划为下一个视频；右划为作者信息；双击点赞，单机暂停。在无wifi连接的情况下会弹出模态框提醒打断观看。</p>
<p>创作者注释，音乐原声等视频基本信息都在底端显示无论是分享，社交，介绍，查看音乐，自己创作，所有内容基本可以在首页找到，这也符合用户操作简单，功能路径短的需求。</p>
<p>TikTok中播放主页的交互方式都具有方便快捷的特点，用户对于短视频的需求有相当一部分时间是在零散时间使用，所以交互方式应该高效。</p>
<p><strong>（2）拍摄作品</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/b4b47Ydq184ZdTFUqSaV.png" alt width="568" height="658" referrerpolicy="no-referrer"></p>
<p>TikTok大约有55%的用户制作内容，点击在底部中心的Tab可以直接进入拍摄/剪辑的功能。</p>
<p>创作者拍摄作品的的界面以高效简洁为主，大多不超过三级；主要服务于特定种类的视频，如Hashtag挑战，回应评论，使用特定模板的UCG(主要)和PCG。</p>
<p>其中主要长/短视频都有直接的拍摄时长设定，分类明确。其中顶部的添加音乐的功能较为成熟。</p>
<p>TikTok中大约80%的热门视频添加了音乐：从观看者的角度，音画结合的内容相比没有背景音乐更容易获得观看和留存；而从创作者的角度，Add Sound这一功能的全面和成熟性也有益于创作出优质内容。</p>
<p>在特定品牌或者KOL的带动下使用相同背景音乐也会给创作者带来更多内容和关注。</p>
<p><strong>（3）剪辑</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/rsQ8xewqs7tqbmuhV7H4.png" alt width="569" height="877" referrerpolicy="no-referrer"></p>
<p>对于使用应用内置剪辑功能的创作者大多可能是普通用户，PCG在剪辑内容上更偏向于pc端的剪辑软件。在保证功能相对全面的同时，内置的剪辑插件也要达到操作简单清晰（2-3级），有效提高创作质量的目的。</p>
<p>在上传视频素材之后，其中滤镜，贴纸，降噪，音乐，效果，字幕，美颜，细分剪辑的功能都相对完整且创作者在每个功能下都可以用简单直观的操作达到自己想要的效果。（如效果功能可以通过长按精确控制时常，并自动暂停视频让创作者选择下一个效果 etc.）对于PCG的创作者来说极易上手并且功能全面。</p>
<p><strong>（4）作品发布</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/SOAu3sG3L9Dp3wyhCpdw.png" alt width="589" height="819" referrerpolicy="no-referrer"></p>
<p>发布作品的页面中的功能主要有编辑视频主题（包括Hashtag，Refer，地点，链接 etc.），权限设置以及自动分享。</p>
<p>每个功能的级数不超过两个，交互效率高，目的直观；和Instagram，Youtube一样，创作者在视频发布前的最后一步也是设置权限；撰写视频主题，发起标签挑战等内容本身外的附加信息。</p>
<p>作品发布后，创作者可以根据自己的目标进行推广和管理互动内容。</p>
<h3>2. 竞品概况</h3>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/0NJy26kuLZyQzN8cX92V.png" alt width="575" height="714" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、TikTok vs YouTube</h2>
<h3>1. SWOT</h3>
<p><strong>（1）TikTok SWOT</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/oP2A7tFE24vb1d7P6WPo.png" alt width="589" height="345" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/cmlTz4vwmRIiPA0EGcs5.png" alt width="585" height="336" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/6479ta8fAaWpc4ug8jlb.png" alt width="585" height="227" referrerpolicy="no-referrer"></p>
<p><strong>（2）YouTube SWOT</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/jjyEyh74CSUOA4YuOHRk.png" alt width="582" height="319" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/iQeSVVqBxxhPobU9aNeI.png" alt width="590" height="283" referrerpolicy="no-referrer"></p>
<h3>2. 为什么选YouTube作为竞品分析对象以及分析的目的</h3>
<p><strong>（1）视频内容</strong></p>
<p>YouTube中/短长度的视频对应了TikTok的视频长度和内容（小于5分钟），不同于处在增长期和成熟期之间的TikTok，用户对YouTube的心智更成熟；不同用户群体对YouTube短内容的期待和诉求是确定的且对TikTok有参考价值。</p>
<p>目的是通过YouTube用户对短视频内容的偏好数据找到内容上的重点：对于YouTube已有可行的短视频内容，哪些是TikTok可借鉴/不可借鉴的。</p>
<p><strong>（2）在电视端（CTV）观看的习惯</strong></p>
<p>2021年北美YouTube的用户在CTV观看视频内容的比例超过一半，除了和Netflix对标的长影视内容，直播/娱乐/新闻 etc. 这些在TikTok上同样有很大热度的内容也是电视端用户的偏好分类；不同于移动端，在电视端观看的用户场景不一样，诉求不一样；信息流的形式可能不再适用于电视端；分析目的是看TikTok内容在电视端的可行性，如何发挥算法优势适应电视端。</p>
<p><strong>（3）YouTube社区功能</strong></p>
<p>YouTube的社区属性比TikTok强，除了内容本身和产品设计，它的社区功能是一个很重要的原因。YouTube社区文化的基础是以优质内容出发，多次且高质量的人与人（创作者与观众），人与内容的连接和互动，从而建立情感和社交属性，社区氛围更浓。</p>
<p>短期看培养时间长，增长曲线缓，但观众通过社区功能的投票/预告/民意调查能直接影响创作者的内容，创作者也能更好知道观众的诉求，是个良性循环。</p>
<p>分析目的是参考YouTube的社区功能，TikTok发展社区文化的可能性有哪些。</p>
<p><strong>（4）社区类产品的可能性</strong></p>
<p>垂类社区（Vertical Communities）在北美社交细分品类中同比增长排名第三（MAU），排在Friends Discovery和Professional之后。北美市场报告显示超过一半的社交媒体软件用户会在平台上直接购物，而相当一部分用户群体中超过一半的人会在YouTube，Instagram，TikTok这种内容社交平台上了解新产品。</p>
<p>参考国内抖音的兴趣电商，商户触达用户的途径很大程度上依赖于观看时长和观看量；从用户角度，关注或者刷到的KOL代替自己主动选品，一定程度上剥夺了用户的自主选品的主动性；社交电商的优势在于直观/简洁/符合兴趣，RedayCloud一项数据显示超过30%的购物网站用户认为结账和创建账户的过程太复杂，而社交电商简化了这个过程。</p>
<p>TikTok的算法和流量优势会给其直播电商和广告带来不错的转化率；然而更高质量，高颜值，小众和专业是新一代（90s）消费群体的消费习惯改变的趋势。</p>
<p>垂类社区可以更好的让用户认识品牌，做出购买行为，如母婴/汽车/运动类，细分化的平台是消费趋势。TikTok的优势在于算法和流量；产品设计和用户筛选/匹配是需要解决的问题。</p>
<h3>3. 视频内容</h3>
<p><strong>（1）用户画像对比</strong></p>
<p>基本数据（2022）:</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/2hXRJ4uHnXY3eTnk5a5f.png" alt width="586" height="269" referrerpolicy="no-referrer"></p>
<p>年龄分布：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/thAHelCJtGQwzlUVvMye.png" alt width="579" height="287" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（darareportal）</p>
<p>18-24年龄段的用户中，TikTok在该年龄段占比为43.4%，比YouTube的14.5%高出近三倍，而在该年龄段下，TikTok的男女比例为3:4，而YouTube为4:3。</p>
<p>可以看出18-24岁的年轻群体，尤其女性，是TikTok的主要受众之一，年轻女性这一单一群体在TikTok用户中所占的比例最大，18-34这一年龄段的女性占总用户40.9%。</p>
<p>YouTube的主要受众则是成年男性，18-44岁的用户中男性占到了75%，总体占29.1%。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/aNd3z3GIa0LYf2jonuuK.png" alt width="541" height="390" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（YouGov）</p>
<p>每个频率分类的用户分布大致一样，需求/用户群体不完全重合，其中TikTok和YouTube的活跃用户（每天访问/使用两次）以上的用户都超过50%。光看这个数字不能说明问题，从用户偏好入手，去看两个产品日活跃的用户分别偏好的视频种类。</p>
<p>有关用户视频偏好：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/Tf9e0l3uOJhrU7yWi85E.png" alt width="590" height="331" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/rpJjGUc6FSyte7ePYqyN.png" alt width="599" height="184" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/8LUoIYEFzrWKQTolthVI.png" alt width="604" height="389" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/A0iz5Tetr96BvBwX4l7n.png" alt width="623" height="510" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/QcJF5DA6V14EYYS4j5yh.png" alt width="623" height="130" referrerpolicy="no-referrer"></p>
<p>TikTok和Youtube用户每天访问的比例分别为67%和74%，20%的TikTok用户和21%的YouTube用户日均访问10+，几乎没差；不考虑内容和用户需求的差异，可以得到的结论是TikTok和YouTube的用户分别对于平台不同内容的不同需求的程度从数量上看大致相等。（设想/枚举场景下两个产品的日活用户观看内容和需求，重合的/不重合的）</p>
<p>从发布内容看，TikTok用户会比YouTube用户更愿意发布内容（62%，49%），超过1/4的TikTok日活跃用户每天至少在TikTok上发布一次照片或评论（27%）。YouTube日活跃用户中只有1/5这样做（20%）。</p>
<p>除去统计方法，数据上看TikTok短视频的挑战和拍摄的简单/社交属性更能有效促进用户的自主创作。</p>
<p>表格中没表现出来的数据有千禧一代（18-34）在 YouTube上观看电影和电视节目的偏好更明显，占比分别是35岁及以上年龄段人群的2倍和3倍。</p>
<p>TikTok用户没有在应用里看电影和电视节目的习惯，这和两个产品的视频长度/性质/定位所养成的用户习惯有很大关系，YouTube的PGC内容主要是由和电视台合作产生。</p>
<p>在YouTube上开通频道的电视台有：CBS、ABC、NBC、福克 斯电视台、CW电视台、ESPN、CNN等超过40家，集合全面的电视和电影频道也很大程度解释了大多用户选择YouTube观看电影电视。</p>
<p>而TikTok由于其短视频的定位（没有YouTube合作的优势）和强娱乐的属性，严肃内容以及电视电影等传统长视频不会出现在TikTok用户的搜索/推荐框里/其本身资源也缺乏。</p>
<p>再看视频种类偏好，运动，游戏，音乐类视频占比都很大；TikTok增长最快类别里面依然有音乐类。</p>
<p>其中值得注意的是TikTok增长最快里面的新闻和摄影类；以短视频的形式，TikTok的‘刷’和推荐机制对于新闻/咨询类的内容是由优势的，摄影类视频在TikTok手机全屏的观看模式下也有比YouTube更好的体验。</p>
<h3>4. 细分分析：（以下信息来源TheShelf，YouGov，Statista/偏好内容基于YouTube的数据）</h3>
<p><strong>（1）婴儿潮一代（57-75）/用户数TikTok十倍</strong></p>
<p>特点：</p>
<ul>
<li>消费能力强（51%的YouTube用户在平台消费）</li>
<li>退休，居家时间多</li>
<li>对科技/潮流类内容了解欲望强，想要跟上潮流</li>
<li>对健康极其关注</li>
<li>使用手机时长更多（5h/day）</li>
</ul>
<p>使用（短）视频平台的目的/诉求：</p>
<ul>
<li>节省时间：比起说明书更愿意搜索观看视频教程；因为对科技/网络产品操作不熟练，更愿意通过社交平台一站式购物。</li>
<li>跟上时代：了解当前时代的科技/软件/商品，目的是和时代接轨</li>
<li>了解健康/养生类知识</li>
</ul>
<p>以上，79%该年龄段的YouTube使用者认为视频社交平台带给了他们Deeper Connection。观看视频内容的核心诉求是更好理解/跟上时代。</p>
<p>婴儿潮一代用户在YouTube上偏好的内容和TikTok做的好的内容很相似；短内容为主，其中娱乐类占比最大（68%：娱/音/新闻），然后依次是教程类，健康类和客观评测。</p>
<p>想要获得这一部分用户,TikTok的优势在操作简捷，娱乐/新闻类短内容突出；而要得到这部分用户，TikTok首先要让他们接触到的内容应该是更正式，清晰/更有信息量的。</p>
<p>比如很多信息流视频中使用的Slang是这部分用户群体不愿意看到的，而很多娱乐/潮流类内容是避不开非正规语言的；算法对这部分人最开始推送的内容要识别和避免，更多推荐咨询/客观类内容；靠谱/客观/效率是这部分用户最初衡量的标准；整体内容上增加教程/实用类内容的数量和推荐权重，让用户对TikTok内容的心智产生迭代（how-to类视频YouTube用户期待占比55%，TikTok27.6%）。</p>
<p>宣传更多实用邮箱/短信/Fcaebook；尝试电视/电脑端应用。</p>
<p>设计上，面对这部分用户默认加大字体和默认的字幕，拥有婴儿潮用户最多的Fcaebook的数据表明平台上85%的视频是静音播放的。</p>
<p><strong>（2）41-56</strong></p>
<p>特点：</p>
<ul>
<li>消费能力强</li>
<li>成长时期社会发展巨大，适应新事物更快</li>
<li>有电脑和电视的使用习惯</li>
<li>倾向于跨平台的分享，尤其Facebook</li>
<li>关心时事/怀旧</li>
<li>女性有‘刷剧’的习惯，不分长短内容</li>
</ul>
<p>偏好内容/策略：</p>
<p>没有明显视频长短的偏好，从视频内容看，多数（75%）用户都会看怀旧类（Nostalgic）内容，然后依次是DIY和新闻时事类。</p>
<p>家庭和工作占据了这个年龄段人群的大多数时间，怀念学生时代，70，80年代的生活方式是他们的爽点和痛点，也是对他们最有吸引力的内容。</p>
<p>在电脑和CTV观看视频内容的习惯可能导致他们选择YouTube而不是TikTok；TikTok面对这部分用户的优势在于制造话题/趋势的能力和一键跨平台分享的功能，分享到Facebook，Twitter的内容会带来不错的宣传效果。</p>
<p>内容上，TikTok的标签挑战是发起怀旧浪潮很不错的途径之一，运营发起像#livebackto70/80s,#highschoolin70/80这类怀旧标签挑战，加上跨平台分享带来的效果可能会很好。</p>
<p>针对女性，短剧/连续内容是一个突出的独有偏好，针对她们增加剧情和连续内容的权重。</p>
<p><strong>（3）27-40</strong></p>
<p>特点：</p>
<ul>
<li>事业上升期，忙，压力大，没时间</li>
<li>网络电视偏好大于传统电视；短内容优于长内容</li>
<li>62%的人看完广告后做出行动/29%的人会看完YouTube的广告内容</li>
<li>有网上购物/社交平台购物的习惯</li>
</ul>
<p>偏好内容/策略：</p>
<p>短内容偏好占比54%/新闻类别中喜欢看人物故事/拆箱视频/quick&fun的娱乐内容。</p>
<p>以上，这部分用户最突出的特点就是忙和压力大。</p>
<p>他们使用视频/社交平台的诉求更多是缓解压力（拆箱，解压类视频）和寻求放松（搞笑类短视频）；从用户占比超YouTube 10%的结果也能看出这和TikTok的优势内容吻合。</p>
<p>短内容满足了刺激感，推荐算法满足了短期内爽感的循环；短期看，同样能满足这些诉求的社交/解压类游戏是个可行的方向；直播电商/购物平台也会有不错的受众。</p>
<p><strong>（4）15-25</strong></p>
<p>特点：</p>
<ul>
<li>多样性/新事物接受度高</li>
<li>KOL影响力大</li>
<li>使用最多社交平台的群体（数量/时间）</li>
<li>社交软件使用占比高过视频平台</li>
</ul>
<p>偏好内容/策略：</p>
<p>两个点，价值认同和娱乐是这个年龄段用户使用内容社交软件的诉求。对事物接受度高和什么社交软件都用是最突出的特点。</p>
<p>偏好短视频，内容接受度高，也是TikTok占比最大的用户群体。对TikTok，KOL至关重要，没有明显的平台偏好和习惯，KOL到哪他们就跟到哪。引入/签约合适的KOL会有效带来增长。</p>
<p>总的来说，在内容上TikTok要避免和要做的：</p>
<ul>
<li>针对不同年龄段的差异化推荐，发挥算法优势；</li>
<li>增加专业和实用类内容的数量，质量（逐渐增加平均内容时长）以及推荐权重；（18%的用户认为TikTok内容没有意义/浪费时间/成瘾）</li>
<li>改进审核过程，避免：错误信息（56%）；浮夸/轻浮的内容（32%）；不雅动作/语言（30%）；过激言论（11%）（biggest frustration about social media内容统计）</li>
<li>电视/电脑端应用的尝试</li>
</ul>
<h3>5. YouTube社区功能</h3>
<p>YouTube博主粉丝数达到1000即可开通社区功能；总的来说是在主页里增加了一个创作者和订阅者/普通用户的日常交流平台，提高互动甚至转化。</p>
<p>对视频创作周期长的的博主，社区功能无疑简化/增加了互动方式。</p>
<p>社区功能可以发布几乎任何形式的内容，让博主和粉丝不再仅是创作和观看视频的关系：视频内容会引发社区标签下的日常讨论和互动。</p>
<p>让博主和粉丝不再仅是创作和观看视频的关系：视频内容会引发社区标签下的日常讨论和互动；博主通过问答和日常分享提高互动和粉丝粘度。</p>
<p>民意调查和讨论让博主更好地了解需求/得到灵感，粉丝获得参与感，更愿意看视频。</p>
<p>社区的这些功能每个都对应了不同的目的和效果；除了视频评论区，Youtube在有意的让博主通过这几种方式实现不同的目的；创作者和用户都获得了更好的体验。</p>
<h3>6. TikTok能做的</h3>
<p>由于YouTube和TikTok内容呈现方式差别的原因，TikTok不适合像YouTube一样单独推出一个社区板块；所有YouTube社区板块下的功能都可以通过TikTok信息流内容呈现形式的差异化和评论区功能实现；像民意调查和投票。</p>
<p>类似的，国内抖音的很多博主会在视频里发起征集，赞高或者评论次数多的评论内容会得到回复和采用，结果是评论和点开评论区的人都多了，博主能通过数据分析工具了解评论关键词和有热度的内容，但看评论的用户很多时候其实没法提取这些信息，参与感不好是一个，还有是不知道博主看没看到。</p>
<p>YouTube的日常，图文，gif，宣传产品和预告在抖音里都可以通过内容形式差异化的方法来达到。</p>
<p>除了像有意的实现这些功能，目的是让创作者主动使用，用户在不离开主页视频和评论区的情况下能清楚看到并且参与：不影响原来的观看体验；内容上，延续之前说的：TikTok上很多火爆，多且杂的娱乐短内容是不容易让用户联想到博主本身的。</p>
<p>换句话说，对TikTok粘性不强/没有观看目标的用户来说，创作者不重要，内容重要；尤其不到45秒的短内容，同样一个搞笑/音乐/搬运/etc. 视频，换个人拍对一些用户来说区别不大。</p>
<p>一个是通过算法和调整权重改变信息流内容，同一个大分类下对不同群体推荐更有价值感的内容；一个就是参考YouTube的社区功能，把短时间内难以提取且有助于增加互动/建立社区的功能提取出来，目的是让人看到而后有可能参与，在功能的辅助下加强的是互动和参与感。</p>
<p>最开始增强的是人和内容的连接，然后是看者和博主的连接，再到三者之间的讨论和对话；最终可能形成的是社区雏形。</p>
<p>以下， TikTok可能可以借鉴的：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/xS237QBZDFOg6qlo314r.png" alt width="559" height="446" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/09/gWUTdO12cEy5xVJiZBsN.png" alt width="572" height="251" referrerpolicy="no-referrer"></p>
<div class="article--copyright"><p>本文由 @hhhsy 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<p>该文观点仅代表作者本人，人人都是产品经理平台仅提供信息存储空间服务。</p>
</div><div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5616465" data-author="1462821" data-avatar="https://static.woshipm.com/woshipm_def_head_2022_4.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            