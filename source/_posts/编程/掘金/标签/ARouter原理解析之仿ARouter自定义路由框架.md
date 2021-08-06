
---
title: 'ARouter原理解析之仿ARouter自定义路由框架'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e780067c86774cc8b253dd7713080f0c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 03:30:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e780067c86774cc8b253dd7713080f0c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">ARouter是什么？</h2>
<p>ARouter是阿里开源的一款android路由框架，帮助 Android App 进行组件化改造的路由框架 —— 支持模块间的路由、通信、解耦；结合路由可以实现组件化。</p>
<h2 data-id="heading-1">ARouter接入指北</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2FARouter%2Fblob%2Fmaster%2FREADME_CN.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/ARouter/blob/master/README_CN.md" ref="nofollow noopener noreferrer">完整Arouter接入指南</a>，ARouter重度用户可以跳过，直接往后看</p>
<ul>
<li>第一步，根build.gradle设置使用arouter-register</li>
</ul>
<pre><code class="hljs language-groovy copyable" lang="groovy">apply <span class="hljs-attr">plugin:</span> <span class="hljs-string">'com.alibaba.arouter'</span>
buildscript &#123;
    repositories &#123;
        mavenCentral()
    &#125;
    dependencies &#123;
        classpath <span class="hljs-string">"com.alibaba:arouter-register:?"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第二步，创建baselib，并加入dependencies</li>
</ul>
<pre><code class="hljs language-groovy copyable" lang="groovy">api <span class="hljs-string">'com.alibaba:arouter-api:x.x.x'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第三步，创建组件module，例如login 或者setting 组件</li>
</ul>
<pre><code class="hljs language-groovy copyable" lang="groovy">android &#123;
    defaultConfig &#123;
        ...
        javaCompileOptions &#123;
            annotationProcessorOptions &#123;
                arguments = [<span class="hljs-attr">AROUTER_MODULE_NAME:</span> project.getName()]
            &#125;
        &#125;
    &#125;
&#125;

dependencies &#123;
    <span class="hljs-comment">// 替换成最新版本, 需要注意的是api</span>
    <span class="hljs-comment">// 要与compiler匹配使用，均使用最新版可以保证兼容</span>
    <span class="hljs-comment">//compile 'com.alibaba:arouter-api:x.x.x' 此移动到baselib中</span>
    api project(<span class="hljs-attr">path:</span> <span class="hljs-string">':baselib'</span>)
    annotationProcessor <span class="hljs-string">'com.alibaba:arouter-compiler:x.x.x'</span>
    ...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第四步，通过注解@Route 注册页面</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 在支持路由的页面上添加注解(必选)</span>
<span class="hljs-comment">// 这里的路径需要注意的是至少需要有两级，/xx/xx</span>
<span class="hljs-meta">@Route(path = "/test/activity")</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">YourActivity</span> <span class="hljs-title">extend</span> <span class="hljs-title">Activity</span> </span>&#123;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第五步，初始化</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">if</span> (isDebug()) &#123;           <span class="hljs-comment">// 这两行必须写在init之前，否则这些配置在init过程中将无效</span>
    ARouter.openLog();     <span class="hljs-comment">// 打印日志</span>
    ARouter.openDebug();   <span class="hljs-comment">// 开启调试模式(如果在InstantRun模式下运行，必须开启调试模式！线上版本需要关闭,否则有安全风险)</span>
&#125;
ARouter.init(mApplication); <span class="hljs-comment">// 尽可能早，推荐在Application中初始化</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第六步，使用ARouter</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">ARouter.getInstance().build(<span class="hljs-string">"/test/activity"</span>).navigation();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">ARouter比传统Intent有哪些优点</h2>
<h3 data-id="heading-3">传统intent的优点</h3>
<ul>
<li>轻量</li>
<li>简单</li>
</ul>
<h3 data-id="heading-4">传统intent的缺点</h3>
<ul>
<li>跳转过程无法控制，一旦调用了<code>startActivity(Intent)</code>便交由系统执行，中间过程无法插手</li>
<li>跳转失败无法捕获、降级，出现问题直接抛出异常</li>
<li>显示Intent中因为存在直接的类依赖关系，导致耦合严重</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">startActivity(<span class="hljs-keyword">new</span> Intent(MainActivity.<span class="hljs-keyword">this</span>, LoginActivity.class));<span class="hljs-comment">//强依赖LoginActivity</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>隐式Intent中会出现规则集中式的管理，导致协作困难，都需要在Manifest中进行配置，导致扩展性比较差</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">//隐式 比 显式更强一点，可以在两个无关子module 之间跳转，由于显式无法引入包，所以无法完成跳转</span>
Intent intent = <span class="hljs-keyword">new</span> Intent();
intent.setClassName(MainActivity.<span class="hljs-keyword">this</span>,<span class="hljs-string">"com.cnn.loginplugin.ui.login.LoginActivity"</span>);<span class="hljs-comment">//设置包路径</span>
startActivity(intent);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">ARouter优点</h3>
<ul>
<li>模块间通信(后面讲原理)</li>
<li>支持url 跳转 <code>build("/test/activity").navigation()</code></li>
<li>支持拦截器</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 比较经典的应用就是在跳转过程中处理登陆事件，这样就不需要在目标页重复做登陆检查</span>
<span class="hljs-comment">// 拦截器会在跳转之间执行，多个拦截器会按优先级顺序依次执行</span>
<span class="hljs-meta">@Interceptor(priority = 8, name = "测试用拦截器")</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestInterceptor</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">IInterceptor</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">process</span><span class="hljs-params">(Postcard postcard, InterceptorCallback callback)</span> </span>&#123;
    ...
    callback.onContinue(postcard);  <span class="hljs-comment">// 处理完成，交还控制权</span>
    <span class="hljs-comment">// callback.onInterrupt(new RuntimeException("我觉得有点异常"));      // 觉得有问题，中断路由流程</span>

    <span class="hljs-comment">// 以上两种至少需要调用其中一种，否则不会继续路由</span>
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">init</span><span class="hljs-params">(Context context)</span> </span>&#123;
    <span class="hljs-comment">// 拦截器的初始化，会在sdk初始化的时候调用该方法，仅会调用一次</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>参数注入，@Autowired注解实现，更方便，需要配合<code>ARouter.getInstance().inject(this);</code>一起使用</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Autowired</span>
    <span class="hljs-keyword">public</span> String name;
    <span class="hljs-meta">@Autowired</span>
    <span class="hljs-keyword">int</span> age;
    <span class="hljs-comment">// 通过name来映射URL中的不同参数</span>
    <span class="hljs-meta">@Autowired(name = "girl")</span> 
    <span class="hljs-keyword">boolean</span> boy;
    <span class="hljs-comment">// 支持解析自定义对象，URL中使用json传递</span>
    <span class="hljs-meta">@Autowired</span>
    TestObj obj;
<span class="hljs-comment">// 使用 withObject 传递 List 和 Map 的实现了</span>
    <span class="hljs-comment">// Serializable 接口的实现类(ArrayList/HashMap)</span>
    <span class="hljs-comment">// 的时候，接收该对象的地方不能标注具体的实现类类型</span>
    <span class="hljs-comment">// 应仅标注为 List 或 Map，否则会影响序列化中类型</span>
    <span class="hljs-comment">// 的判断, 其他类似情况需要同样处理        </span>
    <span class="hljs-meta">@Autowired</span>
    List<TestObj> list;
    <span class="hljs-meta">@Autowired</span>
    Map<String, List<TestObj>> map;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>支持外部url 跳转</li>
</ul>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">activity</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">".SchemeFilterActivity"</span>></span>
            <span class="hljs-comment"><!-- Scheme --></span>
            <span class="hljs-tag"><<span class="hljs-name">intent-filter</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">data</span>
                    <span class="hljs-attr">android:host</span>=<span class="hljs-string">"www.nativie.com"</span>
                    <span class="hljs-attr">android:scheme</span>=<span class="hljs-string">"arouter"</span>/></span>
                <span class="hljs-tag"><<span class="hljs-name">action</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.intent.action.VIEW"</span>/></span>
                <span class="hljs-tag"><<span class="hljs-name">category</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.intent.category.DEFAULT"</span>/></span>
                <span class="hljs-tag"><<span class="hljs-name">category</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.intent.category.BROWSABLE"</span>/></span>
            <span class="hljs-tag"></<span class="hljs-name">intent-filter</span>></span>
<span class="hljs-tag"></<span class="hljs-name">activity</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>简单demo，github做简单静态界面服务器，并部署到<a href="https://link.juejin.cn/?target=https%3A%2F%2Foslanka.github.io%2Fstatichtml.github.io%2F%25EF%25BC%258C%25E6%2589%258B%25E6%259C%25BA%25E6%25B5%258F%25E8%25A7%2588%25E5%2599%25A8%25E6%2589%2593%25E5%25BC%2580%25EF%25BC%258C%25E5%25B9%25B6%25E7%2582%25B9%25E5%2587%25BBhref%25E5%25AE%259E%25E7%258E%25B0html%25E6%2589%2593%25E9%2580%259A%25E5%258E%259F%25E7%2594%259F%25EF%25BC%258C%25E6%258C%2589%25E9%2581%2593%25E7%2590%2586%25E6%259D%25A5%25E8%25AF%25B4%25EF%25BC%258C%25E6%2589%2580%25E6%259C%2589%25E6%259C%25AA%25E6%258B%25A6%25E6%2588%25AA%25E7%259A%2584ARouter%25E8%25B7%25AF%25E5%25BE%2584%25EF%25BC%258C%25E5%259D%2587%25E5%258F%25AF%25E8%25A2%25ABweb%25E6%25B5%258F%25E8%25A7%2588%25E5%2599%25A8%25E8%25B7%25B3%25E8%25BD%25AC%25EF%25BC%258Chtml%25E4%25BB%25A3%25E7%25A0%2581%25E5%25A6%2582%25E4%25B8%258B%25EF%25BC%259A" target="_blank" rel="nofollow noopener noreferrer" title="https://oslanka.github.io/statichtml.github.io/%EF%BC%8C%E6%89%8B%E6%9C%BA%E6%B5%8F%E8%A7%88%E5%99%A8%E6%89%93%E5%BC%80%EF%BC%8C%E5%B9%B6%E7%82%B9%E5%87%BBhref%E5%AE%9E%E7%8E%B0html%E6%89%93%E9%80%9A%E5%8E%9F%E7%94%9F%EF%BC%8C%E6%8C%89%E9%81%93%E7%90%86%E6%9D%A5%E8%AF%B4%EF%BC%8C%E6%89%80%E6%9C%89%E6%9C%AA%E6%8B%A6%E6%88%AA%E7%9A%84ARouter%E8%B7%AF%E5%BE%84%EF%BC%8C%E5%9D%87%E5%8F%AF%E8%A2%ABweb%E6%B5%8F%E8%A7%88%E5%99%A8%E8%B7%B3%E8%BD%AC%EF%BC%8Chtml%E4%BB%A3%E7%A0%81%E5%A6%82%E4%B8%8B%EF%BC%9A" ref="nofollow noopener noreferrer">oslanka.github.io/statichtml.…</a></li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://www.360.com/"</span>></span>测试跳转<span class="hljs-tag"></<span class="hljs-name">a</span>></span> <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"arouter://www.nativie.com/login/login"</span>></span>跳转登录android-ARouter<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"arouter://www.nativie.com/login/login?username=admin&password=123456"</span>></span>跳转登录android-ARouter 带参数<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"arouter://www.nativie.com/setting/setting"</span>></span>跳转android-ARouter 设置界面<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"arouter://www.nativie.com/web/web"</span>></span>跳转android-ARouter 设置界面<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"arouter://www.nativie.com/test/test"</span>></span>跳转android-ARouter 错误路径<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">关于拦截器</h2>
<ul>
<li>拦截器(拦截跳转过程，面向切面编程)</li>
<li>什么是面向切面编程AOP？AOP为Aspect Oriented Programming的缩写，意为：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E9%259D%25A2%25E5%2590%2591%25E5%2588%2587%25E9%259D%25A2%25E7%25BC%2596%25E7%25A8%258B%2F6016335" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E9%9D%A2%E5%90%91%E5%88%87%E9%9D%A2%E7%BC%96%E7%A8%8B/6016335" ref="nofollow noopener noreferrer">面向切面编程</a>，通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E9%25A2%2584%25E7%25BC%2596%25E8%25AF%2591%2F3191547" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E9%A2%84%E7%BC%96%E8%AF%91/3191547" ref="nofollow noopener noreferrer">预编译</a>方式和运行期间动态代理实现程序功能的统一维护的一种技术。AOP是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2FOOP" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/OOP" ref="nofollow noopener noreferrer">OOP</a>的延续，是软件开发中的一个热点，也是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2FSpring" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/Spring" ref="nofollow noopener noreferrer">Spring</a>框架中的一个重要内容，是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E5%2587%25BD%25E6%2595%25B0%25E5%25BC%258F%25E7%25BC%2596%25E7%25A8%258B%2F4035031" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B/4035031" ref="nofollow noopener noreferrer">函数式编程</a>的一种衍生范型。利用AOP可以对业务逻辑的各个部分进行隔离，从而使得业务逻辑各部分之间的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E8%2580%25A6%25E5%2590%2588%25E5%25BA%25A6%2F2603938" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E8%80%A6%E5%90%88%E5%BA%A6/2603938" ref="nofollow noopener noreferrer">耦合度</a>降低，提高程序的可重用性，同时提高了开发的效率</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 拦截器会在跳转之前执行，多个拦截器会按优先级顺序依次执行</span>
<span class="hljs-meta">@Interceptor(priority = 8, name = "测试用拦截器")</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestInterceptor</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">IInterceptor</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">process</span><span class="hljs-params">(Postcard postcard, InterceptorCallback callback)</span> </span>&#123;
    ...
    callback.onContinue(postcard);  <span class="hljs-comment">// 处理完成，交还控制权</span>
    <span class="hljs-comment">// callback.onInterrupt(new RuntimeException("我觉得有点异常"));      // 觉得有问题，中断路由流程</span>

    <span class="hljs-comment">// 以上两种至少需要调用其中一种，否则不会继续路由</span>
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">init</span><span class="hljs-params">(Context context)</span> </span>&#123;
    <span class="hljs-comment">// 拦截器的初始化，会在sdk初始化的时候调用该方法，仅会调用一次</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">动态路由</h2>
<ul>
<li>动态注册路由信息 适用于部分插件化架构的App以及需要动态注册路由信息的场景，可以通过 ARouter 提供的接口实现动态注册 路由信息，目标页面和服务可以不标注 @Route 注解，<strong>注意：同一批次仅允许相同 group 的路由信息注册</strong></li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">ARouter.getInstance().addRouteGroup(<span class="hljs-keyword">new</span> IRouteGroup() &#123;
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">loadInto</span><span class="hljs-params">(Map<String, RouteMeta> atlas)</span> </span>&#123;
            atlas.put(<span class="hljs-string">"/dynamic/activity"</span>,      <span class="hljs-comment">// path</span>
                RouteMeta.build(
                    RouteType.ACTIVITY,         <span class="hljs-comment">// 路由信息</span>
                    TestDynamicActivity.class,  <span class="hljs-comment">// 目标的 Class</span>
                    <span class="hljs-string">"/dynamic/activity"</span>,        <span class="hljs-comment">// Path</span>
                    <span class="hljs-string">"dynamic"</span>,                  <span class="hljs-comment">// Group, 尽量保持和 path 的第一段相同</span>
                    <span class="hljs-number">0</span>,                          <span class="hljs-comment">// 优先级，暂未使用</span>
                    <span class="hljs-number">0</span>                           <span class="hljs-comment">// Extra，用于给页面打标</span>
                )
            );
        &#125;
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">ARouter详细API</h2>
<pre><code class="hljs language-java copyable" lang="java">
<span class="hljs-comment">// 构建标准的路由请求，并指定分组</span>
ARouter.getInstance().build(<span class="hljs-string">"/home/main"</span>, <span class="hljs-string">"ap"</span>).navigation();
<span class="hljs-comment">// 构建标准的路由请求，通过Uri直接解析</span>
Uri uri;
ARouter.getInstance().build(uri).navigation();

<span class="hljs-comment">// 构建标准的路由请求，startActivityForResult</span>
<span class="hljs-comment">// navigation的第一个参数必须是Activity，第二个参数则是RequestCode</span>
ARouter.getInstance().build(<span class="hljs-string">"/home/main"</span>, <span class="hljs-string">"ap"</span>).navigation(<span class="hljs-keyword">this</span>, <span class="hljs-number">5</span>);

<span class="hljs-comment">// 指定Flag</span>
ARouter.getInstance()
    .build(<span class="hljs-string">"/home/main"</span>)
    .withFlags();
    .navigation();

<span class="hljs-comment">// 获取Fragment</span>
Fragment fragment = (Fragment) ARouter.getInstance().build(<span class="hljs-string">"/test/fragment"</span>).navigation();
                    
<span class="hljs-comment">// 对象传递</span>
ARouter.getInstance()
    .withObject(<span class="hljs-string">"key"</span>, <span class="hljs-keyword">new</span> TestObj(<span class="hljs-string">"Jack"</span>, <span class="hljs-string">"Rose"</span>))
    .navigation();

<span class="hljs-comment">// 使用绿色通道(跳过所有的拦截器)</span>
ARouter.getInstance().build(<span class="hljs-string">"/home/main"</span>).greenChannel().navigation();

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">原理探索</h2>
<ul>
<li>ARouter.init 时，通过获取<code>/data/app/包名/base.apk</code>来筛选出ARouter生成的类，如下图。</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e780067c86774cc8b253dd7713080f0c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210729163725845" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>对于Activity类型，跳转<code>ARouter.getInstance().build("/login/login").navigation();</code>，最终执行的是，如下：</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">**
     * Start activity
     *
     * <span class="hljs-meta">@see</span> ActivityCompat
     */
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">startActivity</span><span class="hljs-params">(<span class="hljs-keyword">int</span> requestCode, Context currentContext, Intent intent, Postcard postcard, NavigationCallback callback)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (requestCode >= <span class="hljs-number">0</span>) &#123;  <span class="hljs-comment">// Need start for result</span>
            <span class="hljs-keyword">if</span> (currentContext <span class="hljs-keyword">instanceof</span> Activity) &#123;<span class="hljs-comment">//启动context 为Activity</span>
                ActivityCompat.startActivityForResult((Activity) currentContext, intent, requestCode, postcard.getOptionsBundle());
            &#125; <span class="hljs-keyword">else</span> &#123;
              <span class="hljs-comment">// 启动context 为Application 时，不支持requestCode</span>
                logger.warning(Consts.TAG, <span class="hljs-string">"Must use [navigation(activity, ...)] to support [startActivityForResult]"</span>);
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;<span class="hljs-comment">//启动context 为Application</span>
            ActivityCompat.startActivity(currentContext, intent, postcard.getOptionsBundle());
        &#125;

        <span class="hljs-keyword">if</span> ((-<span class="hljs-number">1</span> != postcard.getEnterAnim() && -<span class="hljs-number">1</span> != postcard.getExitAnim()) && currentContext <span class="hljs-keyword">instanceof</span> Activity) &#123;    <span class="hljs-comment">// Old version.</span>
            ((Activity) currentContext).overridePendingTransition(postcard.getEnterAnim(), postcard.getExitAnim());
        &#125;

        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">null</span> != callback) &#123; <span class="hljs-comment">// Navigation over.</span>
            callback.onArrival(postcard);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>两个无关的module 如何跳转的呢？我们发现最终执行startActivity时，所用的context为Application，思路是这样的，子module启动另外无关子module时，将执行权，交还给主进程/主程序去处理</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bd43b54b3a94db4827b625262db73df~tplv-k3u1fbpfcp-watermark.image" alt="image-20210724170943112" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>打开生成路由文档,AROUTER_GENERATE_DOC="enable",会生成arouter-map-of-xx.json和3个java文件</li>
</ul>
<pre><code class="hljs language-groovy copyable" lang="groovy"><span class="hljs-comment">// 更新 build.gradle, 添加参数 AROUTER_GENERATE_DOC = enable</span>
<span class="hljs-comment">// 生成的文档路径 : build/generated/ap_generated_sources/(debug or release)/com/alibaba/android/arouter/docs/arouter-map-of-$&#123;moduleName&#125;.json</span>
android &#123;
    defaultConfig &#123;
        ...
        javaCompileOptions &#123;
            annotationProcessorOptions &#123;
                arguments = [<span class="hljs-attr">AROUTER_MODULE_NAME:</span> project.getName(), <span class="hljs-attr">AROUTER_GENERATE_DOC:</span> <span class="hljs-string">"enable"</span>]
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-comment">//ARouter映射关系如何生成？Generated出三个文件</span>
<span class="hljs-comment">//ARouter$$Group$$login</span>
<span class="hljs-comment">//ARouter$$Providers$$loginplugin</span>
<span class="hljs-comment">//ARouter$$Root$$loginplugin</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59611e2b853847a498ea66484daddb3f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210724163442843" loading="lazy" referrerpolicy="no-referrer">
<pre><code class="hljs language-java copyable" lang="java">    atlas.put(<span class="hljs-string">"/login/login"</span>, RouteMeta.build(RouteType.ACTIVITY, LoginActivity.class, <span class="hljs-string">"/login/login"</span>, <span class="hljs-string">"login"</span>, <span class="hljs-keyword">new</span> java.util.HashMap<String, Integer>()&#123;&#123;put(<span class="hljs-string">"password"</span>, <span class="hljs-number">8</span>); put(<span class="hljs-string">"username"</span>, <span class="hljs-number">8</span>); &#125;&#125;, -<span class="hljs-number">1</span>, -<span class="hljs-number">2147483648</span>));

<span class="hljs-comment">//map 存映射关系</span>
<span class="hljs-comment">//static Map<String, RouteMeta> routes = new HashMap<>();</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>以上三个文件是如何生成的呢？APT是Annotation Processing Tool的简称,即注解处理工具，apt是在编译期对代码中指定的注解进行解析，然后做一些其他处理（如通过javapoet生成新的Java文件）ARouter使用了两个库<code>auto-service</code> <code>javapoet</code>，来实现从注解到代码的注入，其中<code>auto-service</code>为注解处理器的库，<code>javapoet</code>为代码生成器</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83e9fee02a6f4e6f9cd1b9d2b786e67a~tplv-k3u1fbpfcp-watermark.image" alt="javaPoet" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-10">通过例子了解APT</h2>
<h3 data-id="heading-11">首先我们了解一下元注解，meta-annotation（元注解）</h3>
<ul>
<li>@Target</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">  TYPE, <span class="hljs-comment">// 类、接口、枚举类 </span>
  FIELD, <span class="hljs-comment">// 成员变量（包括：枚举常量）</span>
  METHOD, <span class="hljs-comment">// 成员方法</span>
  PARAMETER, <span class="hljs-comment">// 方法参</span>
  CONSTRUCTOR, <span class="hljs-comment">// 构造方法</span>
  LOCAL_VARIABLE, <span class="hljs-comment">// 局部变量</span>
  ANNOTATION_TYPE, <span class="hljs-comment">// 注解类</span>
  PACKAGE, <span class="hljs-comment">// 可用于修饰：包</span>
  TYPE_PARAMETER, <span class="hljs-comment">// 类型参数，JDK 1.8 新增</span>
  TYPE_USE <span class="hljs-comment">// 使用类型的任何地方，JDK 1.8 新增</span>
  ```

-  <span class="hljs-meta">@Retention</span>

```java
  SOURCE,    只在本编译单元的编译过程中保留，并不写入Class文件中。
  CLASS,       在编译的过程中保留并且会写入Class文件中,但是JVM在加载类的时候不需要将其加载为运行时可见的（反射可见）的注解==是JVM在加载类时反射不可见。
  RUNTIME   在编译过程中保留，会写入Class文件，并且JVM加载类的时候也会将其加载为反射可见的注解。
  ```

-  <span class="hljs-meta">@Documented</span> 注解的作用是：描述在使用 javadoc 工具为类生成帮助文档时是否要保留其注解信息.

-  <span class="hljs-meta">@Inherited</span> 注解的作用是：使被它修饰的注解具有继承性（如果某个类使用了被<span class="hljs-meta">@Inherited</span>修饰的注解，则其子类将自动具有该注解）

- 通过元注解我们定义自己的注解

- [AutoService 注解处理器](https:<span class="hljs-comment">//github.com/google/auto/tree/master/service)</span>

​注解处理器是一个在javac中的，用来编译时扫描和处理的注解的工具。你可以为特定的注解，注册你自己的注解处理器。到这里，我假设你已经知道什么是注解，并且知道怎么申明的一个注解类型。

一个注解的注解处理器，以Java代码（或者编译过的字节码）作为输入，生成文件（通常是.java文件）作为输出。

- 虚处理器`AbstractProcessor`
- `init(ProcessingEnvironment env)`: 【核心】
  每一个注解处理器类都必须有一个空的构造函数。然而，这里有一个特殊的init()方法，它会被注解处理工具调用，并输入`ProcessingEnviroment`参数。`ProcessingEnviroment`提供很多有用的工具类`Elements`,`Types`和`Filer`
- `process(Set< ? extends TypeElement> annotations, RoundEnvironment env)`:【核心】
  这相当于每个处理器的主函数main()。你在这里写你的扫描、评估和处理注解的代码，以及生成Java文件
- `getSupportedAnnotationTypes()`
  这里你必须指定，这个注解处理器是注册给哪个注解的
- `getSupportedSourceVersion()`
  用来指定你使用的Java版本。通常这里返回`SourceVersion.latestSupported()`

- APT 所用的代码生成器：**[JavaPoet](https:<span class="hljs-comment">//github.com/square/javapoet)** is a Java API for generating `.java` source files.（JavaPoet 是一个java api ，为了生成 .java源文件的）</span>

- 官方helloworld

```java
MethodSpec main = MethodSpec.methodBuilder(<span class="hljs-string">"main"</span>)
  .addModifiers(Modifier.PUBLIC, Modifier.STATIC)
  .returns(<span class="hljs-keyword">void</span>.class)
  .addParameter(String[].class, <span class="hljs-string">"args"</span>)
  .addStatement(<span class="hljs-string">"$T.out.println($S)"</span>, System.class, <span class="hljs-string">"Hello, JavaPoet!"</span>)
  .build();

TypeSpec helloWorld = TypeSpec.classBuilder(<span class="hljs-string">"HelloWorld"</span>)
  .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
  .addMethod(main)
  .build();

JavaFile javaFile = JavaFile.builder(<span class="hljs-string">"com.example.helloworld"</span>, helloWorld)
  .build();

javaFile.writeTo(System.out);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过以上可生成以下java 文件</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">package</span> com.example.helloworld;

<span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HelloWorld</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
    System.out.println(<span class="hljs-string">"Hello, JavaPoet!"</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>JavaPoet</code> 主要api</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">- JavaFile 用于构造输出包含一个顶级类的Java文件 
- TypeSpec 生成类，接口，或者枚举  
- MethodSpec 生成构造函数或方法 
- FieldSpec 生成成员变量或字段 
- ParameterSpec  用来创建参数  
- AnnotationSpec 用来创建注解
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>JavaPoet</code> 主要占位符</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">- $L(<span class="hljs-keyword">for</span> Literals) 执行结构的字符或常见类型，或TypeSpec, $S(<span class="hljs-keyword">for</span> Strings) 字符, $T(<span class="hljs-keyword">for</span> Types) 类, $N(<span class="hljs-keyword">for</span> Names) 方法 等标识符
  $L>$S
<span class="hljs-comment">//1.Pass an argument value for each placeholder in the format string to `CodeBlock.add()`. In each example, we generate code to say "I ate 3 tacos"</span>
CodeBlock.builder().add(<span class="hljs-string">"I ate $L $L"</span>, <span class="hljs-number">3</span>, <span class="hljs-string">"tacos"</span>)
 <span class="hljs-comment">//2.When generating the code above, we pass the hexDigit() method as an argument to the byteToHex() method using $N:</span>
  MethodSpec byteToHex = MethodSpec.methodBuilder(<span class="hljs-string">"byteToHex"</span>)
    .addParameter(<span class="hljs-keyword">int</span>.class, <span class="hljs-string">"b"</span>)
    .returns(String.class)
    .addStatement(<span class="hljs-string">"char[] result = new char[2]"</span>)
    .addStatement(<span class="hljs-string">"result[0] = $N((b >>> 4) & 0xf)"</span>, hexDigit)
    .addStatement(<span class="hljs-string">"result[1] = $N(b & 0xf)"</span>, hexDigit)
    .addStatement(<span class="hljs-string">"return new String(result)"</span>)
    .build();
<span class="hljs-comment">//=======================</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">byteToHex</span><span class="hljs-params">(<span class="hljs-keyword">int</span> b)</span> </span>&#123;
  <span class="hljs-keyword">char</span>[] result = <span class="hljs-keyword">new</span> <span class="hljs-keyword">char</span>[<span class="hljs-number">2</span>];
  result[<span class="hljs-number">0</span>] = hexDigit((b >>> <span class="hljs-number">4</span>) & <span class="hljs-number">0xf</span>);
  result[<span class="hljs-number">1</span>] = hexDigit(b & <span class="hljs-number">0xf</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> String(result);
&#125;

<span class="hljs-comment">//$T for Types</span>
<span class="hljs-comment">//We Java programmers love our types: they make our code easier to understand. And JavaPoet is on board. It has rich built-in support for types, including automatic generation of import statements. Just use $T to reference types:</span>
.addStatement(<span class="hljs-string">"return new $T()"</span>, Date.class)== <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Date();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">实战-自定义简易版路由-CRouter</h2>
<ul>
<li>新建name-annotation javaLib，定义CRoute注解</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Target(&#123;ElementType.TYPE&#125;)</span>
<span class="hljs-meta">@Retention(RetentionPolicy.CLASS)</span>
<span class="hljs-keyword">public</span> <span class="hljs-meta">@interface</span> CRoute &#123;
    <span class="hljs-function">String <span class="hljs-title">path</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>新建name-compiler javaLib</li>
</ul>
<pre><code class="hljs language-groovy copyable" lang="groovy"><span class="hljs-number">1.</span>
dependencies &#123;
    implementation project(<span class="hljs-attr">path:</span> <span class="hljs-string">':TestRouter-annotation'</span>)
    annotationProcessor <span class="hljs-string">'com.google.auto.service:auto-service:1.0-rc7'</span>
    compileOnly <span class="hljs-string">'com.google.auto.service:auto-service-annotations:1.0-rc7'</span>

    implementation <span class="hljs-string">'com.squareup:javapoet:1.8.0'</span>
&#125;
<span class="hljs-number">2.</span><span class="hljs-meta">@AutoService</span>(Processor.<span class="hljs-keyword">class</span>)
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestRouteProcessor</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbstractProcessor</span> &#123;</span>
  <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">synchronized</span> <span class="hljs-keyword">void</span> init(ProcessingEnvironment processingEnvironment) &#123;
        <span class="hljs-built_in">super</span>.init(processingEnvironment);
       <span class="hljs-comment">//dosomething</span>
    &#125;
   <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> process(Set<? extends TypeElement> set, RoundEnvironment roundEnvironment) &#123;
      <span class="hljs-comment">//dosomething</span>
    &#125;
&#125;
 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>业务module执行顺序如下</li>
</ul>
<pre><code class="hljs language-groovy copyable" lang="groovy"> <span class="hljs-number">1.</span> annotationProcessor project(<span class="hljs-string">':TestRouter-compiler'</span>)
implementation project(<span class="hljs-string">':TestRouter-annotation'</span>)
<span class="hljs-number">2.</span>添加注解<span class="hljs-meta">@CRoute</span>(path = <span class="hljs-string">"/csetting/csetting"</span>)
<span class="hljs-number">3.</span>编译运行
<span class="hljs-number">4.</span>业务module apt 生成的java 文件，如下：
<span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span>$<span class="hljs-title">csettingC</span>$<span class="hljs-title">csettingHelloWorld</span> &#123;</span>
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> String holder = <span class="hljs-string">"/csetting/csetting:com.cnn.settingplugin.SettingsActivity"</span>;

  <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> main(String[] args) &#123;
    System.out.println(<span class="hljs-string">"Hello, JavaPoet!"</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>参考<code>ARouter-init</code> 方法，写出我们<code>CRouter-init</code></li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"> <span class="hljs-comment">/**
     * Init, it must be call before used router.
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">init</span><span class="hljs-params">(Application application)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (!hasInit) &#123;
            CRouter.application=application;
            hasInit=<span class="hljs-keyword">true</span>;
            <span class="hljs-keyword">try</span> &#123;
                getFileNameByPackageName(application, ROUTE_ROOT_PAKCAGE);
            &#125; <span class="hljs-keyword">catch</span> (PackageManager.NameNotFoundException e) &#123;
                e.printStackTrace();
            &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
                e.printStackTrace();
            &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
                e.printStackTrace();
            &#125;

        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>利用反射获取到注解对应映射关系，并参考ARouter存入HashMap</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/affb6245ca804993bcf232cfe90402c0~tplv-k3u1fbpfcp-watermark.image" alt="image-20210803144725376" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>通过隐式启动Activity模拟跳转</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7608cde6aec4c11b56d3691d8c30dc4~tplv-k3u1fbpfcp-watermark.image" alt="image-20210803144844114" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>到此我们模拟出简易版本的ARouter，完整自定义CRouter</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * Created by caining on 7/29/21 16:09
 * E-Mail Address：cainingning@360.cn
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CRouter</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">volatile</span> <span class="hljs-keyword">static</span> CRouter instance = <span class="hljs-keyword">null</span>;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">volatile</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">boolean</span> hasInit = <span class="hljs-keyword">false</span>;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> Application application;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String ROUTE_ROOT_PAKCAGE = <span class="hljs-string">"com.cnn.crouter"</span>;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> Map<String ,String> mapHolder = <span class="hljs-keyword">new</span> HashMap<>();

    <span class="hljs-comment">/**
     * Init, it must be call before used router.
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">init</span><span class="hljs-params">(Application application)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (!hasInit) &#123;
            CRouter.application=application;
            hasInit=<span class="hljs-keyword">true</span>;
            <span class="hljs-keyword">try</span> &#123;
                getFileNameByPackageName(application, ROUTE_ROOT_PAKCAGE);
            &#125; <span class="hljs-keyword">catch</span> (PackageManager.NameNotFoundException e) &#123;
                e.printStackTrace();
            &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
                e.printStackTrace();
            &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
                e.printStackTrace();
            &#125;

        &#125;
    &#125;

    <span class="hljs-comment">/**
     * Get instance of router. A
     * All feature U use, will be starts here.
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> CRouter <span class="hljs-title">getInstance</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (!hasInit) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> InitException(<span class="hljs-string">"ARouter::Init::Invoke init(context) first!"</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">if</span> (instance == <span class="hljs-keyword">null</span>) &#123;
                <span class="hljs-keyword">synchronized</span> (CRouter.class) &#123;
                    <span class="hljs-keyword">if</span> (instance == <span class="hljs-keyword">null</span>) &#123;
                        instance = <span class="hljs-keyword">new</span> CRouter();
                    &#125;
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> instance;
        &#125;
    &#125;


    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">navigation</span><span class="hljs-params">(String path)</span> </span>&#123;
         startActivity(path);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">startActivity</span><span class="hljs-params">(String path)</span> </span>&#123;
        String classPath
                = mapHolder.get(path);
        <span class="hljs-keyword">if</span> (!TextUtils.isEmpty(classPath)) &#123;
            Intent intent = <span class="hljs-keyword">new</span> Intent();
            intent.setClassName(application, classPath);<span class="hljs-comment">//设置包路径</span>
            ActivityCompat.startActivity(application, intent, <span class="hljs-keyword">null</span>);
        &#125;<span class="hljs-keyword">else</span> &#123;
            Toast.makeText(application, <span class="hljs-string">"路径空啦"</span>, Toast.LENGTH_SHORT).show();
        &#125;
    &#125;


    <span class="hljs-comment">/**
     * 通过指定包名，扫描包下面包含的所有的ClassName
     *
     * <span class="hljs-doctag">@param</span> context     U know
     * <span class="hljs-doctag">@param</span> packageName 包名
     * <span class="hljs-doctag">@return</span> 所有class的集合
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> Set<String> <span class="hljs-title">getFileNameByPackageName</span><span class="hljs-params">(Context context, <span class="hljs-keyword">final</span> String packageName)</span> <span class="hljs-keyword">throws</span> PackageManager.NameNotFoundException, IOException, InterruptedException </span>&#123;
        <span class="hljs-keyword">final</span> Set<String> classNames = <span class="hljs-keyword">new</span> HashSet<>();

        List<String> paths = getSourcePaths(context);
        <span class="hljs-keyword">final</span> CountDownLatch parserCtl = <span class="hljs-keyword">new</span> CountDownLatch(paths.size());

        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> String path : paths) &#123;
            DefaultPoolExecutor.getInstance().execute(<span class="hljs-keyword">new</span> Runnable() &#123;
                <span class="hljs-meta">@Override</span>
                <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
                    DexFile dexfile = <span class="hljs-keyword">null</span>;

                    <span class="hljs-keyword">try</span> &#123;
                        <span class="hljs-keyword">if</span> (path.endsWith(<span class="hljs-string">"EXTRACTED_SUFFIX"</span>)) &#123;
                            <span class="hljs-comment">//NOT use new DexFile(path), because it will throw "permission error in /data/dalvik-cache"</span>
                            dexfile = DexFile.loadDex(path, path + <span class="hljs-string">".tmp"</span>, <span class="hljs-number">0</span>);
                        &#125; <span class="hljs-keyword">else</span> &#123;
                            dexfile = <span class="hljs-keyword">new</span> DexFile(path);
                        &#125;

                        Enumeration<String> dexEntries = dexfile.entries();
                        <span class="hljs-keyword">while</span> (dexEntries.hasMoreElements()) &#123;
                            String className = dexEntries.nextElement();
                            <span class="hljs-keyword">if</span> (className.startsWith(packageName)) &#123;
                                classNames.add(className);
                                <span class="hljs-keyword">try</span> &#123;
                                    Class clazz = Class.forName(className);
                                    Object obj = clazz.newInstance();
                                    Field field03 = clazz.getDeclaredField(<span class="hljs-string">"holder"</span>); <span class="hljs-comment">// 获取属性为id的字段</span>
                                    String value= (String) field03.get(obj);
                                    String[] split = value.split(<span class="hljs-string">":"</span>);
                                    <span class="hljs-keyword">if</span> (split!=<span class="hljs-keyword">null</span>&&split.length==<span class="hljs-number">2</span>) &#123;
                                        mapHolder.put(split[<span class="hljs-number">0</span>],split[<span class="hljs-number">1</span>]);
                                    &#125;
                                    Log.i(<span class="hljs-string">"test-->"</span>,mapHolder.toString());
                                &#125; <span class="hljs-keyword">catch</span> (ClassNotFoundException e) &#123;
                                    e.printStackTrace();
                                &#125; <span class="hljs-keyword">catch</span> (IllegalAccessException e) &#123;
                                    e.printStackTrace();
                                &#125; <span class="hljs-keyword">catch</span> (InstantiationException e) &#123;
                                    e.printStackTrace();
                                &#125; <span class="hljs-keyword">catch</span> (SecurityException e) &#123;
                                    e.printStackTrace();
                                &#125; <span class="hljs-keyword">catch</span> (NoSuchFieldException e) &#123;
                                    e.printStackTrace();
                                &#125; <span class="hljs-keyword">catch</span> (IllegalArgumentException e) &#123;
                                    e.printStackTrace();
                                &#125;
                            &#125;
                        &#125;
                    &#125; <span class="hljs-keyword">catch</span> (Throwable ignore) &#123;
                        Log.e(<span class="hljs-string">"ARouter"</span>, <span class="hljs-string">"Scan map file in dex files made error."</span>, ignore);
                    &#125; <span class="hljs-keyword">finally</span> &#123;
                        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">null</span> != dexfile) &#123;
                            <span class="hljs-keyword">try</span> &#123;
                                dexfile.close();
                            &#125; <span class="hljs-keyword">catch</span> (Throwable ignore) &#123;
                            &#125;
                        &#125;

                        parserCtl.countDown();
                    &#125;
                &#125;
            &#125;);
        &#125;

        parserCtl.await();

        <span class="hljs-keyword">return</span> classNames;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> List<String> <span class="hljs-title">getSourcePaths</span><span class="hljs-params">(Context context)</span> <span class="hljs-keyword">throws</span> PackageManager.NameNotFoundException, IOException </span>&#123;
        ApplicationInfo applicationInfo = context.getPackageManager().getApplicationInfo(context.getPackageName(), <span class="hljs-number">0</span>);
        List<String> sourcePaths = <span class="hljs-keyword">new</span> ArrayList<>();
        sourcePaths.add(applicationInfo.sourceDir); <span class="hljs-comment">//add the default apk path</span>
        <span class="hljs-keyword">return</span> sourcePaths;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">总结</h2>
<ul>
<li>ARouter使用指南</li>
<li>ARouter拦截器</li>
<li>SchemeFilte 实现外部html 跳转Native，打通WEB&Native</li>
<li>了解 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsquare%2Fjavapoet" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/square/javapoet" ref="nofollow noopener noreferrer">JavaPoet</a></strong> &<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fgoogle%2Fauto" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/google/auto" ref="nofollow noopener noreferrer">AutoService 注解处理器</a> apt原理</li>
<li>写出简易版CRouter，通过实战我们了解ARouter实现原理</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FOslanka%2FArouterDemo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Oslanka/ArouterDemo" ref="nofollow noopener noreferrer">项目demo地址</a></li>
</ul>
<h2 data-id="heading-14">问题</h2>
<ul>
<li>除了ARouter，你知道利用apt 实现的框架都有哪些？</li>
<li>ARouter有没有什么缺点？</li>
</ul>
<h2 data-id="heading-15">引用</h2>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2FARouter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/ARouter" ref="nofollow noopener noreferrer">github.com/alibaba/ARo…</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsquare%2Fjavapoet" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/square/javapoet" ref="nofollow noopener noreferrer">github.com/square/java…</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fgoogle%2Fauto" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/google/auto" ref="nofollow noopener noreferrer">github.com/google/auto</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FOslanka%2Fstatichtml.github.io" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Oslanka/statichtml.github.io" ref="nofollow noopener noreferrer">github.com/Oslanka/sta…</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FOslanka%2FArouterDemo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Oslanka/ArouterDemo" ref="nofollow noopener noreferrer">github.com/Oslanka/Aro…</a></p>
</li>
</ul></div>  
</div>
            