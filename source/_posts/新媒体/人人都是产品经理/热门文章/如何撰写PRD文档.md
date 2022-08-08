
---
title: '如何撰写PRD文档'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://image.woshipm.com/wp-files/2014/06/e6902e951e9f7d122ca93383ded67ff3.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 10 Jun 2014 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2014/06/e6902e951e9f7d122ca93383ded67ff3.jpg'
---

<div>   
<p style="color: #373737">产品经理主要有两项职责：①评估产品机会  ② 定义要开发的产品；前者我们在上篇的《如何获得产品立项》文章中已经大致介绍过；而定义开发的产品则需要通过产品需求文档(PRD）来描述产品的特征和功能。本篇主要分享下博主平常工作中是如何撰写移动应用的PRD文档的。</p>
<h2 style="color: #000000" id="toc-1">PRD(开发需求文档）的作用</h2>
<p style="color: #373737">在学习如何撰写PRD之前，我们先要明白写PRD的目的是什么：</p>
<div style="color: #373737">
<p style="font-style: inherit;color: #111111"><strong>①概念化”阶段进入到“图纸化”</strong></p>
<p style="font-weight: inherit;font-style: inherit">我们之前在市场需求文档（MRD）中阐述到的功能，都是表达的一个意向，不考虑实现方法和细节。而PRD则是将概念图纸化，需要阐述详细的细节和实现模型。产品人员可以通过撰写PRD，梳理清楚方案实现过程中的各种问题和影响。</p>
<p style="font-style: inherit;color: #111111"><strong>②向项目成员传达需求的意义和明细</strong></p>
<p style="font-weight: inherit;font-style: inherit">PRD的主要面向对象是项目经理、开发、设计和测试。如何向这些不同的角色表达清楚需求明细，就需要一份规范的PRD文档来描述。项目经理通过文档可以迅速了解任务的规模和相关接口，而开发设计人员通过文档可以了解页面元素和用例规则，测试人员可以提前根据文档撰写测试用例。PRD文档在形式上是项目启动的必要元素之一。</p>
<p style="font-style: inherit;color: #111111"><strong>③ 管理归档需求</strong></p>
<p style="font-weight: inherit;font-style: inherit">大都数的新需求都需要迭代几个版本后才能走向成熟稳定的阶段，如果没有PRD文档，在大型项目中，需求的迭代变更将变的无据可循。PRD的文档修订编号和命名也是项目规范化管理的主要方法之一。</p>
<h2 style="font-style: inherit;color: #000000" id="toc-2">PRD的表现形式</h2>
<p style="font-weight: inherit;font-style: inherit">一般企业内部的PRD文档选择wiki系统或word文档。wiki在协同和保密方面会有优势，而且能够记录修改文档的每一次变更。而word在阅读修改方面比较有优势，一般使用Word加SVN的方式来管理更新文档。这个可根据每个企业的管理规范来选择那种方法更合适。</p>
<h2 style="font-style: inherit;color: #000000" id="toc-3">PRD的主要构成</h2>
<p style="font-weight: inherit;font-style: inherit">一份基础的PRD文档主要由三部分组成<a style="font-weight: inherit;font-style: inherit;color: #195685" href="https://image.woshipm.com/wp-files/2014/06/e6902e951e9f7d122ca93383ded67ff3.jpg"><img data-action="zoom" class="size-full wp-image-1003 aligncenter" title="PRD" src="https://image.woshipm.com/wp-files/2014/06/e6902e951e9f7d122ca93383ded67ff3.jpg" alt width="700" height="360" referrerpolicy="no-referrer"></a></p>
<p style="font-style: inherit;color: #111111"><strong>①引言</strong></p>
<p style="font-weight: inherit;font-style: inherit">引言部分主要包括：需求背景、需求目的、需求概要、涉及范围、全局规则和名词说明，交互原型地址等。引言部分的写作目的是让阅读者快速理解需求背景和概要。如果是公司内部文档，引言部分可以从简写作。</p>
<p style="font-style: inherit;color: #111111"><strong>②业务建模</strong></p>
<p style="font-weight: inherit;font-style: inherit">建模的目的是为了帮助阅读对象更好的理解需要开发的需求，常用的模型种类包括：用例图、实体图、状态图、流程图等。常用的建模语言如UML。UML具体的建模方法<a style="font-weight: inherit;font-style: inherit;color: #195685" href="http://www.uml.org.cn/oobject/OObject.asp#9">请戳这里。</a></p>
<p style="font-style: inherit;color: #111111"><strong>③ 业务模块</strong></p>
<p style="font-weight: inherit;font-style: inherit">业务模块包含具体页面的元素、用例规则，以及相关的原型，流程图。业务模块的描述是整个文档最核心的部分，下面博主用案例来描述一下业务模块的编写方法。</p>
<h2 style="font-style: inherit;color: #000000" id="toc-4">案例介绍：旅行箱–目的地攻略（应用商店搜索“<a style="font-weight: inherit;font-style: inherit;color: #195685" href="http://m.xyz.cn/special/suitcase_ua.html" target="_blank">旅行箱</a>”）</h2>
<p style="font-weight: inherit;font-style: inherit">需求的目标是在APP中展示相关国家/城市的旅游资讯内容，如下图所示：<a style="font-weight: inherit;font-style: inherit;color: #195685" href="https://image.woshipm.com/wp-files/2014/06/5aa8b007a2f97d21f2148f717ca2b5dd.png"><img data-action="zoom" class="aligncenter wp-image-1018" title="2014-6-3 16-29-02" src="https://image.woshipm.com/wp-files/2014/06/5aa8b007a2f97d21f2148f717ca2b5dd.png" alt width="723" height="467" referrerpolicy="no-referrer"></a></p>
<p style="font-weight: inherit;font-style: inherit"><strong style="font-style: inherit">那么我们在第一部分的引言中可以写下简单的需求描述：</strong></p>
<ol style="font-weight: inherit;font-style: inherit">
<li style="font-weight: inherit;font-style: inherit">目的地攻略以城市/国家为单位，展示八个栏目下的文章列表。</li>
<li style="font-weight: inherit;font-style: inherit">初期运营指标为编辑所有涉及城市的归属国家攻略内容，相关城市暂不编辑；APP前台默认显示国家内容卡片，城市内容卡片无数据时隐藏。</li>
<li style="font-weight: inherit;font-style: inherit">运营系统提供内容生成对应的触屏网页，App读取和下载对应网页内容；</li>
</ol>
<p>为了帮开发者迅速了解需求结构，我们需要建一个简单的流程图帮助开发理解功能：</p>
<div style="font-weight: inherit;font-style: inherit"><a style="font-weight: inherit;font-style: inherit;color: #195685" href="https://image.woshipm.com/wp-files/2014/06/74940f9d62cb9b5e41732312a9d4a78d.jpg"><img data-action="zoom" class="wp-image-1021 aligncenter" title="流程图" src="https://image.woshipm.com/wp-files/2014/06/74940f9d62cb9b5e41732312a9d4a78d.jpg" alt width="717" height="843" referrerpolicy="no-referrer"></a></div>
<div style="font-weight: inherit;font-style: inherit"></div>
<div style="font-weight: inherit;font-style: inherit">相对复杂的运营系统，我们可以补充相关用例图和实体关系图：</div>
<div style="font-weight: inherit;font-style: inherit"></div>
<div style="font-weight: inherit;font-style: inherit"></div>
<div style="font-weight: inherit;font-style: inherit"></div>
<div style="font-weight: inherit;font-style: inherit"></div>
<div style="font-weight: inherit;font-style: inherit"></div>
<div style="font-weight: inherit;font-style: inherit"></div>
<div style="font-weight: inherit;font-style: inherit"><a style="font-weight: inherit;font-style: inherit;color: #195685" href="https://image.woshipm.com/wp-files/2014/06/7215448dd197b0ab841feb100c287296.png"><img data-action="zoom" class="size-full wp-image-1022 aligncenter" title="2014-6-3 17-15-41" src="https://image.woshipm.com/wp-files/2014/06/7215448dd197b0ab841feb100c287296.png" alt width="584" height="451" referrerpolicy="no-referrer"></a></div>
<div style="font-weight: inherit;font-style: inherit"></div>
<p style="font-weight: inherit;font-style: inherit">引言和建模部分是为了帮助开发和测试人员快速理解需求，具体的页面和用例规则还需要通过第三部分的业务模块来描述，这里我们节选案例中的文章列表页来描述：</p>
<h3 style="font-style: inherit;color: #111111">文章列表页共包含一个页面，四个用例</h3>
<p><a href="https://image.woshipm.com/wp-files/2014/06/Photo_20140603231259TENP.jpg"><img data-action="zoom" class="size-full wp-image-88735 aligncenter" src="https://image.woshipm.com/wp-files/2014/06/Photo_20140603231259TENP.jpg" alt="Photo_20140603231259TENP" width="700" height="600" srcset="https://www.woshipm.com/wp-content/uploads/2014/06/Photo_20140603231259TENP.jpg 700w, https://www.woshipm.com/wp-content/uploads/2014/06/Photo_20140603231259TENP-312x268.jpg 312w" sizes="(max-width: 700px) 100vw, 700px" referrerpolicy="no-referrer"></a></p>
<p>那我们的描述结构就为：<br>
文章卡片页面元素<br>
收藏文章用例<br>
分享文章用例<br>
查看文章列表<br>
查看文章（太简单可不描述）</p>
<div style="color: #373737">
<h3 style="color: #111111">文章卡片的页面元素描述：</h3>
<div style="color: #373737"><a style="font-weight: inherit;font-style: inherit;color: #195685" href="https://image.woshipm.com/wp-files/2014/06/e5ea61893757b87230ae49b59e7e099c.png"><img data-action="zoom" class="wp-image-1026 aligncenter" title="2014-6-3 17-34-12" src="https://image.woshipm.com/wp-files/2014/06/e5ea61893757b87230ae49b59e7e099c.png" alt width="719" height="388" referrerpolicy="no-referrer"></a></div>
<div style="color: #373737"></div>
<h3 style="color: #111111">（收藏）用例的描述为</h3>
<div style="color: #373737"><a style="font-weight: inherit;font-style: inherit;color: #195685" href="https://image.woshipm.com/wp-files/2014/06/e6e01d80fa76aa89222ede2131f374a0.png"><img data-action="zoom" class=" wp-image-1027 aligncenter" title="收藏" src="https://image.woshipm.com/wp-files/2014/06/e6e01d80fa76aa89222ede2131f374a0.png" alt width="723" height="701" referrerpolicy="no-referrer"></a></div>
<p style="color: #373737">业务模块的描述一般是原型图+数据元素+用例描述，这样可以在原型图的基础上加上对应元素属性的描述，并通过动作描写的方式表达用例规则和各种流程。这样的写作方式不仅可以向不同对象传达产品经理的意图，而且可以帮助产品经理自己梳理需求的逻辑和各种异常流程。</p>
<p style="color: #373737">本文所用例子app为“旅行箱”</p>
<p style="color: #373737">本文为小猛投稿发布，转载请注明出处并附带本文链接</p>
</div>
</div>
                      
</div>
            