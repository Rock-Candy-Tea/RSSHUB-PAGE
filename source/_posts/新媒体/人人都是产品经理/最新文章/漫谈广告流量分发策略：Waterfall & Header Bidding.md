
---
title: '漫谈广告流量分发策略：Waterfall & Header Bidding'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/mKCWqat9sQGegiNRHzMF.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 14 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/mKCWqat9sQGegiNRHzMF.jpg'
---

<div>   
<blockquote><p>编辑导语：流量，作为广告变现的基础，如何让其价值发挥最大化，这应该是每个广告从业人员都需要思考的问题。作者从 ADX 的角度出发，探讨 Waterfall & Header Bidding 的流量分发机制，与你分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4868404 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/mKCWqat9sQGegiNRHzMF.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>流量，作为广告变现的基础，如何合理利用流量，充分发挥其最大价值，是每个广告从业者都会面临的问题。本文从ADX的角度，探讨流量流转中的分发机制，合理的分发机制可最大化流量利益，希望读者能从本文获取一些启发。</p>
<h2 id="toc-1">一、流量流转机制</h2>
<p>ADX（AD Exchange），广告交易市场，在流量流转流程中起承上启下作用，向上对接DSP，向下对SSP/媒体负责，借助其工作流程来了解广告流量流转机制，有助于我们更好的去理解流量过分发过程中可能存在的优化点。广告流量流转机制如下：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/bwNPKHPubbUoWREwSxDY.png" alt width="747" height="959" referrerpolicy="no-referrer"></p>
<ol>
<li>当前端App触发广告流量机会时，会将本次流量下发给其对接的ADX，流量属性中通常会带有广告位和用户信息等相关属性；</li>
<li>ADX在接收到流量请求时，首先会校验流量的合法性，最简单的就是参数校验，然后校验订单/DSP的预设值，最终将该流量下发给哪些DSP；</li>
<li>DSP接收到本次流量时，根据流量中携带的相关属性决定是否参与竞价，如果流量合适，则返回参竞价格（或者dealId）及广告元素给ADX；</li>
<li>ADX接收各家DSP竞价信息，在经过一系列的有效性判断之后根据价格竞价排序，价高者得之，将获胜的广告信息下发给媒体，同时通知DSP其广告获胜了（这一步非必需，但建议有）；</li>
<li>媒体在收到广告信息后，对广告进行渲染展示。</li>
</ol>
<p>当产生用户行为时，需通过监测链接回传ADX和DSP相关行为数据，主要的行为曝光曝光、点击、下载、唤醒等。</p>
<p>针对通过监测链接回传行为数据，有C2S（Client to Server）和S2S（Serverto Server）两种模式，目前大多数客户都投放时都要求C2S的上报方式。</p>
<p>其中关于ADX涉及的各关键指标在上篇《商化广告角色大盘点》中的ADX部分有所提及，本文旨在探讨流量分发机制，对指标不做过多的解释，感兴趣的读者可移步阅读。</p>
<p>通过上述流量流转流程可以发现，广告流量主要在ADX侧进行转发，如果ADX对接了多家DSP，合理的流量分发机制可以提升填充率及ecpm，使得流量收益最大化。</p>
<h2 id="toc-2">二、Waterfall</h2>
<p>当ADX对接了多个DSP时，在请求不同的DSP时，是该串行请求还是该并行请求呢？这里面就涉及不同的策略。</p>
<p>首先来说说串行请求，即Waterfall。Waterfall，中文翻译为“瀑布流”，字面意思理解就是“从上往下流”，但“从上到下”这四个字该如何理解？</p>
<p>在广告行业中，Waterfall指的是“在无法实时评估每次流量的价值时，基于历史eCPM数据，从上到下请求DSP，分发流量”。这就是所说的广告串行请求。</p>
<p>通过一个实际例子来看Waterfall的使用场景。假设ADX对接了三个平台，三个平台的eCPM和填充料分别如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/19rJfUTV89nYxmI3wCgH.jpg" alt width="543" height="191" referrerpolicy="no-referrer"></p>
<p>假如有1000个广告请求，则有以下广告请求方案：</p>
<p><strong>方案1：全部请求DSP1</strong></p>
<p>收益 = 1000 * 20 / 1000 * 30% = 6</p>
<p><strong>方案2：全部请求DSP广告源</strong></p>
<p>收益 = 1000 * 15 / 1000 * 50% = 7.5</p>
<p><strong>方案3：全部请求DSP3</strong></p>
<p>收益 = 1000 * 25 / 1000 *20% = 5</p>
<p>从上述的三个方案来看，虽然方案的eCPM最低，但其填充率最高，最终的总收益最高。那是否说方案2是最佳方案，答案肯定是不是的，因为其只利用了50%的流量，剩下50%的流量被浪费了，于是引申出了方案4。</p>
<p><strong>方案4：先把1000个广告请求全部请求 DSP3 ，把未填充的部分请求 DSP1，最后未填充的部分请求DSP2，具体流量分发流程图如下。</strong></p>
<p>收益 = 1000 * 25 / 1000 * 20% + 800 * 20 / 1000 * 30%+560 *15/ 1000 *50% = 14</p>
<p>方案4最终的收益14元，填充率为72%，相对于前三种方案，既提升了收益，又提升了填充率。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/JTSkkTFUa62GAJ9TaUfX.png" alt width="486" height="533" referrerpolicy="no-referrer"></p>
<p>那既然看着收益和填充率都上去了，是不是采用Waterfall就可以解决流量分发问题了呢，现实总会让你啪啪打脸。Waterfall的方案主要存在以下几个问题点：</p>
<ul>
<li>Waterfall的核心点在于“历史eCPM的数据”，那么如何去衡量一个dsp的历史eCPM数据，这个历史是多久？</li>
<li>串行请求会增大广告展示耗时，平均请求一次至少在100ms以上，多次请求会造成前端展示延迟，用户体验感较差。由于不同广告位的环境不同，用户可接受程度也不一样，需要分广告位设置整体请求次数/超时时间。</li>
<li>由于Waterfall 的请求优先级是根据历史eCPM数据来决定优先级的，针对某次具体请求时，可能排在前面的DSP出价没有后面的出价高。这样一来就会错过排在后面的出价更高的DSP广告，流量利益没有获得最大化。</li>
<li>各个DSP的eCPM数据维护，由于季节性问题，eCPM的数值会发生变化，需要运营同学手动维护，成本较高。</li>
</ul>
<p>这里关于“历史数据的eCPM”，咱们展开讲一下：</p>
<p>这个历史是多久？这个问题是没有标准答案的！因为每个DSP的效果不一样。</p>
<p>我们唯一能够做的就是尽去预测每家的eCPM以及填充率，这可以通过历史数据去验证，也可以通过商务关系去了解，只有得到了正确稳定的数值，对我们来说才是真实可靠的。3天、7天、10天或者更久都是ok的，只要你认为这个数字是合理的，经得起推敲就可以。</p>
<p>对于新对接的DSP，由于其无历史数据积累，需要如何评估其eCPM值呢？</p>
<ul>
<li>可以通过商务运营渠道了解其eCPM和填充率情况；</li>
<li>可以针对新对接的DSP进行流量扶持，积累一定的数据后回归入正常的DSP进行排序。这个流量扶持的周期和样本数据，各家算法团队的要求不太一样，能满足自身业务即可。</li>
</ul>
<p>如果对于两个DSP，他们的eCPM和填充率都一样的情况下，如何排序呢？此时可以从其它纬度来评估，例如接口响应时长，素材质量等方面去考量。</p>
<h2 id="toc-3">三、Header Bidding</h2>
<p>既然Waterfall有诸多问题，那有木有其它替代方案？</p>
<p>读者肯定在想，如果每次竞价的时候，DSP都能实时返回本次出价，那么这样就不需要计算和维护“历史eCPM数据”了，在流量分发时，就可以并行的分发流量，在得到所有DSP的出价后，根据出价决定竞价成功者，这就是“Header Bidding”。</p>
<p>“Header Bidding”，中文翻译为“头部竞价”，字面意思理解就是“流量发给头部买家，头部媒体进行竞价，然后将获胜的底价作为底价去请求其它不支持实时竞价的DSP”。要想实现这个，首先得有如下几个前提：</p>
<ul>
<li>头部买家在返回广告素材时，需要同时返回出价，这样媒体／ADX才可以完成竞价；</li>
<li>非头部买家虽然不支持实时返回出价，但需要支持传入广告位底价，这样如果有广告返回，那么价格一定高于底价，对ADX和媒体来说收益最高。</li>
</ul>
<p>Header Bidding起源于国外，最初应用在PC上面。</p>
<p>DFP(Google Doubleclick For Publisher)，国外PC网站集成最多的广告平台，由于其垄断了PC广告，加上Google的Ad Exchange dynamitc bidding（感兴趣的朋友百度了解），对Publisher和其它DSP很不友好，因此AppNexus希望联手其它的ADX/DSP一起通过Header Bidding技术来撼动DFP的垄断地位。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/SWpbdCdOkZZ0lRzeU06L.png" alt width="414" height="522" referrerpolicy="no-referrer"></p>
<p>从上述的描述中可以发现，header bidding相对于Waterfall具备如下几处优点：</p>
<ul>
<li>公平竞价：所有DSP同时竞价，各自评估流量价值进行出价；</li>
<li>收益最大化：原先排在Waterfall底部的DSP可以通过提高出价来赢得广告展示机会。</li>
</ul>
<p>在国内，PC的发展已相对比较停滞不前，更大的潜力在移动端。因此更准确的说，国内的header bidding应该叫In-App bidding。</p>
<p>由于国内的In-App bidding起步较晚，目前只有几家头部媒体支持实时返回出价，因此在很长的一段时间内都会是headering bidding和Waterfall并存的方式，对于支持实时出价的媒体优先通过header bidding，然后将获胜的出价作为该广告位的底价去请求其它DSP，最终根据价格竞价。</p>
<h2 id="toc-4">四、总结</h2>
<p>其实无论是串行or并行，都只是解决问题的策略，核心目标只有一个“流量收益最大化”。</p>
<ul>
<li>站在媒体方的角度，当然是希望越多的媒体同时竞价；</li>
<li>站在DSP的维度，必然是希望流量先发给自家，自家挑选完之后再发给其他家，甚至可能是流量独占。</li>
</ul>
<p>当然现实中的环境错综复杂，不同的对接方式，也都会都会影响不同的策略，只有紧紧抓住“流量收益最大化”这个重点，兼顾多家利益，才能以不变应万变。</p>
<ul>
<li>电商节各大电商争夺市场的时候，流量预算充足，为了多拿预算，流量优先分发给电商DSP；</li>
<li>某些DSP的eCPM和填充率都还可以，但是就是素材比较low，偶尔还可能涉及到黑五类广告，或者说技术上存在小坑（比如网络延迟高），此时针对这些DSP需要做流量限制；</li>
<li>某些DSP虽然eCPM不高，但是填充率还行，比较适合做保底填充，需要给予一定比例的流量养着；</li>
<li>……</li>
</ul>
<p> </p>
<p>本文由 @包子 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4858523" data-author="653349" data-avatar="https://static.woshipm.com/APP_U_201803_20180319085922_2048.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            