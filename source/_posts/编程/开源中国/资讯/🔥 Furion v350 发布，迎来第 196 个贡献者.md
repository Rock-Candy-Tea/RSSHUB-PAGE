
---
title: '🔥 Furion v3.5.0 发布，迎来第 196 个贡献者'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4e3ea29b3830b1884a39ef97bf92adc77a4.png'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 05:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4e3ea29b3830b1884a39ef97bf92adc77a4.png'
---

<div>   
<div class="content">
                                                                                            <h2>序言</h2> 
<p>持续更新了两年，跨了三个年头，<strong>这是唯一一次更新没有任何 BUG 修复的版本，这说明 Furion 准备好了，你们准备用了吗？😁😁😁</strong></p> 
<p>同时，恭喜 Furion 迎来了第 196 个贡献者，很幸运 Furion 能够在国内众多开源项目中拥有不少的拥趸者，感谢大家的支持。</p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-4e3ea29b3830b1884a39ef97bf92adc77a4.png" width="1920" referrerpolicy="no-referrer"></p> 
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
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p style="margin-left:0; margin-right:0"><strong>新特性</strong></p> 
   <ul> 
    <li>[新增]<span> </span><code>Options</code><span> </span>选项属性支持自定义<span> </span><code>Key</code><span> </span>名称，<code>[MapSettings("key")]</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5B2HN">#I5B2HN</a></li> 
    <li>[新增]<span> </span><code>EventBus</code><span> </span>模块事件<span> </span><code>Id</code><span> </span>支持枚举类型<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/2f328aa8213c8efe7a8480116985573cc6b7fce6">2f328aa</a></li> 
    <li>[新增]<span> </span><code>EventBus</code><span> </span>模块发布者<span> </span><code>PublishAsync</code><span> </span>和<span> </span><code>PublishDelayAsync</code><span> </span>重载<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/2f328aa8213c8efe7a8480116985573cc6b7fce6">2f328aa</a></li> 
    <li>[新增]<span> </span><code>EventBus</code><span> </span>模块拓展方法：<code>Enum.ParseToString()</code><span> </span>和<span> </span><code>String.ParseToEnum()</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/2f328aa8213c8efe7a8480116985573cc6b7fce6">2f328aa</a></li> 
    <li>[新增]<span> </span><strong><code>Furion</code><span> </span>和<span> </span><code>SqlSugar</code><span> </span>脚手架</strong><span> </span>🆕🆕🆕<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/8d9293d1188670626f017ccea4ffb85ac315d2fc">8d9293d</a></li> 
    <li>[新增]<span> </span><code>Dapper</code><span> </span>拓展全局配置委托<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5AYFX">#I5AYFX</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>其他更改</strong></p> 
   <ul> 
    <li>[调整]<span> </span><code>axios-utils.ts</code><span> </span>和<span> </span><code>angular-utils.ts</code><span> </span>，新增请求拦截携带刷新<span> </span><code>Token</code><span> </span>的时机判断<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/82f89bd95573aefa7075676af7f00c55507cb03b">82f89bd</a></li> 
    <li>[优化] 规范化文档<span> </span><code>Swagger</code><span> </span>加载继承注释<span> </span><code><inheritoc /></code><span> </span>性能小优化<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/5f06880564ee8cd2e77caa5957ff18a0c489bdd2">5f06880</a></li> 
    <li>[调整] 脚手架模板，新增<span> </span><code>GlobalUsings.cs</code><span> </span>模式</li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>文档</strong></p> 
   <ul> 
    <li>[新增]<span> </span><code>Furion + SqlSugar</code><span> </span>脚手架文档</li> 
    <li>[更新] 事件总线文档、选项文档、即时通讯文档、<code>.NET5</code><span> </span>升级<span> </span><code>.NET6</code><span> </span>文档、依赖注入文档</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2>本期亮点</h2> 
<ol> 
 <li><strong>事件总线<span> </span><code>Id</code><span> </span>支持枚举类型</strong></li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#990000">EventSubscribe</strong><span>(</span><span style="color:#dd2200">"TO:DO"</span><span>)]</span>  <span style="color:#888888">// 字符串类型</span></span>
<span><strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>Task</span> <strong style="color:#990000">EventHandler1</strong><span>(</span><span>EventHandlerExecutingContext</span> <span>context</span><span>)</span></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#888888">// ....</span></span>
<span><span>&#125;</span></span>

<span><span>[</span><strong style="color:#990000">EventSubscribe</strong><span>(</span><span>YourEnum</span><span>.</span><span>Some</span><span>)]</span> <span style="color:#888888">// 枚举类型</span></span>
<span><strong style="color:#000000">public</strong> <strong style="color:#000000">async</strong> <span>Task</span> <strong style="color:#990000">EventHandler2</strong><span>(</span><span>EventHandlerExecutingContext</span> <span>context</span><span>)</span></span>
<span><span>&#123;</span></span>
<span>    <strong style="color:#445588">var</strong> <span>eventEnum</span> <span>=</span> <span>context</span><span>.</span><span>Source</span><span>.</span><span>EventId</span><span>.</span><strong style="color:#990000">ParseToEnum</strong><span>();</span> <span style="color:#888888">// 将事件 Id 转换成枚举对象</span></span>
<span>    <span style="color:#888888">// ....</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<ol start="2"> 
 <li><strong>事件总线发布支持更简单调用</strong></li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">// 旧版本</span></span>
<span><strong style="color:#000000">await</strong> <span>_eventPublisher</span><span>.</span><strong style="color:#990000">PublishAsync</strong><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#990000">ChannelEventSource</strong><span>(</span><span style="color:#dd2200">"ToDo:Create"</span><span>,</span> <span>name</span><span>));</span></span>

<span><span style="color:#888888">// 新版本</span></span>
<span><strong style="color:#000000">await</strong> <span>_eventPublisher</span><span>.</span><strong style="color:#990000">PublishAsync</strong><span>(</span><span style="color:#dd2200">"ToDo:Create"</span><span>,</span> <span>name</span><span>);</span></span>
<span><strong style="color:#000000">await</strong> <span>_eventPublisher</span><span>.</span><strong style="color:#990000">PublishAsync</strong><span>(</span><span>YourEnum</span><span>.</span><span>Some</span><span>);</span> <span style="color:#888888">// 也支持枚举</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<ol start="3"> 
 <li><strong>选项支持属性自定义配置<span> </span><code>Key</code></strong></li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>"AppInfo"</span><span>:</span><span style="color:#bbbbbb"> </span><span>&#123;</span></span>
<span><span style="color:#bbbbbb">    </span><span>"Name"</span><span>:</span><span style="color:#bbbbbb"> </span><span style="color:#dd1144">"Furion"</span><span>,</span></span>
<span><span style="color:#bbbbbb">    </span><span>"Version"</span><span>:</span><span style="color:#bbbbbb"> </span><span style="color:#dd1144">"1.0.0"</span><span>,</span></span>
<span><span style="color:#bbbbbb">    </span><span>"Company_Name"</span><span>:</span><span style="color:#bbbbbb"> </span><span style="color:#dd1144">"Baiqian"</span><span style="color:#bbbbbb"> </span><span style="background-color:#ffadad; color:#a61717">//</span><span style="color:#bbbbbb"> </span><span style="background-color:#ffadad; color:#a61717">可以和属性不一样</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#000000">public</strong> <strong style="color:#000000">class</strong> <strong style="color:#445588">AppInfoOptions</strong> <span>:</span> <span>IConfigurableOptions</span></span>
<span><span>&#123;</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#445588">string</strong> <span>Name</span> <span>&#123;</span> <strong style="color:#000000">get</strong><span>;</span> <strong style="color:#000000">set</strong><span>;</span> <span>&#125;</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#445588">string</strong> <span>Version</span> <span>&#123;</span> <strong style="color:#000000">get</strong><span>;</span> <strong style="color:#000000">set</strong><span>;</span> <span>&#125;</span></span>

<span>    <span>[</span><strong style="color:#990000">MapSettings</strong><span>(</span><span style="color:#dd2200">"Company_Name"</span><span>)]</span> <span style="color:#888888">// 支持自定义</span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#445588">string</strong> <span>Company</span> <span>&#123;</span> <strong style="color:#000000">get</strong><span>;</span> <strong style="color:#000000">set</strong><span>;</span> <span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<h2>文档更新</h2> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-c56afbbefc5bc55d2ef10001195943c7ab1.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-fe1a471082d3b47fcb3ecd8d496a6e3d664.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-326241c7b98131c2736099be0b473bfd391.png" width="1917" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-3271f9f9f318d834b08fb49624a917036d6.png" width="1917" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            