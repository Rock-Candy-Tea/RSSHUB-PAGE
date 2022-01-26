
---
title: 'Jeepay 1.12.0 正式发布：开箱即用的开源聚合支付系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mgr.png'
author: 开源中国
comments: false
date: Wed, 26 Jan 2022 08:38:00 GMT
thumbnail: 'https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mgr.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Jeepay是一套适合互联网企业使用的开源支付系统，支持多渠道服务商和普通商户模式。已对接</span><code>微信支付</code><span style="background-color:#ffffff; color:#333333">，</span><code>支付宝</code><span style="background-color:#ffffff; color:#333333">，</span><code>云闪付</code><span style="background-color:#ffffff; color:#333333">官方接口，支持聚合码支付。<br> <br> v1.12.0版本升级内容：</span></p> 
<div style="text-align:start"> 
 <ol> 
  <li>增加微信退款异步回调支持</li> 
  <li>新增增加微信H5由payment项目地址统一跳转</li> 
  <li>新增增加关闭订单接口（微信、支付宝、云闪付已对接）</li> 
  <li>新增增加分账失败重新发起功能转</li> 
  <li>优化升级支付宝转账接口（sdk升级到4.22.22.ALL）</li> 
  <li>修复修复微信v3接口小程序支付报错问题：<a href="https://gitee.com/jeequan/jeepay/issues/I4PJKX">#I4PJKX:微信支付服务商模式，小程序使用微信v3支付错误</a></li> 
  <li>修复修复安全漏洞（升级mysql-connector-java、velocity-engine-core版本）</li> 
  <li>修复修复删除服务商时查看子商户数量问题</li> 
 </ol> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更多升级日志：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jeequan.com%2Fdev%2Fupdate%2Fcategory_1016.html" target="_blank">https://www.jeequan.com/dev/update/category_1016.html</a><br> <br> 项目特点</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持多渠道对接，支付网关自动路由</li> 
 <li>已对接<code>微信</code>服务商和普通商户接口，支持<code>V2</code>和<code>V3</code>接口</li> 
 <li>已对接<code>支付宝</code>服务商和普通商户接口，支持RSA和RSA2签名</li> 
 <li>已对接<code>云闪付</code>服务商接口，可选择多家支付机构</li> 
 <li>提供http形式接口，提供各语言的<code>sdk</code>实现，方便对接</li> 
 <li>接口请求和响应数据采用签名机制，保证交易安全可靠</li> 
 <li>系统安全，支持<code>分布式</code>部署，<code>高并发</code></li> 
 <li>管理端包括<code>运营平台</code>和<code>商户系统</code></li> 
 <li>管理平台操作界面简洁、易用</li> 
 <li>支付平台到商户系统的订单通知使用MQ实现，保证了高可用，消息可达</li> 
 <li>支付渠道的接口参数配置界面自动化生成</li> 
 <li>使用<code>spring security</code>实现权限管理</li> 
 <li>前后端分离架构，方便二次开发</li> 
 <li>由原<code>XxPay</code>团队开发，有着多年支付系统开发经验</li> 
</ul> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Jeepay运营平台功能</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay运营平台功能" src="https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mgr.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Jeepay商户系统功能</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay商户系统功能" src="https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mch.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">🍯 系统截图</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>以下截图是从实际已完成功能界面截取,截图时间为：2021-07-06 08:59</code></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay演示界面" src="http://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/yanshi/001.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay演示界面" src="http://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/yanshi/023.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay演示界面" src="http://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/yanshi/002.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay演示界面" src="http://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/yanshi/005.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay演示界面" src="http://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/yanshi/006.png" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            