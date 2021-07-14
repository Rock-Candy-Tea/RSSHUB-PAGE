
---
title: '国内报价-APP时间加速'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40693ef2b3624a6d82f2de1b8f470f8e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 01:45:17 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40693ef2b3624a6d82f2de1b8f470f8e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40693ef2b3624a6d82f2de1b8f470f8e~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>崔迅</strong></p>
</blockquote>
<p>2016年加入去哪儿网，负责国内机票报价搜索系统的维护工作，有丰富的搜索系统性能优化经验。现主要负责业务风控业务。</p>
<h2 data-id="heading-0">背景</h2>
<p>2018-2019 年是机票业务飞速发展的一年，在新增辅营、学生票等新尝试后，业务量屡创新高。随之而来的是请求量的增高及计算复杂度的攀升。从而导致整体报价的响应时间严重恶化。
仅上半年，搜索时长便从200ms上涨至350ms左右。</p>
<p>监控表现如下：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f05e7faf0a04ebfba18189ccd8174e4~tplv-k3u1fbpfcp-watermark.image" alt="2.jpg" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0ab427c705e403fa4564377b50396da~tplv-k3u1fbpfcp-watermark.image" alt="3.jpg" loading="lazy" referrerpolicy="no-referrer">
本文主要描述围绕响应时间超长问题做的几项尝试。</p>
<h2 data-id="heading-1">基础概念及分析</h2>
<h3 data-id="heading-2">结构</h3>
<p>国内报价的系统结构，如图所示：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3494e5a13654184b0af0f0ac8df1aa6~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer">
总体可以分为三层</p>
<p><strong>主系统</strong></p>
<p>作为用户触发搜索的入口，主要做报价数据的整合。如:
报价数据结构的适配，从代理商维度→ 航班维度。
不同数据源报价的整合，如：基础代理商报价/机酒报价/会员报价/大交通报价等等。
服务包/会员服务/酒店券等辅营商品的获取。
对报价做立减/返现等营销活动的处理。</p>
<p><strong>报价支撑</strong></p>
<p>主要进行基础报价的聚合以及进行报价的选举
基础代理商报价的存储及更新。
通过业务规则选举出每个航线的报价最优解。</p>
<p><strong>报价源</strong></p>
<p>主要根据 av/fd 等机票基础信息和报价源计算出基础报价。基础报价数据源主要分成两部分：
运价直连，主要由代理商提供的接口提供，如:航司旗舰店/携程等等。
政策报价，依赖于代理商运营的录入，将代理商的报价信息转化为政策由航司运营录入到 tts 政策系统中。
报价源的时间瓶颈主要是在代理商侧，极难通过限制时间来限制代理商报价的录入，所以主要针对主系统和报价支撑这两个系统做优化。</p>
<p><strong>主要优化方向</strong></p>
<p>提起时间优化，一般可能考虑的都是进行代码重构，性能优化，服务拆分等。但实际从业务中发现，主要耗时其实是在业务或代码结构的不合理导致的，对比而言业务结构的调整优化性价比会很高。
本文会通过对主系统及报价支撑层的优化来介绍在国内报价在时间优化上的一些尝试。</p>
<h3 data-id="heading-3">主系统</h3>
<p>主系统主要是做报价信息的聚合。基本结构如图所示
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcdfeb7ef7ef4f11933c1786a373d312~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>分析可知耗时主要由获取拓展信息与基础报价两部分组成，其余的部分主要做数据结构的转换，优化空间有限。
所以针对获取拓展信息及获取基础报价这两部分进行优化。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0df4d5f2db9d4a3280311e238321e3e8~tplv-k3u1fbpfcp-watermark.image" alt="6.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将一些全局数据的请求提前，减少阻塞等待时间。同时对数据变动不大的数据如：运价数据/航班信息等做本地缓存，提高查询速度。</p>
<h3 data-id="heading-4">搜索结构的变化</h3>
<p>机票搜索分为 list 页搜索及 ota 页的搜索，两种的区别主要是搜索结果的不同，
list 搜索返回的是所有航班的报价信息，每个航班只展示最低价。
ota 搜索返回某一航班的所有报价信息，会展示其所有的报价及标签/辅营等拓展信息。
在原有结构中， ota/list 的区分只有在主系统中存在，在报价支撑层中，没有 list/ota 的概念。
而且因为对于冷门/热门航线，航班的数量也不一致。所以导致热门航线的请求时间会更长（计算量比较大）。
由此是否可以考虑对报价支撑层做业务区分，即：报价支撑层在 ota 搜索时只计算一个航班的报价。</p>
<ul>
<li>优点：ota 搜索只搜索一个航班，对于总体而言计算量会很低（几百个航班 → 一个），响应时间大大降低。</li>
</ul>
<p>计算量基本固定，不会因热门/冷门航线出现大长尾的现象发生。</p>
<ul>
<li>存在的问题：报价支撑层提供的是某一个航线全量数据的缓存，增加 ota 维度，可能导致原有航线维度的缓存新鲜度降低。</li>
</ul>
<p>ota 维度的请求需要实时计算，无法复用原有航线维度缓存。</p>
<ul>
<li>调研:list 搜索与 ota 搜索量的对比大概是 300:1 ，减少 ota 搜索的缓存补充对缓存的新鲜度不会造成很大的影响。</li>
</ul>
<p>单独构建 ota 维度的缓存，独立使用。但大概会增加 10g 左右的 redis 占用(成本可接受)。</p>
<h3 data-id="heading-5">效果</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d08caa6f1c624ba2b26175c21e2fea55~tplv-k3u1fbpfcp-watermark.image" alt="7.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总体平均时间降低了 40% 左右，从 400ms→ 230ms 。</p>
<h3 data-id="heading-6">报价支撑层</h3>
<p>报价支撑层主要承担存储报价以及选举最优报价的功能。
报价数据获取：需要获取全量代理商报价，如果过期则要请求代理商接口获取报价。但代理接口时间不可控。
报价选举：需要从全量代理商报价中，获取每条航线的最优报价。如果代理商报价量越多，则计算时间越长。
基本结构如下：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05abe39f0d7b43e3865cb6d8b2e9626e~tplv-k3u1fbpfcp-watermark.image" alt="8.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">针对选举逻辑的优化</h3>
<p>在进行优化前，先大概计算下一次选举计算量。假如某一次搜索航线有 50 个航班，每个航班有 30 个产品，每个产品有 40 个代理商报价，要每个产品选举出最优报价需要进行 30<em>40</em>50=60000 次计算。
但每次的搜索的航班是固定的，代理商的报价量也是固定的，所以我们的目标是要减少要计算的报价产品的数量。如果从 40 个产品-> 20 个产品，总体计算量就降低 50% 。
机票的报价产品按照展示可以分成有三类：
普通报价产品，可以展示在单程/联程/往返。
只展示在往返或只展示在联程渠道的报价。
不会展示给用户，但会根据业务进行二次加工的报价。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/527b6632d9e54e90a2361b6e719b7bd3~tplv-k3u1fbpfcp-watermark.image" alt="9.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>针对此种情况，可以对产品类型进行拆分，分类为：单程/联程/往返，只计算渠道独有的产品类型，由此来减少计算量。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dea4fe26fe474855a1e96f6cd66e6f5e~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对每个业务场景只选举对应的产品报价，减少计算量，以此来减少时间的消耗。</p>
<h3 data-id="heading-8">效果</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc187b472d6040df99e0c84f9675f163~tplv-k3u1fbpfcp-watermark.image" alt="11.jpg" loading="lazy" referrerpolicy="no-referrer">
单程的平均时间从 250ms → 200ms 。</p>
<h3 data-id="heading-9">全量报价获取</h3>
<p>目前全量报价都是以代理商维度缓存在 redis 中，为了保证报价的新鲜度，每次搜索都需要校验报价是否为有效状态。
基本结构如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7114c352d37b492da5a82cb13fe61ed1~tplv-k3u1fbpfcp-watermark.image" alt="12.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>主要耗时是在阻塞等待结果的环节。但此环节主要是由代理商来确定，如果因为某些代理商的响应时间非常长，会导致整体获取报价的时间出现大长尾的现象。
方案如下：
针对大长尾的代理商做熔断机制，多次超时则熔断，不允许展示。
时间限制/回数比例等参数做调优，解决不合理配置导致时间过长的问题。
先返回过期报价，异步请求有效报价替换过期报价。
但此方案会产生问题：代理商缺失或者报价不及时，是否会导致低价的缺失或者变价?
针对这个问题，进行了线上调研。
结论：
返回过期报价对线上的低价影响较大，此方案不能采用。
只进行熔断及回数比例等调整后，只有个位数的请求低价有变化，基本无业务影响。
此优化只针对第一次搜索，不会影响第二次搜索，影响面很小。
综上所述，总体对业务的影响极低，基本无影响。</p>
<h3 data-id="heading-10">效果</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/069cfc443d3f4cb49c2446e27853afe8~tplv-k3u1fbpfcp-watermark.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer">
单程 wbd 搜索时间，从 280ms→ 200ms 左右。</p>
<h2 data-id="heading-11">总结</h2>
<p>本文主要是以业务为介入点，结合系统结构去优化总体响应时间。
结合业务做时间优化，需要非常熟悉业务和系统的整体结构，但同时效果也比较明显，较少的投入就可以得到很好的效果。
同时加上技术上的优化比如：异步请求去重/数据压缩/序列化方式的选取/ gc 方式调优等，来达到整体时间降低的目的。</p></div>  
</div>
            