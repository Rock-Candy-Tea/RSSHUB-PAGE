
---
title: 'Spring Cloud 升级之路 - 2020.0.x - 6. 使用 Spring Cloud LoadBalancer (1)'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=5001'
author: 掘金
comments: false
date: Fri, 28 May 2021 01:42:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=5001'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文正在参加「Java主题月 - Java 刷题打卡」，详情查看 <a href="https://juejin.cn/post/6962073400005099557/" target="_blank">活动链接</a></p>
</blockquote>
<blockquote>
<p>本项目代码地址：<a href="https://github.com/HashZhang/spring-cloud-scaffold/tree/master/spring-cloud-iiford" target="_blank" rel="nofollow noopener noreferrer">github.com/HashZhang/s…</a></p>
</blockquote>
<p>我们使用 Spring Cloud 官方推荐的 Spring Cloud LoadBalancer 作为我们的客户端负载均衡器。</p>
<h1 data-id="heading-0">Spring Cloud LoadBalancer背景</h1>
<p>Spring Cloud LoadBalancer是一个客户端负载均衡器，类似于Ribbon，但是由于Ribbon已经进入维护模式，并且Ribbon 2并不与Ribbon 1相互兼容，所以Spring Cloud全家桶在Spring Cloud Commons项目中，添加了Spring cloud Loadbalancer作为新的负载均衡器，并且做了向前兼容，就算你的项目中继续用 Spring Cloud Netflix 套装（包括Ribbon，Eureka，Zuul，Hystrix等等）让你的项目中有这些依赖，你也可以通过简单的配置，把ribbon替换成Spring Cloud LoadBalancer。</p>
<h1 data-id="heading-1">负载均衡器在哪里使用？</h1>
<p>Spring Cloud 中内部微服务调用默认是 http 请求，主要通过下面三种 API：</p>
<ul>
<li>RestTemplate：同步 http API</li>
<li>WebClient：异步响应式 http API</li>
<li>三方客户端封装，例如 openfeign</li>
</ul>
<p>如果项目中加入了 spring-cloud-loadbalancer 的依赖并且配置启用了，那么会自动在相关的 Bean 中加入负载均衡器的特性。</p>
<ul>
<li>对于 RestTemplate，会自动对所有 <code>@LoadBalanced</code> 注解修饰的 RestTemplate Bean 增加 Interceptor 从而加上了负载均衡器的特性。</li>
<li>对于 WebClient，会自动创建 <code>ReactorLoadBalancerExchangeFilterFunction</code>，我们可以通过加入<code>ReactorLoadBalancerExchangeFilterFunction</code>会加入负载均衡器的特性。</li>
<li>对于三方客户端，一般不需要我们额外配置什么。</li>
</ul>
<p>这些使用的示例，会在我们系列升级完最后的测试部分看到。</p>
<h1 data-id="heading-2">Spring Cloud LoadBalancer 结构简介</h1>
<p>上一节我们提到了 NamedContextFactory，Spring Cloud LoadBalancer 这里也是使用了这个机制实现了不同微服务使用不同的 Spring Cloud LoadBalancer 配置。相关核心实现是 <code>@LoadBalancerClient</code> 和 <code>@LoadBalancerClients</code> 这两个注解，以及 <code>NamedContextFactory.Specification</code> 的实现 <code>LoadBalancerClientSpecification</code>，<code>NamedContextFactory</code> 的实现 <code>LoadBalancerClientFactory</code>。</p>
<p>经过上一节的详细分析，我们知道可以通过 <code>LoadBalancerClientFactory</code> 知道<strong>默认配置类</strong>为 <code>LoadBalancerClientConfiguration</code>. 并且<strong>获取微服务名称</strong>可以通过 <code>environment.getProperty(LoadBalancerClientFactory.PROPERTY_NAME);</code></p>
<p><a href="https://juejin.cn/post/6967273974111666206"><code>LoadBalancerClientFactory</code></a></p>
<pre><code class="copyable">public static final String NAMESPACE = "loadbalancer";
public static final String PROPERTY_NAME = NAMESPACE + ".client.name";
public LoadBalancerClientFactory() &#123;
super(LoadBalancerClientConfiguration.class, NAMESPACE, PROPERTY_NAME);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看配置类 <code>LoadBalancerClientConfiguration</code>，我们可以发现这个类主要定义两种 Bean，分别是 <code>ReactorLoadBalancer<ServiceInstance></code> 和 <code>ServiceInstanceListSupplier</code>。</p>
<p><code>ReactorLoadBalancer</code> 是负载均衡器，主要提供根据服务名称获取服务实例列表并从从中选择的功能。</p>
<p><a href="https://juejin.cn/post/6967273974111666206"><code>ReactorLoadBalancer</code></a></p>
<pre><code class="copyable">Mono<Response<T>> choose(Request request);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在默认配置中的实现是：</p>
<p><a href="https://juejin.cn/post/6967273974111666206"><code>LoadBalancerClientConfiguration</code></a></p>
<pre><code class="copyable">@Bean
@ConditionalOnMissingBean
public ReactorLoadBalancer<ServiceInstance> reactorServiceInstanceLoadBalancer(
Environment environment,
LoadBalancerClientFactory loadBalancerClientFactory) &#123;
//获取微服务名称
String name = environment.getProperty(LoadBalancerClientFactory.PROPERTY_NAME);
//创建 RoundRobinLoadBalancer 
//注意这里注入的是 LazyProvider，这主要因为在注册这个 Bean 的时候相关的 Bean 可能还没有被加载注册，利用 LazyProvider 而不是直接注入所需的 Bean 防止报找不到 Bean 注入的错误。
return new RoundRobinLoadBalancer(loadBalancerClientFactory.getLazyProvider(name,
ServiceInstanceListSupplier.class), name);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出，默认配置的 <code>ReactorLoadBalancer</code> 实现是 <code>RoundRobinLoadBalancer</code>。这个负载均衡器实现很简单，有一个原子类型的 <code>AtomicInteger position</code>，从 <code>ServiceInstanceListSupplier</code> 中读取所有的服务实例列表，然后对于 <code>position</code> 原子加1，对列表大小取模，返回列表中这个位置的服务实例 <code>ServiceInstance</code>。</p>
<p><a href="https://juejin.cn/post/6967273974111666206"><code>RoundRobinLoadBalancer</code></a></p>
<pre><code class="copyable">public Mono<Response<ServiceInstance>> choose(Request request) &#123;
    //注入的时候注入的是 Lazy Provider，这里取出真正的 Bean，也就是 ServiceInstanceListSupplier
ServiceInstanceListSupplier supplier = serviceInstanceListSupplierProvider
.getIfAvailable(NoopServiceInstanceListSupplier::new);
//获取实例列表
return supplier.get(request)
        .next()
        //从列表中选择一个实例
.map(serviceInstances -> processInstanceResponse(supplier, serviceInstances));
&#125;

private Response<ServiceInstance> processInstanceResponse(ServiceInstanceListSupplier supplier,
List<ServiceInstance> serviceInstances) &#123;
Response<ServiceInstance> serviceInstanceResponse = getInstanceResponse(serviceInstances);
// 如果 ServiceInstanceListSupplier 也实现了 SelectedInstanceCallback，则执行下面的逻辑进行回调。SelectedInstanceCallback 就是每次负载均衡器选择实例之后进行的回调
if (supplier instanceof SelectedInstanceCallback && serviceInstanceResponse.hasServer()) &#123;
((SelectedInstanceCallback) supplier).selectedServiceInstance(serviceInstanceResponse.getServer());
&#125;
return serviceInstanceResponse;
&#125;

private Response<ServiceInstance> getInstanceResponse(List<ServiceInstance> instances) &#123;
if (instances.isEmpty()) &#123;
return new EmptyResponse();
&#125;
//postion 原子 +1 并取绝对值
int pos = Math.abs(this.position.incrementAndGet());
    //返回对应下标的实例
ServiceInstance instance = instances.get(pos % instances.size());
return new DefaultResponse(instance);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ServiceInstanceListSupplier</code> 是服务列表提供者接口：</p>
<p><a href="https://juejin.cn/post/6967273974111666206"><code>ServiceInstanceListSupplier</code></a></p>
<pre><code class="copyable">public interface ServiceInstanceListSupplier extends Supplier<Flux<List<ServiceInstance>>> &#123;
String getServiceId();
default Flux<List<ServiceInstance>> get(Request request) &#123;
return get();
&#125;
static ServiceInstanceListSupplierBuilder builder() &#123;
return new ServiceInstanceListSupplierBuilder();
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>spring-cloud-loadbalancer 中有很多 <code>ServiceInstanceListSupplier</code> 的实现，在默认配置中是通过属性配置指定实现的，这个配置项是<code>spring.cloud.loadbalancer.configurations</code>。例如：</p>
<p><a href="https://juejin.cn/post/6967273974111666206"><code>LoadBalancerClientConfiguration</code></a></p>
<pre><code class="copyable">@Bean
@ConditionalOnBean(ReactiveDiscoveryClient.class)
@ConditionalOnMissingBean
//spring.cloud.loadbalancer.configurations 未指定或者为 default
@ConditionalOnProperty(value = "spring.cloud.loadbalancer.configurations", havingValue = "default",
matchIfMissing = true)
public ServiceInstanceListSupplier discoveryClientServiceInstanceListSupplier(
ConfigurableApplicationContext context) &#123;
return ServiceInstanceListSupplier.builder()
//通过 DiscoveryClient 提供实例
.withDiscoveryClient()
//开启缓存
.withCaching()
.build(context);
&#125;

@Bean
@ConditionalOnBean(ReactiveDiscoveryClient.class)
@ConditionalOnMissingBean
//如果 spring.cloud.loadbalancer.configurations 指定为 zone-preference
@ConditionalOnProperty(value = "spring.cloud.loadbalancer.configurations", havingValue = "zone-preference")
public ServiceInstanceListSupplier zonePreferenceDiscoveryClientServiceInstanceListSupplier(
ConfigurableApplicationContext context) &#123;
return ServiceInstanceListSupplier.builder()
//通过 DiscoveryClient 提供实例
.withDiscoveryClient()
//启用更倾向于同一个 zone 下实例的特性
.withZonePreference()
//开启缓存
.withCaching()
.build(context);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，可以通过 <code>ServiceInstanceListSupplier.builder()</code> 生成官方封装好各种特性的 <code>ServiceInstanceListSupplier</code>。其实从底层实现可以看出，所有的 <code>ServiceInstanceListSupplier</code> 实现都是代理模式，例如对于默认配置，底层代码近似于：</p>
<pre><code class="copyable">return  //开启服务实例缓存
        new CachingServiceInstanceListSupplier(
                        //启用通过 discoveryClient 的服务发现
                        new DiscoveryClientServiceInstanceListSupplier(
                                discoveryClient, env
                        )
                , cacheManagerProvider.getIfAvailable()
        );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了默认配置 <code>LoadBalancerClientConfiguration</code>，用户配置自定义配置则是通过 <code>@LoadBalancerClients</code> 和 <code>@LoadBalancerClient</code>.这个原理是通过 <code>LoadBalancerClientConfigurationRegistrar</code> 实现的。首先，我们来看一下 <code>LoadBalancerClientFactory</code> 这个 <code>NamedContextFactory</code> 是如何创建的：</p>
<p>[<code>LoadBalancerAutoConfiguration</code>]</p>
<pre><code class="copyable">private final ObjectProvider<List<LoadBalancerClientSpecification>> configurations;

public LoadBalancerAutoConfiguration(ObjectProvider<List<LoadBalancerClientSpecification>> configurations) &#123;
    //注入 LoadBalancerClientSpecification List 的 provider
    //在 Bean 创建的时候，进行载入，而不是注册的时候
this.configurations = configurations;
&#125;

@ConditionalOnMissingBean
@Bean
public LoadBalancerClientFactory loadBalancerClientFactory() &#123;
    //创建 LoadBalancerClientFactory
LoadBalancerClientFactory clientFactory = new LoadBalancerClientFactory();
    //读取所有的 LoadBalancerClientSpecification，设置为 LoadBalancerClientFactory 的配置
clientFactory.setConfigurations(this.configurations.getIfAvailable(Collections::emptyList));
return clientFactory;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么，<code>LoadBalancerClientSpecification</code> 这些 Bean 是怎么创建的呢？在 <code>@LoadBalancerClients</code> 和 <code>@LoadBalancerClient</code> 注解中，都包含 <code>@Import(LoadBalancerClientConfigurationRegistrar.class)</code>。这个 <code>@Import</code> 加载一个 <code>ImportBeanDefinitionRegistrar</code>，这里是 <code>LoadBalancerClientConfigurationRegistrar</code>. <code>ImportBeanDefinitionRegistrar</code>里面的方法参数包含<strong>注解元数据，以及注册 Bean 的 <code>BeanDefinitionRegistry</code></strong>。一般通过注解元数据，动态通过 <code>BeanDefinitionRegistry</code> 注册 Bean，在这里的实现是：</p>
<p>[<code>LoadBalancerClients</code>]</p>
<pre><code class="copyable">@Configuration(proxyBeanMethods = false)
@Retention(RetentionPolicy.RUNTIME)
@Target(&#123; ElementType.TYPE &#125;)
@Documented
@Import(LoadBalancerClientConfigurationRegistrar.class)
public @interface LoadBalancerClients &#123;
    //可以指定多个 LoadBalancerClient
LoadBalancerClient[] value() default &#123;&#125;;
//指定所有的负载均衡配置的默认配置
Class<?>[] defaultConfiguration() default &#123;&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>[<code>LoadBalancerClient</code>]</p>
<pre><code class="copyable">@Configuration(proxyBeanMethods = false)
@Import(LoadBalancerClientConfigurationRegistrar.class)
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface LoadBalancerClient &#123;
    //name 和 value 都是微服务名称
@AliasFor("name")
String value() default "";
@AliasFor("value")
String name() default "";
//这个微服务的配置
Class<?>[] configuration() default &#123;&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>[<code>LoadBalancerClientConfigurationRegistrar</code>]</p>
<pre><code class="copyable">@Override
public void registerBeanDefinitions(AnnotationMetadata metadata, BeanDefinitionRegistry registry) &#123;
    //获取 LoadBalancerClients 注解的元数据
Map<String, Object> attrs = metadata.getAnnotationAttributes(LoadBalancerClients.class.getName(), true);
if (attrs != null && attrs.containsKey("value")) &#123;
AnnotationAttributes[] clients = (AnnotationAttributes[]) attrs.get("value");
//对于 value 属性，其实就是一个 LoadBalancerClient 列表，对于每个生成一个特定微服务名字的  LoadBalancerClientSpecification
for (AnnotationAttributes client : clients) &#123;
registerClientConfiguration(registry, getClientName(client), client.get("configuration"));
&#125;
&#125;
//如果指定了 defaultConfiguration，则注册为 default 的配置
if (attrs != null && attrs.containsKey("defaultConfiguration")) &#123;
String name;
if (metadata.hasEnclosingClass()) &#123;
name = "default." + metadata.getEnclosingClassName();
&#125;
else &#123;
name = "default." + metadata.getClassName();
&#125;
registerClientConfiguration(registry, name, attrs.get("defaultConfiguration"));
&#125;
//获取 LoadBalancerClient 注解的元数据
Map<String, Object> client = metadata.getAnnotationAttributes(LoadBalancerClient.class.getName(), true);
String name = getClientName(client);
if (name != null) &#123;
registerClientConfiguration(registry, name, client.get("configuration"));
&#125;
&#125;

private static void registerClientConfiguration(BeanDefinitionRegistry registry, Object name, Object configuration) &#123;
    //初始化 LoadBalancerClientSpecification 的 BeanDefinition，用于注册一个 LoadBalancerClientSpecification Bean
BeanDefinitionBuilder builder = BeanDefinitionBuilder
.genericBeanDefinition(LoadBalancerClientSpecification.class);
//构造器参数
builder.addConstructorArgValue(name);
builder.addConstructorArgValue(configuration);
//注册 Bean
registry.registerBeanDefinition(name + ".LoadBalancerClientSpecification", builder.getBeanDefinition());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从代码中我们可以看出，通过使用 <code>@LoadBalancerClients</code> 和 <code>@LoadBalancerClient</code> 注解可以自动生成对应的 <code>LoadBalancerClientSpecification</code> 进而实现公共负载均衡配置或者特定某个微服务的负载均衡配置。</p>
<blockquote>
<p><strong>微信搜索“我的编程喵”关注公众号，加作者微信，每日一刷，轻松提升技术，斩获各种offer</strong>：</p>
</blockquote></div>  
</div>
            