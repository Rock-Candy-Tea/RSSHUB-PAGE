
---
title: 'YunGouOS 全能支付接口 2.0.20 版本发布，微信个人小程序全面升级半屏支付'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-878613357e9bd9673d7c778cf0eb7b00b63.png'
author: 开源中国
comments: false
date: Wed, 17 Nov 2021 16:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-878613357e9bd9673d7c778cf0eb7b00b63.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">YunGouOS 是一款开源的基于微信和支付宝的官方服务商支付接口开发的支付SDK，YunGouOS负责帮您在微信、支付宝官方进行签约开户，同时也支持自己在微信签约后接入YunGouOS使用，支付结算由微信/支付宝官方直连。主要集成微信官方扫码支付、JSAPI支付、小程序支付、订单查询、退款；支付宝扫码、wap、H5支付、APP支付、查询订单、订单退款等相关支付接口，开发者只需要一个架包即可完成微信/支付宝支付对接，无论您是<strong>个人、个体户、亦或企业</strong>都可以通过 YunGouOS 一键集成微信支付/支付宝支付。我们致力于提供简单的官方支付接口，一行代码快速接入，码出高效！</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在线体验：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yungouos.com%2F%23%2Fdemo" target="_blank">https://www.yungouos.com/#/demo</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支付后可自行在页面退款</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>新特性</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1、微信个人小程序支持半屏拉起支付界面，无需小程序跳转即可完成支付。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2、聚合收款码支持在线配置分账，可实现收款码收款后自动分账，适合分销、异业合作等场景。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3、【微信转账】接口单日单笔限额从原5000元调高至20000元。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">4、新增可签约【微信支付】间联商户，可企业对私结算。</p> 
<p>5、支持微信支付投诉在线处理与客户沟通和处理投诉。</p> 
<p>6、新增【查询分账】接口，与分账回调信息一致。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">7、【微信授权】接口可自定义授权类型，除了基础的获取openid外，还可通过改变授权类型参数以获得更详细的用户信息 比如昵称、头像等。为需要接入“微信登录”功能的客户提供基础能力。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">8、【微信授权】接口同步支持PC的扫码登录，专门针对PC用户设计了授权链接方式、以及网页内展示登录二维码两种方式。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">9、微信登录模块接口开放自有商户对接使用，通过该授权接口可关联自有商户的公众号/小程序/网站 进行使用。</p> 
<p>10、微信【收银台支付】已完成新版全面升级，收银台接口将支持整个YunGouOS生态内的所有商户使用。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>文档更新</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">（1）【微信支付】小程序支付接口文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Fpay%2Fwxpay%2FminPay" target="_blank">https://open.pay.yungouos.com/#/api/api/pay/wxpay/minPay</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">（2）【资金分账】新增查询分账接口文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopen.pay.yungouos.com%2F%23%2Fapi%2Fapi%2Ffinance%2Fprofitsharing%2FgetInfo" target="_blank">https://open.pay.yungouos.com/#/api/api/finance/profitsharing/getInfo</a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>平台更新</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1、聚合收款码支持在线配置分账，可实现收款后自动分账，支持个人微信、微信商户、支付宝账户分账。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2、微信支付->投诉记录 新增在线处理投诉功能，可与用户沟通和处理投诉。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">微信个人小程序无跳转半屏支付</h4> 
<div class="ckeditor-html5-video" data-responsive="true" style="text-align:center"> 
 <video controls="controls" src="https://images.yungouos.com/YunGouOS/merchant/mindemo/pay.mp4" style="height:auto; max-width:100%">
   
 </video> 
</div> 
<p> </p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">微信支付投诉在线处理</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="545" src="https://oscimg.oschina.net/oscnet/up-878613357e9bd9673d7c778cf0eb7b00b63.png" width="1080" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>聚合收款码分账</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="357" src="https://oscimg.oschina.net/oscnet/up-8b46eef5b2e0a95b0ee96c0e728c141bc69.png" width="1080" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>订单报表</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="546" src="https://oscimg.oschina.net/oscnet/up-2d64df76fd39c5f4e45407993fbbd8dd2e8.png" width="1080" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            