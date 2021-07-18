
---
title: 'AI产品经理如何做好数据准备工作'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/f549U8Z0mOGvZ9dv8Tn6.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 18 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/f549U8Z0mOGvZ9dv8Tn6.jpg'
---

<div>   
<blockquote><p>编辑导语：在所有产品类型中，AI产品是市场上较为吃香的。在AI产品领域，数据的准备工作是开始正式工作之前同样重要的一部分。那么，该如何做好数据准备工作呢？</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4886672 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/f549U8Z0mOGvZ9dv8Tn6.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>所有的产品类型中，估计AI产品是最吃数据的了，要训练模型必须喂养大量的数据，2020 年 6 月 9 日，一款颅内肿瘤核磁共振影像辅助诊断软件获得了中国药监局审批，拿到了影像辅助诊断领域的首张 III 类医疗器械证。</p>
<p>这套人工智能软件对脑肿瘤的诊断准确率超过 90%，对其中常见类型的诊断准确率达到 96%。训练这款软件的算法模型喂养了上百万份影像病例，海量数据、强大算力以及高分辨率，让人工智能归纳出来的一套新经验，使得它在影像诊断领域取得突破的基础。</p>
<p>可以这么说，在AI产品领域，数据、算法、算力三分天下，同样重要，数据的准备工作是开始产品设计和开发的必要的前期工作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/urN42joBIZaKhLQ5i8JN.png" alt width="745" height="277" referrerpolicy="no-referrer"></p>
<p>数据准备工作主要包括两个部分，第一是数据收集，第二是数据清洗。</p>
<h2 id="toc-1">一、数据收集</h2>
<p>数据收集顾名思义，就是收集训练所需的数据，比如说，我要做一个人脸识别的模型，那么肯定是要收集人脸数据，我要做个对话机器人系统，肯定要收集语料数据，我要做个有无佩戴安全帽识别，肯定要收集人带安全帽的数据。</p>
<p>我要做个宠物狗的品类识别模型，就要收集各种狗的图像数据，并分类存储。</p>
<p>数据收集简而言之，就是把数据分类存储好的过程，就像是我们做法，先去买菜的过程，并把菜分类存储好的过程。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/qqGoY41hG9Q24SjI8rbN.png" alt width="737" height="281" referrerpolicy="no-referrer"></p>
<p>目前，数据收集主要有三个来源，分别是数据服务商采购、公开网络收集、内部数据。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Wl0olDOol030smsEeTUI.png" alt width="760" height="196" referrerpolicy="no-referrer"></p>
<p>数据提供商提供的数据一般质量都比较好，数据比较大。可以直接拿来做模型训练工作。只不过这类数据一般价格比较高。</p>
<p>而且这类数据的类型一遍是通用型，对于一些小品类，垂直领域的的数据服务商一般没有。例如下面这些，是一家外部提供商提供的数据。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/iXf2RkKKR6Ior3KFsbkR.png" alt width="629" height="2507" referrerpolicy="no-referrer"></p>
<p>网络公开的数据比较好理解，就比如训练提问意图，需要大量的提问意图的短句，这时候可以从知乎爬取。因为知乎是个问答平台。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/y6U4Dm0Z0uogqs7kwxMM.png" alt width="569" height="512" referrerpolicy="no-referrer"></p>
<p>第三种内部数据，也比较好理解，如果有内部数据肯定是先用内部数据，他的获取成本最低，还有就是一些小众垂直领域，外部无法获取也只能从内部获取。</p>
<p>例如疫情初期，北京肿瘤医院新冠肺炎智能识别是基于5000多个病例的 CT 影像样本数据，学习训练样本的病灶纹理，研发了全新的AI算法模型，可在20秒内快速完成新冠肺炎影像的分析，分析结果准确率达96%。这些CT影像就属于内部数据。</p>
<h2 id="toc-2">二、数据清洗</h2>
<p>数据收集完成之后还不能直接拿来用，需要做数据清洗，把这些数据变成可用的数据。这就好比从菜市场买完菜之后做洗菜和切菜的过程。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Z34KQVjFIMpxqFzKaeDF.png" alt width="918" height="373" referrerpolicy="no-referrer"></p>
<p>数据清洗主要是清洗三类数据：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/IzgK4qDsryL700BOGmtF.png" alt width="649" height="404" referrerpolicy="no-referrer"></p>
<p>数据缺失解决办法大体分为两种，第一种是直接删除，第二种是做填补。</p>
<p>数据格式不统一比较好解决，直接做归一化处理就好。</p>
<p>存在异常值的情况，只需要找到异常值，并剔除掉就好。针对不同的数据的异常值找到方法也不尽相同。例如某学校3万人体检，手工录入每个人体重，可以用3σ定律检验可找出录入错误数据。</p>
<h2 id="toc-3">三、总结</h2>
<p>数据收集和数据清洗工作在整个建模过程中很重要，数据的好坏直接影响最后模型的准确性。但是数据收集和数据清洗是个苦活，过程繁琐并且技术含量不高，需要AI产品经理和算法工程师一起完成，这块会花费比较多的时间，一定要有耐心和细心。</p>
<h3>#专栏作家#</h3>
<p>老张，人人都是产品经理专栏作家。AI产品经理，专注于自然语言处理和图像识别领域。现智能保险创业公司合伙人，希望与人工智能领域创业者多多交流。</p>
<p>本文原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4498201" data-author="291942" data-avatar="https://static.woshipm.com/WX_U_201707_20170711143731_7712.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            