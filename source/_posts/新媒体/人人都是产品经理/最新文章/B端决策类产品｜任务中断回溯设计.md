
---
title: 'B端决策类产品｜任务中断回溯设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/7H7mRKLf6U3IWHLV2rgj.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 24 Feb 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/7H7mRKLf6U3IWHLV2rgj.jpg'
---

<div>   
<blockquote><p>编辑导语：如何设计好任务回溯场景，让用户在需要反复进入任务处理流程的情况下，可以获得更加完善的用户体验，并提高用户的业务处理效率？本篇文章里，作者就B端决策类产品中的任务中断回溯设计策略做了解读，一起来看。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5330825 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/7H7mRKLf6U3IWHLV2rgj.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在B端产品线中，特别是在决策类产品中，经常会出现需<strong>要决策的信息量多</strong>、<strong>任务处理周期长而造成任务（主动or被动）中断，用户反复多次进入任务处理流程的情况</strong>。</p>
<p>针对在较长时间段内任务中断回溯的情景场景，从用户心理和业务场景出发设计快速定位任务进度的【<strong>状态标签</strong>】，在任务列表查询区提供【<strong>标签类别筛选</strong>】以及在任务处理详情页面【<strong>同步状态标签及关键信息</strong>】以保持视觉连贯和逻辑映射，从而增强用户定位能力，消灭负担及提高决策效率。</p>
<h2 id="toc-1">一、B端决策类产品流程图</h2>
<p>在这里，简单概括一下决策类产品的整体流程，用户通过逐条或批量处理待决策的任务最终完成所有任务的决策。在此过程中或主动或被动的会出现任务中断的情况，那么用户想要返回任务清单查找未完成或者处理中的任务就需要耗费时间和精力费力查找，这必然导致工作效率的降低。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/7V2PZH6Q6h48AKivi9AF.png" alt width="787" height="338" referrerpolicy="no-referrer"></p>
<p>通过任务中断回溯这一设计手段，用户能够快速定位、精确查找，提高工作效率的同时带来更为平滑的用户体验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Mh0p2sqKbcrKppjJilwS.png" alt width="783" height="343" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、以B端-营销标签洞察产品为例</h2>
<p>项目背景：整合其他来源渠道的标签，并提供标签挂站内商品的服务。用户可通过各维度查询符合条件的营销标签，并可以针对标签进行修改后审核采纳。</p>
<p>用户痛点：业务侧需在一周左右的时间中审核几十条甚至上百条营销标签，任务处理周期长，会出现主动或被动中断任务的情况，在重新开启任务处理流程时，需要从成百上千条任务中找出未审核或未采纳的任务后进行决策</p>
<p><strong>设计目标：解决较长时间段内的审核中断回溯问题，使用户在每次进入该模块时，可以快速定位到未审核的标签。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/l6ohOdR8VI3UWo8OFRP1.png" alt width="786" height="586" referrerpolicy="no-referrer"></p>
<h3>1. 状态标签</h3>
<p>在标签表格中增设标签类别字段。标签类别分别为“已收藏”、“未收藏”、“已采纳”、“未采纳”、“新标签”。</p>
<p>同时，设计三种颜色的标签来分别承载三种标签类别，使用“icon+字段”的视觉手段按状态差异化呈现，且该标签位于表格前列，以期依据用户浏览轨迹来辅助业务侧第一时间即可识别表格中不同类别的标签信息。</p>
<h3>2. 标签类别筛选</h3>
<p>在页面查询区提供标签类别的筛选功能。中断后通过筛选“未采纳”、“未收藏”，即可快查询到待审核的营销标签。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/BOwqNExANGOrasDmglqn.png" alt width="787" height="509" referrerpolicy="no-referrer"></p>
<h3>3. 同步状态标签及关键信息至其他场景</h3>
<p>将每条营销标签的“状态标签”及“关键信息”同步至详情页面。当用户点击表格中的“标签解读”按钮后，新页面打开标签详情页面，即用户能够同时打开多个详情页面。可在一定程度上无限拓展在某一时间内处理的标签个数。</p>
<p>同时，在详情页面的页头展示该标签的“状态标签”与表格中该条的关键字段信息；在详情页面的页尾吸底展示“收藏”与“采纳”两个决策按钮，提升用户的审核效率。</p>
<h3>最后</h3>
<p>以上就是「任务回溯设计」的全部内容啦～</p>
<p>后续会为大家分享<strong>录入流程设计</strong>、<strong>关键信息密度提升设计</strong>、<strong>场景化设计</strong>等一系列的设计方法，希望能给正在从事或准备入局B端的的小伙伴带来启发，也希望跟大家一起探讨更多的B端设计方法。</p>
<p> </p>
<p>本文由 @自转一周的鹿 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5329031" data-author="1001792" data-avatar="http://image.woshipm.com/wp-files/2022/02/SADJQo8Sc1yuZkeItS7W.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            