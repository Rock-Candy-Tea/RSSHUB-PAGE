
---
title: 'UJCMS 3.0.0 发布，全面使用国密加密算法'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-80a0ebd93df8b45fee97e5ee120780e5c78.jpg'
author: 开源中国
comments: false
date: Tue, 14 Jun 2022 08:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-80a0ebd93df8b45fee97e5ee120780e5c78.jpg'
---

<div>   
<div class="content">
                                                                                            <p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; text-align:left">全面使用国密加密算法，包括SM2、SM3、SM4、HmacSM3、PBKDF2WithHmacSM3。增加多站点的演示，以及完善多站点的管理和多站点的权限控制，完善用户、角色的管理和授权功能。增加了Markdown编辑器、后台多页签、对象存储、文库及DOC导入功能。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; text-align:left">破坏性更新包括：</p> 
<ul> 
 <li>使用escape标签处理XSS和空值。所有freemarker页面使用<code>[#escape x as (x)!?html]</code>开头和<code>[/#escape]</code>结尾；使用<code>[#noescape]...[/#noescape]</code>功能替换原有的<code>?no_esc</code></li> 
 <li>密码需用新算法重置</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">升级日志（3.0.0）</h2> 
<ul> 
 <li>新增：系统信息功能</li> 
 <li>新增：密码使用国密PBKDF2WithHmacSM3加密</li> 
 <li>新增：登录时密码传输使用国密SM2非对称加密</li> 
 <li>新增：JWT使用国密HmacSM3加密</li> 
 <li>新增：JWT token使用国密SM4加密</li> 
 <li>新增：随机密钥生成功能</li> 
 <li>新增：前台模板使用escape标签处理XSS和空值问题</li> 
 <li>新增：后台管理界面多页签功能</li> 
 <li>新增：后台管理界面session失效后，自动显示登录框，登录后保留在原页面，防止页面数据丢失</li> 
 <li>新增：区块项新增功能</li> 
 <li>新增：DOC导入功能</li> 
 <li>新增：文库转换功能</li> 
 <li>新增：文库封面自动截图</li> 
 <li>新增：文章管理增加Markdown编辑器</li> 
 <li>新增：附件、HTML静态页、模板支持对象存储（MinIO、阿里云对象存储、腾讯云对象存储、七牛云对象存储）</li> 
 <li>优化：富文本编辑器的字体从16px改为14px</li> 
 <li>优化：富文本编辑器即时校验功能</li> 
 <li>优化：增加上传功能的错误提示</li> 
 <li>优化：application.properties改为application.yaml，避免注释的中文无法在普通编辑器中显示</li> 
 <li>修复：文章管理图片集上传框未对齐</li> 
 <li>修复：删除有图片集的文章报错</li> 
 <li>修复：视频无法上传</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">简介</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left">UJCMS 是在 Jspxcms 多年的开发经验上，重新设计开发的 Java 开源内容管理系统 (java cms)。使用 SpringBoot、MyBatis、Shiro、Lucene、FreeMarker、TypeScript、Vite2、Vue3、ElementPlus2、等技术。针对原系统中的一些痛点问题，进行解决、优化和改进，并使用<span> </span><code>GPL-2</code><span> </span>开源协议发布，可免费商用。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left">技术上选择主流、先进、简单的架构，方便用户进行二次开发。持久化层用 MyBatis 替换了 Hibernate；视图层用前后端分离的 Vue3 替换了 JSP；数据库也进行了重新设计。设计上强调 “简单”、“灵活”，避免繁杂的设计和实现，降低系统维护成本和二次开发难度。功能使用上也要求 “简单”，避免复杂的使用逻辑。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>官网地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ujcms.com%2F" target="_blank">https://www.ujcms.com</a></li> 
 <li>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ujcms.com%2Fdownload%2F" target="_blank">https://www.ujcms.com/download/</a><span> </span>提供安装包下载。</li> 
 <li>演示站前台：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.ujcms.com%2F" target="_blank">https://demo.ujcms.com</a><span> </span>使用手机访问或者浏览器手机模式访问前台，会自动呈现手机页面。</li> 
 <li>演示站后台：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.ujcms.com%2Fcp%2F" target="_blank">https://demo.ujcms.com/cp/</a><span> </span>演示用户登录后只拥有浏览后台功能，所有操作功能点击后都会显示无权访问（403）。如需进行操作测试，可以下载软件到本地安装。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">技术及功能亮点</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left"><strong>自定义字段可查询</strong>：所有的自定义字段都可查询增强了系统的灵活性。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left"><strong>自定义字段可视化设计</strong>：自定义字段使用拖拽式的可视化设计，所见即所得。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left"><strong>URL 地址 SEO 优化</strong>：栏目和文章的动态地址可以通过系统的全局设置功能进行修改。默认的栏目和文章 URL 地址前缀为<span> </span><code>/channel</code><span> </span>和<span> </span><code>/article</code>，可以根据自己的需要修改，如改为<span> </span><code>/categories</code><span> </span>和<span> </span><code>/archives</code>。多站点的情况下，子站点 URL 地址也由原来的<span> </span><code>www.example.com/site-abc</code><span> </span>的形式改为更友好的<span> </span><code>www.example.com/abc</code><span> </span>的形式。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left"><strong>清理垃圾附件</strong>：系统使用时，可能会多传、误传图片等附件；在删除文章后，文章中的图片还保留在系统中，产生大量的未使用的垃圾图片和附件。系统中的附件管理可以查看所有未使用的图片和附件，并可对其进行删除。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left"><strong>附件、模板、索引文件独立部署</strong>：系统运行时产生的文件可以和程序分开，部署到独立的目录，方便系统备份、升级和管理。比如上传的图片和附件、前台的模板、索引文件，都可以部署到程序以外的目录。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left"><strong>模板文件和 CSS、JS 在同一目录</strong>：模板文件和 CSS、JS 分开的目录结构，会给模板制作和部署带来很大的不便性。而将模板文件和 CSS、JS 放在一起的设计，会方便很多。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left"><strong>MyBatis 参数化查询</strong>：后台数据通常会需要通过不同字段进行搜索，对每个表都写大量的查询，无疑是一项繁重的工作。MyBatis 参数化查询功能通过前台传递查询参数，即可实现任意字段及关联表的查询功能（如：Q_title=abc，Q_user-username=test），无需后台编写代码，大幅减少后端的开发工作量。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left"><strong>主副表拆分</strong>：对查询量大的复杂表进行主副表拆分，把常用的查询字段放到主表，不常用的字段放到副表，提升大数据量下的性能表现。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">后端技术</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>SpringBoot：提供了对 Spring 开箱即用的功能。简化了 Spring 配置，提供自动配置 auto-configuration 功能。</li> 
 <li>SpringMVC：MVC 框架，使用方便，Bug 较少。</li> 
 <li>Mybatis：持久化框架。</li> 
 <li>FreeMarker：网站模板组件。</li> 
 <li>Shiro：安全组件。配置简便。</li> 
 <li>Lucene：全文检索组件。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">前端技术</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Vue 3：JavaScript 框架。</li> 
 <li>ElementPlus 2：Vue 3 UI 框架。</li> 
 <li>Vite 2：下一代前端开发与构建工具。</li> 
 <li>TypeScript: JavaScript 的一个超集。</li> 
 <li>TailwindCSS: 功能类优先的 CSS 框架。</li> 
 <li>Tinymce: 富文本编辑器。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能列表</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>内容 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>文章管理</li> 
   <li>栏目管理</li> 
   <li>区块管理</li> 
   <li>附件管理</li> 
   <li>生成管理</li> 
  </ul> </li> 
 <li>配置 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>全局设置</li> 
   <li>站点设置</li> 
   <li>模型管理</li> 
   <li>区块设置</li> 
   <li>字典类型</li> 
   <li>字典数据</li> 
  </ul> </li> 
 <li>用户 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>用户管理</li> 
   <li>角色管理</li> 
   <li>用户组管理</li> 
   <li>组织管理</li> 
  </ul> </li> 
 <li>系统 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>站点管理</li> 
   <li>储存点管理</li> 
  </ul> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">前台模板</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left"><img alt height="1934" src="https://oscimg.oschina.net/oscnet/up-80a0ebd93df8b45fee97e5ee120780e5c78.jpg" width="1351" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">后台界面</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; margin-left:0px; margin-right:0px; text-align:left"><img alt height="713" src="https://oscimg.oschina.net/oscnet/up-cfe14e42ecbeb17974c201494ee2c931758.jpg" width="1367" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            