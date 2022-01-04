
---
title: 'Diboot 2.4.0 发布，多表关联无 SQL 更进一步的性能优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1879'
author: 开源中国
comments: false
date: Tue, 04 Jan 2022 16:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1879'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#404040; text-align:start">老铁们应该知道diboot的logo是个小松鼠，寓意“轻量、灵活、聪明”。<br> diboot如今已经满两岁了，做好一个产品就像孕育一个孩子，随着v2.4版本的发布，这个孩子将越发茁壮。</p> 
<h2 style="text-align:start">v2.4.0 版本带来了如下主要特性：</h2> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>内核 diboot-core & core-starter</li> 
 <li>关联绑定采用异步并发执行，进一步提升查询性能</li> 
 <li>@BindQuery注解支持添加多个组合为OR查询</li> 
 <li>@BindDict注解支持逗号拆分匹配</li> 
 <li>KeyValue替换为LabelValue避免使用时混淆</li> 
 <li>AttachMore支持远程过滤、及附加查询条件、支持跨表树形(异步)构建</li> 
 <li>V、S、D等系列工具类的优化 （thanks @emptypoint）</li> 
 <li>升级依赖版本：spring boot 2.6.2</li> 
</ul> 
<h2 style="text-align:start">文件组件 diboot-file-starter</h2> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>Excel支持大数据量的分页导入分批写入</li> 
 <li>Excel上传的过程优化，包括支持类型推断、上传合法数据、下载错误数据、错误记录标注、异常提示等</li> 
 <li>升级依赖版本：easyexcel 3.0.5</li> 
</ul> 
<h2 style="text-align:start">IAM组件 diboot-IAM-starter</h2> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>组织相关列表页查询支持名称的模糊查询</li> 
 <li>Operation改为OperationCons，避免与swagger3注解冲突 等</li> 
</ul> 
<h2 style="text-align:start">消息通知组件 diboot-message-starter</h2> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>发送消息支持通过模板code查询模板</li> 
</ul> 
<h2 style="text-align:start">定时任务组件 diboot-scheduler-starter</h2> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>优化定时任务初始化逻辑 等</li> 
</ul> 
<h2 style="text-align:start">移动端 diboot-mobile-starter & diboot-mobile-ui</h2> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>支持用户名密码、微信公众号、小程序 登录的对接实现</li> 
 <li>增加CRUD示例页面</li> 
 <li>增加个人中心页面</li> 
 <li>增加IamUser绑定微信登陆</li> 
 <li>增加上传组件、选择器、checkbox、地区选择器、时间选择器、卡片、描述等组件</li> 
 <li>系列页面及组件的多端适配调整优化</li> 
 <li>升级uviewui至1.8.5、适配HBuilder新版本</li> 
</ul> 
<h2 style="text-align:start">PC前端 diboot-antd-admin & diboot-element-admin</h2> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>新增上传文件管理功能</li> 
 <li>调整attachMore相关的命名调用等</li> 
 <li>下拉选项支持远程搜索、支持联动、支持跨表树形(异步)构建</li> 
 <li>excel导入导出优化，错误提示优化，支持导出错误数据等</li> 
 <li>优化消息模板管理功能</li> 
 <li>优化行编辑组件支持树</li> 
</ul> 
<h2 style="text-align:start">🎉 开发工具 diboot-devtools</h2> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>新增移动端页面生成（基于 diboot-mobile-ui）</li> 
 <li>面板组件支持常规统计图表的生成</li> 
 <li>数据表管理新增“参考库建表”，支持常用的省市区建表及数据导入</li> 
 <li>数据表管理新增“批量添加字段”功能</li> 
 <li>swagger接口文档支持切换为Springdoc（替代Springfox）</li> 
 <li>快照实现优化（移除开关、自动保存）（thanks @梦想家）</li> 
 <li>PC端CRUD页面生成支持配置生成远程搜索及多选搜索</li> 
 <li>前端生成相关的性能优化、组件分组与命名优化</li> 
 <li>配置n-n关联时支持自定义中间表表名</li> 
 <li>子表单支持多行表单</li> 
 <li>详情页附加信息支持表格与时间轴的切换</li> 
 <li>支持JDK17</li> 
</ul> 
<h2 style="text-align:start">🎉diboot-cloud (微服务版) v2.4.0</h2> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>关联绑定支持跨服务绑定（分属于不同服务里的对象间可互相绑定）</li> 
 <li>优化KeyValue 替换为 LabelValue以避免使用时混淆</li> 
 <li>Excel上传的过程优化，包括支持类型推断、上传合法数据、下载错误数据、错误记录标注、异常提示等</li> 
 <li>移除actuator依赖提升安全性</li> 
 <li>升级diboot基础组件及 admin-ui 至 2.4.0</li> 
 <li>升级依赖版本: spring-cloud 2021.0.0，spring-boot 2.6.2</li> 
</ul> 
<h2 style="text-align:start">🎉diboot-workflow（工作流版）v2.4.0</h2> 
<ul style="margin-left:20px; margin-right:0"> 
 <li>流程图查看优化，基于bpmn.js渲染流程图替代flowable的图片流程图</li> 
 <li>超大表格布局下的表单设计功能性能优化</li> 
 <li>动态表单导入外部表后，允许更改表单名称与字段标签名</li> 
 <li>升级diboot基础组件及 admin-ui 至 2.4.0</li> 
 <li>升级依赖版本: flowable 6.7.1</li> 
</ul>
                                        </div>
                                      
</div>
            