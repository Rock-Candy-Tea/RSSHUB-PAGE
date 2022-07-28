
---
title: 'RXThinkCMF 敏捷开发框架 Laravel8.x+AntdVue 版本 v1.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3624'
author: 开源中国
comments: false
date: Thu, 28 Jul 2022 08:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3624'
---

<div>   
<div class="content">
                                                                                            <p>v1.1.0 更新内容：<br> 1、设计、规划和研发基础 RBAC 权限架构；<br> 2、编写框架核心底层代码，设计基于 Vue 布局的模板，设计并编写自定义模板 Vue 文件；<br> 3、对系统模板进行架构设计及模板继承相关设计；<br> 4、研发框架基础模块，如字典、配置、行政区划管理等等常规基础模块；<br> 5、设计并研发代码生成器，根据表结构动态解析并生成模块文件和增删改查功能；<br> 6、设计并研发一系列其他配套功能很常规使用函数；</p> 
<h2>项目介绍</h2> 
<p>一款 PHP 语言基于 Laravel8.x、Vue、AntDesign 等框架精心打造的一款模块化、插件化、高性能的前后端分离架构敏捷开发框架，可用于快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，目前框架已集成了完整的 RBAC 权限架构和常规基础模块，前端 Vue 端支持多主题切换，可以根据自己喜欢的风格选择想一个的主题，实现了个性化呈现的需求；</p> 
<p>为了敏捷快速开发，提升研发效率，框架内置了一键 CRUD 代码生成器，自定义了模块生成模板，包括后端 PHP 文件模块和前端 Vue 端个性化模板，可以根据已建好的表结构 (字段注释需规范) 快速的一键生成整个模块的所有代码和增删改查等等功能业务，真正实现了低代码开发，极大的节省了人力成本的同时提高了开发效率，缩短了研发周期，是一款真正意义上实现组件化、低代码敏捷开发框架。</p> 
<h2>环境要求:</h2> 
<ul> 
 <li>PHP >= 7.3 及以上</li> 
 <li>PDO PHP Extension</li> 
 <li>MBstring PHP Extension</li> 
 <li>CURL PHP Extension</li> 
 <li>开启静态重写</li> 
 <li>要求环境支持 pathinfo</li> 
</ul> 
<h2>内置模块</h2> 
<ul> 
 <li>用户管理：用于维护管理系统的用户，常规信息的维护与账号设置。</li> 
 <li>角色管理：角色菜单管理与权限分配、设置角色所拥有的菜单权限。</li> 
 <li>菜单管理：配置系统菜单，操作权限，按钮权限标识等。</li> 
 <li>职级管理：主要管理用户担任的职级。</li> 
 <li>岗位管理：主要管理用户担任的岗位。</li> 
 <li>部门管理：主要管理系统组织架构，对组织架构进行统一管理维护。</li> 
 <li>操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。</li> 
 <li>登录日志：系统登录日志记录查询包含登录异常。</li> 
 <li>字典管理：对系统中常用的较为固定的数据进行统一维护。</li> 
 <li>配置管理：对系统的常规配置信息进行维护，网站配置管理功能进行统一维护。</li> 
 <li>城市管理：统一对全国行政区划进行维护，对其他模块提供行政区划数据支撑。</li> 
 <li>友链管理：对系统友情链接、合作伙伴等相关外链进行集成维护管理的模块。</li> 
 <li>个人中心：主要是对当前登录用户的个人信息进行便捷修改的功能。</li> 
 <li>广告管理：主要对各终端的广告数据进行管理维护。</li> 
 <li>站点栏目：主要对大型系统网站等栏目进行划分和维护的模块。</li> 
 <li>会员管理：对各终端注册的会员进行统一的查询与管理的模块。</li> 
 <li>网站配置：对配置管理模块的数据源动态解析与统一维护管理的模块。</li> 
 <li>通知公告：系统通知公告信息发布维护。</li> 
 <li>代码生成：一键生成模块 CRUD 的功能，包括后端和前端 Vue 等相关代码。</li> 
 <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
</ul> 
<h2>软件信息</h2> 
<ul> 
 <li>软件名称：RXThinkCMF 敏捷开发框架 Laravel8.x+AntdVue 版</li> 
 <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.rxthink.cn" target="_blank">http://www.rxthink.cn</a></li> 
 <li>文档网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.avl.pro.rxthink.cn" target="_blank">http://docs.avl.pro.rxthink.cn</a></li> 
</ul> 
<h2>系统演示</h2> 
<ul> 
 <li>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.avl.pro.rxthink.cn" target="_blank">http://manage.avl.pro.rxthink.cn</a></li> 
</ul> 
<h2>版本说明</h2> 
<table> 
 <thead> 
  <tr> 
   <th>版本名称</th> 
   <th>说明</th> 
   <th>地址</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>RXThinkCMF_TP3.2 专业版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP3.2">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP3.2</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_TP3.2 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP3.2_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP3.2_PRO</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_TP5.1 专业版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP5.1">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP5.1</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_TP5.1 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP5.1_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP5.1_PRO</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_TP6.x 专业版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP6">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP6</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_TP6.x 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP6_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP6_PRO</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_LV5.8 专业版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/laravel520/RXThinkCMF_LV5.8">https://gitee.com/laravel520/RXThinkCMF_LV5.8</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_LV5.8 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/laravel520/RXThinkCMF_LV5.8_PRO">https://gitee.com/laravel520/RXThinkCMF_LV5.8_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp3.2+Vue+ElementUI 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP3.2_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP3.2_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp3.2+Vue+AntDesign 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP3.2_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP3.2_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp5.1+Vue+ElementUI 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP5.1_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP5.1_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp5.1+Vue+AntDesign 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP5.1_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP5.1_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp6.x+Vue+ElementUI 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP6_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP6_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp6.x+Vue+AntDesign 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP6_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP6_PRO</a></td> 
  </tr> 
  <tr> 
   <td>Laravel8.x+Vue+ElementUI 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/laravel520/RXThinkCMF_EVL8_PRO">https://gitee.com/laravel520/RXThinkCMF_EVL8_PRO</a></td> 
  </tr> 
  <tr> 
   <td>Laravel8.x+Vue+AntDesign 旗舰版</td> 
   <td>最新开源版本，master 分支</td> 
   <td><a href="https://gitee.com/laravel520/RXThinkCMF_AVL8_PRO">https://gitee.com/laravel520/RXThinkCMF_AVL8_PRO</a></td> 
  </tr> 
 </tbody> 
</table> 
<h2>特别鸣谢</h2> 
<p>感谢<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.thinkphp.cn" target="_blank">ThinkPHP</a>、<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcn.vuejs.org" target="_blank">Vue</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2F2x.antdv.com%2Fcomponents%2Foverview-cn%2F" target="_blank">AntDesign</a>等优秀开源项目。</p>
                                        </div>
                                      
</div>
            