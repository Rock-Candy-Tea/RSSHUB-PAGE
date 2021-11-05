
---
title: '讲座信息获取小程序的MVP前台+后台设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/l1tkFfGZMyIzLJiXm1hv.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 05 Nov 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/l1tkFfGZMyIzLJiXm1hv.jpg'
---

<div>   
<blockquote><p>编辑导语：对于很多高校学生来讲，经常困扰于这样一种情况，那就是不知道学校最近有哪些讲座，邀请哪些嘉宾前来讲学，因此时常会错失一些重要的讲座。本篇文章作者将分享讲座信息获取小程序的MVP前台+后台设计，有兴趣的小伙伴快来看看吧！</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5205773 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/l1tkFfGZMyIzLJiXm1hv.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>对于很多高校学生来说，如何快速获得身边的讲座信息一直一来都是一大需求痛点。本文以微信小程序为载体，设计讲座信息获取的最小可行性产品。</p>
<h2 id="toc-1">一、需求分析</h2>
<p>对于很多高校学生来讲，经常困扰于这样一种情况，那就是不知道学校最近有哪些讲座，邀请哪些嘉宾前来讲学，因此时常会错失一些重要的讲座。</p>
<p>这主要是因为两个方面的原因产生的，一是很多学校都有好几个校区，每个校区都有不同的学院，各个消息各个学院之间消息并不畅通。二是官网虽有更新讲座信息，但是并没有多少人经常刷新官网，因此错过也就在所难免。</p>
<p>以我自己举例，如果没有看到学校在微信群的通知的话，一些重要嘉宾的讲座基本都会错过。因为线下海报，官网宣传都很难注意到。</p>
<p>身边的很多朋友同样也是这样，自己学院的讲座都容易缺失，更不用说其它学院的了。</p>
<p>作为一个在产品路上努力奔跑的新人，很快就捕捉到了这个需求——及时了解全校范围内的讲座信息。下一步就是思考如何实现的问题。</p>
<p>先讲一下为什么要打造这个产品，如果单纯从商业化的角度来看，其实校园产品很难实现盈利，因为用户的粘性建立和长期留存实现起来困难，很多巨头进入这个领域最后都潦草收尾。</p>
<p>但还是想做这个产品，一是如果在最美好的学习时光，如果错过与很多大咖的交流，对很多人来说也是一种人生遗憾。二是产品目前就这一个模块，如果流量效应还可以的话，完全可以拓展其它模块，后面在演进蓝图里再提到。三是它的实现成本并不高，如果能够实现流量收益是完全可以cover住成本的，而且也是个不错的在校实践机会。</p>
<p><strong>需求已经确认，价值也已经明确。现在我们只是做一个mvp功能，暂时不考虑其它模块，但这个看上去很小的mvp，也有很多问题需要梳理：</strong></p>
<ul>
<li>讲座信息从哪里来</li>
<li>讲座信息收集不全面怎么办</li>
<li>如何对这些讲座信息进行分类</li>
<li>有哪些信息需要展示</li>
<li>如何确认信息真实性</li>
<li>多长时间刷新一次最新信息</li>
<li>用户可以订阅校区/学院讲座信息吗</li>
<li>用户知道了讲座信息但到开讲前遗忘了怎么办</li>
<li>支持用户分享信息吗</li>
<li>产品形态是什么，app,小程序，还是网站</li>
</ul>
<p><strong>经过一番思考与分析，综合考虑用户需求和产品开拓阶段战略，确定了如下问题解决方案：</strong></p>
<ul>
<li>讲座信息爬取自各个学院官网讲座信息板块</li>
<li>支持其它用户上传讲座信息</li>
<li>按照校区、学院对信息进行归类</li>
<li>支持其它实名认证用户反馈以确认信息的真实性</li>
<li>1天刷新一次最新信息</li>
<li>支持用户订阅校区/学院讲座信息</li>
<li>用户预约讲座，开讲前2小时推送提醒</li>
<li>支持用户分享信息至朋友圈及其它社交媒体平台</li>
<li>产品形态是小程序</li>
</ul>
<h2 id="toc-2">二、用户核心流程图</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/xEXRRAQ4W8rb9Uy9iyEB.png" alt width="681" height="516" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、主要功能</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/14kO30KvFh6pUNERR69E.png" alt width="849" height="184" referrerpolicy="no-referrer"></p>
<p><strong>主要功能分为六个部分：</strong></p>
<p><span style="font-size: 16px;">（1）用户点击查看讲座信息。</span></p>
<p>（2）已经实名认证过的用户可以点击反馈，以保证讲座信息的真实有效性。</p>
<p>（3）支持用户分享讲座信息到其它社交媒体平台。</p>
<p>（4）用户预约当前查看的讲座，并接收提醒。</p>
<p>（5）支持用户上传最新讲座信息。</p>
<p>（6）订阅校区/学院，近期有讲座更新及时推送。</p>
<h2 id="toc-4">四、信息结构</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/vsDP1EgGmCrIZk41zUTv.png" alt width="613" height="397" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、页面与交互</h2>
<p>由于是mvp设计，所以功能结构和信息内容并不繁琐，界面设计如下：</p>
<h3>1. 首页–全部讲座</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/9zExkxLGa03XE6XWA08d.png" alt width="640" height="341" referrerpolicy="no-referrer"></p>
<p><strong>（1） </strong><strong>页面逻辑内容</strong></p>
<ul>
<li>页面由顶部tab栏和对应的具体的内容构成；</li>
<li>上方tab栏为“全部讲座”和“我的订阅”；</li>
<li>“全部讲座”显示讲座缩略信息，从左往右，从上往下为课程海报、讲座主题、主讲人、讲座时间、讲座地点和已预约提醒人数，点击进入讲座详情页。</li>
</ul>
<p><strong>（2） </strong><strong>页面交互</strong></p>
<ul>
<li>点击tab切换对应内容，同时显示蓝色下划线，tab字体设置成蓝色；</li>
<li>向左滑动讲座信息模块，显示“提醒”和“反馈”两个标签，点击进入对应页面；</li>
<li>下拉页面刷新讲座信息。</li>
</ul>
<h3>2.  首页–我的订阅</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/nk1SsNyYOyPlpj7lW0kO.png" alt width="777" height="345" referrerpolicy="no-referrer"></p>
<p><strong>（1） </strong><strong>页面逻辑内容</strong></p>
<ul>
<li>页面由顶部tab栏和导航栏以及对应的具体的内容构成；</li>
<li>上方tab栏为“全部讲座”和“我的订阅”；导航栏显示用户订阅的校区/学院；导航栏右侧显示编辑按钮，用户点击可进入订阅编辑页面。</li>
<li>“全部讲座”显示讲座缩略信息，从左往右，从上往下为课程海报、讲座主题、主讲人、讲座时间、讲座地点和已预约提醒人数，点击进入讲座详情页。</li>
</ul>
<p><strong>（2） </strong><strong>页面交互</strong></p>
<ul>
<li>点击tab栏切换对应内容，同时显示蓝色下划线，tab字体设置成蓝色；点击导航栏，对应字体放大一号，设置成蓝色。</li>
<li>向左滑动讲座信息模块，显示“提醒”和“反馈”两个标签，点击进入对应页面；</li>
<li>下拉页面刷新讲座信息。</li>
</ul>
<p>这里想提一下，有朋友可能想问，“我的订阅”这里的内容其实完全可以在“全部讲座”这里用筛选的方式加以实现，为什么还要单独弄一个“我的订阅”呢？其实这样做的原因由三个方面：</p>
<p>第一是我的订阅需要登录权限，用户只有在登录状态下才能操作，这样就可以引导用户注册登录，沉淀用户。如果通过筛选，对于一个MVP产品来说，用户可能就是即用即走。</p>
<p>第二是订阅之后，一旦用户所订阅的类别有更新，用户可以接收推送，提高用户的小程序打开率，而让用户筛选则无法实现这一点。</p>
<p>最后，对于固定关注几个学院的讲座的用户来说，每次都要筛选未免有些麻烦，直接通过订阅，即可查看对应类别下的讲座信息，显然要方便的多。</p>
<p>所以综上选择了订阅的这种方式。</p>
<h3>3. 讲座详情页</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/9ZLsQDDQ5txKIvFmSBh0.png" alt width="663" height="380" referrerpolicy="no-referrer"></p>
<p><strong>（1） </strong><strong>页面逻辑内容</strong></p>
<ul>
<li>页面分为五个模块，分别为讲座基本信息模块、内容简介模块、时间模块、地点模块和底部的分享和与提醒模块；</li>
<li>基本信息模块显示讲座海报、讲座主题、主讲人和主讲人简介；</li>
<li>时间地点模块分别显示讲座的具体时间和地点；</li>
<li>底部为分享按钮和讲座提醒，用户点击可分享讲座至其它社交媒体平台和预约提醒。</li>
</ul>
<p><strong>（2） </strong><strong>页面交互</strong></p>
<p>点击预约提醒，，弹出toast提示“预约成功”，同时设置按钮状态为灰色。</p>
<h3>4. 反馈页</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/OEweF5NCzH7vp8lmUOsI.png" alt width="749" height="520" referrerpolicy="no-referrer"></p>
<p><strong>（1） </strong><strong>页面逻辑内容</strong></p>
<ul>
<li>页面由“讲座错误”和“讲座取消”两栏和底部提交审核按钮构成；</li>
<li>“讲座错误”下拉框分为“主题修改”，“主讲人修改”，“时间修改”，“地点修改”，点击可进入具体页面填写；</li>
<li>“讲座取消”下拉框点击可勾选具体原因；</li>
</ul>
<p><strong>（2） </strong><strong>页面交互</strong></p>
<ul>
<li>点击“讲座错误”或“讲座取消”，前面显示蓝色对勾符号，同时展开下拉框，再次点击可收起。</li>
<li>点击提交审核按钮，弹出toast提示“提交成功”，同时设置按钮状态为灰色。</li>
</ul>
<h3>5. 上传讲座页</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/0bIzJobjPjkO7OE8PLxv.png" alt width="740" height="533" referrerpolicy="no-referrer"></p>
<p><strong>（1）  </strong><strong>页面逻辑内容</strong></p>
<ul>
<li>信息填写框由“讲座主题”、“主讲人”、“地点”、“时间”、“主讲人简介”、“讲座简介”和图片上传等几个部分构成；</li>
<li>底部为提交审核按钮。</li>
</ul>
<p><strong>（2）页面交互</strong></p>
<ul>
<li>点击对应的填写信息框，闪动光标，同时填写栏字体边框设置成蓝色；</li>
<li>点击提交审核按钮，弹出toast提示“提交成功”，同时设置按钮状态为灰色。</li>
</ul>
<h3>6. 当前提醒页</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/iHZbusPzOlFYK1BojdSj.png" alt width="663" height="406" referrerpolicy="no-referrer"></p>
<p><strong>（1） </strong><strong>页面逻辑内容</strong></p>
<ul>
<li>页面由讲座信息模块和“取消提醒”按钮组成；</li>
<li>讲座信息模块显示从左往右，从上往下分别显示讲座海报、讲座主题、主讲人、讲座具体时间、地点信息。</li>
</ul>
<p><strong>（2） </strong><strong>页面交互</strong></p>
<p>点击删除提醒按钮，弹出toast提示“确定取消讲座提醒”，用户根据需要进行操作。</p>
<h3>7. 我的页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/ex6rajMkCTPXX1MuDClP.png" alt width="771" height="527" referrerpolicy="no-referrer"></p>
<p><strong>（1） </strong><strong>页面逻辑内容</strong></p>
<ul>
<li>我的页面由个人信息、实名认证、当前提醒、历史提醒、我的反馈、订阅更新通知、我的设置几个部分组成；</li>
<li>个人信息显示用户头像、昵称和学号。未登录状态个人头像和昵称显示默认值，用户实名认证以后显示学号信息，未实名认证也为默认值；</li>
<li>当前提醒和历史提醒显示用户当前与过往预约讲座提醒的列表；</li>
<li>我的反馈显示用户提交审核的讲座勘误信息和上传的讲座信息，点击可查看具体详情；</li>
<li>点击我的设置可设置相关功能。</li>
</ul>
<p><strong>（2） </strong><strong>页面交互</strong></p>
<p>点击订阅通知更新按钮，设置按钮状态为打开。</p>
<h2 id="toc-6">六、后台设计</h2>
<p>到这里我们基本完成了讲座信息小程序的前台设计和简化版的需求文档写作。但很多时候，后台产品的设计也是产品经理工作的重要组成部分，为了更充分地展示mvp产品前后台的衔接，我把后台的产品设计也加入了进来。</p>
<h3>1. 后台产品功能结构图</h3>
<p>根据前台对产品功能的定义，本款小程序功能实际包括两大块，一是内容的呈现，二是用户对内容进行勘误和自主上传。</p>
<p>对于后台来讲，不仅要考虑信息的呈现的问题，还要考虑信息的抓取来源，以及用户如何进行信息反馈，所以后台目前需要包括内容管理和用户管理两个方面，经过整理的产品后台初步功能结构图如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/y11sTyHQ4Wmvj1H3B3JO.png" alt width="651" height="157" referrerpolicy="no-referrer"></p>
<h3>2. 后台页面及说明</h3>
<p><strong>（1） </strong><strong>内容–内容抓取</strong></p>
<p>在后台的这一模块可以设定前台内容的来源和呈现方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/tnjTWtTT5KGx2KnuhZ5J.png" alt width="673" height="416" referrerpolicy="no-referrer"></p>
<p><strong>页面定义如下：</strong></p>
<p>1）选择需要爬取讲座信息的学院，此选项为必选；</p>
<p>2）根据选择自动带出所对应的校区，此选项为非必选；</p>
<p>3）选择该学院讲座信息爬取的网站，不超过三个来源；</p>
<p>4）选择信息抓取的频率。</p>
<p><strong>（2） </strong><strong>内容—内容管理</strong></p>
<p>这一模块支持对前台内容进行编辑修改以及删除。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/5m5fpPk6TEsOVsfvDRhY.png" alt width="678" height="360" referrerpolicy="no-referrer"></p>
<p><strong>页面定义如下：</strong></p>
<p>1）支持的前台呈现的内容进行筛选，当前可按照讲座主题、所属校区与学院进行筛选；</p>
<p>2）列表字段与前台呈现的字段保持一致；</p>
<p>3）点击学院名称可呈现该学院信息，包括学院官网、信息爬取来源、教务老师联系方式等；</p>
<p>4）操作“编辑”和“删除”按钮实现对信息的管理。</p>
<p><strong>（3） </strong><strong>用户—用户反馈</strong></p>
<p>这一模块支持对用户勘误的信息进行处理。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/6iRIVQFwx0FY9pEHI1Qt.png" alt width="794" height="583" referrerpolicy="no-referrer"></p>
<p><strong>页面定义如下：</strong></p>
<p>1）支持对用户反馈的内容进行筛选，当前可按照讲座主题、所属校区与学院进行筛选；</p>
<p>2）列表字段除了前台呈现的部分字段以外，还包括反馈类型、具体类别、备注以及用户ID；</p>
<p>3）点击学院名称可呈现该学院信息，包括学院官网、信息爬取来源、教务老师联系方式等；点击用户ID可以显示该用户相关信息，包括昵称学号联系方式等，方便运营人员及时联系用户核实反馈信息的真实性。</p>
<p>4）操作“通过”和“忽略”两个按钮实现对信息的管理。点击“通过”，信息即可在前台完成更新。</p>
<p><strong>（4） </strong><strong>用户—用户上传</strong></p>
<p>这一模块支持处理用户上传的讲座信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/QdYR5wBbEhIFOfUK9Mqc.png" alt width="649" height="431" referrerpolicy="no-referrer"></p>
<p><strong>页面定义如下：</strong></p>
<p>1）支持的前台呈现的内容进行筛选，当前可按照讲座主题、所属校区与学院进行筛选；</p>
<p>2）列表字段与前台呈现的字段保持一致；</p>
<p>3）点击学院名称可呈现该学院信息，包括学院官网、信息爬取来源、教务老师联系方式等，点击用户可以显示该用户相关信息，包括昵称学号联系方式等，方便运营及时联系用户核实反馈信息的真实性；</p>
<p>4）操作“通过”和“忽略”按钮实现对信息的管理。点击“通过”，信息即可在前台显示。</p>
<h2 id="toc-7">七、需求排期</h2>
<p>mvp产品虽然比较小，但功能的实现同样有个先后的问题，经过评审后的需求排期如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/pO6ej4MaCyTbYXBDrbMi.png" alt width="620" height="213" referrerpolicy="no-referrer"></p>
<h2 id="toc-8">八、总结</h2>
<p>我们通过需求分析、用户路径、产品功能规划、页面设计、需求文档写作，快速设计出了产品前台的雏形，并通过后台产品方案的设计，完成了整个产品框架的建构，在后面仍需要和研发测试保持沟通，才能让产品最终上线。</p>
<p>前面提到了mvp产品功能演进蓝图的问题，以本款产品为例，如果市场反响还可以，形成一定流量，后面的功能演进蓝图可以包括自习室，校园问答，以及综合查询等等，都可以规模复制和推广到其它院校。</p>
<p><strong>其实这正体现了mvp 产品的最大价值：用较小的成本在最短的时间内快速地验证市场和需求。</strong></p>
<p>万物之始，大道至简，中华道家哲学早已看透产品思维。</p>
<p> </p>
<p>作者：我的鞋子大了，微信公众号：青芒产品笔记，定位于个人产品学习成长平台</p>
<p>本文由 @我的鞋子大了 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5204712" data-author="1287554" data-avatar="http://image.woshipm.com/wp-files/2021/10/M26SrRLWLHThIzPRcdse.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            