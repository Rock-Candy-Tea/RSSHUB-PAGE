
---
title: 'ShopWind V3.4.1 更新，新增瀑布流效果，微信支付 APIv3 接口'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/0615/112143_486e2600_7967349.jpeg'
author: 开源中国
comments: false
date: Mon, 14 Mar 2022 11:39:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/0615/112143_486e2600_7967349.jpeg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">ShopWind是一款基于Yii2.0框架深度重构的B2B2C、O2O行业的电商系统软件，您可以轻松创建和发布属于自己品牌的专业的电商平台，进行全方位的品牌宣传和产品推广。ShopWind v3.x标准版开始走向开源，打造一款完全开源的电商系统，可以免费用于商业运营或者二次开发，免于商业版权的烦恼。v3.x商业版包含PC、手机H5、微商城、APP客户端（Andorid+iOS）、微信小程序、今日头条小程序等多端，其中PC端为开源免费项目，移动端为增值项目。ShopWind提供专业、快速、安全的底层软件设计和免费的更新升级服务，做好完善的开发文档和接口文档方便开发者在底层软件的基础上开发各种应用、模板、或者插件。</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.shopwind.net" target="_blank">https://www.shopwind.net</a></li> 
 <li>开发文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.shopwind.net%2F" target="_blank">https://developer.shopwind.net</a></li> 
 <li>API接口文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.shopwind.net%2Fdev-api" target="_blank">http://docs.shopwind.net/dev-api</a></li> 
 <li>开发者社区：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.shopwind.net" target="_blank">https://forum.shopwind.net</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">PC体验</h4> 
<ul> 
 <li>前台体验：<a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net">http://test.shopwind.net</a><span> </span>买家测试账号：buyer 密码：123456 支付密码：123456</li> 
 <li>后台体验：<a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net%2Fadmin" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net%2Fadmin">http://test.shopwind.net/admin</a><span> </span>平台管理员账号：admin 密码：123456</li> 
 <li>商家体验：<a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net%2Fseller%2Flogin.html" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net%2Fseller%2Flogin.html">http://test.shopwind.net/seller/login.html</a><span> </span>商家测试账号：seller 密码：123456</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">移动端体验（商业版）</h4> 
<ul> 
 <li>H5端体验：<a href="https://gitee.com/link?target=https%3A%2F%2Fh5.shopwind.net" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=https%3A%2F%2Fh5.shopwind.net">https://h5.shopwind.net</a><span> </span>买家测试账号：18978189192 密码：111111 支付密码：111111</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">小程序/APP体验（商业版）</h4> 
<ul> 
 <li>微信小程序（手机浏览器点击链接）：<a href="https://gitee.com/link?target=https%3A%2F%2Fwxaurl.cn%2FVUdm2kw795s" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=https%3A%2F%2Fwxaurl.cn%2FVUdm2kw795s">https://wxaurl.cn/VUdm2kw795s</a></li> 
 <li>Android（安卓版）体验：<a href="https://gitee.com/link?target=https%3A%2F%2Fappgallery.huawei.com%2F%23%2Fapp%2FC103448437" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=https%3A%2F%2Fappgallery.huawei.com%2F%23%2Fapp%2FC103448437">https://appgallery.huawei.com/#/app/C103448437</a></li> 
 <li>iOS（苹果版）体验：<a href="https://gitee.com/link?target=https%3A%2F%2Fapps.apple.com%2Fcn%2Fapp%2Fid1548625748" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=https%3A%2F%2Fapps.apple.com%2Fcn%2Fapp%2Fid1548625748">https://apps.apple.com/cn/app/id1548625748</a></li> 
 <li>商家端体验（小程序）：<a href="https://gitee.com/link?target=https%3A%2F%2Fwxaurl.cn%2FgIG5wMZSOFc" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=https%3A%2F%2Fwxaurl.cn%2FgIG5wMZSOFc">https://wxaurl.cn/gIG5wMZSOFc</a></li> 
 <li>通用体验账号：买家（账号：18978189192 密码：111111 支付密码：111111）、商家（账号：18978189171 密码：111111）</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">页面展示</h4> 
<p><strong>首页/用户中心/分类页</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="首页/用户中心/分类页" src="https://images.gitee.com/uploads/images/2021/0615/112143_486e2600_7967349.jpeg" referrerpolicy="no-referrer"></p> 
<p><strong>产品详情/购物车/下单页</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="产品详情/购物车/下单页" src="https://images.gitee.com/uploads/images/2021/0615/152749_4206fc74_7967349.jpeg" referrerpolicy="no-referrer"></p> 
<p><strong>平台后台管理</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="后台首页" src="https://www.shopwind.net/static/images/ht1.png" referrerpolicy="no-referrer"></p> 
<p><strong>丰富的功能插件</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="营销插件" src="https://www.shopwind.net/static/images/ht2.png" referrerpolicy="no-referrer"></p> 
<p><strong>可视化模板编辑/DIY页面布局</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="模板编辑" src="https://www.shopwind.net/static/images/ht3.png" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:left"><span> </span>更新内容</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>【新增】买家评价订单时可以晒图</li> 
 <li>【新增】详情页显示最近买家评价信息</li> 
 <li>【新增】即时提现到支付宝余额功能</li> 
 <li>【新增】查看买家评价页</li> 
 <li>【新增】商品新品标识</li> 
 <li>【新增】移动端商品展示支持瀑布流效果</li> 
 <li>【新增】退款原路返回功能（支持支付宝和微信）</li> 
 <li>【升级】支付宝支付接口（正式模式）</li> 
 <li>【升级】微信支付APIv3接口</li> 
 <li>【升级】微信小程序登录接口（微信getUserInfo接口变更）</li> 
 <li>【优化】提现银行卡数据表字段</li> 
 <li>【优化】移动端支付方式传值</li> 
 <li>【优化】商品价格货币化显示方式</li> 
 <li>【优化】在线支付订单不在额外新增财务收支记录</li> 
 <li>【优化】商品评价页好中差评传值</li> 
 <li>【优化】后台用户列表数据显示</li> 
 <li>【优化】前台部分CSS及页面</li> 
 <li>【修复】移动端商品详情页商品属性弹窗显示异常</li> 
 <li>【修复】商品评价统计数据有误的问题</li> 
 <li>【修复】优惠券在多个订单可重复使用的问题</li> 
 <li>【修复】详情页商品规格图显示有误等问题</li> 
 <li>【修复】退款模块一处错误</li> 
 <li>【修复】商品详情页左侧商品不显示的问题</li> 
 <li>【修复】邮件发送模块</li> 
 <li>【修复】编辑商品时类目缺失时没有验证的问题 <p> </p> </li> 
</ul>
                                        </div>
                                      
</div>
            