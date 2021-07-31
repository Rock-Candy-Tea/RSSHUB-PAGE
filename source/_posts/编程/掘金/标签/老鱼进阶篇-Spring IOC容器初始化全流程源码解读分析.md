
---
title: '老鱼进阶篇-Spring IOC容器初始化全流程源码解读分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=599'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 01:05:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=599'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>[TOC]</p>
<h1 data-id="heading-0">1、XML方式BeanDefination注册流程</h1>
<h2 data-id="heading-1">1.1、测试demo</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 方法一，已过期</span>
String path = <span class="hljs-string">"spring/beans.xml"</span>;
Resource resource = <span class="hljs-keyword">new</span> ClassPathResource(path);
<span class="hljs-comment">// BeanDefination注册流程</span>
XmlBeanFactory beanFactory = <span class="hljs-keyword">new</span> XmlBeanFactory(resource );

<span class="hljs-comment">// 方法二</span>
String path = <span class="hljs-string">"spring/beans.xml"</span>;
<span class="hljs-comment">// 创建DefaultListableBeanFactory工厂，这也就是Spring的基本容器</span>
DefaultListableBeanFactory beanFactory = <span class="hljs-keyword">new</span> DefaultListableBeanFactory();
<span class="hljs-comment">// 创建BeanDefinition阅读器</span>
XmlBeanDefinitionReader reader = <span class="hljs-keyword">new</span> XmlBeanDefinitionReader(beanFactory);
<span class="hljs-comment">// 进行BeanDefinition注册流程</span>
reader.loadBeanDefinitions(path);

<span class="hljs-comment">// 总结：两种方法最终都是通过XmlBeanDefinitionReader开启解析注册流程</span>

<span class="hljs-comment">// 方法三：通过高级容器进行创建</span>
<span class="hljs-comment">// 创建IoC容器，并进行初始化</span>
ApplicationContext context = <span class="hljs-keyword">new</span> ClassPathXmlApplicationContext(<span class="hljs-string">"spring/spring-ioc.xml"</span>);
<span class="hljs-comment">// 获取Bean的实例</span>
Student bean = (Teacher) context.getBean(Teacher.class);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">1.2、源码分析</h2>
<pre><code class="hljs language-java copyable" lang="java">【XmlBeanFactory】#构造方法
@<span class="hljs-meta">@XmlBeanDefinitionReader</span>
# loadBeanDefinitions(EncodedResource resource)
# doLoadBeanDefinitions(InputSource inputSource, Resource resource)
<span class="hljs-comment">// 通过DOM4J加载解析XML文件，最终形成Document对象</span>
#Document doc = doLoadDocument(inputSource, resource)
<span class="hljs-comment">// 通过对Document对象的操作，完成BeanDefinition的加载和注册工作</span>
# registerBeanDefinitions(doc, resource)
<span class="hljs-comment">// 创建BeanDefinitionDocumentReader来解析Document对象，完成BeanDefinition解析</span>
@<span class="hljs-meta">@BeanDefinitionDocumentReader</span>
<span class="hljs-comment">//解析过程入口，BeanDefinitionDocumentReader只是个接口</span>
# registerBeanDefinitions(doc, ..)
<span class="hljs-comment">// 具体的实现过程在DefaultBeanDefinitionDocumentReader完成</span>
@<span class="hljs-meta">@DefaultBeanDefinitionDocumentReader</span>
<span class="hljs-comment">// 真正实现BeanDefinition解析和注册工作</span>
# registerBeanDefinitions(doc, ..)
<span class="hljs-comment">// 委托给BeanDefinitionParserDelegate</span>
<span class="hljs-comment">// 从Document的根元素开始进行BeanDefinition的解析</span>
# doRegisterBeanDefinitions(doc.getDocumentElement())
# parseBeanDefinitions(Eleme(ele)nt root)
<span class="hljs-comment">// bean标签、import标签、alias标签，则使用默认解析规则</span>
# parseDefaultElement(Element ele)
# processBeanDefinition(ele)
@<span class="hljs-meta">@BeanDefinitionParserDelegate</span>
# parseBeanDefinitionElement(ele)
<span class="hljs-comment">// 最终注册方法</span>
#BeanDefinitionReaderUtils
#registerBeanDefinition
<span class="hljs-comment">// 解析自定义标签，如：<aop:config></span>
#parseCustomElement()
<span class="hljs-comment">// 委托给BeanDefinitionParserDelegate</span>
@<span class="hljs-meta">@BeanDefinitionParserDelegate</span>
# parseCustomElement(..)
                                                # BeanDefinitionParser(..)
                                                    #parse(Element element, ..)
                                                        ...省略
                                                        <span class="hljs-comment">// 最终注册方法</span>
                                                        #BeanDefinitionReaderUtils
                                                            #registerBeanDefinition
    
【ClassPathXmlApplicationContext】#构造方法
    # setConfigLocations(configLocations)
    # refresh()
    @<span class="hljs-meta">@AbstractApplicationContext</span>
    # refresh()
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">refresh</span><span class="hljs-params">()</span> </span>&#123;
                    <span class="hljs-keyword">synchronized</span> (<span class="hljs-keyword">this</span>.startupShutdownMonitor) &#123;
                        <span class="hljs-comment">// Prepare this context for refreshing.</span>
                        <span class="hljs-comment">// STEP 1： 刷新预处理</span>
                        prepareRefresh();

                        <span class="hljs-comment">// Tell the subclass to refresh the internal bean factory.</span>
                        <span class="hljs-comment">// STEP 2：</span>
                        <span class="hljs-comment">// a） 创建IoC容器（DefaultListableBeanFactory）</span>
                        <span class="hljs-comment">//b） 加载解析XML文件（最终存储到Document对象中）</span>
                        <span class="hljs-comment">//c） 读取Document对象，并完成BeanDefinition的加载和注册工作</span>
                        ConfigurableListableBeanFactory beanFactory = 
                            obtainFreshBeanFactory();

                        <span class="hljs-comment">// Prepare the bean factory for use in this context.</span>
                        <span class="hljs-comment">// STEP 3： 对IoC容器进行一些预处理（设置一些公共属性）</span>
                        prepareBeanFactory(beanFactory);

                        <span class="hljs-keyword">try</span> &#123;
                            <span class="hljs-comment">// Allows post-processing of the bean factory </span>
                            <span class="hljs-comment">// in context subclasses.</span>
                            <span class="hljs-comment">// STEP 4： </span>
                            postProcessBeanFactory(beanFactory);

                            <span class="hljs-comment">// Invoke factory processors registered as beans</span>
                            <span class="hljs-comment">// in the context.</span>
                            <span class="hljs-comment">// STEP 5： 调用BeanFactoryPostProcessor后置处理器</span>
                            <span class="hljs-comment">// 对BeanDefinition处理</span>
                            invokeBeanFactoryPostProcessors(beanFactory);

                            <span class="hljs-comment">// Register bean processors that intercept bean creation.</span>
                            <span class="hljs-comment">// STEP 6： 注册BeanPostProcessor后置处理器</span>
                            registerBeanPostProcessors(beanFactory);

                            <span class="hljs-comment">// Initialize message source for this context.</span>
                            <span class="hljs-comment">// STEP 7： 初始化一些消息源（比如处理国际化的i18n等消息源）</span>
                            initMessageSource();

                            <span class="hljs-comment">// Initialize event multicaster for this context.</span>
                            <span class="hljs-comment">// STEP 8： 初始化应用事件广播器</span>
                            initApplicationEventMulticaster();

                            <span class="hljs-comment">// Initialize other special beans </span>
                            <span class="hljs-comment">// in specific context subclasses.</span>
                            <span class="hljs-comment">// STEP 9： 初始化一些特殊的bean</span>
                            onRefresh();

                            <span class="hljs-comment">// Check for listener beans and register them.</span>
                            <span class="hljs-comment">// STEP 10： 注册一些监听器</span>
                            registerListeners();

                            <span class="hljs-comment">// Instantiate all remaining (non-lazy-init) singletons.</span>
                            <span class="hljs-comment">// STEP 11： 实例化剩余的单例bean（非懒加载方式）</span>
                            <span class="hljs-comment">// 注意事项：Bean的IoC、DI和AOP都是发生在此步骤</span>
                            finishBeanFactoryInitialization(beanFactory);

                            <span class="hljs-comment">// Last step: publish corresponding event.</span>
                            <span class="hljs-comment">// STEP 12： 完成刷新时，需要发布对应的事件</span>
                            finishRefresh();
                        &#125; <span class="hljs-keyword">catch</span> (BeansException ex) &#123;
                            <span class="hljs-comment">// Destroy already created singletons</span>
                            <span class="hljs-comment">// to avoid dangling resources.</span>
                            destroyBeans();

                            <span class="hljs-comment">// Reset 'active' flag.</span>
                            cancelRefresh(ex);
...
                        &#125; <span class="hljs-keyword">finally</span> &#123;
                           <span class="hljs-comment">// Reset common introspection caches in Spring's core, since </span>
                           <span class="hljs-comment">// might not ever need metadata for singleton beans anymore</span>
                           resetCommonCaches();
                        &#125;
                    &#125;
                &#125;
<span class="hljs-comment">// 通过此方法来解析相关BeanDefinition, 还会完成其余附属功能</span>
# obtainFreshBeanFactory()
            @<span class="hljs-meta">@AbstractRefreshableApplicationContext</span>
            <span class="hljs-comment">// 如果之前有IoC容器，则销毁</span>
            # refreshBeanFactory()
            <span class="hljs-comment">// 创建IoC容器，也就是DefaultListableBeanFactory</span>
            # createBeanFactory()
            <span class="hljs-comment">// 设置工厂的属性：是否允许BeanDefinition覆盖和是否允许循环依赖</span>
# customizeBeanFactory(beanFactory);
<span class="hljs-comment">// 调用载入BeanDefinition的方法，在当前类中只定义了抽象的</span>
<span class="hljs-comment">// loadBeanDefinitions方法，具体的实现调用子类容器</span>
# loadBeanDefinitions(beanFactory); <span class="hljs-comment">//钩子方法</span>
@@ AbstractXmlApplicationContext
# loadBeanDefinitions(DefaultListableBeanFactory beanFactory)
                            @<span class="hljs-meta">@XmlBeanDefinitionReader</span>
                            <span class="hljs-comment">// XML Bean读取器调用其父类</span>
                            <span class="hljs-comment">// AbstractBeanDefinitionReader读取定位的资源</span>
                            @@ AbstractBeanDefinitionReader
# loadBeanDefinitions(configLocations)
                            ...
                            <span class="hljs-comment">// 委派调用其子类</span>
                            <span class="hljs-comment">// XmlBeanDefinitionReader的方法，实现加载功能</span>
                            # loadBeanDefinitions(Resource resource)
                            <span class="hljs-comment">// 至此，回到上面1或者2的流程处理</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">2、注解方式BeanDefination注册流程</h1>
<h2 data-id="heading-4">2.1 测试代码</h2>
<pre><code class="hljs language-java copyable" lang="java">AnnotationConfigApplicationContext context = <span class="hljs-keyword">new</span> AnnotationConfigApplicationContext(<span class="hljs-string">"com.spring.test.ioc.annotation.po"</span>);
Teacher student = context.getBean(Teacher.class);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">2.2 源码分析</h2>
<pre><code class="hljs language-java copyable" lang="java">【AnnotationConfigApplicationContext】#构造方法
# scan(basePackages);
    # refresh();
@<span class="hljs-meta">@AbstractApplicationContext</span>
    # refresh() 
            <span class="hljs-comment">// 解析源码见1.2说明</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">3、IOC容器启动核心流程（12步）</h1>
<h2 data-id="heading-7">3.1 prepareRefresh刷新预处理</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">prepareRefresh</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-comment">// 1、这个方法设置context的启动日期。</span>
    <span class="hljs-keyword">this</span>.startupDate = System.currentTimeMillis();
    
    <span class="hljs-comment">// 2、设置context当前的状态，是活动状态还是关闭状态。</span>
    <span class="hljs-keyword">this</span>.closed.set(<span class="hljs-keyword">false</span>);
<span class="hljs-keyword">this</span>.active.set(<span class="hljs-keyword">true</span>);
    
    <span class="hljs-comment">// 3、初始化context environment（上下文环境）中的占位符属性来源。</span>
    <span class="hljs-comment">// 扩展覆盖protected void initPropertySources()方法，加载自定义环境属性值</span>
    <span class="hljs-comment">// 如：getEnvironment().getSystemProperties().put("name","bobo");</span>
    initPropertySources();

    <span class="hljs-comment">// 4、验证所有必需的属性。</span>
    <span class="hljs-comment">// 如：上一步getEnvironment().setRequiredProperties("username");</span>
    <span class="hljs-comment">// 则在当前方法会进行校验，不存在则抛出异常</span>
    getEnvironment().validateRequiredProperties();

    <span class="hljs-comment">// 5、创建一些监听器事件的集合</span>
    <span class="hljs-keyword">this</span>.earlyApplicationEvents = <span class="hljs-keyword">new</span> LinkedHashSet<>();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">3.2 obtainFreshBeanFactory创建默认工厂</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">protected</span> ConfigurableListableBeanFactory <span class="hljs-title">obtainFreshBeanFactory</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-comment">// 主要是通过该方法完成IoC容器的刷新</span>
    refreshBeanFactory();
    ConfigurableListableBeanFactory beanFactory = getBeanFactory();
    <span class="hljs-keyword">return</span> beanFactory;
&#125;

<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">void</span> <span class="hljs-title">refreshBeanFactory</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> BeansException </span>&#123;
    <span class="hljs-comment">// 1、如果之前有IoC容器，则销毁</span>
    <span class="hljs-keyword">if</span> (hasBeanFactory()) &#123;
        <span class="hljs-comment">// 销毁bean</span>
        destroyBeans();
        <span class="hljs-comment">// 关闭bean工厂</span>
        closeBeanFactory();
    &#125;
    <span class="hljs-comment">// 2、创建IoC容器，也就是DefaultListableBeanFactory</span>
    DefaultListableBeanFactory beanFactory = createBeanFactory();
    beanFactory.setSerializationId(getId());
    <span class="hljs-comment">// 3、设置工厂的属性：是否允许BeanDefinition覆盖和是否允许循环依赖</span>
    customizeBeanFactory(beanFactory);
    <span class="hljs-comment">// 4、调用载入BeanDefinition的方法，在当前类中只定义了抽象的loadBeanDefinitions方法，</span>
    <span class="hljs-comment">// 具体的实现调用子类容器如：AnnotationConfigWebApplicationContext、</span>
    <span class="hljs-comment">// AbstractXmlApplicationContext</span>
    loadBeanDefinitions(beanFactory);
    <span class="hljs-keyword">synchronized</span> (<span class="hljs-keyword">this</span>.beanFactoryMonitor) &#123;
        <span class="hljs-comment">// 5、将创建好的bean工厂的引用交给的context来管理。</span>
        <span class="hljs-keyword">this</span>.beanFactory = beanFactory;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">3.3 prepareBeanFactory 配置预处理容器</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 配置这个工厂的标准环境，比如context的类加载器和后处理器</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">prepareBeanFactory</span><span class="hljs-params">(ConfigurableListableBeanFactory beanFactory)</span> </span>&#123;
<span class="hljs-comment">// 1、设置beanFactory的类加载器</span>
beanFactory.setBeanClassLoader(getClassLoader());
    <span class="hljs-comment">// 2、设置属性解析器</span>
beanFactory.setBeanExpressionResolver(<span class="hljs-keyword">new</span>                                      StandardBeanExpressionResolver(beanFactory.getBeanClassLoader())); 
beanFactory.addPropertyEditorRegistrar(<span class="hljs-keyword">new</span> 
                ResourceEditorRegistrar(<span class="hljs-keyword">this</span>,getEnvironment()));

<span class="hljs-comment">// 3、添加到后置处理器列表, 新创建的 ApplicationContextAwareProcessor </span>
    <span class="hljs-comment">// 入参为当前 ApplicationContext, 为实现Aware接口的bean设置对应的对象</span>
beanFactory.addBeanPostProcessor(<span class="hljs-keyword">new</span> ApplicationContextAwareProcessor(<span class="hljs-keyword">this</span>));
    <span class="hljs-comment">// 4、忽略自动属性装配/赋值，默认只有BeanFactoryAware被忽略，要忽略其他类型，需要单独设置</span>
    <span class="hljs-comment">// 此处目的是为了交给用户自定义实现Aware功能，基于自定义后置处理器处理Bean依赖</span>
    <span class="hljs-comment">// 忽略该接口的实现类中和接口setter方法入参类型相同的依赖。</span>
    <span class="hljs-comment">// 这样的做法使得ApplicationContextAware和BeanFactoryAware中的ApplicationContext或// BeanFactory依赖在自动装配时被忽略，而统一由框架设置依赖，如ApplicationContextAware接口// 的设置会在ApplicationContextAwareProcessor类中完成.</span>
beanFactory.ignoreDependencyInterface(EnvironmentAware.class);
beanFactory.ignoreDependencyInterface(EmbeddedValueResolverAware.class);
beanFactory.ignoreDependencyInterface(ResourceLoaderAware.class);
beanFactory.ignoreDependencyInterface(ApplicationEventPublisherAware.class);
beanFactory.ignoreDependencyInterface(MessageSourceAware.class);
beanFactory.ignoreDependencyInterface(ApplicationContextAware.class);

<span class="hljs-comment">// 5、该方法的主要作用就是指定该类型接口，如果外部要注入该类型接口的对象，则会注入我们</span>
    <span class="hljs-comment">// 指定的对象，而不会去管其他接口实现类（因为多个实现类不知道注入哪个，在这里明确指定）</span>
beanFactory.registerResolvableDependency(BeanFactory.class, beanFactory);
beanFactory.registerResolvableDependency(ResourceLoader.class, <span class="hljs-keyword">this</span>);
beanFactory.registerResolvableDependency(ApplicationEventPublisher.class, <span class="hljs-keyword">this</span>);
beanFactory.registerResolvableDependency(ApplicationContext.class, <span class="hljs-keyword">this</span>);

    <span class="hljs-comment">// 6、用于处理实现ApplicationListener接口的bean,bean初始化后添加监听</span>
beanFactory.addBeanPostProcessor(<span class="hljs-keyword">new</span> ApplicationListenerDetector(<span class="hljs-keyword">this</span>));
    
    <span class="hljs-comment">// 7、增加对AspectJ的支持</span>
<span class="hljs-keyword">if</span> (beanFactory.containsBean(LOAD_TIME_WEAVER_BEAN_NAME)) &#123;
beanFactory.addBeanPostProcessor(<span class="hljs-keyword">new</span>                      
                      LoadTimeWeaverAwareProcessor(beanFactory));
beanFactory.setTempClassLoader(<span class="hljs-keyword">new</span>                                  
              ContextTypeMatchClassLoader(beanFactory.getBeanClassLoader()));
&#125;
<span class="hljs-comment">// 8、给容器中注册Singleton组件,ConfigurableEnviroment,systemProperties,</span>
    <span class="hljs-comment">// systemEnvironment，添加到singletonObjects（ConcurrentHashMap类型）中</span>
<span class="hljs-keyword">if</span> (!beanFactory.containsLocalBean(ENVIRONMENT_BEAN_NAME)) &#123;
beanFactory.registerSingleton(ENVIRONMENT_BEAN_NAME, getEnvironment());
&#125;
<span class="hljs-keyword">if</span> (!beanFactory.containsLocalBean(SYSTEM_PROPERTIES_BEAN_NAME)) &#123;
beanFactory.registerSingleton(SYSTEM_PROPERTIES_BEAN_NAME, 
                                          getEnvironment().getSystemProperties());
&#125;
<span class="hljs-keyword">if</span> (!beanFactory.containsLocalBean(SYSTEM_ENVIRONMENT_BEAN_NAME)) &#123;
beanFactory.registerSingleton(SYSTEM_ENVIRONMENT_BEAN_NAME, 
                                          getEnvironment().getSystemEnvironment());
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">3.4 postProcessBeanFactory 重写自定义修改bean工厂方法</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 因为此方法的参数是BeanFactory，所以我们可以重写此方法，然后针对beanFactory进行一些修改。</span>
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">postProcessBeanFactory</span><span class="hljs-params">(ConfigurableListableBeanFactory beanFactory)</span> </span>&#123;
    <span class="hljs-comment">// ServletContextAwareProcessor中拿到应用上下文持有的servletContext引用和servletConfig引用</span>
    <span class="hljs-comment">// 1.添加ServletContextAwareProcessor处理器</span>
    beanFactory.addBeanPostProcessor(<span class="hljs-keyword">new</span> 
             ServletContextAwareProcessor(<span class="hljs-keyword">this</span>.servletContext, <span class="hljs-keyword">this</span>.servletConfig));    
    <span class="hljs-comment">// 在自动注入时忽略指定的依赖接口，通常被应用上下文用来注册以其他方式解析的依赖项</span>
    beanFactory.ignoreDependencyInterface(ServletContextAware.class);
    beanFactory.ignoreDependencyInterface(ServletConfigAware.class);

    <span class="hljs-comment">// 2.注册web应用的scopes</span>
    WebApplicationContextUtils.registerWebApplicationScopes(beanFactory, 
                                        <span class="hljs-keyword">this</span>.servletContext);
    
    <span class="hljs-comment">// 3.注册和环境有关的beans</span>
    WebApplicationContextUtils.registerEnvironmentBeans(beanFactory, <span class="hljs-keyword">this</span>.servletContext, <span class="hljs-keyword">this</span>.servletConfig);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">3.5 invokeBeanFactoryPostProcessors BeanFactory处理器</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">invokeBeanFactoryPostProcessors</span><span class="hljs-params">(ConfigurableListableBeanFactory 
                                               beanFactory)</span> </span>&#123;
    <span class="hljs-comment">// 1.getBeanFactoryPostProcessors(): 拿到当前应用上下文beanFactoryPostProcessors</span>
    <span class="hljs-comment">// 变量中的值，默认为空的，除非自己手动调用context.addBeanFactoryPostProcessor</span>
    <span class="hljs-comment">// (beanFactoryPostProcessor)完成自定义添加</span>
    <span class="hljs-comment">// 2.invokeBeanFactoryPostProcessors: 实例化并调用所有已注册的BeanFactoryPostProcessor</span>
PostProcessorRegistrationDelegate.invokeBeanFactoryPostProcessors(beanFactory, 
 getBeanFactoryPostProcessors());

<span class="hljs-keyword">if</span> (beanFactory.getTempClassLoader() == <span class="hljs-keyword">null</span> && 
        beanFactory.containsBean(LOAD_TIME_WEAVER_BEAN_NAME)) &#123;
beanFactory.addBeanPostProcessor(<span class="hljs-keyword">new</span> LoadTimeWeaverAwareProcessor(beanFactory));
beanFactory.setTempClassLoader(<span class="hljs-keyword">new</span> 
ContextTypeMatchClassLoader(beanFactory.getBeanClassLoader()));
&#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">invokeBeanFactoryPostProcessors</span><span class="hljs-params">(
        ConfigurableListableBeanFactory beanFactory, List<BeanFactoryPostProcessor> 
    beanFactoryPostProcessors)</span> </span>&#123;
    Set<String> processedBeans = <span class="hljs-keyword">new</span> HashSet<String>();
    <span class="hljs-comment">// 1. beanFactory为DefaultListableBeanFactory, DefaultListableBeanFactory实现了</span>
    <span class="hljs-comment">// BeanDefinitionRegistry接口，判定为true</span>
    <span class="hljs-keyword">if</span> (beanFactory <span class="hljs-keyword">instanceof</span> BeanDefinitionRegistry) &#123;
        BeanDefinitionRegistry registry = (BeanDefinitionRegistry) beanFactory;
        <span class="hljs-comment">// 1.1 保存普通的BeanFactoryPostProcessor</span>
        List<BeanFactoryPostProcessor> regularPostProcessors = <span class="hljs-keyword">new</span> 
            LinkedList<BeanFactoryPostProcessor>();
        <span class="hljs-comment">// 1.2 保存BeanDefinitionRegistryPostProcessor</span>
        List<BeanDefinitionRegistryPostProcessor> registryProcessors = <span class="hljs-keyword">new</span> 
             LinkedList<BeanDefinitionRegistryPostProcessor>();
        <span class="hljs-comment">// 2. 遍历入参中beanFactoryPostProcessors, 将BeanDefinitionRegistryPostProcessor</span>
        <span class="hljs-comment">// 和普通BeanFactoryPostProcessor区分开</span>
        <span class="hljs-keyword">for</span> (BeanFactoryPostProcessor postProcessor : beanFactoryPostProcessors) &#123;
            <span class="hljs-keyword">if</span> (postProcessor <span class="hljs-keyword">instanceof</span> BeanDefinitionRegistryPostProcessor) &#123;
                <span class="hljs-comment">// 2.1. 如果是BeanDefinitionRegistryPostProcessor</span>
                BeanDefinitionRegistryPostProcessor registryProcessor =
                        (BeanDefinitionRegistryPostProcessor) postProcessor;
                <span class="hljs-comment">// 2.2. 执行BeanDefinitionRegistryPostProcessor接口的</span>
                <span class="hljs-comment">// postProcessBeanDefinitionRegistry方法</span>
                registryProcessor.postProcessBeanDefinitionRegistry(registry);
                <span class="hljs-comment">// 2.3. 添加到registryProcessors(用于最后执行postProcessBeanFactory方法)</span>
                registryProcessors.add(registryProcessor);
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// 3.1. 普通的BeanFactoryPostProcessor添加到regularPostProcessors</span>
                <span class="hljs-comment">// (用于最后执行postProcessBeanFactory方法)</span>
                regularPostProcessors.add(postProcessor);
            &#125;
        &#125;
        
        <span class="hljs-comment">// 保存本次要执行的所有BeanDefinitionRegistryPostProcessor</span>
        List<BeanDefinitionRegistryPostProcessor> currentRegistryProcessors = <span class="hljs-keyword">new</span> 
            ArrayList<BeanDefinitionRegistryPostProcessor>();
        
        <span class="hljs-comment">// 4. 找出所有实现PriorityOrdered接口的BeanDefinitionRegistryPostProcessor实现类</span>
        <span class="hljs-comment">// 找出所有实现BeanDefinitionRegistryPostProcessor接口的Bean的beanName</span>
        String[] postProcessorNames = beanFactory.getBeanNamesForType
            (BeanDefinitionRegistryPostProcessor.class, <span class="hljs-keyword">true</span>, <span class="hljs-keyword">false</span>);
        
        <span class="hljs-comment">// 5. 遍历postProcessorNames</span>
        <span class="hljs-keyword">for</span> (String ppName : postProcessorNames) &#123;
            <span class="hljs-comment">// 5.1. 判定是否实现了PriorityOrdered接口</span>
            <span class="hljs-keyword">if</span> (beanFactory.isTypeMatch(ppName, PriorityOrdered.class)) &#123;
                <span class="hljs-comment">// 5.2. 获取ppName对应的bean实例, 添加到currentRegistryProcessors中,</span>
                <span class="hljs-comment">// beanFactory.getBean方法会触发创建ppName对应的bean实例</span>
                currentRegistryProcessors.add(beanFactory.getBean(ppName, 
BeanDefinitionRegistryPostProcessor.class));
                <span class="hljs-comment">// 5.3. 将实现类名添加到processedBeans，防止重复</span>
                processedBeans.add(ppName);
            &#125;
        &#125;
        <span class="hljs-comment">// 6. 进行排序(根据是否实现PriorityOrdered、Ordered接口和order值来排序)</span>
        sortPostProcessors(currentRegistryProcessors, beanFactory);
        <span class="hljs-comment">// 7. 添加到registryProcessors(用于最后执行postProcessBeanFactory方法)</span>
        registryProcessors.addAll(currentRegistryProcessors);
        <span class="hljs-comment">// 8. 遍历currentRegistryProcessors, 执行postProcessBeanDefinitionRegistry方法</span>
        invokeBeanDefinitionRegistryPostProcessors(currentRegistryProcessors, registry);
        <span class="hljs-comment">// 9. 清空currentRegistryProcessors</span>
        currentRegistryProcessors.clear();
 
       <span class="hljs-comment">// 10. 找出所有实现BeanDefinitionRegistryPostProcessor接口的类, </span>
        <span class="hljs-comment">// 重复查找是因为执行完上面的BeanDefinitionRegistryPostProcessor,</span>
        <span class="hljs-comment">// 可能会新增了其他的BeanDefinitionRegistryPostProcessor</span>
        postProcessorNames = beanFactory.getBeanNamesForType
            (BeanDefinitionRegistryPostProcessor.class, <span class="hljs-keyword">true</span>, <span class="hljs-keyword">false</span>);
        <span class="hljs-keyword">for</span> (String ppName : postProcessorNames) &#123;
            <span class="hljs-comment">// 校验是否实现了Ordered接口，并且还未执行过</span>
            <span class="hljs-keyword">if</span> (!processedBeans.contains(ppName) && beanFactory.isTypeMatch(ppName, 
                                                 Ordered.class)) &#123;
                currentRegistryProcessors.add(beanFactory.getBean(ppName, 
BeanDefinitionRegistryPostProcessor.class));
                processedBeans.add(ppName);
            &#125;
        &#125;
        sortPostProcessors(currentRegistryProcessors, beanFactory);
        registryProcessors.addAll(currentRegistryProcessors);
        <span class="hljs-comment">// 11. 遍历currentRegistryProcessors, 执行postProcessBeanDefinitionRegistry方法</span>
        invokeBeanDefinitionRegistryPostProcessors(currentRegistryProcessors, registry);
        currentRegistryProcessors.clear();
 
        <span class="hljs-comment">// 12. 最后查找所有剩下的BeanDefinitionRegistryPostProcessors</span>
        <span class="hljs-keyword">boolean</span> reiterate = <span class="hljs-keyword">true</span>;
        <span class="hljs-keyword">while</span> (reiterate) &#123;
            reiterate = <span class="hljs-keyword">false</span>;
            <span class="hljs-comment">// 12.1 找出所有实现BeanDefinitionRegistryPostProcessor接口的类</span>
            postProcessorNames = beanFactory.getBeanNamesForType
                (BeanDefinitionRegistryPostProcessor.class, <span class="hljs-keyword">true</span>, <span class="hljs-keyword">false</span>);
            <span class="hljs-keyword">for</span> (String ppName : postProcessorNames) &#123;
                <span class="hljs-comment">// 12.2 跳过已经执行过的</span>
                <span class="hljs-keyword">if</span> (!processedBeans.contains(ppName)) &#123;
                    currentRegistryProcessors.add(beanFactory.getBean(ppName, 
 BeanDefinitionRegistryPostProcessor.class));
                    processedBeans.add(ppName);
                    <span class="hljs-comment">// 12.3 如果有BeanDefinitionRegistryPostProcessor被执行,</span>
                    <span class="hljs-comment">// 则有可能会产生新的BeanDefinitionRegistryPostProcessor,</span>
                    <span class="hljs-comment">// 因此这边将reiterate赋值为true, 代表需要再循环查找一次</span>
                    reiterate = <span class="hljs-keyword">true</span>;
                &#125;
            &#125;
            sortPostProcessors(currentRegistryProcessors, beanFactory);
            registryProcessors.addAll(currentRegistryProcessors);
            <span class="hljs-comment">// 13. 遍历currentRegistryProcessors, 执行postProcessBeanDefinitionRegistry方法</span>
            invokeBeanDefinitionRegistryPostProcessors(currentRegistryProcessors, 
                                                       registry);
            currentRegistryProcessors.clear();
        &#125;
 
        <span class="hljs-comment">// 14. 调用所有BeanDefinitionRegistryPostProcessor的postProcessBeanFactory方法</span>
        <span class="hljs-comment">// (BeanDefinitionRegistryPostProcessor继承自BeanFactoryPostProcessor)</span>
        invokeBeanFactoryPostProcessors(registryProcessors, beanFactory);
        <span class="hljs-comment">// 15. 调用入参beanFactoryPostProcessors中的普通BeanFactoryPostProcessor的</span>
        <span class="hljs-comment">// postProcessBeanFactory方法</span>
        invokeBeanFactoryPostProcessors(regularPostProcessors, beanFactory);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 直接调用传过来的BeanDefinitionRegistryPostProcessor的postProcessBeanFactory方法</span>
        invokeBeanFactoryPostProcessors(beanFactoryPostProcessors, beanFactory);
    &#125;
 
    <span class="hljs-comment">// 到这里入参beanFactoryPostProcessors和容器中的所BeanDefinitionRegistryPostProcessor</span>
    <span class="hljs-comment">// 已经全部处理完毕,下面开始处理容器中的所有BeanFactoryPostProcessor</span>
 
    <span class="hljs-comment">// 16.找出所有实现BeanFactoryPostProcessor接口的类</span>
    String[] postProcessorNames =
            beanFactory.getBeanNamesForType(BeanFactoryPostProcessor.class, <span class="hljs-keyword">true</span>, <span class="hljs-keyword">false</span>);
    <span class="hljs-comment">// 17. 保存实现了PriorityOrdered接口的BeanFactoryPostProcessor</span>
    List<BeanFactoryPostProcessor> priorityOrderedPostProcessors = <span class="hljs-keyword">new</span> 
        ArrayList<BeanFactoryPostProcessor>();
    <span class="hljs-comment">// 保存实现了Ordered接口的BeanFactoryPostProcessor的beanName</span>
    List<String> orderedPostProcessorNames = <span class="hljs-keyword">new</span> ArrayList<String>();
    <span class="hljs-comment">// 保存普通BeanFactoryPostProcessor的beanName</span>
    List<String> nonOrderedPostProcessorNames = <span class="hljs-keyword">new</span> ArrayList<String>();
    <span class="hljs-comment">// 18. 遍历postProcessorNames, 将BeanFactoryPostProcessor</span>
    <span class="hljs-comment">// 按实现PriorityOrdered、实现Ordered接口、普通三种区分开</span>
    <span class="hljs-keyword">for</span> (String ppName : postProcessorNames) &#123;
        <span class="hljs-keyword">if</span> (processedBeans.contains(ppName)) &#123;
            <span class="hljs-comment">// 18.1 跳过已经执行过的</span>
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (beanFactory.isTypeMatch(ppName, PriorityOrdered.class)) &#123;
            <span class="hljs-comment">// 18.2 添加实现了PriorityOrdered接口的BeanFactoryPostProcessor</span>
            priorityOrderedPostProcessors.add(beanFactory.getBean(ppName, 
BeanFactoryPostProcessor.class));
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (beanFactory.isTypeMatch(ppName, Ordered.class)) &#123;
            <span class="hljs-comment">// 18.3 添加实现了Ordered接口的BeanFactoryPostProcessor的beanName</span>
            orderedPostProcessorNames.add(ppName);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 18.4 添加剩下的普通BeanFactoryPostProcessor的beanName</span>
            nonOrderedPostProcessorNames.add(ppName);
        &#125;
    &#125;
 
    <span class="hljs-comment">// 19. 对priorityOrderedPostProcessors排序</span>
    sortPostProcessors(priorityOrderedPostProcessors, beanFactory);
    <span class="hljs-comment">// 20. 调用所有实现PriorityOrdered接口的BeanFactoryPostProcessor</span>
    <span class="hljs-comment">// 遍历priorityOrderedPostProcessors, 执行postProcessBeanFactory方法</span>
    invokeBeanFactoryPostProcessors(priorityOrderedPostProcessors, beanFactory);
 
    <span class="hljs-comment">// 21. 调用所有实现Ordered接口的BeanFactoryPostProcessor</span>
    List<BeanFactoryPostProcessor> orderedPostProcessors = <span class="hljs-keyword">new</span> 
        ArrayList<BeanFactoryPostProcessor>();
    <span class="hljs-keyword">for</span> (String postProcessorName : orderedPostProcessorNames) &#123;
        <span class="hljs-comment">// 21.1 获取postProcessorName对应的bean实例, 添加到orderedPostProcessors, 准备执行</span>
        orderedPostProcessors.add(beanFactory.getBean(postProcessorName, 
                                                 BeanFactoryPostProcessor.class));
    &#125;
    <span class="hljs-comment">// 21.2 对orderedPostProcessors排序</span>
    sortPostProcessors(orderedPostProcessors, beanFactory);
    <span class="hljs-comment">// 21.3 遍历orderedPostProcessors, 执行postProcessBeanFactory方法</span>
    invokeBeanFactoryPostProcessors(orderedPostProcessors, beanFactory);

    <span class="hljs-comment">// 22.调用所有剩下的BeanFactoryPostProcessor</span>
    List<BeanFactoryPostProcessor> nonOrderedPostProcessors = <span class="hljs-keyword">new</span> 
        ArrayList<BeanFactoryPostProcessor>();
    <span class="hljs-keyword">for</span> (String postProcessorName : nonOrderedPostProcessorNames) &#123;
        <span class="hljs-comment">// 22.1 获取postProcessorName对应的bean实例, 添加到nonOrderedPostProcessors</span>
        nonOrderedPostProcessors.add(beanFactory.getBean(postProcessorName, 
BeanFactoryPostProcessor.class));
    &#125;
    <span class="hljs-comment">// 22.2 遍历nonOrderedPostProcessors, 执行postProcessBeanFactory方法</span>
    invokeBeanFactoryPostProcessors(nonOrderedPostProcessors, beanFactory);
 
    <span class="hljs-comment">// 23. 清除元数据缓存（mergedBeanDefinitions、allBeanNamesByType、</span>
    <span class="hljs-comment">// singletonBeanNamesByType），</span>
    <span class="hljs-comment">// 因为后处理器可能已经修改了原始元数据，例如: 替换值中的占位符</span>
    beanFactory.clearMetadataCache();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">3.6 registerBeanPostProcessors 注册后置处理器</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 注册用来拦截bean创建的BeanPostProcessor bean.这个方法需要在所有的application bean初始化之前调、</span>
<span class="hljs-comment">// 用。把这个注册的任务委托给了PostProcessorRegistrationDelegate来完成。</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">registerBeanPostProcessors</span><span class="hljs-params">(ConfigurableListableBeanFactory beanFactory)</span> </span>&#123;
    PostProcessorRegistrationDelegate.registerBeanPostProcessors(beanFactory, <span class="hljs-keyword">this</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">registerBeanPostProcessors</span><span class="hljs-params">(ConfigurableListableBeanFactory 
                            beanFactory,AbstractApplicationContext applicationContext)</span> </span>&#123;
<span class="hljs-comment">// 1. 查找所有实现BeanPostProcessor的后置处理器名称</span>
    String[] postProcessorNames = beanFactory.getBeanNamesForType
        (BeanPostProcessor.class, <span class="hljs-keyword">true</span>, <span class="hljs-keyword">false</span>);
<span class="hljs-comment">// 2. 计算处理器总数</span>
<span class="hljs-keyword">int</span> beanProcessorTargetCount = beanFactory.getBeanPostProcessorCount() + <span class="hljs-number">1</span> + 
            postProcessorNames.length;
beanFactory.addBeanPostProcessor(<span class="hljs-keyword">new</span> BeanPostProcessorChecker(beanFactory, 
 beanProcessorTargetCount));

<span class="hljs-comment">// 3. 对所有的BeanPostProcessor按照PriorityOrdered、Ordered和普通的进行分组存储</span>
List<BeanPostProcessor> priorityOrderedPostProcessors = <span class="hljs-keyword">new</span> ArrayList<>();
List<BeanPostProcessor> internalPostProcessors = <span class="hljs-keyword">new</span> ArrayList<>();
List<String> orderedPostProcessorNames = <span class="hljs-keyword">new</span> ArrayList<>();
List<String> nonOrderedPostProcessorNames = <span class="hljs-keyword">new</span> ArrayList<>();
<span class="hljs-keyword">for</span> (String ppName : postProcessorNames) &#123;
<span class="hljs-keyword">if</span> (beanFactory.isTypeMatch(ppName, PriorityOrdered.class)) &#123;
BeanPostProcessor pp = beanFactory.getBean(ppName, 
                                                           BeanPostProcessor.class);
priorityOrderedPostProcessors.add(pp);
<span class="hljs-keyword">if</span> (pp <span class="hljs-keyword">instanceof</span> MergedBeanDefinitionPostProcessor) &#123;
internalPostProcessors.add(pp);
&#125;
&#125;
<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (beanFactory.isTypeMatch(ppName, Ordered.class)) &#123;
orderedPostProcessorNames.add(ppName);
&#125;
<span class="hljs-keyword">else</span> &#123;
nonOrderedPostProcessorNames.add(ppName);
&#125;
&#125;

<span class="hljs-comment">// 4. 排序并注册所有实现了PriorityOrdered的后置处理器</span>
sortPostProcessors(priorityOrderedPostProcessors, beanFactory);
registerBeanPostProcessors(beanFactory, priorityOrderedPostProcessors);

<span class="hljs-comment">// 5. 排序并注册所有实现了Ordered的后置处理器</span>
List<BeanPostProcessor> orderedPostProcessors = <span class="hljs-keyword">new</span> ArrayList<>();
<span class="hljs-keyword">for</span> (String ppName : orderedPostProcessorNames) &#123;
BeanPostProcessor pp = beanFactory.getBean(ppName, BeanPostProcessor.class);
orderedPostProcessors.add(pp);
<span class="hljs-keyword">if</span> (pp <span class="hljs-keyword">instanceof</span> MergedBeanDefinitionPostProcessor) &#123;
internalPostProcessors.add(pp);
&#125;
&#125;
sortPostProcessors(orderedPostProcessors, beanFactory);
registerBeanPostProcessors(beanFactory, orderedPostProcessors);

<span class="hljs-comment">// 6. 注册所有普通的后置处理器</span>
List<BeanPostProcessor> nonOrderedPostProcessors = <span class="hljs-keyword">new</span> ArrayList<>();
<span class="hljs-keyword">for</span> (String ppName : nonOrderedPostProcessorNames) &#123;
BeanPostProcessor pp = beanFactory.getBean(ppName, BeanPostProcessor.class);
nonOrderedPostProcessors.add(pp);
<span class="hljs-keyword">if</span> (pp <span class="hljs-keyword">instanceof</span> MergedBeanDefinitionPostProcessor) &#123;
internalPostProcessors.add(pp);
&#125;
&#125;
registerBeanPostProcessors(beanFactory, nonOrderedPostProcessors);

<span class="hljs-comment">// 排序并注册所有实现了MergedBeanDefinitionPostProcessor的应用处理器</span>
sortPostProcessors(internalPostProcessors, beanFactory);
registerBeanPostProcessors(beanFactory, internalPostProcessors);

<span class="hljs-comment">// 重新注册用来自动探测内部ApplicationListener的post-processor，</span>
    <span class="hljs-comment">// 这样可以将他们移到处理器链条的末尾</span>
beanFactory.addBeanPostProcessor(<span class="hljs-keyword">new</span> 
                              ApplicationListenerDetector(applicationContext));
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">3.7 initMessageSource 初始化消息源</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 初始化MessageSource接口的一个实现类。这个接口提供了消息处理功能。主要用于国际化/i18n。</span>
<span class="hljs-comment">// 此部分代码不做详细阐述</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initMessageSource</span><span class="hljs-params">()</span> </span>&#123;
    ConfigurableListableBeanFactory beanFactory = getBeanFactory();
    <span class="hljs-keyword">if</span> (beanFactory.containsLocalBean(MESSAGE_SOURCE_BEAN_NAME)) &#123;
        <span class="hljs-keyword">this</span>.messageSource = beanFactory.getBean(MESSAGE_SOURCE_BEAN_NAME, 
                                                 MessageSource.class);
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">this</span>.parent != <span class="hljs-keyword">null</span> && <span class="hljs-keyword">this</span>.messageSource 
            <span class="hljs-keyword">instanceof</span> HierarchicalMessageSource) &#123;
            HierarchicalMessageSource hms = (HierarchicalMessageSource) 
                <span class="hljs-keyword">this</span>.messageSource;
            <span class="hljs-keyword">if</span> (hms.getParentMessageSource() == <span class="hljs-keyword">null</span>) &#123;
                hms.setParentMessageSource(getInternalParentMessageSource());
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">else</span> &#123;
        DelegatingMessageSource dms = <span class="hljs-keyword">new</span> DelegatingMessageSource();
        dms.setParentMessageSource(getInternalParentMessageSource());
        <span class="hljs-keyword">this</span>.messageSource = dms;
        beanFactory.registerSingleton(MESSAGE_SOURCE_BEAN_NAME, <span class="hljs-keyword">this</span>.messageSource);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">3.8 initApplicationEventMulticaster 初始化应用事件广播器</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 为context初始化一个事件监听多路广播器（ApplicationEventMulticaster）</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initApplicationEventMulticaster</span><span class="hljs-params">()</span> </span>&#123;
    ConfigurableListableBeanFactory beanFactory = getBeanFactory();
    <span class="hljs-comment">// 检查是否给context配了一个ApplicationEventMulticaster实现类</span>
    <span class="hljs-keyword">if</span> (beanFactory.containsLocalBean(APPLICATION_EVENT_MULTICASTER_BEAN_NAME)) &#123;
        <span class="hljs-keyword">this</span>.applicationEventMulticaster =
            beanFactory.getBean(APPLICATION_EVENT_MULTICASTER_BEAN_NAME, 
                                ApplicationEventMulticaster.class);
    &#125;
    <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 如果没有，就使用默认的实现类 SimpleApplicationEventMulticaster</span>
        <span class="hljs-keyword">this</span>.applicationEventMulticaster = <span class="hljs-keyword">new</span> 
            SimpleApplicationEventMulticaster(beanFactory);
        beanFactory.registerSingleton(APPLICATION_EVENT_MULTICASTER_BEAN_NAME, 
                                      <span class="hljs-keyword">this</span>.applicationEventMulticaster);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">3.9 onRefresh初始化特殊的Bean</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 在AbstractApplicationContext的子类中初始化其他特殊的bean。其实就是初始化ThemeSource接口的实例。</span>
<span class="hljs-comment">// 这个方法需要在所有单例bean初始化之前调用。</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onRefresh</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> BeansException </span>&#123;
    <span class="hljs-comment">// 是个空壳方法，在AnnotationApplicationContex上下文中没有实现，</span>
    <span class="hljs-comment">// 可能在spring后面的版本会去扩展。</span>
&#125;
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onRefresh</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">this</span>.themeSource = UiApplicationContextUtils.initThemeSource(<span class="hljs-keyword">this</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">3.10 registerListeners 注册应用监听器</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 注册应用的监听器。就是注册实现了ApplicationListener接口的监听器bean，这些监听器是注册到</span>
<span class="hljs-comment">// ApplicationEventMulticaster中的。这不会影响到其它监听器bean。在注册完以后，还会将其前期的事件发布</span>
<span class="hljs-comment">// 给相匹配的监听器。</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">registerListeners</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-comment">// 获取实现了ApplicationListener的监听器</span>
    <span class="hljs-keyword">for</span> (ApplicationListener<?> listener : getApplicationListeners()) &#123;
        <span class="hljs-comment">// 手动注册的监听器绑定到广播器</span>
        getApplicationEventMulticaster().addApplicationListener(listener);
    &#125;

    <span class="hljs-comment">// 取到监听器的名称</span>
    String[] listenerBeanNames = getBeanNamesForType(ApplicationListener.class, <span class="hljs-keyword">true</span>, 
    <span class="hljs-comment">// 设置到广播器                                                false);</span>
    <span class="hljs-keyword">for</span> (String listenerBeanName : listenerBeanNames) &#123;
        getApplicationEventMulticaster().addApplicationListenerBean(listenerBeanName);
    &#125;

   <span class="hljs-comment">// 如果存在早期应用事件，发布事件消息</span>
    Set<ApplicationEvent> earlyEventsToProcess = <span class="hljs-keyword">this</span>.earlyApplicationEvents;
    <span class="hljs-keyword">this</span>.earlyApplicationEvents = <span class="hljs-keyword">null</span>;
    <span class="hljs-keyword">if</span> (earlyEventsToProcess != <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-keyword">for</span> (ApplicationEvent earlyEvent : earlyEventsToProcess) &#123;
            getApplicationEventMulticaster().multicastEvent(earlyEvent);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">3.11 finishBeanFactoryInitialization 实例化非懒加载Bean</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 完成bean工厂的初始化工作。这一步非常复杂，也非常重要，涉及到了bean的创建。第二步中只是完成了</span>
<span class="hljs-comment">// BeanDefinition的定义、解析、处理、注册。但是还没有初始化bean实例。这一步 实例化剩余的单例bean（非懒</span>
<span class="hljs-comment">// 加载方式）. 注意事项：Bean的IoC、DI和AOP都是发生在此步骤</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">finishBeanFactoryInitialization</span><span class="hljs-params">(ConfigurableListableBeanFactory 
                                               beanFactory)</span> </span>&#123;
<span class="hljs-comment">// 1. 初始化此上下文的转换服务</span>
    ...
        <span class="hljs-comment">// 2. 如果beanFactory之前没有注册嵌入值解析器，则注册默认的嵌入值解析器：</span>
        <span class="hljs-comment">// 主要用于注解属性值的解析。</span>
        ...
<span class="hljs-comment">// 3. 初始化LoadTimeWeaverAware Bean实例对象</span>
String[] weaverAwareNames = beanFactory.getBeanNamesForType
            (LoadTimeWeaverAware.class, <span class="hljs-keyword">false</span>, <span class="hljs-keyword">false</span>);
<span class="hljs-keyword">for</span> (String weaverAwareName : weaverAwareNames) &#123;
getBean(weaverAwareName);
&#125;

<span class="hljs-comment">// Stop using the temporary ClassLoader for type matching.</span>
beanFactory.setTempClassLoader(<span class="hljs-keyword">null</span>);

<span class="hljs-comment">// 4. 冻结所有bean定义，注册的bean定义不会被修改</span>
    <span class="hljs-comment">// 或进一步后处理，因为马上要创建 Bean 实例对象了</span>
beanFactory.freezeConfiguration();

<span class="hljs-comment">// 实例化单例Bean， 将在第四节【Bean初始化流程分析】进行讲解</span>
beanFactory.preInstantiateSingletons();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">3.12 finishRefresh 完成刷新发布应用事件</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 完成context的刷新。主要是调用LifecycleProcessor的onRefresh()方法，并且发布事件</span>
<span class="hljs-comment">//（ContextRefreshedEvent）。</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">finishRefresh</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-comment">// Clear context-level resource caches (such as ASM metadata from scanning).</span>
    clearResourceCaches();

    <span class="hljs-comment">// 为此上下文初始化生命周期处理器</span>
    <span class="hljs-comment">// 初始化所有的 LifecycleProcessor</span>
    <span class="hljs-comment">// 在 Spring 中还提供了 Lifecycle 接口， Lifecycle 中包含 start/stop 方法，</span>
    <span class="hljs-comment">// 实现此接口后 Spring 会保证在启动的时候调用其 start 方法开始生命周期，</span>
    <span class="hljs-comment">// 并在 Spring 关闭的时候调用 stop 方法来结束生命周期，通常用来配置后台程序，在启动后一直运行</span>
    <span class="hljs-comment">// （如对 MQ 进行轮询等）。ApplicationContext 的初始化最后正是保证了这一功能的实现。</span>
    initLifecycleProcessor();

    <span class="hljs-comment">// 将刷新完成事件广播到生命周期处理器</span>
    getLifecycleProcessor().onRefresh();

    <span class="hljs-comment">// 广播上下文刷新完成事件</span>
    publishEvent(<span class="hljs-keyword">new</span> ContextRefreshedEvent(<span class="hljs-keyword">this</span>));

    <span class="hljs-comment">// 将spring容器注册到LiveBeansView</span>
    <span class="hljs-comment">// 和MBeanServer和MBean有关的。相当于把当前容器上下文，注册到MBeanServer里面去。</span>
    <span class="hljs-comment">// MBeanServer持有了容器的引用，就可以拿到容器的所有内容，也就让Spring支持到了MBean的相关功能</span>
    LiveBeansView.registerApplicationContext(<span class="hljs-keyword">this</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​</p>
<h1 data-id="heading-19">4、预告： 下一篇幅将对Spring Bean的实例化过程源码部分以及AOP容器的创建及调用流程做详细分析。</h1></div>  
</div>
            