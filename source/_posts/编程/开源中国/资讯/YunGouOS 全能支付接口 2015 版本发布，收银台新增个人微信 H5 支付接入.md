
---
title: 'YunGouOS 全能支付接口 2.0.15 版本发布，收银台新增个人微信 H5 支付接入'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-10cf61ce9b15f154774a74d50f881f95a88.png'
author: 开源中国
comments: false
date: Wed, 09 Jun 2021 02:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-10cf61ce9b15f154774a74d50f881f95a88.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">YunGouOS 是一款开源的基于微信和支付宝的官方个人支付接口开发的支付SDK，YunGouOS负责帮您在微信、支付宝官方进行签约开户，同时也支持自己在微信签约后接入YunGouOS使用，支付结算由微信/支付宝官方直连。主要集成微信官方扫码支付、JSAPI支付、小程序支付、订单查询、退款；支付宝扫码、wap、H5支付、APP支付、查询订单、订单退款等相关支付接口，开发者只需要一个架包即可完成微信/支付宝支付对接，无论您是个人、个体户、亦或企业都可以通过 YunGouOS 一键集成微信支付/支付宝支付。我们致力于提供简单的官方支付接口，一行代码快速接入，码出高效！</span></p> 
<p style="text-align:left">在线体验：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yungouos.com%2F%23%2Fdemo" target="_blank">https://www.yungouos.com/#/demo</a></p> 
<p style="text-align:left">支付后可自行在页面退款</p> 
<h4 style="text-align:left"><strong>新特性</strong></h4> 
<p style="text-align:left">1、微信支付收银台接口新增H5支付（支持个人），用户使用除微信外第三方浏览器将自动拉起微信APP进行支付，支付后自动返回自己网站。</p> 
<p style="text-align:left">2、微信转账、支付宝转账接口新增notify_url参数，支持服务端异步回调接受转账结果。</p> 
<p style="text-align:left">3、新增【查询转账】接口，可主动查询微信转账、支付宝转账结果</p> 
<p style="text-align:left">4、支持【自有商户】免费接入使用，接入后可使用平台所有功能和SDK。（自有商户定义：微信官方申请、或其他地方申请的微信直连商户）</p> 
<h4 style="text-align:left"><strong>文档更新</strong></h4> 
<p>（1）【微信转账】新增notify_url参数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Ffinance%2Frepay%2Fwxpay" target="_blank">https://open.pay.yungouos.com/#/api/api/finance/repay/wxpay</a></p> 
<p>（2）【支付宝转账】新增notify_url参数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Ffinance%2Frepay%2Falipay" target="_blank">https://open.pay.yungouos.com/#/api/api/finance/repay/alipay</a></p> 
<p>（3）【查询转账】新增查询转账文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Ffinance%2Frepay%2FgetRePayInfo" target="_blank">https://open.pay.yungouos.com/#/api/api/finance/repay/getRePayInfo</a></p> 
<p>（4）【代付回调】新增转账结果回调通知文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fcallback%2Frepay" target="_blank">https://open.pay.yungouos.com/#/callback/repay</a></p> 
<h4 style="text-align:left"><strong>平台更新</strong></h4> 
<p>1、微信签约流程更新</p> 
<p>2、商户余额明细列表新增统计信息</p> 
<p>3、商户余额明细支持导出excel方便对账</p> 
<p>4、账户设置-》通知设置 新增 账户通知-》余额预警提醒，支持设置告警余额，余额低于该值则通过公众号发送通知消息</p> 
<p>5、资金服务-》转账付款 新增统计信息，支持导出excel文件</p> 
<p>6、订单报表支持按时间筛选</p> 
<p>7、渠道商户支持实时接收微信支付消费者投诉信息</p> 
<p><img alt height="533" src="https://oscimg.oschina.net/oscnet/up-10cf61ce9b15f154774a74d50f881f95a88.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><img alt height="992" src="https://oscimg.oschina.net/oscnet/up-cb7387e6f2893e09826d20f38f9d33c18cb.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><img alt height="539" src="https://oscimg.oschina.net/oscnet/up-729ee518fb1ec1270538f5d08ba8966dc22.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><img alt height="431" src="https://oscimg.oschina.net/oscnet/up-a6d116254938cb07c987e0d0dd2e8bcdc1c.png" width="1080" referrerpolicy="no-referrer"></p> 
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
            