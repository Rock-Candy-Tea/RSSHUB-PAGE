
---
title: 'Furion 2.0.0：.NET 开发者不可忽视的框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Mon, 19 Apr 2021 13:34:00 GMT
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
<h2>发展大事记</h2> 
<p>自 Furion 诞生一来得到高速发展最大的原因是弥补了 .NET 这么多年没有对标 Java Spring 的框架，所以 Furion 的诞生迅速吸引了非常多的 .NET 开发者，<strong>QQ 群成员达到了 5500 人+</strong>。</p> 
<p>以下是 Furion 的发展大事记：</p> 
<blockquote> 
 <ul> 
  <li><strong>2020 年</strong> 
   <ul> 
    <li><strong>2020 年 06 月 29 日</strong>，在百小僧公司成立 8 周年之际在 Gitee 平台创建了 Fur 仓库。</li> 
    <li><strong>2020 年 09 月 01 日</strong>，正式写下第一行代码。</li> 
    <li><strong>2020 年 10 月 22 日</strong>，Fur 在 Gitee 平台获得 1000 stars.</li> 
    <li><strong>2020 年 11 月 11 日</strong>，单身节当天发布了 1.0.0 正式版。</li> 
    <li><strong>2020 年 11 月 20 日</strong>，Fur 改名为 Furion。</li> 
    <li><strong>2020 年 11 月 23 日</strong>，Furion Logo 由之前的 奶牛 更换为 袋鼠。</li> 
    <li><strong>2020 年 12 月 22 日</strong>，Furion 在 Gitee 平台获得 2000 stars。</li> 
   </ul> </li> 
  <li>2021 年 
   <ul> 
    <li><strong>2021 年 02 月 20 日</strong>，Furion 捐赠项目到 dotNET China 组织。</li> 
    <li><strong>2021 年 03 月 05 日</strong>，Furion 在 Gitee 平台获得 3000 stars。</li> 
    <li><strong>2021 年 04 月 01 日</strong>，Furion 所在群 dotNET China 突破 5000 人。</li> 
    <li><strong>2021 年 04 月 06 日</strong>，Furion 在 Gitee 平台获得 4000 stars。</li> 
    <li><strong>2021 年 04 月 19 日</strong>，Furion 正式发布 2.0.0 版本。</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2>优秀的贡献者们</h2> 
<p>Furion 提供完善的代码注释和文档说明，以至于吸引了<strong>超过 110 个贡献者贡献代码</strong>。 <span style="background-color:#ffffff; color:#40485b">感谢每一位为 Furion </span><span style="background-color:#ffffff; color:#40485b">贡献代码的朋友。</span></p> 
<p><img alt="Giteye chart" src="https://chart.giteye.net/gitee/dotnetchina/Furion/ZS49EPL6.png" referrerpolicy="no-referrer"></p> 
<h2>2.0.0 版本为什么来的那么快</h2> 
<p>通过上面的大事记可以看出，Furion 从 1.0.0 版本过渡到了 2.0.0 版本只用了 5 个月的时间。相对于大部分的开源软件来说，这是非常短的主版本迭代周期。但是为什么依然需要发布 2.0.0 版本呢？有以下原因：</p> 
<blockquote> 
 <ol> 
  <li>创造 Furion 之初没想到该项目短短几个月发展的如此之快，所以 1.x 版本很多功能代码都为了功能开发而开发，在架构设计、灵活维护性及性能方面处理不妥，导致后续拓展新功能带来了不少麻烦，可以说是在功能中制造更多的漏洞。</li> 
  <li>在这 7 个月开源中，每天面对使用者的庞大需求及用户指数增长的威压下，对 .NET 有了更高层次的理解。</li> 
  <li>开源过程中认识了很多朋友，也收获了 112 个贡献者对代码的改进，在他们贡献的代码中也让自己成长了不少。</li> 
  <li>最后一个是为了迎接 .NET 6 版本的到来。</li> 
 </ol> 
</blockquote> 
<p>所以，综上所述，<strong>花了近 15 天的时间对 Furion 的底层架构进行了大面积的重构及优化，其中包括删除了近 2700 行代码，31 个文件及底层架构模式的重大调整。</strong></p> 
<h2>2.0.0 有什么亮点</h2> 
<h3>亮点一：支持控制台应用程序开发</h3> 
<p>Furion 不再局限于 Web 应用开发还额外支持控制台应用程序开发。</p> 
<pre><code class="language-cs">using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace FurionWorkers
&#123;
    public class Program
    &#123;
        public static void Main(string[] args)
        &#123;
            CreateHostBuilder(args).Build().Run();
        &#125;

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .Inject();
    &#125;
&#125;</code></pre> 
<h3>亮点二：内置强大的任务调度</h3> 
<pre><code class="language-cs">// 每隔 1s 执行
SpareTime.Do(1000, (timer, count) => &#123;
    Console.WriteLine("现在时间：" + DateTime.Now.ToString("yyyy-MM-dd HH🇲🇲ss"));
    Console.WriteLine($"一共执行了：&#123;count&#125; 次");
&#125;);</code></pre> 
<pre><code class="language-cs">SpareTime.Do("* * * * *", (timer, count) => &#123;
    Console.WriteLine("现在时间：" + DateTime.Now.ToString("yyyy-MM-dd HH🇲🇲ss"));
    Console.WriteLine($"一共执行了：&#123;count&#125; 次");
&#125;, "cronName", "每分钟执行一次");</code></pre> 
<p><img height="1010" src="https://oscimg.oschina.net/oscnet/up-b43766d63b640b5e0f9260dd2b90309f6e8.png" width="1916" referrerpolicy="no-referrer"></p> 
<h3>亮点三：支持跨平台的守护进程服务</h3> 
<pre><code class="language-cs">using Furion.TaskScheduler;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System;
using System.Threading;
using System.Threading.Tasks;

namespace WorkerService1
&#123;
    public class Worker : BackgroundService
    &#123;
        private readonly ILogger<Worker> _logger;

        public Worker(ILogger<Worker> logger)
        &#123;
            _logger = logger;
        &#125;

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        &#123;
            while (!stoppingToken.IsCancellationRequested)
            &#123;
                // 执行 Cron 表达式任务
                await SpareTime.DoAsync("*/5 * * * * *", () =>
                &#123;
                    _logger.LogInformation("Worker running at: &#123;time&#125;", DateTimeOffset.Now);
                &#125;, stoppingToken, CronFormat.IncludeSeconds);
            &#125;
        &#125;
    &#125;
&#125;</code></pre> 
<p><img height="1010" src="https://oscimg.oschina.net/oscnet/up-e8026227ac4994117dd0d47d2f0dae1dac1.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3>亮点四：支持 Anno + Furion 微服务开发</h3> 
<p><img height="1007" src="https://oscimg.oschina.net/oscnet/up-e6bc3084376bbbe1f8507da489f11f63ecf.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3>亮点五：功能文档已经全部完成</h3> 
<p><img height="1008" src="https://oscimg.oschina.net/oscnet/up-5fa0a2d390abb41d7c2081333e46aa0124d.png" width="1917" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 控制台应用程序及 Worker Services 支持 <a href="https://gitee.com/dotnetchina/Furion/issues/I3K4DG">#I3K4DG</a></li> 
    <li>[新增] 完整任务调度功能 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IRUX">#I3IRUX</a></li> 
    <li>[新增] <code>Cron</code> 表达式解析 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IQ9Y">#I3IQ9Y</a></li> 
    <li>[新增] 支持 <code>Swagger</code> 自定义配置 <code>swagger.json</code> 地址模板 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IHMX">#I3IHMX</a></li> 
    <li>[新增] 支持配置动态 WebApi 区域 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IJAZ">#I3IJAZ</a></li> 
    <li>[新增] 远程请求新增支持传入服务提供器 <code>IServiceProvider</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3IVBL">#I3IVBL</a></li> 
    <li>[新增] 全局配置选型 <code>SupportPackageNamePrefixs</code> 配置，支持配置包前缀 <a href="https://gitee.com/dotnetchina/Furion/issues/I3K0SN">#I3K0SN</a></li> 
    <li>[新增] 应用启动时支持 <code>referenceassembly</code> 类型程序集扫描 <a href="https://gitee.com/dotnetchina/Furion/issues/I3K0SN">#I3K0SN</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[重构] 完整任务调度功能 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IRUX">#I3IRUX</a></li> 
    <li>[重构] 日志模块功能 <a href="https://gitee.com/dotnetchina/Furion/issues/I3J2K0">#I3J2K0</a></li> 
    <li>[重构] 模板引擎功能 <a href="https://gitee.com/dotnetchina/Furion/issues/I3J46E">#I3J46E</a></li> 
    <li>[重构] 底层 <code>EFCoreRepository</code> 仓储 <a href="https://gitee.com/dotnetchina/Furion/issues/I3J6W5">#I3J6W5</a></li> 
    <li>[重构] sql 字符串拓展底层代码 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IVCE">#I3IVCE</a></li> 
    <li>[重构] 底层 <code>SqlRepository</code> 所有逻辑代码 <a href="https://gitee.com/dotnetchina/Furion/issues/I3J6V6">#I3J6V6</a></li> 
    <li>[重构] 数据库实体拓展方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I3J609">#I3J609</a></li> 
    <li>[调整] 事件事件总线同步执行为异步方式执行 <a href="https://gitee.com/dotnetchina/Furion/issues/I3J0WA">#I3J0WA</a></li> 
    <li>[移除] 框架底层 <code>HttpContext.IsAjaxRequest()</code> 拓展 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IVAA">#I3IVAA</a></li> 
    <li>[移除] <code>ValidationTypes.Required</code> 验证 <a href="https://gitee.com/dotnetchina/Furion/issues/I3KR85">#I3KR85</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 关闭 <code>InjectMiniProfiler</code> 参数后内存缓存无效 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IHLR">#I3IHLR</a></li> 
    <li>[修复] 在多租户中调用 <code>Tenant</code> 属性出现偶然性数据库上下文被释放的情况 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IC70">#I3IC70</a></li> 
    <li>[修复] Sql 代理中如果返回基元类型抛出不能将 object 转换成对应类型的异常 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IC84">#I3IC84</a></li> 
    <li>[修复] 存储过程多返回值的时候，outputvalues 的 name 不是定义的 MSG 的 name，是 Msg 类型。 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IC7Y">#I3IC7Y</a></li> 
    <li>[修复] PhoneNumber 手机号验证正则表达式错误 <a href="https://gitee.com/dotnetchina/Furion/issues/I3ID10">#I3ID10</a></li> 
    <li>[修复] 依赖注入 AOP 拦截无法捕获内部异常 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IGCC">#I3IGCC</a></li> 
    <li>[修复] 全局拦截标记异常已被处理后异常过滤器依然执行 <a href="https://gitee.com/dotnetchina/Furion/issues/I3J463">#I3J463</a></li> 
    <li>[修复] 自定义全局异常拦截器不起作用 <a href="https://gitee.com/dotnetchina/Furion/issues/I3K1SJ">#I3K1SJ</a></li> 
    <li>[修复] 在 WorkerService 模式下，还是使用 WebHostEnvironment 来判断 Host 环境，会导致错误 <a href="https://gitee.com/dotnetchina/Furion/issues/I3LCQY">#I3LCQY</a></li> 
    <li>[修复] 定时任务 <code>DoOnce</code> 抛空异常 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3M0ZT">#I3M0ZT</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[改进] 启动时程序集扫描类型 <a href="https://gitee.com/dotnetchina/Furion/issues/I3K0SN">#I3K0SN</a></li> 
    <li>[改进] <code>App.GetConfig<>("key")</code> 不支持获取单个值问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3ILF1">#I3ILF1</a></li> 
    <li>[改进] UrlEncode 应该用 <code>Uri.EscapeDataString()</code> 而不是 <code>HttpUtility.UrlEncode</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3ICTK">#I3ICTK</a></li> 
   </ul> </li> 
  <li> <p><strong>文档变化</strong></p> 
   <ul> 
    <li>[新增] 定位任务、后台任务文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3JHHG">#I3JHHG</a></li> 
    <li>[新增] 辅组角色服务文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3K5GN">#I3K5GN</a></li> 
    <li>[更新] 动态 WebAPI、规范化文档、数据库上下文文档</li> 
   </ul> </li> 
  <li> <p><strong>问答答疑</strong></p> 
   <ul> 
    <li>[答疑] 数据校验，自定义 ErrorMessage 无效问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3ICL3">#I3ICL3</a></li> 
    <li>[答疑] 最新 issue 中新增的“新增常用的 JSON 序列化方法” 会导致 AOP 拦截异常 <a href="https://gitee.com/dotnetchina/Furion/issues/I3I7VE">#I3I7VE</a></li> 
    <li>[答疑] Furion.DatabaseAccessor.PrivateEntityBase 中的 TenantId 数据类型设置为 object <a href="https://gitee.com/dotnetchina/Furion/issues/I3IQV6">#I3IQV6</a></li> 
    <li>[答疑] 有关异常拦截和处理的疑问 <a href="https://gitee.com/dotnetchina/Furion/issues/I3IUFZ">#I3IUFZ</a></li> 
    <li>[答疑] <code>DataValidation</code> 在空值的情况下被忽略掉了<a href="https://gitee.com/dotnetchina/Furion/issues/I3IWSM">#I3IWSM</a></li> 
    <li>[答疑] 日志文档没有更新 <a href="https://gitee.com/dotnetchina/Furion/issues/I3J1DX">#I3J1DX</a></li> 
    <li>[答疑] 对于 webapi 简单类型参数，是否可以以 json 方式提交 <a href="https://gitee.com/dotnetchina/Furion/issues/I3J18I">#I3J18I</a></li> 
    <li>[答疑] <code>IUnifyResultProvider</code> 实现中如果 <code>UnifyModel</code> 的 type 不是范型会报错 <a href="https://gitee.com/dotnetchina/Furion/issues/I3JBXF">#I3JBXF</a></li> 
    <li>[答疑] 如何模块化开发新功能？ <a href="https://gitee.com/dotnetchina/Furion/issues/I3J7ZZ">#I3J7ZZ</a></li> 
    <li>[答疑] 建议增加微服务中间件的集成 <a href="https://gitee.com/dotnetchina/Furion/issues/I3JTZQ">#I3JTZQ</a></li> 
   </ul> </li> 
  <li> <p><strong>不做实现</strong></p> </li> 
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
<p><a href="https://gitee.com/dotnetchina/Furion">Furion</a><span style="background-color:#ffffff; color:#333333"> 遵循 </span><a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE">Apache-2.0</a><span style="background-color:#ffffff; color:#333333"> 开源协议，欢迎大家提交 </span><a href="https://gitee.com/dotnetchina/Furion/pulls">PR</a><span style="background-color:#ffffff; color:#333333"> 或 </span><a href="https://gitee.com/dotnetchina/Furion/issues/new">Issue</a><span style="background-color:#ffffff; color:#333333">。喜欢可以给个 </span><a href="https://gitee.com/dotnetchina/Furion/stargazers">Star</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            