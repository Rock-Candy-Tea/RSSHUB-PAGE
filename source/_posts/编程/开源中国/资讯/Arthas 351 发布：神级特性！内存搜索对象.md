
---
title: 'Arthas 3.5.1 发布：神级特性！内存搜索对象'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://arthas.aliyun.com/doc/_images/arthas.png'
author: 开源中国
comments: false
date: Tue, 18 May 2021 10:59:00 GMT
thumbnail: 'https://arthas.aliyun.com/doc/_images/arthas.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://arthas.aliyun.com/doc/_images/arthas.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify"><code>Arthas</code>是Alibaba开源的Java诊断工具，深受开发者喜爱。</p> 
<ul> 
 <li> <p>Github：https://github.com/alibaba/arthas</p> </li> 
 <li> <p>文档：https://arthas.aliyun.com/doc/</p> </li> 
</ul> 
<p style="text-align:justify">以前使用<code>watch</code>等命令时，我们通常要先知道哪个类，调用了哪个函数，然后触发调用。这样有局限：</p> 
<ol> 
 <li> <p>线上触发调用比较难</p> </li> 
 <li> <p>要watch到正确的函数可能要选择多次</p> </li> 
 <li> <p>条件表达式/结果表达式 可能需要多次测试</p> </li> 
</ol> 
<p style="text-align:justify">另外，如果想要查找内存里的对象，需要heapdump再分析。</p> 
<p style="text-align:justify"><strong>Arthas在最新发布的 3.5.1 版本里，带来神级特性：通过<code>vmtool</code>命令，可以在JVM内存搜索对象。</strong></p> 
<h3 style="text-align:justify">vmtool在线教程</h3> 
<p style="text-align:justify">下面以<code>vmtool</code>在线教程为例，演示<code>vmtool</code>命令的功能：</p> 
<ul> 
 <li> <p>https://arthas.aliyun.com/doc/arthas-tutorials.html?language=cn&id=command-vmtool</p> </li> 
</ul> 
<p style="text-align:justify">首先启动任意spring boot应用，比如：</p> 
<pre><code class="language-bash">wget https://github.com/hengyunabc/spring-boot-inside/raw/master/demo-arthas-spring-boot/demo-arthas-spring-boot.jar
java -jar demo-arthas-spring-boot.jar</code></pre> 
<p style="text-align:justify">然后用<code>arthas</code> attach目标进程，成功之后就可以使用<code>vmtool</code>命令了：</p> 
<p style="text-align:right"> </p> 
<pre><code>wget https://arthas.aliyun.com/arthas-boot.jar</code><code>java -jar arthas-boot.jar</code></pre> 
<h3 style="text-align:justify">查找jvm里的字符串对象</h3> 
<p style="text-align:justify">首先，<code>vmtool</code>命令通过<code>getInstances</code>这个action，在JVM里搜索字符串：</p> 
<pre><code>$ vmtool --action getInstances --className java.lang.String</code><code>@String[][</code><code>    @String[Sorry, deque too big],</code><code>    @String[head=%d tail=%d capacity=%d%n],</code><code>    @String[elements=%s%n],</code><code>    @String[sun/nio/ch/IOVecWrapper],</code><code>    @String[40252e37-8a73-4960-807e-3495addd5b08:1620922383791],</code><code>    @String[40252e37-8a73-4960-807e-3495addd5b08:1620922383791],</code><code>    @String[sun/nio/ch/AllocatedNativeObject],</code><code>    @String[sun/nio/ch/NativeObject],</code><code>    @String[sun/nio/ch/IOVecWrapper$Deallocator],</code><code>    @String[Java_sun_nio_ch_FileDispatcherImpl_writev0],</code><code>]</code></pre> 
<h3 style="text-align:justify">limit参数</h3> 
<blockquote> 
 <p>通过 <code>--limit</code>参数，可以限制返回值数量，避免获取超大数据时对JVM造成压力。默认值是10。</p> 
</blockquote> 
<p style="text-align:justify">所以上面的命令实际上等值于：</p> 
<pre><code>vmtool --action getInstances --className java.lang.String --limit 10</code></pre> 
<p style="text-align:justify">如果设置<code>--limit</code>为负数，则遍历所有对象。</p> 
<h3 style="text-align:justify">查找spring context</h3> 
<p style="text-align:justify">以前的在线教程里，我们需要通过<code>tt</code>命令来拦载spring调用，然后获取到spring context。</p> 
<p style="text-align:justify">通过<code>vmtool</code>命令，我们可以直接获取到srping context：</p> 
<pre><code>$ vmtool --action getInstances \</code><code>--className org.springframework.context.ApplicationContext</code><code>@ApplicationContext[][</code><code>    @AnnotationConfigEmbeddedWebApplicationContext[org.springframework.boot.context.embedded.AnnotationConfigEmbeddedWebApplicationContext@12028586: startup date [Thu May 13 16:08:38 UTC 2021]; root of context hierarchy],</code><code>]</code></pre> 
<h3 style="text-align:justify">指定返回结果展开层数</h3> 
<blockquote> 
 <p><code>getInstances</code> action返回结果绑定到<code>instances</code>变量上，它是数组。</p> 
</blockquote> 
<blockquote> 
 <p>通过 <code>-x</code>/<code>--expand</code> 参数可以指定结果的展开层次，默认值是1。</p> 
</blockquote> 
<p style="text-align:justify"><code>vmtool --action getInstances --className org.springframework.context.ApplicationContext -x 2</code></p> 
<h3 style="text-align:justify">获取srping bean，执行表达式</h3> 
<blockquote> 
 <p><code>getInstances</code> action返回结果绑定到<code>instances</code>变量上，它是数组。可以通过<code>--express</code>参数执行指定的表达式。</p> 
</blockquote> 
<p style="text-align:justify">比如，查找所有的spring beans名字：</p> 
<pre><code>vmtool --action getInstances \</code><code>--className org.springframework.context.ApplicationContext \</code><code>--express 'instances[0].getBeanDefinitionNames()'</code></pre> 
<p style="text-align:justify">比如，调用<code>userController.findUserById(1)</code>函数：</p> 
<pre><code>$ vmtool --action getInstances \</code><code>--className org.springframework.context.ApplicationContext \</code><code>--express 'instances[0].getBean("userController").findUserById(1)'</code><code>@User[</code><code>    id=@Integer[1],</code><code>    name=@String[name1],</code><code>]</code></pre> 
<h3 style="text-align:justify">查找所有的spring mapping对象</h3> 
<p style="text-align:justify"><code>vmtool --action getInstances --className org.springframework.web.servlet.HandlerMapping</code></p> 
<pre><code>$ vmtool --action getInstances --className org.springframework.web.servlet.HandlerMapping</code><code>@HandlerMapping[][</code><code>    @SimpleUrlHandlerMapping[org.springframework.web.servlet.handler.SimpleUrlHandlerMapping@5d3819c8],</code><code>    @EmptyHandlerMapping[org.springframework.web.servlet.config.annotation.WebMvcConfigurationSupport$EmptyHandlerMapping@11d509ba],</code><code>    @RequestMappingHandlerMapping[org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping@56a5f2e3],</code><code>    @WelcomePageHandlerMapping[org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration$WelcomePageHandlerMapping@4c0a4ed3],</code><code>    @EmptyHandlerMapping[org.springframework.web.servlet.config.annotation.WebMvcConfigurationSupport$EmptyHandlerMapping@51e1f8c3],</code><code>    @BeanNameUrlHandlerMapping[org.springframework.web.servlet.handler.BeanNameUrlHandlerMapping@68c0a39c],</code><code>    @SimpleUrlHandlerMapping[org.springframework.web.servlet.handler.SimpleUrlHandlerMapping@110b768d],</code><code>]</code></pre> 
<h3 style="text-align:justify">查找所有的 javax.servlet.Filter</h3> 
<p style="text-align:justify">在Arthas的在线教程里，我们介绍过怎么排查http请求 404/401 的问题。使用的是 <code>trace javax.servlet.Filter *</code>命令。</p> 
<p style="text-align:justify">现在使用<code>vmtool</code>命令，我们可以直接查找出所有的Filter对象，加速定位过程。</p> 
<pre><code>$ vmtool --action getInstances --className javax.servlet.Filter</code><code>@Filter[][</code><code>    @OrderedCharacterEncodingFilter[org.springframework.boot.web.filter.OrderedCharacterEncodingFilter@49b69493],</code><code>    @OrderedHiddenHttpMethodFilter[org.springframework.boot.web.filter.OrderedHiddenHttpMethodFilter@5477cb9e],</code><code>    @AdminFilter[com.example.demo.arthas.AdminFilterConfig$AdminFilter@3b625385],</code><code>    @WsFilter[org.apache.tomcat.websocket.server.WsFilter@14875f22],</code><code>    @OrderedRequestContextFilter[org.springframework.boot.web.filter.OrderedRequestContextFilter@6bed550e],</code><code>    @OrderedHttpPutFormContentFilter[org.springframework.boot.web.filter.OrderedHttpPutFormContentFilter@3e538cba],</code><code>]</code></pre> 
<h3 style="text-align:justify">指定 classloader name</h3> 
<p style="text-align:justify">在多classloader情况下，还可以指定classloader来查找对象：</p> 
<pre><code>vmtool --action getInstances \</code><code> --classLoaderClass org.springframework.boot.loader.LaunchedURLClassLoader \</code><code> --className org.springframework.context.ApplicationContext</code></pre> 
<h3 style="text-align:justify">指定 classloader hash</h3> 
<p style="text-align:justify">可以通过<code>sc</code>命令查找到加载class的 classloader。</p> 
<pre><code>$ sc -d org.springframework.context.ApplicationContext</code><code> class-info        org.springframework.boot.context.embedded.AnnotationConfigEmbeddedWebApplicationContext</code><code> code-source       file:/private/tmp/demo-arthas-spring-boot.jar!/BOOT-INF/lib/spring-boot-1.5.13.RELEASE.jar!/</code><code> name              org.springframework.boot.context.embedded.AnnotationConfigEmbeddedWebApplicationContext</code><code>...</code><code> class-loader      +-org.springframework.boot.loader.LaunchedURLClassLoader@19469ea2</code><code>                     +-sun.misc.Launcher$AppClassLoader@75b84c92</code><code>                       +-sun.misc.Launcher$ExtClassLoader@4f023edb</code><code> classLoaderHash   19469ea2</code></pre> 
<p style="text-align:justify">然后用<code>-c</code>/<code>--classloader</code> 参数指定：</p> 
<pre><code>vmtool --action getInstances \</code><code>-c 19469ea2 \</code><code>--className org.springframework.context.ApplicationContext</code></pre> 
<h3 style="text-align:justify">强制GC</h3> 
<p style="text-align:justify">当启用 <code>-XX:+DisableExplicitGC</code>的JVM参数之后，调用<code>System.Gc()</code>可能并不会触发GC行为。</p> 
<p style="text-align:justify"><code>vmtool</code>里提供了强制GC的功能：</p> 
<pre><code>vmtool --action forceGc</code></pre> 
<p style="text-align:justify">如果应用配置了<code>-verbose:gc</code>参数，则可以在应用的标准输出里看到类似的日志：</p> 
<pre><code>[GC (JvmtiEnv ForceGarbageCollection)  25760K->17039K(349696K), 0.0015299 secs]</code><code>[Full GC (JvmtiEnv ForceGarbageCollection)  17039K->16840K(353792K), 0.0154049 secs]</code></pre> 
<h3 style="text-align:justify">致谢</h3> 
<ul> 
 <li> <p><code>vmtool</code>功能是在社区开发者<code>dragon-zhang(张子成)</code>的最初PR上，多次讨论修改完成的，感谢他的工作，同时欢迎大家提出PR，参与开发😄。</p> </li> 
</ul> 
<h3 style="text-align:justify">总结</h3> 
<ul> 
 <li> <p>vmtool wiki: https://arthas.aliyun.com/doc/vmtool</p> </li> 
 <li> <p>Release 日志: https://github.com/alibaba/arthas/releases/tag/arthas-all-3.5.1</p> </li> 
</ul> 
<p style="text-align:justify">上面只展示使用<code>vmtool</code>命令操作spring context的例子。实际上可以应用在很多方面，比如：</p> 
<ul> 
 <li> <p>查找 RPC 的 Provider/Consumer 实例</p> </li> 
 <li> <p>查找 MQ 的订阅对象信息</p> </li> 
 <li> <p>查找 Mybatis 的mapping对象</p> </li> 
</ul> 
<p style="text-align:justify">欢迎大家到Issue里分享使用经验：https://github.com/alibaba/arthas/issues</p> 
<p style="text-align:justify">最后我们正在寻找小伙伴，特别是深圳的同学，欢迎大家加入。</p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU2MTY2MjE4OQ%3D%3D%26mid%3D2247483992%26idx%3D1%26sn%3D83f711eded1fefc48ddc974786da219d%26scene%3D21%23wechat_redirect" target="_blank">阿里云-云原生-中间件招聘（深圳/杭州）</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            