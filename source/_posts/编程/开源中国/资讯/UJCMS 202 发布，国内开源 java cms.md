
---
title: 'UJCMS 2.0.2 发布，国内开源 java cms'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-80a0ebd93df8b45fee97e5ee120780e5c78.jpg'
author: 开源中国
comments: false
date: Wed, 23 Mar 2022 10:32:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-80a0ebd93df8b45fee97e5ee120780e5c78.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">应用户要求，将许可协议从 `AGPL-3` 改为 `GPL-2`，并开放组织管理功能。同时修复已发现的BUG，升级组件。</p> 
<h2 style="text-align:left">升级日志（2.0.1, 2.0.2）</h2> 
<ul> 
 <li>许可协议由 AGPL-3 改为 GPL-2</li> 
 <li>开放组织管理功能</li> 
 <li>增加全局设置中栏目URL和文章URL自定义地址的合法校验</li> 
 <li>增加站点设置中域名的合法校验</li> 
 <li>修复：前台搜索报错（ChannelInnerBase不能转换为Anchor）</li> 
 <li>修复：文章管理中没有编辑器的页面无法提交</li> 
 <li>升级owasp-java-html-sanitizer组件版本至20211018.2</li> 
 <li>升级guava组件版本至30.1-jre</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">简介</h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">UJCMS是在Jspxcms多年的开发经验上，重新设计开发的Java开源内容管理系统(java cms)。使用SpringBoot、MyBatis、Shiro、Lucene、FreeMarker、TypeScript、Vite2、Vue3、ElementPlus2、等技术。针对原系统中的一些痛点问题，进行解决、优化和改进，并使用<code>GPL-2</code>开源协议发布，可免费商用。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">技术上选择主流、先进、简单的架构，方便用户进行二次开发。持久化层用MyBatis替换了Hibernate；视图层用前后端分离的Vue3替换了JSP；数据库也进行了重新设计。设计上强调“简单”、“灵活”，避免繁杂的设计和实现，降低系统维护成本和二次开发难度。功能使用上也要求“简单”，避免复杂的使用逻辑。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>官网地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ujcms.com%2F" target="_blank">https://www.ujcms.com</a></li> 
 <li>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ujcms.com%2Fdownload%2F" target="_blank">https://www.ujcms.com/download/</a><span> </span>提供安装包下载。</li> 
 <li>演示站前台：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.ujcms.com%2F" target="_blank">https://demo.ujcms.com</a><span> </span>使用手机访问或者浏览器手机模式访问前台，会自动呈现手机页面。</li> 
 <li>演示站后台：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.ujcms.com%2Fcp%2F" target="_blank">https://demo.ujcms.com/cp/</a><span> </span>演示用户登录后只拥有浏览后台功能，所有操作功能点击后都会显示无权访问（403）。如需进行操作测试，可以下载软件到本地安装。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">技术及功能亮点</h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><strong>自定义字段可查询</strong>：所有的自定义字段都可查询增强了系统的灵活性。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><strong>自定义字段可视化设计</strong>：自定义字段使用拖拽式的可视化设计，所见即所得。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><strong>URL地址SEO优化</strong>：栏目和文章的动态地址可以通过系统的全局设置功能进行修改。默认的栏目和文章URL地址前缀为<code>/channel</code>和<code>/article</code>，可以根据自己的需要修改，如改为<code>/categories</code>和<code>/archives</code>。多站点的情况下，子站点URL地址也由原来的<code>www.example.com/site-abc</code>的形式改为更友好的<code>www.example.com/abc</code>的形式。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><strong>清理垃圾附件</strong>：系统使用时，可能会多传、误传图片等附件；在删除文章后，文章中的图片还保留在系统中，产生大量的未使用的垃圾图片和附件。系统中的附件管理可以查看所有未使用的图片和附件，并可对其进行删除。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><strong>附件、模板、索引文件独立部署</strong>：系统运行时产生的文件可以和程序分开，部署到独立的目录，方便系统备份、升级和管理。比如上传的图片和附件、前台的模板、索引文件，都可以部署到程序以外的目录。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><strong>模板文件和CSS、JS在同一目录</strong>：模板文件和CSS、JS分开的目录结构，会给模板制作和部署带来很大的不便性。而将模板文件和CSS、JS放在一起的设计，会方便很多。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><strong>MyBatis参数化查询</strong>：后台数据通常会需要通过不同字段进行搜索，对每个表都写大量的查询，无疑是一项繁重的工作。MyBatis参数化查询功能通过前台传递查询参数，即可实现任意字段及关联表的查询功能（如：Q_title=abc，Q_user-username=test），无需后台编写代码，大幅减少后端的开发工作量。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><strong>主副表拆分</strong>：对查询量大的复杂表进行主副表拆分，把常用的查询字段放到主表，不常用的字段放到副表，提升大数据量下的性能表现。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">后端技术</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>SpringBoot：提供了对Spring开箱即用的功能。简化了Spring配置，提供自动配置auto-configuration功能。</li> 
 <li>SpringMVC：MVC框架，使用方便，Bug较少。</li> 
 <li>Mybatis：持久化框架。</li> 
 <li>FreeMarker：网站模板组件。</li> 
 <li>Shiro：安全组件。配置简便。</li> 
 <li>Lucene：全文检索组件。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">前端技术</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Vue 3：JavaScript框架。</li> 
 <li>ElementPlus 2：Vue 3 UI 框架。</li> 
 <li>Vite 2：下一代前端开发与构建工具。</li> 
 <li>TypeScript: JavaScript的一个超集。</li> 
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
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><img alt height="1934" src="https://oscimg.oschina.net/oscnet/up-80a0ebd93df8b45fee97e5ee120780e5c78.jpg" width="1351" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">后台界面</h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><img alt height="713" src="https://oscimg.oschina.net/oscnet/up-cfe14e42ecbeb17974c201494ee2c931758.jpg" width="1367" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            