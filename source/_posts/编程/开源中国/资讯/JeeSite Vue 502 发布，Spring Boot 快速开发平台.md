
---
title: 'JeeSite Vue 5.0.2 发布，Spring Boot 快速开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8393'
author: 开源中国
comments: false
date: Fri, 01 Apr 2022 00:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8393'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0; margin-right:0; text-align:start"><span>升级内容</span></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 Vue BPM 模块，流程按钮组件、流程图、流程代码生成</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 oaLeave 请假流程，对应 BPM 模块的入门演示实例</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 支持动态弹窗和抽屉，传输数据方法 setModalData setDrawerData</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 editComponentProps 支持函数类型，方便传参返回自定义属性 Oliver</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 VirtualScroll 虚拟列表增加 scrollToBottom 属性，可以一直滚动到最底部 Oliver</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 CollapseContainer 折叠时，一起折叠边框，并支持 expand 双向绑定 Oliver</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 TreeSelect 增加 isDisable 属性，自定义<span style="background-color:rgba(9, 187, 7, 0.31)">禁</span>用项 Oliver</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 Select 增加 each 属性，每次鼠标点击都重新拉取数据 Oliver</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 用户 Excel 导入功能，Model 弹窗示例</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 EditableCell 编辑表格，也可以使用 format 参数 Oliver</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 RadioGroup 等组件，增加 Object 类型</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 弹窗组件 centered 默认居中显示</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 表单里的日期选择框样式宽度顶格</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 去掉 firefox 下的 drawer 多余的滚动条</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 有些浏览器不支持一个:not设置多个选择器问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 所有 api 接口和 views 界面，强化类型，利于调试提醒</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 菜单管理，如果包含 <code>://</code> 则默认是 <code>IFRAME</code> 组件</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 表单 Schema 默认值，当使用 validate 情况下没有生效问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 axios get 中文转义改进 #I4WFLV</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">请与 <code>jeesite-vue</code> 代码仓库源码进行同步，合并代码。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">前后端版本号暂不同，匹配后端版本为 <code>JeeSite v5.0.1</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">该版本无用户数限制，无在线人数限制</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">后端升级内容</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">升级 Spring Boot 2.5.11</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">同步 V4.4.0 带来的所有新特性和优化改进</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 Global.getPropertyToLong 方法，快速应对 Long 的属性</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 vue 和 beetl 两种前端的菜单分类 BEETL、IFRAME、LAYOUT</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 fixTreeData(list, parentCode, ... 方法，方便指定数据修正树结构</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 session.sessionIdAttributeName 属性，多一种传 sid 的方式</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 单点简单登录接口 token 支持设置时效性，1天：yyyyMMdd、1小时：yyyyMMddHH、1分钟：yyyyMMddHHmm</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 动态数据源配置接口，提供更好的动态数据源操作方法。</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 IdWorker 工具的 -DworkerId -DdatacenterId 参数</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BPM 管控系统，方便超管进行任务签收分配和查看</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BPM 弹窗模式下流程分类，设置弹窗大小，界面改进</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BPM 流程跟踪，根据情况查询历史表还是运行时表，提高性能</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 Layer 弹窗标题优化，个别浏览器分辨率下，消除滚动条</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 消息列表，原来发送者根据编码查找，改为根据名称查找</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 缓存管理，不存储当前用户信息，防止获取缓存数据带上一个用户信息</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 多线程，Redis 消息监听线程池、用户缓存清理线程池、消息推送线程池，避免高并发情况下太多的线程问题。</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 取消 WebUploader 上传超时参数 #I4WP8B</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 租户模式，支持<span style="background-color:rgba(9, 187, 7, 0.31)">显</span><span style="background-color:rgba(9, 187, 7, 0.31)">示</span>游客在线用户查询</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 启用多数据源条件，支持动态添加数据源的情况，自由启用数据源路由。</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 BPM getTaskByBusinessKey 设置 userCode 无效问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 form:extend 设置标签名不生效问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">关于 Spring 0day 不确定是否属实，我们已对 JeeSite 所有版本都增加了class 参数过滤。</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">后端升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">修改 <code>pom.xml</code> 文件中的 <code>jeesite-parent</code> 版本号为 <code>5.0.1-SNAPSHOT</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-common</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-module-core</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你是跨版本升级，请注意每一个版本的升级方法，业务上有调整的地方进行修改</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">执行 <code>root/package.bat(sh)</code> 打包脚本，强制更新依赖即可。</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">了解更多</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 官网地址：http://jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 在线文档：http://docs.jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 演示地址：http://vue.jeesite.com</p> </li> 
</ul>
                                        </div>
                                      
</div>
            