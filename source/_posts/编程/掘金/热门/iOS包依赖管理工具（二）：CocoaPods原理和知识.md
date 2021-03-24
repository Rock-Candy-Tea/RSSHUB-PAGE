
---
title: 'iOS包依赖管理工具（二）：CocoaPods原理和知识'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=8094'
author: 掘金
comments: false
date: Sat, 27 Feb 2021 20:00:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=8094'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<h1 data-id="heading-0">iOS包依赖管理工具系列</h1>
<p><a href="https://juejin.cn/post/6932739864613879821" target="_blank">iOS包依赖管理工具（一）：CocoaPods了解篇</a></p>
<p><a href="https://juejin.cn/post/6934158661912789006" target="_blank">iOS包依赖管理工具（二）：CocoaPods原理和知识</a></p>
<p><a href="https://juejin.cn/post/6934978194751619080" target="_blank">iOS包依赖管理工具（三）：创建自己的 Pod 库</a></p>
<p><a href="https://juejin.cn/post/6935089831298990088" target="_blank">iOS包依赖管理工具（四）：Swift Package Manager（SPM）了解篇</a></p>
<p><a href="https://juejin.cn/post/6935598901265186829" target="_blank">iOS包依赖管理工具（五）：Swift Package Manager（SPM）自定义篇</a></p>
<p><a href="https://juejin.cn/post/6935661353080193054" target="_blank">iOS包依赖管理工具（六）：CocoaPods VS SPM 总结篇</a></p>
</blockquote>
<blockquote>
<p>上一篇我们了解了 CocoaPods ，以及如何安装，本篇将进一步深入了解</p>
</blockquote>
<h2 data-id="heading-1">1、pod的install与update区别，使用场景</h2>
<h3 data-id="heading-2">1.1、pod install：</h3>
<blockquote>
<p>会去检查podfile.lock是否已经包含该库，如果包含则继续判断是否指定版本， 如果指定版本就去检查podfile.lock中保存的版本是否与新指定的相同，相同则跳过，不相同则更新，如果没有指定版本则不检查更新直接跳过，如果不包含该库则去下载该库并将版本保存在podfile.lock文件中。</p>
<p>每次当pod install 命令运行，并下载安装新的pods的时候，他会在Podfile.lock中为每个pod写入它安装的版本。此文件跟踪每一个已安装的版本，并且锁定这些版本。当运行pod install 的时候它仅仅解析那些Podfile.lock中位列出的依赖关系。</p>
<p>对于Podfile.lock中列出的pods，它仅仅会下载指明的版本，不会去检查是否有新版本可用。</p>
<p>对于Podfile.lock中未列出的pods，他会搜索与Podfile中内容相匹配的版本 (例如 pod 'MyPod', '~>1.2')。</p>
</blockquote>
<h3 data-id="heading-3">1.2、pod update：</h3>
<blockquote>
<p>这个命令会忽略Podfile.lock中的记录，直接去找符合Podfile文件中的该依赖库的约束版本（无约束的话就是最新版本）。一般在你想要更新pods到一个新的版本的时候使用。当运行pod update PODNAME 时，CocoaPods将尝试查找PODNAME的更新版本，而不考虑Podfile.lock中列出的版本。 它会将pod更新为可能的最新版本（只要它与Podfile中的版本限制相匹配）。</p>
<p>如果运行pod更新没有pod名称，CocoaPods将更新您Podfile中列出的每个pod到最新的版本。</p>
</blockquote>
<h3 data-id="heading-4">1.3、pod install使用场景：</h3>
<blockquote>
<ol>
<li>新创建工程，第一次引入pod库时</li>
<li>修改了Podfile文件，添加或删除了所依赖的pod库时。</li>
<li>团队中新人拉取工程后获取pod库时。</li>
<li>团队中，不同开发者要同步对pod库的依赖时(有人改变了依赖关系，删除或增加pod时。</li>
</ol>
<p>如果有人执行了pod update, 此时他的Podfile.lock文件中的跟踪版本就已经变更，此时，其他人只要pod install就能更新为和Podfile.lock文件中的版本。</p>
<p>如果Podfile和Podfile.lock的记录相冲突，Podfile文件中指定了低于Podfile.lock中记录的版本。会以Podfile文件为准，并在获取成功后更新Podfile.lock文件。)</p>
</blockquote>
<h3 data-id="heading-5">1.4、pod update使用场景：</h3>
<blockquote>
<ol>
<li>一般在你想要更新pods到一个新的版本的时候使用。</li>
</ol>
</blockquote>
<h2 data-id="heading-6">2、podfile指定版本号时的逻辑运算符</h2>
<pre><code class="copyable">Besides no version, or a specific one, it is also possible touse logical operators:
'> 0.1'    Any version higher than 0.1         0.1以上
'>= 0.1'   Version 0.1 and any higher version  0.1以上，包括0.1
'< 0.1'    Any version lower than 0.1          0.1以下
'<= 0.1'   Version 0.1 and any lower version   0.1以下，包括0.1

In addition to the logic operators CocoaPods has an optimisicoperator ~>:
'~> 0.1.2' Version 0.1.2 and the versions up to 0.2, not including 0.2 and higher  0.2以下(不含0.2)，0.1.2以上（含0.1.2）
'~> 0.1' Version 0.1 and the versions up to 1.0, not including 1.0 and higher      1.0以下(不含1.0)，0.1以上（含0.1）
'~> 0' Version 0 and higher, this is basically the same as not having it.          0和以上，等于没有此约束
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3、Podfile语法</h2>
<pre><code class="copyable">1. source
     * 指定 specs 的位置，自定义添加自己的 podspec。
     * 如果没有自定义添加 podspec，则可以不添加这一项，因为默认使用 CocoaPods 官方的 source。一旦指定了其它 source，那么就必须指定官方的 source，如上例所示。

 2. platform :iOS, '8.0'
     * 指定了开源库应该被编译在哪个平台以及平台的最低版本。
     * 如果不指定平台版本，官方文档里写明各平台默认值为 iOS：4.3，OS X：10.6，tvOS：9.0，watchOS：2.0。

 3. use_frameworks!
     使用 frameworks 动态库替换静态库链接
     * Swift 项目 CocoaPods 默认 use_frameworks!
     * OC 项目 CocoaPods 默认 #use_frameworks!

 4. inhibit_all_warnings!
     * 屏蔽 CocoaPods 库里面的所有警告
     * 这个特性也能在子 target 里面定义，如果你想单独屏蔽某 pod 里面的警告也是可以的，例如：
         `pod 'JYCarousel', :inhibit_warnings => true`

 5. workspace
     * 指定包含所有 projects 的 Xcode workspace
     * 如果没有指定 workspace，并且在 Podfile 所在目录下只有一个 project，那么 project 的名称会被用作 workspace 的名称

 6. target ‘xxxx’ do ... end
     * 指定特定 target 的依赖库
     * 可以嵌套子 target 的依赖库
 
 7. project
     * 默认情况下是没有指定的，当没有指定时，会使用 Podfile 目录下与 target 同名的工程
     * 如果指定了 project，如上例所示，则 CocoaPodsTest 这个 target 只有在 CocoaPodsTest 工程中才会链接

 8. inherit! :search_paths
     * 明确指定继承于父层的所有 pod，默认就是继承的

 9. 依赖库的基本写法
     pod 'AFNetworking' --> 不显式指定依赖库版本，表示每次都获取最新版本
     pod 'AFNetworking', '2.0' --> 只使用 2.0 版本
     pod 'AFNetworking', '> 2.0' --> 使用高于 2.0 的版本
     pod 'AFNetworking', '>= 2.0' --> 使用大于或等于 2.0 的版本
     pod 'AFNetworking', '< 2.0' --> 使用小于 2.0 的版本
     pod 'AFNetworking', '<= 2.0' --> 使用小于或等于 2.0 的版本
     pod 'AFNetworking', '~> 0.1.2' --> 使用大于等于 0.1.2 但小于 0.2 的版本
     pod 'AFNetworking', '~> 0.1' --> 使用大于等于 0.1 但小于 1.0 的版本
     pod 'AFNetworking', '~> 0' --> 高于 0 的版本，写这个限制和什么都不写是一个效果，都表示使用最新版本
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">4、Podfile.lock</h2>
<ul>
<li>Podfile.lock这个文件是我们新建Podfile文件后会自动生成的一个文件，里面存储了我们已经安装的依赖库的版本。</li>
<li>当我们第一次运行Podfile时，如果对依赖库不指定版本的话，cocoapods会安装最新的版本，同时将pods的版本记录在Podfile.lock文件中。这个文件会保持对每个pod已安装版本的跟踪，并且锁定这些版本。再执行pod install的话，只会处理没有记录在Podfile.lock中的依赖库，会查找匹配Podfile中描述的版本。对于已经记录在Podfile.lock的依赖库，会下载Podfile.lock文件中记录的版本，而不会检查是否有更新。当然，如果你约束了pods的版本的话，会按照你指定的版本进行安装，同时也会更新Podfile.lock记录的信息。</li>
</ul>
<p>Podfile.lock内部</p>
<pre><code class="copyable">PODS:
  - Masonry (1.1.0)
DEPENDENCIES:
  - Masonry (~> 1.1.0)
SPEC REPOS:
  trunk:
    - Masonry
  SPEC CHECKSUMS:
     Masonry: 678fab65091a9290e40e2832a55e7ab731aad201
    PODFILE CHECKSUM: 7a5a6c829f4d2252e3e3d116ab9757a3b270ed8a
    COCOAPODS: 1.9.3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：</p>
<blockquote>
<p>Podfile.lock 应该加入到版本控制里面，不应该把这个文件加入到 ignores 中。因为 Podfile.lock 会锁定当前各依赖库的版本，之后如果多次执行 <code>pod install</code> 不会更改版本，执行 <code>pod update</code> 时才会更改 Podfile.lock。这样在多人协作的时候，可以防止出现第三方库升级时造成大家各自的第三方库版本不一致。</p>
</blockquote>
<h2 data-id="heading-9">5、Cocoapods原理</h2>
<p>是将所有的依赖库都放到另一个名为Pods的项目中, 然而让主项目依赖Pods项目,这样,源码管理工作任务从主项目移到了Pods项目中：</p>
<ul>
<li>Pods项目最终会编译成一个名为libPods.a的文件, 主项目只要依赖这个.a文件即可.</li>
<li>对于资源文件, CocoaPods提供了一个名为Pods-resources.sh的bash脚步, 该脚本在每次项目, 编译的时候都会执行,将第三方库的各种资源文件复制到目标目录中。</li>
<li>CocoaPods通过一个名为Pods.xcconfig的文件在编译设置所有的依赖和参数。</li>
</ul>
<h2 data-id="heading-10">6、下载原理</h2>
<pre><code class="copyable">s.source = &#123; :git => 'git@gitlab.xxx.net:ios-thirdpartservice/xxxreact.git', :tag => '1.0.0' &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当使用Cocoapods导入私有库时：</p>
<ul>
<li>根据:git => ‘<a href="mailto:git@gitlab.xxx.net">git@gitlab.xxx.net</a>:ios-thirdpartservice/xxxreact.git’找到对应的git仓库</li>
<li>根据:tag => ‘1.0.0’定位到对应tag的提交（如果没有注明Pod依赖库版本则定位到最后一次的提交）</li>
<li>然后在这次提交中检索缀为.podspec的文件（文件可以随便命名）
<ul>
<li>找到podspec文件后先要验证s.name是否与Podfile中的一致：
<ul>
<li>如果不一致则install时会报错：[!]Unable to find a specification for ‘React’.</li>
<li>验证成功后，就会根据Podspec中的s.source_files找到需要导入的代码文件，并通过其他的的数据找到对应的配置文件或资源文件等。</li>
</ul>
</li>
</ul>
</li>
<li>最后将其下载到本地项目中</li>
</ul>
<p>如果是共有库，这些原理也相同：</p>
<ul>
<li>只是共有库要将podspec文件上传到cocoapods</li>
<li>在导入的时候通过名字React去cocoapods匹配对应的podspec</li>
<li>然后根据s.source去找到对应的仓库和对应的版本</li>
<li>然后会再去匹配新的podspec</li>
</ul>
<p>后边的步骤就完全相同了。</p>
<h2 data-id="heading-11">7、集成原理</h2>
<p>当所有的依赖库都下载完后，Cocoapods会将所有的依赖库都放到另一个名为Pods的项目中，然后让主项目依赖Pods项目。</p>
<p>这样，源码管理工作都从主目录移到了Pods项目中。Pods项目最终会编译成为一个名为libPods.a的文件，主项目只要依赖这个.a文件即可。</p>
<p>对于资源文件：</p>
<blockquote>
<p>Cocoapods提供了一个名为Pods-resource.sh的bash脚本，该脚本在每次项目编译的时候都会执行，将Pods依赖库的各种资源文件复制到目标目录中。Cocoapods还通过一个名为Pods.xcconfig的文件来在编译时设置所有的依赖和参数。</p>
</blockquote>
<h2 data-id="heading-12">8、版本控制原理</h2>
<p>当执行完pod install之后，cocoapods会生成一个podfile.lock的文件。该文件最大的用处在于多人开发。</p>
<p>如果你没有在podfile中指定pods版本pod ‘React’，那么默认为获取当前React依赖库的最新版本。</p>
<p>当团队中的某个人执行完pod install命令后，生产的podfile.lock文件就记录下了当时最新pods依赖库的版本，这时团队中的
其他人check下来这份包含podfile.lock文件的工程以后，再去执行pod install命令时，获取下来的pods依赖库的版本和最开始
用户获取到的版本一致。</p>
<p>如果没有podfile.lock文件，后续所有用户执行pod install命令都会获取最新版本的React，这就可能造成一个团队使用的依赖
库版本不一致，这对团队协作来说绝对是个灾难。</p>
<p>在这种情况下，如果团队想使用当前最新版本的React依赖库，有两种方案：</p>
<ul>
<li>更改podfile，使其指向最新版本的React依赖库</li>
<li>执行pod update命令；</li>
</ul>
<p>鉴于podfile.lock文件对团队协作如此重要，所以应该加入到版本控制里面</p>
<h2 data-id="heading-13">9、第三方库使用另一个第三方库的情况</h2>
<p>例如：MJExtension.Framework 和 SDWebImage.Framework，如何在MJExtension的某个类中使用来自SDWebImage库的类？</p>
<ol>
<li>在pod中 找到MJExtension, 在Build Phases 中 导入SDWebImage.Framework；</li>
<li>在pod的MJExtension.Framework 中，找到Build Settings 配置Framework Search Paths 的 Debug 和 Release，添加 PODS_CONFIGURATION_BUILD_DIR/SDWebImage"；</li>
<li>在pod的MJExtension.xcconfig中 添加：FRAMEWORK_SEARCH_PATHS = "PODS_CONFIGURATION_BUILD_DIR/SDWebImage"</li>
</ol>
<h2 data-id="heading-14">10、指定repo镜像</h2>
<pre><code class="copyable">pod repo remove master
pod repo add master https://gitee.com/mirrors/CocoaPods-Specs （gitee镜像）
pod repo update
pod repo remove master
pod repo add master https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git （清华镜像）
pod repo update
source 'https://gitee.com/mirrors/CocoaPods-Specs.git'
source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">11、移除项目中的 CocoaPods</h2>
<ol>
<li>删除工程文件夹下的 Podfile、Podfile.lock 和 Pods 文件夹</li>
<li>删除 .xcworkspace 文件</li>
<li>打开 xcodeproj 文件，删除项目中的 Pods 文件夹以及 Pods.xcconfig 引用和 libpods.a 静态库</li>
<li>打开 Build Phases 选项，删除 Check Pods Manifest.lock、Copy Pods Resources 和 Embeded Pods Frameworks 选项</li>
</ol>
<p>完成以上步骤即可移除项目中的 CocoaPods，项目即可编译运行。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            