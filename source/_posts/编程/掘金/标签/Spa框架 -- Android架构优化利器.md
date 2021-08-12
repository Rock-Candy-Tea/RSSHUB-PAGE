
---
title: 'Spa框架 -- Android架构优化利器'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3fe83f685aa437e810bb6649bdc25c3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 04:17:31 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3fe83f685aa437e810bb6649bdc25c3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1 背景</h2>
<p>在组件化的模式设计里，模块之间基于接口编程，模块内不对实现类进行硬编码。因为一旦代码里涉及具体的实现类，就违反了可拔插的原则，当需要替换一种实现，就需要修改代码。为了实现在模块装配的时候能不在程序里动态指明，这就需要一种服务发现机制。 SPI就是这样的一个机制：为某个接口寻找服务实现的机制。有点类似IOC的思想，就是将装配的控制权移到程序之外，在模块化设计中这个机制尤其重要。</p>
<h2 data-id="heading-1">2 业界技术方案</h2>
<h3 data-id="heading-2">2.1 常规模块依赖方式</h3>
<p>组件开发过程中，如果想要在模块B中实例化模块A中的类或使用模块A中的方法，常规的方式是让模块B依赖模块A，如下图所示：</p>
<p>                             <img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3fe83f685aa437e810bb6649bdc25c3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是组件化开发过程中，往往并不希望某些模块之间有直接的依赖关系，因为如果依赖关系建立了，模块之间的耦合性就高了。</p>
<h3 data-id="heading-3">2.2 Java的SPI机制</h3>
<p>有没有什么办法可以解决这个问题呢？可以使用Java提供的SPI机制！</p>
<p>SPI(Service Provider Interface)是JDK内置的一种服务发现机制。它的应用还是非常广泛的，尤其在服务端开发技术栈中，</p>
<ul>
<li>
<p>JDBC 中通过 SPI 的方式加载不同的驱动实现</p>
</li>
<li>
<p>SLF4J中通过 SPI 的方式加载不同提供商的日志实现类</p>
</li>
<li>
<p>Gradle源码中有大量的服务是基于 SPI机制来做服务实现扩展的</p>
</li>
<li>
<p>SpringFactoriesLoader 是 Spring 中十分重要的一个扩展机制之一，算是SPI的一个变种，原理基本一致</p>
</li>
</ul>
<h3 data-id="heading-4">2.3 SPI是如何解决上述问题的呢？</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a2ed8221d0c45e4bab314888580f790~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Java的SPI机制使用流程如上图所示，</p>
<ul>
<li>首先需要一个Base模块提供IA接口，模块A和模块B都依赖Base模块</li>
<li>模块A中的类A实现IA接口</li>
<li>SourceSet下创建resources/META-INF/services父目录，</li>
<li>在父目录下创建以IA接口的全限定名为文件名的文本文件，文件内容是IA实现类的全限定名列表，以回车换行分割</li>
<li>最后模块B就可以通过ServiceLoader.load(IA.class)方法来创建模块A中类A对象了</li>
</ul>
<h3 data-id="heading-5"> 2.4 Java原生SPI机制的不足</h3>
<p>如果你熟悉SPI机制那么你会发现，无论是在JDBC, SLF4J,Gradle还是Spring中，一个模块往往只是提供个别关键接口作为一个服务的切入点让外部模块发现，这通常是足够的。</p>
<p>但如果有大量的服务需要被发现，那么就要在resources/META-INF/services目录写很多的接口文件，然后使用ServiceLoader去加载。</p>
<ul>
<li>问题一：写法太繁琐,接口多了不易维护, 能不能简化？</li>
<li>问题二：resources/META-INF/services下配置的接口文件是个配置文件, ServiceLoader通过文件流读出接口实现类的全限定名，再通过反射实例化出具体的实现类对象, 性能较低，而且服务越多性能越低。</li>
<li>问题三:  它只提供了服务发现的能力。ServiceLoader只负责把服务实例化出来。没有对实例化的对象做任何管理。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85e4e011c6e44213b00fbbe599f3415c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">3. 简单易用的SPI机制 -- spa       </h2>
<h3 data-id="heading-7">3.1 spa服务发现机制                   </h3>
<p>github链接: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fluqinx%2Fsp" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/luqinx/sp" ref="nofollow noopener noreferrer">github.com/luqinx/sp</a></p>
<p>spa(Service Pool for Android)将待实例化的类看成一个一个的服务, 是基于Java SPI思想基础之上创建出来的全新的SPI机制，但是他不仅仅只有服务发现能力，还有服务生命周期管理，服务优先级管理，服务拦截管理等等Java SPI之外的能力，它生于Android，但不仅仅只试用于Android端，理论上Jvm环境下都适用。</p>
<p>                          <img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6092c50f6abf457b827286e246819eee~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>spa的基本思想如上图所示:</p>
<ol>
<li>spa使用注解替代了繁琐的services文件配置, 使用方式得到了极大的简化</li>
<li>spa在编译阶段通过字节码生成为被@Service注解标记的接口实现类创建工厂方法，实现类对象通过工厂方法创建，不存在文件流操作也不需要反射实例化对象，提高了性能。</li>
<li>无需读配置，无需缓存映射表，因此spa甚至做到了无需手动初始化。</li>
</ol>
<p>其他类似的框架普遍需要在运行时读配置文件(io)，缓存配置映射表和反射创建对象，这些都会对性能造成一定影响。而spa并不需要，spa在编译阶段生成工厂类来替代配置文件和和缓存映射，这很容易理解。不使用反射，spa是如何创建服务对象的呢？</p>
<p>其实很简单，模块隔离只是一个模式设计, 是为了在开发过程中不让不相关的模块相互之间存在引用关系，从而降低模块之间的耦合性。模块编译后代码最终会变成字节码/jar/aar/dex， 而字节码/jar/aar/dex里并没有模块的概念。通俗的说A类中创建B类对象时，类A并不关心也并不知道类B是写在哪个模块的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62bcb9b04c064d98b1aaeec338cea1e6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这也是为什么spa是使用字节码生成而不是apt代码生成的原因。</p>
<p>到这里, spa已解决了跨模块无直接依赖情况下实例化对象的问题。</p>
<p>                                     <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53b4780a780f4d21b7f6e928d87663a1~tplv-k3u1fbpfcp-watermark.image" alt="就这?就这?就这?就这?就这?表情包图片- 求表情网,斗图从此不求人!" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到这你可能发现，主流的路由组件ARouter也有类似的能力，为什么不直接使用ARouter呢？只是因为spa性能更好一点？ </p>
<p>跨模块实例化对象是spa的核心能力，但远远不是全部，比如spa在什么时候创建服务对象，一个服务被创建后什么时候会被gc回收？</p>
<h3 data-id="heading-8">3.2 spa服务的生命周期</h3>
<p>可以对比一下ARouter, 使用过ARouter的同学应该知道，ARouter通过实现IProvider接口定义一个服务，这个服务创建后是全局生命周期的，且全局唯一相当于一个单例。</p>
<p>这在一些场景下是非常有用的，比如我需要一个全局存储服务StorageService，提供save, get, delete等存储相关能力，我可以任何时候、任意模块下通过StorageService接口获取到的这个单例服务并使用它，非常方便。</p>
<p>但ARouter只能创建全局生命周期的服务，这是不够的，比如多个业务模块都需要一个品类Fragment并命名为CategoryFragment， 为了模块解耦，我需要将CategoryFragment当做一个服务 ，且需要根据不同的品类id创建多个CategoryFragment。ARouter的服务是没办法创建多个的，且因为是单例Fragment无法被回收会造成内存泄漏。</p>
<p>spa可以通过@Service注解的scope字段定义一个服务的生命周期，常用的生命周期就是上述的两种，</p>
<p>StorageService伪代码如下：</p>
<pre><code class="copyable">// 全局生命周期，全局唯一
@Service(scope = Spa.Global)
public class StorageServiceImpl implements StorageService &#123;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CategoryFragment伪代码如下:</p>
<pre><code class="copyable">// 默认生命周期，每次都会创建一个新的CategoryFragment,
@Service
public class CategoryFragment implements CategoryService &#123;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取服务的伪代码如下</p>
<pre><code class="copyable">....

StorageService storageService = Spa.getService(StorageService.class); 

CategoryService categoryFragment = Spa.getService(CategoryService.class);

....
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了以上两种常用生命周期，还有被弱引用、软引用持有的生命周期和自定义生命周期管理。</p>
<h3 data-id="heading-9">3.3 spa服务优先级管理</h3>
<p>当一个服务有多个实现类，那Spa.getService(xx.class)会获取哪一个呢？因此Spa引入服务优先级管理。</p>
<p><strong>3.3.1  为什么需要优先级管理？</strong></p>
<p>当你的想写一个基础服务，而这个服务需要在不同的环境条件下执行不同的行为，有什么好的办法呢？(不同环境可以指不同的编译环境buildType, 也可以是不同的运行环境(Java or Android, windows or Mac), 也可以是不同的业务场景， 甚至可以是不同的项目等等)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3464171b8c704198b062d4f66a87f915~tplv-k3u1fbpfcp-watermark.image" alt="举个栗子卡通图片(第1页) - 要无忧健康图库" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我的项目中内部环境和生产环境的代码是严格分离的，内部环境相关的代码比如日志，调试工具，分析工具，数据Mock等是绝对不会打到生成环境的安装包中的。这保证了生成环境的安全性和性能。</p>
<p>以日志输出为例, </p>
<pre><code class="copyable">public interface LogService implements IService &#123;
    void e(String tag, String message);
    ....
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>内部环境中, 需要将日志输出到控制台，方便发现问题, 因为内部环境代码和生产环境是隔离的，可以将优先级设置高一点。则当它存在时会优先被实例化</p>
<pre><code class="copyable">@Service(scope = Spa.global, priority = 100)
public class AlphaLogService implements LogService &#123;
    
    void e(String tag, String message) &#123;
        ...
        Log.e(tag, message);
    &#125;

    ....
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>线上生产环境，则不能输出到控制台, 而是根据一定策略上传到日志平台，因为代码环境隔离生产环境并不存在AlphaLogService，所以虽然ProductLogService是低优先级，但它依然会被实例化</p>
<pre><code class="copyable">@Service(scope = Spa.global, priority = 10)
public class ProductLogService implements LogService &#123;
    void e(String tag, String message) &#123;        ...
        RemoteLog.e(tag, message);
    &#125;

    ....
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有人可能会觉得: 简单的if-else就能解决的问题你为什么要搞得这么复杂？？？</p>
<p>是的， if-else能解决不同环境使用不同的日志输出，但是if-else很难在环境隔离的前提下拿到不同环境的LogService的实现类</p>
<p><strong>3.3.2 spa也可以同时获取多个服务实现</strong></p>
<p>ServiceLoader的load方法返回的ServiceLoader对象是一个Iterator迭代器，迭代器内容就是服务接口的实现列表。Spa有实现这一个功能吗？直接上代码</p>
<p>假设拦截器服务接口Interceptor，有A, B, C三个拦截器实现</p>
<pre><code class="copyable">// 服务接口
public interface Interceptor extends IService&#123;
    void intercept();
    String interceptorName();
&#125;

// 拦截器A
@Service(priority = 10)
public class AInterceptor implements Interceptor &#123;

    void intercept() &#123;
        System.out.println("interceptor A is running...");
    &#125;    

    public String interceptorName() &#123;
        return "A";
    &#125;
&#125;

// 拦截器B
@Service(priority = 30)
public class BInterceptor implements Interceptor &#123;

    void intercept() &#123;
        System.out.println("interceptor B is running...")
    &#125;

    public String interceptorName() &#123;
        return "B";
    &#125;
&#125;

// 拦截器C
@Service(priority = 20)
public class CInterceptor implements Interceptor &#123;

    void intercept() &#123;
        System.out.println("interceptor C is running...")
    &#125;

    public String interceptorName() &#123;
        return "C";
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Spa使用CombineService来组合多个服务接口实现，CombineService同样也是一个Iterator迭代器，迭代器的返回顺序将按服务器优先级值大小依次返回</p>
<pre><code class="copyable">CombineService<Interceptor> as = Spa.getCombineService(Interceptor.class);
for (Interceptor interceptor: interceptors) &#123;    
    System.out.print(interceptor.interceptorName());
&#125;

// 输出 BCA
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Spa.getCombineService(Interceptor.class)返回的对象也同时是一个Interceptor代理, 当代理对象的intercept()方法执行时，将按优先级顺序依次执行每个服务实现的intercept()方法</p>
<pre><code class="copyable">Interceptor interceptor = Spa.getCombineService(Interceptor.class);
interceptor.intercept();

// 输出
// interceptor B is running...
// interceptor C is running...
// interceptor A is running...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CombineService默认策略是按优先级大小来决定多服务的执行顺序，上面示例中，多个Interceptor服务对象的intercept()方法的调用大体流程如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a870b3911d649a19e44cea1c2c31b20~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>ComineService也可以通过实现CombineStrategy接口来支持自定义执行策略。</p>
<p>1. 定义自定义多服务执行策略</p>
<pre><code class="copyable">public class InterceptorStrategy implements CombineStrategy &#123;
    @Override    
    public boolean filter(Class serviceClass, Method method, Object[] args) &#123;    
        return Interceptor.class.isAssignableFrom(serviceClass); // 选择策略对应的接口
    &#125;

    @Override
    public Object invoke(final List<ServiceProxy> proxies, Class serviceClass, final Method method, final Object[] args) &#123;
        // 自定义调用过程
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2. 使用自定义对服务执行策略</p>
<pre><code class="copyable">Interceptor interceptor = Spa.getCombineService(Interceptor.class, InterceptorStrategy);
interceptor.intercept()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自定义多服务执行策略是非常有用的，在spa的内部就有多处应用</p>
<ul>
<li>场景1: SpRouter中路由拦截策略，业务可以通过实现RouteInterceptor接口，调用onContinue或onInterrapt()来决定是继续路由还是拦截路由，实现类是RouteCombineStrategy。每个路由框架一般都有路由拦截能力，方式大同小异，这里就不再赘述，感兴趣可以自行查看实现方式。</li>
<li>场景2: 自定义生命周期的类型检查策略，实现类是CustomCombineStrategy，感兴趣可以自行查看。</li>
<li>场景3: spa服务拦截的拦截策略，业务可以通过实现IServiceInterceptor接口，调用onContinue或onInterrapt()来决定是继续执行方法还是拦截掉方法不执行，又或者是换一个方法执行等等。服务拦截是spa不可或缺的一部分。</li>
</ul>
<h3 data-id="heading-10">3.4 spa服务拦截</h3>
<p>spa定义的服务默认支持服务拦截能力，通过拦截能力可以实现服务的AOP操作，想要拦截spa的服务也很简单只需要实现IServiceInterceptor接口, 且服务拦截器也被当做服务，所以需要使用@Service注解标记</p>
<pre><code class="copyable">@Service
public class MinPriorityServiceInterceptor implements IServiceInterceptor &#123;    
    @Override    
    public void intercept(Class<? extends IService> originClass, IService source, Method method, Object[] args, IServiceInterceptorCallback callback) &#123;
        logger.log(source.toString() + ": " + method.getName());
        if (method.getReturnType() == int.class) &#123;
            callback.onInterrupt(100); // 拦截方法，并返回100
        &#125; else &#123;
            callback.onContinue(method, args); // 不拦截，继续执行
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以将@Service的注解参数disableIntercept设置为true来禁用服务拦截。</p>
<h3 data-id="heading-11">3.5 服务别名</h3>
<p>上面的介绍都是通过类来查找服务，Spa同时还支持给类设置别名，然后通过别名来查找服务。别名用@Service注解的path(为什么不是alias? 历史原因)参数标识。</p>
<pre><code class="copyable">@Service(path = "firstAlias", scope = Spa.Scope.Global)
public class MyAliasService implements IService &#123;
....
&#125;

// 使用
MyAliasService byPath = Spa.getService("firstAlias");
// spa通过接口/抽象类查找它的实现类/子类对应的服务用getService(IXxx.class)
// spa通过指定具体的服务实现类创建服务对象使用getFixedService(Xxx.class)
MyAliasService byClass = Spa.getFixedService(MyAliasService.class); 
assert byPath == byClass; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Spa的核心是通过类来查找服务，别名查找也是在类查找的基础上做了一层映射: spa在编译阶段生成了PathServicesInstance类，它维护着一张别名(path)到服务类的映射表。</p>
<p><img src="https://airtake-private-data-1254153901.cos.ap-shanghai.myqcloud.com/smart/pontos/162666155046d9e2eaf4c.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDopcCYgw0qRoyV5qfKjvg2pPkqESnb5zI%26q-sign-time%3D1628596922%3B1628600522%26q-key-time%3D1628596922%3B1628600522%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D8ced8e10336feedae33e61a41fe5b9cbdddb00cc" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>﻿</p>
<p>﻿</p>
<h2 data-id="heading-12">4. 总结</h2>
<p>Spa是目前最完备的SPI开源方案，虽然大厂们开源的如ARouter, DRouter, WMRouter等路由方案都有类似的SPI能力，但它们的立足点都是解决Android框架下的路由问题，不是纯粹的SPI方案。而Spa的目标是跨模块创建服务和管理服务，它不关心上层的服务具体是什么，所以Spa的服务管理能力更强大，且更容易扩展。</p>
<p>如果想要ARouter一样的路由能力可以使用spa下的SpRouter, SpRouter就是基于Spa实现的一套路由方案。</p>
<p>﻿</p>
<h2 data-id="heading-13">5. 思考</h2>
<p>想象一下，如果把项目中页面、弹窗、功能都抽象成一个个的服务，然后将这些服务以资源的形式(比如URL)暴露出来给内部和外部访问(比如给混合端(H5, Flutter)访问，通过接口访问，通过推送访问，通过adb访问等等), 当这些服务达到一定规模，整个App是不是变得更加灵活、更加动态化，这就是我当前应用的服务化的框架。</p>
<h2 data-id="heading-14">参考文档：</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Frgb-24bit.github.io%2Fblog%2F2019%2Fjava-spi.html" target="_blank" rel="nofollow noopener noreferrer" title="https://rgb-24bit.github.io/blog/2019/java-spi.html" ref="nofollow noopener noreferrer">rgb-24bit.github.io/blog/2019/j…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fjalja365%2Fp%2F14718532.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/jalja365/p/14718532.html" ref="nofollow noopener noreferrer">www.cnblogs.com/jalja365/p/…</a></p></div>  
</div>
            