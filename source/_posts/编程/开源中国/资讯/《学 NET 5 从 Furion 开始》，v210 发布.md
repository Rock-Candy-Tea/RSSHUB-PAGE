
---
title: '《学 .NET 5 从 Furion 开始》，v2.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Fri, 23 Apr 2021 20:11:00 GMT
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
<h2><img height="1080" src="https://oscimg.oschina.net/oscnet/up-3d826dc2471775c26d5d98670fe67e1b966.png" width="1920" referrerpolicy="no-referrer"></h2> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 新增定时任务 <code>ISpareTimeWorker</code> 方式支持 <code>[SpareTime("&#123;配置路径&#125;&#125;]</code> 方式 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NTUX">#I3NTUX</a></li> 
    <li>[新增] 定时任务支持异步委托 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NP96">#I3NP96</a></li> 
    <li>[新增] 轻量级分布式连续 GUID 生成器 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NKLZ">#I3NKLZ</a></li> 
    <li>[新增] <code>ClayObject</code> 模块，处理 <code>ExpandoObject</code> 及 <code>IDictionary<string,object></code> 类型 <a href="https://gitee.com/dotnetchina/Furion/issues/I3N3J4">#I3N3J4</a></li> 
    <li>[新增] <code>Scoped.CreateUnitOfWork(handler)</code> 创建作用域并自动提交数据库更改方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NU3G">#I3NU3G</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[调整] 规范化结果接口 <code>OnResponseStatusCodes</code> 方法，新增 <code>UnifyResultStatusCodesOptions</code> 参数 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NDB9">#I3NDB9</a></li> 
    <li>[移除] <strong>雪花 ID 实现代码 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NKLZ">#I3NKLZ</a></strong></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] <code>Swagger</code> 不能支持非 int 类型的枚举 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NQM8">#I3NQM8</a></li> 
    <li>[修复] 数据库线程池多线程并发问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NR4L">#I3NR4L</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[改进] 支持应用启动的时候迁移种子数据 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NH3M">#I3NH3M</a></li> 
   </ul> </li> 
  <li> <p><strong>文档变化</strong></p> 
   <ul> 
    <li>[新增] 分布式 ID 生成文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3B6CX">#I3B6CX</a></li> 
    <li>[新增] 新增模块化开发文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NSUS">#I3NSUS</a></li> 
    <li>[更新] 20.4 字符串拓展方式 > 错误<code>ToAESDecrypt</code> 写成了 <code>ToToAESDecrypt</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3NNKV">#</a></li> 
   </ul> </li> 
  <li> <p><strong>问答答疑</strong></p> 
   <ul> 
    <li>[答疑] 有关【定时任务/委托】的疑问 <a href="https://gitee.com/dotnetchina/Furion/issues/I3N3EW">#I3N3EW</a></li> 
    <li>[答疑] 统一返回格式支持自定义 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NU1G">#I3NU1G</a></li> 
   </ul> </li> 
  <li> <p><strong>不做实现</strong></p> 
   <ul> 
    <li>[作废] 期待 IEnumerableExtensions 扩展 OrderBy 函数来支持分页排序 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NOQ9">#I3NOQ9</a></li> 
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
            