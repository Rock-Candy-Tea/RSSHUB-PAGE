
---
title: '以notion为例，浅析如何设计一款saas应用'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/VcXBiCZN7IbqEZff0SMG.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 21 May 2020 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/VcXBiCZN7IbqEZff0SMG.jpg'
---

<div>   
<blockquote><p>本文以notion为例，讲述了设计一款SaaS应用的7个步骤，与大家分享！</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-3890769" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/VcXBiCZN7IbqEZff0SMG.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>本文将以notion这款产品为案例，分析产品经理如何设计一款应用。</p>
<h2 id="toc-1">一、定义产品</h2>
<p>定义产品是设计产品的第一步，要用一句话说清楚。</p>
<p>notion的产品定义：notion是一款集合文件、文件管理以及数据库（all in one）的工作空间（来自notion网）。它囊括了wiki、word和teambition的常用功能，在此之外进行了扩展。重新定义了协作文档，像一款来自未来的软件。</p>
<p>产品名词解释：产品名词解释可以让整个团队对功能有相同的认知。</p>
<ul>
<li>workspace：工作空间</li>
<li>page：页面</li>
<li>notion的页面是无限层级的，一个页面能够添加多个页面，页面中的页面也可以继续添加页面。</li>
<li>block：块一个标题、一张图表都被定义为块，块具备在页面中随意拖拽的特性。</li>
<li>database：数据库，database也是block的一种，它主要包含图表、看板等。</li>
<li>view：视图，database可以用不同视图切换展示，例如表格可以切换为看板。</li>
<li>template：模版，可以直接复用的样式。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/ySeUxRO02deS547UIYmJ.gif" width="600" height="316" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、分析产品解决了什么问题？</h2>
<p>不解决用户问题的产品是没有生存空间的。</p>
<p>notion解决的用户问题：工作生活中，为了完成信息的录入和管理，我们常常要开启多个应用。频繁的切换、数据的黏贴大大降低了工作效率，notion以其all in one的原则解决这种问题。提高人们的工作效率。</p>
<h2 id="toc-3">三、研究行业现状，思考需求本质</h2>
<p>研究行业现状能够让产品具备市场竞争力。但行业现状的报告只能作为参考，核心的决策还是要取决于对用户需求本质的思考。</p>
<p>比如网易云音乐推出之前，音乐行业报告显示用户评论的意愿只有4%。</p>
<p>但真实情况是现在网易云音乐3亿用户中50%喜欢评论。因而仅仅以数据报告为依据并不准确。</p>
<p>牛奶找到了两张与saas相关的图表来浅析notion的行业现状。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/XViaFm2PBHCxLaAGrq7w.jpeg" width="600" height="432" referrerpolicy="no-referrer"></p>
<p>图一是金融行业数字化进行中，各项技术的占比，我们可以看到saas应用资金消耗占比最高。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/TYVbBum7qXPSshUfY7on.jpeg" width="600" height="494" referrerpolicy="no-referrer"></p>
<p>根据图二分析，目前saas应用整体的规模是逐年增加，这是利好现象，但是增速是明显递减的。</p>
<p>综上，我们可以分析得初步的结论，saas应用是有市场且可变现的。</p>
<p>用户或企业希望通过类notion的办公软件提升效率，应用操作越简单越好。如果仅仅把notion当作一个在线文档编辑器，上手确实很快，但如果真正实现all in one就要花一些功夫了。</p>
<p>notion虽然省去了切换应用的成本，但增加了操作难度。这与我们提出协同办公软件的核心需求相悖。</p>
<p>为什么说notion的学习成本很高呢？</p>
<p>牛奶本身是设计专业出身，学过很多技能型软件，新的工具我一般上手会比较快。但即便在这样的背景下，我想要了解notion的功能还查看大量的官方帮助文档和b站视频，在自己使用的时候仍然出现了问题。</p>
<h2 id="toc-4">四、分析竞品</h2>
<p>竞品分析就像走一条被前人踩出的山路。会让自己的产品少走很多弯路。</p>
<h3>1. notion竞品分析</h3>
<p>notion是一款创新型工具，没有完全一致的竞品。有一些类似的竞品，如，markdown、wiki、teambition、富文本、okr系统等。</p>
<p>除了这些经常被提到的竞品，笔者还认为notion某种程度上像一个自建网站的工具。通过分享notion的链接，可以将自己设计的页面分享给他人。</p>
<p><strong>与竞品相比，notion的优点</strong></p>
<p>通过功能的集合提升效率。all in one不是说说而已。</p>
<p><strong>与竞品相比，notion的缺点</strong></p>
<ul>
<li>学习成本高：notion创造了新的文档操作方式，因而是需要一定的学习成本的。在使用不局限于在线文档的功能时，需要对软件进行深入了解，这会打退一部分用户，当然也吸引来一群喜欢自定义的发烧友。</li>
<li>功能纵深不足：对于某些工具的深度使用者，notion是无法满足其需求的。增加了广度，自然要舍弃功能纵深，否则产品会过分庞大。</li>
</ul>
<h3>2. 产品面临的挑战</h3>
<p>notion新定义的block以及无限层级的页面都不同于我们常规的操作。因而产生的理解成本是notion需要面对的挑战。</p>
<p>notion整体的操作很有写代码的味道。从很多notion应用的介绍都出自于程序员之手就可以看出。notion目前通过提供很多可复用的模板，让用户更快掌握。</p>
<p>用户到底会不会接受这个新工具呢？</p>
<p>我们可以尝试根据俞军的产品价值公式来计算。</p>
<p style="text-align: center;"><strong>产品价值=(新体验-旧体验)-换用成本</strong></p>
<p>计算方式说明：选取功能全面、效率提升、服务质量、性价比、是否好玩、是否满足审美要求，是否满足炫耀的心理这八个因素来估算新体验和旧体验的差值，每个因素满分是100分，分别赋予不同的权重。这样总分就等于各项分数乘以权重。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/xVZwbErIQeYTPzvnbMjw.png" width="600" height="174" referrerpolicy="no-referrer"></p>
<p>注意：这里评分是根据使用软件的初期体验给出的。随着时间迁移，notion的操作复杂度会下降，易用性就会提升。但用户初期的体验很重要，没有了第一次也很难再有第二次。</p>
<p>根据计算结果，新体验还是优于旧体验的，不过这6分的提升不知道是否能战胜迁移文件产生的”替换成本“。</p>
<p>牛奶按照自己对协同办公软件的理解给出了权重和评分，这显然是不够准确的。但从中我们可以理解到三点相对客观的结论。</p>
<ol>
<li>如果用户心中协同办公软件的替换成本远远大于新旧体验的差值，那么用户不会选择更换。</li>
<li>对于一些小众用户，他们喜欢新鲜有趣的产品。当好玩和兴奋等因素权重和分数增加时，用户选择notion意愿也随之增强。</li>
<li>notion的效率提升得分不够高，是全新的操作方式造成的如果市场上出现了跟风现象；帮助notion培养了用户的使用习惯，那么notion的竞争力将大大提升。</li>
</ol>
<h2 id="toc-5">五、构建用户画像</h2>
<p>用户画像是我们在搜集到很多数据后，根据数据整合出来的几个典型的虚拟人物。可以帮助产品理解用户是什么样的人，有什么样的问题。</p>
<p>虽然是虚拟人物，我们会赋予他名字、照片、年龄、兴趣爱好，让这个人越丰满越好。他能够作为和他同年龄段、同职业等特征的群体的代表。</p>
<p>总结起来就是，概括后具体，虚拟却真实。</p>
<p>牛奶归纳了三个典型的notion用户画像</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/WW097VmE9pZRMQ6cpHMR.jpeg" width="603" height="335" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/PhuF6BSh7uEF1KklZe5T.jpeg" width="600" height="528" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/rh5mVk23dgWBdwDC99kd.jpeg" width="600" height="551" referrerpolicy="no-referrer"></p>
<p>详细的用户画像绘制方式可参照产品创新必备方法论-国外系统的产品创新方法论（一）</p>
<p>清楚了产品定位、产品要解决的问题、用户画像等问题，接下来就要看看如何把想法落地交付了。</p>
<h2 id="toc-6">六、思考产品形态</h2>
<p>了解了要解决的问题、用户画像，就要考虑产品的形态，什么样的形态可以最高效的解决用户的问题。</p>
<p>notion如何实现all in one的产品形态？</p>
<p>这部分是notion产品设计的难点，也是它与众不同的原因。我们来一起分析下notion的产品经理是如何思考解决问题的。一句话简单来说是将元素进行拆解、组合和丢弃，形成新的元素。这个新元素叫做block。这里的元素是指我们在文档、看板等工具中用到的最小单元，比如字体、图形、字号、符号等。</p>
<p>我们拿to do list举个例子。常规情况下我们在word里建一个to do list需要有选框和文本，然后通过复制多次选框和文本形成一个to do list。notion将这个组合定义为一个block，通过增删来实现选框和文本组合的快速操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/5Eve7Nv7IobIusCBfkNo.png" width="600" height="623" referrerpolicy="no-referrer"></p>
<p>Heading1也是一个block。就是我们常用的大标题，notion取消了字体大小和切换字体的功能，用既定的字号，将字体加粗后定义为一个可直接使用的block。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/qZtBdHqjhjkMjZplRJHA.png" width="600" height="640" referrerpolicy="no-referrer"></p>
<p>block的意义是将常用操作组合定义，避免细节操作带来的时间成本浪费。当然block也不能尽善尽美，比如字体在这里就被丢弃了。</p>
<p>因任何组合或单独的元素都可以被定义为block，比如图标、链接、看板。我们将在功能列表处对block做一个相对全面的总结。</p>
<h2 id="toc-7">七、撰写产品说明</h2>
<p>最后一部分是撰写产品相关说明的文档，可以让整个团队理解产品经理的想法。</p>
<h3>1. 版本和修订记录</h3>
<p>版本的迭代是为了快速叠以及尽早验证市场。通过功能的用户价值和商业价值评定优先级，同时，优先开发核心功能置后扩展功能。</p>
<p>记录版本修订是为了让团队清晰每一次的工作变化，避免混乱。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/ZFpQKwOvlCu1cVQkpk2F.png" width="600" height="49" referrerpolicy="no-referrer"></p>
<h3>2. 框架图</h3>
<p>框架图可以展示产品的层级关系。例如notion的workspace和page就是包含关系。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/qyVL39lcfUPdHQf1hlnw.png" width="600" height="1076" referrerpolicy="no-referrer"></p>
<h3>3. 页面展示形式：原型</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/dfotiLOlcQyV2dtYOpTu.png" width="600" height="583" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图片为notion产品截图</p>
<p>原型绘制遵循清晰明确的总原则，通过字体和颜色区分层级。</p>
<p>推荐阅读原型：“到底怎么画？”——如何画好产品原型</p>
<h3>4. 功能和操作</h3>
<p>以表格的形式清晰的描述功能的定义和所包含的操作。</p>
<p>牛奶这里按照功能是否有操作、功能分类进行了举例，如下图</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/iK9oqvDSp6Mtc3t33heT.png" width="600" height="697" referrerpolicy="no-referrer"></p>
<h3>5. 功能流程图</h3>
<p>流程图可以直观展现产品操作路径和系统判断流程。notion的操作流程并不复杂，其复杂性更多的体现在多样性。</p>
<p>page、block等功能的操作并不需要确认，如果误操作可以回撤。因而几乎没有复杂流程。</p>
<p>我们以【删除workspace】为例绘制功能流程图，这是为数不多可构成相对长流程的功能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/PQTfuGBG4nnyQYcFI52v.png" width="600" height="846" referrerpolicy="no-referrer"></p>
<h3>6. 操作方式说明</h3>
<ul>
<li>快捷调用block</li>
<li>用户输入：”/“</li>
<li>产品响应：弹出block选择窗口</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/365CT4eA0Btfx1mO8JjE.png" width="600" height="675" referrerpolicy="no-referrer"></p>
<p style="text-align: left;">版权说明：本文关于notion的漫画人物全部取自notion官网。关于产品的功能、用户画像、流程图为牛奶自己绘制。</p>
<h3>#专栏作家#</h3>
<p>牛奶，公众号：产品经理的小红书，人人都是产品经理专栏作家。分享对产品的思考和总结。</p>
<p>本文原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="3888889" data-author="369338" data-avatar="https://static.woshipm.com/APP_U_202101_20210112114359_2691.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            