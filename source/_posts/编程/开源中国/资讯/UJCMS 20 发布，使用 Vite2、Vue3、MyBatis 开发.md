
---
title: 'UJCMS 2.0 发布，使用 Vite2、Vue3、MyBatis 开发'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-80a0ebd93df8b45fee97e5ee120780e5c78.jpg'
author: 开源中国
comments: false
date: Tue, 08 Mar 2022 09:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-80a0ebd93df8b45fee97e5ee120780e5c78.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292e; text-align:left">本次主要增加了用户比较关心的页面静态化功能、下载防盗链等功能。并且使用liquibase管理数据库版本，实现数据库表结构自动创建和自动升级功能，以及首次运行自动插入数据库初始化数据，免去了用户手动执行sql脚本的工作。</p> 
<p style="color:#24292e; text-align:left">随着ElementPlus2正式版发布，意味着Vue3的生态已经完善。UJCMS对前端技术进行了完整的更新，打包工具从webpack迁移到vite2，ElementPlus也升级到了2.0正式版，TailwindCSS升级到3.0。</p> 
<h2 style="text-align:left">升级日志（2.0.0）</h2> 
<ul> 
 <li>新增静态页生成功能</li> 
 <li>新增静态页设置功能</li> 
 <li>新增任务管理功能</li> 
 <li>新增防盗链下载功能</li> 
 <li>新增下载文件名可为中文</li> 
 <li>数据库表结构自动创建及自动升级功能</li> 
 <li>首次运行数据自动初始化</li> 
 <li>支持国产数据库</li> 
 <li>使用vite2代替webpack</li> 
 <li>升级到element-plus-2.0正式版</li> 
 <li>修复新窗口打开选项无效的问题</li> 
 <li>修复api/auth/jwt/login登录接口不加Authorization的header会出现403的问题</li> 
</ul> 
<h2 style="text-align:left">简介</h2> 
<p style="color:#24292e; text-align:left">UJCMS是在Jspxcms多年的开发经验上，重新设计开发的Java开源内容管理系统(java cms)。使用SpringBoot、MyBatis、Shiro、Lucene、FreeMarker、TypeScript、Vite2、Vue3、ElementPlus2、等技术。针对原系统中的一些痛点问题，进行解决、优化和改进，并使用<code>AGPL-3</code>开源协议发布，可免费商用。</p> 
<p style="color:#24292e; text-align:left">技术上选择主流、先进、简单的架构，方便用户进行二次开发。持久化层用MyBatis替换了Hibernate；视图层用前后端分离的Vue3替换了JSP；数据库也进行了重新设计。设计上强调“简单”、“灵活”，避免繁杂的设计和实现，降低系统维护成本和二次开发难度。功能使用上也要求“简单”，避免复杂的使用逻辑。</p> 
<ul> 
 <li>官网地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ujcms.com%2F" target="_blank">https://www.ujcms.com</a></li> 
 <li>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ujcms.com%2Fdownload%2F" target="_blank">https://www.ujcms.com/download/</a><span> </span>提供安装包下载。</li> 
 <li>演示站前台：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.ujcms.com%2F" target="_blank">https://demo.ujcms.com</a><span> </span>使用手机访问或者浏览器手机模式访问前台，会自动呈现手机页面。</li> 
 <li>演示站后台：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.ujcms.com%2Fcp%2F" target="_blank">https://demo.ujcms.com/cp/</a><span> </span>演示用户登录后只拥有浏览后台功能，所有操作功能点击后都会显示无权访问（403）。如需进行操作测试，可以下载软件到本地安装。</li> 
 <li>QQ交流群：626599871</li> 
</ul> 
<h2 style="text-align:left">技术及功能亮点</h2> 
<p style="color:#24292e; text-align:left"><strong>自定义字段可查询</strong>：所有的自定义字段都可查询增强了系统的灵活性。</p> 
<p style="color:#24292e; text-align:left"><strong>自定义字段可视化设计</strong>：自定义字段使用拖拽式的可视化设计，所见即所得。</p> 
<p style="color:#24292e; text-align:left"><strong>URL地址SEO优化</strong>：栏目和文章的动态地址可以通过系统的全局设置功能进行修改。默认的栏目和文章URL地址前缀为<code>/channel</code>和<code>/article</code>，可以根据自己的需要修改，如改为<code>/categories</code>和<code>/archives</code>。多站点的情况下，子站点URL地址也由原来的<code>www.example.com/site-abc</code>的形式改为更友好的<code>www.example.com/abc</code>的形式。</p> 
<p style="color:#24292e; text-align:left"><strong>清理垃圾附件</strong>：系统使用时，可能会多传、误传图片等附件；在删除文章后，文章中的图片还保留在系统中，产生大量的未使用的垃圾图片和附件。系统中的附件管理可以查看所有未使用的图片和附件，并可对其进行删除。</p> 
<p style="color:#24292e; text-align:left"><strong>附件、模板、索引文件独立部署</strong>：系统运行时产生的文件可以和程序分开，部署到独立的目录，方便系统备份、升级和管理。比如上传的图片和附件、前台的模板、索引文件，都可以部署到程序以外的目录。</p> 
<p style="color:#24292e; text-align:left"><strong>模板文件和CSS、JS在同一目录</strong>：模板文件和CSS、JS分开的目录结构，会给模板制作和部署带来很大的不便性。而将模板文件和CSS、JS放在一起的设计，会方便很多。</p> 
<p style="color:#24292e; text-align:left"><strong>MyBatis参数化查询</strong>：后台数据通常会需要通过不同字段进行搜索，对每个表都写大量的查询，无疑是一项繁重的工作。MyBatis参数化查询功能通过前台传递查询参数，即可实现任意字段及关联表的查询功能（如：Q_title=abc，Q_user-username=test），无需后台编写代码，大幅减少后端的开发工作量。</p> 
<p style="color:#24292e; text-align:left"><strong>主副表拆分</strong>：对查询量大的复杂表进行主副表拆分，把常用的查询字段放到主表，不常用的字段放到副表，提升大数据量下的性能表现。</p> 
<h2 style="text-align:left">后端技术</h2> 
<ul> 
 <li>SpringBoot：提供了对Spring开箱即用的功能。简化了Spring配置，提供自动配置auto-configuration功能。</li> 
 <li>SpringMVC：MVC框架，使用方便，Bug较少。</li> 
 <li>Mybatis：持久化框架。</li> 
 <li>FreeMarker：网站模板组件。</li> 
 <li>Shiro：安全组件。配置简便。</li> 
 <li>Lucene：全文检索组件。</li> 
</ul> 
<h2 style="text-align:left">前端技术</h2> 
<ul> 
 <li>TypeScript: JavaScript的一个超集。</li> 
 <li>Vue 3：JavaScript框架。</li> 
 <li>ElementPlus：Vue 3 UI 框架。</li> 
 <li>TailwindCSS: 功能类优先的 CSS 框架。</li> 
 <li>Tinymce: 富文本编辑器。</li> 
</ul> 
<h2 style="text-align:left">功能列表</h2> 
<ul> 
 <li>内容 
  <ul> 
   <li>文章管理</li> 
   <li>栏目管理</li> 
   <li>区块管理</li> 
   <li>附件管理</li> 
   <li>生成管理</li> 
  </ul> </li> 
 <li>配置 
  <ul> 
   <li>全局设置</li> 
   <li>站点设置</li> 
   <li>模型管理</li> 
   <li>区块设置</li> 
   <li>字典类型</li> 
   <li>字典数据</li> 
  </ul> </li> 
 <li>用户 
  <ul> 
   <li>用户管理</li> 
   <li>角色管理</li> 
   <li>用户组管理</li> 
   <li>组织管理</li> 
  </ul> </li> 
 <li>系统 
  <ul> 
   <li>站点管理</li> 
   <li>储存点管理</li> 
  </ul> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">前台模板</h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><img alt height="1934" src="https://oscimg.oschina.net/oscnet/up-80a0ebd93df8b45fee97e5ee120780e5c78.jpg" width="1351" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">后台界面</h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><img alt height="713" src="https://oscimg.oschina.net/oscnet/up-cfe14e42ecbeb17974c201494ee2c931758.jpg" width="1367" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            