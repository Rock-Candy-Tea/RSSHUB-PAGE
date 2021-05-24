
---
title: '学 Java 必学 Spring，学 C# 离不开 Furion，v2.7.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Mon, 24 May 2021 16:27:00 GMT
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
<h2>版本序言</h2> 
<p>经过上百次版本的迭代改进，Furion 日渐稳定完善，使用者也是指数增长，<strong>目前总增速保持在每天 15K 的下载量，QQ 交流群也超过 6400+ 人，每天的增速保持在 30/天。</strong></p> 
<p><span style="color:#2980b9"><strong>以后再有人问：“你们 C# 有什么拿得出手的框架不？“，可以自豪的回答：”Furion“。</strong></span></p> 
<h2>本期亮点</h2> 
<p><strong>1、框架启动内存占用由 136M 下降到了 86M，并提供了更精确的 GC 回收控制。</strong></p> 
<p><img height="1068" src="https://oscimg.oschina.net/oscnet/up-7207b441bbfe75a5fc33459bbd180750003.png" width="1907" referrerpolicy="no-referrer"></p> 
<p><strong>2、支持 EFCore 完整的 `SQL` 执行日志输出</strong></p> 
<p><img height="724" src="https://oscimg.oschina.net/oscnet/up-6b13659cfed9202e87ce163ba85a97b7437.png" width="1350" referrerpolicy="no-referrer"></p> 
<p><strong>3、`Scoped` 支持同步异步作用域写法</strong></p> 
<p><img height="921" src="https://oscimg.oschina.net/oscnet/up-0446f86d5bfda17f5a88333a9cf1cd4c696.png" width="1244" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 工作单元特性，支持静态类强制性开启共享事务 <a href="https://gitee.com/dotnetchina/Furion/issues/I3S9N8">#I3S9N8</a></li> 
    <li>[新增] <code>EFCore</code> 执行 <code>sql</code> 模式打印日志 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SE8X">#I3SE8X</a></li> 
    <li>[新增] 远程请求支持默认 <code>HttpClient</code> 配置 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SI17">#I3SI17</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[调整] <strong><code>Scoped.CreateUnitOfWork</code> 名称为 <code>Scoped.CreateUow</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3SJPU">#I3SJPU</a></strong></li> 
    <li>[调整] <code>JWTEncryption.Validate</code> 返回值，支持返回 <code>TokenValidationResult</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3S2ND">#I3S2ND</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] <code>Scoped</code> 系列方法异步出现 <code>Task is cancel</code> 情况 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SJF6">#I3SJF6</a></li> 
    <li>[修复] <code>Mysql</code> 数据库的 <code>ToPagedList</code> 方法返回的结果进行遍历出现 <code>MySqlConnection is aleady use</code> 问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SJQ3">#I3SJQ3</a></li> 
    <li>[修复] <code>tool/cli.psl</code> 没有包含项目名称 <a href="https://gitee.com/dotnetchina/Furion/issues/I3S1T6">#I3S1T6</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[优化] <strong>框架底层性能，大大减少内存占用和溢出情况，启动内存从之前 <code>136M</code> 下将到 <code>86M</code></strong></li> 
    <li>[调整] 更新部分列 <code>UpdateIncludeNowAsync</code> 具有二义性 <a href="https://gitee.com/dotnetchina/Furion/issues/I3RW9Q">#I3RW9Q</a></li> 
   </ul> </li> 
  <li> <p><strong>文档变化</strong></p> 
   <ul> 
    <li>[更新] 4.2.9 的示例代码文档，方法没有放在 class 中 <a href="https://gitee.com/dotnetchina/Furion/issues/I3S9T5">#I3S9T5</a></li> 
   </ul> </li> 
  <li> <p><strong>问答答疑</strong></p> 
   <ul> 
    <li>[答疑] 默认 <code>MasterDbContextLocator</code> 不随自定义的参数生成 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SDBB">#I3SDBB</a></li> 
   </ul> </li> 
  <li> <p><strong>不做实现</strong></p> 
   <ul> 
    <li>[废弃] 添加令牌桶限流算法 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SCDV">#I3SCDV</a></li> 
    <li>[废弃] 定时任务立即执行需求 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SF4A">#I3SF4A</a></li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2>框架特点</h2> 
<ul> 
 <li><strong>全新面貌</strong>：基于 <code>.NET5/6</code> 平台，没有历史包袱</li> 
 <li><strong>极易入门</strong>：只需要一个 <code>Inject()</code> 即可完成配置</li> 
 <li><strong>极速开发</strong>：内置丰富的企业应用开发功能</li> 
 <li><strong>极少依赖</strong>：框架只依赖两个第三方包</li> 
 <li><strong>极其灵活</strong>：轻松面对多变复杂的需求</li> 
 <li><strong>极易维护</strong>：采用独特的架构思想，只为长久维护设计</li> 
 <li><strong>完整文档</strong>：提供完善的开发文档</li> 
</ul> 
<h2>功能模块图</h2> 
<p><img src="https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/functions.png" referrerpolicy="no-referrer"></p> 
<h2>文档概括图</h2> 
<h2><img height="1080" src="https://oscimg.oschina.net/oscnet/up-0ba33cf268e8445493b1b7f0003294f89d0.png" width="1920" referrerpolicy="no-referrer"></h2> 
<h2>贡献者画像</h2> 
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
            