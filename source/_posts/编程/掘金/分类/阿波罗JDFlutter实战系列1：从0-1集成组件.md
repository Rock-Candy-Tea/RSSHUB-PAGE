
---
title: '阿波罗JDFlutter实战系列1：从0-1集成组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50f31796cf30410cbb5e35ec6a48b902~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 01:38:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50f31796cf30410cbb5e35ec6a48b902~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、概述</h2>
<p>本文主要汇总介绍基于Google Flutter封装的JDFlutter，用于组件开发的整体流程，快速准确的定位组件开发的有效信息，为新手小白提供参考；</p>
<p>以下基于 Mac 开发，其中<strong><strong>前置准备</strong></strong>为相关资料文档，对于0开发经验小白而言，可重点关注熟悉 Dart 语言开发规范，初步掌握之后，可跳过并开始<strong><strong>环境构建</strong></strong>步骤，逐步带你开发起来～</p>
<h2 data-id="heading-1">二、前置准备</h2>
<p>Dart 为 Flutter 开发用语言，Pub 用于提供官方和其他开发者提供的开源插件仓库，yaml 为 Flutter 工程的插件配置文件。</p>
<h3 data-id="heading-2">1、开发语言 Dart 官方网站</h3>
<p>英文官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdart.dev%2Fguides" target="_blank" rel="nofollow noopener noreferrer" title="https://dart.dev/guides" ref="nofollow noopener noreferrer">dart.dev/guides</a></p>
<p>中文官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdart.cn%2Fguides" target="_blank" rel="nofollow noopener noreferrer" title="https://dart.cn/guides" ref="nofollow noopener noreferrer">dart.cn/guides</a></p>
<h3 data-id="heading-3">2、Google Flutter官方网站</h3>
<p>英文官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.dev%2Fdocs" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.dev/docs" ref="nofollow noopener noreferrer">flutter.dev/docs</a></p>
<p>中文官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.cn%2Fdocs" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.cn/docs" ref="nofollow noopener noreferrer">flutter.cn/docs</a></p>
<p>Pub官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.dev" ref="nofollow noopener noreferrer">pub.dev</a></p>
<h3 data-id="heading-4">3、JDFlutter官方网站</h3>
<p>官网：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fdoc.jd.com%2Fjd_flutter%2Fincompany%2FJDFlutter%2Fintroduction.html" target="_blank" rel="nofollow noopener noreferrer" title="http://doc.jd.com/jd_flutter/incompany/JDFlutter/introduction.html" ref="nofollow noopener noreferrer">doc.jd.com/jd_flutter/…</a></p>
<p>Pub官网：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fpub.jd.com%2F%23%2Findex" target="_blank" rel="nofollow noopener noreferrer" title="http://pub.jd.com/#/index" ref="nofollow noopener noreferrer">pub.jd.com/#/index</a></p>
<h3 data-id="heading-5">4、其他</h3>
<p>yaml 配置文件相关介绍：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F81365711aa47" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/81365711aa47" ref="nofollow noopener noreferrer">www.jianshu.com/p/81365711a…</a></p>
<h2 data-id="heading-6">三、环境构建</h2>
<p>Google官方提供了其 Flutter 环境安装方式，不过相对较复杂；这里总结出通过 JDFlutterTool（IDE）进行环境安装构建，同步构建Google Flutter环境的方式，最后统一 Google Flutter 和 JDFlutter 环境。</p>
<h3 data-id="heading-7">1、JDFlutterTool</h3>
<p>该 IDE 不用作开发使用，用于配置环境、构建管理 Flutter 工程以及打包发布等流程，其中开发需使用其他IDE，包括但不限于：Android Studio、VS Code等，下文会针对 Android Studio 具体介绍。</p>
<h4 data-id="heading-8">IDE安装</h4>
<p>Version 1.3.0 (2021) 版本下载安装后启动效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50f31796cf30410cbb5e35ec6a48b902~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<p>右上角先通过ERP登录，然后进入环境配置页面，下载安装环境SDK：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c47701a89fd743f397a93d65f1db1627~tplv-k3u1fbpfcp-watermark.image" alt="2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>步骤1：推荐安装jdf-1.22.5版本SDK。</p>
<p>步骤2：下载安装完成之后，设置为默认。</p>
<p>步骤3：下载完成以后，可以点击查看安装目录，<strong><strong>接下来通过该目录路径设置 Google Flutter 环境变量，统一环境</strong></strong>。</p>
<h4 data-id="heading-9">Google Flutter 环境配置</h4>
<p>→ 通过上述 步骤3 获取到安装好的 SDK 路径，例如："/Users/y*****3/workspace/jdflutter/sdk/jdf-1.22.5/bin"（ ⚠️ 路径需要指定到 bin ）。</p>
<p>→ Mac终端配置 Google Flutter 环境变量： </p>
<br>
<blockquote>
<p><em>终端执行</em> <em><strong><strong>vim .zshrc</strong></strong></em></p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97268988162445b7882dbfacb93e5ba8~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>步骤1：键盘切换至<strong><strong>英文输入模式</strong></strong>，键入 <strong><strong>i</strong></strong> 进入编辑模式。</p>
<p>步骤2：将获取到的路径添加到配置文件中。</p>
<p>步骤3：键盘 esc 后键入 <strong><strong>:wq</strong></strong>（英文冒号wq）回车保存并退出。</p>
<br>
<blockquote>
<p><em>终端执行</em> <em><strong><strong>source .zshrc</strong></strong></em></p>
</blockquote>
<p>使当前配置文件更改生效。</p>
<br>
<blockquote>
<p><em>另起终端窗口分别执行</em> <em><strong><strong>jdflutter --version</strong></strong></em> <em>、</em> <em><strong><strong>flutter --version</strong></strong></em></p>
</blockquote>
<p>查看 JDFlutter、Google Flutter 环境是否设置成功</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cf5d50f1e194c2db07975729343e5ba~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>→ 成功可显示如上所示，flutter SDK 当前版本显示为 1.22.5、dart SDK 当前版本显示为 2.10.4（两个命令执行顺序不分先后，并且不会互相影响，只是为了对比清晰）。</p>
<p>→ 另起终端窗口目的：为了验证环境变量配置是否生效。</p>
<p>→ jdflutter 为 JDFlutter 命令，flutter 为 Google Flutter 命令，之后使用其一即可。</p>
<br>
<p>至此，Google Flutter 环境配置完成，并且与 JDFlutter 环境统一，使用同一个SDK。</p>
<h3 data-id="heading-10">2、Android Studio</h3>
<p>本开发采用 Android Studio 开发，其他开发 IDE 请自行查阅资料，但无论哪种开发工具，均包括以下几点配置项。</p>
<h4 data-id="heading-11">IDE安装</h4>
<p>可下载最新版本，地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.google.cn/studio" ref="nofollow noopener noreferrer">developer.android.google.cn/studio</a></p>
<p>汉化参考地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fws1836300%2Farticle%2Fdetails%2F99552211" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/ws1836300/article/details/99552211" ref="nofollow noopener noreferrer">blog.csdn.net/ws1836300/a…</a></p>
<p>（以下界面显示效果均为 Android Studio 4.2.1 版本，不同版本可能存在差异）</p>
<h4 data-id="heading-12">插件配置（flutter插件、dart插件）</h4>
<p>配置插件是为了在开发过程中实现编译器语法高亮、自动提示、代码补全、编译运行等功能。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eac0bf7b2a364d3db1685bceaec8ff2b~tplv-k3u1fbpfcp-watermark.image" alt="5.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装好 Android Studio 后运行，首先打开设置，然后选择插件（Plugin）在所示位置输入 flutter 和 dart，搜索查找相应插件并安装。</p>
<p>至此，Android Studio 配置完成，接下来通过 flutter 命令检测环境。</p>
<h3 data-id="heading-13">3、环境检测及相关问题</h3>
<p>以下通过 flutter 命令检测环境配置，以及遇到的相关问题的解决方法。</p>
<p>终端执行 <strong><strong>flutter doctor</strong></strong>，没有问题的情况下，执行结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc7df0b338144dce9cd6586a01cc1b15~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>说明：绿色对勾表示当前检测项正常，其中 6 个检测项分别代表：</p>
<p>① flutter SDK是否安装并配置完成。</p>
<p>② Android toolchain 是否安装并配置完成。</p>
<p>③ iOS 侧开发工具 Xcode IDE 是否安装并配置完成。</p>
<p>④ Android Studio IDE 开发工具是否安装并配置完成。</p>
<p>⑤ VS Code IDE 开发工具是否安装并配置完成。</p>
<p>⑥ 是否已存在并运行可调试的设备，包括真机或者模拟器。</p>
<br>
<p>可能出现的非正常执行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d20bcd1b40e4196909a8034c4d8818b~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>说明：黄色叹号表示当前检测项存在问题，针对以上问题的解决方法：</p>
<p><strong><strong>Android license status unknown</strong></strong>：存在未同意的许可，终端执行 <strong><strong>flutter doctor --android-licenses</strong></strong>，依照提示同意所有许可即可。</p>
<p><strong><strong>Flutter plugin not installed、Dart plugin not installed</strong></strong>：Android Studio IDE 未安装 flutter、dart 插件，如果前面的配置已完成，插件实际上是已经安装成功的，但是此处依然会提示未安装，原因在于新版本的 Android Studio 的插件安装位置与 flutter doctor 检测的目录路径不同导致，进行软连接即可，终端执行：ln -s ~/Library/Application\ Support/Google/AndroidStudio4.2.1/plugins ~/Library/Application\ Support/AndroidStudio4.2.1，其中 4.2.1 为当前版本。</p>
<p><strong><strong>VS Code...</strong></strong>：VS Code IDE 未安装 flutter 插件（扩展），如果不使用该 IDE 开发则可以忽略，如果需要可以参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fliyangzmx%2Farticle%2Fdetails%2F105463681" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/liyangzmx/article/details/105463681" ref="nofollow noopener noreferrer">blog.csdn.net/liyangzmx/a…</a> 。</p>
<p><strong><strong>Xcode...</strong></strong>：如果非 iOS 开发，即未安装 Xcode IDE 的情况下，此处也可能会提示黄色叹号的警告或者红色叉的错误，可以忽略。</p>
<h2 data-id="heading-14">四、工程构建</h2>
<p>统一使用 JDFlutterTool 进行工程创建和管理，其预置了 JDFlutter 环境，由于做组件开发，所以首先需要创建 plugin 组件工程，然后创建 module 工程，用于组件打包、生成产物并集成到原生工程中。</p>
<h3 data-id="heading-15">1、JDFlutterTool 创建 Plugin 组件工程</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3947e00cd4c84f2d9153f45f6ca3fe85~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>流程说明：</p>
<p>步骤1：打开 JDFlutterTool，选择”新建“，进入第二个页面。</p>
<p>步骤2：在创建页面首先选择类型，图中对所有类型进行了说明。</p>
<p>步骤3：由于我们进行组件开发，所有这里选择 plugin，图中对业务型、功能型选择进行了说明，其他按照要求填写即可。</p>
<br>
<p>完成以上步骤后，IDE自动创建 git 仓库，并提示打开仓库管理页面，也可以通过如下方式找到仓库，并手动克隆到本地进行开发。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2464171d2a04335b12fac8c8a7c675e~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong><strong>⚠️</strong></strong> 图3 中显示的只是创建好的 git 仓库，需要手动克隆到本地，然后通过首页“打开”克隆好的工程，选择 图4 中 Android Studio 打开工程进行开发。</p>
<h3 data-id="heading-16">2、JDFlutterTool 创建 Module 工程</h3>
<p>上述介绍的 Plugin 就是我们要开发的组件，那么如何将它集成到原生项目中？这就要借助于 Module：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91c42854450f464fa0d9f8336d506279~tplv-k3u1fbpfcp-watermark.image" alt="10.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>module 创建过程与 plugin 创建过程相同，无非在选择类型时选择 module，后续也同样需要手动克隆到本地。</p>
<h3 data-id="heading-17">3、工程主要结构简介</h3>
<p>对 plugin 工程和 module 工程的项目结构进行简单对比，如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f69ad283592445eb45db215033c8c95~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中，yaml 配置文件用于管理配置工程所需的依赖、资源（如图片资源）等。</p>
<br>
<p><strong><strong>⚠️</strong></strong> 对于 plugin 工程的 yaml 配置文件 ② 和内部 example 工程的 yaml 配置文件 ① 而言，需要注意以下几点，引入 JDFlutter 官方话术：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c7b36c8cb4047a0932d600b235ca89e~tplv-k3u1fbpfcp-watermark.image" alt="12.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解读：在 ② 的配置文件中，如果需要使用到 JDFlutter 提供的<strong><strong>基础组件</strong></strong>，注意此处所指的是基础组件，则只能依赖容器插件（如下图），然后在 example 的配置文件 ① 中依赖所需基础组件进行调试开发，最终打包时再在 module 内依赖相关基础组件；</p>
<p>但是在 ② 中依然可以依赖所需的第三方插件。</p>
<h2 data-id="heading-18">五、打包及调试</h2>
<p>开发过程中，对于网络接口请求，这里采用的是 flutter 与原生交互，通过原生发送请求，最后将请求结果传递给 flutter 的方式，那么理所当然的离不开将上述介绍的 module 打包产物并集成到原生工程调试的过程。</p>
<h3 data-id="heading-19">1、module 打包</h3>
<p>作为调试开发，我们选择本地构建、debug 类型：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae04cc97d3bb470f9b6e661321959a8a~tplv-k3u1fbpfcp-watermark.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上进行构建，等待片刻后，生成打包产物，将生成文件集成到原生宿主工程内，集成过程详见：</p>
<p>Android：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fdoc.jd.com%2Fjd_flutter%2Fincompany%2FJDFlutter%2FJDF_Container%2Faccess-step%2Fstep-intro%2Fstep-8.html" target="_blank" rel="nofollow noopener noreferrer" title="http://doc.jd.com/jd_flutter/incompany/JDFlutter/JDF_Container/access-step/step-intro/step-8.html" ref="nofollow noopener noreferrer">doc.jd.com/jd_flutter/…</a></p>
<p>iOS：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fdoc.jd.com%2Fjd_flutter%2Fincompany%2FJDFlutter%2FJDF_Container%2Faccess-step%2Fstep-intro%2Fstep-10.html" target="_blank" rel="nofollow noopener noreferrer" title="http://doc.jd.com/jd_flutter/incompany/JDFlutter/JDF_Container/access-step/step-intro/step-10.html" ref="nofollow noopener noreferrer">doc.jd.com/jd_flutter/…</a></p>
<h3 data-id="heading-20">2、开发调试</h3>
<p>这里我们采用 Attach 将 Android Studio 与设备之间建立 Socket 连接的方式进行调试开发。 </p>
<p>首先，选择好待调试设备，运行上述配置好打包产物的原生宿主工程。</p>
<p>然后，在 module 工程下，Android Studio IDE 的终端内执行：<strong><strong>flutter attach</strong></strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/960cb6d98f684cf0b7b2b3eb7075ae09~tplv-k3u1fbpfcp-watermark.image" alt="15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果当前运行多个设备，终端会要求通过输入数字选择当前运行着打包产物的设备。</p>
<p>如果当前设备内存在多个包名的应用，可能终端会再要求根据包名直接选择应用，根据提示修改命令即可。</p>
<br>
<p>attach 成功后，可直接输入以下字母执行相应操作，其中使用比较频繁的是：r 和 R，进行代码更新后的热重载操作：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ff916bacfcc4ece917bcb8d2cfcb0ab~tplv-k3u1fbpfcp-watermark.image" alt="16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上为全部内容，至此，作为小白的开发汇总到此结束，有任何问题欢迎随时指正，感谢您的耐心阅读～</p></div>  
</div>
            