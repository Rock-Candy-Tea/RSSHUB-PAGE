
---
title: '学 .NET5_6 从 Furion 开始，v2.11.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Thu, 01 Jul 2021 18:25:00 GMT
thumbnail: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:center"><img height="80" src="https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png" width="127" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <p style="text-align:center"><a href="https://gitee.com/dotnetchina/Furion/stargazers"><img alt="star" src="https://gitee.com/dotnetchina/Furion/badge/star.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/members"><img alt="fork" src="https://gitee.com/dotnetchina/Furion/badge/fork.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fstargazers" target="_blank"><img alt="GitHub stars" src="https://img.shields.io/github/stars/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fnetwork" target="_blank"><img alt="GitHub forks" src="https://img.shields.io/github/forks/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/badge/license-Apache2-yellow" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></p> 
</div> 
<div style="text-align:left"> 
 <p style="text-align:center">让 .NET 开发更简单，更通用，更流行。</p> 
</div> 
<p> </p> 
<h2>本期更新</h2> 
<blockquote> 
 <p><span style="color:#2980b9"><strong>该版本有多个破坏性更改，更新时请认真查看。</strong></span></p> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] <code>App.Configuration.Reload()</code> 拓展 <a href="https://gitee.com/dotnetchina/Furion/issues/I3XYI8">#I3XYI8</a></li> 
    <li>[新增] <code>ISubscribeHandler</code> 支持异步方法定义 <a href="https://gitee.com/dotnetchina/Furion/issues/I3XYHJ">#I3XYHJ</a></li> 
    <li>[新增] <code>app.UseUnifyResultStatusCodes()</code> 可配置修改返回状态码 <a href="https://gitee.com/dotnetchina/Furion/issues/I3VZQH">#I3VZQH</a></li> 
    <li>[新增] 远程请求添加默认 <code>User-Agent</code> 头 <a href="https://gitee.com/dotnetchina/Furion/issues/I3W17C">#I3W17C</a></li> 
    <li>[新增] 支持 <code>Sql</code> 高级代理切换数据库上下文定位器 <a href="https://gitee.com/dotnetchina/Furion/issues/I3XFP6">#I3XFP6</a> <a href="https://gitee.com/dotnetchina/Furion/issues/I3XDCR">#I3XDCR</a></li> 
    <li>[新增] 定时任务 <code>CronFormat</code> 自动识别 <a href="https://gitee.com/dotnetchina/Furion/issues/I3Y7GT">#I3Y7GT</a></li> 
    <li>[新增] <code>Sql 高级代理</code> 拦截功能 <a href="https://gitee.com/dotnetchina/Furion/issues/I3YHG4">#I3YHG4</a></li> 
    <li>[新增] 拦截远程请求所有异常处理 <a href="https://gitee.com/dotnetchina/Furion/issues/I3YPDE">#I3YPDE</a></li> 
    <li>[新增] 远程请求配置 <code>Timeout</code> 超时时间 <a href="https://gitee.com/dotnetchina/Furion/issues/I3YPPK">#I3YPPK</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[移除] <strong><code>FakeDelete</code> 假删除/软删除所有功能 <a href="https://gitee.com/dotnetchina/Furion/issues/I3XKII">#I3XKII</a></strong></li> 
    <li>[调整] <code>[NonAutomatic]</code> 特性名称为 <code>[Manual]</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3XKKX">#I3XKKX</a></li> 
    <li>[调整] <code>[NotChangedListener]</code> 特性名称为 <code>[SuppressChangedListener]</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3XKLZ">#I3XKLZ</a></li> 
    <li>[调整] <code>[ManualSaveChanges]</code> 名称为 <code>[ManualCommit]</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3XKNP">#I3XKNP</a></li> 
    <li>[调整] <strong><code>DbContext.TenantIdQueryFilterExpression</code> 名称为 <code>DbContext.BuildTenantQueryFilter</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3XKTB">#I3XKTB</a></strong></li> 
    <li>[调整] <code>[SkipScan]</code> 名称为 <code>[SuppressSniffer]</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3XN5N">#I3XN5N</a></li> 
    <li>[调整] <code>[SkipProxy]</code> 名称为 <code>[SuppressProxy]</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3XN7O">#I3XN7O</a></li> 
    <li>[重构] <code>Sql</code> 执行，性能提升 20% <a href="https://gitee.com/dotnetchina/Furion/issues/I3W33U">#I3W33U</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 动态 WebAPI 扫描控制器没有屏蔽没有注册的第三方控制器 <a href="https://gitee.com/dotnetchina/Furion/issues/I3Y7TJ">#I3Y7TJ</a></li> 
    <li>[修复] <code>AppDbContext</code> 设置 <code>TablePrefix</code> 无效： <a href="https://gitee.com/dotnetchina/Furion/issues/I3Y57Q">#I3Y57Q</a></li> 
    <li>[修复] 修复定时任务使用异步委托导致程序终止 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3XVZ0">#I3XVZ0</a></li> 
    <li>[修复] 事件总线一个 <code>消息id</code> 对应多个 <code>Handler</code> 只触发第一个<a href="https://gitee.com/dotnetchina/Furion/issues/I3XYP0">#I3XYP0</a></li> 
    <li>[修复] <code>.ToPagedList()</code> 分页方法传入小于或等于 0 的页码 <a href="https://gitee.com/dotnetchina/Furion/issues/I3XNAN">#I3XNAN</a></li> 
    <li>[修复] <code>JSON</code> 序列化默认 <code>DateTimeOffset</code> 异常 <a href="https://gitee.com/dotnetchina/Furion/issues/I3XMOL">#I3XMOL</a></li> 
    <li>[修复] 继承 <code>Serlig</code> 日志在 <code>Worker Service</code> 生成重复日志 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3WA0L">#I3WA0L</a> <a href="https://gitee.com/dotnetchina/Furion/pulls/331">!331</a></li> 
    <li>[修复] <code>粘土对象</code> 动态添加 <code>Clay</code> 类型 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3W9LW">#I3W9LW</a></li> 
    <li>[修复] <code>ValidationTypes.Numeric</code> 校验数值类型正则表达式错误 <a href="https://gitee.com/dotnetchina/Furion/issues/I3WADS">#I3WADS</a></li> 
    <li>[修复] 数据库命令参数 <code>DbParameter</code> 的 <code>Value</code> 是 <code>object</code> 类型的时候且不指定 <a href="https://gitee.com/dotnetchina/Furion/issues/I3YKM6">#I3YKM6</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[增强] 支持 <code>appsettings.json</code> 等自定义配置文件中文命名 <a href="https://gitee.com/dotnetchina/Furion/issues/I3YBFD">#I3YBFD</a></li> 
    <li>[改进] 远程请求配置命名客户端 <code>BaseAddress</code> 地址兼容处理 <a href="https://gitee.com/dotnetchina/Furion/issues/I3YCRH">#I3YCRH</a></li> 
    <li>[移除] 框架无用代码、优化代码</li> 
    <li>[优化] <code>Furion</code> 在 <code>非 Web</code> 环境下性能</li> 
   </ul> </li> 
  <li> <p><strong>文档变化</strong></p> 
   <ul> 
    <li>[新增] 会话和状态管理 文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3YI3G">#I3YI3G</a></li> 
    <li>[更新] 远程请求、日志、数据库上下文、远程请求、<code>Sql</code> 高级代理文档</li> 
    <li>[更新] 配置文件 <a href="https://gitee.com/dotnetchina/Furion/issues/I3Y2EV">#I3Y2EV</a></li> 
   </ul> </li> 
  <li> <p><strong>问答答疑</strong></p> 
   <ul> 
    <li>[答疑] <code>dapper</code> 多个数据源如何继承 <a href="https://gitee.com/dotnetchina/Furion/issues/I3WUOI">#I3WUOI</a></li> 
    <li>[答疑] 关于 <code>SpareTime</code> 多次执行问题<a href="https://gitee.com/dotnetchina/Furion/issues/I3XEQU">#I3XEQU</a></li> 
    <li>[答疑] 选项更改通知（热更新）：数据库里的数据更改了如何通知选项进行改变？ <a href="https://gitee.com/dotnetchina/Furion/issues/I3XYI8">#I3XYI8</a></li> 
    <li>[答疑] <code>SaaS</code> 多租户添加时无法获取租户<code>Id</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3Y5CF">#I3Y5CF</a></li> 
    <li>[答疑] 获取 <code>_httpContextAccessor.HttpContext</code> 为空<a href="https://gitee.com/dotnetchina/Furion/issues/I3Y6BI">#I3Y6BI</a></li> 
    <li>[答疑] <code>Ubuntu</code> 中使用 <code>App.Configuration</code> 方法读取不到值 <a href="https://gitee.com/dotnetchina/Furion/issues/I3Y74H">#I3Y74H</a></li> 
    <li>[答疑] 数据库上下文作用域问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3YHXP">#I3YHXP</a></li> 
    <li>[答疑] 使用 <code>UnitofWork</code> 提交事务，可以提交成功，但是系统会有错误 <a href="https://gitee.com/dotnetchina/Furion/issues/I3YIWU">#I3YIWU</a></li> 
   </ul> </li> 
  <li> <p><strong>不做实现</strong></p> 
   <ul> 
    <li>[废弃] <code>SpareTIme</code> 新增 <code>Dashboard</code> 控制台看板，同时可以对任务进行暂停、删除、查看<a href="https://gitee.com/dotnetchina/Furion/issues/I3XELY">#I3XELY</a></li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2 style="text-align:left">贡献者画像</h2> 
<p style="text-align:left"><img alt="Giteye chart" src="https://chart.giteye.net/gitee/dotnetchina/Furion/ZS49EPL6.png" referrerpolicy="no-referrer"></p> 
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
<p> </p>
                                        </div>
                                      
</div>
            