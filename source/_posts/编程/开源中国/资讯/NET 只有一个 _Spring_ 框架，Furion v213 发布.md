
---
title: '.NET 只有一个 _Spring_ 框架，Furion v2.13 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Wed, 14 Jul 2021 14:25:00 GMT
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
<p>Furion 经过近 1 年的发展，目前已经成为 <strong>Gitee 平台 C# 板块⭐️最高星⭐️项目</strong>，参与代码贡献的开发者达 145人，在 Nuget 一个平台下总下载已达突破 683K（每天增速 30K+），Gitee 仓库每天浏览量量平均 2000+PV，Furion 文档每天浏览量平均每天 20000+PV。</p> 
<p><strong>从各项数据来看，Furion 正在成为 .NET 版本的 Spring 框架。</strong></p> 
<p><img height="1034" src="https://oscimg.oschina.net/oscnet/up-c245303e85d4d899e74566fb15b75f170e5.png" width="1235" referrerpolicy="no-referrer"></p> 
<p><img height="894" src="https://oscimg.oschina.net/oscnet/up-6c8d0fc815f8c7089a24f4f588a1847bd96.png" width="1214" referrerpolicy="no-referrer"></p> 
<p><img height="899" src="https://oscimg.oschina.net/oscnet/up-23a928cdb753253796469dea19f6420f9c9.png" width="1489" referrerpolicy="no-referrer"></p> 
<p><img height="1009" src="https://oscimg.oschina.net/oscnet/up-282dbe04bde706e524aa5963b51d252a8c7.png" width="1919" referrerpolicy="no-referrer"></p> 
<p><img height="1010" src="https://oscimg.oschina.net/oscnet/up-202cc9d65519f3dcf395ecb4c75910b0a30.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img src="https://dotnetchina.gitee.io/furion/img/functions.png" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 简易字符串模板功能，支持远程请求、数据库模块、日志模块、事件总线模块、定时任务模块、异常模块、数据校验模块 <a href="https://gitee.com/dotnetchina/Furion/issues/I402BL">#I402BL</a></li> 
    <li>[新增] <code>404</code> 状态码规范化默认处理 <a href="https://gitee.com/dotnetchina/Furion/issues/I408F5">#I408F5</a></li> 
    <li>[新增] 定时任务 <code>ISpareTimeWorker</code> 声明方式支持异步方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I40KWR">#I40KWR</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[升级] <strong>框架依赖 <code>SDK</code> 为 <code>.NET 5.0.8</code> 版本</strong></li> 
    <li>[移除] <code>Db.GetNewDbContext()</code> 静态方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I400BK">#I400BK</a></li> 
    <li>[移除] 数据库模块时态表拓展支持 <a href="https://gitee.com/dotnetchina/Furion/issues/I405HI">#I405HI</a></li> 
    <li>[调整] <code>IJsonSerializerProvider</code> 接口参数，新增 <code>inherit</code> 参数 <a href="https://gitee.com/dotnetchina/Furion/issues/I3ZQU5">#I3ZQU5</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] <code>Worker Services</code> 定时任务边界值问题导致跳过单次任务 <a href="https://gitee.com/dotnetchina/Furion/issues/I405NI">#I405NI</a></li> 
    <li>[修复] <code>Worker Services</code> 独立发布后程序集扫描失效 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3ZH3X">#I3ZH3X</a></li> 
    <li>[修复] 远程请求如果配置了 <code>Client</code> 客户端但传入了空 <code>RequestUrl</code> 地址导致异常问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I40BC6">#I40BC6</a></li> 
    <li>[修复] 规范化结果篡改非短路端状态码出现异常 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I408F5">#I408F5</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[优化] <code>App.GetServiceProvider(type)</code> 解析服务性能 <a href="https://gitee.com/dotnetchina/Furion/issues/I40KXN">#I40KXN</a></li> 
    <li>[调整] 视图引擎保存成文件流默认缓存区大小，从 <code>4096</code> 提升至 <code>8192</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I40KH5">#I40KH5</a></li> 
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
                                        </div>
                                      
</div>
            