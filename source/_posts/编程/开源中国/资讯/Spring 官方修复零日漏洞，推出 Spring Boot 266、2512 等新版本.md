
---
title: 'Spring 官方修复零日漏洞，推出 Spring Boot 2.6.6、2.5.12 等新版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3.toutiaoimg.com/origin/tos-cn-i-tjoges91tu/T1iwz9MACvzGaf?from=pc'
author: 开源中国
comments: false
date: Sat, 02 Apr 2022 09:00:00 GMT
thumbnail: 'https://p3.toutiaoimg.com/origin/tos-cn-i-tjoges91tu/T1iwz9MACvzGaf?from=pc'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">一、漏洞说明</h2> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">这个漏洞还要从 3 月 29 日晚间说起。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">彼时有不少网友爆料，Spring 框架出现“史诗级” RCE 漏洞，平地一声雷，一时之间，快要入睡的开发者们纷纷坐起查看关于漏洞的情况，闹得技术圈中人心惶惶。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">不过有些不同寻常的是，这个漏洞并没有像 Log4j2 事件那样引起圈内诸多企业大厂的紧急行动，甚至连国外披露漏洞的根源也是来自 QQ 和国内部分网络安全网站。</p> 
<p><img alt="Spring 官方证实：框架爆大漏洞，JDK 9 及以上版本均受影响" src="https://p3.toutiaoimg.com/origin/tos-cn-i-tjoges91tu/T1iwz9MACvzGaf?from=pc" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">这也让不少网友猜测，该漏洞应该是国内某个安全机构、安全人员最先发现的。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">果不其然，据 3 月 31 日国家信息安全漏洞共享平台（CNVD）发布的《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fview.inews.qq.com%2Fa%2F20220401A03R1S00" target="_blank">关于Spring框架存在远程命令执行漏洞的安全公告</a>》显示，这群神秘的白帽子们包括蚂蚁科技集团、奇安信科技、杭州安恒信息技术、安天科技、360、北京天融信，当然这些都是后话了。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">1.1 Spring 零日漏洞真的存在</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">就在开发者越来越焦灼时，Spring.io 官方于 3 月 31 日晚间出面证实了这一漏洞的存在，并带来了解决方案。</p> 
<p><img alt="Spring 官方证实：框架爆大漏洞，JDK 9 及以上版本均受影响" src="https://p3.toutiaoimg.com/origin/tos-cn-i-tjoges91tu/T1ix0Nu2ZDqHeE?from=pc" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">根据公告，我们发现这个漏洞的影响远比我们想象的更为严重，如果满足以下几种门槛，极有可能受漏洞影响：</p> 
<ul style="margin-left:30px; margin-right:30px"> 
 <li> <p style="margin-left:0px; margin-right:0px">JDK 9 或更高版本</p> </li> 
 <li> <p style="margin-left:0px; margin-right:0px">Apache Tomcat 作为 Servlet 容器</p> </li> 
 <li> <p style="margin-left:0px; margin-right:0px">打包为传统的 WAR（与 Spring Boot 可执行 jar 相比）</p> </li> 
 <li> <p style="margin-left:0px; margin-right:0px">spring-webmvc 或 spring-webflux 依赖</p> </li> 
 <li> <p style="margin-left:0px; margin-right:0px">Spring Framework 版本 5.3.0 到 5.3.17、5.2.0 到 5.2.19 以及更早的版本</p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">二、官方更新</h2> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">2.1 初步解决方案</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">当前 Spring.io 已经发布了 <strong>Spring Framework 5.3.18</strong> 和 <strong>5.2.20 </strong>版本，同时还带来了最新的依赖于 Spring Framework 5.3.18 的<strong> Spring Boot 2.6.6</strong> 和<strong> 2.5.12</strong> 。因为如果你能升级到 Spring Framework 5.3.18 和 5.2.20，就不用以下的修复方案了。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">如果不可以，Spring 官方建议通过 @ControllerAdvice 来设置 WebDataBinder 的 disallowedFields。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#00753b">@ControllerAdvice</span></code><code><span style="color:#00753b">@Order</span>(Ordered.LOWEST_PRECEDENCE)</code><code><span style="color:#114ba6">public</span> <span><span style="color:#114ba6">class</span> <span style="color:#a82e2e">BinderControllerAdvice</span> </span>&#123;</code><code> <span style="color:#00753b">@InitBinder</span></code><code> <span style="color:#8a7304"><span style="color:#114ba6">public</span> <span style="color:#114ba6">void</span> <span style="color:#a82e2e">setAllowedFields</span><span>(WebDataBinder dataBinder)</span> </span>&#123;</code><code> String denylist = <span style="color:#114ba6">new</span> String&#123;<span style="color:#00753b">"class.*"</span>, <span style="color:#00753b">"Class.*"</span>, <span style="color:#00753b">"*.class.*"</span>, <span style="color:#00753b">"*.Class.*"</span>&#125;;</code><code> dataBinder.setDisallowedFields(denylist);</code><code> &#125;</code><code>&#125;</code></pre> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>这个解决方案通常会有效，但也并不是 100% 可以阻止漏洞。因此为了更加保险一些，Spring.io 还建议应用程序可以扩展<br> RequestMappingHandlerAdapter，同时在所有其他初始化之后，在最后更新WebDataBinder。为了实现这一点，Spring Boot 应用程序可以声明一个 WebMvcRegistrations（Spring MVC）或 WebFluxRegistrations bean（Spring WebFlux）。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在Spring MVC中（在WebFlux中也类似）示例如下：</p> 
<pre><strong style="color:#000080">package </strong>vip.mate.demo;

<strong style="color:#000080">import </strong>org.springframework.boot.SpringApplication;
<strong style="color:#000080">import </strong>org.springframework.boot.autoconfigure.<span style="color:#808000">SpringBootApplication</span>;
<strong style="color:#000080">import </strong>org.springframework.boot.autoconfigure.web.servlet.WebMvcRegistrations;
<strong style="color:#000080">import </strong>org.springframework.context.annotation.<span style="color:#808000">Bean</span>;
<strong style="color:#000080">import </strong>org.springframework.web.bind.ServletRequestDataBinder;
<strong style="color:#000080">import </strong>org.springframework.web.context.request.NativeWebRequest;
<strong style="color:#000080">import </strong>org.springframework.web.method.annotation.InitBinderDataBinderFactory;
<strong style="color:#000080">import </strong>org.springframework.web.method.support.InvocableHandlerMethod;
<strong style="color:#000080">import </strong>org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter;
<strong style="color:#000080">import </strong>org.springframework.web.servlet.mvc.method.annotation.ServletRequestDataBinderFactory;

<strong style="color:#000080">import </strong>java.util.ArrayList;
<strong style="color:#000080">import </strong>java.util.Arrays;
<strong style="color:#000080">import </strong>java.util.Collections;
<strong style="color:#000080">import </strong>java.util.List;

<span style="color:#808000">@SpringBootApplication
</span><strong style="color:#000080">public class </strong>MyApp &#123;
    <strong style="color:#000080">public static void </strong>main(String[] args) &#123;
        SpringApplication.<em>run</em>(MyApp.<strong style="color:#000080">class</strong>, args);
    &#125;

    <span style="color:#808000">@Bean
</span><span style="color:#808000">    </span><strong style="color:#000080">public </strong>WebMvcRegistrations mvcRegistrations() &#123;
        <strong style="color:#000080">return new </strong>WebMvcRegistrations() &#123;
            <span style="color:#808000">@Override
</span><span style="color:#808000">            </span><strong style="color:#000080">public </strong>RequestMappingHandlerAdapter getRequestMappingHandlerAdapter() &#123;
                <strong style="color:#000080">return new </strong>ExtendedRequestMappingHandlerAdapter();
            &#125;
        &#125;;
    &#125;

    <strong style="color:#000080">private static class </strong>ExtendedRequestMappingHandlerAdapter <strong style="color:#000080">extends </strong>RequestMappingHandlerAdapter &#123;
        <span style="color:#808000">@Override
</span><span style="color:#808000">        </span><strong style="color:#000080">protected </strong>InitBinderDataBinderFactory createDataBinderFactory(List<InvocableHandlerMethod> methods) &#123;
            <strong style="color:#000080">return new </strong>ServletRequestDataBinderFactory(methods, getWebBindingInitializer()) &#123;
                <span style="color:#808000">@Override
</span><span style="color:#808000">                </span><strong style="color:#000080">protected </strong>ServletRequestDataBinder createBinderInstance(Object target, String name, NativeWebRequest request) <strong style="color:#000080">throws </strong>Exception &#123;
                    ServletRequestDataBinder binder = <strong style="color:#000080">super</strong>.createBinderInstance(target, name, request);
                    String[] fields = binder.getDisallowedFields();
                    List<String> fieldList = <strong style="color:#000080">new </strong>ArrayList<>(fields != <strong style="color:#000080">null </strong>? Arrays.<em>asList</em>(fields) : Collections.<em>emptyList</em>());
                    fieldList.addAll(Arrays.<em>asList</em>(<strong style="color:#008000">"class.*"</strong>, <strong style="color:#008000">"Class.*"</strong>, <strong style="color:#008000">"*.class.*"</strong>, <strong style="color:#008000">"*.Class.*"</strong>));
                    binder.setDisallowedFields(fieldList.toArray(<strong style="color:#000080">new </strong>String[]&#123;&#125;));
                    <strong style="color:#000080">return </strong>binder;
                &#125;
            &#125;;
        &#125;
    &#125;
&#125;
</pre> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>对于没有 Spring Boot 的 Spring MVC，应用程序可以从 @EnableWebMvc 切换到直接扩展<br> DelegatingWebMvcConfiguration，如这个文档中（https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-config-advanced-java）高级配置部分所述，然后重写<span> </span>createRequestMappingHandlerAdapter 方法。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">基于以上，我们建议受漏洞影响的产品（服务）厂商和信息系统运营者第一时间进行自查，并及时升级至最新版本。</p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            