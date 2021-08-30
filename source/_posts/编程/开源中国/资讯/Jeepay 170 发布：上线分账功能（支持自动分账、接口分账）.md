
---
title: 'Jeepay 1.7.0 发布：上线分账功能（支持自动分账、接口分账）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mgr.png'
author: 开源中国
comments: false
date: Mon, 30 Aug 2021 15:39:00 GMT
thumbnail: 'https://jeequan.oss-cn-beijing.aliyuncs.com/jeepay/img/jeepay_mgr.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">Jeepay是一套适合互联网企业使用的开源支付系统，支持多渠道服务商和普通商户模式。已对接</span><code>微信支付</code><span style="background-color:#ffffff; color:#333333">，</span><code>支付宝</code><span style="background-color:#ffffff; color:#333333">，</span><code>云闪付</code><span style="background-color:#ffffff; color:#333333">官方接口，支持聚合码支付。<br> <br> v1.7.0版本升级内容：</span></p> 
<ol> 
 <li>商户系统新增分账组管理、分账关系绑定、分账记录查询功能；</li> 
 <li>支付网关新增分账绑定、分账请求API;</li> 
 <li>支付测试支持分账选项；</li> 
 <li>解决服务商配置修改后没有更新缓存的问题；</li> 
 <li>退款中的订单改为定时任务实时补单；</li> 
 <li>订单表记录表记录商户费率快照: <a href="https://gitee.com/jeequan/jeepay/issues/I46MDI">#I46MDI:提交一个费率模块的使用介意</a></li> 
 <li>退款订单表记录微信异常信息：<a href="https://gitee.com/jeequan/jeepay/issues/I47KUF">#I47KUF:微信退款失败，错误信息未记录</a></li> 
 <li>主扫被扫都记录上游渠道用户ID: <a href="https://gitee.com/jeequan/jeepay/issues/I47KRW">#I47KRW:订单列表 用户标识页面不显示的BUG</a></li> 
</ol> 
<p style="text-align:start">更多升级日志：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jeequan.com%2Fdev%2Fupdate%2Fcategory_1016.html" target="_blank">https://www.jeequan.com/dev/update/category_1016.html</a><br> <br> 项目特点</p> 
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
            