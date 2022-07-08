
---
title: '《学 .NET 从 Furion 开始》，v3.7.6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3ceb83053a2a7f3afec6c4ef042ea1e8258.png'
author: 开源中国
comments: false
date: Fri, 08 Jul 2022 08:16:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3ceb83053a2a7f3afec6c4ef042ea1e8258.png'
---

<div>   
<div class="content">
                                                                                            <p>自 2020年 09 月 01 日 Furion 诞生起马不停蹄的更新至今，目前无论是关注量还是 Nuget 下载量，在国内 .NET 开发框架中属于非常热门的框架，<strong>Nuget 总安装量 277 万次</strong>，查看下载量：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fprofiles%2Fmonk.soul" target="_blank">https://www.nuget.org/profiles/monk.soul</a><strong>，有 206 个开发者参与贡献，编写了 231 万字的文档。</strong></p> 
<ul> 
 <li><strong>项目地址：</strong><a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
 <li><strong>文档地址</strong>：<a href="https://dotnetchina.gitee.io/furion/">https://dotnetchina.gitee.io/furion/</a></li> 
</ul> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-3ceb83053a2a7f3afec6c4ef042ea1e8258.png" width="1347" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-d247b57981e95b03d2f2fb6346e1c7d8228.png" width="1508" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-cbddf5393b0bece853745520fa75363f7b8.png" width="1508" referrerpolicy="no-referrer"></p> 
<hr> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span><strong><code>Minimal API</code><span> </span>应用支持：<code>.AddInjectMini()</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I4KOQ5" target="_blank">#I4KOQ5</a></strong></li> 
    <li>[新增]<span> </span>跨域<span> </span><code>WithExposedHeaders</code><span> </span>默认配置<span> </span><code>access-token</code><span> </span>和<span> </span><code>x-access-token</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/42ebdfd33a01353a0b3a801528de052990d2e4c9" target="_blank">42ebdfd</a></li> 
    <li>[新增]<span> </span>脚手架默认启用<span> </span><code>app.UseHttpLogging()</code><span> </span><code>HTTP</code><span> </span>日志<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/42ebdfd33a01353a0b3a801528de052990d2e4c9" target="_blank">42ebdfd</a></li> 
    <li>[新增]<span> </span><strong><code>Furion</code><span> </span>和<span> </span><code>ASP.NET Core</code><span> </span>完整<span> </span><code>json</code><span> </span>配置的<span> </span><code>JSON Schema</code><span> </span>架构<span> </span><a href="https://gitee.com/dotnetchina/Furion/raw/net6/schemas/v3/furion-schema.json" target="_blank">JSON Schema</a></strong></li> 
    <li>[新增]<span> </span><code>Sql</code><span> </span>代理支持返回单个类类型参数<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/1d7fb5b5330c5a30098056818a93a0879034fecd" target="_blank">1d7fb5b</a></li> 
    <li>[新增]<span> </span><code>Sql</code><span> </span>代理支持返回<span> </span><code>ValueTuple</code><span> </span>单个类类型参数<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/876a2f5f7e2d07fa3bbc3f5b99c0653893e0ada8" target="_blank">876a2f5</a></li> 
    <li>[新增]<span> </span>组件化设计模块，支持比<span> </span><code>AppStartup</code><span> </span>更灵活便捷的设计<span> </span><a href="https://gitee.com/dotnetchina/Furion/tree/net6/framework/Furion/Components" target="_blank">#components</a></li> 
    <li>[新增]<span> </span>独立工作单元单元模块，支持任何第三方<span> </span><code>ORM</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/a02413d6887d258ad3a1ba972bb6a08d29291d0c" target="_blank">a02413d</a></li> 
    <li>[新增]<span> </span>跨域<span> </span><code>FixedClientToken</code><span> </span>配置参数<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/bd016386681631a5539bcf215c068c2069bba15f" target="_blank">bd01638</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span><strong><code>Minimal API</code><span> </span>应用支持：<code>.AddInjectMini()</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I4KOQ5" target="_blank">#I4KOQ5</a></strong></li> 
    <li>[新增]<span> </span><strong><code>Furion</code><span> </span>和<span> </span><code>ASP.NET Core</code><span> </span>完整<span> </span><code>json</code><span> </span>配置的<span> </span><code>JSON Schema</code><span> </span>架构<span> </span><a href="https://gitee.com/dotnetchina/Furion/raw/net6/schemas/v3/furion-schema.json" target="_blank">JSON Schema</a></strong></li> 
    <li>[新增]<span> </span>组件化设计模块，支持比<span> </span><code>AppStartup</code><span> </span>更灵活便捷的设计<span> </span><a href="https://gitee.com/dotnetchina/Furion/tree/net6/framework/Furion/Components" target="_blank">#components</a></li> 
    <li>[新增]<span> </span>独立工作单元单元模块，支持任何第三方<span> </span><code>ORM</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/a02413d6887d258ad3a1ba972bb6a08d29291d0c" target="_blank">a02413d</a></li> 
    <li>[调整]<span> </span><code>.AddDb<></code><span> </span>和<span> </span><code>.AddDbPool<></code><span> </span>自定义委托参数签名，由<span> </span><code>Action<DbContextOptionsBuilder></code><span> </span>改为：<code>Action<IServiceProvider, DbContextOptionsBuilder></code></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[修复]<span> </span>自<span> </span><code>v3.6.3</code><span> </span>版本依赖，执行原生<span> </span><code>Sql</code><span> </span>添加了参数校验导致存储过程执行错误问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5ERMQ" target="_blank">#I5ERMQ</a></li> 
    <li>[修复]<span> </span><code>tools/cli.ps1</code><span> </span>脚本工具出现数据库链接被占用问题</li> 
    <li>[修复]<span> </span><code>JWTSettings</code><span> </span>算法配置<span> </span><code>JSON Schema</code><span> </span>错误问题，感谢<span> </span><a href="https://gitee.com/gitwentao" target="_blank">@gitwentao</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5G27B" target="_blank">#I5G27B</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/516" target="_blank">!516</a></li> 
    <li>[修复]<span> </span>基于策略授权在不配置<span> </span><code>Policy</code><span> </span>的情况下出现空异常问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5EVF2" target="_blank">#I5EVF2</a></li> 
    <li>[修复]<span> </span>启用数据库实体跟踪时导致新增实体多次查询数据库问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I4J2LZ" target="_blank">#I4J2LZ</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[调整]<span> </span>脚手架所有<span> </span><code>.json</code><span> </span>文件，默认添加<span> </span><code>JSON Schema</code><span> </span>支持</li> 
   </ul> </li> 
  <li> <p><strong>文档</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span>组件化启动文档</li> 
    <li>[新增]<span> </span><code>Vue/React/Angular</code><span> </span>请求代理文档</li> 
    <li>[新增]<span> </span><code>JSON Schema</code><span> </span>文档，支持配置智能提示和验证</li> 
    <li>[更新]<span> </span>跨域文档、规范化文档、配置文档、日志文档、IIS 部署文档</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<p> </p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-b2c36a482ab1c6e62c8fa89cb12cd6b7464.png" width="1919" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-2b8ca18da4af2862359c05bf2d089dd3276.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            