
---
title: '开源独立站 OpenCart 中文更新 _ 营销推广功能（第 7 期）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.opencart.cn/storage/uploads/image/2022/04/25/af3aad3d73a029676b1f3896753a2f01.png'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 15:02:00 GMT
thumbnail: 'https://www.opencart.cn/storage/uploads/image/2022/04/25/af3aad3d73a029676b1f3896753a2f01.png'
---

<div>   
<div class="content">
                                                                                            <p>点击头像&关注<strong>OpenCart中文</strong></p> 
<p style="margin-left:0; margin-right:0">旗下产品——OpenCart免费版、OpenCart国际专业版、OpenCart中文专业版、OpenCart专业版多商家</p> 
<p style="margin-left:0; margin-right:0"><strong>前言</strong></p> 
<p style="margin-left:0; margin-right:0">在电商运营中，最常见的手段就是各种形式的促销手段。它的规则多样，对提高客单价和客单量有很大的帮助。</p> 
<p style="margin-left:0; margin-right:0">接下来我们来看看开源独立站OpenCart3.8的营销推广有哪些方式</p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>01、推广会员功能</strong></p> 
<p style="margin-left:0; margin-right:0">——又称联盟会员，主要用于发展下级获取佣金</p> 
<p style="margin-left:0; margin-right:0">联盟账户佣金设置比例后，当普通用户变成推广会员后，佣金比例会默认这里设置的数值。</p> 
<p style="margin-left:0; margin-right:0">比如：这里是5%，新推广会员的佣金便会默认为5%佣金比例。</p> 
<p style="margin-left:0; margin-right:0">配置方式：系统设置→网店设置→选项设置→联盟会员</p> 
<p><img height="421" src="https://www.opencart.cn/storage/uploads/image/2022/04/25/af3aad3d73a029676b1f3896753a2f01.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">注：“自动添加佣金”是指当订单状态变为已完成时，联盟会员会收取到佣金。</p> 
<p style="margin-left:0; margin-right:0"><strong>1|注册推广联盟会员</strong></p> 
<p style="margin-left:0; margin-right:0">注册流程：注册账号→会员中心→注册推广联盟账号</p> 
<p><img height="384" src="https://www.opencart.cn/storage/uploads/image/2022/04/25/769230728e9d8c85184729d049ac4b64.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">填写公司名称、网址、税号、支付方式等相关信息，填写完成后提交。</p> 
<p style="margin-left:0; margin-right:0">如果后台设置了账户需审核，则要在后台：营销推广→推广会员，将刚注册的推广联盟会员状态从禁用更改为启用</p> 
<p><img height="248" src="https://www.opencart.cn/storage/uploads/image/2022/04/25/1526cb315229bd4b4d5d11039ff6ff11.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">注：该页面，为管理推广会员页。可筛选会员、编辑会员的跟踪码、设置佣金信息等。</p> 
<p style="margin-left:0; margin-right:0"><strong>2|会员推广</strong></p> 
<p style="margin-left:0; margin-right:0">在会员中心点击跟踪码：（只有注册了推广联盟的客户才可以在会员中心看到跟踪码）</p> 
<p><img height="422" src="https://www.opencart.cn/storage/uploads/image/2022/04/25/123d532c35b9ddaed8c16bb17826ce8e.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">选择要推广的商品，需要手动输入商品关键词搜索。如下图：</p> 
<p style="margin-left:0; margin-right:0"><img height="313" src="https://www.opencart.cn/storage/uploads/image/2022/04/25/11e5839c698cfcecb29dc3d2a2af6cf5.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">搜索到对应商品后，选择商品，生成跟踪链接后，点击复制跟踪链接。</p> 
<p><img height="329" src="https://www.opencart.cn/storage/uploads/image/2022/04/25/fa92de7de2f927b85ee2946f6ecb1218.png" width="750" referrerpolicy="no-referrer"></p> 
<p><strong>3|佣金设置</strong></p> 
<p style="margin-left:0; margin-right:0">系统中有3个地方可以设置佣金，有优先级关系：</p> 
<p style="margin-left:0; margin-right:0">1. 营销推广→推广会员，可设置单个联盟会员的佣金。每个联盟会员佣金可不一致。</p> 
<p style="margin-left:0; margin-right:0">2. 单个商品设置佣金比例，该佣金是针对商品。</p> 
<p style="margin-left:0; margin-right:0">注：如果同时设置了商品佣金、推广会员佣金 则按商品佣金计算！</p> 
<p style="margin-left:0; margin-right:0">举例说明：网站设置了推广会员佣金5%，商品佣金0%，商品金额为¥159。被分享者购买该商品，后台可在 “订单销售” → 订单管理，对应订单中 看到所得佣金为¥7.95</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/7bb96d228beabefcf21fc1421ebb5713.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">3. 当订单变为已完成时，手动点击添加佣金。</p> 
<p style="margin-left:0; margin-right:0">设置流程：系统设置→网店设置→选项设置→联盟会员→关闭“自动添加佣金”</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/185deadedf8a2fdad60cae6400a44ebc.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">如图所示：可看到佣金已成功添加</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/5dbade6c434a87269914e15f421eb359.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">用户可以在会员中心可看到余额变动</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/51f6f2f34ef0c168c5f4f8ac892f55f3.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>02、优惠券功能</strong></p> 
<p style="margin-left:0px; margin-right:0px">优惠券发放有以下几种方式： </p> 
<p style="margin-left:0px; margin-right:0px">    1. 用户领取优惠券</p> 
<p style="margin-left:0px; margin-right:0px">    2. 用户注册优惠券</p> 
<p style="margin-left:0px; margin-right:0px">    3. 推荐送优惠券</p> 
<p style="margin-left:0; margin-right:0">优惠券设置后，会员可在会员中心查看优惠券。</p> 
<p style="margin-left:0; margin-right:0">用户将商品加入购物车，在购物车点击使用优惠券，提交订单。</p> 
<p style="margin-left:0; margin-right:0"><strong>1|创建优惠券</strong></p> 
<p style="margin-left:0; margin-right:0">设置流程：营销推广→优惠券→点击添加</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/60b05be969d268088b06567d33dbf34c.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">进入设置优惠券内容，保存时如果有报错，根据提示完善即可</p> 
<p style="margin-left:0; margin-right:0">优惠券可针对特定客户、客户组、特定商品、分类、品牌使用</p> 
<p style="margin-left:0; margin-right:0"><strong>2|注册送优惠券</strong></p> 
<p style="margin-left:0; margin-right:0">1. 优惠券创建好后，在 营销推广→注册奖励，勾选创建的优惠券，再点击保存。</p> 
<p style="margin-left:0; margin-right:0">2. 可以设置推荐者和被推荐者，都获取优惠券</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/4e0ec644cc0775d1148d5a3a43222ce1.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">客户注册账号成功后，提示已获得优惠券。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/6ac7dae3e98304aaa6adc2206cfa4454.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">会员中心优惠券列表可看到当前可用优惠券。</p> 
<p style="margin-left:0; margin-right:0"><strong>3|领取优惠券</strong></p> 
<p style="margin-left:0; margin-right:0">优惠券可领取设置流程：模块管理→通用模块→搜索“优惠券”→点击编辑</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/e8aa594b3adfded4a61c62935f72c9e9.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/e953983068c9bd51eda51d94000593be.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">后台登录的前提下，可以在首页顶部点击：编辑首页。将优惠券部署到首页，方便客户领取。</p> 
<p style="margin-left:0; margin-right:0">放置好位置之后点击保存并退出。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/0ff7351fe45a0522589dd5c8cf7f9472.png" referrerpolicy="no-referrer"></p> 
<p><img height="388" src="https://www.opencart.cn/storage/uploads/image/2022/04/25/c55300358ec567a7d5150b6106e3bee6.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>4|使用优惠券</strong></p> 
<p style="margin-left:0; margin-right:0">开启优惠券可用流程：模块管理→订单费用→开启优惠券</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/b232d9c5db9e07c097ff3ffca2b361e5.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">结账页面，点击选择优惠券，如下图所示会显示可用的优惠券，选中结账即可抵扣相应的金额</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/25/cca566dd422bcd5d72d9d50038dbce46.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>总结</strong></p> 
<p style="margin-left:0; margin-right:0"><span>1.<span> </span><strong>推广会员功能</strong>，最主要的作用就是调动老用户的积极性，<strong>通过对老客户的激励，裂变新的客户</strong></span></p> 
<p style="margin-left:0; margin-right:0">2.<span> </span><strong>优惠券功能</strong>，则是更加侧重对现有用户的成交转化，<strong>大大提升客户成交率</strong>，降低用户决策成本</p> 
<p style="margin-left:0; margin-right:0"><strong>往期推荐</strong></p> 
<p style="margin-left:0; margin-right:0">1、<a href="https://www.oschina.net/news/192010" target="_blank">开源独立站 OpenCart 中文更新 | 商品管理功能（第 6 期）</a></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">2、<a href="https://www.oschina.net/news/190101" target="_blank">OpenCart 中文更新 | 订单发货模块功能（第 5 期）</a></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">想了解独立站怎么做？想了解OpenCart网站设计？</p> 
<p style="margin-left:0; margin-right:0">使用过程中遇到问题？对OpenCart有新的功能需求？</p> 
<p style="margin-left:0; margin-right:0">网站定制化需求？<strong>欢迎随时联系我们！</strong></p>
                                        </div>
                                      
</div>
            