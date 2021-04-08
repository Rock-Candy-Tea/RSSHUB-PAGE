
---
title: '精华篇：APP闪屏的设计门道'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/R6RsoFHi28eTvb1l1S2l.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 08 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/R6RsoFHi28eTvb1l1S2l.jpg'
---

<div>   
<blockquote><p>导语：本期内容可能会让很多UI设计师大开眼界，因为每个知识点都是UI设计中的精华技能，非常有可能助你突破自身的设计边界。文中会围绕APP闪屏设计知识分享，从闪屏的作用，到设计助力闪屏功能，再到一个闪屏尺寸适配所有主流分辨率手机，以及UI设计如何结合广告学知识巧妙的设计，在这篇文章中都会详细的告诉你答案。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4447147" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/R6RsoFHi28eTvb1l1S2l.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、启动页与闪屏的区别</h2>
<p>首先我们要知道APP的启动页和闪屏不是一个东西，启动页是用户打开产品第一眼看到的页面，闪屏是启动页之后出现的页面。</p>
<h3>1. 启动页</h3>
<p>启动页是一个APP必不可少的页面，在iOS规范中，上架AppStore必须有启动页，Android系统会有1-2s的白屏，所以两个端都需要启动页。苹果官方给的解释是，为了增加APP启动时的用户体验，确实如此，当打开一个产品时，首页内容都需要一定的时间加载。</p>
<p>启动页的设计角度一般是品牌信息传递，建立用户与产品的认知，一般时常都在2s以内（看网速和手机性能）。启动页的设计一般不做动画效果，因为只要是动画，就会让用户感觉等待时间变长了。</p>
<h3>2. 闪屏</h3>
<p>闪屏是启动页后面紧接着出现的页面，当然有很多产品没有闪屏，如微信、淘宝等，因为产品的定位和运营模式不同。闪屏与启动页不同，闪屏是用来运营的，比如投放日常广告、活动运营、节日等等，大多数产品闪屏出现的时间是3s或5s，一般都提供“跳过”按钮。</p>
<p>闪屏的设计为了运营，所以可以适当有动画效果或者视频，目的是能够更加吸引用户，加深印象或是提高点击率。</p>
<h3>3. 为什么启动页不能用来运营？</h3>
<p>启动页是写在安装包里面的程序，如果更换就得发版，闪屏的程序设计是从后台配置完成，所以可以满足日常更换。</p>
<h2 id="toc-2">二、如何减少用户等待感知</h2>
<p>对用户来讲启动页和闪屏展示的时间越短越好，那时间减少不了，就可以通过设计让用户对时间的感知变少，从而提高体验。看下图，两张图通过平滑过度，给用户的感觉是一张图在变化，这样时间上给用户的感知是变快的。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/D4vV8gZm90LNnsDTzZbJ.png" alt="【精华篇】APP闪屏的设计门道" width="401" height="438" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">用户等待感知短</p>
<p>当然对于不同的产品，设计的倾向性是不一样的，比如网易云音乐，启动页是强烈的红色，然后生硬的切换到一个跟启动页没有任何视觉关联的闪屏。这样的设计形式，用户等完一个页面，又等一个页面，那就会给用户在时间上的感知是变长的。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/OKhCtZBcEV28FhdgYQ2J.png" alt="【精华篇】APP闪屏的设计门道" width="401" height="437" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">品牌感知传递强</p>
<p>但是，对于一个音乐产品，渲染产品调性传递品牌，要远远大于减少用户等待时间的体验。所以，从这点来看，网易云音乐这样的设计形式，也是非常恰当的，设计应该根据产品的定位，来确定设计的倾向性。</p>
<p>敲黑板，划重点！ 下面的内容才是本文重点！</p>
<h2 id="toc-3">三、定义闪屏设计尺寸</h2>
<p>手机尺寸那么多，闪屏设计尺寸应该如何定义，很多APP的解决方案是使用两张不同比例的闪屏，还有一部分APP是区分系统，iOS适配一张图，Android适配一张图。</p>
<p>下面我以小米商城闪屏的改版为例，分享如何用一张闪屏尺寸适配所有机型，并详细介绍适配的原理。下图是改版前的闪屏，需要上传两张图，一张1080*2070（不带底部logo），另一张是720*1280（带底部logo）。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/nhvR5cLuy0WJkUIRzMna.png" alt="【精华篇】APP闪屏的设计门道" width="394" height="449" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">老版本闪屏需要上传两个尺寸图</p>
<p>两张图，设计人员就需在两个模版上进行排版设计，小米商城闪屏更换频率非常高，这样其实会付出很多时间成本。所以，我们团队尝试使用一张图适配所有机型，这其中的难点就是，找到一个合适的尺寸适配所有手机，并且闪屏内容的呈现在任意手机上都得合适，内容不能被裁剪。</p>
<p>先跟大家普及一下小米公司APP的设计稿尺寸，因为小米手机是Android系统，所以UI设计稿会优先适配安卓的主流手机，即1080*2340，这个尺寸接近iPhone12的比例和尺寸，切图相当于3倍图。</p>
<p>所以，闪屏宽度设定一定是1080px，然后高度分为两部分组成，一个是内容运营区（闪屏内容设计区域），一个是logo位，如下图所示。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/CMy2Zo8ycdtdZInoyCmj.png" alt="【精华篇】APP闪屏的设计门道" width="300" height="365" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">蓝色部分为闪屏</p>
<p>logo位部分由开发写到程序中，所以闪屏页面高度要去掉logo位高度。闪屏设计尺寸即是蓝色部分，正常来看应该是主流长屏分辨率手机与现存短屏分辨率手机的平均数即可，但其实并不可取。</p>
<p>因为，短屏分辨率手机毕竟使用人群是少数，设计的宗旨一向都是优先考虑大多数用户。所以，定义闪屏尺寸的原则是让类似小米11、iPhone12等主流比例手机呈现的完美，短屏分辨率手机如iPhone8只要呈现的不出错即可。</p>
<p>以安卓主流分辨率1080*2340为例（这个比例接近iPhone12），如下图，logo位高度设定为270px，把这个图切给开发，让开发等比缩放去适配所有手机即可。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/IUHleL2tlAR7pehDTIIb.png" alt="【精华篇】APP闪屏的设计门道" width="300" height="407" referrerpolicy="no-referrer"></p>
<p>很多安卓手机底部会有一个系统高度，这个位置不可以占用，但开发可以改变颜色，所以这部分颜色可以跟启动页或闪屏颜色调成一致。页面分辨率2340减去270的logo位就是2070，这就是长屏主流手机闪屏大概要呈现的高度，然后需要用这个尺寸去兼顾短屏分辨率手机。</p>
<p>把短屏手机也计算出来，安卓最短的手机比例是16:9（比例等同于iOS的iPhone8），以1080*1920为例，如下图，1920同样是减去logo位的270像素等于1650。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/6xRDA2DK8XRB2CmJZXsl.png" alt="【精华篇】APP闪屏的设计门道" width="404" height="444" referrerpolicy="no-referrer"></p>
<p>接下来就是最关键的时刻，要用1080*2070和1080*1650两个尺寸设定闪屏的设计模版。先说一下手机的适配原理，如果一个张图片的比例和手机屏幕不一致，开发设定是撑满手机屏幕，这时手机上展示的图片就会出现上下或左右被裁剪的情况。</p>
<p>所以，综合两个不同比例的尺寸，短屏手机裁剪上下，长屏手机裁剪左右，然后把呈现的内容保证在不被裁剪掉的区域。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/xFwVX7mlXiI877vqIkJS.png" alt="【精华篇】APP闪屏的设计门道" width="403" height="490" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">闪屏模版尺寸设定尝试</p>
<p>最后经过很多次的尝试，最终选用1080*1920作为闪屏的设计尺寸，向上向下适配内容的呈现都非常合适。下图是iOS和安卓手机的适配效果，向下适配16:9的手机（裁剪上下），向上适配20:9的手机（裁剪左右）。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ob4xO7wEOHypchSnwU9s.png" alt="【精华篇】APP闪屏的设计门道" width="606" height="351" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">长短屏手机闪屏适配效果</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/QmHgptiNAWS6jE0rfUsw.png" alt="【精华篇】APP闪屏的设计门道" width="407" height="374" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">定制闪屏设计模版</p>
<p>模版中页面上方留了较大面积，是为了让标题内容能够呈现在长屏手机更恰当的位置上，长屏手机内容靠上，看上去不会很舒适。底部空间留的较少，因为底部再加上logo位的高度，就会让页面看起来很协调。</p>
<p>最终小米商城的闪屏就是用一个尺寸适配了所有分辨率的手机，思路和适配原理都已经讲清楚，如果自家的产品是优先满足iOS手机，完全可以用上面介绍的方法尝试。</p>
<p>敲黑板！ 下面内容可能会颠覆你对UI设计的认知！</p>
<h2 id="toc-4">四、“跳过”按钮位置设计</h2>
<p>闪屏尺寸说完了，闪屏上面还有一个“跳过”按钮，这个按钮的位置设计非常非常重要，而且大有学问，会牵扯到广告学，按钮合理的设计会让一个产品的收入倍增。</p>
<p>还是以小米商城的闪屏为例，之前的闪屏“跳过”按钮在页面右下角，新版我把“跳过”按钮放到了右上角，为什么？</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/880oC6Bf9zSWRdAG331Z.png" alt="【精华篇】APP闪屏的设计门道" width="402" height="439" referrerpolicy="no-referrer"></p>
<p>可以肯定的是，“跳过”按钮，放在右上角，用户体验是不够好的，右下角用户操作起来才会更便捷，改为右上角其实就是为了让用户少点击。用户不去点击“跳过”按钮，那闪屏内容曝光的时间就会更长，这符合小米商城自营平台的定位，自营平台闪屏展示都是自己平台的内容。</p>
<p>有很多产品闪屏的“跳过”按钮，放在右下角，如微博、网易云音乐，优先满足用户体验，是因为广告的性质不同。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/IzGXZn5hwROXIVoWAzoV.png" alt="【精华篇】APP闪屏的设计门道" width="398" height="434" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“跳过”按钮在右下角的产品</p>
<p>在广告学中有这样几个词：CPS、CPC、CPM、CPT。</p>
<ul>
<li>CPS：Cost Per Sales是一种广告的推广方式，是通过实际的销售量进行收费，比如每卖一单收取多少钱，转化越多，收入越多。</li>
<li>CPC：Cost Per Click这种推广方式是，按照点击量来进行收费，点击一次，收一次费。</li>
<li>CPM：Cost Per Mille此种推广方式是按曝光量进行计算收费，只要用户看见这个广告，就会计费一次。</li>
<li>CPT：Cost Per Time这种推广方式是，通过时间进行收费，比如包一个月包一个季度等。</li>
</ul>
<p>了解完常见的几种广告推广方式后，我们再看一下微博和网易云音乐两款产品。他们的广告如果是CPM（曝光量）和CPT（包时间）的推广方式，那“跳过”按钮放到右下角可以提升用户体验，还不会影响推广的收入。</p>
<p>再来看一下脉脉和花瓣两个产品，他们的推广方式大概率是按CPC（点击率）或CPS（转化率）收费的。闪屏的“跳过”按钮放在右上角，内容的设计形式上强调并引导用户去点击广告。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【精华篇】APP闪屏的设计门道" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/psYjMrcoBOKtpsS4h5hQ.png" alt="【精华篇】APP闪屏的设计门道" width="400" height="437" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“跳过”按钮在右上角的产品</p>
<p>聊一下脉脉和花瓣的闪屏设计，脉脉把闪屏设计成弹窗的形式，用一种骗的形式，引导用户点击假弹窗的“知道了”或关闭图标。用户的点击行为与心里目标完全不一样，这样的设计虽然能让平台获得更多的广告收入，但也损害了用户对平台的好感。</p>
<p>花瓣闪屏的设计较为友好，实实在在的告诉用户这是广告，你有兴趣就点“去看看”去了解，没兴趣就等一等，或点击“跳过”。花瓣这种设计形式较为适合CPS（转化率）的推广放过，因为点击了解的用户，都是对广告兴趣的精准人群。</p>
<h2 id="toc-5">五、后语</h2>
<p>最后总结一下文章的内容，启动页和闪屏是两个东西，通过设计可以让用户等待的时间感知更快，从而提高体验。闪屏可以用一张图适配所有大中小手机，闪屏的“跳过”按钮大有学问，合适的设计可以让平台的收入倍增。</p>
<p>设计从来都是用来满足商业目的的，一个小小的按钮设计，都会很大影响到平台的收入，所以UI设计任何时候都需要清楚的了解产品定位以及商业模式，这样才能有效的产出设计。</p>
<p>身为设计师，为了满足商业目的可以做讨巧的设计，但要拒绝无底线无原则的设计，做一个有品，有良心的设计师很重要。</p>
<h3>#专栏作家#</h3>
<p>吴星辰，微信公众号：互联网设计帮，人人都是产品经理专栏作家。</p>
<p>本文原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4447057" data-author="882855" data-avatar="https://static.woshipm.com/WX_U_201905_20190514184830_8086.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            