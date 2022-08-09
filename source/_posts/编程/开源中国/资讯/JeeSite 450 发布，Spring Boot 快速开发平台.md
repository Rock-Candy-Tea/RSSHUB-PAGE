
---
title: 'JeeSite 4.5.0 发布，Spring Boot 快速开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9776'
author: 开源中国
comments: false
date: Tue, 09 Aug 2022 08:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9776'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:start">升级内容</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">升级 spring boot 2.6.10、mybatis-spring 2.0.7、shiro 1.9.1、shardingsphere 5.1.1 等</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">微服务组件升级 spring cloud 2021.0.2、nacos 2.1.0、seata 1.5.0、sentinel 1.8.4 等</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 左树右表、导入导出代码生成、微服务启动脚本模板</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 支持OSS对象存储的文件预览（阿里、腾讯、七牛、MinIO）</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 @Table允许排序设置为空参数 mybatis.allowOrderEmpty 为空时，不自动添加主键排序条件。</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 form:treeselect 组件的 fastSearch快速查询参数，关闭后点击查询按钮再查询</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 DAO 批量更新语句方法，可动态 ExecutorType 指定</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 顶部菜单自动折叠到更多下拉菜单</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 BootStrap 版的<span data-darkreader-inline-bgcolor style="--darkreader-inline-bgcolor:#999700; background-color:#fffb00">黑暗主题</span>模式</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 Laydate 组件的多语言切换</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 DiffDataUtils 差异比较工具，新增 DiffOptions 差异比较选项，自定义包含和排除等设置</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 可以根据 window.toTopWindow 参数设定是否可以突破 iframe 到顶端的开关</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 ListUtils 本地分页代码，如果总共就1页，则直接返回</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 POM文件结构，对于新版IDE的一些提示优化</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 代码生成 数值类型最大数值的越界优化 #I5J7UR</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 新增smartToFit参数，当grid宽度小于窗口宽度时不让自适应</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 RoutingTransactionFactory 动态数据源，实时判断</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 点击全部已读后，更新右上角消息个数</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 去掉基类上的事务注解，方便业务定义</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 删除用户没有及时清除session问题pr!22</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 流程脚本选择，管理按钮增加 bpm:bpmScript:edit 权限控制</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 重载表格后，设置列排序显示隐藏对话框更新</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 业务流程 撤回任务时，下一个任务是会签的时候，提示流程已经结束的问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 用户管理 重命名ur是sql关键词，导致jsqlparser4.4不能解析</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 文件管理 解决文件柜管理修改后未刷新列表问题</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">修改 <code>pom.xml</code> 文件中的 <code>jeesite-parent</code> 版本号为 <code>4.4.1-SNAPSHOT</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-common</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-module-core</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你是跨版本升级，请注意每一个版本的升级方法，业务上有调整的地方进行修改</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">本次跨中版本升级了 Spring Boot 及 Spring Cloud 框架，建议做下完整测试</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">执行 <code>root/package.bat(sh)</code> 打包脚本，强制更新依赖。</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">了解更多</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 官网地址：http://jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 在线文档：http://docs.jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 演示地址：http://demo.jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite <span>Vue</span> 演示地址：http://vue.jeesite.com</p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            