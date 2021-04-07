
---
title: 'React Native 引入第三方 Android SDK'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dae28850b2e24bc98a6dd5ed0c2bc189~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 02:30:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dae28850b2e24bc98a6dd5ed0c2bc189~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>大家好，我是 <a href="https://github.com/youngjuning" target="_blank" rel="nofollow noopener noreferrer">@洛竹</a></p>
<p>本文首发于 <a href="https://youngjuning.js.org/" target="_blank" rel="nofollow noopener noreferrer">洛竹的官方网站</a></p>
<p>本文同步于公众号『洛竹早茶馆』，转载请联系作者。</p>
<p>创作不易，养成习惯，素质三连！</p>
</blockquote>
<p>在 React Native 开发中，如果一个原生 SDK 没有适配 React Native 的插件，原则上我们不推荐你使用。但是万不得已的情况下，我们有办法吗？答案是肯定的。步骤大致分为集成 SDK、编写桥接代码。知难行易，本文就是顺着这个思路来解决让前端工程师脑壳疼的集成第三方 SDK 并编写桥接代码的问题。</p>
<h2 data-id="heading-0">预备知识</h2>
<p>在我们开发安卓项目的时候，不会所有的功能都自己去造轮子，经常要使用到各种的其他包，其中有谷歌给我们提供的各种 <code>support</code> 包，也有各种第三方的功能库，有时候我们自己也会将一些功能封装成包。这些包存在和导入的形式也多种多样，有远程仓库的，有直接拷贝到本地的，<code>jar</code> 包、<code>aar</code> 包、<code>so</code> 包等。所幸我们都可以在主工程和各个 <code>Module</code> 的 <code>build.gradle</code> 里进行统一管理。— <a href="http://t.cn/Ai9T02Jq" target="_blank" rel="nofollow noopener noreferrer">Android 依赖导入全攻略</a></p>
<h3 data-id="heading-1">依赖引入方式</h3>
<p><code>Android Gradle plugin 3.0</code> 几个引入依赖的方法：</p>
<p><strong>implementation</strong></p>
<p>对于使用了该命令编译的依赖，对该项目有依赖的项目将无法访问到使用该命令编译的依赖中的任何程序，也就是将该依赖隐藏在内部，而不对外部公开。<code>react-native link</code> 命令即使用该方式</p>
<p>使用 <code>implementation</code> 会使编译速度有所增快：比如我在一个 <code>library</code> 中使用 <code>implementation</code> 依赖了 <code>gson</code> 库，然后我的主项目依赖了 <code>library</code>，那么，我的主项目就无法访问 <code>gson</code> 库中的方法。这样的好处是编译速度会加快，我换了一个版本的 <code>Gson</code> 库，但只要 <code>library</code> 的代码不改动，就不会重新编译主项目的代码。</p>
<p><strong>api</strong></p>
<p>等同于 compile 指令</p>
<p><strong>compileOnly</strong></p>
<p>等同于 <code>provided</code>，只在编译时有效，不会参与打包，不会包含到 <code>apk</code> 文件中。可以用来解决重复导入库的冲突。</p>
<h2 data-id="heading-2">远程仓库依赖</h2>
<blockquote>
<p>这里我们以 LeanCloud Android SDK 的引入来演示</p>
</blockquote>
<p>引入远程仓库依赖是很方便的，但在之前我们需要在项目根目录的 <code>build.gradle</code> 声明远程仓库的地址。</p>
<pre><code class="hljs language-diff copyable" lang="diff">buildscript &#123;
    repositories &#123;
        jcenter()
<span class="hljs-addition">+        //这里是 LeanCloud 的包仓库</span>
<span class="hljs-addition">+        maven &#123;</span>
<span class="hljs-addition">+            url "http://mvn.leancloud.cn/nexus/content/repositories/public"</span>
<span class="hljs-addition">+        &#125;</span>

    &#125;
    dependencies &#123;
        classpath 'com.android.tools.build:gradle:1.0.0'
    &#125;
&#125;

allprojects &#123;
    repositories &#123;
        jcenter()
<span class="hljs-addition">+        //这里是 LeanCloud 的包仓库</span>
<span class="hljs-addition">+        maven &#123;</span>
<span class="hljs-addition">+            url "http://mvn.leancloud.cn/nexus/content/repositories/public"</span>
<span class="hljs-addition">+        &#125;</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后打开 <code>app</code> 目录下的 <code>build.gradle</code> 进行如下配置：</p>
<pre><code class="hljs language-diff copyable" lang="diff">android &#123;
<span class="hljs-addition">+    //为了解决部分第三方库重复打包了META-INF的问题</span>
<span class="hljs-addition">+    packagingOptions&#123;</span>
<span class="hljs-addition">+        exclude 'META-INF/LICENSE.txt'</span>
<span class="hljs-addition">+        exclude 'META-INF/NOTICE.txt'</span>
<span class="hljs-addition">+    &#125;</span>
    lintOptions &#123;
        abortOnError false
    &#125;
&#125;

dependencies &#123;
    compile ('com.android.support:support-v4:21.0.3')

<span class="hljs-addition">+    // LeanCloud 基础包</span>
<span class="hljs-addition">+    compile ('cn.leancloud.android:avoscloud-sdk:4.7.10')</span>
<span class="hljs-addition">+</span>
<span class="hljs-addition">+    // 推送与即时通讯需要的包</span>
<span class="hljs-addition">+    compile ('cn.leancloud.android:avoscloud-push:4.7.10@aar')&#123;transitive = true&#125;</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">本地依赖</h2>
<blockquote>
<p>使用 Android Studio 的同学请参考: <a href="http://t.cn/Ai9TFsHH" target="_blank" rel="nofollow noopener noreferrer">Android Studio 引入 jar 包和 so 文件（armeabi 和 armeabi-v7a）</a></p>
</blockquote>
<h3 data-id="heading-4">jar 包</h3>
<p>1、将 <code>jar</code> 文件复制、粘贴到 <code>app/libs</code> 目录中，React Native 默认没有该文件夹，清新建一个</p>
<p>2、打开 <code>app/build.gradle</code>，进行如下配置以列出包含 <code>jar</code> 包的文件夹路径。</p>
<blockquote>
<p>注意：React Native 默认已经进行了这个配置</p>
</blockquote>
<pre><code class="hljs language-diff copyable" lang="diff">dependencies &#123;
    implementation fileTree(dir: "libs", include: ["*.jar"])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和远程仓库依赖引入方式不同，如果本地同时存在两个不同的 <code>jar</code> 包，或者本地已有 <code>jar</code> 包，再去远程依赖不同版本的 <code>jar</code> 包，就会报错。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dae28850b2e24bc98a6dd5ed0c2bc189~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>解决方式：将其中的一个采用 <code>compileOnly</code> 替换 <code>implementation</code>。顾名思义，<code>compileOnly</code> 只在编译时起作用，不会包含到 <code>APK</code> 里面，在运行时也就避免找到重复的类了。</p>
<h3 data-id="heading-5">aar 包</h3>
<p><code>arr</code> 全称是 <code>Andorid Archive</code>,是一个 Android 库项目的二进制归档文件，使用 Android Studio ，非常简单可以生成一个 AAR 文件。</p>
<p>和 <code>jar</code> 包不同，<code>aar</code> 包存放的路径声明和依赖引入是分开的：</p>
<p>1、将 <code>aar</code> 包复制到 <code>lib</code> 目录下</p>
<p>2、在项目根目录 <code>build.gradle</code>中声明 <code>aar</code> 文件存放路径</p>
<pre><code class="hljs language-diff copyable" lang="diff">buildscript &#123;
  repositories &#123;
<span class="hljs-addition">+    flatDir &#123; // 引用本项目的libs下的aar</span>
<span class="hljs-addition">+      dir "$rootDir/libs"</span>
<span class="hljs-addition">+    &#125;</span>
  &#125;
&#125;
allprojects &#123;
  repositories &#123;
<span class="hljs-addition">+    flatDir &#123; // 引用本项目的libs下的aar</span>
<span class="hljs-addition">+      dir "$rootDir/libs"</span>
<span class="hljs-addition">+    &#125;</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、在 <code>app/build.gradle</code> 中注入依赖</p>
<blockquote>
<p>注意：远程 <code>aar</code> 引入形式是：<code>implementation('com.sishu.android:watermelondb:0.7.0@aar')</code></p>
</blockquote>
<pre><code class="hljs language-diff copyable" lang="diff">dependencies &#123;
<span class="hljs-addition">+    implementation(name: 'aar名字', ext: 'aar')</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">so 文件</h3>
<p>直接在 <code>src->main</code> 下新建一个文件夹 <code>jniLib</code> ，然后再把 <code>so</code> 文件所在的那个文件夹 <code>armeabi</code> 复制过去。</p>
<blockquote>
<p>注：<code>jniLib</code> 是 so 文件默认的放置目录</p>
</blockquote>
<h2 data-id="heading-7">坑</h2>
<h3 data-id="heading-8">都是 Proguard 惹的祸</h3>
<p>有时候明明导入了 <code>jar</code> 包，却仍然找不到 <code>jar</code> 包中的方法呢？八成是因为你开启了混淆，最安全的就是空间换安全。但是一个较真的程序员不能满足于此，我们还是要搞清楚 Proguard 惹了什么祸的。这里分享给大家一招：</p>
<p>打开 Android Studio 像原生开发工程师一样使用 Logcat 查看应用日志，比如你找到是 <code>com.huawei.**</code> 这个库找不到，那么进行如下配置：</p>
<pre><code class="hljs language-diff copyable" lang="diff"><span class="hljs-addition">+ -dontwarn com.huawei.**</span>
<span class="hljs-addition">+ -keep class com.huawei.**&#123;*;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>-dontwarn</code> 表示让 ProGuard 不要警告找不到 <code>com.huawei.**</code> 这个包里面的类的相关引用</li>
<li><code>-keep class</code> 表示保持 <code>com.huawei.**</code> 这个包里面的所有类和所有方法不被混淆。再次编译打包，发现 apk 大小要明显大于之前的包。运行 app，问题解决！</li>
</ul>
<h3 data-id="heading-9">aar 包中的资源文件重复了</h3>
<p>资源文件重复了，主工程的资源文件会直接覆盖 <code>aar</code> 包中的文件，并且不会有任何报错或者提示，最终 <code>aar</code> 包中也会直接用主工程的资源文件，所以需要注意命名方式。暂时没有更好的解决方法。</p>
<h3 data-id="heading-10">AndroidManifest 合并错误</h3>
<p>同样也是发生在 <code>aar</code> 包上， Android Studio 项目每个 module 中都可以有一个 <code>AndroidManifest.xml</code> 文件，但最终的 APK 文件只能包含一个 <code>AndroidManifest.xml</code> 文件。在构建应用时，Gradle 构建会将所有清单文件合并到一个封装到 APK 的清单文件中。aar 包的清单文件和我们的 app 清单文件属性冲突时：用 <code>tools:replace="属性名"</code> 解决。</p>
<h3 data-id="heading-11">annotationProcessor 与 compileOnly 的区别</h3>
<p>上文说了 <code>annotationProcessor</code> 与 <code>compileOnly</code> 都是只编译并不打入 apk 中，他俩到底有什么区别呢？扮演的角色不一样，<code>annotationProcessor</code> 作用是编译时生成代码，编译完真的就不需要了，<code>compileOnly</code> 是有重复的库，为的是剃除只保留一个库，最终还是需要的。</p>
<h2 data-id="heading-12">参考</h2>
<ul>
<li><a href="http://t.cn/Ai9HmlWb" target="_blank" rel="nofollow noopener noreferrer">Android Studio 引入 jar 包和 so 库</a></li>
<li><a href="http://t.cn/Ai9T02Jq" target="_blank" rel="nofollow noopener noreferrer">Android 依赖导入全攻略</a></li>
<li><a href="http://t.cn/Ai98bNbj" target="_blank" rel="nofollow noopener noreferrer">React-native 使用原生(ios, android)第三方 sdk</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            