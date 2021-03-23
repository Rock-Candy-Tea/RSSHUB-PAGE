
---
title: '学 .NET 5 从 Furion 开始，v1.16.0 发布'
categories: 
 - 编程
 - 开源中国
 - — 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Tue, 23 Mar 2021 16:38:00 GMT
thumbnail: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:center"><img height="80" src="https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png" width="127" referrerpolicy="no-referrer"></p> 
<div> 
 <p style="text-align:center"><a href="https://gitee.com/dotnetchina/Furion/stargazers"><img alt="star" src="https://gitee.com/dotnetchina/Furion/badge/star.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/members"><img alt="fork" src="https://gitee.com/dotnetchina/Furion/badge/fork.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fstargazers" target="_blank"><img alt="GitHub stars" src="https://img.shields.io/github/stars/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fnetwork" target="_blank"><img alt="GitHub forks" src="https://img.shields.io/github/forks/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/badge/license-Apache2-yellow" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></p> 
</div> 
<div> 
 <p style="text-align:center">让 .NET 开发更简单，更通用，更流行。</p> 
</div> 
<h2>dotNET China 组织</h2> 
<p>Furion 目前已捐赠给 <a href="https://gitee.com/dotnetchina">dotNET China</a> 组织进行维护。</p> 
<p>dotNET China 组织地址：<a href="https://gitee.com/dotnetchina">https://gitee.com/dotnetchina</a></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-dd4d1e6f2b96961e5aa8ffa59db8dfe0913.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-0aa9cd2acc2fe3932a3fd154614971765f3.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-98d58c84aabac9b29bb3437fd886ffb75d4.png" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] <code>IDGenerator</code> 雪花 ID 算法，感谢 <a href="https://gitee.com/yitter/idgenerator">idgenerator</a> 作者提交 PR <a href="https://gitee.com/dotnetchina/Furion/pulls/204">#PR204</a> <a href="https://gitee.com/dotnetchina/Furion/issues/I3B60S">#I3B60S</a></li> 
    <li>[新增] <code>DbContext</code> 刷新多租户缓存拓展方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I39N5U">#I39N5U</a></li> 
    <li>[新增] 自定义配置单个控制器名称规范，如小写路由 <a href="https://gitee.com/dotnetchina/Furion/issues/I3A5XL">#I3A5XL</a></li> 
    <li>[新增] 获取当前选择区域语言方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I3BSDH">#I3BSDH</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[升级] .NET 5 SDK 至 5.0.4 版本 <a href="https://gitee.com/dotnetchina/Furion/issues/I3ASTL">#I3ASTL</a></li> 
    <li>[重构] 远程请求所有功能 <a href="https://gitee.com/dotnetchina/Furion/issues/I2LB7M">#I2LB7M</a></li> 
    <li>[重构] <code>JSON</code> 序列化功能，提供统一的抽象接口，方便自由替换 <code>JSON</code> 库 <a href="https://gitee.com/dotnetchina/Furion/issues/I39GT9">#I39GT9</a></li> 
    <li>[重构] 验证失败返回消息模型及规范化接口验证参数 <a href="https://gitee.com/dotnetchina/Furion/issues/I3AFQW">#I3AFQW</a></li> 
    <li>[优化] 插件式开发热插拔功能，实现动态加载卸载 <a href="https://gitee.com/dotnetchina/Furion/pulls/200">#PR200</a>, 感谢 <a href="https://gitee.com/samwangcoder">@SamWangCoder</a></li> 
    <li>[移除] 移除 <code>JsonSerializerUtility</code> 静态类及移除属性大写序列化拓展配置 <a href="https://gitee.com/dotnetchina/Furion/issues/I3AFRJ">#I3AFRJ</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] <code>MVC</code> 模式下不支持验证自定义验证逻辑 <a href="https://gitee.com/dotnetchina/Furion/issues/I39LM5">#I39LM5</a></li> 
    <li>[修复] 验证数值类型正则表达式不支持负数 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I39YUV">#I39YUV</a></li> 
    <li>[修复] 框架启动时无法加载未被引用的程序集 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3A3Z4">#I3A3Z4</a></li> 
    <li>[修复] <code>EFCoreRepository.IsAttached()</code> 方法判断错误 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3A824">#I3A824</a></li> 
    <li>[修复] <code>动态API</code> 驼峰显示配置无效 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3AF32">#I3AF32</a></li> 
    <li>[修复] <code>cli.ps1</code> 不支持新版本 <code>EFCore</code> bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3APO9">#I3APO9</a></li> 
    <li>[修复] <code>EFCore</code> 实体配置 <code>[Table]</code> 特性无效 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3BAYH">#I3BAYH</a></li> 
    <li>[修复] 动态 WebAPI <code>CheckIsSplitCamelCase</code> bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3BLKX">#I3BLKX</a></li> 
    <li>[修复] 修复动态 WebAPI 配置保留 Action 的 Async 后缀无效问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3C3DA">#I3C3DA</a></li> 
    <li>[修复] <code>JWT</code> Token 刷新后旧的刷新 Token 依旧可用 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3C8ZH">#I3C8ZH</a></li> 
    <li>[修复] 多语言 <code>Razor</code> 视图变量多语言乱码问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3CBMU">#I3CBMU</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[优化] 默认序列化提供器 <code>System.Text.Json</code> 反序列化字符串时区分大小写问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3BSXV">#I3BSXV</a></li> 
    <li>[优化] 优化 <code>MessageCenter</code> 性能问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I39PRR">#I39PRR</a></li> 
    <li>[优化] 数据库上下文池小性能优化</li> 
   </ul> </li> 
  <li> <p><strong>文档变化</strong></p> 
   <ul> 
    <li>[新增] <code>Docker</code> 环境下自动化部署 <a href="https://gitee.com/dotnetchina/Furion/pulls/209">#PR209</a></li> 
    <li>[新增] <code>JSON</code> 序列化 文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3B6D8">#I3B6D8</a></li> 
    <li>[更新] 跨域、安全授权、即时通信文档、多语言、规范化文档</li> 
   </ul> </li> 
  <li> <p><strong>问答答疑</strong></p> 
   <ul> 
    <li>[答疑] <code>Furion.Extras.DatabaseAccessor.SqlSugar</code> 配置多个数据库打印 SQL 语句问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I39PDC">#I39PDC</a></li> 
    <li>[答疑] <code>ORACLE</code> 数据库多租户模式下返回值为指定类型时系统卡死 <a href="https://gitee.com/dotnetchina/Furion/issues/I39RNH">#I39RNH</a></li> 
    <li>[答疑] 假删除指向异常 <a href="https://gitee.com/dotnetchina/Furion/issues/I39XZA">#I39XZA</a></li> 
    <li>[答疑] <code>Furion</code> 多语言配置节是放在 <code>AppSettings</code> 里面还是外面呢？ <a href="https://gitee.com/dotnetchina/Furion/issues/I3A4SB">#I3A4SB</a></li> 
    <li>[答疑] 没找到数据库上下文 <a href="https://gitee.com/dotnetchina/Furion/issues/I3A5HS">#I3A5HS</a></li> 
    <li>[答疑] 有 <code>QQ</code> 交流群吗？ <a href="https://gitee.com/dotnetchina/Furion/issues/I3AAM7">#I3AAM7</a></li> 
    <li>[答疑] <code>Vue3</code> 环境下配置 <code>SignalR</code> 跨域出错 <a href="https://gitee.com/dotnetchina/Furion/issues/I3ALQ7">#I3ALQ7</a></li> 
    <li>[答疑] 设置 <code>Swagger</code> 参数非必填 <a href="https://gitee.com/dotnetchina/Furion/issues/I3AT02">#I3AT02</a></li> 
    <li>[答疑] EFCore 调用 Insert 时报 <code>Unknown column 'Discriminator' in 'field list'</code> 异常 <a href="https://gitee.com/dotnetchina/Furion/issues/I3B2LC">#I3B2LC</a></li> 
    <li>[答疑] 逆向 <code>mysql</code> 数据库时 <code>cli</code> 出现错误 <a href="https://gitee.com/dotnetchina/Furion/issues/I3B64F">#I3B64F</a></li> 
    <li>[答疑] Sql 高级代理使用过程中 DateTime 类型的参数序列化失败 <a href="https://gitee.com/dotnetchina/Furion/issues/I3AZXK">#I3AZXK</a></li> 
    <li>[答疑] 使用 Mysql 执行 Add-Migration 报错 <a href="https://gitee.com/dotnetchina/Furion/issues/I3B8EW">#I3B8EW</a></li> 
    <li>[答疑] Saas 多租户模式-独立 Database 模式下无法获取 Tenant, 导致无法自动切换的问题<a href="https://gitee.com/dotnetchina/Furion/issues/I3AVXU">#I3AVXU</a></li> 
    <li>[答疑] 如何自定义 WebAPI 统一结果模型 <a href="https://gitee.com/dotnetchina/Furion/issues/I3BBYW">#I3BBYW</a> <a href="https://gitee.com/dotnetchina/Furion/issues/I3BBYV">#I3BBYV</a></li> 
    <li>[答疑] 在 <code>Web.Entry</code> 项目新建了一个 <code>Controller</code>，多了未知方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I3BKH5">#I3BKH5</a></li> 
    <li>[答疑] <code>AOP</code> 拦截如何解析服务 <a href="https://gitee.com/dotnetchina/Furion/issues/I3BUM3">#I3BUM3</a></li> 
    <li>[答疑] 动态 WebAPI 返回参数被省略 <a href="https://gitee.com/dotnetchina/Furion/issues/I3C2XR">#I3C2XR</a></li> 
    <li>[答疑] 如何设置某一个接口响应数据不自动转小写，按原始字段名返回 <a href="https://gitee.com/dotnetchina/Furion/issues/I38L9B">#I38L9B</a></li> 
    <li>[答疑] code first 如何配置自动迁移 <a href="https://gitee.com/dotnetchina/Furion/issues/I3CCR0">#I3CCR0</a></li> 
    <li>[答疑] webapi 混合授权如何区分不同系统 <a href="https://gitee.com/dotnetchina/Furion/issues/I3CJCY">#I3CJCY</a></li> 
    <li>[答疑] EFCore 不支持递归无限级遍历关系 <a href="https://gitee.com/dotnetchina/Furion/issues/I3CET9">#I3CET9</a></li> 
   </ul> </li> 
  <li> <p><strong>不做实现</strong></p> 
   <ul> 
    <li>[废弃] 建议 <code>EFCore</code> 可配置外键关系导航问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3994X">#I3994X</a></li> 
    <li>[废弃] 建议将 <code>EFCore</code> 剥离出来，作为插件的形式提供。这样可以选择自己喜欢的 <code>ORM</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3ABNX">#I3ABNX</a></li> 
    <li>[废弃] 事件总线能否提供返回值 <a href="https://gitee.com/dotnetchina/Furion/issues/I3AWL6">#I3AWL6</a></li> 
    <li>[废弃] Sql 模板能仿照 Mybatis 一样加各种标签吗？<a href="https://gitee.com/dotnetchina/Furion/issues/I3ASRS">#I3ASRS</a></li> 
    <li>[废弃] EFCore 更新或排除更新指定列支持传入 DTO 模型 <a href="https://gitee.com/dotnetchina/Furion/issues/I3AS5K">#I3AS5K</a></li> 
    <li>[废弃] 新增 <code>UnitOfWork</code> 事务完成事件 <a href="https://gitee.com/dotnetchina/Furion/issues/I3BRMI">#I3BRMI</a></li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2 style="text-align:left">文档地址</h2> 
<ul> 
 <li>国内文档：<a href="https://dotnetchina.gitee.io/furion" target="_blank">https://dotnetchina.gitee.io/furion</a></li> 
 <li>国外文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffurion.pro%2F" target="_blank">https://furion.pro</a></li> 
</ul> 
<h2 style="text-align:left">项目地址</h2> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmonksoul%2FFurion" target="_blank">https://github.com/monksoul/Furion</a></li> 
 <li>Docker：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fr%2Fmonksoul%2Ffurion" target="_blank">https://hub.docker.com/r/monksoul/furion</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank">https://www.nuget.org/packages/Furion</a></li> 
</ul> 
<p style="text-align:left"><a href="https://gitee.com/dotnetchina/Furion">Furion</a><span style="background-color:#ffffff; color:#333333"> 遵循 </span><a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE">Apache-2.0</a><span style="background-color:#ffffff; color:#333333"> 开源协议，欢迎大家提交 </span><a href="https://gitee.com/dotnetchina/Furion/pulls">PR</a><span style="background-color:#ffffff; color:#333333"> 或 </span><a href="https://gitee.com/dotnetchina/Furion/issues/new">Issue</a><span style="background-color:#ffffff; color:#333333">。喜欢可以给个 </span><a href="https://gitee.com/dotnetchina/Furion/stargazers">Star</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            