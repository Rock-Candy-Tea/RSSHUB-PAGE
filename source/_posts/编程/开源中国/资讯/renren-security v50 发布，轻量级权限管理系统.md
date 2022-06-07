
---
title: 'renren-security v5.0 发布，轻量级权限管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5762c252683f5ced1b036121867ce3178db.png'
author: 开源中国
comments: false
date: Tue, 07 Jun 2022 15:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5762c252683f5ced1b036121867ce3178db.png'
---

<div>   
<div class="content">
                                                                                            <p>renren-security v5.0 发布，轻量级权限管理系统</p> 
<p>renren-security是一套轻量级的权限系统，采用前后端分离架构，主要包括用户管理、角色管理、部门管理、菜单管理、定时任务、参数管理、字典管理、文件上传、系统日志、API模块等功能。其中，还拥有多数据源、数据权限、Redis缓存动态开启与关闭、统一异常处理等技术特点。现已全面支持MySQL、Oracle、SQL Server、PostgreSQL数据库。</p> 
<div>
 <strong>更新日志：</strong> 
 <p><span style="background-color:#ffffff; color:#40485b">• 完全重构renren-security，改成前后端分离架构，更符合企业需求</span><br> <span style="background-color:#ffffff; color:#40485b">• 友好的代码结构及注释，便于阅读及二次开发</span><br> <span style="background-color:#ffffff; color:#40485b">• 满足《阿里巴巴Java开发手册》规范要求，可作为企业代码规范</span><br> <span style="background-color:#ffffff; color:#40485b">• 实现前后端分离，通过token进行数据交互，前端再也不用关注后端技术</span><br> <span style="background-color:#ffffff; color:#40485b">• 灵活的权限控制，可控制到页面或按钮，满足绝大部分的权限需求</span><br> <span style="background-color:#ffffff; color:#40485b">• 提供CrudService接口，对增删改查进行封装，代码更简洁</span><br> <span style="background-color:#ffffff; color:#40485b">• 页面交互使用Vue2.x，极大的提高了开发效率</span><br> <span style="background-color:#ffffff; color:#40485b">• 完善的部门管理及数据权限，通过注解实现数据权限的控制</span><br> <span style="background-color:#ffffff; color:#40485b">• 完善的XSS防范及脚本过滤，彻底杜绝XSS攻击</span><br> <span style="background-color:#ffffff; color:#40485b">• 完善的代码生成机制，可在线生成entity、xml、dao、service、vue、sql代码，减少70%以上的开发任务</span><br> <span style="background-color:#ffffff; color:#40485b">• 支持集群部署，session存储在redis中</span><br> <span style="background-color:#ffffff; color:#40485b">• 引入quartz定时任务，可动态完成任务的添加、修改、删除、暂停、恢复及日志查看等功能</span><br> <span style="background-color:#ffffff; color:#40485b">• 引入Hibernate Validator校验框架，轻松实现后端校验</span><br> <span style="background-color:#ffffff; color:#40485b">• 引入云存储服务，已支持：七牛云、阿里云、腾讯云等</span><br> <span style="background-color:#ffffff; color:#40485b">• 引入swagger文档支持，方便编写API接口文档</span></p> 
 <p> </p> 
</div> 
<p>官方社区：https://www.renren.io/community</p> 
<p>前端UI：<a href="https://gitee.com/renrenio/renren-ui">https://gitee.com/renrenio/renren-ui</a></p> 
<p>开发文档：http://www.renren.io/guide</p> 
<p>演示地址：http://demo.open.renren.io/renren-security  (账号：admin  密码：admin)</p> 
<p>    <img alt height="1789" src="https://oscimg.oschina.net/oscnet/up-5762c252683f5ced1b036121867ce3178db.png" width="3404" referrerpolicy="no-referrer"> </p> 
<p><img alt height="1855" src="https://oscimg.oschina.net/oscnet/up-4c94599f43ac6a73757a667320e8b4e6cc9.png" width="2898" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            