
---
title: '再谈双亲委派模型与Flink的类加载策略'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/195230-6c59d7b82fa30225.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/195230-6c59d7b82fa30225.png'
---

<div>   
<h3>类加载</h3>
<p>简书被请去喝了三天茶，笔者也度过了炒鸡忙乱的三天。今天事情终于少一点了，专栏再开，写篇基础的热热身吧。</p>
<p>我们知道，在JVM中，一个类加载的过程大致分为加载、链接（验证、准备、解析）、初始化5个阶段。而我们通常提到类的加载，就是指利用类加载器（ClassLoader）通过类的全限定名来获取定义此类的二进制字节码流，进而构造出类的定义。Flink作为基于JVM的框架，在flink-conf.yaml中提供了控制类加载策略的参数<code>classloader.resolve-order</code>，可选项有<code>child-first</code>（默认）和<code>parent-first</code>。本文来简单分析一下这个参数背后的含义。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="802" data-height="758"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-6c59d7b82fa30225.png" data-original-width="802" data-original-height="758" data-original-format="image/png" data-original-filesize="46517" src="https://upload-images.jianshu.io/upload_images/195230-6c59d7b82fa30225.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>parent-first类加载策略</h3>
<p>ParentFirstClassLoader和ChildFirstClassLoader类的父类均为FlinkUserCodeClassLoader抽象类，先来看看这个抽象类，代码很短。</p>
<pre><code class="java">public abstract class FlinkUserCodeClassLoader extends URLClassLoader &#123;
    public static final Consumer<Throwable> NOOP_EXCEPTION_HANDLER = classLoadingException -> &#123;&#125;;

    private final Consumer<Throwable> classLoadingExceptionHandler;

    protected FlinkUserCodeClassLoader(URL[] urls, ClassLoader parent) &#123;
        this(urls, parent, NOOP_EXCEPTION_HANDLER);
    &#125;

    protected FlinkUserCodeClassLoader(
            URL[] urls,
            ClassLoader parent,
            Consumer<Throwable> classLoadingExceptionHandler) &#123;
        super(urls, parent);
        this.classLoadingExceptionHandler = classLoadingExceptionHandler;
    &#125;

    @Override
    protected final Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException &#123;
        try &#123;
            return loadClassWithoutExceptionHandling(name, resolve);
        &#125; catch (Throwable classLoadingException) &#123;
            classLoadingExceptionHandler.accept(classLoadingException);
            throw classLoadingException;
        &#125;
    &#125;

    protected Class<?> loadClassWithoutExceptionHandling(String name, boolean resolve) throws ClassNotFoundException &#123;
        return super.loadClass(name, resolve);
    &#125;
&#125;
</code></pre>
<p>FlinkUserCodeClassLoader继承自URLClassLoader。因为Flink App的用户代码在运行期才能确定，所以通过URL在JAR包内寻找全限定名对应的类是比较合适的。而ParentFirstClassLoader仅仅是一个继承FlinkUserCodeClassLoader的空类而已。</p>
<pre><code class="java">static class ParentFirstClassLoader extends FlinkUserCodeClassLoader &#123;
    ParentFirstClassLoader(URL[] urls, ClassLoader parent, Consumer<Throwable> classLoadingExceptionHandler) &#123;
        super(urls, parent, classLoadingExceptionHandler);
    &#125;
&#125;
</code></pre>
<p>这样就相当于ParentFirstClassLoader直接调用了父加载器的loadClass()方法。<a href="https://www.jianshu.com/p/67021213872a" target="_blank">之前已经讲过</a>，JVM中类加载器的层次关系和默认loadClass()方法的逻辑由双亲委派模型（parents delegation model）来体现，复习一下含义：</p>
<blockquote>
<p>如果一个类加载器要加载一个类，它首先不会自己尝试加载这个类，而是把加载的请求委托给父加载器完成，所有的类加载请求最终都应该传递给最顶层的启动类加载器。只有当父加载器无法加载到这个类时，子加载器才会尝试自己加载。</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="652" data-height="602"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-22a3ec7d98ab9b27.png" data-original-width="652" data-original-height="602" data-original-format="image/png" data-original-filesize="94732" src="https://upload-images.jianshu.io/upload_images/195230-22a3ec7d98ab9b27.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>可见，Flink的parent-first类加载策略就是照搬双亲委派模型的。也就是说，用户代码的类加载器是Custom ClassLoader，Flink框架本身的类加载器是Application ClassLoader。用户代码中的类先由Flink框架的类加载器加载，再由用户代码的类加载器加载。但是，Flink默认并不采用parent-first策略，而是采用下面的child-first策略，继续看。</p>
<h3>child-first类加载策略</h3>
<p>我们已经了解到，双亲委派模型的好处就是随着类加载器的层次关系保证了被加载类的层次关系，从而保证了Java运行环境的安全性。但是在Flink App这种依赖纷繁复杂的环境中，双亲委派模型可能并不适用。例如，程序中引入的Flink-Cassandra Connector总是依赖于固定的Cassandra版本，用户代码中为了兼容实际使用的Cassandra版本，会引入一个更低或更高的依赖。而同一个组件不同版本的类定义有可能会不同（即使类的全限定名是相同的），如果仍然用双亲委派模型，就会因为Flink框架指定版本的类先加载，而出现莫名其妙的兼容性问题，如NoSuchMethodError、IllegalAccessError等。</p>
<p>鉴于此，Flink实现了ChildFirstClassLoader类加载器并作为默认策略。它打破了双亲委派模型，使得用户代码的类先加载，官方文档中将这个操作称为"Inverted Class Loading"。代码仍然不长，录如下。</p>
<pre><code class="java">public final class ChildFirstClassLoader extends FlinkUserCodeClassLoader &#123;
    private final String[] alwaysParentFirstPatterns;

    public ChildFirstClassLoader(
            URL[] urls,
            ClassLoader parent,
            String[] alwaysParentFirstPatterns,
            Consumer<Throwable> classLoadingExceptionHandler) &#123;
        super(urls, parent, classLoadingExceptionHandler);
        this.alwaysParentFirstPatterns = alwaysParentFirstPatterns;
    &#125;

    @Override
    protected synchronized Class<?> loadClassWithoutExceptionHandling(
            String name,
            boolean resolve) throws ClassNotFoundException &#123;
        // First, check if the class has already been loaded
        Class<?> c = findLoadedClass(name);

        if (c == null) &#123;
            // check whether the class should go parent-first
            for (String alwaysParentFirstPattern : alwaysParentFirstPatterns) &#123;
                if (name.startsWith(alwaysParentFirstPattern)) &#123;
                    return super.loadClassWithoutExceptionHandling(name, resolve);
                &#125;
            &#125;

            try &#123;
                // check the URLs
                c = findClass(name);
            &#125; catch (ClassNotFoundException e) &#123;
                // let URLClassLoader do it, which will eventually call the parent
                c = super.loadClassWithoutExceptionHandling(name, resolve);
            &#125;
        &#125;

        if (resolve) &#123;
            resolveClass(c);
        &#125;
        return c;
    &#125;

    @Override
    public URL getResource(String name) &#123;
        // first, try and find it via the URLClassloader
        URL urlClassLoaderResource = findResource(name);
        if (urlClassLoaderResource != null) &#123;
            return urlClassLoaderResource;
        &#125;
        // delegate to super
        return super.getResource(name);
    &#125;

    @Override
    public Enumeration<URL> getResources(String name) throws IOException &#123;
        // first get resources from URLClassloader
        Enumeration<URL> urlClassLoaderResources = findResources(name);
        final List<URL> result = new ArrayList<>();

        while (urlClassLoaderResources.hasMoreElements()) &#123;
            result.add(urlClassLoaderResources.nextElement());
        &#125;

        // get parent urls
        Enumeration<URL> parentResources = getParent().getResources(name);
        while (parentResources.hasMoreElements()) &#123;
            result.add(parentResources.nextElement());
        &#125;

        return new Enumeration<URL>() &#123;
            Iterator<URL> iter = result.iterator();

            public boolean hasMoreElements() &#123;
                return iter.hasNext();
            &#125;

            public URL nextElement() &#123;
                return iter.next();
            &#125;
        &#125;;
    &#125;
&#125;
</code></pre>
<p>核心逻辑位于loadClassWithoutExceptionHandling()方法中，简述如下：</p>
<ol>
<li>调用findLoadedClass()方法检查全限定名name对应的类是否已经加载过，若没有加载过，再继续往下执行。</li>
<li>检查要加载的类是否以alwaysParentFirstPatterns集合中的前缀开头。如果是，则调用父类的对应方法，以parent-first的方式来加载它。</li>
<li>如果类不符合alwaysParentFirstPatterns集合的条件，就调用findClass()方法在用户代码中查找并获取该类的定义（该方法在URLClassLoader中有默认实现）。如果找不到，再fallback到父加载器来加载。</li>
<li>最后，若resolve参数为true，就调用resolveClass()方法链接该类，最后返回对应的Class对象。</li>
</ol>
<p>可见，child-first策略避开了“先把加载的请求委托给父加载器完成”这一步骤，只有特定的某些类一定要“遵循旧制”。alwaysParentFirstPatterns集合中的这些类都是Java、Flink等组件的基础，不能被用户代码冲掉。它由以下两个参数来指定：</p>
<ul>
<li>
<code>classloader.parent-first-patterns.default</code>，不建议修改，固定为以下这些值：</li>
</ul>
<pre><code>java.;
scala.;
org.apache.flink.;
com.esotericsoftware.kryo;
org.apache.hadoop.;
javax.annotation.;
org.slf4j;
org.apache.log4j;
org.apache.logging;
org.apache.commons.logging;
ch.qos.logback;
org.xml;
javax.xml;
org.apache.xerces;
org.w3c
</code></pre>
<ul>
<li>
<code>classloader.parent-first-patterns.additional</code>：除了上一个参数指定的类之外，用户如果有其他类以child-first模式会发生冲突，而希望以双亲委派模型来加载的话，可以额外指定（分号分隔）。</li>
</ul>
<h3>The End</h3>
<p>今天下午大雨，晚高峰一片混乱，费了九牛二虎之力才回到家（虽然只有4公里路），还是早点洗洗睡吧。</p>
<p>民那晚安晚安。</p>
  
</div>
            