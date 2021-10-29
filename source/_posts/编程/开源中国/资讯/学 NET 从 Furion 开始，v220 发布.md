
---
title: '学 .NET 从 Furion 开始，v2.20 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Fri, 29 Oct 2021 12:44:00 GMT
thumbnail: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img height="80" src="https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png" width="80" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <p style="margin-left:0; margin-right:0; text-align:center"><a href="https://gitee.com/dotnetchina/Furion/stargazers"><img alt="star" src="https://gitee.com/dotnetchina/Furion/badge/star.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/members"><img alt="fork" src="https://gitee.com/dotnetchina/Furion/badge/fork.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fstargazers" target="_blank"><img alt="GitHub stars" src="https://img.shields.io/github/stars/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fnetwork" target="_blank"><img alt="GitHub forks" src="https://img.shields.io/github/forks/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/badge/license-MulanPSL--2.0-orange" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></p> 
</div> 
<div style="text-align:left"> 
 <p style="margin-left:0; margin-right:0; text-align:center">让 .NET 开发更简单，更通用，更流行。</p> 
</div> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p style="margin-left:0; margin-right:0"><strong>突破性变化</strong></p> 
   <ul> 
    <li><strong>[重构]<span> </span><code>EventBus</code><span> </span>模块，采用<span> </span><a href="https://gitee.com/dotnetchina/Jaina">Jaina</a><span> </span>方式</strong></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 远程请求上传文件异常<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/0c0752c624799d7d3c7661a8f36a93983399bb59">0c0752</a></li> 
    <li>[修复] 框架启动不支持环境变量<span> </span><code>ASPNETCORE_HOSTINGSTARTUPASSEMBLIES</code><span> </span>配置<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/438">!438</a></li> 
    <li>[修正] 依赖注入<span> </span><code>InjectionAttribute</code><span> </span>特性的<span> </span><code>ExceptInterfaces</code><span> </span>单词拼写错误问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/436">!436</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>其他更改</strong></p> 
   <ul> 
    <li>[优化]<span> </span><code>InjectionAttribute</code><span> </span>代码<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/435">!435</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>文档</strong></p> 
   <ul> 
    <li>[新增] 事件总线新文档</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:left">框架特点</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>全新面貌：基于 <code>.NET5/6</code> 平台，没有历史包袱</li> 
 <li>极少依赖：框架只依赖两个第三方包</li> 
 <li>极易入门：只需要一个 <code>Inject()</code> 即可完成配置</li> 
 <li>极速开发：内置丰富的企业应用开发功能</li> 
 <li>极其灵活：轻松面对多变复杂的需求</li> 
 <li>极易维护：采用独特的架构思想，只为长久维护设计</li> 
 <li>完整文档：提供完善的开发文档</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">使用文档</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong>国内文档</strong>：<a href="https://dotnetchina.gitee.io/furion">https://dotnetchina.gitee.io/furion</a></li> 
 <li>国外文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffurion.pro%2F" target="_blank">https://furion.pro</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">开源地址</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Gitee：<a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmonksoul%2FFurion" target="_blank">https://github.com/monksoul/Furion</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank">https://www.nuget.org/packages/Furion</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">贡献代码</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>Furion</code> 遵循 <a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE">MulanPSL-2.0</a> 开源协议，欢迎大家提交 <code>Pull Request</code> 或 <code>Issue</code>。如果要为项目做出贡献，请查看 <a href="https://dotnetchina.gitee.io/furion/docs/contribute">贡献指南</a>。感谢每一位为 <code>Furion</code> 贡献代码的朋友。<br> <img alt src="https://oscimg.oschina.net/oscnet/up-4d6070e117acbf15270e4d5f31498838fdf.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            