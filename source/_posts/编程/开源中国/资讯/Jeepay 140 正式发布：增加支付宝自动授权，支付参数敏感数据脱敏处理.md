
---
title: 'Jeepay 1.4.0 正式发布：增加支付宝自动授权，支付参数敏感数据脱敏处理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mgr.png'
author: 开源中国
comments: false
date: Mon, 19 Jul 2021 19:14:00 GMT
thumbnail: 'https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mgr.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">Jeepay是一套适合互联网企业使用的开源支付系统，支持多渠道服务商和普通商户模式。已对接</span><code>微信支付</code><span style="background-color:#ffffff; color:#333333">，</span><code>支付宝</code><span style="background-color:#ffffff; color:#333333">，</span><code>云闪付</code><span style="background-color:#ffffff; color:#333333">官方接口，支持聚合码支付。<br> <br> v1.4.0版本升级内容：</span></p> 
<ol> 
 <li>新增系统内服务商子商户的支付宝扫码授权（免录参数）；</li> 
 <li>新增系统内的参数脱敏处理功能，对敏感数据使用***替代并不可回显仅支持修改；</li> 
 <li>升级springboot版本 2.4.5==》2.4.8（ spring-security <5.4.7 存在安全漏洞：CVE-2021-22119）；</li> 
 <li>删除sun.misc.BASE64Decoder的引用，避免部分环境编译报错的问题；</li> 
 <li>解决其他已知问题。</li> 
</ol> 
<p style="text-align:start">更多升级日志：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jeequan.com%2Fdev%2Fupdate.html%23article_95" target="_blank">https://www.jeequan.com/dev/update.html#article_95</a><br> <br> 项目特点</p> 
<ul> 
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
 <p>Jeepay运营平台功能</p> 
</blockquote> 
<p style="text-align:left"><img alt="Jeepay运营平台功能" src="https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mgr.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>Jeepay商户系统功能</p> 
</blockquote> 
<p style="text-align:left"><img alt="Jeepay商户系统功能" src="https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mch.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">🍯 系统截图</h2> 
<p style="text-align:left"><code>以下截图是从实际已完成功能界面截取,截图时间为：2021-07-06 08:59</code></p> 
<p style="text-align:left"><img alt="Jeepay演示界面" src="http://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/yanshi/001.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt="Jeepay演示界面" src="http://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/yanshi/023.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt="Jeepay演示界面" src="http://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/yanshi/002.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt="Jeepay演示界面" src="http://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/yanshi/005.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt="Jeepay演示界面" src="http://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/yanshi/006.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            