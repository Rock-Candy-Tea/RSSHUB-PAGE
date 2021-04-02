
---
title: 'Java后端架构开荒实战（二）——单机到集群'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c63eed412ee43229711755b07165227~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Apr 2021 18:19:26 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c63eed412ee43229711755b07165227~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>上一篇文章做了一些准备工作，这边文章正式开始写代码。</p>
<p>在做好单实例架构之后，升级到集群是一件很容易的事情，所以把单机和集群放在这一篇一起说。</p>
<h2 data-id="heading-1">二、单体项目架构</h2>
<p>在开始前先说一下本文一些名词的定义吧。</p>
<ul>
<li>组织(org)：这个就是公司的意思，一个公司组织下面可能会有多个项目。</li>
<li>项目(project)：项目在内部是要自洽的，项目和项目的调用之间就属于第三方调用了。比如本文提到的电商后端就是一个项目，组织公共类库就属于另外一个项目，每个项目有自己的生命周期。</li>
<li>应用（application）：应用一般是一个领域服务的形式，在单体应用中可能是一个业务模块，在微服务架构中可能是一个微服务。</li>
</ul>
<h3 data-id="heading-2">2.1 组织公共类库</h3>
<p>这种二方库一般是公司组织级别的，就是封装了所有项目都可能用到的公共方法、配置和工具类等等，注意区别与项目里面的公共类库，这些类库的设计要注意通用性。</p>
<p>一些项目级别的专有配置和工具就不要放到这里来啦。</p>
<p>可以按照springboot源码那样按maven模块组织，也可以简单一点只分包吧。</p>
<p>贴一下web方面经常需要的配置：</p>
<p>统一返回结果BaseResult，一个通用的用接口层的范型返回对象是非常重要的。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaseResult</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-comment">/**
     * 返回状态
     */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">boolean</span> success;
    <span class="hljs-comment">/**
     * 返回状态码
     */</span>
    <span class="hljs-keyword">private</span> String code;
    <span class="hljs-comment">/**
     * 返回信息
     */</span>
    <span class="hljs-keyword">private</span> String message;
    <span class="hljs-comment">/**
     * 返回数据
     */</span>
    <span class="hljs-keyword">private</span> T data;
    ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>跨域配置，注意这里@ConditionalOnWebApplication web应用才生效。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * <p>
 * 跨域配置
 * </p>
 *
 * <span class="hljs-doctag">@author</span> robbendev
 */</span>
<span class="hljs-meta">@ConditionalOnWebApplication</span>
<span class="hljs-meta">@Configuration</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GlobalCorsConfig</span> </span>&#123;


    <span class="hljs-meta">@Bean</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> CorsFilter <span class="hljs-title">corsFilter</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-comment">//1.添加CORS配置信息</span>
        CorsConfiguration config = <span class="hljs-keyword">new</span> CorsConfiguration();
        <span class="hljs-comment">//放行哪些原始域</span>
        config.addAllowedOrigin(<span class="hljs-string">"*"</span>);

        <span class="hljs-comment">//是否发送Cookie信息</span>
        config.setAllowCredentials(<span class="hljs-keyword">true</span>);
        <span class="hljs-comment">//放行哪些原始域(请求方式)</span>
        config.addAllowedMethod(<span class="hljs-string">"*"</span>);
        <span class="hljs-comment">//放行哪些原始域(头部信息)</span>
        config.addAllowedHeader(<span class="hljs-string">"*"</span>);

        config.setMaxAge(<span class="hljs-number">3600L</span>);
        <span class="hljs-comment">//暴露哪些头部信息（因为跨域访问默认不能获取全部头部信息）</span>
        config.addExposedHeader(<span class="hljs-string">"Content-Type"</span>);
        config.addExposedHeader(<span class="hljs-string">"X-Requested-With"</span>);
        config.addExposedHeader(<span class="hljs-string">"accept"</span>);
        config.addExposedHeader(<span class="hljs-string">"Origin"</span>);
        config.addExposedHeader(<span class="hljs-string">"Access-Control-Request-Method"</span>);
        config.addExposedHeader(<span class="hljs-string">"Access-Control-Request-Headers"</span>);

        <span class="hljs-comment">//2.添加映射路径</span>
        UrlBasedCorsConfigurationSource configSource = <span class="hljs-keyword">new</span> UrlBasedCorsConfigurationSource();
        configSource.registerCorsConfiguration(<span class="hljs-string">"/**"</span>, config);

        <span class="hljs-comment">//3.返回新的CorsFilter.</span>
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> CorsFilter(configSource);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通用业务异常，web应用的一般在业务层抛出手动抛出，由全局异常捕获转然后转化成通用返回值返回。</p>
<pre><code class="hljs language-kava copyable" lang="kava">/**
 * 通用业务异常
 *
 * @author robbendev
 */
@EqualsAndHashCode(callSuper = true)
@Data
public class BizException extends RuntimeException implements Serializable &#123;

    /**
     * 序列化
     */
    private static final long serialVersionUID = -4636716497382947499L;

    /**
     * 错误码
     */
    private String code;

    /**
     * 错误信息
     */
    private String message;

    /**
     * 错误详情
     */
    private Object data;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>备份流 （RequestBakRequestWrapper就不贴了），拦截器那里会用到。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 对request请求进行包装备份请求参数
 *
 * <span class="hljs-doctag">@author</span> robbendev
 */</span>
<span class="hljs-meta">@ConditionalOnWebApplication</span>
<span class="hljs-meta">@Component</span>
<span class="hljs-meta">@ServletComponentScan</span>
<span class="hljs-meta">@WebFilter(filterName = "requestBakFilter")</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RequestBakFilter</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Filter</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">init</span><span class="hljs-params">(FilterConfig filterConfig)</span> <span class="hljs-keyword">throws</span> ServletException </span>&#123;

    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">doFilter</span><span class="hljs-params">(ServletRequest request, ServletResponse response, FilterChain chain)</span> <span class="hljs-keyword">throws</span> IOException, ServletException </span>&#123;
        HttpServletRequest servletRequest = (HttpServletRequest) request;
        RequestBakRequestWrapper requestWrapper = <span class="hljs-keyword">new</span> RequestBakRequestWrapper(servletRequest);
        chain.doFilter(requestWrapper, response);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">destroy</span><span class="hljs-params">()</span> </span>&#123;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他的配置各个公司的最佳实践不一而同。</p>
<h3 data-id="heading-3">2.2 项目公共类库</h3>
<p>这种公共类库是项目级别的，每个不同的项目会有项目内部的自定义公用类库需求。</p>
<p>如果你需要web开发就需要springboot-web诸如此类，这些就定义在这里。</p>
<h4 data-id="heading-4">项目依赖</h4>
<p>shop-common/pom/xml</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">parent</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbendev-shop-backend<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>1.0-SNAPSHOT<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">parent</span>></span>
<span class="hljs-tag"><<span class="hljs-name">modelVersion</span>></span>4.0.0<span class="hljs-tag"></<span class="hljs-name">modelVersion</span>></span>

<span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>shop-common<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
<span class="hljs-tag"><<span class="hljs-name">packaging</span>></span>jar<span class="hljs-tag"></<span class="hljs-name">packaging</span>></span>


<span class="hljs-tag"><<span class="hljs-name">dependencies</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.springframework.boot<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>spring-boot-starter-web<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependencies</span>></span>
...


<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">用户登陆</h4>
<p>用户登陆算是比较独立的模块，单拎一小节。</p>
<ul>
<li>spring security + jwt的方案。</li>
<li>服务端session这种。</li>
</ul>
<p>大家可以自行搜索一下oauth2.0和一些单点登录的方案。</p>
<p>shop项目的话用户登陆token签发是通过服务端session来做的。对应的服务定义在shop-common里面。贴一个token的本地缓存简单实现</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Service</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TokenServiceImpl</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">TokenService</span> </span>&#123;

    <span class="hljs-keyword">private</span> Map<String, Token> session = <span class="hljs-keyword">new</span> ConcurrentHashMap<>();

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">save</span><span class="hljs-params">(Token token)</span> </span>&#123;
        session.put(token.getToken(), token);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">remove</span><span class="hljs-params">(String token)</span> </span>&#123;
        session.remove(token);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>有兴趣的同学可以试试如何实现过期缓存。</p>
</blockquote>
<h4 data-id="heading-6">文件服务</h4>
<p>不贴代码了，也是属于shop-common模块的，各个云服务商都提供样板代码。
注意做成接口实现分离形式，在项目里浅封装一下。</p>
<h4 data-id="heading-7">其他</h4>
<p>还有一些应用级别的配置类、拦截器，日志处理等等。代码先不贴了，这些实践现在都很成熟。</p>
<h3 data-id="heading-8">2.3 应用模块组织</h3>
<p>如何组织我们项目的业务模块能够有一个比较好的扩展性？</p>
<ol>
<li>业务模块全部放在一个maven模块里面，通过分包的方式组织模块。</li>
</ol>
<p>这种方式通过分包的方式组织模块，但是由于没有架构层面的强约束，很容易各个模块的方法混在一起，在后期不容易拆分。</p>
<ol start="2">
<li>通过maven模块化组织，让每个模块引入其他业务模块的接口，每个业务模块实现自己的业务方法。</li>
</ol>
<p>明显可以看到第二种方式在大型项目后台中有一个比较好的拓展性：</p>
<ul>
<li>实现了模块之间的解耦合。</li>
<li>如果是单体应用部署只用打包在一起部署，如果是微服务的话引入服务层框架，对每个模块单独部署。升级方便。</li>
<li>避免在项目初期引入过多复杂的组件，同时又有快速扩展能力。按需升级。</li>
</ul>
<p>贴代码robbendev-shop-backend整理架构  ：</p>
<pre><code class="copyable">├── boot  //聚合了所有模块的单应用启动模块
│   ├── pom.xml
│   └── src
│       ├── main
│       └── test
├── build  //这里指定了打包顺序
│   ├── pom.xml
├── pom.xml
├── shop-common  //项目的公用类库
│   ├── pom.xml
│   └── src
└── shop-modules  //项目的模块拆分
    ├── pom.xml
    ├── shop-market  //营销模块 
    │   ├── market-interfaces //营销服务接口二方库
    │   ├── market-service   //营销服务
    │   ├── pom.xml
    ├── shop-orders  //订单模块
    │   ├── orders-interfaces //订单服务接口二方库
    │   ├── orders-service  //订单服务
    │   ├── pom.xml
    ├── shop-product //产品服务
    │   ├── pom.xml  
    │   ├── product-interfaces //产品服务接口二方库
    │   ├── product-service  //产品服务
    └── shop-user  //用户服务
        ├── pom.xml
        ├── user-interfaces //用户服务接口二方库
        └── user-service   //用户服务
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到不同模块是按照模块组织，每个业务模块通过ineterfaces模块和其他模块通信。</p>
<h3 data-id="heading-9">2.4 应用架构</h3>
<h4 data-id="heading-10">应用架构的方法论</h4>
<p>下面看一下单个应用模块如何组织，单个应用构建的的方法论现在已经比较成熟，这里说两种</p>
<ol>
<li>经典的三层架构- controller、service、dao、entity</li>
</ol>
<p>这种很容易让service层膨胀的很大，一个类几千行，每个方法可能会变成事务脚本。</p>
<p>好处就是比较符合直觉思维，写起来也快，代码阅读起来也比较顺利。
缺点可能service层过于臃肿，代码的业务含义不强。</p>
<ol start="2">
<li>ddd建模 - interfaces、application、infrastruture、domain</li>
</ol>
<p>这个可以参考一下相关书籍，这里不赘述。我自己还是比较偏向这一种的，现在也慢慢开始流行起来了。一些核心的概念包括聚合、仓储、领域服务、领域事件、应用服务等。</p>
<p>领域对象建模主要是帮助如何建设一个自洽的应用，是属于应用层而不是架构层的方法论。但是由于领域对象建模的思想和微服务思想有大部分相似的地方，所以在做微服务的拆分的时候可以用领域对象方法来做指导，其实微服务拆分本来就是业务模块、限界上下文的划分。</p>
<p>完全的领域建模落地实施起来会比较困难，尤其是在实体的状态管理，领域事件溯源等。所以在实际开发中不用完全照搬领域对象建模的概念，接下来我贴一下我自己的领域对象建模实践。</p>
<p>首先刚才说到的接口实现分离，把二方库依赖版本添加到之前我们提到的统一二方库依赖pom.xml中</p>
<p>贴一下market-service的pom：</p>
<pre><code class="hljs language-xml copyable" lang="xml">//...
<span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbdendev-common<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;robbendev-common.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>

<span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>shop-common<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;robbendev-shop-backend.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>

<span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>market-interfaces<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;robbendev-shop-backend.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>

<span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>orders-interfaces<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;robbendev-shop-backend.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>

<span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>product-interfaces<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;robbendev-shop-backend.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>

...

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就可以通过接口访问其他模块的方法。</p>
<p>贴一下单个模块的分包，这里单个业务其实可以继续分模块解耦合，但是考虑项目初期的业务复杂程度不会很大，所以还是只分包做分层处理，模块开发的时候团队之间约定好一些基本规范。
order模块按照领域对象建模的分包:</p>
<pre><code class="copyable">├── orders-interfaces
│   ├── pom.xml
│   └── src
│       ├── main
│       │   ├── java
│       │   │   └── com.robbebdev.shop.order
│       │   │                   ├── dto //模块接口参数
│       │   │                   │   ├── request //入参定义
│       │   │                   │   └── response //出参定义
│       │   │                   └── service  //模块服务接口
├── orders-service
│   ├── pom.xml
│   └── src
│       ├── main
│       │   ├── java
│       │   │   └── com.robbendev.shop.order
│       │   │                   ├── application //应用服务层
│       │   │                   ├── domain //领域层
│       │   │                   ├── infrastucture //基础设施层
│       │   │                   └── interfaces //用户接口层
├── pom.xml

<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到有两个maven模块
一个是interfaces模块，里面有模块接口定义和参数定义
一个是service模块，里面会在用户接口层实现interfaces里面的服务接口方法，其他层就和一个ddd的项目差不多。</p>
<h4 data-id="heading-11">业务代码</h4>
<p>贴一个demo接口具体实现吧，以订单模块为例子，现在写一个更新订单接口。</p>
<pre><code class="copyable">├── orders-interfaces
│   └── src
│       ├── main
│       │   ├── java
│       │   │   └── com
│       │   │       └── robbendev.shop.order.dto
│       │   │                   │   ├── request
│       │   │                   │   │   └── FindOrderReq.java
│       │   │                   │   └── response
│       │   │                   │       └── FindOrderResp.java
│       │   │                   └── service
│       │   │                       └── IOrderApi.java
├── orders-service
│   └── src
│       ├── main
│       │   ├── java
│       │   │   └── com
│       │   │       └── robbendev
│       │   │           └── shop
│       │   │               └── order
│       │   │                   ├── application
│       │   │                   │   ├── IOrderService.java //应用服务接口 
│       │   │                   │   └── IOrderServiceImpl.java //应用服务实现类 其实这里可以不用接口，但是兼容一些人的开发习惯吧。
│       │   │                   ├── domain
│       │   │                   │   ├── Order.java  //实体
│       │   │                   │   └── OrderRepository.java //仓储接口
│       │   │                   ├── infrastucture
│       │   │                   │   ├── dataobject
│       │   │                   │   │   └── OrderDO.java //数据对象
│       │   │                   │   ├── mapper
│       │   │                   │   │   └── OrderMapper.java //数据接口
│       │   │                   │   └── repository
│       │   │                   │       └── OrderRepositoryImpl.java //仓储的db实现
│       │   │                   └── interfaces
│       │   │                       └── OrderController.java //暴露的外部api，需要实现interfaces包中的 IOrderApi


<span class="copy-code-btn">复制代码</span></code></pre>
<p>模块间通信api</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * <p>
 * 模块通信的api,具体的实现在用户接口层。
 * </p>
 *
 * <span class="hljs-doctag">@author</span> robbendev
 * <span class="hljs-doctag">@since</span> 2021/4/1 5:07 下午
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">IOrderApi</span> </span>&#123;

    <span class="hljs-function">BaseResult<FindOrderResp> <span class="hljs-title">findOrder</span><span class="hljs-params">(FindOrderReq req)</span></span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>应用服务</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * <p>
 * 应用服务，这里是浅浅的一层，可以作为领域层的门面，实体到出参的转换在这里做。
 * </p>
 *
 * <span class="hljs-doctag">@author</span> robbendev
 * <span class="hljs-doctag">@since</span> 2021/4/1 5:35 下午
 */</span>
<span class="hljs-meta">@Service</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">IOrderServiceImpl</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">IOrderService</span> </span>&#123;

    <span class="hljs-meta">@Resource</span>
    OrderRepository orderRepository;


    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> FindOrderResp <span class="hljs-title">findOrder</span><span class="hljs-params">(FindOrderReq req)</span> </span>&#123;
        Order order = orderRepository.findById(req.getId());
        FindOrderResp findOrderResp = <span class="hljs-keyword">new</span> FindOrderResp();
        findOrderResp.setAmount(order.getAmount());
        findOrderResp.setProductName(order.getProductName());
        findOrderResp.setId(order.getId());

        <span class="hljs-keyword">return</span> findOrderResp;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实体</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 实体，聚合，聚合根！概念参考ddd。像id这些可以用primitive domain实现，像这样。
 * <code>private OrderId id;</code>
 *
 * <span class="hljs-doctag">@author</span> robbendev
 * <span class="hljs-doctag">@since</span> 2021/4/1 5:14 下午
 */</span>
<span class="hljs-meta">@Data</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Order</span> </span>&#123;

    <span class="hljs-keyword">private</span> Long id;
    <span class="hljs-keyword">private</span> BigDecimal amount;
    <span class="hljs-keyword">private</span> String productName;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>仓储接口</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * <p>
 * 仓储接口，概念参考ddd，可以有多个实现，db实现呀，es实现等。
 * </p>
 *
 * <span class="hljs-doctag">@author</span> robbendev
 * <span class="hljs-doctag">@since</span> 2021/4/1 5:25 下午
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">OrderRepository</span> </span>&#123;

    <span class="hljs-function">Order <span class="hljs-title">findById</span><span class="hljs-params">(Long id)</span></span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>数据对象</p>
<pre><code class="copyable">/**
 * <p>
 * 数据对象，和数据库表字段一一对应。
 * </p>
 *
 * @author robbendev
 * @since 2021/4/1 5:16 下午
 */
@Data
public class OrderDO &#123;

    private Long id;
    private BigDecimal amount;
    private String productName;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>数据库访问接口</p>
<pre><code class="copyable">/**
 * <p>
 * 数据库访问接口
 * </p>
 *
 * @author robbendev
 * @since 2021/4/1 5:27 下午
 */
@Mapper
public interface OrderMapper &#123;

    @Select("select * from order where id =#&#123;id&#125;")
    OrderDO getById(Long id);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>仓储的实现</p>
<pre><code class="copyable">/**
 * <p>
 * 仓储的db实现。
 * </p>
 *
 * @author robbendev
 * @since 2021/4/1 5:25 下午
 */
@Component
public class OrderRepositoryDBImpl implements OrderRepository &#123;

    @Resource
    OrderMapper orderMapper;


    @Override
    public Order findById(Long id) &#123;

        OrderDO orderDO = orderMapper.getById(id);

        //对象转换替换方案 mapsStruct 或者beanUtils。
        //有对实体作状态跟踪的方案，但是比较复杂，这里没有选用。
        //所以在ddd选型的时候不用全上，适合就好。
        Order order = new Order();
        order.setId(orderDO.getId());
        order.setAmount(orderDO.getAmount());
        order.setProductName(orderDO.getProductName());

        return order;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用户接口</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * <p>
 * 用户接口（user interface,概念参考ddd）api
 * </p>
 *
 * <span class="hljs-doctag">@author</span> robbendev
 * <span class="hljs-doctag">@since</span> 2021/4/1 5:13 下午
 */</span>
<span class="hljs-meta">@RestController</span>
<span class="hljs-meta">@RequestMapping("/order")</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OrderController</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">IOrderApi</span> </span>&#123;

    <span class="hljs-meta">@Resource</span>
    IOrderService orderService;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-meta">@PostMapping("/findOrder")</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> BaseResult<FindOrderResp> <span class="hljs-title">findOrder</span><span class="hljs-params">(<span class="hljs-meta">@RequestBody</span> FindOrderReq req)</span> </span>&#123;
        FindOrderResp resp = orderService.findOrder(req);
        <span class="hljs-keyword">return</span> BaseResult.success(resp);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数据库ddl和配置文件就不写了，就一个springboot默认数据库配置。</p>
<h3 data-id="heading-12">2.5 单体应用启动</h3>
<p>在集成之前先看下build模块打包项目pom配置，因为要注意一下打包顺序。</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">parent</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbendev-shop-backend<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>1.0-SNAPSHOT<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">parent</span>></span>
<span class="hljs-tag"><<span class="hljs-name">modelVersion</span>></span>4.0.0<span class="hljs-tag"></<span class="hljs-name">modelVersion</span>></span>

<span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>build<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>

<span class="hljs-tag"><<span class="hljs-name">packaging</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">packaging</span>></span>

<span class="hljs-tag"><<span class="hljs-name">modules</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>../shop-common<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>../shop-modules/shop-market/market-interfaces<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>../shop-modules/shop-orders/orders-interfaces<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>../shop-modules/shop-product/product-interfaces<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>../shop-modules/shop-user/user-interfaces<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>../shop-modules/shop-market/market-service<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>../shop-modules/shop-orders/orders-service<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>../shop-modules/shop-product/product-service<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>../shop-modules/shop-user/user-service<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>../boot<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
<span class="hljs-tag"></<span class="hljs-name">modules</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到先打包项目公共类库（根据之前的概念，组织公共类库的发布是属于另外的项目，应该有独立的生命周期。），再打包模块接口，最后打包模块应用。这样就不会出现说”哎呀，你搞了什么，我怎么这个文件又找不到。“</p>
<p>再看boot模块的pom文件和代码</p>
<pre><code class="copyable"><parent>
    <artifactId>robbendev-shop-backend</artifactId>
    <groupId>com.robbendev</groupId>
    <version>1.0-SNAPSHOT</version>
</parent>
<modelVersion>4.0.0</modelVersion>

<packaging>jar</packaging>
<artifactId>boot</artifactId>


<dependencies>

    <dependency>
        <groupId>com.robbendev</groupId>
        <artifactId>market-interfaces</artifactId>
    </dependency>

    <dependency>
        <groupId>com.robbendev</groupId>
        <artifactId>market-service</artifactId>
    </dependency>

    <dependency>
        <groupId>com.robbendev</groupId>
        <artifactId>orders-interfaces</artifactId>
    </dependency>

    <dependency>
        <groupId>com.robbendev</groupId>
        <artifactId>orders-service</artifactId>
    </dependency>
    
    //...产品用户


</dependencies>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在boot模块里面，几行代码就可以运行一个springboot web程序</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * <p>
 *
 * </p>
 *
 * <span class="hljs-doctag">@author</span> robbendev
 * <span class="hljs-doctag">@since</span> 2021/3/31 2:43 下午
 */</span>
<span class="hljs-meta">@SpringBootApplication</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppBoot</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        SpringApplication.run(AppBoot.class, args);
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行成功截图</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">01</span> <span class="hljs-number">16</span>:<span class="hljs-number">40</span>:<span class="hljs-number">33.987</span>  INFO <span class="hljs-number">9926</span> --- [           main] com.robbendev.shop.AppBoot               : Starting AppBoot on huluobindeMacBook-Pro.local with PID <span class="hljs-number">9926</span> (/Users/huluobin/IdeaProjects/robbendev-shop-backend/boot/target/classes started by huluobin in /Users/huluobin/IdeaProjects/robbendev-common)
<span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">01</span> <span class="hljs-number">16</span>:<span class="hljs-number">40</span>:<span class="hljs-number">33.991</span>  INFO <span class="hljs-number">9926</span> --- [           main] com.robbendev.shop.AppBoot               : No active profile set, falling back to <span class="hljs-keyword">default</span> profiles: <span class="hljs-keyword">default</span>
<span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">01</span> <span class="hljs-number">16</span>:<span class="hljs-number">40</span>:<span class="hljs-number">34.856</span>  INFO <span class="hljs-number">9926</span> --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : <span class="hljs-function">Tomcat initialized with <span class="hljs-title">port</span><span class="hljs-params">(s)</span>: 8080 <span class="hljs-params">(http)</span>
2021-04-01 16:40:34.868  INFO 9926 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2021-04-01 16:40:34.869  INFO 9926 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.37]
2021-04-01 16:40:34.969  INFO 9926 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2021-04-01 16:40:34.970  INFO 9926 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 887 ms
2021-04-01 16:40:35.150  INFO 9926 --- [           main] o.s.s.concurrent.ThreadPoolTaskExecutor  : Initializing ExecutorService 'applicationTaskExecutor'
2021-04-01 16:40:35.301  INFO 9926 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on <span class="hljs-title">port</span><span class="hljs-params">(s)</span>: 8080 <span class="hljs-params">(http)</span> with context path ''
2021-04-01 16:40:35.309  INFO 9926 --- [           main] com.robbendev.shop.AppBoot               : Started AppBoot in 1.944 <span class="hljs-title">seconds</span> <span class="hljs-params">(JVM running <span class="hljs-keyword">for</span> <span class="hljs-number">3.03</span>)</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>然后post一下我们刚才的接口，一切ok。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c63eed412ee43229711755b07165227~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>好啦，到这里我们整个项目的框架就搭建好了，现在可以按照模块去进行业务开发了。</p>
<h2 data-id="heading-13">三、集群</h2>
<h3 data-id="heading-14">分布式Session</h3>
<p>之前我们token是使用的本地缓存，那么在集群情况下就可能会出现不同请求落在不同实例上，导致缓存失效。解决方案：</p>
<ul>
<li>每个实例都存一份。这样有点浪费。</li>
<li>请求的时候按照一定的路由规则保证每次落在相同的机器上。有点麻烦</li>
<li>把session单独出来。这样需要保证全局缓存的稳定。</li>
</ul>
<p>这里选第三种方案了，也比较主流。看一下redis的实现</p>
<pre><code class="copyable">@Service
public class TokenServiceRedisImpl implements TokenService &#123;
    @Resource
    StringRedisTemplate stringRedisTemplate;

    @Override
    public void save(Token token) &#123;
        stringRedisTemplate.opsForValue().set(token.getToken(), JsonUtilByFsJson.beanToJson(token)
                , 1, TimeUnit.DAYS);
    &#125;

    @Override
    public void remove(String token) &#123;
        stringRedisTemplate.delete(token);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在自己的登陆服务里面切换一下就行。</p>
<h3 data-id="heading-15">负载均衡</h3>
<p>借助Kubernetes的特性，我们可以很容易的实现水平扩容和负载均衡。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5101382258a42ecbdd162124dbc3e66~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
把这玩意直接改成你希望扩展的数量就行，然后kubernetes service会自动负载。</p>
<p>或者改yml</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">spec:</span>
  <span class="hljs-attr">progressDeadlineSeconds:</span> <span class="hljs-number">600</span>
  <span class="hljs-attr">replicas:</span> <span class="hljs-number">1</span>  <span class="hljs-string">//这里改副本数量</span>
  <span class="hljs-attr">revisionHistoryLimit:</span> <span class="hljs-number">10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">小结</h2>
<p>本篇主要覆盖了一个java后端从0到1再到集群的一个过程。主要是一些工程上的实践和方法论，同时也是我自己实践过程的一些心路历程。</p>
<p>在服务层做了集群以后，后面我会继续讲一下数据层一如的一些实践，比如数据源分库，中间件分库分表等等，最后再讲微服务。风格的话还是和这篇文章类似。</p>
<p>觉得有收获的同学们帮忙点个赞。<br>
拍砖或者联系我<a href="mailto:robbendev@gmail.com">robbendev@gmail.com</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            