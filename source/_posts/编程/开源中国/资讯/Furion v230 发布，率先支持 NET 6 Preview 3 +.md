
---
title: 'Furion v2.3.0 发布，率先支持 .NET 6 Preview 3 +'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Thu, 06 May 2021 09:43:00 GMT
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
<h3>支持 .NET 6</h3> 
<p>目前微软已经发布 .NET 6 Preview 3 版本，不出意外这两天微软将发布 .NET 6 Preview 4 版本。<strong>Furion 团队在五一期间修改了将近 20 个文件实现了底层完全支持 .NET 6 Preview 3 版本</strong>，源码地址：</p> 
<ul> 
 <li>Gitee 地址：<a href="https://gitee.com/dotnetchina/Furion/tree/feature%2Fnet6/">https://gitee.com/dotnetchina/Furion/tree/feature%2Fnet6/</a></li> 
 <li>Nuget 地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion%2F3.0.0-preview.3.21201.2" target="_blank">https://www.nuget.org/packages/Furion/3.0.0-preview.3.21201.2</a> （<strong>想尝鲜的朋友可以试试</strong>）</li> 
</ul> 
<p>后续版本迭代周期将和微软官方同步，也就是 27~30 天一个版本。</p> 
<h2>无缝升级</h2> 
<p><strong>Furion 团队承诺现有使用 .NET 5 版本的项目可以无缝升级到 .NET 6 版本，所有兼容处理交给 Furion 底层去处理。</strong></p> 
<h2>dotNET China 每周精选</h2> 
<p><strong>dotNET China 社区组织每周精选已经更新到第 8 期：</strong></p> 
<p><img height="1034" src="https://oscimg.oschina.net/oscnet/up-5140d756602d277e050fa738f8587e7b967.png" width="879" referrerpolicy="no-referrer"></p> 
<p>dotNET China 官方组织地址：<a href="https://gitee.com/dotnetchina">https://gitee.com/dotnetchina</a></p> 
<p>欢迎大家捐赠优秀国人项目或申请加入组织。</p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] <code>Furion.Extras.DatabaseAccessor.MongoDB</code> 拓展包支持 <a href="https://gitee.com/dotnetchina/Furion/issues/I3PKST">#I3PKST</a></li> 
    <li>[新增] 动态粘土类型直接转 <code>object</code> 或 <code>dynamic</code> 类型 <a href="https://gitee.com/dotnetchina/Furion/issues/I3OY27">#I3OY27</a></li> 
    <li>[新增] 新增 <code>Oops.Retry</code> 方法，支持设置方法调用失败进行重试 <a href="https://gitee.com/dotnetchina/Furion/issues/I3PJKQ">#I3PJKQ</a></li> 
    <li>[新增] <code>JWTSettings</code> 配置节点 <code>Algorithm</code>，用于配置加密算法 <a href="https://gitee.com/dotnetchina/Furion/issues/I3PQGV">#I3PQGV</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[支持] 支持 .NET 6.0.0 Preview 3 版本 <a href="https://gitee.com/dotnetchina/Furion/issues/I3P2C7">#I3P2C7</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 使用数据库生成模型 <code>tools/cli.ps1</code>，从数据库表生成的实体异常 <a href="https://gitee.com/dotnetchina/Furion/issues/I3PL18">#I3PL18</a></li> 
    <li>[修复] 贴了 <code>[NonUntify]</code> 特性后，<code>Swagger</code> 的 <code>Example Value</code> 没有匹配正确 <a href="https://gitee.com/dotnetchina/Furion/issues/I3PK0L">#I3PK0L</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[改进] 框架默认序列化应该从配置中读取，而非手动编写 <a href="https://gitee.com/dotnetchina/Furion/issues/I3P1SJ">#I3P1SJ</a></li> 
    <li>[改进] <code>SqlSugar</code> 拓展库，支持非泛型仓储获取上下文操作对象 <a href="https://gitee.com/dotnetchina/Furion/issues/I3PK2N">#I3PK2N</a></li> 
    <li>[改进] 支持分布式内存缓存可配置化 <a href="https://gitee.com/dotnetchina/Furion/issues/I3POKD">#I3POKD</a></li> 
   </ul> </li> 
  <li> <p><strong>文档变化</strong></p> 
   <ul> 
    <li>[文档] 添加 <code>JWTSettings</code> 配置独立文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3PQGW">#I3PQGW</a></li> 
   </ul> </li> 
  <li> <p><strong>问答答疑</strong></p> </li> 
  <li> <p><strong>不做实现</strong></p> 
   <ul> 
    <li>[废弃] CAS 支持<a href="https://gitee.com/dotnetchina/Furion/issues/I3PIET">#I3PIET</a></li> 
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
            