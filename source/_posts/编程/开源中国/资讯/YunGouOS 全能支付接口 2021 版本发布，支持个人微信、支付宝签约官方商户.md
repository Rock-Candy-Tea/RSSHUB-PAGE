
---
title: 'YunGouOS 全能支付接口 2.0.21 版本发布，支持个人微信、支付宝签约官方商户'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a0828c063ce99db5030c45b7009f3f50344.png'
author: 开源中国
comments: false
date: Thu, 14 Apr 2022 03:27:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a0828c063ce99db5030c45b7009f3f50344.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">YunGouOS 是一款开源的基于微信和支付宝的官方服务商支付接口开发的支付SDK，YunGouOS负责帮您在微信、支付宝官方进行签约开户，同时也支持自己在微信签约后接入YunGouOS使用，支付结算由微信/支付宝官方直连。主要集成微信官方扫码支付、JSAPI支付、小程序支付、订单查询、退款；支付宝扫码、wap、H5支付、APP支付、查询订单、订单退款等相关支付接口，开发者只需要一个架包即可完成微信/支付宝支付对接，无论您是<strong>个人、个体户、亦或企业</strong>都可以通过 YunGouOS 一键集成微信支付/支付宝支付。我们致力于提供简单的官方支付接口，一行代码快速接入，码出高效！</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在线体验：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yungouos.com%2F%23%2Fdemo" target="_blank">https://www.yungouos.com/#/demo</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支付后可自行在页面退款</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>平台更新</strong></h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">1、云支付聚合收款码门店电话支持固话、手机、400号码。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">2、云支付聚合收款码支持自定义二维码logo，上传门店logo即可。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">3、开放市场新增云会员模块，支持储值、消费、微信卡包联动，微信卡包内支持跳转到“智慧云会员卡”小程序进行消费明细查询。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">4、官网支持自定义登录超时时间，该功能目前内测白名单制，如有需要联系在线客服申请。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">5、订单管理-》API订单 新增通过聚合码查询、统计订单，支持聚合API和云支付聚合码的维度查询。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">6、分账账单 新增停止分账功能，未发起分账付款前支持手动停止。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">7、云支付聚合码新增广告管理模块【仅限服务商】，可管理下属商户支付后广告配置，支持公众号文章引流、微信流量主广告接入。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">8、商户接入支持服务商账户接入，接入后可通过我司平台完成商户签约（免开户费），使用平台所有功能【需开通服务商权益】。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">9、因相关产品政策调整，下线微信商户号结算账户修改功能，如需修改请登录微信商户平台自助修改</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">10、新增支付宝投诉通知和投诉记录功能。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>文档更新</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">（1）【微信支付】新增QQ小程序支付接口文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Fpay%2Fwxpay%2FqqPay" target="_blank">https://open.pay.yungouos.com/#/api/api/pay/wxpay/qqPay</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">（2）【微信支付】发起退款接口新增外部退款单号，文档地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Fpay%2Fwxpay%2FrefundOrder" target="_blank">https://open.pay.yungouos.com/#/api/api/pay/wxpay/refundOrder</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">（3）【支付宝支付】发起退款新增外部退款单号、新增退款异步回调。文档地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Fpay%2Falipay%2FrefundOrder" target="_blank">https://open.pay.yungouos.com/#/api/api/pay/alipay/refundOrder</a></p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:left"><strong>官方文档：</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F" target="_blank">https://open.pay.yungouos.com</a></p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:left"><strong>示例代码</strong>：</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-SpringBoot-Demo">JAVA版本SpringBoot示例</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-UniApp-Demo">UniApp版本示例</a></p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:left"><strong>下载地址</strong> ：</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-JAVA-SDK">JAVA版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-PHP-SDK">PHP版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-WxApp-SDK">小程序版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-JS-SDK">JS版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-Node-SDK">Node版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-UniApp-SDK">UniApp版本下载</a></li> 
</ul> 
<p> </p> 
<p><img alt height="2440" src="https://oscimg.oschina.net/oscnet/up-a0828c063ce99db5030c45b7009f3f50344.png" width="1354" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            