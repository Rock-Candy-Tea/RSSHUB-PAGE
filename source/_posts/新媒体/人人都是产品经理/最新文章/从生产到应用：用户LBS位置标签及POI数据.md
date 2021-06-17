
---
title: '从生产到应用：用户LBS位置标签及POI数据'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/xDSpTNEY6lZel2itkUfl.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 17 Jun 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/xDSpTNEY6lZel2itkUfl.jpg'
---

<div>   
<blockquote><p>编辑导语：如何设计与地理位置相关的用户标签，并使其投入产品应用中？其中，我们需要了解LBS服务——基于位置的服务，及POI数据。本篇文章里，作者系统介绍了LBS位置标签与POI数据，并给出了后续的产品化应用方案，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4719984 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/xDSpTNEY6lZel2itkUfl.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p><strong>“</strong>LBS相关的标签，是用户标签画像系统中的重要内容。<strong>”</strong></p>
<p>好久没有分享关于用户画像、用户标签相关的内容了。关于标签数据，之前有分享过《用户生命周期标签的计算》、《<a href="http://www.woshipm.com/pd/4233876.html">用户画像中的兴趣类标签如何计算</a>》。今天分享一下，关于LBS相关的标签内容。</p>
<h2 id="toc-1">一、什么是LBS</h2>
<p>讲LBS标签之前，先来看看LBS具体的一些内容吧。</p>
<h3>1. 什么是LBS服务</h3>
<p>LBS，即基于位置的服务（Location Based Services）。其实在日常我们的生活中，关于LBS的服务是非常常用的。</p>
<p>目前主要的LBS服务提供商，就是高德、百度、腾讯这些比较常见。其他绝大部分的APP应用，都是调用这些服务厂商提供的接口服务能力。</p>
<p>像我们常用的百度地图，基本产品逻辑就是围绕地理位置进行的。比如进行定位服务、路线规划、地点搜索、导航等等。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/xJDzCUizCpnVbLkAwJvs.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="737" height="340" referrerpolicy="no-referrer"></p>
<p>再比如，外卖软件中骑手配送路径的实时展示、配送员调度等。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/RmkVayLNXSk1qq38ZJ4G.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="737" height="397" referrerpolicy="no-referrer"></p>
<p>相关的应用很多，所有涉及到地理位置的相关功能，都属于LBS的范畴。</p>
<h3>2. LBS服务的类别</h3>
<p>总结下来，主要的LBS相关的服务可以总结为五类：地图服务、搜索服务、定位服务、路线规划服务、导航服务。</p>
<p><strong>1）地图服务</strong></p>
<p>这个比较好理解，地图是LBS服务的基础。无论是导航、还是看定位等，都是要基于地图进行呈现。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/PqM1UftupLeZJ9xuVF22.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="735" height="301" referrerpolicy="no-referrer"></p>
<p>虽然地图很常见了，但是其实关于地图呈现的内容是非常多的。比如，地图的风格、地图的覆盖物（比如交通轨道、河流等）的选择、聚合点的设置、地图中心位置的设置等等……</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/F6y7UCRbD6oq4uxvXm7Z.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="733" height="499" referrerpolicy="no-referrer"></p>
<p><strong>2）搜索服务</strong></p>
<p>所谓的搜索服务，即对地理位置相关的内容进行搜索。</p>
<p>基于不同的搜索对象，可以将搜索分为：POI数据搜索、地址数据搜索、行政区划数据搜索、公交数据搜索等等。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ei98bIQQVq5LdCKJn4wn.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="738" height="431" referrerpolicy="no-referrer"></p>
<p>比如上面，就是一个POI的搜索，这里能看到一个周边的围栏。关于POI和地址围栏，我们后面展开阐述。</p>
<p><strong>3）定位服务</strong></p>
<p>定位其实比较好理解，就是确定目前设备所处的位置。</p>
<p>通常，服务提供商提供的定位信息，是基于GPS、基站、WIFI等内容进行的混合定位。相对单模式定位，会更加精准。</p>
<p><strong>4）路线规划及导航</strong><strong>服务</strong></p>
<p>路线规划服务也比较好理解，就是提供两点之间的路线规划。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/7jNlpZMFulAmwyCGCZaa.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="737" height="386" referrerpolicy="no-referrer"></p>
<p>路线规划是导航的前提。根据交通方式的不同，可以有多种路线规划方式，比如驾车路线规划、公交路线规划、骑行路线规划、步行路线规划等。</p>
<h2 id="toc-2">二、POI和地理围栏</h2>
<p>上文中，我们提到了POI和地理围栏，由于比较重要，这里着重展开介绍一下。</p>
<h3>1. 什么是POI</h3>
<p>所谓的POI，即Point of Interest。怎么理解呢？比如，一个学校、一个小卖部、一个公交站、一个小区，都可以理解成一个POI。</p>
<p>想象一下，地图只是提供了一个底层的画板，只有在地图上叠加一个个的POI点位，地图的信息才能丰富起来，数据才有了价值。基于一个个的POI信息，可以进行更好的搜索、定位等等功能。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/QwsnRQAejSy31S61xtad.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="735" height="512" referrerpolicy="no-referrer"></p>
<p>比如上图，我们搜索“便利蜂”，出现的结果，就是和便利蜂相关的POI列表。</p>
<p>通常一个POI必备名称、地址（具体地址）、坐标（经纬度）、类别四个属性。至于其他属性，比如手机号、省市区等等，属于扩展信息。</p>
<h3>2. 示例：高德的POI数据</h3>
<p>我们看一下高德对外提供的POI接口数据。</p>
<p>首先是按照行政区域的POI数量：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/nPnDKkGuFtUGk1NHD58K.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="734" height="416" referrerpolicy="no-referrer"></p>
<p>我们可以看到，光北京市的POI数量就达到了347万个。</p>
<p>我们看具体POI列表，就比较容易理解了：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/DVxBLmqujQrKRKuFSqFr.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="738" height="475" referrerpolicy="no-referrer"></p>
<p>上面有机关单位、有汽车维修、有餐厅……这一个个具体的点，都是POI。每个POI除了列表中呈现的信息：名称、地址、电话、类别，还有啥信息呢？如下图：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ZSmU9npVUOTTfq21XS24.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="737" height="645" referrerpolicy="no-referrer"></p>
<p>看到了吧，信息是非常全的。还有街景信息，这里就不放截图了。</p>
<h3>3. 地理围栏</h3>
<p>上文讲了POI。注意，POI是一个【点】。和【点】对应的概念是【区域】，我们称之为“围栏”。</p>
<p>比如一个小区，虽然也可以在POI列表中呈现，可以用一个经纬度表示定位。但我们知道，小区其实是一个区域，而不只是一个点。这时，如果为了更加精准的分析服务，我们需要用到地理围栏。</p>
<p>所谓围栏，就是一个封闭的区域。例如下图：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/W2JsTBF9JaZEAGmjR1Iq.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="736" height="470" referrerpolicy="no-referrer"></p>
<p>百度地图中，用虚线将颐和园的边界进行了围起来。我们可以清楚地了解颐和园的区域范围，而不仅仅是一个POI点信息（其实颐和园也是有POI点的，上图中的序号位置1，就是颐和园的POI。如果只有POI而没有围栏，是不是效果差很多）。</p>
<p>当然，大部分地理信息其实是不需要围栏的。比如便利蜂，我们没必要知道便利蜂门店精准的区域，基本经纬度就可以了。但是比如行政区（例如北京市海淀区）、小区、学校等，还是有必要了解围栏信息的。</p>
<h2 id="toc-3">三、地理位置标签</h2>
<p>关于LBS和POI等相关的内容，上面也只是概括地讲了讲，细节层面确实内容非常丰富，值得大家深入研究研究。这里是时候进入我们的正题了，那就是地理位置相关的用户标签。</p>
<p>首先明确一下，我们这里的标签对象，是人：即给人打上和地理位置相关的标签。</p>
<h3>1. 需求背景</h3>
<p>我们在精准营销中，经常需要结合地理位置信息进行定向人群圈选，从而精准触达。</p>
<p>举个例子。我是一个线下便利店的店长，经营原浆啤酒。由于保质期短，且线下经营，潜在顾客基本就是店周边小区的人群，而且是爱喝啤酒的男顾客偏多。</p>
<p>因此，我需要营销触达的人群应该是【门店周边3KM居住小区】+【男顾客】+【爱喝啤酒】。</p>
<p>关于【男顾客】、【爱喝啤酒】应该是基础标签、偏好标签，可以参考《用户偏好标签计算》。至于【门店周边3KM小区】这个标签该如何获得呢？</p>
<p>对，这就需要地理位置信息相关的标签了。</p>
<h3>2. 具体计算逻辑</h3>
<p>如何获得这个标签呢？这里的关键是对用户的历史LBS位置进行建模、计算。</p>
<p>这个模型说复杂也并不复杂，但是细节内容比较多。通常来讲，基于用户APP上传的地理位置信息，我们会同时给用户打三个地理位置相关标签：用户的家的位置、用户的公司的位置、用户常出现的位置（除家和公司外）。</p>
<p>由于用户使用APP的时长、频次通常不是很长，我们一般需要稍微长一点的数据来计算用户的地理信息标签。一般可以考虑使用近30天数据（过长也不合适，时效性差且计算量大）来计算标签。而且由于用户的行为通常比较稳定，标签的更新时效也没必要每日更新，能每周更新一次标签就可以了。</p>
<p>具体的计算逻辑主要有这么几条：</p>
<ul>
<li>工作日时间有地理位置的日志超过*%就判定该位置是公司；</li>
<li>夜间有地理位置的日志超过*%就判定该位置是家；</li>
<li>其余时间经常出现的日志最高的位置判定为常去地。</li>
</ul>
<p>大的逻辑是这样，但是有很多细节计算逻辑，这里就不展开了。</p>
<h3>3. 地理位置数据表</h3>
<p>通过上面的计算，最终可以生成一张专门的用户地理位置相关的表。以用户ID为主键，分别三个字段：预测的家的位置、公司位置、常去地位置。</p>
<p>这里的原始地理位置，可以以经纬度进行存储。</p>
<h2 id="toc-4">四、LBS标签的产品应用</h2>
<p>地理位置标签数据计算好了，如何进行产品化应用呢？其实主要就是进行人群的圈选。具体的圈选方式，可以有以下几种方案。</p>
<h3>1. 基于具体POI+半径圈选</h3>
<p>比如，上面例子中，我们想基于便利店周边3KM进行人群圈选。</p>
<p>便利店作为圆心的POI，圈选该POI周边半径3KM以内的人群作为目标人群，即可满足诉求。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/32aB6JLg0oQdSJDJhIF4.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="734" height="489" referrerpolicy="no-referrer"></p>
<p>上面的截图是基于POI+距离半径来进行的人群圈选。【清华大学-北门】、【清华大学公寓】等都是一个个POI，下面的选择范围是距离半径。</p>
<h3>2. 基于地理围栏圈选</h3>
<p>第一种方式中，比较容易实现。但是有时想要圈选更具体精准的某个区域内的人群。</p>
<p>比如想圈选北京市西城区的全部潜在人群，或者某个学校的所有学生，这时就需要借助地理围栏进行圈选。</p>
<p>从数据层面，除了需要用户地理位置信息、POI信息外，还需要相关的地理围栏信息。通过地理围栏才能判断用户是否在围栏内。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/OtZIAzByLHRal7UqVMqn.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="738" height="244" referrerpolicy="no-referrer"></p>
<p>上面这个就是基于POI围栏进行圈选。</p>
<p>下面这个基于行政区进行的圈人，本质也是地理围栏。但是由于场景比较多，就进行了单独呈现。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/1Tv6cwwOqQadrsMZcMDs.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="743" height="134" referrerpolicy="no-referrer"></p>
<h3>3. 其他类型圈选</h3>
<p>本质上，所有的圈选都要么是基于POI+半径，要么是基于围栏。但是上面也看到了，有些特殊场景，从产品设计层面可以单独拿出来，比如行政区圈选。</p>
<p>另外，可以看一下下面的基于场景圈人。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Ve9UIioG5fwGrejb9keV.png" alt="标签数据——用户LBS位置标签及POI数据如何从生产到应用？" width="739" height="375" referrerpolicy="no-referrer"></p>
<p>这样可以对特定类型的人群进行圈选。</p>
<p>关于LBS、用户地理位置标签相关的内容就分享这些，欢迎大家继续关注~</p>
<p> </p>
<p>本文由 @首席数据科学家 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4717473" data-author="188996" data-avatar="http://image.woshipm.com/wp-files/2020/09/72OA3xPk4gH26z6hPOXB.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            