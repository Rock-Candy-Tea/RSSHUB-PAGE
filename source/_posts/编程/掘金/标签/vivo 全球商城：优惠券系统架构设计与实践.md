
---
title: 'vivo 全球商城：优惠券系统架构设计与实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c0af190b22a43f79da142e962aedb55~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 17:37:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c0af190b22a43f79da142e962aedb55~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、业务背景</h1>
<p>优惠券是电商常见的营销手段，具有灵活的特点，既可以作为促销活动的载体，也是重要的引流入口。优惠券系统是vivo商城营销模块中一个重要组成部分，早在15年vivo商城还是单体应用时，优惠券就是其中核心模块之一。随着商城的发展及用户量的提升，优惠券做了服务拆分，成立了独立的优惠券系统，提供通用的优惠券服务。目前，优惠券系统覆盖了优惠券的4个核心要点：创、发、用、计。</p>
<ul>
<li>
<p><strong>创</strong>指优惠券的创建，包含各种券规则和使用门槛的配置。</p>
</li>
<li>
<p><strong>发</strong>指优惠券的发放，优惠券系统提供了多种发放优惠券的方式，满足针对不同人群的主动发放和被动发放。</p>
</li>
<li>
<p><strong>用</strong>指优惠券的使用，包括正向购买商品及反向退款后的优惠券回退。</p>
</li>
<li>
<p><strong>计</strong>指优惠券的统计，包括优惠券的发放数量、使用数量、使用商品等数据汇总。</p>
</li>
</ul>
<p>vivo商城优惠券系统除了提供常见的优惠券促销玩法外，还以优惠券的形式作为其他一些活动或资产的载体，比如手机类商品的保值换新、内购福利、与外部广告商合作发放优惠券等。</p>
<p>以下为vivo商城优惠券部分场景的展示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c0af190b22a43f79da142e962aedb55~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">二、系统架构及变迁</h1>
<p>优惠券最早和商城耦合在一个系统中。随着vivo商城的不断发展，营销活动力度加大，优惠券使用场景增多，优惠券系统逐渐开始“力不从心”，暴露了很多问题：</p>
<ul>
<li>
<p>海量优惠券的发放，达到优惠券单库、单表存储瓶颈。</p>
</li>
<li>
<p>与商城系统的高耦合，直接影响了商城整站接口性能。</p>
</li>
<li>
<p>优惠券的迭代更新受限于商城的版本安排。</p>
</li>
<li>
<p>针对多品类优惠券，技术层面没有沉淀通用优惠券能力。</p>
</li>
</ul>
<p>为了解决以上问题，19年优惠券系统进行了系统独立，提供通用的优惠券服务，独立后的系统架构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe1d43bcdecb4ad5b6be79bcdaa952d7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>优惠券系统独立迁移方案</strong></p>
<p>如何将优惠券从商城系统迁移出来，并兼容已对接的业务方和历史数据，也是一大技术挑战。系统迁移有两种方案：停机迁移和不停机迁移。</p>
<p>我们采用的是不停机迁移方案：</p>
<ul>
<li>迁移前，运营停止与优惠券相关的后台操作，避免产生优惠券静态数据。</li>
</ul>
<blockquote>
<p>静态数据：优惠券后台生成的数据，与用户无关。</p>
<p>动态数据：与用户有关的优惠券数据，含用户领取的券、券和订单的关系数据等。</p>
</blockquote>
<ul>
<li>
<p>配置当前数据库开关为单写，即优惠券数据写入商城库（旧库）。</p>
</li>
<li>
<p>优惠券系统上线，通过脚本迁移静态数据。迁完后，验证静态数据迁移准确性。</p>
</li>
<li>
<p>配置当前数据库开关为双写，即线上数据同时写入商城库和优惠券新库。此时服务提供的数据源依旧是商城库。</p>
</li>
<li>
<p>迁移动态数据。迁完后，验证动态数据迁移准确性。</p>
</li>
<li>
<p>切换数据源，服务提供的数据源切换到新库。验证服务是否正确，出现问题时，切换回商城数据源。</p>
</li>
<li>
<p>关闭双写，优惠券系统迁移完成。</p>
</li>
</ul>
<p>迁移后优惠券系统请求拓扑图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a99f49e3c4164919b1019e62c6e94246~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">三、系统设计</h1>
<h2 data-id="heading-3">3.1 优惠券分库分表</h2>
<p>随着优惠券发放量越来越大，单表已经达到瓶颈。为了支撑业务的发展，综合考虑，对用户优惠券数据进行分库分表。</p>
<p><strong>关键字：技术选型、分库分表因子</strong></p>
<p>分库分表有成熟的开源方案，这里不做过多介绍。参考之前项目经验，采用了公司中间件团队提供的自研框架。原理是引入自研的MyBatis的插件，根据自定义的路由策略计算不同的库表后缀，定位至相应的库表。</p>
<p>用户优惠券与用户id关联，并且用户id是贯穿整个系统的重要字段，因此使用用户id作为分库分表的路由因子。这样可以保证同一个用户路由至相同的库表，既有利于数据的聚合，也方便用户数据的查询。</p>
<p>假设共分N个库M个表，分库分表的路由策略为：</p>
<blockquote>
<p>库后缀databaseSuffix = hash(userId) / M %N</p>
<p>表后缀tableSuffix = hash(userId) % M</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e6e66c52a304ca8bd601b362d7b3b99~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">3.2 优惠券发放方式设计</h2>
<p>为满足各种不同场景的发券需求，优惠券系统提供三种发券方式：<strong>统一领券接口</strong>、<strong>后台定向发券</strong>、<strong>券码兑换发放</strong>。</p>
<h3 data-id="heading-5">3.2.1 统一领券接口</h3>
<p><strong>保证领券校验的准确性</strong></p>
<p>领券时，需要严格校验优惠券的各种属性是否满足：比如领取对象、各种限制条件等。其中，比较关键的是库存和领取数量的校验。因为在高并发的情况下，需保证数量校验的准确性，不然很容易造成用户超领。</p>
<p>存在这样的场景：A用户连续发起两次领取券C的请求，券C限制每个用户领取一张。第一次请求通过了领券数量的校验，在用户优惠券未落库的情况下，如果不做限制，第二次请求也会通过领券数量的校验。这样A用户会成功领取两张券C，造成超领。</p>
<p>为了解决这个问题，优惠券采用的是分布式锁方案，分布式锁的实现依赖于Redis。在校验用户领券数量前先尝试获取分布式锁，优惠券发放成功后释放锁，保证用户领取同一张券时不会出现超领。上面这种场景，用户第一次请求成功获取分布式锁后，直至第一次请求成功释放已获取的分布式锁或超时释放，不然用户第二次请求会获取分布式锁失败，这样保证A用户只会成功领取一张。</p>
<p><strong>库存扣减</strong></p>
<p>领券要进行库存扣减，常见库存扣减方案有两种：</p>
<blockquote>
<p>**方案一：**数据库扣减。</p>
<p>扣减库存时，直接更新数据库中库存字段。</p>
<p>该方案的<strong>优点</strong>是简单便捷，查验库存时直接查库即可获取到实时库存。且有数据库事务保证，不用考虑数据丢失和不一致的问题。</p>
<p><strong>缺点</strong>也很明显，主要有两点：</p>
<p>1）库存是数据库中的单个字段，在更新库存时，所有的请求需要等待行锁。一旦并发量大了，就会有很多请求阻塞在这里，导致请求超时，进而系统雪崩。</p>
<p>2）频繁请求数据库，比较耗时，且会大量占用数据库连接资源。</p>
</blockquote>
<blockquote>
<p>**方案二：**基于redis实现库存扣减操作。</p>
<p>将库存放到缓存中，利用redis的incrby特性来扣减库存。</p>
<p>该方案的<strong>优点</strong>是突破数据库的瓶颈，速度快，性能高。</p>
<p><strong>缺点</strong>是系统流程会比较复杂，而且需要考虑缓存丢失或宕机数据恢复的问题，容易造成库存数据不一致。</p>
</blockquote>
<p>从优惠券系统当前及可预见未来的流量峰值、系统维护性、实用性上综合考虑，优惠券系统采用了方案一的改进方案。改进方案是将单库存字段分散成多库存字段，分散数据库的行锁，减少并发量大的情况数据库的行锁瓶颈。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eca20a48766a4fa5a89643389c73654e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>库存数更新后，会将库存平均分配成M份，初始化更新到库存记录表中。用户领券，随机选取库存记录表中已分配的某一库存字段（共M个）进行更新，更新成功即为库存扣减成功。同时，定时任务会定期同步已领取的库存数。相比方案一，该方案突破了数据库单行锁的瓶颈限制，且实现简单，不用考虑数据丢失和不一致的问题。</p>
<p><strong>一键领取多张券</strong></p>
<p>在对接的业务方的领券场景中，存在用户一键领取多张券的情形。因此统一领券接口需要支持用户一键领券，除了领取同一券模板的多张，也支持领取不同券模板的多张。一般来说，一键领取多张券指领取不同券模板的多张。在实现过程中，需要注意以下几点：</p>
<p><strong>1）如何保证性能</strong></p>
<p>领取多张券，如果每张券分别进行校验、库存扣减、入库，那么接口性能的瓶颈卡在券的数量上，数量越多，性能直线下降。那么在券数量多的情况下，怎么保证高性能呢？主要采取两个措施：</p>
<blockquote>
<p>a. <strong>批量操作</strong>。</p>
<p>从发券流程来看，瓶颈在于券的入库。领券是实时的（异步的话，不能实时将券发到用户账户下，影响到用户的体验还有券的转化率），券越多，入库时与数据库的IO次数越多，性能越差。批量入库可以保证与数据库的IO的次数只有一次，不受券的数量影响。如上所述，用户优惠券数据做了分库分表，同一用户的优惠券资产保存在同一库表中，因此同一用户可实现批量入库。</p>
<p>b. <strong>限制单次领券数量</strong>。</p>
<p>设置阀值，超出数量后，直接返回，保证系统在安全范围内。</p>
</blockquote>
<p><strong>2）保证高并发情况下，用户不会超领</strong></p>
<p>假如用户在商城发起请求，一键领取A/B/C/D四张券，同时活动系统给用户发放券A，这两个领券请求是同时的。其中，券A限制了每个用户只能领取一张。按照前述采用分布式锁保证校验的准确性，两次请求的分布式锁的key分别为：</p>
<blockquote>
<p>用户id+A_id+B_id+C_id+D_id</p>
<p>用户id+A_id</p>
</blockquote>
<p>这种情况下，两次请求的分布式锁并没有发挥作用，因为锁key是不同，数量校验依旧存在错误的可能性。为避免批量领券过程中用户超领现象的发生，在批量领券过程中，对分布锁的获取进行了改造。上例一键领取A/B/C/D四张券，需要批量获取4个分布式锁，锁key为：</p>
<blockquote>
<p>用户id+A_id</p>
<p>用户id+B_id</p>
<p>用户id+C_id</p>
<p>用户id+D_id</p>
</blockquote>
<p>获取其中任何一个锁失败，即表明此时该用户正在领取其中某一张券，需要自旋等待（在超时时间内）。获取所有的分布式锁成功，才可以进行下一步。</p>
<p><strong>接口幂等性</strong></p>
<p>统一领券接口需保证幂等性（幂等性：用户对于同一操作发起的一次请求或者多次请求的结果是一致的）。在网络超时、异常情况下，领券结果没有及时返回，业务方会进行领券重试。如果接口不保证幂等性，会造成超发。幂等性的实现有多种方案，优惠券系统利用数据库的唯一索引来保证幂等。</p>
<p>领券最早是不支持幂等性的，表设计没有考虑幂等性。</p>
<p>那么<strong>第一个需要考虑的问题：在哪个表来添加唯一索引呢？</strong></p>
<p>无非两种方案：现有的表或者新建表。</p>
<ul>
<li>
<p>采用现有的表，不需要增加表的关联。但如上所述，因为做了分库分表，大量的表需要添加唯一字段，并且需要兼容历史数据，需要保证历史数据新增字段的唯一性。</p>
</li>
<li>
<p>采用新建表这种方式，不需要兼容历史数据，但缺陷也很明显，增加了一层表的关联，对性能和现有逻辑都有很大影响。综合考虑，我们选取了在现有表添加唯一字段这种方式，这样更利于保证性能和后续的维护性。</p>
</li>
</ul>
<p>**第二个考虑的问题：怎么兼容历史数据和业务方？**历史数据增加了唯一字段，需要填入唯一值，不然无法添加唯一索引。我们采用脚本刷数据的方式，构造唯一值并刷新到每一行历史数据中。优惠券已对接的业务方没有传入唯一编码，针对这种情况，优惠券侧生成唯一编码作为替代，保证兼容性。</p>
<h3 data-id="heading-6">3.2.2 定向发券</h3>
<p>定向发券用于运营在后台针对特定人群进行发券。定向发券可以弥补用户主动领券，人群覆盖不精准、覆盖面不广的问题。通过定向发券，可以精准覆盖特定人群，提高下单转化率。在大促期间，大范围人群的定向发券还可以承载活动push和降价促销双重任务。</p>
<p>定向发券主要在于人群的圈选和发券流程的设计，整体流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee40873e93d14594869e924cc2410f30~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>定向发券不同于用户主动领券，定向发券的量通常会很大（亿级）。为了支撑大批量的定向发券，定向发券做了一些优化：</p>
<p><strong>1）去除事务</strong>。事务逻辑过重，对于定向发券来说没必要。发券失败，记录失败的券，保证失败可以重试。</p>
<p><strong>2）轻量化校验</strong>。定向发券限制了券类型，通过限制配置的方式规避需严格校验属性的配置。不同于用户主动领券校验逻辑的冗长，定向发券的校验非常轻量，大大提升发券性能。</p>
<p><strong>3）批量插入</strong>。批量券插入减少数据库IO次数，消除数据库瓶颈，提升发券速度。定向发券是针对不同的用户，用户优惠券做了分库分表，为了实现批量插入，需要在内存中先计算出不同用户对应的库表后缀，数据归集后再批量插入，最多插入M次，M为库表总个数。</p>
<p><strong>4）核心参数可动态配置</strong>。比如单次发券数量，单次读库数量，发给消息中心的消息体包含的用户数量等，可以控制定向发券的峰值速度和平均速度。</p>
<h3 data-id="heading-7"><strong>3.2.3 券码兑换</strong></h3>
<p>站外营销券的发放方式与其他券不同，通过券码进行兑换。券码由后台导出，通过短信或者活动的方式发放到用户，用户根据券码兑换后获取相应的券。券码的组成有一定的规则，在规则的基础上要保证安全性，这种安全性主要是券码校验的准确性，防止已兑换券码的再次兑换和无效券码的恶意兑换。</p>
<h2 data-id="heading-8">3.3 精细化营销能力设计</h2>
<p>通过标签组合配置的方式，优惠券提供精细化营销的能力，以实现优惠券的千人千面。标签可分为准实时和实时，值得注意的是，一些实时的标签的处理需要前提条件，比如地区属性需要用户授权。</p>
<p>优惠券的精准触达：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0dd6bdb51474d1a89e85b4282340d91~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">3.4 券和商品之间的关系</h2>
<p>优惠券的使用需要和商品关联，可关联所有商品，也可以关联部分商品。为了灵活性地满足运营对于券关联商品的配置，优惠券系统有两种关联方式：</p>
<blockquote>
<p>a. 黑名单。</p>
<p>可用商品 = 全部商品 - 黑名单商品。</p>
<p>黑名单适用于券的可使用商品范围比较广这种情况，全部商品排除掉黑名单商品就是券的可使用范围。</p>
<p>b. 白名单。</p>
<p>可用商品 = 白名单商品。</p>
<p>白名单适用于券的可使用商品范围比较小这种情况，直接配置券的可使用商品。</p>
</blockquote>
<p>除此以外，还有超级黑名单的配置，黑名单和白名单只对单个券有效，超级黑名单对所有券有效。当前优惠券系统提供商品级的关联，后续优惠券会支持商品分类维度的关联，分类维度 + 商品维度可以更灵活地关联优惠券和商品。</p>
<h2 data-id="heading-10">3.5 高性能保证</h2>
<p>优惠券对接系统多，存在高流量场景，优惠券对外提供接口需保证高性能和高稳定性。</p>
<p><strong>多级缓存</strong></p>
<p>为了提升查询速度，减轻数据库的压力，同时为了应对瞬时高流量带来热点key的场景（比如发布会直播结束切换流量至特定商品商详页、热点活动商品商详页都会给优惠券系统带来瞬时高流量），优惠券采用了多级缓存的方式。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94c4b77641b64605aa58db174cf53cc0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>数据库读写分离</strong></p>
<p>优惠券除了上述所说的分库分表外，在此基础上还做了读写分离操作。主库负责执行数据更新请求，然后将数据变更实时同步到所有从库，用从库来分担查询请求，解决数据库写入影响查询的问题。主从同步存在延迟，正常情况下延迟不超过1ms，优惠券的领取或状态变更存在一个耗时的过程，主从延迟对于用户来说无感知。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7dbdc2fe8c0489ca93d8919b0653e0f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>依赖外部接口隔离熔断</strong></p>
<p>优惠券内部依赖了第三方的系统，为了防止因为依赖方服务不可用，产生连锁效应，最终导致优惠券服务雪崩的事情发生，优惠券对依赖外部接口做了隔离和熔断。</p>
<p><strong>用户维度优惠券字段冗余</strong></p>
<p>查询用户相关的优惠券数据是优惠券最频繁的查询操作之一，用户优惠券数据做了分库分表，在查询时无法关联券规则表进行查询，为了减少IO次数，用户优惠券表中冗余了部分券规则的字段。优惠券规则表字段较多，冗余的字段不能很多，要在性能和字段数之间做好平衡。</p>
<h1 data-id="heading-11">四、总结及展望</h1>
<p>最后对优惠券系统进行一个总结：</p>
<ul>
<li>
<p>不停机迁移，平稳过渡。自独立后已稳定运行2年，性能足以支撑vivo商城未来3-5年的高速发展。</p>
</li>
<li>
<p>系统解耦，迭代效率大幅提升。</p>
</li>
<li>
<p>针对业务问题，原则是选择合适实用的方案。</p>
</li>
<li>
<p>具备完善的优惠券业务能力。</p>
</li>
</ul>
<p>展望：目前优惠券系统主要服务于vivo商城，未来我们希望将优惠券能力开放，为内部其他业务方提供通用一体化的优惠券平台。</p>
<blockquote>
<p>作者：vivo互联网开发团队-Yan Chao</p>
</blockquote></div>  
</div>
            