
---
title: 'Diboot 2.3.1 发布，易上手的企业级低代码开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4987'
author: 开源中国
comments: false
date: Mon, 11 Oct 2021 06:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4987'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#404040; text-align:start">Diboot是为开发者所打造的一个低代码开发平台，一个数倍提效的赋能工具。</p> 
<p style="color:#404040; text-align:start">Diboot不但拥有从前端到后端的整个基础架构，帮你更快开展项目。而且还拥有开发过程中的前后端一系列已有组件，助你少造轮子。还具有一套自动化工具，在开发过程中，前后端方面都可以帮您提质增效。</p> 
<p style="color:#404040; text-align:start">Diboot将致力于有效提高软件的代码质量、开发效率、可维护性，同时也对其打造了自动化工具来完成系列重复工作和复杂工作。</p> 
<p style="color:#404040; text-align:start">Diboot将通过系列基础组件化繁为简，又通过高效工具以简驭繁。</p> 
<h3 style="text-align:start">更新重点</h3> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>core内核支持字段加密与脱敏，安全等保放心用</li> 
 <li>移动端发布: 后端基础组件diboot-mobile-starter 和 配套前端UI diboot-mobile-ui</li> 
 <li>scheduler定时任务组件支持开关日志、自定义名称等系列优化</li> 
 <li>devtools前端生成新增支持关联场景的集成方案，使面板组件易于集成</li> 
 <li>devtools前端代码生成后支持自动格式化</li> 
 <li>devtools前端列表生成支持可选editable可编辑表格</li> 
 <li>升级依赖版本：spring boot 2.5.5, mybatis-plus 3.4.3.4，shiro 1.8.0</li> 
 <li>微服务 diboot-cloud v2.3.1版本同步升级 (企业版用户可参考docs下的文档升级)</li> 
 <li>系列优化与改进，可见如下更新详情</li> 
</ul> 
<h4 style="text-align:start">diboot-core & diboot-core-starter</h4> 
<p style="color:#404040; text-align:start">🎉 新增：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>新增@ProtectField注解实现字段加密与脱敏，支持安全等保</li> 
 <li>BindEntityList新增支持多个ID拼接存储的值进行拆解绑定</li> 
 <li>BindFieldList新增支持orderBy排序</li> 
 <li>新增diboot.global.init-sql全局配置，关闭sql自动初始化检查</li> 
 <li>新增InvalidUsageException用于提示错误的调用</li> 
</ul> 
<p style="color:#404040; text-align:start">🍻 优化：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>优化请求参数的合法检查、异常信息过滤等安全防护</li> 
 <li>优化PagingJsonResult添加空构造方法，便于反序列化</li> 
 <li>优化BaseService的N-N更新接口实现</li> 
 <li>升级依赖版本：spring boot 2.5.5, mybatis-plus 3.4.3.4...</li> 
</ul> 
<p style="color:#404040; text-align:start">🐛 修复：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>Fix bug: 优化select字段逻辑特定情况下误转换有AS别名字段的问题</li> 
</ul> 
<h4 style="text-align:start">文件组件 diboot-file-starter v2.3.1</h4> 
<p style="color:#404040; text-align:start">🍻 优化：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>优化文件类型黑白名单及合法检查逻辑</li> 
</ul> 
<h4 style="text-align:start">IAM组件 diboot-IAM-starter v2.3.1</h4> 
<p style="color:#404040; text-align:start">🎉新增：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>新增IamSecurityUtils.getCurrentUserId()，直接返回用户id</li> 
</ul> 
<p style="color:#404040; text-align:start">🍻 优化：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>优化异步日志保存类，指定异步executor，避免多异步执行器场景下冲突</li> 
 <li>用户角色更新接口实现逻辑优化</li> 
 <li>升级依赖版本: shiro1.8.0</li> 
</ul> 
<p style="color:#404040; text-align:start">🐛 修复：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>Fix bug: 下载接口添加<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fgithub.com%252Flog" target="_blank">@log</a>日志注解报异常问题</li> 
</ul> 
<h4 style="text-align:start">消息通知组件 diboot-message-starter v2.3.1</h4> 
<p style="color:#404040; text-align:start">🍻 优化：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>邮件通道默认支持发送HTML格式邮件</li> 
 <li>优化异步日志保存类，指定executor，避免多异步执行器场景下冲突</li> 
 <li>优化message的模板id允许为空，支持不依赖模板的消息记录</li> 
 <li>定时任务组件 diboot-scheduler-starter v2.3.1</li> 
</ul> 
<p style="color:#404040; text-align:start">🍻 优化：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>新增createByName字段冗余，移除IAM依赖</li> 
 <li>定时任务对象新增saveLog是否记录日志开关</li> 
 <li>定时任务名称支持自定义及模糊查询</li> 
 <li>优化异步日志保存类，指定executor，避免多异步执行器场景下冲突</li> 
</ul> 
<h4 style="text-align:start">移动端组件 diboot-mobile-starter (新组件) v2.3.1</h4> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>支持H5账号密码登录、微信小程序登录与注册、微信公众号登录与注册</li> 
 <li>组件自动配置，iam-member移动端成员表自动初始化</li> 
 <li>提供配套 diboot-mobile-ui (uni-app版) 前端框架</li> 
</ul> 
<h4 style="text-align:start">移动端前端 diboot-mobile-ui (新项目) v2.3.1</h4> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>基于uni-app基础轻量封装</li> 
 <li>支持H5账号密码登录</li> 
 <li>支持微信小程序登录与自动注册</li> 
 <li>支持微信公众号登录与自动注册</li> 
</ul> 
<h4 style="text-align:start">PC前端 diboot-antd-admin v2.3.1</h4> 
<p style="color:#404040; text-align:start">🍻 优化：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>调整attachMore请求逻辑，兼容自定义attachMore和通用attachMore接口</li> 
 <li>新增自定义开区间查询</li> 
 <li>定时任务支持配置标题及日志开关</li> 
 <li>新增可编辑表格</li> 
 <li>调整文件上传大小为10M</li> 
 <li>引入图片预览组件</li> 
</ul> 
<p style="color:#404040; text-align:start">🐛 修复：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>Fix bug: 点击上传的文件项弹窗异常问题</li> 
 <li>PC前端 diboot-element-admin v2.3.1</li> 
</ul> 
<p style="color:#404040; text-align:start">🍻 优化：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>调整attachMore请求逻辑，兼容自定义attachMore和通用attachMore接口</li> 
 <li>新增自定义开区间查询</li> 
 <li>定时任务支持配置标题及日志开关</li> 
 <li>新增可编辑表格</li> 
 <li>调整文件上传大小为10M</li> 
</ul> 
<h4 style="text-align:start">工具 diboot-devtools v2.3.1</h4> 
<p style="color:#404040; text-align:start">🎉 新增：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>前端生成新增支持关联场景的集成方案，使面板组件易于集成</li> 
 <li>前端代码生成后自动格式化</li> 
 <li>前端列表生成支持可选editable可编辑表格</li> 
</ul> 
<p style="color:#404040; text-align:start">🍻 优化：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>支持PostgreSQL 12+版本</li> 
 <li>N-N关联配置支持自定义属性名</li> 
 <li>字段自动填充实现改为生成MP的MetaObjectHandler实现类</li> 
</ul> 
<p style="color:#404040; text-align:start">🐛 修复：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>fix：1-n的详情页设置保存快照后恢复回显异常问题</li> 
 <li>fix：后端代码删除后，之前的关联设置未能正确回显的问题</li> 
 <li>fix：非id,uuid主键的已有表生成后端代码报错的问题</li> 
</ul> 
<h4 style="text-align:start">微服务 diboot-cloud v2.3.1</h4> 
<p style="color:#404040; text-align:start">🎉 新增：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>用户列表新增excel上传下载功能</li> 
</ul> 
<p style="color:#404040; text-align:start">🍻 优化：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>配置简化优化，包路径优化，common基础组件改为starter，增加自动配置，业务模块无需再配置scan "com.diboot"</li> 
 <li>auth-server中的resource server配置移至yml中</li> 
 <li>scheduler定时任务新增saveLog是否记录日志开关，定时任务名称支持自定义及模糊查询</li> 
 <li>message模块邮件通道支持发送HTML格式邮件</li> 
 <li>依赖升级</li> 
</ul> 
<p style="color:#404040; text-align:start">🐛 修复：</p> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>fix：图片文件下载的弹窗预览异常问题</li> 
</ul>
                                        </div>
                                      
</div>
            