
---
title: '学 .NET 从 Furion 开始，v3.1.4 发布，安装量破 231 万'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://dotnetchina.gitee.io/furion/img/furionlogo.png'
author: 开源中国
comments: false
date: Thu, 14 Apr 2022 15:48:00 GMT
thumbnail: 'https://dotnetchina.gitee.io/furion/img/furionlogo.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:center"><img height="80" src="https://dotnetchina.gitee.io/furion/img/furionlogo.png" referrerpolicy="no-referrer"></p> 
<div style="text-align:center"> 
 <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/dotnetchina/Furion/stargazers" target="_blank"><img alt="star" src="https://gitee.com/dotnetchina/Furion/badge/star.svg?theme=gvp" referrerpolicy="no-referrer"></a><span> </span><a href="https://gitee.com/dotnetchina/Furion/members" target="_blank"><img alt="fork" src="https://gitee.com/dotnetchina/Furion/badge/fork.svg?theme=gvp" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fstargazers" target="_blank"><img alt="GitHub stars" src="https://img.shields.io/github/stars/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fnetwork" target="_blank"><img alt="GitHub forks" src="https://img.shields.io/github/forks/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fblob%2Fmain%2FLICENSE" target="_blank"><img alt="GitHub license" src="https://img.shields.io/badge/license-MulanPSL--2.0-orange" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></p> 
</div> 
<div style="text-align:center"> 
 <p style="margin-left:0; margin-right:0">让 .NET 开发更简单，更通用，更流行。</p> 
</div> 
<h2 style="text-align:start">💐 序言<a href="https://dotnetchina.gitee.io/furion/docs#-%E5%BA%8F%E8%A8%80">​</a></h2> 
<blockquote> 
 <p>无私奉献不是天方夜谭，有时候，我们也可以做到。</p> 
</blockquote> 
<h2 style="text-align:start">🍕 名字的由来<a href="https://dotnetchina.gitee.io/furion/docs#-%E5%90%8D%E5%AD%97%E7%9A%84%E7%94%B1%E6%9D%A5">​</a></h2> 
<blockquote> 
 <p>故事是这样子的：</p> 
 <p style="margin-left:0; margin-right:0">自微软宣布<span> </span><code>.NET 5</code><span> </span>平台消息之后，就琢磨着开发一个基于<span> </span><code>.NET 5</code><span> </span>平台的开发框架，想做第一个吃<span> </span><code>.NET 5</code><span> </span>螃蟹尝鲜之人。</p> 
 <p style="margin-left:0; margin-right:0">一开始想到了<span> </span><code>Lazier</code><span> </span>作为框架的名称，中文有<span> </span><strong>更懒</strong><span> </span>的意思。符合我的 “一切从简，只为了更懒” 的开发理念。</p> 
 <p style="margin-left:0; margin-right:0">但是<span> </span><strong>更懒</strong><span> </span>和<span> </span><strong>更烂</strong><span> </span>中文读音相近且没有特色，而且寓意也不是很好，对此换名问题苦恼了好些天。</p> 
 <p style="margin-left:0; margin-right:0">刚好有一次在 QQ 群中无意间刷到了群友发的<span> </span><strong>“先知”</strong><span> </span>单词：<strong>“<code>Furion [fu:rɪən]</code>”</strong>，就那一刻，就认定它了！</p> 
 <p><code>Furion</code><span> </span>中文有<span> </span><code>先知</code><span> </span>的意思，恰好符合我创造框架的初衷。所以，<strong><code>Furion</code></strong><span> </span>就诞生了。</p> 
</blockquote> 
<h2 style="text-align:start">🍟 文档地址<a href="https://dotnetchina.gitee.io/furion/docs#-%E6%96%87%E6%A1%A3%E5%9C%B0%E5%9D%80">​</a></h2> 
<ul> 
 <li>国内文档：<a href="https://dotnetchina.gitee.io/furion" target="_blank">https://dotnetchina.gitee.io/furion</a></li> 
 <li>国外文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffurion.icu%2F" target="_blank">https://furion.icu</a></li> 
</ul> 
<h2 style="text-align:start">🌭 开源地址<a href="https://dotnetchina.gitee.io/furion/docs#-%E5%BC%80%E6%BA%90%E5%9C%B0%E5%9D%80">​</a></h2> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/dotnetchina/Furion" target="_blank">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmonksoul%2FFurion" target="_blank">https://github.com/monksoul/Furion</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank">https://www.nuget.org/packages/Furion</a></li> 
</ul> 
<h2 style="text-align:start">🥥 框架拓展包<a href="https://dotnetchina.gitee.io/furion/docs#-%E6%A1%86%E6%9E%B6%E6%8B%93%E5%B1%95%E5%8C%85">​</a></h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; border-collapse:collapse; box-sizing:border-box; color:#1c1e21; display:block; font-family:system-ui,-apple-system,"Segoe UI",Roboto,Ubuntu,Cantarell,"Noto Sans",sans-serif,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:var(--ifm-spacing-vertical); orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th style="background-color:var(--ifm-table-head-background)">包类型</th> 
   <th style="background-color:var(--ifm-table-head-background)">名称</th> 
   <th style="background-color:var(--ifm-table-head-background)">版本</th> 
   <th style="background-color:var(--ifm-table-head-background)">描述</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-blue?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion 核心包</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Pure" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-blue?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Pure</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Pure" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Pure.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion 纯净版包（不含 EFCore）</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.Authentication.JwtBearer" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-blue?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Extras.Authentication.JwtBearer</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.Authentication.JwtBearer" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Extras.Authentication.JwtBearer.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion Jwt 拓展包</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.DependencyModel.CodeAnalysis" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-blue?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Extras.DependencyModel.CodeAnalysis</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.DependencyModel.CodeAnalysis" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Extras.DependencyModel.CodeAnalysis.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion CodeAnalysis 拓展包</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.ObjectMapper.Mapster" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-blue?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Extras.ObjectMapper.Mapster</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.ObjectMapper.Mapster" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Extras.ObjectMapper.Mapster.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion Mapster 拓展包</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.DatabaseAccessor.SqlSugar" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-blue?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Extras.DatabaseAccessor.SqlSugar</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.DatabaseAccessor.SqlSugar" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Extras.DatabaseAccessor.SqlSugar.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion SqlSugar 拓展包</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.DatabaseAccessor.Dapper" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-blue?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Extras.DatabaseAccessor.Dapper</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.DatabaseAccessor.Dapper" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Extras.DatabaseAccessor.Dapper.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion Dapper 拓展包</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.DatabaseAccessor.MongoDB" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-blue?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Extras.DatabaseAccessor.MongoDB</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.DatabaseAccessor.MongoDB" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Extras.DatabaseAccessor.MongoDB.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion MongoDB 拓展包</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.Logging.Serilog" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-blue?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Extras.Logging.Serilog</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Extras.Logging.Serilog" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Extras.Logging.Serilog.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion Serilog 拓展包</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Tools.CommandLine" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-blue?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Tools.CommandLine</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Tools.CommandLine" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Tools.CommandLine.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion Tools 命令行参数解析</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:start">🍄 框架脚手架<a href="https://dotnetchina.gitee.io/furion/docs#-%E6%A1%86%E6%9E%B6%E8%84%9A%E6%89%8B%E6%9E%B6">​</a></h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; border-collapse:collapse; box-sizing:border-box; color:#1c1e21; display:block; font-family:system-ui,-apple-system,"Segoe UI",Roboto,Ubuntu,Cantarell,"Noto Sans",sans-serif,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:var(--ifm-spacing-vertical); orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th style="background-color:var(--ifm-table-head-background)">模板类型</th> 
   <th style="background-color:var(--ifm-table-head-background)">名称</th> 
   <th style="background-color:var(--ifm-table-head-background)">版本</th> 
   <th style="background-color:var(--ifm-table-head-background)">描述</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.Mvc%2F" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-yellow?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Template.Mvc</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.Mvc%2F" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Template.Mvc.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Mvc 模板</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.Api%2F" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-yellow?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Template.Api</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.Api%2F" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Template.Api.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">WebApi 模板</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.App%2F" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-yellow?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Template.App</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.App%2F" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Template.App.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Mvc/WebApi 模板</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.Razor%2F" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-yellow?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Template.Razor</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.Razor%2F" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Template.Razor.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">RazorPages 模板</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.RazorWithWebApi%2F" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-yellow?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Template.RazorWithWebApi</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.RazorWithWebApi%2F" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Template.RazorWithWebApi.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">RazorPages/WebApi 模板</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.Blazor%2F" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-yellow?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Template.Blazor</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.Blazor%2F" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Template.Blazor.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Blazor 模板</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.BlazorWithWebApi%2F" target="_blank"><img alt="nuget" src="https://shields.io/badge/-Nuget-yellow?cacheSeconds=604800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Furion.Template.BlazorWithWebApi</td> 
   <td style="border-style:solid"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion.Template.BlazorWithWebApi%2F" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.Template.BlazorWithWebApi.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></td> 
   <td style="border-style:solid">Blazor/WebApi 模板</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#1c1e21; text-align:start"><strong><a href="https://dotnetchina.gitee.io/furion/docs/template" target="_blank">如何使用脚手架</a></strong></p> 
<h2 style="text-align:start">🍎 框架特点<a href="https://dotnetchina.gitee.io/furion/docs#-%E6%A1%86%E6%9E%B6%E7%89%B9%E7%82%B9">​</a></h2> 
<ul> 
 <li>全新面貌：基于<span> </span><code>.NET5/6</code><span> </span>平台，没有历史包袱</li> 
 <li>极少依赖：框架只依赖两个第三方包</li> 
 <li>极易入门：只需要一个<span> </span><code>Inject()</code><span> </span>即可完成配置</li> 
 <li>极速开发：内置丰富的企业应用开发功能</li> 
 <li>极其灵活：轻松面对多变复杂的需求</li> 
 <li>极易维护：采用独特的架构思想，只为长久维护设计</li> 
 <li>完整文档：提供完善的开发文档</li> 
 <li><strong>跨全平台：支持所有主流操作系统及 .NET 全部项目类型</strong></li> 
</ul> 
<h2 style="text-align:start">🥝 功能模块<a href="https://dotnetchina.gitee.io/furion/docs#-%E5%8A%9F%E8%83%BD%E6%A8%A1%E5%9D%97">​</a></h2> 
<p><img height="1294" src="https://oscimg.oschina.net/oscnet/up-34efd9e2dc96deeb335e12457ec1e3b09fe.png" width="1112" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">🥐 框架依赖<a href="https://dotnetchina.gitee.io/furion/docs#-%E6%A1%86%E6%9E%B6%E4%BE%9D%E8%B5%96">​</a></h2> 
<p style="color:#1c1e21; text-align:start"><code>Furion</code><span> </span>为了追求极速入门，极致性能，尽可能的不使用或减少第三方依赖。目前<span> </span><code>Furion</code><span> </span>仅集成了以下两个依赖：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMiniProfiler%2Fdotnet" target="_blank">MiniProfiler</a>：性能分析和监听必备</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdomaindrivendev%2FSwashbuckle.AspNetCore" target="_blank">Swashbuckle</a>：<code>Swagger</code><span> </span>接口文档</li> 
</ul> 
<p style="color:#1c1e21; text-align:start">麻雀虽小五脏俱全。<code>Furion</code><span> </span>即使只集成了这两个依赖，但是主流的<span> </span><code>依赖注入/控制反转</code>，<code>AOP</code><span> </span>面向切面编程，<code>事件总线</code>，<code>数据验证</code>，<code>数据库操作</code><span> </span>等等一个都不少。</p> 
<h2 style="text-align:start">🥗 环境要求<a href="https://dotnetchina.gitee.io/furion/docs#-%E7%8E%AF%E5%A2%83%E8%A6%81%E6%B1%82">​</a></h2> 
<ul> 
 <li>Visual Studio 2019 16.8 +</li> 
 <li>.NET 5 SDK +</li> 
 <li>.Net Standard 2.1 +</li> 
</ul> 
<h2 style="text-align:start">🥪 支持平台<a href="https://dotnetchina.gitee.io/furion/docs#-%E6%94%AF%E6%8C%81%E5%B9%B3%E5%8F%B0">​</a></h2> 
<ul> 
 <li>运行环境 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Windows</li> 
   <li>Linux</li> 
   <li>MacOS/MacOS M1 CPU</li> 
   <li>Docker/K8S/K3S/Rancher</li> 
   <li>Xamarin/MAUI</li> 
  </ul> </li> 
 <li>数据库 
  <ul style="margin-left:0; margin-right:0"> 
   <li>SqlServer</li> 
   <li>Sqlite</li> 
   <li>Azure Cosmos</li> 
   <li>MySql</li> 
   <li>MariaDB</li> 
   <li>PostgreSQL</li> 
   <li>InMemoryDatabase</li> 
   <li>Oracle</li> 
   <li>Firebird</li> 
   <li>达梦数据库</li> 
   <li>MongoDB</li> 
  </ul> </li> 
 <li>应用部署 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Kestrel</li> 
   <li>Nginx</li> 
   <li>Jexus</li> 
   <li>IIS</li> 
   <li>Apache</li> 
   <li>PM2</li> 
   <li>Supervisor</li> 
   <li>独立发布/单文件</li> 
   <li>容器（Docker/K8S/K3S/Rancher）</li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:start">🍖 关于性能<a href="https://dotnetchina.gitee.io/furion/docs#-%E5%85%B3%E4%BA%8E%E6%80%A7%E8%83%BD">​</a></h2> 
<p style="color:#1c1e21; text-align:start"><code>Furion</code><span> </span>目前采用<span> </span><code>Visual Studio 2019 16.8</code><span> </span>自带性能测试和<span> </span><code>JMeter</code><span> </span>进行测试，由于篇幅有限，只贴部分测试图，测试结果如下：</p> 
<p><img src="https://dotnetchina.gitee.io/furion/img/xncs.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">🌴 Stars 趋势图<a href="https://dotnetchina.gitee.io/furion/docs#-stars-%E8%B6%8B%E5%8A%BF%E5%9B%BE">​</a></h2> 
<p><img height="300" src="https://oscimg.oschina.net/oscnet/up-7768ba0ffd98d2032d596d6e06404421249.png" width="900" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">🍻 贡献代码<a href="https://dotnetchina.gitee.io/furion/docs#-%E8%B4%A1%E7%8C%AE%E4%BB%A3%E7%A0%81">​</a></h2> 
<p style="color:#1c1e21; text-align:start"><code>Furion</code><span> </span>遵循<span> </span><a href="https://gitee.com/dotnetchina/Furion/blob/net6/LICENSE" target="_blank">MulanPSL-2.0</a><span> </span>开源协议，欢迎大家提交<span> </span><code>PR</code><span> </span>或<span> </span><code>Issue</code>。</p> 
<p style="color:#1c1e21; text-align:start">如果要为项目做出贡献，请查看<span> </span><a href="https://dotnetchina.gitee.io/furion/docs/contribute">贡献指南</a>。感谢每一位为<span> </span><code>Furion</code><span> </span>贡献代码的朋友。</p> 
<h2>💖本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p style="margin-left:0; margin-right:0"><strong>新特性</strong></p> 
   <ul> 
    <li>[新增]<span> </span><code>IFormFile</code><span> </span>拓展方法<span> </span><code>ToByteArray()</code></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>突破性变化</strong></p> 
   <ul> 
    <li>[更新] 所有依赖包至最新版</li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复]<span> </span><code>Swagger</code><span> </span>的<span> </span><code>schema</code><span> </span>类型如果是<span> </span><code>C# Object</code><span> </span>类型无法正确生成前端代码问题<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fswagger-api%2Fswagger-codegen-generators%2Fissues%2F692">Swagger 官方 Issue</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/1a252747fd60fc87a8ed4425c8edf7803f96ce43">1a25274</a></li> 
    <li>[修复]<span> </span><code>Worker Service</code><span> </span>发布成<span> </span><code>Windows Services</code><span> </span>时日志绝对路径问题 感谢<span> </span><a href="https://gitee.com/jacoat">@jacoat</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/467">!467</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>其他更改</strong></p> 
   <ul> 
    <li>[调整] 定时任务失败后异常处理逻辑，感谢<span> </span><a href="https://gitee.com/cxs1992">@程小胜</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/463">!463</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>文档</strong></p> 
   <ul> 
    <li>[更新] 定时任务文档，日志文档</li> 
    <li>[新增] 文件上传/下载 文档，包含单文件/多文件/Base64/Byte[]</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<p><img height="1007" src="https://oscimg.oschina.net/oscnet/up-54bd7983d6c789f34af11f8134bad883a57.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            