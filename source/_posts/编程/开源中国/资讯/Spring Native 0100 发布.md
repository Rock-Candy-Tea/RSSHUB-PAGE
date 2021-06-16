
---
title: 'Spring Native 0.10.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5238'
author: 开源中国
comments: false
date: Wed, 16 Jun 2021 08:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5238'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Spring Native 0.10.0 已发布，此版本基于 <a href="https://www.oschina.net/news/142532/spring-boot-2-5-0-released" target="_blank">Spring Boot 2.5</a> 和 <a href="https://www.oschina.net/news/138729/graalvm-21-1-released" target="_blank">GraalVM 21.1</a>，主要带来了以下新功能：</p> 
<ul> 
 <li> <p>引入原生测试 (native testing)</p> </li> 
 <li> <p>新增来自 GraalVM 团队的新官方 Gradle 插件</p> </li> 
 <li> <p>引入可用于类的 AOT(ahead-of-time) 代理</p> </li> 
</ul> 
<p>此外还包括 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Freleases%2Ftag%2F0.10.0" target="_blank">43 个错误修复、文档改进和依赖项升级</a>这些变化。</p> 
<h3>原生测试和 Gradle 插件</h3> 
<p>Spring Native 开发团队称一直在与 GraalVM 团队合作，以将原生镜像在构建插件方面提升到一个新的水平。现在，新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgraalvm%2Fnative-build-tools" target="_blank">原生构建工具</a>取代了前者<code>native-image-maven-plugin</code>，并支持使用本地编译器<code>native-image</code>构建和测试原生应用程序。</p> 
<p>以前仅提供 Maven 支持，现在提供了 Maven 和 Gradle 插件。如果你正在升级，新的 Maven 插件坐标为<code>org.graalvm.buildtools:native-maven-plugin:0.9.0</code>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.spring.io%2Fspring-native%2Fdocs%2Fcurrent%2Freference%2Fhtmlsingle%2F%23_add_the_native_build_tools_plugin" target="_blank">配置好原生构建工具插件后</a>，开发者不仅可以通过<code>mvn -Pnative -DskipTests package</code>或<code>gradle nativeBuild</code>构建自己的应用程序，还可以使用<code>mvn -Pnative test</code>或<code>gradle nativeTest</code>将 JUnit 5 测试作为原生镜像运行。对此，Spring Native 本身已升级以添加初始测试支持，因此<code>@SpringBootTest</code>会作为原生镜像运行。这是原生 Spring Boot 应用程序的一个重要里程碑，也是 JVM 生态的一个重要里程碑，包括 Spring 本身，现在可以使用官方插件来提升原生支持的质量和可维护性。</p> 
<h3>可用于类的 AOT(ahead-of-time) 代理</h3> 
<div style="text-align:start"> 
 <p><span style="color:#191e1e"><span style="color:#333333">对于原生镜像，需要在构建时定义代理。到目前为止，Spring Native 只支持只能在接口上使用的 JDK 代理，</span></span>不支持在 JVM 上通过 CGLIB 代理处理的用于类的代理，<span style="color:#191e1e"><span style="color:#333333">因为原生世界不支持在运行时生成字节码。</span></span></p> 
</div> 
<div style="text-align:start"> 
 <div> 
  <pre><code class="language-java">// Typical security use case of a class proxy now supported on native
@Service
public class GreetingService &#123;

    public String hello() &#123;
        return "Hello!";
    &#125;

    @PreAuthorize("hasRole('ADMIN')")
    public String adminHello() &#123;
        return "Goodbye!";
    &#125;
&#125;</code></pre> 
  <div style="text-align:start"> 
   <p><span style="color:#191e1e"><span style="color:#333333">但从 0.10 开始，现在可以在构建时通过<code>@AotProxyHint</code>注释生成用于类的代理。请注意前者<code>@ProxyHint</code>已被重命名为<code>@JdkProxyHint</code>，以避免混淆。</span></span></p> 
  </div> 
  <div style="text-align:start"> 
   <p><span style="color:#191e1e"><span style="color:#333333">此功能允许在类上实现支持安全性、事务和广泛的其他基于代理的机制。</span></span></p> 
   <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F06%2F14%2Fspring-native-0-10-0-available-now" target="_blank">详细更新说明查看发布公告</a>。</p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            