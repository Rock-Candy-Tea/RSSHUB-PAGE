
---
title: '.NET 5 框架 Furion 2.2.0 发布，祝贺 QQ 交流群人数破 6000 人大关'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Thu, 29 Apr 2021 11:41:00 GMT
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
<h2>喜报分享</h2> 
<p>还是老样子，先来汇报近期成果：</p> 
<blockquote> 
 <ul> 
  <li><strong>Starred</strong>：4610 个</li> 
  <li><strong>Forked</strong>：1560 个</li> 
  <li><strong>Wathing</strong>：1540 个</li> 
  <li><strong>Issues</strong>：662 个</li> 
  <li><strong>Pull Request</strong>：276 个</li> 
  <li><strong>贡献者</strong>：116 个</li> 
  <li><strong>代码提交</strong>：2684 次</li> 
  <li><strong>文档篇数</strong>：132 篇</li> 
  <li><strong>QQ 交流群</strong>：6003 人（<strong>重叠人不超过 100 人</strong>）</li> 
 </ul> 
</blockquote> 
<p><img height="930" src="https://oscimg.oschina.net/oscnet/up-797aa6b908926c91db329ff2e8ebeb95d95.png" width="1498" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-65ff2aae41978b6bbf2efdd9f37f4477b64.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-1ad0ce9e320b3a84b9e25206aadbf6de068.png" width="1918" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-2eec5b28da7d4e347f6e752cdd13a88faea.png" width="1238" referrerpolicy="no-referrer"></p> 
<p><img height="1033" src="https://oscimg.oschina.net/oscnet/up-8257040dbf6d516a7844b030925c483c32f.png" width="1237" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] <code>Clay</code> 粘土类型，支持让 <code>C#</code> 创建一个弱类型对象并操作弱类型 <a href="https://gitee.com/dotnetchina/Furion/issues/I3O2QQ">#I3O2QQ</a></li> 
    <li>[新增] 新增 <code>Scoped.Create</code> 带返回值重载 <a href="https://gitee.com/dotnetchina/Furion/issues/I3O47J">#I3O47J</a></li> 
    <li>[新增] 支持 <code>Scoped.Create()</code> 一系列方法支持传入作用域工厂 <a href="https://gitee.com/dotnetchina/Furion/issues/I3OAP5">#I3OAP5</a></li> 
    <li>[新增] 支持事件总线同步执行方式 <a href="https://gitee.com/dotnetchina/Furion/issues/I3OAW2">#I3OAW2</a></li> 
    <li>[新增] <code>[DataValidation]</code> 跳过空字符串和空值验证 <a href="https://gitee.com/dotnetchina/Furion/issues/I3OGEN">#I3OGEN</a></li> 
    <li>[新增] <code>Worker Service</code> 可配置是否自动注册 <code>Worker</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3OLW4">#I3OLW4</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 定时任务设置 <code>cancelInNoneNextTime: false</code> 一次也不执行 <a href="https://gitee.com/dotnetchina/Furion/issues/I3O3N0">#I3O3N0</a></li> 
    <li>[修复] SpareTime 自定义下次执行时间出现空异常 <a href="https://gitee.com/dotnetchina/Furion/issues/I3O46X">#I3O46X</a></li> 
    <li>[修复] <code>MiniProfiler</code> 设置为 <code>false</code> 时，数据库上下文提交拦截器未添加 <a href="https://gitee.com/dotnetchina/Furion/issues/I3OAWX">#I3OAWX</a></li> 
    <li>[修复] <code>[Consumes("application/x-www-form-urlencoded")]</code> 和 <code>ModelQuery</code> 配置同时配置导致空引用问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3ODUR">#I3ODUR</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[优化] 支持发布后代码精简配置，减少不必要的文件夹输出 <a href="https://gitee.com/dotnetchina/Furion/issues/I3OAPF">#I3OAPF</a></li> 
    <li>[优化] 自动刷新 Token 机制，新增容错值处理，解决并发 Token 刷新失败问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3OGYF">#I3OGYF</a></li> 
   </ul> </li> 
  <li> <p><strong>文档变化</strong></p> 
   <ul> 
    <li>[新增] 粘土对象文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3OG18">#I3OG18</a></li> 
   </ul> </li> 
  <li> <p><strong>问答答疑</strong></p> 
   <ul> 
    <li>[答疑] 动态 WebAPI 如何获取接收文件 <a href="https://gitee.com/dotnetchina/Furion/issues/I3O29B">#I3O29B</a></li> 
    <li>[答疑] 定时任务使用 <code>Scope.CreateUnitOfWork</code> 引发的问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3O2CD">#I3O2CD</a></li> 
    <li>[答疑] 单文件发布程序工作不正常 <a href="https://gitee.com/dotnetchina/Furion/issues/I3O4D8">#I3O4D8</a></li> 
    <li>[答疑] 同时配置租户过滤器和软删除过滤器，最终的 sql 只生成了一种过滤条件 <a href="https://gitee.com/dotnetchina/Furion/issues/I3OB0A">#I3OB0A</a></li> 
    <li>[答疑] HTTP 重定向 HTTPS 后跨域失效 <a href="https://gitee.com/dotnetchina/Furion/issues/I3OB8R">#I3OB8R</a></li> 
    <li>[答疑] 在 PostgreSql 数据库使用 <code>rep.FirstOrDefault(u => u.Id == UserId);</code> 引起异常 <a href="https://gitee.com/dotnetchina/Furion/issues/I3O5OF">#I3O5OF</a></li> 
    <li>[答疑] 定时任务有时能触发有时不能触发 <a href="https://gitee.com/dotnetchina/Furion/issues/I3ORBE">#I3ORBE</a></li> 
   </ul> </li> 
  <li> <p><strong>不做实现</strong></p> 
   <ul> 
    <li>[作废] 框架中的 swagger 是否有提供导出文档为 markdwon/word 的功能计划？ <a href="https://gitee.com/dotnetchina/Furion/issues/I3OL8O">#I3OL8O</a></li> 
    <li>[作废] 数据库实体父子继承，子类生成的 SQL 不一样 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NHU3">#I3NHU3</a></li> 
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
            