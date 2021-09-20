
---
title: '案例：如何用SQL分析电商用户行为数据'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/xfu6l4D6ff3NDWJ3lfqX.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 25 Sep 2020 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/xfu6l4D6ff3NDWJ3lfqX.jpg'
---

<div>   
<blockquote><p>编辑导语：在日常工作中，经常会用到数据分析的方法，数据分析可以帮助我们快速清晰的了解目前数据走向，也可以对用户的活跃度和转化度进行分析；本文作者以“淘宝用户行为数据集”为例，用SQL进行分析，我们一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4197914" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/xfu6l4D6ff3NDWJ3lfqX.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>笔者之前主要是做增长方向的，平时工作中主要基于问题做数据分析，大部分时候都是怎么快怎么来，很少有各种工具、各种分析方法全来一遍的；所以本次借分析“淘宝用户行为数据集”为案例，梳理一下自己的数据分析技能。</p>
<p>本文以“淘宝用户行为数据集”的分析全过程为例，展示数据分析的全过程。</p>
<ul>
<li>使用工具：MySQL、Excel、Navicat、PowerBI；</li>
<li>数据来源：阿里天池实验室-淘宝用户行为数据集；</li>
<li>分析类型：描述分析、诊断分析；</li>
<li>分析方法：漏斗分析、用户路径分析、RFM用户价值分析、活跃/存留分析、帕累托分析、假设验证分析。</li>
</ul>
<p>目录如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/MCvb0mmv5GVPKEDS8GNu.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1237" height="auto" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、分析流程和方法</h2>
<h3>1. 数据分析类型</h3>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/rvGgtEoSPgQnaXpoJYmX.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1070" height="auto" referrerpolicy="no-referrer"></p>
<p>当没有清晰的数据看板时我们需要先清洗杂乱的数据，基于分析模型做可视化，搭建描述性的数据看板。</p>
<p>在没有很明确问题或问题很多很复杂的情况下，直接看杂乱的源数据不仅效率很低，也很难得到有价值的信息。</p>
<p>然后基于描述性的数据挖掘问题，提出假设做优化，或者基于用户特征数据进行预测分析找规律，基于规律设计策略。</p>
<p>简单来说：</p>
<ul>
<li>描述性分析就是：“画地图”；</li>
<li>诊断性分析就是：“找问题”；</li>
<li>预测性分析就是：“找规律”；</li>
</ul>
<h3>2. 数据分析的两个典型场景</h3>
<p>在数据分析中有两个典型的场景：</p>
<p>一种是有数据，没有问题，需要先整体分析数据，然后再根据初步的描述分析，挖掘问题做诊断性分析，提出假设，设计策略解决问题。</p>
<p>另一种是已经发现了问题，或者已经有了假设，这种做数据分析更偏向于验证假设。</p>
<h2 id="toc-2">二、淘宝用户行为分析</h2>
<p>本次是对“淘宝用户行为数据集”进行分析，在分析之前我们并不知道有什么问题，所以需要先进行描述性分析，分析数据挖掘问题。</p>
<h3>1. 解读元数据</h3>
<p>我们首先来看下这个数据集的元数据：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/PF9hHRK4rQBgJKGRzlZw.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1049" height="auto" referrerpolicy="no-referrer"></p>
<p>数据集包含了2017年11月25日至2017年12月3日之间，有行为的约一百万随机用户的所有行为（行为包括四种：点击商品详情页、购买商品、将商品放入购物车、收藏商品）。</p>
<p>数据集的每一行表示一条用户行为，由用户ID、商品ID、商品类目ID、行为类型和时间戳组成，并以逗号分隔。</p>
<p>本数据集包含：用户数量987994、商品数量4162024、商品类目数量9439；所有行为数量100150807。</p>
<h3>2. 选择分析方法</h3>
<p>根据以上数据字段我们可以拿用户行为为主轴从纵深方向提出一些问题，然后再从数据中找答案</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/25aysKMRjtfGTlbyBvEY.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1210" height="auto" referrerpolicy="no-referrer"></p>
<p>纵向：</p>
<ul>
<li>这个数据集中用户的日活跃和周活跃时间有什么规律吗？</li>
<li>在当日活跃的用户次日、三日、四日……还有多少活跃？</li>
</ul>
<p>深向：</p>
<ul>
<li>用户从浏览到购买的整体转化率怎么样？</li>
<li>用户从浏览到购买的路径是怎么样子的？</li>
<li>平台主要会给用户推送什么商品？</li>
<li>用户喜欢什么类目？喜欢什么商品？</li>
<li>怎么判断哪些是高价值用户 ？</li>
</ul>
<p>下面是叮当整理的常用分析方法：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/DGHZkHtUlrGxSPcOR8SH.png" alt="如何用SQL分析电商用户行为数据（案例）" width="713" height="auto" referrerpolicy="no-referrer"></p>
<p>我们可以给前面的问题匹配一下分析方法，便于后面的分析：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/R7ok1opX5iKG7t5TSRLA.png" alt="如何用SQL分析电商用户行为数据（案例）" referrerpolicy="no-referrer"></p>
<h3>3. 数据清洗</h3>
<p>为了便于后面的数据分析，在分析之前我们需要先对做一下清洗。</p>
<p>1）数据预处理</p>
<p>看元数据（字段解释，数据来源，数据类型，数据量……）初步发现问题为之后的处理做准备。</p>
<p>数据导入：由于整体数据集有100W+条数据，导入太慢，本次仅导入10W条分析。</p>
<p>添加列名：数据导入时默认使用第一行数据作为列名，由于本数据集没有列名，需要添加。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/XwidmkZYNueOO8hN0E0d.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1285" height="auto" referrerpolicy="no-referrer"></p>
<p>2）缺失值清洗</p>
<p>确定缺失值范围，去除不需要字段，填充缺失内容。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/4gVAZLaAIfUy6luZYWY1.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1283" height="441" referrerpolicy="no-referrer"></p>
<p>3）格式内容清洗</p>
<p>根据元数据格式和后续分析需要的格式对数据进行处理。</p>
<p>timestamps字段是时间戳字符类型，而后面要做存留分析和用户活跃时间段需要用到时间戳中的日期字段和时间字段，在这里需要提前分下列。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/LMW6uSL95AcSMBnIGqxB.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1240" height="284" referrerpolicy="no-referrer"></p>
<p>4）逻辑错误清洗</p>
<p>去除重复值，异常值。</p>
<p>去除重复值：并把用户ID、商品ID、时间戳设置为主键。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/f6JsfZ57t4LkXxWDgaFy.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1123" height="330" referrerpolicy="no-referrer"></p>
<p>异常值处理：查询并删除2017年11月25日至2017年12月3日之外的数据。</p>
<p>剔除不在本次分析范围的数据。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/R9gqJ7sIQRMzQ3G7QZuo.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1201" height="auto" referrerpolicy="no-referrer"></p>
<p>查询并删除小于2017-11-25的。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/gFkw4UGgqaqYrhMSJTYa.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1209" height="357" referrerpolicy="no-referrer"></p>
<p>验证数据：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/PXkUJ7hzEXu5jlA8go7c.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1259" height="386" referrerpolicy="no-referrer"></p>
<h3>4. 描述分析</h3>
<p>1）这个数据集中用户的日活跃和周活跃时间有什么规律吗？</p>
<p>分析思路：</p>
<p>从“时间戳“字段中抽取出“日期”和“小时”的数据，创建一个“活跃时间”字段，并从“行为类型”中用分组方式把用户的“浏览”“收藏”“加购物车”“购买”行为抽离出来，组成一个视图表，导出到Excel中用透视表分析用户的日活跃规律和周活跃规律。</p>
<p>SQL提数：</p>
<p>增加活跃时间字段。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/JM9pA9KeLXtSXSmc2qcD.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1253" height="auto" referrerpolicy="no-referrer"></p>
<p>查询用户 活跃时间分布，并创建视图。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/AIP04v87sYrv2PGhKCIy.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1258" height="473" referrerpolicy="no-referrer"></p>
<p>Excel可视化：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/iT9pEyTtTfDhgtrcQwOc.png" alt="如何用SQL分析电商用户行为数据（案例）" width="691" height="343" referrerpolicy="no-referrer"></p>
<p>活跃曲线整体为上升状态，同为周六日，12月2号、3号相比11月25日、26日活跃度更高。</p>
<p>是否是用户增长带来的？</p>
<p>用户在周六周日相比其他时间更活跃（周六周日为休息日，用户有更多时间。）</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/YHXGXGKlN0HHMeerWqzQ.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1036" height="auto" referrerpolicy="no-referrer"></p>
<p>一天内用户活跃的最高峰期为21点（用户在这个时间段空闲较多。）</p>
<p>正常工作职场工作者的睡前时间，996的应该也下班啦。</p>
<p>2）在当日活跃的用户次日、三日、四日……还有多少活跃？</p>
<p>分析思路：</p>
<p>用户存留的分析可以分为“新用户存留”和“活跃用户存留”。</p>
<p>新用户存留一般指：新注册用户在一定时间周期内还会不会再登录。</p>
<p>活跃用户存留需要根据产品类型和用户场景选择“关键行为”和选择“时间周期”。</p>
<ul>
<li>关键行为：淘宝作为购物网站，用户浏览，收藏，加购，购买商品与交易行为高度相关都可作为关键行为。</li>
<li>时间周期：淘宝拥有海量的SKU，基本可以满足用户各方面的需求，理论上用户每天都有购买需求，时间周期可以按天。</li>
</ul>
<p>SO，实际上这个问题就是在求，数据集第一日在APP有关键行为的用户在第二天、第三天……还会继续在APP中有关键行为的用户占比。</p>
<p>我们需要先列出每用户每天及当天后面又活跃的日期，用于后面求次日存留，三日存留……之后按日期对用户进行分组，并抽取之后9天依然活跃的用户数量；最后用活跃用户表中后续活跃用户除首日活跃数量乘100加%号。</p>
<p>SQL提数：</p>
<p>列出每用户每天及当天后面又活跃的日期，并创建“活跃时间间隔表”用于后面求次日存留、三日存留……。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/ZtfTwPshNCwy612nOo2Y.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1281" height="286" referrerpolicy="no-referrer"></p>
<p>对“活跃时间间隔表视图”引用进行分组统计，计算每日存留人数并创建视图。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/mWQQoxdq2BT3xZfpgL4t.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1228" height="auto" referrerpolicy="no-referrer"></p>
<p>对存留人数表进行计算，统计活跃用户留存率。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/ZEcx8NOWEAMGrflDz1iv.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1229" height="755" referrerpolicy="no-referrer"></p>
<p>Excel可视化：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/SJUtw5K6cIK3KFTyknas.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1146" height="auto" referrerpolicy="no-referrer"></p>
<ul>
<li>用户增长：从2017年11月15日致2017年12月3日，活跃用户新增38%；</li>
<li>存留增长：从2017年11月15日致2017年12月3日，活跃用户次日留存增长18.67%，当日的活跃用户留存也在快速增长，第七日留存比次日留存高18.56%。</li>
</ul>
<p>假设随时间增长的留存率提升来源于新dau提升策略的优化，后续存留的提升来源于召回策略的优化。</p>
<p>3）用户从浏览到购买的整体转化率怎么样？</p>
<p>分析思路：</p>
<p>将数据集中按不同用户，不同商品维度进行分组获得某一用户行为对某一商品不同行为的数据；然后对“用户行为漏斗表”中的浏览、加购物车、收藏、购买行为进行分组统计。</p>
<p>SQL提数：</p>
<p>把各种用户行为分离出来并创建视图方便后续查询用户行为数据。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/drc2gVo2BFUa7hPORVZi.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1213" height="517" referrerpolicy="no-referrer"></p>
<p>查询整体数据漏斗。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/0CxihUexDwb2HBlAdNdd.png" alt="如何用SQL分析电商用户行为数据（案例）" width="970" height="283" referrerpolicy="no-referrer"></p>
<p>Excel可视化：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/ZaRaRJrGllgdaehexQ3J.png" alt="如何用SQL分析电商用户行为数据（案例）" width="669" height="401" referrerpolicy="no-referrer"></p>
<p>用户从浏览到购买整体转化率2.3%，具体主要在哪个环节流失还需要再细分用户路径分析。</p>
<p>4）用户从浏览到购买的路径是怎么样子的？</p>
<p>分析思路：</p>
<p>穷举所有可能的用户路径，引用“用户行为漏斗表”视图，计在数据中点击行为大于0，购买行为大于0，其他两项为0，则判定本用户购买路径为；点击—购买，其他路径同理，多次查询并用Excel表记录查询数据，用户PowerBI桑基图做可视化。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/51qw49ndHpNTYKbzMyA1.png" alt="如何用SQL分析电商用户行为数据（案例）" width="452" height="auto" referrerpolicy="no-referrer"></p>
<p>SQL提数：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/Us8P8xpNS8pivTeKdI5g.png" alt="如何用SQL分析电商用户行为数据（案例）" width="913" height="auto" referrerpolicy="no-referrer"></p>
<p>PowerBI可视化：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/NZ50vokRvBfJcnWzRBnz.png" alt="如何用SQL分析电商用户行为数据（案例）" width="845" height="auto" referrerpolicy="no-referrer"></p>
<p>用户从浏览到购买的路径主要有4条，路径越长转化率越低：</p>
<ul>
<li>路径1：浏览→购买：转化率1.45%；</li>
<li>路径2：浏览→加购物车→购买：转化率0.33；</li>
<li>路径3：浏览→收藏→购买：转化率0.11%；</li>
<li>路径4：浏览→收藏→加购物车→购买：转化率0.03%；</li>
</ul>
<p>以上转化率等于起始路径到购买的转化</p>
<p>5）平台主要给用户推送什么商品？</p>
<p>分析思路：</p>
<p>虽然我们没法直接从数据中找到平台推送的数据，但作为平台流量倾斜的商品，浏览量一般都会比其他商品的浏览量高一些；我们可以引用“用户行为漏斗表”视图统计浏览量前100的商品及其类目。</p>
<p>SQL提数：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/KpmityklgBf7ZxIDVC6S.png" alt="如何用SQL分析电商用户行为数据（案例）" width="964" height="322" referrerpolicy="no-referrer"></p>
<p>Excel可视化：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/0CCh3bTZ7BRi3okoV8rL.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1081" height="504" referrerpolicy="no-referrer"></p>
<p>描述性分析：</p>
<p>浏览量top100的商品浏览量呈阶梯分布，越靠前的阶梯之间的落差相对越大在这个阶梯中的商品越少，越靠后商品浏览量阶梯之间的落差相对越小，同阶梯内的商品越多。</p>
<p>是否是用于淘宝流量分配规则的原因造成的？（假设淘宝的规则是给所有商品分配的初始流量是一样的，后期这些商品中那些商品转化率高就给哪些商品更多曝光。）</p>
<p>浏览量TOP100的商品所属类目中，4756105、3607361、4357323三个类目浏览量远超其他类目。</p>
<p>这个几个类目商品类型是否是高频刚需类型的呢？</p>
<p>6）用户喜欢什么商品？</p>
<p>分析思路：</p>
<p>找高转化率的商品（销量高的有可能只是低价或者流量大）。</p>
<p>SQL提数：</p>
<p>查询计算商品转化率，升序排列，取前100个。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/NR3tWFIHvgrSgSszcA11.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1085" height="375" referrerpolicy="no-referrer"></p>
<p>Excel可视化：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/U06jHPRc6GJRcnj2yjx7.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1127" height="527" referrerpolicy="no-referrer"></p>
<p>描述性分析：</p>
<p>从商品看：有17款商品转化率超过了1。</p>
<p>是否是由于用户直接从购物车或者商品收藏直接复购，未点击商详？</p>
<p>从类目看：这些商品所属类目分布均匀，除965809、4801426、2735466、2640118、5063620、4789432、2945933这7个类目之外，其他类目都只有一个商品在转化率TOP100的商品中。</p>
<p>是否是由于淘宝是根据“同一类目下的高转化商品”给用户做推荐的？</p>
<p>7）怎么判断哪些是高价值用户 ？</p>
<p>分析思路：</p>
<p>用户价值分析常用的分析方式是RFM模型。</p>
<p>RFM模型是3个指标的缩写，最近一次消费时间（R）、消费频率（F）、消费金额（M）。</p>
<p>然后给这三个指标根据价值分5个等级 ，进行打分计算分值和平均值，然后根据分值与平均值对比，分出“高”“中”“低”，综合进行用户分层。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/WzT0cB2FXXBI9hWOTUZR.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1165" height="auto" referrerpolicy="no-referrer"></p>
<p>本次分析中的R,F,M具体定义（仅用于演示分析方法，无实际业务参考价值）：</p>
<ul>
<li>R：根据用户最近一次的购买时间与2017年12月3日之间的差值，判断用户最近一次消费时间间隔；</li>
<li>F：将数据集中用户在2017年11月25日至2017年12月3日9天时间内的购买次数作为消费频率；</li>
<li>M：由于本数据集中未包含购买金额字段，暂时排除此指标。</li>
</ul>
<p>SQL取数与分析：</p>
<p>建立打分标准：先计算R,F的值，并排序，根据R,F值最大值和最小值得区间设计本次得打分标准。</p>
<p>关于打分标准：不同业务的用户消费频率、消费金额、精细化运营策略与成本……都是不同，一般常用”分位数“建立打分标准；由于SQL并不是专业得统计分析工具，计算分位数较为复杂，本次仅使用最大值和最小值的区间初略建立规则。</p>
<p>分位数：是指在统计学中把所有数值由小到大排列并分成几等份，取处于对应几个分割点位置的数值。</p>
<p>查询并计算R，F值创建视图：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/SdRi6uM7snU8gTJkbgHY.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1202" height="359" referrerpolicy="no-referrer"></p>
<p>引用RF数值表，分别查询R,F的最大值和最小值：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/NRYJnymW3TrH9iIvNcS2.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1215" height="279" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/UJSo2kwaS7LcnbAUcMap.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1292" height="auto" referrerpolicy="no-referrer"></p>
<p>结合人工浏览的建立打分标准：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/OhASQCgPvefPI6RTVlCh.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1079" height="284" referrerpolicy="no-referrer"></p>
<p>消费时间间隔：在1~8区间内四等分。</p>
<p>消费频率：由于人工 浏览时发现很少有超过20次购买的，故消费频率在20以内四等分。</p>
<p>给R，F按价值打分：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/p8EhOEStU6X0F7frmanl.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1222" height="512" referrerpolicy="no-referrer"></p>
<p>计算价值的平均值：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/7Ecz7TYEjn5zfMO9EnaX.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1134" height="223" referrerpolicy="no-referrer"></p>
<p>用平均值和用户分类规则表比较得出用户分类：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/YtdbgEqjvpWkXFOfeLv5.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1139" height="390" referrerpolicy="no-referrer"></p>
<p>查询各类用户数量：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/kC0lanzVuGCuLUDjRBfV.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1189" height="357" referrerpolicy="no-referrer"></p>
<p>Excel可视化：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/grPwqs9aCjJN5GmW030y.png" alt="如何用SQL分析电商用户行为数据（案例）" width="886" height="364" referrerpolicy="no-referrer"></p>
<p>由于缺失了商品价格部分的数据，本模块暂时没有分析结论。</p>
<h3>5. 诊断分析</h3>
<p>通过描述性分析得到可视化的数据后，我们一般会先看一下是否符合业务常识，如：假设一个页面的UV（浏览人数）比PV（浏览次数）还高，那这个数据质量肯定是有问题的。</p>
<p>如果符合常识接下来我们会通过与行业平均数据和本产品的同比环比对比看是否正常，如果不正常就要找原因，设计解决方案，如果正常那就看是否有可以优化的地方。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/UPAtUXZ5OAUjGbAfwWig.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1173" height="401" referrerpolicy="no-referrer"></p>
<p>1）诊断分析结论</p>
<p>我们首先来看一下这些描述性分析是否符合业务常识和指标是否正常：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/62a41ecDq2F7NiSLHT3m.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1177" height="530" referrerpolicy="no-referrer"></p>
<p>a. 活跃曲线整体为上升状态，同为周六日，12月2号，3号相比11月25日，26日活跃度更高。</p>
<p>正常：结合描述分析4中的活跃用户的增长。</p>
<p>b. 用户在周六周日相比其他时间更活跃。</p>
<p>正常：周六周日为休息日，用户有更多时间来刷淘宝，反映在数据上就是活跃度的增加。</p>
<p>c. 一天内用户活跃的最高峰期为21点。</p>
<p>正常：用户在这个时间段有空闲，996的都下班啦~</p>
<p>d. 从2017年11月15日致2017年12月3日，活跃用户新增38%。</p>
<p>还需验证：如果是由于新注册用户或者老用户召回策略带来的增长符合常识，具体还需结合新注册用户数据和用户召回策略数据做验证。</p>
<p>e. 从2017年11月15日致2017年12月3日，活跃用户次日留存增长18.67%，当日的活跃用户留存也在快速增长，第七日留存比次日留存高18.56%。</p>
<p>不符合常识：因为从长期来看用户都是会流失的，只是生命周期长短问题，而从淘宝的用户行为来看同批用户的存留数据竟然随着时间的增加而增加。</p>
<p>假设场景可能是这样的：用户小A注册了淘宝APP，第二天就不再登录了，而第三天收到了淘宝的推荐提醒（APP消息、短信……）；在消息中发现了自己喜欢的商品，而且还有优惠下单买了，第四天又收到了淘宝的消息，还是自己喜欢的。</p>
<p>这里的具体数据还需要结合用户生命周期运营的策略和数据做验证。</p>
<p>f. 用户从浏览到购买整体转化率2.3%。</p>
<p>正常，根据之前了解到的电商数据，多种客单价的商品（几十~几千）在一起，整体转化率在2%~3%之间，当然具体还需要结合历史的同比，环比数据取看。</p>
<p>g. 用户从浏览到购买的路径主要有4条，路径越长转化率越低。</p>
<p>正常：从流量的角度，每多一个步骤就会多一些用户流失这个符合常识。</p>
<p>h. 浏览量top100的商品浏览量呈阶梯分布，越靠前的阶梯之间的落差相对越大在这个阶梯中的商品越少，越靠后商品浏览量阶梯之间的落差相对越小，同阶梯内的商品越多。</p>
<p>待验证：假设淘宝会给高转化的爆款商品更多的曝光，商品浏览量呈金字塔分布是正常的。</p>
<p>i. 浏览量TOP100的商品所属类目中，4756105、3607361、4357323三个类目浏览量远超其他类目。</p>
<p>还需验证：抽取购买购买次数判断这个几个类目商品类型是否是高频刚需类型的呢？</p>
<p>j. 从商品看：有17款商品转化率超过了1。</p>
<p>不正常：</p>
<p>还需验证：是否是由于用户直接从购物车或者商品收藏直接复购，未点击商详？</p>
<p>k. 从类目看：这些商品所属类目分布均匀，除965809，4801426，2735466，2640118，5063620，4789432，2945933这7个类目之外，其他类目都只有一个商品在转化率TOP100的商品中。</p>
<p>还需验证：是否是由于淘宝是根据“同一类目下的高转化商品”给用户做推荐的？</p>
<p>2）假设与验证</p>
<p>根据以上诊断分析我们梳理出了以下假设，做假设验证。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/hHAiSg9yeIOr0n6pbfo0.png" alt="如何用SQL分析电商用户行为数据（案例）" width="994" height="auto" referrerpolicy="no-referrer"></p>
<p>假设1：这些商品中有高转化率的爆款商品。</p>
<p>引用“商品转化率视图”查询排名前5的商品转化率：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/Evri5e78YcbvBFXFh5cM.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1194" height="auto" referrerpolicy="no-referrer"></p>
<p>对比同类目的其他商品转化率：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/3xVZPFkWAgKRR9sYt02G.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1223" height="549" referrerpolicy="no-referrer"></p>
<p>对比浏览量TOP5的商品，发现这些商品转化率在同一类目下并不高，假设不成立。</p>
<p>假设2：4756105，3607361，4357323三个类目属于高频刚需类目。</p>
<p>抽取这几个类目的商品某买频次数据验证。</p>
<p>创建类目购买频次表：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/rM4Myez00aPgAybdYmlt.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1127" height="auto" referrerpolicy="no-referrer"></p>
<p>计算类目购买频次平均值：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/cBxGgBhUoqis9oWR2flw.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1034" height="auto" referrerpolicy="no-referrer"></p>
<p>查询4756105、3607361、4357323三个类目的购买频次：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/ntlFU1KZk47ZWqaFJp1R.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1059" height="261" referrerpolicy="no-referrer"></p>
<p>4756105、3607361、4357323三个类目的用户购买频次明显高于平均值，假设成立。</p>
<p>假设3：有部分用户是未点击商详直接从收藏和购物车购买的。</p>
<p>查询转化率超过1的商品的用户行为数据：</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/kJIY7zpniYFefKv4BYUK.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1032" height="509" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/ADoDe0ycnx9h9VQqgGOR.png" alt="如何用SQL分析电商用户行为数据（案例）" width="1025" height="auto" referrerpolicy="no-referrer"></p>
<p>用户不是直接从收藏和购物车购买的，只是后续复购未点击商详，假设不成立。</p>
<p>假设4：淘宝推荐的商品主要是“同一类目下的高转化商品”。</p>
<p>给浏览量TOP100的商品和转化率TOP100的商品做匹配看其中重合的商品有多少。</p>
<p><img data-action="zoom" class=" aligncenter" title="如何用SQL分析电商用户行为数据（案例）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/0RXDbDrcQaJWH4tGwdFb.png" alt="如何用SQL分析电商用户行为数据（案例）" width="693" height="352" referrerpolicy="no-referrer"></p>
<p>用Excel对浏览量TOP100的商品ID和转化率TOP100的商品ID进行去重，结果无重复值，假设不成立。</p>
<p>3）结论：</p>
<p>用户活跃：用户活跃曲线整体呈上升趋势，在一周中周六，周日活跃度比平时更高；在一天中用户活跃曲线从凌晨4点开始往上升，在中午12点和下午5~6点有两个小低谷（吃饭），到晚上9点时活跃度达到顶峰。</p>
<p>用户留存：从2017年11月15日致2017年12月3日的用户留存数据来看，淘宝的用户留存数据较好，活跃用户次日留存增长18.67%；当日的活跃用户留存也在快速增长，第七日留存比次日留存高18.56%。</p>
<p>用户转化：整体转化2.3%，用户从浏览到购买的路径主要有4条，路径越长转化率越低。</p>
<ul>
<li>路径1：浏览→购买：转化率1.45%；</li>
<li>路径2：浏览→加购物车→购买：转化率0.33；</li>
<li>路径3：浏览→收藏→购买：转化率0.11%；</li>
<li>路径4：浏览→收藏→加购物车→购买：转化率0.03%；</li>
</ul>
<p>平台推荐与用户偏好：从数据集中的数据来看，排除用户兴趣偏好标签，淘宝给用户用户推送的商品主要是高频刚需的类目，促使用户复购，流量回流平台。</p>
<p>以上结论受数据量和数据类型的影响，并不一定准确，仅用来练习数据分析方法。</p>
<p> </p>
<p>作者：小叮当，微信：zxxp153，公众号：叮当的成长地图</p>
<p>本文由 @小叮当v1.6 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4197429" data-author="365942" data-avatar="http://image.woshipm.com/wp-files/2019/06/pncvg2JRr0zisB5jmVOd.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            