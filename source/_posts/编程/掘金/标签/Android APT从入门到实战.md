
---
title: 'Android APT从入门到实战'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4b637a8cdf34634b72a1c46a6cf6bff~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 00:54:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4b637a8cdf34634b72a1c46a6cf6bff~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li>
<h2 data-id="heading-0">APT是什么?有什么用?</h2>
</li>
</ul>
<p><strong>APT</strong>(Annotation Processing Tool)即<strong>注解处理器</strong>，在编译的时候可以处理注解然后搞一些事情，也可以在编译时生成一些文件之类的。<code>ButterKnife和EventBus都使用了APT技术，如果不会APT技术就很难看懂这两个框架的源码。</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4b637a8cdf34634b72a1c46a6cf6bff~tplv-k3u1fbpfcp-watermark.image" alt="tempImage1629265217303.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h2 data-id="heading-1">实现效果</h2>
</li>
</ul>
<p>我们来实现一个简单的功能，只要在任何类的成员变量上添加一个 <code>@Print</code>注解，就可以动态生成一个方法，然后把成员变量的变量名输出：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f28ab10589ec4d7b97045e16524d4ec0~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>动态生成的类大概长这样:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a75751a20d0495ba9ec0ec0f22102de~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h2 data-id="heading-2">整理思路</h2>
</li>
</ul>
<ol>
<li>首先我们需要创建两个JavaLibrary</li>
<li>一个用来定义注解，一个用来扫描注解</li>
<li>获取到添加注解的成员变量名</li>
<li>动态生成类和方法用IO生成文件</li>
</ol>
<ul>
<li>
<h2 data-id="heading-3">实战</h2>
</li>
<li>
<h3 data-id="heading-4"><code>创建一个空项目</code></h3>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4a5f19a7c07498187add9c2565d6fa5~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-5"><code>创建两个JavaLibrary</code></h3>
</li>
</ul>
<ol>
<li>注解的Lib: <strong><code>apt-annotation</code></strong></li>
<li>扫描注解的Lib: <strong><code>apt-processor</code></strong></li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86531d5308294ba38167c24d456d2155~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d29f1a977ff43a0b82dc3c21dc1b166~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-6"><code>创建完之后</code></h3>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c589d44d4fb4972a92efa7ff45f0cf5~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-7"><code>app模块依赖两个Library</code></h3>
</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">implementation <span class="hljs-title">project</span><span class="hljs-params">(path: <span class="hljs-string">':apt-annotation'</span>)</span>
annotationProcessor <span class="hljs-title">project</span><span class="hljs-params">(path: <span class="hljs-string">':apt-processor'</span>)</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8eeae94773304b5db8269a921377f9db~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-8"><code>注解Lib中创建一个注解类</code></h3>
</li>
</ul>
<p>如果还不会自定义注解的同学，可以先去看我之前写的一篇<a href="https://juejin.cn/post/6982471491568812040" target="_blank" title="https://juejin.cn/post/6982471491568812040">Java自定义注解入门到实战</a></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Retention(RetentionPolicy.CLASS)</span>
<span class="hljs-meta">@Target(ElementType.FIELD)</span>
<span class="hljs-keyword">public</span> <span class="hljs-meta">@interface</span> Print &#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7956871e21454e38aa78a7f58954a0c1~tplv-k3u1fbpfcp-watermark.image" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-9"><code>扫描注解的Lib添加依赖</code></h3>
</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">dependencies &#123;
    <span class="hljs-comment">//自动注册，动态生成 META-INF/...文件</span>
    implementation <span class="hljs-string">'com.google.auto.service:auto-service:1.0-rc6'</span>
    annotationProcessor <span class="hljs-string">'com.google.auto.service:auto-service:1.0-rc6'</span>
    <span class="hljs-comment">//依赖apt-annotation</span>
    <span class="hljs-function">implementation <span class="hljs-title">project</span><span class="hljs-params">(path: <span class="hljs-string">':apt-annotation'</span>)</span>
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71f96b31e9034c8295623a64555bca64~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-10"><code>创建扫描注解的类</code></h3>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5018b691d52f4d51a9cea36296ff9ae9~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-11"><code>重写init方法，输出Hello,APT</code></h3>
</li>
</ul>
<p>注意: 这里是JavaLib，所以不能使用Log打印，这里可以使用Java的println()或注解处理器给我们提供的方法，建议使用注解处理器给我们提供的</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/457a2866c3614eeba000b41c2058e0c0~tplv-k3u1fbpfcp-watermark.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-12"><code>见证奇迹</code></h3>
</li>
</ul>
<p>现在我们已经完成了APT的基本配置，现在我们可以build一下项目了，成败在此一举</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/577ed3798b434d698e880558aed64c5a~tplv-k3u1fbpfcp-watermark.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-13"><code>踩坑指南</code></h3>
</li>
</ul>
<ol>
<li>如果你已经成功输出了文本，说明APT已经配置好，可以继续下一步了</li>
<li><strong><code>如果你失败了：</code></strong></li>
</ol>
<blockquote>
<ol>
<li>如果继承的时候找不到AbstractProcessor类，那你 <strong><code>创建的肯定不是JavaLibrary，你可以删掉重新创建</code></strong></li>
<li>如果点击编译没反应，你可以试试先 <strong><code>clear一下项目再重新编译</code></strong></li>
<li>如果都不行，就去检查一下前面流程的 <strong><code>依赖是否都配置正确</code></strong></li>
</ol>
</blockquote>
<ul>
<li>
<h3 data-id="heading-14"><code>继续完成功能</code></h3>
</li>
</ul>
<p>现在我们可以继续完成上面要实现的功能了，我们需要先来实现几个方法</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 要扫描扫描的注解，可以添加多个
 */</span>
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> Set<String> <span class="hljs-title">getSupportedAnnotationTypes</span><span class="hljs-params">()</span> </span>&#123;
    HashSet<String> hashSet = <span class="hljs-keyword">new</span> HashSet<>();
    hashSet.add(Print.class.getCanonicalName());
    <span class="hljs-keyword">return</span> hashSet;
&#125;

<span class="hljs-comment">/**
 * 编译版本，固定写法就可以
 */</span>
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> SourceVersion <span class="hljs-title">getSupportedSourceVersion</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">return</span> processingEnv.getSourceVersion();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73a8849007c84d29b47e183075b89aab~tplv-k3u1fbpfcp-watermark.image" alt="15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-15"><code>定义注解</code></h3>
</li>
</ul>
<p>我们先在MianActivity中添加两个成员变量并使用我们定义的注解</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf465597b8eb4cd78ee83d766d2ed305~tplv-k3u1fbpfcp-watermark.image" alt="17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-16"><code>定义注解</code></h3>
</li>
</ul>
<p>真正解析注解的地方是在<code>process</code>方法，我们先试试能不能拿到被注解的变量名</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 扫描注解回调
 */</span>
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">process</span><span class="hljs-params">(Set<? extends TypeElement> annotations, RoundEnvironment roundEnv)</span> </span>&#123;
    <span class="hljs-comment">//拿到所有添加Print注解的成员变量</span>
    Set<? extends Element> elements = roundEnv.getElementsAnnotatedWith(Print.class);
    <span class="hljs-keyword">for</span> (Element element : elements) &#123;
        <span class="hljs-comment">//拿到成员变量名</span>
        Name simpleName = element.getSimpleName();
        <span class="hljs-comment">//输出成员变量名</span>
        processingEnv.getMessager().printMessage(Diagnostic.Kind.NOTE,simpleName);
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2affe238b9a349bfaa456060765da96b~tplv-k3u1fbpfcp-watermark.image" alt="18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-17"><code>编译试一下</code></h3>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a16fcf4484349179190061714ff0b55~tplv-k3u1fbpfcp-watermark.image" alt="19.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-18"><code>生成类</code></h3>
</li>
</ul>
<p>既然能拿到被注解的变量名，后面就简单了，我们只需要用字符串拼出来一个工具类，然后用IO流写到本地就ok了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a201abb806a47a7867aeead4b7d91d9~tplv-k3u1fbpfcp-watermark.image" alt="20.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-19"><code>查看效果</code></h3>
</li>
</ul>
<p>现在点击一下编译，然后我们可以看到app模块下的build文件已经有我们生成的类了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b1adabd5b6844cc80b60216bbc18db7~tplv-k3u1fbpfcp-watermark.image" alt="21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-20"><code>调用方法</code></h3>
</li>
</ul>
<p>现在我们回到<code>MainActivity</code>，就可以直接调用这个动态生成的类了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/492f37ade090492290ab2215bd18f667~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aedf526b84884172beb85cfd82783bca~tplv-k3u1fbpfcp-watermark.image" alt="tempImage1629273861493.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h2 data-id="heading-21">实战结束</h2>
</li>
</ul>
<p>结束了吗...好像是结束了，但是上面拼接类的方法感觉一不小心就会写错，有没有更好的方法呢，我们先来看看<code>EventBus的源码</code>是怎么生成的:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74ae972f2fb1489fbe2d599479653375~tplv-k3u1fbpfcp-watermark.image" alt="23.png" loading="lazy" referrerpolicy="no-referrer">
看到大佬也是这样拼接的，这我就放心了🤡，我们再看一下<code>ButterKnife的源码</code>是怎么生成的:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6b0a8faa7b34c78ab7ff090963d19ec~tplv-k3u1fbpfcp-watermark.image" alt="24.png" loading="lazy" referrerpolicy="no-referrer">
<code>ButterKnife的源码</code>竟然不是用字符串拼接的!!! 隐约看到<code>TypeSpec.classBuilder</code>，这是啥玩意？不过身为资深的程序猿这点问题我们还是可以很容易的找到答案的</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58f216ca1ff74897a3976de9feff62d4~tplv-k3u1fbpfcp-watermark.image" alt="25.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-22"><code>JavaPoet</code></h3>
</li>
</ul>
<p>经过一个小时的百度，大概研究了一下JavaPoet，这玩意好像可以帮我们<code>以面向对象的思维来生成类</code>，这样我们就不用手动拼接字符串的方式来生成类了，那我们来优化一下上面的代码:</p>
<pre><code class="copyable">先添加依赖
implementation 'com.squareup:javapoet:1.13.0'
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03d726eb7c40441983f16ed5ba4f09cf~tplv-k3u1fbpfcp-watermark.image" alt="29.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 扫描注解回调
 */</span>
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">process</span><span class="hljs-params">(Set<? extends TypeElement> annotations, RoundEnvironment roundEnv)</span> </span>&#123;
    <span class="hljs-comment">//拿到所有添加Print注解的成员变量</span>
    Set<? extends Element> elements = roundEnv.getElementsAnnotatedWith(Print.class);

    <span class="hljs-comment">//生成类</span>
    TypeSpec.Builder classBuilder = TypeSpec
            .classBuilder(<span class="hljs-string">"PrintUtil"</span>)
            .addModifiers(Modifier.PUBLIC, Modifier.FINAL);

    <span class="hljs-keyword">for</span> (Element element : elements) &#123;
        <span class="hljs-comment">//拿到成员变量名</span>
        Name simpleName = element.getSimpleName();
        <span class="hljs-comment">//生成方法</span>
        MethodSpec method = MethodSpec.methodBuilder(<span class="hljs-string">"print$$"</span>+simpleName)
                .addModifiers(Modifier.PUBLIC, Modifier.STATIC)
                .returns(<span class="hljs-keyword">void</span>.class)
                .addStatement(<span class="hljs-string">"$T.out.println($S)"</span>, System.class, <span class="hljs-string">"Hello, JavaPoet!"</span>)
                .build();
        classBuilder.addMethod(method);
    &#125;
    <span class="hljs-comment">//包</span>
    JavaFile javaFile = JavaFile
            .builder(<span class="hljs-string">"com.lkx.helloapt"</span>, classBuilder.build())
            .build();
    <span class="hljs-keyword">try</span> &#123;
        javaFile.writeTo(processingEnv.getFiler());
    &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
        e.printStackTrace();
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a93393dd01684e6db8c4ce1f0e667712~tplv-k3u1fbpfcp-watermark.image" alt="27.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h3 data-id="heading-23"><code>编译一下</code></h3>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0eb07800bfa84493850d87595ed5640f~tplv-k3u1fbpfcp-watermark.image" alt="28.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8032a038c8474c6e9efa3c54ca9e35cc~tplv-k3u1fbpfcp-watermark.image" alt="tempImage1629276608514.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h2 data-id="heading-24">总结</h2>
</li>
</ul>
<ol>
<li>APT可以在编译器扫描注解帮我们提前生成类</li>
<li>JavaPoet可以帮我们优雅的生成类，再也不用拼接了</li>
<li>APT最主要的功能就是可以替代反射的一些功能，避免降低性能</li>
<li>APT只会在编译时影响一点点速度，在运行期不会，而反射刚好相反</li>
</ol></div>  
</div>
            