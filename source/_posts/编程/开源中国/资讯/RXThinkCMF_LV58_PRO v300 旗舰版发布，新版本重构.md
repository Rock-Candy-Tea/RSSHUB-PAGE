
---
title: 'RXThinkCMF_LV5.8_PRO v3.0.0 旗舰版发布，新版本重构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f78452df333fd95b179b048ee6ef2cf11d0.png'
author: 开源中国
comments: false
date: Mon, 14 Feb 2022 10:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f78452df333fd95b179b048ee6ef2cf11d0.png'
---

<div>   
<div class="content">
                                                                                            <p>v3.0.0更新如下:<br> 1、重构系统操作日志功能，详细系统操作人信息；<br> 2、重构系统登录日志功能，准确详细的记录登录、退出时用户的状态信息；<br> 3、重新设计系统登录背景图，提升视觉效果提升用户使用体验；<br> 4、重构代码生成器，完善代码生成器表名精确搜索功能；<br> 5、重构系统工具演示案例，新增两个演示案例，丰富了表单元素；<br> 6、重构系统菜单层级显示，新增三级菜单显示，案例如系统工具菜单栏；<br> 7、代码生成器新增批量生成模块的功能，可以选择多张表批量同步生成；<br> 8、解决代码生成器生成模块时有重复内容的问题；目前已采用单库单表结构生成规则；<br> 9、重构部门管理模块，数据表sys_dep变更为sys_dept,新增部门全称、部门编码、部门类型等等字段；<br> 10、重构字典管理模块，数据表sys_dict_type变成为sys_dict ,sys_dic便成为sys_dict_data;相应文件名也同步更新；<br> 11、重构配置管理模块，数据表sys_config_group变成为sys_config ,sys_config便成为sys_config_data;相应文件名也同步更新；<br> 12、重写系统欢迎页，新增百度EChart统计；<br> 13、升级菜单管理功能，新增导入数据和导出数据权限节点；<br> 14、系统架构新增导入、导出核心组件，使用时可以直接调用；<br> 15、职级管理模块新增导入、导出Excel的案例功能，方便开发者参考；<br> 16、菜单管理模块表单编辑进行重构，新增导入、导出、设置权限、重置密码等权限节点；<br> 17、重构个人中心模块，解决样式错乱以及保存后未及时刷新的问题；<br> 18、升级代码生成器，自动化生成菜单菜单进行优化和调整；<br> 19、升级网站配置模块，表单参数和内容进行优化处理；<br> 20、新增系统设置菜单，网站设置调整到新的菜单下，便于合理的功能划分；</p> 
<h2>📚 项目介绍</h2> 
<p>一款 PHP 语言基于 Laravel5.8 + Layui + MySQL等框架精心打造的一款模块化、插件化、高性能的前后端分离架构敏捷开发框架，可用于快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，框架自研了一套个性化的组件，实现了可插拔的组件式开发方式：单图上传、多图上传、下拉选择、开关按钮、单选按钮、多选按钮、图片裁剪等等一系列个性化、轻量级的组件，是一款真正意义上实现组件化开发的敏捷开发框架，框架已集成了完整的RBAC权限架构和常规基础模块，同时支持多主题切换，可以根据自己喜欢的风格选择想一个的主题，实现了个性化呈现的需求；</p> 
<p>为了敏捷快速开发，提升研发效率，框架内置了一键CRUD代码生成器，自定义了模块生成模板，可以根据已建好的表结构(字段注释需规范)快速的一键生成整个模块的所有代码和增删改查等等功能业务，真正实现了低代码开发，极大的节省了人力成本的同时提高了开发效率，缩短了研发周期，是一款真正意义上实现组件化、低代码敏捷开发框架。</p> 
<h2>🍻 环境要求:</h2> 
<ul> 
 <li>PHP >= 7.3</li> 
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
 <li>代码生成：一键生成模块CRUD的功能，包括后端和前端等相关代码。</li> 
 <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
</ul> 
<h2>👷 开发者信息</h2> 
<ul> 
 <li>系统名称：RXThinkCMF_LV5.8_PRO混编旗舰版</li> 
 <li>软件作者：@牧羊人</li> 
 <li>软件出处：南京RXThinkCMF研发中心</li> 
 <li>软件咨询：<a href="https://gitee.com/link?target=http%3A%2F%2Fwpa.qq.com%2Fmsgrd%3Fv%3D3%26uin%3D1051386190%26site%3Dqq%26menu%3Dyes">1051386190</a></li> 
 <li>官网网址：<a href="https://gitee.com/link?target=http%3A%2F%2Fwww.rxthink.cn">http://www.rxthink.cn</a></li> 
 <li>文档网址：<a href="https://gitee.com/link?target=http%3A%2F%2Fdocs.lv5.8.rxthink.cn">http://docs.lv5.8.rxthink.cn</a></li> 
 <li>开源协议：LGPL-3.0</li> 
</ul> 
<h2>🎨 系统演示</h2> 
<p>演示地址：<a href="https://gitee.com/link?target=http%3A%2F%2Fmanage.lv5.8.pro.rxthink.cn">http://manage.lv5.8.pro.rxthink.cn</a></p> 
<table> 
 <thead> 
  <tr> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>admin</td> 
   <td>123456</td> 
   <td>演示环境无法进行修改删除操作</td> 
  </tr> 
 </tbody> 
</table> 
<h2>🔧 模块展示</h2> 
<p><br> <img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-f78452df333fd95b179b048ee6ef2cf11d0.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-5a09d56c588140867e321d1e5d1fa64057d.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-f3d62a3e4b9ce547114b150f0e43a35fedd.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-5b61e7dcc0f2ca1880ecc2ef24b8b6d81a4.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-59a27014ead6fee295a79096115de37696c.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            