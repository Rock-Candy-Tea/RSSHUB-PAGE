
---
title: 'RXThinkCMF 敏捷开发框架 ThinkPhp6.x+EleVue 版本 v1.8.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7922'
author: 开源中国
comments: false
date: Wed, 03 Aug 2022 10:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7922'
---

<div>   
<div class="content">
                                                                                            <p>v1.8.0更新内容：<br> 1、升级代码生成器，解决生成时内容重复的问题；<br> 2、重构前端Vue自定义生成模板，主要优化查询条件那块，实现动态识别并创建多场景筛选条件；<br> 3、优化生成器管理模块，对接表名称、表描述筛选条件，后端服务业务进行重整；<br> 4、解决之前版本代码生成器列表页创建时间和更新时间无法显示的问题；<br> 5、解决近期用户使用过程中反馈的BUG；<br> 6、新增CMS文章管理模块，由于文章编辑页内容较多，采用抽屉展开效果，未采用传统的直接弹窗模式；<br> 7、菜单做了划分，站点和栏目管理调整值CMS管理菜单中；<br> 8、升级通知公告模块，升级编辑器，同文章管理同步，同时新增内容支持图文自动化处理机制；<br> 9、前端系统新增多环境发布配置，文件分别为：开发环境(.env.development)、测试环境(.env.test)、线上环境(.env.production)<br> 10、更新用户管理模块，添加或编辑后重置用户整体缓存；</p> 
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
            