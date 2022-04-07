
---
title: 'OpenCart 中文更新 _ 订单发货模块功能（第 5 期）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.opencart.cn/storage/uploads/image/2022/04/07/4624304c7802e1ff24079aa4fa8fdd2c.png'
author: 开源中国
comments: false
date: Thu, 07 Apr 2022 15:46:00 GMT
thumbnail: 'https://www.opencart.cn/storage/uploads/image/2022/04/07/4624304c7802e1ff24079aa4fa8fdd2c.png'
---

<div>   
<div class="content">
                                                                                            <p><strong>OpenCart.cn</strong>——PHP 开源跨境外贸电商独立站系统，旗下产品有：</p> 
<p style="margin-left:0; margin-right:0">OpenCart国际专业版、OpenCart中文专业版、OpenCart多商家、OpenCart移动APP</p> 
<p style="margin-left:0; margin-right:0"><strong>前言</strong>：电商行业中，发货是非常重要的一个环节。这篇文章将带你了解opencart国际专业版中，订单发货模块的相关功能。</p> 
<p style="margin-left:0; margin-right:0">【1】身份证信息验证【2】下单流程【3】发货流程【4】电子面单配置</p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>01、上传身份证</strong></p> 
<p style="margin-left:0; margin-right:0">针对特殊商品，需要用户提供身份证信息的场景。后台中可以设置<strong>开启“身份证信息”</strong>，用户在提交订单，<strong>添加新地址</strong>时就需要提交身份证信息。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/07/4624304c7802e1ff24079aa4fa8fdd2c.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">在opencart后台：</p> 
<p style="margin-left:0; margin-right:0">通用模块→搜“身份证”→点击编辑→选择国家→状态设为启用</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/07/e2d8d59374ee083b5cab2a374a529c13.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/07/c355cb837f87573af6330eb50264c563.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">用户在添加地址时候，就会发现地址信息中会出现<strong>身份证号码、身份证照片</strong>必填项。</p> 
<p style="margin-left:0; margin-right:0"><span>✦✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>02、下单流程</strong></p> 
<p style="margin-left:0; margin-right:0">下单时，可选择是否使用优惠券、礼品劵、积分和余额来抵扣商品金额。</p> 
<p style="margin-left:0; margin-right:0">可以选择的支付方式有微信支付、支付宝、银行转账、货到付款等支付方式。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/07/1c85c5cbf65748147c01eecb89b3c0f6.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>1. 积分的使用方式：</strong></p> 
<p style="margin-left:0; margin-right:0">（1）积分的获取方式：签到送积分，注册奖励送积分和购买商品送积分</p> 
<p style="margin-left:0; margin-right:0">（2）客户需要先有积分，才能使用积分抵扣金额</p> 
<p style="margin-left:0; margin-right:0">（3）商品需要开启积分，在单个商品，点击<strong>“其他信息”</strong>配置开启即可<br> （4）设置积分抵扣率在客户管理—客户分组设置。</p> 
<p style="margin-left:0; margin-right:0">注意：</p> 
<p style="margin-left:0; margin-right:0">顾客购买商品，可以使用的（取整）积分数 公式如下：</p> 
<p style="margin-left:0; margin-right:0">    （商品单价x使用积分系数）x 商品数量 = 可使用积分</p> 
<p style="margin-left:0; margin-right:0">例如：</p> 
<p style="margin-left:0; margin-right:0">商品A的价格位89.8元，使用积分系数2</p> 
<p style="margin-left:0; margin-right:0">那么商品可用积分为每个商品89.8X2=179.6，取整后为179</p> 
<p style="margin-left:0; margin-right:0">购买两个可使用积分为179X2=358。</p> 
<p style="margin-left:0; margin-right:0"><strong>2. 积分不足：</strong></p> 
<p style="margin-left:0; margin-right:0">当积分余额不足时，需要其他付款方式补齐差额。</p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>03、发货流程</strong></p> 
<p style="margin-left:0; margin-right:0">（1）当状态为：已支付、待处理时，这时可在后台<strong>订单销售</strong>→<strong>发货管理</strong>中进行发货。</p> 
<p style="margin-left:0; margin-right:0">（2）在列表页找到对应订单，点击发货管理，进入编辑页<strong>添加快递单号</strong>。</p> 
<p style="margin-left:0; margin-right:0">（3）<strong>点击确认发货</strong>，会员可在会员中心历史订单进入订单详情页，<strong>可查看快递信息和轨迹</strong>（需要配置快递跟踪）</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/07/d8cf1f26137b8f56112e8fe407c5d1b9.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>04、电子面单使用</strong></p> 
<p style="margin-left:0; margin-right:0">发货单打印功能目前仅支持快递鸟</p> 
<p style="margin-left:0; margin-right:0">需要在快递鸟平台申请电子面单，如图：</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/07/282c27778d555b88024dfd1f2b1c07d0.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">快递单号是自动获取的，目前支持的快递公司是“无需申请直接打印”的账号类型</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/07/1c7d41e53eaf6d35e8164214dea7ce4a.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">注：另外还有如下四种账号类型：<br> 1. 月结账号直接打印（德邦、EMS非广东省内）：需要线下联系当地网点申请开通，其中EMS需要申请大客户号。</p> 
<p style="margin-left:0; margin-right:0">2. 快递鸟后台申请（优速、韵达、圆通、远成、安能、百世、申通）：需要在快递鸟后台申请。该申请会提交到快递公司审核，过程2-3个工作日。申请结果以电话/短信告知电子面单账户<br> （1）优速成功后可直接使用，无需充值单号。<br> （2）中通需要找当地网点充值非菜鸟类型单号。</p> 
<p style="margin-left:0; margin-right:0">（3）韵达会自动充值50个单号，百世和圆通为100个。<br> 3. 需线下申请账号（申通、京东、信丰、国通、天天、速尔、品骏）</p> 
<p style="margin-left:0; margin-right:0">4. 快运电子面单。在后台配置好快递鸟订单快递跟踪和电子面单打印。</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#7f8c8d">注：仅快递鸟支持电子面单，下图为顺丰电子面单内容预览</span></p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/07/25b7dfb84e1e328f560ab65ac8e03b10.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">想了解独立站怎么做？想了解OpenCart网站设计？使用过程中遇到问题？</p> 
<p style="margin-left:0; margin-right:0">对OpenCart有新的功能需求？网站定制化需求？<strong>欢迎随时联系我们！</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>相关阅读</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Fproducts_update" target="_blank"><strong>opencart中文产品更新动态</strong></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F296" target="_blank"><strong>《跨境电商独立站靠谱吗？》</strong></a></p>
                                        </div>
                                      
</div>
            