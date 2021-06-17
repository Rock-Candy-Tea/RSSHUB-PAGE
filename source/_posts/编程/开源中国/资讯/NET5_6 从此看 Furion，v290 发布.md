
---
title: '.NET5_6 从此看 Furion，v2.9.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Thu, 17 Jun 2021 07:40:00 GMT
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
<p>时间飞逝，转眼间 Furion 诞生 <span style="background-color:#ffffff; color:#000000">289 天。</span></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#000000">从无人知晓到现在 .NET 人人皆知；</span></li> 
 <li><strong><span style="background-color:#ffffff; color:#000000">从 0 个 star 到现在近 6000 stars；</span></strong></li> 
 <li><span style="background-color:#ffffff; color:#000000">从下载量 0K 到现在近 500K；</span></li> 
 <li><strong><span style="background-color:#ffffff; color:#000000">从 QQ 群 1 人 到现在 7300 人；</span></strong></li> 
 <li><span style="background-color:#ffffff; color:#000000">从 1 次提交到现在 3000 次提交；</span></li> 
 <li><span style="background-color:#ffffff; color:#000000">从 0 个 Issue 到现在 780 个 Issues；</span></li> 
 <li><span style="background-color:#ffffff; color:#000000">从 0 个 Pull Request 到现在 330 个 Pull Request；</span></li> 
 <li><strong><span style="background-color:#ffffff; color:#000000">从 1 个贡献者到现在 137 个贡献者；</span></strong></li> 
 <li><span style="background-color:#ffffff; color:#000000">从...</span></li> 
</ul> 
<p>皇天不负苦心人，Furion 正在吸引越来越多的人使用。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-d3fec00a0f1e69d66a49a61eaa75c00882b.png" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] <strong>应用全局未托管资源监听，并实现特定时机释放非托管资源</strong> <a href="https://gitee.com/dotnetchina/Furion/issues/I3VXAU">#I3VXAU</a></li> 
    <li>[新增] 不包含 <code>EntityFramework.Core</code> 版本的 <code>Furion.Pure</code> 包<a href="https://gitee.com/dotnetchina/Furion/issues/I3VGW8">#I3VGW8</a></li> 
    <li>[新增] swagger 支持设置多语言方式，设置的语言自动添加到 api 地址后面 <a href="https://gitee.com/dotnetchina/Furion/issues/I3VDTD">#I3VDTD</a></li> 
    <li>[新增] 动态 WebAPI 支持 <code>[FromRoute]</code> 非必填（选填）参数设置 <a href="https://gitee.com/dotnetchina/Furion/issues/I3VFIM">#I3VFIM</a></li> 
    <li>[新增] 动态 WebAPI 参数支持配置路由约束 <a href="https://gitee.com/dotnetchina/Furion/issues/I3VFIR">#I3VFIR</a></li> 
    <li>[新增] <code>MD5</code> 和 <code>DESC</code> 加密支持 <code>大写</code> 输出 <a href="https://gitee.com/dotnetchina/Furion/pulls/326">#326</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[新增] <code>Furion</code> 所有包生成 <code>.snupkg</code> 包，支持开发阶段直接调试 <code>Furion</code> 所有包源码 <a href="https://gitee.com/dotnetchina/Furion/issues/I3VFIX">#I3VFIX</a></li> 
    <li>[调整] <code>repository.BuildChange()</code> 方法的返回值，多返回一个 <code>IServiceScope</code> 对象 <a href="https://gitee.com/dotnetchina/Furion/issues/I3VX3D">#I3VX3D</a></li> 
    <li>[调整] <code>JWT</code> 刷新 <code>Token</code> 方法 <code>AutoRefreshToken</code> 参数 <code>days</code> 改为 <code>minutes</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3VXNB">#I3VXNB</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] <code>App.GetOptionsSnapshot<></code> 从根服务解析异常 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3VS2X">#I3VS2X</a></li> 
    <li>[修复] 修复远程请求如果出现异常，返回 <code>Stream</code> 为 null 导致异常的问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3VSTU">#I3VSTU</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[优化] 运行时内存，实现请求结束自动释放未托管资源 <a href="https://gitee.com/dotnetchina/Furion/issues/I3VXAU">#I3VXAU</a></li> 
   </ul> </li> 
  <li> <p><strong>文档变化</strong></p> 
   <ul> 
    <li>[更新] <code>App</code> 静态类文档、远程请求文档、分表分库文档</li> 
   </ul> </li> 
  <li> <p><strong>问答答疑</strong></p> 
   <ul> 
    <li>[答疑] 动态 WebAPI，自定义根据方法名生成 [HttpMethod] 规则报错 <a href="https://gitee.com/dotnetchina/Furion/issues/I3VKQG">#I3VKQG</a></li> 
    <li>[答疑] <code>InsertAsync</code> 的时候提示 <code>ID</code> 为空 <a href="https://gitee.com/dotnetchina/Furion/issues/I3VS7E">#I3VS7E</a></li> 
   </ul> </li> 
  <li> <p><strong>不做实现</strong></p> </li> 
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
            