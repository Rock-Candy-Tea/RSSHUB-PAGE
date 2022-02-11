
---
title: 'strongshop 开源跨境商城 v1.5.1 发布，支持多语言录入和第三方登录'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b639a72f33e1838a058498698d184a8f8ab.jpg'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 15:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b639a72f33e1838a058498698d184a8f8ab.jpg'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">stongshop v1.5.1 更新内容如下：</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>产品支持多语言录入</li> 
 <li>文章添加<code>唯一标识</code>字段</li> 
 <li>支持第三方登录（Google、Facebook）</li> 
 <li>更新laravel-strongadmin为github包链接</li> 
 <li>加入aboutus文章</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">StrongShop 简介</h2> 
<p>StrongShop 是一款免费开源的跨境电商商城网站。<br> StrongShop 是基于 PHP Laravel 框架开发的一款 Web 商城系统。<br> 开发缘起是公司的一套跨境商城系统，原先公司使用的系统是基于 Ecshop 二次开发的，后来因为漏洞太多甚至还被黑客盗过数据库，于是基于 Laravel框架 重新开发了一套。<br> 然后觉得现在不都流行开源嘛，于是兴起学着开源 (●ˇ∀ˇ●)。感兴趣的小伙伴可以一起交流学习！</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">系统特点</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于 PHP Laravel6 框架开发</li> 
 <li>遵循 BSD-3-Clause 开源协议，免费商用</li> 
 <li>支持多语言，多货币，多种国际配送方式</li> 
 <li>PayPal 支付，国际信用卡支付</li> 
 <li>PC Web 端和移动端自适应</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">架构特点</h2> 
<p>该项目在没有对 laravel 基础框架进行改写的情况下充分使用了 laravel 的 中间件、事件系统、artisan 命令行、模型关联 等特性，这使得项目架构有着更好的解耦性，也更易于上手和二次开发。 所有此项目目前比较适合中小型项目敏捷二开。后期该项目可能会考虑对 laravel 基础框架进行些许改写变动，以便更适用于中大型项目和插件开发使用。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">主要功能</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>购物车</li> 
 <li>权限管理</li> 
 <li>产品管理</li> 
 <li>分类管理</li> 
 <li>会员管理</li> 
 <li>订单管理</li> 
 <li>文章管理</li> 
 <li>网站设置</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">后续功能迭代</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>插件功能开发：秒杀活动、促销活动等</li> 
 <li>完善 api 接口并支持前端 VUE</li> 
 <li>后台数据分析</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">目录结构</h2> 
<p style="color:#c8c3bc; margin-left:0px; margin-right:0px; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.strongshop.local%2Fwiki%2Ftree">点击查看目录结构</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">前端技术</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Bootstrap3</li> 
 <li>Jquery1.11</li> 
 <li>Jquery ui</li> 
 <li>layui 前端框架</li> 
 <li>layer 弹出层</li> 
 <li>Glyphicons 字体图标</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">运行环境</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Linux | Windows</li> 
 <li>MySql 5.7+</li> 
 <li>Nginx 1.10+</li> 
 <li>PHP >= 7.2.5</li> 
 <li>PDO PHP 拓展</li> 
 <li>OpenSSL PHP 拓展</li> 
 <li>Exif PHP 拓展</li> 
 <li>Fileinfo PHP 拓展</li> 
 <li>Mbstring PHP 拓展</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">系统安装</h2> 
<p style="color:#c8c3bc; margin-left:0px; margin-right:0px; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.strongshop.local%2Fwiki%2Finstall">http://www.strongshop.local/wiki/install</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">系统演示</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>演示站点 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.strongshop.cn">http://www.strongshop.cn</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">截图示例</h2> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>注册页面</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-b639a72f33e1838a058498698d184a8f8ab.jpg" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>产品列表页</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-03db953b96d6ba0780cfac93156558d8a1f.jpg" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>产品详情页</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-bc11b81b1c44ffbd8d48da962d29c90b887.jpg" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>结算页</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-95194b865f7753177a4294baa44bcb8845f.jpg" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            