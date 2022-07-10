
---
title: '三个印度人改变压缩算法 一意孤行 没它就没有JPEG'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220710/Sbe1a7390-79bd-4dcb-b2b5-646452c831c8.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sun, 10 Jul 2022 15:33:34 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220710/Sbe1a7390-79bd-4dcb-b2b5-646452c831c8.jpg'
---

<div>   
<p>世界上最好用的压缩软件是什么？</p>
<p>微信。</p>
<p>这个段子想必很多人都听过。</p>
<p>一张几兆的图片，经微信一发，立马降到几百kb。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/be1a7390-79bd-4dcb-b2b5-646452c831c8.jpg" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="185" src="https://img1.mydrivers.com/img/20220710/Sbe1a7390-79bd-4dcb-b2b5-646452c831c8.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>△如果是有损压缩画质会下降（右图天空有波纹）</p>
<p>虽说这是个吐槽，但u1s1，图片视频压缩其实是一项非常必要的技术。</p>
<p>比如视频通话、传输大量图片时，如果不压缩的话，要么图像完全无法传送，要么就是干等了。</p>
<p>所以在数字时代这几十年里，萌生出了很多相关的技术，比如JPEG、H.26X。</p>
<p>不过你或许不知道，这些技术往上追溯，可以从47年前说起。</p>
<p>有三位名不见经传的印度工程师“一意孤行”，在没申请到研究经费的情况下，利用暑假时间鼓捣出来了一项技术，后来直接成为图像视频压缩的行业标准。</p>
<p>它就是DCT。</p>
<p>全称为Discrete Cosine Transform，即离散余弦变换。</p>
<p>而有趣的是，DCT诞生之初时，就连作者本人都没有想到，它后来会有如此巨大的影响力。</p>
<p><span style="color:#0000ff;"><strong>没有DCT，就没有JPEG/MPEG</strong></span></p>
<p>直接说DCT可能很多人不知道是什么，但JPEG大家肯定都听过。</p>
<p>它除了是一种常见的图片文件后缀名，其实也是一种有损压缩标准，可以把一张图片从左边这样变成右边这样：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/f42ee1a5-09d3-4f79-b391-f7bbd6a4e0a8.png" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="292" src="https://img1.mydrivers.com/img/20220710/Sf42ee1a5-09d3-4f79-b391-f7bbd6a4e0a8.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>ps.有损和无损的区别：无损压缩可以再100%还原图像；有损不可以，但有损压缩后的图像大小会大大减少。</p>
<p>DCT就是实现这个过程的一种基础技术。</p>
<p>它是傅立叶变换的一种，可以将图像从空域转换到频域，也就是把图像从像素矩阵变成用带有频率等信息的函数来表示。</p>
<p>具体变换过程，我们以一张图像中一个3x3的像素块为例：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/86c1fd77-453f-4d4f-971f-50a110239531.png" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="572" src="https://img1.mydrivers.com/img/20220710/S86c1fd77-453f-4d4f-971f-50a110239531.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>△ 图源博客园博主@沉默的背影 X-Pacific</p>
<p>对这个像素块做DTC变换，就相当于把除了第一个像素以外，其余像素的部分信息都抽取到第一个格中。</p>
<p>这样，第一个格的像素值表示的就是一张图的总体样貌，称为低频信息；其余格表示的就是图像中人物或物体的细节，称为高频信息。</p>
<p>经DCT转换后，每个3x3的像素块都会产生1个DC（直流）系数（位于第一个格）及8个AC（交流）系数（剩余格），前者是DCT最重要的输出。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/2d137253-c789-4da7-b55f-0a56861df379.png" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="213" src="https://img1.mydrivers.com/img/20220710/S2d137253-c789-4da7-b55f-0a56861df379.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>由于大部分的图像能量会集中在低频部分，因此转换之后输出的DC系数值比较大，而输出的AC系值比较小。</p>
<p>利用“人眼对低频分量的图像比对高频分量的图像更敏感”这一原理，再通过量化保存下来低频分量，舍弃高频分量（将大部分AC系数值变为0）、丢掉那些对视觉效果影响不大的信息，从而达到压缩目的。</p>
<p>从下面这两张图像的三维投影，我们可以看到DCT变换带来的改变：</p>
<p>（上：原图；下：经过DCT变换后）</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/9ef6c55a-2e21-4d6c-8e45-f6bdefdc0c42.png" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="643" src="https://img1.mydrivers.com/img/20220710/S9ef6c55a-2e21-4d6c-8e45-f6bdefdc0c42.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>在实际的JPEG压缩标准中，都是将一张图像分成若干个8x8的像素块（不够的用空白补齐）。</p>
<p>将色彩空间从RGB转为YUV之后，从左至右、从上至下对每个块进行DCT变换。</p>
<p>然后对每个块变换得来的系数进行量化，在这个过程中，一些重要的分量就被去除了，且无法恢复。</p>
<p>因此，这是一种不可逆的有损压缩技术。</p>
<p>接着对量化后得到的AC系数和DC系数再分别进行编码，经过哈夫曼编码后得到下面这样的一大串数字。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/80ecf8ad-56d6-4708-baf7-051a9ad4a918.png" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="232" src="https://img1.mydrivers.com/img/20220710/S80ecf8ad-56d6-4708-baf7-051a9ad4a918.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>解压缩时对每个图像块做DCT反转换（IDCT），就可以重建完整图像。</p>
<p>具体计算过程如下：</p>
<p>首先将图片中每个像素的原始灰度和亮度值用8bit表示，也就是(0，255)这个范围。</p>
<p>由于大多数值都会分布在128左右，所以会将这些值都减去128，这样会有更多值为0，有利于压缩，这时候范围变成(-128，127)。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/22c87679-c690-4adb-a35b-1dc4b86ea4e2.png" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="159" src="https://img1.mydrivers.com/img/20220710/S22c87679-c690-4adb-a35b-1dc4b86ea4e2.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>然后再用DCT变换公式进行变换，二维的用这个：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/6f1dfe7b-3e04-422c-9752-7936806ec62d.png" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="76" src="https://img1.mydrivers.com/img/20220710/S6f1dfe7b-3e04-422c-9752-7936806ec62d.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>变换完后进行根据量化表进行量化，将大部分系数变为0，完成压缩。</p>
<p style="text-align: center"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="342" src="https://img1.mydrivers.com/img/20220710/d413eef8-a849-496e-8fca-808441d229ce.png" style="border: black 1px solid" w="400" referrerpolicy="no-referrer"></p>
<p>ps.量化表是根据人眼对量化误差的视觉阈值来确定的，有固定的一张表。</p>
<p>后面就是前面说的一系列编码过程了。</p>
<p>1974年1月，这项技术首次被发表在IEEE Transactions on Computers上面。</p>
<p>自此，图像和视频压缩领域的行业标准就诞生了。</p>
<p>1998年世界首个视频压缩标准H.261、1992年的JPEG和MPEG、2010年的WebP、2013年的HEIF、2018年谷歌亚马逊等公司联合创建的AV1……等压缩标准都是基于这项技术，且一直沿用至今。</p>
<p><span style="color:#0000ff;"><strong>40多年都名不见经传的发明者</strong></span></p>
<p>DCT的作者有3位，分别是Nasir Ahmed（纳西尔·艾哈迈德）、K.R. Rao（K.R.拉奥）和T. Natarajan（T.纳塔拉詹）。</p>
<p>纳西尔是新墨西哥大学电气与计算机工程系名誉教授。</p>
<p>他1940年出生于印度班加罗尔，1966年在新墨西哥大学获得博士学位。</p>
<p>1966-1968年，他在霍尼韦尔公司担任首席工程师，1968-1983年在堪萨斯州立大学担任教授。</p>
<p>1983-2001年，他回到新墨西哥大学担任电气与计算机工程系首席教授。在此期间，他先后担任过系主任、研究生院院长等职位。</p>
<p>今年，纳西尔已经有82岁高龄。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/64af4f53-7356-4371-b5eb-809b467f8f5f.png" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="307" src="https://img1.mydrivers.com/img/20220710/S64af4f53-7356-4371-b5eb-809b467f8f5f.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>另一位主要作者是K.R.拉奥。</p>
<p>他同样是一位美籍印度裔学者。</p>
<p>1960年，他在佛罗里达大学获得核工程专业博士学位。1966年，又在新墨西哥大学获得电气与计算机工程专业博士学位。</p>
<p>之后50年，他一直在得克萨斯州阿灵顿分校工作，担任电气工程系教授。</p>
<p>与此同时，他还是IEEE Fellow。</p>
<p>2021年1月15日，拉奥教授挥别人世，享年89岁。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/070b5937-0536-47a1-8949-35ec34f04ba1.jpg" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="803" src="https://img1.mydrivers.com/img/20220710/S070b5937-0536-47a1-8949-35ec34f04ba1.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>T.纳塔拉詹当时是纳西尔带的博士生，如今在互联网上已经检索不到太多他的相关信息。</p>
<p>可以说相比于大名鼎鼎的DCT，几位发明者称得上是“名不见经传”了。</p>
<p>实际上，40多年来，DCT发明的幕后故事一直鲜有人关注。</p>
<p>甚至连纳西尔的儿子都表示，“从来没想过父亲带来的影响有如此之大”。</p>
<p>而将纳西尔从幕后推至台前的，还多亏了一部美剧中的一波致敬。</p>
<p>2020年，《我们的生活》中有一段剧情是纳西尔以视频通话的方式，讲述了自己和妻子相爱的故事。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/eb6e0553-8a5d-48d1-88a2-ccf30fd083bf.png" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="398" src="https://img1.mydrivers.com/img/20220710/Seb6e0553-8a5d-48d1-88a2-ccf30fd083bf.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>片方表示，设计这一桥段的初衷，就是希望更多人意识到，当下我们能够通过互联网快速发送图片视频，都与纳西尔的工作离不开关系。</p>
<p>剧情播出后，不少媒体将DCT定义为“改变世界的算法”，也称纳西尔这位名不见经传的工程师，终于从幕后推到了台前。</p>
<p>不过，纳西尔在自己的回忆视频里表示，当初真的没想到DCT会带来如此大的影响。</p>
<p>我也无法预测技术发展的速度，对于FaceTime这些应用的出现，我感到非常惊讶。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/fa2d9035-0697-4e84-a78e-f12e9e9412a6.png" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="316" src="https://img1.mydrivers.com/img/20220710/Sfa2d9035-0697-4e84-a78e-f12e9e9412a6.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>△纳西尔年轻时（图左）</p>
<p>要知道，DCT最初可能差一点就被扼杀在了摇篮里。</p>
<p>1972年，当时已经对DCT初有构思的纳西尔向美国国家科学基金会（NSF）递交了一份申请，希望NSF能为他研究DCT提供资金支持。</p>
<p>不过令纳西尔惊讶的是，这个申请直接被毙掉了，评审人给出的意见是“它太简单了”。</p>
<p>但好在纳西尔并没有放弃，他始终觉得这个idea很有新意。</p>
<p>唯一令他有所顾虑的是，他可能是只能利用假期来完成DCT的相关工作了，而且这期间可能没有任何收入。</p>
<p>所以，纳西尔回家和妻子说：</p>
<p>我有直觉，这事儿值得做下去。只不过我们需要计划好如何度过一个没有薪水的暑假。</p>
<p>妻子没有任何犹豫就支持了他。</p>
<p>于是，在1973年的夏天，DCT的研究工作正式开始了。</p>
<p>参与到这项研究的，还有纳西尔的好友拉奥和博士生纳塔拉詹。</p>
<p>拉奥也是支持纳西尔研究DCT的重要人物之一。</p>
<p>在纳西尔的申请被毙掉后，他第一时间把自己的想法告诉了好友拉奥。</p>
<p>拉奥给出了这样的回复：</p>
<p>你要立即把这些结果以短文的形式发表。</p>
<p>这就是“How I Came Up with the Discrete Cosine Transform”诞生的始末。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220710/37e3e7fe-6410-4039-98f5-1ce9f48d1b7b.png" target="_blank"><img alt="三个印度人改变压缩算法 一意孤行整个暑假" h="157" src="https://img1.mydrivers.com/img/20220710/S37e3e7fe-6410-4039-98f5-1ce9f48d1b7b.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>后来，这篇文章几乎称得上是图片视频压缩领域的必读之文。</p>
<p>之后的故事，也就是我们所熟知的了。</p>
<p>1974年，《Discrete Cosine Transform》在IEEE Transactions on Computers上发表。</p>
<p>截至目前，这篇文章的被引次数已经达到5878次。</p>
<p>纳西尔曾在采访中表示，自己人生中最大的礼物，就是人们对DCT的认可。</p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：随心</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/yindu.htm">印度</a><a href="https://news.mydrivers.com/tag/yasuo.htm">压缩</a><a href="https://news.mydrivers.com/tag/suanfa.htm">算法</a>  </p>
        
</div>
            