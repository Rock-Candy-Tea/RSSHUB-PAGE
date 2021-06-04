
---
title: 'iOS技能拓展 多环境配置'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acfc1afa1e314bbfb984aecc481aae96~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 11 May 2021 05:40:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acfc1afa1e314bbfb984aecc481aae96~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">写在前面</h2>
<p>关于多环境</p>
<ul>
<li><code>Project</code>：包含了项目所有信息——所有代码、资源文件（workSpace就是包含多个Project）</li>
<li><code>Target</code>：对指定代码和资源文件的具体构建方式</li>
<li><code>Scheme</code>: 对指定Target的环境配置</li>
</ul>
<h2 data-id="heading-1">一、多Target</h2>
<p><code>Target</code>就是个打工人，是具体干活的人；而<code>Scheme</code>就是老板（环境配置），谁给的钱多（指定哪个环境）<code>Target</code>就给谁干活（执行哪份配置）</p>
<h4 data-id="heading-2">1.Duplicate Target</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acfc1afa1e314bbfb984aecc481aae96~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">2.统一名称</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4703b9e0ec04491da40430d23ff2e046~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">3. 修改BundleId和AppIcon</h4>
<p>就可以很好区分两个<code>Target</code>了
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1dd6800080243eca36c46cea0b89721~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">4.使用宏定义来区分Target</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a309faf7154844629ecd97c7fd8877d0~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223192120000.png" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/586f15ddf9da4192ac765dddd8a5626d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223192221125.png" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adc33b1bacb24123bbf46256b8b8d60c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223192301115.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">5.Swift配置</h4>
<p>Swift配置略有不同，它是通过<code>Other Swift Flags</code>来预编译宏的</p>
<ol>
<li>先创建Swift文件并创建桥接文件</li>
<li>添加Swift文件到编译列表中</li>
<li>指定Swift语言版本和桥接文件<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdaf84629aaf45719fd10387b2ac425d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223193628976.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>此时可以先使用OC和Swift进行混编了<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/138d9e4be2d94402b022e55984fa14ef~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223193919321.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>使用预定义宏（与OC不同的是，Swift需要使用“-D xxx”的形式，点击回车会分成两行）<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d63560a8afab4cdfbf1bc6bce1859c9a~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223195616963.png" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5674064b32174e0897dc743e4c2100b0~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223195722989.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ol>
<p>其实<code>多Target</code>也是用到了<code>Scheme</code>配置——与前文中说的，使用哪套配置取决于选择<code>Scheme</code>对应的<code>Target</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30e7ff119ef84b36b09c781c701b99ff~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223200551758.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>多Target配置多环境虽然能满足我们的需求，但是会生成多个info.plist文件，且操作繁琐——Target之间还需要来回切换来配置不同的参数，好在我们还有别的配置方案</p>
</blockquote>
<h2 data-id="heading-7">二、多Scheme</h2>
<p>这种方案与<code>多Target</code>方案较为类似，都是通过自定义参数来达成需求。与其叫<code>多Scheme</code>，更不如叫<code>多Configuration</code></p>
<h4 data-id="heading-8">1.新增Configuration</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be314cb921994d5399f610f9771ce54b~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223202336544.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">2.新增Scheme</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaa65522427341709e5ee4928ec02ac0~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223202424554.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">3.Scheme对应Configuration</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2b7884330e549dfae0bf9a60404e9b1~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223202529243.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">4.新增自定义配置</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e4c465fbe8c4ef6b6b55c5db0c647bf~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223203347870.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">5.多Scheme方案也可以修改BundleId和AppIcon</h4>
<p>只要是BuildSettings里面有的都可以多环境配置</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6e1228751f34c48808abb99c57f7d25~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210224091309339.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">6.利用info.plist文件进行映射</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8002403e4f3c47bcaa64cd9fcd8f2b60~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223202915532.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd5917506d0745d79fa30dc2d0ae3b52~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223203504772.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这样子就可以通过切换Scheme来完成多环境配置，但是自定义配置还是有点复杂</p>
</blockquote>
<h2 data-id="heading-14">三、多Xcconfig</h2>
<h4 data-id="heading-15">1.新建Xcconfig</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57e2c9ac6ee94d9b9b7eeb67c67d957d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223204954187.png" loading="lazy" referrerpolicy="no-referrer">
命名方式最好是<code>Config-项目名称.环境Configuration.xcconfig</code>（可参考Cocoapods集成的xcconfig文件）<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e26f90badcb245d4925ea9926251ee4b~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223205642424.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">2.Configuration选择对应的Xcconfig</h4>
<p>上面的入口是配置<code>Project</code>，下面的入口是配置<code>Target</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bba6071f27dd4bbd9bdd4ca47f8a713c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210224091734621.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">3.配置Xcconfig文件</h4>
<p>部分变量配置到BuildSettings中不起作用，如<code>PRODUCT_BUNDLE_IDENTIFIER</code></p>
<h4 data-id="heading-18">4.配置info.plist文件进行映射</h4>
<p>同方案二一样配置<code>info.plist文件</code>进行映射
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd37e15c85c94c38be0cc683b0bf4441~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210223210121484.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>xcconfig文件实质就是在配置BuildSetting里面的选项——<a href="https://xcodebuildsettings.com/" target="_blank" rel="nofollow noopener noreferrer">Xcode Build Settings网站</a>详细介绍了各个变量</p>
</blockquote>
<h2 data-id="heading-19">四、Xcconfig冲突</h2>
<h4 data-id="heading-20">1.Pods-config冲突</h4>
<p>往往我们在多环境下进行<code>podfile</code>配置后，终端会发出如下警告，且项目无法运行
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996b41bde648478a959313455f480ec4~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
从字面意思上看就是“项目已经配置了<code>config</code>，<code>Pods-config</code>可能不会生效”——为了解决这个警告，也是为了正常运行项目，我们需要在自定义的<code>Xcconfig</code>文件中引用<code>Pods-config</code></p>
<p>根据提示在xcconfig文件中添加<code>Target Support Files/Pods-FXDemo/Pods-FXDemo.release.xcconfig</code>。仅仅是这样还无法引用对应的<code>Pods-config</code>，根据目录应该使用如下的导入方式：</p>
<pre><code class="copyable">#include "Pods/Target Support Files/Pods-FXDemo/Pods-FXDemo.debug.xcconfig"

ConfigurationString = 这是开发环境
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在所有环境配置中都引用<code>Pods-config</code>，终端警告就会消除</p>
<h4 data-id="heading-21">2.继承xcconfig</h4>
<p>光光是上面这种引用操作还不够，引用只是将原有配置全部引用过来，如果重写的话就会进行覆盖<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9d5ef6574d448bbae88630cbd08ac6e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">因此我们需要使用Xcode内置的<code>$(inherited)</code>字段来继承（<code>Pods-config</code>也是如此操作的）</p>
<pre><code class="copyable">#include "Pods/Target Support Files/Pods-FXDemo/Pods-FXDemo.debug.xcconfig"

ConfigurationString = 这是开发环境
OTHER_LDFLAGS = $(inherited) -framework "FXSDK"
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">3.新增Other Linker Flags</h4>
<p>在<code>引用</code>和<code>继承</code>之后，还可以在<code>BuildSettings</code>新增链接
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2a39865716c45b1b97e8b0b3045dadb~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-23">五、Xcconfig拓展</h4>
<ul>
<li>include可以使用绝对路径/相对路径</li>
</ul>
<pre><code class="copyable">// 绝对路径
#include "Pods/Target Support Files/Pods-FXDemo/Pods-FXDemo.debug.xcconfig"
// 相对路径
#include "/Users/felix/Desktop/FXDemo/Pods/Target Support Files/Pods-FXDemo/Pods-FXDemo.debug.xcconfig"
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>网址的定义可以使用中间量去实现（使用变量可以用<code>$()</code>或<code>$&#123;&#125;</code>）</li>
</ul>
<pre><code class="copyable">diagonal = /
ConfigurationString = https:$&#123;diagonal&#125;/baidu.com
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用环境变量来限制生效的场景</li>
</ul>
<pre><code class="copyable">// 表示在debug环境+模拟器+x86架构下才链接“FXSDK”
OTHER_LDFLAGS[config=Debug][sdk=iphonesimulator*][arch=x86_64] = -framework "FXSDK"
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">写在后面</h2>
<p>其实多环境配置不仅仅只是操作<code>Target</code>、<code>Scheme</code>、<code>Xcconfig</code>，要理解他们各自的功能，搭配使用才能更好地完成多环境配置需求</p></div>  
</div>
            