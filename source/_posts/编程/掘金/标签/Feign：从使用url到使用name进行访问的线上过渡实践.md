
---
title: 'Feign：从使用url到使用name进行访问的线上过渡实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=3020'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 04:45:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=3020'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">相关背景</h4>
<ol>
<li>业务实例都部署在k8s集群，服务之间调用采用的协议是http，http工具使用的是feign</li>
<li>服务注册发现采用k8s集群的service，feign的写法都是使用url=$&#123;<a href="https://link.juejin.cn/?target=http%3A%2F%2Fservice_name" target="_blank" rel="nofollow noopener noreferrer" title="http://service_name" ref="nofollow noopener noreferrer">http://service_name</a>&#125;</li>
<li>为了将服务注册发现的能力掌控在应用程序这边，方便扩展灰度，负载等功能，决定引入nacos为注册中心，使用基于客户端的服务发现和负载均衡（k8s的service能力是基于服务端的）</li>
</ol>
<h4 data-id="heading-1">jar版本依赖</h4>
<ol>
<li>
<p>springboot / cloud的基础版本</p>
<ol>
<li>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">properties</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">springboot.version</span>></span>2.4.6<span class="hljs-tag"></<span class="hljs-name">springboot.version</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">spring.cloud.version</span>></span>2020.0.3<span class="hljs-tag"></<span class="hljs-name">spring.cloud.version</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">alibaba.version</span>></span>2021.1<span class="hljs-tag"></<span class="hljs-name">alibaba.version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">properties</span>></span>
<span class="hljs-tag"><<span class="hljs-name">dependencyManagement</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">dependencies</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.alibaba.cloud<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>spring-cloud-alibaba-dependencies<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;alibaba.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">type</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">type</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">scope</span>></span>import<span class="hljs-tag"></<span class="hljs-name">scope</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.springframework.cloud<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>spring-cloud-dependencies<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;spring.cloud.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">type</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">type</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">scope</span>></span>import<span class="hljs-tag"></<span class="hljs-name">scope</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.springframework.boot<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>spring-boot-dependencies<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;springboot.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">type</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">type</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">scope</span>></span>import<span class="hljs-tag"></<span class="hljs-name">scope</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">dependencies</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependencyManagement</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
</li>
</ol>
<h4 data-id="heading-2">遇到的问题</h4>
<ol>
<li>
<p>服务数量多，不允许一次性上线切换（服务数量少也不允许，这是一个危险的行为）</p>
</li>
<li>
<p>由于设计的原因，有些服务有依赖顺序，甚至有些服务有循环依赖关系</p>
<ol>
<li>假如A服务引用了B服务，C服务，如果此时A服务引入了nacos后，且B，C还未上线，那么A服务对B和C的调用会失败</li>
<li>假如A服务和B服务相互依赖，那么也会有问题（不管谁先上线，只要有流量就会有问题）</li>
</ol>
</li>
</ol>
<h4 data-id="heading-3">解决思路</h4>
<p>让服务发现的能力有一个“过渡”的过程，有变量控制开关决定使用nacos的服务发现还是k8s的服务发现</p>
<ol>
<li>
<p>举个DEMO，还是A，B，C服务，3者都在k8s集群中，那么A对B的Feign的写法是以下</p>
<ol>
<li>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-meta">@FeignClient(name=<span class="hljs-string">"B"</span>,url=<span class="hljs-string">"http://service-B"</span>,contextId=<span class="hljs-string">"bCtx"</span>)</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">BFeign</span></span>&#123;
  <span class="hljs-meta">@GetMapping</span>
  String helloB();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
</li>
<li>
<p>希望达到的效果</p>
<ol>
<li>A的feign代码还是保持原先一致，引入nacos的服务注册发现后，在B引入nacos上线之前A依然正常调用B</li>
<li>B的feign代码也是保持这种写法风格，引入nacos的服务注册发现后，B对A的调用正常，A对B的调用也正常</li>
</ol>
</li>
</ol>
<h4 data-id="heading-4">开始动手改造</h4>
<h5 data-id="heading-5">原理</h5>
<ol>
<li>
<p>在当前版本依赖下，feign构造client的源码是以下这样的（我会把注释标在代码里）</p>
<ol>
<li>
<pre><code class="hljs language-ini copyable" lang="ini"><T> T getTarget() &#123;
    FeignContext <span class="hljs-attr">context</span> = beanFactory != null ? beanFactory.getBean(FeignContext.class)
        : applicationContext.getBean(FeignContext.class)<span class="hljs-comment">;</span>
    Feign.Builder <span class="hljs-attr">builder</span> = feign(context)<span class="hljs-comment">;</span>
    // 如果发现FeignClient注解里没有url参数,那么默认当前FeignClient需要客户端发现/负载均衡
    // 但是因为我们要有一个过渡阶段，所以不能直接去掉url用name，不然就会遇到上面描述的问题
    if (!StringUtils.hasText(url)) &#123;
      // 省略N行
      return (T) loadBalance(builder, context, new HardCodedTarget<>(type, name, url))<span class="hljs-comment">;</span>
    &#125;
    if (StringUtils.hasText(url) && !url.startsWith("http")) &#123;
      <span class="hljs-attr">url</span> = <span class="hljs-string">"http://"</span> + url<span class="hljs-comment">;</span>
    &#125;
    // 走到这里来，就意味着有url属性
    // 那么open feign会认为你是不需要客户端相关能力了，就是一个单纯的http工具了
    String <span class="hljs-attr">url</span> = this.url + cleanPath()<span class="hljs-comment">;</span>
    Client <span class="hljs-attr">client</span> = getOptional(context, Client.class)<span class="hljs-comment">;</span>
    if (client != null) &#123;
      // 如果发现引入了spring loadbalancer，也会因为有url，直接把默认的Client
      // 因为我们要使用nacos的服务注册发现，所以我们同时也会引入spring loadbalancer
      if (client instanceof FeignBlockingLoadBalancerClient) &#123;
        <span class="hljs-attr">client</span> = ((FeignBlockingLoadBalancerClient) client).getDelegate()<span class="hljs-comment">;</span>
      &#125;
      if (client instanceof RetryableFeignBlockingLoadBalancerClient) &#123;
        <span class="hljs-attr">client</span> = ((RetryableFeignBlockingLoadBalancerClient) client).getDelegate()<span class="hljs-comment">;</span>
      &#125;
      builder.client(client)<span class="hljs-comment">;</span>
    &#125;
    Targeter <span class="hljs-attr">targeter</span> = get(context, Targeter.class)<span class="hljs-comment">;</span>
    return (T) targeter.target(this, builder, context, new HardCodedTarget<>(type, name, url))<span class="hljs-comment">;</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
</li>
</ol>

<ol start="2">
<li>
<p>从上面的源码得知，因为有url，所以open feign会忽略你隐入的loadbalancer，直接把默认的client取出来使用</p>
<ol>
<li>
<p>从这个地方可以切入，通过构造我们自己的feign client返回给feign builder</p>
</li>
<li>
<p>我们自己的feign client（这里包括下文都称为proxy feign client）需要包括什么功能呢？</p>
<ol>
<li>通过读取当前spring环境的配置，来决定使用url进行访问，还是使用name去获取ip：port来访问</li>
</ol>
</li>
</ol>
</li>
<li>
<p>如何把我们构造proxy feign client塞给builder呢？</p>
<ol>
<li>
<p>这里有一些点要注意，因为open feign的可拓展性，支持开发者自定义client的类型，也支持是否使用loadbalancer能力的client</p>
</li>
<li>
<p>基于上述的点，我们不能直接通过Configuration的形式去返回一个client去代替本来的client</p>
<ol>
<li>如果我们使用这种方式的话，那么其他上下文会因为条件注解忽略掉本来的client</li>
</ol>
</li>
<li>
<p>如何解决呢？</p>
<ol>
<li>
<p>动态代理去改变FeignContext获取client的逻辑</p>
<ol>
<li>FeignContext会根据上下文，条件注解等来综合获取一个client</li>
<li>利用动态代理，去包装这个获取的行为，构造一个proxy feign client</li>
</ol>
</li>
</ol>
</li>
</ol>
</li>
<li>
<p><strong>开始上刺刀</strong></p>
<ol>
<li>
<p>注入一个BeanPostProcessor，监听FeignContext的初始化行为</p>
<ol>
<li>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 注入BeanPostProcessor</span>
<span class="hljs-meta">@Configuration</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">ExampleConfiguration</span> &#123;
    <span class="hljs-meta">@Bean</span>
    <span class="hljs-keyword">public</span> BeanPostProcessor <span class="hljs-title function_">FeignContextBeanPostProcessor</span><span class="hljs-params">()</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">FeignContextBeanPostProcessor</span>();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// </span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">FeignContextBeanPostProcessor</span> <span class="hljs-keyword">implements</span> <span class="hljs-title class_">BeanPostProcessor</span>, ApplicationContextAware &#123;
​
    ApplicationContext applicationContext;
​
    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">setApplicationContext</span><span class="hljs-params">(ApplicationContext applicationContext)</span> <span class="hljs-keyword">throws</span> BeansException &#123;
        <span class="hljs-built_in">this</span>.applicationContext = applicationContext;
    &#125;
​
    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> Object <span class="hljs-title function_">postProcessAfterInitialization</span><span class="hljs-params">(Object bean, String beanName)</span> <span class="hljs-keyword">throws</span> BeansException &#123;
        <span class="hljs-keyword">if</span> (!(bean <span class="hljs-keyword">instanceof</span> FeignContext)) &#123;
            <span class="hljs-keyword">return</span> BeanPostProcessor.<span class="hljs-built_in">super</span>.postProcessAfterInitialization(bean, beanName);
        &#125;
        <span class="hljs-comment">// 如果是FeignContext，那么使用cglib库创建一个代理返回</span>
        <span class="hljs-type">FeignContext</span> <span class="hljs-variable">feignContext</span> <span class="hljs-operator">=</span> (FeignContext) bean;
        <span class="hljs-type">Enhancer</span> <span class="hljs-variable">enhancer</span> <span class="hljs-operator">=</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Enhancer</span>();
        enhancer.setSuperclass(FeignContext.class);
        <span class="hljs-comment">// 代理拦截器</span>
        enhancer.setCallback(<span class="hljs-keyword">new</span> <span class="hljs-title class_">FeignContextMethodInterceptor</span>(feignContext, applicationContext));
        <span class="hljs-keyword">return</span> enhancer.create();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="hljs language-ini copyable" lang="ini">public class FeignContextMethodInterceptor implements MethodInterceptor &#123;
    // 定义我们要拦截的方法
    // feignbuilder在获取client时，是通过FeignContext去获取对应的Context，然后从Context获取到client返回
    final String <span class="hljs-attr">PROXY_METHOD</span> = <span class="hljs-string">"getInstance"</span><span class="hljs-comment">;</span>
​
    FeignContext origin<span class="hljs-comment">;</span>
​
    ApplicationContext applicationContext<span class="hljs-comment">;</span>
​
    public FeignContextMethodInterceptor(FeignContext feignContext, ApplicationContext applicationContext) &#123;
        <span class="hljs-attr">this.origin</span> = feignContext<span class="hljs-comment">;</span>
        <span class="hljs-attr">this.applicationContext</span> = applicationContext<span class="hljs-comment">;</span>
    &#125;
​
    @Override
    public Object intercept(Object o, Method method, Object<span class="hljs-section">[]</span> objects, MethodProxy methodProxy) throws Throwable &#123;
        // 定位获取实例的方法，并且参数是Client类型
        if (PROXY_METHOD.equals(method.getName()) && <span class="hljs-attr">objects.length</span> == <span class="hljs-number">2</span> && objects[<span class="hljs-number">1</span>].equals(Client.class)) &#123;
            // 执行原方法
            Client <span class="hljs-attr">client</span> = (Client) method.invoke(origin, objects)<span class="hljs-comment">;</span>
            // 什么情况会为空呢？根据上述FeignClientFactoryBean的源码可以得知
            // 如果一个FeignClient具有url，但是没有引入负载均衡相关的库，那么就不去设置Client
            // 有人可能会问，没有client请求不会有问题吗？--答案是不会的，可以去看看源码，feign.Feign.Builder中成员变量client有默认值
            // 这种情况下，你都没有引入负载均衡器，那实际上我就当你直接使用url了
            if (<span class="hljs-attr">client</span> == null) &#123;
                return null<span class="hljs-comment">;</span>
            &#125;
            // 获取contextId
            String <span class="hljs-attr">contextId</span> = (String) objects[<span class="hljs-number">0</span>]<span class="hljs-comment">;</span>
            // 根据contextId查找feign client的工厂bean
            FeignClientFactoryBean <span class="hljs-attr">clientFactoryBean</span> = findFeignClientFactoryBeanByContextId(contextId)<span class="hljs-comment">;</span>
            if (<span class="hljs-attr">clientFactoryBean</span> == null) &#123;
                return client<span class="hljs-comment">;</span>
            &#125;
            String <span class="hljs-attr">url</span> = clientFactoryBean.getUrl()<span class="hljs-comment">;</span>
            String <span class="hljs-attr">name</span> = clientFactoryBean.getName()<span class="hljs-comment">;</span>
            // 如果url和name不同时存在，那按我的理解是 你已经完成了过渡期，你已经做出了你的最佳选择
            if (StringUtils.isBlank(url) || StringUtils.isBlank(name)) &#123;
                return client<span class="hljs-comment">;</span>
            &#125;
            // 返回我们的proxy client 
            return new ProxyClient(client, name, url ,contextId,
                    (StandardEnvironment) applicationContext.getEnvironment())<span class="hljs-comment">;</span>
        &#125; else &#123;
            return method.invoke(origin, objects)<span class="hljs-comment">;</span>
        &#125;
    &#125;
​
    private FeignClientFactoryBean findFeignClientFactoryBeanByContextId(String contextId) &#123;
        String<span class="hljs-section">[]</span> <span class="hljs-attr">beanDefinitionNames</span> = applicationContext.getBeanDefinitionNames()<span class="hljs-comment">;</span>
        if (<span class="hljs-attr">beanDefinitionNames</span> == null || beanDefinitionNames.length == <span class="hljs-number">0</span>) &#123;
            return null<span class="hljs-comment">;</span>
        &#125;
        AutowireCapableBeanFactory <span class="hljs-attr">beanFactory</span> = applicationContext.getAutowireCapableBeanFactory()<span class="hljs-comment">;</span>
        ConfigurableListableBeanFactory <span class="hljs-attr">configurableListableBeanFactory</span> = (ConfigurableListableBeanFactory) beanFactory<span class="hljs-comment">;</span>
        for (String beanDefinitionName : beanDefinitionNames) &#123;
            BeanDefinition <span class="hljs-attr">beanDefinition</span> = configurableListableBeanFactory.getBeanDefinition(beanDefinitionName)<span class="hljs-comment">;</span>
            Object <span class="hljs-attr">feignClientsRegistrarFactoryBean</span> = beanDefinition.getAttribute(<span class="hljs-string">"feignClientsRegistrarFactoryBean"</span>)<span class="hljs-comment">;</span>
            if (<span class="hljs-attr">feignClientsRegistrarFactoryBean</span> == null || !(feignClientsRegistrarFactoryBean instanceof FeignClientFactoryBean)) &#123;
                continue<span class="hljs-comment">;</span>
            &#125;
            FeignClientFactoryBean <span class="hljs-attr">factoryBean</span> = (FeignClientFactoryBean) feignClientsRegistrarFactoryBean<span class="hljs-comment">;</span>
            String <span class="hljs-attr">cId</span> = factoryBean.getContextId()<span class="hljs-comment">;</span>
            if (contextId.equals(cId)) &#123;
                return factoryBean<span class="hljs-comment">;</span>
            &#125;
        &#125;
        return null<span class="hljs-comment">;</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
</li>
<li>
<p>简单的ProxyClient</p>
<ol>
<li>
<pre><code class="hljs language-ini copyable" lang="ini">public class ProxyClient implements Client &#123;
    // 定义一个配置的格式
    static final String <span class="hljs-attr">PROP_PATTERN</span> = <span class="hljs-string">"discovery.&#123;0&#125;.type"</span><span class="hljs-comment">;</span>
    // 如果配置值是client，那么使用客户端发现
    static final String <span class="hljs-attr">_CLIENT</span> = <span class="hljs-string">"client"</span><span class="hljs-comment">;</span>
    // 如果配置是server，那么使用服务端发现，也就是直接使用url访问
    static final String <span class="hljs-attr">_SERVER</span> = <span class="hljs-string">"server"</span><span class="hljs-comment">;</span>
​
    StandardEnvironment standardEnvironment<span class="hljs-comment">;</span>
​
    Client target<span class="hljs-comment">;</span>
​
    Client noLoadBalancerClient<span class="hljs-comment">;</span>
​
    String contextId<span class="hljs-comment">;</span>
​
    String name<span class="hljs-comment">;</span>
​
    String url<span class="hljs-comment">;</span>
​
    public ProxyClient(Client client, String name, String url, String contextId, StandardEnvironment standardEnvironment) &#123;
        <span class="hljs-attr">this.name</span> = name<span class="hljs-comment">;</span>
        <span class="hljs-attr">this.url</span> = url<span class="hljs-comment">;</span>
        <span class="hljs-attr">this.contextId</span> = contextId<span class="hljs-comment">;</span>
        <span class="hljs-attr">this.target</span> = client<span class="hljs-comment">;</span>
        <span class="hljs-attr">this.standardEnvironment</span> = standardEnvironment<span class="hljs-comment">;</span>
        // 这个地方跟FeignClientFactoryBean构造feign源码一样，要拿出默认的client
        if (client instanceof FeignBlockingLoadBalancerClient) &#123;
            <span class="hljs-attr">noLoadBalancerClient</span> = ((FeignBlockingLoadBalancerClient) client).getDelegate()<span class="hljs-comment">;</span>
        &#125;
        if (client instanceof RetryableFeignBlockingLoadBalancerClient) &#123;
            <span class="hljs-attr">noLoadBalancerClient</span> = ((RetryableFeignBlockingLoadBalancerClient) client).getDelegate()<span class="hljs-comment">;</span>
        &#125;
    &#125;
    
    // 从上下文环境中获取变量来决定使用什么方式访问
    // 项目中可以引入配置中心，通过动态配置来达到随时切换的效果！
    public boolean isClientProxyType() &#123;
        String <span class="hljs-attr">propKey</span> = MessageFormat.format(PROP_PATTERN, contextId)<span class="hljs-comment">;</span>
        String <span class="hljs-attr">proxyType</span> = standardEnvironment.getProperty(propKey)<span class="hljs-comment">;</span>
        if (_CLIENT.equals(proxyType)) &#123;
            return true<span class="hljs-comment">;</span>
        &#125; else if (_SERVER.equals(proxyType)) &#123;
            return false<span class="hljs-comment">;</span>
        &#125; else &#123;
            return true<span class="hljs-comment">;</span>
        &#125;
    &#125;
​
​
    @Override
    public Response execute(Request request, Request.Options options) throws IOException &#123;
        boolean <span class="hljs-attr">clientProxyType</span> = isClientProxyType()<span class="hljs-comment">;</span>
        if (clientProxyType) &#123;
            Request <span class="hljs-attr">newRequest</span> = Request.create(request.httpMethod(), reconstructUrl(request.url()),
                    request.headers(), request.body(), request.charset(), request.requestTemplate())<span class="hljs-comment">;</span>
            return target.execute(newRequest, options)<span class="hljs-comment">;</span>
        &#125; else &#123;
            return noLoadBalancerClient.execute(request, options)<span class="hljs-comment">;</span>
        &#125;
    &#125;
​
    private String reconstructUrl(String url) &#123;
        String <span class="hljs-attr">host</span> = URI.create(this.url).getHost()<span class="hljs-comment">;</span>
        return StringUtils.replace(url,host,this.name)<span class="hljs-comment">;</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
</li>
</ol>
</li>
</ol>
<h4 data-id="heading-6">写在最后</h4>
<ol>
<li>如果有需要转载，请附上原地址，谢谢啦</li>
<li>感谢各位大佬的浏览，有什么想法意见，或者文中有什么错误的地方，留言评论！</li>
</ol></div>  
</div>
            