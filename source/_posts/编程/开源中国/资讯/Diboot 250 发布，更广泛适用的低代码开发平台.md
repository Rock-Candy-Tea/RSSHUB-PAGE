
---
title: 'Diboot 2.5.0 发布，更广泛适用的低代码开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3495'
author: 开源中国
comments: false
date: Wed, 06 Apr 2022 10:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3495'
---

<div>   
<div class="content">
                                                                                            <p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">    Diboot 2.5.0 版本已于近期发布，该版本我们主要聚焦于：基础框架和工具持续打磨升级；cloud版本近乎重构后，全面支持SSO及多租户；workflow工作流补齐短板站上新台阶，表单流程功能进一步增强，可适用于更加广泛的场景；官网文档内容全面改版，减少上手门槛。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span>diboot v2.5.0 版本的主要更新如下：</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong>core 内核 :</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">attachMore接口优化，支持别名及安全检查</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">重构数据范围权限的实现以适配更多场景，增加缓存以避免重复解析</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>IAM 组件：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">新增系统配置功能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增支持通过OAuth2单点登录</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">用户体系相关表主键更改为雪花id，便于数据同步场景处理</p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><strong>mobile-ui</strong><span> </span>移动端前端：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">优化了：移动端页面布局、首页展示等</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>PC端前端（antd-admin & <strong>element-admin</strong>）：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">新增支持多tab打开页面，页面布局紧凑化，让页面显示更多内容</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增系统配置功能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">预置支持OAuth2 SSO单点登录登出的默认实现</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span style="color:#7b0c00"><strong>diboot-devtools</strong><span> </span><strong>开发工具 ：</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">新用户自动开通高级功能<strong>7天免费体验</strong><span> </span>(废除引荐码)</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">后端字段支持配置可选“乐观锁”生成@version注解</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">搜索区的关联字段可切换“下拉”/“左树”展示形式，可<strong>直接生成左树右列表</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增outputPathBase配置项，支持将组件的基础代码生成到指定路径下</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">devtools 前端CRUD生成页面 默认加载最新的快照，并支持重置&暂存</p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#7b0c00">diboot-cloud 微服务版（企业版）</span></strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">auth-center 统一认证中心 与 user-center 用户中心 从原auth-server模块剥离，便于后期维护</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持<strong>SSO单点登录</strong>&统一退出（用于企业门户）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持<strong>Portal</strong>首页门户，支持client客户端应用接入管理（用于企业门户）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持<strong>多租户</strong>与其权限体系配置功能（用于SaaS系统）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">集成<strong>Skywalking</strong>，支持微服务性能监控、链路追踪、日志收集</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增用户体系相关<strong>数据同步接口</strong>，用于子系统同步用户相关数据</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增@InnerApi注解，用于服务间后端调用接口</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增初始数据可执行脚本，一键初始化全部基础数据</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化模块拆分与命名，服务模块下的各环境配置文件统一</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">升级diboot前后端及Spring各依赖版本至最新</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span style="color:#7b0c00"><strong>diboot-workflow 工作流版（企业版）</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><strong>表单设计器：</strong></p> 
  <ul style="list-style-type:square; margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:0; margin-right:0">新增支持公式计算（数字计算、日期计算等）</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">新增自动编号组件</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">新增级联选择器组件</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">表单输入框等支持从接口中设置默认值数据</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">表单字段支持显隐受控</p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>表单数据引擎：</strong>支持动态CRUD管理功能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>流程设计器：</strong></p> 
  <ul style="list-style-type:square; margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:0; margin-right:0">支持服务任务</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">支持子流程</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">支持信号事件配置</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">支持定时器事件配置</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">多实例支持配置候选组</p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>流程：</strong></p> 
  <ul style="list-style-type:square; margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:0; margin-right:0">新增流程发起暂存功能</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">新增任务执行时指定下一节点执行人</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">优化任务处理界面UI&UE，增大操作空间，布局紧凑</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">优化流程设计器、表单设计器页面UI&UE，增大设计区空间</p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">升级diboot前后端及Spring各依赖版本至最新</p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            