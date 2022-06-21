
---
title: 'YunGouOS 2.0.23 版本发布，支持个人微信、支付宝签约申请官方商户接口'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5617'
author: 开源中国
comments: false
date: Tue, 21 Jun 2022 15:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5617'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">YunGouOS 是一款开源的基于微信和支付宝的官方服务商支付接口开发的支付 SDK，YunGouOS 负责帮您在微信、支付宝官方进行签约开户，同时也支持自己在微信签约后接入 YunGouOS 使用，资金由微信 / 支付宝官方结算，不经过任何第三方平台。主要集成微信官方扫码支付、JSAPI 支付、小程序支付、订单查询、退款；支付宝扫码、wap、H5 支付、APP 支付、查询订单、订单退款等相关支付接口，开发者只需要一个架包即可完成微信 / 支付宝支付对接，无论您是<strong>个人、个体户、亦或企业</strong>都可以通过 YunGouOS 一键集成微信支付 / 支付宝支付。我们致力于提供简单的官方支付接口，一行代码快速接入，码出高效！</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在线体验：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yungouos.com%2F%23%2Fdemo" target="_blank">https://www.yungouos.com/#/demo</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支付后可自行在页面退款</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>平台更新</strong></h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">1、新增QQ小程序内使用微信支付，支持个人商户；</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">2、支持自有微信、支付宝服务商账户接入，可接入自己的服务商进行商户签约入驻；</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">3、设备管理升级，支持按绑定新款收款音响设备，支持按设备设置语音播报模版；</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">4、支付宝普通商户签约流程优化，无需商家授权，商家完成和支付宝签约后自动授权；</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">5、聚合收款码增加取消付款时语音播报功能，用户取消音响可进行播报；</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">6、订单管理-》退款记录 增加退款总额统计，支持条件统计，退款详情新增订单支付时间显示；</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">7、修复订单管理-》API订单页面 退款金额统计错误问题；</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">8、修复微信退款失败，回调中没有退款状态问题；</p> 
<p>9、修复自有支付宝服务商进行商户入驻时，支付宝审核状态通知不及时问题；</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>文档更新</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    【微信支付】新增 QQ 小程序支付接口文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Fpay%2Fwxpay%2FqqPay" target="_blank">https://open.pay.yungouos.com/#/api/api/pay/wxpay/qqPay</a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>官方文档：</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F" target="_blank">https://open.pay.yungouos.com</a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>示例代码</strong>：</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-SpringBoot-Demo">JAVA 版本 SpringBoot 示例</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-UniApp-Demo">UniApp 版本示例</a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>下载地址</strong> ：</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-JAVA-SDK">JAVA 版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-PHP-SDK">PHP 版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-WxApp-SDK">小程序版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-JS-SDK">JS 版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-Node-SDK">Node 版本下载</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/YunGouOS/YunGouOS-PAY-SDK/tree/master/YunGouOS-UniApp-SDK">UniApp 版本下载</a></li> 
</ul>
                                        </div>
                                      
</div>
            