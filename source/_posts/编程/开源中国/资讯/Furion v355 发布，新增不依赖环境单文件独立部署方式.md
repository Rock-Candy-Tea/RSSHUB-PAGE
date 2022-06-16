
---
title: 'Furion v3.5.5 发布，新增不依赖环境单文件独立部署方式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fa3e6297cd2e313047fce79793200bf90e1.png'
author: 开源中国
comments: false
date: Thu, 16 Jun 2022 16:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fa3e6297cd2e313047fce79793200bf90e1.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2><strong>历史背景</strong></h2> 
<p style="color:#1c1e21; text-align:start">自<span> </span><code>.NET Core 3</code><span> </span>起，微软就提供了单文件发布的技术支持，但实际上并不是<span> </span><code>.NET</code><span> </span>所有<span> </span><code>CLR</code><span> </span>都支持单文件发布，如<span> </span><code>Microsoft.Extensions.DependencyModel</code><span> </span>包本身不支持单文件发布，原因是内部使用了<span> </span><code>Assembley.CodeBase</code>。</p> 
<p style="color:#1c1e21; text-align:start"><strong>好巧不巧</strong>，<code>Furion</code><span> </span>中招了，在过去两年中，<code>Furion</code><span> </span>依赖该包的<span> </span><code>DependencyContext.Default</code><span> </span>特性进行程序集扫描，所以单文件发布也就成了<span> </span><code>Furion</code><span> </span>不愿提起的痛！！！</p> 
<p style="color:#1c1e21; text-align:start"><strong>终于，在<span> </span><code>Furion v3.5.2+</code><span> </span>版本想出了新的解决方案，自此彻底解决了单文件发布的问题。</strong></p> 
<div style="text-align:start"> 
 <div> 
  <p><code>.NET</code><span> </span>官方单文件发布说明</p> 
 </div> 
 <div> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fdotnet%2Fcore%2Fdeploying%2Fsingle-file%2Foverview" target="_blank">https://docs.microsoft.com/zh-cn/dotnet/core/deploying/single-file/overvie</a></p> 
 </div> 
</div> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li> <p>[新增] <code>sql</code> 转实体支持多种命名策略（纯大写，纯小写，带下划线分割等等），如 <code>Oracle</code> 数据库 <a href="https://gitee.com/dotnetchina/Furion/commit/a90e24516387e088b2c427e6b99d3dab937116c9" target="_blank">a90e245</a></p> </li> 
    <li> <p>[新增] <code>FS.InitalContentTypeProvider()</code> 拓展方法，获取系统内所有支持的 <code>Content-Type</code> 文件提供器 <a href="https://gitee.com/dotnetchina/Furion/commit/6099900472d93dab7012f0b091b05c914be11c4a" target="_blank">6099900</a></p> </li> 
    <li> <p>[新增] <code>TP.Wrapper(...)</code> 拓展方法，主要用来生成规范化的日志模板 <a href="https://gitee.com/dotnetchina/Furion/commit/427999aba4847522ea91c42df6164e5fe69c5bc0" target="_blank">427999a</a></p> </li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li><strong>[解决]<span> </span>彻底解决了<span> </span><code>Furion</code><span> </span>不能单文件发布的问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/7e8e0b708bcdac670aa835dec5cd494d41ff3648" target="_blank">7e8e0b7</a></strong></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[修复]<span> </span>框架规范化文档<span> </span><code>Swagger</code><span> </span>不支持<span> </span><code>Controller</code><span> </span>派生类<span> </span><code>api</code><span> </span>路由问题，原生<span> </span><code>ASP.NET</code><span> </span>是支持的<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/29e47bce3678767c4793ad254777704ab9dd7e03" target="_blank">29e47bc</a></li> 
    <li>[修复]<span> </span>基于<span> </span><code>Schema</code><span> </span>多租户配置无效问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/6f820ce0f28dd27a6e265b969b5b4095de676106" target="_blank">6f820ce</a></li> 
    <li>[修复]<span> </span>指定实体<span> </span><code>[Table(schema:"dbo")]</code><span> </span>特性后<span> </span><code>Schema</code><span> </span>无效问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/6f820ce0f28dd27a6e265b969b5b4095de676106" target="_blank">6f820ce</a></li> 
    <li>[修复]<span> </span>数据库视图不支持<span> </span><code>Schema</code><span> </span>配置问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/6f820ce0f28dd27a6e265b969b5b4095de676106" target="_blank">6f820ce</a></li> 
    <li>[修复]<span> </span>规范化结果极端情况下出现<span> </span><code>空异常</code><span> </span>问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/c9b0ef09427418e2ccb88d3a4c02e7a29d9d510e" target="_blank">c9b0ef</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li> <p>[调整] 对象映射默认支持忽略大小写 <a href="https://gitee.com/dotnetchina/Furion/pulls/486" target="_blank">!486</a></p> </li> 
   </ul> </li> 
  <li> <p><strong>文档</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span><code>Furion</code><span> </span>单文件发布文档</li> 
    <li>[新增]<span> </span><code>Furion + SqlSugar</code><span> </span>脚手架文档</li> 
    <li>[新增]<span> </span><code>TP</code><span> </span>全局静态类文档</li> 
    <li>[更新]<span> </span>事件总线文档、选项文档、即时通讯文档、<code>.NET5</code><span> </span>升级<span> </span><code>.NET6</code><span> </span>文档、依赖注入文档、跨域文档、数据加解密文档</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2>本期文档</h2> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-fa3e6297cd2e313047fce79793200bf90e1.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-c14433fe86a1a4e3db0f2383b0d34672e0b.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-3c639126a3ed44e1041565175ff990fcee3.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-b2a039139c652c9e5e4b33f5df0233be9d7.png" width="1918" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-7adddaf8e92558e7a2fb519d63b06ec6733.png" width="1920" referrerpolicy="no-referrer">​​​​​​​</p>
                                        </div>
                                      
</div>
            