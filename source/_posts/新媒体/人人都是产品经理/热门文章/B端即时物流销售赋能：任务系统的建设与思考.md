
---
title: 'B端即时物流销售赋能：任务系统的建设与思考'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/xjfbXZFM7Q6P5jsQFYJ9.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 25 Apr 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/xjfbXZFM7Q6P5jsQFYJ9.jpg'
---

<div>   
<blockquote><p>编辑导语：如今即时物流已经深入到我们的生活当中，为了实现销售过程与销售结果的可视化的管理需求，便需要通过任务系统来实现，具体要怎么做呢？一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5409999" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/xjfbXZFM7Q6P5jsQFYJ9.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>物流即时配送业务，是连接客户与骑士即时配送服务的供需撮合。</p>
<h2 id="toc-1">一、业务场景</h2>
<p>即时物流配送已经深入到我们日常生活中：</p>
<ul>
<li>我们在xx平台下单购买了一杯奶茶，商家接到订单后制作完成，骑手接到货品送到我们手中</li>
<li>我们在xx超市买了几个鸡蛋，骑士帮我们把鸡蛋送到我们手中</li>
</ul>
<p>在这当中，骑手的配送服务就是即时物流配送，通过上述业务场景，我们画出用户交易模型：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端即时物流销售赋能：任务系统的建设与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/jJEEyZROHLfzDUc4qS2m.jpeg" alt="B端即时物流销售赋能：任务系统的建设与思考" width="790" height="436" referrerpolicy="no-referrer"></p>
<p>对于即时物流平台而言，在上述的交易模型中，目标是撮合公司运力与商家订单，实现骑士运力与物流订单的平衡。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端即时物流销售赋能：任务系统的建设与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/dRS1ZdHPQRMfLXgjZY7v.jpeg" alt="B端即时物流销售赋能：任务系统的建设与思考" width="795" height="265" referrerpolicy="no-referrer"></p>
<p>然而每个即时物流平台的运力供给是有限的，根据愈军老师《产品方法轮》中的供需定律，为实现预期收入最大化这个目标，我们从以下三个角度入手：</p>
<ul>
<li>增加客户数量</li>
<li>提升高质量客户占比</li>
<li>提升运营人员服务效率，即“人效”</li>
</ul>
<h2 id="toc-2">二、行动</h2>
<p>基于公司业务用户分类，分析各用户目标与需求：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/BCPkS3KQT7X2VNeF4Twk.png" alt width="973" height="361" referrerpolicy="no-referrer"></p>
<p>E-R图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端即时物流销售赋能：任务系统的建设与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/XFh2kHCykqeRLbJMuTL9.jpeg" alt="B端即时物流销售赋能：任务系统的建设与思考" width="957" height="457" referrerpolicy="no-referrer"></p>
<p>结合销售的工作方式，同时实现销售过程与销售结果的可视化的管理需求，因此，通过任务系统来实现。</p>
<h3>1. 任务系统方案</h3>
<p>根据任务系统用户及使用场景，为实现任务系统的数据闭环，将其拆分为以下三个部分：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端即时物流销售赋能：任务系统的建设与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/F8ppliW3vjcJjrWODmjJ.jpeg" alt="B端即时物流销售赋能：任务系统的建设与思考" width="896" height="251" referrerpolicy="no-referrer"></p>
<p>任务主体主要包含三个部分：</p>
<ul>
<li>任务基本信息：主要是对任务的信息介绍，如：任务的名称、任务的执行期间、任务下发时间、任务说明等</li>
<li>任务对象：任务的目标对象，如：商家、企业等</li>
<li>任务跟进人：任务的执行人，如：一线商家拓展人员、商家运营等</li>
</ul>
<p><strong>1）任务下发</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端即时物流销售赋能：任务系统的建设与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/DIOwCI5MdKZgAVh4XC3c.jpeg" alt="B端即时物流销售赋能：任务系统的建设与思考" width="723" height="470" referrerpolicy="no-referrer"></p>
<p>由销售运营创建任务，设定任务基本信息、任务对象、任务跟进人，跟进人本次任务目标、完成本次任务的动作抓手。</p>
<p>关注点：</p>
<ul>
<li>任务对象分配任务跟进人：业务中可能按照商家品类、商家区域分发给对应的销售</li>
<li>任务目标：针对商家的任务目标，一般是完成签约、增加充值、提升订单数量</li>
<li>动作抓手：完成不同的目标，可提供的抓手也不一样，如：</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/d1ORH47EPKAwbIcTtdn9.png" alt width="543" height="338" referrerpolicy="no-referrer"></p>
<p><strong>2）任务跟进</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端即时物流销售赋能：任务系统的建设与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/RDFXiIYXKatg1lYvYSE8.jpeg" alt="B端即时物流销售赋能：任务系统的建设与思考" width="710" height="451" referrerpolicy="no-referrer"></p>
<p>任务下发完成后，在跟进期间的任务需要一线销售人员及时处理待办的任务。</p>
<p>一线销售人员的待办任务，其关心的几个要素展示：</p>
<ul>
<li>任务的时效性：可跟进的时间，如：周一到周日的时间范围要完成</li>
<li>任务的目标：是为了完成签约，还是完成发单，或者是收集商户使用反馈等</li>
<li>任务的对象：需要跟进的任务对象基本信息，商家名称、品类、地址（距离）、发单情况、完单情况、当前价格及其他要求等</li>
<li>动作抓手：提供完成目标的动作抓手有哪些，如拜访需要收集的信息，可以对商家发券等</li>
</ul>
<p>说明：</p>
<ul>
<li>针对一个商家可能存在多个问题或目标，所以存在一个商家在同期下发多个任务的场景。此时需要提供一线销售人员查看商家的视角来跟进任务，避免一个销售完成了该对象充值的任务，没有完成该对象其他的任务，导致销售再次联系该商家。</li>
</ul>
<p><strong>3）任务查</strong><strong>看</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端即时物流销售赋能：任务系统的建设与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/e4KfzVBBHOk7D1eGqe4X.jpeg" alt="B端即时物流销售赋能：任务系统的建设与思考" width="751" height="316" referrerpolicy="no-referrer"></p>
<p>在任务进行中或任务结束后，销售管理者可随时查看销售完成的过程与结果数据，并根据过程与结果数据进行后续任务策略调整。</p>
<ul>
<li>任务对象维度：关注任务对象的问题是否解决（结果数据），如何解决的（过程数据），那种解决的结果更好（动作抓手），没完成的原因是啥（拜访数据），没完成的任务对象催促完成或调整跟进人</li>
<li>销售维度：关注这些销售的任务对象，有多少个任务对象，哪些完成了，哪些没完成，对比销售间的差距</li>
</ul>
<h3>2. 任务系统的整体结构</h3>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端即时物流销售赋能：任务系统的建设与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/nhudkKsFReCxaN77NFzf.jpeg" alt="B端即时物流销售赋能：任务系统的建设与思考" width="769" height="740" referrerpolicy="no-referrer"></p>
<p><strong>1）通用能力建设</strong></p>
<p>在上述内容的基础上，为将任务系统建设的更通用，支持各种业务场景；将任务系统按照下图进行抽象，形成中台化的组件能力。</p>
<ul>
<li>任务类型：不同的场景配置任务对象、下发前动作、分配规则、跟进人动作、目标组件。如：风险商户跟进任务、流失商户跟进任务、商机拓展任务等。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端即时物流销售赋能：任务系统的建设与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/HQmZpCdNxEO1XPh6waV3.png" alt="B端即时物流销售赋能：任务系统的建设与思考" width="893" height="563" referrerpolicy="no-referrer"></p>
<p><strong>2）扩展</strong></p>
<ul>
<li>目标对象若是商家，可自建或接入商家画像系统，定时周期圈选目标商家，形成销售过程自动化的能力，能够实时发现新增的风险商户与流失商户，及时触达销售进行跟进该部分商家。</li>
<li>目标对象若是骑士，接入骑士画像系统，通过实时发现问题骑士或目标骑士，并实时下发给骑士跟进人。</li>
<li>任务系统可支持各种实体对象，对其进行业务触达，并实现过程与结果的可视化。如：发券、营销等业务。</li>
</ul>
<h2 id="toc-3">三、后续思考扩展</h2>
<ol>
<li>订单与运单的匹配模式：派单、抢单</li>
<li>任务完成后的绩效奖金归属</li>
</ol>
<p> </p>
<p>本文由 @瑟福 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5409694" data-author="300550" data-avatar="https://static.woshipm.com/APP_U_202204_20220424174618_4608.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            