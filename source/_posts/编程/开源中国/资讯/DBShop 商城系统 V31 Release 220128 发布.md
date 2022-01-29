
---
title: 'DBShop 商城系统 V3.1 Release 220128 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-935399731889136addb4890704783bb91b2.png'
author: 开源中国
comments: false
date: Fri, 28 Jan 2022 18:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-935399731889136addb4890704783bb91b2.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:start">DBShop企业级商城系统，使用PHP语言基于Laminas（Zendframework 3） + Doctrine 2 组合框架开发完成。可定制、多终端、多场景、多支付、多货币；严谨的安全机制，可靠稳定；方便的操作管理，节约时间；清晰的权限分配，责任分明；便捷的更新处理，一键搞定；丰富的插件市场，扩展无限。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>前台提供：简体中文、繁体中文、英文、日文、韩文 显示。</strong></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">系统框架</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Laminas （Zendframework 3）</li> 
 <li>Doctrine 2</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">环境要求</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>服务器系统</strong> Linux、Unix、Mac、Windows、其他</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>web服务器</strong> Apache、Nginx、IIS、其他</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>MySQL版本</strong> >= 5.6</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>PHP版本</strong> >= 7.2</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>PHP扩展|库</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>PDO</li> 
 <li>SSL（openssl）</li> 
 <li>Fileinfo</li> 
 <li>intl</li> 
 <li>Curl</li> 
 <li>GD2</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>系统空间</strong> >= 500M</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>更新日志：</strong></p> 
<ul> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">新增 对Google和Facebook的登录支持 [<strong>插件</strong>]</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">修正 注册用户未填写手机号码时，后台编辑账户信息，电话号码识别错误的问题</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">修复 系统潜在的安全隐患</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 商城二维码和商品二维码，当改变域名后，无需删除处理，会自动匹配新域名</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 form扩展</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 对分类图片和品牌图片上传重新命名</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 后台商品库存可设置为0</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 后台添加和编辑商品时，对于分类和主分类的判断</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 当客户组为客户设置中的注册默认分组，则该组不能开启等级积分功能</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 下架商品，管理员可以在后台进行预览</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 模板商品详情，图片自动调整</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化  修改广告路径为 tuiImage</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 时间调用显示的代码</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 货币金额显示的代码</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 后台销售页面，前台跳转支付，更好的支持预付款</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 支付</li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: start;">优化 订单支付完成判断</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>在线文档地址：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.loongdomsoft.com%2F" target="_blank">https://docs.loongdomsoft.com/</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>前台演示地址：</strong><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fv3.dbshop.net%2F" target="_blank">http://v3.dbshop.net</a><br> <strong>后台演示地址：</strong><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fv3.dbshop.net%2Fadmin" target="_blank">http://v3.dbshop.net/admin</a><br> <strong>后台登录账号：</strong>dbshop<br> <strong>后台登录密码：</strong>123456</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt height="318" src="https://oscimg.oschina.net/oscnet/up-935399731889136addb4890704783bb91b2.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt height="438" src="https://oscimg.oschina.net/oscnet/up-2a10d87169518ff3590a641b918e95a2814.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt height="306" src="https://oscimg.oschina.net/oscnet/up-4c99aa3bc36cd815ba6585a6c400b726bb7.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt height="404" src="https://oscimg.oschina.net/oscnet/up-21a7773040bd4fab00897a97c87e3d9c188.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt height="396" src="https://oscimg.oschina.net/oscnet/up-4bc8e4e8bc97e0f0855e8337dce22da947c.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt height="410" src="https://oscimg.oschina.net/oscnet/up-fdec0119a9a8bdc28c9cf30e11f42cafd3b.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.loongdom.com.cn%2Fdbshop%2FV3.1%2FDBShopV3.1_Release220128.tar.gz" target="_blank"><span> </span>https://download.loongdom.com.cn/dbshop/V3.1/DBShopV3.1_Release220128.tar.gz</a></strong></p>
                                        </div>
                                      
</div>
            