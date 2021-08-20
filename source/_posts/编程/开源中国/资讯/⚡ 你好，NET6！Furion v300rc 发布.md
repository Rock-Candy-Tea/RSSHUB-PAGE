
---
title: '⚡ 你好，.NET6！Furion v3.0.0.rc 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5d0792ed8d4a6fa8ccd481ea58d0d422d9c.png'
author: 开源中国
comments: false
date: Fri, 20 Aug 2021 14:30:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5d0792ed8d4a6fa8ccd481ea58d0d422d9c.png'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p>自 2020年09月01日 写下第一行代码直至今日已临近 1 周年，<strong>Furion 从 .NET5 出发，但不止步于此。</strong></p> 
</blockquote> 
<p>自 2021年05月26日 微软正式发布 .NET 6 Preview 4 版本起，<strong>Furion 就着手开发基于 .NET6 版本框架开发，完全采用最新的 C#9 - C#10 编写整个框架代码，同时保持和 .NET5 版本功能代码高度同步。</strong></p> 
<p><span style="color:#d35400"><strong>截至 2021年08月20日，Furion 基于 .NET 6 Preview 7 和 C#10 完成了所有 .NET5 版本功能代码，实现了100%的功能兼容，另外提供了  Furion.Upgrade.NET6 全自动化升级工具。</strong></span></p> 
<h3>Furion.Upgrade.NET6</h3> 
<p>Furion.Upgrade.NET6 是 Furion 推出的自动化升级工具，可以<strong>自动化实现无错误将 Furion v2（.NET5）版本代码升级到 Furion v3（.NET6）</strong>。</p> 
<p><strong>开发者可放心安心升级，没有任何升级和迁移成本。保证每一个 Furion 用户都能从旧版本升级到未来版本。</strong></p> 
<p><img height="647" src="https://oscimg.oschina.net/oscnet/up-5d0792ed8d4a6fa8ccd481ea58d0d422d9c.png" width="960" referrerpolicy="no-referrer"></p> 
<p><img height="797" src="https://oscimg.oschina.net/oscnet/up-0a237e508823ce547ecd22a282e949dce2b.png" width="960" referrerpolicy="no-referrer"></p> 
<p><img height="677" src="https://oscimg.oschina.net/oscnet/up-03b39431a358ad69394a76fa4da677f6782.png" width="960" referrerpolicy="no-referrer"></p> 
<p><img height="528" src="https://oscimg.oschina.net/oscnet/up-a7041fd0b8a1698effd9467387a3313b216.png" width="960" referrerpolicy="no-referrer"></p> 
<p><img height="729" src="https://oscimg.oschina.net/oscnet/up-926ea4b0377cb5cae59a42ca36116563156.png" width="960" referrerpolicy="no-referrer"></p> 
<p><img height="770" src="https://oscimg.oschina.net/oscnet/up-f6144b7c28ce6d345dc41a8b427a3b3475e.png" width="960" referrerpolicy="no-referrer"></p> 
<h2>新旧版本显著对比</h2> 
<h4><span style="color:#3498db"><strong>1. 初始化 Program.cs 对比</strong></span></h4> 
<p>.NET5 版本：</p> 
<pre><code class="language-cs">using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;

namespace Furion.Web.Entry
&#123;
    public class Program
    &#123;
        public static void Main(string[] args)
        &#123;
            CreateHostBuilder(args).Build().Run();
        &#125;

        public static IHostBuilder CreateHostBuilder(string[] args)
        &#123;
            return Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                &#123;
                    webBuilder.Inject()
                              .UseStartup<Startup>();
                &#125;);
        &#125;
    &#125;
&#125;</code></pre> 
<p><strong>.NET6 版本：</strong></p> 
<pre><code class="language-cs">var builder = WebApplication.CreateBuilder(args).Inject();
var app = builder.Build();
app.Run();</code></pre> 
<p>你没看错，这就是 C#10 的语法，支持顶级命名空间写法。</p> 
<h4><span style="color:#3498db">2. 无 Startup.cs 化</span></h4> 
<p>.NET5 版本：</p> 
<pre><code class="language-cs">using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;

namespace Furion.Web.Entry
&#123;
    public class Startup
    &#123;
        public void ConfigureServices(IServiceCollection services)
        &#123;
            // 代码迁移至 Furion.Web.Core/Startup.cs
        &#125;

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        &#123;
            // 代码迁移至 Furion.Web.Core/Startup.cs
        &#125;
    &#125;
&#125;</code></pre> 
<p><strong>.NET6 版本：</strong></p> 
<p>无需创建 Startup.cs 类</p> 
<h4><span style="color:#3498db">3. 更精简的代码结构</span></h4> 
<p>.NET5 版本：</p> 
<pre><code class="language-cs">﻿using Furion.DynamicApiController;

namespace FurionApi.Application
&#123;
    public class SystemAppService : IDynamicApiController
    &#123;
        private readonly ISystemService _systemService;
        public SystemAppService(ISystemService systemService)
        &#123;
            _systemService = systemService;
        &#125;

        public string GetDescription()
        &#123;
            return _systemService.GetDescription();
        &#125;
    &#125;
&#125;</code></pre> 
<p><strong>.NET6 版本：</strong></p> 
<pre><code class="language-cs">using Furion.DynamicApiController;

namespace FurionApi.Application;

public class SystemAppService : IDynamicApiController
&#123;
    private readonly ISystemService _systemService;
    public SystemAppService(ISystemService systemService)
    &#123;
        _systemService = systemService;
    &#125;

    public string GetDescription()
    &#123;
        return _systemService.GetDescription();
    &#125;
&#125;</code></pre> 
<p>无需 using 常用命名空间，同时命名空间可独占一行，无需包裹类定义。</p> 
<h2>.NET6 版本源码</h2> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/dotnetchina/Furion/tree/net6-dev/">https://gitee.com/dotnetchina/Furion/tree/net6-dev/</a></li> 
 <li>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Ftree%2Fnet6-dev%2F" target="_blank">https://github.com/MonkSoul/Furion/tree/net6-dev/</a></li> 
</ul> 
<h2>文档手册</h2> 
<p><a href="https://dotnetchina.gitee.io/furion/">https://dotnetchina.gitee.io/furion/</a></p>
                                        </div>
                                      
</div>
            