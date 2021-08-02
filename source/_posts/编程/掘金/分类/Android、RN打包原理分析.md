
---
title: 'Android、RN打包原理分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5adedb675fc47b9a08f45885b017ea7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 00:20:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5adedb675fc47b9a08f45885b017ea7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">目录：</h2>
<p><strong>Android打包原理</strong></p>
<p><a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">Android apk文件夹目录结构</a></p>
<p><a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">Android打包脚本gradle执行流程流程</a></p>
<p><a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">App安装流程</a></p>
<p><strong>RN打包原理</strong></p>
<p><a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">RN bundle文件结构</a></p>
<p><a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">metro打包流程</a></p>
<p><a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">RN拆包原理</a></p>
<p><strong>Android、RN打包比较</strong></p>
<p><a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">Android、RN打包比较</a></p>
<p>在分析一件事物原理的时候我喜欢从结果开始逆向推理过程，这样更容易理解</p>
<h2 data-id="heading-1">Android打包原理</h2>
<h3 data-id="heading-2">Android apk文件夹目录结构</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5adedb675fc47b9a08f45885b017ea7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d63824919ee147e5aa954228a47f2753~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>无图无真相，通过AS或者解压打包好的apk目录如上图</p>
<p><strong>lib</strong></p>
<p>lib目录下存放的是底层代码C/C++编译出来的so文件，如音视频、人脸识别等，其中x86、arm代表兼容不同的芯片类型。</p>
<p>由于java性能有限，很多对性能要求比较高的功能都需要通过C/C++实现，so同样增强了app的安全性，不容易被反编译。</p>
<p>so库由于无法被压缩是整个apk包体积中占比最大的，很多app只兼容armev7来减少包大小（google play开放了bundle功能，可根据用户手机选择下载对应型号的app），也有通过动态下发部分功能不是很重要的so库来达到优化包大小的目的。</p>
<p><strong>res</strong></p>
<p>Android的资源文件目录，包含布局、动画</p>
<p><strong>assets</strong></p>
<p>这里保存的是打包过程不能被压缩需要保留的原始文件，比如字体文件，RN的本地bundle文件也经常放这里。</p>
<p><strong>dex文件</strong></p>
<p>.dex文件是Android系统运行在Dalvik Virtual Machine上的可执行文件，也是Android爱普的核心。项目的Java源码通过javac生成class文件，在通过dx工具生成为classes.dex文件。</p>
<p><strong>AndroidManifest.xml</strong></p>
<p>这个文件可以意为清单文件或者全局配置文件。里面有很多应用的配置信息，权限、版本号、四大组件的注册也在其中。</p>
<p><strong>META-INF文件夹</strong></p>
<p>该目录主要作用就是用于保证APK的完整性和安全性。主要有三个文件：</p>
<p>MANIFEST.MF：保存了整个apk文件中所有文件的文件名+SHA-1后的base64编码值。象征着apk的完整性。</p>
<p>CERT.RSA：保存了公匙和加密方式的信息。</p>
<p>CERT.SF：这个文件与MANIFEST.MF的结构一样，只是其编码会被私匙加密。每次安装时，通过该文件夹中的文件，就可以完成验证的过程。如果apk包被改变了，而篡改者没有私匙生成的CERT.SF，则无法完成校验。</p>
<p><strong>resource.arsc文件</strong></p>
<p>该文件是所有文件中结构最复杂的。</p>
<p>它记录了资源文件，资源文件位置和资源id的映射关系。并且将所有的string都存放在了string pool中，节省了在查找资源时，字符串处理的开销。</p>
<h3 data-id="heading-3">Android打包脚本gradle执行流程流程</h3>
<p>先借用一张官方Android打包图镇楼</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31100d5fd443430cbc9e47f9e7105c30~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示：</p>
<p><strong>1.打包资源文件，生成R.java文件</strong></p>
<p>R.java是资源文件引用的一个映射,没一个资源都会在编译的过程中生成一个唯一id</p>
<p>打包资源文件的工具是aapt(The Android Asset Packing Tool)，位于android-sdk/platform-tools目录下。
在这个过程中，项目中的AndroidManifest.xml文件和布局文件xml都会编译生成相应的R.java。</p>
<p>同时还有编译生成resources.arsc和uncompiled res文件（二进制文件 & 非二进制文件） <br>
非二进制文件（eg：res/raw、res/pic）保持原样。</p>
<p>assets资源文件内容保持原样。</p>
<p><strong>2.处理AIDL文件，生成相应的java文件</strong></p>
<p>这个过程使用的工具是aidl（Android Interface Definition Language），位于android-sdk/platform-tools目录下。</p>
<pre><code class="copyable">aidl工具解析接口定义文件，然后生成相应的java接口，供程序调用。
如果项目中没有使用到aidl文件，那么这个过程可以跳过。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.编译项目源代码，生成.class文件</strong></p>
<p>项目中所有的java文件，包括R.java文件和**.aidl文件，都会被java编译器（Java Compiler）编译成.class文件。</p>
<pre><code class="copyable">生成的class文件位于工程中的bin/classes目录下。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.转换所有的class文件，生成classes.dex文件</strong></p>
<p>这个过程使用的工具是dx，该工具位于android-sdk/platform-tools。</p>
<p>该工具可以生成供Android系统虚拟机的执行文件 classes.dex。</p>
<p>dx工具主要工作就是将java字节码转换成Dalvik字节码、压缩常量池以及消除冗余信息等。</p>
<p>任何第三方的lib和.class文件都会被转换成.dex文件</p>
<p><strong>5.打包生成Apk文件</strong></p>
<p>所有没有编译过的资源（eg： images）、编译过的资源和.dex文件都会被 apkbuilder 工具打包到最终的.apk文件中去。</p>
<pre><code class="copyable">打包工具apkbuilder位于android-sdk/tools目录下。

apkbuilder实际上是一个脚本文件，调用的是android-sdk/tools/lib/sdklib.jar文件中的 com.android.sdklib.build.ApkbuilderMainl类。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.对Apk文件签名</strong></p>
<p>apk文件只有被签名才能被安装在设备上。</p>
<p>签名文件(keystore)有2种</p>
<pre><code class="copyable"> 一种是用于调试的 debug.keystore，开发工具中Run以后在设备上运行的Apk就是debug.keystore签名，在Android sdk中可以找到，是固定的
 一种是用于发布正式版本的keystore，属于开发自行创建申请的证书，起到防止app被冒名顶替的作用
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.对签名后的文件进行对齐处理</strong></p>
<p>在生成最终 APK 之前，打包器会使用 zipalign 工具对应用进行优化，位于android-sdk/tools目录下。</p>
<pre><code class="copyable">对齐的主要过程是：

> 将Apk包中的所有资源文件距离文件起始位置偏移4字节整数倍。
> 对齐之后可以减少运行时内存的使用。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">App安装流程</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f711c2e8592480191a12c80e72b8f1d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>复制APK到/data/app目录下，解压并扫描安装包。</li>
<li>资源管理器解析APK里的资源文件。</li>
<li>解析AndroidManifest文件，并在/data/data/目录下创建对应的应用数据目录。</li>
<li>然后对dex文件进行优化，并保存在dalvik-cache目录下。</li>
<li>将AndroidManifest文件解析出的四大组件信息注册到PackageManagerService中。</li>
<li>安装完成后，发送广播。</li>
</ol>
<h2 data-id="heading-5">RN打包原理</h2>
<h3 data-id="heading-6">RN bundle文件结构</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f194cf3caaaf45c897132c2ba1271093~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2e9331acccd431284d6d64c7bb0ce16~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图，生成的bundle大致分为四层</p>
<p><strong>var层</strong></p>
<p>包含了当前进程，当前运行环境，bundle启动时间等</p>
<p><strong>polyfill层</strong></p>
<p>文件中!(function(r)开头的部分代表的是polyfill层，定义了对 <code>define（__d）</code>、 <code>require（__r）</code>、<code>clear（__c）</code> 的支持，以及 module（react-native 及第三方 dependences 依赖的 module） 的加载逻辑;</p>
<p><strong>模块定义层</strong>:</p>
<p>__d 定义的代码块，包括 RN 框架源码 js 部分、自定义 js 代码部分、图片资源信息，供 require 引入使用</p>
<p><strong>require层</strong></p>
<p>r 定义的代码块，找到 d 定义的代码块 并执行</p>
<h3 data-id="heading-7">metro打包流程</h3>
<p>metro 打包的整个流程大致分为:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a2c3bdfb6694a05a460bd3278e18679~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.命令参数解析</strong></p>
<pre><code class="copyable">react-native bundle --dev false  --platform android  --entry-file index.js --config bundle.main.js --bundle-output ./CodePush/index.android.bundle --assets-dest ./CodePush --sourcemap-output ./CodePush/index.android.bundle.map "
<span class="copy-code-btn">复制代码</span></code></pre>
<p>platform：对应的平台，android/ios
--entry-file: 入口文件
--config：额外配置，拆包有用到
--bundle-output：生成的bundle文件输出位置
--assets-dest：图片等资源文件输出位置
--sourcemap-output：sourcemap映射文件输出位置</p>
<p><strong>2.metro 打包服务启动</strong></p>
<ul>
<li>合并 metro 默认配置和自定义配置，并设置 maxWorkers,resetCache，--config就属于用户的额外配置</li>
<li>根据解析得到参数，构建 requestOptions，传递给打包函数</li>
<li>实例化 metro Server</li>
<li>启动 metro 构建 bundle</li>
<li>处理资源文件，解析</li>
<li>关闭 Metro Server</li>
</ul>
<p><strong>3.解析和转化</strong></p>
<p>Metro Server 使用<code>IncrementalBundler</code>进行 js 代码的解析和转换**</p>
<p>在 Metro 使用<code>IncrementalBundler</code>进行解析转换的主要作用是：</p>
<ul>
<li>返回了<strong>以入口文件为入口的所有相关依赖文件的依赖图谱和 babel 转换后的代码</strong>；</li>
<li>返回了<strong>var 定义部分及 polyfill 部分所有相关依赖文件的依赖图谱和 babel 转换后的代码</strong>；</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90ccd4ebb3e64c869bb6d1d79c27bfc8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>生成的依赖关系图谱如下</p>
<pre><code class="copyable">[
&#123;
  dependencies: Map(404) &#123; // 入口文件下每个文件所依赖其他文件的关系图谱
    '/Users/alexganggao/Desktop/react-native-ssr/ReactNativeSSR/index.js' => &#123;
     &#123;
    inverseDependencies: Set(1) &#123;
      '/Users/alexganggao/Desktop/react-native-ssr/ReactNativeSSR/index.js'
    &#125;,
    path: '/Users/alexganggao/Desktop/react-native-ssr/ReactNativeSSR/App.js',
    dependencies: Map(8) &#123;

      '@babel/runtime/helpers/createClass' => &#123;
        absolutePath: '/Users/alexganggao/Desktop/react-native-ssr/ReactNativeSSR/node_modules/@babel/runtime/helpers/createClass.js',
        data: &#123;
          name: '@babel/runtime/helpers/createClass',
          data: &#123; isAsync: false &#125;
        &#125;
      &#125;,
      // ....
      'react' => &#123;
        absolutePath: '/Users/alexganggao/Desktop/react-native-ssr/ReactNativeSSR/node_modules/react/index.js',
        data: &#123; name: 'react', data: &#123; isAsync: false &#125; &#125;
      &#125;,
      'react-native' => &#123;
        absolutePath: '/Users/alexganggao/Desktop/react-native-ssr/ReactNativeSSR/node_modules/react-native/index.js',
        data: &#123; name: 'react-native', data: &#123; isAsync: false &#125; &#125;
      &#125;
    &#125;,
    getSource: [Function: getSource],
    output: [
      &#123;
        data: &#123;// 对应文件转换后的代码
          code: `__d(function(g,r,i,a,m,e,d)&#123;var t=r(d[0]);Object.defineProperty(e,"__esModule",&#123;value:!0&#125;),e.default=void 0;var n=t(r(d[1])),u=t(r(d[2])),l=t(r(d[3])),c=t(r(d[4])),f=t(r(d[5])),o=t(r(d[6])),s=r(d[7]);function y()&#123;if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try&#123;return Date.prototype.toString.call(Reflect.construct(Date,[],function()&#123;&#125;)),!0&#125;catch(t)&#123;return!1&#125;&#125;var p=(function(t)&#123;(0,l.default)(R,t);var p,h,x=(p=R,h=y(),function()&#123;var t,n=(0,f.default)(p);if(h)&#123;var u=(0,f.default)(this).constructor;t=Reflect.construct(n,arguments,u)&#125;else t=n.apply(this,arguments);return(0,c.default)(this,t)&#125;);function R()&#123;return(0,n.default)(this,R),x.apply(this,arguments)&#125;return(0,u.default)(R,[&#123;key:"render",value:function()&#123;return o.default.createElement(o.default.Fragment,null,o.default.createElement(s.View,&#123;style:v.body&#125;,o.default.createElement(s.Text,&#123;style:v.text&#125;,"\u4f60\u597d\uff0c\u4e16\u754c")))&#125;&#125;]),R&#125;)(o.default.Component);e.default=p;var v=s.StyleSheet.create(&#123;body:&#123;backgroundColor:'white',flex:1,justifyContent:'center',alignItems:'center'&#125;,text:&#123;textAlign:'center',color:'red'&#125;&#125;)&#125;);`,
          lineCount: 1,
          map: [
            [ 1, 177, 9, 0, '_react' ],
            [ 1, 179, 9, 0, '_interopRequireDefault' ],
            [ 1, 181, 9, 0, 'r' ],
            [ 1, 183, 9, 0, 'd' ],
            [ 1, 185, 9, 0 ],
            [ 1, 190, 10, 0, '_reactNative' ],
            // .....
          ],
          functionMap: &#123;
            names: [ '<global>', 'App', 'render' ],
            mappings: 'AAA;eCW;ECC;GDQ;CDC'
          &#125;
        &#125;,
        type: 'js/module'
      &#125;
    ]
  &#125;
    &#125;,

    '/Users/alexganggao/Desktop/react-native-ssr/ReactNativeSSR/App.js' => &#123;
      inverseDependencies: [Set],
      path: '/Users/alexganggao/Desktop/react-native-ssr/ReactNativeSSR/App.js',
      dependencies: [Map],
      getSource: [Function: getSource],
      output: [Array]
    &#125;,
    '/Users/alexganggao/Desktop/react-native-ssr/ReactNativeSSR/app.json' => &#123;
      inverseDependencies: [Set],
      path: '/Users/alexganggao/Desktop/react-native-ssr/ReactNativeSSR/app.json',
      dependencies: Map(0) &#123;&#125;,
      getSource: [Function: getSource],
      output: [Array]
    &#125;
  &#125;,
  entryPoints: [ //入口文件
    '/Users/alexganggao/Desktop/react-native-ssr/ReactNativeSSR/index.js'
  ],
  importBundleNames: Set(0) &#123;&#125;
&#125;

]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.生成</strong></p>
<p>metro 代码生成部分使用 <code>baseJSBundle</code> 得到代码，并使用 <code>baseToString</code> 拼接最终 <code>Bundle</code> 代码</p>
<p>在 <code>baseJSBundle</code> 中:</p>
<ul>
<li><code>baseJSBundle</code>整体调用了三次 <code>processModules</code>分别用于解析出: <code>preCode</code> , <code>postCode</code> 和 <code>modules</code> 其对应的分别是<strong>var 和 polyfills 部分的代码</strong> , <strong>require 部分的代码</strong> ,  <strong><code>_d</code> 部分的代码</strong></li>
<li><code>processModules</code> 经过两次 <code>filter</code> 过滤出所有类型为 <code>js/</code>类型的数据，第二次过滤使用用户自定义 <code>filter</code> 函数；过滤完成之后使用 <code>wrapModule</code> 转换成<code>_d(factory,moduleId,dependencies)</code>的代码，类似于设计模式中的责任链模式</li>
</ul>
<p>在<code>baseToString</code>中:</p>
<ul>
<li>先将 var 及 polyfill 部分的代码使用\n 进行字符串拼接；</li>
<li>然后将<code>_d</code> 部分的代码使用 <code>moduleId</code> 进行<strong>升序排列</strong>并使用字符串拼接的方式构造<code>_d</code> 部分的代码;</li>
<li>最后合如<code>_r</code>部分的代码</li>
</ul>
<p><strong>5.停止打包服务</strong></p>
<p>停止打包服务</p>
<p>总结如下几点:</p>
<ol>
<li>整个 metro 进行依赖分析和 babel 转换主要通过了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Fjest%2Ftree%2Fmaster%2Fpackages%2Fjest-haste-map%2Fsrc" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/jest/tree/master/packages/jest-haste-map/src" ref="nofollow noopener noreferrer">JestHasteMap (opens new window)</a>去做依赖分析；</li>
<li>在做依赖分析的通过，metro 会监听当前目录的文件变化，然后以最小变化生成最终依赖关系图谱；</li>
<li>不管是入口文件解析还是 polyfill 文件的依赖解析都是使用了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Fjest%2Ftree%2Fmaster%2Fpackages%2Fjest-haste-map%2Fsrc" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/jest/tree/master/packages/jest-haste-map/src" ref="nofollow noopener noreferrer">JestHasteMap (opens new window)</a>;</li>
</ol>
<h3 data-id="heading-8">RN拆包原理</h3>
<p>在打包生成过程中<code>processModules</code> 经过两次 <code>filter</code> 过滤出所有类型为 <code>js/</code>类型的数据，第二次过滤使用用户自定义 <code>filter</code> 函数；过滤完成之后使用 <code>wrapModule</code> 转换成<code>_d(factory,moduleId,dependencies)</code>的代码，类似于设计模式中的责任链模式</p>
<pre><code class="copyable">function createModuleIdFactory() &#123;
  const fileToIdMap = new Map();
  let nextId = 0;
  return path => &#123;
    let id = fileToIdMap.get(path);

    if (typeof id !== "number") &#123;
      id = nextId++;
      fileToIdMap.set(path, id);
    &#125;

    return id;
  &#125;;
&#125;

module.exports = createModuleIdFactory;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>逻辑比较简单，如果查到 map 里没有记录这个模块则 id 自增，然后将该模块记录到 map 中，所以从这里可以看出，官方代码生成 moduleId 的规则就是自增，所以这里要替换成我们自己的配置逻辑，我们要做拆包就需要保证这个 id 不能重复，但是这个 id 只是在打包时生成，如果我们单独打业务包，基础包，这个 id 的连续性就会丢失，所以对于 id 的处理，我们还是可以参考上述开源项目，每个包有十万位间隔空间的划分，基础包从 0 开始自增，业务 A 从 1000000 开始自增，又或者通过每个模块自己的路径或者 uuid 等去分配，来避免碰撞，但是字符串会增大包的体积，这里不推荐这种做法。</p>
<p>在基础包生成以后，打业务包的时候过滤所有基础包moduleId即可</p>
<pre><code class="copyable">function postProcessModulesFilter(module) &#123;
  const path = module["path"];
  for (let i = 0, len = excludeFiles.length; i < len; i++) &#123;
    if (path.indexOf(excludeFiles[i]) >= 0) &#123;
      return false;
    &#125;
  &#125;
  return true;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">Android、RN打包比较</h2>
<p>apk,bundle文件都是能够在对应平台安装运行的压缩文件，不管是gradle还是metro都只是担任打包角色，换一种工具一样可行</p>
<p>两者都提供了开发可以介入打包流程的入口，都是责任链+拦截器模式</p>
<p>RN的hermes原理是提前预编译减少启动时间，同样Android在5.0以上引入了art也是对apk中的dex文件进行预编译，来减少app启动时长</p>
<p><strong>RN打包原文参考：</strong>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.gaogangsever.cn%2Freact%2Freact-native_bundle%25E5%2588%25B0bundle%25E7%2594%259F%25E6%2588%2590%25E5%2588%25B0%25E5%25BA%2595%25E5%258F%2591%25E7%2594%259F%25E4%25BA%2586%25E4%25BB%2580%25E4%25B9%2588.html%23metro-%25E6%259E%2584%25E5%25BB%25BA-bundle-%25E7%2594%259F%25E6%2588%2590" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.gaogangsever.cn/react/react-native_bundle%E5%88%B0bundle%E7%94%9F%E6%88%90%E5%88%B0%E5%BA%95%E5%8F%91%E7%94%9F%E4%BA%86%E4%BB%80%E4%B9%88.html#metro-%E6%9E%84%E5%BB%BA-bundle-%E7%94%9F%E6%88%90" ref="nofollow noopener noreferrer">blog.gaogangsever.cn/react/react…</a></p></div>  
</div>
            