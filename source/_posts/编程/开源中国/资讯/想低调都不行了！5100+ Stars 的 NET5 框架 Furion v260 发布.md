
---
title: '想低调都不行了！5100+ Stars 的 .NET5 框架 Furion v2.6.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Mon, 17 May 2021 14:50:00 GMT
thumbnail: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p> </p> 
<p style="text-align:center"><img height="80" src="https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png" width="127" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <p style="text-align:center"><a href="https://gitee.com/dotnetchina/Furion/stargazers"><img alt="star" src="https://gitee.com/dotnetchina/Furion/badge/star.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/members"><img alt="fork" src="https://gitee.com/dotnetchina/Furion/badge/fork.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fstargazers" target="_blank"><img alt="GitHub stars" src="https://img.shields.io/github/stars/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fnetwork" target="_blank"><img alt="GitHub forks" src="https://img.shields.io/github/forks/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/badge/license-Apache2-yellow" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></p> 
</div> 
<div style="text-align:left"> 
 <p style="text-align:center">让 .NET 开发更简单，更通用，更流行。</p> 
</div> 
<p> </p> 
<h2>版本总结</h2> 
<p>Furion 框架在 Gitee 平台获得超 5.1K Stars 的关注量，近 2K 的 Watching 和 Forks，Gitee 指数 90 分，超过 120 个开发者贡献代码，QQ 群人数已逾 6300+，Nuget 总下载近 300K。各项数据每天仍以指数增长中。</p> 
<p><strong>可以这么说，Furion 框架想低调都不行了！</strong></p> 
<p><img height="1007" src="https://oscimg.oschina.net/oscnet/up-82c658c3d23e35147fa218103447a5ea3d9.png" width="1245" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 虚拟文件服务，支持物理文件和嵌入资源文件 <a href="https://gitee.com/dotnetchina/Furion/issues/I3RBR9">#I3RBR9</a></li> 
    <li>[新增] 读写分离/主从复制仓储 <code>IMSRepository</code> 和 <code>IMSRepository<TMasterDbContextLocator></code> 仓储，可进行随机或自定义获取从库</li> 
    <li>[新增] 数据脱敏处理 <a href="https://gitee.com/dotnetchina/Furion/issues/I3R5ZF">#I3R5ZF</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[移除] <strong><code>InsertOrUpdate</code> 一系列数据库操作方法</strong> <a href="https://gitee.com/dotnetchina/Furion/issues/I3RI9L">#I3RI9L</a></li> 
    <li>[移除] 所有包含 <code>Exists</code> 单词的数据库操作方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I3RJ0T">#I3RJ0T</a></li> 
    <li>[调整] 分布式 GUID <code>IDGenerater</code> 静态类名称为 <code>IDGen</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3RGUA">#I3RGUA</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 远程调用方法错误，请求报文头 <code>Headers</code> 不能添加到 <code>IHttpDispatchProxy</code> 的子接口上 <a href="https://gitee.com/dotnetchina/Furion/issues/I3RAF7">#I3RAF7</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[优化] 应用启动性能，减少内存分配</li> 
   </ul> </li> 
  <li> <p><strong>文档变化</strong></p> 
   <ul> 
    <li>[新增] 脱敏处理文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3R6WZ">#I3R6WZ</a></li> 
    <li>[新增] 文件系统文档、<code>FS</code> 静态类文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3RCC4">#I3RCC4</a></li> 
    <li>[更新] 读写分离/主从复制、数据库仓储文档、<code>Db</code> 静态类 <a href="https://gitee.com/dotnetchina/Furion/issues/I3R3B6">#I3R3B6</a></li> 
   </ul> </li> 
  <li> <p><strong>问答答疑</strong></p> 
   <ul> 
    <li>[答疑] 关于 <code>Furion</code> 集群部署 <a href="https://gitee.com/dotnetchina/Furion/issues/I3R3J4">#I3R3J4</a></li> 
    <li>[答疑] 升级最新框架以后， 数据库生成模型报错 <a href="https://gitee.com/dotnetchina/Furion/issues/I3R7TP">#I3R7TP</a></li> 
    <li>[答疑] 数据库上下文事务执行中，<code>SaveNow</code> 执行后有警告 <a href="https://gitee.com/dotnetchina/Furion/issues/I3RAJI">#I3RAJI</a></li> 
   </ul> </li> 
  <li> <p><strong>不做实现</strong></p> 
   <ul> 
    <li>[拒绝] 有序 <code>Guid</code> 精度是固定的毫秒级：1 毫秒内生成的多个 <code>Guid</code> 是无序的 <a href="https://gitee.com/dotnetchina/Furion/issues/I3R59J">#I3R59J</a></li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2>贡献者列表</h2> 
<p><img alt="Giteye chart" src="https://chart.giteye.net/gitee/dotnetchina/Furion/ZS49EPL6.png" referrerpolicy="no-referrer"></p> 
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
            