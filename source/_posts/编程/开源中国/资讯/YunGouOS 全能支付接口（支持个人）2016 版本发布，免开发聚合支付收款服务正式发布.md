
---
title: 'YunGouOS 全能支付接口（支持个人）2.0.16 版本发布，免开发聚合支付收款服务正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-accb0d23e02eeb14eb8e91d81a840dc10f1.png'
author: 开源中国
comments: false
date: Thu, 19 Aug 2021 07:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-accb0d23e02eeb14eb8e91d81a840dc10f1.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">YunGouOS 是一款开源的基于微信和支付宝的官方服务商支付接口开发的支付SDK，YunGouOS负责帮您在微信、支付宝官方进行签约开户，同时也支持自己在微信签约后接入YunGouOS使用，支付结算由微信/支付宝官方直连。主要集成微信官方扫码支付、JSAPI支付、小程序支付、订单查询、退款；支付宝扫码、wap、H5支付、APP支付、查询订单、订单退款等相关支付接口，开发者只需要一个架包即可完成微信/支付宝支付对接，无论您是个人、个体户、亦或企业都可以通过 YunGouOS 一键集成微信支付/支付宝支付。我们致力于提供简单的官方支付接口，一行代码快速接入，码出高效！</span></p> 
<p style="text-align:left">在线体验：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yungouos.com%2F%23%2Fdemo" target="_blank">https://www.yungouos.com/#/demo</a></p> 
<p style="text-align:left">支付后可自行在页面退款</p> 
<h4 style="text-align:left"><strong>新特性</strong></h4> 
<p>1、新增【云支付】产品，无需开发，可视化配置生成收款二维码，支持微信、支付宝收款和异步回调。</p> 
<p style="text-align:left">2、新增【银行卡转账】接口，支持通过API接口给指定的银行卡进行转账。</p> 
<p style="text-align:left">3、新增【支付盾】产品，可通过支付盾有效拦截羊毛党、恶意投诉等情况发生。开放API接口并永久免费。</p> 
<p style="text-align:left">4、【微信分账】【支付宝分账】新增分账异步回调服务，分账后无需主动查询分账结果，可通过异步回调接收结果。</p> 
<p style="text-align:left">5、支持【自有商户】免费接入使用，接入后可使用平台所有功能和SDK。（自有商户定义：微信官方申请、或其他地方申请的微信直连商户）</p> 
<h4 style="text-align:left"><strong>文档更新</strong></h4> 
<p style="text-align:left">（1）【支付盾】新增添加黑名单接口文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Fpay%2Fblack%2Fcreate" target="_blank">https://open.pay.yungouos.com/#/api/api/pay/black/create</a></p> 
<p style="text-align:left">（2）【支付盾】新增黑名单验证接口文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Fpay%2Fblack%2Fcheck" target="_blank">https://open.pay.yungouos.com/#/api/api/pay/black/check</a></p> 
<p style="text-align:left">（3）【银行卡转账】新增银行卡转账接口文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Ffinance%2Frepay%2Fbank" target="_blank">https://open.pay.yungouos.com/#/api/api/finance/repay/bank</a></p> 
<p style="text-align:left">（4）【分账回调】新增分账结果回调通知文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fcallback%2Fprofit" target="_blank">https://open.pay.yungouos.com/#/callback/profit</a></p> 
<p style="text-align:left">（5）【生成分账】生成分账新增notify_url参数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Ffinance%2Fprofitsharing%2FcreateBill" target="_blank">https://open.pay.yungouos.com/#/api/api/finance/profitsharing/createBill</a></p> 
<h4 style="text-align:left"><strong>平台更新</strong></h4> 
<p style="text-align:left">1、支付宝签约流程更新，支持个人、个体户、企业签约支付宝商户。</p> 
<p style="text-align:left">2、开放市场模块新增【支付盾】产品</p> 
<p style="text-align:left">3、开放市场模块新增【云支付】产品</p> 
<p style="text-align:left">4、支付宝签约新增H5支付、APP支付直接开通，无需签约后再单独开通。</p> 
<h4 style="text-align:left">支付宝商户签约</h4> 
<p style="text-align:left"><img alt height="522" src="https://oscimg.oschina.net/oscnet/up-accb0d23e02eeb14eb8e91d81a840dc10f1.png" width="1080" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left"><strong>聚合支付</strong></h4> 
<p style="text-align:left">聚合支付效果预览</p> 
<p style="text-align:left"><img alt height="600" src="https://oscimg.oschina.net/oscnet/up-41f4dd422374415346c432a0179e71f5d36.png" width="400" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt height="486" src="https://oscimg.oschina.net/oscnet/up-8b2fa8d3dd199481ef378dca6b4f573acfa.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"> </p> 
<h4 style="text-align:left"><strong>支付盾</strong></h4> 
<p style="text-align:left">支付盾效果预览</p> 
<p style="text-align:left"><img alt height="322" src="https://oscimg.oschina.net/oscnet/up-6f66846fb18df752bcea20531516d859bc7.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt height="361" src="https://oscimg.oschina.net/oscnet/up-d0da36af7f11921d7f423afb3bec9f2e4cd.png" width="1080" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left"><strong>订单报表</strong></h4> 
<p style="text-align:left"><img alt height="546" src="https://oscimg.oschina.net/oscnet/up-2d64df76fd39c5f4e45407993fbbd8dd2e8.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"> </p> 
<p style="text-align:left"><strong>官方文档：</strong></p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F" target="_blank">https://open.pay.yungouos.com</a></p> 
<p style="text-align:left"><strong>示例代码</strong>：</p> 
<p style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-SpringBoot-Demo">JAVA版本SpringBoot示例</a></p> 
<p style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-UniApp-Demo">UniApp版本示例</a></p> 
<p style="text-align:left"><strong>下载地址</strong> ：</p> 
<ul> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-JAVA-SDK">JAVA版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-PHP-SDK">PHP版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-WxApp-SDK">小程序版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-JS-SDK">JS版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-Node-SDK">Node版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-UniApp-SDK">UniApp版本下载</a></li> 
</ul>
                                        </div>
                                      
</div>
            