
---
title: '移动应用遗留系统重构（16）- Gradle依赖管理篇'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54b9a3555f03484b80e32cbc232005d1~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 04:33:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54b9a3555f03484b80e32cbc232005d1~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>上一篇<a href="https://juejin.cn/post/6979198588630859806" target="_blank">移动应用遗留系统重构（15）- 数据库重构示例篇</a>我们提到CloudDisk团队已经拆分成了多仓库开发，但各个模块各自维护了第三方库。这样除了版本不统一、也导致打包构建时会带入多个版本的三方库。</p>
<p>由于目前各业务模块已经分仓开发，我们无法使用ext.的声明，统一版本号及定义库别名。我们只能以Gradle插件的形式发布到Maven库中，这样所有其他模块就可以直接apply使用。</p>
<h1 data-id="heading-1">CloudDisk Gradle 插件改造</h1>
<h2 data-id="heading-2">Gradle 插件</h2>
<ol>
<li>创建buildSrc模块</li>
<li>创建BasePlugin类及LibPluginExtension</li>
<li>创建resource/META-INF/gradle-plugin/com.cloud.disk.plugin.properties,声明class</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java">implementation-<span class="hljs-class"><span class="hljs-keyword">class</span></span>=com.cloud.disk.plugin.BasePlugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.发布插件，在使用的工程apply</p>
<pre><code class="hljs language-java copyable" lang="java">apply plugin: <span class="hljs-string">'com.cloud.disk.plugin'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>BasePlugin类如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BasePlugin</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Plugin</span><<span class="hljs-title">Project</span>> </span>&#123;

    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Project mProject

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">apply</span><span class="hljs-params">(Project project)</span> </span>&#123;
        mProject=project
        project.extensions.create(<span class="hljs-string">"Lib"</span>, LibPluginExtension.class)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>LibPluginExtension类如下,部分代码省略：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LibPluginExtension</span> </span>&#123;
    String roomVersion = <span class="hljs-string">'2.2.6'</span>
    String lifeCycleVersion = <span class="hljs-string">'2.3.0'</span>
    String hiltVersion = <span class="hljs-string">'2.31.2-alpha'</span>
    <span class="hljs-comment">//... ...</span>

    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">test</span><span class="hljs-params">()</span> </span>&#123;
        BasePlugin.mProject.dependencies &#123;
            testImplementation <span class="hljs-string">"junit:junit:$junitVersion"</span>
            testImplementation <span class="hljs-string">"org.mockito:mockito-inline:$mockitoVersion"</span>
            testImplementation <span class="hljs-string">"android.arch.core:core-testing:1.1.1"</span>
            testImplementation <span class="hljs-string">"com.google.truth:truth:1.0.1"</span>
            testImplementation <span class="hljs-string">'com.tngtech.archunit:archunit-junit4:0.15.0'</span>
            testImplementation <span class="hljs-string">"org.robolectric:robolectric:$robolectricVersion"</span>
            testImplementation <span class="hljs-string">'androidx.test:core:1.3.0'</span>
            testImplementation <span class="hljs-string">'androidx.test.ext:junit:1.1.2'</span>
            testImplementation <span class="hljs-string">"androidx.test.espresso:espresso-core:$espressoVersion"</span>
            testImplementation <span class="hljs-string">"androidx.test.espresso:espresso-intents:$espressoVersion"</span>
            debugImplementation <span class="hljs-string">"androidx.fragment:fragment-testing:1.3.1"</span>
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">room</span><span class="hljs-params">()</span> </span>&#123;
        BasePlugin.mProject.dependencies &#123;
            implementation <span class="hljs-string">"androidx.room:room-runtime:$roomVersion"</span>
            implementation <span class="hljs-string">"androidx.room:room-ktx:$roomVersion"</span>
            kapt <span class="hljs-string">"androidx.room:room-compiler:$roomVersion"</span>
            testImplementation <span class="hljs-string">"androidx.room:room-testing:$roomVersion"</span>
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">coroutines</span><span class="hljs-params">()</span> </span>&#123;
        BasePlugin.mProject.dependencies &#123;
            implementation <span class="hljs-string">"org.jetbrains.kotlinx:kotlinx-coroutines-core:$coroutinesVersion"</span>
            implementation <span class="hljs-string">"org.jetbrains.kotlinx:kotlinx-coroutines-android:$coroutinesVersion"</span>
            testImplementation <span class="hljs-string">"org.jetbrains.kotlinx:kotlinx-coroutines-test:1.3.3"</span>
        &#125;
    &#125;

     
    <span class="hljs-comment">// ... ...</span>

   
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">CloudDisk 改造</h2>
<ol>
<li>dynamicBundle模块修改如下：</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java">dependencies &#123;
    implementation <span class="hljs-string">'com.cloud.disk:api:1.0.0'</span>
    implementation <span class="hljs-string">'com.cloud.disk:library:1.0.0'</span>
    implementation <span class="hljs-string">'com.cloud.disk:platform:1.0.0'</span>

    project.Lib.kotlin()
    project.Lib.supportV4()
    project.Lib.appCompact()
    project.Lib.material()
    project.Lib.router()
    project.Lib.mvvm()
    project.Lib.ktx()
    project.Lib.coroutines()
    project.Lib.room()
    project.Lib.hilt()
    project.Lib.test()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>dynamicDebug模块修改如下：</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java">dependencies &#123;
    implementation <span class="hljs-string">'com.cloud.disk:api:1.0.0'</span>
    <span class="hljs-function">implementation <span class="hljs-title">project</span><span class="hljs-params">(<span class="hljs-string">':dynamicBundle'</span>)</span>

    project.Lib.<span class="hljs-title">hilt</span><span class="hljs-params">()</span>
    project.Lib.<span class="hljs-title">test</span><span class="hljs-params">()</span>
    project.Lib.<span class="hljs-title">appCompact</span><span class="hljs-params">()</span>
    project.Lib.<span class="hljs-title">material</span><span class="hljs-params">()</span>
    project.Lib.<span class="hljs-title">constraintlayout</span><span class="hljs-params">()</span>
    project.Lib.<span class="hljs-title">kotlin</span><span class="hljs-params">()</span>
    project.Lib.<span class="hljs-title">ktx</span><span class="hljs-params">()</span>
&#125;

</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>完整修改见<a href="https://github.com/junbin1011/CloudDisk/commit/8e1b7a8c228ecad2b6a1b14deba824cfe9cd80e4" target="_blank" rel="nofollow noopener noreferrer">Github</a></p>
<h1 data-id="heading-4">总结</h1>
<p>本篇主要分享了 CloudDisk Gradle 插件改造，包含统一的三方库的版本管理及如何简化依赖调用，有效的解决了三方库版本不统一问题。</p>
<p>随着重构工作的持续，各个模块已经补充了足量的自动化测试，但CloudDisk团队目前的CI只提供打包的功能，供测试团队进行验证。分仓以后也没有对独立模块仓库建立流水线，测试团队还是只能在最后做集成的验收。</p>
<p>下一篇，移动应用遗留系统重构（17）- 流水线设计篇。我们将重新对CloudDisk进行流水线的设计，包含质量门禁检查及根据单个模块、APP集成，制定对应的策略。</p>
<h1 data-id="heading-5">CloudDisk示例代码</h1>
<p><a href="https://github.com/junbin1011/CloudDisk" target="_blank" rel="nofollow noopener noreferrer">CloudDisk</a></p>
<h1 data-id="heading-6">系列链接</h1>
<p><a href="https://juejin.cn/post/6943470229905211422" target="_blank">移动应用遗留系统重构（1）- 开篇</a></p>
<p><a href="https://juejin.cn/post/6945313969556946980" target="_blank">移动应用遗留系统重构（2）-架构篇</a></p>
<p><a href="https://juejin.cn/post/6947855094272491556" target="_blank">移动应用遗留系统重构（3）-示例篇</a></p>
<p><a href="https://juejin.cn/post/6950077521790500894" target="_blank">移动应用遗留系统重构（4）-分析篇</a></p>
<p><a href="https://juejin.cn/post/6952298178095874055" target="_blank">移动应用遗留系统重构（5）- 重构方法篇</a></p>
<p><a href="https://juejin.cn/post/6954635678982340622" target="_blank">移动应用遗留系统重构（6）- 测试篇</a></p>
<p><a href="https://juejin.cn/post/6959504791642832909" target="_blank">移动应用遗留系统重构（7）- 解耦重构演示篇(一)+视频演示</a></p>
<p><a href="https://juejin.cn/post/6963214120178941983" target="_blank">移动应用遗留系统重构（8）- 依赖注入篇</a></p>
<p><a href="https://juejin.cn/post/6966166367821103117" target="_blank">移动应用遗留系统重构（9）- 路由篇</a></p>
<p><a href="https://juejin.cn/post/6970870458660945934" target="_blank">移动应用遗留系统重构（10）- 解耦重构演示篇（二）</a></p>
<p><a href="https://juejin.cn/post/6973836199655899149" target="_blank">移动应用遗留系统重构（11）- 制品管理篇</a></p>
<p><a href="https://juejin.cn/post/6974634615537401886" target="_blank">移动应用遗留系统重构（12）- 编译调试篇</a></p>
<p><a href="https://juejin.cn/post/6975877150314332168" target="_blank">移动应用遗留系统重构（13）- 编译调试篇</a></p>
<p><a href="https://juejin.cn/post/6975877150314332168" target="_blank">移动应用遗留系统重构（13）- 编译调试篇</a></p>
<p><a href="https://juejin.cn/post/6977702335879315493" target="_blank">移动应用遗留系统重构（14）- Kotlin+MVVM重构示例篇</a></p>
<p><a href="https://juejin.cn/post/6979198588630859806" target="_blank">移动应用遗留系统重构（15）- 数据库重构示例篇</a></p>
<h1 data-id="heading-7">大纲</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54b9a3555f03484b80e32cbc232005d1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">关于</h1>
<ul>
<li>作者：黄俊彬</li>
<li><a href="https://junbin.tech/" target="_blank" rel="nofollow noopener noreferrer">博客：junbin.tech</a></li>
<li><a href="https://github.com/junbin1011" target="_blank" rel="nofollow noopener noreferrer">GitHub: junbin1011 </a></li>
<li><a href="https://www.zhihu.com/people/junbin-9-77" target="_blank" rel="nofollow noopener noreferrer">知乎: @JunBin</a></li>
</ul></div>  
</div>
            