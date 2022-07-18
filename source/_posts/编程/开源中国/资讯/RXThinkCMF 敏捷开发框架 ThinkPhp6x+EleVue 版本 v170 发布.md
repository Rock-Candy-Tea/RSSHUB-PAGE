
---
title: 'RXThinkCMF 敏捷开发框架 ThinkPhp6.x+EleVue 版本 v1.7.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7021'
author: 开源中国
comments: false
date: Mon, 18 Jul 2022 09:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7021'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>v1.7.0更新内容：</strong></p> 
<p>1、重点解决添加和更新数据时添加人、创建时间、更新时间问题，重点修改文件BaseModel.php;<br> 2、解决模块列表创建时间和更新时间显示不对的问题，统一时间*1000；<br> 3、修复近期用户使用过程中反馈的BUG；<br> 4、数据表更名为：evtp6.pro;<br> 5、升级会员管理模块，解决所属城市无法存储和展示问题，字段变更如下：province_id变更为province_code，city_id变更为city_code,district_id变更为district_code;<br> 6、修复会员等级模块创建日期和更新日期无法显示问题；<br> 7、升级系统用户管理模块，新增城市选择、详细地址、所属部门、状态、备注等信息；evt_user表做了更新，province_id变更为province_code，city_id变更为city_code,district_id变更为district_code;<br> 8、重构字典模块，前端Vue做了更新优化，数据表evt_dict变更为evt_dict_data, evt_dicttype变更为evt_dict;<br> 9、重构配置模块，前端Vue做了优化升级，数据表evt_config变更为evt_config_data,evt_configgroup变更为evt_config;<br> 10、修复部门管理模块BUG，删除POST请求地址进行纠正；<br> 11、菜单管理模块做了优化升级，之前由于菜单管理列表改成异步加载，导致添加或编辑菜单时上线菜单无法选择，由此进行了升级优化；<br> 12、城市管理模块做了优化升级，城市表evt_city数据源进行了重新采集；<br> 13、解决添加和更新数据时无法存储用户ID的问题；<br> 14、解决近期用户使用过程中反馈的BUG修复；</p> 
<p> </p> 
<h2>项目介绍</h2> 
<p>一款 PHP 语言基于 ThinkPhp6.x、Vue、ElementUI 等框架精心打造的一款模块化、插件化、高性能的前后端分离架构敏捷开发框架，可用于快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，目前框架已集成了完整的 RBAC 权限架构和常规基础模块，前端 Vue 端支持多主题切换，可以根据自己喜欢的风格选择想一个的主题，实现了个性化呈现的需求；</p> 
<p>为了敏捷快速开发，提升研发效率，框架内置了一键 CRUD 代码生成器，自定义了模块生成模板，包括后端 PHP 文件模块和前端 Vue 端个性化模板，可以根据已建好的表结构 (字段注释需规范) 快速的一键生成整个模块的所有代码和增删改查等等功能业务，真正实现了低代码开发，极大的节省了人力成本的同时提高了开发效率，缩短了研发周期，是一款真正意义上实现组件化、低代码敏捷开发框架。</p> 
<h2>环境要求:</h2> 
<ul> 
 <li>PHP >= 7.3 (推荐 7.3)</li> 
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
 <li>软件名称：RXThinkCMF 敏捷开发框架 ThinkPhp6.x+EleVue 版本</li> 
 <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.rxthink.cn" target="_blank">http://www.rxthink.cn</a></li> 
 <li>文档网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.evtp6.pro.rxthink.cn" target="_blank">http://docs.evtp6.pro.rxthink.cn</a></li> 
</ul> 
<h2>系统演示</h2> 
<ul> 
 <li>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.evtp6.pro.rxthink.cn" target="_blank">http://manage.evtp6.pro.rxthink.cn</a></li> 
</ul>
                                        </div>
                                      
</div>
            