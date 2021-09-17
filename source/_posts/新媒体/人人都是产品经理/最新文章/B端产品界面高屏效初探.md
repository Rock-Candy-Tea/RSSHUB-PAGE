
---
title: 'B端产品界面高屏效初探'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/uhICkQcZ8OaWmnYb6AN7.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 17 Sep 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/uhICkQcZ8OaWmnYb6AN7.jpg'
---

<div>   
<blockquote><p>编辑导语：在B端设计领域，用户对界面的屏效方面都存在同样的诉求。本篇作者就对这一问题，从用户案例收集、竞品分析和论文查阅入手，进行视觉、交互和信息三层面的实践设计，推荐想了解B端产品界面屏效，如何从倾听用户需求，到发现问题和解决问题过程的童鞋阅读。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5140165 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/uhICkQcZ8OaWmnYb6AN7.jpg" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、背景</h2>
<p>在 B 端设计领域中，不管是内部用户、产品、设计师、开发，还是外部产品、设计师等，总能听到关于界面「屏效」方面的诉求或吐槽。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/frTRUJtm3YAIY5KPJYCt.png" referrerpolicy="no-referrer"></p>
<p>「屏效」狭义理解是「界面过度留白」；广义理解，「屏效」源自谐音“坪效”，指的是每坪的面积可以产出多少营业额(营业额/专柜所占总坪数）。而「屏效」对于界面而言可以指屏幕单位时间、单位面积内的信息可以带来多少商业效益/效率提升。</p>
<p>为了探索在 B 端产品中用户为何对「界面过度留白」或「屏效」问题如此敏感，于是我们展开了「屏效」专题的设计探索与实践。「屏效」专题探索主要以「探索」与「实践」相结合的方式展开，将实践过程中反复验证有效的设计策略沉淀成设计手册，同步将部分功能进行工程化，确保可以开箱即用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/Ilei33CEqtNjXXbk5oZa.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、探索阶段-为谁在何时何地设计</h2>
<h3>1. 用户声音｜不同的故事相似的诉求</h3>
<p>面向内部设计师和终端用户投放的《高屏效诉求》《中后台产品满意度调研》问卷中认为提高屏效能极大提升用户体验的设计师占 58.14%；认为提升屏效对体验有提升的终端用户占 50.6%。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/ZrRE8psAZhg2W9saC0sb.png" referrerpolicy="no-referrer"></p>
<p>外部知乎上针对《Ant Design 4.0 设计价值观》的 13 条反馈里，其中就有 2 点提到关键字「效率」。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/ZDptEKkUXrLjOhC6qqrI.png" referrerpolicy="no-referrer"></p>
<p>通过了解不同用户和产品类型发现，不同的用户在工作场景的产品使用中有着相似的特征：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/cNasvYeloVzZG5Bbk2sW.png" referrerpolicy="no-referrer"></p>
<h3>2. 案例收集｜发现问题，大胆假设</h3>
<p>纵观 B 端产品界面，发现普遍问题和收录在解决屏效问题上实践得比较好的案例，为了逐步突破问题，选择以数据产品中覆盖率极高的表格为设计切入点，通过线上跨产品多端地毯式的体验走查，发现表格三个层次的问题：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/UZ1Tv9BbvAFl7qW1ACFG.png" referrerpolicy="no-referrer"></p>
<p>视觉、交互层在无需理解业务场景和用户目标的情况下，都较容易发现，属基础问题，但很多「过度留白」的屏效问题往往是信息被组织方式的差异导致的「过度留白」。</p>
<p><strong>综上我们提出假设：为提高屏效，可从视觉、交互、信息三个层次解决。</strong></p>
<p>视觉层为提高信息查阅速度，可以通过提高信息密度；交互层为提高操作速度，可以缩短当前手势到目标之间的距离；信息层为提高信息被理解的速度，可以通过重组织等方式。</p>
<p>基于假设，我们进行了进一步的桌面研究，查阅论文等书籍，寻找设计理论的验证和指导。</p>
<h3>3. 竞品分析｜寻找实践证据，谨慎验证</h3>
<p>我们知道视觉上界面留白过多（过疏会增加滚屏成本，过密因易串行而影响阅读效率），以表格「行高」为例，探索各表格在字号、字高和行高的关系，因为不同字体的同字号实际像素高度会有差异。</p>
<p>因此选择的是字高（即文字垂直高度的视觉大小）而非字号或字行高，决定留白的两个重要因子是字高和表格行高，以次推演，界面元素和元素间距的留白关系，探究在视觉层怎样的留白率能保证甚至提升屏效。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/hn8Hh6kNi8MLrpXPTz6H.png" referrerpolicy="no-referrer"></p>
<p>以数据产品中的表格为例，通过直接和间接竞对的方式，分别从数据的查阅（视觉）、分析（交互）维度进行功能点和设计细节上的比对，来看看优秀产品是如何解决屏效问题。</p>
<ul>
<li>直接竞对：内部用户口碑较好的产品。</li>
<li>A、B外界竞对：同领域的 Tableau、网易有数、金山、微软表格。</li>
<li>间接竞对：谷歌邮箱、AntD 等的紧凑主题的常规列表（一维表格）。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/sTqSxURkYinlM6Kc3qVK.png" referrerpolicy="no-referrer"></p>
<p>通过竞品分析可以发现，数据分析领域的表格留白率普遍较低（信息密度高），尤其是金山和微软的电子表格，其次是同类面向数据用户的 Tableau、网易有数，而谷歌邮箱等工作台常用的常规列表紧凑版本中，留白率和数据领域的电子表格不相上下。</p>
<p>紧凑版的使用场景也常常是面对数据量巨大的信息呈现，通过切换紧凑主题，提升信息的快速浏览，而这也非常适合数据分析场景中巨大的数据量呈现。因此我们的产品在留白率的提升空间极大，而在实际案例实践中，也已经将表格行高优化至 30px，克制的使用留白。</p>
<p>除此外，竞品其他层次的设计也做了比对，总结来看整体设计做法：高密度、少屏数、少留白等。</p>
<p><strong>文字陷阱：中英文字高不等于字号</strong></p>
<p>举个容易犯错的竞品参考是，谷歌在紧凑版主题下字号 12px，列表行高是 28px，但在 AntD Table 中同样的 12px 和列表行高 28px 就会发现非常拥挤，缺乏呼吸感。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/UPMrzulKF6bNZ9ER59YY.png" referrerpolicy="no-referrer"></p>
<p>原因在于谷歌的 12px 是英文字体，实际字高只有 10px，而 AntD Table 的语境是中文字偏多，实际字高有 12px，所以留白的差异在于一个是 18px（28-10），一个是 16px（28-12），这也是为什么决定决定留白的两个重要因子是「字高」和表格行高，而非「字号」和表格行高，进一步推演，决定界面留白的是「元素视觉高度」和「元素间距」。</p>
<h3>4. 论文查阅｜寻找理论证据，谨慎验证</h3>
<p><strong>研究表明，低密度认知负荷低，但高密度任务完成率高，用户更喜好。</strong></p>
<p>参考资料：论文《基于眼动的网页对称性和复杂度对用户认知的影响的研究》。</p>
<p>对于信息，用户需要需要阅读（视觉），思考和理解（认知），需要点击按钮、操作鼠标和打字（行动），在人机工程学中，统称为负荷。即认知（记忆）负荷、视觉负荷、动作负荷，即分别对应用户体验设计的三个层级，信息/视觉/交互。而负荷所花费资源从多到少依次为：认知 > 视觉 > 行动。</p>
<p>认知负荷，举个例子，看了但不一定懂了。你是否有这么一种体验——刷抖音，虽然很多（信息密度小，输出效率低），但可以一直刷下去并且刷很久；而看一门 C4D 教学视频，即使就短短十来分钟（信息密度大，输出效率高），但是却要看上半天。</p>
<p>因为刷短视频时，你的输入效率远高于作者的输出效率，而看一门 C4D 教学视频时，你的输入效率远低于作者的输出效率。</p>
<p>可是，输出效率是客观的，输入效率是主观的。如果输出效率很高，你可以通过提高自己的输入效率（比如让自己成为 C4D 专家）来跟上作者，从而变强；否则输出效率很低（信息质量低），你的输入效率很高（很专业），信息于你而言都是无效的。</p>
<p>假设负荷总量不变的情况下，那么以上三类场景界面需要对用户负担分配大致如下：</p>
<p>官网品宣类需要低认知成本，低视觉负担，视觉要求高，用户才会被吸引过来阅读，甚至酷炫的交互更能增加互动体验而带来的趣味感。比如苹果官网，信息量极少、图版率高带来极具艺术的视觉体验、进而吸引用户愿意跟随屏幕滚动渐进式接受信息。</p>
<p>而 B 端应用因为是专业使用，首先认知方面随着员工的专业度提高而降低，因此可以通过提高视觉负担，来降低行动负担，进而减少操作用时，当然最佳情况是三个维度能整体降低负担，让总负担降低，就需要更多设计巧思了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/iUkAh378c46AltZTilFP.png" referrerpolicy="no-referrer"></p>
<p>面向内部设计师和终端用户投放的《高屏效诉求调研》预设解决方案中，设计师常用的 Top 3 做法为：【信息层】隐藏不必要信息、【视觉层】提高布局紧凑度、【交互层】减少点击跳转。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/MxbCmObroUfWvv1Y01HB.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、实践阶段-如何设计</h2>
<p>通过以上的探索，我们可以确定的是，B 端产品面向专业人员的工作界面设计中，提高屏效可从视觉、交互、信息三个层次进行，视觉层-高密度，即提高屏幕信息密度；交互层-低跳转，通过减少页面跳转、手势与常用操作的距离等；信息层-有效性，通过重组织或辅助信息帮助用户理解，甚至提供帮助手册等以提高用户专业能力。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/Uy71rRatFoVFmR0qpS32.png" referrerpolicy="no-referrer"></p>
<p>基于以上的总结，对产品进行优化。下面以一个简单案例进行设计策略的解读。一位运营同学想对比 A、B 两不同人群在相同维度（白领-有信用卡）下的人数差异，寻找运营机会点。</p>
<p>如下表格经过高屏效策略优化前后对比图，优化前相同维度下不同人群数量的对比需要视线来回跳动比对，而优化后的表格内容，更符合用户看差异场景下分析目的数据查阅，视线锁定相同维度，即可快速比对数值大小。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/DtseyIUnfvAUYCgfIJeJ.png" referrerpolicy="no-referrer"></p>
<p>下面以视觉、交互、信息三个层次解剖设计过程背后的思考。</p>
<h3>1. 视觉层｜高密度-克制的留白</h3>
<blockquote><p>眼动理论：研究表明，人眼最小可视视角 0.3 度，水平最大眼动舒适转动区 30度，垂直最大眼动舒适转动区 55度。可得出人眼最小识别范围 12px，水平视野舒适眼动宽 1200px，垂直视野舒适眼动高 2200px。参考资料：论文《基于眼动交互的用户界面设计与研究》。</p></blockquote>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/JdSTO3gtFJPGXyLmpTb6.png" referrerpolicy="no-referrer"></p>
<p>如图，缩小表格行高的同时，目标信息之间的眼动距离随之缩短，在眼动舒适区内看到更多信息，便于信息的高效获取。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/wdESaOk2Tl4qrjdOL403.png" referrerpolicy="no-referrer"></p>
<h3>2. 交互层｜低跳转-高频信息前置</h3>
<blockquote><p>理论基础：菲茨定律是用来预测从任意一点到目标位置所需时间的数学模型，它由保罗·菲茨在1954年首先提出。这个模型考虑了用户定位点的初始位置与目标的相对距离、目标的大小、移动的最短时间。三者之间关系公式为：T=a+blog2(D/W+1)，W为其中目标的大小；D为到目标的距离；T为移动到目标所用最短时间。参考资料：菲兹定律。</p></blockquote>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/ond9Pv3GcMCPuMWfQhA7.png" referrerpolicy="no-referrer"></p>
<p>表格单元格借助交互状态，增加悬浮出现的信息组件，前置显示目标单元格明细信息，同时通过交互出现的指示器辅助行列信息的获取，高频操作考虑手势位置放置，缩短与操作目标的距离，以提高整体操作效率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/NtKRUT1JRTJYIXpO87go.png" referrerpolicy="no-referrer"></p>
<h3>3. 信息层｜有效性-信息重组织</h3>
<blockquote><p>理论基础：交互设计四大策略「组织、删除、隐藏、转移」。参考资料：《简约至上》。</p></blockquote>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/yJiA5p9Z6CTVJWYGrjLM.png" referrerpolicy="no-referrer"></p>
<p>用户为了对比 A、B 两不同人群在相同维度（白领-有信用卡）下的人数差异，但内容的重组织方式让两数据行需要频繁点击滚动条来查看，根据用户目标，将关联性大的数据放置相邻列（即将要对比的人群放置列头），即可快速查阅，减少眼跳距离。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/bjqLKrVdyUsvAi7Pv3a4.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、结语</h2>
<p>设计趋势中常见的大字体大留白界面，但在 B 端场景中，面对紧张的工作节奏，时间和注意力变得尤为可贵，相对而言，基于复杂度守恒定律， B 端信息量大且高频访问的产品中，「用得快」要比「看得美」更重要，「高密度」「低跳转」诠释的即是「空间换时间」，少一次点击，少一次跳转，少一份等待，就多一份时间和效率。</p>
<p>特别感谢小伙伴的指导和帮助：@完白 @梓义 @不过 @铭秋 @元尧</p>
<p>参考资料：</p>
<p>论文《基于眼动的网页对称性和复杂度对用户认知的影响的研究》</p>
<p>论文《基于眼动交互的用户界面设计与研究》</p>
<p>《Ant Design 3.0 背后的故事》</p>
<p>https://sizecalc.com/ 可以计算通过视觉距离，物理大小和最终得到感知角度的网站</p>
<p>https://experience.sap.com/fiori-design-web/cozy-compact/</p>
<p>https://www.material.io/design/layout/applying-density.html#usage</p>
<p> </p>
<p>作者：白弦，蚂蚁集团设计师</p>
<p>本文由 @Ant Design 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5137876" data-author="1275742" data-avatar="http://image.woshipm.com/wp-files/2021/05/qQzaYS0DiYKZrsomCZyR.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            