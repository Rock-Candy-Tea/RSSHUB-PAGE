
---
title: '85万核心的世界最大AI芯片打破记录：要"杀死" GPU！'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220623/Sf247ce07-485f-4178-b1df-e3a0f901b7f4.jpg'
author: 快科技（原驱动之家）
comments: false
date: Thu, 23 Jun 2022 19:53:48 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220623/Sf247ce07-485f-4178-b1df-e3a0f901b7f4.jpg'
---

<div>   
<p>以造出世界上最大加速器芯片CS-2 Wafer Scale Engine闻名的公司Cerebras宣布，他们已经在利用“巨芯”进行人工智能训练上走出了重要的一步，<strong>训练出了单芯片上全世界最大的NLP（自然语言处理）AI模型。</strong></p>
<p>该模型具有20亿个参数，基于CS-2芯片进行训练。</p>
<p>这块全世界最大的加速器芯片采用7nm制程工艺，由一整块方形的晶圆刻蚀而成。</p>
<p>它的大小数百倍于主流芯片，具有15KW的功率，<strong><span style="color:#ff0000;">集成了2.6万亿个7nm晶体管，封装了850000个内核和40GB内存。</span></strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220623/f247ce07-485f-4178-b1df-e3a0f901b7f4.jpg" target="_blank"><img alt="85万核心的世界最大AI芯片打破记录：要" 杀死" gpu！" h="311" src="https://img1.mydrivers.com/img/20220623/Sf247ce07-485f-4178-b1df-e3a0f901b7f4.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
图1 CS-2 Wafer Scale Engine芯片</p>
<p><strong>单芯片训练AI大模型新纪录</strong></p>
<p>NLP模型的开发是人工智能中的一个重要领域。利用NLP模型，人工智能可以“理解”文字含义，并进行相应的动作。OpenAI的DALL.E模型就是一个典型的NLP模型。这个模型可以将使用者的输入的文字信息转化为图片输出。</p>
<p>比如当使用者输入“牛油果形状的扶手椅”后，AI就会自动生成若干与这句话对应的图像。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220623/3ea93e49-4127-4b49-a4e5-253c72d9ea21.jpg" target="_blank"><img alt="85万核心的世界最大AI芯片打破记录：要" 杀死" gpu！" h="293" src="https://img1.mydrivers.com/img/20220623/S3ea93e49-4127-4b49-a4e5-253c72d9ea21.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
图：AI接收信息后生成的“牛油果形状扶手椅”图片</p>
<p>不止于此，该模型还能够使AI理解物种、几何、历史时代等复杂的知识。</p>
<p>但要实现这一切并不容易，NLP模型的传统开发具有极高的算力成本和技术门槛。</p>
<p>实际上，如果只讨论数字，Cerebras开发的这一模型20亿的参数量在同行的衬托下，显得有些平平无奇。</p>
<p>前面提到的DALL.E模型具有120亿个参数，而目前最大的模型是DeepMind于去年年底推出的Gopher，具有2800亿个参数。</p>
<p>但除去惊人的数字外，Cerebras开发的NLP还有一个巨大的突破：它降低了NLP模型的开发难度。</p>
<p><strong>「巨芯」如何打败GPU？</strong></p>
<p>按照传统流程，开发NLP模型需要开发者将巨大的NLP模型切分若干个功能部分，并将他们的工作负载分散到成百上千个图形处理单元上。</p>
<p>数以千百计的图形处理单元对厂商来说意味着巨大的成本。</p>
<p>技术上的困难也同样使厂商们痛苦不堪。</p>
<p>切分模型是一个定制的问题，每个神经网络、每个GPU的规格、以及将他们连接（或互联）在一起的网络都是独一无二的，并且不能跨系统移植。</p>
<p>厂商必须在第一次训练前将这些因素统统考虑清楚。</p>
<p>这项工作极其复杂，有时候甚至需要几个月的时间才能完成。</p>
<p>Cerebras表示，这是NLP模型训练中“最痛苦的方面之一”，只有极少数公司拥有开发NLP所必要的资源和专业知识。对于人工智能行业中的其他公司而言，NLP的训练则太昂贵、太耗时且无法使用。</p>
<p><strong>但如果单个芯片就能够支持20亿个参数的模型，就意味着不需要使用海量的GPU分散训练模型的工作量。这可以为厂商节省数千个GPU的训练成本和相关的硬件、扩展要求，同时这也使厂商不必经历切分模型并将其工作负载分配给数千个GPU的痛苦。</strong></p>
<p>Cerebras也并未仅仅执拗于数字，评价一个模型的好坏，参数的数量并不是唯一标准。</p>
<p>比起希望诞生于“巨芯”上的模型“努力”，Cerebras更希望的是模型“聪明”。</p>
<p>之所以Cerebras能够在参数量上取得爆炸式增长，是因为利用了权重流技术。这项技术可以将计算和内存的占用量解耦，并允许将内存扩展到足以存储AI工作负载中增加的任何数量的参数。</p>
<p>由于这项突破，<strong>设置模型的时间从几个月减少到了几分钟</strong>，并且开发者在GPT-J和GPT-Neo等型号之间“只需几次按键”就可以完成切换。这让NLP的开发变得更加简单。</p>
<p>这使得NLP领域出现了新的变化。</p>
<p>正如Intersect360 Research 首席研究官 Dan Olds 对Cerebras取得成就的评价：“Cerebras 能够以具有成本效益、易于访问的方式将大型语言模型带给大众，这为人工智能开辟了一个激动人心的新时代。”</p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：上方文Q</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/xinpian.htm">芯片</a><a href="https://news.mydrivers.com/tag/rengongzhineng.htm">人工智能</a><a href="https://news.mydrivers.com/tag/xianka.htm">显卡</a>  </p>
        
</div>
            