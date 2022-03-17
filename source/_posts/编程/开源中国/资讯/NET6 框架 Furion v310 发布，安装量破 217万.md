
---
title: '.NET6 框架 Furion v3.1.0 发布，安装量破 217万'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8be609b8137519ea2aed7fa4a0846da4deb.png'
author: 开源中国
comments: false
date: Thu, 17 Mar 2022 05:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8be609b8137519ea2aed7fa4a0846da4deb.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>说点什么</h2> 
<p>距上一次更新已过去3个多月有余，这段时间不活跃主要原因是公司技术转型和私人问题耽搁了。</p> 
<p>那么还是对项目做现阶段总结：</p> 
<blockquote> 
 <ul> 
  <li><strong>Stars</strong>：7.8K</li> 
  <li><strong>Forked</strong>：3.3K</li> 
  <li><strong>Watching</strong>：3K</li> 
  <li><strong>Contributors</strong>：184人</li> 
  <li><strong>Nuget 总安装</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fprofiles%2Fmonk.soul" target="_blank">217万</a></li> 
  <li><strong>QQ群</strong>：8321人</li> 
 </ul> 
</blockquote> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-8be609b8137519ea2aed7fa4a0846da4deb.png" width="1380" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-7b5722e36c94876f9bd7cab8057f466700c.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="395" src="https://oscimg.oschina.net/oscnet/up-ed6ec94c563ba4eda2eddcdb845a4527430.png" width="1138" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 远程请求模块异常<span> </span><code>Http</code><span> </span>状态码<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/462">!462</a></li> 
    <li>[新增] 动态 WebAPI 支持小驼峰配置<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I4W1R4">#I4W1R4</a></li> 
    <li>[新增] 远程请求<span> </span><code>SendAsByteArrayAsync</code><span> </span>等一系列方法，支持返回<span> </span><code>byte[]</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/452">!452</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[升级]<span> </span><code>.NET6</code><span> </span>依赖包全部升级至<span> </span><code>Nuget</code><span> </span>最新版<span> </span><code>v6.0.3</code></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复]<span> </span><code>.NET6 WebApplication</code><span> </span>模式二级虚拟目录问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I4UZLM">#I4UZLM</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I4PZ0C">#I4PZ0C</a></li> 
    <li>[修复] 日期验证不支持<span> </span><code>2022-03-01 0:00:00</code>（现在支持小时域<span> </span><code>0</code><span> </span>和<span> </span><code>00</code>） 问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I4Y3NT">#I4Y3NT</a></li> 
    <li>[修复] 环境配置和文件配置优先级问题</li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[过时] 标记<span> </span><code>Furion.Extras.Logging.Serilog</code><span> </span>拓展包<span> </span><code>IWebHost</code><span> </span>拓展为过时状态</li> 
   </ul> </li> 
  <li> <p><strong>文档</strong></p> 
   <ul> 
    <li>[文档] 优化文档体验，新增面包屑导航，重写文档缓存，提升文档访问速度</li> 
    <li>[文档] 更新动态 API 文档、配置文档、远程请求文档</li> 
    <li>[文档] 更新二级虚拟目录文档</li> 
   </ul> </li> 
  <li> <p><strong>本期亮点</strong></p> </li> 
 </ul> 
 <ol> 
  <li>新增动态<span> </span><code>WebApi</code><span> </span>支持小驼峰路径，如<span> </span><code>GetMyName</code><span> </span>-><span> </span><code>getMyName</code>：</li> 
 </ol> 
 <div style="text-align:start"> 
  <pre>&#123;
    <span style="color:var(--color-prettylights-syntax-entity-tag)">"DynamicApiControllerSettings"</span>: &#123;
        <span style="color:var(--color-prettylights-syntax-entity-tag)">"LowercaseRoute"</span>: <span style="color:var(--color-prettylights-syntax-constant)">false</span>,
        <span style="color:var(--color-prettylights-syntax-entity-tag)">"KeepName"</span>: <span style="color:var(--color-prettylights-syntax-constant)">true</span>,
        <span style="color:var(--color-prettylights-syntax-entity-tag)">"AsLowerCamelCase"</span>: <span style="color:var(--color-prettylights-syntax-constant)">true</span>
    &#125;
&#125;</pre> 
 </div> 
 <ol start="2"> 
  <li>支持<span> </span><code>.NET6 WebApplication</code><span> </span>模式二级虚拟目录配置：</li> 
 </ol> 
 <div style="text-align:start"> 
  <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">app</span>.<span style="color:var(--color-prettylights-syntax-entity)">UseVirtualPath</span>(<span style="color:var(--color-prettylights-syntax-entity)">app</span> <span style="color:var(--color-prettylights-syntax-keyword)">=></span>
&#123;
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">app</span>.<span style="color:var(--color-prettylights-syntax-entity)">UseInject</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span>.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Empty</span>);  <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">//</span> 注意 String.Empty 只是例子，可以不填或填其他的，见一分钟入门</span>
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">app</span>.<span style="color:var(--color-prettylights-syntax-entity)">MapControllers</span>();
&#125;);</pre> 
 </div> 
</blockquote> 
<h2 style="text-align:start">文档地址<a href="https://dotnetchina.gitee.io/furion/docs#-%E6%96%87%E6%A1%A3%E5%9C%B0%E5%9D%80">​</a></h2> 
<ul> 
 <li>国内文档：<a href="https://dotnetchina.gitee.io/furion" target="_blank">https://dotnetchina.gitee.io/furion</a></li> 
 <li>国外文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffurion.icu%2F" target="_blank">https://furion.icu</a></li> 
</ul> 
<h2 style="text-align:start">开源地址<a href="https://dotnetchina.gitee.io/furion/docs#-%E5%BC%80%E6%BA%90%E5%9C%B0%E5%9D%80">​</a></h2> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/dotnetchina/Furion" target="_blank">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmonksoul%2FFurion" target="_blank">https://github.com/monksoul/Furion</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank">https://www.nuget.org/packages/Furion</a></li> 
</ul>
                                        </div>
                                      
</div>
            