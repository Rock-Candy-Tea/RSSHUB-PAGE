
---
title: '🔥 Furion v3.7.2 发布，再也不用手写前端 Ajax 了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f47d09c730429e108219ef3178396748787.png'
author: 开源中国
comments: false
date: Thu, 30 Jun 2022 12:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f47d09c730429e108219ef3178396748787.png'
---

<div>   
<div class="content">
                                                                                            <h2>极速效率</h2> 
<p>这个版本最大的亮点就是<span style="color:#d35400"><strong>新增了 WebAPI 自动生成 Vue2+，React，Angular 三大框架的 Ajax 请求代码，以后再也不用自己手写 Ajax ，开发效率至少提高 50%+，给前端程序员减负。</strong></span></p> 
<p><span style="color:#2980b9"><strong>另外添加了 JSON Schema 支持，在任何主流的 IDE 中都支持配置智能补全和验证。</strong></span></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-f47d09c730429e108219ef3178396748787.png" width="1914" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-5c74d49cd22df60ff862c46c6a070be5651.png" width="1918" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-10c44c7e8b288baf9235caa9db88473853a.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-5df93248291a10165530ee02f99843930e2.png" width="1917" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span>跨域<span> </span><code>WithExposedHeaders</code><span> </span>默认配置<span> </span><code>access-token</code><span> </span>和<span> </span><code>x-access-token</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/42ebdfd33a01353a0b3a801528de052990d2e4c9" target="_blank">42ebdfd</a></li> 
    <li>[新增]<span> </span>脚手架默认启用<span> </span><code>app.UseHttpLogging()</code><span> </span><code>HTTP</code><span> </span>日志<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/42ebdfd33a01353a0b3a801528de052990d2e4c9" target="_blank">42ebdfd</a></li> 
    <li>[新增]<span> </span><strong><code>Furion</code><span> </span>和<span> </span><code>ASP.NET Core</code><span> </span>完整<span> </span><code>json</code><span> </span>配置的<span> </span><code>JSON Schema</code><span> </span>架构<span> </span><a href="https://gitee.com/dotnetchina/Furion/raw/net6/schemas/v3/furion-schema.json" target="_blank">JSON Schema</a></strong></li> 
    <li>[新增]<span> </span><code>Sql</code><span> </span>代理支持返回单个类类型参数<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/1d7fb5b5330c5a30098056818a93a0879034fecd" target="_blank">1d7fb5b</a></li> 
    <li>[新增]<span> </span><code>Sql</code><span> </span>代理支持返回<span> </span><code>ValueTuple</code><span> </span>单个类类型参数<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/876a2f5f7e2d07fa3bbc3f5b99c0653893e0ada8" target="_blank">876a2f5</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span><strong><code>Furion</code><span> </span>和<span> </span><code>ASP.NET Core</code><span> </span>完整<span> </span><code>json</code><span> </span>配置的<span> </span><code>JSON Schema</code><span> </span>架构<span> </span><a href="https://gitee.com/dotnetchina/Furion/raw/net6/schemas/v3/furion-schema.json" target="_blank">JSON Schema</a></strong></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[修复]<span> </span>自<span> </span><code>v3.6.3</code><span> </span>版本依赖，执行原生<span> </span><code>Sql</code><span> </span>添加了参数校验导致存储过程执行错误问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5ERMQ" target="_blank">#I5ERMQ</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[调整]<span> </span>脚手架所有<span> </span><code>.json</code><span> </span>文件，默认添加<span> </span><code>JSON Schema</code><span> </span>支持</li> 
   </ul> </li> 
  <li> <p><strong>文档</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span><code>Vue/React/Angular</code><span> </span>请求代理文档</li> 
    <li>[新增]<span> </span><code>JSON Schema</code><span> </span>文档，支持配置智能提示和验证</li> 
    <li>[更新]<span> </span>跨域文档、规范化文档、配置文档、日志文档</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2>本期亮点</h2> 
<ol style="margin-left:0; margin-right:0"> 
 <li><strong>新增<span> </span><code>JSON Schema</code><span> </span>支持，所有<span> </span><code>.json</code><span> </span>文件支持智能提示和验证</strong></li> 
</ol> 
<pre><code class="language-json">&#123;
  "$schema": "https://gitee.com/dotnetchina/Furion/raw/net6/schemas/v3/furion-schema.json",

  "Logging": &#123;
    "LogLevel": &#123;
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.Hosting.Lifetime": "Information",
      "Microsoft.EntityFrameworkCore": "Information",
      "Microsoft.AspNetCore.HttpLogging.HttpLoggingMiddleware": "Information"
    &#125;
  &#125;,
  "AllowedHosts": "*"
&#125;</code></pre> 
<p><img src="https://dotnetchina.gitee.io/furion/img/js1.png" referrerpolicy="no-referrer"></p> 
<ol start="2" style="margin-left:0; margin-right:0"> 
 <li><strong>根据<span> </span><code>Swagger</code><span> </span>生成<span> </span><code>Vue/React/Angular</code><span> </span>前端请求代码</strong></li> 
</ol> 
<p><img src="https://dotnetchina.gitee.io/furion/img/sg6.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://dotnetchina.gitee.io/furion/img/sg8.png" referrerpolicy="no-referrer"></p> 
<ol start="3" style="margin-left:0; margin-right:0"> 
 <li><strong><code>Sql</code><span> </span>代理支持返回单个类类型参数</strong></li> 
</ol> 
<pre><code class="language-cs">public interface ISql : ISqlDispatchProxy
&#123;
    // 集合类型
    [SqlExecute("select * from person")]
    List<Person> GetPersons();

    // 自 v3.7.2+ 版本支持返回单个类类型参数
    [SqlExecute("select * from person where id=@id")]
    Person GetPerson(int id);
&#125;</code></pre> 
<pre><code class="language-cs">public interface ISql : ISqlDispatchProxy
&#123;
    [SqlExecute(@"
            select * from person where id =@id;
            select * from person")]
    (Person, List<Person>) GetData(int id); // 注意返回值是 `(Person, List<Person>)` 组合
&#125;</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            