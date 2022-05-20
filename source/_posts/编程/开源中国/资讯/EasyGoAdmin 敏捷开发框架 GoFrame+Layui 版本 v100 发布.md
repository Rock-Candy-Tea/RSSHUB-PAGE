
---
title: 'EasyGoAdmin 敏捷开发框架 GoFrame+Layui 版本 v1.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f73ef815a7c9a79b45a729109d4e98566b0.png'
author: 开源中国
comments: false
date: Fri, 20 May 2022 11:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f73ef815a7c9a79b45a729109d4e98566b0.png'
---

<div>   
<div class="content">
                                                                                            <p>v1.0.0 更新内容：<br> 1、设计、规划和研发基础 RBAC 权限架构；<br> 2、编写框架核心底层代码，设计基于 Layout 布局的模板，设计并编写自定义模板 html 文件；<br> 3、对系统模板进行架构设计及模板继承相关设计；<br> 4、研发框架基础模块，如字典、配置、行政区划管理等等常规基础模块；<br> 5、设计并研发代码生成器，根据表结构动态解析并生成模块文件和增删改查功能；<br> 6、设计并研发一系列其他配套功能很常规使用函数；<br> 7、设计并研发框架核心组件 widget;</p> 
<h2>项目介绍</h2> 
<p>一款 Go 语言基于GoFrame、Layui、MySQL等框架精心打造的一款模块化、高性能、企业级的敏捷开发框架，本着简化开发、提升开发效率的初衷触发，框架自研了一套个性化的组件，实现了可插拔的组件式开发方式：单图上传、多图上传、下拉选择、开关按钮、单选按钮、多选按钮、图片裁剪等等一系列个性化、轻量级的组件，是一款真正意义上实现组件化开发的敏捷开发框架。</p> 
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
 <li>代码生成：一键生成模块CRUD的功能，包括后端Go和前端HTML、JS等相关代码。</li> 
 <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
</ul> 
<h2>软件信息</h2> 
<ul> 
 <li>软件名称：EasyGoAdmin敏捷开发框架GoFrame+Layui版本</li> 
 <li>软件作者：@半城风雨 团队荣誉出品</li> 
 <li>软件出处：深圳EasyGoAdmin研发中心</li> 
 <li>软件协议：LGPL-3.0</li> 
 <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.easygoadmin.vip" target="_blank">官网地址</a></li> 
 <li>文档网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.goframe.layui.easygoadmin.vip" target="_blank">文档地址</a></li> 
</ul> 
<h2>系统演示</h2> 
<ul> 
 <li>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.goframe.layui.easygoadmin.vip" target="_blank">点击查看演示环境</a></li> 
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
   <td>GoFrame+Layui混编版</td> 
   <td>采用GoFrame、Layui等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_Layui</a></td> 
  </tr> 
  <tr> 
   <td>Beego+Layui混编版</td> 
   <td>采用Beego、Layui等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_Layui</a></td> 
  </tr> 
  <tr> 
   <td>Gin+Layui混编版</td> 
   <td>采用Gin、Layui等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_Layui</a></td> 
  </tr> 
  <tr> 
   <td>Iris+Layui混编版</td> 
   <td>采用Iris、Layui等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_Layui</a></td> 
  </tr> 
  <tr> 
   <td>GoFrame+EleVue前后端分离版</td> 
   <td>采用GoFrame、Vue、ElementUI等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>Beego+EleVue前后端分离版</td> 
   <td>采用Beego、Vue、ElementUI等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>Gin+EleVue前后端分离版</td> 
   <td>采用Gin、Vue、ElementUI等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>Iris+EleVue前后端分离版</td> 
   <td>采用Iris、Vue、ElementUI等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>GoFrame+AntdVue前后端分离版</td> 
   <td>采用GoFrame、Vue、AntDesign等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td>Beego+AntdVue前后端分离版</td> 
   <td>采用Beego、Vue、AntDesign等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td>Gin+AntdVue前后端分离版</td> 
   <td>采用Gin、Vue、AntDesign等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td>Iris+AntdVue前后端分离版</td> 
   <td>采用Iris、Vue、AntDesign等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_AntdVue</a></td> 
  </tr> 
 </tbody> 
</table> 
<h2>项目结构</h2> 
<div> 
 <div> 
  <pre><span>├── app             // 应用目录</span>
<span>│   ├── controller  // 控制器</span>
<span>│   ├── dao         // DAO层</span>
<span>│   ├── model       // 模型层</span>
<span>│   └── service     // 服务层</span>
<span>│   └── utils       // 系统工具</span>
<span>│   └── widget      // 核心组件</span>
<span>├── boot</span>
<span>├── config          // 系统配置</span>
<span>├── docker</span>
<span>├── document        // 文档目录</span>
<span>├── i18n            // 国际化</span>
<span>├── library         // 类库</span>
<span>├── packed</span>
<span>├── public          // 资源目录</span>
<span>├── router          // 路由</span>
<span>├── template        // 模板</span>
<span>├── Dockerfile</span>
<span>├── go.mod</span>
<span>└── main.go</span></pre> 
 </div> 
</div> 
<h2>核心组件</h2> 
<ul> 
 <li>单图上传组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;upload_image "avatar|头像|90x90|建议上传尺寸450x450|450x450" .info.Avatar "" 0&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>多图上传组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;album "avatar|图集|90x90|20|建议上传尺寸450x450" .info.Avatar "" 0&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>下拉选择组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;select "gender|1|性别|name|id" "1=男,2=女,3=保密" .info.Gender&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>单选按钮组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;radio "gender|name|id" "1=男,2=女,3=保密" .info.Gender&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>复选框组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;checkbox "role_ids|name|id" .roleList .info.RoleIds&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>城市选择组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;city .info.DistrictCode 3 1&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>开关组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;switch "status" "在用|禁用" .info.Status&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>日期组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;date "birthday|1|出生日期|date" .info.Birthday&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>图标组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;icon "icon" .info.Icon&#125;&#125;</span></pre> 
 </div> 
</div> 
<ul> 
 <li>穿梭组件</li> 
</ul> 
<div> 
 <div> 
  <pre><span>&#123;&#123;transfer "func|0|全部节点,已赋予节点|name|id|220x350" "1=列表,5=添加,10=修改,15=删除,20=详情,25=状态,30=批量删除,35=添加子级,40=全部展开,45=全部折叠" .funcList&#125;&#125;</span></pre> 
 </div> 
</div> 
<h2>模块展示</h2> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-f73ef815a7c9a79b45a729109d4e98566b0.png" width="1920" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            