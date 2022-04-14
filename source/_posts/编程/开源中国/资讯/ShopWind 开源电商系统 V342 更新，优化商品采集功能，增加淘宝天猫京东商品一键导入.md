
---
title: 'ShopWind 开源电商系统 V3.4.2 更新，优化商品采集功能，增加淘宝天猫京东商品一键导入'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://forum.shopwind.net/storage/attachments/2022/03/23/sGkv6q8aAQe3cC8OQUQcj97RF2Ewt0cDmdEkl44H.jpg?imageMogr2/format/webp/quality/80/interlace/1/ignore-error/1'
author: 开源中国
comments: false
date: Thu, 14 Apr 2022 15:15:00 GMT
thumbnail: 'https://forum.shopwind.net/storage/attachments/2022/03/23/sGkv6q8aAQe3cC8OQUQcj97RF2Ewt0cDmdEkl44H.jpg?imageMogr2/format/webp/quality/80/interlace/1/ignore-error/1'
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
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>前台体验：<a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net">http://test.shopwind.net</a><span> </span>买家测试账号：buyer 密码：123456 支付密码：123456</li> 
 <li>后台体验：<a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net%2Fadmin" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net%2Fadmin">http://test.shopwind.net/admin</a><span> </span>平台管理员账号：admin 密码：123456</li> 
 <li>商家体验：<a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net%2Fseller%2Flogin.html" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=http%3A%2F%2Ftest.shopwind.net%2Fseller%2Flogin.html">http://test.shopwind.net/seller/login.html</a><span> </span>商家测试账号：seller 密码：123456</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">移动端体验（商业版）</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>H5端体验：<a href="https://gitee.com/link?target=https%3A%2F%2Fh5.shopwind.net" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=https%3A%2F%2Fh5.shopwind.net">https://h5.shopwind.net</a><span> </span>买家测试账号：18978189192 密码：111111 支付密码：111111</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">小程序/APP体验（商业版）</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>微信小程序（手机浏览器点击链接）：<a href="https://gitee.com/link?target=https%3A%2F%2Fwxaurl.cn%2FVUdm2kw795s" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=https%3A%2F%2Fwxaurl.cn%2FVUdm2kw795s">https://wxaurl.cn/VUdm2kw795s</a></li> 
 <li>Android（安卓版）体验：<a href="https://gitee.com/link?target=https%3A%2F%2Fappgallery.huawei.com%2F%23%2Fapp%2FC103448437" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=https%3A%2F%2Fappgallery.huawei.com%2F%23%2Fapp%2FC103448437">https://appgallery.huawei.com/#/app/C103448437</a></li> 
 <li>iOS（苹果版）体验：<a href="https://gitee.com/link?target=https%3A%2F%2Fapps.apple.com%2Fcn%2Fapp%2Fid1548625748" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=https%3A%2F%2Fapps.apple.com%2Fcn%2Fapp%2Fid1548625748">https://apps.apple.com/cn/app/id1548625748</a></li> 
 <li>商家端体验（小程序）：<a href="https://gitee.com/link?target=https%3A%2F%2Fwxaurl.cn%2FgIG5wMZSOFc" target="_blank"><span> </span></a><a href="https://gitee.com/link?target=https%3A%2F%2Fwxaurl.cn%2FgIG5wMZSOFc">https://wxaurl.cn/gIG5wMZSOFc</a></li> 
 <li>通用体验账号：买家（账号：18978189192 密码：111111 支付密码：111111）、商家（账号：18978189171 密码：111111）</li> 
</ul> 
<h4><strong>商品采集功能介绍</strong></h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <div style="margin-left:0; margin-right:0"> 
    <p style="margin-left:0; margin-right:0; text-align:justify">ShopWind电商系统在v3.4.x版本加入了数据采集功能，支持淘宝、天猫、京东、1688、拼多多商品一键采集到平台的功能，你只需要输入商品详情页链接，就可以批量实现导入，导入的数据包括：商品标题，价格，库存，主图，规格（包括规格图），描述等字段。</p> 
    <p style="margin-left:0; margin-right:0; text-align:justify">一、使用采集功能前，您需要先配置数据采集组件秘钥，秘钥申请：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.99api.com%2FLogin%3Flog%3D5%26referee%3D19843" target="_blank">https://www.99api.com/Login?log=5&referee=19843</a></p> 
    <p style="margin-left:0; margin-right:0; text-align:justify">二、进入商家后台-》商品管理-》采集商品</p> 
    <p style="margin-left:0; margin-right:0; text-align:justify">三、输入淘宝京东等商品详情页地址（支持批量），选择数据来源平台后提交</p> 
    <p style="margin-left:0; margin-right:0; text-align:justify">四、导入后如图3所示</p> 
   </div> 
  </div> 
 </div> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <div style="margin-left:0; margin-right:0">
    <img alt="图片" height="310" src="https://forum.shopwind.net/storage/attachments/2022/03/23/sGkv6q8aAQe3cC8OQUQcj97RF2Ewt0cDmdEkl44H.jpg?imageMogr2/format/webp/quality/80/interlace/1/ignore-error/1" width="683" referrerpolicy="no-referrer">
   </div> 
  </div> 
  <div style="margin-left:0; margin-right:0"> 
   <div style="margin-left:0; margin-right:0">
    <img alt="图片" height="425" src="https://forum.shopwind.net/storage/attachments/2022/03/23/Th2bOFHoYmSy6CtOz5NbuWMsbElveuj1TEM4NtoE.jpg?imageMogr2/format/webp/quality/80/interlace/1/ignore-error/1" width="683" referrerpolicy="no-referrer">
   </div> 
  </div> 
  <div style="margin-left:0; margin-right:0"> 
   <div style="margin-left:0; margin-right:0">
    <img alt="图片" height="373" src="https://forum.shopwind.net/storage/attachments/2022/03/23/mTi5iVPp6lUlZRFRjqYv8GELyiG8ApSIFMsIJPZ5.jpg?imageMogr2/format/webp/quality/80/interlace/1/ignore-error/1" width="683" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<p> </p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">其他页面展示</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>首页/用户中心/分类页</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="首页/用户中心/分类页" src="https://images.gitee.com/uploads/images/2021/0615/112143_486e2600_7967349.jpeg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>产品详情/购物车/下单页</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="产品详情/购物车/下单页" src="https://images.gitee.com/uploads/images/2021/0615/152749_4206fc74_7967349.jpeg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>平台后台管理</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="后台首页" src="https://www.shopwind.net/static/images/ht1.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>丰富的功能插件</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="营销插件" src="https://www.shopwind.net/static/images/ht2.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>可视化模板编辑/DIY页面布局</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="模板编辑" src="https://www.shopwind.net/static/images/ht3.png" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><span> </span>更新内容</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>【新增】数据采集淘宝天猫京东商品模块</li> 
 <li>【新增】商品长图和主图视频功能</li> 
 <li>【新增】详情页显示最近买家评价信息</li> 
 <li>【新增】即时提现到支付宝余额功能</li> 
 <li>【新增】查看买家评价页</li> 
 <li>【新增】商品新品标识</li> 
 <li>【新增】移动端商品展示支持瀑布流效果</li> 
 <li>【新增】退款原路返回功能（支持支付宝和微信）</li> 
 <li>【优化】商品规格字段</li> 
 <li>【优化】移动端支付方式传值</li> 
 <li>【优化】商品价格货币化显示方式</li> 
 <li>【优化】后台用户列表数据显示</li> 
 <li>【优化】前台部分CSS及页面</li> 
 <li>【修复】移动端商品详情页商品属性弹窗显示异常</li> 
 <li>【修复】商品评价统计数据有误的问题</li> 
 <li>【修复】优惠券在多个订单可重复使用的问题</li> 
 <li>【修复】详情页商品规格图显示有误等问题</li> 
 <li>【修复】退款模块一处错误</li> 
 <li>【修复】商品详情页左侧商品不显示的问题</li> 
</ul>
                                        </div>
                                      
</div>
            