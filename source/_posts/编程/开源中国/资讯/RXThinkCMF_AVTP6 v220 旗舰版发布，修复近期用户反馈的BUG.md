
---
title: 'RXThinkCMF_AVTP6 v2.2.0 旗舰版发布，修复近期用户反馈的BUG'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c1cbffd4e6e1a07555d9bdd0ae766945266.png'
author: 开源中国
comments: false
date: Wed, 12 Jan 2022 08:46:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c1cbffd4e6e1a07555d9bdd0ae766945266.png'
---

<div>   
<div class="content">
                                                                                            <p>v2.2.0 更新内容：<br> 1、修改系统配置模块，修复复选框无法显示的问题；</p> 
<div> 
 <div> 
  <h2>📚 项目介绍</h2> 
  <p>一款 PHP 语言基于 ThinkPhp6.x + Vue + AntDesign等框架精心打造的一款模块化、插件化、高性能的前后端分离架构敏捷开发框架，可用于快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，目前框架已集成了完整的RBAC权限架构和常规基础模块，前端Vue端支持多主题切换，可以根据自己喜欢的风格选择想一个的主题，实现了个性化呈现的需求；</p> 
  <p>为了敏捷快速开发，提升研发效率，框架内置了一键CRUD代码生成器，自定义了模块生成模板，包括后端PHP文件模块和前端Vue端个性化模板，可以根据已建好的表结构(字段注释需规范)快速的一键生成整个模块的所有代码和增删改查等等功能业务，真正实现了低代码开发，极大的节省了人力成本的同时提高了开发效率，缩短了研发周期，是一款真正意义上实现组件化、低代码敏捷开发框架。</p> 
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
   <li>代码生成：一键生成模块CRUD的功能，包括后端和前端Vue等相关代码。</li> 
   <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
  </ul> 
  <h2>👷 开发者信息</h2> 
  <ul> 
   <li>系统名称：RXThinkCMF_AVTP6_PRO前后端分离框架</li> 
   <li>软件作者：@牧羊人</li> 
   <li>软件出处：南京RXThinkCMF研发中心</li> 
   <li>官网网址：<a href="https://gitee.com/link?target=http%3A%2F%2Fwww.rxthink.cn">http://www.rxthink.cn</a></li> 
   <li>文档网址：<a href="https://gitee.com/link?target=http%3A%2F%2Fdocs.avtp6.pro.rxthink.cn">http://docs.avtp6.pro.rxthink.cn</a></li> 
   <li>开源协议：LGPL-3.0</li> 
  </ul> 
  <h2>🎨 系统演示</h2> 
  <p>演示地址：<a href="https://gitee.com/link?target=http%3A%2F%2Fmanage.avtp6.pro.rxthink.cn">http://manage.avtp6.pro.rxthink.cn</a></p> 
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
  <p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-c1cbffd4e6e1a07555d9bdd0ae766945266.png" width="1920" referrerpolicy="no-referrer"></p> 
  <p><img alt="效果图2" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP6_PRO/raw/master/public/uploads/demo/2.png" referrerpolicy="no-referrer"></p> 
  <p><img alt="效果图3" src="https://gitee.com/ruoxi520_admin/RXThinkCMF_AVTP6_PRO/raw/master/public/uploads/demo/3.png" referrerpolicy="no-referrer"></p> 
 </div> 
</div> 
<h2>🍻 贡献者名单</h2> 
<p>@牧羊人</p> 
<h2>🍻 安全&缺陷</h2> 
<p>如果你发现了一个安全漏洞或缺陷，请发送邮件到 <a href="https://www.oschina.net/action/GoToLink?url=mailto%3Arxthinkcmf%40163.com" target="_blank">rxthinkcmf@163.com</a>,所有的安全漏洞都将及时得到解决。</p> 
<h2>✨ 特别鸣谢</h2> 
<p>感谢<a href="https://gitee.com/link?target=http%3A%2F%2Fwww.thinkphp.cn">ThinkPHP</a>、<a href="https://gitee.com/link?target=https%3A%2F%2Fcn.vuejs.org%2F">VueJs</a>、<a href="https://gitee.com/link?target=https%3A%2F%2F2x.antdv.com%2Fcomponents%2Foverview-cn%2F">AntDesign</a>等优秀开源项目。</p>
                                        </div>
                                      
</div>
            