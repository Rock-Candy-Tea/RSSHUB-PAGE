
---
title: 'mica-auto 2.1.3 发布，idea 增量编译 bug 修复'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7565'
author: 开源中国
comments: false
date: Fri, 06 Aug 2021 09:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7565'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">一、简介</h2> 
<p style="text-align:start"><strong>mica-auto</strong> （Spring boot stater开发利器）用来生成 Spring boot starter 的一些基础配置，是 Spring cloud 微服务框架 Mica 中的一个基础组件，</p> 
<h2 style="text-align:start">二、功能</h2> 
<ul> 
 <li> <p>生成 <code>spring.factories</code>。</p> </li> 
 <li> <p>生成 <code>spring-devtools.properties</code></p> </li> 
 <li> <p>生成 <code>FeignClient</code> 到 <code>spring.factories</code> 中，供 <code>mica-cloud</code> 中完成 Feign 自动化配置。</p> </li> 
 <li> <p>生成 java Spi 配置，需要添加 <code>@AutoService</code> 注解。</p> </li> 
</ul> 
<table cellspacing="0" style="width:1140px"> 
 <thead> 
  <tr> 
   <th>注解</th> 
   <th>spring.factories 或 Spi key</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoContextInitializer</code></td> 
   <td style="border-color:#dfe2e5">ApplicationContextInitializer</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoListener</code></td> 
   <td style="border-color:#dfe2e5">ApplicationListener</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoRunListener</code></td> 
   <td style="border-color:#dfe2e5">SpringApplicationRunListener</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoEnvPostProcessor</code></td> 
   <td style="border-color:#dfe2e5">EnvironmentPostProcessor</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoFailureAnalyzer</code></td> 
   <td style="border-color:#dfe2e5">FailureAnalyzer</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoConfigImportFilter</code></td> 
   <td style="border-color:#dfe2e5">AutoConfigurationImportFilter</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoTemplateProvider</code></td> 
   <td style="border-color:#dfe2e5">TemplateAvailabilityProvider</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoEnableCircuitBreaker</code></td> 
   <td style="border-color:#dfe2e5">EnableCircuitBreaker</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoConfigDataLocationResolver</code></td> 
   <td style="border-color:#dfe2e5">ConfigDataLocationResolver</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoConfigDataLoader</code></td> 
   <td style="border-color:#dfe2e5">ConfigDataLoader</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoDatabaseInitializerDetector</code></td> 
   <td style="border-color:#dfe2e5">DatabaseInitializerDetector</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoDependsOnDatabaseInitializationDetector</code></td> 
   <td style="border-color:#dfe2e5">DependsOnDatabaseInitializationDetector</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@Component</code></td> 
   <td style="border-color:#dfe2e5">EnableAutoConfiguration</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoIgnore</code></td> 
   <td style="border-color:#dfe2e5">忽略，不生成到 spring.factories</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><code>@AutoService</code></td> 
   <td style="border-color:#dfe2e5">java Spi 生成配置</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:start">三、更新记录</h2> 
<ul> 
 <li> <p>✨ 代码优化，优化流关闭。</p> </li> 
 <li> <p>✨ 优化 github actions。</p> </li> 
 <li> <p>🐛 修复 spi，去除注释。</p> </li> 
 <li> <p>🐛 修复 gitee #I4193Q idea 增量编译 bug。</p> </li> 
 <li> <p>🐛 修复 spring-devtools.properties 匹配 bug。</p> </li> 
</ul> 
<h2 style="text-align:start">四、使用</h2> 
<p style="text-align:start">注意： 如果你项目中使用了 Lombok 请将 mica-auto 的依赖放置到 Lombok 后面。</p> 
<p style="text-align:start">4.1 maven</p> 
<pre style="text-align:left"> <span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span>
   <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>
   <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>mica-auto<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>
   <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>2.1.3<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span>
   <span style="color:#117700"><</span><span style="color:#117700">scope</span><span style="color:#117700">></span>provided<span style="color:#117700"></</span><span style="color:#117700">scope</span><span style="color:#117700">></span>
 <span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></pre> 
<p style="text-align:start">4.2 gradle >= 5.x</p> 
<pre style="text-align:left"> <span style="color:#000000">annotationProcessor</span>(<span style="color:#aa1111">"net.dreamlu:mica-auto:2.1.3"</span>)</pre> 
<p style="text-align:start">4.3 gradle < 5.x</p> 
<pre style="text-align:left"> <span style="color:#000000">compileOnly</span> <span style="color:#aa1111">"net.dreamlu:mica-auto:2.1.3"</span></pre> 
<p style="text-align:start">4.4 java spi 示例：</p> 
<ol> 
 <li> <p>添加注解 <a href="https://www.oschina.net/news/154036/mica-auto-2-1-3-released">@AutoService </a> 指定 spi 接口 Processor.class。</p> </li> 
</ol> 
<pre style="text-align:left"> <span style="color:#770088">package</span> <span style="color:#0000ff">foo</span>.<span style="color:#000000">bar</span>;
 ​
 <span style="color:#770088">import</span> <span style="color:#000000">javax</span>.<span style="color:#000000">annotation</span>.<span style="color:#000000">processing</span>.<span style="color:#000000">Processor</span>;
 ​
 <span style="color:#555555">@AutoService</span>(<span style="color:#000000">Processor</span>.<span style="color:#770088">class</span>)  
 <span style="color:#770088">public</span> <span style="color:#770088">class</span> <span style="color:#0000ff">MyProcessor</span> <span style="color:#770088">implements</span> <span style="color:#000000">Processor</span> &#123;
 <span style="color:#aa5500">// …</span>
 &#125;</pre> 
<p style="text-align:start">AutoService 将会自动生成 spi 的配置文件 META-INF/services/javax.annotation.processing.Processor 。内容:</p> 
<pre style="text-align:left"> <span style="color:#000000">foo</span>.<span style="color:#000000">bar</span>.<span style="color:#000000">MyProcessor</span></pre> 
<h2 style="text-align:start">五、使用场景</h2> 
<ol> 
 <li> <p>Spring boot starter 开发利器，自动生成 spring.factories、spring-devtools.properties 配置。</p> </li> 
 <li> <p>多模块项目中的子项目，包名不同时的自动配置（主项目不建议添加）。</p> </li> 
 <li> <p>java spi 扩展自动生成配置。</p> </li> 
</ol> 
<p style="text-align:start">建议关注如梦技术码云：<a href="https://gitee.com/596392912">https://gitee.com/596392912</a> ，更多微服务核心组件值得拥有</p>
                                        </div>
                                      
</div>
            