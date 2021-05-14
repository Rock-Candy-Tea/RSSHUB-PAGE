
---
title: 'Odoo 商城模块 Oejia_weshop v0.2.3 发布，多种客户资产及客户分级，多商户管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cors.zfour.workers.dev/?http://oejia.net/files/201809/13194924637.jpeg'
author: 开源中国
comments: false
date: Fri, 14 May 2021 11:08:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://oejia.net/files/201809/13194924637.jpeg'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:left">概述</h3> 
<p style="text-align:left">oejia_weshop 是基于Odoo实现的商城系统<br> 如果您想要搭建一套进销存(ERP)系统并实现微信商城及完整的电商管理后台，用OE商城系统（Odoo + oejia_weshop 系列模块）是个不错的选择，强大的生态，灵活的架构，可适应未来各种新的在线商业模式<br> 如果您已使用odoo系统，而想要在微信小程序上实现自己的独立的微商城卖odoo里的商品，装上 oejia_weshop 模块即可，无额外的数据迁移之类的工作。<br> 包含微信小程序商城、H5公众号商城、头条抖音小程序商城等各种商城端的实现，可覆盖品牌自营商城toC销售、toB批发供货、企业电商化采购等各种业务场景。</p> 
<h3 style="text-align:left">v0.2.3</h3> 
<ul> 
 <li>修复当已有的微信用户partner归档后客户端授权请求提示异常信息</li> 
 <li>增加商品搜索时条码匹配的支持</li> 
 <li>修复自取时运费计算的问题</li> 
 <li>分类增加返回是否有子类; 图标为空时返回默认图片</li> 
 <li>商品分类增加层级全名</li> 
 <li>订单和产品菜单权限优化</li> 
 <li>增加返回商品需要的积分</li> 
 <li>增加”客户”菜单组，菜单排序优化</li> 
 <li>增加cli_price用于价格返回到前端的统一处理</li> 
 <li>地址接口兼容不必填省市区的情况</li> 
 <li>增加发货时间及action_receive确认收货动作</li> 
 <li>绑定手机号的同时返回账号是否可用状态</li> 
 <li>优化订单行随订单同时创建</li> 
 <li>客户端背景图静态url调整</li> 
 <li>订单创建兼容多公司情况</li> 
 <li>增加镜像小程序的支持</li> 
 <li>新版的授权登录接口直接传递userInfo用于注册的支持</li> 
</ul> 
<h3 style="text-align:left">商业版更新</h3> 
<ul> 
 <li>优化变体商品提交订单的支持</li> 
 <li>客户端变体支持可选项的联动控制</li> 
 <li>增加评论图片的支持</li> 
 <li>增加配置开关控制客户是否需要走账号注册流程</li> 
 <li>增加订单最小起订金额设置的支持</li> 
 <li>增加客户提交开通申请的后台审核流程的支持</li> 
 <li>增加分类别名;增加产品需要积分数的功能支持</li> 
 <li>积分相关功能完善；钱包明细修复</li> 
 <li>菜单结构优化，更有层次感，更清晰</li> 
 <li>增加开关控制是否需要登录后才可以看商品价格</li> 
 <li>增加自动确认收货实现，是否开启可配</li> 
 <li>优化余额支付时的流水类型</li> 
 <li>订单积分扣减实现部分用余额支付的支持</li> 
 <li>增加是否开启在线支付的开关支持</li> 
 <li>增加商品图片及图文描述的云存储及CDN加速的支持</li> 
 <li>增加客户价格表简化功能界面</li> 
 <li>增加镜像小程序支持实现多个小程可同时使用</li> 
 <li>商城小程序客户端的多项优化</li> 
</ul> 
<h3 style="text-align:left">预览</h3> 
<p style="text-align:left"><img alt src="https://cors.zfour.workers.dev/?http://oejia.net/files/201809/13194924637.jpeg" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">后台</p> 
<p style="text-align:left"><img alt src="https://cors.zfour.workers.dev/?http://oejia.net/files/202003/28164158386.jpeg" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">使用说明</h3> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJoneXiong%2Foejia_weshop%2Fblob%2Fmaster%2FREADME.md" target="_blank">https://github.com/JoneXiong/oejia_weshop/blob/master/README.md</a></p> 
<p style="text-align:left">常见问题处理： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Foejia.net%2Fblog%2F2018%2F12%2F21%2Foejia_weshop_qa.html" target="_blank">http://oejia.net/blog/2018/12/21/oejia_weshop_qa.html</a></p> 
<h3 style="text-align:left">其他相关扩展</h3> 
<p style="text-align:left"><strong>商城(小程序/H5)客服消息集成</strong> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Foejia.net%2Fblog%2F2018%2F12%2F21%2Fodoo_kf.html" target="_blank">http://oejia.net/blog/2018/12/21/odoo_kf.html</a></p> 
<p style="text-align:left"><strong>融合电商工具的引导客户下单的企业微信CRM系统</strong> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Foejia.net%2Fblog%2F2020%2F03%2F31%2Foejia_wx_crm_about.html" target="_blank">http://oejia.net/blog/2020/03/31/oejia_wx_crm_about.html</a></p>
                                        </div>
                                      
</div>
            