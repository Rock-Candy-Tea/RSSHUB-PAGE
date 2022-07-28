
---
title: 'MyCms 自媒体商城 v3.6 发布，兼容微擎应用开发'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png'
author: 开源中国
comments: false
date: Thu, 28 Jul 2022 10:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1700" src="https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png" width="3164" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MyCms 是一款基于 Laravel 开发的开源免费的自媒体 CMS + 商城系统，助力开发者知识技能变现。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MyCms 基于 Apache2.0 开源协议发布，<strong>免费且可商业使用</strong>，欢迎持续关注我们。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">v3.6 更新内容</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">重点：兼容微擎开发<br> 新增：后台删除后操作<br> 新增：后台通用控制器增加 with<br> 新增：后台时间控件增加最大值和最小值<br> 优化：公共函数备注<br> 移除：ignition包</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#40485b">更新说明</span></strong></p> 
<p>一、兼容微擎开发</p> 
<p>开发者在开发微擎应用时，需要重新熟悉微擎系统的框架，才能进行微擎的应用开发。</p> 
<p>现在 MyCms 兼容了微擎的开发模式，可以直接使用 MyCms 来进行微擎应用的开发，微擎版和独立版简单配置即可切换。</p> 
<pre><code>.env 文件

IS_WE7=(true:开启微擎模式/false:独立版本模式)
WE7_ADDON_NAME=(微擎应用名称)</code></pre> 
<p>二、时间控件增加最大值和最小值</p> 
<p>data-date-min：日期最小值</p> 
<p>data-date-max：日期最大值</p> 
<pre><code><input type="text" name="date" data-date-type="date" data-date="yyyy-MM-dd"
                                 data-date-min="2022-07-28" data-date-max="2022-08-28"  class="layui-input" lay-reqtext="请选择日期" placeholder="请选择日期" value=""></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>站点地址</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">官方网站 : https://www.mycms.net.cn/</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">使用手册：https://www.mycms.net.cn/shouce</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">二次开发(陆续更新)：https://www.mycms.net.cn/dev</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">API 文档：https://www.mycms.net.cn/api-doc</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">模板下载：https://www.mycms.net.cn/muban</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">源码下载 : https://gitee.com/qq386654667/mycms</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">演示后台 : https://demo.mycms.net.cn/system/login</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">演示后台：admin /admin</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>优秀案例</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>在线计算网<span> </span>: https://www.zaixianjisuan.com/</li> 
 <li>程序员导航<span> </span>: https://nav.mycms.net.cn/</li> 
 <li>古诗词网<span> </span>: https://www.gushici.top/</li> 
 <li>火马活码：https://www.huomahuoma.com/</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">重磅推荐</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">活码二维码工具是经过深度挖掘，制作的一款为广大运营者提供便捷的推广裂变工具。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">文档地址：https://www.mycms.net.cn/huoma</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">活码官网：https://www.huomahuoma.com/</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><br> <img alt height="1031" src="https://oscimg.oschina.net/oscnet/up-a0812ec5378b22cae403ec5914a8968c4f8.png" width="1242" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            