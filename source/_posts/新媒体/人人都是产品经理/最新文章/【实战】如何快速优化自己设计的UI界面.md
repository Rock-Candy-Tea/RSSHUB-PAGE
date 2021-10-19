
---
title: '【实战】如何快速优化自己设计的UI界面'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2021/10/JkwV6bTUWBEhyVlOXJhG.png'
author: 人人都是产品经理
comments: false
date: Tue, 19 Oct 2021 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2021/10/JkwV6bTUWBEhyVlOXJhG.png'
---

<div>   
<div class="work-decoration-title">
<blockquote><p>编辑导语：UI界面设计不能抛开本质而注重形式，如果没有理解信息和内容的因果，是很难做出合理的设计的。本篇文章里，作者分别从个人中心、pc端迁移移动端以及图文列表优化三个方面分析UI界面案例，一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-704459 aligncenter" src="https://image.yunyingpai.com/wp/2021/10/JkwV6bTUWBEhyVlOXJhG.png" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>最近帮小伙伴们批改一些UI界面，UI界面设计不能抛开本质而注重形式，如果没有理解信息和内容的因果，是很难做出合理的设计的。</p>
</div>
<div class="left-img-con">
<div class="work-show-box">
<div class="article-content-wraper">
<p>那么收到小伙伴们的作业，我们一起来看看有没有什么问题，希望可以帮助大家解决一些问题。</p>
<h2 id="toc-1"><strong>案例1: 个人中心</strong></h2>
<p>从提交的这张UI界面来分析，先看一下整体，我们利用模块覆盖法来将页面的内容区分一下：</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/r0MuSGNFVGmLcgV57HjD.png" width="600" height="579" referrerpolicy="no-referrer"></p>
<p>我们发现顶部的内容在整体视觉上比较拥挤，并且信息比较散，所以我们要对顶部这块内容再拆分重组一下。这里他将数字部分内容整合到了左侧，但是这样会让左侧内容过于拥挤，而且右侧区域只有一个图标是达不到平衡的效果，虽然放了标签，但是标签和人的关联性还是差了一些，所以标签要么跟头像要么跟名字，而不要躲在角落里。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/EQcjdgS8m4XVDKoZhoN5.png" width="599" height="212" referrerpolicy="no-referrer"></p>
<p>另外数字的字体使用也会有一种被挤扁的感受，这里不建议用这样很瘦的字体。并且这里其实他将点赞和收藏一起收了起来可能是因为左侧放不下了，那么我们直接就另一起一行放数字新信息即可。这样名字与头像和平衡对称，数字又可以水平平均铺开，这是一种常规的处理方法。</p>
<p>其次，整个版面白色区域较多，那么中间的开通会员卡片的色彩就过于重了，虽然我们需要引导用户去开通，但是视觉上给人感知太强烈，就感觉有点突兀。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/mdLhu4QIuSjcYe87Yq7w.png" width="603" height="128" referrerpolicy="no-referrer"></p>
<p>个人中心其实更多的是展示与我相关的信息和内容，目前大部分产品的设计风格也都是以简洁为主，所以我们也尽可能的利用到这点。卡片插在中间是个不错的想法，但是一般我们在做UI设计的时候层级做出3层及3层以内即可，不要出现第四层。</p>
<p>3层指的是：<strong>背景层、内容层、悬浮层/叠加层</strong>，如果一个界面中出现4层，会导致界面的层级过多，信息就较为复杂，所以这个界面中，收藏夹一栏的卡片是不需要加投影的，只需要图标加文字的上下排列即可。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/Kdb12JKi2C4RHu4Cim9L.png" width="601" height="150" referrerpolicy="no-referrer"></p>
<p>接下去，下方的功能列表在浏览上效率过低，我们看到要浏览完这列信息我们视线需要折行，并且这些功能是不需要都放在页面下方去堆叠，其实顶部导航栏也是可以利用起来的，由于这是一款美食类的产品，用户很多时候也会在个人中心去搜索我创建的食谱、作品等内容，所以像搜索和消息可以直接放在导航栏，而设置和关于这些较低频的操作就可以合并起来，那么原来6行列表就变为了4行，那这四行内容我们可以直接用横向排列的形式去做了。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/z8QQfplzce90nkFobidF.png" width="600" height="285" referrerpolicy="no-referrer"></p>
<p>那么最后，如果要对界面做视觉上的优化，我们要对信息重新排版、图标进行重新设计，在原图中我觉得底部中间的图标还是具有品牌特征的，那么我们就把这个品牌特征拿过来，作为一个辅助图形，这个辅助图形就可以用在小标签和卡片背景的修饰中。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/8NlfVdnMdk63UeQYisfh.png" width="600" height="644" referrerpolicy="no-referrer"></p>
<p>很多新人设计师在做UI界面的时候就会不知道应该放什么信息上去。所以要明白的是这个信息能告诉用户什么，用户能通过这个信息判断什么，用户的浏览顺序和重点在哪里？</p>
<p>好了，再强调一遍，当你设计完一个UI界面的时候，先问一下自己这4个问题：</p>
<ol>
<li><strong>这个界面告诉用户哪些信息</strong></li>
<li><strong>用户能否通过这些信息判断自己是否要继续任务流程</strong></li>
<li><strong>界面的浏览顺序是怎样的</strong></li>
<li><strong>信息展示的重点和次要点是否展示合理</strong></li>
</ol>
<p>接下来讲两个案例：</p>
<h2 id="toc-2"><strong>案例2: pc端迁移移动端案例</strong></h2>
<p>第一次从pc端迁移过来的同学会有这几个问题，同样的界面信息和内容如果要完全保留的迁移到移动端应该怎么设计，一个界面放不了那么多内容。比如我们先来看这个这个卡片列表：</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/yQEW40c2iRxSsLekjBTK.png" width="600" height="636" referrerpolicy="no-referrer"></p>
<p>这个列表的信息很有pc端的特点，这位同学其实是有意识的将重要信息强化了，但是pc端到移动端我们是可以<strong>简化很多信息和细节的，另外在用户浏览的路径上也会有不同。</strong></p>
<p>那我们看到这个卡片中的信息，从上往下依次浏览好像并没有问题，但就是因为没有问题，这才是问题。类似这样的信息卡片，其实如果按照这样排，那么用户就会浏览完所有信息再做决策，而我们知道的是<strong>并不是所有信息都需要让用户去关注到</strong>，例如最终要的是标题、状态和查看轨迹，而不重要的是工单和创建时间。</p>
<p>怎么判断重不重要呢？一个是用户查看和操作的频率，另外就是业务侧的侧重点。这边为了隐藏一些敏感信息某些文案就处理了一下，大家可以看一下我们方案的前后对比。</p>
<p>这里没有删减任何信息，因为确实在业务方面需要某些信息，<strong>但是像“创建时间”“查看轨迹”“当前状态”这些是没有必要的文案就可以省略。而卡片的状态一般在移动端上会放在右上角显示，并且在移动端中不需要加图标做修饰。</strong></p>
<p>在原来的卡片中，如果我们要根据创建时间去找的话，<strong>因为工单、创建、状态3行文字有点类似，所以会导致寻找效率不高，那么我们就讲工单还有时间分开放置，</strong><strong>在滚动浏览的时候可以更好的寻找。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/iJMIL3CuDdokJp7mjOa0.png" width="600" height="536" referrerpolicy="no-referrer"></p>
<p>而查看轨迹按钮我还是去掉了，考虑到的既然这里是轨迹轨迹订单列表那么用户就知道进来是要查看轨迹的，所以不需要全部在卡片中给按钮，这个也是web和移动端的区别，<strong>移动端的卡片是可以整体点击的，就和电商的订单列表、提现记录等卡片列表一样的都可以点进详情，而web中的卡片则不行</strong>，所以用户在这里反正需要点击一次，那么这里就不需要给一个轨迹按钮，还显得更复杂。</p>
<p>再来讲个案例，相信很多同学在pc端的b端设计中遇到过这样的问题，<strong>就是很多表格类的信息在web端可以一屏放下，到移动端就放不下了，那该怎么去做。</strong>其实如果你们可以去参考阿里云的app，类似于这样pc端b端的移植到移动端来说，也只能部分移植。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/UhrWNA5ru9ChiKvz4dfv.png" width="601" height="277" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/806CNihnrsPVfEIYzhVf.png" width="601" height="637" referrerpolicy="no-referrer"></p>
<p><strong>因为移动端的导航太有限了，像pc端左侧和顶部的筛选控件可以放多层联动，并且横向可以展开更多的标签，但是移动端横线太受限了</strong>，大家可以看一下如果我们真的要整体迁移的话就会变成以下这样的情况，但是移动端的核心的方便快捷，并不适合那么复杂的内容在一个界面去进行交互流转，所以左侧纵向tab导航不会出现下拉展开的二级联动。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/T1TFI2vu8lWmZGHAooJ1.png" width="600" height="468" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/2mbvwgTUWudYPANOy7jN.png" width="600" height="504" referrerpolicy="no-referrer"></p>
<p>所以大家几乎没有看到过最后那样的终极形态，因为实在太复杂了，但是如果讲左侧的纵向导航去掉的话其实还是可以看一下。在这个表格中横向的筛选元素很多，那么就通过滑动或者点击来获取更多标签和表格内容，另外标签可以做排序但不能做展开筛选，类似的形式可以参考下汽车之家或者汽车配置界面。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/Tskcb5r0PmbybVCIa6Zx.png" width="601" height="235" referrerpolicy="no-referrer"></p>
<h2 id="toc-3"><strong>案例3: 图文列表优化</strong></h2>
<p>这是一个比较典型的图文布局案例，需要注意的是很多小的细节，整体来看页面上半部分有效信息太少。什么是有效信息就和上文我们提到的4点是一样的，如果你的界面只是为了展示好看的图片和简单的标题来排版，那么这个界面一定是无效的。如下：</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/EKHuxG8EJ7tR4olvnP0i.png" width="600" height="636" referrerpolicy="no-referrer"></p>
<p>然后底部的左文右图区域的信息又比较密集，和上半部分形成了一个明显的反差。另外加上一些小细节的处理不到位：卡片投影太短太深，圆角不够统一，文字行间距不合理，功能位置摆放不合理，这样整体就感觉到很多瑕疵。另外如果只是自己做练习那么图片可以选择的更美观一些，而不需要收到产品业务的限制，那么我们花10分钟来重新调整一下整体的布局和优化一些细节。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/10/vprxSM2NCb3HECR39V1C.png" width="600" height="574" referrerpolicy="no-referrer"></p>
<p>在版式上最后做了两个略有区别的版本，你们觉得哪个更好呢？</p>
</div>
</div>
<div>
<div class="document">
<h3>＃专栏作家＃</h3>
<p>应骏，人人都是产品经理专栏作家，公众号：应谋鬼计（shejishiyj）</p>
<p>本文由 @应骏 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
</div>
</div>
</div>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5182472" data-author="122389" data-avatar="http://image.woshipm.com/wp-files/2020/07/T0aylnsv7c0xtCSWj9YU.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            