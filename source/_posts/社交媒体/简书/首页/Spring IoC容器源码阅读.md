
---
title: 'Spring IoC容器源码阅读'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/8926909-70b8cc67ac059bc2.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/8926909-70b8cc67ac059bc2.png'
---

<div>   
<p>最近磕Spring源码有一段时间，直接上手阅读的难度还是非常大，体系庞大且分支线繁杂，我在阅读的时候，进入各种实现类很容易绕的不知所踪了，因此打算把阅读的Spring源码做一个总结，把核心脉络给梳理出来，后面根据Spring的核心实现也尝试自己去手写一个简易版的Easy-Spring项目，体会下手撸造轮子的感觉。</p>
<p>IoC容器的顶级类：BeanFactory，负责生产 bean 的工厂，同时管理各个 bean 实例，可以先来看下和 BeanFactory 接口相关的主要的继承结构：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1386" data-height="842"><img data-original-src="//upload-images.jianshu.io/upload_images/8926909-70b8cc67ac059bc2.png" data-original-width="1386" data-original-height="842" data-original-format="image/png" data-original-filesize="138282" src="https://upload-images.jianshu.io/upload_images/8926909-70b8cc67ac059bc2.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">BeanFactory体系</div>
</div>
<p>除了 BeanFactory 接口外，还有一个重要的 ApplicationContext 其实就是一个 BeanFactory，但是BeanFactory 只提供了最简单的容器的功能（实例化对象和拿对象的功能），所以被称为低级容器，而ApplicationContext 则是一个高级的容器，提供了更多的有用的功能，如国际化、访问资源、消息发送、响应机制等。下面就从IoC容器的启动开始讲起：</p>
<h3>Refresh主流程</h3>
<hr>
<p>首先是IoC的容器启动，第一步要从 ClassPathXmlApplicationContext 的构造方法说起，通过分析<code>ClassPathXmlApplicationContext</code>类，首先是调用自己的构造方法，然后开始调用最重要的refresh()方法，容器可以去调用 refresh() 这个方法重建ApplicationContext 的，<code>refresh()</code>会将原来的 ApplicationContext 销毁，然后再重新执行一次初始化操作。此处贴上最核心的<code>refresh()</code>方法源码与解析：</p>
<pre><code>@Override
public void refresh() throws BeansException, IllegalStateException &#123;
   // 来个锁，不然 refresh() 还没结束，你又来个启动或销毁容器的操作，那不就乱套了嘛
   synchronized (this.startupShutdownMonitor) &#123;

      // 准备工作，记录下容器的启动时间、标记“已启动”状态、处理配置文件中的占位符
      prepareRefresh();

      // 这步比较关键，这步完成后，配置文件就会解析成一个个 Bean 定义，注册到 BeanFactory 中，
      // 当然，这里说的 Bean 还没有初始化，只是配置信息都提取出来了，
      // 注册也只是将这些信息都保存到了注册中心(说到底核心是一个 beanName-> beanDefinition 的 map)
      ConfigurableListableBeanFactory beanFactory = obtainFreshBeanFactory();

      // 设置 BeanFactory 的类加载器，添加几个 BeanPostProcessor，手动注册几个特殊的 bean
      // 这块待会会展开说
      prepareBeanFactory(beanFactory);

      try &#123;
         // 【这里需要知道 BeanFactoryPostProcessor 这个知识点，Bean 如果实现了此接口，
         // 那么在容器初始化以后，Spring 会负责调用里面的 postProcessBeanFactory 方法。】

         // 这里是提供给子类的扩展点，到这里的时候，所有的 Bean 都加载、注册完成了，但是都还没有初始化
         // 具体的子类可以在这步的时候添加一些特殊的 BeanFactoryPostProcessor 的实现类或做点什么事
         postProcessBeanFactory(beanFactory);
         // 调用 BeanFactoryPostProcessor 各个实现类的 postProcessBeanFactory(factory) 回调方法
         invokeBeanFactoryPostProcessors(beanFactory);          
         // 注册 BeanPostProcessor 的实现类，注意看和 BeanFactoryPostProcessor 的区别
         // 此接口两个方法: postProcessBeforeInitialization 和 postProcessAfterInitialization
         // 两个方法分别在 Bean 初始化之前和初始化之后得到执行。这里仅仅是注册，之后会看到回调这两方法的时机
         registerBeanPostProcessors(beanFactory);

         // 初始化当前 ApplicationContext 的 MessageSource，国际化这里就不展开说了，不然没完没了了
         initMessageSource();

         // 初始化当前 ApplicationContext 的事件广播器，这里也不展开了
         initApplicationEventMulticaster();

         // 从方法名就可以知道，典型的模板方法(钩子方法)，不展开说
         // 具体的子类可以在这里初始化一些特殊的 Bean（在初始化 singleton beans 之前）
         onRefresh();

         // 注册事件监听器，监听器需要实现 ApplicationListener 接口。这也不是我们的重点，过
         registerListeners();

         // 重点，重点，重点
         // 初始化所有的 singleton beans
         //（lazy-init 的除外）
         finishBeanFactoryInitialization(beanFactory);

         // 最后，广播事件，ApplicationContext 初始化完成，不展开
         finishRefresh();
      &#125;

      catch (BeansException ex) &#123;
         if (logger.isWarnEnabled()) &#123;
            logger.warn("Exception encountered during context initialization - " +
                  "cancelling refresh attempt: " + ex);
         &#125;

         // Destroy already created singletons to avoid dangling resources.
         // 销毁已经初始化的 singleton 的 Beans，以免有些 bean 会一直占用资源
         destroyBeans();

         // Reset 'active' flag.
         cancelRefresh(ex);

         // 把异常往外抛
         throw ex;
      &#125;

      finally &#123;
         // Reset common introspection caches in Spring's core, since we
         // might not ever need metadata for singleton beans anymore...
         resetCommonCaches();
      &#125;
   &#125;
&#125;
</code></pre>
<p>主要去看两个关键方法：</p>
<ul>
<li><code>ConfigurableListableBeanFactory beanFactory = obtainFreshBeanFactory();</code></li>
<li><code>finishBeanFactoryInitialization(beanFactory);</code></li>
</ul>
<p>上面的obtainFreshBeanFactory方法是去按照配置文件就会解析成一个个 Bean 定义，注册到 BeanFactory 中，此处的Bean 还没有初始化，只是配置信息都提取出来了，保存到了DefaultListableBeanFactory类里面的一个线程安全的HashMap中：</p>
<p>DefaultListableBeanFactory.java，166行</p>
<pre><code>/** Map of bean definition objects, keyed by bean name. */
private final Map<String, BeanDefinition> beanDefinitionMap = new ConcurrentHashMap<>(256);
</code></pre>
<p>而下一个finishBeanFactoryInitialization方法则是去初始化所有的singleton beans，因此这篇文章也主要是围绕着 refresh 这两个关键方法去梳理工作流程和脉络。</p>
<h3>一、obtainFreshBeanFactory方法</h3>
<hr>
<h4>1. 首先，是创建 Bean 容器前的准备工作：</h4>
<pre><code> // 准备工作，记录下容器的启动时间、标记“已启动”状态、处理配置文件中的占位符
prepareRefresh();
</code></pre>
<h4>2. 创建 Bean 容器，加载并注册 Bean</h4>
<p>这里有一个<code>obtainFreshBeanFactory()</code>。注意，这个方法是全文最重要的部分之一，这里将会<strong>初始化 BeanFactory、加载 Bean、注册 Bean</strong>等等。</p>
<pre><code>protected ConfigurableListableBeanFactory obtainFreshBeanFactory() &#123;
    refreshBeanFactory();
    return getBeanFactory();
&#125;
</code></pre>
<p>这个时候找一下 AbstractRefreshableApplicationContext.java 中的<code>refreshBeanFactory()</code>方法，这里要注意的是这一段：</p>
<pre><code>// 加载 Bean 到 BeanFactory 中
loadBeanDefinitions(beanFactory);
</code></pre>
<p>BeanFactory 是 Bean 容器，那么 Bean 又是什么呢？ BeanDefinition 就是我们所说的 Spring 的 Bean，我们自己定义的各个 Bean 其实会转换成一个个 BeanDefinition 存在于 Spring 的 BeanFactory 中。Bean 在代码层面上可以简单认为是 BeanDefinition 的实例。<br>
<strong><em>BeanDefinition 中保存了我们的 Bean 信息，比如这个 Bean 指向的是哪个类、是否是单例的、是否懒加载、这个 Bean 依赖了哪些 Bean 等等。注意这个里面没有getInstance()获取实例的方法</em></strong></p>
<p>总结一下：到 refresh 中的 obtainFreshBeanFactory 方法，Bean 还没有初始化，只是配置信息都提取出来了，注册也只是将这些信息都保存到了注册中心(说到底核心是一个 beanName-> beanDefinition 的 map)。</p>
<h3>二、finishBeanFactoryInitialization方法</h3>
<hr>
<p>这个 finishBeanFactoryInitialization 方法就是要去初始化所有的 singleton beans，换句话说：<strong>Spring 会在这个阶段完成所有的 singleton beans 的实例化</strong>。首先进入到 AbstractApplicationContext 类里面的 finishBeanFactoryInitialization 方法：</p>
<p>// AbstractApplicationContext.java 834</p>
<pre><code>protected void finishBeanFactoryInitialization(ConfigurableListableBeanFactory beanFactory) &#123;
   // 开始初始化
   beanFactory.preInstantiateSingletons();
&#125;
</code></pre>
<p>又要换一个实现类 DefaultListableBeanFactory 才开始做初始化工作，这里要分两种情况，是否为工厂Bean类型<br>
// DefaultListableBeanFactory 728</p>
<pre><code>public void preInstantiateSingletons() throws BeansException &#123;
            // FactoryBean 的话，在 beanName 前面加上 ‘&’ 符号。再调用 getBean，getBean 方法别急
            final FactoryBean<?> factory = (FactoryBean<?>) getBean(FACTORY_BEAN_PREFIX + beanName);
            // 对于普通的 Bean，只要调用 getBean(beanName) 这个方法就可以进行初始化了
            getBean(beanName);
&#125;
</code></pre>
<h4>AbstractBeanFactory类</h4>
<p>接下来，我们就进入到非常重要的 AbstractBeanFactory 类里面的 getBean(beanName) 方法了，这个方法我们经常用来从 BeanFactory 中获取一个 Bean，初始化的getBean也在这个方法里封装。这里的流程大致概括一下就是：</p>
<ul>
<li>1、先处理Bean 的名称，因为如果以“&”开头的Bean名称表示获取的是对应的 FactoryBean 对象；</li>
<li>2、从缓存中获取单例Bean，有则进一步判断这个Bean是不是在创建中，如果是的就等待创建完毕，否则直接返回这个Bean对象</li>
<li>3、如果不存在单例Bean缓存，则先进行循环依赖的解析</li>
<li>4、解析完毕之后先获取父类BeanFactory，获取到了则调用父类的getBean方法，不存在则先合并然后创建Bean<br>
// AbstractBeanFactory 196</li>
</ul>
<pre><code>@SuppressWarnings("unchecked")
protected <T> T doGetBean(
      final String name, final Class<T> requiredType, final Object[] args, boolean typeCheckOnly)
      throws BeansException &#123;
   // 获取一个 “正统的” beanName，处理两种情况，一个是前面说的 FactoryBean(前面带 ‘&’)，
   // 一个是别名问题，因为这个方法是 getBean，获取 Bean 用的，你要是传一个别名进来，是完全可以的
   final String beanName = transformedBeanName(name);

   // 检查下是不是已经创建过了
   Object sharedInstance = getSingleton(beanName);

   // 检查一下这个 BeanDefinition 在容器中是否存在
   BeanFactory parentBeanFactory = getParentBeanFactory();

   // 先初始化依赖的所有 Bean，这个很好理解。
   // 注意，这里的依赖指的是 depends-on 中定义的依赖
   String[] dependsOn = mbd.getDependsOn();

   // 如果是 singleton scope 的，创建 singleton 的实例
   if (mbd.isSingleton()) &#123;
      return createBean(beanName, mbd, args);
   ｝
&#125;
</code></pre>
<p>把上面的代码串起来一张流程图是长这个样子的：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="883" data-height="514"><img data-original-src="//upload-images.jianshu.io/upload_images/8926909-9840315e9d64bf0a" data-original-width="883" data-original-height="514" data-original-format="image/png" data-original-filesize="20529" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">AbstractBeanFactory类中获取Bean的流程</div>
</div>
<p>假设这个是第一次去初始化bean那么就会走入到本 AbstractBeanFactory 类里面一个虚函数中去：</p>
<pre><code>protected abstract Object createBean(String beanName, RootBeanDefinition mbd, Object[] args) throws BeanCreationException;
</code></pre>
<h4>AbstractAutowireCapableBeanFactory类</h4>
<p>AbstractAutowireCapableBeanFactory 这个类会实现createBean的方法，主要是在真正创建bean之前做一些前置的检查条件，可以很快过一下，进入到真正的 doCreateBean 方法中去。<br>
// AbstractAutowireCapableBeanFactory 447</p>
<pre><code>protected Object createBean(String beanName, RootBeanDefinition mbd, Object[] args) throws BeanCreationException &#123;
   Object beanInstance = doCreateBean(beanName, mbdToUse, args);
&#125;
</code></pre>
<p>接下来我们挑 doCreateBean 中的三个细节出来说说。流程图如下：</p>
<ul>
<li>1、先检查 instanceWrapper变量是不是null，这里一般是null，除非当前正在创建的Bean在 factoryBeanInstanceCache中存在这个是保存还没创建完成的FactoryBean的集合。</li>
<li>2、调用createBeanInstance方法实例化Bean，这个方法在后面会讲解</li>
<li>3、如果当前 RootBeanDefinition对象还没有调用过实现了的 MergedBeanDefinitionPostProcessor 接口的方法，则会进行调用 。</li>
<li>4、 当满足以下三点（1）是单例Bean，（2）尝试解析bean之间的循环引用，（3）bean目前正在创建中<br>
则会进一步检查是否实现了 SmartInstantiationAwareBeanPostProcessor接口如果实现了则调用是实现的 getEarlyBeanReference方法</li>
<li>5、 调用 populateBean方法进行属性填充，这里后面会讲解</li>
<li>6、 调用 initializeBean方法对Bean进行初始化，这里后面会讲解</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="760" data-height="948"><img data-original-src="//upload-images.jianshu.io/upload_images/8926909-dabae6d53bb10547" data-original-width="760" data-original-height="948" data-original-format="image/png" data-original-filesize="83253" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">创建bean的流程图</div>
</div>
<p>把上面的核心步骤抽取出来也就是三个方法：<strong>一个是创建 Bean 实例的 createBeanInstance 方法，一个是依赖注入的 populateBean 方法，还有就是回调方法 initializeBean。</strong>抽取执行的关键代码位置就在如下三处：</p>
<pre><code>protected Object doCreateBean(final String beanName, final RootBeanDefinition mbd, final Object[] args)
      throws BeanCreationException &#123;
   if (instanceWrapper == null) &#123;
      // 说明不是 FactoryBean，这里实例化 Bean，这里非常关键，细节之后再说
      instanceWrapper = createBeanInstance(beanName, mbd, args);
   &#125;
   try &#123;
      // 这一步也是非常关键的，这一步负责属性装配，因为前面的实例只是实例化了，并没有设值，这里就是设值
      populateBean(beanName, mbd, instanceWrapper);
      if (exposedObject != null) &#123;
         // 还记得 init-method 吗？还有 InitializingBean 接口？还有 BeanPostProcessor 接口？
         // 这里就是处理 bean 初始化完成后的各种回调
         exposedObject = initializeBean(beanName, exposedObject, mbd);
      &#125;
   &#125; catch (Throwable ex) &#123;&#125;
&#125;
</code></pre>
<h5>a.创建 Bean 实例</h5>
<p>我们先看看 createBeanInstance 方法。需要说明的是，这个方法如果每个分支都分析下去，必然也是极其复杂冗长的，我们挑重点说。此方法的目的就是实例化我们指定的类。</p>
<pre><code>protected BeanWrapper createBeanInstance(String beanName, RootBeanDefinition mbd, Object[] args) &#123;
   // 调用无参构造函数
   return instantiateBean(beanName, mbd);
&#125;
</code></pre>
<p>挑个简单的无参构造函数构造实例来看看：</p>
<pre><code>protected BeanWrapper instantiateBean(final String beanName, final RootBeanDefinition mbd) &#123;
   // 实例化，关键的地方
   beanInstance = getInstantiationStrategy().instantiate(mbd, beanName, parent);
&#125;
</code></pre>
<p>// SimpleInstantiationStrategy 59</p>
<pre><code>public Object instantiate(RootBeanDefinition bd, String beanName, BeanFactory owner) &#123;
   // 如果不存在方法覆写，那就使用 java 反射进行实例化，否则使用 CGLIB,
   // 方法覆写 请参见附录"方法注入"中对 lookup-method 和 replaced-method 的介绍
   if (bd.getMethodOverrides().isEmpty()) &#123;
      // 利用构造方法进行实例化
      return BeanUtils.instantiateClass(constructorToUse);
   &#125;
   else &#123;
      // 存在方法覆写，利用 CGLIB 来完成实例化，需要依赖于 CGLIB 生成子类，这里就不展开了。
      // tips: 因为如果不使用 CGLIB 的话，存在 override 的情况 JDK 并没有提供相应的实例化支持
      return instantiateWithMethodInjection(bd, beanName, owner);
   &#125;
&#125;
</code></pre>
<h5>b.bean 属性注入</h5>
<p>看完了 createBeanInstance(...) 方法，我们来看看 populateBean(...) 方法，该方法负责进行属性设值，处理依赖。<br>
// AbstractAutowireCapableBeanFactory 1203</p>
<pre><code>protected void populateBean(String beanName, RootBeanDefinition mbd, BeanWrapper bw) &#123;
   // bean 实例的所有属性都在这里了
   PropertyValues pvs = mbd.getPropertyValues();
   // 设置 bean 实例的属性值
   applyPropertyValues(beanName, mbd, bw, pvs);
</code></pre>
<h5>c.initializeBean 初始化</h5>
<p>属性注入完成后，这一步其实就是处理各种回调了，这块代码比较简单。</p>
<p>到此就完成了Spring中IoC容器一遍串讲，已经缩减了大量非关键代码流程，体现出了主脉络，但是关于创建 bean 这一块还可以在下一篇文章中重点安排下，那一块很精华值得深入阅读，主链路的讲解就先到这里。</p>
<p>最后讲一下源码阅读方式，这里有两种：一种是直接初始化一个Spring的工程，然后下载相应的依赖源码，顺着源码一点点读，非常简便，缺点也很明显不能在源码基础上做笔记+注释。还有一种是直接从github上fork源码分支到本地，然后在本地源码基础上加上关键的注释，并且在关键的分支循环上都说明一下原因，虽然这样的源码阅读稍微麻烦点，但是读过以后记忆更深刻，而且可以把注释笔记一并提交到自己git代码仓库里，时刻温故知新。</p>
<h3>主要参考目录</h3>
<hr>
<p>1.<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fjavadoop.com%2Fpost%2Fspring-ioc" target="_blank">Spring IOC 容器源码分析</a><br>
2.<a href="https://www.jianshu.com/p/a85c95a74093" target="_blank">Spring 创建Bean流程</a><br>
3.<a href="https://links.jianshu.com/go?to=https%3A%2F%2Ftech.souyunku.com%2F%3Fp%3D13107" target="_blank">Spring的Bean生命周期，11 张高清流程图及代码，深度解析</a></p>
  
</div>
            