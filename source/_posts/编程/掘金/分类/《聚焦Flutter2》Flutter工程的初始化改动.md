
---
title: '《聚焦Flutter.2》Flutter工程的初始化改动'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2519'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 07:01:24 GMT
thumbnail: 'https://picsum.photos/400/300?random=2519'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0"><span>前言</span></h1>
<blockquote>
<p>本文以创建名为“focus_flutter”的项目为例。</p>
</blockquote>
<p>本文是在用Android Studio创建Flutter工程后，进行了一些初始配置的修改：</p>
<ol>
<li>创建项目，并为项目初始化git仓库；</li>
<li>android模块：修改包名，创建签名，修改release编译配置；</li>
<li>ios模块：修改包名，添加开发者信息；</li>
<li>修改.gitignore，保存一些重要文件，丢弃一些冗余文件；</li>
<li>提交所有修改；</li>
</ol>
<p>本文创建Flutter项目的基础环境版本信息如下：</p>
<blockquote>
<p>2021-06-04</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">Flutter version: 2.2.1
Dart version: 2.13.1
Android studio version: 4.2.1
Flutter plugin version: 57.0.2
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1"><span>项目初建</span></h1>
<p>Android Studio 创建 flutter 应用, 放到 focus_flutter 目录下，并初始化git仓库。</p>
<ol>
<li>确定项目的创建信息，创建项目；</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 项目的创建信息</span>
工程名：focus_flutter
包名：com.focus
平台配置：
1.android：
    默认使用androidx*
    默认编程语言kotlin
2.ios:
    默认编程语言swift
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>初始化git仓库。</li>
<li>修改工程根目录和android目录下的.gitignore文件，保留<code>*.iml</code>配置文件。iml是工程的组织文件，最好保留。</li>
</ol>
<h1 data-id="heading-2"><span>Android模块基础配置修改</span></h1>
<ol>
<li>使用Android Studio打开Flutter工程的android模块：</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">project->flutter->open android module <span class="hljs-keyword">in</span> android studio
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>编译android/app，确定是否可以编译通过。注意，ndk没装匹配的版本可能导致编译不过。</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">flutter<span class="hljs-string">'2.2.1'</span>创建的工程，Android需要安装ndk<span class="hljs-string">'21.1.6352462'</span>，否则单独编译<span class="hljs-string">"project/android"</span>模块会报错;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>修改android模块目录下的.gitignore文件，保留iml配置文件，iml是工程的组织，保留后，可以在Android Studio的flutter项目状态下，右键菜单中直接选择在新窗口中打开android模块。</li>
<li>修改自己喜欢的包名：</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">1. 修改 AndroidManifest.xml 文件包名的配置为：<span class="hljs-string">"com.focus.flutter"</span>.
2. 修改 <span class="hljs-string">"project/android/app/build.gradle"</span> 内的applicationId为：<span class="hljs-string">"com.focus.flutter"</span>.
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>kotlin和gradle版本以官方初始demo为准, 否则release打包时会有一些问题。</li>
<li>为应用创建jks秘钥文件：</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 1. 先确定秘钥信息如下：</span>
keystore password: focus1024
<span class="hljs-built_in">alias</span>: focus_flutter
key password: focus2048
validity(years): 100
first and last name(姓名): thlllzq
organizational unit(组织): focus
organization：focus
city and locality(城市和地区)：shanghai
state or province(州或省)：shanghai
country code(国家代码): CHN

<span class="hljs-comment"># 2. 再通过命令行创建秘钥，放到“project/app/”目录下;</span>
$ <span class="hljs-comment"># 输入以下keytool命令生成jks秘钥，并按提示填写额外的配置信息，最后以Y结束。</span>
$ keytool -genkey -v -keystore keystore.jks -keyalg RSA -keysize 2048 -validity 36500 -<span class="hljs-built_in">alias</span> focus_flutter -storepass focus1024 -keypass focus2048

<span class="hljs-comment"># 3. 创建秘钥属性文件，方便在build.gradle配置中引用；</span>
<span class="hljs-comment"># key.properties</span>
--------------------
storePassword=focus1024
keyPassword=focus2048
keyAlias=focus_flutter
storeFile=keystore.jks
--------------------
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li><code>android/app/build.gradle</code> 文件中配置打包信息；</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 在app/build.gradle文件中配置release签名和编译类型</span>
<span class="hljs-comment"># build.gradle</span>
--------------------
<span class="hljs-comment"># 在android&#123;&#125;配置信息前，加载keystore.jks的配置信息</span>
def keystoreProperties = new Properties()
def keystorePropertiesFile = rootProject.file(<span class="hljs-string">'app/key.properties'</span>)
<span class="hljs-keyword">if</span> (keystorePropertiesFile.exists()) &#123;
    keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
&#125;
...
android &#123;
    signingConfigs &#123;
        <span class="hljs-comment"># 读取秘钥配置文件中的签名秘钥</span>
        release &#123;
            keyAlias keystoreProperties[<span class="hljs-string">'keyAlias'</span>]
            keyPassword keystoreProperties[<span class="hljs-string">'keyPassword'</span>]
            storeFile keystoreProperties[<span class="hljs-string">'storeFile'</span>] ? file(keystoreProperties[<span class="hljs-string">'storeFile'</span>]) : null
            storePassword keystoreProperties[<span class="hljs-string">'storePassword'</span>]
        &#125;
    &#125;
    buildTypes &#123;
        release &#123;
            signingConfig signingConfigs.release
        &#125;
    &#125;
&#125;
--------------------
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>测试打包；</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># “flutter build”默认打release包,是包含所有目标ABI编译代码的胖apk,初始项目打包大小为15.4MB.</span>
$ flutter build apk
<span class="hljs-comment"># “--split-per-abi”设置按不同目标ABI分别打包,不同ABI的包更小。</span>
$ flutter build apk --split-per-abi
<span class="hljs-comment"># 分包打包，包含如下几个类型apk，初始项目打包，单个包大小约为5MB.</span>
[project]/build/app/outputs/apk/release/app-armeabi-v7a-release.apk
[project]/build/app/outputs/apk/release/app-arm64-v8a-release.apk
[project]/build/app/outputs/apk/release/app-x86_64-release.apk
<span class="hljs-comment"># 指定ABI架构打包</span>
$ flutter build apk --target-platform android-arm
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="9">
<li>安装apk到设备；</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">$ flutter install
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3"><span>iOS模块基础配置修改</span></h1>
<blockquote>
<p>Flutter 支持 iOS 8.0+</p>
</blockquote>
<ol>
<li>使用Xcode打开Flutter工程的ios模块：</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">project->flutter->open iOS module <span class="hljs-keyword">in</span> Xcode
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>iOS模块修改包名和应用名，添加开发者信息：</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">1. 在Xcode中,打开App的iOS目录中的 Runner.xcworkspace。
2. 在Xcode的项目导航栏中选择Runner,在Runner配置窗口来配置App的属性信息：
-----------------------
<span class="hljs-comment"># 修改包名和应用名称</span>
->[General]
    Display Name: 应用名称
    Bundle Identifier: App ID
->[Info]
Bundle name：应用名

<span class="hljs-comment"># 添加开发者账号信息</span>
->[Signing & Capabilities]
    Team: Apple开发者账号
-----------------------
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>设置信任开发者，并运行app;</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">1. 连接iPhone手机，手机会提示信任连接的设备；
2. 安装应用：输入命令“flutter run”即可将应用安装到iPhone设备。
3. 安装信任问题：第一次安装到手机无法打开，会提示到设置里设置信任后再运行!!!
-----------------------
<span class="hljs-comment"># 设置信任开发者</span>
iPhone设置信任：设置->通用->设备管理->选择信任的开发者；
-----------------------
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4"><span>提交工程git</span></h1>
<ol>
<li>修改根目录下的.gitignore文件；</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># .gitignore</span>
<span class="hljs-comment"># 1.提交.iml工程组织文件到git仓库；</span>
<span class="hljs-comment">#*.iml</span>
<span class="hljs-comment"># 2.忽略 pubspec.lock 文件,该文件是依赖项下载缓存配置文件，可自动生成，不需要提交。</span>
pubspec.lock
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>修改android目录下的.gitignore文件；</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 需要提交的一些必要文件</span>
-----------------------
<span class="hljs-comment">#gradle-wrapper.jar</span>
<span class="hljs-comment">#/gradlew</span>
<span class="hljs-comment">#/gradlew.bat</span>
<span class="hljs-comment">#GeneratedPluginRegistrant.java</span>
-----------------------
<span class="hljs-comment"># iml文件是模块的组织文件，需要提交，保留此文件，可以直接在flutter工程状态下直接选择用Android Studio打开android模块；</span>
-----------------------
<span class="hljs-comment">#*.iml</span>
-----------------------
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>提交所有更改到git仓库。</li>
</ol></div>  
</div>
            