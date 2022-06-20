
---
title: 'Furion v3.6.4 发布，贡献者破 200 人'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-afeae29b6d6421d88dc7d85928b6340c0ce.png'
author: 开源中国
comments: false
date: Mon, 20 Jun 2022 16:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-afeae29b6d6421d88dc7d85928b6340c0ce.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>前言</h2> 
<p>近期 Furion 框架用户暴增，仿佛回到了刚诞生的时候，每天都有很多需求，一些隐藏两年都没发现的 bug 被浮出水面，更新更是一天一个版本迭代~</p> 
<p>从 v3.6.0 版本开始，Furion 对通用主机进行的重构，终于拥有辨识度极高的入门体验以及个性化的错误页。</p> 
<p><strong>另外值得庆祝的是，Furion 终于迎来了第 200 个贡献者。😊</strong></p> 
<h2>框架信息</h2> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/dotnetchina/Furion" target="_blank">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmonksoul%2FFurion" target="_blank">https://github.com/monksoul/Furion</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank">https://www.nuget.org/packages/Furion</a></li> 
 <li>国内文档：<a href="https://dotnetchina.gitee.io/furion" target="_blank">https://dotnetchina.gitee.io/furion</a></li> 
 <li>国外文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffurion.icu%2F" target="_blank">https://furion.icu</a></li> 
</ul> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-afeae29b6d6421d88dc7d85928b6340c0ce.png" width="1918" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span><code>Serve.Run()</code><span> </span>极简主机模式，真正实现极速入门。<a href="https://gitee.com/dotnetchina/Furion/commit/95cac5b391b70d73bfc94147ee40eef529b2eec6" target="_blank">95cac5b</a></li> 
    <li>[新增]<span> </span><code>TP.Wrapper(...)</code><span> </span>拓展方法，主要用来生成规范化的日志模板<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/427999aba4847522ea91c42df6164e5fe69c5bc0" target="_blank">427999a</a></li> 
    <li>[支持]<span> </span>项目类型为<span> </span><code><Project Sdk="Microsoft.NET.Sdk"></code><span> </span>的控制台项目<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/fb08a6548d49921aa143d01389a2592b92e94e31" target="_blank">fb08a65</a></li> 
    <li>[新增]<span> </span><code>BadPageResult</code><span> </span>错误页面类型<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/495" target="_blank">!494</a></li> 
    <li>[新增]<span> </span><code>[SchemaId]</code><span> </span>特性，解决不同程序集相同的类名生成<span> </span><code>Swagger</code><span> </span>的<span> </span><code>SchemaId</code><span> </span>冲突问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5D3CU" target="_blank">#I5D3CU</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[支持]<span> </span>项目类型为<span> </span><code><Project Sdk="Microsoft.NET.Sdk"></code><span> </span>的控制台项目<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/fb08a6548d49921aa143d01389a2592b92e94e31" target="_blank">fb08a65</a></li> 
    <li>[新增]<span> </span><code>Serve.Run()</code><span> </span>极简主机模式，真正实现极速入门。<a href="https://gitee.com/dotnetchina/Furion/commit/95cac5b391b70d73bfc94147ee40eef529b2eec6" target="_blank">95cac5b</a></li> 
    <li>[调整]<span> </span>未启用规范化结果时，<code>MVC</code><span> </span>验证失败返回<span> </span><code>BadPageResult()</code><span> </span>页面类型<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/495" target="_blank">!494</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[修复]<span> </span>修复默认注册的<span> </span><code>services.AddResponseCaching();</code><span> </span>服务导致<span> </span><code>.axd</code><span> </span>内嵌资源请求错误问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/495" target="_blank">!495</a></li> 
    <li>[修复]<span> </span><code>Oracle</code><span> </span>数据库执行<span> </span><code>sql</code><span> </span>必须要求命令参数和<span> </span><code>sql</code><span> </span>语言参数数量一致<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5D057" target="_blank">#I5D057</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[调整]<span> </span>开放验证服务选项<span> </span><code>SuppressModelStateInvalidFilter</code><span> </span>属性为可配置<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/495" target="_blank">!494</a></li> 
   </ul> </li> 
  <li> <p><strong>文档</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span><code>Serve.Run()</code><span> </span>文档</li> 
    <li>[新增]<span> </span><code>HttpContext</code><span> </span>文档</li> 
    <li>[新增]<span> </span><code>GlobalUsings</code><span> </span>文档</li> 
    <li>[新增]<span> </span><code>TP</code><span> </span>全局静态类文档</li> 
    <li>[更新]<span> </span>跨域文档</li> 
   </ul> </li> 
  <li> <p><strong>精彩贡献</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li><a href="https://gitee.com/dotnetchina/Furion/pulls/494" target="_blank">!494</a><span> </span>优秀<span> </span><code>Pull Request</code><span> </span>辩论典范</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2>本期亮点</h2> 
<p><strong>1. 极简入门体验</strong></p> 
<pre><code class="language-cs">Serve.Run();

[DynamicApiController]
public class HelloService
&#123;
    public string Say()
    &#123;
        return "Hello, Furion";
    &#125;
&#125;</code></pre> 
<p><img src="https://dotnetchina.gitee.io/furion/img/07.png" referrerpolicy="no-referrer"></p> 
<p><strong>2. 内置错误页</strong></p> 
<pre><code class="language-cs">using Furion.FriendlyException;

public IActionResult Add(Person person)
&#123;
    if(!ModelState.IsValid)
    &#123;
        return new BadPageResult();
    &#125;
&#125;</code></pre> 
<p><img src="https://dotnetchina.gitee.io/furion/img/er1.png" referrerpolicy="no-referrer"></p> 
<h2>新增文档</h2> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-172935390e02406a4626e98ee7b87cf3380.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1078" src="https://oscimg.oschina.net/oscnet/up-e0dfd89fd2088a581dc07cff05a5cc958d3.png" width="1907" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-63c91e479f0df0c3077401aab31bad04486.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-aff20fa5eaadcd0896be91c14f623a96c60.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            