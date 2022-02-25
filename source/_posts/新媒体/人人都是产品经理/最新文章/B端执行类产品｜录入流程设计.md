
---
title: 'B端执行类产品｜录入流程设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/DSWF88n1dDDpDq9SsihB.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 25 Feb 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/DSWF88n1dDDpDq9SsihB.jpg'
---

<div>   
<blockquote><p>编辑导语：在B端产品中，用户常常会使用信息录入功能，然而有时用户录入的数据较为复杂，此时系统若不能优化录入流程和后续的信息处理，业务的最终处理效率则大概率会被拉低。本篇文章里，作者总结了B端产品中录入流程的相应设计策略，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5331078 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/DSWF88n1dDDpDq9SsihB.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>执行类产品中，信息录入是用户工作中最常见的场景之一，用户按照要求录入信息提交给系统，系统整合信息以完成执行结果。</p>
<p>页面中，由属性控件和数据容器组成的实体是整个录入流程的载体，录入流程设计的关键是<strong>【信息编排】</strong>与<strong>【高封装度表单】</strong>。<strong>帮助用户明确当前页面任务，快速查找和定位修改目标，轻松准确地理解表单项含义及生效后果，同时简化填写流程，确保用户准确、轻松、快速地完成任务。</strong></p>
<p><strong>【信息编排】</strong>：将大型、复杂任务拆解为多个部分，并按照相关性分组，减轻用户输入负担。每部分内容单独处理，但最终一起完成提交。通过适当的任务分割，可以降低用户出错率。</p>
<p><strong>【高封装度表单】</strong>：根据表单的结构关系判断、寻找共性的内容，将它们封装为一个卡片，也可以封装成一个组。主要的目的就是减少用户认知负担，提升操作/使用效率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/cwxNcjE5Ys6nlHD6FGy9.png" alt width="701" height="331" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/tj9UGG0Ej1EQgEqeVrrn.png" alt width="705" height="421" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">案例：B端-某仓网布局项目</h2>
<p>项目背景：物流侧因某些原因需经常搬仓，规划侧需知道搬仓对拆单率及耗材费用等影响。因此，上线搬仓模拟系统，辅助业务在线上模拟与评估搬仓方案，通过系统自动化测算搬仓前后的各项指标，决策出最优的搬仓方案。</p>
<p>用户痛点：搬仓模拟流程复杂，录入数据繁多，用户线上录入搬仓物品的效率低下。</p>
<p><strong>设计目标：调研整理用户工作流程，通过整合任务场景，设计逻辑清晰操作简单的录入流程，优化搬仓路径下各物品集的操作及展示。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/OXLyZKcl4BYIJm3JL172.png" alt width="708" height="552" referrerpolicy="no-referrer"></p>
<h3>1. 信息编排</h3>
<p>区分信息间层级关系-使用格式塔心理原则对项目、任务与物品集进行层级区分展示。整体逻辑为项目包含任务，任务包含物品集，一个完整的项目包含基本信息+任务。再根据信息关联性将每个信息点集合成信息组。并根据眼动原理设计最优浏览路径（F型动线）。</p>
<p><strong>项目=A基本信息</strong>（项目名称与模拟时间）<strong>+B任务</strong>（最多5个任务，其中任务包含搬仓路径与搬仓物品；每个任务最多包含5个物品集，物品集包含搬仓物品维度与温层属性）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Gyfz8kalgHegQVZWUDA3.png" alt width="702" height="196" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/KrYKAAYByjcsYf0DI0gQ.png" alt width="713" height="515" referrerpolicy="no-referrer"></p>
<h3>2. 高封装度表单</h3>
<p>根据搬仓逻辑及表单结构关系（项目>任务>物品集）及每个结构下添加的内容的一致性（每个任务必须填写搬仓路径及物品集，每个物品集必须选择物品集维度及温层），将它们封装为一个卡片，每个卡片内的结构内容封装成一个组。</p>
<p>除了嵌套逻辑，高封装度的表单还要注意组件选取，高封装度表单要保持组件选择及样式的一致性，整个封装组件要有可复用性，整个录入流程从视觉层到交互层给用户一致的体验，以此来减少用户认知负担，提升操作效率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/04wonQTIpx7weSEhKlk5.png" alt width="703" height="648" referrerpolicy="no-referrer"></p>
<h3>最后</h3>
<p>以上就是「录入流程设计」的全部内容啦～</p>
<p>后续会为大家分享<strong>关键信息密度提升设计</strong>、<strong>场景化设计</strong>等一系列的设计方法，希望能给正在从事或准备入局B端的的小伙伴带来启发，也希望跟大家一起探讨更多的B端设计方法。</p>
<p> </p>
<p>本文由 @自转一周的鹿 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5329589" data-author="1001792" data-avatar="http://image.woshipm.com/wp-files/2022/02/SADJQo8Sc1yuZkeItS7W.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            