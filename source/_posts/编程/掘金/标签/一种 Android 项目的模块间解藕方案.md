
---
title: '一种 Android 项目的模块间解藕方案'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/961a4f965e344576a5858181d32c76c9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 17:26:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/961a4f965e344576a5858181d32c76c9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在 Android 开发中，当项目增加一定规模之后，一般都会采用多模块的项目结构。当然也能采用插件化的开发模式，具体采用什么开发模式，开发者可以自行定夺。这里将介绍下我所熟悉的一种模块化开发机制。本质是基于 gradle 的 Multi-Project 构建和 Java 的动态代理机制。</p>
<p>这个方案现已提取开源：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FstefanJi%2FAndroid-MPD" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/stefanJi/Android-MPD" ref="nofollow noopener noreferrer">github.com/stefanJi/An…</a></p>
<p>// settings.gradle</p>
<pre><code class="hljs language-gradle copyable" lang="gradle"><span class="hljs-keyword">include</span> <span class="hljs-string">':app'</span>, <span class="hljs-string">':feature_a'</span>, <span class="hljs-string">':feature_b'</span>, <span class="hljs-string">':feature_c'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/961a4f965e344576a5858181d32c76c9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>利用这套机制时：比如开发者开发 A 功能时，只会涉及 feature_a 模块中代码的修改，那么开发者就可以让 gradle 不编译其他模块中的代码（在 settings.gradle 中注释不需要的模块），从而能够减少本地开发时的编译耗时，也能够让某些代码只会在开发期间存在（比如为了方便测试单独提供的 admin 模块）。</p>
<h2 data-id="heading-0">选择性编译</h2>
<p>同时为了避免因为模块间彼此依赖，导致个别模块不编译的目标无法实现。于是要求各个模块之间不能直接依赖具体实现，只能依赖某个公共模块（比如 app 模块）提供的接口。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d53ce0f6feb4820bf777bdf2a815059~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体实现是:</p>
<p>在 app 模块中定义模块 feature_a 能够提供的功能，比如打开 feature_a 中的一个 Activity.</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">IFeatureA</span> </span>&#123;
    <span class="hljs-meta">@Nullable</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Class<Activity> <span class="hljs-title">getActivityOfA</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 feature_a 中实现这个接口:</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FeatureA</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">IFeatureA</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> Class<Activity> <span class="hljs-title">getActivityOfA</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> FeatureAActivity.class;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 app 中注入 IFeatureA 接口的具体实现:</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FeatureRegister</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> IFeatureA featureA;

    <span class="hljs-meta">@Nullable</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> IFeatureA <span class="hljs-title">getFeatureA</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (featureA == <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">try</span> &#123;
                <span class="hljs-comment">// 这里使用反射能够在即使 feature_a 模块未加入编译之后也能够成功编译</span>
                featureA = (IFeatureA) Class.forName(<span class="hljs-string">"io.github.stefanji.feature_a.FeatureA"</span>).newInstance();
            &#125; <span class="hljs-keyword">catch</span> (ClassNotFoundException e) &#123;
                <span class="hljs-comment">// 如果 feature_a 未加入编译，则会触发异常</span>
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> featureA;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后 feature_b 需要获取 feature_a 的 FeatureAActivity:</p>
<pre><code class="hljs language-java copyable" lang="java">IFeatureA featureA = FeatureRegister.getFeatureA();
Class<Activity> activityClass = <span class="hljs-keyword">null</span>;
<span class="hljs-keyword">if</span> (featureA != <span class="hljs-keyword">null</span>) &#123;
    activityClass = featureA.getActivityOfA();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">动态代理未加入编译的模块</h2>
<p>在上面我们已经能够实现不编译某些模块，并且项目整体编译不会出现问题。但是每次访问其他模块提供的功能时，从 app 模块获取实现之后需要进行判空处理。不是太优雅。</p>
<p>于是可以利用动态代理，如果目标模块没有被编译，那么就返回一个实现了目标模块功能接口的代理对象。
修改 app 中代码如下:</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@NotNull</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> IFeatureA <span class="hljs-title">getFeatureA</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">if</span> (featureA == <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-keyword">try</span> &#123;
            featureA = (IFeatureA) Class.forName(<span class="hljs-string">"io.github.stefanji.feature_a.FeatureA"</span>).newInstance();
        &#125; <span class="hljs-keyword">catch</span> (ClassNotFoundException e) &#123;
        &#125;
        <span class="hljs-comment">// 如果 feature_a 模块未没编译，FeatureA 类将找不到，就动态生成一个 Proxy 类</span>
        <span class="hljs-keyword">if</span> (featureA == <span class="hljs-keyword">null</span>) &#123;
            featureA = (IFeatureA) Proxy.newProxyInstance(FeatureRegister.class.getClassLoader(),
                    <span class="hljs-keyword">new</span> Class[]&#123;IFeatureA.class&#125;,
                    <span class="hljs-keyword">new</span> InvocationHandler() &#123;
                        <span class="hljs-meta">@Override</span>
                        <span class="hljs-function"><span class="hljs-keyword">public</span> Object <span class="hljs-title">invoke</span><span class="hljs-params">(Object proxy, Method method, Object[] args)</span> <span class="hljs-keyword">throws</span> Throwable </span>&#123;
                            Class returnType = method.getReturnType();
                            <span class="hljs-comment">// 让原始类型返回零值</span>
                            <span class="hljs-keyword">if</span> (returnType == <span class="hljs-keyword">boolean</span>.class) &#123;
                                <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
                            &#125;
                            <span class="hljs-keyword">if</span> (returnType == <span class="hljs-keyword">int</span>.class) &#123;
                                <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
                            &#125;
                            <span class="hljs-keyword">if</span> (returnType == <span class="hljs-keyword">float</span>.class) &#123;
                                <span class="hljs-keyword">return</span> <span class="hljs-number">0f</span>;
                            &#125;
                            <span class="hljs-comment">//...</span>
                            <span class="hljs-comment">// 让引用类型返回 null</span>
                            <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
                        &#125;
                    &#125;);
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> featureA;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就不用做如下判空了:</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">if</span> (featureA != <span class="hljs-keyword">null</span>) &#123;
    activityClass = featureA.getActivityOfA();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">自动化</h2>
<p>每新增一个模块，我们就需要重复上面的步骤，在 FeatureRegister 中注册新的 Feature 接口。这种重复的操作，当然可以利用注解处理器或 gradle transform 之类的代码生成机制，让编译器去自动生成模板代码。</p></div>  
</div>
            