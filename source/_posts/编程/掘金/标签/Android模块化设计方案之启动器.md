
---
title: 'Android模块化设计方案之启动器'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d6e0b01d7734e7dba6b567867c2307b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 15 May 2021 01:17:41 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d6e0b01d7734e7dba6b567867c2307b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>1、<a href="https://juejin.cn/post/6945409454967881758" target="_blank">Android模块化设计方案模型图</a></p>
<p>2、<a href="https://juejin.cn/post/6945413567285821453" target="_blank">Android模块化设计方案之接口API化</a></p>
<p>3、<a href="https://juejin.cn/post/6945414175405375518" target="_blank">Android模块化设计方案之使用代理模式解耦</a></p>
<p>4、<a href="https://juejin.cn/post/6946932311216619527" target="_blank">Android模块化设计方案之sourceSets配置</a></p>
<p>5、Android模块化设计方案之启动器</p>
<p>在文章的开始，我先抛出来两个问题：</p>
<p><strong>问题一</strong> ：众所周知，随着我们App的规模越来越膨胀，在Application里面要做的初始化的业务逻辑和三方类库越来越多，直接影响就是App的冷启动速度，同时也让代码的可读性变差，如何合理的管理这些初始化任务？</p>
<p><strong>问题二</strong> ：在进行模块化开发的时候，总有一些模块要初始化一些本模块特有业务或类库，如何在修改/新增本模块初始化项的时候，尽可能的不修改其他的模块包括壳工程模块在内？</p>
<p>为了解决这两个困惑本打已久的问题，本打Google了许久也没有找到一个比较合适的方案，既然没有现成的轮子用，也只能花点时间打磨一个轮子出来了，于是基于APT技术，打造了这个轮子，它就是<strong>启动器</strong>——<strong>XStarter</strong></p>
<p><strong>那么什么是启动器？</strong></p>
<p>其实就是一个对项目中一些需要初始化的逻辑进行统一管理调度的工具类库，它可以通过简单的配置就能实现启动项的加载顺序以及是否延迟初始化或者在子线程中进行初始化，而且本身支持模块化的设计，能够最大程度做到项目解耦。那么下面我就简单介绍一下XStarter的使用方式吧。</p>
<p>项目源码地址：<a href="https://github.com/wangkunhui/XStarter" target="_blank" rel="nofollow noopener noreferrer">github.com/wangkunhui/…</a></p>
<p>第一步，引入项目依赖，starter_version = "1.0.0-rc"。</p>
<p>在Java模块中：</p>
<pre><code class="hljs language-groovy copyable" lang="groovy">android &#123;
  defaultConfig&#123;
    javaCompileOptions &#123;
      annotationProcessorOptions &#123;
         arguments = [<span class="hljs-attr">STARTER_MODULE_NAME:</span> project.getName()]
      &#125;
    &#125;
  &#125;
&#125;

dependencies &#123;
    implementation <span class="hljs-string">"com.wangkh.moduler:XStarter:$starter_version"</span>
    annotationProcessor <span class="hljs-string">"com.wangkh.moduler:XStarter-compiler:$starter_version"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在Kotlin模块中：</p>
<pre><code class="hljs language-groovy copyable" lang="groovy">apply <span class="hljs-attr">plugin:</span> <span class="hljs-string">'kotlin-kapt'</span>
kapt &#123;
    arguments &#123;
        arg(<span class="hljs-string">"STARTER_MODULE_NAME"</span>, project.getName())
    &#125;
&#125;

dependencies &#123;
    implementation <span class="hljs-string">"com.wangkh.moduler:XStarter:$starter_version"</span>
    kapt <span class="hljs-string">"com.wangkh.moduler:XStarter-compiler:$starter_version"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步，在Application中进行注册。</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">XStarter.isDebug = <span class="hljs-literal">true</span> <span class="hljs-comment">// 是否为测试模式</span>
XStarter.emit(DemoApplication.instance) <span class="hljs-comment">// 开启启动器</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三部，在需要初始化数据的模块中创建启动器类。</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-meta">@Starter(mainProcessOnly = false)</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">KotlinStarter</span> : <span class="hljs-type">IStarter &#123; // 类名可以任意命名</span></span>
    <span class="hljs-meta">@StarterMethod(priority = 99, isSync = false, isDelay = true)</span>
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">initTest</span><span class="hljs-params">(application:<span class="hljs-type">Application</span>)</span></span> &#123; <span class="hljs-comment">//方法名可以任意命名</span>
        <span class="hljs-comment">//TODO 执行模块中需要初始化的逻辑</span>
    &#125;

    <span class="hljs-meta">@StarterFinish(listen = <span class="hljs-meta-string">"initTest"</span>)</span>
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">listenTest</span><span class="hljs-params">(e:<span class="hljs-type">Exception</span>)</span></span> &#123; <span class="hljs-comment">// 监听initTest方法是否执行完毕，如果不需要监听，可以不写listenTest方法</span>
        Log.e(<span class="hljs-string">"KotlinStarter"</span>, <span class="hljs-string">"test初始化完成"</span>)
    &#125;
  
    <span class="hljs-meta">@StarterMethod(priority = 60, isSync = true, isDelay = true)</span>
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">initTest2</span><span class="hljs-params">()</span></span> &#123; <span class="hljs-comment">//方法名可以任意命名</span>
<span class="hljs-comment">//TODO 初始化另外一些东西，由于这个方法下初始化不需要用到Application，所以参数为空就行。</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只需要通过以上代码，项目在启动的时候就会自动的寻找<strong>KotlinStarter</strong>类并调用生命的初始化方法<strong>initTest</strong>，如果需要监听<strong>initTest</strong>是否已经执行完毕，可以定义一个监听方法<strong>listenTest</strong>（方法名可以任意命名），但是其注解@StarterFinish的参数listen中的字符串一定要与被监听的方法名保持一致即可。</p>
<p><strong>注解及参数说明</strong></p>
<pre><code class="hljs language-html copyable" lang="html">@Starter // 标注启动管理类

    mainProcessOnly -- 是否只在主进程初始化 true 只在主进程中初始化 false 所有进程都进行初始化

@StarterMethod  //标注启动方法，只能用到@Starter修饰的类中，否则无效。

    priority -- 该启动方法的优先级，[0-99],数值越大优先级越高，默认50；
    
    isSync -- 是否同步初始化（即在主线程中进行初始化操作），true 是 false 不是，即可以在子线程中进行初始化，默认true；

    isDelay -- 是否可以延迟初始化，true 是 false 不是，立即初始化，不延迟，默认false；

@StarterFinish //启动方法的监听方法，只能用到@Starter修饰的类中，否则无效。

    listen -- 要监听方法的方法名，必填参数；

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>混淆配置</strong></p>
<pre><code class="copyable">-keep public class com.wang.android.starter.executor.**&#123;*;&#125;
-keep public class com.wang.android.starter.manager.**&#123;*;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，我们在梳理一下文章最开始时候留下的两个问题。</p>
<p>问题一：原本那些需要在Application类中进行初始化的类库被解耦到各个业务模块里面，剥离了Application中的业务代码，并且提供了统一的方式进行处理。只需要通过简单的注解配置，就能指定该类库的初始化优先级、初始化线程和是否可以延迟初始化，不需要做额外的改动。</p>
<p>问题二：由于Application中的业务代码被彻底剥离，在我们需要对模块的启动类库进行修改或新增模块的时候，只需要去对应Module的启动器类中修改就可以了，无需更改壳工程中的代码。</p>
<p>实现思路是通过APT技术在编译时生成对启动器类的代理类和管理类，通过管理类对所有启动器中的方法进行统一调度。</p>
<p>好了，关于启动器的部分就介绍完毕了，如果该文章能够帮到你，欢迎<strong>点赞评论</strong>和<strong>关注</strong>，一起交流探讨~</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d6e0b01d7734e7dba6b567867c2307b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            