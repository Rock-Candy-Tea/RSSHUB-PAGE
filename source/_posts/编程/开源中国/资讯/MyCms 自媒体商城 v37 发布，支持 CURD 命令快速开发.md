
---
title: 'MyCms 自媒体商城 v3.7 发布，支持 CURD 命令快速开发'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png'
author: 开源中国
comments: false
date: Tue, 16 Aug 2022 09:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1700" src="https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png" width="3164" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MyCms 是一款基于 Laravel 开发的开源免费的自媒体 CMS + 商城系统，助力开发者知识技能变现。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MyCms 基于 Apache2.0 开源协议发布，<strong>免费且可商业使用</strong>，欢迎持续关注我们。</span></p> 
<p><strong style="color:#333333">v3.7 更新内容</strong></p> 
<p><span style="background-color:#ffffff; color:#40485b">新增：快速CURD命令</span><br> <span style="background-color:#ffffff; color:#40485b">修复：修复不开启swoole时清理缓存错误</span></p> 
<p><strong>更新重点说明</strong></p> 
<p>一、<span style="background-color:#ffffff; color:#40485b">快速CURD命令</span></p> 
<pre><code class="language-php">php artisan make:curd 表名 模块名</code></pre> 
<p style="color:#747070; text-align:start">参数1：数据表名称</p> 
<p style="color:#747070; text-align:start">参数2：功能所属的模块名称</p> 
<p style="color:#747070; text-align:start">该命令新增/修改的文件如下：</p> 
<p style="color:#747070; text-align:start">控制器：Modules/System/Http/Controllers/Admin/StaffController.php<br> 模型：Modules/System/Models/StaffModel.php<br> 请求类：Modules/System/Http/Requests/StaffRequest.php</p> 
<p style="color:#747070; text-align:start">列表模板：Modules/System/Resources/views/admin/staff/index.blade.php<br> 新建模板：Modules/System/Resources/views/admin/staff/create.blade.php<br> 编辑模板：Modules/System/Resources/views/admin/staff/edit.blade.php<br> Javascript：public/mycms/admin/js/system.staff.js</p> 
<p style="color:#747070; text-align:start">路由：Modules/System/Routes/web.php</p> 
<p>具体使用说明：https://www.mycms.net.cn/dev/dev-fast-curd.html</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>站点地址</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">官方网站 : https://www.mycms.net.cn/</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">使用手册：https://www.mycms.net.cn/shouce</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">二次开发 (陆续更新)：https://www.mycms.net.cn/dev</p> </li> 
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
                                        </div>
                                      
</div>
            