
---
title: '庆五一，.NET5_6 框架 Furion v3.2.0 发布，Stars 达 8000'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7ef31a4b8e33a1e752342ad8ad722bbac43.png'
author: 开源中国
comments: false
date: Fri, 29 Apr 2022 06:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7ef31a4b8e33a1e752342ad8ad722bbac43.png'
---

<div>   
<div class="content">
                                                                                            <h2>阶段总结</h2> 
<p><span style="color:#d35400"><strong>Furion 框架在 Gitee 平台提交了 4113 次更改，编写了 190万字的使用文档，贡献者 189 人，Nuget 总安装量 239 万。</strong></span></p> 
<blockquote> 
 <ul> 
  <li>项目地址：<a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
  <li>Nuget 安装量：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fprofiles%2Fmonk.soul" target="_blank">https://www.nuget.org/profiles/monk.soul</a></li> 
  <li>文档地址：<a href="https://dotnetchina.gitee.io/furion/">https://dotnetchina.gitee.io/furion/</a></li> 
 </ul> 
</blockquote> 
<p><img height="1007" src="https://oscimg.oschina.net/oscnet/up-7ef31a4b8e33a1e752342ad8ad722bbac43.png" width="1314" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p style="margin-left:0; margin-right:0"><strong>新特性</strong></p> 
   <ul> 
    <li>[新增]<span> </span><code>IFormFile</code><span> </span>拓展方法<span> </span><code>ToByteArray()</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/da69640da2331e2c8582b88bbda965c5ad7ecbe0">da69640</a></li> 
    <li>[新增] 规范化文档<span> </span><code>ServeDir</code><span> </span>虚拟目录配置功能，支持一键将一级目录切换至二级目录部署（IIS）<a href="https://gitee.com/dotnetchina/Furion/commit/87183921ac8b6f9856db01b4de679b858a58e753">8718392</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>突破性变化</strong></p> 
   <ul> 
    <li>[更新] 所有依赖包至最新版</li> 
    <li>[重构] 依赖注入模块核心代码，移除注册服务采用反射机制，减少反射性能损耗<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/acdb3157af92891610a1ba6d317b6af3f09e233f">acdb315</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复]<span> </span><code>Swagger</code><span> </span>的<span> </span><code>schema</code><span> </span>类型如果是<span> </span><code>C# Object</code><span> </span>类型无法正确生成前端代码问题<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fswagger-api%2Fswagger-codegen-generators%2Fissues%2F692">Swagger 官方 Issue</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/1a252747fd60fc87a8ed4425c8edf7803f96ce43">1a25274</a></li> 
    <li>[修复]<span> </span><code>Worker Service</code><span> </span>发布成<span> </span><code>Windows Services</code><span> </span>时日志绝对路径问题 感谢<span> </span><a href="https://gitee.com/jacoat">@jacoat</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/467">!467</a></li> 
    <li>[修复]<span> </span><code>Nginx</code><span> </span>和<span> </span><code>IIS</code><span> </span>对二级虚拟目录配置不同导致<span> </span><code>404</code><span> </span>问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/87183921ac8b6f9856db01b4de679b858a58e753">8718392</a></li> 
    <li>[修复] 远程请求模块未初始化<span> </span><code>OnRequestFailded</code><span> </span>导致空异常问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I54PK7">#I54PK7</a></li> 
    <li>[修复] 依赖注入反射出现<span> </span><code>Not found Method</code><span> </span>bug<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I546L1">#I546L1</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>其他更改</strong></p> 
   <ul> 
    <li>[调整] 定时任务失败后异常处理逻辑，感谢<span> </span><a href="https://gitee.com/cxs1992">@程小胜</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/463">!463</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>文档</strong></p> 
   <ul> 
    <li>[更新] 定时任务文档，日志文档</li> 
    <li>[新增] 文件上传/下载 文档，包含单文件/多文件/Base64/Byte[]</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<p><img height="1007" src="https://oscimg.oschina.net/oscnet/up-de5f9f3457c08d371ffbe417c102a7e1098.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            