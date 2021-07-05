
---
title: 'ERP系统：SKU产品库的两种设计方案'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/36HCEfgG2liyCmVKG1LD.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 04 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/36HCEfgG2liyCmVKG1LD.jpg'
---

<div>   
<blockquote><p>编辑导语：在做电商时，SKU产品库是大多数运营者会接触的系统，而在SKU产品库中，又有两种不同的设计方案，这二者又有何区别？</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4808410 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/36HCEfgG2liyCmVKG1LD.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、在线产品与本地产品</h2>
<p>在聊SKU产品库的设计方案之前，我们先了解一下两个名词：<strong>在线产品与本地产品。</strong></p>
<p>在线产品，一般是指电商平台上的“商品管理”或者“产品管理”模块中产品。而与之相对应则是本地产品或者也叫做库存产品，就是指实际存放在仓储中的实体产品。</p>
<p>一般来说，电商平台上卖的产品就是实际放在仓库中的实体产品，那为什么要区分为两种产品进行管理呢？</p>
<p>如果是对于单店铺或者是单平台来说，这两者保持一致其实是没问题的。但是由于电商卖家往往会开设多个店铺，运营多个平台，以此来提升自己的曝光度，获取更多的流量，所以就需要在多个平台，多个店铺上架自己的产品。</p>
<p>多个平台，多个店铺之间为了避免相同的产品被平台检测为恶意铺货或者不同的平台规则不一样，就会衍生出不同的在线产品，它们本质上可能对应的是同一款产品，但是由于不同的平台规则限制，最终会导致产品的一些基础信息各不相同。<br>
在跨境电商ERP中，不同平台的产品维护与管理统称为“刊登”或者“产品”。所以，当卖家需要经营多个平台，多个店铺的时候，就需要分别对不同的平台的产品进行管理。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/JAZ5jsGxr1PH9Wz3t96L.png" alt width="588" height="305" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">马帮ERP</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/SLuDyyLI56FvXUsWmvE5.png" alt width="574" height="282" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">店小秘ERP</p>
<p>虽然在多个平台有多个不同的产品，但是实际卖家要卖的产品可能就是那么几个，也就是实际放在仓库中的产品数量并没有那么多。</p>
<p>当不同的平台的订单都进入到了ERP中之后，就会出现一个问题：<strong>每个平台的订单中的产品都不一样，那么我应该实际发出哪一款产品给用户呢？</strong></p>
<p>这就是涉及到“本地产品与在线产品”的映射问题了，在跨境电商ERP中，这种关系也叫做“商品匹配”或者“产品配对”。</p>
<p>即通过接口将所有在线产品都同步到一个公共池中，然后设置一些规则将这些在线产品与本地产品绑定起来，后续平台订单进来了之后，通过这一层绑定关系可以自动匹配出实际要发货的产品是哪个，这个实际要发出的产品，也就是标题中提到的“本地产品”或者也称“库存产品”。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/7n8IDLnDXJuCelFGSKFg.png" alt width="637" height="228" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">店小秘的商品配对</p>
<h2 id="toc-2">二、两种设计方案介绍</h2>
<p>经过我的调研和实践，如果需要搭建一套用来管理本地产品的“SKU产品库”，一般会有两种设计方案：</p>
<ol>
<li>平台型设计方案，类似于电商平台的产品管理模式，以SPU为主体；</li>
<li>库存性设计方案，以实际的库存管理粒度为主体，即以SKU为主体。</li>
</ol>
<p>跨境电商ERP中采用方案2的居多，是主流的做法，而采用方案1的比较少，不太常见。</p>
<p>下面我分别来介绍一下这两种设计方案的具体细节。</p>
<h3>1. 平台型设计方案（以SPU为主体）</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/7oNQYywiNNAtwIcjgr5a.png" alt width="589" height="293" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">阿里巴巴国际站后台-产品管理</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/kQIIXXV860t7vIxY6Xqv.png" alt width="556" height="222" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">有赞后台-产品管理</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/5He8XbWc0C5LChftV4YV.png" alt width="544" height="253" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">淘宝千牛后台-产品管理</p>
<p>以上三张图都是很典型的电商后台产品管理的界面，每一行展示的都是一款产品（SPU）的主要信息，这个跟用户在前台看到的列表是相同的。</p>
<p>但是实际用户点击进去了之后就会发现，当要购买一款具体的产品的时候，ta还需要选择一些规格，这样才能确定最终的价格。这些逐个选择的规格，最后就组成了实际的SKU，也就是能确定具体的库存单位是哪个。</p>
<p>具体的操作路径如下图所示：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/QylFRk8wzAniaVOIyMuX.jpeg" alt width="625" height="464" referrerpolicy="no-referrer"></p>
<p>其中我了解的采用平台型设计方案ERP有：通途，金蝶等。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/DZyERD49PbQULgzYF1qb.png" alt width="573" height="244" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">通途ERP-产品管理</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/njekbogXfPt4HRP9UQL0.png" alt width="611" height="267" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">金蝶星辰-产品管理</p>
<h3>2. 库存型设计方案（以SKU为主体）</h3>
<p>库存型设计方案是市面上最主流的，最常见的方案。无论是单品还是多规格品，在创建之后都会以SKU的维度展示，所有的信息也都是在SKU维度进行更新的。SPU只是在创建多规格产品的时候用来快捷生成多个SKU的载体而已，当生成了SKU之后，SPU也就几乎没啥作用了。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/rZS86q7WpEbgtu50YWJ7.png" alt width="606" height="315" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">芒果店长ERP-产品管理</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/tsy1c1LrZDMMbE1fZSO0.png" alt width="541" height="339" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">店小秘ERP-产品管理</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/vaHiaIcNWS6G5rToJUOi.png" alt width="565" height="302" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">马帮ERP-产品管理</p>
<h2 id="toc-3">三、两种设计方案的差异</h2>
<p>如果只是单纯的看图似乎并看不出两种设计方案的差异在哪里，不过如果你对此话题比较感兴趣的话我建议你可以去申请一些试用账号体验一下，相信会对其中的细节有更深的理解的。在此，我用一些文字来解释一下其中的关键差异。</p>
<h3>1. 展现方式不一样</h3>
<p>平台型设计方案是以SPU为维度展示产品的，而库存型设计方案则是以SKU为维度展示产品的。如果以SPU为维度，那么一些差异性的细节就不好展示了，例如价格、重量、尺寸，库存、可用情况等，这些信息一般是跟SKU挂钩的。</p>
<h3>2. 编辑方式不一样</h3>
<p>平台型设计方案如果要编辑具体的产品信息，需要编辑两块的内容，一块是公共的数据，也就是所有SKU都继承的内容；另一块是单个SKU关联的信息，不同的规格组合对应的信息不一样，需要单独维护。</p>
<p>库存型设计方案则直接就到了最小库存单位粒度了，所有的信息都是独立的，可以各自维护的。例如41码的鞋子和42码的鞋子是不同的SKU，可以分别维护这两者的信息，而不用考虑公共信息继承的问题。</p>
<p>你可以把41码的那个SKU的名字改成“女鞋”，而42码的那个SKU的名字改成“老人鞋”，虽然从电商产品管理的角度来说这不合理，但是在ERP中却没有限制，因为它们的SKU没有变化。</p>
<h3>3. 调用的方式不一样</h3>
<p>平台型设计方案，在需要选择SKU的时候，要先选择SPU，然后通过选择不同的规格来确定想要的那个SKU；而库存型设计方案则简单多了，只需要直接选择相应的SKU即可。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/BgYsO431LyDiRJaZOz5U.png" alt width="582" height="320" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">先选择SPU，再选择规格确定SKU</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/K5hsBtyaRG49wqUJPlDo.png" alt width="597" height="292" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">直接选择SKU</p>
<h3>4. 删除的逻辑不一样</h3>
<p>平台型设计方案，如果需要删除SKU的时候，需要通过删除规格来删除SKU，而且需要在SPU的载体上操作；而库存型设计方案则直接选择对应的SKU即可删除，不会和SPU等有什么强关联的关系。</p>
<h3>5.平台型设计方案的利弊</h3>
<p>总结来说，库存管理的本质还是以SKU为最小粒度，无论是平台型设计方案还是库存型设计方案最后都是通过以管理SKU来达到管理实物的作用。</p>
<p>以SPU为载体，然后通过规格去确定SKU有一定的好处，也有很明显的弊端，这也是为什么主流的跨境电商ERP中都不太选用此方案的原因。</p>
<p>主要的利处和弊端分别如下：</p>
<p><strong>利处：</strong></p>
<ul>
<li>维护产品资料的时候可以与平台产品的逻辑保持一致，便于用户上手和理解；</li>
<li>适用于多规格属性比较多的产品，可以通过先选择产品然后再通过规格来定位具体的SKU；</li>
<li>适用于需要维护比较丰富的产品资料的场景，因为很多资料都是在SPU的维度，这样可以减少重复维护的工作量。比较适合B2B的模式，需要使用产品库的内容给用户做报价。</li>
</ul>
<p><strong>弊端：</strong></p>
<ul>
<li>调用产品的时候会麻烦一点，需要通过选择SPU再选择SKU，还需要记忆相应的规格来确定最终的SKU；</li>
<li>编辑和维护的时候有两套入口，一个是SPU的入口，一个是SKU的入口，会比较麻烦一些，而且SKU的入库能维护的信息不多；</li>
<li>无规格的产品和多规格的产品并列展示的时候，需要后台做特殊处理，例如给无规格的产品也加上SPU+SKU的关系；</li>
<li>查看和展示的时候不够直观，尤其是放在仓库层面来使用的时候，仓库应该是以SKU的粒度来管理是最有效的，但是此处也需要做特殊处理，将SKU抽离出来，并排展示。</li>
</ul>
<h2 id="toc-4">四、一些踩坑点</h2>
<p>上面介绍完了两种设计方案的一些差异，如果是按照库存型设计方案来做，基本上市面上主流的跨境ERP都是这样做的，该踩的坑别人都踩过了，所以自己只要对着竞品走一遍后，踩坑几率就可以大大降低。</p>
<p>所以这里谈到的踩坑点是针对平台型设计方案来总结的，这一块网络上已有的资料比较少，而且采用这种做法的ERP也比较少，所以踩坑点就多了些。</p>
<h3>1. 单规格产品与多规格产品的转化</h3>
<p>单规格和多规格产品的不同就在于规格是否大于1种以上，如果是大于1种以上则是多规格，如果是只有一种规格则是单规格。</p>
<p>为了避免单规格和多规格的随意转化，影响关联的单据和历史数据等，一般跨境电商EPR创建产品的入口就会分成两个：“创建普通产品”和“创建多规格产品”。</p>
<p>创建普通产品则是在创建SPU的同时也创建了SKU，而且SKU的所有信息都是从SPU这里继承来的，此刻的SPU编码会和SKU编码一致，SPU的存在只是为了兼容，以致于表结构呈现一体性。</p>
<p>创建多规格产品，则是先创建SPU，然后通过规格的组合自动生成SKU，SPU编码和SKU编码不相同，而是SKU维度上需要填写相应的属性，例如成本价、销售价、期初库存、重量等。</p>
<h3>2. 平台产品的接口字段兼容</h3>
<p>以阿里巴巴国际站为例，国际站的产品接口中，当有平台产品有规格信息的时候，SKU信息是有的；当没有规格信息的时候，则SKU信息为空。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ExIIKsrc8UBXX1SkOVFA.png" alt width="574" height="270" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">阿里巴巴国际产品接口示意图</p>
<p>倘若还有其他的平台，例如Amazon、Wish、eBay等，它们的产品接口中SKU的逻辑可能和阿里巴巴国际站一样，也可能不一样。</p>
<p>所以在设计本地的SKU产品库的时候，要考虑这种接口上的数据兼容，当平台的产品只有SPU没有SKU的时候，应该怎么与本地产品做映射。</p>
<h3>3. 产品库的展示与编辑</h3>
<p>平台上的产品管理都是以SPU的维度来管理的， 但是如果放在ERP或者仓库中，那么这种逻辑是否可以直接沿用，这个也是一个坑。</p>
<p><strong>从我一段时间的调研和体验来说，以SPU维度展示和以SKU维度展示都应该要做，因为它们适用于不同的场景。</strong></p>
<p>以SPU维度的展示可以放在基础的产品管理页面，类似于平台的产品管理。这样可以很方便的维护这些数据，编辑和查看都是从SPU的维度进去。</p>
<p>而以SKU维度的展示可以放在例如库存查询，库存流水，或者就叫做专门的“SKU产品管理”页面。可以单个的对SKU的一些信息维护，例如条形码，价格，库存信息，销售情况等。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Km1trX9YYYBMfVlkpbWI.png" alt width="611" height="273" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">SPU维度展示产品</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/lN8n5paMBGDLzetNUVQq.png" alt width="613" height="410" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">SKU维度展示产品</p>
<h3>#专栏作家#</h3>
<p>vitamin，也自称“皮酱”，微信公众号：皮酱叨逼叨。目前是一位外贸SaaS领域的供应链产品经理，曾做过3年半的跨境仓储物流方向的产品。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4806735" data-author="227259" data-avatar="http://image.woshipm.com/wp-files/2017/12/yvQWfakqo1j7mb14txHL.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            