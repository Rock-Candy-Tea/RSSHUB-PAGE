
---
title: 'ERP系统：SPU和SKU的踩坑总结'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/FK0TijGw8EUHJ1ywVcyQ.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 01 Jun 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/FK0TijGw8EUHJ1ywVcyQ.jpg'
---

<div>   
<blockquote><p>编辑导语：SPU和SKU是电商后台和ERP后台的重要单元。SPU即标准化产品单元，SKU即最小库存单元。而电商后台系统设计与ERP系统设计有所不同，单纯地借助电商后台管理系统设计，将导致ERP设计上有所误差。本文作者结合其工作经验对ERP系统设计中的SPU和SKU设置进行阐述，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4630051 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/FK0TijGw8EUHJ1ywVcyQ.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、SPU和SKU的关系</h2>
<p>关于SPU和SKU的基础概念的了解，建议大家还是看看一些关于电商的书籍介绍，在此我就不做过多的整理，直接从《电商产品经理兵法：基于SaaS的电商系统设计与实践》此书中搬运一些基础概念过来。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="ERP系统：SPU和SKU的踩坑总结" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/vONRfFw8SL4h5rGThjps.jpeg" alt="ERP系统：SPU和SKU的踩坑总结" width="780" height="548" referrerpolicy="no-referrer"></p>
<h3>1. 什么是SPU？</h3>
<p>SPU即标准化产品单元，是一组可复用、易检索的标准化信息的集合。该集合描述了一个“产品”的特性。</p>
<p>通俗来说，属性值、特性相同的商品就可以称为一个SPU。也可以说，SPU是一个抽象出来的模板。</p>
<p>一般来说，类目系统中的关键属性（品牌、货号等）能够确定一个SPU，例如，iPhone 6就是一个SPU，诺基亚N97也是一个SPU，这与商家无关，与颜色、款式、套餐也无关。</p>
<p>SPU的属性是分类属性的子集。只要用户在SPU中定义了属性，那么用户在录入商品时，就不需要再次录入，也不可以更改。</p>
<p>摘自《电商产品经理兵法：基于SaaS的电商系统设计与实践》</p>
<h3>2. 什么是SKU？</h3>
<p>SKU即单品/最小库存单元。目前，SKU在各种零售商品中应用得非常普遍。例如，某款衣服是一件商品，不同颜色、不同尺码的该款衣服，对应不同的SKU。SKU比较简单，就是把销售的值组合存放，再加上库存、价格。例如，该款衣服的黑色大号共有5件，每件20元；红色小号共有3件，每件21元。</p>
<p>摘自《电商产品经理兵法：基于SaaS的电商系统设计与实践》</p>
<h3>3. 电商后台与ERP的商品管理差别</h3>
<p>电商后台往往不会直接有SKU层面的管理，都是在「商品管理」中处理，也就是在SPU层面来管理。主要涉及的操作有商品发布、编辑/修改、商品上/下架、提交商品审核等。</p>
<p>而ERP中，往往是在SKU层面进行管理的，例如发起采购、创建订单、查看库存、出入库单据等，都是关联的SPU。</p>
<p>所以在设计ERP的商品管理功能的时候，如果只是单纯地参考电商后台的管理，很容易踩坑，也很不太能理解背后是怎么运作、怎么管理的。</p>
<p>前段时间我刚好在调研这一块的业务，既调研了电商后台商品管理的一些逻辑，也上手试用了好几款ERP的商品管理，有一些疑惑已经解开，同时也有一些踩下的坑让我记忆犹新。</p>
<p>所以此文就来谈谈前段时间我是怎么被SPU和SKU这两个东西折磨的，还有踩过的坑分别有哪些。</p>
<h2 id="toc-2">二、SPU删除规格之后怎么处理？</h2>
<p>基于电商后台的规则，SKU是通过SPU的多规格来生成的，例如在创建SPU的时候，选择不同的规格，然后不同的规格就会通过笛卡尔乘积，生成不同的SKU。</p>
<p>在梳理这一块的逻辑的时候我就发现了一个问题：如果一个SPU的规格属性有两种「颜色」和「尺码」，然后在「颜色」中有“红色”、“蓝色”，在「尺码」中有“S”和“M”，则意味着一共是会生成四个SKU。</p>
<p>但是如果允许后期修改规格（修改规格属性或者修改规格值）的内容的话，会重新生成SKU，同时老的SKU在这里就无法体现了（因为规格不存在或者属性不存在）。</p>
<p>例如下图，如果将“蓝色”改成“绿色”，那么应该重新生成SKU，但是原来的“蓝色”规格的SKU就“消失”了。还有如果一些创建商品的时候没有选择规格，然后只是生成了一个SKU，后续如果要增加规格的时候，那么原来的商品也不能和后续多规格衍生的SKU形成相同的结构（规格结构不一样）。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="ERP系统：SPU和SKU的踩坑总结" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/JvVtmtHYOwz7Aw8lxs2a.jpeg" alt="ERP系统：SPU和SKU的踩坑总结" width="780" height="234" referrerpolicy="no-referrer"></p>
<p>如果SKU编码BS和BM是在库的、有库存的，那么直接删除这两个SKU显然是不合理的，但是由于电商的管理应该大多数是基于SPU层面，所以如果修改了规格属性（电商也叫销售属性），那么被更改了的那个应该不能再出现了，类似于此款停产或者不再售卖了。</p>
<p>下图是淘宝的千牛后台，发布商品的时候先选择对应的类目后，会给出对应的销售属性，而且是都必填，所以不存在中途增加和修改销售规格的情况出现。</p>
<p>但是ERP系统就不会有这么严谨的逻辑，而且也没有对应的类目信息。</p>
<p>所以这一块如果限制死了，不允许客户添加规格，那么就可能会满足不了一些多规格的商品的信息维护；如果放开了限制，那么用户就可以随意调整对应的规格信息，那么生成的SKU可能就会和原SPU断开关联。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="ERP系统：SPU和SKU的踩坑总结" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/dAZZcXvnNm2Sc6g726E6.jpeg" alt="ERP系统：SPU和SKU的踩坑总结" width="782" height="393" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">千牛后台截图</p>
<p>基于上述的情况，我查了很多资料，也问了一些朋友之后发现，如果是单纯地参考电商平台的后台处理逻辑，那么很难兼容各行各业的商家的产品。</p>
<p><b>于是我开始找了另一类竞品：电商ERP，主要还是跨境类的，例如店小秘、马帮、通途等。</b></p>
<p>结果发现它们的处理方式很巧妙，在创建商品的时候可以选择类型：</p>
<ul>
<li>单规格产品，也可以称为无规格产品；</li>
<li>多规格产品，可以自由添加规格进行变换。</li>
</ul>
<p>单规格产品不能转为多规格，如果需要增加规格，则需要重新创建SPU再生成SKU；多规格产品也不能转为单规格产品，多规格产品一定要选择至少一项规格属性。<b>这样一分类，就将很多复杂的场景给隔离开了，只需要重点关注多规格产品的管理即可。</b></p>
<h2 id="toc-3">三、无规格的产品怎么创建SKU？</h2>
<p>在没有仔细地调研跨境ERP的做法的时候，关于无规格的产品怎么创建SKU的问题，我们内部讨论了两种方案。</p>
<ol>
<li>直接创建SPU的时候，不填写规格信息，当没有规格信息的时候，默认SPU对应一个SKU，即一对一的关系；</li>
<li>创建SPU的时候，填写一个规格，例如衣服就只有一个型号「白色的中码」，那么就是创建一个规格「White*M」。</li>
</ol>
<p>后来调研了跨境ERP的做法之后，我发现这两种做法都不好，具体的理由和上面的是一样的。<b>如果当前只有一个规格，后期多了规格需要拓展的时候，在此商品SPU的基础上拓展SKU，还是会踩坑。例如删除了“白色”这个规格，然后用了其他颜色，也删除了“M”这个尺码，那么之前的「White*M」就挂不在SPU之下了。</b></p>
<p>所以我决定采用跨境ERP的做法，在创建SKU的时候要先选择类型，到底是单规格产品还是多规格产品。如果是单规格产品，那么直接就生成SKU，不能拓展所谓的规格属性；如果是多规格产品，则先生成父级SPU，然后再通过多规格属性来拓展生成具体的SKU。</p>
<p><b>而且多规格的产品，不能添加&删除原来的规格属性，只能追加对应的属性值。</b></p>
<p>例如一开始的规格属性是「颜色」和「尺码」，后续编辑的时候，只能继续追加「颜色」的属性值，或者追加「尺码」的属性值，而不能再删除「颜色」或者添加新的其他规格属性。同时也要限制不允许随意删除已生成的SKU（例如上面提到的BM和BS），要先判断SKU是否已被使用。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="ERP系统：SPU和SKU的踩坑总结" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/gGzXOs5h07YMKkiJbmYH.jpeg" alt="ERP系统：SPU和SKU的踩坑总结" width="780" height="508" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">有赞后台截图</p>
<p>所以，最终我所选择的方案是：<b>无规格的产品直接创建一个单品SKU，不需要和SPU关联；而有规格的产品则先创建SPU之后，再通过规格来创建SKU。</b></p>
<p>当然还有更简单的办法就是，ERP中不存在SPU的概念，直接全部创建的都是SKU，用映射的方式来将电商平台的SPU下的SKU映射到系统中。这种逻辑是最简单粗暴的，利弊都很明显，只是我们要支持的业务场景，不允许这样做……</p>
<h2 id="toc-4">四、供应商与SPU&SKU的关系</h2>
<p>供应商是与SPU关联还是和SKU关联，这个也是我之前一直很纠结的一个问题。按理说，供应商提供的是具体的产品，那么自然而然应该是跟SKU关联。</p>
<p>但是有一部分的SKU是通过SPU的多规格属性演化而来的，如果供应商直接和SKU关联，那么则意味着创建好了SKU之后，还需要分别对同SPU但是不同SKU的产品一一设置供应商关系、供应商报价等。</p>
<p>从操作层面来说，用户要做多次重复的工作；从设计层面来说，有很多可复用的属性没有复用到……</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="ERP系统：SPU和SKU的踩坑总结" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/eL29yjUgOyZronnYSEHd.jpeg" alt="ERP系统：SPU和SKU的踩坑总结" width="780" height="376" referrerpolicy="no-referrer"></p>
<p><b>创建多规格产品（SKU）的时候，将供应商信息挂在SPU维度上，然后SKU继承这些信息，就避免了逐个SKU维护供应商的繁琐操作。</b></p>
<p><b>如果是创建单规格产品（SKU）的时候，将供应商信息直接挂在SKU维度上，一个SKU就维护一次。</b></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="ERP系统：SPU和SKU的踩坑总结" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/DWvax2vzsVWxZZ7v1An2.jpeg" alt="ERP系统：SPU和SKU的踩坑总结" width="781" height="940" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">通途ERP截图</p>
<p>通途ERP也是这样的做法，比较清晰明了。</p>
<h2 id="toc-5">五、SKU如何编辑？可以编辑哪些信息？</h2>
<p>上面提到了，我们创建了SKU的时候有两个入口，一个是创建单规格产品，一个是创建多规格产品。所以对应的，我们编辑SKU的入口也有两个，一个是从SPU层面进入编辑，另外一个是从SKU的层面进入编辑。</p>
<p>期初我一直觉得既然创建好了SKU，那么其实在ERP中，SPU基本上就没啥作用了，所以编辑只需要在SKU层面即可。</p>
<p>但是随着对业务的分析，以及对SPU和SKU的关系的进一步熟悉，我发现如果只是在SKU层编辑就会出现一些很奇怪的问题。</p>
<p>例如「iPhone 12 国行」可以算作是一个SPU，然后“iPhone 12 国行 红色 64G”（简称为：红色64G）和“iPhone 12 国行 白色 128G”（简称为：白色128G）则是其所对应的SKU。</p>
<p>如果我将所有的编辑都放在SKU层面，那么我自然而然可以编辑一些“基础信息”、“非关键属性”、“销售信息”等。</p>
<p>如果只是编辑“销售信息”那么还没什么问题，因为不同的SKU就是因为销售属性不一样而做的区分。但是如果允许编辑一些“基础信息”，例如说“名称”、“描述”、“类目”等，那么可以将“iPhone 12 国行 红色 64G”改成“苹果12 中国红 64G”，也可以改成“苹果11 白色 64G”等等，这样就会乱套了。</p>
<p>所以，SKU的编辑应该遵循和创建的逻辑相同，也要符合SPU和SKU的关系的定义。有两个入口创建，也就有两个入口编辑。同时，不同的入口可以编辑的信息是不一样的。</p>
<p>SPU维度编辑的“基础信息”等应该是复用在所有的SKU层面的，即改了SPU的信息则SKU的信息也要改；SKU维度的编辑，只能是一些自己独立的属性，例如“售价”、“库存信息”、“采购价格”等。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="ERP系统：SPU和SKU的踩坑总结" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/nfgFEOsQrgMd61NUhUoB.jpeg" alt="ERP系统：SPU和SKU的踩坑总结" width="781" height="474" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">千牛后台截图</p>
<h2 id="toc-6">六、一些参考资料</h2>
<p>最后分享一些相关参考资料给大家，如果大家对电商后台或者ERP后台感兴趣的，可以根据下面的关键词进行搜索。有一些后台账号是需要申请试用的，找个小号去申请比较好，能避免后续很多的骚扰。</p>
<ul>
<li><b>电商后台的竞品：</b>千牛（淘宝商家后台）、刘志远——电商后台产品设计课程、相关图书（京东）、有赞。</li>
<li><b>ERP的竞品：</b>店小秘、马帮、金蝶星辰、聚水潭。</li>
</ul>
<h3>#专栏作家#</h3>
<p>vitamin，微信公众号：皮酱叨逼叨。人人都是产品经理专栏作家，公众号运营小白，初中级B端产品一枚（一年开发经验+三年产品经验）。主导过在线教育类产品，目前是跨境电商供应链仓储物流产品一枚，欢迎勾搭，一同学习。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4625140" data-author="227259" data-avatar="http://image.woshipm.com/wp-files/2017/12/yvQWfakqo1j7mb14txHL.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            