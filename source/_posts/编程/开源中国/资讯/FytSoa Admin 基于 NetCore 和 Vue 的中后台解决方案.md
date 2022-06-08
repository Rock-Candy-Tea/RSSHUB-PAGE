
---
title: 'FytSoa Admin 基于 NetCore 和 Vue 的中后台解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/feiyit/fytsoa/raw/master/doc/img/jiagou.png'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 11:30:00 GMT
thumbnail: 'https://gitee.com/feiyit/fytsoa/raw/master/doc/img/jiagou.png'
---

<div>   
<div class="content">
                                                                                            <h2>更新内容</h2> 
<blockquote> 
 <p>【新增】控制台可自定义编辑模块</p> 
 <p>【新增】站点管理模块，支持配置多个站点</p> 
 <p>【新增】投票模块完成，支持投票项自定义编辑，统计投票信息</p> 
 <p>【新增】授权增加API授权，服务端并验证是否有权限调用API，基本实现服务端权限至按钮级别</p> 
 <p>【优化】个人信息，支持修改</p> 
 <p>【优化】表格组件，增加打印和导出功能（列可自定义）</p> 
 <p>【更新】升级VueCli 5，使用webpack 5</p> 
 <p>【新增】.env.development .env.production 调整本地环境和生产环境模式</p> 
 <p>【优化】资源管理器升级上传组件，完成文件类型搜索以及刷新和复制链接功能</p> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:left">介绍</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">FytSoa Admin是一个快速搭建中后台解决方案，后台基于NetCore 6 和前端VUE3+Element+Plus实现。使用最新的前沿技术栈，提供各类使用组件方便在业务开发时调用，并且持续性的提供丰富的业务模块，帮助你快速搭建企业级中后台任务。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">表格支持右击快捷键菜单<br> 表格自定义列-打印<br> 表格自定义列-导出</p> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:left">架构图</h3> 
<div>
 <img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/jiagou.png" width="80%" referrerpolicy="no-referrer">
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">特点</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">模块化：全新的架构和模块化的开发机制，便于灵活扩展和二次开发</p> 
</blockquote> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">动态API</p> 
</blockquote> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">DDD模式-领域驱动设计</p> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:left">技术点</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">NetCore SDK 6.0+</p> 
</blockquote> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">ORM SqlSugar</p> 
</blockquote> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Mysql</p> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:left">后台教程</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888"># 数据库连接</span></span>

<span>在doc文件夹，通过数据库工具执行fytsoa.sql脚本</span>

<span><span style="color:#888888"># 修改连接字符串</span></span>

<span>打开FytSoa.ApiService,找到appsetting.json修改链接字符串，如果是开发环境，</span>

<span>可以修改appsettings.Development.json</span>

<span><span style="color:#888888"># 启动项目</span></span>

<span>打开终端，定位到FytSoa.ApiService目录，执行：dotnet run <span style="color:#008080">urls</span><span>=</span>http://<strong style="color:#000000">*</strong>:5100</span>

<span><span style="color:#888888"># 访问接口</span></span>

<span>打开浏览器：访问  http://localhost:5100/fytapiui/index.html   </span>
<span>如看到Swagger增强FytApi.MUI接口文档说明项目启动成</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">前端安装教程</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888"># 进入项目目录</span></span>

<span><span style="color:#0086b3">cd </span>admin</span>

<span><span style="color:#888888"># 安装依赖</span></span>

<span>cnpm i  或者  npm i</span>

<span><span style="color:#888888"># 启动项目(开发模式)</span></span>

<span>npm run serve</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">启动完成后浏览器访问<span> </span><a href="https://gitee.com/link?target=http%3A%2F%2Flocalhost%3A2800">http://localhost:2800</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">项目截图</h3> 
<p><img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/home.jpg" width="100%" referrerpolicy="no-referrer"><span style="background-color:#ffffff; color:#40485b"><span> </span></span><img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/dashboard.jpg" width="100%" referrerpolicy="no-referrer"><span style="background-color:#ffffff; color:#40485b"><span> </span></span><img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/usercenter.jpg" width="100%" referrerpolicy="no-referrer"><span style="background-color:#ffffff; color:#40485b"><span> </span></span><img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/admin.jpg" width="100%" referrerpolicy="no-referrer"><span style="background-color:#ffffff; color:#40485b"><span> </span></span><img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/authorize.jpg" width="100%" referrerpolicy="no-referrer"><span style="background-color:#ffffff; color:#40485b"><span> </span></span><img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/log.jpg" width="100%" referrerpolicy="no-referrer"><span style="background-color:#ffffff; color:#40485b"><span> </span></span><img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/file.jpg" width="100%" referrerpolicy="no-referrer"><span style="background-color:#ffffff; color:#40485b"><span> </span></span><img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/menu.jpg" width="100%" referrerpolicy="no-referrer"><span style="background-color:#ffffff; color:#40485b"><span> </span></span><img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/message.jpg" width="100%" referrerpolicy="no-referrer"><span style="background-color:#ffffff; color:#40485b"><span> </span></span><img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/site.jpg" width="100%" referrerpolicy="no-referrer"><span style="background-color:#ffffff; color:#40485b"><span> </span></span><img src="https://gitee.com/feiyit/fytsoa/raw/master/doc/img/vote.jpg" width="100%" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            