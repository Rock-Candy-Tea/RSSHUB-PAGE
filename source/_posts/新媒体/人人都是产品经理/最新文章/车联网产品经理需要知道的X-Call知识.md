
---
title: '车联网产品经理需要知道的X-Call知识'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/vNuGCDIx26ihhHbwQ6Lf.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 13 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/vNuGCDIx26ihhHbwQ6Lf.jpg'
---

<div>   
<blockquote><p>编辑导语：X-Call知识对于车联网产品经理来说是十分基础的知识，本篇文章作者分享了有关X-Call的相关内容，重点介绍了其概念和服务流程等，感兴趣的一起来看一下吧，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5436963 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/vNuGCDIx26ihhHbwQ6Lf.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>X-Call是对E-Call、B-Call和 I-Call功能的一种合称。</p>
<p>就像V2X是V2P/V2V/V2I/V2N的合称、XMI是HMI/EMI的合称一样</p>
<p>X-Call是车联网的一项服务。在车企里，X-Call的工作是与TSP平台对接。</p>
<p>TSP平台已经是一个相对标准化的产品了，在架构上都会对X-Call功能做对应的预留，因此X-Call与TSP的对接工作也很快捷。车企，X-Call的产品设计工作也比较简单，在做TSP的时候搂草打兔子就做了。我们首先说下I-Call，然后重点介绍E-Call和B-Call。</p>
<h2 id="toc-1">一、I-call是什么</h2>
<p><b> I-Call是信息服务。</b>I-Call的产品形态就是网络电话。</p>
<p>在服务层面，I-Call提供人工客服人员对话，能做一些车辆的远程设置，也会有一些车主无聊时找客服闲聊。</p>
<p>I-Call一般是付费通话的。我有个前同事对就车主撩骚的需求动过脑子，想在车机上做一个美女陪聊的应用，按时收费。</p>
<p>如果大家想感受下车主通过I-Call聊骚，应该可以搜到相关视频。据一些不负责的谣言说，宝马和比亚迪的车主用这个功能比较多。谣言还说宝马客服说话态度好，比亚迪的女客服声音好听。</p>
<h2 id="toc-2">二、E-call是什么</h2>
<p><b>E-Call是汽车的紧急救援呼叫系统。</b></p>
<p>注意，E-Call只是“呼叫”，呼叫之后还需要救援资源去响应，即救援管理系统、救援团队、救援服务。</p>
<p>E-Call系统和服务是两个意思。</p>
<p>在救援服务体系里，针对不同的紧急状况，会有不同的救援服务。救援的类型有中国急救、医院、直升机救援、消防、公安、公路路政、水上救援、野外救援、道路救援。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="你需要知道的X-Call知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/3qU3UftuVF116uqMcMAc.jpeg" alt="你需要知道的X-Call知识" width="673" height="400" referrerpolicy="no-referrer"></p>
<p>如果车企定制，这些服务E-Call都能支持。但最主要的还是医院120。虽然E-Call系统是车联网的一个小产品，但对用户来说，是紧急状况下的一个生命机会。希望所有的车型都能装这个功能，哪怕用户永远用不上。</p>
<h2 id="toc-3">三、B-call是什么</h2>
<p><b>B-Call是非事故道路救援</b>服务内容有拖车、快修、搭电、加水、送油、换胎。</p>
<p>跟E-Call比起来，B-Call没有那么重要了。但一些车型不做E-Call却做B-Call，只因E-Call是成本项，B-Call有可能带来服务分成。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="你需要知道的X-Call知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/veqr0lYpfJ09XJMDcz9h.jpeg" alt="你需要知道的X-Call知识" width="669" height="295" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、E-call/B-call的服务流程</h2>
<p>E-Call/B-Call的救援服务车企都做不了。车企要对接第三方的救援系统和救援服务，是通过TSP平台去对接第三方。所以车企内的产品和研发团队做两项工作：车端到TSP的流程（逻辑）、TSP到第三方的对接。</p>
<p><b>供应商上的服务流程如下图：</b></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="你需要知道的X-Call知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/m1VnaPQ6EKVeOeJG1ath.jpeg" alt="你需要知道的X-Call知识" width="672" height="317" referrerpolicy="no-referrer"></p>
<p>紧急救助的时间每早一分钟，后期致残率、致死率均能降低5%，素有“白金十分钟”、“黄金一小时”的说法。所以在服务流程中，有几个关键指标：</p>
<p><b>整体时效：</b>我们以远盟（第三方E-Call服务商）的服务为例，看下整个E-Call的服务时效。从呼叫到救护车出发大概2~3分钟。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="你需要知道的X-Call知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/qJioqh6tPt9znLUlhJkW.jpeg" alt="你需要知道的X-Call知识" width="675" height="311" referrerpolicy="no-referrer"></p>
<p><b>派车能力：</b>救护车的呼叫是由E-Call的服务中心发出，并非车端直连120。E-Call的供应商会有特定资源和专属呼叫通道。这种资源是第三方服务的竞争力之一。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="你需要知道的X-Call知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/a02JOI3cr9gavQ6NcM37.jpeg" alt="你需要知道的X-Call知识" width="661" height="318" referrerpolicy="no-referrer"></p>
<p><b>精准PSAP：</b>PASP是公共安全应答点。是紧急医疗服务常见的一个专业术语。有国际标准，也有国内标准。国内标准中，公共安全应答点涉及到通信网编号、信号、接续、安全防范报警系统。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="你需要知道的X-Call知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/jXXMOl1NV7MTxo06C0KB.jpeg" alt="你需要知道的X-Call知识" width="669" height="334" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、E-call的服务价值</h2>
<p>根据欧盟的数据，欧盟E-Call的服务价值：每年可以挽救2500个生命，降低15%的重伤数量，同时节省40%的救援时间，减少的社会经济损失大约260亿欧元。</p>
<p>所以欧盟是第一个通过“自动紧急拨号服务”法案的。欧盟境内出售的所有私家车和轻型乘用车都必须安装E-Call系统。</p>
<h2 id="toc-6">六、E-call的产品逻辑</h2>
<p>E-Call的产品逻辑或者叫产品设计，是需要产品经理输出的。其核心的设计就是下面这种流程图，涉及多端联动，用泳道图的形式表现出来便可。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="你需要知道的X-Call知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/0G9muvzqcjPipSrEZHIO.jpeg" alt="你需要知道的X-Call知识" width="678" height="650" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">七、E-call的现状</h2>
<p>除了欧盟，俄罗斯、沙特、阿联酋也都出台了安装E-Call的强制法案。中国目前还在推进立法。</p>
<p>E-Call很细分，2021年全球市场规模大概十几亿美金。前装的主要供应商是慧翰，他们是做系统为主。还有一些做后装的，比如发掘科技。但做救援的公司主要还是远盟，他们拥有较多的资质和资源，能够做到很好的全时救援，目前也提供一款车联网SmartE-Call的系统+救援产品，非常有竞争力。</p>
<p>最后提下救援费用。B-Call的一些服务，一般保险公司都赠送了。另外这种非事故道路救援需求，用户用手机自己联系更加方便，所以从需求上B-Call应该淡出车联网，但从服务运营和做运营收入上考虑，B-Call还会存在。</p>
<p>E-Call这种紧急救援的费用，一般是救护车费用+医疗费。医疗费有车险，救护车的费用不超过xxx元/年，是服务商来支付。服务商会按照每车每年向车企收取一定的费用。</p>
<p> </p>
<p>本文由 @赛博七号 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5436614" data-author="728723" data-avatar="http://image.woshipm.com/wp-files/2022/05/yH587nP4SOM7rIk7be0M.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            