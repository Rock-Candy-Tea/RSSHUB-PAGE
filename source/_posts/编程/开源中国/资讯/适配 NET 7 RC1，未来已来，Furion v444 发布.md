
---
title: '适配 .NET 7 RC1，未来已来，Furion v4.4.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5963f799240eeb2c63f6f4e25ad1695a8ad.png'
author: 开源中国
comments: false
date: Thu, 15 Sep 2022 05:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5963f799240eeb2c63f6f4e25ad1695a8ad.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:center"><span style="color:#e67e22">.NET 未来已来，你来不来？！</span></h2> 
<h2>重新起航</h2> 
<blockquote> 
 <div style="text-align:start">
  不忘初心，感恩遇见，感恩信任
 </div> 
 <div style="text-align:start">
   
 </div> 
 <div style="text-align:start"> 
  <p style="margin-left:0; margin-right:0">2020 年 09 月 01 日，一个叫<span> </span><code>Fur</code><span> </span>的开源项目在<span> </span><code>Gitee</code><span> </span>的襁褓中悄然诞生，她的出生仿佛带着某种使命，没有包袱，无限可能。</p> 
  <p style="margin-left:0; margin-right:0">她缓缓的张开双眼，干净雪亮的眼睛似乎对这个世界充满了好奇，任何事物在她眼前晃过都像是直击灵魂的思想碰撞，这些在她看来都是非常宝贵的财富。她貌似有用不完的精力，一路汲取知识，升级打怪，不断奔跑，乐此不疲。</p> 
  <p style="margin-left:0; margin-right:0">记得 2020 年 11 月 11 日的单身节，她迎来了“一岁（v1.0.0）”生日，自那以后，IT 这个大银幕上频繁出现她的身影，越来越多<span> </span><code>.NET5</code><span> </span>开发者转粉，像是告诉这个世界，她就是 IT 界大明星。</p> 
  <p style="margin-left:0; margin-right:0">每一个明星都有一个好听的艺名，她当然也不例外，2020 年 11 月 20 日，经纪人百小僧为她起名为<span> </span><code>Furion</code>。</p> 
  <p style="margin-left:0; margin-right:0">2021 年 11 月 09 日起，她进入了每个孩子都经历过的叛逆期，年少轻狂喜新厌旧，抛弃了曾经支持她的<span> </span><code>.NET5</code><span> </span>粉丝们，投入到新的<span> </span><code>.NET6</code><span> </span>拥趸者怀抱中，自此过上了奢靡富足的生活。</p> 
  <p style="margin-left:0; margin-right:0">但她过的不开心，时常在夜里想起<span> </span><code>.NET5</code><span> </span>的粉丝们，内心非常自责，但在双重工作压力下她毅然选择了忽视他们的诉求，仿佛他们就是累赘。</p> 
  <p style="margin-left:0; margin-right:0">时间真的是好东西，曾经认为是对的，经过岁月的蹉跎历磨，渐渐的明白：不忘初心，方能始终。</p> 
  <p>这一次，不落下一人（<code>.NET5</code>，<code>.NET6</code>，...，<code>.NET N</code>），携手共进，重新起航，感恩遇见，感恩信任。</p> 
 </div> 
</blockquote> 
<hr> 
<h2>项目信息</h2> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion" target="_blank">https://github.com/MonkSoul/Furion</a></li> 
 <li>文档：<a href="https://dotnetchina.gitee.io/furion/">https://dotnetchina.gitee.io/furion</a></li> 
</ul> 
<hr> 
<h2>准备工作</h2> 
<p>早就在 .NET7 发布 Preview 版本的时候，Furion 团队就着实进行适配，前前后后耗时4个多月解决了 .NET5 升级到 .NET6、.NET7 的所有问题，<strong>保证一套代码兼容 .NET5+，支持现有的所有 Furion 版本升级，包括 0.x，1.x，2.x，3.x 版本。</strong></p> 
<p>在适配 .NET7 过程中主要参考微软提供了两篇文档：</p> 
<ul> 
 <li><strong>ASP.NET Core 7 新增功能：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Faspnet%2Fcore%2Frelease-notes%2Faspnetcore-7.0%3Fview%3Daspnetcore-7.0" target="_blank">https://docs.microsoft.com/zh-cn/aspnet/core/release-notes/aspnetcore-7.0?view=aspnetcore-7.0</a></strong></li> 
 <li><strong>EntityFramework 7 新增功能：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fef%2Fcore%2Fwhat-is-new%2Fef-core-7.0%2Fwhatsnew" target="_blank">https://docs.microsoft.com/zh-cn/ef/core/what-is-new/ef-core-7.0/whatsnew</a></strong></li> 
</ul> 
<p><img height="720" src="https://oscimg.oschina.net/oscnet/up-5963f799240eeb2c63f6f4e25ad1695a8ad.png" width="1235" referrerpolicy="no-referrer"></p> 
<p><img height="901" src="https://oscimg.oschina.net/oscnet/up-4c4df37aec861d357f0415d8caee7268519.png" width="1158" referrerpolicy="no-referrer"></p> 
<hr> 
<h2>文档更新</h2> 
<ul> 
 <li>文档地址： <a href="https://dotnetchina.gitee.io/furion/">https://dotnetchina.gitee.io/furion/</a></li> 
</ul> 
<h2>1. 内置强大实时的本地搜索</h2> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-f6ae314f5f28697722843ddf6557d3057dd.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3>2. 添加升级或集成 .NET7 的文档</h3> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-e02f1cec4799307b48eb30b92a16742f1e8.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3>3. 改进更新日志模板规范</h3> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-af3f0070eaffd0af9daa575b6e1c2bbc68d.png" width="1920" referrerpolicy="no-referrer"></p> 
<hr> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li><code>v4.4.4</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5R5TI">https://gitee.com/dotnetchina/Furion/issues/I5R5TI</a></li> 
  <li><code>v4.4.3</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5QVH3">https://gitee.com/dotnetchina/Furion/issues/I5QVH3</a></li> 
  <li><code>v4.4.2</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5QDHX">https://gitee.com/dotnetchina/Furion/issues/I5QDHX</a></li> 
  <li><code>v4.4.1</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5Q3SX">https://gitee.com/dotnetchina/Furion/issues/I5Q3SX</a></li> 
  <li><code>v4.4.0</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5PQHR">https://gitee.com/dotnetchina/Furion/issues/I5PQHR</a></li> 
 </ul> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 新增友好异常可控制是否输出错误日志配置<span> </span><code>LogError: true</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PKJH">#I5PKJH</a></li> 
    <li>[新增]<span> </span><code>DateOnlyJsonConverter</code><span> </span>和<span> </span><code>DateOnlyOffsetJsonConverter</code><span> </span>序列化转换器<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/565">!565</a></li> 
    <li>[新增] 事件总线<span> </span><code>LogEnabled</code><span> </span>配置，可控制是否输出服务日志<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QLY5">#I5QLY5</a></li> 
    <li>[新增]<span> </span><strong>可实现任何多套规范化结果功能，支持特定控制器，特定方法</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QZ37">#I5QZ37</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[支持]<span> </span><strong><code>.NET 6.0.9</code><span> </span>和<span> </span><code>.NET 7.0 RC1</code></strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/be5b4098bae2153f8d49cf9797e454afde0d0aab">be5b40</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/1eee77bff0954336dcc5402a09a3195667bb80f2">1eee77b</a></li> 
    <li>[调整] 远程请求<span> </span><code>.SetBodyBytes</code><span> </span>为<span> </span><code>.SetFiles</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PMS5">#I5PMS5</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PIYI">#I5PIYI</a></li> 
    <li>[移除] 远程请求<span> </span><code>[BodyBytes]</code><span> </span>设计，采用<span> </span><code>HttpFile</code><span> </span>方式<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PMS5">#I5PMS5</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PIYI">#I5PIYI</a></li> 
    <li>[调整] 所有的<span> </span><code>AddInject</code><span> </span>和<span> </span><code>UseInject</code><span> </span>参数设计<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QCF0">#I5QCF0</a></li> 
    <li>[调整]<span> </span><strong>远程请求所有<span> </span><code>xxxAsStreamAsync</code><span> </span>返回值</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QVEB">#I5QVEB</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 远程请求代理模式非泛型参数导致数组溢出问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5Q3SN">#I5Q3SN</a></li> 
    <li>[修复]<span> </span><code>LoggingMonitor</code><span> </span>客户端<span> </span><code>IP</code><span> </span>记录错误<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QCU1">#I5QCU1</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/562">!562</a></li> 
    <li>[修复] 远程请求响应报文中包含<span> </span><code>charset=gbk</code><span> </span>进行序列化后乱码问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QVEB">#I5QVEB</a></li> 
    <li>[修复] 文件日志断电时丢失日志问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/db7d51bba569001bc363727a6683ab3f31c3fc1d">db7d51b</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[调整]<span> </span><code>JWTEncryption</code><span> </span>静态类，支持无需注册<span> </span><code>services.AddJwt()</code><span> </span>使用<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PPKE">#I5PPKE</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5POLZ">#I5POLZ</a></li> 
    <li>[调整] 事件总线默认日志类名为<span> </span><code>System.Logging.EventBusService</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QLY5">#I5QLY5</a></li> 
   </ul> </li> 
  <li> <p><strong>文档</strong></p> 
   <ul> 
    <li>[新增]<span> </span><code>.NET6</code><span> </span>升级<span> </span><code>.NET7</code><span> </span>文档</li> 
    <li>[新增]<span> </span><code>ASP.NET 7</code><span> </span>集成文档</li> 
    <li>[更新] 友好异常文档、远程请求文档、依赖注入文档、即时通讯文档、事件总线文档、Worker Service 文档、单元测试文档、入门指南文档</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2>本期亮点</h2> 
<h3>1. 文档支持全文搜索、模糊搜索、代码搜索、搜索高亮</h3> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-693157867d6aef2d39a90d75c4862cba9c6.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3>2. 远程请求第三方 API 上传文件更加易用</h3> 
<p><strong>代理模式</strong></p> 
<pre><code class="language-cs">public interface IHttp : IHttpDispatchProxy
&#123;
    [Post("https://www.furion.icu/upload", ContentType = "multipart/form-data")] 
    Task<HttpResponseMessage> PostXXXAsync(HttpFile file);

    // 支持多个文件
    [Post("https://www.furion.icu/upload", ContentType = "multipart/form-data")] 
    Task<HttpResponseMessage> PostXXXAsync(HttpFile[] files);
    
    // 支持多个文件
    [Post("https://www.furion.icu/upload", ContentType = "multipart/form-data")] 
    Task<HttpResponseMessage> PostXXXAsync(IList<HttpFile> files);
&#125;</code></pre> 
<p><strong>字符串模式</strong></p> 
<pre><code class="language-cs">var bytes = File.ReadAllBytes("image.png");

// 单个文件
var result = await "https://localhost:44316/api/test-module/upload-file"
                      .SetContentType("multipart/form-data")
                      .SetFiles(HttpFile.Create("file", bytes, "image.png")).PostAsync();

// 多个文件
var result = await "https://localhost:44316/api/test-module/upload-muliti-file"
                      .SetContentType("multipart/form-data")
                      .SetFiles(HttpFile.CreateMultiple("files", (bytes, "image1.png"), (bytes, "image2.png"))).PostAsync();</code></pre> 
<h3>3. 简化框架初始配置参数签名</h3> 
<pre><code class="language-cs">public void ConfigureServices(IServiceCollection services)
&#123;
    services.AddInject(options =>
    &#123;
        options.ConfigureSwaggerGen(gen => 
        &#123;
            // ...
        &#125;);
    &#125;);
&#125;</code></pre> 
<pre><code class="language-cs"> public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
 &#123;
      app.UseInject(configure: options =>
      &#123;
          options.ConfigureSwagger(swg => 
          &#123;
              // ...
          &#125;);

          options.ConfigureSwaggerUI(ui =>
          &#123;
             // ...
          &#125;);
      &#125;);
&#125;</code></pre> 
<h2>4. 支持多套接口规范化处理</h2> 
<pre><code class="language-cs">// 替换默认的
services.AddUnifyProvider<SpeciallyResultProvider>();

// 添加更多规范化配置
services.AddUnifyProvider<SpeciallyResultProvider>("unique_name");</code></pre> 
<pre><code class="language-cs">[UnifyProvider]    // 默认的（不贴也是默认的）
public class FurionAppService: IDynamicApiController
&#123;
&#125;

[UnifyProvider("specially")]    // 自定义的
public class FurionAppService: IDynamicApiController
&#123;
&#125;


[UnifyProvider]    // 默认的
public class FurionAppService: IDynamicApiController
&#123;
    [UnifyProvider("specially")] // 复写默认的
    public string GetName()
    &#123;
    &#125;
&#125;</code></pre>
                                        </div>
                                      
</div>
            