
---
title: '依赖注入（五）—— Dagger的Lazy与Provider'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=938'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 05:25:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=938'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Lazy</h1>
<p>在Dagger中Lazy可以将要注入的依赖项转变为懒加载模式，这样注入的依赖项，只有在需要使用时，才会调用对应的依赖生成方法。懒加载的实现很简单，只需要在注入位置将依赖项的类型设置为<code>Lazy</code>接口的类型参数即可。</p>
<pre><code class="hljs language-Kotlin copyable" lang="Kotlin"><span class="hljs-meta">@Inject</span>
<span class="hljs-meta">@GsonType(value = <span class="hljs-string">"normal"</span>)</span>
<span class="hljs-keyword">lateinit</span> <span class="hljs-keyword">var</span> gson: Lazy<Gson>

gson.<span class="hljs-keyword">get</span>() <span class="hljs-comment">// 调用get获取依赖项实例，第一次调用时才会执行依赖生成方法</span>
gson.<span class="hljs-keyword">get</span>() <span class="hljs-comment">// 后续再调用，获取的是同一个实例</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>💡 在kotlin中使用Dagger时需要注意Lazy接口是<code>dagger.Lazy</code>，而不是<code>kotlin.Lazy</code>。</p>
</blockquote>
<h3 data-id="heading-1">实现原理</h3>
<p>Dagger实现懒加载模式的原理是在执行依赖注入时，将对应的对象工厂对象使用<code>DoubleCheck.lazy</code>方法包装一下，返回一个<code>DoubleCheck</code>代理实例，而通过查看源码可知，<code>DoubleCheck</code>实现了<code>Lazy</code>接口。</p>
<pre><code class="hljs language-Java copyable" lang="Java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">MainActivity_MembersInjector</span> <span class="hljs-keyword">implements</span> <span class="hljs-title class_">MembersInjector</span><MainActivity> &#123;
  <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Provider<Gson> gsonProvider;

  <span class="hljs-meta">@Override</span>
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">injectMembers</span><span class="hljs-params">(MainActivity instance)</span> &#123;
    injectGson(instance, DoubleCheck.lazy(gsonProvider));
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">Provider</h1>
<p>Provider是<code>javax.inject</code>包中提供的一个接口，Dagger对此接口也提供了支持，使用该接口可以直接依赖项的Provider对象，从而实现每次使用时都调用依赖提供方法获取新的对象的效果。Provider的使用和Lazy一样，也是只需要在注入位置将依赖项的类型设置为<code>Provider</code>接口的类型参数即可。</p>
<pre><code class="hljs language-Kotlin copyable" lang="Kotlin"><span class="hljs-meta">@Inject</span>
<span class="hljs-meta">@GsonType(value = <span class="hljs-string">"normal"</span>)</span>
<span class="hljs-keyword">lateinit</span> <span class="hljs-keyword">var</span> gson: Provider<Gson>

gson.<span class="hljs-keyword">get</span>() <span class="hljs-comment">// 每次调用都会执行依赖生成方法，</span>
gson.<span class="hljs-keyword">get</span>() <span class="hljs-comment">// 获取新的对象。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">实现原理</h3>
<p>我们知道，Dagger会在编译时为所有的依赖项生成对应的工厂类，并且在获取依赖项实例时，也是通过这个工厂类的实例来获取的。</p>
<pre><code class="hljs language-Java copyable" lang="Java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">CommonModule_ProvideGsonFactory</span> <span class="hljs-keyword">implements</span> <span class="hljs-title class_">Factory</span><Gson> &#123;
  <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> CommonModule <span class="hljs-keyword">module</span>;
  <span class="hljs-keyword">public</span> <span class="hljs-title function_">CommonModule_ProvideGsonFactory</span><span class="hljs-params">(CommonModule <span class="hljs-keyword">module</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.<span class="hljs-keyword">module</span> = <span class="hljs-keyword">module</span>;
  &#125;
  <span class="hljs-meta">@Override</span>
  <span class="hljs-keyword">public</span> Gson <span class="hljs-title function_">get</span><span class="hljs-params">()</span> &#123;
    <span class="hljs-keyword">return</span> provideGson(<span class="hljs-keyword">module</span>);
  &#125;
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Student <span class="hljs-title function_">provideGson</span><span class="hljs-params">(CommonModule instance)</span> &#123;
    <span class="hljs-keyword">return</span> Preconditions.checkNotNullFromProvides(instance.provideGson());
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>工厂类实现自<code>Factory</code>接口，而<code>Factory</code>接口则继承了<code>Provider</code>接口：</p>
<pre><code class="hljs language-Java copyable" lang="Java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">interface</span> <span class="hljs-title class_">Factory</span><T> <span class="hljs-keyword">extends</span> <span class="hljs-title class_">Provider</span><T> &#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当Dagger检测到要注入的依赖项是<code>Provider</code>接口的参数化实例时，就会直接注入该依赖项的工厂类实例，因此，当我们调用注入对象的<code>get</code>方法时，实际就是通过工厂实例间接调用了<code>inject- constructor</code>或<code>provides-method</code>。</p>
<pre><code class="hljs language-Java copyable" lang="Java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">MainActivity_MembersInjector</span> <span class="hljs-keyword">implements</span> <span class="hljs-title class_">MembersInjector</span><MainActivity> &#123;
  <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Provider<Gson> gsonProvider;

  <span class="hljs-meta">@Override</span>
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">injectMembers</span><span class="hljs-params">(MainActivity instance)</span> &#123;
    injectGson(instance, gsonProvider);
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            