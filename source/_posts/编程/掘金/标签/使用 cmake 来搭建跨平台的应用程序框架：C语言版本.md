
---
title: '使用 cmake 来搭建跨平台的应用程序框架：C语言版本'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d22aa86944124512b2e0fd2aad4120f6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 10 May 2021 22:27:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d22aa86944124512b2e0fd2aad4120f6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>我们在写应用程序的过程中，经常需要面对一个开发场景：编写跨平台的应用程序。</p>
<p>这种要求对于 Linux 系列的平台来说，还是比较好处理的，大部分情况下只需要换一个交叉编译工具链即可，涉及到硬件平台相关部分再嵌入几个内联汇编。</p>
<p>但是，对于 Windows 平台来说，就稍微麻烦一些。你可能会说，在 Windows 平台上用 cygwin, minGW 也可以统一编译啊，但是你能指望客户在安装你的程序时，还需要去部署兼容 Linux 的环境吗？最好的解决方式，还是使用微软自家的开发环境，比如VS等等。</p>
<p>这篇文章，我们以一个最简单的程序，来描述如何使用 cmake 这个构建工具，来组织一个跨平台的应用程序框架。</p>
<p>阅读这篇文章，您可以收获下面几个知识点：</p>
<blockquote>
<ol>
<li>
<p>cmake 在编译库文件、应用程序中的相关指令；</p>
</li>
<li>
<p>Windows 系统中的动态库导出、导入写法；</p>
</li>
<li>
<p>如何利用宏定义来进行跨平台编程；</p>
</li>
</ol>
</blockquote>
<p>在公众号后台留言【430】，可以收到示例代码。在 Linux/Windows 系统中可以直接编译、执行，拿来即用。</p>
<h2 data-id="heading-1">二、示例代码说明</h2>
<h4 data-id="heading-2">1. 功能描述</h4>
<p>示例代码的主要目的，是用来描述如何组织一个跨平台的应用程序结构。它的功能比较简单，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d22aa86944124512b2e0fd2aad4120f6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">2. 文件结构</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f173471de7e4f10bc27f3726cd72aba~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<ol>
<li>
<p>Common：放置一些开源的第三方库，例如：网络处理，json 格式解析等等;</p>
</li>
<li>
<p>Application: 应用程序，使用 Utils生成的库;</p>
</li>
<li>
<p>Uitls：放置一些工具、助手函数，例如：文件处理、字符串处理、平台相关的助手函数等等，最后会编译得到库文件（动态库 libUtils.so、静态库 libUtils.a）;</p>
</li>
<li>
<p>如果扩展其他模块，可以按照 Utils 的文件结构复制一个即可。</p>
</li>
</ol>
</blockquote>
<h4 data-id="heading-4">3. cmake 构建步骤</h4>
<p>在示例代码根目录下，有一个“总领” CMakeLists.txt 文件，主要用来设置编译器、编译选项，然后去 include 其他文件夹中的 CMakeLists.txt 文件，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2b71184ffe64e58b1c975e53685a8d3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">4. Utils 目录说明</h4>
<p>这个目录的编译输出是库文件：</p>
<blockquote>
<p>Linux 系统：libUtils.so, libUtils.a;</p>
<p>Windows 系统：libUtils.dll, libUtils.lib, libUtils.a;</p>
</blockquote>
<p>其中的 CMakeLists.txt 文件内容如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dc2393c9c5e4d058f9cd964ddd61c49~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前，代码中只写了一个最简单的函数 getSystemTimestamp()，在可执行应用程序中，将会调用这个函数。</p>
<h4 data-id="heading-6">5. Application 目录说明</h4>
<p>这个目录的编译输出是：一个可执行程序，其中调用了 libUtils 库中的函数。</p>
<p>CMakeLists.txt 文件内容如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0d9fa5b715a4c52ad12b894941a0518~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">三、Linux 系统下操作步骤</h2>
<h4 data-id="heading-8">1. 创建构建目录 build</h4>
<pre><code class="copyable">$ mkdir build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在一个独立的 build 目录中编译，生成的中间代码不会污染源代码，这样对于使用 git 等版本管控工具来说非常的方便，在提交的时候只需要 ignore build 目录即可，强烈推荐按照这样的方式来处理。</p>
<h4 data-id="heading-9">2. 执行 cmake，生成 Makefile</h4>
<pre><code class="copyable">$ cd build
$ cmake ..
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b84a7bda34d48318061ccd1466f00fe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">3. 编译 Utils 库</h4>
<pre><code class="copyable">$ cd Utils/src
$ make
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e1400d3ffd34e3e947e95587f5de240~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 CMakeLists.txt 中的最后部分是安装指令，把产生的库文件和头文件，安装到源码中的 install 目录下。</p>
<pre><code class="copyable">$ make install
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40f7b5b1106341dbb0d6a2f8d34771cf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">4. 编译可执行程序 Application</h4>
<p>Application 使用到了 libUtils.so 库，因此需要手动把 libUtils.so 和头文件，复制到 Application 下面对应的 lib/linux 和 include 目录下。</p>
<p>当然，也可以把这个操作写在 Utils 的安装命令里。</p>
<pre><code class="copyable">$ cd build/Application/src
$ make
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/071be55299864024bc2868cfdba90076~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行生成的可执行程序 main，即可看到输出结果。</p>
<h2 data-id="heading-12">四、Widnows 系统下操作步骤</h2>
<h4 data-id="heading-13">1. 通过 cmake 指令生成 VS 工程</h4>
<p>同样的道理，新建一个 build 目录，然后在其中执行 <code>cmake ..</code> 指令，生成 VS 解决方案，我使用的是 VS2019:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afcde8a41c69470e83878aeb2617ade3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9110d9ceb31b460381f1eec003eda902~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">2. 编译 Utils 库文件</h4>
<p>使用 VS2019 打开工程文件 DemoApp.sln，在右侧的解决方案中，可以看到：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1894cc584194d74b90e5f4fb8537b79~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 libUtils_shared 单击右键，选择【生成】:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f963c8ee6a3e46c2a48cf5569266f9b1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，在目录 build\Utils\src\Debug 下面，可以看到生成的文件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/738006207c5543c98e1ae74729e3c937~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">3. 编译可执行程序  Application</h4>
<p>因为Application需要使用 Utils 生成的库，因此，需要手动把库和头文件复制到 Application 下面的 lib/win32 和 include 目录下。</p>
<p>在 VS 解决方案窗口中，在 main 目标上，单击右键，选择【生成】:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9375dfb499b54da59ef18c3ccf2987bd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，在目录 build\Application\src\Debug 下可以看到生成的可执行程序:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3df02a71367745f9ba48d662c9526369~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>直接单击 main.exe 执行，报错：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d80a70c103446f499b1958713aa4b66~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要把 libUtils.dll 动态库文件复制到 main.exe 所在的目录下，然后再执行，即可成功。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c5e8ddf55984be7a9ce3e19ecf44706~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">五、总结</h2>
<p>这篇文章的操作过程主要以动态库为主，如果编译、使用静态库，执行过程是一样一样的。</p>
<p>如果操作过程有什么问题，欢迎留言、讨论，谢谢！</p>
<p>在公众号后台留言【430】，可以收到示例代码。在 Linux/Windows 系统中可以直接编译、执行，拿来即用。</p>
<p>祝您好运！</p>
<p><br><br></p>

---------- End ----------
<br><br>
让知识流动起来，越分享，越幸运！    
<br><br>
星标公众号，能更快找到我！
<br>


Hi~你好，我是道哥，一枚嵌入式开发老兵。

<br>
推荐阅读
<br>
<p><a href="https://mp.weixin.qq.com/s/TwDiDmApmsIVSIFh2h1osQ" target="_blank" rel="nofollow noopener noreferrer">1. C语言指针-从底层原理到花式技巧，用图文和代码帮你讲解透彻</a><br>
<a href="https://mp.weixin.qq.com/s/oY2pF5ilk8UCq09022Tt6w" target="_blank" rel="nofollow noopener noreferrer">2. 原来gdb的底层调试原理这么简单</a><br>
<a href="https://mp.weixin.qq.com/s/xOdwQQHIjEobe4jR_2gDRQ" target="_blank" rel="nofollow noopener noreferrer">3. 一步步分析-如何用C实现面向对象编程</a><br>
<a href="https://mp.weixin.qq.com/s/HJqh0JHIqhabRd5zHmKAiw" target="_blank" rel="nofollow noopener noreferrer">4. 图文分析：如何利用Google的protobuf，来思考、设计、实现自己的RPC框架</a><br>
<a href="https://mp.weixin.qq.com/s/OwfnCQo8s8E1KzuVKKca1g" target="_blank" rel="nofollow noopener noreferrer">5. 都说软件架构要分层、分模块，具体应该怎么做(一)</a><br>
<a href="https://mp.weixin.qq.com/s/MRrDKhEGyNEbrZy2DqzjtQ" target="_blank" rel="nofollow noopener noreferrer">6. 都说软件架构要分层、分模块，具体应该怎么做(二)</a></p></div>  
</div>
            