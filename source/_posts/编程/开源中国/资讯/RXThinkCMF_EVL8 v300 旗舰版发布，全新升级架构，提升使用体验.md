
---
title: 'RXThinkCMF_EVL8 v3.0.0 旗舰版发布，全新升级架构，提升使用体验'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/1.png'
author: 开源中国
comments: false
date: Fri, 25 Feb 2022 10:43:00 GMT
thumbnail: 'https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/1.png'
---

<div>   
<div class="content">
                                                                                            <p>v3.0.0 更新内容：<br> 1、前端UI架构全新升级，整体框架了做了重构和优化；<br> 2、模块Vue文件做列表页和编辑表单也分层设计，增强可维护性降低维护成本；<br> 3、优化用户管理模块，列表新增部门名称列；<br> 4、优化升级字典管理模块和配置管理模块；<br> 5、优化升级登录日志和操作日志；<br> 6、友链管理模块新增使用平台和友链类型筛选条件，表结构新增备注note字段；<br> 7、增强菜单管理模块，新增是否隐藏菜单hide字段;<br> 8、重构个人中心页面，去掉之前Base64头像上传方式，统一采用自研上传图片组件，服务器直接处理图片链接即可；<br> 9、优化会员管理模块，新增性别查询条件；<br> 10、重构代码生成器，重写自定义生成器模板，代码生成更友好，功能更强；<br> 11、重构菜单管理模块，调整菜单节点创建业务逻辑，采用全部删除重新创建的方式；<br> 12、优化会员管理模块，新增会员等级选项；<br> 13、职级管理模块新增导入、导出Excel文件的功能；</p> 
<h2>📚 项目介绍</h2> 
<p>一款 PHP 语言基于 Laravel8.x + Vue + ElementUI等框架精心打造的一款模块化、插件化、高性能的前后端分离架构敏捷开发框架，可用于快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，目前框架已集成了完整的RBAC权限架构和常规基础模块，前端Vue端支持多主题切换，可以根据自己喜欢的风格选择想一个的主题，实现了个性化呈现的需求；</p> 
<p>为了敏捷快速开发，提升研发效率，框架内置了一键CRUD代码生成器，自定义了模块生成模板，包括后端PHP文件模块和前端Vue端个性化模板，可以根据已建好的表结构(字段注释需规范)快速的一键生成整个模块的所有代码和增删改查等等功能业务，真正实现了低代码开发，极大的节省了人力成本的同时提高了开发效率，缩短了研发周期，是一款真正意义上实现组件化、低代码敏捷开发框架。</p> 
<h2>🍻 环境要求:</h2> 
<ul> 
 <li>PHP >= 7.3及以上</li> 
 <li>PDO PHP Extension</li> 
 <li>MBstring PHP Extension</li> 
 <li>CURL PHP Extension</li> 
 <li>开启静态重写</li> 
 <li>要求环境支持pathinfo</li> 
</ul> 
<h2>🍪 内置模块</h2> 
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
 <li>代码生成：一键生成模块CRUD的功能，包括后端和前端Vue等相关代码。</li> 
 <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
</ul> 
<h2>👷 开发者信息</h2> 
<ul> 
 <li>系统名称：RXThinkCMF_EVL8_PRO前后端分离框架</li> 
 <li>软件作者：@牧羊人</li> 
 <li>软件出处：南京RXThinkCMF研发中心</li> 
 <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.rxthink.cn" target="_blank">官网网址</a></li> 
 <li>文档网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.evl.pro.rxthink.cn" target="_blank">文档网址</a></li> 
 <li>开源协议：LGPL-3.0</li> 
</ul> 
<h2>🎨 系统演示</h2> 
<table> 
 <thead> 
  <tr> 
   <th>演示地址</th> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.evl.pro.rxthink.cn" target="_blank">点击查看演示环境</a></td> 
   <td>admin</td> 
   <td>123456</td> 
   <td>演示环境无法进行修改删除操作</td> 
  </tr> 
 </tbody> 
</table> 
<h2>📌 版本说明</h2> 
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
   <td>RXThinkCMF_TP3.2专业版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP3.2">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP3.2</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_TP3.2旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP3.2_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP3.2_PRO</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_TP5.1专业版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP5.1">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP5.1</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_TP5.1旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP5.1_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP5.1_PRO</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_TP6.x专业版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP6">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP6</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_TP6.x旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_TP6_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_TP6_PRO</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_LV5.8专业版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/laravel520/RXThinkCMF_LV5.8">https://gitee.com/laravel520/RXThinkCMF_LV5.8</a></td> 
  </tr> 
  <tr> 
   <td>RXThinkCMF_LV5.8旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/laravel520/RXThinkCMF_LV5.8_PRO">https://gitee.com/laravel520/RXThinkCMF_LV5.8_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp3.2+Vue+ElementUI旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP3.2_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP3.2_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp3.2+Vue+AntDesign旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP3.2_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP3.2_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp5.1+Vue+ElementUI旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP5.1_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP5.1_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp5.1+Vue+AntDesign旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP5.1_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP5.1_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp6.x+Vue+ElementUI旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP6_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_EVTP6_PRO</a></td> 
  </tr> 
  <tr> 
   <td>ThinkPhp6.x+Vue+AntDesign旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP6_PRO">https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP6_PRO</a></td> 
  </tr> 
  <tr> 
   <td>Laravel8.x+Vue+ElementUI旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/laravel520/RXThinkCMF_EVL8_PRO">https://gitee.com/laravel520/RXThinkCMF_EVL8_PRO</a></td> 
  </tr> 
  <tr> 
   <td>Laravel8.x+Vue+AntDesign旗舰版</td> 
   <td>最新开源版本，master分支</td> 
   <td><a href="https://gitee.com/laravel520/RXThinkCMF_AVL8_PRO">https://gitee.com/laravel520/RXThinkCMF_AVL8_PRO</a></td> 
  </tr> 
 </tbody> 
</table> 
<h2>🔧 模块展示</h2> 
<p><img alt="效果图1" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/1.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图3" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/3.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图4" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/4.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图5" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/5.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图7" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/7.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图8" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/8.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图9" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/9.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图10" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/10.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图11" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/11.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图12" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/12.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图13" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/13.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图14" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/14.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图17" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/17.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图18" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_EVL8_PRO/raw/master/public/uploads/demo/18.png" referrerpolicy="no-referrer"></p> 
<h2>✨ 特别鸣谢</h2> 
<p>感谢<a href="https://gitee.com/link?target=https%3A%2F%2Flearnku.com%2Flaravel">Laravel</a>、<a href="https://gitee.com/link?target=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN">ElementUI</a>、<a href="https://gitee.com/link?target=https%3A%2F%2Fcn.vuejs.org%2F">Vue</a>等优秀开源项目。</p>
                                        </div>
                                      
</div>
            