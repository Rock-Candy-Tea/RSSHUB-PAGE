
---
title: 'UX细节设计思路——必经流程简化'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/lkOGky4ktYPbTNxHe5qM.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 29 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/lkOGky4ktYPbTNxHe5qM.jpg'
---

<div>   
<blockquote><p>编辑导语：当可以预判用户可能的一系列操作时，交互设计上应该将这系列流程做简化处理，即必经流程简化。本文作者对这个设计思路进行了分析，一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5462450" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/lkOGky4ktYPbTNxHe5qM.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>优秀UX细节创新设计让用户感到方便、贴心、可靠、安全、愉悦。UX细节创新设计并非都来自一刹那的灵光乍现， 创新能力也不是少数人只可意会不可言传的一种天赋，优秀的UX细节创新设计其实有章可循，创新能力是可以通过后天培养提升的，更多内容可参阅《伟大的小细节》一书。</p>
<p>本文分享技巧——必经流程简化。</p>
<p><b>必经流程简化的设计思路：</b>当可以预判用户可能的一系列操作时，交互设计上应该将这系列流程做简化处理。</p>
<p>这种简化包含两种类型：</p>
<ol>
<li>剔除可预见用户操作中不必要的操作流程</li>
<li>合并可预见用户操作中必操作的流程</li>
</ol>
<p>简单行之有效的办法就是操作流程记录法，记录下不同场景用户达成某一项目标的完整流程，在流程各节点中寻找可以判断用户意图的节点，跳过不必要的流程，或者合并必要流程。</p>
<p>操作记录法设计产品Tips：</p>
<ul>
<li>画出完整流程图，不仅有助于察觉可以优化的地方，严谨的流程分析也是发现设计漏洞的重要手段。</li>
<li>不要局限于自身产品流程设计，用户完成一项功能可能需要在不同的网站和App中切换操作，要将这些操作也纳入设计范围。</li>
</ul>
<h2 id="toc-1">01 设计讲解 – 登录注册</h2>
<p>注册/登录是网站、手机App必备的基本功能。随着移动互联网的普及，为防止恶意注册账户，许多网站、手机App在注册时都会使用手机号作为账户，并需要通过短信验证才可生效。</p>
<p>为了省掉用户手动输入短信验证码的麻烦，一些App提供了获取验证短信并自动填写短信验证码的功能，如日韩、东南亚非常流行的聊天软件LINE。</p>
<p>目前国内的一些App也支持这样的功能，如“爱鲜蜂”。爱鲜蜂是一个较为特别的案例，本文以爱鲜蜂为例进行讲解。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="UX细节设计思路之 必经流程简化" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/WfTnLYnqBN2sUb29uzpF.jpeg" alt="UX细节设计思路之 必经流程简化" width="311" height="549" referrerpolicy="no-referrer"></p>
<p>LINE获取到验证短信后会自动填写短信验证码：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="UX细节设计思路之 必经流程简化" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/0uIZjFBxmmbkKK6hwVAw.jpeg" alt="UX细节设计思路之 必经流程简化" width="304" height="538" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">爱鲜蜂注册页面及MIUI短信提示框</p>
<p>第二张截图的主体是爱鲜蜂的注册界面，当输入手机号点击获取验证码后，爱鲜蜂会读取短信，并将短信中的验证码自动填写到验证码输入框中；而界面的顶部则是MIUI的短信提示框，它也根据短信内容判断出这是一条短信验证码，点击右边复制按钮，即可复制验证码，直接粘贴至验证码输入框内即可。</p>
<p>单纯站在爱鲜蜂注册功能的设计者的角度，一个完整的注册流程只需要包含如下环节：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="UX细节设计思路之 必经流程简化" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/rYCI6KERkUS6FHcyjyvS.png" alt="UX细节设计思路之 必经流程简化" width="1280" referrerpolicy="no-referrer"></p>
<p>乍一看并没有可以优化的空间，这里先阐明功能实现的设计思维与需求解决设计思维的区别，前者只要求功能设计运转正常合理即可，而后者除了需要完成前者所需要实现的功能外，还需有代入感，把自己当成用户，设计时就不能只局限于自己所提供的服务了。</p>
<p>基于需求解决的设计思维，一个完整、顺利的注册流程应该是：在输入手机号与填写验证码之间，用户还会需要切换到短信功能、记住验证码或者复制验证码、返回到“爱鲜蜂”App 中，然后才是输入或粘贴验证码。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="UX细节设计思路之 必经流程简化" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/EyiN0Y3m9CYK2QCQNrbu.jpeg" alt="UX细节设计思路之 必经流程简化" width="358" height="332" referrerpolicy="no-referrer"></p>
<p>流程中，切换到短信功能、记住验证码或者复制验证码、返回到“爱鲜蜂”App中、输入或粘贴验证码是用户必须要做的事情，此时为了优化用户体验，技术人员可以用技术手段，帮用户完成这部分操作（读取手机短信内容、识别短信中的验证码、复制验证码并粘贴到验证码输入框中）。</p>
<p>那我们再往前思考，既然自动帮用户填写好验证码，为什么不直接帮助用户完成验证并登录呢？可以先思考几分钟再看后面的内容。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="UX细节设计思路之 必经流程简化" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/wy0xRFhXKVWQjVCC0pmT.jpeg" alt="UX细节设计思路之 必经流程简化" width="352" height="400" referrerpolicy="no-referrer"></p>
<p>除了为用户带来方便的细节设计能力外，严谨是比此类细节创新更重要的品质，之所以不能设计成填写手机号便可自动登录，主要原因有以下两点：</p>
<ol>
<li>不是所有设备都能成功获取到读取短信权限（比如用户设置了不允许App获取自己的短信信息），一旦短信获取失败，而用户又无法手动填写，那么整个注册流程便卡住了，无法继续下去，这将是严重的设计错误。</li>
<li>用户注册时并不一定使用当前手机，即用其他手机接收验证短信， 或者正在使用iTouch、iPad等根本就无法接收短信的设备进行注册，同样会导致整个注册流程无法继续。</li>
</ol>
<p>当然，如果能够妥善处理好这些问题，一键注册登录也未尝不是一个优秀的细节设计。</p>
<h2 id="toc-2">02 设计案例</h2>
<h3><b>1. MIUI</b></h3>
<p>前面爱鲜蜂注册页面顶部的短信提示框同样是基于用户的行为预判的优秀细节设计，MIUI系统能够识别收到的短信是不是验证短信，如果是验证短信，则短信提示框右侧提供一个复制验证码的按钮，用户点击该按钮，MIUI会提取短信中的验证码复制到手机的剪贴板中，并提示：MIUI已经帮您复制好短信验证码，直接粘贴即可。</p>
<p>这样用户就不必切换至短信功能中阅读或复制验证码，在当前操作界面中即可完成验证码的复制、粘贴。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="UX细节设计思路之 必经流程简化" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/nk0QURBNC0ymzPNbE7Vq.jpeg" alt="UX细节设计思路之 必经流程简化" width="358" height="605" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">MIUI收到短信验证码后提供复制验证码按钮</p>
<h3><b>2. 搜狗输入法</b></h3>
<p>正常情况下，各类括号（如大括号、小括号、中括号）、书名号、引号等标点符号都是成对出现的，既然必然成对出现，那输入正括号后，自动输入反括号，并将光标跳回到括号间，这样输入既方便，也能防止忘记输入反括号。搜狗输入法就这么机智地干了！</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="UX细节设计思路之 必经流程简化" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/DWc2MrnUrmMHeStMeFTf.jpeg" alt="UX细节设计思路之 必经流程简化" width="694" height="292" referrerpolicy="no-referrer"></p>
<p>使用搜狗输入法输入正括号后，会自动补全反括号，并将光标跳转至括号之间。</p>
<h3><b>3. Google</b></h3>
<p>必经流程简化的另外一种情况是必要流程合并。当一位设计师需要按照黄金比例设计一个作品时，正常的流程是：打开搜索引擎>搜索黄金比例>找到有黄金比例具体数值的网页>点击去复制黄金比例数值>切换到计算器计算所需要的对应数值（雅虎、必应、NAVER及国内各大搜索引擎皆可体验）。</p>
<p>Google 对此作了体验优化，当用户使用Google搜索“Golden Ratio（黄金比例）” 时，搜索结果会弹出一个计算器，搜索结果中直接展示黄金比例数值，如果需要计算，就直接继续操作吧！</p>
<p>分析起来，Google先是帮助用户直接将所需要的黄金比例数据提取出来，省去用户一个个网页去查找的烦恼。而后是考虑到了用户可能会使用该数值进行计算，又直接提供了一个计算器，方便用户直接计算。</p>
<p>更进一步，Google将两者合并到一个界面中，用户可能只需要一个黄金比例数值，并不受影响啊，不是么！</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="UX细节设计思路之 必经流程简化" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/or3xMJiMkY2wA094K3F5.jpeg" alt="UX细节设计思路之 必经流程简化" width="678" height="468" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">在Google中搜索“Golden Ratio（黄金比例）”</p>
<h3><b>4. 淘宝</b></h3>
<p>同样也是必要流程合并的细节创新，这个细节创新多少有点儿无奈— App出于商业和安全性的考虑，微信屏蔽了手机淘宝App的分享链接，从手机淘宝并不能直接分享链接给微信好友。</p>
<p>于是手机淘宝创造性地发明了“淘口令”。可很多用户还是习惯使用截图给好友分享商品，可收到截图的微信朋友可就有点麻烦了，想要访问这个商品，要么要求好友重新发淘口令，要么根据截图内容去淘宝搜索，不论怎样，都是一件挺麻烦的事情。</p>
<p>当手机淘宝发现用户使用手机淘宝对商品详情页进行截图时，会弹出一个对话框出来告诉你“已经为您生成淘口令”，用户可以选择将截屏和淘口令一并发给好友，这样就避免了好友再次询问淘口令或者使用截图内容去搜索的麻烦。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="UX细节设计思路之 必经流程简化" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/CCLPqz7QTEXRpokffyrW.jpeg" alt="UX细节设计思路之 必经流程简化" width="333" height="592" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="UX细节设计思路之 必经流程简化" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/F9D0ahveyVz5bbQ9D3YE.jpeg" alt="UX细节设计思路之 必经流程简化" width="341" height="606" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">手机淘宝App商品详情页界面</p>
<h3><b>5. Waymate.de</b></h3>
<p>http://Waymate.de是德国一家专门做旅行路线规划的网站，当使用 Waymate.de 搜索一个行程时，加载过程中会显示计划时间目的地的天气状况，提供给用户参考，如果用户正好需要查询，则省去再查询天气的操作，即便用户并不需要这一信息，对用户的操作也无任何影响。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="UX细节设计思路之 必经流程简化" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/qsGEvsHpgYuOzv3WsbJn.jpeg" alt="UX细节设计思路之 必经流程简化" width="620" height="345" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Waymate.de行程加载页面</p>
<p> </p>
<p>作者：文哲，微信公众号：伟大的小细节，《伟大的小细节》作者。</p>
<p>本文由 @Stanley 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5462064" data-author="113325" data-avatar="http://image.woshipm.com/wp-files/2021/12/VN17TBzw0dBKq9znIDAQ.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            