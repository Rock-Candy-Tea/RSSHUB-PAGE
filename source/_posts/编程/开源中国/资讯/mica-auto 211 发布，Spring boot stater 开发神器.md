
---
title: 'mica-auto 2.1.1 发布，Spring boot stater 开发神器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1951'
author: 开源中国
comments: false
date: Tue, 06 Jul 2021 02:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1951'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">一、简介</h2> 
<p style="text-align:start">mica-auto 是 Spring cloud 微服务框架 <code>Mica</code> 中的一个基础组件，用来生成 <code>Spring boot starter</code> 的一些基础配置。仅仅编译级别即可 maven、gradle 编译时会自动处理生成所需的配置。 ​</p> 
<h2 style="text-align:start">二、初衷</h2> 
<p style="text-align:start">在开发和维护大量 Spring boot stater 时我们需要添加 spring.factories 配置，偶尔忘记 添加和删减 <code>spring.factories</code> 配置中的类会导致微服务启动失败。为了减少失误和人工介入故开发了 <code>mica-auto</code>，在 2019年1月12日开源 <code>0.0.1</code> 版本，之后在 <a href="https://gitee.com/596392912/mica">mica</a> 和 pig 团队的多个 stater 组件中使用。</p> 
<h2 style="text-align:start">三、功能</h2> 
<ul> 
 <li> <p>生成 <code>spring.factories</code>。</p> </li> 
 <li> <p>生成 <code>spring-devtools.properties</code></p> </li> 
 <li> <p>生成 <code>FeignClient</code> 到 <code>spring.factories</code> 中，供 mica-cloud 中完成 Feign 自动化配置。</p> </li> 
 <li> <p>生成 java <code>Spi</code> 配置，需要添加 <code>@AutoService</code> 注解。</p> </li> 
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
   <td style="border-color:#dfe2e5">@AutoContextInitializer</td> 
   <td style="border-color:#dfe2e5">ApplicationContextInitializer</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoListener</td> 
   <td style="border-color:#dfe2e5">ApplicationListener</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoRunListener</td> 
   <td style="border-color:#dfe2e5">SpringApplicationRunListener</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoEnvPostProcessor</td> 
   <td style="border-color:#dfe2e5">EnvironmentPostProcessor</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoFailureAnalyzer</td> 
   <td style="border-color:#dfe2e5">FailureAnalyzer</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoConfigImportFilter</td> 
   <td style="border-color:#dfe2e5">AutoConfigurationImportFilter</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoTemplateProvider</td> 
   <td style="border-color:#dfe2e5">TemplateAvailabilityProvider</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoEnableCircuitBreaker</td> 
   <td style="border-color:#dfe2e5">EnableCircuitBreaker</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoConfigDataLocationResolver</td> 
   <td style="border-color:#dfe2e5">ConfigDataLocationResolver</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoConfigDataLoader</td> 
   <td style="border-color:#dfe2e5">ConfigDataLoader</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoDatabaseInitializerDetector</td> 
   <td style="border-color:#dfe2e5">DatabaseInitializerDetector</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoDependsOnDatabaseInitializationDetector</td> 
   <td style="border-color:#dfe2e5">DependsOnDatabaseInitializationDetector</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@Component</td> 
   <td style="border-color:#dfe2e5">EnableAutoConfiguration</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoIgnore</td> 
   <td style="border-color:#dfe2e5">忽略，不生成到 spring.factories</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">@AutoService</td> 
   <td style="border-color:#dfe2e5">java Spi 生成配置</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:start">四、变更记录</h2> 
<ul> 
 <li> <p>✨ 添加 DatabaseInitializer 相关支持</p> </li> 
 <li> <p>✨ 优化 jar manifest</p> </li> 
 <li> <p>✅ Adding google compile-testing.</p> </li> 
 <li> <p>⬆️ 升级 Spring boot 到 2.5.2</p> </li> 
</ul> 
<h2 style="text-align:start">五、使用</h2> 
<p style="text-align:start">注意： 如果你项目中使用了 <code>Lombok</code> 请将 <code>mica-auto</code> 的依赖放置到 <code>Lombok</code> 后面。</p> 
<p style="text-align:start">5.1 maven</p> 
<pre style="text-align:left"> <span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span>
   <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>
   <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>mica-auto<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>
   <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>2.1.1<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span>
   <span style="color:#117700"><</span><span style="color:#117700">scope</span><span style="color:#117700">></span>provided<span style="color:#117700"></</span><span style="color:#117700">scope</span><span style="color:#117700">></span>
 <span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></pre> 
<p style="text-align:start">5.2 gradle >= 5.x</p> 
<pre style="text-align:left"> <span style="color:#000000">annotationProcessor</span>(<span style="color:#aa1111">"net.dreamlu:mica-auto:2.1.1"</span>)</pre> 
<p style="text-align:start">5.3 gradle < 5.x</p> 
<pre style="text-align:left"> <span style="color:#000000">compileOnly</span> <span style="color:#aa1111">"net.dreamlu:mica-auto:2.1.1"</span></pre> 
<p style="text-align:start">5.4 java spi 示例：</p> 
<ol> 
 <li> <p>添加注解 @AutoService 指定 spi 接口 Processor.class。 </p> </li> 
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
<h2 style="text-align:start">六、使用场景</h2> 
<ul> 
 <li> <p>Spring boot starter 开发利器，自动生成 spring.factories、spring-devtools.properties 配置。</p> </li> 
 <li> <p>多模块项目中的子项目，包名不同时的自动配置（主项目不建议添加）。</p> </li> 
 <li> <p>java spi 扩展自动生成配置。</p> </li> 
</ul> 
<p style="text-align:start">关注如梦技术码云：<a href="https://gitee.com/596392912">https://gitee.com/596392912</a> ，更多微服务核心组件值得拥有。</p>
                                        </div>
                                      
</div>
            