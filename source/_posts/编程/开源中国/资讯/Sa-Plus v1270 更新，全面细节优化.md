
---
title: 'Sa-Plus v1.27.0 更新，全面细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-plus/pre-2.png'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 10:56:00 GMT
thumbnail: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-plus/pre-2.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Sa-Plus 是一个基于 SpringBoot 架构的快速开发框架，内置代码生成器。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>框架集成 JavaWeb 开发常见功能：文件上传、角色授权、全局异常处理、redis 控制台、API 日志统计、全局配置、跨域处理等等，让你不再为项目的基础设施劳神费心！</li> 
 <li>内置代码生成器，高自动化代码生成：普通 input、多行文本域、富文本、枚举按钮、日期控件、图片上传、音频上传、视频上传、 多图上传、树形表格、聚合外键......</li> 
 <li>你只需写上简单的表注释，即可直接生成：Java 代码、后台管理页面、接口文档等，使项目中80%的代码做到自动化，省时省力</li> 
 <li>代码清晰明了，方便二次修改，另可自定义代码生成模板，根据自己的代码风格灵活扩展</li> 
</ul> 
<h4><strong>更新日志</strong></h4> 
<p>本次更新版本 v1.27.0 新增Vue单页版UI皮肤，基于 vue-element-admin 魔改：</p> 
<ul> 
 <li>升级：Sa-Token 升级至 v1.29.0 版本</li> 
 <li>优化：优化全局 el-alert 样式</li> 
 <li>优化：AjaxJson在未添加分页条件时，将不返回dataCount字段</li> 
 <li>修复：AjaxJson getData 的返回值改为Object</li> 
 <li>修复：Redis 序列化格式改为 json 序列化形式</li> 
 <li>修复：修复全局API日志的时间格式与真实请求不一致的问题</li> 
 <li>修复：启动时的 Network 打印加上try-catch，解决某些情况下的获取失败</li> 
 <li>修复：新增404接口处理，返回json格式化消息</li> 
 <li>优化：优化API全局日志算法，使404也能记录API全局日志</li> 
 <li>优化：将默认角色更名为开发者权限和系统管理员权限</li> 
 <li>新增：新增以演示模式启动的方式</li> 
 <li>新增：新增配置<span> </span><code>log-to-file</code><span> </span>和<span> </span><code>log-to-db</code><span> </span>决定是否输出API请求日志</li> 
 <li>修改：配置项 “是否抛出sql” 转移到 application.yml 中</li> 
 <li>优化：让API日志插入不打印sql，且改为异步插入提高请求响应速度</li> 
 <li>修改：列表查询时排序条件改为具体的字段名</li> 
 <li>优化：设定项目缓存默认为json序列化方式，方便在控制台的二次修改</li> 
 <li>优化：接口鉴权方式改为注解鉴权</li> 
 <li>优化：修改部分权限码，更符合语义</li> 
 <li>新增：全局配置随机头像功能</li> 
 <li>新增：新增账号模拟登陆功能</li> 
 <li>新增：新增后台管理相关接口文档</li> 
 <li>新增：管理员的登陆日志</li> 
 <li>新增：后台登录新增 [记住我] 功能</li> 
 <li>修复：修复部分代码生成的错误之处</li> 
 <li>升级：升级 sp-com 多模块版相关功能</li> 
 <li>升级：升级 vue 单页版相关功能</li> 
 <li>升级：登录接口集成限流控制</li> 
</ul> 
<p><strong>项目地址：<a href="https://gitee.com/click33/sa-plus">https://gitee.com/click33/sa-plus</a></strong></p> 
<h4><strong>截图预览</strong></h4> 
<p><img src="https://color-test.oss-cn-qingdao.aliyuncs.com/sa-plus/pre-2.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://color-test.oss-cn-qingdao.aliyuncs.com/sa-plus/pre-4.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://color-test.oss-cn-qingdao.aliyuncs.com/sa-plus/pre-7.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://color-test.oss-cn-qingdao.aliyuncs.com/sa-plus/pre-8.png" referrerpolicy="no-referrer"></p> 
<p>更多信息详见官网文档</p>
                                        </div>
                                      
</div>
            