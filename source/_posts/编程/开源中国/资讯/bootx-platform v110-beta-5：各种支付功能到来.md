
---
title: 'bootx-platform v1.1.0-beta-5：各种支付功能到来'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9f0044b76071d5a7f598ceab591c5fedb02.png'
author: 开源中国
comments: false
date: Fri, 15 Jul 2022 08:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9f0044b76071d5a7f598ceab591c5fedb02.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2> 🍈项目介绍</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left">项目地址：<a href="https://gitee.com/bootx/bootx-platform">https://gitee.com/bootx/bootx-platform</a>，非常欢迎看看项目介绍留以及个<strong>Star</strong>呀🤺🤺🤺</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left"><span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#b7b1a7; background-color:#ffffff; color:#40485b">基于Spring Boot框架打造，针对单体式应用进行专门设计，提供整套服务模块，努力为打造全方位企业级开发解决方案， 致力将开源版打造成超越商业版后台管理框架的项目。前端分为vue2版和vue3版，vue2使用</span><span data-darkreader-inline-bgcolor style="--darkreader-inline-bgcolor:#181a1b; background-color:#ffffff"> </span>ANTD PRO VUE<span data-darkreader-inline-bgcolor style="--darkreader-inline-bgcolor:#181a1b; background-color:#ffffff"> 作为脚手架，vue3使用 </span>Vben-Admin-Next<span data-darkreader-inline-bgcolor style="--darkreader-inline-bgcolor:#181a1b; background-color:#ffffff"> 作为脚手架（开发中）。 移动端使用 </span>Taro<span data-darkreader-inline-bgcolor style="--darkreader-inline-bgcolor:#181a1b; background-color:#ffffff"> vue3+TS为技术栈（开发中）。分布式版本 Bootx-Cloud（计划后期重启），尽请期待。</span></p> 
<h2><span>🍒更新说明</span></h2> 
<p><span>经过数夜的奋战，基本上成功达到了预期的目标，将支付相关大部分功能进行了完善和优化。同时申请了正式的商户号，可以更方便的部署出来进行演示（支付完可以从后台进行退款），通过结算台演示，可以测试支付宝和微信的各种支付方式，同时还可以测试聚合支付（一个二维码被支付宝或微信扫码都可以支付，同时扫支付宝或微信的付款码也可以自动识别并进行支付）。</span></p> 
<p><span>🥰 结算台演示地址：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fweb.platform.bootx.cn%2Fcashier" target="_blank">http://web.platform.bootx.cn/cashier 🥰</a></p> 
<p>☺️<span>后台支付订单模块地址：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fweb.platform.bootx.cn%2Fpayment%2Forder%2Fpayment" target="_blank">http://web.platform.bootx.cn/payment/order/payment</a>☺️</p> 
<h2>🛠️本次功能更新</h2> 
<ul> 
 <li>抽象支付相关接口，通过策略+模板等设计模式抽象出：支付、退款、撤销、同步、超时等API接口，方便调用</li> 
 <li>使用RabbitMQ消息中间件进行消息通知，保证高可靠性</li> 
 <li><strong>微信支付</strong>，支持扫码支付、付款码支付、公众号支付、小程序支付、APP支付，v3版API开发中</li> 
 <li><strong>支付宝支付</strong>，支持扫码支付、PC网站支付、H5网站支付、付款码支付，支持Cert/秘钥模式</li> 
 <li><strong>钱包支付</strong>，支持钱包支付</li> 
 <li><strong>储值卡支付</strong>，支持多卡组合支付和单卡多次支付</li> 
 <li><strong>现金支付</strong>，支持现金支付</li> 
 <li><strong>聚合支付</strong>，支持微信和支付宝二维码扫码或付款码支付</li> 
 <li><strong>组合支付</strong>，支持一种异步支付方式和多种同步支付方式进行合并支付</li> 
 <li><strong>退款功能</strong>，支持多次部分退款和全额退款</li> 
 <li>增加支付信息同步功能，支持与支付网关同步支付状态</li> 
 <li>增加支付定时关闭功能，使用定时时间轮+消息通知实现</li> 
 <li>增加结算收银台演示，演示微信和支付各种方式的支付，以及扫码和付款码的聚合支付演示</li> 
 <li>增加简单支付收银台演示，演示单渠道支付</li> 
 <li>增加组合支付演示，演示多种支付方式组合进行支付</li> 
 <li>增加<code>JacksonListTypeHandler</code><span> </span><code>MyBatis-Plus</code>的类型处理器</li> 
 <li>优化系统中注入的<code>Jackson</code>的<code>ObjectMapper</code>注入，增加携带类型信息<code>ObjectMapper</code>注入</li> 
 <li>优化<code>JacksonUtil</code>方法设置<code>ObjectMapper</code>限制，增加支持序列化带类型信息的Json方法</li> 
 <li>fix: 前端业务页面F5刷新后，字典项有几率获取不到</li> 
</ul> 
<h2>🚩下一次更新内容</h2> 
<p><span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#c8c3bc; background-color:#ffffff; color:#333333">微信服务号消息通知、钉钉消息通知、短信消息发送等通知相关功能，同时支付功能将继续优化，对退款、钱包、储值卡模块进行完善。</span></p> 
<h2>🍎支付相关接口</h2> 
<pre><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">bootx-platform 
    ├── PayService -- 支付接口
    ├── PayRefundService -- 退款退款接口
    ├── PayCancelService -- 支付撤销接口
    ├── PayCallbackService -- 支付回调处理接口
    ├── PayExpiredTimeService -- 支付超时处理接口</span>
<span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">    ├── PaySyncService -- 支付信息同步接口</span></pre> 
<h2>🥞新功能截图</h2> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-9f0044b76071d5a7f598ceab591c5fedb02.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>支付收银台(多种支付方式)</p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-704dd26d9b85cb44d65c771610ac4ac47e9.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>组合支付收银台</p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-cfff268688f7a3fd6c7eea0797a256e8c98.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-429c524da0a2154fa73a597e2c03bf2387d.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>聚合支付(扫码和付款码)</p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-08b9db916bd8af5bd90acbe44f7a78c07a7.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>支付宝PC支付</p> 
<p><img height="1218" src="https://oscimg.oschina.net/oscnet/up-f4fc5476925b233375b69c78441fd2821d7.png" width="563" referrerpolicy="no-referrer"></p> 
<p>支付宝H5支付</p> 
<p><img height="1792" src="https://oscimg.oschina.net/oscnet/up-ed53086a8006fa7b19ed5cc14b64ffce55c.jpg" width="828" referrerpolicy="no-referrer"></p> 
<p>微信支付</p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-fa4bd4f0688c5ecf0b398c9d64fc5e07579.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-0d9d32650d3f45af115d9c2c5a3c3a5b417.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>支付订单</p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-d04cc9b3c38fe5fbe6fb99013b7453017d8.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-bd5c856172abb97b8fa966eba5cc019c96d.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>支付退款(全额退款/部分退款)</p>
                                        </div>
                                      
</div>
            