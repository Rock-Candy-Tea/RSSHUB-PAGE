
---
title: 'zyplayer-doc 1.0.9 发布，现代化的、集中式的数据库管理工具，WIKI 文档工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6caa2a287a3d115d7bfa2f26ce771bfd74c.png'
author: 开源中国
comments: false
date: Sun, 25 Jul 2021 16:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6caa2a287a3d115d7bfa2f26ce771bfd74c.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">软件介绍</h2> 
<p style="text-align:start">zyplayer-doc是一款定位为公司内部和个人使用的在线工具，现有数据库文档、WIKI文档、swagger 文档、dubbo文档、ElasticSearch文档等，管理端具有人员管理、权限管理功能等功能。项目后端使用spring-boot、mybatis-plus等框架，前端使用Vue、element-ui、zui等框架。</p> 
<h2 style="text-align:start">数据库模块</h2> 
<p style="text-align:start">本次升级内容：<br> 1、增加hive和impala数据源支持，可查看表结构、执行SQL查询数据<br> 2、框架优化，数据查询和层级更合理<br> 3、数据查看优化，执行器支持复制为insert、update、json格式<br> 4、数据库表数据导出支持，支持导出为为insert、update、json格式，可使用单个文件导出或zip压缩文件导出<br> 5、增加表关系图（简版，找到更好的ER图组件再替换）<br> 6、将表字段、表结构、表关系图、表数据查看页面合并到一个页面，更加便于使用<br> 7、sqlserver数据库查询加强，数据查询、库表信息、数据导出等全功能支持<br> 8、优化SQL编辑器引入方式，优化自动提示，优化sqlserver表、字段注释获取和更新方式，数据查询时改为需指定数据库，便于库表检索提示<br> 9、SQL编辑器自动提示库、表、列逻辑优化，更加好用<br> 10、sql执行增加动态参数功能，SQL中可使用$&#123;xx&#125;或#&#123;xx&#125;动态参数<br> 11、数据预览列表头移上去展示列说明<br> 12、前端代码自动打包至各模块的文件夹内，不再需要拷贝打包后的文件<br> 13、优化关于页面和项目升级提示</p> 
<p style="text-align:start">这是一个令人兴奋的版本，在看到群友和项目的反馈及评论后，发现了项目的价值和不足之处，刺激着我对项目进行了大刀阔斧的修改，现已具有多库表在线管理、人员查询更新权限控制、库表信息查看、表字段查看、表和字段注释编辑、表关系图、表数据查询、表数据/表结构/建表语句导出、多数据源之间的数据互导、存储过程编辑、SQL执行查询等功能，数据库支持MySQL、SQLServer、Oracle、PostgreSQL、Hive、Impala，平常对数据库的操作已不成问题，由于在工作中一直使用的此工具在操作数据库，所以使用上面会更加人性化，了解开发人员痛点，明白大家的刚需。</p> 
<p style="text-align:start">下个版本将着重去做数据导入、在线更新数据、表设计和数据备份功能，争取做大做强，创造辉煌！</p> 
<p style="text-align:start">强烈建议大家试用一波，有使用上的建议都会满足大家，接待速度超快的喔~</p> 
<h2 style="text-align:start">wiki模块</h2> 
<p style="text-align:start">本次升级内容：<br> 1、wiki模块使用vant移动端框架支持手机端文档查看适配 #I2BC14<br> 2、wiki查看页面优化</p> 
<p style="text-align:start">本次对wiki模块优化较少，主要由于精力放在了数据库模块和大家发聩较少</p> 
<p style="text-align:start">项目开源地址：<a href="https://gitee.com/zyplayer/zyplayer-doc">https://gitee.com/zyplayer/zyplayer-doc</a><br> 在线体验地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.zyplayer.com" target="_blank">http://doc.zyplayer.com</a> 账号：zyplayer 密码：123456<br> 最新版打包文件下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpan.baidu.com%2Fs%2F1yMmnle01XR4TDjo2hfvw-Q" target="_blank">https://pan.baidu.com/s/1yMmnle01XR4TDjo2hfvw-Q</a> 提取码:3adf，选择最新版下载使用</p> 
<h2 style="text-align:start">数据查询页</h2> 
<p><img height="960" src="https://oscimg.oschina.net/oscnet/up-6caa2a287a3d115d7bfa2f26ce771bfd74c.png" width="1917" referrerpolicy="no-referrer"></p> 
<h2>表数据查看和筛选</h2> 
<p><img height="962" src="https://oscimg.oschina.net/oscnet/up-4e8ffe0377eee35aeba2d2dce8fc5d2cbae.png" width="1920" referrerpolicy="no-referrer"></p> 
<h2>库表导出</h2> 
<p><img height="958" src="https://oscimg.oschina.net/oscnet/up-90f3de411b33f2a97f34642ddc23499c72d.png" width="1920" referrerpolicy="no-referrer"></p> 
<h2>wiki查看页</h2> 
<p><img height="950" src="https://oscimg.oschina.net/oscnet/up-a758a769a0f524622e97b3bddf6b5469bd3.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            