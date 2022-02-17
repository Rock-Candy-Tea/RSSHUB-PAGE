
---
title: 'B端表单设计思考'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/02/vqKbYwtxJ5Eu6sa06rUh.png'
author: 人人都是产品经理
comments: false
date: Thu, 17 Feb 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/02/vqKbYwtxJ5Eu6sa06rUh.png'
---

<div>   
<blockquote><p>编辑导语：在设计表单时，你有考虑过如何排版？左对齐还是右对齐？纵排列还是横排列？这篇文章作者详细介绍了B端表单设计中的对齐问题，推荐想要了解B端表单设计的童鞋阅读。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-753668 aligncenter" src="https://image.yunyingpai.com/wp/2022/02/vqKbYwtxJ5Eu6sa06rUh.png" alt referrerpolicy="no-referrer"></p>
<p>当我们使用表单组件、或设计表单页面时Label 和 input 应该上下还是左右排列、表单项应该纵向排列还是横向排列、在页面中应该居中对齐还是左对齐呢</p>
<p>当我们使用表单组件、或设计表单页面时，往往有最直觉的设计经验本能驱动我们去解决这类看似在界面设</p>
<p>计中最简单的问题，但每每到细微之处，又会有无数疑问从细节中冒出来给我们设计师造成困扰。</p>
<p>在做表单设计中经常这样的两个问题：</p>
<p><img data-action="zoom" class="fr-fic fr-dib aligncenter" src="http://image.woshipm.com/wp-files/2022/02/AFnVtCfsiNYpyBcCFoqt.jpg" width="601" height="338" data-settime="3" data-status="true" data-picid="3959314" referrerpolicy="no-referrer"></p>
<p><strong>一是对齐问题。</strong></p>
<p>标题到底向左还是向右对齐，好像两种都有可以都不太影响操作。</p>
<p><strong>二是输入框长度问题。</strong></p>
<p>A：你这个框长度为什么不一样啊，看起来好乱。</p>
<p>B：你这么框为什么这么长，我这只有展示两个数字啊 。</p>
<h2 id="toc-1">一、对齐问题</h2>
<p><img data-action="zoom" class="fr-fic fr-dib aligncenter" src="http://image.woshipm.com/wp-files/2022/02/XQ7Qabwb4FO6jaBGyPBq.jpg" width="450" height="253" data-settime="3" data-status="true" data-picid="3959318" referrerpolicy="no-referrer"></p>
<p>先说下对齐问题，怎么去选择对齐方式，在日常表单设计中常见的对齐方式有左对齐、右对齐、和顶部对齐。</p>
<p>然后三种对齐方式分从<strong>内容关联性</strong>、<strong>标题长度的灵活性、空间的占比、阅读体验</strong>等几个维度进行优劣分析。</p>
<p><img data-action="zoom" class="fr-fic fr-dib aligncenter" src="http://image.woshipm.com/wp-files/2022/02/l4wymfhU8skwiimLyf4S.jpg" width="450" height="253" data-settime="3" data-status="true" data-picid="3959346" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="fr-fic fr-dib aligncenter" src="http://image.woshipm.com/wp-files/2022/02/rbqwNgOZuH948Gq0yDAc.png" width="451" height="296" data-settime="3" data-status="true" data-picid="3959350" referrerpolicy="no-referrer"></p>
<p>优点：阅读视线对齐，比较符合人正常浏览习惯，竖向空间占用较少。</p>
<p>缺点：标题<strong>长度限制性较大</strong>、<strong>内容关联性较低</strong>、浏览效率低、阅读成本较高。</p>
<p>适用场景：<strong>标题字符数≤7</strong>，表单内容适中、逻辑相对复杂、<strong>需要仔细阅读</strong>的页面。</p>
<p><img data-action="zoom" class="fr-fic fr-dib aligncenter" src="http://image.woshipm.com/wp-files/2022/02/1v0XxaYwXRY6SH9bshUR.png" width="450" height="192" data-settime="3" data-status="true" data-picid="3959356" referrerpolicy="no-referrer"></p>
<p>优点：<strong>内容关联性强</strong>、版式整齐、竖向空间占用少。</p>
<p>缺点：标题长度灵活性不高、左边起点对不齐、<strong>浏览速度慢。</strong></p>
<p>适用场景：数据内容多、逻辑关系简单、标题字数少的情况（如筛选条件）。</p>
<p><img data-action="zoom" class="fr-fic fr-dib aligncenter" src="http://image.woshipm.com/wp-files/2022/02/4VMnYzQONKBOysBFryhL.png" width="451" height="219" data-settime="3" data-status="true" data-picid="3959359" referrerpolicy="no-referrer"></p>
<p>优点：标签字符<strong>长度灵活度高、浏览效率相对较高、信息展示清晰。</strong></p>
<p>缺点：竖向空间占比大。</p>
<p>适用场景：标题字符数较长的情况。</p>
<p><img data-action="zoom" class="fr-fic fr-dib aligncenter" src="http://image.woshipm.com/wp-files/2022/02/tN3IcbWb4Fpr3YQN3JxE.jpg" width="450" height="253" data-settime="3" data-status="true" data-picid="3959360" referrerpolicy="no-referrer"></p>
<p>从上面的分析可以看出来影响表单布局方式的主要是两点：</p>
<p><strong>页面内容 </strong>和 <strong>承载内容的容器。</strong></p>
<ol>
<li>页面内容：<strong>内容数量的多少</strong>直接会影响布局，内容越少信息逻辑越简单，思考过程越容易，反之内容越多逻辑结构越复杂，考虑的东西就越多，要有序的、有规律的去布局信息。</li>
<li>容器：容器的大小对应单位面积展示信息数量的多少，也会直接影响到表单的布局，常见的容器有<strong>页面（最大）、抽屉（大）、弹窗（中）、气泡（小）</strong>。</li>
</ol>
<p>tips：容器的选择要符合当期业务场景分析适用情况，主要从上下页面的关联性、任务的复杂程度 和 操作流畅程度 去选择适合的容器</p>
<p><img data-action="zoom" class="fr-fic fr-dib aligncenter" src="http://image.woshipm.com/wp-files/2022/02/atDamMzorQgULB5rQa7g.jpg" width="450" height="253" data-settime="3" data-status="true" data-picid="3959361" referrerpolicy="no-referrer"></p>
<p>如果页面直接存在强关联性，需要停留在当期页面进行操作并且展示信息不多时，建议使用弹窗或者抽屉。</p>
<p>如果关联较弱且信息量较大时，建议新开页面进行操作，沉浸操作注意力会更加集中。</p>
<h2 id="toc-2">二、总结</h2>
<p>对于信息量大、业务场景复杂、需要仔细阅读的页面（如合同审核、项目审批、订单报价等）推荐 <strong>单列 左对齐方式</strong> 布局。</p>
<p>当标题字数长度过长，影响页面排版美观和体验时，推荐<strong> 顶对齐方式</strong> 布局。</p>
<p>正常情况推荐 <strong>单列布局</strong> 的方式。</p>
<ul>
<li>体验上：阅读速度快能提高填写效率。</li>
<li>设计上：减少设计成本，复用率高。</li>
<li>技术上：开发成本低，比较容易适配和扩展。</li>
</ul>
<p><strong>多列布局时，建议采用 右对齐方式布局</strong>，保证模块之间的亲密性，减少阅读误差。多列阅读效率较低，除特殊情况不建议采用多列布局。</p>
<p> </p>
<p>原文链接：https://m.ui.cn/details/610344</p>
<p>本文由 @木登Zero 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
                      
</div>
            