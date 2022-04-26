
---
title: 'Odoo 商城模块 Oejia_weshop v1.0.1 发布，统一强大的后台多种客户端支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cors.zfour.workers.dev/?http://oejia.net/files/201809/13194924637.jpeg'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 10:09:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://oejia.net/files/201809/13194924637.jpeg'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0px; margin-right:0px; text-align:left">概述</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">oejia_weshop 是基于Odoo实现的商城系统<br> 如果您想要搭建一套进销存(ERP)系统并实现微信商城及完整的电商管理后台，用OE商城系统（Odoo + oejia_weshop 系列模块）是个不错的选择，强大的生态，灵活的架构，可适应未来各种新的在线商业模式<br> 如果您已使用odoo系统，而想要在微信小程序上实现自己的独立的微商城卖odoo里的商品，装上 oejia_weshop 模块即可，无额外的数据迁移之类的工作。<br> 包含微信小程序商城、H5公众号商城、头条抖音小程序商城、PC电脑端商城等各种商城端的实现，可覆盖品牌自营商城toC销售、toB批发供货、企业电商化采购等各种业务场景。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">v1.0.1</h3> 
<ul style="margin-left:25px; margin-right:0"> 
 <li>微信用户wxapp.user增加来源ID；订单处理过程的order_dict增加entry</li> 
 <li>优化电商订单的过滤条件</li> 
 <li>异常信息返回的编码兼容处理</li> 
 <li>菜单增加角色权限</li> 
 <li>controllers base增加_makeup_context</li> 
 <li>更新物流商字典库，物流商菜单顺序和权限优化</li> 
 <li>WxappCategory类增加get_categorys接口函数</li> 
 <li>修复兼容新版od的权限问题</li> 
 <li>订单列表视图优化，订单增加显示是否已支付</li> 
 <li>分类增加首页导航展示开关</li> 
 <li>商品按分类排序及推荐商品单独排序的支持</li> 
 <li>横幅图功能增强，跳转相关优化</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">商业版更新</h3> 
<ul style="margin-left:25px; margin-right:0"> 
 <li>增加快递鸟付费版接口的支持</li> 
 <li>增加 share_profile 系统参数, 分享的文案可后台配置</li> 
 <li>发货的实现转移到调拨单上；支持分批发货</li> 
 <li>发货单接口兼容odoo老版本的处理</li> 
 <li>发货状态处理优化</li> 
 <li>微信用户增加企业码字段</li> 
 <li>订单设置销售员的同时设置公司</li> 
 <li>增加商品视频展示的支持</li> 
 <li>快递物流跟踪增加快递100的支持</li> 
 <li>优化商品详情页主图的url的获取</li> 
 <li>增加境外wepayez支付方式的支持</li> 
 <li>注册申请逻辑优化</li> 
 <li>产品变体时返回积分的修复</li> 
 <li>增加推荐商品页面及单独排序支持</li> 
 <li>货到付款的单确认收货时不转为待支付</li> 
 <li>分类增加右上角跳转到产品</li> 
 <li>修复jpg图片被识别为mimetype为application的问题</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">预览</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">图一</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://cors.zfour.workers.dev/?http://oejia.net/files/201809/13194924637.jpeg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">后台</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://cors.zfour.workers.dev/?http://oejia.net/files/202003/28164158386.jpeg" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">社区版相关地址</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJoneXiong%2Foejia_weshop%2Freleases" target="_blank">https://github.com/JoneXiong/oejia_weshop/releases</a><br> 项目地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJoneXiong%2Foejia_weshop" target="_blank">https://github.com/JoneXiong/oejia_weshop</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">使用说明</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJoneXiong%2Foejia_weshop%2Fblob%2Fmaster%2FREADME.md" target="_blank">https://github.com/JoneXiong/oejia_weshop/blob/master/README.md</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">常见问题处理：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Foejia.net%2Fblog%2F2018%2F12%2F21%2Foejia_weshop_qa.html" target="_blank">http://oejia.net/blog/2018/12/21/oejia_weshop_qa.html</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">其他相关扩展</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>OE商城多店铺版扩展</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Foejia.net%2Fblog%2F2021%2F08%2F31%2Fweshop_multi_show.html" target="_blank">http://oejia.net/blog/2021/08/31/weshop_multi_show.html</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Odoo 通用H5商城模块</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.calluu.cn%2Fshop%2Fproduct%2Fodoo-h5-24%3Fcategory%3D1" target="_blank">https://www.calluu.cn/shop/product/odoo-h5-24?category=1</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Odoo OE商城 PC 版</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.calluu.cn%2Fshop%2Fproduct%2Fodoo-oe-pc-71%3Fcategory%3D1" target="_blank">https://www.calluu.cn/shop/product/odoo-oe-pc-71?category=1</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>OE商城多公司/多商城版</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.calluu.cn%2Fshop%2Fproduct%2Foe-69%3Fcategory%3D1" target="_blank">https://www.calluu.cn/shop/product/oe-69?category=1</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>OE商城平台多商户版</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.calluu.cn%2Fshop%2Fproduct%2Foe-51%3Fcategory%3D1" target="_blank">https://www.calluu.cn/shop/product/oe-51?category=1</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Odoo 小程序商城分销模块</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.calluu.cn%2Fshop%2Fproduct%2Fodoo-23%3Fcategory%3D1" target="_blank">https://www.calluu.cn/shop/product/odoo-23?category=1</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>OE商城积分模块</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.calluu.cn%2Fshop%2Fproduct%2Foe-52%3Fcategory%3D1" target="_blank">https://www.calluu.cn/shop/product/oe-52?category=1</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>小程序商城优惠券、秒杀、特价活动模块</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.calluu.cn%2Fshop%2Fproduct%2F35%3Fcategory%3D1" target="_blank">https://www.calluu.cn/shop/product/35?category=1</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>商城(小程序/H5)客服消息集成</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Foejia.net%2Fblog%2F2018%2F12%2F21%2Fodoo_kf.html" target="_blank">http://oejia.net/blog/2018/12/21/odoo_kf.html</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>融合电商工具的引导客户下单的企业微信CRM系统</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Foejia.net%2Fblog%2F2020%2F03%2F31%2Foejia_wx_crm_about.html" target="_blank">http://oejia.net/blog/2020/03/31/oejia_wx_crm_about.html</a></p>
                                        </div>
                                      
</div>
            