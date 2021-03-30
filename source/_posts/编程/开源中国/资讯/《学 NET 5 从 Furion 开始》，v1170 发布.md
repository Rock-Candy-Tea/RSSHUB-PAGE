
---
title: '《学 .NET 5 从 Furion 开始》，v1.17.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Tue, 30 Mar 2021 17:13:00 GMT
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
<h2 style="text-align:left">说点什么</h2> 
<p><strong>自 2020 年 09 月 01 日起，Furion 更新了近 200 个版本，完成了 530 个 Issues，合并处理了 230 个 Pull Request，同时 QQ 群总成员也将突破 5100 人。在 Gitee 中 Stars 关注量近 3.8k，同时 Fork 和 Watching 也达到了 1.1k +。</strong>得到这样的成绩也算是为 .NET 做出了点贡献。未来的路还很长，Furion 不忘初心，一如既往。</p> 
<p><img height="1824" src="https://oscimg.oschina.net/oscnet/up-7bd2a379c1747ba8774997f43977b875eec.png" width="2736" referrerpolicy="no-referrer"></p> 
<p><img height="1824" src="https://oscimg.oschina.net/oscnet/up-345121aa1400c7aab91c8db9b41a76c10db.png" width="2736" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 动态 WebAPI 支持继承基类配置特性 <a href="https://gitee.com/dotnetchina/Furion/issues/I3D5PX">#I3D5PX</a></li> 
    <li>[新增] 远程请求支持 <code>multipart/form-data</code> 内容类型处理 <a href="https://gitee.com/dotnetchina/Furion/issues/I3D7KG">#I3D7KG</a></li> 
    <li>[新增] 字符串加密拓展 <a href="https://gitee.com/dotnetchina/Furion/issues/I3DHBW">#I3DHBW</a></li> 
    <li>[新增] 新增远程请求可直接下载返回值内容转为 string 类型 <a href="https://gitee.com/dotnetchina/Furion/issues/I3DIGR">#I3DIGR</a></li> 
    <li>[新增] 远程请求地址支持模板引擎 <a href="https://gitee.com/dotnetchina/Furion/issues/I3D5Y8">#I3D5Y8</a></li> 
    <li>[新增] <code>[DataValidation]</code> 错误消息支持 <code>string.Format</code> 操作 <a href="https://gitee.com/dotnetchina/Furion/issues/I3E08W">#I3E08W</a></li> 
    <li>[新增] 远程请求 <code>HttpRequestMessage</code> 拓展方法 <code>AppendQueries()</code> 追加更多 <code>query</code> 参数拓展 <a href="https://gitee.com/dotnetchina/Furion/issues/I3E3DI">#I3E3DI</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[调整] <code>IRepository.AsAsyncEnumerable()</code> 返回值 <a href="https://gitee.com/dotnetchina/Furion/issues/I3DIQ1">#I3DIQ1</a>，调整为：<code>rep.AsQueryable().ToListAsync()</code></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 数据验证失败后也打印了成功的字段 <a href="https://gitee.com/dotnetchina/Furion/issues/I3CVBS">#I3CVBS</a></li> 
    <li>[修复] 远程请求配置 <code>contentType</code> 为 <code>application/x-www-form-urlencoded</code> 无效问题<a href="https://gitee.com/dotnetchina/Furion/issues/I3CWBS">#I3CWBS</a></li> 
    <li>[修复] 远程请求无法打印完整的请求地址，比如配置了 HttpClient 之后 <a href="https://gitee.com/dotnetchina/Furion/issues/I3CY42">#I3CY42</a></li> 
    <li>[修复] 程序启动时排除默认配置文件算法不对，应该采用正则表达式匹配 <a href="https://gitee.com/dotnetchina/Furion/issues/I3D9E7">#I3D9E7</a></li> 
    <li>[修复] 远程请求成功请求拦截不生效 <a href="https://gitee.com/dotnetchina/Furion/issues/I3DOE4">#I3DOE4</a></li> 
    <li>[修复] <code>Dapper</code> 拓展数据库切换为 oracle 时，系统找不到指定的文件 <code>Oracle.ManagedDataAccess.Core</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3DYM3">#I3DYM3</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[改进] 获取 <code>JWT token</code> 信息支持配置 <code>Token</code> 前缀，如 <code>Bearer </code><a href="https://gitee.com/dotnetchina/Furion/issues/I3DJIV">#I3DJIV</a></li> 
    <li>[改进] 刷新 Token 黑名单存储方式，将内存缓存调整为分布式缓存 <a href="https://gitee.com/dotnetchina/Furion/issues/I3DPBR">#I3DPBR</a></li> 
   </ul> </li> 
  <li> <p><strong>文档变化</strong></p> 
   <ul> 
    <li>[调整] 远程请求文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3CPJO">#I3CPJO</a></li> 
   </ul> </li> 
  <li> <p><strong>问答答疑</strong></p> 
   <ul> 
    <li>[答疑] <code>LinqExpression.And</code> 没有 2 个参数的方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I3CXKZ">#I3CXKZ</a></li> 
    <li>[答疑] 异常信息 如何记录到数据库中:) <a href="https://gitee.com/dotnetchina/Furion/issues/I3DDGO">#I3DDGO</a></li> 
    <li>[答疑] 无键实体选用 <code>IEntityNotKey</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3DWRF">#I3DWRF</a></li> 
    <li>[答疑] 根据主键删除一条记录不成功，无错误信息 <a href="https://gitee.com/dotnetchina/Furion/issues/I3DWWF">#I3DWWF</a></li> 
    <li>[答疑] 如何自定义接口返回格式 <a href="https://gitee.com/dotnetchina/Furion/issues/I3DZN6">#I3DZN6</a></li> 
    <li>[答疑] DynamicApiController 如何在运行时决定是否公开一个 Action <a href="https://gitee.com/dotnetchina/Furion/issues/I3D5UL">#I3D5UL</a></li> 
    <li>[答疑] <code>Furion.DatabaseAccessor.DbHelpers</code> 方法：<code>ConvertToDbParameters</code> 是不是应该过滤掉贴 <code>NotMapped</code> 的特性 <a href="https://gitee.com/dotnetchina/Furion/issues/I3E2XS">#I3E2XS</a></li> 
   </ul> </li> 
  <li> <p><strong>不做实现</strong></p> 
   <ul> 
    <li>[废弃] 框架是否提供 <code>ISoftDelete</code> 类似接口 <a href="https://gitee.com/dotnetchina/Furion/issues/I3CP93">#I3CP93</a></li> 
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
            