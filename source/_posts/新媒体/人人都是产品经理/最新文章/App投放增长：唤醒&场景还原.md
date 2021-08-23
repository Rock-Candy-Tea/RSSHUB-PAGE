
---
title: 'App投放增长：唤醒&场景还原'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/bPSV3EXeIQiBHQAzITur.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 23 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/bPSV3EXeIQiBHQAzITur.jpg'
---

<div>   
<blockquote><p>编辑导读：在App投放推广中，唤醒用户是常见的运营策略。想要让用户重新活跃起来，转化用户的行为，必须从场景上还原用户的路径，从根本上找到用户增长的奥秘。本文从“唤醒&场景还原”角度展开App投放增长的方法，一起来看看。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5100739 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/bPSV3EXeIQiBHQAzITur.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在日常App投放推广中，拉新和拉活往往是增长的两大运营策略。众所周知，“所见即所得”的场景化营销能给用户带来较好的广告体验，进而提升转化。那么从产品层面该如何来保证用户引流到目标App时第一个页面就是其期望的广告创意内容呢？本期我们来讲一讲这其中涉及到的两种关键技术：唤醒和场景还原。</p>
<h2 id="toc-1">一、前言</h2>
<p>在这个广告漫天的时代，相信大多数用户在使用App的时候都遇到类似的场景：在使用某资讯类App的时候，浏览到了淘宝的商品广告，当你点击该广告内容时，自动打开了你手机上已经安装的淘宝App并且定位到了该商品的详情页。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="App投放增长：唤醒&场景还原" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/z9tY6FAmO28EXyAgsSpf.gif" alt="App投放增长：唤醒&场景还原" width="223" height="394" referrerpolicy="no-referrer"></p>
<p>作为用户，心里一定在想：“这购物真方便，都不要自己打开淘宝搜索商品了”。</p>
<p>作为广告主，心里在想：“又拉活了一个用户，说不定还能带来一笔转化”。</p>
<p>用户&广告主其乐融融，开开心心完成了ROI。</p>
<p>那么，资讯类App是如何唤醒淘宝App的呢，淘宝App又是如何跳转至用户浏览的广告页面呢？</p>
<p>接下来的篇幅将为您讲解这其中的黑科技：唤醒和场景还原。</p>
<p><strong>唤醒&场景还原，作为运营常用的拉活增长手段，有利于提升老用户在App的活跃度，场景化的唤醒更能激发用户的转化意愿。</strong></p>
<p>其适用于如下几个营销场景：</p>
<p><strong>1）微信、QQ等社交软件–>目标App</strong></p>
<p>现在App为了做裂变都会带有分享功能，用户A分享了App内容链接至微信或QQ，用户B点开该链接后，会引导用户B打开该App或者下载该APP，从而对用户B实现拉新或者拉活。</p>
<p><strong>2）短信、邮件、push等 –>目标App</strong></p>
<p>短信、邮件、push也是常规的运营营销手段，用户A打开了某App的推广短信、邮件、push等，会引导用户打开该App或者下载该App。</p>
<p><strong>3）宿主App–>目标App</strong></p>
<p>用户A在宿主App上浏览并点击了目标App的推广活动，宿主App会引导用户打开该App或者下载该App。简而言之，任何需要将用户吸引到目标App的活动都会用到唤醒和场景还原。</p>
<h2 id="toc-2">二、DeepLink</h2>
<p>说到唤醒&场景还原，不得不说到DeepLink技术，因此他是实现唤醒和场景功能的基础。</p>
<p>Deeplink分为Deeplink和Deferred Deeplink，行业内常说的“Deeplink”往往是这两者的统称。</p>
<p><strong>Deeplink：</strong>深度链接，指已安装目标App的情况下，宿主App把特定的参数通过url 的形式传递给目标App，从而直接在目标App内打开指定的内部页面，实现从链接直达App 内部页面的跳转。</p>
<p><strong>Deferred Deeplink：</strong>延迟深度链接，区别于普通的Deeplink，主要是增加了一个是否已安装目标App的判断，用户点击链接时，如果未安装 App，则引导用户前往应用市场，下载完对应 App后，首次打开该 App 时自动跳转进入指定的内部页面。</p>
<h2 id="toc-3">三、唤醒方式</h2>
<p>目前常用的App唤醒方式包含如下几种：Url Scheme、Universal Link、App Link。</p>
<h3>1. UrlScheme</h3>
<p>在用户在点击scheme链接后，如果已安装则通过参数调用目标App并打开指定页面，如果未安装App，点击链接后无反应。</p>
<p>通过Url Scheme方式，需要App端能够接收参数，传递给 App。</p>
<p>由于Scheme在未安装App时点击链接无反应的问题，所以在在投放时，一般都会选择双链。</p>
<p>即Scheme+H5，在唤醒失败的时候可以打开H5页面。</p>
<p>通过Scheme唤醒App时，一般都会先判断用户是否已安装目标App。</p>
<p>针对是否已安装App的判断，Android可通过App包名判断，IOS只能判断40个App(系统级别，变更列表需要发版)。</p>
<p>所以这也是为什么广告平台提供的已安装App用户定向支持Android的原因，其可以通过下发包名list在App端进行探测。</p>
<p>在进行已安装App判断时，如果是可以明确判断已安装，直接使用Scheme进行唤醒。</p>
<p>如果无法判断当前设备是否已安装目标App，优先使用scheme进行唤醒并设置倒计时，监听倒计时结束之前是否已唤醒目标App。</p>
<p>常用的监听方法是判断当前页面是否可见。</p>
<h3>2. Universal Link</h3>
<p>Universal link是苹果推出的通用链接技术，如果目标App 支持Universal link，就可以通过访问http/https链接打开目标App内指定页面。</p>
<p>如果没有安装App，可以跳转到自定义网页，很好的解决了Scheme在未安装App无反应的缺陷，但仅限在IOS（9.0以上版本）上使用，在Android上会打开对应的H5页面。例如：https://dp.ctrip.com。</p>
<p>由于Universal Link仅在IOS上才可以唤醒App，因此在投放时，如果需要使用Universal Link，那么需要做系统定向，仅定向IOS用户。</p>
<h3>3. App Link</h3>
<p>App link是Android（6.0以上版本）推出的链接技术，功能类似于IOS的Universal link。</p>
<p>如果使用App link进行投放，同样需要选择系统定向。</p>
<h2 id="toc-4">四、场景还原</h2>
<p><strong>场景还原，主要解决在用户未安装目标App时如何在下载安装激活之后打开App内指定页面的问题。</strong></p>
<p>相比于传统的唤醒，其难点主要在于新下载激活的App如何获取在宿主App点击时候的链接内容。目前常规的信息传递方式主要是监测链接和剪贴板方案。</p>
<h3>1. 监测链接</h3>
<p><strong>当用户点击唤醒按钮时，通过监测链接回传用户的设备号信息和点击内容。</strong></p>
<p>在用户下载安装激活后，通过设备号匹配其在宿主App内的点击内容，即可知晓此时需要引导用户至哪个对应页面。</p>
<p>目前主流的广告平台在上报监测数据时，都支持替换监测链接中的落地页宏。</p>
<p>除了落地页宏，也可以通过其他宏获取映射关系，比如说广告ID/创意ID等，这就需要维护宏参数和落地页的关系。</p>
<p>该方案依赖于广告平台侧需要支持对应的宏替换，其触发时机是用户看到或者点击广告创意（最外层）。</p>
<p>如果投放的内容是聚合页，用户在聚合页内的操作，平台侧是无法提供的，只能依靠广告主的技术去实现还原。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="App投放增长：唤醒&场景还原" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nkqtC7Q3pMq51uqHv8nn.png" alt="App投放增长：唤醒&场景还原" width="393" height="216" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="App投放增长：唤醒&场景还原" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/00xh1DldOuyJbbN3ndLp.png" alt="App投放增长：唤醒&场景还原" width="385" height="211" referrerpolicy="no-referrer"></p>
<h3>2. 剪贴板</h3>
<p>在说到通过监测链接进行场景还原时，对于投放的内容是聚合页场景，无法很好地完成场景还原，那么广告主可以通过剪贴板的功能来实现聚合页中的内容场景还原。</p>
<p>当用户在在聚合页发生交互行为时，由于聚合页是广告主自己搭建的页面，可嵌入自家采集数据的JS-SDK，该SDK的主要作用是采集用户在当前页面的交互行为，然后进行数据上报。</p>
<p>这样当用户下载激活时，就可以通过该数据进行场景还原，打开对应的页面。</p>
<h3>最佳实践</h3>
<p>为了达到最优的场景还原，一般都是监测链接+剪贴板的方案搭配使用，优先使用剪贴板记录的数据（因为其更接近用户在宿主App中最后的操作行为记录）。</p>
<h2 id="toc-5">五、总结</h2>
<p>其实场景还原的技术方案与《App投放增长：归因模型及框架介绍》中讲的归因方案有异曲同工之处，读者可以相互借鉴。</p>
<p><strong>其核心都是在于获取记录转化发生前的用户行为，场景还原的转化是用户首次打开App，使用的归因模型是Last Model逻辑。</strong></p>
<p> </p>
<p>作者：包子，公众号：商业化产品日常日记</p>
<p>文由 @包子 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5096909" data-author="653349" data-avatar="https://static.woshipm.com/APP_U_201803_20180319085922_2048.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            