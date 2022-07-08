
---
title: 'Jeepay 1.14.0 正式发布：开箱即用的开源聚合支付系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202207/08190720_WljY.png'
author: 开源中国
comments: false
date: Fri, 08 Jul 2022 19:03:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202207/08190720_WljY.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Jeepay 是一套适合互联网企业使用的开源支付系统，支持多渠道服务商和普通商户模式。已对接</span><code>微信支付</code><span style="background-color:#ffffff; color:#333333">，</span><code>支付宝</code><span style="background-color:#ffffff; color:#333333">，</span><code>云闪付</code><span style="background-color:#ffffff; color:#333333">官方接口，支持聚合码支付。<br> <br> v1.14.0 版本升级内容：</span></p> 
<div style="text-align:start"> 
 <ol> 
  <li>增加docker的支持</li> 
  <li>优化从请求中获取参数并以+=拼接的方式,使用更为优雅的流式拼接</li> 
  <li>优化优化商户删除逻辑</li> 
  <li>优化分账执行API, 解决提示订单不存在的问题</li> 
  <li>优化扩充日志表请求和响应数据的长度</li> 
  <li>修复解决因目录不存在导致证书下载失败问题</li> 
  <li>修复微信、支付宝设置订单超时bug</li> 
  <li>修复OSS保存路径未考虑设置前缀问题</li> 
  <li>修复订单关闭传递参数字段与文档描述不一致</li> 
  <li>修复微信退款通知检验退款金额问题</li> 
 </ol> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更多升级日志：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jeequan.com%2Fdev%2Fupdate%2Fcategory_1016.html" target="_blank">https://www.jeequan.com/dev/update/category_1016.html</a><br> <br> 项目特点</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持多渠道对接，支付网关自动路由</li> 
 <li>已对接<code>微信</code>服务商和普通商户接口，支持<span> </span><code>V2</code><span> </span>和<span> </span><code>V3</code><span> </span>接口</li> 
 <li>已对接<code>支付宝</code>服务商和普通商户接口，支持 RSA 和 RSA2 签名</li> 
 <li>已对接<code>云闪付</code>服务商接口，可选择多家支付机构</li> 
 <li>提供 http 形式接口，提供各语言的<span> </span><code>sdk</code><span> </span>实现，方便对接</li> 
 <li>接口请求和响应数据采用签名机制，保证交易安全可靠</li> 
 <li>系统安全，支持<code>分布式</code>部署，<code>高并发</code></li> 
 <li>管理端包括<code>运营平台</code>和<code>商户系统</code></li> 
 <li>管理平台操作界面简洁、易用</li> 
 <li>支付平台到商户系统的订单通知使用 MQ 实现，保证了高可用，消息可达</li> 
 <li>支付渠道的接口参数配置界面自动化生成</li> 
 <li>使用<span> </span><code>spring security</code><span> </span>实现权限管理</li> 
 <li>前后端分离架构，方便二次开发</li> 
 <li>由原<span> </span><code>XxPay</code><span> </span>团队开发，有着多年支付系统开发经验</li> 
</ul> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Jeepay 运营平台功能</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay运营平台功能" src="https://static.oschina.net/uploads/img/202207/08190720_WljY.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Jeepay 商户系统功能</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay商户系统功能" src="https://static.oschina.net/uploads/img/202207/08190720_luZt.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">🍯 系统截图</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>以下截图是从实际已完成功能界面截取,截图时间为：2021-07-06 08:59</code></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay演示界面" src="https://static.oschina.net/uploads/img/202207/08190720_qjBV.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay演示界面" src="https://static.oschina.net/uploads/img/202207/08190721_IaeV.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay演示界面" src="https://static.oschina.net/uploads/img/202207/08190721_jxZD.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Jeepay演示界面" src="https://static.oschina.net/uploads/img/202207/08190721_AAZk.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            