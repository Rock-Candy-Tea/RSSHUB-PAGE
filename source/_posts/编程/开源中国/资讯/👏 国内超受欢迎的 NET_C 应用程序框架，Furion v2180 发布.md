
---
title: '👏 国内超受欢迎的 .NET_C# 应用程序框架，Furion v2.18.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/license-MulanPSL--2.0-orange?cacheSeconds=10800'
author: 开源中国
comments: false
date: Wed, 18 Aug 2021 14:45:00 GMT
thumbnail: 'https://img.shields.io/badge/license-MulanPSL--2.0-orange?cacheSeconds=10800'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p><strong>截至 2021年08月18日，Furion 在 Nuget 单个平台安装量近 100万次（99万）。</strong>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fprofiles%2Fmonk.soul" target="_blank">点击查看统计地址</a>]</p> 
 <p><strong>截至 2021年08月18日，Furion 在 Gitee 平台收获：6900 stars，2858 watches，2995 forks，163 contributes。</strong>[<a href="https://gitee.com/dotnetchina/Furion">点击查看仓库地址</a>]</p> 
</blockquote> 
<h1 style="text-align:left">Furion</h1> 
<p style="text-align:left"><a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE"><img alt="license" src="https://img.shields.io/badge/license-MulanPSL--2.0-orange?cacheSeconds=10800" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fprofiles%2Fmonk.soul" target="_blank"><img alt="nuget downloads" src="https://img.shields.io/badge/downloads-989k-green?cacheSeconds=10800" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina"><img alt="dotNET China" src="https://img.shields.io/badge/organization-dotNET%20China-yellow?cacheSeconds=10800" referrerpolicy="no-referrer"></a></p> 
<p style="text-align:left">一个应用程序框架，您可以将它集成到任何 .NET/C# 应用程序中。</p> 
<h2 style="text-align:left">安装</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank">Package Manager</a></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre>Install-Package<span style="color:#bbbbbb"> </span>Furion</pre> 
 </div> 
</div> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank">.NET CLI</a></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre>dotnet<span style="color:#bbbbbb"> </span>add<span style="color:#bbbbbb"> </span>package<span style="color:#bbbbbb"> </span>Furion</pre> 
 </div> 
</div> 
<h2 style="text-align:left">例子</h2> 
<p style="text-align:left">我们在<a href="https://dotnetchina.gitee.io/furion">主页</a>上有不少例子，这是让您入门的第一个：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>var</strong> services = Inject.<strong>Create</strong>();
services.<strong>AddRemoteRequest</strong>();
services.<strong>Build</strong>();

<strong>var</strong> responseString = <strong>await</strong> <span style="color:#dd2200">"https://dotnet.microsoft.com/"</span>.<strong>GetAsStringAsync</strong>();
responseString.<strong>LogInformation</strong>();</pre> 
 </div> 
</div> 
<h2 style="text-align:left">文档</h2> 
<p style="text-align:left">您可以在<a href="https://dotnetchina.gitee.io/furion">主页</a>或<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffurion.pro%2F" target="_blank">备份主页</a>找到 Furion 文档。</p> 
<h2 style="text-align:left">贡献</h2> 
<p style="text-align:left">该存储库的主要目的是继续发展 Furion 核心，使其更快、更易于使用。 Furion 的开发在 <a href="https://gitee.com/dotnetchina/Furion">Gitee</a> 上公开进行，我们感谢社区贡献错误修复和改进。阅读<a href="https://dotnetchina.gitee.io/furion/docs/contribute">贡献指南</a>内容，了解如何参与改进 Furion。</p> 
<h2 style="text-align:left">许可证</h2> 
<p style="text-align:left">Furion 采用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flicense.coscl.org.cn%2FMulanPSL2" target="_blank">MulanPSL-2.0</a> 开源许可证，了解<a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE">项目许可证</a>。</p> 
<div style="text-align:left"> 
 <div> 
  <pre>Copyright (c) 2020-2021 百小僧, Baiqian Co.,Ltd.
Furion is licensed under Mulan PSL v2.
You can use this software according to the terms andconditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
            http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUTWARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.</pre> 
 </div> 
</div> 
<h2>日志</h2> 
<ul> 
 <li> <p><strong>新特性</strong></p> 
  <ul> 
   <li>[新增] <code>Furion.Tools.CommandLine</code> 拓展库 <a href="https://gitee.com/dotnetchina/Furion/tree/master/tools/Furion.Tools/Furion.Tools.CommandLine">查看源码</a></li> 
   <li>[新增] 基于 <code>AsyncLocal<T></code> 的 <code>CallContext</code> 实现 <a href="https://gitee.com/dotnetchina/Furion/commit/9057a212aab8057b668086bd14369fa68ce120df">9057a21</a></li> 
   <li>[新增] 远程请求可配置请求移除重试策略 <a href="https://gitee.com/dotnetchina/Furion/commit/656da87a667c2da7d82425cdcd47146e99602d65">656da87</a></li> 
   <li>[新增] 远程请求 <code>OnRequestFailded</code> 事件 <a href="https://gitee.com/dotnetchina/Furion/commit/4a3da4ba2c69380fe5f8c2fda80054544c0a3468">4a3da4b</a></li> 
  </ul> </li> 
 <li> <p><strong>突破性变化</strong></p> 
  <ul> 
   <li>[移除] <code>Scoped</code> 所有带返回值方法 <a href="https://gitee.com/dotnetchina/Furion/commit/656da87a667c2da7d82425cdcd47146e99602d65">656da87</a></li> 
   <li>[调整] <strong>在 <code>ConfigureService</code> 中调用 <code>App.GetOptions<>()</code> 获取配置逻辑</strong> <a href="https://gitee.com/dotnetchina/Furion/commit/afa4ac347152ccac37bd1d0f9af1e8ffb665a662">afa4ac3</a></li> 
  </ul> </li> 
 <li> <p><strong>问题修复</strong></p> 
  <ul> 
   <li>[修复] v2.16+ 版本重构 <code>AppDbContextBuilder</code> 之后写错实体类型 <a href="https://gitee.com/dotnetchina/Furion/issues/I45E6M">#I45E6M</a></li> 
   <li>[修复] 远程请求单个值序列化错误处理方式 <a href="https://gitee.com/dotnetchina/Furion/commit/3282eba2cecb505e339ef3f9c8e823f84dcb43f0">3282eba</a></li> 
   <li>[修复] v2.17.3+ 单元测试创建 <code>TestServer</code> bug <a href="https://gitee.com/dotnetchina/Furion/issues/I45JR3">#I45JR3</a></li> 
   <li>[修复] <code>Retry.Invoke</code> 正常方法死循环 bug <a href="https://gitee.com/dotnetchina/Furion/pulls/392">!392</a></li> 
   <li>[修复] 刷新 <code>Token</code> 生成新 <code>Token</code> 存在数组/集合类型导致 <code>Key</code> 重复异常问题 <a href="https://gitee.com/dotnetchina/Furion/commit/aeea2b1b19434f3171bd1c77be057ca36ecf9be2">aeea2b1</a></li> 
   <li>[修复] 远程请求序列化引用类型对象（不含 <code>string</code>）不正确的处理 <a href="https://gitee.com/dotnetchina/Furion/commit/93cf63a023f3372b80edb5debc46271d2281318a">93cf63a</a></li> 
   <li>[修复] <code>AppDbContext</code> 默认租户属性受工作单元影响问题 <a href="https://gitee.com/dotnetchina/Furion/commit/e51557fdf37ae5646b2ea37c227c970eccdbed38">e51557f</a></li> 
  </ul> </li> 
 <li> <p><strong>文档</strong></p> 
  <ul> 
   <li>[新增] 包管理工具文档</li> 
   <li>[更新] 模板引擎、<code>Sql</code> 操作，<code>数据库上下文</code> 等等文档</li> 
  </ul> </li> 
</ul> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-00b21ee50d908c498ae91faed4f58a52978.png" width="1915" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-2166f5f2c1d77df63f1c37d8d1a844af30d.png" width="1911" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-75770673dea1c4672a1d32d2c49c279063a.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            