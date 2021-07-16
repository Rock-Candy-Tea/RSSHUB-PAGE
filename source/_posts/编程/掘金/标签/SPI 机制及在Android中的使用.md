
---
title: 'SPI 机制及在Android中的使用'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96e0f08cd137494480255989ea2ff82e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 07:12:39 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96e0f08cd137494480255989ea2ff82e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>SPI</code>即 <code>Service Provider Interface</code>，该方案是为某个接口动态寻找服务的机制，类似IOC的思想。</p>
<h2 data-id="heading-0">SPI的使用</h2>
<p>先通过一个简单的例子来对SPI机制有一个初步的认识</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96e0f08cd137494480255989ea2ff82e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">定义接口</h3>
<p>在Android Studio中新建一个module，新增一个接口<code>Machine</code>, 接口定义如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Machine</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">powerOn</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">实现类</h3>
<p>新增两个实现类，分别是<code>TV</code>和<code>Computer</code>, 如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TV</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Machine</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">powerOn</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"TV power on"</span>);
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Computer</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Machine</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">powerOn</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"Computer power on"</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">定义类关系</h3>
<ul>
<li>在<code>main</code>目录下定义一个<code>resources.META-INF.services</code>目录, 在该目录下添加一个名为<code>com.fred.spi.Machine</code>文件，需要注意该文件名必须是和上面的<code>Machine</code>对应上。</li>
<li>在<code>com.fred.spi.Machine</code>文件中添加两行
<pre><code class="copyable">com.fred.spi.impl.Computer
com.fred.spi.impl.TV
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-4">测试</h3>
<ul>
<li>我们定义一个<code>MachineFactory</code>类，用一个工厂来管理。</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MachineFactory</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> MachineFactory mInstance;
    <span class="hljs-keyword">private</span> Iterator<Machine> mIterator;

    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">MachineFactory</span><span class="hljs-params">()</span> </span>&#123;
        ServiceLoader<Machine> loader = ServiceLoader.load(Machine.class);
        mIterator = loader.iterator();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">static</span> MachineFactory <span class="hljs-title">getInstance</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">null</span> == mInstance) &#123;
            <span class="hljs-keyword">synchronized</span> (MachineFactory.class) &#123;
                <span class="hljs-keyword">if</span> (<span class="hljs-keyword">null</span> == mInstance) &#123;
                    mInstance = <span class="hljs-keyword">new</span> MachineFactory();
                &#125;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> mInstance;
    &#125;
    <span class="hljs-function">Machine <span class="hljs-title">getMachine</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> mIterator.next();
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">boolean</span> <span class="hljs-title">hasNextMachine</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> mIterator.hasNext();
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>测试入口文件</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
    MachineFactory factory = MachineFactory.getInstance();
    <span class="hljs-keyword">while</span> (factory.hasNextMachine()) &#123;
       factory.getMachine().powerOn();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行上面的代码会输出</p>
<pre><code class="copyable">Computer power on
TV power on
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从java代码的层面上看，我们并没有任何地方new Computer, TV; 更没有执行其<code>powerOn()</code>方法，只是在一个配置文件里面加了<code>Computer</code>, <code>TV</code>对应的类名。</p>
<h2 data-id="heading-5">SPI机制原理</h2>
<p>在<code>MachineFactory</code>中我们可以看到，加载<code>Machine</code>接口的实现类只依赖于一行代码：</p>
<pre><code class="copyable">ServiceLoader<Machine> loader = ServiceLoader.load(Machine.class);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着只需要对<code>ServiceLoader</code>进行遍历，就可以找到所有有实现类。在上面的例子中，因为我们在<code>com.fred.spi.Machine</code>文件中配了两个，所以能找到两个实现类。</p>
<h2 data-id="heading-6"><code>ServiceLoader</code>的源码</h2>
<p>我们来从<code>ServiceLoader</code>的源码角度看看是如何完成类加载的。由于<code>ServiceLoader</code>是在<code>rt.jar</code>包中, 我们在安装jdk的时候是可以下载一个<code>src.zip</code>文件，可以将该文件导入到IDE中去关联源码，但<code>rt.jar</code>并不在<code>src.zip</code>中，从<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Funofficial-openjdk%2Fopenjdk%2Fblob%2Fjdk8u%2Fjdk8u%2Fjdk%2Fsrc%2Fshare%2Fclasses%2Fjava%2Futil%2FServiceLoader.java" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/unofficial-openjdk/openjdk/blob/jdk8u/jdk8u/jdk/src/share/classes/java/util/ServiceLoader.java" ref="nofollow noopener noreferrer">这里</a>可以拿到相关的代码。
其核心代码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ServiceLoader</span><<span class="hljs-title">S</span>>
    <span class="hljs-keyword">implements</span> <span class="hljs-title">Iterable</span><<span class="hljs-title">S</span>>
</span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String PREFIX = <span class="hljs-string">"META-INF/services/"</span>;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <S> <span class="hljs-function">ServiceLoader<S> <span class="hljs-title">load</span><span class="hljs-params">(Class<S> service)</span> </span>&#123;
        ClassLoader cl = Thread.currentThread().getContextClassLoader();
        <span class="hljs-keyword">return</span> ServiceLoader.load(service, cl);
    &#125;

    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <S> <span class="hljs-function">ServiceLoader<S> <span class="hljs-title">load</span><span class="hljs-params">(Class<S> service,
                                                ClassLoader loader)</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ServiceLoader<>(service, loader);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">ServiceLoader</span><span class="hljs-params">(Class<S> svc, ClassLoader cl)</span> </span>&#123;
        service = Objects.requireNonNull(svc, <span class="hljs-string">"Service interface cannot be null"</span>);
        loader = (cl == <span class="hljs-keyword">null</span>) ? ClassLoader.getSystemClassLoader() : cl;
        acc = (System.getSecurityManager() != <span class="hljs-keyword">null</span>) ? AccessController.getContext() : <span class="hljs-keyword">null</span>;
        reload();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">reload</span><span class="hljs-params">()</span> </span>&#123;
        providers.clear();
        lookupIterator = <span class="hljs-keyword">new</span> LazyIterator(service, loader);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">private</span> Iterator<String> <span class="hljs-title">parse</span><span class="hljs-params">(Class<?> service, URL u)</span>
        <span class="hljs-keyword">throws</span> ServiceConfigurationError
    </span>&#123;
        InputStream in = <span class="hljs-keyword">null</span>;
        BufferedReader r = <span class="hljs-keyword">null</span>;
        ArrayList<String> names = <span class="hljs-keyword">new</span> ArrayList<>();
        <span class="hljs-keyword">try</span> &#123;
            in = u.openStream();
            r = <span class="hljs-keyword">new</span> BufferedReader(<span class="hljs-keyword">new</span> InputStreamReader(in, <span class="hljs-string">"utf-8"</span>));
            <span class="hljs-keyword">int</span> lc = <span class="hljs-number">1</span>;
            <span class="hljs-keyword">while</span> ((lc = parseLine(service, u, r, lc, names)) >= <span class="hljs-number">0</span>);
        &#125; <span class="hljs-keyword">catch</span> (IOException x) &#123;
            fail(service, <span class="hljs-string">"Error reading configuration file"</span>, x);
        &#125; <span class="hljs-keyword">finally</span> &#123;
            <span class="hljs-keyword">try</span> &#123;
                <span class="hljs-keyword">if</span> (r != <span class="hljs-keyword">null</span>) r.close();
                <span class="hljs-keyword">if</span> (in != <span class="hljs-keyword">null</span>) in.close();
            &#125; <span class="hljs-keyword">catch</span> (IOException y) &#123;
                fail(service, <span class="hljs-string">"Error closing configuration file"</span>, y);
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> names.iterator();
    &#125;

    <span class="hljs-keyword">private</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LazyIterator</span>
            <span class="hljs-keyword">implements</span> <span class="hljs-title">Iterator</span><<span class="hljs-title">S</span>>
        </span>&#123;

            Class<S> service;
            ClassLoader loader;
            Enumeration<URL> configs = <span class="hljs-keyword">null</span>;
            Iterator<String> pending = <span class="hljs-keyword">null</span>;
            String nextName = <span class="hljs-keyword">null</span>;

            <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">LazyIterator</span><span class="hljs-params">(Class<S> service, ClassLoader loader)</span> </span>&#123;
                <span class="hljs-keyword">this</span>.service = service;
                <span class="hljs-keyword">this</span>.loader = loader;
            &#125;

            <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">hasNextService</span><span class="hljs-params">()</span> </span>&#123;
                <span class="hljs-keyword">if</span> (nextName != <span class="hljs-keyword">null</span>) &#123;
                    <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
                &#125;
                <span class="hljs-keyword">if</span> (configs == <span class="hljs-keyword">null</span>) &#123;
                    <span class="hljs-keyword">try</span> &#123;
                        String fullName = PREFIX + service.getName();
                        <span class="hljs-keyword">if</span> (loader == <span class="hljs-keyword">null</span>)
                            configs = ClassLoader.getSystemResources(fullName);
                        <span class="hljs-keyword">else</span>
                            configs = loader.getResources(fullName);
                    &#125; <span class="hljs-keyword">catch</span> (IOException x) &#123;
                        fail(service, <span class="hljs-string">"Error locating configuration files"</span>, x);
                    &#125;
                &#125;
                <span class="hljs-keyword">while</span> ((pending == <span class="hljs-keyword">null</span>) || !pending.hasNext()) &#123;
                    <span class="hljs-keyword">if</span> (!configs.hasMoreElements()) &#123;
                        <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
                    &#125;
                    pending = parse(service, configs.nextElement());
                &#125;
                nextName = pending.next();
                <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
            &#125;

            <span class="hljs-function"><span class="hljs-keyword">private</span> S <span class="hljs-title">nextService</span><span class="hljs-params">()</span> </span>&#123;
                <span class="hljs-keyword">if</span> (!hasNextService())
                    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> NoSuchElementException();
                String cn = nextName;
                nextName = <span class="hljs-keyword">null</span>;
                Class<?> c = <span class="hljs-keyword">null</span>;
                <span class="hljs-keyword">try</span> &#123;
                    c = Class.forName(cn, <span class="hljs-keyword">false</span>, loader);
                &#125; <span class="hljs-keyword">catch</span> (ClassNotFoundException x) &#123;
                    fail(service,
                         <span class="hljs-string">"Provider "</span> + cn + <span class="hljs-string">" not found"</span>);
                &#125;
                <span class="hljs-keyword">if</span> (!service.isAssignableFrom(c)) &#123;
                    fail(service,
                         <span class="hljs-string">"Provider "</span> + cn  + <span class="hljs-string">" not a subtype"</span>);
                &#125;
                <span class="hljs-keyword">try</span> &#123;
                    S p = service.cast(c.newInstance());
                    providers.put(cn, p);
                    <span class="hljs-keyword">return</span> p;
                &#125; <span class="hljs-keyword">catch</span> (Throwable x) &#123;
                    fail(service,
                         <span class="hljs-string">"Provider "</span> + cn + <span class="hljs-string">" could not be instantiated"</span>,
                         x);
                &#125;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> Error();          <span class="hljs-comment">// This cannot happen</span>
            &#125;

            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">hasNext</span><span class="hljs-params">()</span> </span>&#123;
                <span class="hljs-keyword">if</span> (acc == <span class="hljs-keyword">null</span>) &#123;
                    <span class="hljs-keyword">return</span> hasNextService();
                &#125; <span class="hljs-keyword">else</span> &#123;
                    PrivilegedAction<Boolean> action = <span class="hljs-keyword">new</span> PrivilegedAction<Boolean>() &#123;
                        <span class="hljs-function"><span class="hljs-keyword">public</span> Boolean <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123; <span class="hljs-keyword">return</span> hasNextService(); &#125;
                    &#125;;
                    <span class="hljs-keyword">return</span> AccessController.doPrivileged(action, acc);
                &#125;
            &#125;

            <span class="hljs-function"><span class="hljs-keyword">public</span> S <span class="hljs-title">next</span><span class="hljs-params">()</span> </span>&#123;
                <span class="hljs-keyword">if</span> (acc == <span class="hljs-keyword">null</span>) &#123;
                    <span class="hljs-keyword">return</span> nextService();
                &#125; <span class="hljs-keyword">else</span> &#123;
                    PrivilegedAction<S> action = <span class="hljs-keyword">new</span> PrivilegedAction<S>() &#123;
                        <span class="hljs-function"><span class="hljs-keyword">public</span> S <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123; <span class="hljs-keyword">return</span> nextService(); &#125;
                    &#125;;
                    <span class="hljs-keyword">return</span> AccessController.doPrivileged(action, acc);
                &#125;
            &#125;
        &#125;
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，其思路就是:</p>
<ol>
<li>先获得一个classloader</li>
<li>然后去加载<code>META-INF/services/</code>下面的文件，获取相关的配置，如代码：</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java">String fullName = PREFIX + service.getName();
<span class="hljs-keyword">if</span> (loader == <span class="hljs-keyword">null</span>)
    configs = ClassLoader.getSystemResources(fullName);
<span class="hljs-keyword">else</span>
    configs = loader.getResources(fullName);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>获取对应的实现类名, 即<code>parse</code>方法</li>
<li>利用反射，根据类名去创建对应的实例， 即<code>nextService</code>方法</li>
</ol>
<h2 data-id="heading-7">Android中的应用</h2>
<p>SPI机制能够较好的解藕，便于代码的扩展，比如有这么个场景，我们需要从多个数据源获取数据，每一个数据源相关的操作都作为一个子module集成到app中，这个时候，我们可以定义一个<code>META-INF/services/xxx</code>文件，来配置数据源。</p>
<p>如果开发者自己写过类似于<code>ARouter</code>这种路由框架，肯定会了解<code>com.google.auto.service:auto-service</code>, 该组件便是简化了SPI的使用，让开发者不需要去手动维护<code>META-INF/services/xxx</code>。</p>
<p>在我们自己写一个路由框架时，会需要自己实现一个<code>AbstractProcessor</code>, 用来生成路由相关的配置。于是会定义一个类似的文件：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@AutoService(Processor.class)</span>
<span class="hljs-comment">// 允许/支持的注解类型，让注解处理器处理</span>
<span class="hljs-meta">@SupportedAnnotationTypes(&#123;Constants.ROUTER_ANNOTATION_TYPES&#125;)</span>
<span class="hljs-comment">// 指定JDK编译版本</span>
<span class="hljs-meta">@SupportedSourceVersion(SourceVersion.RELEASE_7)</span>
<span class="hljs-comment">// 注解处理器接收的参数</span>
<span class="hljs-meta">@SupportedOptions(&#123;Constants.MODULE_NAME, Constants.APT_PACKAGE&#125;)</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RouterProcessor</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbstractProcessor</span> </span>&#123;
    <span class="hljs-keyword">private</span> Elements elementsUtils;
    
    ....

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">手写注入</h3>
<p>如果我们不采用自动注入的方式，我们需要自己去维护一个<code>META-INF/services/xxx</code>文件(上面代码中的第一行就没有必要加了)，如下；</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/078beb58602044e7b1b3c9b0c6caabd4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们需要将对应Processor配置到这个文件里面，而Google的<code>com.google.auto.service:auto-service</code>组件便是简化了SPI的使用，让开发者不需要去手动维护<code>META-INF/services/xxx</code>。只需要加一个注解，由框架在编译时自动生成这个配置文件</p>
<h3 data-id="heading-9">自动注入</h3>
<p>再回到上面的第一行代码<code>@AutoService(Processor.class)</code>, 这个注解是<code>auto-service</code>这个库提供的。在编译阶段，会执行<code>AutoServiceProcessor</code>的<code>process</code>方法，在该方法中会先调用<code>generateConfigFiles</code>生成配置文件，如下：</p>
<pre><code class="hljs language-java copyable" lang="java"> <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">generateConfigFiles</span><span class="hljs-params">()</span> </span>&#123;
    Filer filer = processingEnv.getFiler();

    <span class="hljs-keyword">for</span> (String providerInterface : providers.keySet()) &#123;
      String resourceFile = <span class="hljs-string">"META-INF/services/"</span> + providerInterface;
      log(<span class="hljs-string">"Working on resource file: "</span> + resourceFile);
      <span class="hljs-keyword">try</span> &#123;
        SortedSet<String> allServices = Sets.newTreeSet();
        <span class="hljs-keyword">try</span> &#123;
       
          FileObject existingFile = filer.getResource(StandardLocation.CLASS_OUTPUT, <span class="hljs-string">""</span>,
              resourceFile);
          log(<span class="hljs-string">"Looking for existing resource file at "</span> + existingFile.toUri());
          Set<String> oldServices = ServicesFiles.readServiceFile(existingFile.openInputStream());
          log(<span class="hljs-string">"Existing service entries: "</span> + oldServices);
          allServices.addAll(oldServices);
        &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
          log(<span class="hljs-string">"Resource file did not already exist."</span>);
        &#125;

        Set<String> newServices = <span class="hljs-keyword">new</span> HashSet<String>(providers.get(providerInterface));
        <span class="hljs-keyword">if</span> (allServices.containsAll(newServices)) &#123;
          log(<span class="hljs-string">"No new service entries being added."</span>);
          <span class="hljs-keyword">return</span>;
        &#125;

        allServices.addAll(newServices);
        log(<span class="hljs-string">"New service file contents: "</span> + allServices);
        FileObject fileObject = filer.createResource(StandardLocation.CLASS_OUTPUT, <span class="hljs-string">""</span>,
            resourceFile);
        OutputStream out = fileObject.openOutputStream();
        ServicesFiles.writeServiceFile(allServices, out);
        out.close();
        log(<span class="hljs-string">"Wrote to: "</span> + fileObject.toUri());
      &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
        fatalError(<span class="hljs-string">"Unable to create "</span> + resourceFile + <span class="hljs-string">", "</span> + e);
        <span class="hljs-keyword">return</span>;
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终生成了配置文件中的类便指向了我们自定义的Processor。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d0dd6db0dfb4c0c935b41518d9ac9fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当这个模块在使用的时候，便可以通过该配置找到具体的实现类，并完成实例化。</p></div>  
</div>
            