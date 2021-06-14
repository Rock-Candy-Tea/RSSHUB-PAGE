
---
title: '移动App如何设计广告位？从这4个角度出发'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/01/6T32j5hotsa0qpcUwzUl.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 16 Jan 2020 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/01/6T32j5hotsa0qpcUwzUl.jpg'
---

<div>   
<blockquote><p>文章主要围绕移动App上广告位如何设计进行了分析探讨，作者从4个角度对这个问题进行了解答，与大家分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-3328459 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/01/6T32j5hotsa0qpcUwzUl.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>记得当年面试商业产品经理时，面试官拿着手机问我，你会选择在手机系统里哪个位置设计广告位做变现？</p>
<p>我当时完全是个商业化小白，对这个问题没有什么概念，就指着主页的天气、日历说这些位置都可以啊。现在想想真是蒙昧无知。</p>
<p>本文主要和你聊聊，移动App上广告位如何设计，以下是一些工作中个人积累的经验，我尽量用白话表述，有不对与不完善的地方，欢迎留言指正和补充。</p>
<p>首先明确下目的，设计广告位的目的是为了收益。跟收益有关的因素有广告显示位置，广告展示形式，广告出现频次，广告源。</p>
<h2 id="toc-1">一、广告显示位置</h2>
<h3>1. 寻找流量大的位置</h3>
<p>如下图，一个广告位置设计在App启动时-开屏位置，一个广告位位置设计在App首页信息流-内容页位置。这两个相比当然是App启动时的广告位置请求人数最多，因为只要人们打开这个App，广告位置就可以请求广告。</p>
<p>理论上来说，你的App哪里流量大，哪里放广告位就越有价值，一个App里会在不同的流量界面可以设计很多广告位。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/01/6BxhWF3Hj8DBQtYFmjSc.jpg" width="602" height="510" referrerpolicy="no-referrer"></p>
<p>一个App流量最大的地方就是在启动时吗？统计机构AppOptix发布了安卓手机用户每天解锁次数为每天65.8次，用手机的第一步就是解锁，每天解锁这么次，这里流量巨大，要是能把广告位放在这里就好了！</p>
<p>如下图，有钱的地方，早已经有人行动了，这里也成了工具类App兵家必争之地。因为工具类软件用户使用频次低，为了想办法增加广告收益，利用各种手段保活，监听系统广播，占领了用户手机的锁屏位置，在锁屏上为用户提供资讯，其中嵌入信息流广告，来增加收益。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/01/8buLvwL7cAzS6VjgSqeM.jpg" width="606" height="500" referrerpolicy="no-referrer"></p>
<p>上面那些锁屏广告用户体验不太好，一些有品牌App，考虑到用户体验和口碑，不会直接在锁屏上放置广告，他们利用锁屏位置为自己的功能模块导流，如下图，锁屏画布底部有视频、音乐、小说等快捷方式入口，可以为自己的产品导流。</p>
<p>锁屏阅读上将资讯以卡片的形式展示，用户可以左右滑动，对于自己喜欢的可以点击进入，在内容页面上可以设计相应的广告位。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/01/XEvo4PSqvUMEq6Hao3ep.jpg" width="602" height="495" referrerpolicy="no-referrer"></p>
<p>在设计广告位时，先梳理App内各个功能模块的流量，找到流量大的地方。</p>
<p>若你的App用户使用频次较低，你需要创造高频次场景，可以考虑将功能外延至系统内流量大的地方，如锁屏位置、通知栏常驻、桌面悬浮挂件等，当然这需要向用户申请授权。</p>
<h3>2. 注意不要让用户误触</h3>
<p>现在智能机手机都是通过手指按下和滑动来完成操作，很容易出现误碰的现象，这个被称作“胖手指”，由误碰带来的广告点击不在少数。</p>
<p>如下图，广告区域是推荐阅读，推荐阅读下方是悬浮的底部菜单。当用户上滑操作或点击菜单栏上互动元素时，很容易发生误触。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/01/jgYgkvBuelBaZleKZ76r.jpg" width="599" height="426" referrerpolicy="no-referrer"></p>
<p>误触的危害：</p>
<ol>
<li>伤害用户体验，造成用户的反感，导致用户流失，敏感的用户可能会直接卸载你的App；</li>
<li>伤害广告主的利益，误点击的广告转化率很差，广告主的效果无法得到保障，可能会影响到媒体方广告单价；</li>
<li>目前很多广告平台都会过滤误触的行为，误触带来的点击是不计费的，误触可能会影响媒体的评分，评分会影响到媒体方广告的收益。</li>
</ol>
<p>如何应对：</p>
<ol>
<li>媒体方在自己设计广告位时，不要将广告放在互动元素旁边；</li>
<li>广告平台通过“边缘检测”过滤误点击；</li>
<li>根据网上资料显示谷歌百度某些广告位场景，对于在广告边缘的点击，会提示用户进行二次确认，确保是用户的主动点击行为。</li>
</ol>
<h2 id="toc-2">二、广告展现形式设计</h2>
<h3>1. 尽可能设置成常见的广告位类型。</h3>
<p>如下图，常见的广告位类型有开屏广告、banner广告、插屏广告、信息流广告、原生广告、视频广告、激励视频。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/01/rkTP6C3OWmTTSRVT954L.jpg" width="792" height="480" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/01/XS4TqE66Eo8Uri2Tso9L.jpg" width="793" height="487" referrerpolicy="no-referrer"></p>
<p>各个类型的广告位要设置成常见的比例，方面接入各个广告平台，以保证足够的填充率，具体的比例在广点通、穿山甲创建广告位时会有显示。</p>
<p>一般而言，广告素材的尺寸越大，往往点击率越高，比如开屏点击率大于信息流大图，信息流大图点击率大于信息流小图。因为素材尺寸越大，就越显眼，素材也能更好传递内容，所以点击率会相对较高。</p>
<p>但是这也不是绝对，比如插屏类型素材尺寸虽大，但点击率不高，因为它蹦出来的形式，人们下意识的认为就是广告，会不加思索的关掉。</p>
<p>如今，信息流大图也有个趋势，过去因为点击率高，广告都做成了大图形式，导致有一部分敏锐的用户，看到大图就想到广告，注意力就直接跳过了。流量背后的用户群体不同，实际的点击率还要以客观数据为准。</p>
<p>如下图红框处，作为流量方，为了增加点击率，还可以在广告位中设计可点击的元素，按钮的形式配上文案，更容易吸引用户点击。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/01/RdIIgF4Mxqpubnpxe49N.jpg" width="802" height="494" referrerpolicy="no-referrer"></p>
<p>如下图，头部的流量方，会设计一些别出心裁的样式，以吸引用户的注意力，提升点击率，如开屏广告和信息流广告联动，信息流翻转广告，朋友圈可互动的广告等。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/01/sujLF4cZEIHxVGhVBw11.gif" width="300" height="600" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、广告出现频次</h2>
<p>有些广告位上的广告出现是有频次的，太频繁的出现会影响用户体验。</p>
<p>比如，在开屏广告这里，你打开视频App等待5秒开屏广告结束后，进入了视频列表，这时收到一个微信消息，去微信中查看回复，然后再切换回刚才那个视频App，结果它又来5秒开屏广告，这时你肯定对这视频App产生了反感。</p>
<p>如果每次应用启动都有开屏广告，则会让人厌烦，所以一般会设定一个广告频次，包含广告出现的间隔和每天最大出现的次数。</p>
<p>合理的广告频次和间隔，需要兼顾收益与用户体验。具体数值设定多少，因产品而异，需要建立一个对照组，多个测试组，去分析评估广告频次与收益，广告频次与留存的影响度，最终确定合理的数值。</p>
<h2 id="toc-4">四、广告源</h2>
<p>对于中小媒体，可直接接入外部主流的广告平台，如广点通、穿山甲、百度等。对于媒体而言，到底该把流量分给哪家广告源呢？一般以ecpm来对比，ecpm是展示1000次广告预估的收益。那是不是就可以每次同时请求各家广告平台，看谁ecpm高，就把流量给谁呢。</p>
<p>理论上是这样的，但目前各家广告平台一般情况下不会实时返回价格，所以做不到实时比价，只能根据前一天的ecpm来比价，哪家ecpm高，先请求哪家，依次类推，这种方式叫瀑布流（waterfall）。</p>
<p>随着根据ecpm高低分配流量的需求，就诞生了广告聚合平台（mediation），他包含了主流的广告平台，可以在平台设定广告源的排序，自动同步ecpm等功能，聚合平台可以根据需要内部研发或者接入第三方。</p>
<p>对于中大型媒体，拥有自己的广告主，往往都有自家的广告平台，包含投放平台（DSP），交易平台，流量管理平台。一般是优先将流量分给自家广告主/自家DSP，然后是其他DSP。</p>
<p>这块内容简单提下，关于mediation，waterfall，Header Bidding（In-app bidding）属于广告变现的核心内容，后续将单独写个文章来讲。</p>
<p><strong>上面分别从广告显示位置，广告展现形式，广告出现频次，广告源的角度拆解了如何设计广告位。</strong></p>
<p>广告位一切的设计都是围绕着收益进行，下面从收益的角度进行拆解。</p>
<p style="text-align: center;">广告位的收益 = 广告位的曝光次数 * 广告点击率 * 广告点击单价。= 广告请求人数 * 广告人均请求次数 * 广告填充率 * 广告展示率 * 广告点击率 * 广告点击单价</p>
<ul>
<li>广告请求人数：与广告显示位置流量大小、广告位置用户留存率有关。</li>
<li>广告人均请求次数：与广告出现频次有关</li>
<li>广告填充率：与广告源有关</li>
<li>广告展示率：与广告位置与请求逻辑有关</li>
<li>广告点击率：与广告展现形式和广告素材有关</li>
<li>广告点击单价：与广告源、广告转化效果有关</li>
</ul>
<p><strong>上面这个公式只是短期来看收益最大化的公式，长期来说，要关注“广告请求人数”即产品的生命周期（LT），主要跟产品的留存有关。不能为了收益，加过多的广告位，不然会影响用户体验，要考虑一个长远的收益，不要被眼前的收益蒙蔽。</strong></p>
<p>本篇讲述了流量变现，广告位如何设计。下篇文章将讲下广告聚合平台（mediation），waterfall相关的内容。</p>
<p> </p>
<p>作者：夜星，商业产品经理，每周分享在线广告领域的思考，期待与你的交流，微信公众号：夜星独白</p>
<p>本文由 @夜星 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="3324903" data-author="142926" data-avatar="http://image.woshipm.com/wp-files/2019/12/LUQRmsL7VvFOlv2H5XDA.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            