
---
title: '倒推夸克浏览器APP需求文档'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/NDrtlKCbzoZv7mL9jVHy.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 19 Oct 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/NDrtlKCbzoZv7mL9jVHy.jpg'
---

<div>   
<blockquote><p>编辑导读：说到浏览器，夸克的口碑在众多浏览器产品中一直是正面居多。本文作者对夸克浏览器APP进行需求文档的倒推，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5182065 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/NDrtlKCbzoZv7mL9jVHy.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>目的：提高自己对需求文档的撰写能力，以倒推的方式去理解需求文档编写的本质和过程。做一份能让读者一目了然的文档，毕竟文档的本质是准确有效的沟通表达工具。</p>
<h2 id="toc-1">一、文档综述</h2>
<h3>1.1 版本修订记录</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/6Qup16lOW2ngmBO8A9xE.jpg" alt width="758" height="283" referrerpolicy="no-referrer"></p>
<h3>1.2 PRD输出环境</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/hCYR1KNkG98VL1fLd9Qo.jpg" alt width="594" height="441" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、产品概述</h2>
<h3>2.1 产品介绍</h3>
<p>夸克浏览器是一款以轻、快为核心，设计风格简约，专注用户浏览体验的信息获取工具。夸克浏览器致力于用极简思路对抗信息冗余，满足用户对于浏览器最本质的需求，启动时无任何多余加载项，瞬间启动无需等待。</p>
<h3>2.2 产品定位</h3>
<p>夸克浏览器无信息流、搭载极速AI引擎智能搜索，为用户的信息获取提供极速精准的搜索体验。</p>
<h2 id="toc-3">三、需求分析</h2>
<h3>3.1 需求背景以及场景分析</h3>
<p>现如今，人们获取知识的途径大部分来自上网浏览和搜索，而在飞速发展的信息时代中，生产和传播度日益加快为用户带来丰富供给满足多元需求同时，也出现象信息爆炸这样的诸多难题其中尤以信息泛滥、信息超载、信息浪费等最为明显。信息泛滥和超载，导致真正有价值的信息被大量无用信息所淹没，用户不得不耗费大量的时间精力来挑选真正有价值的信息。尤其是现状大部分APP都是广告以及弹窗，非常影响用户的使用体验。</p>
<p>以下是柠檬在日常生活的场景和需求，信息也源自于网络搜集，非纯拟写。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/0yXBjGRnNRg1xPbR9l2w.jpg" alt width="742" height="563" referrerpolicy="no-referrer"></p>
<h3>3.2 用户画像</h3>
<p><strong>3.2.1 区域分布</strong></p>
<p>从百度指数信息可获知，地域分布城市排行榜前五名的是：北京、重庆、成都、广州、深圳。从中可以看出使用夸克的主要用户群体在一二线城市等经济发达地区。这些城市有大量的互联网用户，对互联网内容信息的获取需求相比其他城市的用户更高。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/75TABLCEcaGQIDbed68g.jpg" alt width="1268" height="547" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">来源：百度指数</p>
<p><strong>3.2.2 用户属性</strong></p>
<p><strong>人群属性</strong></p>
<p>从图中内容可以看出使用夸克的用户群体年龄阶段分布在20-40岁，这个年龄段的用户大部分是大学生或者已经工作的职业者，用户群体的成长环境以及工作经历使得他们对浏览器的需求也越来越高。</p>
<p><strong>性别分布</strong></p>
<p>从图右边的柱状图可以看出，夸克浏览器的用户群体性别分布男性大概为58%，女性大概42%，可以看出夸克更受男性用户的欢迎，也是夸克用户的主力军。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ADgkf8yipo1f2NKcmoPz.jpg" alt width="1755" height="579" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">来源：百度指数</p>
<p><strong>兴趣分布</strong></p>
<p>从下面的柱状图和标签可以看出，夸克的用户群体在使用方面的需求相对广泛，各个标签占比相差不大，反应出夸克的功能能够满足大部分用户的需求，能够有效满足用户的使用需求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/dugzOkOV1kuJGbNZS10h.jpg" alt width="1269" height="383" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">来源：百度指数</p>
<p><strong>总结</strong>：根据上面百度指数呈现出来的信息，夸克的用户群体是主要分布在一二线城市、年龄阶段在20-40岁、以男性用户为主，并且用户的兴趣需求广泛。</p>
<h2 id="toc-4">四、产品结构</h2>
<h3>4.1 夸克APP功能结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/b7IDXSHSLht5PUFkyErY.jpg" alt width="853" height="682" referrerpolicy="no-referrer"></p>
<p><strong>总结</strong>：从上面功能结构图可以看出夸克浏览器主要是由【搜索】、【阅读】、【网盘】、【夸克宝宝】组成，搜索功能板块通过AI智能引擎搜索可以快速精准得到结果；阅读板块多样化满足用户阅读娱乐需求；网盘的强大功能能够满足用户的文件保存和同步需求；夸克宝宝拟人化的动态和萌化的声音更能给用户陪伴感。</p>
<h3>4.2 夸克APP信息结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/qZk0E38zVH0oKBKdQD3D.jpg" alt width="1266" height="1774" referrerpolicy="no-referrer"></p>
<p><strong>总结</strong>：从上面的信息结构图可以看出，夸克浏览器的信息结构主要是通过小程序以及网页跳转的方式组合的功能模块，玩法新奇且多样化，这是好处。但是在首页中的【捷径】、【AI应用】等功能模块，内容太过于乱且复杂，会让用户的选择体验造成较差的影响，未能做到相对的精简化。并且跳转页面的方式会让用户等待时间变长，操作路径变长，产生烦躁的情绪。需要收集用户反馈做下一步迭代，删减低使用率的小程序和网页网址。</p>
<h2 id="toc-5">五、全局说明</h2>
<h3>5.1 权限说明</h3>
<p>功能权限区分为登录状态和非登录状态</p>
<p><strong>1）非登录状态</strong></p>
<p>夸克学习功能板块中的夸克翻译、作文搜索等功能不能使用，以及夸克网盘中的功能都不能正常使用。其他功能正常浏览使用。</p>
<p><strong>2）登录状态</strong></p>
<p>登录状态下，用户可以对APP内的所以功能正常操作使用。</p>
<h3>5.2 键盘说明</h3>
<ul>
<li>点击手机号和验证码输入框时，页面底部弹出数字键盘</li>
<li>点击其他搜索栏或者输入框，底部弹出全字母中英文键盘</li>
</ul>
<h3>5.3 页面交互</h3>
<p><strong>5.3.1 搜索功能交互页面</strong></p>
<p>文字搜索页面交互</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/tb7l9DCoZQzKT76oMtFc.jpg" alt width="986" height="582" referrerpolicy="no-referrer"></p>
<p><strong>文字搜索</strong>：当点击搜索框或首页下滑时，皆可弹出文字搜索栏。输入框中输入文字之后，“取消”变成“搜索”，点击即可跳转至搜索结果页</p>
<p>语音搜索页面交互</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/F19qaNXURe3s0yjWgPKO.jpg" alt width="792" height="733" referrerpolicy="no-referrer"></p>
<p><strong>语音搜索</strong>：</p>
<p>当点击搜索栏中的语音按钮，会弹出夸克宝宝识别语音，识别成功后会自动跳转至搜索页。当没有声音输入时，“夸克宝宝正在听”会变成“不好意思，我好像没有听见”，并且有“点击重试”按钮。</p>
<p>点击首页其他任意一处即可收起语音输入。</p>
<p>拍照扫描页面交互</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/hCTCFv6DxRsmsZsBda1s.jpg" alt width="792" height="737" referrerpolicy="no-referrer"></p>
<p><strong>拍照扫描页面交互</strong>：当点击搜索框中的扫描图标时，跳转至扫描拍照页，根据用户需求选择不同标签和功能。在左上角可关闭返回首页导航。</p>
<p><strong>5.3.2 阅读板块页面</strong></p>
<p>阅读板块之书架页面交互</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/4SqSWk2g1AceyW8adNqz.jpg" alt width="1104" height="726" referrerpolicy="no-referrer"></p>
<p><strong>阅读板块交互</strong>：阅读娱乐板块细分为四大功能模块，分别为“书架”、“小说”、“漫画”、“游戏”。在书架页面中，有页面交互的功能有：点击搜索框会跳转空白页并弹出全字母键盘；在定制推荐书籍下面，点击之后跳转至阅读功能，当退出时弹出“将本书加入书架”，用户可选择下次或者加入。</p>
<p><strong>小说和漫画功能板块的交互基本同上</strong></p>
<p><strong>游戏功能板块点击即跳转至小程序模块。未详细展示</strong></p>
<p><strong>5.3.3 窗口页面跳转交互</strong></p>
<p>窗口页面交互逻辑</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/6V5uRPiiC0AHzx81lEmH.jpg" alt width="671" height="717" referrerpolicy="no-referrer"></p>
<p><strong>窗口页面交互</strong>：在窗口页，点击图标之后会缩小当前窗口，并在下方显示“返回”“增加”“删除”按钮图标，用户根据需求可操作增加减少或者保留窗口。</p>
<p><strong>5.3.4 夸克网盘页面交互</strong></p>
<p>主要页面交互在非登录状态</p>
<p><strong>夸克网盘非登录状态页面交互</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/4MYwbcNT5s24VqpYvGF8.jpg" alt width="1055" height="680" referrerpolicy="no-referrer"></p>
<p>网盘非登录交互：在点击网盘图标后会跳转至网盘页面，当前页面为非登录状态。若点击任何功能皆会弹出“登录弹窗”。用户根据自身要求可以选择登录方式，登录前需要勾选“同意用户协议”，若不勾选则不能登录。</p>
<p><strong>登录成功状态</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/O6qEiO9EPa6oxm4fZp3z.jpg" alt width="820" height="715" referrerpolicy="no-referrer"></p>
<p>网盘登录成功状态：可正常使用任何功能，在右下角有“首页图标”，按下即可返回首页导航页。</p>
<h3>5.4 页面异常</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/4jKLX0qZSSOKfOZycAW7.jpg" alt width="379" height="717" referrerpolicy="no-referrer"></p>
<p>当网络异常时，页面显示网页连接失败提示，</p>
<h2 id="toc-6">六、业务流程图</h2>
<h3>6.1 夸克登录业务流程图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/POolCjHkq10vZc9a9b3j.png" alt width="1530" height="1310" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">七、产品主要功能页面逻辑及说明</h2>
<p>夸克浏览器页面由四大功能页面组成，分别为首页导航、阅读娱乐、夸克网盘以及个人中心四大板块。以下将展示出四大功能页面的逻辑图，以便读者能够清晰了解。</p>
<h3>7.1 首页导航逻辑图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/80LW8kaVoNqJAwOLPFLt.jpg" alt width="1666" height="2134" referrerpolicy="no-referrer"></p>
<p>首页导航功能逻辑说明：</p>
<p><strong>搜索功能分为三种搜索方式，分别为文字搜索、语音搜索、拍照搜索。其对应的触发方式是：</strong></p>
<p><strong>1-1文字搜索</strong>：按住首页空白处下滑可触发；点击搜索框可触发，在输入框中输入文字后，右边的“取消”会自动变成“搜索”。</p>
<p><strong>1-2语音搜索</strong>：点击语音图标即可弹出语音输入弹窗。当有语音输入时，自动识别并跳转之搜索页；当没有语音时，会变成提示语“不好意思，我没有听见”并且有“点击重试”按钮。</p>
<p><strong>1-3拍照搜索</strong>：点击拍照图标即可跳转至搜索扫描页，用户根据自身需求选择相对应的标签功能，分别有：“扫码”、“翻译”、“试卷”、“题目”、“识物”、“扫描文件”、“提取文字”、“扫描证件”、“自拍证件照”、“扫描药品”等功能标签。点击左上角图标可返回首页，点击右上角两个图标可开启“手电筒”以及“摄像头切换”。</p>
<p><strong>功能模块组件：首页默认的功能组件是：“捷径”、“AI应用”、“精选”、“夸克学习”。其相应的功能有：</strong></p>
<p><strong>2-1捷径</strong>：“每日关注”中有天气功能、历史上的今天、热搜榜、夸克知识局、更多热搜、疫情等；“娱乐一起嗨”中有00后黑话、5分钟小测试、趣味小游戏、心爱书房、二次元动漫、免费小说等；“每日推荐”中有云上赏名校、今日笑不停、高分影视、今日份壁纸、每日星座运势等；“每日有料”中有毒舌日历、热门表情包、今日话题、公开课、3小时公益等。</p>
<p><strong>其他几个功能组块也是这样的构成方式，只不过功能不一样，就不一一列举，是在太多…</strong></p>
<p><strong>总结</strong>：在首页导航页面，夸克做到了极致的精简和高颜值，并且能够提供多种搜索方式供用户选择；在功能组件模块中的功能也是多种多样，能够满足大部分用户的需求，有效提高用户的使用时间。但是这一方面也有缺点，过多的功能会让用户选择不来，可根据用户点击率来适当删减部分功能。</p>
<h3>7.2 夸克网盘逻辑图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ODCkfMeYHMRVZqnwcmdT.jpg" alt width="2526" height="2151" referrerpolicy="no-referrer"></p>
<p>夸克网盘页面逻辑说明：</p>
<p><strong>前置条件：用户需要登录才能使用网盘功能，非登录状态下不能使用，点击任何图标都会弹出登录弹窗。</strong></p>
<p>夸克网盘具有会员制，会员与非会员部分权益有所差异，会员具备有更多的存储空间、极速下载、视频备份、极速上传、大文件上传等权益。非会员制能够使用的功能页相对比较齐全。</p>
<ul>
<li>云文件板块：视频、图片、文档、音频、压缩包等云上传保存网盘的功能。</li>
<li>常用工具板块：我的文件、云收藏、手机备份、扫描文件等。</li>
<li>转换工具板块：转为word、转为PPT、转为Excel、转为PDF等转换文档功能。</li>
<li>扫描工具板块：扫描文件、自拍证件照、扫描证件等。</li>
<li>夸克文档板块：实用范文、PPT模板、简历模板、全部分类等。</li>
<li>功能动态版：不同功能随机展示…</li>
<li>最近文件：最近使用的文件会在这里显示，可显示和隐藏。</li>
</ul>
<p><strong>总结</strong>：夸克网盘的功能工具总体而言比较齐全，能够满足大部分用户在文件以及编辑等方面的需求，并且在非会员的状态下，大部分功能都能够使用。能够有效获取非付费用户的好感以及使用频率，从而提高网盘的用户基数。</p>
<h3>7.3 阅读娱乐逻辑图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ijOuTWcxG4qkwmBhBs9O.jpg" alt width="2182" height="2193" referrerpolicy="no-referrer"></p>
<p>阅读娱乐页面逻辑及说明：</p>
<p><strong>阅读娱乐页面主要由四大功能页组成，分别是“书架”、“小说”、“漫画”、“游戏”。</strong></p>
<ul>
<li><strong>书架页</strong>：主要功能是搜索和书架展示，右上角功能图标分别是历史记录以及小说会员，在页面下方可根据用户喜好随机推荐书籍，并且可以根据标签定制推荐。</li>
<li><strong>小说页</strong>：主要功能是搜索以及推荐，还可通过分类、排行、精选、免费等标签功能进去浏览，右上角功能图标可将小说添加至首页导航以及进入小说会员。</li>
<li><strong>漫画页</strong>：漫画页功能主要是根据排行榜以及分类，用户可根据自身喜好选择。右上角图标分别是漫画会员、搜索、以及添加漫画至首页导航。</li>
<li><strong>游戏页</strong>：游戏页主要是根据标签进行分栏展示，右上角图标分别是搜索和添加游戏至首页导航。</li>
</ul>
<p><strong>总结</strong>：阅读娱乐页面能够满足用户的看和玩的需求，多样化的分类和个性化的推荐，能够在用户无法选择的时候随机推荐，解决了用户的选择困难问题。并且在该板块设置了相关的会员制，可给用户更多的选择和体验。</p>
<h3>7.4 个人中心逻辑图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/0ILEcdtxavrAkHIG4eHq.jpg" alt width="1787" height="2039" referrerpolicy="no-referrer"></p>
<p>我的页面逻辑及说明：</p>
<p>我的页面中展示的功能相对比较少，主要是“书签”、“历史”、“下载”“网盘”、“夸克宝宝”以及一些浏览器的设置功能，在这里可以查看手机的文件以及清理等。呈现给用户简约的一面。</p>
<h2 id="toc-8">八、商业模式分析</h2>
<p>夸克的盈利模式主要是靠会员机制、广告和夸克课程，会员极致分为网盘会员、小说会员、漫画会员三种模式，广告页主要呈现是在小说阅读页的下方呈现。夸克课程在夸克学习页课程销售。</p>
<p><strong>1）网盘会员：网盘会员分为三类，普通会员、超级会员以及学生套餐</strong></p>
<p>1-1普通会员：连续包月新用户专享首月1.9元，后面每月仅需5元，连续包年费用50元。单年费用60元，单月费用12元。支付方式可通过支付宝、花呗、和微信支付三种方式支付。相比非会员多了3TB空间、极速下载、视频备份、极速上传、大文件上传等权益。</p>
<p>1-2超级会员：连续包月新用户专享每月19.9元，连续包季58元，连续包年198元。并且设置了花呗分期免息，分别是12个月，15*12期；6个月，9*12期；3个月，5.5*12期。支付方式也是同上，权益方面比非会员多了6TB空间、视频备份、文件格式转换、极速下载、极速上传、无限云收藏、无限云解压、AI画质、音频模式、视频倍速…..等等，还有好多就不一一列举了，反正意思就是，充钱就是爹的意思。</p>
<p>1-3学生套餐：参与夸克校园计划，需要进行学生认证。连续包年费用10.9元；连续包月0.99元，权益和普通会员一致，支付方式同上。</p>
<p><strong>2）小说会员</strong>：小说会员只有一种会员模式，但是在付费方面用户有多种选择，分别是：连续包月，首月1元次月开始15元；单月20元；连续包季35元；3个月会员45元；6个月会员90元；连续包年88元等六种付费模式。可让用户根据自身需要进行选择。付款方式只能是支付宝。会员享受权益是“全场免广告”、“会员书库”、“付费书9折”等权益。</p>
<p><strong>3）漫画会员</strong>：漫画会员会跳转至快看漫画，若开通的话是快看会员。用户有四种付费方式，分别是连续包月15元、一个月18元、3个月50元、12个月183元。付费会员享受的特权有“每日礼包”、“作品限免”、“会员折扣”、“提前阅读”、“尊贵身份”…等等。</p>
<p><strong>4）夸克的付费课程是在夸克学习功能板块的自学。不同的课程费用不同，用户据需购买。</strong></p>
<p><strong>总结</strong>：夸克虽然是说简约无信息流，但是盈利模式还是有三种方式，给用户极致简约的体验，让用户留在夸克，不同的用户可根据自身需求开通不同的会员。并且付费模式多样化，可以让用户有更多的选择，而不是强绑强卖。广告的盈利方式比较单一，只有在小说阅读页才有展示栏，并且小说会员可以关闭广告，在夸克学习页的课程也是不同课程不同费用。从上可以总结出，夸克的盈利模式主要是靠会员机制。</p>
<h2 id="toc-9">九、总结</h2>
<p>夸克浏览器作为一款由UC出品的产品，其强大的后台系统和数据支持是它成功必不可少的条件。简约高颜值的页面、极速精准的搜索功能、无信息流和免广告更是获取了无数用户的好感和支持。并且在付费方面更是以用户为中心，多样化的付费方式可以让用户有了更多的选择。强大的功能模块能够有效提升用户的使用时长。</p>
<p>拟人化的夸克宝宝能够给用户更多的陪伴感。在网盘功能的使用上，非付费用户也能够使用较多功能，能够有效促活用户提升用户基数。因此，相比于市面上的其他浏览器，夸克浏览器更符合年轻用户的需求和体验感受，并且年轻用户付费能力较强，所以夸克浏览器保持创新和风格化，相信能够在市场上更能在这竞争状态下胜出，做独一无二的自己。</p>
<p>本人是一名0-1年的产品新人，做这份需求文档的目的之一是在广州找工作和理解需求文档的编写流程和本质。在整个编写过程中，我借鉴了部分前辈的框架逻辑，也加入了我的个人想法。如果写的不好，请给出意见，谢谢各位大大。</p>
<p> </p>
<p>本文由 @Thinker 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5180778" data-author="1241774" data-avatar="https://static.woshipm.com/APP_U_202103_20210330224012_6904.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            