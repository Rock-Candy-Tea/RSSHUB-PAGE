
---
title: 'B端产品降本增效的产品逻辑设计和业务实践'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/rea43mfXz6DOMqGFq6Ml.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 17 Jun 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/rea43mfXz6DOMqGFq6Ml.jpg'
---

<div>   
<blockquote><p>编辑导语：在互联网人口红利见顶的当下，如何利用B端产品推动企业降本增效？这需要我们进一步理解B端产品降本增效的产品逻辑。本篇文章里，作者分析了产品逻辑，并总结了电商发布系统降本增效的产品实践过程，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4720656 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/rea43mfXz6DOMqGFq6Ml.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>当前互联网人口红利基本结束，来自中国互联网络信息中心（CNNIC）数据表明：截止2020年底，国内网名规模接近10亿，2020年增长8540万，互联网普及率达70.4%，接近发达国家，已经接近上限。</p>
<p>现在全社会全行业都在向B端挖掘红利，那么B端如何帮助企业实现降本增效呢？本文提出降本增效的产品设计逻辑，并在后续文章中给出具体商业化案例实践，看看成熟企业是如何落地。</p>
<h2 id="toc-1">一、B端产品分类</h2>
<p>我们将B端产品分为企业自身使用的B端产品和平台商家使用的B端产品。</p>
<h3><strong>1. 企业自身使用的B端产品</strong></h3>
<ul>
<li>服务对象：企业自身；</li>
<li>产品形态：ERP、CRM等；</li>
<li>产品提供者：IBM、用友等；</li>
<li>部署方式：部署在所服务企业的私有云或者第三方云平台。</li>
</ul>
<h3>2. 平台商家使用的B端产品</h3>
<ul>
<li>服务对象：众多企业形成B端生态；</li>
<li>产品形态：阿里/美团商家系统等；</li>
<li>产品提供者：阿里/美团等；</li>
<li>部署方式：部署在互联网平台端。</li>
</ul>
<p>但是不管哪类B端产品，它们的使用对象都是企业，企业是市场竞争的主体，B端产品核心目标是为企业降本增效。</p>
<h2 id="toc-2">二、B端产品降本增效益的产品逻辑</h2>
<p>针对B端工作：重复、繁杂、专业的特点，我们降成本的产品设计逻辑要点和功能要求如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效的产品逻辑设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Ai4G56nfoKiqOJmpdvxG.png" alt="B端产品降本增效的产品逻辑设计" width="552" height="324" referrerpolicy="no-referrer"></p>
<p>针对B端产品管理对象众多、业务蕴含的数据价值大，增效益手段是挖掘大数据价值，其产品设计规范和功能支撑要求如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效的产品逻辑设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/T55thIAKdTfaE6LBzOUM.png" alt="B端产品降本增效的产品逻辑设计" width="552" height="313" referrerpolicy="no-referrer"></p>
<p>前面我们阐述了B端产品降本增效的产品设计原则，这里我们以电商平台的商品发布系统为例，来阐明上述原则是如何落地，满足千万级商家成熟业务的好用的产品系统。</p>
<p>商品发布系统由电商平台开发，解决商家在平台经营所需的商品信息发布，是商家系统重要组件，其业务流程如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/HJ9Cpd0adUWEvhwrk0yY.png" alt="B端产品降本增效产品设计原则的案例实践" width="551" height="410" referrerpolicy="no-referrer"></p>
<p>电商平台商品发布系统的产品架构如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/lgal9vv7J6Us9WmqeDrB.png" alt="B端产品降本增效产品设计原则的案例实践" width="550" height="141" referrerpolicy="no-referrer"></p>
<p>这需要后端大数据智能化和各类知识库支撑商品发布业务的准确、快速、低成本的B端商家诉求。</p>
<h2 id="toc-3">三、电商发布系统降成本产品实践</h2>
<h3>1. 降成本实践之一：重复繁杂工作自动化</h3>
<p><strong>1）问题呈现</strong></p>
<p>每天的商品上新、营销活动都需要大量修图抠图工作，电商平台和商家每年耗费大量美工投入到图片制作。</p>
<p><strong>2）业务案例</strong></p>
<p>2017年双11多达4亿张图片，如果靠设计师人工去设计制作，即使是业务熟练的设计师，也需要100位设计师不眠不休工作300年。</p>
<p><strong>3）产品方案</strong></p>
<p>利用系统来完成上述重复繁杂的工作，实现人机替代，比如阿里的鲁班设计系统每秒能做8000张图。这种通过深度学习海量素材，自动生成各种图片，不仅大大减少了人的工作量，而且系统设计的图片点击率增长一倍多，除了点评平台自己使用外，直接赋能给商家使用，大大降低了商家小二的工作量。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/P88VOj9Mn6ktLyVHYdju.png" alt="B端产品降本增效产品设计原则的案例实践" width="372" height="423" referrerpolicy="no-referrer"></p>
<h3>2. 降成本实践之二：专业工作智能化</h3>
<p><strong>1）问题呈现</strong></p>
<p>B端产品对商家小二专业知识要求高，商家的用人成本高。</p>
<p><strong>2）业务案例</strong></p>
<ul>
<li>类目选择环节，需要小二熟悉平台类目体系；</li>
<li>在属性填写环节，需要小二熟悉商品知识；</li>
<li>在图片制作环节，需要小二熟悉国家电商法律法规以及平台运营规范。</li>
</ul>
<p><strong>3）产品方案</strong></p>
<p>将专业知识内嵌的产品系统，减少对商家小二知识的依赖，通过智能化技术进行支撑。</p>
<p>比如类目选择环节的产品设计：将类目知识内嵌的系统，减少对小二知识的依赖。商品类目由系统自动通过商品标题计算得到，无需小二熟悉，而商品标题从商品包装说明书可以得到，无需小二对商品知识的依赖。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/5rB8NfzRRopPG1eaKMqP.png" alt="B端产品降本增效产品设计原则的案例实践" width="520" height="274" referrerpolicy="no-referrer"></p>
<p>在属性填写环节的产品设计：将属性知识内嵌的系统，小二仅仅需要确定商品类目，系统自动带出本类目的属性项和供小二选择的属性值，无需小二逐个了解复杂的商品知识。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/aHS0IHqvLjAFg65CjnEs.png" alt="B端产品降本增效产品设计原则的案例实践" width="251" height="386" referrerpolicy="no-referrer"></p>
<h3>3. 降成本实践之三：便捷自助学习专业知识</h3>
<p><strong>1）问题呈现</strong></p>
<p>有些专业知识比较生涩，或者小二对平台规则不熟悉。</p>
<p><strong>2）产品设计</strong></p>
<p>对商家小二不熟悉的知识或者规则，系统在页面给出指引或者视频图文在线交互学习，引导小二正确操作。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/3ghqhDBfMWzQsJBMj9pL.png" alt="B端产品降本增效产品设计原则的案例实践" width="529" height="224" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/MGrADQ8OtnxJIOHDFrly.png" alt="B端产品降本增效产品设计原则的案例实践" width="534" height="86" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/mRGmwpbKwu8BIYRRAzAQ.png" alt="B端产品降本增效产品设计原则的案例实践" width="523" height="449" referrerpolicy="no-referrer"></p>
<h3>4. 降成本实践之四：系统自检和容错</h3>
<p><strong>1）问题呈现</strong></p>
<ol>
<li>在智能化或在线学习前提下，小二仍旧可能发生错误操作，或者利益驱使下故意犯错。</li>
<li>系统知识不完备，可能是正确操作，但是系统认为是错误的。</li>
</ol>
<p><strong>2）产品设计</strong></p>
<ol>
<li>系统具备实时自检能力，根据事先内嵌的专业知识，实时校验并提示商家实时纠错。</li>
<li>如果商家坚持，系统具备容错能力，业务依旧可以进入后续环节，而不是在线等待。</li>
</ol>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/zXHnwuCtPkfUSJdH7J4v.png" alt="B端产品降本增效产品设计原则的案例实践" width="347" height="354" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、电商发布系统增效益产品实践</h2>
<h3>1. 增效益实践之一：规范化</h3>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/egi4XkjnJajrudmJ97nX.png" alt="B端产品降本增效产品设计原则的案例实践" width="525" height="250" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/QgC0JwN6TPpn7rg2FTLs.png" alt="B端产品降本增效产品设计原则的案例实践" width="524" height="350" referrerpolicy="no-referrer"></p>
<h3>2. 增效益实践之二：标准化</h3>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/YiEGMnAigekDEa0ExKpM.png" alt="B端产品降本增效产品设计原则的案例实践" width="523" height="267" referrerpolicy="no-referrer"></p>
<h3>3. 增效益实践之三：平台化</h3>
<p><strong>1）业务问题</strong></p>
<p>平台上大量商家做完全相同的工作，能否在商家间共享工作结果，节约社会资源。</p>
<p><strong>2）业务案例</strong></p>
<p>电商平台数以百计商家在卖相同的苹果手机，这些商家发布商品都需要填写商品的参数信息（多达上百项），如苹果11系列256G黑色手机，参数信息包括：</p>
<ul>
<li>品牌：苹果；</li>
<li>系列：11；</li>
<li>内存：256G；</li>
<li>颜色：黑色；</li>
<li>重量：XXX；</li>
<li>屏幕：XXX；</li>
<li>摄像：XXX；</li>
<li>电池：XXX；</li>
<li>网络：XXX；</li>
<li>……</li>
</ul>
<p>百余项都需要填写。</p>
<p><strong>3）产品方案</strong></p>
<p><strong>平台化共享思路</strong></p>
<p>平台牵头建设产品信息库，商家共享这份产品信息库，不仅大大减少商家录入成本，提升商家工作效率，而且商品的数据一致性得到保障，更能发挥数据的价值。</p>
<p>商品描述=商品的产品信息+商品的销售信息。</p>
<p>商品的产品信息=商品类目+品牌+属性，产品信息是商品客观描述，与商家无关。</p>
<p>商品的销售信息=商品标题+卖点+营促销+图片+详情，商家描述如何售卖商品，比如满千减百。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/QPq4dcStHxsdpEbQk8qN.png" alt="B端产品降本增效产品设计原则的案例实践" width="524" height="190" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/QayI7CBvyOsjNntgTMSy.png" alt="B端产品降本增效产品设计原则的案例实践" width="525" height="287" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品降本增效产品设计原则的案例实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/wDhJbmnn8ksPGnDiaLCx.png" alt="B端产品降本增效产品设计原则的案例实践" width="522" height="261" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、总结</h2>
<p>说明，上述案例仅仅是为了说明B端产品降本增效产品逻辑设计落地，本设计原则对大多数B端产品都使用。对于产品经理而言，B端产品经理是企业降本增效的“引擎”，主导系统架构设计，能否按照降本增效背后本质的产品逻辑，设计出具备人机替代、智能化、规范化、标准化和平台化系统功能，决定降本增效能否实现。</p>
<p>同时在业务流程中，我们需要设计好交互学习环节来降低工作人员的专业知识的学习成本，同时建立检错容错能力确保业务顺利快速展开。</p>
<h2 id="toc-6">六、后记</h2>
<p>当前行业进入下半场，每个企业都在进行数智化转型升级，并着手挖掘存量用户的价值，撮合商品与消费者之间供需匹配是价值变现的主要方法，而搜索推荐就是实现供需匹配的主要机制。</p>
<p>目前国内只有少数头部的互联网企业具备成熟完备的人才队伍，其他企业面临专业人才零散、知识结构不足的窘境，社会巨大的人才需求与社会高质量人才供给严重不足的矛盾，制约了企业数智化转型升级，也制约了从业者职业发展。</p>
<p>鉴于搜索推荐商品专业性特点，公开成体系资料相对少，资料难度深浅不一，难以满足企业和职场人士的迫切需求，本人过去10年专注电商，深度参与并主导搭建两大电商平台的搜索推荐流量分发及商品管理系统，熟悉电商平台的策略、产品、运营、数据和研发各环节。现将上述知识总结提炼成打造实战型电商搜索体系，打造实战型电商推荐体系，打造实战型电商商品管理体系，汇集成PPT，致力于专业知识的普及推广，为行业进步输出一份力量，内容将陆续发布。</p>
<p>历史文章系列：</p>
<ul>
<li><a href="http://www.woshipm.com/it/4707841.html">拼多多与阿里的技术差距大吗？</a></li>
<li><a href="http://www.woshipm.com/operate/4686389.html" target="_blank" rel="noopener">电商搜索流量分配策略未来进化方向探讨</a></li>
<li><a href="http://www.woshipm.com/pd/4675268.html" target="_blank" rel="noopener">从体系构建角度看电商搜索</a></li>
<li><a href="http://www.woshipm.com/operate/4654468.html" target="_blank" rel="noopener">电商商品分层分级及具体操盘策略</a></li>
<li><a href="http://www.woshipm.com/operate/4642670.html" target="_blank" rel="noopener">电商搜索流量分配的商业化策略</a></li>
<li><a href="http://www.woshipm.com/it/4637646.html" target="_blank" rel="noopener">电商搜索流量分配的市场宏观调控策略</a></li>
<li><a href="http://www.woshipm.com/it/4598818.html" target="_blank" rel="noopener">提升电商搜索GMV产品策略之浅见（一）前端产品篇</a></li>
<li><a href="http://www.woshipm.com/it/4608143.html" target="_blank" rel="noopener">提升电商搜索GMV产品策略之浅见（二）召回排序篇</a></li>
<li><a href="http://www.woshipm.com/pd/4610856.html" target="_blank" rel="noopener">提升电商搜索GMV产品策略之浅见（三）场景和动线篇</a></li>
<li><a href="http://www.woshipm.com/operate/4613828.html" target="_blank" rel="noopener">搜索联想词产品实践系列之浅见（一）定位-评估和召回篇</a></li>
<li><a href="http://www.woshipm.com/it/4614452.html" target="_blank" rel="noopener">搜索联想词产品实践系列之浅见（二）排序-场景动线篇</a></li>
</ul>
<p> </p>
<p>作者：毛新年，公众号：资深电商专家毛新年</p>
<p>本文由 @产品专家毛新年 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4707853" data-author="1147851" data-avatar="http://image.woshipm.com/wp-files/2021/05/JPmu23XFoVbPpGYcEVoC.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            