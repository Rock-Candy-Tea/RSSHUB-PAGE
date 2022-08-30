
---
title: '.NET 框架 Furion v4.3.4 发布，日志模块全新体验'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-02188b434314699df2a6effac1fcf294794.png'
author: 开源中国
comments: false
date: Tue, 30 Aug 2022 16:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-02188b434314699df2a6effac1fcf294794.png'
---

<div>   
<div class="content">
                                                                                            <h2>序言</h2> 
<p>自 Furion v3.9.2 版本有了自主可控的日志组件之后，越来越多的 Furion 框架使用者移除了第三方日志组件选择框架内置的，<strong>Furion 框架提供了企业开发所需的几乎所有日志需求。</strong></p> 
<p>本期更新主要对日志性能，日志模板，日志功能进行了改进优化。</p> 
<ul> 
 <li>仓库地址：<a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>文档地址：<a href="https://dotnetchina.gitee.io/furion/">https://dotnetchina.gitee.io/furion/</a></li> 
</ul> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-02188b434314699df2a6effac1fcf294794.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-4fd7fdabe89c2b96bdaf4c62e1d3be4ced6.png" width="1920" referrerpolicy="no-referrer"></p> 
<h2>本期亮点</h2> 
<h3>1.  更加美观的日志模板</h3> 
<pre><code>[INF] [Microsoft.Hosting.Lifetime] 2022-08-30T15:52:13.7033488+08:00 [ListeningOnAddress] 
      Now listening on: https://localhost:5001
[INF] [Microsoft.Hosting.Lifetime] 2022-08-30T15:52:13.7405477+08:00 [0] 
      Application started. Press Ctrl+C to shut down.
[INF] [Microsoft.Hosting.Lifetime] 2022-08-30T15:52:13.7453185+08:00 [0] 
      Hosting environment: Development
[INF] [Microsoft.Hosting.Lifetime] 2022-08-30T15:52:13.7482401+08:00 [0] 
      Content root path: D:\Workplaces\OpenSources\Furion\samples\Furion.Web.Entry\
[WRN] [Furion.Application.TestLoggerServices] 2022-08-30T15:52:32.3892150+08:00 [0] 
      我是一个二配置日志 20
[ERR] [Furion.Application.TestLoggerServices] 2022-08-30T15:52:35.1479371+08:00 [0] 
      测试日志异常      
      ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      System.Exception: 错误啦
      ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[INF] [System.Logging.LoggingMonitor] 2022-08-30T15:53:26.3936806+08:00 [0] 
      ┏━━━━━━━━━━━  Logging Monitor ━━━━━━━━━━━
      ┣ Furion.Application.TestLoggerServices.GetPerson (Furion.Application)
      ┣ 
      ┣ 控制器名称：          TestLoggerServices
      ┣ 操作名称：            GetPerson
      ┣ 路由信息：            [area]: ; [controller]: test-logger; [action]: person
      ┣ 请求方式：            GET
      ┣ 请求地址：            https://localhost:5001/api/test-logger/person/233
      ┣ 来源地址：            https://localhost:5001/api/index.html
      ┣ 浏览器标识：          Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70
      ┣ 客户端 IP 地址：      0.0.0.1
      ┣ 服务端 IP 地址：      0.0.0.1
      ┣ 服务端运行环境：      Development
      ┣ 执行耗时：            56ms
      ┣ ━━━━━━━━━━━━━━━  参数列表 ━━━━━━━━━━━━━━━
      ┣ Content-Type：        
      ┣ 
      ┣ id (Int32)：          233
      ┣ ━━━━━━━━━━━━━━━  返回信息 ━━━━━━━━━━━━━━━
      ┣ 原始类型：            Furion.Application.Persons.PersonDto
      ┣ 最终类型：            Furion.UnifyResult.RESTfulResult`1[[System.Object, System.Private.CoreLib, Version=6.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]
      ┣ 最终返回值：          &#123;"StatusCode":200,"Data":&#123;"Id":233,"Name":null,"Age":0,"Address":null,"PhoneNumber":null,"QQ":null,"CreatedTime":"0001-01-01T00:00:00+00:00","Childrens":null,"Posts":null&#125;,"Succeeded":true,"Errors":null,"Extras":null,"Timestamp":1661846006385&#125;
      ┗━━━━━━━━━━━  Logging Monitor ━━━━━━━━━━━
[ERR] [System.Logging.FriendlyException] 2022-08-30T15:53:33.0839966+08:00 [0] 
      Attempted to divide by zero.      
      ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      System.DivideByZeroException: Attempted to divide by zero.
         at Furion.Application.TestLoggerServices.测试直接抛出异常拦截(Int32 id) in D:\Workplaces\OpenSources\Furion\samples\Furion.Application\TestLoggerServices.cs:line 92
         at lambda_method108(Closure , Object , Object[] )
         at Microsoft.AspNetCore.Mvc.Infrastructure.ActionMethodExecutor.SyncObjectResultExecutor.Execute(IActionResultTypeMapper mapper, ObjectMethodExecutor executor, Object controller, Object[] arguments)
         at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.<InvokeActionMethodAsync>g__Logged|12_1(ControllerActionInvoker invoker)
         at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.<InvokeNextActionFilterAsync>g__Awaited|10_0(ControllerActionInvoker invoker, Task lastTask, State next, Scope scope, Object state, Boolean isCompleted)
         at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.Rethrow(ActionExecutedContextSealed context)
         at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.Next(State& next, Scope& scope, Object& state, Boolean& isCompleted)
         at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.InvokeInnerFilterAsync()
      --- End of stack trace from previous location ---
         at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.<InvokeNextExceptionFilterAsync>g__Awaited|26_0(ResourceInvoker invoker, Task lastTask, State next, Scope scope, Object state, Boolean isCompleted)
      ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[INF] [Microsoft.EntityFrameworkCore.Database.Command] 2022-08-30T15:53:44.1172386+08:00 [Microsoft.EntityFrameworkCore.Database.Command.CommandExecuted] 
      Executed DbCommand (53ms) [Parameters=[@__p_0='1'], CommandType='Text', CommandTimeout='30']
      SELECT "p"."Id", "p"."Address", "p"."Age", "p"."CreatedTime", "p"."Name", "p"."UpdatedTime"
      FROM "Person" AS "p"
      WHERE "p"."Id" = @__p_0
      LIMIT 1
[WRN] [Microsoft.EntityFrameworkCore.Query] 2022-08-30T15:53:49.0965317+08:00 [Microsoft.EntityFrameworkCore.Query.MultipleCollectionIncludeWarning] 
      Compiling a query which loads related collections for more than one collection navigation, either via 'Include' or through projection, but no 'QuerySplittingBehavior' has been configured. By default, Entity Framework will use 'QuerySplittingBehavior.SingleQuery', which can potentially result in slow query performance. See https://go.microsoft.com/fwlink/?linkid=2134277 for more information. To identify the query that's triggering this warning call 'ConfigureWarnings(w => w.Throw(RelationalEventId.MultipleCollectionIncludeWarning))'.
[INF] [Microsoft.EntityFrameworkCore.Database.Command] 2022-08-30T15:53:49.1180132+08:00 [Microsoft.EntityFrameworkCore.Database.Command.CommandExecuted] 
      Executed DbCommand (2ms) [Parameters=[], CommandType='Text', CommandTimeout='30']
      SELECT "p"."Id", "p"."Name", "p"."Age", "p"."Address", "p0"."PhoneNumber", "p0"."QQ", "p"."CreatedTime", "p0"."Id", "c"."Id", "c"."Name", "c"."Gender", "t"."Id", "t"."Name", "t"."PersonsId", "t"."PostsId"
      FROM "Person" AS "p"
      LEFT JOIN "PersonDetail" AS "p0" ON "p"."Id" = "p0"."PersonId"
      LEFT JOIN "Children" AS "c" ON "p"."Id" = "c"."PersonId"
      LEFT JOIN (
          SELECT "p2"."Id", "p2"."Name", "p1"."PersonsId", "p1"."PostsId"
          FROM "PersonPost" AS "p1"
          INNER JOIN "Post" AS "p2" ON "p1"."PostsId" = "p2"."Id"
      ) AS "t" ON "p"."Id" = "t"."PersonsId"
      ORDER BY "p"."Id", "p0"."Id", "c"."Id", "t"."PersonsId", "t"."PostsId"</code></pre> 
<p><img height="1036" src="https://oscimg.oschina.net/oscnet/up-ca6562b57bb525d3acfc03bcfed7f821570.png" width="1523" referrerpolicy="no-referrer"></p> 
<h3>2. 支持 Visual Studio Code 日志收缩、异常日志高亮</h3> 
<p><img height="946" src="https://oscimg.oschina.net/oscnet/up-79977d36fc41d2546ff5f9411dc0dfb16de.png" width="1279" referrerpolicy="no-referrer"></p> 
<p><img height="909" src="https://oscimg.oschina.net/oscnet/up-90e87e172be4cc921a7e6418f8bc5d133b2.jpg" width="1425" referrerpolicy="no-referrer"></p> 
<h3>3. 提供 RabbitMQ 事件总线使用指南</h3> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-7b8dfc016ead88c8a0555e43a5386a5f393.png" width="1919" referrerpolicy="no-referrer"></p> 
<h3>4. 提供 Log 静态类写日志更多功能</h3> 
<pre><code class="language-cs">// 创建日志对象
var logger = Log.CreateLogger("日志名称");

// 创建日志工厂
using var loggerFactory = Log.CreateLoggerFactory(builder => &#123;
    // ....
&#125;);

// 日志记录
Log.Information("Information");
Log.Warning("Warning");
Log.Error("Error");
Log.Debug("Debug");
Log.Trace("Trace");
Log.Critical("Critical");</code></pre> 
<h3>5. 提供 MessageCenter 事件总线静态类</h3> 
<pre><code class="language-cs">// 发送消息（含诸多重载）
await MessageCenter.PublishAsync("messageId", new &#123;&#125;);

// 动态订阅消息
MessageCenter.Subscribe("messageId", async (ctx) => &#123;
    Console.WriteLine("我是动态的");
    await Task.CompletedTask;
&#125;);

// 取消订阅
MessageCenter.Unsubscribe("messageId");</code></pre> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span><code>AppSettings</code><span> </span>配置的<span> </span><code>ExcludeAssemblies</code><span> </span>属性，支持忽略指定程序集扫描<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/7b7747f38c84acfe7df3469599bebf417e5ad843" target="_blank">7b7747f</a></li> 
    <li>[新增]<span> </span><code>Oops.Oh</code><span> </span>和<span> </span><code>Oops.Bah</code><span> </span>支持设置额外数据<span> </span><code>.WithData(data)</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5O38E" target="_blank">#I5O38E</a></li> 
    <li>[新增]<span> </span>定时任务<span> </span><code>Crontab.GetSleepMilliseconds(baseTime)</code><span> </span>获取下一个发生时间的时间差<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/d024fae670b7ce3fd4bfd26aee70ed318a4c0383" target="_blank">d024fae</a></li> 
    <li>[新增]<span> </span><strong>友好异常默认打印异常日志，避免生产环境漏掉重要异常信息<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/6e3a5bdd0fd22a7f9ae618b7495cd64081a7f2e8" target="_blank">6e3a5bd</a></strong></li> 
    <li>[新增]<span> </span>日志静态类<span> </span><code>Log.CreateLoggerFactory()</code><span> </span>静态方法<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/75c672afc58b393313916c433cb9d92c779b9629" target="_blank">75c672a</a></li> 
    <li>[新增]<span> </span><strong>事件总线<span> </span><code>MessageCenter</code><span> </span>静态类，解决从<span> </span><code>Fur v1.x</code><span> </span>版本升级问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/a29fc7cf63a3ea41b1617a6ad98a701a243e24f8" target="_blank">a29fc7c</a></strong></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span><strong><code>Furion</code><span> </span>程序集<span> </span><code>PublicKeyToken</code><span> </span>强签名</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/26b12c0fd64b153a71496eb62110567e05450f20" target="_blank">26b12c0</a></li> 
    <li>[调整]<span> </span><strong>事件总线<span> </span><code>IEventBusFactory</code><span> </span>事件工厂方法<span> </span><code>AddSubscriber -> Subscribe</code>，<code>RemoveSubscriber -> Unsubscribe</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/a29fc7cf63a3ea41b1617a6ad98a701a243e24f8" target="_blank">a29fc7c</a></strong></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[修复]<span> </span>生成包含<span> </span><code>中文</code><span> </span>的<span> </span><code>JWT Token</code><span> </span>解密后出现乱码问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5O397" target="_blank">#I5O397</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[调整]<span> </span>默认输出文件日志模板，使其更加美观<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/1518cf3be74524ed0d3f73360068a9a0ec6685d9" target="_blank">#1518cf3</a></li> 
   </ul> </li> 
  <li> <p><strong>文档</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span><code>RabbitMQ</code><span> </span>事件总线文档</li> 
    <li>[更新]<span> </span><code>AppSettings</code><span> </span>配置文档、事件总线文档、多数据库配置文档、日志文档、定时任务文档、<code>MessageCenter</code><span> </span>文档</li> 
   </ul> </li> 
 </ul> 
</blockquote>
                                        </div>
                                      
</div>
            