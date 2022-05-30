
---
title: '产品需求文档的写作(五) – 用例文档(UML用例图、流程图)'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/48.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 18 Apr 2014 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/48.jpg'
---

<div>   
<img data-action="zoom" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/48.jpg" referrerpolicy="no-referrer"><div>
<p><a href="http://image.woshipm.com/wp-files/2014/04/c2cec3fdfc0392450d3c25f78694a4c27c1e25b9.png">
</a></p><p><a href="http://image.woshipm.com/wp-files/2014/04/c2cec3fdfc0392450d3c25f78694a4c27c1e25b9.png">在产品和技术领域里都有UML的技能知识，而对于产品人员的UML则更多的是指用例图，也就是我所称呼的用户流程图。在讲PRD文档写作的</a><a title="梳理需求(产品结构图和用户流程图)" href="http://www.woshipm.com/?p=80078" target="_blank">第二篇文章</a>里，我提到了用户流程图的制作，实际上用户流程图是我在产品规则的初期对用例图的一种结构化的表达方式，由于以结构化的方式描述用例太抽象，缺少逻辑性表达，并且那篇文章更偏向于功能性用户流程，还不是实际意义上的用例，因此今天我补文一篇，细讲一下UML用例图和用例文档。</p>
<p>用例文档是由多个用例组成的一份文档，主要用于技术开发与测试使用，他是PRD中的重要辅助文档，用于讲解某个环节的功能逻辑，例如用户注册、活动报名等等功能都是需要用例辅助说明的。用例文档的写作时间在原型设计之后，通常和PRD文档同步撰写。</p>
<p>用例文档中有两个关联文件，分别是用例图和流程图。用例图是UML的一种类图表现方式，是从用户角度描述产品功能，并指出该用户在产品各功能中的操作权限。流程图是通过线框图形的方式描述产品功能的处理过程，主要是描述功能的执行顺序、分支和循环的逻辑。</p>
<p>写用户文档的常用软件是Word，其中用例图和流程图的制作软件常用的是Visio，当然也有用Axure RP软件制作的，例如下面的第三步流程图就是用Axure RP制作的。</p>
<p>一份完整的用例文档分别是由以下三点内容组成，其中第3点的“用例”是描述功能逻辑的部分，根据功能的多少决定有多少个用例。</p>
<p>用例文档的大概组成部分如下：<br>
1、修改记录：每次修改的备注记录，同PRD文档。<br>
2、角色介绍：描述参与系统中的各个角色<br>
3、用例：同下方步骤的第4步，其中第3步中的流程图是直接插入到第4步的流程图表格项中的。</p>
<p>用例文档的模板格式如同以上三点内容，通过Word文档绘制表格，在表格中撰写用例描述，表格的格式和样式参考以下示例图。</p>
<p>1、撰写用例文档的第一步是注明使用产品的各个角色(参与者)和角色说明(角色介绍)。（如下图）</p>
<p><img data-action="zoom" class="aligncenter" alt="角色" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2014/04/29a7e96467b69a9f5a93332e29e9b0de.jpg" referrerpolicy="no-referrer"></p>
<p>2、第二步是以用例图的方式注明角色在前后端的用例关系。（如下图）</p>
<p><img data-action="zoom" class="aligncenter" alt="会员中心UML用例图" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2014/04/34d5d911f0aacc6c3a70b4925cb35ca3.jpg" referrerpolicy="no-referrer"></p>
<p>3、第三步是以流程图的方式注明角色在各个功能环节的活动过程。（如下图：以活动报名为示例）</p>
<p><img data-action="zoom" class="aligncenter" alt="流程图" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2014/04/cff5497121104c2b8e0cb41ed2083a9b.jpg" referrerpolicy="no-referrer"></p>
<p>4、第四步则是以用例文档的方式将以上三步整合到一起，并撰写各个功能环节的用例描述。（如下图）</p>
<p><img data-action="zoom" class="aligncenter" alt="流程图" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2014/04/34d5d911f0aacc6c3a70b4925cb35ca31.jpg" referrerpolicy="no-referrer"></p>
<p>表格说明：<br>
4.1、用例名：此功能环节的名称<br>
4.2、用例编号：在此产品中该用例的编号<br>
4.3、行为角色：参与或操作(执行)该功能的角色<br>
4.4、简要说明：用最少的文字描述一下该用例的需求<br>
4.5、前置条件：参与或操作(执行)此功能的前提条件<br>
4.6、后置条件：执行完毕后的结果条件<br>
4.7、流程图：该功能的角色活动过程(处理过程)图（第三步中的图）</p>
<p>上面示范的用例描述相对简单，也是最常用和基本的用例描述内容，当然也有稍微复杂一点的用例文档，文档中会详细描述使用场景、事件流和信息字段，也有一些用例文档还会插入产品界面效果图。</p>
<p>使用场景主要描述行为角色在不同情况下使用产品时，根据情况或问题给出相应的系统反馈。事件流类似流程图，只不过是通过文字的方式描述角色的活动过程。信息字段主要是描述用例中所用到的数据字段。</p>
<p>这些更多的描述内容取决于个人的习惯，最终目的都是为了描述清晰产品逻辑，因此我的原则就是用越少的文字描述清晰越多的需求说明。（毕竟这些文档是产品开发中的执行文档，文字不在多，表达清晰即可。）</p>
<blockquote><p>产品需求文档(PRD)的写作：<br>
<a href="http://www.woshipm.com/?p=80054" target="_blank">产品需求文档(PRD)的写作方法</a>（文章的摘要介绍）<br>
<a href="http://www.woshipm.com/?p=80070" target="_blank">产品需求文档的写作(一) – 写前准备(信息结构图)</a><br>
<a href="http://www.woshipm.com/?p=80078" target="_blank">产品需求文档的写作(二) – 梳理需求(产品结构图和用户流程图)</a><br>
<a href="http://www.woshipm.com/?p=80086" target="_blank">产品需求文档的写作(三) – 原型设计(手绘原型,灰模原型,交互原型)</a><br>
<a href="http://www.woshipm.com/?p=80091" target="_blank">产品需求文档的写作(四) – 撰写文档(PRD文档)</a><br>
<a href="http://www.woshipm.com/?p=80096" target="_blank">产品需求文档的写作(五) – 用例文档(UML用例图、流程图)</a></p></blockquote>
</div>
<div>
<div>
<p>本文出自 产品经理 <a href="http://tangjie.me/" target="_blank">唐杰</a></p>
</div>
</div>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="80096" data-author="1499" data-avatar="https://static.woshipm.com/APP_U_202103_20210317232622_5217.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            