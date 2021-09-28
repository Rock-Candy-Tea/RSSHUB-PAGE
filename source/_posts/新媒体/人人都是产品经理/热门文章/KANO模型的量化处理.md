
---
title: 'KANO模型的量化处理'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/XjWzGySZdMx7Ock3wrPv.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 23 Sep 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/XjWzGySZdMx7Ock3wrPv.jpg'
---

<div>   
<blockquote><p>编辑导读：KANO模型主要是对用户需求分类和排序，通过分析用户对产品功能的满意程度，来对产品的功能进行升级，从而确定产品实现过程中的优先级。本文作者围绕“KANO模型的量化处理”进行分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5148709 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/XjWzGySZdMx7Ock3wrPv.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>很多大厂在产品商业化、产品设计以及运营方面已经达到了非常精细化程度，比如在对需求优先级进行排序的时候，大家都听说过KANO模型，很多产品经理也会采用该模型去“凭感觉”进行划分，但感觉的问题在于一些模糊不清的地带和一些需要通过互相说服来决策的时刻，这种定性的方式很难让人达成共识。于是很多公司的用研部门会将“定量”的方式引入其中进行辅助，尤其越是庞大的产品，越是会做这样的事情。</p>
<p>既然说到这，那就来聊聊KANO模型，在定量的方式上可以如何去实施。</p>
<p>背景就不去做交代了，假定目前已经确定了一些需求已经要做，<strong>但由于开发资源以及项目时间周期的限制，目前只能从中挑出一部分需求去进行设计，而且大家争执不下的情况下，于是通过收集到用户以及内部员工具体的一些答案通过统计结果来进行量化抉择</strong>，便挑选出合适的用户发出了调查问卷，设计问卷的时候为了方便后面的量化操作，问题需要存在一定的设计逻辑。</p>
<h2 id="toc-1">一、明确需求分类</h2>
<p>先基于KANO模型，可以把需求分成如下几类：</p>
<ul>
<li>M：必备型需求，即痛点</li>
<li>O：期望型需求，即符合预期的</li>
<li>A：兴奋型需求，即超出用户预期的</li>
<li>I：无差异型需求，即用户不在意的</li>
<li>R：反向型需求，即会引起用户反感的</li>
</ul>
<p>对吧，很简单，但你思维稍微停一下，你会发现，它的本质<strong>只不过是按照将需求对用户的感受进行了不同程度的分类，这些程度之间是存在逻辑上的递进关系的</strong>。</p>
<p>你不觉得这玩意的底层逻辑跟之前接触过的很多东西都很像吗？比如，学校里面给学生打分的时候会有优秀、良好等方面的评级，公司里会按照不同岗位划分出不同的组织架构，哪怕去个奶茶店也会遇到小杯、中杯、大杯的区分。</p>
<p>这些东西的底层逻辑，要概括一下的话，<strong>其实都是基于MECE原则对某个事物按照“彼此独立，完全穷尽”的方式进行了分类而已</strong>。</p>
<h2 id="toc-2">二、调查问卷设计</h2>
<p>为了更好的得到方便量化的结果，问题设计上可以分为两个方向并提供不同的选项供用户选择。</p>
<p>问题可以包含两个方向：<strong>增加某个功能后用户的态度</strong>以及<strong>不增加某个功能时用户的态度</strong></p>
<p>答案则提供几种不同的程度，由喜欢程度的高到低分别是：<strong>非常喜欢、符合预期、无所谓、勉强接受、很不喜欢</strong></p>
<p>最终构建出来的结果如下图所示：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/bGew3PSLcUAyiHqyJBSR.png" referrerpolicy="no-referrer"></p>
<p>那么，在这里有一种比较特殊的情况，就是可疑结果（Q），毕竟对于一个功能的提供与否，用户都表现出了很喜欢或者很不喜欢这种自相矛盾的情况，所以，这样的结果在最终统计时，一般都需要排除掉。</p>
<p>同样，思维在这里稍微停一下，你会发现依然是一个仿佛接触过无数过的玩意。好像有点四象限法则的影子？好像还有点SWOT分析的赶脚？甚至这玩意还似曾相似的出现在你不知道要不要跳槽而感到迷茫时，你在纸上列出来的不同维度的对比……</p>
<p>其实，这些东西的底层就是<strong>矩阵思维，本质就是多角度纵横交叉的看待同样的一个问题</strong>。</p>
<h2 id="toc-3">三、调查问卷数据清洗加工</h2>
<p>在收集到问卷的结果后，对数据进行清洗并加工。下图所示就是之前我们在公司收集上来的调查问卷当中部分用户的反馈结果：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/dJ2iukfBFMamNmlbHpcR.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、对问卷进行需求分类</h2>
<p>再结合上面的不同需求类型的矩阵图，就可以<strong>针对每一条需求都划分出每个用户所认为的需求的类型是什么了，</strong>最终我们就定义出了需求的类型如下图所示：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/DSczy1wG7m3KYUqZFHPv.png" referrerpolicy="no-referrer"></p>
<p>到这里之后，其实问题就出现了。<strong>对于同样一条需求，不同用户所定义的需求类型是不一样的，那么，我们总得按照某种方式计算出一个最后的标准吧？最典型的思维方式就是少数服从多数，于是就可以考虑采用统计同一需求不用用户不同类型的定义，然后计算趋向于对用户带来好的方向影响的占比，再计算给用户带来不好的方向影响的占比，最后按照平均值划分进行定义</strong>。</p>
<p>在KANO模型里也是采用了上面的思考方式，只不过定义出了一个叫做better-worse系数的东西。</p>
<p style="text-align: center;"><strong>better系数 = (A+O)/(A+O+M+I)</strong></p>
<p style="text-align: center;"><strong>worse系数绝对值 = |-(M+O)/(A+O+M+I)|</strong></p>
<p>按照收集上来的问卷（包含了900份调查问卷的结果），统计和计算后的数据如下图所示：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/Dm5l69OIwZoaNdKPE4sv.png" referrerpolicy="no-referrer"></p>
<p>将统计后的每个需求对应的坐标点放置在better-worse坐标系当中，并且在坐标系当中基于所有的坐标点，<strong>生成better的平均值对应的参考线以及worse的平均值对应的参考线,划分出最终的兴奋型、必备型、期望型、无差异型需求，按照优先级必备型>期望型>兴奋型>无差异型划分出优先级即可</strong>。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/Xntl8xyHdPMgZuV5iCqA.png" referrerpolicy="no-referrer"></p>
<p>至此，一个KANO模型在实际工作中的量化处理案例就讲完了。</p>
<p> </p>
<p>作者：小风，产品经理；公众号：村上风</p>
<p>本文由 @小风 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5146446" data-author="174084" data-avatar="http://image.woshipm.com/wp-files/2017/05/altDeyYzpWUviBGO5CaP.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            