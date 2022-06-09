
---
title: 'EasyGoAdmin 敏捷开发框架 Iris+Layui 版本 v2.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a56170e0b1391d0edfb18be9745f88f07b0.png'
author: 开源中国
comments: false
date: Thu, 09 Jun 2022 15:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a56170e0b1391d0edfb18be9745f88f07b0.png'
---

<div>   
<div class="content">
                                                                                            <p>v2.0.0 更新内容：<br> 1、设计、规划和研发基础RBAC权限架构；<br> 2、编写框架核心底层代码，设计基于Layout布局的模板，设计并编写自定义模板html文件；<br> 3、对系统模板进行架构设计及模板继承相关设计；<br> 4、研发框架基础模块，如字典、配置、行政区划管理等等常规基础模块；<br> 5、设计并研发代码生成器，根据表结构动态解析并生成模块文件和增删改查功能；<br> 6、设计并研发一系列其他配套功能很常规使用函数；<br> 7、设计并研发框架核心组件widget;<br> 8、完善系统模块，重写系统数据；</p> 
<h2>项目介绍</h2> 
<p>一款 Go 语言基于 Iris、Layui、MySQL 等框架精心打造的一款模块化、高性能、企业级的敏捷开发框架，本着简化开发、提升开发效率的初衷触发，框架自研了一套个性化的组件，实现了可插拔的组件式开发方式：单图上传、多图上传、下拉选择、开关按钮、单选按钮、多选按钮、图片裁剪等等一系列个性化、轻量级的组件，是一款真正意义上实现组件化开发的敏捷开发框架。</p> 
<h2>项目特点</h2> 
<ul> 
 <li>模块化、松耦合</li> 
 <li>模块丰富、开箱即用</li> 
 <li>简洁易用、快速接入</li> 
 <li>文档详尽、易于维护</li> 
 <li>自顶向下、体系化设计</li> 
 <li>统一框架、统一组件、降低选择成本</li> 
 <li>开发规范、设计模式、代码分层模型</li> 
 <li>强大便捷的开发工具链</li> 
 <li>完善的本地中文化支持</li> 
 <li>设计为团队及企业使用</li> 
</ul> 
<h2>内置模块</h2> 
<ul> 
 <li>用户管理：用于维护管理系统的用户，常规信息的维护与账号设置。</li> 
 <li>角色管理：角色菜单管理与权限分配、设置角色所拥有的菜单权限。</li> 
 <li>菜单管理：配置系统菜单，操作权限，按钮权限标识等。</li> 
 <li>职级管理：主要管理用户的职级。</li> 
 <li>岗位管理：主要管理用户担任职务。</li> 
 <li>部门管理：配置系统组织机构（公司、部门、小组），树结构展现支持数据权限。</li> 
 <li>字典管理：对系统中常用的较为固定的数据进行统一维护。</li> 
 <li>配置管理：对系统的常规配置信息进行维护，网站配置管理功能进行统一维护。</li> 
 <li>通知公告：系统通知公告信息发布维护。</li> 
 <li>操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。</li> 
 <li>登录日志：系统登录日志记录查询包含登录异常。</li> 
 <li>代码生成：一键生成模块 CRUD 的功能，包括后端 Go 和前端 HTML、JS 等相关代码。</li> 
 <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
</ul> 
<h2>软件信息</h2> 
<ul> 
 <li>系统名称：EasyGoAdmin敏捷开发框架Iris+Layui版本</li> 
 <li>软件作者：@半城风雨 团队荣誉出品</li> 
 <li>软件出处：深圳 EasyGoAdmin 研发中心</li> 
 <li>软件协议：LGPL-3.0</li> 
 <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.easygoadmin.vip" target="_blank">http://www.easygoadmin.vip</a></li> 
 <li>文档网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.iris.layui.easygoadmin.vip" target="_blank">http://docs.iris.layui.easygoadmin.vip</a></li> 
</ul> 
<h2>系统演示</h2> 
<ul> 
 <li>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.iris.layui.easygoadmin.vip" target="_blank">http://manage.iris.layui.easygoadmin.vip</a></li> 
</ul> 
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
<h2>版本说明</h2> 
<table> 
 <thead> 
  <tr> 
   <th>版本名称</th> 
   <th>版本说明</th> 
   <th>版本地址</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>GoFrame+Layui 混编版</td> 
   <td>采用 GoFrame、Layui 等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_Layui</a></td> 
  </tr> 
  <tr> 
   <td>Beego+Layui 混编版</td> 
   <td>采用 Beego、Layui 等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_Layui</a></td> 
  </tr> 
  <tr> 
   <td>Gin+Layui 混编版</td> 
   <td>采用 Gin、Layui 等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_Layui</a></td> 
  </tr> 
  <tr> 
   <td>Iris+Layui 混编版</td> 
   <td>采用 Iris、Layui 等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_Layui</a></td> 
  </tr> 
  <tr> 
   <td>GoFrame+EleVue 前后端分离版</td> 
   <td>采用 GoFrame、Vue、ElementUI 等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>Beego+EleVue 前后端分离版</td> 
   <td>采用 Beego、Vue、ElementUI 等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>Gin+EleVue 前后端分离版</td> 
   <td>采用 Gin、Vue、ElementUI 等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>Iris+EleVue 前后端分离版</td> 
   <td>采用 Iris、Vue、ElementUI 等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>GoFrame+AntdVue 前后端分离版</td> 
   <td>采用 GoFrame、Vue、AntDesign 等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td>Beego+AntdVue 前后端分离版</td> 
   <td>采用 Beego、Vue、AntDesign 等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td>Gin+AntdVue 前后端分离版</td> 
   <td>采用 Gin、Vue、AntDesign 等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td>Iris+AntdVue 前后端分离版</td> 
   <td>采用 Iris、Vue、AntDesign 等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_AntdVue</a></td> 
  </tr> 
 </tbody> 
</table> 
<h2>核心组件</h2> 
<ul> 
 <li>单图上传组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;upload_image <span>"avatar|头像|90x90|建议上传尺寸450x450|450x450"</span> .info.Avatar <span>""</span> <span>0</span>&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>多图上传组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;album <span>"avatar|图集|90x90|20|建议上传尺寸450x450"</span> .info.Avatar <span>""</span> <span>0</span>&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>下拉选择组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;<span>select</span> <span>"gender|1|性别|name|id"</span> <span>"1=男,2=女,3=保密"</span> .info.Gender&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>单选按钮组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;radio <span>"gender|name|id"</span> <span>"1=男,2=女,3=保密"</span> .info.Gender&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>复选框组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;checkbox <span>"role_ids|name|id"</span> .roleList .info.RoleIds&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>城市选择组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span><span>&#123;&#123;city</span> <span>.info.DistrictCode</span> <span>3</span> <span>1</span><span>&#125;&#125;</span></span></pre> 
 </div> 
</div> 
<ul> 
 <li>开关组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;<span>switch</span> <span>"status"</span> <span>"在用|禁用"</span> .info.Status&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>日期组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;<span>date</span> <span>"birthday|1|出生日期|date"</span> .info.Birthday&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>图标组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;<span>icon</span> "<span>icon</span>" <span>.info</span><span>.Icon</span>&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>穿梭组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;transfer <span>"func|0|全部节点,已赋予节点|name|id|220x350"</span> <span>"1=列表,5=添加,10=修改,15=删除,20=详情,25=状态,30=批量删除,35=添加子级,40=全部展开,45=全部折叠"</span> .funcList&#125;&#125;</span></pre> 
 </div> 
</div> 
<h2>模块展示</h2> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-a56170e0b1391d0edfb18be9745f88f07b0.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            