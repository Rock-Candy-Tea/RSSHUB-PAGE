
---
title: 'Furion 让开发者重新认识了 .NET，v2.4.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Wed, 12 May 2021 14:34:00 GMT
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
<h2>庆祝 5K 说点</h2> 
<p>自 2020年09月01日 发布以来，Furion 一直高速发展，Stars 趋势图也勾勒出了指数增长的线条美，截至今日，诞生 7个月12天。</p> 
<p>今天，Furion 项目在 Gitee 平台突破了 5K Stars，QQ 交流群成员达 6200 +，Nuget 下载破 260K。或许 5K Stars 对 Java 项目来说只是个小目标，但对国内 .NET 开源项目来说，无疑是梦想中的目标。</p> 
<p>当然 Stars 的多少并不能决定项目优秀与否，但是从侧面也能反映出 .NET 正在崛起。</p> 
<p><strong>作者贡献度：</strong></p> 
<p><a href="https://gitee.com/monksoul">https://gitee.com/monksoul</a></p> 
<p><img height="294" src="https://oscimg.oschina.net/oscnet/up-b81cc974f9c00b4a05adada8ad40ae26144.png" width="927" referrerpolicy="no-referrer"></p> 
<p><strong>项目概况图：</strong></p> 
<p><a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></p> 
<p><img height="964" src="https://oscimg.oschina.net/oscnet/up-aa180a85b8e66c0225736c51925db0eb56c.png" width="1266" referrerpolicy="no-referrer"></p> 
<p><img height="909" src="https://oscimg.oschina.net/oscnet/up-72ba578ab37be134894088e3cb20b4186a6.png" width="893" referrerpolicy="no-referrer"></p> 
<p><strong>Stars 趋势图：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwhnb.wang%2Fdotnetchina%2FFurion%3Fe%3D43200" target="_blank">https://whnb.wang/dotnetchina/Furion?e=43200</a></p> 
<p><img alt src="https://whnb.wang/img/dotnetchina/Furion?e=43200" referrerpolicy="no-referrer"></p> 
<p><strong>贡献者画像：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgiteye.net%2Fchart%2FZS49EPL6" target="_blank">https://giteye.net/chart/ZS49EPL6</a></p> 
<p><img alt src="https://chart.giteye.net/gitee/dotnetchina/Furion/ZS49EPL6.png" referrerpolicy="no-referrer"></p> 
<p><strong>框架文档：</strong></p> 
<p><a href="https://dotnetchina.gitee.io/furion/">https://dotnetchina.gitee.io/furion/</a></p> 
<p><img height="1007" src="https://oscimg.oschina.net/oscnet/up-4b8aaa43f4419048699461e89a000cdf3e9.png" width="1918" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 支持自动加载模块化/插件 <code>.xml</code> 注释文件 <a href="https://gitee.com/dotnetchina/Furion/issues/I3Q7XY">#I3Q7XY</a></li> 
    <li>[新增] <code>AppDbContext.FailedAutoRollback</code> 属性，可配置事务是否自动回滚 <a href="https://gitee.com/dotnetchina/Furion/issues/I3QOUS">#I3QOUS</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[升级] <strong>.NET 5 SDK 为 5.0.6 版本</strong></li> 
    <li>[新增] <code>IJsonSerializerProvider.GetSerializerOptions()</code> 接口方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I3QIJN">#I3QIJN</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 通过 <code>services.AddInject()</code> 方式注册，模块化/插件不加载 <a href="https://gitee.com/dotnetchina/Furion/issues/I3Q7XH">#I3Q7XH</a></li> 
    <li>[修复] 种子数据返回 <code>null</code> 报空异常 <a href="https://gitee.com/dotnetchina/Furion/issues/I3QCM5">#I3QCM5</a></li> 
    <li>[修复] 通过 <code>Clay.Object</code> 创建粘土对象后属性变小写问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3QRV3">#I3QRV3</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[优化] <code>Furion</code> 框架底层性能，减少内存占用，提高应用初始化速度 <a href="https://gitee.com/dotnetchina/Furion/commit/92f8cc1">92f8cc1</a></li> 
   </ul> </li> 
  <li> <p><strong>文档变化</strong></p> 
   <ul> 
    <li>[更新] JSON 序列化文档、规范化结果文档、数据库上下文文档</li> 
   </ul> </li> 
  <li> <p><strong>问答答疑</strong></p> 
   <ul> 
    <li>[答疑] <code>InsertOrUpdateNowAsync</code> 报错 <a href="https://gitee.com/dotnetchina/Furion/issues/I3QKO5">#I3QKO5</a></li> 
   </ul> </li> 
  <li> <p><strong>不做实现</strong></p> 
   <ul> 
    <li>[废弃] 定时任务自定义 <code>Failed</code> 事件 <a href="https://gitee.com/dotnetchina/Furion/issues/I3QCM2">#I3QCM2</a></li> 
    <li>[废弃] 模块化动态生成数据库表 <a href="https://gitee.com/dotnetchina/Furion/issues/I3QH3G">#I3QH3G</a></li> 
    <li>[废弃] 建议事件总线新增 MQ 支持 <a href="https://gitee.com/dotnetchina/Furion/issues/I3QWZ4">#I3QWZ4</a></li> 
    <li>[废弃] 重构规范化整个模块代码 <a href="https://gitee.com/dotnetchina/Furion/issues/I3NFT7">#I3NFT7</a></li> 
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
            