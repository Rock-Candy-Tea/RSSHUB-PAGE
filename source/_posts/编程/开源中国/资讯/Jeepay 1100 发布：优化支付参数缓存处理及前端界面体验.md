
---
title: 'Jeepay 1.10.0 发布：优化支付参数缓存处理及前端界面体验'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mgr.png'
author: 开源中国
comments: false
date: Mon, 22 Nov 2021 09:07:00 GMT
thumbnail: 'https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mgr.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Jeepay是一套适合互联网企业使用的开源支付系统，支持多渠道服务商和普通商户模式。已对接</span><code>微信支付</code><span style="background-color:#ffffff; color:#333333">，</span><code>支付宝</code><span style="background-color:#ffffff; color:#333333">，</span><code>云闪付</code><span style="background-color:#ffffff; color:#333333">官方接口，支持聚合码支付。<br> <br> v1.10.0版本升级内容：</span></p> 
<div style="text-align:start"> 
 <ol> 
  <li>系统配置、 商户应用、服务商参数配置是否使用内存缓存支持开关式配置；</li> 
  <li>订单号生成支持使用mybatis-plus方式；</li> 
  <li>支付订单全额退款时状态修改为已退款；</li> 
  <li>调整系统的表格密度，一屏显示更多数据；</li> 
  <li>订单列表页支持多合一订单查询和展示；</li> 
  <li>登录页面增加登录验证码默认超时时间，并给予用户反馈；</li> 
  <li>商户系统的支付测试和转账默认一个应用；</li> 
  <li>统一下单接口删除了channelUser字段，统一使用channelExtra传参；</li> 
  <li>角色权限关联表字段扩容，避免入库出现问题；<span> </span><a href="https://gitee.com/jeequan/jeepay/issues/I4DKRL">#I4DKRL:t_sys_role_ent_rela表 ent_id 字段短</a><span> </span>;</li> 
  <li>解决云闪付退款传参不正确导致的问题；</li> 
  <li>修复文件存储位置选择阿里云oss时上传位置错误的问题；</li> 
  <li>解决聚合码更新费率问题 ：<a href="https://gitee.com/jeequan/jeepay/issues/I4D2EB">#I4D2EB:使用收银台聚合支付时, 商家的费率, 手续费没有更新上</a><span> </span>;</li> 
  <li>优化支付工具类；</li> 
  <li>微信退款异常添加日志信息；</li> 
  <li>调整接口返回的ContentType:<span> </span><a href="https://gitee.com/jeequan/jeepay/issues/I4H2UX">#I4H2UX:BizExceptionResolver.outPutJson的contentType错误</a><span> </span>;</li> 
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
                                        </div>
                                      
</div>
            