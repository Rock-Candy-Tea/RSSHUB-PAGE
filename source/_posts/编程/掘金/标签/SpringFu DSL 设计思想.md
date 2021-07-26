
---
title: 'SpringFu DSL 设计思想'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b80341ac4364565b2f4b5056bed905a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 19:28:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b80341ac4364565b2f4b5056bed905a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" title="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<p>让我们再回头看看这个启动类：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> </span>&#123;

    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> JafuApplication app = Jafu.webApplication(ioc ->
            ioc.beans(beanDefinition ->
                    beanDefinition.bean(SampleHandler.class)
                            .bean(SampleService.class)
                            .bean(Sample.class)
            ).enable(WebMvcServerDsl.webMvc(dsl ->
                    dsl.port(dsl.profiles().contains(<span class="hljs-string">"test"</span>) ? <span class="hljs-number">8181</span> : <span class="hljs-number">8080</span>)
                            .router(router -> &#123;
                                SampleHandler handler = dsl.ref(SampleHandler.class);
                                router.GET(<span class="hljs-string">"/sayHello"</span>, handler::hello);
                            &#125;)
                            .converters(c ->
                                    c.string().jackson()
                            )
            ))
    );

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        ConfigurableApplicationContext context = app.run(args);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码中可以看到，不论是 <code>Jafu.webApplication</code> 还是 <code>ConfigurationDsl.enable()</code> 或者 <code>WebMvcServerDsl.webMvc()</code> 他们都有一个共同的特点就是通过 DSL 来描述设置、加载配置、定义 Bean ，可以说 <code>DSL</code> 就是整个 SpringFu 的驱动器和灵魂。</p>
<p>那么对于这些 DSL 又究竟是什么，里面都有哪些神奇的小组件，DSL 之间又有哪些使用小技巧呢？带着这些问题可以一起来扒一扒 SpringFu 的源码。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b80341ac4364565b2f4b5056bed905a~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210710194145037" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到上面这个图一切就明朗起来了，如果说 SpringBoot 的自动配置是通过 <code>xxxAutoConfiguration</code> 那么SpringFu 的核心就在于 <code>xxxDsl</code> 。是的他将所有的组件都通过一份 <code>DSL代码</code>  来做配置和组合。而 DSL 的本质其实是 <code>ApplicationContextInitializer</code> 如果你恰好也熟悉 SpringBoot 的自动配置原理的话，你会顿时明白他们本质是同一个东西，都是通过 <code>ApplicationContextInitializer</code> 这个钩子函数来魔改 Spring 定义框架行为的。</p>
<p>如果你还不太熟悉 <code>ApplicationContextInitializer</code> 可以参看我写的这篇文章：xxx ，浅显易懂的介绍了他是什么，怎么用，为什么这么用。</p>
<h2 data-id="heading-0">顶级 Dsl</h2>
<p>​这里说的顶级 Dsl 并不是指他在类层级上属于顶层，而是说他是用于配置一个 SpringBoot 应用的 Dsl ，要启动一个 SpringBoot 应用首先要定义这个 Dsl。</p>
<p>​这个类的代码也是非常简单，核心功能点在于执行用户自定义的 DslFunction。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ApplicationDsl</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">ConfigurationDsl</span> </span>&#123;

<span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Consumer<ApplicationDsl> dsl;

ApplicationDsl(Consumer<ApplicationDsl> dsl) &#123;
<span class="hljs-keyword">super</span>(configurationDsl -> &#123;&#125;);
<span class="hljs-keyword">this</span>.dsl = dsl;
&#125;

<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initialize</span><span class="hljs-params">(GenericApplicationContext context)</span> </span>&#123;
<span class="hljs-keyword">super</span>.initialize(context);
<span class="hljs-keyword">this</span>.dsl.accept(<span class="hljs-keyword">this</span>); <span class="hljs-comment">// 执行自定义 DSL</span>
<span class="hljs-keyword">new</span> MessageSourceInitializer().initialize(context); <span class="hljs-comment">// 注册国际化的 AutoConfigurationBean </span>
&#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>追溯下 <code>ApplicationDsl</code> 的父类 <code>ConfigurationDsl</code> 看起来方法不少，但要注意一个点我们可以把所有的 Dsl 类都分为两部分：<code>配置</code> 和 <code>执行</code> 。配置即组装当前 Dsl 的上下文，执行则是根据前面组装的上下文执行 initialize 方法。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecf807f7a78a41b8ab11661f2460d387~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210710200135821" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​上图两个红框的部分，分别是 <code>提供给用户的配置方法</code> 和 <code>系统执行的初始化方法</code> 。核心方法如下：</p>
<h3 data-id="heading-1">logging</h3>
<p>​配置日志等级</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> ConfigurationDsl <span class="hljs-title">logging</span><span class="hljs-params">(Consumer<LoggingDsl> dsl)</span> </span>&#123;
   <span class="hljs-keyword">new</span> LoggingDsl(dsl);
   <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">configurationProperties</h3>
<p>使用配置类</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <T> <span class="hljs-function">ConfigurationDsl <span class="hljs-title">configurationProperties</span><span class="hljs-params">(Class<T> clazz, String prefix)</span> </span>&#123;
   context.registerBean(clazz.getSimpleName() + <span class="hljs-string">"ConfigurationProperties"</span>, clazz, () -> <span class="hljs-keyword">new</span> FunctionalConfigurationPropertiesBinder(context).bind(prefix, Bindable.of(clazz)).get());
   <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">beans</h3>
<p>注册 bean</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> ConfigurationDsl <span class="hljs-title">beans</span><span class="hljs-params">(Consumer<BeanDefinitionDsl> dsl)</span> </span>&#123;
   <span class="hljs-keyword">new</span> BeanDefinitionDsl(dsl).initialize(context);
   <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">enable</h3>
<p>​立即执行某个具体的 <code>Dsl</code></p>
<pre><code class="hljs language-java copyable" lang="java">
<span class="hljs-function"><span class="hljs-keyword">public</span> ConfigurationDsl <span class="hljs-title">enable</span><span class="hljs-params">(ApplicationContextInitializer<GenericApplicationContext> configuration)</span> </span>&#123;
   <span class="hljs-keyword">return</span> (ConfigurationDsl) <span class="hljs-keyword">super</span>.enable(configuration);
&#125;

<span class="hljs-function"><span class="hljs-keyword">protected</span> AbstractDsl <span class="hljs-title">enable</span><span class="hljs-params">(ApplicationContextInitializer<GenericApplicationContext> dsl)</span> </span>&#123;
  dsl.initialize(context);
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时他还有一个重载的方法，立即执行 <code>ConfigurationDsl</code></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> ConfigurationDsl <span class="hljs-title">enable</span><span class="hljs-params">(Consumer<ConfigurationDsl> configuration)</span> </span>&#123;
   <span class="hljs-keyword">new</span> ConfigurationDsl(configuration).initialize(context);
   <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">listener</h3>
<p>添加监听器</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <E extends ApplicationEvent> <span class="hljs-function">ConfigurationDsl <span class="hljs-title">listener</span><span class="hljs-params">(Class<E> clazz, ApplicationListener<E> listener)</span> </span>&#123;
   context.addApplicationListener(e -> &#123;
      <span class="hljs-comment">// TODO Leverage SPR-16872 when it will be fixed</span>
      <span class="hljs-keyword">if</span> (clazz.isAssignableFrom(e.getClass())) &#123;
         listener.onApplicationEvent((E)e);
      &#125;
   &#125;);
   <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在追溯 <code>ConfigurationDsl</code> 的父类 <code>AbstractDsl</code> 可以看到他提供了几个获取 Bean 以及获取环境变量的方法提供给所有的 Dsl</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AbstractDsl</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">ApplicationContextInitializer</span><<span class="hljs-title">GenericApplicationContext</span>> </span>&#123;

   <span class="hljs-keyword">protected</span> GenericApplicationContext context;

   <span class="hljs-keyword">public</span> <T> <span class="hljs-function">T <span class="hljs-title">ref</span><span class="hljs-params">(Class<T> beanClass)</span> </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.context.getBean(beanClass);
   &#125;

   <span class="hljs-keyword">public</span> <T> <span class="hljs-function">T <span class="hljs-title">ref</span><span class="hljs-params">(Class<T> beanClass, String name)</span> </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.context.getBean(name, beanClass);
   &#125;

   <span class="hljs-function"><span class="hljs-keyword">public</span> Environment <span class="hljs-title">env</span><span class="hljs-params">()</span> </span>&#123;
      <span class="hljs-keyword">return</span> context.getEnvironment();
   &#125;

   <span class="hljs-function"><span class="hljs-keyword">public</span> List<String> <span class="hljs-title">profiles</span><span class="hljs-params">()</span> </span>&#123;
      <span class="hljs-keyword">return</span> Arrays.asList(context.getEnvironment().getActiveProfiles());
   &#125;

   <span class="hljs-function"><span class="hljs-keyword">protected</span> AbstractDsl <span class="hljs-title">enable</span><span class="hljs-params">(ApplicationContextInitializer<GenericApplicationContext> dsl)</span> </span>&#123;
      dsl.initialize(context);
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
   &#125;
  
   <span class="hljs-meta">@Override</span>
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initialize</span><span class="hljs-params">(GenericApplicationContext context)</span> </span>&#123;
      <span class="hljs-keyword">this</span>.context = context;
   &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">DSL 设计思路</h2>
<p>​看了一个顶级 Dsl 的源码后我们大致能够窥探到整个 SpringFu 的 Dsl 的设计思路了：<code>执行 xx 操作就返回 xxDsl，并且在执行 xx 操作时传递 xxDsl 中预置方法的组合，来定义这个 Dsl 的行为。</code> 看文字还是比较抽象的，结合一个例子和图就会很明白了。</p>
<pre><code class="hljs language-java copyable" lang="java">WebMvcServerDsl webDsl = WebMvcServerDsl.webMvc(dsl ->
                            dsl.port(dsl.profiles().contains(<span class="hljs-string">"test"</span>) ? <span class="hljs-number">8181</span> : <span class="hljs-number">8080</span>)
                                .router(router -> &#123;
                                    SampleHandler handler = dsl.ref(SampleHandler.class);
                                    router.GET(<span class="hljs-string">"/sayHello"</span>, handler::hello);
                                &#125;)
                                .converters(c ->
                                        c.string().jackson()
                                )
                    );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这段代码就是用于构造一个：</p>
<ul>
<li>端口号为 8181 （测试环境） 8080 （非测试环境）</li>
<li>路由为 <code>/sayHello</code> 访问方式为 <code>Get</code></li>
<li>返回格式为 json</li>
</ul>
<p>的 WebDsl 整体流程我们可以理解如下的流图</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f872ac324734877b63c638002a9d266~tplv-k3u1fbpfcp-zoom-1.image" alt="WebDsl 执行流程图" loading="lazy" referrerpolicy="no-referrer"></div>  
</div>
            