
---
title: 'Android 组件化思考与总结'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bd567fa6dee4709b4b857d244744c36~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 18:02:55 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bd567fa6dee4709b4b857d244744c36~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>updata time  2020年10月09日14:03:57</p>
</blockquote>
<p><a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">CSDN</a></p>
<p><a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">参考文章-ARouter原理</a></p>
<h2 data-id="heading-0">前言</h2>
<p>   在平时的开发过程中，中小项目MVC 、MVP 已经够用。但在大公司中，由于过多的业务逻辑，数个开发人员合作开发。复用问题、不方便、编译时长，方便测试等问题的出现，也就决定了Android 架构的演变方向，最近时间充裕，该片文章为本人从零搭建组件化的一些思考记录及总结，有不对的地方还望多包涵。</p>
<h2 data-id="heading-1">一、 什么是组件化</h2>
<p>   项目按功能拆分成功若干个组件，每个组件负责相应的功能，每个组件都可以以一个单独的 module 开发，并且可以单独抽出来作为 SDK 对外发布使用，比如登录组件，视频组件。组件化与模块化其实很相似，但不同的是模块化是以业务为导向，组件化是以功能为导向。一般一个模块可以包含多个组件。</p>
<p>   自己对项目架构进行一个图形化</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bd567fa6dee4709b4b857d244744c36~tplv-k3u1fbpfcp-watermark.image" alt="1.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>BaseLib ：各种基础工具类，比如：Log工具类，Activity 入栈出栈， 等基础工具类为基础Lib，可以供所有Lib依赖</p>
</li>
<li>
<p>Lib : 基础功能Sdk底层封装。比如：网络Sdk ，图片加载，数据库等功能都封装为单独的Lib。</p>
</li>
<li>
<p>基础业务层 ：module可封装工具类 如： BaseActivity BaseFragment 等</p>
</li>
<li>
<p>业务层 ： 每个模块代表了一个业务，模块之间相互隔离解耦，方便维护和复用。（类似模块化）</p>
</li>
<li>
<p>宿主层 :  App外壳，不参与业务功能实现，主要承担App生成和 初始化功能。</p>
</li>
</ul>
<blockquote>
<p>上述架构为本人项目，读者可以根据业务情况自行拆分，baseLib和Lib其实也可以合并为一个整体</p>
</blockquote>
<h2 data-id="heading-2">二、 组件化完善与优化</h2>
<p>   相比于单个App Module ,多个Module 多个Lib 要实现业务逻辑，还存在一些问题：
1 .  组件间界面跳转，不同组件之间不仅会有数据的传递，也会有相互的页面跳转。（<a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">ARouter</a>）
2 . 数据传递与组件间方法 如何相互调用。
3 . 如何获取组件中 Fragment 的实例并将组件中的 Fragment 实例添加到主项目的界面中？
4 . 单个模块如何独立运行和组件式运行 切换问题。
5 . 多个content provider 初始话插件方式的优化 （<a href="https://juejin.im/post/6844904190440013837#heading-3" target="_blank" title="https://juejin.im/post/6844904190440013837#heading-3">StartUp</a>)
6. module单独运行 和合并运行管理。</p>
<h2 data-id="heading-3">三、组件化问题解决</h2>
<h3 data-id="heading-4">1 . 界面跳转</h3>
<p>   Activity跳转分为 显示跳转和隐式跳转，但是显示跳转存在Activity之间的双向依赖，不符合组件化的架构思想定位，我们这里使用 隐式跳转，但是手搓Schame，清单文件会非常混乱，这里我们使用 alibaba 的开源库 ARouter。</p>
<blockquote>
<p>原理:代码里加入的@Route注解，在编译时期通过apt生成存储path和activityClass映射关系的类文件，app进程启动的时候拿到这些类文件，把保存这些映射关系的数据读到map中，进行路由跳转的时候，通过build()方法传入要到达页面的路由地址，ARouter会通过它自己存储的路由表找到路由地址对应的Activity.class(activity.class = map.get(path))，然后new Intent()，当调用ARouter的withString()方法它的内部会调用intent.putExtra(String name, String value)，调用navigation()方法，它的内部会调用startActivity(intent)进行跳转，这样便可以实现相互没有依赖的module顺利的启动对方的Activity了。</p>
</blockquote>
<p>代码示例：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-comment">// 路由 gradle引入（kotlin 和 java引入方式区分）</span>
    api libs.arouter_api
    kapt libs.arouter_compiler


<span class="hljs-comment">// 定义路由地址</span>
<span class="hljs-keyword">object</span> ARouterConstant &#123;

    <span class="hljs-comment">// == 服务</span>
    <span class="hljs-keyword">const</span> <span class="hljs-keyword">val</span> LOGIN_SERVICE = <span class="hljs-string">"/login/login_service"</span>

    <span class="hljs-comment">//====== login</span>
    <span class="hljs-comment">//跳转到登陆页面</span>
    <span class="hljs-keyword">const</span> <span class="hljs-keyword">val</span> LOGIN_ACTIVITY = <span class="hljs-string">"/login/LoginActivity"</span>
    <span class="hljs-keyword">const</span> <span class="hljs-keyword">val</span> LOGIN_FRAGMENT = <span class="hljs-string">"/login/LoginFragment"</span>
    ...

&#125;


<span class="hljs-comment">// 路由地址目标类</span>
<span class="hljs-meta">@Route(path = LOGIN_ACTIVITY)</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoginActivity</span> : <span class="hljs-type">ContainerActivity</span></span>() &#123;

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">initBaseFragment</span><span class="hljs-params">()</span></span>: Fragment? &#123;
        <span class="hljs-keyword">return</span> LoginFragment()
    &#125;
&#125;

<span class="hljs-comment">//调用界面跳转</span>
ARouter.build(ARouterConstant . LOGIN_ACTIVITY).navigation()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2 . 通信问题</h3>
<p>   常用的通信方式有：BroadcastReceiver 、EventBus、接口等，考虑到 BroadcastReceiver 偏重，Eventbus 虽然3.0以后采用注解方式通信比2.X版本采用反射快得多，但根据组件化架构多个Module都依赖于Base Module，这里使用ARouter 的IProvider方式进行数据传递。</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-comment">//接口定义</span>
<span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">LoginService</span> : <span class="hljs-type">IProvider &#123;</span></span>

    <span class="hljs-keyword">val</span> userInfo: UserBean?

    ...
&#125;


<span class="hljs-comment">//接口实现</span>
<span class="hljs-meta">@Route(path = LOGIN_SERVICE)</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoginServiceImpl</span> : <span class="hljs-type">LoginService &#123;</span></span>

    <span class="hljs-keyword">override</span> <span class="hljs-keyword">val</span> userInfo: UserBean
        <span class="hljs-keyword">get</span>() = getUserBean()

    ...
&#125;


<span class="hljs-comment">// 调用</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoginImpl</span> <span class="hljs-keyword">public</span> <span class="hljs-keyword">constructor</span></span>() &#123;

    <span class="hljs-keyword">init</span> &#123;
        <span class="hljs-comment">//初始化</span>
        ARouter.getInstance().inject(<span class="hljs-keyword">this</span>)
    &#125;

    <span class="hljs-meta">@Autowired(name = ARouterConstant.LOGIN_SERVICE)</span>
    <span class="hljs-keyword">lateinit</span> <span class="hljs-keyword">var</span> mLoginService: LoginService

    <span class="hljs-comment">/**
     * 获取用户信息
     */</span>
    <span class="hljs-keyword">val</span> userInfo: UserBean?
        <span class="hljs-keyword">get</span>() = mLoginService.userInfo
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">3. 单工程方案</h3>
<p>  由于多个Module，存在独立运行和合并运行的情况，资源文件命名冲突及 Lib、Module定义等问题。</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-comment">// module_home.gradle文件</span>
apply from: rootProject.file(<span class="hljs-string">'module.gradle'</span>)

android &#123;

    defaultConfig &#123;
        <span class="hljs-comment">//仅在以application方式编译时才添加applicationId属性</span>
        <span class="hljs-keyword">if</span> (runAsApp) &#123;
            applicationId build_version.applicationId + <span class="hljs-string">'.module_home'</span>
        &#125;
    &#125;

    <span class="hljs-comment">//资源命名规范</span>
    resourcePrefix <span class="hljs-string">"home_"</span>

    kotlinOptions &#123;
        jvmTarget = JavaVersion.VERSION_1_8.toString()
    &#125;

&#125;

dependencies &#123;
    implementation fileTree(dir: <span class="hljs-string">"libs"</span>, include: [<span class="hljs-string">"*.jar"</span>])
    ...

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上述资源规范，可以让各个module出现命名不规范的变量名，会给予提示。</p>
<pre><code class="hljs language-gradle copyable" lang="gradle"><span class="hljs-comment">// </span>
<span class="hljs-comment">//是否library</span>
<span class="hljs-keyword">def</span> isLibrary = ext.has(<span class="hljs-string">'isLibrary'</span>)
ext.isLibrary = isLibrary
<span class="hljs-comment">//</span>
<span class="hljs-keyword">def</span> isMainLibrary = ext.has(<span class="hljs-string">'isMainLibrary'</span>)
ext.isMainLibrary = isMainLibrary

<span class="hljs-comment">//设置到ext中，供lib的build.gradle使用</span>
apply plugin: <span class="hljs-string">'com.android.library'</span>
apply plugin: <span class="hljs-string">'kotlin-android'</span>
apply plugin: <span class="hljs-string">'kotlin-android-extensions'</span>


android &#123;
    compileSdkVersion build_version.compileSdkVersion
    buildToolsVersion build_version.buildToolsVersion

    defaultConfig &#123;
        ...
    &#125;

    buildTypes &#123;
        debug &#123;
            ...
        &#125;
        release &#123;
            release &#123;
                ...
            &#125;
        &#125;
    &#125;

    <span class="hljs-keyword">sourceSets</span> &#123;
        main &#123;
            jniLibs.srcDirs = [<span class="hljs-string">'libs'</span>]
        &#125;
    &#125;
    <span class="hljs-comment">// 省略部分配置</span>
    ...

&#125;

<span class="hljs-keyword">dependencies</span> &#123;
    implementation <span class="hljs-keyword">fileTree</span>(dir: <span class="hljs-string">"libs"</span>, <span class="hljs-keyword">include</span>: [<span class="hljs-string">"*.jar"</span>])
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码，通过ext.isLibrary来区分该module是以lib方式运行还是独立运行。</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-meta">local.properties</span> <span class="hljs-string">文件</span>

<span class="hljs-meta">sdk.dir</span>=<span class="hljs-string">/Users/yangmingchuan/Library/Android/sdk</span>

<span class="hljs-meta">//</span> <span class="hljs-string">配置本地debug 开关</span>
<span class="hljs-comment">#module_home=true</span>
<span class="hljs-comment">#module_login=true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-gradle copyable" lang="gradle">module.gradle 文件

<span class="hljs-comment">//配置AndroidManifest.xml在library模式和application模式下的文件路径</span>
android &#123;
    <span class="hljs-comment">//隐藏部分配置</span>
    ...

    <span class="hljs-keyword">sourceSets</span> &#123;
        main &#123;
            jniLibs.srcDirs = [<span class="hljs-string">'libs'</span>]
            <span class="hljs-comment">//默认的作为application运行时Manifest文件路径</span>
            <span class="hljs-keyword">def</span> debugManifest = <span class="hljs-string">'src/main/debug/AndroidManifest.xml'</span>
            <span class="hljs-keyword">if</span> (runAsApp && <span class="hljs-keyword">project</span>.<span class="hljs-keyword">file</span>(debugManifest).exists()) &#123;
                manifest.srcFile debugManifest
            &#125; <span class="hljs-keyword">else</span> &#123;
                manifest.srcFile <span class="hljs-string">'src/main/AndroidManifest.xml'</span>
                <span class="hljs-comment">//集成开发模式下自动排除debug文件夹中的所有Java文件</span>
                <span class="hljs-comment">// 可以将debug代码放在这个包内，例如：Application子类</span>
                java &#123;
                    <span class="hljs-keyword">exclude</span> <span class="hljs-string">'debug/**'</span>
                &#125;
            &#125;
            <span class="hljs-comment">// 注：2018-03-12推荐：将组件单独以app运行时的测试代码及资源放到src/main/debug/目录下</span>
            <span class="hljs-keyword">if</span> (runAsApp) &#123;
                <span class="hljs-comment">//debug模式下，如果存在src/main/debug/assets，则自动将其添加到assets源码目录</span>
                <span class="hljs-keyword">if</span> (<span class="hljs-keyword">project</span>.<span class="hljs-keyword">file</span>(<span class="hljs-string">'src/main/debug/assets'</span>).exists()) &#123;
                    assets.srcDirs = [<span class="hljs-string">'src/main/assets'</span>, <span class="hljs-string">'src/main/debug/assets'</span>]
                &#125;
                <span class="hljs-comment">//debug模式下，如果存在src/main/debug/java，则自动将其添加到java源码目录</span>
                <span class="hljs-keyword">if</span> (<span class="hljs-keyword">project</span>.<span class="hljs-keyword">file</span>(<span class="hljs-string">'src/main/debug/java'</span>).exists()) &#123;
                    java.srcDirs = [<span class="hljs-string">'src/main/java'</span>, <span class="hljs-string">'src/main/debug/java'</span>]
                &#125;
                <span class="hljs-comment">//debug模式下，如果存在src/main/debug/res，则自动将其添加到资源目录</span>
                <span class="hljs-keyword">if</span> (<span class="hljs-keyword">project</span>.<span class="hljs-keyword">file</span>(<span class="hljs-string">'src/main/debug/res'</span>).exists()) &#123;
                    res.srcDirs = [<span class="hljs-string">'src/main/res'</span>, <span class="hljs-string">'src/main/debug/res'</span>]
                &#125;
            &#125;

        &#125;
    &#125;

     <span class="hljs-comment">//隐藏部分配置</span>
    ...

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码，使用读取 local.properties 本地配置，sync project 后，即可单Module运行 加载src/main/debug文件夹下的清单文件， 开始debug测试。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5bb729e0d9e47128f2d9a16c43980c0~tplv-k3u1fbpfcp-watermark.image" alt="2.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>该文章为本人学习组件化总结，有不当的地方还望指出，一起学习。
后续不断更新....</p>
<p>不要脸贴下GitHub <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyangmingchuan%2FComponentMaster" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/yangmingchuan/ComponentMaster" ref="nofollow noopener noreferrer">ComponentMaster</a></p></div>  
</div>
            