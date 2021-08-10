
---
title: '🔥 Furion v2.17 发布，带来全新的 IPC 进程通信模块'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Tue, 10 Aug 2021 11:10:00 GMT
thumbnail: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:center"><img height="80" src="https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png" width="80" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <p style="text-align:center"><a href="https://gitee.com/dotnetchina/Furion/stargazers"><img alt="star" src="https://gitee.com/dotnetchina/Furion/badge/star.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/members"><img alt="fork" src="https://gitee.com/dotnetchina/Furion/badge/fork.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fstargazers" target="_blank"><img alt="GitHub stars" src="https://img.shields.io/github/stars/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fnetwork" target="_blank"><img alt="GitHub forks" src="https://img.shields.io/github/forks/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/badge/license-MulanPSL--2.0-orange" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></p> 
</div> 
<div style="text-align:left"> 
 <p style="text-align:center">让 .NET 开发更简单，更通用，更流行。</p> 
</div> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] <code>IPC（Inter-Process Communication，进程间通信）</code> 模块功能，目前提供进程内通信和共享内存进程外通讯 <a href="https://gitee.com/dotnetchina/Furion/tree/master/framework/Furion/ProcessChannel">ProcessChannel</a></li> 
    <li>[新增] 远程请求 <code>application/xml</code> 和 <code>text/xml</code> 默认支持 <a href="https://gitee.com/dotnetchina/Furion/commit/4753a1aed527a6282fe6c05036de9d50bd3b3dd8">4753a1a</a></li> 
    <li>[新增] 控制台全局异常拦截 <a href="https://gitee.com/dotnetchina/Furion/commit/4a4fe1f40e1856ea36a0c0d19ca625d3f7bf95b7">4a4fe1f</a></li> 
    <li>[新增] 支持自定义 <code>.json</code> 配置文件扫描目录 <a href="https://gitee.com/dotnetchina/Furion/commit/3e2910a8b775fb6323e293b020bbe7cdfb4c6436">3e2910a</a></li> 
    <li>[新增] 支持数据库实体接口显式实现接口配置 <a href="https://gitee.com/dotnetchina/Furion/commit/9610a0a481f4f78770bc2fc3ed4cabbef2a8f937">9610a0a</a></li> 
    <li>[新增] 控制台应用程序全局拦截 <code>[IfException]</code> 支持 <a href="https://gitee.com/dotnetchina/Furion/commit/4a4fe1f40e1856ea36a0c0d19ca625d3f7bf95b7">4a4fe1f</a></li> 
    <li>[新增] 依赖注入模块接口可以限制实现类生存周期，实现类也支持复写生存周期 <a href="https://gitee.com/dotnetchina/Furion/commit/d2ce089130300cdd8b1bc6792f325c5d38ee9404">d2ce089</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[抽离] <code>Oops.Retry()</code> 重试策略功能至新类：<code>Retry.Invoke()</code> <a href="https://gitee.com/dotnetchina/Furion/commit/6a7bbd0b30a653b9a42d340a63520485aa6bbfa4">6a7bbd0</a></li> 
    <li>[移除] <code>IHttpContextAccessor.SigninToSwagger()</code> 拓展，请使用 <code>IHttpContextAccessor.HttpContext.SigninToSwagger()</code>，退出也一样</li> 
    <li>[移除] 全局处理 <code>Request Body</code> 重复读处理 <code>Request.EnableBuffering()</code> <a href="https://gitee.com/dotnetchina/Furion/commit/d92c24bdb43bfb01643007ebb6a4ee42a5c738e9">d92c24b</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 规范化状态码过滤逻辑错误问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I44JYS">#I44JYS</a></li> 
    <li>[修复] 非关系型数据库（内存数据库）注册及操作异常 <a href="https://gitee.com/dotnetchina/Furion/commit/e1676512a54374427bedbde17cd8cb59d7852557">e167651</a></li> 
    <li>[修复] 远程请求默认序列化问题 <a href="https://gitee.com/dotnetchina/Furion/commit/a55603bf7ed109296375dbeffc31591a6f8f8e49">a55603b</a></li> 
    <li>[修复] 定时任务零点/整点提前一秒触发问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I4321L">#I4321L</a></li> 
    <li>[修复] 友好异常在子类重写抽象类方法内部抛异常无法获取的问题 <a href="https://gitee.com/dotnetchina/Furion/commit/4a4fe1f40e1856ea36a0c0d19ca625d3f7bf95b7">4a4fe1f</a></li> 
    <li>[修复] 修复非 Web 项目抛异常问题 <a href="https://gitee.com/dotnetchina/Furion/commit/4a4fe1f40e1856ea36a0c0d19ca625d3f7bf95b7">4a4fe1f</a></li> 
    <li>[修复] 数据库实体模型贴 <code>[NotMapper]</code> 特性无效 <a href="https://gitee.com/dotnetchina/Furion/issues/I44MNO">#I44MNO</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[调整] Swagger 生成泛型 SchemaIds 默认连接符，由 <code>Of</code> 改为 <code>_</code> <a href="https://gitee.com/dotnetchina/Furion/commit/81946b64e81d9e290f80cd5bcebdb69c99001153">81946b6</a></li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div> 
    <p><img height="1008" src="https://oscimg.oschina.net/oscnet/up-89fcfefadbc4080b5366b9f13c42f2a0ed9.png" width="1913" referrerpolicy="no-referrer"></p> 
    <h2>框架特点</h2> 
    <ul> 
     <li>全新面貌：基于 <code>.NET5/6</code> 平台，没有历史包袱</li> 
     <li>极少依赖：框架只依赖两个第三方包</li> 
     <li>极易入门：只需要一个 <code>Inject()</code> 即可完成配置</li> 
     <li>极速开发：内置丰富的企业应用开发功能</li> 
     <li>极其灵活：轻松面对多变复杂的需求</li> 
     <li>极易维护：采用独特的架构思想，只为长久维护设计</li> 
     <li>完整文档：提供完善的开发文档</li> 
     <li><strong>跨全平台：支持所有主流操作系统及 .NET 全部项目类型</strong></li> 
    </ul> 
    <h2>文档视频</h2> 
    <ul> 
     <li><strong>国内文档</strong>：<a href="https://dotnetchina.gitee.io/furion">https://dotnetchina.gitee.io/furion</a></li> 
     <li>国外文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffurion.pro%2F" target="_blank">https://furion.pro</a></li> 
     <li>视频教程：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspace.bilibili.com%2F695987967" target="_blank">https://space.bilibili.com/695987967</a></li> 
    </ul> 
    <h2>开源地址</h2> 
    <ul> 
     <li>Gitee：<a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
     <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmonksoul%2FFurion" target="_blank">https://github.com/monksoul/Furion</a></li> 
     <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank">https://www.nuget.org/packages/Furion</a></li> 
    </ul> 
    <h2>贡献代码</h2> 
    <p><code>Furion</code> 遵循 <a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE">MulanPSL-2.0</a> 开源协议，欢迎大家提交 <code>Pull Request</code> 或 <code>Issue</code>。如果要为项目做出贡献，请查看 <a href="https://dotnetchina.gitee.io/furion/docs/contribute">贡献指南</a>。感谢每一位为 <code>Furion</code> 贡献代码的朋友。</p> 
    <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgiteye.net%2Fchart%2FZS49EPL6" target="_blank"><img alt="Furion 贡献者画像" src="https://chart.giteye.net/gitee/dotnetchina/Furion/ZS49EPL6.png" referrerpolicy="no-referrer"></a></p> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            