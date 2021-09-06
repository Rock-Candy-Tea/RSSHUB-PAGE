
---
title: 'B端产品OMS——从需求到落地'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/M1LLKT8hOcwVzxaDpXDB.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 06 Sep 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/M1LLKT8hOcwVzxaDpXDB.jpg'
---

<div>   
<blockquote><p>编辑导语：在供应链业务中，OMS设计是一个相对常见的模块，产品经理在进行OMS设计时，需要依据客户需求与开发阶段进行系统规划和设计优化。本篇文章里，作者结合自身经验，对OMS设计案例进行了整体复盘，不妨来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5125836 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/M1LLKT8hOcwVzxaDpXDB.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h3>前言</h3>
<p>从学校毕业到工作毕业二个月有余，加入一家传统企业担任B端产品经理。从此终于从之前的“纸上谈兵”过渡到“真枪实战”的阶段。</p>
<h2 id="toc-1">一、需求分析</h2>
<p>我们公司负责供应链业务。我接到的第一个项目是为集团内部做一个<strong>OMS（订单管理系统Order Management System）</strong>。</p>
<p>OMS的主要作用是方便我们的客户根据门店的不同需求在OMS上下单，再由OMS将需求推送到<strong>WMS（仓库管理系统Warehouse Management System）。</strong></p>
<p>WMS收到入库单后，会对入库的物料进行检查、清点并将物料放入对应的托盘并记录；收到出库单后，WMS根据出库物料的数量将物料检查完后通过TMS（运输管理系统Transportation Management System）将物料发到客户订单指定的地点。</p>
<p>以往的客户通过我们的业务人员在WMS下单，进行物料出入库的操作。但有的客户公司下有多个对应的门店。这些门店对物料的需求是不一样的，如果所有的门店都通过业务人员下单，无疑公司的管理和人力成本会急剧上升。</p>
<p>此外为了加强对客户的风险管控，出入库控制需要接入一套风控系统，因此业务流程演变由原来的客户——WMS转变成了客户——OMS——风控系统——WMS。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/ao7dfGwW9HMGstbcAnG2.jpg" alt width="745" height="88" referrerpolicy="no-referrer"></p>
<p>和业务方共同参会后，确定了OMS的需求。第一阶段OMS只做最核心的出库，加入风控功能。</p>
<p>梳理下来功能点有：</p>
<ol>
<li>出库询问；</li>
<li>出库结果推送；</li>
<li>在库明细查询；</li>
<li>取消订单。</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/M3ZUNjmdGEdh7zRrUYT9.png" alt width="354" height="230" referrerpolicy="no-referrer"></p>
<p>在四个功能点的基础上，我对四个需求的场景做了细化，细化后的功能需求有：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/nllfqLowGtm9coXUvior.png" alt width="746" height="535" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、整理产品需求文档</h2>
<p>由于我们的开发和我们并不在现场一起办公，因此第一阶段在满足一位客户业务需求的前提下，没有做的特别激进。</p>
<p>从客户角度看，主要实现了查看订单功能和订单取消功能。在内部产品需求文档中我填入了需求背景、专业术语、业务流程图、产品原型以及服务器信息等就完成了需求文档。</p>
<h3>1. 产品需求文档</h3>
<p>在内部产品需求文档模板中我填入了需求背景、专业术语、业务流程图、产品原型以及服务器信息等就完成了需求文档。</p>
<p>这里令我印象最深刻的就是产品原型的绘制与优化。一开始我的想法很天真也很简单。做了个订单列表页来让用户查看订单和取消订单，做一个订单上传页让用户上传订单。把两个功能按钮放在网页左侧，咔嚓完成！</p>
<p>第一版原型就画成了下图这样：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/0WB3jul5S4koxb9S3wTm.png" alt width="747" height="435" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2.1  订单列表页</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/n5yQrkzkMdnij0Ua4bjx.png" alt width="743" height="422" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2.2 订单详情页</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/kkeedqlM2kU4q6Gqg0sW.png" alt width="752" height="429" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2.3  出库单上传页</p>
<p>看上去客户想要的功能都实现了，在体验完阿里巴巴订单页后，我发现了三个优化的点：</p>
<ol>
<li>某些订单不允许被取消。例如用户已经取消的订单应该没有取消订单按钮或者取消订单按钮不可用。</li>
<li>没有筛选功能来迅速帮助用户找到需要的订单。</li>
<li>便捷查看用户关心的订单。</li>
</ol>
<p>这点绝对是用户的痛点，对于用户来说，未通过审核系统的订单是他们所最关心的，因此应该有一个按钮，让订单列表中展示的都是审核未通过的订单。此外已取消的订单也是用户所比较关心的订单，因此加入审核未通过和已取消按钮来放置这些用户较为关心的订单。</p>
<p>优化后的原型图如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/vh8Pv8nyWK1IbziG11LO.png" alt width="749" height="424" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2.4  优化后的订单列表页</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/hURRnsKPJOT5IXtHIHop.png" alt width="744" height="422" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2.5  审核未通过订单列表页</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/okWc5kZ4DbetKysqbo1V.png" alt width="745" height="421" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2.6  已取消订单列表页</p>
<h3>2. ER图</h3>
<p>看了杨堃老师的《决胜B端》，懂得对于一名B端产品经理来说，梳理业务中的实体关系图是很重要的一门功课。</p>
<p>在我参与的这个OMS中，实体关系图如下图所示。其中订单是用户下单的实体，抽取了订单中可能包含多种物料的共同属性。多个不同的订单明细确保了一个订单能支持多种物料出入库。一个订单对应WMS的多个容器，不同的容器跟装的物料明细也是一对多关系。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/yhcQL6nKoz5Nj80YNZci.jpg" alt width="376" height="317" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、总结</h2>
<p>输出原型和需求文档后，后续的主要工作内容就是对开发进度的把控，并为下一轮的开发迭代做准备。</p>
<p>作为一名产品新人，自己希望通过第一个项目来明白整个流程，让自己对供应链业务有个入门的理解。</p>
<p>下一步打算阅读更多的B端产品书籍和文章，体验优秀的B端产品设计，揣摩设计背后的深意来提升自己的产品操刀能力。后续也会写更多的文章来对项目进行复盘。</p>
<p> </p>
<p>本文由 @爱喝咖啡的猫 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5123546" data-author="838453" data-avatar="http://image.woshipm.com/wp-files/2021/09/5MkfyxM1pVAh3MlRHXw4.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            